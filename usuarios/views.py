from django.shortcuts import render
from .filters import UsuariosFilter
from .models import Usuarios
# Create your views here.

def search(request):
    all_usuarios = Usuarios.objects.all()
    user_filter = UsuariosFilter(request.GET, queryset=all_usuarios)
    return render(request, 'usuarios/user_list.html', {'filter': user_filter})