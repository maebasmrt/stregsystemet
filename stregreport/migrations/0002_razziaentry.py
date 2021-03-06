# Generated by Django 2.2.5 on 2019-10-28 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stregsystem', '0009_auto_20191028_2057'),
        ('stregreport', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RazziaEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, null=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stregsystem.Member')),
                ('razzia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stregreport.BreadRazzia')),
            ],
        ),
    ]
