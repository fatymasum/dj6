from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



from django.contrib import admin
from .models import BlogPost

admin.site.register(BlogPost)

from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'



from rest_framework import viewsets
from .models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.views import BlogPostViewSet

router = DefaultRouter()
router.register(r'posts', BlogPostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]


