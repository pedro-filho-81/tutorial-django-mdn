from django.urls import path
# do aplicativo catalog importe o arquivo views
from catalog import views

# lista de urls
urlpatterns = [
  # do arquivo views inclua a função cadastro
  path('catalog/', views.cadastro, name='cadastro')
]
