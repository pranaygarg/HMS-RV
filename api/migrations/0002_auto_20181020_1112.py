# Generated by Django 2.1.2 on 2018-10-20 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostelite',
            name='usn',
            field=models.ForeignKey(db_column='USN', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, related_name='hostelite', serialize=False, to='api.Student'),
        ),
    ]
