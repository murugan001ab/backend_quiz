from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import User, Question
from .serialiser import UserSerializer, QuestionSerializer

class UserCreateView(APIView):
    """Save user name & score"""

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    def post(self, request):    
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuestionListView(APIView):
    """Fetch all questions"""
    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)
