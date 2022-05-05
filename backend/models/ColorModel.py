from django.db import models
from django.contrib.auth.models import User 

class Colormodel(models.Model):
    colormodelid = models.AutoField(db_column='ColorModelID', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    isdefault = models.BooleanField(db_column='IsDefault', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ColorModel'