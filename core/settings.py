import environ
from utils.custom_settings import ModuleSettings

env = environ.Env()

DEFAULTS = {
    "MIN_ENTRY_CHARACTERS": env("MIN_ENTRY_CHARACTERS", default=1),
    "MAX_ENTRY_CHARACTERS": env("MAX_ENTRY_CHARACTERS", default=1000000),
    "MIN_TOPIC_CHARACTERS": env("MAX_ENTRY_CHARACTERS", default=3),
    "MAX_TOPIC_CHARACTERS": env("MAX_ENTRY_CHARACTERS", default=255),
    "PAGINATION_NUMBER": env("PAGINATION_NUMBER", default=50),
    "LLM_NODEL_API_KEY": env("LLM_NODEL_API_KEY", default=""),
}

core_settings = ModuleSettings("core_settings", DEFAULTS)
