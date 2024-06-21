# # import pandas as pd
# # from sqlalchemy import create_engine
# # import requests
# # import schedule
# # import time
# # from datetime import datetime, timedelta
# # import dj_database_url
# # import psycopg2

# # # Replace these variables with your database credentials
# # # user = 'root'
# # # password = ''
# # # host = 'localhost'
# # # port = '3306'  # Default MySQL port
# # # database = 'attendapp'
# # #'ENGINE': 'django.db.backends.mysql',
# #  ##       
# # import requests
# # import base64

# # ##DATABASE
# # database_url = "postgres://default:5VsuIBhUnkP1@ep-wild-field-a1xpuji5.ap-southeast-1.aws.neon.tech:5432/verceldb?sslmode=require"
# # engine = create_engine(database_url)

# # # #VARIABLE FOR API
# # # empcode = "ALL"
# # # previousdate = (datetime.now() - timedelta(days=1)).strftime('%d-%m-%Y')
# # # presentdate = datetime.now().strftime('%d-%m-%Y')

# # api_url = "https://api.etimeoffice.com/api/DownloadInOutPunchData?Empcode=ALL&&FromDate=01/09/2023&&ToDate=30/05/2024"
# # api_key = "ORANGEDATATECH:HR@Orange:UY7g2#!gWEA6kB8:true"


# # # Encode the API key in base64
# # base64_api_key = base64.b64encode(api_key.encode()).decode()

# # headers = {
# #     "Authorization": f"Basic {base64_api_key}",
# #     "Content-Type": "application/json",
# # }

# # try:
# #     response = requests.get(api_url, headers=headers)

# #     if response.status_code == 200:
# #         entry_dataALL = response.json()
# #     else:
# #         print(f"Error: {response.status_code} - {response.text}")

# # except Exception as e:
# #     print(f"An error occurred: {e}")
# # ##
# # # Example DataFrame
# # import pandas as pd

# # # Your JSON data
# # json_data = entry_dataALL

# # # Extract the 'PunchData' key
# # punch_data = json_data['InOutPunchData']

# # # Create a DataFrame with the desired columns
# # df = pd.DataFrame(punch_data, columns=['Empcode', 'INTime', 'OUTTime', 'WorkTime', 'OverTime', 'BreakTime', 'Status', 'DateString', 'Remark', 'Erl_Out', 'Late_In',
# #                                        'Name'])


# # # Create SQLAlchemy engine
# # #engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}')

# # # Store DataFrame in MySQL database
# # table_name = 'employee1'
# # df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)

# # print(f'DataFrame successfully stored in table "{table_name}"')

# # # # Schedule the task
# # # schedule.every().day.at("10:30").do(fetch_and_store_data)
# # # schedule.every().day.at("02:00").do(fetch_and_store_data)

# # # print("Scheduler started. Waiting for the next scheduled task...")

# # # # Run the scheduler
# # # while True:
# # #     schedule.run_pending()
# # #     time.sleep(1)



# # ##DATABASE
# # # BASE_DIR = Path(__file__).resolve().parent.parent

# # # os.environ['DATABASE_URL'] = "postgres://default:5VsuIBhUnkP1@ep-wild-field-a1xpuji5.ap-southeast-1.aws.neon.tech:5432/verceldb?sslmode=require"

# # # DATABASES = {
# # #     'default': dj_database_url.config(
# # #         default=os.getenv('DATABASE_URL')
# # #     )
# # # }
# # # #pandas, sqlalchemy, psycopg2-binary, requests, schedule



# # # GEDATATECH:HR@Orange:UY7g2#!gWEA6kB8:true"

# # # # Encode the API key in base64
# # # base64_api_key = base64.b64encode(api_key.encode()).decode()

# # # headers = {
# # #     "Authorization": f"Basic {base64_api_key}",
# # #     "Content-Tyimport pandas as pd
# # # from sqlalchemy import create_engine
# # # import requests
# # # import schedule
# # # import time
# # # from datetime import datetime, timedelta
# # # import base64

# # # ##DATABASE
# # # database_url = "postgresql://default:5VsuIBhUnkP1@ep-wild-field-a1xpuji5.ap-southeast-1.aws.neon.tech:5432/verceldb?sslmode=require"
# # # engine = create_engine(database_url)

