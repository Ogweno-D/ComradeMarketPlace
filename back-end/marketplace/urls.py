from django.urls import path
from .views import (
    ProductViewSet,
    CommentViewSet,
    ProductImageViewSet,
    CategoryViewSet,
    BookmarkViewSet,
)

urlpatterns = [
    # Products
    path(
        "all-products",
        ProductViewSet.as_view({"get": "get_products"}),
        name="product-list",
    ),
    path(
        "products",
        ProductViewSet.as_view({"post": "create_product"}),
        name="product-create",
    ),
    path(
        "products/update",
        ProductViewSet.as_view({"put": "update_product"}),
        name="product-update",
    ),
    path(
        "products/delete",
        ProductViewSet.as_view({"delete": "delete_product"}),
        name="product-delete",
    ),
    # Comments
    path(
        "product/comments",
        CommentViewSet.as_view({"get": "get_comments_by_product"}),
        name="product-comment-list",
    ),
    path(
        "user/comments",
        CommentViewSet.as_view({"get": "get_comments_by_user"}),
        name="user-comment-list",
    ),
    path(
        "comments",
        CommentViewSet.as_view({"post": "post_comment"}),
        name="comment-create",
    ),
    path(
        "comments/delete",
        CommentViewSet.as_view({"delete": "delete_comment"}),
        name="comment-delete",
    ),
    # Product Images
    path(
        "product/images",
        ProductImageViewSet.as_view({"get": "get_images"}),
        name="product-image-list",
    ),
    path(
        "product/images/add",
        ProductImageViewSet.as_view({"post": "create"}),
        name="product-image-create",
    ),
    path(
        "product/images/delete/<int:pk>",
        ProductImageViewSet.as_view({"delete": "destroy"}),
        name="product-image-delete",
    ),
    # Categories
    path(
        "all-categories",
        CategoryViewSet.as_view({"get": "get_categories"}),
        name="category-list",
    ),
    path(
        "category/add",
        CategoryViewSet.as_view({"post": "create_category"}),
        name="category-create",
    ),
    path(
        "category/delete",
        CategoryViewSet.as_view({"delete": "delete_category"}),
        name="category-delete",
    ),
    # Bookmarks
    path(
        "user/product-bookmarks",
        BookmarkViewSet.as_view({"get": "get_bookmarks_by_user"}),
        name="bookmark-list",
    ),
    path(
        "product-bookmark/add",
        BookmarkViewSet.as_view({"post": "create_bookmark"}),
        name="bookmark-create",
    ),
    path(
        "toggle/favorite",
        BookmarkViewSet.as_view({"put": "update_bookmark"}),
        name="bookmark-update",
    ),
    path(
        "product-bookmark/delete",
        BookmarkViewSet.as_view({"delete": "delete_bookmark"}),
        name="bookmark-delete",
    ),
]
