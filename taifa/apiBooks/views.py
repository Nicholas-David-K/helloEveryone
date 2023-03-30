from .serializers import EbookSerializer, ReviewSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework import permissions
from rest_framework.exceptions import ValidationError


from taifa.models import Ebook, Review
from .permissions import IsAdminUserOrReadOnly, IsReviewAuthorOrReadOnly
from .pagination import SmallSetPagination

# class EbookListCreateAPIView(APIView):

#     def get(self, request):
#         ebooks = Ebook.objects.all()
#         serializer = EbookSerializer(ebooks, many=True)
#         return Response(serializer.data)


#     def post(self, request):
#         serializer = EbookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# * CONCRETE VIEW CLASSES
class EbookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ebook.objects.all().order_by("-id")
    serializer_class = EbookSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = SmallSetPagination


class EbookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class ReviewListCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get("ebook_pk")
        ebook = get_object_or_404(Ebook, pk=ebook_pk)

        review_author = self.request.user

        review_qs = Review.objects.filter(ebook=ebook, review_author=review_author)
        
        if review_qs.exists():
            raise ValidationError({"message": "You have already reviewed this E-book."})

        serializer.save(ebook=ebook, review_author=review_author)


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadOnly]


# #* GENERIC API VIEW AND MIXINS
# class EbookListCreateAPIView(mixins.ListModelMixin, mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Ebook.objects.all()
#     serializer_class = EbookSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
