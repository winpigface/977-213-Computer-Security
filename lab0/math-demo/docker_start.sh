sudo docker build -t math-demo .
sudo docker run -d -p 2224:1337 --name math-demo math-demo
sudo docker ps
