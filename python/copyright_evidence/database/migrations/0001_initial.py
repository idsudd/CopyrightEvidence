# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-14 22:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('label', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('label', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_description', models.CharField(help_text='Description of the data.', max_length=511)),
                ('sample_size', models.IntegerField(help_text='Sample size of the dataset.')),
                ('start_material_year', models.IntegerField(help_text='The year when the data collection began.')),
                ('end_material_year', models.IntegerField(help_text='The year when the data collection ended.')),
            ],
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('code', models.CharField(max_length=63, primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=511)),
            ],
        ),
        migrations.CreateModel(
            name='EvidenceBasedPolicy',
            fields=[
                ('code', models.CharField(max_length=1, primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=511)),
                ('description', models.CharField(max_length=511)),
            ],
        ),
        migrations.CreateModel(
            name='FundamentalIssue',
            fields=[
                ('code', models.CharField(max_length=1, primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=511)),
                ('description', models.CharField(max_length=511)),
            ],
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('label', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Method',
            fields=[
                ('label', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('qualitative', models.BooleanField(default=False, help_text='Whether the method is qualitative.')),
            ],
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('code', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=255)),
                ('url', models.CharField(help_text='URL to the corresponding Wiki page.', max_length=511)),
                ('year', models.IntegerField(help_text='Year of publication.')),
                ('title', models.CharField(help_text='Title of the study.', max_length=511)),
                ('abstract', models.TextField(help_text='Abstract of the study.', null=True)),
                ('plain_text_proposition', models.TextField(help_text='Main results of the study.', null=True)),
                ('intervention_response', models.TextField(help_text='Policy implications as stated by author.', null=True)),
                ('link', models.CharField(help_text='URL to the PDF of the study.', max_length=511, null=True)),
                ('authentic_link', models.CharField(help_text='URL to the original version of the study.', max_length=511, null=True)),
                ('comparative', models.BooleanField(default=False, help_text='Whether the study is comparative.')),
                ('literature_review', models.BooleanField(default=False, help_text='Whether the study contains a literature review.')),
                ('government_or_policy', models.BooleanField(help_text='Whether the study is a governament or policy study.')),
                ('analysis_methods', models.ManyToManyField(help_text='Analysis method(s) of the study.', related_name='anaysis_method_set', to='database.Method')),
                ('authors', models.ManyToManyField(to='database.Author')),
                ('collection_methods', models.ManyToManyField(help_text='Collection method(s) of the study.', related_name='collection_methods_set', to='database.Method')),
                ('countries', models.ManyToManyField(help_text='Countries mentioned in the study.', to='database.Country')),
                ('data_sources', models.ManyToManyField(help_text='Other studies used as data sources.', related_name='data_source_study_set', to='database.Study')),
                ('disciplines', models.ManyToManyField(help_text='Discipline(s) of the study.', to='database.Discipline')),
                ('evidence_based_policies', models.ManyToManyField(help_text='Evidence based policies covered in the study.', to='database.EvidenceBasedPolicy')),
                ('fundamental_issues', models.ManyToManyField(help_text='Fundamental issue(s) covered in the study.', to='database.FundamentalIssue')),
                ('industries', models.ManyToManyField(help_text='Industry(ies) involved in the study.', to='database.Industry')),
                ('methods', models.ManyToManyField(help_text='Method(s) of the study.', related_name='method_set', to='database.Method')),
                ('references', models.ManyToManyField(help_text='Other works referenced in the study.', related_name='referencing_study_set', to='database.Study')),
            ],
        ),
        migrations.AddField(
            model_name='dataset',
            name='study',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Study'),
        ),
    ]