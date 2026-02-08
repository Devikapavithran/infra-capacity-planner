import psutil
import time
from datetime import datetime
import smtplib
from email.message import EmailMessage
import os

log_file = "/var/log/system_monitor.log"

CPU_THRESHOLD = 1
MEMORY_THRESHOLD = 70
DISK_THRESHOLD = 80
def send_email_alert(subject, body):
    sender = "devikapavithran3002@gmail.com"
    receiver = "devikapavithran3002@gmail.com"
    app_password = os.getenv("EMAIL_PASSWORD")

    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = receiver

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, app_password)
        smtp.send_message(msg)
while True:
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    timestamp = datetime.now()

    log_entry = f"{timestamp} | CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%\n"

    print(log_entry)

    with open(log_file, "a") as f:
        f.write(log_entry)

    # 🚨 ALERT LOGIC
   # 🚨 ALERT LOGIC

if cpu > CPU_THRESHOLD:
    alert_msg = f"🚨 High CPU Usage detected: {cpu}%"
    print(alert_msg)
    send_email_alert("CPU ALERT", alert_msg)

if memory > MEMORY_THRESHOLD:
    alert_msg = f"🚨 High Memory Usage detected: {memory}%"
    print(alert_msg)
    send_email_alert("MEMORY ALERT", alert_msg)

if disk > DISK_THRESHOLD:
    alert_msg = f"🚨 CRITICAL: Disk Usage detected at {disk}%"
    print(alert_msg)
    send_email_alert("DISK ALERT", alert_msg)

    time.sleep(5)

