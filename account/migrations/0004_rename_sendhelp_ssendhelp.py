# Generated by Django 4.1.5 on 2023-08-02 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0003_remove_sendhelp_author_remove_sendhelp_status"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="SendHelp",
            new_name="SSendHelp",
        ),
    ]
