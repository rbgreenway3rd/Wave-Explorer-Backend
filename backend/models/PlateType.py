from django.db import models
from django.contrib.auth.models import User

class Platetype(models.Model):
    platetypeid = models.AutoField(db_column='PlateTypeID', primary_key=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    rows = models.IntegerField(db_column='Rows')  # Field name made lowercase.
    cols = models.IntegerField(db_column='Cols')  # Field name made lowercase.
    isdefault = models.BooleanField(db_column='IsDefault')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PlateType'