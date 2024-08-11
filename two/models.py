from django.db import models


class TwoInfo(models.Model):
    """Вторая БД запись"""
    name = models.CharField(verbose_name="Вторая БД запись", max_length=20, unique=True, db_index=True, db_comment="Вторая БД запись")

    class Meta:
        db_table = 'two_info'
        verbose_name = 'Вторая БД запись'
        verbose_name_plural = 'Вторая БД запись'

    def __str__(self):
        return self.name
