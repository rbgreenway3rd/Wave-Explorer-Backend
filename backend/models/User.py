from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    userid = models.AutoField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='Firstname', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    lastname = models.CharField(db_column='Lastname', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    role = models.IntegerField(db_column='Role')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'User'
