from rest_framework import serializers
from department.models import Department
from rest_framework.decorators import api_view

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name', 'created_at', 'updated_at')