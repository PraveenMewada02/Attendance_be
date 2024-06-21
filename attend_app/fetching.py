
# # # import pandas as pd
# # # from sqlalchemy import create_engine
# # # import requests
# # # import base64
# # # from datetime import datetime, timedelta
# # # import smtplib
# # # from email.mime.text import MIMEText
# # # from email.mime.multipart import MIMEMultipart


# # # # Database URL
# # # database_url = "postgresql+psycopg2://default:5VsuIBhUnkP1@ep-wild-field-a1xpuji5.ap-southeast-1.aws.neon.tech:5432/verceldb?sslmode=require"
# # # engine = create_engine(database_url)

# # # # API key and base64 encoding
# # # api_key = "ORANGEDATATECH:HR@Orange:UY7g2#!gWEA6kB8:true"
# # # base64_api_key = base64.b64encode(api_key.encode()).decode()

# # # headers = {
# # #     "Authorization": f"Basic {base64_api_key}",
# # #     "Content-Type": "application/json",
# # # }

# # # # Email configuration
# # # EMAIL_HOST = 'smtp.gmail.com'
# # # EMAIL_PORT = 587
# # # EMAIL_USE_TLS = True
# # # EMAIL_HOST_USER = 'pravinmewada1999@gmail.com'  # Your email address
# # # EMAIL_HOST_PASSWORD = '*******'  # Your email password or app password
# # # DEFAULT_FROM_EMAIL = 'pravinmewada1999@gmail.com'

# # # def send_missing_punch_email(user_email, date):
# # #     subject = 'Missing Punch Notification'
# # #     message = f'Dear User,\n\nIt seems that you have a missing punch on {date}. Please make sure to report this to HR or rectify it as soon as possible.\n\nBest regards,\nAttendance System'
    
# # #     msg = MIMEMultipart()
# # #     msg['pravinmewada1999@gmail.com'] = DEFAULT_FROM_EMAIL
# # #     msg['ritikjaiswal8888@gmail.com'] = user_email
# # #     msg['punch missing'] = subject

# # #     msg.attach(MIMEText(message, 'plain'))
    
# # #     try:
# # #         server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
# # #         server.starttls()
# # #         server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
# # #         text = msg.as_string()
# # #         server.sendmail(DEFAULT_FROM_EMAIL, user_email, text)
# # #         server.quit()
# # #         print(f"Email sent to {user_email} for missing punch on {date}")
# # #     except Exception as e:
# # #         print(f"Failed to send email to {user_email} for missing punch on {date}: {e}")

# # # def fetch_and_store_data():
# # #     # Calculate previous and present dates
# # #     previousdate =  8/6/2024#datetime.now().strftime('%d-%m-%Y') #(datetime.now() - timedelta(days=1)).strftime('%d-%m-%Y')
# # #     presentdate = 8/6/2024 #datetime.now().strftime('%d-%m-%Y')

# # #     # API URL with dynamic dates
# # #     api_url = f"https://api.etimeoffice.com/api/DownloadInOutPunchData?Empcode=ALL&FromDate={previousdate}&ToDate={presentdate}"

# # #     try:
# # #         response = requests.get(api_url, headers=headers)

# # #         if response.status_code == 200:
# # #             entry_dataALL = response.json()
# # #         else:
# # #             print(f"Error: {response.status_code} - {response.text}")
# # #             return

# # #     except Exception as e:
# # #         print(f"An error occurred: {e}")
# # #         return

# # #     # Extract the 'InOutPunchData' key
# # #     punch_data = entry_dataALL.get('InOutPunchData', [])

# # #     # Create a DataFrame with the desired columns
# # #     df = pd.DataFrame(punch_data, columns=[
# # #         'Empcode', 'INTime', 'OUTTime', 'WorkTime', 'OverTime', 'BreakTime', 
# # #         'Status', 'DateString', 'Remark', 'Erl_Out', 'Late_In', 'Name'
# # #     ])

# # #     # TABLE_NAME
# # #     table_name = 'employee'

# # #     # Store DataFrame in PostgreSQL database
# # #     df.to_sql(name=table_name, con=engine, if_exists='append', index=False)

# # #     print(f'DataFrame successfully stored in table "{table_name}"')

# # #     # Check for missing punches and send emails
# # #     check_and_send_missing_punch_emails(previousdate)

# # # def check_and_send_missing_punch_emails(date):
# # #     query = f"""
# # #     SELECT "Empcode", "Name", "INTime", "DateString"
# # #     FROM employee
# # #     WHERE "INTime" IS NULL AND "DateString" = '{date}'
# # #     """
# # #     df_missing_punches = pd.read_sql(query, con=engine)
    
# # #     for _, row in df_missing_punches.iterrows():
# # #         user_email = f"{row['Empcode']}@company.com"  # Replace with actual logic to get user email
# # #         send_missing_punch_email(user_email, row['DateString'])

# # # # Schedule the fetch_and_store_data function to run daily
# # # # Uncomment below lines to use scheduling
# # # # schedule.every().day.at("01:00").do(fetch_and_store_data)

# # # # while True:
# # # #     schedule.run_pending()
# # # #     time.sleep(1)

# # # # For immediate run
# # # fetch_and_store_data()

# # #///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# import pandas as pd
# from sqlalchemy import create_engine
# import requests
# import base64
# from datetime import datetime

