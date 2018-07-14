# Generated by Django 2.0.2 on 2018-02-03 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('node', '0001_initial'),
        ('docker', '0001_initial'),
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(db_index=True, max_length=120)),
                ('type', models.SmallIntegerField(choices=[(1, 'GAUGE'), (2, 'COUNTER'), (3, 'DERIVE'), (4, 'ABSOLUTE')])),
                ('unit', models.SmallIntegerField(choices=[(1, '%'), (10, 'KB'), (11, 'MB'), (20, 'req'), (21, 'req/s'), (30, 'Hour'), (31, 'Day')])),
                ('sort', models.IntegerField(db_index=True, default=0)),
                ('docker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='docker.Docker')),
                ('node', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='node.Node')),
                ('server', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='server.Server')),
            ],
            options={
                'ordering': ['sort'],
            },
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max', models.FloatField()),
                ('value', models.FloatField()),
                ('min', models.FloatField()),
                ('date', models.DateField(db_index=True)),
                ('chart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chart.Chart')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Hour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max', models.FloatField()),
                ('value', models.FloatField()),
                ('min', models.FloatField()),
                ('date', models.DateField(db_index=True)),
                ('hour', models.SmallIntegerField(db_index=True)),
                ('chart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chart.Chart')),
            ],
            options={
                'ordering': ['date', 'hour'],
            },
        ),
        migrations.CreateModel(
            name='Raw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('timestamp', models.DateTimeField(db_index=True)),
                ('chart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chart.Chart')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]