from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    projectid = models.AutoField(db_column='ProjectID', primary_key=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    archived = models.BooleanField(db_column='Archived', blank=True, null=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Project'