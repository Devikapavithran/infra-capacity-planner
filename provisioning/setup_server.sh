#!/bin/bash

echo "=============================="
echo " Starting Server Provisioning "
echo "=============================="

# Update packages
sudo apt update -y
sudo apt upgrade -y

echo "System updated"

# Install Python
sudo apt install python3 -y

echo "Python installed"

# Install Nginx
sudo apt install nginx -y

echo "Nginx installed"

# Start Nginx
sudo systemctl start nginx
sudo systemctl enable nginx

echo "Nginx started successfully"

echo "✅ Server provisioning completed!"
