from django.db import models
from django.contrib.auth.models import User

class Indicator(models.Model):
    indicatorid = models.AutoField(db_column='IndicatorID', primary_key=True)  # Field name made lowercase.
    methodid = models.ForeignKey('Method', models.DO_NOTHING, db_column='MethodID')  # Field name made lowercase.
    excitationfilterposition = models.IntegerField(db_column='ExcitationFilterPosition')  # Field name made lowercase.
    emissionsfilterposition = models.IntegerField(db_column='EmissionsFilterPosition')  # Field name made lowercase.
    description = models.TextField(db_column='Description', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    signaltype = models.IntegerField(db_column='SignalType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Indicator'