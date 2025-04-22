from django.db import migrations
from django.contrib.auth.models import User

def create_superuser(apps, schema_editor):
    User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')

class Migration(migrations.Migration):

    dependencies = [
        # You should replace '0001_initial' with your actual latest migration file
        ('Smart', '0002_casestudyzip'),
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
