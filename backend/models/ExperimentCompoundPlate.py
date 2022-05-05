from django.db import models
from django.contrib.auth.models import User 
from backend.models.Experiment import Experiment

class Experimentcompoundplate(models.Model):
    experimentcompoundplateid = models.AutoField(db_column='ExperimentCompoundPlateID', primary_key=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    barcode = models.TextField(db_column='Barcode', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    experimentid = models.ForeignKey(Experiment, models.DO_NOTHING, db_column='ExperimentID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ExperimentCompoundPlate'