# # Database URL
# database_url = "postgresql+psycopg2://default:5VsuIBhUnkP1@ep-wild-field-a1xpuji5.ap-southeast-1.aws.neon.tech:5432/verceldb?sslmode=require"
# engine = create_engine(database_url)

# # API credentials
# api_url_template = "https://api.etimeoffice.com/api/DownloadInOutPunchData?Empcode=ALL&FromDate={}&ToDate={}"
# api_key = "ORANGEDATATECH:HR@Orange:UY7g2#!gWEA6kB8:true"

# # Encode the API key in base64
# base64_api_key = base64.b64encode(api_key.encode()).decode()

# headers = {
#     "Authorization": f"Basic {base64_api_key}",
#     "Content-Type": "application/json",
# }

# # Function to fetch data from the API
# def fetch_data_from_api(date):
#     formatted_date = date.strftime('%d/%m/%Y')
#     api_url = api_url_template.format(formatted_date, formatted_date)
#     try:
#         response = requests.get(api_url, headers=headers)
#         if response.status_code == 200:
#             return response.json().get('InOutPunchData', [])
#         else:
#             print(f"Error: {response.status_code} - {response.text}")
#             return []
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return []

# # Function to store data in PostgreSQL database
# def store_data(df, table_name):
#     df.to_sql(name=table_name, con=engine, if_exists='append', index=False)
#     print(f"DataFrame successfully stored in table '{table_name}'")

# # Main execution flow
# table_name = "attendance_data_of_14"
# date_input = input("Enter the date (dd/mm/yyyy): ")#datetime.today().strftime('%d/%m/%Y')#   #
#                                                       #datetime.now().strftime('%d-%m-%Y')
# # Validate the date format
# try:
#     date_object = datetime.strptime(date_input, '%d/%m/%Y')
# except ValueError:
#     print("Incorrect date format, should be dd/mm/yyyy")
# else:
#     # Fetch data from API
#     data = fetch_data_from_api(date_object)
#     if not data:
#         print(f"No data found for the entered date: {date_input}")
#     else:
#         # Create a DataFrame with the desired columns
#         df = pd.DataFrame(data, columns=[
#             'Empcode', 'INTime', 'OUTTime', 'WorkTime', 'OverTime', 'BreakTime', 
#             'Status', 'DateString', 'Remark', 'Erl_Out', 'Late_In', 'Name'
#         ])
#         # Store the data in the database
#         store_data(df, table_name)
#         print("Data for the specified date:")
#         print(df)

# ######################################

#SCHEDULING PROGRAM TO SAVE AND DELETE THE PREVIOUS DATA.
import pandas as pd
from sqlalchemy import create_engine, text
import requests
import base64
from datetime import datetime, timedelta
import time
import threading

# Database URL
database_url = "postgresql+psycopg2://default:5VsuIBhUnkP1@ep-wild-field-a1xpuji5.ap-southeast-1.aws.neon.tech:5432/verceldb?sslmode=require"
engine = create_engine(database_url)

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

# Function to store data in PostgreSQL database
def store_data(df, table_name):
    df.to_sql(name=table_name, con=engine, if_exists='append', index=False)
    print(f"DataFrame successfully stored in table '{table_name}'")

# Function to delete data of the previous day
def delete_previous_date_data(table_name):
    with engine.connect() as conn:
        delete_query = text(f"DELETE FROM {table_name} WHERE DATE_TRUNC('day', TO_TIMESTAMP(DateString, 'DD/MM/YYYY')) < CURRENT_DATE")
        result = conn.execute(delete_query)
        print(f"Deleted {result.rowcount} rows of data older than today from '{table_name}'")

# Function to schedule the deletion at the start of the next day
def schedule_deletion(table_name):
    now = datetime.now()
    next_day = now + timedelta(days=1)
    next_day_start = datetime.combine(next_day, datetime.min.time())
    seconds_until_next_day = (next_day_start - now).total_seconds()

    def run_deletion():
        while True:
            time.sleep(seconds_until_next_day)
            delete_previous_date_data(table_name)
            # Calculate seconds until the next day
            now = datetime.now()
            next_day = now + timedelta(days=1)
            next_day_start = datetime.combine(next_day, datetime.min.time())
            seconds_until_next_day = (next_day_start - now).total_seconds()

    deletion_thread = threading.Thread(target=run_deletion)
    deletion_thread.daemon = True
    deletion_thread.start()

# Main execution flow
table_name = "deletion_18"

# Fetch data from API for the current date
date_object = datetime.now()
data = fetch_data_from_api(date_object)
if not data:
    print(f"No data found for the entered date: {date_object.strftime('%d/%m/%Y')}")
else:
    # Create a DataFrame with the desired columns
    df = pd.DataFrame(data, columns=[
        'Empcode', 'INTime', 'OUTTime', 'WorkTime', 'OverTime', 'BreakTime', 
        'Status', 'DateString', 'Remark', 'Erl_Out', 'Late_In', 'Name'
    ])
    # Store the data in the database
    store_data(df, table_name)
    print("Data for the specified date:")
    print(df)

# Schedule the deletion task
schedule_deletion(table_name)

# Keep the script running to ensure the deletion task can run
while True:
    time.sleep(1)
