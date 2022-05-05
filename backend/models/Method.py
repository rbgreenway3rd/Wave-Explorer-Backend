from django.db import models
from django.contrib.auth.models import User

class Method(models.Model):
    methodid = models.AutoField(db_column='MethodID', primary_key=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bravomethodfile = models.TextField(db_column='BravoMethodFile', db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ownerid = models.IntegerField(db_column='OwnerID', blank=True, null=True)  # Field name made lowercase.
    projectid = models.IntegerField(db_column='ProjectID', blank=True, null=True)  # Field name made lowercase.
    ispublic = models.BooleanField(db_column='IsPublic')  # Field name made lowercase.
    isauto = models.BooleanField(db_column='IsAuto', blank=True, null=True)  # Field name made lowercase.
    imageplatebarcodereset = models.IntegerField(db_column='ImagePlateBarcodeReset', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Method'