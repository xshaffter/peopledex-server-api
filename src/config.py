from common.fastapi.core.parameters.managers import Environ
from common.fastapi.core.parameters.parameter_manager import ParameterManager


class Config(ParameterManager):
    is_simulation: bool = Environ(False)
    ACCESS_KEY_ID: str = Environ(...)
    SECRET_ACCESS_KEY: str = Environ(...)