#Display the empcode whose intime is not present & also send the email
#Need view
import pandas as pd
from sqlalchemy import create_engine
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Database URL
database_url = "postgresql+psycopg2://default:5VsuIBhUnkP1@ep-wild-field-a1xpuji5.ap-southeast-1.aws.neon.tech:5432/verceldb?sslmode=require"
engine = create_engine(database_url)

# Email configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'pravinmewada1999@gmail.com'  # Your email address
smtp_password = 'nczy qogr vofn kmcv'  # Your email password

# Function to send email
def send_email(to_address, subject, body):
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = to_address
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        text = msg.as_string()
        server.sendmail(smtp_username, to_address, text)
        server.quit()
        print(f"Email sent to {to_address}")
    except Exception as e:
        print(f"Failed to send email to {to_address}: {e}")

# Main execution flow
if __name__ == "__main__":
    table_name = "attend_app_count_number"
    employee_details_table = "attend_app_employee_details"
    date_input = input("Enter the date (dd/mm/yyyy): ")

    # Validate the date format
    try:
        date_object = datetime.strptime(date_input, '%d/%m/%Y')
    except ValueError:
        print("Incorrect date format, should be dd/mm/yyyy")
    else:
        formatted_date = date_object.strftime('%d/%m/%Y')

        # Query to fetch attendance data for the given date
        query = f"""
            SELECT * FROM {table_name}
            WHERE DateString = '{formatted_date}'
        """
        df = pd.read_sql(query, engine)

        # Filter based on null or '--:--' entries in INTime
        filtered_df = df[(df['intime'].isnull()) | (df['intime'] == '--:--')]

        if filtered_df.empty:
            print(f"No people found with missing entries on {date_input}")
        else:
            emp_codes_with_issues = filtered_df['empcode'].tolist()
            print(f"Empcodes with missing entries on {date_input}: {emp_codes_with_issues}")

            # Query to fetch email addresses for the employees with missing INTime
            emp_codes_str = "','".join(emp_codes_with_issues)
            email_query = f"""
                SELECT emp_code, email FROM {employee_details_table}
                WHERE emp_code IN ('{emp_codes_str}')
            """
            email_df = pd.read_sql(email_query, engine)

            # Send emails to employees with missing INTime
            for index, row in email_df.iterrows():
                emp_code = row['emp_code']
                email = row['email']
                subject = "Missing In Time Alert"
                body = f"""Hi,\n\nYou have a missing In time entry on {date_input}. Please rectify this as soon as possible.\n\nThank you."""
                send_email(email, subject, body)

            print(f"Emails sent to employees with missing INTime on {date_input}")

            # Print the DataFrame for verification
            print("Data for the specified date:")
            print(df)
