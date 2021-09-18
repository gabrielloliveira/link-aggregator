import uuid as uuid_lib

from django.db import models


class DefaultBaseModel(models.Model):
    created_at = models.DateTimeField("criado em", auto_now_add=True)
    updated_at = models.DateTimeField("atualizado em", auto_now=True)
    uuid = models.UUIDField(
        "UUID", unique=True, editable=False, default=uuid_lib.uuid4, db_index=True
    )

    class Meta:
        abstract = True


class Link(DefaultBaseModel):
    url = models.URLField("URL", unique=True)
    description = models.TextField("descrição", blank=True, null=True)

    def __str__(self) -> str:
        return self.url