# # # #VARIABLE FOR API
# # # # empcode = "ALL"
# # # # previousdate = (datetime.now() - timedelta(days=1)).strftime('%d-%m-%Y')
# # # # presentdate = datetime.now().strftime('%d-%m-%Y')

# # # api_url = f"https://api.etimeoffice.com/api/DownloadInOutPunchData?Empcode=ALL&&FromDate=01/09/2024&&ToDate=30/05/2024"
# # # api_key = "ORANpe": "application/json",
# # # }

# # # def fetch_and_store_data():
# # #     try:
# # #         response = requests.get(api_url, headers=headers)

# # #         if response.status_code == 200:
# # #             entry_dataALL = response.json()

# # #             # Extract the 'PunchData' key
# # #             punch_data = entry_dataALL['InOutPunchData']

# # #             # Create a DataFrame with the desired columns
# # #             df = pd.DataFrame(punch_data, columns=['Empcode', 'INTime', 'OUTTime', 'WorkTime', 'OverTime', 'BreakTime', 'Status', 'DateString', 'Remark', 'Erl_Out', 'Late_In', 'Name'])

# # #             # Store DataFrame in PostgreSQL database
# # #             table_name = 'employee1'
# # #             df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)

# # #             print(f'DataFrame successfully stored in table "{table_name}"')

# # #         else:
# # #             print(f"Error: {response.status_code} - {response.text}")

# # #     except Exception as e:
# # #         print(f"An error occurred: {e}")

# # # # # Schedule the task
# # # # schedule.every().day.at("10:30").do(fetch_and_store_data)
# # # # schedule.every().day.at("14:00").do(fetch_and_store_data)

# # # # print("Scheduler started. Waiting for the next scheduled task...")

# # # # Run the scheduler
# # # # while True:
# # # #     schedule.run_pending()
# # # #     time.sleep(1)

#####################
#PERFECT CODE TO STORE THE DATA IN THE DB-

import pandas as pd
from sqlalchemy import create_engine
import requests
import schedule
import time
from datetime import datetime, timedelta
import base64

##DATABASE
database_url = "postgresql://default:5VsuIBhUnkP1@ep-wild-field-a1xpuji5.ap-southeast-1.aws.neon.tech:5432/verceldb?sslmode=require"
engine = create_engine(database_url)

#VARIABLE FOR API
# empcode = "ALL"
# previousdate = (datetime.now() - timedelta(days=1)).strftime('%d-%m-%Y')
# presentdate = datetime.now().strftime('%d-%m-%Y')

api_url = f"https://api.etimeoffice.com/api/DownloadInOutPunchData?Empcode=ALL&&FromDate=01/09/2023&&ToDate=09/06/2024"
api_key = "ORANGEDATATECH:HR@Orange:UY7g2#!gWEA6kB8:true"

# Encode the API key in base64
base64_api_key = base64.b64encode(api_key.encode()).decode()

headers = {
    "Authorization": f"Basic {base64_api_key}",
    "Content-Type": "application/json",
}

def fetch_and_store_data():
    try:
        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            entry_dataALL = response.json()

            # Extract the 'PunchData' key
            punch_data = entry_dataALL['InOutPunchData']

            # Create a DataFrame with the desired columns
            df = pd.DataFrame(punch_data, columns=['Empcode', 'INTime', 'OUTTime', 'WorkTime', 'OverTime', 'BreakTime', 'Status', 'DateString', 'Remark', 'Erl_Out', 'Late_In', 'Name'])

            # Store DataFrame in PostgreSQL database
            table_name = 'attendance_data'
            df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)

            print(f'DataFrame successfully stored in table "{table_name}"')

        else:
            print(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"An error occurred: {e}")

# # # # # Schedule the task
# # # # schedule.every().day.at("10:30").do(fetch_and_store_data)
# # # # schedule.every().day.at("14:00").do(fetch_and_store_data)

# # # # print("Scheduler started. Waiting for the next scheduled task...")

# # # # # Run the scheduler
# # # # while True:
# # # #     schedule.run_pending()
# # # #     time.sleep(1)




# # # import pandas as pd
# # # from sqlalchemy import create_engine
# # # import requests
# # # import schedule
# # # import time
# # # from datetime import datetime, timedelta
# # # import base64

