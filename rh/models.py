from django.db import models

# Create your models here.
class Funcionarios(models.Model):
    foto = models.ImageField(null=True, blank=True)
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    data_contratacao = models.DateField()
    status = models.BooleanField(default=True)
    
    #corrige o problema de duplo 's' no nome do modelo no admin
    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários" # Define o nome plural correto
    def __str__(self):
        return self.nome
    
    # contato/models.py
from django.db import models
from django.utils import timezone

class MensagemContato(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    assunto = models.CharField(max_length=200)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(default=timezone.now)
    lido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.assunto} - {self.nome} ({self.email})"

    class Meta:
        verbose_name = "Mensagem de Contato"
        verbose_name_plural = "Mensagens de Contato"
        ordering = ['-data_envio']

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def _str_(self):
        # Isto ajuda a exibir um nome legível na área administrativa
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(null=True, blank=True)
    categoria = models.CharField(max_length=100,null=True, blank=True)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    em_estoque = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos" 
    def _str_(self):
        return self.nome
    
    
class Cliente(models.Model):
    nome_completo = models.CharField(max_length=255)
    # PositiveIntegerField garante que a idade não será negativa
    idade = models.PositiveIntegerField()
    email = models.EmailField(unique=True) # unique=True evita emails duplicados
    contato = models.CharField(max_length=20) # Para telefone/celular

    def _str_(self):
        return self.nome_completo
    
class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    celular = models.CharField(max_length=20)
    assunto = models.CharField(max_length=150)
    descricao = models.TextField()

    def _str_(self):
        # Mostra o assunto e o nome no admin
        return f"{self.assunto} - {self.nome}"