from rest_framework import routers

from example.views import BookViewSet

router = routers.SimpleRouter()
router.register('books', BookViewSet)

urlpatterns = router.urls
# urlpatterns = [
#     path("hello/", HelloAPI),
#     path("fbv/books/", booksAPI),
#     path("fbv/book/<int:bid>/", bookAPI),
#     path("cbv/books/", BooksAPI.as_view()),
#     path("cbv/book/<int:bid>/", BookAPI.as_view()),
#     path("mixins/books/", BooksAPIMixins.as_view()),
#     path("mixins/book/<int:bid>", BookAPIMixins.as_view())
# ]
