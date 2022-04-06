from django.urls import path
from . import views
from django.conf import settings


urlpatterns = [
    path('',views.BookListView.as_view(),name='book_list'),
    path('index/',views.IndexView.as_view()),
    path('book/<int:pk>/',views.BookDetailView.as_view(),name='book_detail'),
    path('book/add',views.BookCreateView.as_view(),name='book_add'),
    path('book/<int:pk>/edit',views.BookUpdateView.as_view(),name='book_edit'),
    path('book/<int:pk>/remove',views.BookDeleteView.as_view(),name='book_remove'),
    path('drafts/',views.DraftListView.as_view(),name='book_draft'),
    path('book/<int:pk>/publish/',views.book_publish_view,name='book_publish'),
]