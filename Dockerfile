# ...existing code...
FROM nginx:alpine

WORKDIR /usr/share/nginx/html

# Remove default nginx content then copy your static site files
RUN rm -rf ./*

COPY ./index.html .
COPY ./resources ./resources

# Do NOT EXPOSE any port here; Coolify will handle port mapping.
CMD ["nginx", "-g", "daemon off;"]
# ...existing code...