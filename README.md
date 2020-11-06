# cse138-project2
 The source code for a web server that provides a REST interface,  
 along with a Docker file to create a container that runs it.  
 The web server is built in python, using the Django framework.
 
 ## Capabilities
 
 The web server supports one endpoints, `kvs/`.
 
 `kvs/<key>` links to a key-value store that supports  
    a. Inserting new key-value pairings through PUT.  
    b. Updating the value of an existing key through PUT.  
    c. Getting the value of an existing key through GET.  
    d. Deleting an existing key through DELETE.  

 The server can run in either in main or follower mode.  
 Main instances receive and respond directly to requests.
 Follower instances receive requests and forward them to a main instance.  
 Follower mode is instantiated through the environmental variable FORWARDING_ADDRESS. 

 By default main instances are linked to port 13800.
 
 ## Limitations
 
 Invalid HTTP methods return the string `This method is unsupported.` and the status code 405.  
 Invalid endpoints return status code 404.   
 Follower requests will return the status code 503 on timeout. 


Written for CSE 138 Fall 20 with Professor Peter Alvaro at UCSC.

