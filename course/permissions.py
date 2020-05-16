#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = "__Jack__"


from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """自定义权限：只允许对象的所有者能够编辑"""

    def has_object_permission(self, request, view, obj):
        """
        所有的request请求都有读权限，因此一律允许GET/HEAD/OPTIONS方法
        :param request:
        :param view:
        :param obj:
        :return: bool
        """
        if request.method in permissions.SAFE_METHODS:  # SAFE_METHODS = ("GET", "HEAD", "OPTIONS")
            return True
        # 对象的所有者才有写权限
        return obj.teacher == request.user
