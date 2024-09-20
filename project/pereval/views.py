from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Users, Coords, PerevalAdded, PerevalImage
from .serializers import UsersSerializer, PerevalAddedSerializer, CoordsSerializer, PerevalImageSerializer

@api_view(['GET'])
def get_pereval_by_id(request, id):
    try:
        pereval = PerevalAdded.objects.get(id=id)
        pereval_serializer = PerevalAddedSerializer(pereval)
        return Response(pereval_serializer.data, status=status.HTTP_200_OK)
    except PerevalAdded.DoesNotExist:
        return Response({"message": "Pereval not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PATCH'])
def update_pereval(request, id):
    try:
        pereval = PerevalAdded.objects.get(id=id)

        if pereval.status != 'new':
            return Response({"state": 0, "message": "Cannot update record with status other than 'new'"}, status=status.HTTP_400_BAD_REQUEST)

        coords_data = request.data.get('coords')
        coords_serializer = CoordsSerializer(pereval.coord, data=coords_data)
        if coords_serializer.is_valid():
            coords_serializer.save()
        else:
            return Response({"state": 0, "message": coords_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        pereval_data = request.data.get('pereval')
        pereval_data.pop('user', None)
        pereval_data.pop('status', None)

        pereval_serializer = PerevalAddedSerializer(pereval, data=pereval_data, partial=True)
        if pereval_serializer.is_valid():
            pereval_serializer.save()
            return Response({"state": 1, "message": "Record updated successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"state": 0, "message": pereval_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except PerevalAdded.DoesNotExist:
        return Response({"state": 0, "message": "Pereval not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"state": 0, "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_perevals_by_user_email(request):
    try:
        email = request.query_params.get('user__email')
        if not email:
            return Response({"message": "Email query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

        user = Users.objects.get(email=email)
        perevals = PerevalAdded.objects.filter(user=user)
        pereval_serializer = PerevalAddedSerializer(perevals, many=True)
        return Response(pereval_serializer.data, status=status.HTTP_200_OK)
    except Users.DoesNotExist:
        return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def example_view(request):
    """
    Example:
    Возвращает пример данных.

    ---
    parameters:
      - name: id
        description: Уникальный идентификатор
        required: true
        type: integer
        paramType: path
    responses:
      200:
        description: Успешный запрос.
        schema:
          type: object
          properties:
            message:
              type: string
              description: Сообщение.
              example:  API ответ.
    """
    data = {"message": "Пример API ответа"}
    return Response(data, status=status.HTTP_200_OK)