---
url: https://docs.cloud.google.com/logging/docs/samples/logging-stdlogging/
title: Write standard logs \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:10.623583+00:00
---

# Write standard logs  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/samples/logging-stdlogging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Samples ](https://docs.cloud.google.com/logging/docs/samples)



#  Write standard logs Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to use Cloud Logging in a standard library-compatible way.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Setting Up Cloud Logging for Go](https://docs.cloud.google.com/logging/docs/setup/go)



## Code sample

### Go

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Sample stdlogging writes log.Logger logs to the Cloud Logging.
    package main
    
    import (
    	"context"
    	"log"
    
    	"cloud.google.com/go/logging"
    )
    
    func main() {
    	ctx := context.Background()
    
    	// Sets your Google Cloud Platform project ID.
    	projectID := "YOUR_PROJECT_ID"
    
    	// Creates a client.
    	client, err := logging.NewClient(ctx, projectID)
    	if err != nil {
    		log.Fatalf("Failed to create client: %v", err)
    	}
    	defer client.Close()
    
    	// Sets the name of the log to write to.
    	logName := "my-log"
    
    	logger := client.Logger(logName).[StandardLogger](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/logging/latest/index.html#cloud_google_com_go_logging_Logger_StandardLogger)(logging.[Info](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/logging/latest/index.html#cloud_google_com_go_logging_Default_Debug_Info_Notice_Warning_Error_Critical_Alert_Emergency))
    
    	// Logs "hello world", log entry is visible at
    	// Cloud Logs.
    	logger.Println("hello world")
    }
    

### Python

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Imports the Cloud Logging client library
    import google.cloud.logging
    
    # Instantiates a client
    client = google.cloud.logging.[Client](https://docs.cloud.google.com/python/docs/reference/logging/latest/google.cloud.logging_v2.client.Client.html)()
    
    # Retrieves a Cloud Logging handler based on the environment
    # you're running in and integrates the handler with the
    # Python logging module. By default this captures all logs
    # at INFO level and higher
    client.[setup_logging](https://docs.cloud.google.com/python/docs/reference/logging/latest/google.cloud.logging_v2.client.Client.html#google_cloud_logging_v2_client_Client_setup_logging)()
    
    # Imports Python standard library logging
    import logging
    
    # The data to log
    text = "Hello, world!"
    
    # Emits the data using the standard logging module
    logging.warning(text)
    
    print("Logged: {}".format(text))

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudlogging). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
