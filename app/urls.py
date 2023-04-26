from django.contrib import admin
from django.urls import path, include
from .views import(
    ContactFromView,
    VisitlogView,
    #ContactFromDetailsView,
    #VisitlogDetailsView,
    AppkeywordView,
    #AppkeywordDetailsView,
    AppView,
    #AppDetailsView,
    AppScreenshotView,
    AppkeywordScreenshotView,
    CampaignView,
    CampaignReviewView,
    DeviceView,
    ReviewerAccount

)

urlpatterns = [
    #path('app/contact/', admin.site.urls)
    path('app/contact/', ContactFromView.as_view()),
    #path('app/contact/<int:pk>/', ContactFromDetailsView.as_view()),
    path('app/visitingblog/', VisitlogView.as_view()),
    #path('app/visitingblog/<int:pk>/', VisitlogDetailsView.as_view()),
    path('app/appkeyword/', AppkeywordView.as_view()),
    #path('app/appkeyword/<int:pk>/', AppkeywordDetailsView.as_view()),
    path('app/app/', AppView.as_view()),
    #path('app/app/<int:pk>/', AppDetailsView.as_view()),
    path('app/app-screenshot/', AppScreenshotView.as_view()),
    path('app/appkeyword-screenshot/', AppkeywordScreenshotView.as_view()),
    path('app/campaign/', CampaignView.as_view()),
    path('app/campaign-review/', CampaignReviewView.as_view()),
    path('app/device/', DeviceView.as_view()),
    path('app/reviewer-account/', ReviewerAccount.as_view()),
]
