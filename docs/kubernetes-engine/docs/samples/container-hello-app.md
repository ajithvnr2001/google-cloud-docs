---
url: https://docs.cloud.google.com/kubernetes-engine/docs/samples/container-hello-app/
title: Hello app source code \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:28:27.000823+00:00
---

# Hello app source code  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/samples/container-hello-app/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Samples ](https://docs.cloud.google.com/kubernetes-engine/docs/samples)



#  Hello app source code Stay organized with collections  Save and categorize content based on your preferences. 

Source code for GKE Hello app server.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Deploy an app to a GKE cluster](https://docs.cloud.google.com/kubernetes-engine/docs/deploy-app-cluster)



## Code sample

### Go

To authenticate to GKE, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    package main
    
    import (
    	"fmt"
    	"log"
    	"net/http"
    	"os"
    )
    
    func main() {
    	// register hello function to handle all requests
    	mux := http.NewServeMux()
    	mux.HandleFunc("/", hello)
    
    	// use PORT environment variable, or default to 8080
    	port := os.Getenv("PORT")
    	if port == "" {
    		port = "8080"
    	}
    
    	// start the web server on port and accept requests
    	log.Printf("Server listening on port %s", port)
    	log.Fatal(http.ListenAndServe(":"+port, mux))
    }
    
    // hello responds to the request with a plain-text "Hello, world" message.
    func hello(w http.ResponseWriter, r *http.Request) {
    	log.Printf("Serving request: %s", r.URL.Path)
    	host, _ := os.Hostname()
    	fmt.Fprintf(w, "Hello, world!\n")
    	fmt.Fprintf(w, "Version: 1.0.0\n")
    	fmt.Fprintf(w, "Hostname: %s\n", host)
    }
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=container). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
