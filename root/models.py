from django.utils import timezone
from django.db import models

from .managers import SoftDeleteManager, ByPassSoftDeleteManager
from .utils import related_objects


class SoftDeleteModel(models.Model):
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        for related in related_objects(self):
            related.deleted_at = timezone.now()
            related.save()
        self.deleted_at = timezone.now()
        self.save()

    objects = SoftDeleteManager()
    all_objects = ByPassSoftDeleteManager()