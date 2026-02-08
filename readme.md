 Autonomous Infrastructure Monitoring & Capacity Planning System

## 🚀 Overview
This project is a production-inspired infrastructure monitoring system designed to proactively detect resource bottlenecks and prevent service disruption.

It provisions a Linux server, deploys a real workload using Nginx, continuously monitors CPU, memory, and disk utilization, and triggers automated email alerts when thresholds are breached.

The system promotes a shift from reactive troubleshooting to proactive infrastructure management.

---

## ⭐ Key Features

✅ Automated server provisioning using Bash  
✅ Real-time infrastructure monitoring with Python  
✅ systemd-managed service for high availability  
✅ Intelligent threshold-based alerting  
✅ Automated email notifications for critical events  
✅ Secure credential handling via environment variables  
✅ Production-style logging  

---

## 🧠 Architecture

User Traffic  
↓  
Nginx (Workload)  
↓  
System Resource Consumption  
↓  
Python Monitoring Agent  
↓  
Alert Engine  
↓  
Email Notification  

---

## 🛠 Tech Stack

- AWS EC2 (Ubuntu)
- Python
- Bash
- Nginx
- systemd
- Linux
- SMTP (Email Alerts)

---

## ⚙️ How It Works

The monitoring agent runs as a background service and collects infrastructure metrics at regular intervals.

When resource utilization crosses defined thresholds:

👉 An automated alert is triggered  
👉 A structured email notification is sent  
👉 Operators can take immediate action  

This mimics real-world Site Reliability Engineering practices.

---

## 🔐 Security Best Practices

Sensitive credentials are NOT stored in code.

Environment variables are used to securely manage secrets, aligning with production security standards.

---

## 📈 Why This Project Matters

Infrastructure failures rarely occur instantly — they build over time due to unnoticed capacity strain.

This system demonstrates proactive monitoring and operational awareness, both critical skills for modern DevOps and Cloud Engineers.

---

## 👩‍💻 Author

Devika S.
