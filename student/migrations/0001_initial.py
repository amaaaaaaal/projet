# Generated by Django 5.0.4 on 2024-04-14 21:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=200)),
                ('type', models.IntegerField(choices=[(0, 'Offre'), (1, 'Demande')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Logement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localisation', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('contactInfo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeStg', models.IntegerField(choices=[(1, 'Ouvrier'), (2, 'Technicien'), (3, 'PFE')])),
                ('societe', models.CharField(max_length=200)),
                ('duree', models.IntegerField()),
                ('sujet', models.CharField(max_length=200)),
                ('contactInfo', models.CharField(max_length=200)),
                ('specialite', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depart', models.CharField(max_length=255)),
                ('destination', models.CharField(max_length=200)),
                ('heuredep', models.TimeField()),
                ('nbresieges', models.IntegerField()),
                ('contactInfo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=8)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Evenement',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='student.post')),
                ('intiule', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('lieu', models.CharField(max_length=200)),
                ('contactInfo', models.CharField(max_length=200)),
            ],
            bases=('student.post',),
        ),
        migrations.CreateModel(
            name='Recommandation',
            fields=[
                ('post_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='student.post')),
                ('text', models.CharField(max_length=200)),
            ],
            bases=('student.post',),
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('like', models.BooleanField()),
                ('pt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.post')),
                ('rd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.user')),
            ],
        ),
        migrations.CreateModel(
            name='EvenClub',
            fields=[
                ('evenement_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='student.evenement')),
                ('club', models.CharField(max_length=200)),
            ],
            bases=('student.evenement',),
        ),
        migrations.CreateModel(
            name='EvenSocial',
            fields=[
                ('evenement_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='student.evenement')),
                ('prix', models.DecimalField(decimal_places=3, max_digits=15)),
            ],
            bases=('student.evenement',),
        ),
    ]
