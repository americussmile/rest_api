# generic
from rest_framework import generics, mixins
from postings.models import BlogPost
from  .serializer import  BlogPostSerializer
from django.db.models import Q
from .permission import IsOwnerOrReadOnly

class BlogPostAPIView(generics.ListAPIView, mixins.CreateModelMixin):
    lookup_field = 'pk'
    serializer_class =  BlogPostSerializer
    # permission_classes = [] # all thing are allowed, no authentication

    def get_queryset(self):
        qs = BlogPost.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(Q(title__icontains=query)|Q(content__icontains=query)).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.patch(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}


# change the RetrieveUpdate will change the API console
class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class =  BlogPostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return BlogPost.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}
    # def get_object(self):
    #     pk = self.kwargs.get('pk')
