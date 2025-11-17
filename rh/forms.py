from django import forms
from .models import MensagemContato
from django.contrib.auth.models import User #from para login

class ContatoModelForm(forms.ModelForm):
    
    class Meta:
        model = MensagemContato
        
        # CAMPOS ATUALIZADOS
        fields = ['nome', 'email', 'celular', 'assunto', 'descricao']

        # WIDGETS ATUALIZADOS
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Seu nome completo', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'seu-email@exemplo.com', 'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'placeholder': 'Ex: (XX) XXXXX-XXXX', 'class': 'form-control'}),
            'assunto': forms.TextInput(attrs={'placeholder': 'Assunto da mensagem', 'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Digite sua mensagem...', 'class': 'form-control'}),
        }
        
        # LABELS ATUALIZADOS
        labels = {
            'nome': 'Nome Completo',
            'email': 'Seu E-mail',
            'celular': 'Celular/Contato',
            'descricao': 'Descrição (Mensagem)',
        }

#form de login
class LoginForm(forms.Form):
    username = forms.CharField(label='Usuário')
    password = forms.CharField(label='Senha',widget=forms.PasswordInput)

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
