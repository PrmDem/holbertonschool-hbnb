FROM ubuntu:latest
# choisir ubuntu la derniere version
RUN apt-get update && apt-get upgrade -y
#l installer unbuntu
RUN apt-get install -y python3 python3-pip build-essential python3-dev libpq-dev
#installer python3
WORKDIR /docker
#choisir dossier repertoire de travail
COPY requirements.txt .
#copy requierments.txt probleme de l installation
RUN pip install --no-cache-dir --break-system-packages -r requirements.txt
#installer env
COPY . .
#tout copier
EXPOSE  5000
#choisir le port du server
CMD [ "python3", "run.py" ]
#lancer le serveur
