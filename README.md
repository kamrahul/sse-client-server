# sse-client-server
This project explains the SSE from a flask server running in port 7001 to a angular client application which runs at port 4200 which receives messages on realtime without getting a longpooled messages.

 # Ngrok setup ( Optional Setup)

 ## Download ng rok 
 > https://dashboard.ngrok.com/

 ## Run command to setup 
 <pre>
  sudo cp ngrok /usr/local/bin      
</pre>    

 ## Setup you token
 <pre>
 ngrok config add-authtoken <yourToken>
 </pre>

## Run command
<pre>
 ngrok http 80
 </pre>



# Run the flask server 
> Go to flask-server>server_app.py 
> This will run the server in port 7001

# Run the angular client application
> Go to angular-client>sse-client

### Follow these commands

<pre>
> npm install
> ng serve
</pre>
This will serve application in port 4200


# Checking the SSE working
> Open localhost:4200 and you can see the application is running and you get the time as response sent from server which is running under localhost:7001/stream

# NgRok configuration
## Run Ngrok for port 7001
<pre>
ngrok http 7001
</pre>
### This command will forward localhost 7001 to online port 
<pre>
Forwarding                    https://6f5f-103-154-37-20.in.ngrok.io -> http://localhost:7001    
</pre>

## Check ngrok connection visting the forwarded url
> https://6f5f-103-154-37-20.in.ngrok.io/hello/rahul




# Resources 
- https://stackoverflow.com/questions/12232304/how-to-implement-server-push-in-flask-framework

- https://itnext.io/event-source-with-angular-c9f7f5369082