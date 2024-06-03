from django.shortcuts import redirect, render
from django.views import View
from uta_user.models import UtaUser
from uta_user.forms import UserForm
from django.contrib.auth.mixins import LoginRequiredMixin
import requests
import xmltodict
from uta_user.models import FaqMain,Faq, Comment



# Create your views here.

class RouteListView(LoginRequiredMixin,View):
    def get(self,request):
        uta_user = UtaUser.objects.get(auth_user=request.user)
        my_routes = uta_user.my_routes.all()
        context = {'uta_user': uta_user,
            'my_routes':my_routes}
        
        return render(request=request,template_name='uta_user/my_routes_list.html',context=context)

class RouteMapView(LoginRequiredMixin,View):

    UTA_TOKEN = 'UYDFQ0B0AK7' # this is not best practice for production systems and secrets

    def get(self,request):

        uta_user = UtaUser.objects.get(auth_user=request.user)
        my_routes = uta_user.my_routes.all()
        locations = []
        for route in my_routes:
            print(route)
            locations.extend(get_uta(self.UTA_TOKEN,route.route_number))
        
        context = {'uta_user': uta_user,
                   'my_routes':my_routes,
                   'locations':locations}

        return render(request=request,template_name='uta_user/route_map.html',context=context)
    
class HomeView(LoginRequiredMixin,View):

    UTA_TOKEN = 'UYDFQ0B0AK7' # this is not best practice for production systems and secrets

    def get(self,request):
        uta_user = UtaUser.objects.get(auth_user=request.user)
        my_routes = uta_user.my_routes.all()
        locations = []
        for route in my_routes:
            print(route)
            locations.extend(get_uta(self.UTA_TOKEN,route.route_number))
        
        context = {'uta_user': uta_user,
                   'my_routes':my_routes,
                   'locations':locations}

        return render(request=request,template_name='uta_user/index.html',context=context)
    
class UserCreateEdit(LoginRequiredMixin,View):
    def post(self,request,user_id=None):

        if user_id:
            uta_user = UtaUser.objects.get(pk=user_id)
        else:
            uta_user = UtaUser.objects.get(auth_user=request.user)

        form = UserForm(request.POST,instance=uta_user)
        if form.is_valid():
            uta_user = form.save()

        return redirect('my_routes_list')

    def get(self,request):

        uta_user = UtaUser.objects.get(auth_user=request.user)
        form = UserForm(instance=uta_user)
        
        return render(request = request,template_name = 'uta_user/user_edit.html',context = {'uta_user':uta_user,'form':form})

class ContactView(LoginRequiredMixin,View):

    def get(self,request):
        uta_user = UtaUser.objects.get(auth_user=request.user)
        
        context = {'uta_user': uta_user}

        return render(request=request,template_name='uta_user/contact.html',context=context)
    
class FaqView(View):

    def get(self,request):
        faq_main = FaqMain.objects.get(active=True)
        my_hello = 'hello world!'
        context = {'faq_main':faq_main,'hi':my_hello}
        return render(request=request,template_name='uta_user/faq.html',context=context)
 
# This function calls the UTA api for a given route. Returns a list of dictionaries of lat/lon/name
def get_uta(uta_secret,route_number):

    print(uta_secret,route_number)
    url = f'http://api.rideuta.com/SIRI/SIRI.svc/VehicleMonitor/ByRoute?route={route_number}&onwardcalls=true&usertoken={uta_secret}'
    response = requests.get(url)

    xml_dict = xmltodict.parse(response.text)

    locations = xml_dict['Siri']['VehicleMonitoringDelivery']['VehicleActivity']['MonitoredVehicleJourney']

    lat_long = []

    print(locations)

    for location in locations:
        location_dict = {}
        location_dict['lat'] = location['VehicleLocation']['Latitude']
        location_dict['lon'] = location['VehicleLocation']['Longitude']
        location_dict['name'] = location['PublishedLineName']

        lat_long.append(location_dict)

    return(lat_long)


class CommentList(View):
    def get(self,request):
        comments = Comment.objects.all()

        context = {'comments':comments}

        return render(request=request,
                      template_name='uta_user/comment_list.html',
                      context=context)
    
