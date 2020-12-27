from django.shortcuts import render
from rest_framework import viewsets, status
# Create your views here.
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.models import Movie, Rating
from api.serializers import MovieSerializers, RatingSerializers, UserSerializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    authentication_classes = (TokenAuthentication,)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['POST'])
    def rate_movie(self, request, pk=None):
        if 'stars' in request.data:
            movie = Movie.objects.get(id=pk)
            user = request.user
            print('user', user)

            stars = request.data['stars']
            try:
                rating = Rating.objects.get(user=user.id, movie=movie.id)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializers(rating, many=False)
                response = {'message': 'Rating Updated', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)

            except:
                Rating.objects.create(user=user, movie=movie, stars=stars)
                serializer = RatingSerializers(rating, many=False)
                response = {'message': 'Rating created', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message': 'Data need to be provided'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializers
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
