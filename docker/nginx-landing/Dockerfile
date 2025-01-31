FROM nginx:latest

# Set working directory
WORKDIR /usr/share/nginx/html

# Copy default index.html and styles.css into the container image
COPY index.html /usr/share/nginx/html/index.html
COPY styles.css /usr/share/nginx/html/styles.css

# Copy custom Nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf
