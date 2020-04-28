from django.urls import path
from .views import *

urlpatterns = [
    path('', BookListView.as_view(), name='home'),
    path('detail/<int:pk>/', book_detail_view, name='detail'),
    path('news/', NewBookListView.as_view(), name='new'),
    path('random/', RandomBookView.as_view(), name='random'),
    path('create/', BookCreate.as_view(), name='create'),
    path('update/<int:pk>', BookUpdate.as_view(), name='update'),
    path('delete/<int:pk>', BookDelete.as_view(), name='delete'),

]


