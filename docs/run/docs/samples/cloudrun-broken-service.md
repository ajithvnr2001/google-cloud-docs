---
url: https://docs.cloud.google.com/run/docs/samples/cloudrun-broken-service/
title: Service for local troubleshooting \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:25.874529+00:00
---

# Service for local troubleshooting  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/samples/cloudrun-broken-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Samples ](https://docs.cloud.google.com/run/docs/samples)



#  Service for local troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

Sample demonstrating an easily broken service that is difficult to troubleshoot without careful investigation, and an improved version of the code.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Local troubleshooting](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/tutorials/local-troubleshooting)
  * [Tutorial: Local troubleshooting of a Cloud Run service](https://docs.cloud.google.com/run/docs/tutorials/local-troubleshooting)



## Code sample

### Go

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    

### Java

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### Node.js

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### Python

To authenticate to Cloud Run, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudrun). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
