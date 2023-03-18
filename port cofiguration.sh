##Port cofiguration for multiple site
https://github.com/frappe/bench/wiki/Multitenant-Setup

# Switch off DNS based multitenancy
bench config dns_multitenant off
# Create new-site 
bench new-site {site_name}

# Set port
bench set-nginx-port {site_name} 82 

# Re generate nginx config
bench setup nginx

# Reload nginx
sudo service nginx reload

# Reload supervisor
sudo service supervisor restart