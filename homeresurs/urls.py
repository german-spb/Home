"""
URL configuration for homeresurs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from resurses import views
from django.conf import settings
from django.conf.urls.static import static
from resurses.views import CountersFormView, SuccessView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('counters/', views.counters),
    path('documents/', views.documents),
    path('documents/<int:file_id>/', views.document_view),
    path('documents_german/', views.documents_german_upload, name='german'),
    path('documents_german/<int:file_id>/', views.document_view),
    path('documents_irina/<int:file_id>/', views.document_view),
    path('documents_german_delete/<int:file_id>/', views.document_delete, name='document_delete'),
    path('documents_irina/', views.documents_irina_upload),
    path('documents_mark/', views.documents_mark_upload),
    path('documents_mark/<int:file_id>/', views.document_view),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('input_date/', CountersFormView.as_view(), name='input_date'),
    path('success/', SuccessView.as_view(), name='success'),
    path('list_counters/', views.list_counters),
    path('list_counters/list_counters_date_pay/', views.create_data_pay),
    path('delete_all/', views.all_delete),
    path('delete_documents/', views.delete_documents),
    path('delete/<int:file_id>/', views.delete, name='delete'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)