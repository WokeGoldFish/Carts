from rest_framework.permissions import IsAuthenticated


from rest_framework.response import Response
from rest_framework.decorators import api_view

from ecom.models import Post
from .serializers import PostSerializer, RegistrationSerializer
from api import serializers

from rest_framework.authtoken.models import Token


# Create your views here.

@api_view (['Get'])
def index(request):
    return Response({'hello' : 'there'})

@api_view (['Get'])
def getPosts(request):
    posts = Post.objects.all()
    serializer  = PostSerializer(posts, many = True)
    return Response({
        'status' : 'ok',
        'posts': serializer.data
    })

@api_view(['Get'])
def getPost(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        serializer  = PostSerializer(post, many = False)
        return Response({
        'status' : 'ok',
        'post': serializer.data
        })
    except:
        return Response({
        'status' : 'not ok',
        'post': serializer.data
    })

@api_view(['POST'])
def createPost(request):
    serializer = PostSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['POST'])
def updatePost(request, post_id):
    post = Post.objects.get(id =post_id)
    serializer = PostSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
def deletePost(request, post_id):
    post = Post.objects.get(id =post_id)
    post.delete
    return Response('post go bye bye')


@api_view(['POST'])
def apiLogin(request):
    serializer = RegistrationSerializer(data=request.data)
    return Response('got data')


@api_view(['POST'])
def apiSignUp(request):
    serializer = RegistrationSerializer(data=request.data)
    if serializer.is_valid():
        account = serializer.save()
        token = Token.objects.get(user=account).key
        data = {
            'status': 'ok',
            'email' : account.email,
            'username': account.username,
            'token': token
        }
        return Response(data)
    return Response(serializer.errors)