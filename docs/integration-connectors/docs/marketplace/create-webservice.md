---
url: https://docs.cloud.google.com/integration-connectors/docs/marketplace/create-webservice/
title: Create a web service \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:41:35.175378+00:00
---

# Create a web service  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/marketplace/create-webservice/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — BigQuery Connector**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

# Create a web service

This page describes how to create a web service in the VM using the Gin web framework that is written in Golang. You can choose to create the web service in any other framework that you want to use. 

  1. To download the Go package in the VM, run the following command in the VM: 
         
         wget https://go.dev/dl/go1.22.5.linux-amd64.tar.gz
           

  2. Install Go in the VM. For information, see [Install Go](https://go.dev/doc/install).
  3. To create a new directory for the web service, run the following command: 
         
         mkdir SERVICE_REPO
           cd SERVICE_REPO
           




### Additional considerations

When you create a web service, you must be aware of the following considerations: 

  * Inputs that you require during VM creation are available as environment variables and have the following prefix: `CONNECTOR_ENV_`.
  * When you set up the web service, use the environment variables to read such values.
  * Only values that are required to set up the web service must be taken as input during the VM creation.
  * The port of the service must be taken as input from the CONNECTOR_ENV_PORT variable.
  * Use other environment variables for optional inputs.
  * You can also get inputs during connection creation. You can define these fields when you create the custom connector and pass them as path, query, or headers in each API call.
  * Ensure that the server runs on the localhost.



### Logging

Log the required information and push the logs to Cloud Logging. This helps connector consumers track and debug failures. To publish logs to Cloud Logging, you can use the following Cloud Logging client available in Go: <https://pkg.go.dev/cloud.google.com/go/logging#NewClient>

You must initialize the logger in main and add a middleware in Gin to track all the incoming requests. You must track the method, path, status, and latency for a request. To filter the logs, use the appropriate severity while logging. In the web service, read the log level from the environment variable. The log level is taken as optional input from during the VM creation. By default, Info logs can be used. The following are the log levels: 

  * DEBUG: logs every part of the request including the HTTP request/response traces.
  * INFO: logs service startup, service shutdown, requests, and other information.
  * ERROR: logs request failure, formatting exceptions, and other errors.



### Graceful shutdown

Set up the server to gracefully shutdown and handle the in progress requests. For information about how to gracefully restart or stop the server, see [Graceful restart or stop](https://gin-gonic.com/docs/examples/graceful-restart-or-stop/). 

### Concurrency

Gin servers inherently support concurrent requests using Go routines. By default, an undefined number of requests are allowed to be processed by Go routines. However, in some cases, when requests are expected to be resource intensive, use worker pools to restrict and buffer the requests on the server. For more information, see [Worker pools example](https://gobyexample.com/worker-pools). 

### Test and build the binary

  1. Set the port and run the server by using the following commands:
    
    EXPORT CONNECTOR_ENV_PORT = 8081
    go get .
    go run .

These commands bundle the required libraries and run the server. 

  2. To verify the server, run the following curl command on the VM: 
         
         curl -X POST -H "Content-Type: application/json" -H "X-Custom-Header: MyValue" -d '{"name": "Alice", "address": "123 Main St", "gender": "F"}' http://localhost:8081/postData/456
         
         curl -v http://localhost:8081/getData -H "TestKey: MyValue"

  3. Create the binary and use it as the VM image by using the following command: 
         
         go build -o SERVICE_NAME

  4. Move the binary to the root folder by using the following command: 
         
         sudo cp SERVICE_NAME /opt

  5. Run the service again to verify that the binary is working as expected by using the following command: 
         
         sudo chmod +x SERVICE_NAME
         ./SERVICE_NAME




### Containerize the application

  1. Install Docker. For information, see [Install Docker](https://docs.docker.com/engine/install/debian/).
  2. Create a Docker file to run binaries. 
         
         FROM alpine:latest
         WORKDIR /opt
         COPY . .
         CMD ["./SERVICE_NAME"]

  3. Build the connector container by using the following command: 
         
         sudo docker build -t connector-container .

  4. Run the docker container. Set `--restart=unless-stopped` to restart the service in case of unexpected failure.



#### Container level task

All logs in stdout can be routed to Cloud Logging by using the gcplogs Log driver while running the docker container. This helps to track the startup or unexpected failure or shutdown of the service. 

To route the logs to Cloud Logging, run the following command: 
    
    
      sudo docker run --name connector-service -e
      CONNECTOR_ENV_PORT=$CONNECTOR_ENV_PORT -p
      $CONNECTOR_ENV_PORT:$CONNECTOR_ENV_PORT --restart=unless-stopped ----log-driver=gcplogs connector-container

## What's next

  * Learn how to [create a custom connector](https://docs.cloud.google.com/integration-connectors/docs/marketplace/create-custom-connector).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
