# FastAPI

FastAPI implementations
 

## Installation

Installez les librairies en utilisant la commande suivante

```bash
pip3 install fastapi httptools==0.1.* uvloop uvicorn
```

## Lancement du serveur 

```bash
uvicorn main:api --reload
```

Si vous rencontrez un problème, vous pouvez également utiliser la commande suivante

```bash
python3 -m uvicorn main:api --reload
```
Cette commande s'assure de lancer le server web de [FastAPI] (https://fastapi.tiangolo.com/)s à l'aide du package _uvicorn_ installé avec _pip3_.
L'argument _--reload_ permet de mettre à jour automatiquement l'API lorsqu'on effectue des changements du fichier source. Dans la console, on doit observer la ligne suivante:


Dans une autre console, lancez la commande suivante pour faire une requête sur le endpoint /

```bash
curl -X GET http://127.0.0.1:8000/
```

## Documentation


### OpenAPi: 
Ouvrez le endpoint _docs_ dans le navigateur: http://localhost:8000/docs

Vous devriez arriver sur cette interface [OpenAPI](https://www.openapis.org/) (anciennement Swagger).

### ReDoc:  
Ouvrez le endpoint _/redocs_ dans le navigateur: http://localhost:8000/redocs

Cette interface est générée par [ReDoc](https://github.com/Redocly/redoc). 
Enfin, nous pouvons nous rendre au endpoint /openapi.json. 
On retrouvera la déclaration de l'API utilisée par ReDoc et OpenAPI pour générer les documentations:
 

 



