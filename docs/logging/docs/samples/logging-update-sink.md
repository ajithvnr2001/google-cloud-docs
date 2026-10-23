---
url: https://docs.cloud.google.com/logging/docs/samples/logging-update-sink/
title: Update a sink \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:43.969618+00:00
---

# Update a sink  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/samples/logging-update-sink/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Samples ](https://docs.cloud.google.com/logging/docs/samples)



#  Update a sink Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to update a Cloud Logging Sink.

## Code sample

### C#

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    private void UpdateSinkLog(string sinkId, string logId)
    {
        var sinkClient = ConfigServiceV2Client.Create();
        LogName logName = new LogName(s_projectId, logId);
        LogSinkName sinkName = new LogSinkName(s_projectId, sinkId);
        var sink = sinkClient.GetSink(sinkName, _retryAWhile);
        sink.Filter = $"logName={logName.ToString()}AND severity<=ERROR";
        sinkClient.UpdateSink(sinkName, sink, _retryAWhile);
        Console.WriteLine($"Updated {sinkId} to export logs from {logId}.");
    }
    

### Go

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"log"
    
    	"cloud.google.com/go/logging/logadmin"
    )
    
    func updateSink(projectID string) (*logadmin.Sink, error) {
    	ctx := context.Background()
    	client, err := logadmin.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/logging/latest/logadmin.html#cloud_google_com_go_logging_logadmin_Client_NewClient)(ctx, projectID)
    	if err != nil {
    		log.Fatalf("logadmin.NewClient: %v", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/logging/latest/logadmin.html#cloud_google_com_go_logging_logadmin_Client_Close)()
    	sink, err := client.[UpdateSink](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/logging/latest/logadmin.html#cloud_google_com_go_logging_logadmin_Client_UpdateSink)(ctx, &logadmin.Sink{
    		ID:          "severe-errors-to-gcs",
    		Destination: "storage.googleapis.com/logsinks-new-bucket",
    		Filter:      "severity >= INFO",
    	})
    	return sink, err
    }
    

### Java

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    SinkInfo sinkInfo =
        SinkInfo.newBuilder(sinkName, DatasetDestination.of(datasetName))
            .setVersionFormat(SinkInfo.VersionFormat.V2)
            .setFilter("severity>=ERROR")
            .build();
    Sink sink = logging.update(sinkInfo);

### PHP

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Logging\LoggingClient;
    
    /**
     * Update a log sink.
     *
     * @param string $projectId
     * @param string $sinkName
     * @param string $filterString
     */
    function update_sink($projectId, $sinkName, $filterString)
    {
        $logging = new LoggingClient(['projectId' => $projectId]);
        $sink = $logging->sink($sinkName);
        $sink->update(['filter' => $filterString]);
        printf("Updated a sink '%s'." . PHP_EOL, $sinkName);
    }

### Python

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def update_sink(sink_name, filter_):
        """Changes a sink's filter.
    
        The filter determines which logs this sink matches and will be exported
        to the destination. For example a filter of 'severity>=INFO' will send
        all logs that have a severity of INFO or greater to the destination.
        See https://cloud.google.com/logging/docs/view/advanced_filters for more
        filter information.
        """
        logging_client = logging.Client()
        sink = logging_client.sink(sink_name)
    
        sink.reload()
    
        sink.filter_ = filter_
        print("Updated sink {}".format(sink.name))
        sink.update()
    
    

### Ruby

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/logging"
    
    logging = Google::Cloud::[Logging](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging/latest/Google-Cloud-Logging.html).new
    storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).new
    # bucket_name = "name-of-my-storage-bucket"
    bucket  = storage.create_bucket bucket_name
    # sink_name = "name-of-my-sink"
    sink    = logging.sink sink_name
    
    sink.destination = "storage.googleapis.com/#{bucket.id}"
    
    sink.save
    puts "Updated sink destination for #{sink.name} to #{sink.destination}"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudlogging). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
