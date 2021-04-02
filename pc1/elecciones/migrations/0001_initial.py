# Generated by Django 3.1.7 on 2021-04-02 01:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_candidato', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info_candidato', models.CharField(max_length=200)),
                ('votos', models.IntegerField(default=0)),
                ('candidato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elecciones.region')),
            ],
        ),
    ]
