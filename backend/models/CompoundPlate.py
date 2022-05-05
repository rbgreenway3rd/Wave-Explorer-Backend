from django.db import models
from django.contrib.auth.models import User 

class Compoundplate(models.Model):
    compoundplateid = models.AutoField(db_column='CompoundPlateID', primary_key=True)  # Field name made lowercase.
    methodid = models.ForeignKey('Method', models.DO_NOTHING, db_column='MethodID')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    barcodereset = models.IntegerField(db_column='BarcodeReset', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CompoundPlate'