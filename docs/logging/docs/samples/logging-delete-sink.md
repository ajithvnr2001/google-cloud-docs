---
url: https://docs.cloud.google.com/logging/docs/samples/logging-delete-sink/
title: Delete a sink \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:47.345450+00:00
---

# Delete a sink  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/samples/logging-delete-sink/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Samples ](https://docs.cloud.google.com/logging/docs/samples)



#  Delete a sink Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to delete a Cloud Logging Sink.

## Code sample

### C#

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    private void DeleteSink(string sinkId)
    {
        var sinkClient = ConfigServiceV2Client.Create();
        LogSinkName sinkName = new LogSinkName(s_projectId, sinkId);
        sinkClient.DeleteSink(sinkName, _retryAWhile);
        Console.WriteLine($"Deleted {sinkId}.");
    }
    

### Go

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"log"
    
    	"cloud.google.com/go/logging/logadmin"
    )
    
    func deleteSink(projectID string) error {
    	ctx := context.Background()
    	client, err := logadmin.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/logging/latest/logadmin.html#cloud_google_com_go_logging_logadmin_Client_NewClient)(ctx, projectID)
    	if err != nil {
    		log.Fatalf("logadmin.NewClient: %v", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/logging/latest/logadmin.html#cloud_google_com_go_logging_logadmin_Client_Close)()
    	if err := client.[DeleteSink](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/logging/latest/logadmin.html#cloud_google_com_go_logging_logadmin_Client_DeleteSink)(ctx, "severe-errors-to-gcs"); err != nil {
    		return err
    	}
    	return nil
    }
    

### Java

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    boolean deleted = logging.deleteSink(sinkName);
    if (deleted) {
      // the sink was deleted
    } else {
      // the sink was not found
    }

### PHP

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Logging\LoggingClient;
    
    /**
     * Delete a log sink.
     *
     * @param string $projectId The Google project ID.
     * @param string $sinkName The name of the sink.
     */
    function delete_sink($projectId, $sinkName)
    {
        $logging = new LoggingClient(['projectId' => $projectId]);
        $logging->sink($sinkName)->delete();
        printf("Deleted a sink '%s'." . PHP_EOL, $sinkName);
    }

### Python

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def delete_sink(sink_name):
        """Deletes a sink."""
        logging_client = logging.Client()
        sink = logging_client.sink(sink_name)
    
        sink.delete()
    
        print("Deleted sink {}".format(sink.name))
    
    

### Ruby

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/logging"
    
    logging = Google::Cloud::[Logging](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging/latest/Google-Cloud-Logging.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging/latest/Google-Cloud-Logging.html)
    
    # sink_name = "name-of-my-sink"
    sink = logging.sink sink_name
    sink.delete
    puts "Deleted sink: #{sink.name}"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudlogging). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