# # # # Database connection URL
# # # database_url = "postgresql://default:5VsuIBhUnkP1@ep-wild-field-a1xpuji5.ap-southeast-1.aws.neon.tech:5432/verceldb?sslmode=require"
# # # engine = create_engine(database_url)

# # # # API variables
# # # # empcode = "ALL"
# # # # previousdate = (datetime.now() - timedelta(days=1)).strftime('%d-%m-%Y')
# # # # presentdate = datetime.now().strftime('%d-%m-%Y')

# # # #api_url = f"https://api.etimeoffice.com/api/DownloadInOutPunchData?Empcode={empcode}&&FromDate={previousdate}&&ToDate={presentdate}"
# # # api_url = f"https://api.etimeoffice.com/api/DownloadInOutPunchData?Empcode=ALL&FromDate=01/09/2023&ToDate=30/05/2024"
# # # api_key = "ORANGEDATATECH:HR@Orange:UY7g2#!gWEA6kB8:true"

# # # # Encode the API key in base64
# # # base64_api_key = base64.b64encode(api_key.encode()).decode()

# # # headers = {
# # #     "Authorization": f"Basic {base64_api_key}",
# # #     "Content-Type": "application/json",
# # # }

# # # def fetch_and_store_data():
# # #     try:
# # #         response = requests.get(api_url, headers=headers)

# # #         if response.status_code == 200:
# # #             entry_dataALL = response.json()

# # #             # Extract the 'InOutPunchData' key
# # #             punch_data = entry_dataALL.get('InOutPunchData', [])

# # #             if punch_data:
# # #                 # Create a DataFrame with the desired columns
# # #                 df = pd.DataFrame(punch_data, columns=[
# # #                     'Empcode', 'INTime', 'OUTTime', 'WorkTime', 'OverTime', 
# # #                     'BreakTime', 'Status', 'DateString', 'Remark', 'Erl_Out', 
# # #                     'Late_In', 'Name'
# # #                 ])

# # #                 # Store DataFrame in PostgreSQL database
# # #                 table_name = 'Employee'
# # #                 df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)

# # #                 print(f'DataFrame successfully stored in table "{table_name}"')

# # #             else:
# # #                 print("No punch data found in the API response.")

# # #         else:
# # #             print(f"Error: {response.status_code} - {response.text}")

# # #     except Exception as e:
# # #         print(f"An error occurred: {e}")

# # # Schedule the task
# # # schedule.every().day.at("13:35").do(fetch_and_store_data)
# # # schedule.every().day.at("14:00").do(fetch_and_store_data)

# # # print("Scheduler started. Waiting for the next scheduled task...")

# # # # Run the scheduler
# # # while True:
# # #     schedule.run_pending()
# # #     time.sleep(1)


# # import requests
# # import base64
# # from datetime import datetime, timedelta
# # from django.utils.dateparse import parse_datetime
# # import django
# # import os

# # # Set up Django environment
# # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'new_folder.settings')
# # django.setup()

# # from new_folder.models import Employee

# # # API URL and key
# # api_url = "https://api.etimeoffice.com/api/DownloadInOutPunchData?Empcode=ALL&FromDate=10/01/2024&ToDate=10/01/2024"
# # api_key = "ORANGEDATATECH:HR@Orange:UY7g2#!gWEA6kB8:true"

# # # Encode the API key in base64
# # base64_api_key = base64.b64encode(api_key.encode()).decode()

# # headers = {
# #     "Authorization": f"Basic {base64_api_key}",
# #     "Content-Type": "application/json",
# # }

# # try:
# #     response = requests.get(api_url, headers=headers)

# #     if response.status_code == 200:
# #         entry_dataALL = response.json()

# #         # Extract the 'InOutPunchData' key
# #         punch_data = entry_dataALL.get('InOutPunchData', [])

# #         for entry in punch_data:
# #             # Parse date and time fields
# #             date = datetime.strptime(entry['DateString'], '%d-%m-%Y').date()
# #             intime = parse_datetime(entry['INTime']).time() if entry['INTime'] else None
# #             outtime = parse_datetime(entry['OUTTime']).time() if entry['OUTTime'] else None

