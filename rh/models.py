from django.db import models
from django.utils import timezone
from django import forms
from django.contrib.auth.models import User

class Funcionarios(models.Model):
    foto = models.ImageField(null=True, blank=True)
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    data_contratacao = models.DateField()
    status = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários" 
    def __str__(self):
        return self.nome
    
# NOVO MODELO: PRODUTO
class Produto(models.Model):
    imagem = models.ImageField(upload_to='produtos', null=True, blank=True)
    nome = models.CharField(max_length=150)
    categoria = models.CharField(max_length=100)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        
    def __str__(self):
        return self.nome

# NOVO MODELO: CLIENTE
class Cliente(models.Model):
    nome_completo = models.CharField(max_length=150)
    idade = models.IntegerField()
    email = models.EmailField()
    contato = models.CharField(max_length=20) 

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        
    def __str__(self):
        return self.nome_completo

# MODELO MensagemContato (MODIFICADO)
class MensagemContato(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    celular = models.CharField(max_length=20, null=True, blank=True) 
    assunto = models.CharField(max_length=200)
    descricao = models.TextField() 
    data_envio = models.DateTimeField(default=timezone.now)
    lido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.assunto} - {self.nome} ({self.email})"

    class Meta:
        verbose_name = "Mensagem de Contato"
        verbose_name_plural = "Mensagens de Contato"
        ordering = ['-data_envio']


# rh/forms.py
class LoginForm(forms.Form):
    username = forms.CharField(label='Usuário')
    password = forms.CharField(label='Senha',widget=forms.PasswordInput)

# rh/forms.py
class RegistroForm(forms.ModelForm):
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme a senha',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','email')

    def clean(self):
        cleaned = super().clean()
        if cleaned.get('password') != cleaned.get('password2'):
            raise forms.ValidationError('Senhas diferentes')
        return cleaned
