# Generated by Django 2.0.2 on 2018-03-07 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('razaoSocial', models.CharField(max_length=60)),
                ('nomeFantasia', models.CharField(max_length=60)),
                ('tipo', models.CharField(choices=[('F', 'Pessoa Física'), ('J', 'Pessoa Jurídica')], default='F', max_length=1)),
                ('cnpjcpf', models.CharField(blank=True, max_length=14, null=True)),
                ('inscricao', models.CharField(blank=True, max_length=9, null=True)),
                ('regiao', models.CharField(blank=True, max_length=14, null=True)),
                ('grupo', models.CharField(blank=True, max_length=14, null=True)),
                ('endereco', models.CharField(blank=True, max_length=60, null=True)),
                ('complemento', models.CharField(blank=True, max_length=60, null=True)),
                ('bairro', models.CharField(blank=True, max_length=60, null=True)),
                ('cidade', models.CharField(blank=True, max_length=60, null=True)),
                ('cep', models.CharField(blank=True, max_length=9, null=True)),
                ('uf', models.CharField(blank=True, max_length=2, null=True)),
                ('telefone1', models.CharField(blank=True, max_length=20, null=True)),
                ('telefone2', models.CharField(blank=True, max_length=20, null=True)),
                ('telefoneCelular', models.CharField(blank=True, max_length=20, null=True)),
                ('tipoPagamento', models.CharField(blank=True, max_length=2, null=True)),
                ('vencimento', models.DateField(blank=True, max_length=10, null=True)),
                ('limiteCreditoPedido', models.DecimalField(blank=True, decimal_places=2, max_digits=16, max_length=16, null=True)),
                ('limiteGeralCredito', models.DecimalField(blank=True, decimal_places=2, max_digits=16, max_length=16, null=True)),
                ('status', models.CharField(blank=True, max_length=1, null=True)),
                ('justificaBloqueio', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ('razaoSocial',),
            },
        ),
        migrations.CreateModel(
            name='FormaPagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=2)),
                ('descricaoPagamento', models.CharField(max_length=60)),
            ],
            options={
                'ordering': ('sigla',),
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Cliente')),
                ('formapagamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.FormaPagamento')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='shop.Product')),
            ],
        ),
        migrations.CreateModel(
            name='PrazoPagamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricaoPrazoPagamento', models.CharField(max_length=60)),
            ],
            options={
                'ordering': ('descricaoPrazoPagamento',),
            },
        ),
        migrations.AddField(
            model_name='order',
            name='prazopagamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.PrazoPagamento'),
        ),
    ]
