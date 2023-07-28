# To run backend - 
```
cd backend
env\Scripts\activate.bat
cd auction 
python manage.py runserver
```

# To run frontend -
```
cd frontend
npm run dev
```

# for developers -
pip freeze > requirements.txt

superuser - admin

email - admin@gmail.com

password - admin@123


## user generation tips -
username - jignesh, harman
email - jignesh@gmail.com, harman@gmail.com
password - ignesh@1234, arman@1234 # drop 1st letter
first_name - jignesh, harman
last_name - patil, singh
usertype - Not staff, staff

## admin/Superuser account credentials -
Username: admin2
Email: admin2@gmail.com
Password: dmin2@1234
Password (again): dmin2@1234
Superuser created successfully.

## to start celery worker -
```
celery -A auction.celery worker --loglevel=info (do this inside outermost auction folder => celery -A myproject.celery worker --loglevel=info)
celery -A celery worker --loglevel=info 
```

Payment link 
```
https://rzp.io/l/rxLxyVp
```

## ERRORS :
if "django.db.utils.OperationalError: no such table: main_auctionmodel" this error comes then
python manage.py migrate --run-syncdb  => Creates tables for apps without migrations
python manage.py makemigrations main => specify name
python manage.py migrate main => specify name

## STAR THIS REPOSITORY IF LOVED OUR EFFORTS!

## Contributors 😎 <p align="center"> 
Backend - <a href="https://github.com/KedarKK1/auction_website_WTL/graphs/contributors"> <img src="https://contrib.rocks/image?repo=KedarKK1/auction_website_WTL" /> </a> 

<br />
Frontend - <a href="https://github.com/KedarKK1/auction_frontend_WTL/graphs/contributors"> <img src="https://contrib.rocks/image?repo=KedarKK1/auction_frontend_WTL" /> </a>  
</p>

# Event Screenshots
<img src="./Screenshots/ss1.PNG" alt="home_page" />
<img src="./Screenshots/ss2.PNG" alt="auctions_list_page" />
<img src="./Screenshots/ss3.PNG" alt="auction_page" />
<img src="./Screenshots/ss4.PNG" alt="auction_page2" />
<!-- <img src="./Screenshots/ss5.PNG" alt="login_page" /> -->
<img src="./Screenshots/ss15.PNG" alt="razorpay_page" />
<img src="./Screenshots/ss16.PNG" alt="djoser_page" width="230px" height="4000px" />
<img src="./Screenshots/ss17.PNG" alt="djoser_page_2" width="190px" height="2000px" />
<img src="./Screenshots/ss18.PNG" alt="djoser_page_3" width="190px" height="2000px" />
<img src="./Screenshots/ss19.PNG" alt="djoser_page_4" width="190px" height="2000px" />
<img src="./Screenshots/ss20.PNG" alt="signUp_api_page" />
<img src="./Screenshots/ss21.PNG" alt="signIn_api_token_generation_page" />
<img src="./Screenshots/ss27.PNG" alt="token_generation_page" />
<img src="./Screenshots/ss22.PNG" alt="all_routes_page" />
<img src="./Screenshots/ss23.PNG" alt="auction_api_page" />
<img src="./Screenshots/ss24.PNG" alt="auction_image_page" />
<img src="./Screenshots/ss25.PNG" alt="authentication_error_page" />
<img src="./Screenshots/ss26.PNG" alt="authorization_error_page" />
<img src="./Screenshots/ss28.PNG" alt="all_auctions_list_page" />
<img src="./Screenshots/ss29.PNG" alt="new_auctions_page" />
<img src="./Screenshots/ss5.PNG" alt="about_us_page" />
<img src="./Screenshots/ss6.PNG" alt="our_team_page" />
<img src="./Screenshots/ss7.PNG" alt="login_page" />
<img src="./Screenshots/ss8.PNG" alt="new_account_page" />
<img src="./Screenshots/ss9.PNG" alt="all_db_model_page" />
<img src="./Screenshots/ss10.PNG" alt="auction_model_list_page" />
<img src="./Screenshots/ss11.PNG" alt="auction_model_page" />
<img src="./Screenshots/ss13.PNG" alt="auction_code_page" />