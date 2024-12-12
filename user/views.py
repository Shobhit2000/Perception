from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserSerializer
from .models import User

@api_view(['POST'])
def signup(request):
    """
    Endpoint to add a User in MongoDB

    Returns:
        json: json response stating whether the data was inserted or if there was an error
    """
    try:
        user = User.objects.filter(email=request.data.get('email')).first()
        if user:
            return Response('User with the provided email already exists, Please try another email', status=status.HTTP_409_CONFLICT)

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            raise Exception(serializer.errors)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    

@api_view(['POST'])
def login(request):
    """
    Endpoint to add a User in MongoDB

    Returns:
        json: json response stating whether the data was inserted or if there was an error
    """
    try:
        user = User.objects.filter(email=request.data.get('email'), password=request.data.get('password')).first()
        if user:
            return Response('User Logged In', status=status.HTTP_200_OK)
        else:
            raise Exception('Invalid Credentials !!')

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


@api_view(['GET'])
def find_user(request):
    """
    Endpoint to find a User

    Returns:
        json: json response stating whether the User was found or if there was an error
    """
    try:
        user = User.objects.filter(id=request.data.get('id')).first()
        if user:
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            raise Exception('User Not found')
    
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

@api_view(['GET'])
def find_all_users(request):
    """
    Endpoint to find all Users

    Returns:
        json: json response stating whether the User was found or if there was an error
    """
    try:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    

@api_view(['DELETE'])
def delete_user(request):
    """
    Endpoint to delete a User

    Returns:
        json: json response stating whether the User was deleted or if there was an error
    """
    try:
        user = User.objects.filter(id=request.data.get('id')).first()
        if user:
            user.delete()
            return Response('User Deleted', status=status.HTTP_204_NO_CONTENT)
        else:
            raise Exception('User Not Found to be deleted')
    
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


@api_view(['PUT'])
def update_user(request):
    """
    Endpoint to Update an existing User in MongoDB

    Returns:
        json: json response stating whether the User was updated or if there was an error
    """
    try:
        user = User.objects.filter(id=request.data.get('id')).first()
        if user:
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                raise Exception(serializer.errors)
        else:
            raise Exception('No User found to be updated')
    
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)