from django.db import models
from backend.models.User import User
from backend.models.Project import Project

class Userproject(models.Model):
    userid = models.OneToOneField(User, models.DO_NOTHING, db_column='UserID', primary_key=True)  # Field name made lowercase.
    projectid = models.ForeignKey(Project, models.DO_NOTHING, db_column='ProjectID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserProject'
        unique_together = (('userid', 'projectid'),)