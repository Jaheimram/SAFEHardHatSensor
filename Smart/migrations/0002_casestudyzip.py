# Generated by Django 5.1.7 on 2025-04-03 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Smart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseStudyZip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('zip_file', models.FileField(upload_to='case_studies/zips/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
