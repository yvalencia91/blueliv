# Requirements  

* The software must be able to scale to millions of users requesting the list of occurrences  
  ```
  Create a fargate cluster with autoscaling and metrics
  setup up. Depending on network in or CPU/Memory 
  performance trigger the autoscaling.
  
  One point that I'm missing is the fact to apply a cache
  strategy in the API. I was thinking on doing a 'lazy
  cache' strategy given the fact that data is updated 
  once a day. I'm showing how it works in the image 
  'Cloud_solution_blueliv.png'
  ```
* Scraping will only be done once a day, on a schedule.
  ```
  I'm simulating different days by sleeping 10 seconds 
  in the main loop.
  
  Another option for this could be using a crontab or 
  scheduler with a lambda function.
  ```
* API must be secure
  ```
  Both the GET and POST methods on the path /threat
  require a jwt token.
  
  I'm leaving registry and login open just for the 
  the demo.
  ```
* Explain how you would provide visibility in production for Errors, Metrics and Alerts.
  ```
  For this I'm implementing a single-node EKA stack
  (elasticsearch + kibana + apm server). I've configured
  them inside the same network so the api service will
  resolve the DNS through the service name.
  
  Elasticsearch has a Observability module which will
  help us detect Errors, design metrics and report Alerts
  ```
* Show a diagram with named components of the production infrastructure to be able to scale
  ```
  Shown in the image. Fargate Cluster should be configured
  for autoscaling.
  ```
