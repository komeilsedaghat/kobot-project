from django.urls import path

from .views import ListPostView,AddPostView,EditPostView,SearchView

app_name = "post"
urlpatterns = [
    path('',ListPostView.as_view(),name='List'),
    path('page/<int:page>/',ListPostView.as_view(),name='List'),
    path('add-post/',AddPostView.as_view(),name='add-post'),
    path('edit-post/<int:pk>/',EditPostView.as_view(),name='edit-post'),
    path('search/',SearchView.as_view(),name='search'),

]