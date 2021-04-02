from django.db import models


class SoftDeleteManager(models.Manager):

    def get_queryset(self):
        return super(SoftDeleteManager, self).get_queryset().filter(deleted_at=None)

    def all_with_deleted(self):
        return super(SoftDeleteManager, self).get_queryset()


class ByPassSoftDeleteManager(models.Manager):

    def get_queryset(self):
        return super(ByPassSoftDeleteManager, self).get_queryset()