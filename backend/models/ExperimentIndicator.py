from django.db import models
from django.contrib.auth.models import User 
from backend.models.Experiment import Experiment

class Experimentindicator(models.Model):
    experimentindicatorid = models.AutoField(db_column='ExperimentIndicatorID', primary_key=True)  # Field name made lowercase.
    experimentid = models.ForeignKey(Experiment, models.DO_NOTHING, db_column='ExperimentID', blank=True, null=True)  # Field name made lowercase.
    excitationfilterdesc = models.CharField(db_column='ExcitationFilterDesc', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    emissionfilterdesc = models.CharField(db_column='EmissionFilterDesc', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    excitationfilterpos = models.IntegerField(db_column='ExcitationFilterPos', blank=True, null=True)  # Field name made lowercase.
    emissionfilterpos = models.IntegerField(db_column='EmissionFilterPos', blank=True, null=True)  # Field name made lowercase.
    maskid = models.IntegerField(db_column='MaskID', blank=True, null=True)  # Field name made lowercase.
    exposure = models.IntegerField(db_column='Exposure', blank=True, null=True)  # Field name made lowercase.
    gain = models.IntegerField(db_column='Gain', blank=True, null=True)  # Field name made lowercase.
    preampgain = models.IntegerField(db_column='PreAmpGain', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    signaltype = models.IntegerField(db_column='SignalType', blank=True, null=True)  # Field name made lowercase.
    flatfieldcorrection = models.IntegerField(db_column='FlatFieldCorrection', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ExperimentIndicator'