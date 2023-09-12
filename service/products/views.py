from rest_framework.response import Response
from rest_framework.views import APIView

class TestDataApiView(APIView):
    def get(self, request):
        # Получаем набор всех записей из таблицы Capital
        # Сериализуем извлечённый набор записей
        data = {'test': 'data', 'hello': 'world'}
        return Response(data)
