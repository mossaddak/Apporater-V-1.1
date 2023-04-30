# <a href="https://apporaterapiv11devbymossaddak.pythonanywhere.com/">Live Link

# Sing Up

post => http://127.0.0.1:8000/api/account/sing-up/

=) passing data fields: 

    {
        "username": "mossadak",
        "first_name": "mossaddak",
        "last_name": "sium",
        "email": "10000mossaddak@gmail.com"
    }

# Total User

get => http://127.0.0.1:8000/api/account/total_user/

# Login

post => http://127.0.0.1:8000/api/account/login/

=) passing data fields:


    {
        "username":"mossadak",
        "password":"1234"
    }


# Profile
get, patch => http://127.0.0.1:8000/api/account/profile/

=) passing data fields: username, password, first_name, last_name, email

note: Here username field is mandetory

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

<b>Note:</b> you also wiil get the average rating from here.

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




