from django.urls import path
from . import views

urlpatterns = [
    path('empleados', views.EmpleadoListView.as_view(), name='empleados'),
    path('<int:pk>/detalles_empleado', views.EmpleadoDetailView.as_view(), name='detalles_empleado'),
    path('<int:pk>/delete_empleado', views.EmpleadoDeleteView.as_view(), name='delete_empleado'),
    path('crear_empleado', views.EmpleadoCreateView.as_view(), name='crear_empleado' ),
    path('<int:pk>/modificar_empleado', views.EmpleadoUpdateView.as_view(), name='modificar_empleado'),
]