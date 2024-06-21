from rest_framework import status
#from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CustomUser,Employer_Profile,Employee_Details
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login 
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import logout
from django.db.models import Count
from django.shortcuts import get_object_or_404
import json
from rest_framework.generics import DestroyAPIView
from rest_framework import viewsets
from rest_framework.generics import RetrieveUpdateAPIView
from .serializers import UserUpdateSerializer,EmployerProfileSerializer ,GetEmployeeDetailsSerializer,EmployeeDetailsSerializer,GetEmployerDetailsSerializer
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
#from .forms import PDFUploadForm
#from .models import PDFFile
from django.db import transaction
from rest_framework.decorators import api_view
# from django.core.mail import send_mail            # added later
# from django.core.mail import sendmessage          # added later
# from auth_project.settings import EMAIL_HOST_USER # added later
 
@csrf_exempt
def login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Invalid JSON', 'status_code':status.HTTP_400_BAD_REQUEST})

        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return JsonResponse({'success': False, 'message': 'email and password are required','status_code':status.HTTP_400_BAD_REQUEST})

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Invalid credentials','status_code':status.HTTP_400_BAD_REQUEST})

        if check_password(password, user.password):
            auth_login(request, user) 
            user_data = {
                'id': user.id,
                'username': user.username,
                'name': user.name,
                'email': user.email,
            }
            refresh = RefreshToken.for_user(user)
            response_data = {
                'success': True,
                'message': 'Login successful',
                'user_data': user_data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'code': status.HTTP_200_OK,
            }
            return JsonResponse(response_data)
        else:
            return JsonResponse({'success': False, 'message': 'Invalid credentials','status_code':status.HTTP_400_BAD_REQUEST})
    else:
        return JsonResponse({'message': 'Please use POST method for login','status_code':status.HTTP_400_BAD_REQUEST})





@csrf_exempt
def register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON','status_code':status.HTTP_400_BAD_REQUEST})

        #name = data.get('name')
        username = data.get('username')
        email = data.get('email')
        password1 = data.get('password1')
        password2 = data.get('password2')

        if not all([ username, email, password1, password2]):
            return JsonResponse({'error': 'All fields are required', 'status_code':status.HTTP_400_BAD_REQUEST})

        if password1 != password2:
            return JsonResponse({'error': 'Passwords do not match', 'status_code':status.HTTP_400_BAD_REQUEST})

        if not (len(password1) >= 8 and any(c.isupper() for c in password1) and any(c.islower() for c in password1) and any(c.isdigit() for c in password1) and any(c in '!@#$%^&*()_+' for c in password1)):
            return JsonResponse({'error': 'Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character', 'status_code':status.HTTP_400_BAD_REQUEST})

        User = get_user_model()
        if CustomUser.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username taken', 'status_code':status.HTTP_400_BAD_REQUEST})
        if CustomUser.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email taken', 'status_code' :status.HTTP_400_BAD_REQUEST})

        try:
            user = CustomUser.objects.create_user( email=email, username=username, password=password1)
            user.save()
            return JsonResponse({'message': 'Successfully registered', 'status_code':status.HTTP_201_CREATED})
        except Exception as e:
            return JsonResponse({'error': str(e), 'status_code':status.HTTP_500_INTERNAL_SERVER_ERROR})
    else:
        return JsonResponse({'message': 'Please use POST method for registor', 'status_code':status.HTTP_400_BAD_REQUEST})


########################

   

# def dashboard(request):
#     return render( 'dashboard.html')




