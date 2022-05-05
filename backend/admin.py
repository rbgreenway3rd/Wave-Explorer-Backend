from django.contrib import admin
 

from backend.models.AnalysisFrame import Analysisframe
from backend.models.Analysis import Analysis
from backend.models.AuthGroup import AuthGroup
from backend.models.AuthGroupPermissions import AuthGroupPermissions
from backend.models.AuthPermission import AuthPermission
from backend.models.AuthUserGroups import AuthUserGroups
from backend.models.AuthUserUserPermissions import AuthUserUserPermissions
from backend.models.AuthtokenToken import AuthtokenToken
from backend.models.AuthUser import AuthUser
from backend.models.CameraSettings import Camerasettings
from backend.models.ColorModel import Colormodel
from backend.models.ColorModelStop import Colormodelstop
from backend.models.CompoundPlate import Compoundplate
from backend.models.Django import DjangoAdminLog, DjangoContentType, DjangoMigrations, DjangoSession
from backend.models.EventMarker import Eventmarker
from backend.models.Experiment import Experiment
from backend.models.ExperimentCompoundPlate import Experimentcompoundplate
from backend.models.ExperimentImage import Experimentimage
from backend.models.ExperimentIndicator import Experimentindicator
from backend.models.Filter import Filter
from backend.models.Indicator import Indicator
from backend.models.Mask import Mask
from backend.models.Method import Method
from backend.models.Plate import Plate
from backend.models.PlateType import Platetype
from backend.models.Project import Project
from backend.models.ReferenceImage import Referenceimage
from backend.models.Sysdiagrams import Sysdiagrams
from backend.models.User import User
from backend.models.UserProject import Userproject
from backend.models.UserProfile import UserProfile


# Register models here.
admin.site.register(Analysis)
admin.site.register(Analysisframe)
admin.site.register(AuthGroup)
admin.site.register(AuthGroupPermissions)
admin.site.register(AuthPermission)
admin.site.register(AuthtokenToken)
admin.site.register(AuthUser)
admin.site.register(AuthUserGroups)
admin.site.register(AuthUserUserPermissions)
admin.site.register(Camerasettings)
admin.site.register(Colormodel)
admin.site.register(Colormodelstop)
admin.site.register(Compoundplate)
admin.site.register(Eventmarker)
admin.site.register(Experiment)
admin.site.register(Experimentcompoundplate)
admin.site.register(Experimentimage)
admin.site.register(Experimentindicator)
admin.site.register(Filter)
admin.site.register(Indicator)
admin.site.register(Mask)
admin.site.register(Method)
admin.site.register(Plate)
admin.site.register(Platetype)
admin.site.register(Project)
admin.site.register(Referenceimage)
admin.site.register(Sysdiagrams)
# admin.site.register(User)
admin.site.register(Userproject)
admin.site.register(DjangoAdminLog)
admin.site.register(DjangoContentType)
admin.site.register(DjangoMigrations)
admin.site.register(DjangoSession)

#code for django admin interface

class UserAdmin(admin.ModelAdmin):
    list_display = ('userid', 'firstname', 'lastname', 'username', 'password', 'role')

admin.site.register(User, UserAdmin)