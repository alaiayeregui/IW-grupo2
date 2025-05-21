from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

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
    path('correo_contacto', views.ContactoEmailView.as_view(), name = 'correo_contacto'),
    path('proyectos', views.ProyectoListView.as_view(), name='proyectos'),
    path('<int:pk>/detalles_proyecto', views.ProyectoDetailView.as_view(), name='detalles_proyecto'),
    path('<int:pk>/delete_proyecto', views.ProyectoDeleteView.as_view(), name='delete_proyecto'),
    path('crear_proyecto', views.ProyectoCreateView.as_view(), name='crear_proyecto' ),
    path('<int:pk>/modificar_proyecto', views.ProyectoUpdateView.as_view(), name='modificar_proyecto'),
    path('responsables', views.ResponsableListView.as_view(), name='responsables'),
    path('<int:pk>/detalles_responsable', views.ResponsableDetailView.as_view(), name='detalles_responsable'),
    path('<int:pk>/delete_resposable', views.ResponsableDeleteView.as_view(), name='delete_responsable'),
    path('crear_responsable', views.ResponsableCreateView.as_view(), name='crear_responsable' ),
    path('<int:pk>/modificar_responsable', views.ResponsableUpdateView.as_view(), name='modificar_responsable'),
    path('tareas', views.TareaFiltrarLista, name='tareas'),
    path('<int:pk>/detalles_tarea', views.TareaDetailView.as_view(), name='detalles_tarea'),
    path('crear_tarea', views.TareaCreateView.as_view(), name='crear_tarea'),
    path('<int:pk>/delete_tarea', views.TareaDeleteView.as_view(), name='delete_tarea'),
    path('<int:pk>/modificar_tarea', views.TareaUpdateView.as_view(), name='modificar_tarea'),
    path('<int:pk>/modificar_tarea_notas', views.TareaNotasUpdateView.as_view(), name='modificar_tarea_notas'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)