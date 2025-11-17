from django.contrib import admin 

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('login/',views.login_view ,name='login'),
    path('logout/',views.logout_view ,name='logout'),
    path('registrar/',views.registrar_view ,name='registrar'),
    path('perfil/',views.perfil ,name='perfil'),
    path('logout', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path('',views.home, name='home'),
    path('produtos/',views.produtos, name='produtos'),
    path('clientes/',views.clientes, name='clientes'),
    path('funcionarios/',views.funcionarios, name='funcionarios'),

   # A URL para a página do formulário
    # Ex: http://127.0.0.1:8000/contato/
    path('contato/', views.formulario_contato_view, name='contatos'),
    
    # A URL para onde o usuário é enviado após o sucesso
    # Ex: http://127.0.0.1:8000/contato/sucesso/
    path('contato/sucesso/', views.contato_sucesso_view, name='contato_sucesso'),
]
