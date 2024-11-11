from django.urls import path

from position.api.views import (position_view, 
                                PositionListCreateApiView,PositionRetrieveUpdateView,)

urlpatterns = [
    # path('position/', position_view , name='position'),
    path('position/', PositionListCreateApiView.as_view(), name='position'),
    path('position/<int:pk>/', PositionRetrieveUpdateView.as_view() , name='position_update'),
    
]
