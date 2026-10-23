---
url: https://docs.cloud.google.com/logging/docs/samples/logging-write-log-entry-advanced/
title: Write request logs \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:43.780731+00:00
---

# Write request logs  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/samples/logging-write-log-entry-advanced/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Samples ](https://docs.cloud.google.com/logging/docs/samples)



#  Write request logs Stay organized with collections  Save and categorize content based on your preferences. 

An example of how to log HTTP request logs.

## Code sample

### Go

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Writes an advanced log entry to Cloud Logging.
    package main
    
    import (
    	"context"
    	"log"
    	"net/http"
    	"os"
    
    	"cloud.google.com/go/logging"
    )
    
    func main() {
    	ctx := context.Background()
    
    	// Creates a client.
    	projectID := os.Getenv("GOOGLE_CLOUD_PROJECT")
    	client, err := logging.NewClient(ctx, projectID)
    	if err != nil {
    		log.Fatalf("Failed to create client: %v", err)
    	}
    	defer client.Close()
    
    	// Sets the name of the log to write to.
    	logger := client.Logger("my-log")
    
    	// Logs a basic entry.
    	logger.[Log](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/logging/latest/index.html#cloud_google_com_go_logging_Logger_Log)(logging.[Entry](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/logging/latest/index.html#cloud_google_com_go_logging_Entry){Payload: "hello world"})
    
    	// TODO(developer): replace with your request value.
    	r, err := http.NewRequest("GET", "http://example.com", nil)
    
    	// Logs an HTTPRequest type entry.
    	// Some request metadata will be autopopulated in the log entry.
    	httpEntry := logging.[Entry](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/logging/latest/index.html#cloud_google_com_go_logging_Entry){
    		Payload: "optional message",
    		HTTPRequest: &logging.[HTTPRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/logging/latest/index.html#cloud_google_com_go_logging_HTTPRequest){
    			Request: r,
    		},
    	}
    	logger.[Log](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/logging/latest/index.html#cloud_google_com_go_logging_Logger_Log)(httpEntry)
    }
    

### Java

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.[MonitoredResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.MonitoredResource.html);
    import com.google.cloud.logging.[HttpRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.HttpRequest.html);
    import com.google.cloud.logging.[LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry.html);
    import com.google.cloud.logging.[Logging](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.html);
    import com.google.cloud.logging.[LoggingOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions.html);
    import com.google.cloud.logging.[Payload](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Payload.html);
    import com.google.cloud.logging.[Severity](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Severity.html);
    import java.util.Collections;
    
    /** Write LogEntry with HTTP request using the Cloud Logging API. */
    public class LogEntryWriteHttpRequest {
    
      public static void main([String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html)[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) logName = "log-name"; // i.e "my-log"
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) payLoad = "payload"; // i.e "Hello world!"
        [HttpRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.HttpRequest.html) httpRequest =
            [HttpRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.HttpRequest.html).newBuilder()
                .setRequestUrl("www.example.com")
                .setRequestMethod([HttpRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.HttpRequest.html).RequestMethod.GET) // Supported method GET,POST,PUT,HEAD
                .setStatus(200)
                .build();
        createLogEntryRequest(logName, payLoad, httpRequest);
      }
    
      public static void createLogEntryRequest([String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) logName, [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) payLoad, [HttpRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.HttpRequest.html) httpRequest)
          throws Exception {
        // Instantiates a logging client
        try ([Logging](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.html) logging = [LoggingOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions.html).getDefaultInstance().getService()) {
          // create an instance of LogEntry with HTTP request
          [LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry.html) logEntry =
              [LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry.html).newBuilder([Payload](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Payload.html).StringPayload.of(payLoad))
                  .setSeverity([Severity](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Severity.html).ERROR)
                  .setLogName(logName)
                  .setHttpRequest(httpRequest)
                  .setResource([MonitoredResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.MonitoredResource.html).newBuilder("global").build())
                  .build();
    
          // Writes the log entry asynchronously
          logging.write(Collections.singleton(logEntry));
          System.out.printf("Logged: %s", payLoad);
        }
      }
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudlogging). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
