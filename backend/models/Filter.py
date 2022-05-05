from django.db import models
from django.contrib.auth.models import User

class Filter(models.Model):
    filterid = models.AutoField(db_column='FilterID', primary_key=True)  # Field name made lowercase.
    filterchanger = models.IntegerField(db_column='FilterChanger')  # Field name made lowercase.
    positionnumber = models.IntegerField(db_column='PositionNumber')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    partnumber = models.CharField(db_column='PartNumber', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Filter'