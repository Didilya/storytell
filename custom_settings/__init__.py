class ModuleSettings:
    def __init__(
        self,
        name,
        defaults=None,
    ):
        self.name = name
        self.defaults = defaults or []
        if self.defaults:
            for item in self.defaults.items():
                setattr(self, item[0], item[1])
