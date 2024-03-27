sudo docker build -t ctf-docker .
sudo docker run -d -p 2222:1337 --name ctf-docker ctf-docker
#sudo docker run -d -p 127.0.0.1:1337:1337/tcp --name ctf-docker ctf-docker
sudo docker ps
