# Instruction

* Please use an Ubuntu machine to do this lab exercise. You can access one in the lab room.

* Make sure your machine has docker installed. If it's not, please install docker: https://docs.docker.com/engine/install/ubuntu/

* Read the introduction to docker: https://docker-curriculum.com/#introduction

* This demo folder implements docker-based xinetd service for running ./deploy/chal.py over the network. 

* To run this demo, go to terminal. In terminal, make sure you are in ./demo folder and run 'sudo sh docker_start.sh'

* After running the demo, you should be able to access ./deploy/chal.py over the network from your IP address at port 1337. To do so, run 'nc localhost 1337'. You can also access via your friend's computer (if both of your computers can discover each other, e.g., in the same LAN). To access your friend's program, run 'nc your-friend-ip 1337'

* After you are done with this, you can exit and kill this container by running 'sudo sh docker_kill.sh'.


