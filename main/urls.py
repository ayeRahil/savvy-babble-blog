from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('articles/', views.HomeView.as_view(template_name='main/allarticles.html'), name='all-article'),
    path('authors/', views.AuthorView.as_view(), name='authors'),
    path('article/<int:pk>', views.PostDetailView.as_view(), name='article-detail'),
    path('add_article/', views.CreateArticleView.as_view(), name='add-article'),
    path('add_category/', views.CreateCategoryView.as_view(), name='add-category'),
    path('category/<str:cats>', views.CategoryView, name='category'),
    path('article/update/<int:pk>', views.UpdateArticleView.as_view(), name='update-article'),
    path('article/<int:pk>/remove', views.DeleteArticleView.as_view(), name='delete-article'),
]