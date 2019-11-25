from .models import Usuarios
import django_filters

class UsuariosFilter(django_filters.FilterSet):
    first_correo = django_filters.CharFilter(name='correo',lookup_expr='icontains')
    class Meta:
        model = Usuarios
        fields = ['nombre', 'correo', 'usuario','first_correo']