from django.db import models
from django.contrib.auth.models import User 

class Experiment(models.Model):
    experimentid = models.AutoField(db_column='ExperimentID', primary_key=True)  # Field name made lowercase.
    plateid = models.ForeignKey('Plate', models.DO_NOTHING, db_column='PlateID')  # Field name made lowercase.
    methodid = models.IntegerField(db_column='MethodID')  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='TimeStamp')  # Field name made lowercase.
    description = models.TextField(db_column='Description', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    horzbinning = models.IntegerField(db_column='HorzBinning', blank=True, null=True)  # Field name made lowercase.
    vertbinning = models.IntegerField(db_column='VertBinning', blank=True, null=True)  # Field name made lowercase.
    roi_origin_x = models.IntegerField(db_column='ROI_Origin_X', blank=True, null=True)  # Field name made lowercase.
    roi_origin_y = models.IntegerField(db_column='ROI_Origin_Y', blank=True, null=True)  # Field name made lowercase.
    roi_width = models.IntegerField(db_column='ROI_Width', blank=True, null=True)  # Field name made lowercase.
    roi_height = models.IntegerField(db_column='ROI_Height', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Experiment'