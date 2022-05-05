from django.db import models
from django.contrib.auth.models import User 


class Analysis(models.Model):
    analysisid = models.AutoField(db_column='AnalysisID', primary_key=True)  # Field name made lowercase.
    experimentindicatorid = models.ForeignKey('Experimentindicator', models.DO_NOTHING, db_column='ExperimentIndicatorID')  # Field name made lowercase.
    description = models.TextField(db_column='Description', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase.
    runtimeanalysis = models.BooleanField(db_column='RuntimeAnalysis', blank=True, null=True)  # Field name made lowercase.
    controlwellstring = models.TextField(db_column='ControlWellString', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    numfoframes = models.IntegerField(db_column='NumFoFrames', blank=True, null=True)  # Field name made lowercase.
    dynamicrationumeratorid = models.IntegerField(db_column='DynamicRatioNumeratorID', blank=True, null=True)  # Field name made lowercase.
    dynamicratiodenominatorid = models.IntegerField(db_column='DynamicRatioDenominatorID', blank=True, null=True)  # Field name made lowercase.
    maskid = models.IntegerField(db_column='MaskID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Analysis'