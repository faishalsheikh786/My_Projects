# Generated by Django 5.0 on 2023-12-30 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_student_sem1_sgpa_alter_student_sem2_sgpa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='sem1_sgpa',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='sem2_sgpa',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='sem3_sgpa',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='sem4_sgpa',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='sem5_sgpa',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='sem6_sgpa',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='sem7_sgpa',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='sem8_sgpa',
            field=models.FloatField(null=True),
        ),
    ]
