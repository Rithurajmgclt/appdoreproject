from django.shortcuts import render,HttpResponse,redirect
from app.models import Registration,Title
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
import sys
from django.http import JsonResponse
from django.core import serializers
import json
from django.forms.models import model_to_dict
import simplejson

from app.models import Registration
 


# Create your views here.
def index(request):
# registration'................................................
    users = Registration.objects.all()
    title = Title.objects.all()
    print(users)
    return render(request,'app/registration.html',{'user':users,'titles':title})



def add_points(request):

    if request.method =="POST":
        first_name =  request.POST['firstname']
        last_name =  request.POST['lastname']
        title = request.POST['title']
        parent_id = 0
        parent_id_check = request.POST.get('select_parent')
        user2 =Registration.objects.values_list('parent_id',flat=True)
        if parent_id_check ==''  and title =='CEO':
            parent_id = 0
        if parent_id_check == '' and title !='CEO':
            messages.warning(request, 'select parent ')
            return redirect('indexpage')
        if parent_id_check !='' and title !='CEO':
            parent_id = parent_id_check 
            user3 = Registration.objects.get(reg_id=parent_id_check)
            present_point = user3.points
            present_point += 1
            user3.points = present_point
            user3.save()
            if user3.parent_id !=0:
                idp=user3.parent_id
                user4 = Registration.objects.get(reg_id=idp)
                present_point = user4.points
                present_point += 0.5
                user4.points = present_point
                user4.save()
        if title=='CEO' and 0 in user2 :
            messages.warning(request, 'CEO already assigned')
            return redirect('indexpage')
        user = Registration.objects.create(first_name=first_name, last_name=last_name, title=title, parent_id=parent_id, points=0)
    return redirect('tree_view') 

def tree_view(request):
    return render(request,'app/tree_view.html')


class Create_tree(APIView):

    def get(self, request, format=None):
        parentid_first = Registration.objects.get(parent_id=0).reg_id
        custom_data = {'id': self.get_Top_parent().reg_id,
                        'name':self.get_Top_parent().first_name,
                        'title':self.get_Top_parent().title,
                        'points':self.get_Top_parent().points,
                        'child' :self.get_child(parentid_first)}

        return Response(custom_data)

    def get_Top_parent(self,parentId=0):
        parent = Registration.objects.get(parent_id=parentId)
        return parent
   
    
    def get_child(self,parentid=0):
        child_deatil = list(Registration.objects.filter(parent_id=parentid).values_list('reg_id',flat=True))
        child = []
        for i in child_deatil:
            obj = Registration.objects.get(reg_id=i)
            d={}
            d['id'] =obj.reg_id 
            d['name'] = obj.first_name
            d['title'] = obj.title
            d['points'] = obj.points
            parentid = obj.reg_id
            d['child'] = self.get_child(parentid)
            child.append(d)
        return child    

       
        

    
            
        
    