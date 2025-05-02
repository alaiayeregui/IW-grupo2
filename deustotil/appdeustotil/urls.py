from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('empleados', views.EmpleadoListView.as_view(), name='empleados'),
    path('<int:pk>/detalles_empleado', views.EmpleadoDetailView.as_view(), name='detalles_empleado'),
    path('<int:pk>/delete_empleado', views.EmpleadoDeleteView.as_view(), name='delete_empleado'),
    path('crear_empleado', views.EmpleadoCreateView.as_view(), name='crear_empleado' ),
    path('<int:pk>/modificar_empleado', views.EmpleadoUpdateView.as_view(), name='modificar_empleado'),
    path('clientes', views.ClienteListView.as_view(), name='clientes'),
    path('<int:pk>/detalles_cliente', views.ClienteDetailView.as_view(), name='detalles_cliente'),
    path('<int:pk>/detalles_proyecto', views.ProyectoDetailView.as_view(), name='detalles_proyecto'),
    path('<int:pk>/modificar_cliente', views.ClienteUpdateView.as_view(), name='modificar_cliente'),
    path('crear_cliente', views.ClienteCreateView.as_view(), name='crear_cliente' ),
    path('proyectos', views.ProyectoListView.as_view(), name='proyectos'),
    path('<int:pk>/detalles_proyecto', views.ProyectoDetailView.as_view(), name='detalles_proyecto'),
    path('<int:pk>/delete_proyecto', views.ProyectoDeleteView.as_view(), name='delete_proyecto'),
    path('crear_proyecto', views.ProyectoCreateView.as_view(), name='crear_proyecto' ),
    path('<int:pk>/modificar_proyecto', views.ProyectoUpdateView.as_view(), name='modificar_proyecto'),
]