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
# from tkinter.font import names

from django.contrib import admin
from django.urls import path
from resurses import views
from django.conf import settings
from django.conf.urls.static import static
from resurses.views import CountersFormView, SuccessView
# from tkinter import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('counters/', views.counters),

    path('documents/', views.documents, name='documents_home'),
    path('documents/<int:file_id>/', views.document_view),
    path('documents_home_delete/<int:file_id>/', views.delete_document_home, name='delete_home'),
    path('documents_home_delete_confirm/<int:file_id>/', views.document_delete_home_confirm, name='document_home_delete'),

    path('documents_german/<int:file_id>/', views.document_view),
    path('documents_german/', views.documents_german_upload, name='documents_german'),
    path('documents_german_delete/<int:file_id>/', views.delete_document_german, name='delete_german'),
    path('documents_german_delete_confirm/<int:file_id>/', views.document_delete_german_confirm, name='document_german_delete'),

    path('documents_irina/<int:file_id>/', views.document_view),
    path('documents_irina/', views.documents_irina_upload, name='documents_irina'),
    path('documents_irina_delete/<int:file_id>/', views.delete_document_irina, name='delete_irina'),
    path('documents_irina_delete_confirm/<int:file_id>/', views.document_delete_irina_confirm, name='document_irina_delete'),

    path('documents_mark/', views.documents_mark_upload, name='documents_mark'),
    path('documents_mark/<int:file_id>/', views.document_view),
    path('documents_mark_delete/<int:file_id>/', views.delete_document_mark, name='delete_mark'),
    path('documents_mark_delete_confirm/<int:file_id>/', views.document_delete_mark_confirm, name='document_mark_delete'),
    path('delete_documents/', views.delete_documents, name='delete_all_documents'),

    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('input_date/', CountersFormView.as_view(), name='input_date'),
    path('success/', SuccessView.as_view(), name='success'),

    path('list_counters/', views.list_counters, name='counters'),
    path('delete_all/', views.all_delete, name='delete_all_counters'),
    path('list_counters/counters_edit/<int:id>/', views.counters_edit),



    path('book/', views.book_upload, name= 'book'),
    path('delete_book/<int:file_id>/', views.delete_book, name='delete_book_confirm'),
    path('delete_book_confirm/<int:file_id>/', views.delete_book_confirm, name='delete_book'),
    path('download/', views.download_book, name='download')


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)