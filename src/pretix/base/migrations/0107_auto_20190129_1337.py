# Generated by Django 2.1.5 on 2019-01-29 13:37

from django.db import migrations, models
import django.db.models.deletion
import jsonfallback.fields
import pretix.base.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0106_auto_20190118_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='datetime',
            field=models.DateTimeField(db_index=True, verbose_name='Date'),
        ),
    ]
