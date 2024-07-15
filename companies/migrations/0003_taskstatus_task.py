# Generated by Django 4.2.4 on 2024-07-15 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'companies_task_status',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField(null=True)),
                ('due_date', models.DateTimeField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.employee')),
                ('enterprise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.enterprise')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.taskstatus')),
            ],
        ),
    ]
