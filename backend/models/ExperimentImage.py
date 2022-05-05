from django.db import models
from django.contrib.auth.models import User 

class Experimentimage(models.Model):
    experimentimageid = models.AutoField(db_column='ExperimentImageID', primary_key=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='TimeStamp')  # Field name made lowercase.
    experimentindicatorid = models.ForeignKey('Experimentindicator', models.DO_NOTHING, db_column='ExperimentIndicatorID')  # Field name made lowercase.
    msecs = models.IntegerField(db_column='MSecs')  # Field name made lowercase.
    maxpixelvalue = models.IntegerField(db_column='MaxPixelValue')  # Field name made lowercase.
    compressionalgorithm = models.IntegerField(db_column='CompressionAlgorithm', blank=True, null=True)  # Field name made lowercase.
    filepath = models.TextField(db_column='FilePath', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ExperimentImage'