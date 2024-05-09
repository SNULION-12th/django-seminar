from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import PostSerializer
from .models import Post
from drf_yasg.utils import swagger_auto_schema

# Create your views here.
class PostListView(APIView):
    @swagger_auto_schema(
            operation_id='게시글 목록 조회',
            operation_description='게시글 목록을 조회합니다.',
            responses={200: PostSerializer(many=True)}
        )
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True) #직렬화할 데이터가 많으므로 many=True 넣어주기
        return Response(serializer.data, status=status.HTTP_200_OK)

			
    @swagger_auto_schema(
            operation_id='게시글 생성',
            operation_description='게시글을 생성합니다.',
            request_body=PostSerializer,
            responses={201: PostSerializer}
        )
    def post(self, request):
        title = request.data.get('title')
        content = request.data.get('content')
        if not title or not content:
            return Response({"detail": "[title, content] fields missing."}, status=status.HTTP_400_BAD_REQUEST)
        post = Post.objects.create(title=title, content=content)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
	
class PostDetailView(APIView):
    @swagger_auto_schema(
            operation_id='게시글 상세 조회',
            operation_description='게시글 1개의 상세 정보를 조회합니다.',
            responses={200: PostSerializer}
        )
    def get(self, request, post_id): #url에서 id 변수 받아와서 쓸거라고 명시
        try: #게시물을 찾을 수 있는지 분기처리
            post = Post.objects.get(id=post_id)
        except:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
            operation_id='게시글 업데이트',
            operation_description= '게시글 1개의 제목 및 내용을 업데이트합니다.',
            request_body=PostSerializer,
            responses={200: PostSerializer}
    )
    def put(self, request, post_id): #과제 api
        try:
            post = Post.objects.get(id = post_id)
        except:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        title = request.data.get('title')
        content = request.data.get('content')
        if not title or not content:
            return Response({"detail": "[title, content] fields missing."}, status=status.HTTP_400_BAD_REQUEST)
        post = Post.objects.update(title=title, content=content)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_UPDATED)
		
    @swagger_auto_schema(
            operation_id='게시글 삭제',
            operation_description='게시글을 삭제합니다.',
            responses={204: 'No Content', 404: 'Not Found'}
        )
    def delete(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
        except:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        post.delete() #장고 모델 클래스 내에서 제공해주는 ORM 메소드 
        return Response(status=status.HTTP_204_NO_CONTENT)
