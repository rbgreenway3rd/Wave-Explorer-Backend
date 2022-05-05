from django.db import models
from backend.models.Analysis import Analysis
from django.contrib.auth.models import User 

class Analysisframe(models.Model):
    analysisframeid = models.AutoField(db_column='AnalysisFrameID', primary_key=True)  # Field name made lowercase.
    analysisid = models.ForeignKey(Analysis, models.DO_NOTHING, db_column='AnalysisID')  # Field name made lowercase.
    sequencenumber = models.IntegerField(db_column='SequenceNumber')  # Field name made lowercase.
    rows = models.IntegerField(db_column='Rows')  # Field name made lowercase.
    cols = models.IntegerField(db_column='Cols')  # Field name made lowercase.
    valuestring = models.TextField(db_column='ValueString', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AnalysisFrame'
        unique_together = (('analysisid', 'sequencenumber'),)