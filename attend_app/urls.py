from django.urls import path
from . import views
from .views import UserUpdateAPIView,EmployerProfileEditView,UserDeleteAPIView,EmployeeDetailsUpdateAPIView
from django.urls import include, path
from rest_framework import routers
from .views import fetch_and_store_data


urlpatterns = [
    path("register", views.register, name="register"),
    path("login",views.login, name="login"),
    #path('dashboard/',views.dashboard,name='dashboard'),
    path('logout',views.logout,name='logout'),
    path('employer-profile/', views.EmployerProfile, name='employer_profile'),
    #path('TaxDetails/', views.TaxDetails, name='Tax_details'),
    path('employee_details/', views.EmployeeDetails, name='employee_details'),
    path('employee_details/<int:employee_id>/',EmployeeDetailsUpdateAPIView.as_view(), name='Employee_Details_UpdateAPIView'),
    path('<str:username>/', UserUpdateAPIView.as_view(),name='User-Update-API-View'),
    path('employer-profile/<int:employer_id>/',EmployerProfileEditView.as_view(),name='Employer_Profile_UpdateAPIView'),
    path('delete/<str:username>/', UserDeleteAPIView.as_view(), name='user-delete'),
    #path('upload', views.upload_pdf, name='upload_pdf'),
    path('getemployeedetails/<int:employer_id>/', views.get_employee_by_employer_id, name='employee-by-employer-id'),
    path('getemployerdetails/<int:employer_id>/', views.get_employer_details, name='employer-detail-by-employer-id'),
    #path('DashboardData',views.get_dashboard_data, name='iwo_dashboard'),
    #path('IWO_Data',views.insert_iwo_detail, name='iwo_pdf_data'),
    #@email url
    # count url
    path('dashboard_data', fetch_and_store_data, name='fetch_data'),

    # path('email_list', views.email_data_list, name='email_data_list'),
    # path('email_data/<int:pk>/', views.email_data_detail, name='email_data_detail'),
    # path('email_data/new/', views.email_data_new, name='email_data_new'),
    # path('email_data/<int:pk>/edit/', views.email_data_edit, name='email_data_edit'),
    # path('email_data/<int:pk>/delete/', views.email_data_delete, name='email_data_delete'),





]



