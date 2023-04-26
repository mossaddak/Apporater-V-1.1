from django.contrib import admin
from .models import(
    contactform,
    visitlog,
    transaction,
    appkeyword,
    app,
    app_screenshot,
    campaign,
    campaign_review,
    devices,
    reviewer_account,
    appkeyword_screenshot
)

# Register your models here.
admin.site.register(contactform)
admin.site.register(visitlog)
admin.site.register(transaction)
admin.site.register(appkeyword)
admin.site.register(app)
admin.site.register(app_screenshot)
admin.site.register(campaign)
admin.site.register(campaign_review)
admin.site.register(devices)
admin.site.register(reviewer_account) 
admin.site.register(appkeyword_screenshot) 