# #             # Convert worktime, overtime, breaktime to timedelta
# #             worktime = timedelta(hours=int(entry['WorkTime'].split(':')[0]), minutes=int(entry['WorkTime'].split(':')[1]))
# #             overtime = timedelta(hours=int(entry['OverTime'].split(':')[0]), minutes=int(entry['OverTime'].split(':')[1]))
# #             breaktime = timedelta(hours=int(entry['BreakTime'].split(':')[0]), minutes=int(entry['BreakTime'].split(':')[1]))

# #             # Create and save Employee instance
# #             employee = Employee(
# #                 emp_code=entry['Empcode'],
# #                 name=entry['Name'],
# #                 date=date,
# #                 intime=intime,
# #                 outtime=outtime,
# #                 worktime=worktime,
# #                 overtime=overtime,
# #                 breaktime=breaktime,
# #                 status=entry['Status'],
# #                 remark=entry['Remark'],
# #                 erlout=entry['Erl_Out'],
# #                 latein=entry['Late_In']
# #             )
# #             employee.save()

# #         print("Data successfully stored in the Employee table.")

# #     else:
# #         print(f"Error: {response.status_code} - {response.text}")

# # except Exception as e:
# #     print(f"An error occurred: {e}")





















# import pandas as pd
# from sqlalchemy import create_engine
# import requests
# import base64

# # Database URL
# database_url = "postgres://default:5VsuIBhUnkP1@ep-wild-field-a1xpuji5.ap-southeast-1.aws.neon.tech:5432/verceldb?sslmode=require"
# engine = create_engine(database_url)

# # API URL and key
# api_url = "https://api.etimeoffice.com/api/DownloadInOutPunchData?Empcode=ALL&FromDate=01/09/2023&ToDate=09/06/2024"
# api_key = "ORANGEDATATECH:HR@Orange:UY7g2#!gWEA6kB8:true"

# # Encode the API key in base64
# base64_api_key = base64.b64encode(api_key.encode()).decode()

# headers = {
#     "Authorization": f"Basic {base64_api_key}",
#     "Content-Type": "application/json",
# }

# try:
#     response = requests.get(api_url, headers=headers)

#     if response.status_code == 200:
#         entry_dataALL = response.json()
#     else:
#         print(f"Error: {response.status_code} - {response.text}")

# except Exception as e:
#     print(f"An error occurred: {e}")

# # Extract the 'InOutPunchData' key
# punch_data = entry_dataALL.get('InOutPunchData', [])

# # Create a DataFrame with the desired columns
# df = pd.DataFrame(punch_data, columns=[
#     'Empcode', 'INTime', 'OUTTime', 'WorkTime', 'OverTime', 'BreakTime', 
#     'Status', 'DateString', 'Remark', 'Erl_Out', 'Late_In', 'Name'
# ])

# # Define the table name
# table_name = 'employee'

# # Store DataFrame in PostgreSQL database
# df.to_sql(name=table_name, con=engine, if_exists='append', index=False)

# print(f'DataFrame successfully stored in table "{table_name}"')

# #####WORKED#####3

# import pandas as pd
# from sqlalchemy import create_engine
# import requests
# import base64
# import schedule
# import time
# from datetime import datetime, timedelta

# # Database URL
# database_url = "postgresql+psycopg2://default:5VsuIBhUnkP1@ep-wild-field-a1xpuji5.ap-southeast-1.aws.neon.tech:5432/verceldb?sslmode=require"
# engine = create_engine(database_url)


# # API variables
# empcode = "ALL"
# previousdate = 1/9/2023#(datetime.now() - timedelta(days=1)).strftime('%d-%m-%Y')
# presentdate = 9/6/2024#datetime.now().strftime('%d-%m-%Y')


# # API URL and key
# api_url = "https://api.etimeoffice.com/api/DownloadInOutPunchData?Empcode={empcode}&FromDate={previousdate}&ToDate={presentdate}"
# api_key = "ORANGEDATATECH:HR@Orange:UY7g2#!gWEA6kB8:true"

# # Encode the API key in base64
# base64_api_key = base64.b64encode(api_key.encode()).decode()

# headers = {
#     "Authorization": f"Basic {base64_api_key}",
#     "Content-Type": "application/json",
# }

# try:
#     response = requests.get(api_url, headers=headers)

#     if response.status_code == 200:
#         entry_dataALL = response.json()
#     else:
#         print(f"Error: {response.status_code} - {response.text}")

# except Exception as e:
#     print(f"An error occurred: {e}")

