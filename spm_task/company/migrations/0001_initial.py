# Generated by Django 4.2.11 on 2024-05-02 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(choices=[('SMALL BUSINESS', 'Small Business'), ('STARTUP', 'Startup'), ('CORPORATE', 'Corporate')], default='SMALL BUSINESS', max_length=20)),
                ('name', models.CharField(max_length=255)),
                ('approval', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.approval')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Startup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('funding_rounds', models.SmallIntegerField(null=True)),
                ('founders', models.CharField(blank=True, max_length=255, null=True)),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='startup', to='company.company')),
            ],
        ),
        migrations.CreateModel(
            name='SmallBusiness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_employess', models.SmallIntegerField(null=True)),
                ('industry', models.CharField(blank=True, max_length=50, null=True)),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='small_business', to='company.company')),
            ],
        ),
        migrations.CreateModel(
            name='Corporate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='corporate', to='company.company')),
            ],
        ),
    ]
