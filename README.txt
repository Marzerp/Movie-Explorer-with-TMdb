Para construir:

docker run  -it mi-proyecto 

Para correr:

docker run -it mi-proyecto
docker run -it -v "$(pwd)/KEY.dat:/app/KEY.dat" mi-proyecto

IMPORTANTE:

Verificar que KEY.dat NO APAREZCA en .dockerignore. De otra manera falla el open al archivo.
