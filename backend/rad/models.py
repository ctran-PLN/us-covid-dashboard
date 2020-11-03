# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AllStatesDaily(models.Model):
    date = models.DateTimeField()
    state = models.CharField(primary_key=True, max_length=200)
    fips = models.IntegerField(blank=True, null=True)
    deaths = models.IntegerField(blank=True, null=True)
    updated = models.BigIntegerField(blank=True, null=True)
    cases = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'all_states_daily'
        unique_together = (('state', 'date'),)

    def get_uniques_as_dict(self):
        return {'date': self.date, 'state': self.state}


class UsaDaily(models.Model):
    date = models.DateTimeField(primary_key=True)
    cases = models.IntegerField(blank=True, null=True)
    deaths = models.IntegerField(blank=True, null=True)
    updated = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'usa_daily'

    def get_uniques_as_dict(self):
        return {'date': self.date}