@csrf_exempt
def EmployerProfile(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            required_fields = ['employer_name', 'street_name', 'federal_employer_identification_number', 'city', 'state', 'country', 'zipcode', 'email', 'number_of_employees', 'department', 'location']
            missing_fields = [field for field in required_fields if field not in data or not data[field]]
            if missing_fields:
                return JsonResponse({'error': f'Required fields are missing: {", ".join(missing_fields)}','status_code':status.HTTP_400_BAD_REQUEST})
            
            # Validate length of federal_employer_identification_number
            if len(str(data['federal_employer_identification_number'])) != 9:
                return JsonResponse({'error': 'Federal Employer Identification Number must be exactly 9 characters long', 'status_code':status.HTTP_400_BAD_REQUEST})
            
            if Employer_Profile.objects.filter(email=data['email']).exists():
                return JsonResponse({'error': 'Email already registered', 'status_code':status.HTTP_400_BAD_REQUEST})
            
            user = Employer_Profile.objects.create(**data)
            return JsonResponse({'message': 'Employer Detail Successfully Registered'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
    else:
        return JsonResponse({'message': 'Please use POST method','status_code':status.HTTP_400_BAD_REQUEST})


@csrf_exempt
def EmployeeDetails(request):
    if request.method == 'POST' :
        try:
            data = json.loads(request.body)
            required_fields = ['emp_code', 'name', 'email', 'emp_role', 'username']
            missing_fields = [field for field in required_fields if field not in data or not data[field]]
            
            if missing_fields:
                return JsonResponse({'error': f'Required fields are missing: {", ".join(missing_fields)}', 'status_code':status.HTTP_400_BAD_REQUEST})
            
            # if Employee_Details.objects.filter(employee_id=data['employee_id']).exists():
            #     return JsonResponse({'error': 'Employee ID already exists', 'status_code':status.HTTP_400_BAD_REQUEST})
            
            Employee_Details.objects.create(**data)
            return JsonResponse({'message': 'Employee Details Successfully Registered', 'status_code':status.HTTP_201_CREATED})
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format','status_code':status.HTTP_400_BAD_REQUEST})
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return JsonResponse({'message': 'Please use POST method ', 'status_code':status.HTTP_400_BAD_REQUEST})
    
    
#for Updating the Employer Profile data

class EmployerProfileEditView(RetrieveUpdateAPIView):
    queryset = Employer_Profile.objects.all()
    serializer_class = EmployerProfileSerializer
    lookup_field = 'employer_id'
    @csrf_exempt
    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data

        # Check for missing fields
        required_fields = ['employer_name', 'street_name', 'federal_employer_identification_number', 'city', 'state', 'country', 'zipcode', 'email', 'number_of_employees', 'department', 'location']
        missing_fields = [field for field in required_fields if field not in data or not data[field]]
        if missing_fields:
            return JsonResponse({'error': f'Required fields are missing: {", ".join(missing_fields)}', 'status_code':status.HTTP_400_BAD_REQUEST})

        # Validate length of federal_employer_identification_number
        if 'federal_employer_identification_number' in data and len(str(data['federal_employer_identification_number'])) != 9:
            return JsonResponse({'error': 'Federal Employer Identification Number must be exactly 9 characters long', 'status_code':status.HTTP_400_BAD_REQUEST})

        # Validate email if it's being updated
        if 'email' in data and Employer_Profile.objects.filter(email=data['email']).exclude(employer_id=instance.employer_id).exists():
            return JsonResponse({'error': 'Email already registered', 'status_code':status.HTTP_400_BAD_REQUEST})

        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response_data = {
            'success': True,
            'message': 'Data Updated successfully',
            'Code': status.HTTP_200_OK
        }
        return JsonResponse(response_data)




#For updating the Registor details

class UserUpdateAPIView(RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserUpdateSerializer
    lookup_field = 'username'  
    @csrf_exempt
    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response_data = {
                'success': True,
                'message': 'Data Updated successfully',
                'Code': status.HTTP_200_OK}
        return JsonResponse(response_data)
    



#update employee Details
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class EmployeeDetailsUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Employee_Details.objects.all()
    serializer_class = EmployeeDetailsSerializer
    lookup_field = 'employee_id'  
    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response_data = {
                'success': True,
                'message': 'Data Updated successfully',
                'Code': status.HTTP_200_OK}
        return JsonResponse(response_data)


# For Deleting the Employer Profile data
@method_decorator(csrf_exempt, name='dispatch')
class UserDeleteAPIView(DestroyAPIView):
    queryset = CustomUser.objects.all()
    lookup_field = 'username' 
    @csrf_exempt
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        response_data = {
                'success': True,
                'message': 'Data Deleted successfully',
                'Code': status.HTTP_200_OK}
        return JsonResponse(response_data)
    




#Get Employer Details on the bases of Employer_ID

@api_view(['GET'])
def get_employee_by_employer_id(request, employer_id):
    employees=Employee_Details.objects.filter(employer_id=employer_id)
    if employees.exists():
        try:
            serializer = GetEmployeeDetailsSerializer(employees, many=True)
            response_data = {
                    'success': True,
                    'message': 'Data Get successfully',
                    'Code': status.HTTP_200_OK}
            response_data['data'] = serializer.data
            return JsonResponse(response_data)


        except Employee_Details.DoesNotExist:
            return JsonResponse({'message': 'Data not found', 'status_code':status.HTTP_404_NOT_FOUND})
    else:
        return JsonResponse({'message': 'Employer ID not found', 'status':status.HTTP_404_NOT_FOUND})



#Get Employer Details from employer ID

@api_view(['GET'])
def get_employer_details(request, employer_id):
    employees=Employer_Profile.objects.filter(employer_id=employer_id)
    if employees.exists():
        try:
            serializer = GetEmployerDetailsSerializer(employees, many=True)
            response_data = {
                    'success': True,
                    'message': 'Data Get successfully',
                    'Code': status.HTTP_200_OK}
            response_data['data'] = serializer.data
            return JsonResponse(response_data)


        except Employer_Profile.DoesNotExist:
            return JsonResponse({'message': 'Data not found', 'status_code':status.HTTP_404_NOT_FOUND})
    else:
        return JsonResponse({'message': 'Employer ID not found', 'status_code':status.HTTP_404_NOT_FOUND})

#count the number using this code
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import requests
import base64
from datetime import datetime, time
from .models import count_number
import json

# API credentials
api_url_template = "https://api.etimeoffice.com/api/DownloadInOutPunchData?Empcode=ALL&FromDate={}&ToDate={}"
api_key = "ORANGEDATATECH:HR@Orange:UY7g2#!gWEA6kB8:true"

# Encode the API key in base64
base64_api_key = base64.b64encode(api_key.encode()).decode()

headers = {
    "Authorization": f"Basic {base64_api_key}",
    "Content-Type": "application/json",
}

# Function to fetch data from the API
def fetch_data_from_api(date):
    formatted_date = date.strftime('%d/%m/%Y')
    api_url = api_url_template.format(formatted_date, formatted_date)
    try:
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            return response.json().get('InOutPunchData', [])
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Function to analyze the data
def analyze_data(df):
    # Ensure 'INTime' and 'OUTTime' are properly parsed as datetime objects
    df['INTime'] = pd.to_datetime(df['INTime'], format='%H:%M', errors='coerce')
    df['OUTTime'] = pd.to_datetime(df['OUTTime'], format='%H:%M', errors='coerce')
    reference_time = time(10, 15)
    
    # Extract the time part from the INTime column
    df['INTimeOnly'] = df['INTime'].dt.time
    
    ontime_count = df[df['INTimeOnly'] <= reference_time].shape[0]
    latein_count = df[df['INTimeOnly'] > reference_time].shape[0]
    absent_count = df[df['INTime'].isna() & df['OUTTime'].isna()].shape[0]

    return {
        "ONTime": ontime_count,
        "LateIN": latein_count,
        "Absent": absent_count
    }

@csrf_exempt
def fetch_and_store_data(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            date_input = data.get("date")
            
            # Validate the date format
            try:
                date_object = datetime.strptime(date_input, '%d/%m/%Y')
                date_str = date_object.strftime('%d/%m/%Y')
            except ValueError:
                return JsonResponse({"error": "Incorrect date format, should be dd/mm/yyyy"}, status=400)
            
            # Fetch data from API
            data = fetch_data_from_api(date_object)
            if not data:
                return JsonResponse({"error": f"No data found for the entered date: {date_input}"}, status=404)
            else:
                # Create a DataFrame with the desired columns
                df = pd.DataFrame(data, columns=[
                    'Empcode', 'INTime', 'OUTTime', 'WorkTime', 'OverTime', 'BreakTime', 
                    'Status', 'DateString', 'Remark', 'Erl_Out', 'Late_In', 'Name'
                ])
                # Ensure the DateString column is consistent
                df['DateString'] = date_str

                # Truncate the existing data
                count_number.objects.all().delete()
                
                # Store the data in the database using Django ORM
                for _, row in df.iterrows():
                    count_number.objects.update_or_create(
                        empcode=row['Empcode'],
                        datestring=row['DateString'],
                        defaults={
                            'intime': row['INTime'],
                            'outtime': row['OUTTime'],
                            'worktime': row['WorkTime'],
                            'overtime': row['OverTime'],
                            'breaktime': row['BreakTime'],
                            'status': row['Status'],
                            'remark': row['Remark'],
                            'erl_out': row['Erl_Out'],
                            'late_in': row['Late_In'],
                            'name': row['Name'],
                        }
                    )
                
                # Perform the analysis on the data
                analysis_result = analyze_data(df)
                
                return JsonResponse({"analysis": analysis_result}, status=200)
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)

######################





# @csrf_exempt
# def get_dashboard_data(request):
#     total_iwo = IWO_Details_PDF.objects.count()

#     employees_with_single_iwo = IWO_Details_PDF.objects.values('employee_id').annotate(iwo_count=Count('employee_id')).filter(iwo_count=1).count()

#     employees_with_multiple_iwo = IWO_Details_PDF.objects.values('employee_id').annotate(iwo_count=Count('employee_id')).filter(iwo_count__gt=1).count()

#     active_employees = IWO_Details_PDF.objects.filter(IWO_Status='active').count()

#     data = {
#         'Total IWO': total_iwo,
#         'Employees with Single IWO': employees_with_single_iwo,
#         'Employees with Multiple IWO': employees_with_multiple_iwo,
#         'Active_employees': active_employees,
#     }

#     return JsonResponse({'data':data,'status_code':status.HTTP_200_OK})
  