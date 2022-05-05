from django.db import models
from django.contrib.auth.models import User 

class Eventmarker(models.Model):
    eventmarkerid = models.AutoField(db_column='EventMarkerID', primary_key=True)  # Field name made lowercase.
    experimentid = models.ForeignKey('Experiment', models.DO_NOTHING, db_column='ExperimentID')  # Field name made lowercase.
    sequencenumber = models.IntegerField(db_column='SequenceNumber')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EventMarker'