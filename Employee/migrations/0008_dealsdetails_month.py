# Generated by Django 4.1.4 on 2023-01-09 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0007_alter_adddoctor_enterd_by_alter_addproduct_enterd_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='dealsdetails',
            name='month',
            field=models.DateField(auto_now=True),
        ),
    ]
