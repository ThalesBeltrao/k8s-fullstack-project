FROM nginx:alpine

# Remove config padrão
RUN rm -f /etc/nginx/conf.d/default.conf

# Copia sua config
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copia os arquivos do site
COPY . /usr/share/nginx/html

# Garante que o nginx fique em foreground
CMD ["nginx", "-g", "daemon off;"]
