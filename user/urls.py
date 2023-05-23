from django.urls import path
from .views import CreateUserView, DeleteUserView, UpdateUserView, GetUserByIdView

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create_user'),
    path('get-user/', GetUserByIdView.as_view(), name='get_user_by_id'),
    path('delete/<int:user_id>/', DeleteUserView.as_view(), name='delete_user'),
    path('update/<int:user_id>/', UpdateUserView.as_view(), name='update_user'),
]