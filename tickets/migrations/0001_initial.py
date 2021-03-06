# Generated by Django 2.0 on 2018-03-16 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('date', models.DateField(blank=True, null=True, verbose_name='holiday date')),
            ],
            options={
                'verbose_name': 'Holiday',
                'verbose_name_plural': 'Holidays',
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, verbose_name='service subcategory')),
                ('sla', models.IntegerField(blank=True, help_text='sla in hours', null=True, verbose_name='sla')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'service subcategory',
                'verbose_name_plural': 'service subcategories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ServiceOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('expiry_date', models.DateTimeField(blank=True, null=True, verbose_name='expiry date')),
                ('status', models.CharField(choices=[('in_progress', 'In progress'), ('resolved', 'Resolved'), ('done', 'Done'), ('cancelled', 'Cancelled')], default='in_progress', max_length=50)),
                ('description', models.TextField(verbose_name='description')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tickets.ServiceCategory')),
            ],
            options={
                'verbose_name': 'service order',
                'verbose_name_plural': 'service orders',
            },
        ),
        migrations.CreateModel(
            name='WorkHourSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_hour', models.IntegerField(default=9, help_text='i.e.: "9" for 9am', verbose_name='Work start time')),
                ('end_hour', models.IntegerField(default=18, help_text='i.e.: "18" for 6pm', verbose_name='Work end time')),
            ],
            options={
                'verbose_name': 'Working hours settings',
            },
        ),
    ]
