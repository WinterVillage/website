FROM nginx:alpine

WORKDIR /usr/share/nginx/html

# Remove default nginx content
RUN rm -rf ./*

# Copy static site files
COPY ./index.html .
COPY ./resources ./resources

# Copy custom nginx configuration
COPY ./nginx.conf /etc/nginx/conf.d/default.conf

# Do NOT EXPOSE any port here; Coolify will handle port mapping.
CMD ["nginx", "-g", "daemon off;"]