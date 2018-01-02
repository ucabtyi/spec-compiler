import logger_factory

logger = logger_factory.get_basic_logger(__name__)


class SpecCompiler:

    def compile(self, f):
        return