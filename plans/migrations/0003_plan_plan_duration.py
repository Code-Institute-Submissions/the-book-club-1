# Generated by Django 3.1.1 on 2020-09-20 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0002_planduration'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='plan_duration',
            field=models.ForeignKey(default='3', on_delete=django.db.models.deletion.RESTRICT, to='plans.planduration'),
        ),
    ]