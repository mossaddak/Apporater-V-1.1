from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializer import(
    contactformSerializer,
    visitlogSerializer,
    appkeywordSerializer,
    appSerializer,
    app_screenshotSerializer,
    appkeyword_screenshotSerializer,
    campaignSerializer,
    campaign_reviewSerializer,
    devicesSerializer,
    reviewer_accountSerializer
)
from .models import(
    contactform,
    visitlog,
    appkeyword,
    app,
    app_screenshot,
    appkeyword_screenshot,
    campaign,
    campaign_review,
    devices,
    reviewer_account
)
from rest_framework.permissions import (
    IsAuthenticated
)
from rest_framework_simplejwt.authentication import (
    JWTAuthentication
)
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
    BasePermission,
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
)
from django.db.models.functions import TruncDate
from datetime import timedelta
from django.utils import timezone
from django.db.models import Count
from django.db.models import Avg


#permissions============================>
class AdminAccessOnlyOtherCanSee(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        
        if request.method in['GET','POST','PUT','DELETE'] and user.is_superuser:
            return True
        return False

# contact start ======================================================>
class ContactFromView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def post(self, request):
        serializer = contactformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    'data': serializer.data,
                    'message': "Thank you for contacting us."
                },
                status=status.HTTP_201_CREATED
            )
        else:
            errors = serializer.errors
            error_list = []
            for field, error in errors.items():
                error_list.append(f"{field.capitalize()}: {error[0]}")
            message = "\n".join(error_list)
            return Response(
                {
                    'data': errors,
                    'message': f"The following errors occurred:\n{message}"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
    
    def get(self, request):
        if request.user.is_authenticated and request.user.is_superuser:
            all_contact = contactform.objects.all()
            serializer = contactformSerializer(all_contact, many=True)

            return Response(
                    {
                        'data': serializer.data,
                        'message': "Data fetch"
                    },
                    status=status.HTTP_200_OK
                )
        else:
            return Response(
                    {
                        'message': "You don't have permission for this"
                    },
                    status=status.HTTP_403_FORBIDDEN
                )
#contact end ==================!        

# Visitlog start ======================================================>
class VisitlogView(APIView):

    def get(self, request):
        visiting_blogs = visitlog.objects.all()
        serializer = visitlogSerializer(visiting_blogs, many=True)

        return Response(
                {
                    'data': serializer.data,
                    'message': "Data fetch"
                },
                status=status.HTTP_302_FOUND
            )
#contact end ==================!

#Appkeyword start ======================================================>
class AppkeywordView(APIView):
    
    def get(self, request):
        
        visiting_blogs = appkeyword.objects.all()
        serializer = appkeywordSerializer(visiting_blogs, many=True)

        return Response(
            {
                'data': serializer.data,
                'message': "Data fetch"
            },
            status=status.HTTP_302_FOUND
        )
#Appkeyword end ==================!

#app start ======================================================>
class AppView(APIView):
    
    def get(self, request):
        visiting_blogs = app.objects.all()
        serializer = appSerializer(visiting_blogs, many=True)

        return Response(
            {
                'data': serializer.data,
                'message': "Data fetch"
            },
            status=status.HTTP_302_FOUND
        )
#app end ==================!

#app_screenshot start ======================================================>
class AppScreenshotView(APIView):
    def get(self, request):
        all_data = app_screenshot.objects.all()
        serializer = app_screenshotSerializer(all_data, many=True)
        average_rating = all_data.aggregate(Avg('ratings'))


        return Response(
            {
                'data': serializer.data,
                'total':all_data.count(),
                'average_rating': average_rating['ratings__avg'],
                'message': "Data fetch"
            },
            status=status.HTTP_302_FOUND
        )
#app_screenshot end ==================!


class AppkeywordScreenshotView(APIView):
    def get(self, request):
        all_data = appkeyword_screenshot.objects.all()
        serializer = appkeyword_screenshotSerializer(all_data, many=True)
        today = timezone.now().date()
        five_days_ago = today - timedelta(days=5)
        last_five_days_data = appkeyword_screenshot.objects.filter(created_at__gte=five_days_ago + timedelta(days=1)).annotate(day=TruncDate('created_at')).values('day').annotate(total_reviews=Count('id'))
 
        return Response(
            {
                'overall_reviews':all_data.count(),
                'last_five_days_review':last_five_days_data,
                'message': "Data fetch"
            },
            status=status.HTTP_302_FOUND
        )

class CampaignView(APIView):
    def get(self, request):
        all_data = campaign.objects.all()
        serializer = campaignSerializer(all_data, many=True)

        return Response(
            {
                'data': serializer.data,
                'message': "Data fetch"
            },
            status=status.HTTP_302_FOUND
        )
    
class CampaignReviewView(APIView):
    def get(self, request):
        all_data = campaign_review.objects.all()
        serializer = campaign_reviewSerializer(all_data, many=True)

        today = timezone.now().date()
        five_days_ago = today - timedelta(days=5)
        
        last_five_days_data = campaign_review.objects.filter(created_at__gte=five_days_ago + timedelta(days=1)).annotate(day=TruncDate('created_at')).values('day').annotate(total_reviews=Count('id'))
        
        
        return Response(
            {
                'overall_reviews':all_data.count(),
                'last_five_days_review':last_five_days_data,
                'message': "Data fetch"
            },
            status=status.HTTP_302_FOUND 
        )
     
class DeviceView(APIView):
    def get(self, request):
        all_data = devices.objects.all()
        serializer = devicesSerializer(all_data, many=True)

        return Response(
            {
                'data': serializer.data,
                'message': "Data fetch"
            },
            status=status.HTTP_302_FOUND
        )
    
class ReviewerAccount(APIView):
    def get(self, request):
        all_data = reviewer_account.objects.all()
        serializer = reviewer_accountSerializer(all_data, many=True)

        return Response(
            {
                'data': serializer.data,
                'message': "Data fetch"
            },
            status=status.HTTP_302_FOUND
        )
 


