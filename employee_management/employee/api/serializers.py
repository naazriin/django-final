from rest_framework import serializers
from employee.models import Employee
from position.models import Position
from department.models import Department
from rest_framework.decorators import api_view
from department.api.serializers import DepartmentSerializer
from position.api.serializers import PositionSerializer

class EmployeeSerializer(serializers.ModelSerializer):
    # department_id = serializers.CharField(source = "department.name")
    # position_id = serializers.CharField(source="position.name")
    department_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all()
    )
    department_id = DepartmentSerializer(read_only=True, source='department') 
    
    position_id = serializers.PrimaryKeyRelatedField(
        queryset=Position.objects.all()
    )
    position_id = PositionSerializer(read_only=True, source='position') 
    
    class Meta:
        model = Employee
        fields = ('id', 'name','surname','email','department_id','position_id','status',
                  'created_at', 'updated_at')