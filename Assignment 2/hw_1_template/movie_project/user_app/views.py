from django.shortcuts import render
from django.views import View

# Create your views here.

class UserHome(View):
    def get(self,request):
        return render(request,'user_app/user_home.html')

class MovieListView(View):
    def get(self,request):
        return render(request,'user_app/movie_list.html')
    
class MovieDetailView(View):
    def get(self,request):
        return render(request,'user_app/movie_detail.html')
    
class MovieUpdateView(View):
    def get(self,request):
        return render(request,'user_app/movie_update.html')
    
    def post(self,request):
        return render(request,'user_app/movie_list.html')   
    
class MovieAddView(View):
    def get(self,request):
        return render(request,'user_app/movie_add.html')
    
    def post(self,request):
        return render(request,'user_app/movie_list.html')    
    
    
class MovieDeleteView(View):
    def get(self,request):
        return render(request,'user_app/movie_delete.html')
    
    def post(self,request):
        return render(request,'user_app/movie_list.html')
    
class MovieLogin(View):
    def get(self,request):
        return render(request,'user_app/login.html')
