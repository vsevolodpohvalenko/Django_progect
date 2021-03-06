# Generated by Django 3.0.7 on 2020-06-12 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50, verbose_name='Authors name')),
                ('comment_text', models.CharField(max_length=200, verbose_name='Comments text')),
            ],
            options={
                'verbose_name': 'Capable Comment',
                'verbose_name_plural': 'Capable Comments',
            },
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Capable Article', 'verbose_name_plural': 'Capable Articles'},
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.AddField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article'),
        ),
    ]
