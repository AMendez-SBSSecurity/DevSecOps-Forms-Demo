
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import csv_operations
import git_operations
import configparser
def logic(update_changes, id,food,note):
    git_operations.clone_repo("./Automation","github.com/AMendez-SBSSecurity/DevSecOps-Demo.git")
    csv_operations.fnctUpdatel_ine("./Automation/menu_person.csv","99","0,1,2",id,food,note)
    #TODO Send mail
    body =f'Hi {id},\n Your order of: {food} Has been successfully registered'
    send_email(id + "Order Summary", body)
    if update_changes:
        git_operations.push_changes("./Automation")
    if os.path.exists("./Automation"):
        os.system('cmd /c "rmdir /s /Q Automation"')


    
    print()

def third_logic(id,food,note):
    if os.path.exists("./Automation"):
        os.system('cmd /c "rmdir /s /Q Automation"')
    git_operations.clone_repo("./Automation","github.com/AMendez-SBSSecurity/DevSecOps-WebApp-Demo.git")
    csv_operations.fnctUpdatel_ine("./Automation/static/data.csv","99","0,1,2",id,food,note)

    #Update Page Parameter
    config = configparser.ConfigParser()
    config.read("./Automation/app.properties")
    config.set("Page","appState", "True")
    with open("./Automation/app.properties", "w") as file:
        config.write(file)
    git_operations.push_changes("./Automation")
    if os.path.exists("./Automation"):
        os.system('cmd /c "rmdir /s /Q Automation"')
    #TODO Send mail


    
    print()

# Define your email configuration
EMAIL_FROM = "andresmendez9896@gmail.com"
EMAIL_TO_1 = "andresmendez9896@gmail.com"
EMAIL_TO_2 = "sergio.bascon@sbssecurity.io"

def send_email(subject, body):
    receivers = [EMAIL_TO_1, EMAIL_TO_2]
    msg = MIMEMultipart()
    msg["From"] = EMAIL_FROM
    msg["To"] = ', '.join(receivers)
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)  # Use your SMTP server and port
        server.starttls()
        server.login("andresmendez9896@gmail.com","habwnknmrartdvuf")
        server.sendmail(EMAIL_FROM, receivers, msg.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Error sending email: {e}")

