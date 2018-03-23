# Pi_secure
If you want to know who comes to your room whenever you are away, or if you want to know which dog ruins your shoes all the time, then this device is for you; with the system we have built you can solve all your mysteries. 
# The Idea
The idea of this project is to detect a motion, and send an email right away, which will contain a link to the stream; on that stream you are able to see whatever triggered the motion detection sensor; to be exact, the whole idea of this project is to solve a mystery
# How? 
To be exact, the idea of this system is to start working whenever the pi boots, so that you don’t have to run a file whenever you want it to work; In order for our pi to work automatically, we have created launcher.sh file, so that our pi runs pir.py file at boot. After overriding some restrictions in the terminal, we have allowed launcher.sh to run at boot.
