---
url: https://docs.cloud.google.com/logging/docs/samples/logging-get-sink/
title: Get a sink \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:48.954477+00:00
---

# Get a sink  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/samples/logging-get-sink/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Samples ](https://docs.cloud.google.com/logging/docs/samples)



#  Get a sink Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to retrieve the metadata for a Cloud Logging Sink.

## Code sample

### Go

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/logging/logadmin"
    )
    
    // getSink retrieves the metadata for a Cloud Logging Sink.
    func getSink(w io.Writer, projectID, sinkName string) error {
    	ctx := context.Background()
    
    	client, err := logadmin.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/logging/latest/logadmin.html#cloud_google_com_go_logging_logadmin_Client_NewClient)(ctx, projectID)
    	if err != nil {
    		return err
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/logging/latest/logadmin.html#cloud_google_com_go_logging_logadmin_Client_Close)()
    
    	sink, err := client.Sink(ctx, sinkName)
    	if err != nil {
    		return err
    	}
    	fmt.Fprintf(w, "%v\n", sink)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.logging.[Logging](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.html);
    import com.google.cloud.logging.[LoggingOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions.html);
    import com.google.cloud.logging.[Sink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Sink.html);
    
    /** Retrieve Cloud Logging Sink metadata. */
    public class GetSinkMetadata {
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        // The Name of your sink
        String sinkName = "sink-name"; // i.e my-sink
    
        getSinkMetadata(sinkName);
      }
    
      public static void getSinkMetadata(String sinkName) throws Exception {
        // Instantiates a logging client
        try ([Logging](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.html) logging = [LoggingOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions.html).[getDefaultInstance](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions.html#com_google_cloud_logging_LoggingOptions_getDefaultInstance__)().getService()) {
    
          [Sink](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Sink.html) sink = logging.getSink(sinkName);
    
          // print sink metadata
          System.out.println("Name:" + sink.getName());
          System.out.println("Version Format:" + sink.[getVersionFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SinkInfo.html#com_google_cloud_logging_SinkInfo_getVersionFormat__)());
          System.out.println("Filter:" + sink.getFilter());
          System.out.println("Destination:" + sink.getDestination());
        }
      }
    }

### Python

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from typing import List
    from google.cloud import logging
    
    
    def get_sink(project_id: str, sink_name: str) -> logging.Sink:
        """Retrieves the metadata for a Cloud Logging Sink.
    
        Args:
            project_id: the ID of the project
            sink_name: the name of the sink
    
        Returns:
            A Cloud Logging Sink.
        """
        client = logging.Client(project=project_id)
        sink = client.sink(sink_name)
        sink.reload()
        print(f"Name: {sink.name}")
        print(f"Destination: {sink.destination}")
        print(f"Filter: {sink.filter_}")
        return sink
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudlogging). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