# # Extract the 'InOutPunchData' key
# punch_data = entry_dataALL.get('InOutPunchData', [])

# # Create a DataFrame with the desired columns
# df = pd.DataFrame(punch_data, columns=[
#     'Empcode', 'INTime', 'OUTTime', 'WorkTime', 'OverTime', 'BreakTime', 
#     'Status', 'DateString', 'Remark', 'Erl_Out', 'Late_In', 'Name'
# ])

# # TABLE_NAME
# table_name = 'employee'

# # Store DataFrame in PostgreSQL database
# df.to_sql(name=table_name, con=engine, if_exists='append', index=False)

# print(f'DataFrame successfully stored in table "{table_name}"')

# #SCHEDULING
# # schedule.every().day.at("13:35")
# # schedule.every().day.at("14:00").do(fetch_and_store_data)

# # print("Scheduler started. Waiting for the next scheduled task...")

# # # RUNNING THE SCHEDULER
# # while True:
# #     schedule.run_pending()
# #     time.sleep(1)



# ##
# #
# #
# # #
# # #
# #THE WORKING PYTHON SCRIPT WITH PYTHON SCRIPTS BELOW THIS THERE IS DJANGO SCRIPTS.

# import pandas as pd
# from sqlalchemy import create_engine
# import requests
# import base64
# import schedule
# import time
# from datetime import datetime, timedelta

# # Database URL
# database_url = "postgresql+psycopg2://default:5VsuIBhUnkP1@ep-wild-field-a1xpuji5.ap-southeast-1.aws.neon.tech:5432/verceldb?sslmode=require"
# engine = create_engine(database_url)

# # API key and base64 encoding
# api_key = "ORANGEDATATECH:HR@Orange:UY7g2#!gWEA6kB8:true"
# base64_api_key = base64.b64encode(api_key.encode()).decode()

# headers = {
#     "Authorization": f"Basic {base64_api_key}",
#     "Content-Type": "application/json",
# }

# def fetch_and_store_data():
#     # Calculate previous and present dates
#     previousdate = 1/9/2024#(datetime.now() - timedelta(days=1)).strftime('%d-%m-%Y')
#     presentdate = 8/6/2024#datetime.now().strftime('%d-%m-%Y')

#     # API URL with dynamic dates
#     api_url = f"https://api.etimeoffice.com/api/DownloadInOutPunchData?Empcode=ALL&FromDate={previousdate}&ToDate={presentdate}"

#     try:
#         response = requests.get(api_url, headers=headers)

#         if response.status_code == 200:
#             entry_dataALL = response.json()
#         else:
#             print(f"Error: {response.status_code} - {response.text}")
#             return

#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return

#     # Extract the 'InOutPunchData' key
#     punch_data = entry_dataALL.get('InOutPunchData', [])

#     # Create a DataFrame with the desired columns
#     df = pd.DataFrame(punch_data, columns=[
#         'Empcode', 'INTime', 'OUTTime', 'WorkTime', 'OverTime', 'BreakTime', 
#         'Status', 'DateString', 'Remark', 'Erl_Out', 'Late_In', 'Name'
#     ])

#     # TABLE_NAME
#     table_name = 'employee'

#     # Store DataFrame in PostgreSQL database
#     df.to_sql(name=table_name, con=engine, if_exists='append', index=False)

#     print(f'DataFrame successfully stored in table "{table_name}"')

# # # Schedule the job to run daily at a specific time, e.g., 02:00 AM
# # schedule.every().day.at("16:35").do(fetch_and_store_data)
# # schedule.every().day.at("16:40").do(fetch_and_store_data)

# # # Keep the script running to execute the scheduled jobs
# # while True:
# #     schedule.run_pending()
# #     time.sleep(1)


# # Schedule the task
# schedule.every().day.at("15:30").do(fetch_and_store_data)
# schedule.every().day.at("15:32").do(fetch_and_store_data)

# print("Scheduler started. Waiting for the next scheduled task...")

# # Run the scheduler
# while True:
#     schedule.run_pending()
#     time.sleep(1)
# ## /////////////////////////////////////
# import datetime
# from api.models import data
# from api.utils import send_missing_punch_email

