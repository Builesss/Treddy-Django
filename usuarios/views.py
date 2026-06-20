from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import CustomLoginForm

class CustomLoginView(LoginView):
    template_name = 'usuarios/login.html'
    authentication_form = CustomLoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        # Capa de seguridad: Aseguramos que solo usuarios activos entren
        if self.request.user.estado != 'Activo':
            messages.error(self.request, "Su cuenta no está activa. Contacte al administrador.")
            logout(self.request)
            return reverse_lazy('login')
        return reverse_lazy('dashboard')

    def form_invalid(self, form):
        messages.error(self.request, "Credenciales incorrectas o caracteres no permitidos.")
        return super().form_invalid(form)

@login_required
def dashboard_view(request):
    user = request.user
    # Delegación de dashboard por roles (POO y Patrón Strategy simplificado)
    if user.tipo_usuario == 'Administrador':
        template = 'usuarios/dashboards/admin.html'
    elif user.tipo_usuario == 'Vendedor':
        template = 'usuarios/dashboards/vendedor.html'
    else:
        template = 'usuarios/dashboards/cliente.html'
        
    return render(request, template, {'user': user})

def custom_logout(request):
    logout(request)
    return redirect('login')
