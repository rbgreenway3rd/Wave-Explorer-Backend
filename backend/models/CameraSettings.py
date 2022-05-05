from django.db import models
from django.contrib.auth.models import User 

class Camerasettings(models.Model):
    camerasettingsid = models.AutoField(db_column='CameraSettingsID', primary_key=True)  # Field name made lowercase.
    vssindex = models.IntegerField(db_column='VSSIndex')  # Field name made lowercase.
    hssindex = models.IntegerField(db_column='HSSIndex')  # Field name made lowercase.
    vertclockampindex = models.IntegerField(db_column='VertClockAmpIndex')  # Field name made lowercase.
    useemamp = models.BooleanField(db_column='UseEMAmp')  # Field name made lowercase.
    useframetransfer = models.BooleanField(db_column='UseFrameTransfer')  # Field name made lowercase.
    description = models.TextField(db_column='Description', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    isdefault = models.BooleanField(db_column='IsDefault')  # Field name made lowercase.
    startingexposure = models.IntegerField(db_column='StartingExposure')  # Field name made lowercase.
    exposurelimit = models.IntegerField(db_column='ExposureLimit')  # Field name made lowercase.
    highpixelthresholdpercent = models.IntegerField(db_column='HighPixelThresholdPercent')  # Field name made lowercase.
    lowpixelthresholdpercent = models.IntegerField(db_column='LowPixelThresholdPercent')  # Field name made lowercase.
    minpercentpixelsabovelowthreshold = models.IntegerField(db_column='MinPercentPixelsAboveLowThreshold')  # Field name made lowercase.
    maxpercentpixelsabovehighthreshold = models.IntegerField(db_column='MaxPercentPixelsAboveHighThreshold')  # Field name made lowercase.
    increasingsignal = models.BooleanField(db_column='IncreasingSignal')  # Field name made lowercase.
    startingbinning = models.IntegerField(db_column='StartingBinning', blank=True, null=True)  # Field name made lowercase.
    emgainlimit = models.IntegerField(db_column='EMGainLimit', blank=True, null=True)  # Field name made lowercase.
    roix = models.IntegerField(db_column='RoiX', blank=True, null=True)  # Field name made lowercase.
    roiy = models.IntegerField(db_column='RoiY', blank=True, null=True)  # Field name made lowercase.
    roiw = models.IntegerField(db_column='RoiW', blank=True, null=True)  # Field name made lowercase.
    roih = models.IntegerField(db_column='RoiH', blank=True, null=True)  # Field name made lowercase.
    usecropmode = models.BooleanField(db_column='UseCropMode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CameraSettings'