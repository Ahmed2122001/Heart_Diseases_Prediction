from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile
import re
from django.contrib import auth
# Create your views here.

def signUp(request):
    if request.method == 'POST' and 'btnsignup' in request.POST:
        username = None
        age = None
        email = None
        gender = None
        phone = None
        city = None
        password = None
        confirm_password = None
        is_add = None
        if 'username' in request.POST: username = request.POST.get('username')
        else: messages.error(request, 'Error in User Name')
        if 'age' in request.POST: age = request.POST.get('age')
        else: messages.error(request, 'Error in Age')
        if 'email' in request.POST: email = request.POST.get('email')
        else: messages.error(request, 'Error in Email')
        if 'gender' in request.POST: gender = request.POST.get('gender')
        else: messages.error(request, 'Error in Gender')
        if 'phone' in request.POST: phone = request.POST.get('phone')
        else: messages.error(request, 'Error in Phon Number')
        if 'city' in request.POST: city = request.POST.get('city')
        else: messages.error(request, 'Error in City')
        if 'password' in request.POST: password = request.POST.get('password')
        else: messages.error(request, 'Error in Password')
        if 'confirm_password' in request.POST: confirm_password = request.POST.get('confirm_password')
        else: messages.error(request, 'Error in Confirm Password')

        if username and age and email and gender and phone and city and password and confirm_password:
            
            # Check if username is taken
            if User.objects.filter(username=username).exists():
                messages.error(request, 'This username is taken')
            else:
                # Check if email is taken
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'This email is taken')
                else:
                    # Check if email is Valid
                    patt = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
                    if re.match(patt, email):
                        if len(username) < 3:
                             messages.error(request, 'Username must be at least 3 characters long.')
                        else:
                            # Check if Phone is Valid
                            patt1 = "^\d+$"
                            if re.match(patt1,phone):
                                if len(password) < 6:
                                    messages.error(request, 'Password must be at least 6 characters long.')
                                else:
                                    if password == confirm_password:
                                        # add user
                                        user = User.objects.create_user(username = username, email = email, password = password )
                                        user.save()

                                        # add user profile
                                        userprofile = UserProfile(user = user, age = age, gender = gender, phone = phone, city = city)
                                        userprofile.save()

                                        # Clear fields
                                        username = ''
                                        age = ''
                                        email = ''
                                        gender = ''
                                        phone = ''
                                        city = ''
                                        password = ''
                                        confirm_password = ''

                                        # Success Message
                                        messages.success(request, 'Your account is created')

                                        is_add = True
                                    else:
                                        messages.error(request, 'Passwords do not match')
                            else:
                                messages.error(request, 'Phone number must contain only digits.')
                    else:
                        messages.error(request, 'Invalid email')
        else:
            messages.error(request, 'Check empty fields')
        return render(request , 'accounts/signUp.html', {
            'username' : username,
            'age' : age,
            'email': email,
            'gender' : gender,
            'phone' : phone,
            'city' : city,
            'password' : password,
            'confirm_password' : confirm_password,
            'is_added' : is_add
        })
    else:
        return render(request , 'accounts/signUp.html')


def Login(request):
    if request.method == 'POST' and 'btnlogin' in request.POST :
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
        else:
            messages.error(request, 'username or Password invalid')
        return redirect('Login')
    else:
        return render(request , 'accounts/Login.html')

def profile(request):
    context = None
    if request.user is not None:
        if not request.user.is_anonymous:
            user = request.user
            profile = UserProfile.objects.get(user=user)
            if request.method == 'POST' and 'btnsave' in request.POST:
                user_name = request.POST.get('user_name')
                age = request.POST.get('age')
                gender = request.POST.get('gender')
                city = request.POST.get('city')
                phone = request.POST.get('phone')
                email = request.POST.get('email')
                
                if len(user_name) < 3:
                    messages.error(request, 'Username must be at least 3 characters long.')
                else:
                    patt = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
                    if re.match(patt, email):
                        patt1 = "^\d+$"
                        if re.match(patt1,phone):
                            user.username = user_name
                            user.email = email
                            profile.age = age
                            profile.gender = gender
                            profile.city = city
                            profile.phone = phone
                            user.save()
                            profile.save()
                        else:
                            messages.error(request, 'Phone number must contain only digits.')
                    else:
                        messages.error(request, 'Invalid email')
                
            context = {
                'user' : user,
                'profile': profile
            }
        return render(request , 'accounts/profile.html',context)
    
    else:
        return redirect('profile')

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('index')