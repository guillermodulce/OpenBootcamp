# Generated by Django 4.1.1 on 2022-10-21 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('country_code', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.country')),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('extra_dec', models.BooleanField(default=False)),
                ('extra_jun', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=5)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.location')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15)),
                ('description', models.TextField(null=True)),
                ('salary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.salary')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.job')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.place')),
            ],
        ),
    ]
