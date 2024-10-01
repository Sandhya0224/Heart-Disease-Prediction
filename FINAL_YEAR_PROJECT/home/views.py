from django.shortcuts import render,redirect
import joblib
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import UserCreationform,Authenticationform
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

model = joblib.load('static/LogisticRegression')

# Create your views here.
def index(request):
    # return HttpResponse("This is index page")
    return render(request, 'index.html')

def userlogin(request):
    # return HttpResponse("This is login page")
    form = Authenticationform()
    context = {'form':form}
    if request.method == 'POST':
        form = Authenticationform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect('prediction')
    return render(request, 'login.html',context)

def registration(request):
    # return HttpResponse("This is registration page")
    form = UserCreationform()
    context = {'form':form}
    if request.method == 'POST':
        form = UserCreationform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'registration.html',context)

def prediction(request):
    if request.user.is_authenticated:
    # return HttpResponse("This is prediction page")
        if request.method == "POST":
            age = int(request.POST.get('age'))
            sex = int(request.POST.get('sex'))
            chestPainTypes = int(request.POST.get('chestPainTypes'))
            restingBloodPressure = int(request.POST.get('restingBloodPressure'))
            serumCholestrol = int(request.POST.get('serumCholestrol'))
            fastingBloodSugar = int(request.POST.get('fastingBloodSugar'))
            restingElectrocardiographicResults = int(request.POST.get('restingElectrocardiographicResults'))
            maximumHeartRateAchieved = int(request.POST.get('maximumHeartRateAchieved'))
            exerciseInducedAngina = int(request.POST.get('exerciseInducedAngina'))
            depressionInduced = float(request.POST.get('depressionInduced'))
            slope = int(request.POST.get('slope'))
            flourosopy = int(request.POST.get('flourosopy'))
            defectOrNot = int(request.POST.get('defectOrNot'))

            pred = model.predict([[age,sex,chestPainTypes,restingBloodPressure,serumCholestrol,fastingBloodSugar,
                                restingElectrocardiographicResults,maximumHeartRateAchieved,exerciseInducedAngina,
                                depressionInduced,slope,flourosopy,defectOrNot]])
            print(pred)

            output = {
                "output" : pred
            }
            
            return render(request, 'prediction.html',output)

        else:
            return render(request, 'prediction.html')
    return redirect('login')


def userlogout(request):
    logout(request)
    return redirect('login')


