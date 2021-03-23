from django.urls import path
from .views import *

urlpatterns = [

    path("", BookmarkListView.as_view(), name='list'),
    #as_view()는 앞 클래스형 뷰인 BookmarkListView를 함수형 view로 바꿔주는 역할
    path("add/", BookmarkCreateView.as_view(), name='add'),
    path("detail/<int:pk>/", BookmarkDetailView.as_view(), name='detail'),
    path("update/<int:pk>/", BookmarkUpdateView.as_view(), name='update'),
    path("delete/<int:pk>/", BookmarkDeleteView.as_view(), name='delete'),
]