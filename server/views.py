from email.mime import image
from pydoc import describe
from django.views import View
from django.core.files.storage import FileSystemStorage
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import *
from django.shortcuts import render


'''ALUMNI REQUESTS'''
@method_decorator(csrf_exempt, name='dispatch')
class ViewAlumnis(View):
    def get(self, request):
        """GET ALL THE ALUMNIS"""
        alumnis_data = []
        alumnis = Alumni.objects.all()
        for alumni in alumnis:
            alumnis_data.append({
                "name": alumni.name,
                "registration_no": alumni.registration_no, 
                "passing_year": alumni.passing_year,
                "branch": alumni.branch,
                "email_id": alumni.email_id,
                "company": alumni.company,
                "designation": alumni.designation,
                "image": alumni.image_url
            })
        alumnis_info = {
            "alumnis" : alumnis_data
        }
        return JsonResponse(alumnis_info, status=200)


@method_decorator(csrf_exempt, name="dispatch")
class CreateAlumni(View):
    def post(self,request):
        """CREATE ALUMNI"""
        data = json.loads(request.body.decode("utf-8")) 
        name = data.get("name")
        registration_no = data.get("registration_no")
        passing_year = data.get("passing_year")
        branch = data.get("branch")
        email_id = data.get("email_id")
        company = data.get("company")
        designation = data.get("designation")
        alumni_data = {
            "name":name,
            "registration_no":registration_no, 
            "passing_year":passing_year,
            "branch":branch,
            "email_id": email_id,
            "company" : company,
            "designation" : designation
        }
        alumni = Alumni.objects.create(**alumni_data)
        alumni.save()
        return JsonResponse({"data":alumni_data}, status=200)

@method_decorator(csrf_exempt, name="dispatch")
class UpdateAlumni(View):
    def patch(self,request, registration_no):
        """UPDATE INFORMATION OF ALUMNI"""
        data = json.loads(request.body.decode("utf-8"))
        Alumni.objects.filter(registration_no=registration_no).update(**data)
        data = {
            "messege": f"Alumni {registration_no} is updaated"
        }
        return JsonResponse(data)
    
    def delete(self,request, registration_no):
        alumni = Alumni.objects.get(registration_no = registration_no)
        alumni.delete()
        data = {
            "messege": f"Alumni {registration_no} has been deleted"
        }
        return JsonResponse(data)


@method_decorator(csrf_exempt, name="dispatch")
class UpdateAlumniImage(View):
    def post(self,request, registration_no):
        """UPLOAD IMAGE OF THE ALUMNI"""
        file = request.FILES['file']
        fss = FileSystemStorage()
        file = fss.save("alumni_images/"+file.name,file)
        file_url = fss.url(file)
        Alumni.objects.filter(registration_no=registration_no).update(image_url=file_url)
        data = {
            "messege": f"Alumni {registration_no} image uploaded"
        }
        return JsonResponse(data)



'''EVENTS VIEWS'''
@method_decorator(csrf_exempt, name="dispatch")
class ViewEvents(View):
    def get(self, request):
        """GET ALL THE EVENTS"""
        events_data = []
        events = Event.objects.all()
        for event in events:
            events_data.append({
                "name": event.name,
                "schedule": event.schedule,
                "description": event.description,
                "event_image": event.event_image
            })
        events_info = {
            "events": events_data
        }
        return JsonResponse(events_info,status=200)

@method_decorator(csrf_exempt, name="dispatch")
class CreateEvent(View):
    def post(self,request):
        """CREATE EVENT"""
        name = request.POST.get("name")
        schedule = request.POST.get("schedule")
        description = request.POST.get("description")
        event_image = request.FILES['file']
        fss = FileSystemStorage()
        event_image = fss.save("event_images/"+event_image.name,event_image)
        event_image_url = fss.url(event_image)
        event_data = {
            "name": name,
            "schedule": schedule,
            "description": description,
            "event_image": event_image_url
        }
        event = Event.objects.create(**event_data)
        event.save()
        event_info = {
            "event": event
        }
        return JsonResponse(event_info, status=200)
    

"""HIRING VIEWS"""
@method_decorator(csrf_exempt, name="dispatch")
class ViewHirings(View):
    def get(self, request):
        """GET ALL THE EVENTS"""
        hirings_data = []
        hirings = Hiring.objects.all()
        for hiring in hirings:
            hirings_data.append({
                "company": hiring.company,
                "title": hiring.title,
                "location": hiring.location,
                "description": hiring.description,
            })
        hirings_info = {
            "hirings": hirings_data
        }
        return JsonResponse(hirings_info,status=200)

@method_decorator(csrf_exempt, name="dispatch")
class CreateHiring(View):
    def post(self,request):
        """CREATE HIRING"""
        data = json.loads(request.body.decode("utf-8"))
        company = data.get("company")
        title = data.get("title")
        location = data.get("location")
        description = data.get("description")
        hiring_data ={
            "company": company,
            "title": title,
            "location": location,
            "description": description
        }
        hiring = Hiring.objects.create(**hiring_data)
        data = {
            "messege": "added hirng successfully"
        }
        return JsonResponse(data, status=200)








