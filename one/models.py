from django.db import models


class OneInfo(models.Model):
    """Первая БД запись"""
    name = models.CharField(verbose_name="Первая БД запись", max_length=20, unique=True, db_index=True, db_comment="Первая БД запись")

    class Meta:
        db_table = 'one_info'
        verbose_name = 'Первая БД запись'
        verbose_name_plural = 'Первая БД запись'

    def __str__(self):
        return self.name
