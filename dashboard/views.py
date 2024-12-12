from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import DashboardSerializer
from .models import Dashboard

@api_view(['POST'])
def create_dashboard(request):
    """
    Endpoint to create a dashboard

    Returns:
        json: json response stating whether the data was inserted or if there was an error
    """
    try:
        dashboard = Dashboard.objects.filter(id=request.data.get('id'), 
                                             name=request.data.get('name')).first()
        if dashboard:
            return Response('Dashboard with the same name already exists, please provide another name', status=status.HTTP_409_CONFLICT)
        
        serializer = DashboardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            raise Exception(serializer.errors)

    except Exception as e:
        return Response(e, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    

@api_view(['GET'])
def find_dashboard(request):
    """
    Endpoint to find a Dashboard

    Returns:
        json: json response stating whether the User was found or if there was an error
    """
    try:
        dashboard = Dashboard.objects.filter(id=request.data.get('id')).first()

        if dashboard:
            serializer = DashboardSerializer(dashboard)
            return Response(serializer.data)
        else:
            raise Exception('No Dashboard with this name found')

    except Exception as e:
        return Response(e, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


@api_view(['GET'])
def find_all_dashboards(request):
    """
    Endpoint to find all Dashboards for a user_id

    Returns:
        json: json response stating whether the dashboard was found or if there was an error
    """
    try:
        dashboards = Dashboard.objects.filter(user_id=request.data.get('user_id'))
        serializer = DashboardSerializer(dashboards, many=True)
        return Response(serializer.data)

    except Exception as e:
        return Response(e, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    

@api_view(['DELETE'])
def delete_dashboard(request):
    """
    Endpoint to delete a Dashboard

    Returns:
        json: json response stating whether the User was deleted or if there was an error
    """
    try:
        dashboard = Dashboard.objects.filter(id=request.data.get('id')).first()
        if dashboard:
            dashboard.delete()
            return Response('Dashboard Deleted Successfully', status=status.HTTP_204_NO_CONTENT)
        else:
            raise Exception('No Dashboard found to delete')

    except Exception as e:
        return Response(e, status=status.HTTP_422_UNPROCESSABLE_ENTITY)    


@api_view(['DELETE'])
def delete_all_dashboards(request):
    """
    Endpoint to delete all Dashboards for a User

    Returns:
        json: json response stating whether the User was deleted or if there was an error
    """
    try:
        dashboards = Dashboard.objects.filter(user_id=request.data.get('user_id'))
        if dashboards:
            dashboards.delete()
            return Response('Dashboard Deleted Successfully', status=status.HTTP_204_NO_CONTENT)
        else:
            raise Exception('No Dashboards found for this user to delete')

    except Exception as e:
        return Response(e, status=status.HTTP_422_UNPROCESSABLE_ENTITY)   


@api_view(['PUT'])
def update_dashboard(request):
    """
    Endpoint to Update an existing Dashboard

    Returns:
        json: json response stating whether the User was updated or if there was an error
    """
    try:
        dashboard = Dashboard.objects.filter(id=request.data.get('id')).first()
        
        if dashboard:
            serializer = DashboardSerializer(dashboard, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                raise Exception(serializer.errors)
        else:
            raise Exception('No Dashboard found to be updated')
    
    except Exception as e:
        return Response(e, status=status.HTTP_422_UNPROCESSABLE_ENTITY)