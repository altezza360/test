from django.urls import path, include
from .views import base, manager, specialist_view, create_specialist, create_order, edit_order, delete_order, customers, register, user_page


urlpatterns = [
    path('', base, name = 'base_url'),
    path('manager_page/', manager, name='manager_url'),
    path('specialists/<str:pk>/', specialist_view, name='specialist_view_url'),
    path('create_specialist/', create_specialist, name='create_specialist_url'),
    path('create_order/', create_order, name='create_order_url'),
    path('edit_order/<str:pk>', edit_order, name="edit_order_url"),
    path('delete_order/<str:pk>', delete_order, name="delete_order_url"),
    path('customers/', customers, name='customers_url'),
    path('register/', register, name="register_url"),
    # path('login/', loginPage, name="login"),
    # path('logout/', logoutUser, name="logout"),
    path('user_page/', user_page, name="user_page_url")
]

