import uuid
from django.db.models import UUIDField


class UidField(UUIDField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("db_index", True)
        kwargs.setdefault("unique", True)
        kwargs.setdefault("editable", False)
        kwargs.setdefault("default", uuid.uuid4)
        super().__init__(*args, **kwargs)
