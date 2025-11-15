from django.shortcuts import redirect, render
from .models import Funcionarios, Produto
from .forms import ContatoModelForm
# Create your views here.
def home(request):
    return render(request,'home.html')
def produtos(request):
    produtos = Produto.objects.filter(em_estoque=True)
    context = {
        'produtos': produtos
    }
    return render(request,'produtos.html',context)
def clientes(request):
    return render(request,'clientes.html')
def funcionarios(request):
    funcionarios = Funcionarios.objects.filter(status=True)
    context = {
        'funcionarios': funcionarios
    }
    return render(request,'funcionarios.html',context)

# A view principal do formulário
def formulario_contato_view(request):
    if request.method == 'POST':
        # Cria a instância do formulário com os dados vindos do request
        form = ContatoModelForm(request.POST)
        
        if form.is_valid():
            # A MÁGICA DO MODELFORM:
            # form.save() cria e salva um novo objeto 'MensagemContato'
            # no banco de dados com os dados do formulário.
            form.save()
            
            # Redireciona para uma página de sucesso
            return redirect('contato_sucesso')
    
    else:
        # Se for um GET, apenas cria um formulário vazio
        form = ContatoModelForm()

    # Passa o formulário (vazio ou com erros) para o template
    return render(request, 'contato/contatos.html', {'form': form})


# Uma view simples para a página de "sucesso"
def contato_sucesso_view(request):
    return render(request, 'contato/contato_sucesso.html')

from django.shortcuts import render
# Importe o modelo de Produto que criámos
from .models import Produto

# --- View para a Página de Produtos ---

def lista_produtos(request):
    """
    Esta view busca todos os produtos cadastrados no banco de dados
    e os envia para o template 'produtos.html'.
    """
    
    # 1. Buscar todos os objetos "Produto" na base de dados
    # O .order_by('nome') organiza os produtos por ordem alfabética
    produtos = Produto.objects.all().order_by('nome')
    
    # 2. Criar um "contexto" (um dicionário) para enviar os dados para o template
    # A chave 'produtos' será o nome da variável que usaremos no HTML
    contexto = {
        'produtos': produtos
    }
    
    # 3. Renderizar a página HTML (template) com os dados (contexto)
    # Vamos chamar o nosso template de 'produtos.html'
    return render(request, 'produtos.html', contexto)