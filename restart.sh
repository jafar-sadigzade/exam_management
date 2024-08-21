#!/bin/bash

# Reload the systemd manager configuration
sudo systemctl daemon-reload

# Restart the Gunicorn service
sudo systemctl restart gunicorn

# Test the Nginx configuration
sudo nginx -t

# If the Nginx configuration test is successful, restart Nginx
sudo systemctl restart nginx
