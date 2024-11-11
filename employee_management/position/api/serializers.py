from rest_framework import serializers
from position.models import Position
from department.models import Department
from rest_framework.decorators import api_view
from department.api.serializers import DepartmentSerializer

class PositionSerializer(serializers.ModelSerializer):
    # department_id = serializers.CharField(source = "department.name")
    
    department_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all()
    )
    department_id = DepartmentSerializer(read_only=True, source='department') 
    
    class Meta:
        model = Position
        fields = ('id', 'name', 'salary','department_id', 'created_at', 'updated_at')
     
     