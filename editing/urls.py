
from django.contrib import admin
from django.urls import path
from filer.views import authreg, api_auth, api_reg, home, create_file, edit_file, delete, download, tables, api_requests
from telega.views import send_message

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authreg, name='authreg'),
    path('api_reg/', api_reg, name='api_reg'),
    path('api_auth/', api_auth, name='api_auth'),
    path('home/', home, name='home'),
    path('tables/', tables, name='tables'),
    path('create_file/<str:ext>/', create_file, name='create_file'),
    path('edit_file/<str:file_id>/', edit_file, name='edit_file'),
    path('delete/<str:file_id>/', delete, name='delete'),
    path('download/<str:file_id>/', download, name='download'),
    path('send_message/', send_message, name='send_message'),
    path('api_requests/', api_requests, name='api_requests'),
]