# def check_and_send_missing_punch_emails():
#     today = datetime.date.today()
#     missing_punches = Attendance.objects.filter(intime__isnull=True, date=today)
#     for record in missing_punches:
#         user_email = record.user.email  
#         send_missing_punch_email(user_email, today)


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# import pandas as pd
# from sqlalchemy import create_engine
# import requests
# import base64
# from datetime import datetime, timedelta
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# # Database URL
# database_url = "postgresql+psycopg2://default:5VsuIBhUnkP1@ep-wild-field-a1xpuji5.ap-southeast-1.aws.neon.tech:5432/verceldb?sslmode=require"
# engine = create_engine(database_url)

# # API key and base64 encoding
# api_key = "ORANGEDATATECH:HR@Orange:UY7g2#!gWEA6kB8:true"
# base64_api_key = base64.b64encode(api_key.encode()).decode()

# headers = {
#     "Authorization": f"Basic {base64_api_key}",
#     "Content-Type": "application/json",
# }

# # Email configuration
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'pravinmewada1999@gmail.com'  # Your email address
# EMAIL_HOST_PASSWORD = 'pm931630'  # Your email password or app password
# DEFAULT_FROM_EMAIL = 'pravinmewada1999@gmail.com'

# def send_missing_punch_email(user_email, date):
#     subject = 'Missing Punch Notification'
#     message = f'Dear User,\n\nIt seems that you have a missing punch on {date}. Please make sure to report this to HR or rectify it as soon as possible.\n\nBest regards,\nAttendance System'
    
#     msg = MIMEMultipart()
#     msg['pravinmewada1999@gmail.com'] = DEFAULT_FROM_EMAIL
#     msg['ritikjaiswal8888@gmail.com'] = user_email
#     msg['Subject is checking'] = subject

#     msg.attach(MIMEText(message, 'plain'))
    
#     try:
#         server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
#         server.starttls()
#         server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
#         text = msg.as_string()
#         server.sendmail(DEFAULT_FROM_EMAIL, user_email, text)
#         server.quit()
#         print(f"Email sent to {user_email} for missing punch on {date}")
#     except Exception as e:
#         print(f"Failed to send email to {user_email} for missing punch on {date}: {e}")

# def fetch_and_store_data():
#     # Calculate previous and present dates
#     previousdate = (datetime.now() - timedelta(days=1)).strftime('%d-%m-%Y')
#     presentdate = datetime.now().strftime('%d-%m-%Y')

#     # API URL with dynamic dates
#     api_url = f"https://api.etimeoffice.com/api/DownloadInOutPunchData?Empcode=ALL&FromDate={previousdate}&ToDate={presentdate}"

#     try:
#         response = requests.get(api_url, headers=headers)

#         if response.status_code == 200:
#             entry_dataALL = response.json()
#         else:
#             print(f"Error: {response.status_code} - {response.text}")
#             return

#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return

#     # Extract the 'InOutPunchData' key
#     punch_data = entry_dataALL.get('InOutPunchData', [])

#     # Create a DataFrame with the desired columns
#     df = pd.DataFrame(punch_data, columns=[
#         'Empcode', 'INTime', 'OUTTime', 'WorkTime', 'OverTime', 'BreakTime', 
#         'Status', 'DateString', 'Remark', 'Erl_Out', 'Late_In', 'Name'
#     ])

#     # TABLE_NAME
#     table_name = 'employee'

#     # Store DataFrame in PostgreSQL database
#     df.to_sql(name=table_name, con=engine, if_exists='append', index=False)

#     print(f'DataFrame successfully stored in table "{table_name}"')

#     # Check for missing punches and send emails
#     check_and_send_missing_punch_emails(previousdate)

# def check_and_send_missing_punch_emails(date):
#     query = f"""
#     SELECT "Empcode", "Name", "INTime", "DateString"
#     FROM employee
#     WHERE "INTime" IS NULL AND "DateString" = '{date}'
#     """
#     df_missing_punches = pd.read_sql(query, con=engine)
    
#     for _, row in df_missing_punches.iterrows():
#         user_email = f"{row['Empcode']}@company.com"  # Replace with actual logic to get user email
#         send_missing_punch_email(user_email, row['DateString'])

# Schedule the fetch_and_store_data function to run daily
# Uncomment below lines to use scheduling
# schedule.every().day.at("01:00").do(fetch_and_store_data)

# while True:
#     schedule.run_pending()
#     time.sleep(1)

# For immediate run
fetch_and_store_data()
