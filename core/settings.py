import environ
from custom_settings import ModuleSettings

env = environ.Env()

DEFAULTS = {
    "MIN_ENTRY_CHARACTERS": env("MIN_ENTRY_CHARACTERS", default=1),
    "MAX_ENTRY_CHARACTERS": env("MAX_ENTRY_CHARACTERS", default=1000000),
}

core_settings = ModuleSettings("CORE", DEFAULTS)
