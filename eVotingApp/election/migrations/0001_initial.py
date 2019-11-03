# Generated by Django 2.2.5 on 2019-11-01 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_surname', models.CharField(default='', max_length=50)),
                ('candidate_givenname', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ElectionDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('election_date', models.DateField(help_text='Please use the following format: YYYY-MM-DD')),
                ('start_time', models.TimeField(blank=True)),
                ('end_time', models.TimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_name', models.CharField(default='', max_length=50)),
                ('party_logo', models.ImageField(default='/media/UAP.jpg', upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='PartyPreference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_preference', models.IntegerField(default='')),
                ('party', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='election.Party')),
            ],
        ),
        migrations.CreateModel(
            name='CandidatePreference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_preference', models.IntegerField(default='')),
                ('candidate', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='election.Candidate')),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='party',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='election.Party'),
        ),
    ]
