from django.db import models
from django.contrib.auth.models import User

class Plate(models.Model):
    plateid = models.AutoField(db_column='PlateID', primary_key=True)  # Field name made lowercase.
    projectid = models.ForeignKey('Project', models.DO_NOTHING, db_column='ProjectID')  # Field name made lowercase.
    ownerid = models.IntegerField(db_column='OwnerID', blank=True, null=True)  # Field name made lowercase.
    barcode = models.TextField(db_column='Barcode', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    platetypeid = models.IntegerField(db_column='PlateTypeID', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ispublic = models.BooleanField(db_column='IsPublic')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Plate'