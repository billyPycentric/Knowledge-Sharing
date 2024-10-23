# HTTPx VS REQUESTS   
What are Request in python   
Basically what Requests are in python , they are standard module(a file that can be imported , has functions and classes) for sending and receiving HTTP request in python.   

What are Httpx in python   
It is basically mordified Request, it is also a HTTP library just that it was implemented to handle asynchronous requests natively(Perforig multiple http requests concurrently) it supports HTTP/1.1 and HTTP/2 and it can handle auth and proxies(Gateway between use and internet) , redirects   

Why HTTPx over Request   
* JSON , decoding   
* Handles Asychronous Programming   
* Http/1.1 and http/2 support   
## Core feats for ***REQUESTS***   
1. Cookie Handling   
2. Session Handling   
3. Multiple file uploads      

## Differences   
Pros -> hasnt been around long enough   
Cons -> supports http/2   
Pros -> has been around long enough   
Cons-> doesnt support http/2 