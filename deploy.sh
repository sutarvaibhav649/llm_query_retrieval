#!/bin/bash
echo "Starting deployment..."
git pull origin main
# Add other deployment commands as needed, e.g.:
# pip install -r requirements.txt
# systemctl restart your_fastapi_service
echo "Deployment completed."
