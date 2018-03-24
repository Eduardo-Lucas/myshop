from django.db import models
from shop.models import Product

FISICA_JURIDICA_CHOICES = (('F', 'Pessoa Física'), ('J', 'Pessoa Jurídica'))


class FormaPagamento(models.Model):
    sigla = models.CharField(max_length=3)
    descricaoPagamento = models.CharField(max_length=60)

    class Meta:
        ordering = ('sigla',)

    def __str__(self):
        return self.descricaoPagamento


class PrazoPagamento(models.Model):
    descricaoPrazoPagamento = models.CharField(max_length=60)

    class Meta:
        ordering = ('descricaoPrazoPagamento',)

    def __str__(self):
        return self.descricaoPrazoPagamento


class Cliente(models.Model):
    codigo = models.IntegerField()
    razaoSocial = models.CharField(max_length=60)
    nomeFantasia = models.CharField(max_length=60)
    tipo = models.CharField(max_length=1, choices=FISICA_JURIDICA_CHOICES, default='F')
    cnpjcpf = models.CharField(max_length=14, blank=True, null=True)
    inscricao = models.CharField(max_length=9, blank=True, null=True)
    regiao = models.CharField(max_length=14, blank=True, null=True)
    grupo = models.CharField(max_length=14, blank=True, null=True)
    # codigoVendedor = models.CharField(max_length=14, blank=True, null=True)
    endereco = models.CharField(max_length=60, blank=True, null=True)
    complemento = models.CharField(max_length=60, blank=True, null=True)
    bairro = models.CharField(max_length=60, blank=True, null=True)
    cidade = models.CharField(max_length=60, blank=True, null=True)
    cep = models.CharField(max_length=9, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    telefone1 = models.CharField(max_length=20, blank=True, null=True)
    telefone2 = models.CharField(max_length=20, blank=True, null=True)
    telefoneCelular = models.CharField(max_length=20, blank=True, null=True)
    tipoPagamento = models.CharField(max_length=2, blank=True, null=True)
    vencimento = models.DateField(max_length=10, blank=True, null=True)
    limiteCreditoPedido = models.DecimalField(max_length=16, max_digits=16, decimal_places=2, blank=True, null=True)
    limiteGeralCredito = models.DecimalField(max_length=16, max_digits=16, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    justificaBloqueio = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ('razaoSocial',)

    def __str__(self):
        return 'Cliente {}'.format(self.razaoSocial)


class Order(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Cliente ")
    formapagamento = models.ForeignKey(FormaPagamento, on_delete=models.CASCADE, blank=True, null=True,
                                       verbose_name="Forma de Pagamento ")
    prazopagamento = models.ForeignKey(PrazoPagamento, on_delete=models.CASCADE, blank=True, null=True,
                                       verbose_name="Prazo de Pagamento ")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "pedido"
        verbose_name_plural = "pedidos"

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
