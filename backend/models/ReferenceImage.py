from django.db import models
from django.contrib.auth.models import User

class Referenceimage(models.Model):
    referenceimageid = models.AutoField(db_column='ReferenceImageID', primary_key=True)  # Field name made lowercase.
    width = models.IntegerField(db_column='Width')  # Field name made lowercase.
    height = models.IntegerField(db_column='Height')  # Field name made lowercase.
    depth = models.IntegerField(db_column='Depth')  # Field name made lowercase.
    imagedata = models.BinaryField(db_column='ImageData')  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='TimeStamp')  # Field name made lowercase.
    numbytes = models.IntegerField(db_column='NumBytes')  # Field name made lowercase.
    maxpixelvalue = models.IntegerField(db_column='MaxPixelValue')  # Field name made lowercase.
    compressionalgorithm = models.IntegerField(db_column='CompressionAlgorithm')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReferenceImage'