from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Users, Coords, PerevalAdded
from .serializers import UsersSerializer, PerevalAddedSerializer, CoordsSerializer, PerevalImageSerializer


@api_view(['POST'])
def submitData(request):
    try:
        user_data = request.data.get('user')
        user_serializer = UsersSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
        else:
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        coords_data = request.data.get('coords')
        coords_serializer = CoordsSerializer(data=coords_data)
        if coords_serializer.is_valid():
            coords = coords_serializer.save()
        else:
            return Response(coords_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        pereval_data = request.data.get('pereval')
        pereval_data['coord'] = coords.id
        pereval_data['status'] = 'new'
        pereval_serializer = PerevalAddedSerializer(data=pereval_data)
        if pereval_serializer.is_valid():
            pereval = pereval_serializer.save()

            # Обработка изображений
            images_data = request.data.get('images', [])
            for img_data in images_data:
                img_serializer = PerevalImageSerializer(data=img_data)
                if img_serializer.is_valid():
                    img_serializer.save(pereval=pereval)
                else:
                    return Response(img_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(pereval_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "Data submitted successfully"}, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
