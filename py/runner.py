import sys
import glob
import logger_factory
import traceback
import my_compiler
import os
from optparse import OptionParser

logger = logger_factory.get_basic_logger(__name__)


class Script:
    def __init__(self, compilers):
        pass

class ScriptContext:
    def __init__(self):
        pass


def compile_specs(spec, glbs):
    with open(spec) as spec_f:
        compiler = my_compiler.SpecCompiler()
        script_name = os.path.basename(spec).replace(".py", "")

        def custom_script(name=script_name):
            return

        tree = compiler.compile(spec_f)
        exec tree in glbs, locals()


def main(spec_dir):
    for pathfile in glob.glob("%s/*.py" % spec_dir):
        try:
            compile_specs(pathfile, globals())
        except:
            logger.error("Failed to compiler %s" % pathfile)
            traceback.print_exc()


if __name__ == "__main__":

    parser = OptionParser("Usage: %prog")
    parser.add_option("-d", "--dir", type=str, dest="spec_dir", default="spec")

    (options, args) = parser.parse_args()

    spec_dir = options.spec_dir
    main(spec_dir)