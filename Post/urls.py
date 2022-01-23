from django.urls import path

from .views import ListAddPostView,EditPostView,SearchView,CommentView

app_name = "post"
urlpatterns = [
    path('',ListAddPostView.as_view(),name='List'),
    path('page/<int:page>/',ListAddPostView.as_view(),name='List'),
    path('edit-post/<int:pk>/',EditPostView.as_view(),name='edit-post'),
    path('search/',SearchView.as_view(),name='search'),
    path('comment/<str:text>/',CommentView.as_view(),name='comment'),

]