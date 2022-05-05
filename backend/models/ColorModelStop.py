from django.db import models
from django.contrib.auth.models import User 
from backend.models.ColorModel import Colormodel

class Colormodelstop(models.Model):
    colormodelstopid = models.AutoField(db_column='ColorModelStopID', primary_key=True)  # Field name made lowercase.
    colormodelid = models.ForeignKey(Colormodel, models.DO_NOTHING, db_column='ColorModelID')  # Field name made lowercase.
    colorindex = models.IntegerField(db_column='ColorIndex')  # Field name made lowercase.
    red = models.SmallIntegerField(db_column='Red')  # Field name made lowercase.
    green = models.SmallIntegerField(db_column='Green')  # Field name made lowercase.
    blue = models.SmallIntegerField(db_column='Blue')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ColorModelStop'