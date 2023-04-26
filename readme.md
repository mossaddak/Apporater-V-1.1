# Sing Up
post => http://127.0.0.1:8000/api/account/sing-up/
=) passing data fields: email, profile_picture, username, password, first_name, last_name

# Account Verification
post => http://127.0.0.1:8000/api/account/verify/
=) passing data fields: otp

# Login
post => http://127.0.0.1:8000/api/account/login/
=) passing data fields: username, password

# Profile
get, patch => http://127.0.0.1:8000/api/account/profile/
=) passing data fields: username, password, first_name, last_name, email, profile_picture
note: For patching no need to pass anything, authenticated users can change their information through the field just need to hit the link with the field information wants to change.

# Contact Form
post = > http://127.0.0.1:8000/api/app/contact/
=) passing data fields: fullname, email, message

# Visiting Blog
get = > http://127.0.0.1:8000/api/app/visitingblog/

# App Keyword
get = > http://127.0.0.1:8000/api/app/appkeyword/

# App
get = > http://127.0.0.1:8000/api/app/app/

# App Screenshot
get = > http://127.0.0.1:8000/api/app/app-screenshot/

# Appkeyword Screenshot
get = > http://127.0.0.1:8000/api/app/appkeyword-screenshot/

# Campaing
get = > http://127.0.0.1:8000/api/app/campaign/

# Campaing Review
get = > http://127.0.0.1:8000/api/app/campaign-review/

# Devices
get = > http://127.0.0.1:8000/api/app/device/

# Reviewer Account
get = > http://127.0.0.1:8000/api/app/reviewer-account/

