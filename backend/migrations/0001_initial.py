# Generated by Django 4.0.4 on 2022-05-05 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('analysisid', models.AutoField(db_column='AnalysisID', primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Description', null=True)),
                ('timestamp', models.DateTimeField(blank=True, db_column='TimeStamp', null=True)),
                ('runtimeanalysis', models.BooleanField(blank=True, db_column='RuntimeAnalysis', null=True)),
                ('controlwellstring', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='ControlWellString', null=True)),
                ('numfoframes', models.IntegerField(blank=True, db_column='NumFoFrames', null=True)),
                ('dynamicrationumeratorid', models.IntegerField(blank=True, db_column='DynamicRatioNumeratorID', null=True)),
                ('dynamicratiodenominatorid', models.IntegerField(blank=True, db_column='DynamicRatioDenominatorID', null=True)),
                ('maskid', models.IntegerField(blank=True, db_column='MaskID', null=True)),
            ],
            options={
                'db_table': 'Analysis',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Analysisframe',
            fields=[
                ('analysisframeid', models.AutoField(db_column='AnalysisFrameID', primary_key=True, serialize=False)),
                ('sequencenumber', models.IntegerField(db_column='SequenceNumber')),
                ('rows', models.IntegerField(db_column='Rows')),
                ('cols', models.IntegerField(db_column='Cols')),
                ('valuestring', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='ValueString', null=True)),
            ],
            options={
                'db_table': 'AnalysisFrame',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=255)),
                ('codename', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthtokenToken',
            fields=[
                ('key', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=40, primary_key=True, serialize=False)),
                ('created', models.DateTimeField()),
            ],
            options={
                'db_table': 'authtoken_token',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=150, unique=True)),
                ('first_name', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=150)),
                ('last_name', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=150)),
                ('email', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Camerasettings',
            fields=[
                ('camerasettingsid', models.AutoField(db_column='CameraSettingsID', primary_key=True, serialize=False)),
                ('vssindex', models.IntegerField(db_column='VSSIndex')),
                ('hssindex', models.IntegerField(db_column='HSSIndex')),
                ('vertclockampindex', models.IntegerField(db_column='VertClockAmpIndex')),
                ('useemamp', models.BooleanField(db_column='UseEMAmp')),
                ('useframetransfer', models.BooleanField(db_column='UseFrameTransfer')),
                ('description', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Description', null=True)),
                ('isdefault', models.BooleanField(db_column='IsDefault')),
                ('startingexposure', models.IntegerField(db_column='StartingExposure')),
                ('exposurelimit', models.IntegerField(db_column='ExposureLimit')),
                ('highpixelthresholdpercent', models.IntegerField(db_column='HighPixelThresholdPercent')),
                ('lowpixelthresholdpercent', models.IntegerField(db_column='LowPixelThresholdPercent')),
                ('minpercentpixelsabovelowthreshold', models.IntegerField(db_column='MinPercentPixelsAboveLowThreshold')),
                ('maxpercentpixelsabovehighthreshold', models.IntegerField(db_column='MaxPercentPixelsAboveHighThreshold')),
                ('increasingsignal', models.BooleanField(db_column='IncreasingSignal')),
                ('startingbinning', models.IntegerField(blank=True, db_column='StartingBinning', null=True)),
                ('emgainlimit', models.IntegerField(blank=True, db_column='EMGainLimit', null=True)),
                ('roix', models.IntegerField(blank=True, db_column='RoiX', null=True)),
                ('roiy', models.IntegerField(blank=True, db_column='RoiY', null=True)),
                ('roiw', models.IntegerField(blank=True, db_column='RoiW', null=True)),
                ('roih', models.IntegerField(blank=True, db_column='RoiH', null=True)),
                ('usecropmode', models.BooleanField(blank=True, db_column='UseCropMode', null=True)),
            ],
            options={
                'db_table': 'CameraSettings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Colormodel',
            fields=[
                ('colormodelid', models.AutoField(db_column='ColorModelID', primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Description', max_length=100, null=True)),
                ('isdefault', models.BooleanField(blank=True, db_column='IsDefault', null=True)),
            ],
            options={
                'db_table': 'ColorModel',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Colormodelstop',
            fields=[
                ('colormodelstopid', models.AutoField(db_column='ColorModelStopID', primary_key=True, serialize=False)),
                ('colorindex', models.IntegerField(db_column='ColorIndex')),
                ('red', models.SmallIntegerField(db_column='Red')),
                ('green', models.SmallIntegerField(db_column='Green')),
                ('blue', models.SmallIntegerField(db_column='Blue')),
            ],
            options={
                'db_table': 'ColorModelStop',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Compoundplate',
            fields=[
                ('compoundplateid', models.AutoField(db_column='CompoundPlateID', primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Description', max_length=200, null=True)),
                ('barcodereset', models.IntegerField(blank=True, db_column='BarcodeReset', null=True)),
            ],
            options={
                'db_table': 'CompoundPlate',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', null=True)),
                ('object_repr', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=100)),
                ('model', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=255)),
                ('name', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Eventmarker',
            fields=[
                ('eventmarkerid', models.AutoField(db_column='EventMarkerID', primary_key=True, serialize=False)),
                ('sequencenumber', models.IntegerField(db_column='SequenceNumber')),
                ('name', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Name', max_length=50, null=True)),
                ('description', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Description', null=True)),
                ('timestamp', models.DateTimeField(blank=True, db_column='TimeStamp', null=True)),
            ],
            options={
                'db_table': 'EventMarker',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('experimentid', models.AutoField(db_column='ExperimentID', primary_key=True, serialize=False)),
                ('methodid', models.IntegerField(db_column='MethodID')),
                ('timestamp', models.DateTimeField(db_column='TimeStamp')),
                ('description', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Description', null=True)),
                ('horzbinning', models.IntegerField(blank=True, db_column='HorzBinning', null=True)),
                ('vertbinning', models.IntegerField(blank=True, db_column='VertBinning', null=True)),
                ('roi_origin_x', models.IntegerField(blank=True, db_column='ROI_Origin_X', null=True)),
                ('roi_origin_y', models.IntegerField(blank=True, db_column='ROI_Origin_Y', null=True)),
                ('roi_width', models.IntegerField(blank=True, db_column='ROI_Width', null=True)),
                ('roi_height', models.IntegerField(blank=True, db_column='ROI_Height', null=True)),
            ],
            options={
                'db_table': 'Experiment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Experimentcompoundplate',
            fields=[
                ('experimentcompoundplateid', models.AutoField(db_column='ExperimentCompoundPlateID', primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Description', null=True)),
                ('barcode', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Barcode', null=True)),
            ],
            options={
                'db_table': 'ExperimentCompoundPlate',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Experimentimage',
            fields=[
                ('experimentimageid', models.AutoField(db_column='ExperimentImageID', primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(db_column='TimeStamp')),
                ('msecs', models.IntegerField(db_column='MSecs')),
                ('maxpixelvalue', models.IntegerField(db_column='MaxPixelValue')),
                ('compressionalgorithm', models.IntegerField(blank=True, db_column='CompressionAlgorithm', null=True)),
                ('filepath', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='FilePath', null=True)),
            ],
            options={
                'db_table': 'ExperimentImage',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Experimentindicator',
            fields=[
                ('experimentindicatorid', models.AutoField(db_column='ExperimentIndicatorID', primary_key=True, serialize=False)),
                ('excitationfilterdesc', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='ExcitationFilterDesc', max_length=50, null=True)),
                ('emissionfilterdesc', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='EmissionFilterDesc', max_length=50, null=True)),
                ('excitationfilterpos', models.IntegerField(blank=True, db_column='ExcitationFilterPos', null=True)),
                ('emissionfilterpos', models.IntegerField(blank=True, db_column='EmissionFilterPos', null=True)),
                ('maskid', models.IntegerField(blank=True, db_column='MaskID', null=True)),
                ('exposure', models.IntegerField(blank=True, db_column='Exposure', null=True)),
                ('gain', models.IntegerField(blank=True, db_column='Gain', null=True)),
                ('preampgain', models.IntegerField(blank=True, db_column='PreAmpGain', null=True)),
                ('description', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Description', max_length=100, null=True)),
                ('signaltype', models.IntegerField(blank=True, db_column='SignalType', null=True)),
                ('flatfieldcorrection', models.IntegerField(blank=True, db_column='FlatFieldCorrection', null=True)),
            ],
            options={
                'db_table': 'ExperimentIndicator',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('filterid', models.AutoField(db_column='FilterID', primary_key=True, serialize=False)),
                ('filterchanger', models.IntegerField(db_column='FilterChanger')),
                ('positionnumber', models.IntegerField(db_column='PositionNumber')),
                ('description', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Description', max_length=80, null=True)),
                ('manufacturer', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Manufacturer', max_length=80, null=True)),
                ('partnumber', models.CharField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='PartNumber', max_length=50, null=True)),
            ],
            options={
                'db_table': 'Filter',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('indicatorid', models.AutoField(db_column='IndicatorID', primary_key=True, serialize=False)),
                ('excitationfilterposition', models.IntegerField(db_column='ExcitationFilterPosition')),
                ('emissionsfilterposition', models.IntegerField(db_column='EmissionsFilterPosition')),
                ('description', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Description', null=True)),
                ('signaltype', models.IntegerField(db_column='SignalType')),
            ],
            options={
                'db_table': 'Indicator',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mask',
            fields=[
                ('maskid', models.AutoField(db_column='MaskID', primary_key=True, serialize=False)),
                ('rows', models.IntegerField(db_column='Rows')),
                ('cols', models.IntegerField(db_column='Cols')),
                ('xoffset', models.IntegerField(db_column='XOffset')),
                ('yoffset', models.IntegerField(db_column='YOffset')),
                ('xsize', models.IntegerField(db_column='XSize')),
                ('ysize', models.IntegerField(db_column='YSize')),
                ('xstep', models.FloatField(db_column='XStep')),
                ('ystep', models.FloatField(db_column='YStep')),
                ('angle', models.FloatField(db_column='Angle')),
                ('shape', models.IntegerField(db_column='Shape')),
                ('description', models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Description')),
                ('referenceimageid', models.IntegerField(blank=True, db_column='ReferenceImageID', null=True)),
                ('isdefault', models.BooleanField(blank=True, db_column='IsDefault', null=True)),
                ('barrelstrength', models.FloatField(blank=True, db_column='BarrelStrength', null=True)),
                ('barrelzoom', models.FloatField(blank=True, db_column='BarrelZoom', null=True)),
            ],
            options={
                'db_table': 'Mask',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Method',
            fields=[
                ('methodid', models.AutoField(db_column='MethodID', primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Description', null=True)),
                ('bravomethodfile', models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='BravoMethodFile')),
                ('ownerid', models.IntegerField(blank=True, db_column='OwnerID', null=True)),
                ('projectid', models.IntegerField(blank=True, db_column='ProjectID', null=True)),
                ('ispublic', models.BooleanField(db_column='IsPublic')),
                ('isauto', models.BooleanField(blank=True, db_column='IsAuto', null=True)),
                ('imageplatebarcodereset', models.IntegerField(blank=True, db_column='ImagePlateBarcodeReset', null=True)),
            ],
            options={
                'db_table': 'Method',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Plate',
            fields=[
                ('plateid', models.AutoField(db_column='PlateID', primary_key=True, serialize=False)),
                ('ownerid', models.IntegerField(blank=True, db_column='OwnerID', null=True)),
                ('barcode', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Barcode', null=True)),
                ('platetypeid', models.IntegerField(blank=True, db_column='PlateTypeID', null=True)),
                ('description', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Description', null=True)),
                ('ispublic', models.BooleanField(db_column='IsPublic')),
            ],
            options={
                'db_table': 'Plate',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Platetype',
            fields=[
                ('platetypeid', models.AutoField(db_column='PlateTypeID', primary_key=True, serialize=False)),
                ('description', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Description', max_length=80)),
                ('rows', models.IntegerField(db_column='Rows')),
                ('cols', models.IntegerField(db_column='Cols')),
                ('isdefault', models.BooleanField(db_column='IsDefault')),
            ],
            options={
                'db_table': 'PlateType',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('projectid', models.AutoField(db_column='ProjectID', primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Description', null=True)),
                ('archived', models.BooleanField(blank=True, db_column='Archived', null=True)),
                ('timestamp', models.DateTimeField(blank=True, db_column='TimeStamp', null=True)),
            ],
            options={
                'db_table': 'Project',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Referenceimage',
            fields=[
                ('referenceimageid', models.AutoField(db_column='ReferenceImageID', primary_key=True, serialize=False)),
                ('width', models.IntegerField(db_column='Width')),
                ('height', models.IntegerField(db_column='Height')),
                ('depth', models.IntegerField(db_column='Depth')),
                ('imagedata', models.BinaryField(db_column='ImageData', max_length='max')),
                ('timestamp', models.DateTimeField(db_column='TimeStamp')),
                ('numbytes', models.IntegerField(db_column='NumBytes')),
                ('maxpixelvalue', models.IntegerField(db_column='MaxPixelValue')),
                ('compressionalgorithm', models.IntegerField(db_column='CompressionAlgorithm')),
                ('description', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Description', max_length=200)),
                ('type', models.IntegerField(blank=True, db_column='Type', null=True)),
            ],
            options={
                'db_table': 'ReferenceImage',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sysdiagrams',
            fields=[
                ('name', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', max_length=128)),
                ('principal_id', models.IntegerField()),
                ('diagram_id', models.AutoField(primary_key=True, serialize=False)),
                ('version', models.IntegerField(blank=True, null=True)),
                ('definition', models.BinaryField(blank=True, max_length='max', null=True)),
            ],
            options={
                'db_table': 'sysdiagrams',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.AutoField(db_column='UserID', primary_key=True, serialize=False)),
                ('firstname', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Firstname', max_length=50)),
                ('lastname', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Lastname', max_length=50)),
                ('username', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Username', max_length=50)),
                ('password', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='Password', max_length=50)),
                ('role', models.IntegerField(db_column='Role')),
            ],
            options={
                'db_table': 'User',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Userproject',
            fields=[
                ('userid', models.OneToOneField(db_column='UserID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='backend.user')),
            ],
            options={
                'db_table': 'UserProject',
                'managed': False,
            },
        ),
    ]
