---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/tutorials/local-troubleshooting/
title: Local troubleshooting \u00a0|\u00a0 Knative serving \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:43.520133+00:00
---

# Local troubleshooting  |  Knative serving  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/tutorials/local-troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Local troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows how to troubleshoot a broken Knative serving service using Stackdriver tools for discovery and a local development workflow for investigation.

This step-by-step "case study" companion to the [troubleshooting guide](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/troubleshooting) uses a sample project that results in runtime errors when deployed, which you troubleshoot to find and fix the problem.

## Objectives

  * Write, build, and deploy a service to Knative serving
  * Use Cloud Logging to identify an error
  * Retrieve the container image from Container Registry for a root cause analysis
  * Fix the "production" service, then improve the service to mitigate future problems



**Caution:** Container Registry is deprecated. Effective March 18, 2025, Container Registry is shut down, and writing images to Container Registry is unavailable. For details on the deprecation and how to migrate to Artifact Registry, see [Container Registry deprecation](https://docs.cloud.google.com/container-registry/docs/deprecations/container-registry-deprecation).

## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Cloud Build](https://docs.cloud.google.com/build)
  * [Container Registry](https://docs.cloud.google.com/container-registry)
  * [Knative serving](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)
  * [Cloud Logging](https://docs.cloud.google.com/logging)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

  * This tutorial assumes that you have Knative serving [installed and configured on your cluster](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install).
  * Ensure that your command-line environment is set up and the tools are up-to-date: 
    * [GKE clusters on Google Cloud](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install/on-gcp/command-line-tools)
    * [GKE clusters outside Google Cloud](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/install/outside-gcp/command-line-tools)

  * Install [curl](https://curl.haxx.se/dlwiz/?type=bin) to try out the service.
  * Install [Docker locally](https://docs.docker.com/install/).



## Assembling the code

Build a new Knative serving greeter service step-by-step. As a reminder, this service creates a runtime error on purpose for the troubleshooting exercise.

  1. Create a new project:

###  Node.js 

Create a Node.js project by defining the service package, initial dependencies, and some common operations. 
     1. Create a `hello-service` directory:
            
            mkdir hello-service
            cd hello-service
            

     2. Generate a `package.json` file:
            
            npm init --yes
            npm install express@4
            

     3. Open the new `package.json` file in your editor and configure a `start` script to run `node index.js`. When you're done, the file will look like this:
            
            {
              "name": "hello-service",
              "version": "1.0.0",
              "description": "",
              "main": "index.js",
              "scripts": {
                  "start": "node index.js",
                  "test": "echo \"Error: no test specified\" && exit 1"
              },
              "keywords": [],
              "author": "",
              "license": "ISC",
              "dependencies": {
                  "express": "^4.17.1"
              }
            }

If you continue to evolve this service beyond the immediate tutorial, consider filling in the description, author, and evaluate the license. For more details, read the [package.json documentation](https://docs.npmjs.com/creating-a-package-json-file). 

###  Python 

     1. Create a new `hello-service` directory:
            
            mkdir hello-service
            cd hello-service
            

     2. Create a requirements.txt file and copy your dependencies into it: 
            
            pytest==9.0.3; python_version >= "3.10"
            Flask==3.1.3; python_version >= '3.9'
            gunicorn==23.0.0
            Werkzeug==3.1.9; python_version >= '3.10'
            

###  Go 

     1. Create a `hello-service` directory:
            
            mkdir hello-service
            cd hello-service
            

     2. Create a Go project by initializing a new [go module](https://blog.golang.org/using-go-modules):
            
            go mod init <var>my-domain</var>.com/hello-service
            

You can update the specific name as you wish: you should update the name if the code is published to a web-reachable code repository.

###  Java 

     1. Create a maven project:
            
            mvn archetype:generate \
              -DgroupId=com.example \
              -DartifactId=hello-service \
              -DarchetypeArtifactId=maven-archetype-quickstart \
              -DinteractiveMode=false
            

     2. Copy the dependencies into your `pom.xml` dependency list (between the `<dependencies>` elements):
            
            <dependency>
              <groupId>com.sparkjava</groupId>
              <artifactId>spark-core</artifactId>
              <version>2.9.4</version>
            </dependency>
            <dependency>
              <groupId>org.slf4j</groupId>
              <artifactId>slf4j-api</artifactId>
              <version>2.0.12</version>
            </dependency>
            <dependency>
              <groupId>org.slf4j</groupId>
              <artifactId>slf4j-simple</artifactId>
              <version>2.0.12</version>
            </dependency>
            

     3. Copy the build setting into your `pom.xml` (under the `<dependencies>` elements):
            
            <build>
              <plugins>
                <plugin>
                  <groupId>com.google.cloud.tools</groupId>
                  <artifactId>jib-maven-plugin</artifactId>
                  <version>3.4.0</version>
                  <configuration>
                    <to>
                      <image>gcr.io/PROJECT_ID/hello-service</image>
                    </to>
                  </configuration>
                </plugin>
              </plugins>
            </build>
            

  2. Create an HTTP service to handle incoming requests:

###  Node.js 
         
         const express = require('express');
         const app = express();
         
         app.get('/', (req, res) => {
           console.log('hello: received request.');
         
           const {NAME} = process.env;
           if (!NAME) {
             // Plain error logs do not appear in Stackdriver Error Reporting.
             console.error('Environment validation failed.');
             console.error(new Error('Missing required server parameter'));
             return res.status(500).send('Internal Server Error');
           }
           res.send(`Hello ${NAME}!`);
         });
         const port = parseInt(process.env.PORT) || 8080;
         app.listen(port, () => {
           console.log(`hello: listening on port ${port}`);
         });

###  Python 
         
         import json
         import os
         
         from flask import Flask
         
         
         app = Flask(__name__)
         
         
         @app.route("/", methods=["GET"])
         def index():
             """Example route for testing local troubleshooting.
         
             This route may raise an HTTP 5XX error due to missing environment variable.
             """
             print("hello: received request.")
         
             NAME = os.getenv("NAME")
         
             if not NAME:
                 print("Environment validation failed.")
                 raise Exception("Missing required service parameter.")
         
             return f"Hello {NAME}"
         
         
         if __name__ == "__main__":
             PORT = int(os.getenv("PORT")) if os.getenv("PORT") else 8080
         
             # This is used when running locally. Gunicorn is used to run the
             # application on Cloud Run. See entrypoint in Dockerfile.
             app.run(host="127.0.0.1", port=PORT, debug=True)

###  Go 
         
         // Sample hello demonstrates a difficult to troubleshoot service.
         package main
         
         import (
         	"fmt"
         	"log"
         	"net/http"
         	"os"
         )
         
         func main() {
         	log.Print("hello: service started")
         
         	http.HandleFunc("/", helloHandler)
         
         
         	port := os.Getenv("PORT")
         	if port == "" {
         		port = "8080"
         		log.Printf("Defaulting to port %s", port)
         	}
         
         	log.Printf("Listening on port %s", port)
         	log.Fatal(http.ListenAndServe(fmt.Sprintf(":%s", port), nil))
         }
         
         func helloHandler(w http.ResponseWriter, r *http.Request) {
         	log.Print("hello: received request")
         
         	name := os.Getenv("NAME")
         	if name == "" {
         		log.Printf("Missing required server parameter")
         		// The panic stack trace appears in Cloud Error Reporting.
         		panic("Missing required server parameter")
         	}
         
         	fmt.Fprintf(w, "Hello %s!\n", name)
         }
         

###  Java 
         
         import static spark.Spark.get;
         import static spark.Spark.port;
         
         import org.slf4j.Logger;
         import org.slf4j.LoggerFactory;
         
         public class App {
         
           private static final Logger logger = LoggerFactory.getLogger(App.class);
         
           public static void main(String[] args) {
             int port = Integer.parseInt(System.getenv().getOrDefault("PORT", "8080"));
             port(port);
         
             get(
                 "/",
                 (req, res) -> {
                   logger.info("Hello: received request.");
                   String name = System.getenv("NAME");
                   if (name == null) {
                     // Standard error logs do not appear in Stackdriver Error Reporting.
                     System.err.println("Environment validation failed.");
                     String msg = "Missing required server parameter";
                     logger.error(msg, new Exception(msg));
                     res.status(500);
                     return "Internal Server Error";
                   }
                   res.status(200);
                   return String.format("Hello %s!", name);
                 });
           }
         }

  3. Create a `Dockerfile` to define the container image used to deploy the service:

###  Node.js 
         
         # Use the official lightweight Node.js image.
         # https://hub.docker.com/_/node
         FROM node:20-slim
         # Create and change to the app directory.
         WORKDIR /usr/src/app
         
         # Copy application dependency manifests to the container image.
         # A wildcard is used to ensure copying both package.json AND package-lock.json (when available).
         # Copying this first prevents re-running npm install on every code change.
         COPY package*.json ./
         
         # Install dependencies.
         # if you need a deterministic and repeatable build create a
         # package-lock.json file and use npm ci:
         # RUN npm ci --omit=dev
         # if you need to include development dependencies during development
         # of your application, use:
         # RUN npm install --dev
         
         RUN npm install --omit=dev
         
         # Copy local code to the container image.
         COPY . ./
         
         # Run the web service on container startup.
         CMD [ "npm", "start" ]
         

###  Python 
         
         # Use the official Python image.
         # https://hub.docker.com/_/python
         FROM python:3.14
         
         # Allow statements and log messages to immediately appear in the Cloud Run logs
         ENV PYTHONUNBUFFERED True
         
         # Copy application dependency manifests to the container image.
         # Copying this separately prevents re-running pip install on every code change.
         COPY requirements.txt ./
         
         # Install production dependencies.
         RUN pip install -r requirements.txt
         
         # Copy local code to the container image.
         ENV APP_HOME /app
         WORKDIR $APP_HOME
         COPY . ./
         
         # Run the web service on container startup.
         # Use gunicorn webserver with one worker process and 8 threads.
         # For environments with multiple CPU cores, increase the number of workers
         # to be equal to the cores available.
         # Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run to handle instance scaling.
         CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
         

###  Go 
         
         # Use the official Go image to create a binary.
         # This is based on Debian and sets the GOPATH to /go.
         # https://hub.docker.com/_/golang
         FROM golang:1.25-bookworm as builder
         
         # Create and change to the app directory.
         WORKDIR /app
         
         # Retrieve application dependencies.
         # This allows the container build to reuse cached dependencies.
         # Expecting to copy go.mod and if present go.sum.
         COPY go.* ./
         RUN go mod download
         
         # Copy local code to the container image.
         COPY . ./
         
         # Build the binary.
         RUN go build -v -o server
         
         # Use the official Debian slim image for a lean production container.
         # https://hub.docker.com/_/debian
         # https://docs.docker.com/develop/develop-images/multistage-build/#use-multi-stage-builds
         FROM debian:bookworm-slim
         RUN set -x && apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
             ca-certificates && \
             rm -rf /var/lib/apt/lists/*
         
         # Copy the binary to the production image from the builder stage.
         COPY --from=builder /app/server /server
         
         # Run the web service on container startup.
         CMD ["/server"]
         

###  Java 

This sample uses [Jib](https://github.com/GoogleContainerTools/jib) to build Docker images using common Java tools. Jib optimizes container builds without the need for a Dockerfile or having [Docker](https://www.docker.com/) installed. 
         
         <plugin>
           <groupId>com.google.cloud.tools</groupId>
           <artifactId>jib-maven-plugin</artifactId>
           <version>3.4.0</version>
           <configuration>
             <to>
               <image>gcr.io/PROJECT_ID/hello-service</image>
             </to>
           </configuration>
         </plugin>
         




## Shipping the code

Shipping code consists of three steps: building a container image with Cloud Build, uploading the container image to Container Registry, and deploying the container image to Knative serving.

To ship your code:

  1. Build your container and publish on Container Registry:

###  Node.js 
         
         gcloud builds submit --tag gcr.io/PROJECT_ID/hello-service

Where PROJECT_ID is your Google Cloud project ID. You can check your current project ID with `gcloud config get-value project`.

Upon success, you should see a SUCCESS message containing the ID, creation time, and image name. The image is stored in Container Registry and can be re-used if desired. 

###  Python 
         
         gcloud builds submit --tag gcr.io/PROJECT_ID/hello-service

Where PROJECT_ID is your Google Cloud project ID. You can check your current project ID with `gcloud config get-value project`.

Upon success, you should see a SUCCESS message containing the ID, creation time, and image name. The image is stored in Container Registry and can be re-used if desired. 

###  Go 
         
         gcloud builds submit --tag gcr.io/PROJECT_ID/hello-service

Where PROJECT_ID is your Google Cloud project ID. You can check your current project ID with `gcloud config get-value project`.

Upon success, you should see a SUCCESS message containing the ID, creation time, and image name. The image is stored in Container Registry and can be re-used if desired. 

###  Java 
         
         mvn compile jib:build -Dimage=gcr.io/PROJECT_ID/hello-service

Where PROJECT_ID is your Google Cloud project ID. You can check your current project ID with `gcloud config get-value project`.

Upon success, you should see a BUILD SUCCESS message. The image is stored in Container Registry and can be re-used if desired. 

  2. Run the following command to deploy your app:
         
         gcloud run deploy hello-service --image gcr.io/PROJECT_ID/hello-service

Replace PROJECT_ID with your Google Cloud project ID. `hello-service` is both the container image name and name of the Knative serving service. Notice that the container image is deployed to the service and cluster that you configured previously under Setting up gcloud

Wait until the deployment is complete: this can take about half a minute. On success, the command line displays the service URL.




## Trying it out

Try out the service to confirm you have successfully deployed it. Requests should fail with a HTTP 500 or 503 error (members of the class [5xx Server errors](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes#5xx_Server_errors)). The tutorial walks through troubleshooting this error response.

If your cluster is configured with a routable [default domain](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/default-domain), skip the steps above and instead copy the URL into your web browser.

If you don't use [automatic TLS certificates](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/managed-tls) and [domain mapping](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/mapping-custom-domains) you are not provided a navigable URL for your service.

Instead, use the provided URL and the IP address of the service's ingress gateway to create a `curl` command that can make requests to your service:

  1. To obtain the external IP for the Load Balancer, run the following command:
         
         kubectl get svc istio-ingressgateway -n ASM-INGRESS-NAMESPACE

Replace ASM-INGRESS-NAMESPACE with the namespace where your Cloud Service Mesh ingress is located. Specify `istio-system` if you installed Cloud Service Mesh using its default configuration.

The resulting output looks similar to the following:
         
         NAME                   TYPE           CLUSTER-IP     EXTERNAL-IP  PORT(S)
         istio-ingressgateway   LoadBalancer   XX.XX.XXX.XX   pending      80:32380/TCP,443:32390/TCP,32400:32400/TCP

where the **EXTERNAL-IP** value is your external IP address of the Load Balancer.

  2. Run a `curl` command using this `GATEWAY_IP` address in the URL.
         
         curl -G -H "Host: SERVICE-DOMAIN" https://EXTERNAL-IP/

Replace SERVICE-DOMAIN with the default assigned domain of your service. You can obtain this by taking the default URL and removing the protocol `http://`.

  3. See the HTTP 500 or HTTP 503 error message.




## Investigating the problem

Visualize that the HTTP 5xx error encountered above in Trying it out was encountered as a production runtime error. This tutorial walks through a formal process for handling it. Although production error resolution processes vary widely, this tutorial presents a particular sequence of steps to show the application of useful tools and techniques.

To investigate this problem you will work through these phases:

  * Collect more details on the reported error to support further investigation and set a mitigation strategy.
  * Relieve user impact by deciding to push forward in a fix or rollback to a known-healthy version.
  * Reproduce the error to confirm the correct details have been gathered and that the error is not a one-time glitch
  * Perform a root cause analysis on the bug to find the code, configuration, or process which created this error



At the start of the investigation you have a URL, timestamp, and the message "Internal Server Error".

### Gathering further details

Gather more information about the problem to understand what happened and determine next steps.

Use available tools to collect more details:

  1. [View logs](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/logging) for more details.

  2. Use Cloud Logging to review the sequence of operations leading to the problem, including error messages.




### Rollback to a healthy version

If you have a [revision](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/managing/revisions) that you know was working, you can rollback your service to use that revision. For example, you will not be able to perform a rollback on the new `hello-service` service that you deployed in this tutorial because it contains only a single revision.

To locate a revision and rollback your service:

  1. [List all of the revisions of your service](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/managing/revisions#viewing_the_list_of_revisions_for_a_service).

  2. [Migrate all traffic to the healthy revision](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/rollouts-rollbacks-traffic-migration).




### Reproducing the error

Using the details you obtained previously, confirm the problem consistently occurs under test conditions.

Send the same HTTP request by trying it out again, and see if the same error and details are reported. It may take some time for error details to show up.

Because the sample service in this tutorial is read-only and doesn't trigger any complicating side effects, reproducing errors in production is safe. However, for many real services, this won't be the case: you may need to reproduce errors in a test environment or limit this step to local investigation.

Reproducing the error establishes the context for further work. For example, if developers cannot reproduce the error further investigation may require additional instrumentation of the service.

### Performing a root cause analysis

Root cause analysis is an important step in [effective troubleshooting](https://landing.google.com/sre/sre-book/chapters/effective-troubleshooting/) to ensure you fix the problem instead of a symptom.

Previously in this tutorial, you reproduced the problem on Knative serving which confirms the problem is active when the service is hosted on Knative serving. Now reproduce the problem locally to determine if the problem is isolated to the code or if it only emerges in production hosting.

  1. If you have not used Docker CLI locally with Container Registry, authenticate it with gcloud:
         
         gcloud auth configure-docker

For alternative approaches see [Container Registry authentication methods](https://docs.cloud.google.com/container-registry/docs/advanced-authentication).

  2. If the most recently used container image name is not available, the service description has the information of the most recently deployed container image:
         
         gcloud run services describe hello-service

Find the container image name inside the `spec` object. A more targeted command can directly retrieve it:
         
         gcloud run services describe hello-service \
            --format="value(spec.template.spec.containers.image)"

This command reveals a container image name such as `gcr.io/PROJECT_ID/hello-service`.

  3. Pull the container image from the Container Registry to your environment, this step might take several minutes as it downloads the container image:
         
         docker pull gcr.io/PROJECT_ID/hello-service

Later updates to the container image that reuse this name can be retrieved with the same command. If you skip this step, the `docker run` command below pulls a container image if one is not present on the local machine.

  4. Run locally to confirm the problem is not unique to Knative serving:
         
         PORT=8080 && docker run --rm -e PORT=$PORT -p 9000:$PORT \
            gcr.io/PROJECT_ID/hello-service

Breaking down the elements of the command above,

     * The `PORT` environment variable is used by the service to determine the port to listen on inside the container.
     * The `run` command starts the container, defaulting to the entrypoint command defined in the Dockerfile or a parent container image.
     * The `--rm` flag deletes the container instance on exit.
     * The `-e` flag assigns a value to an environment variable. `-e PORT=$PORT` is propagating the `PORT` variable from the local system into the container with the same variable name.
     * The `-p` flag publishes the container as a service available on localhost at port 9000. Requests to localhost:9000 will be routed to the container on port 8080. This means output from the service about the port number in use will not match how the service is accessed.
     * The final argument `gcr.io/PROJECT_ID/hello-service` is a repository path pointing to the latest version of the container image. If not available locally, docker attempts to retrieve the image from a remote registry.

In your browser, open <http://localhost:9000>. Check the terminal output for error messages that match those on Google Cloud Observability.

If the problem is not reproducible locally, it may be unique to the Knative serving environment. Review the [Knative serving troubleshooting guide](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/troubleshooting) for specific areas to investigate.

In this case the error is reproduced locally.




Now that the error is doubly-confirmed as persistent and caused by the service code instead of the hosting platform, it's time to investigate the code more closely.

For purposes of this tutorial it is safe to assume the code inside the container and the code in the local system is identical.

###  Node.js 

Find the source of the error message in the file `index.js` around the line number called out in the stack trace shown in the logs: 
    
    
    const {NAME} = process.env;
    if (!NAME) {
      // Plain error logs do not appear in Stackdriver Error Reporting.
      console.error('Environment validation failed.');
      console.error(new Error('Missing required server parameter'));
      return res.status(500).send('Internal Server Error');
    }

###  Python 

Find the source of the error message in the file `main.py` around the line number called out in the stack trace shown in the logs: 
    
    
    NAME = os.getenv("NAME")
    
    if not NAME:
        print("Environment validation failed.")
        raise Exception("Missing required service parameter.")

###  Go 

Find the source of the error message in the file `main.go` around the line number called out in the stack trace shown in the logs:
    
    
    name := os.Getenv("NAME")
    if name == "" {
    	log.Printf("Missing required server parameter")
    	// The panic stack trace appears in Cloud Error Reporting.
    	panic("Missing required server parameter")
    }

###  Java 

Find the source of the error message in the file `App.java` around the line number called out in the stack trace shown in the logs:
    
    
    String name = System.getenv("NAME");
    if (name == null) {
      // Standard error logs do not appear in Stackdriver Error Reporting.
      System.err.println("Environment validation failed.");
      String msg = "Missing required server parameter";
      logger.error(msg, new Exception(msg));
      res.status(500);
      return "Internal Server Error";
    }

Examining this code, the following actions are taken when the `NAME` environment variable is not set:

  * An error is logged to Google Cloud Observability
  * An HTTP error response is sent



The problem is caused by a missing variable, but the root cause is more specific: the code change adding the hard dependency on an environment variable did not include related changes to deployment scripts and runtime requirements documentation.

## Fixing the root cause

Now that we have collected the code and identified the potential root cause, we can take steps to fix it.

  * Check whether the service works locally with the `NAME` environment available in place:

    1. Run the container locally with the environment variable added:
           
           PORT=8080 && docker run --rm -e PORT=$PORT -p 9000:$PORT \
            -e NAME="Local World!" \
            gcr.io/PROJECT_ID/hello-service

    2. Navigate your browser to <http://localhost:9000>

    3. See "Hello Local World!" appear on the page

  * Modify the running Knative serving service environment to include this variable:

    1. Run the services update command with the `--update-env-vars` parameter to add an environment variable:
           
           gcloud run services update hello-service \
             --update-env-vars NAME=Override
           

    2. Wait a few seconds while Knative serving creates a new revision based on the previous revision with the new environment variable added.

  * Confirm the service is now fixed:

    1. Navigate your browser to the Knative serving service URL.
    2. See "Hello Override!" appear on the page.
    3. Verify that no unexpected messages or errors appear in Cloud Logging.



## Improving future troubleshooting speed

In this sample production problem, the error was related to operational configuration. There are code changes that will minimize the impact of this problem in the future.

  * Improve the error log to include more specific details.
  * Instead of returning an error, have the service fall back to a safe default. If using a default represents a change to normal functionality, use a warning message for monitoring purposes.



Let's step through removing the `NAME` environment variable as a hard dependency.

  1. Remove the existing `NAME`-handling code:

###  Node.js 
         
         const {NAME} = process.env;
         if (!NAME) {
           // Plain error logs do not appear in Stackdriver Error Reporting.
           console.error('Environment validation failed.');
           console.error(new Error('Missing required server parameter'));
           return res.status(500).send('Internal Server Error');
         }

###  Python 
         
         NAME = os.getenv("NAME")
         
         if not NAME:
             print("Environment validation failed.")
             raise Exception("Missing required service parameter.")

###  Go 
         
         name := os.Getenv("NAME")
         if name == "" {
         	log.Printf("Missing required server parameter")
         	// The panic stack trace appears in Cloud Error Reporting.
         	panic("Missing required server parameter")
         }

###  Java 
         
         String name = System.getenv("NAME");
         if (name == null) {
           // Standard error logs do not appear in Stackdriver Error Reporting.
           System.err.println("Environment validation failed.");
           String msg = "Missing required server parameter";
           logger.error(msg, new Exception(msg));
           res.status(500);
           return "Internal Server Error";
         }

  2. Add new code that sets a fallback value:

###  Node.js 
         
         const NAME = process.env.NAME || 'World';
         if (!process.env.NAME) {
           console.log(
             JSON.stringify({
               severity: 'WARNING',
               message: `NAME not set, default to '${NAME}'`,
             })
           );
         }

###  Python 
         
         NAME = os.getenv("NAME")
         
         if not NAME:
             NAME = "World"
             error_message = {
                 "severity": "WARNING",
                 "message": f"NAME not set, default to {NAME}",
             }
             print(json.dumps(error_message))

###  Go 
         
         name := os.Getenv("NAME")
         if name == "" {
         	name = "World"
         	log.Printf("warning: NAME not set, default to %s", name)
         }

###  Java 
         
         String name = System.getenv().getOrDefault("NAME", "World");
         if (System.getenv("NAME") == null) {
           logger.warn(String.format("NAME not set, default to %s", name));
         }

  3. Test locally by re-building and running the container through the affected configuration cases:

###  Node.js 
         
         docker build --tag gcr.io/PROJECT_ID/hello-service .

###  Python 
         
         docker build --tag gcr.io/PROJECT_ID/hello-service .

###  Go 
         
         docker build --tag gcr.io/PROJECT_ID/hello-service .

###  Java 
         
         mvn compile jib:build

Confirm the `NAME` environment variable still works:
         
         PORT=8080 && docker run --rm -e $PORT -p 9000:$PORT \
          -e NAME="Robust World" \
          gcr.io/PROJECT_ID/hello-service

Confirm the service works without the `NAME` variable:
         
         PORT=8080 && docker run --rm -e $PORT -p 9000:$PORT \
          gcr.io/PROJECT_ID/hello-service

If the service does not return a result, confirm the removal of code in the first step did not remove extra lines, such as those used to write the response.

  4. Deploy this by revisiting the Deploy your code section.

Each deployment to a service creates a new revision and automatically starts serving traffic when ready.

To clear the environment variables set earlier:

`gcloud run services update hello-service --clear-env-vars`




Add the new functionality for the default value to automated test coverage for the service.

## Finding other issues in the logs

You may see other issues in the Log Viewer for this service. For example, an unsupported system call will appear in the logs as a "Container Sandbox Limitation".

For example, the Node.js services sometimes result in this log message:
    
    
    Container Sandbox Limitation: Unsupported syscall statx(0xffffff9c,0x3e1ba8e86d88,0x0,0xfff,0x3e1ba8e86970,0x3e1ba8e86a90). Please, refer to https://gvisor.dev/c/linux/amd64/statx for more information.
    

In this case, the lack of support does not impact the hello-service sample service.

## Clean up

You can delete the resources created for this tutorial to avoid incurring costs.

### Deleting tutorial resources

  1. Delete the Knative serving service you deployed in this tutorial:
         
         gcloud run services delete SERVICE-NAME

Where SERVICE-NAME is your chosen service name.

You can also delete Knative serving services from the Google Cloud console:

[Go to Knative serving](https://console.cloud.google.com/kubernetes/run)

  2. Remove the gcloud default configurations you added during the tutorial setup:
         
         gcloud config unset run/platform
          gcloud config unset run/cluster
          gcloud config unset run/cluster_location
         

  3. Remove the project configuration:
         
         gcloud config unset project
         

  4. Delete other Google Cloud resources created in this tutorial:

     * [Delete the container image](https://docs.cloud.google.com/container-registry/docs/managing#deleting_images) named `gcr.io/<var>PROJECT_ID</var>/hello-service` from Container Registry.
     * If you created a cluster for this tutorial, [delete the cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deleting-a-cluster).



## What's next

  * Learn more about how to use [Cloud Logging](https://docs.cloud.google.com/logging/docs) to gain insight into production behavior.
  * For more about [Knative serving troubleshooting](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/troubleshooting).
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
