from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index, name="index"),
    path("principal/", views.principal, name="principal"),
    path("padres/", views.padres, name="padres"),
    path("<str:casanombre>", views.mostrar_casa, name="casa_id"),
    path("<str:casa_nombre>/mod", views.casa_modificacion, name="casa_mod"),
    path("crear/", views.crear_casa, name="crear_casa"),
    path("disponibles/", views.disponibles_casa, name="disponibles_casa"),
    path("propiedades/", views.propiedades_casa, name="propiedades_casa"),
    path("blog/", views.blogs_ver, name="blogs_ver"),
    path("blog/<str:blog_titulo>/", views.blogs_vista, name="blogs_vista"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
