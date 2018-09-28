from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('livros/', include([
        path('', views.LivroSearchForm.as_view(), name='livro-list'),
        path('list.json', views.LivroJsonListView.as_view(), name='livro-json-list'),
        path('novo/', views.LivroCreateView.as_view(), name='livro-create'),
        path('<int:pk>/', views.LivroUpdateView.as_view(), name='livro-update'),
    ])),
    path('autores/', include([
        path('', views.AutorListView.as_view(), name='autor-list'),
        path('taken/', views.autor_nome_registrado, name='autor-taken'),
        path('novo/', views.AutorCreateView.as_view(), name='autor-create'),
        path('<int:pk>/', views.AutorUpdateView.as_view(), name='autor-update'),
    ])),
    path('remover/<int:pk>/<str:app>/<str:model>/', views.GenericDeleteView.as_view(), name='generic-delete'),

    path('editora/',include([
        path('', views.EditoraListView.as_view(), name='editora-list'),
        path('novo/', views.EditoraCreateView.as_view(), name='editora-create'),
        path('<int:pk>/', views.EditoraUpdateView.as_view(), name='editora-update'),

        ])),

     path('loja/',include([
        path('', views.LojaListView.as_view(), name='loja-list'),
        path('novo/', views.LojaCreateView.as_view(), name='loja-create'),
        path('<int:pk>/', views.LojaUpdateView.as_view(), name='loja-update'),

        ])),

]
