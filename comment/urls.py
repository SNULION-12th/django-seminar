from django.urls import path
from .views import CommentListView, CommentDetailView

app_name = 'comment'
urlpatterns = [
    # CBV url path
    path("", CommentListView.as_view()),
    path("<int:comment_id>/", CommentDetailView.as_view())
]
