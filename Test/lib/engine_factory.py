from engine import Engine

class EngineFactory(object):
    @classmethod
    def create_engine(cls, engine_type):
        return Engine(engine_type)