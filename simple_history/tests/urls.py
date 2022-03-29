from __future__ import unicode_literals

from django.urls import path
from django.contrib import admin

from simple_history.tests.view import (
    BucketDataRegisterRequestUserCreate,
    BucketDataRegisterRequestUserDetail,
    PollCreate,
    PollDelete,
    PollDetail,
    PollList,
    PollUpdate,
    PollWithHistoricalIPAddressCreate,
)
from . import other_admin

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('other-admin/', other_admin.site.urls),
    path(
        'bucket_data/add/',
        BucketDataRegisterRequestUserCreate.as_view(),
        name="bucket_data-add",
    ),
    path(
        'bucket_data/<int:pk>/',
        BucketDataRegisterRequestUserDetail.as_view(),
        name="bucket_data-detail",
    ),
    path('poll/add/', PollCreate.as_view(), name="poll-add"),
    path(
        'pollwithhistoricalipaddress/add',
        PollWithHistoricalIPAddressCreate.as_view(),
        name="pollip-add",
    ),
    path('poll/<int:pk>/', PollUpdate.as_view(), name="poll-update"),
    path('poll/<int:pk>/delete/', PollDelete.as_view(), name="poll-delete"),
    path('polls/<int:pk>/', PollDetail.as_view(), name="poll-detail"),
    path('polls/', PollList.as_view(), name="poll-list"),
]
