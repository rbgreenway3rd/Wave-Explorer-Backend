from django.db import models
from django.contrib.auth.models import User

class Mask(models.Model):
    maskid = models.AutoField(db_column='MaskID', primary_key=True)  # Field name made lowercase.
    rows = models.IntegerField(db_column='Rows')  # Field name made lowercase.
    cols = models.IntegerField(db_column='Cols')  # Field name made lowercase.
    xoffset = models.IntegerField(db_column='XOffset')  # Field name made lowercase.
    yoffset = models.IntegerField(db_column='YOffset')  # Field name made lowercase.
    xsize = models.IntegerField(db_column='XSize')  # Field name made lowercase.
    ysize = models.IntegerField(db_column='YSize')  # Field name made lowercase.
    xstep = models.FloatField(db_column='XStep')  # Field name made lowercase.
    ystep = models.FloatField(db_column='YStep')  # Field name made lowercase.
    angle = models.FloatField(db_column='Angle')  # Field name made lowercase.
    shape = models.IntegerField(db_column='Shape')  # Field name made lowercase.
    description = models.TextField(db_column='Description', db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    platetypeid = models.ForeignKey('Platetype', models.DO_NOTHING, db_column='PlateTypeID')  # Field name made lowercase.
    referenceimageid = models.IntegerField(db_column='ReferenceImageID', blank=True, null=True)  # Field name made lowercase.
    isdefault = models.BooleanField(db_column='IsDefault', blank=True, null=True)  # Field name made lowercase.
    barrelstrength = models.FloatField(db_column='BarrelStrength', blank=True, null=True)  # Field name made lowercase.
    barrelzoom = models.FloatField(db_column='BarrelZoom', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Mask'