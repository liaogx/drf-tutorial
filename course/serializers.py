#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = "__Jack__"

from django import forms
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ("name", "introduction", "teacher", "price")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    # teacher_username = serializers.CharField(source="teacher.username")
    teacher = serializers.ReadOnlyField(source="teacher.username")  # 外键字段 只读

    class Meta:  # 写法和上面的CourseForm类似
        model = Course
        # exclude = ("id",)  # 注意元组中只有1个元素时不能写成("id")
        fields = ("id", "name", "introduction", "teacher", "price", "created_at", "updated_at")
        # fields = "__all__"

# class CourseSerializer(serializers.HyperlinkedModelSerializer):
#     teacher = serializers.CharField(source="teacher.username")
#
#     # teacher = serializers.ReadOnlyField(source="username")  # 外键字段 只读
#
#     class Meta:  # 写法和上面的CourseForm类似
#         model = Course
#         # url是默认值，可在settings.py中设置URL_FIELD_NAME使全局生效
#         fields = ("id", "url", "name", "introduction", "teacher", "price", "created_at", "updated_at")
#         # read_only_fields = ("teacher",)  # 模型类中设置editable=False或AutoField字段默认被为只读属性
