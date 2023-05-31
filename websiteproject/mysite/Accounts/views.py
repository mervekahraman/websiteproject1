from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
#from django.contrib.auth.decorators import User


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('account')
        else:
            return render(request, 'login.html', {'error': 'Invalid login credentials'})
    else:
        return render(request, 'login.html')


user1 = User.objects.create_user("Nick", "nickjanckson1978@outlook.com", "nickpassword")
user2 = User.objects.create_user("Amy", "wrightamy@gmail.com", "amypassword")
user3 = User.objects.create_user("Carrie", "carriewalker@outlook.com", "carriepassword")

user1.last_name="JACKSON"
user2.last_name="WRIGHT"
user3.last_name="WALKER"

user1.save()
user2.save()
user3.save()
