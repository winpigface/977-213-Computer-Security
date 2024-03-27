sudo docker build -t add-demo .
sudo docker run -d -p 2223:1337 --name add-demo add-demo
sudo docker ps
