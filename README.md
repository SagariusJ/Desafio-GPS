# Desafio GPS Microservicios
El desafio fue realizado en python version 3.12 utilizando el framework de FastAPI.
## CONSIDERACIONES
Al levantar el proyecto con el comando: 
```bash
docker compose up -d --build
```
Existe la probabilidad de que los microservicios se creen pero no se inicializen en primera instancia, al levantar por segunda vez el proyecto (sin la necesidad de build) funcionará de manera correcta.
