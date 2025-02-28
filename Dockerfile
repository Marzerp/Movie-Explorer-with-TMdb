# Usar Nginx como servidor web
FROM nginx:latest

# Copiar hello.html a la carpeta pública de Nginx
COPY ./www/index.html /usr/share/nginx/html/

# Exponer el puerto 80
EXPOSE 80

# Ejecutar Nginx en primer plano
CMD ["nginx", "-g", "daemon off;"]
