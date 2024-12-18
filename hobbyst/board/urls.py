from django.urls import path
from board.views import (
    home,
    comment_add,
    comment_delete,
    post_add,
    tags,
    post_detail,
    post_like,
    feed_page,
)

app_name = "board"
urlpatterns = [
    path("", home, name="home"),
    path("comment_add/", comment_add, name="comment_add"),
    path("comments/<int:comment_id>/delete/", comment_delete, name="comment_delete"),
    path("post_add/", post_add, name="post_add"),
    path("tags/<str:tag_name>/", tags, name="tags"),
    path("<int:post_id>/", post_detail, name="post_detail"),
    path("<int:post_id>/like/", post_like, name="post_like"),
    path("feed/", feed_page, name="feed_page"),
]
