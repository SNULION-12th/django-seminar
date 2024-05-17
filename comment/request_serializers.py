from rest_framework import serializers
from post.serializers import PostSerializer
from account.request_serializers import SignInRequestSerializer


class CommentCreateRequestSerializer(serializers.Serializer):
    author = SignInRequestSerializer()
    post = serializers.IntegerField()
    content = serializers.CharField()

class CommentListRequestSerializer(serializers.Serializer):
    post = serializers.IntegerField()
    
class CommentUpdateRequestSerializer(serializers.Serializer):
    data = CommentCreateRequestSerializer()
    comment_id = serializers.CharField()
    
class CommentDeleteRequestSerializer(serializers.Serializer):
    author = SignInRequestSerializer()
    comment_id =serializers.CharField()
    