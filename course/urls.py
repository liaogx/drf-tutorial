#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = "__Jack__"


from django.urls import path, include
from rest_framework.routers import DefaultRouter

from course import views

router = DefaultRouter()
router.register("viewsets", views.CourseViewSet)

urlpatterns = [
    # Function Based View
    path("fbv/list/", views.course_list, name="fbv-list"),
    path("fbv/detail/<int:pk>/", views.course_detail, name="fbv-detail"),

    # Classed Based View
    path("cbv/list/", views.CourseList.as_view(), name="cbv-list"),
    path("cbv/detail/<int:pk>/", views.CourseDetail.as_view(), name="cbv-detail"),

    # Generic Classed Based View
    path("gcbv/list/", views.GCourseList.as_view(), name="gcbv-list"),
    path("gcbv/detail/<int:pk>/", views.GCourseDetail.as_view(), name="gcbv-detail"),

    # DRF viewsets
    path("", include(router.urls)),
]
