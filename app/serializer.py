from rest_framework.serializers import (
    ModelSerializer
)

from rest_framework import (
    serializers
)

from .models import(
    contactform,
    visitlog,
    transaction,
    appkeyword,
    app,
    app_screenshot,
    appkeyword_screenshot,
    campaign,
    campaign_review,
    devices,
    reviewer_account
)

class contactformSerializer(ModelSerializer):
    class Meta:
        model = contactform
        fields = "__all__"

class visitlogSerializer(ModelSerializer):
    class Meta:
        model = visitlog
        fields = "__all__"

class appkeywordSerializer(ModelSerializer):
    class Meta:
        model = appkeyword
        fields = "__all__"

class appSerializer(ModelSerializer):
    class Meta:
        model = app
        fields = "__all__"

class app_screenshotSerializer(ModelSerializer):
    class Meta:
        model = app_screenshot
        fields = "__all__"

class appkeyword_screenshotSerializer(ModelSerializer):
    class Meta:
        model = appkeyword_screenshot
        fields = "__all__"


class campaignSerializer(ModelSerializer):
    class Meta:
        model = campaign
        fields = "__all__"

class campaign_reviewSerializer(ModelSerializer):
    class Meta:
        model = campaign_review
        fields = "__all__"

class devicesSerializer(ModelSerializer):
    class Meta:
        model = devices
        fields = "__all__"

class reviewer_accountSerializer(ModelSerializer):
    class Meta:
        model = reviewer_account
        fields = "__all__" 




