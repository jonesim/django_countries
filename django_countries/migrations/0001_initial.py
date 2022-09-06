# Generated by Django 3.2.7 on 2022-07-04 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=600)),
                ('iso_code', models.CharField(blank=True, max_length=9, null=True)),
            ],
            options={
                'verbose_name_plural': 'Countries',
            },
        ),
    ]
