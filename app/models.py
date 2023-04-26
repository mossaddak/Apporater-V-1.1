from django.db import models

# Create your models here.
class contactform(models.Model):
    fullname = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)         
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pk}.{self.fullname}"

class visitlog(models.Model):
    email = models.TextField(blank=True, null=True)
    utm_medium = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    utm_campaign = models.TextField(blank=True, null=True)
    discount =  models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.pk}.{self.email}"

class transaction(models.Model):
    formid = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.TextField(blank=True, null=True)
    stripe_session_id = models.TextField(blank=True, null=True)


class appkeyword(models.Model):
    keyword = models.TextField(blank=True, null=True)
    form_id = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.pk}.{self.keyword}"

class app(models.Model):
    platform = models.TextField(blank=True, null=True)
    package_id = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    app_title = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.pk}.{self.platform}"

class app_screenshot(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    screenshot_source = models.TextField(blank=True, null=True)
    app_id = models.TextField(blank=True, null=True)
    installs = models.TextField(blank=True, null=True)
    minInstalls = models.TextField(blank=True, null=True)
    reviews = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    score = models.TextField(blank=True, null=True)
    shortdescription = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    jsonObj = models.TextField(blank=True, null=True)
    developer_email = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.pk}.{self.title}"

class appkeyword_screenshot(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    appkeyword_id = models.TextField(blank=True, null=True)  #foreign key to id of appkeyord
    market = models.TextField(blank=True, null=True) #which country
    ranking = models.TextField(blank=True, null=True) #keyword ranking of the app in the market 
    def __str__(self):
        return f"{self.pk}.{self.appkeyword_id}"

class campaign(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    form_id = models.TextField(blank=True, null=True)  
    transaction_id = models.TextField(blank=True, null=True)  
    user_id = models.TextField(blank=True, null=True)  
    status = models.TextField(blank=True, null=True)  
    package_id = models.TextField(blank=True, null=True)  
    installs_count = models.TextField(blank=True, null=True)  
    reviews_count = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"{self.pk}.{self.form_id}"
 
class campaign_review(models.Model):
    created_at = models.DateTimeField(null=True)
    campaign_id  = models.TextField(blank=True, null=True)  
    review_text  = models.TextField(blank=True, null=True)  
    given_by_user_id  = models.TextField(blank=True, null=True)  
    given_on_device_id  = models.TextField(blank=True, null=True)  
    app_id = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"{self.pk}.{self.campaign_id}"


class devices(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    device_name = models.TextField(blank=True, null=True)  
    device_imei = models.TextField(blank=True, null=True)  
    device_platform = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"{self.pk}.{self.device_name}"


class reviewer_account(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.TextField(blank=True, null=True)  
    last_name = models.TextField(blank=True, null=True)  
    email = models.TextField(blank=True, null=True)  
    platform = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.pk}.{self.first_name}"

