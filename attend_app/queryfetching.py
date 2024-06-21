import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

# db URL
database_url = "postgresql+psycopg2://default:5VsuIBhUnkP1@ep-wild-field-a1xpuji5.ap-southeast-1.aws.neon.tech:5432/verceldb?sslmode=require"
engine = create_engine(database_url)

# query 
def query_data(table_name, date):
    print(f"Querying data for date: {date} in table: {table_name}")  # Debugging line
    query = f"""
    SELECT "Empcode", "INTime", "OUTTime", "WorkTime", "OverTime", "BreakTime", 
           "Status", "DateString", "Remark", "Erl_Out", "Late_In", "Name"
    FROM {table_name}
    WHERE "DateString" = '{date}'
    """
    df = pd.read_sql(query, con=engine)
    return df

#fetch  data 
def fetch_all_data(table_name):
    query = f"SELECT * FROM {table_name} LIMIT 25"
    df = pd.read_sql(query, con=engine)
    return df

# data input
table_name = "attendance_data"  
date_input = input("Enter the date (dd/mm/yyyy): ")

# Validate the date format
try:
    datetime.strptime(date_input, '%d/%m/%Y')
except ValueError:
    print("Incorrect date format, should be dd/mm/yyyy")
else:
    # Query the database with the provided date
    data = query_data(table_name, date_input)
    if data.empty:
        print(f"No data found for the entered date: {date_input}")
    else:
        #print("Data for the specified date:")
        print(data)
    #Optional: Fetch some data for debugging
    # debug_data = fetch_all_data(table_name)
    # print("Sample data from the table for debugging:")
    # print(debug_data)

#SCHEDULE
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# TO STORE THE DATA

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


# # # API variables
# # empcode = "ALL"
# # previousdate = 1/9/2023
# # #(datetime.now() - timedelta(days=1)).strftime('%d-%m-%Y')
# # presentdate = 7/6/2024
# # #datetime.now().strftime('%d-%m-%Y')


# # API URL and key
# api_url = "https://api.etimeoffice.com/api/DownloadInOutPunchData?Empcode=ALL&FromDate=01/09/2023&ToDate=07/06/2024"
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

#/////////////////////////////                   ///////////////////////                 //////////////////////         //////////  /




# import pandas as pd
# from sqlalchemy import create_engine
# import requests
# import base64
# import schedule
# import time
# from datetime import datetime, timedelta


# database_url = "postgresql+psycopg2://default:5VsuIBhUnkP1@ep-wild-field-a1xpuji5.ap-southeast-1.aws.neon.tech:5432/verceldb?sslmode=require"
# engine = create_engine(database_url)



# api_url = "https://api.etimeoffice.com/api/DownloadInOutPunchData?Empcode=ALL&FromDate=01/09/2023&ToDate=07/06/2024"
# api_key = "ORANGEDATATECH:HR@Orange:UY7g2#!gWEA6kB8:true"


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


# punch_data = entry_dataALL.get('InOutPunchData', [])


# df = pd.DataFrame(punch_data, columns=[
#     'Empcode', 'INTime', 'OUTTime', 'WorkTime', 'OverTime', 'BreakTime', 
#     'Status', 'DateString', 'Remark', 'Erl_Out', 'Late_In', 'Name'
# ])


# table_name = 'employee'


# df.to_sql(name=table_name, con=engine, if_exists='append', index=False)

# print(f'DataFrame successfully stored in table "{table_name}"')
