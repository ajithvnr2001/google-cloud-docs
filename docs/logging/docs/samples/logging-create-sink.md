---
url: https://docs.cloud.google.com/logging/docs/samples/logging-create-sink/
title: Create a sink \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:36:51.678378+00:00
---

# Create a sink  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/samples/logging-create-sink/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Samples ](https://docs.cloud.google.com/logging/docs/samples)



#  Create a sink Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to create a Cloud Logging Sink.

## Code sample

### C#

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    private void CreateSink(string sinkId, string logId)
    {
        var sinkClient = ConfigServiceV2Client.Create();
        LogSink myLogSink = new LogSink();
        myLogSink.Name = sinkId;
    
        // This creates a sink using a Google Cloud Storage bucket 
        // named the same as the projectId.
        // This requires editing the bucket's permissions to add the Entity Group 
        // named 'cloud-logs@google.com' with 'Owner' access for the bucket.
        // If this is being run with a Google Cloud service account,
        // that account will need to be granted 'Owner' access to the Project.
        // In Powershell, use this command:
        // PS > Add-GcsBucketAcl <your-bucket-name> -Role OWNER -Group cloud-logs@google.com
        myLogSink.Destination = "storage.googleapis.com/" + s_projectId;
        LogName logName = new LogName(s_projectId, logId);
        myLogSink.Filter = $"logName={logName.ToString()}AND severity<=ERROR";
        ProjectName projectName = new ProjectName(s_projectId);
        sinkClient.CreateSink(projectName, myLogSink, _retryAWhile);
        Console.WriteLine($"Created sink: {sinkId}.");
    }
    

### Go

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"log"
    
    	"cloud.google.com/go/logging/logadmin"
    )
    
    func createSink(projectID string) (*logadmin.Sink, error) {
    	ctx := context.Background()
    	client, err := logadmin.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/logging/latest/logadmin.html#cloud_google_com_go_logging_logadmin_Client_NewClient)(ctx, projectID)
    	if err != nil {
    		log.Fatalf("logadmin.NewClient: %v", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/logging/latest/logadmin.html#cloud_google_com_go_logging_logadmin_Client_Close)()
    	sink, err := client.[CreateSink](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/logging/latest/logadmin.html#cloud_google_com_go_logging_logadmin_Client_CreateSink)(ctx, &logadmin.Sink{
    		ID:          "severe-errors-to-gcs",
    		Destination: "storage.googleapis.com/logsinks-bucket",
    		Filter:      "severity >= ERROR",
    	})
    	return sink, err
    }
    

### Java

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    SinkInfo sinkInfo = SinkInfo.of(sinkName, DatasetDestination.of(datasetName));
    Sink sink = logging.create(sinkInfo);

### PHP

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Logging\LoggingClient;
    
    /**
     * Create a log sink.
     *
     * @param string $projectId The Google project ID.
     * @param string $sinkName The name of the sink.
     * @param string $destination The destination of the sink.
     * @param string $filterString The filter for the sink.
     */
    function create_sink($projectId, $sinkName, $destination, $filterString)
    {
        $logging = new LoggingClient(['projectId' => $projectId]);
        $logging->createSink(
            $sinkName,
            $destination,
            ['filter' => $filterString]
        );
        printf("Created a sink '%s'." . PHP_EOL, $sinkName);
    }

### Python

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def create_sink(sink_name, destination_bucket, filter_):
        """Creates a sink to export logs to the given Cloud Storage bucket.
    
        The filter determines which logs this sink matches and will be exported
        to the destination. For example a filter of 'severity>=INFO' will send
        all logs that have a severity of INFO or greater to the destination.
        See https://cloud.google.com/logging/docs/view/advanced_filters for more
        filter information.
        """
        logging_client = logging.Client()
    
        # The destination can be a Cloud Storage bucket, a Cloud Pub/Sub topic,
        # or a BigQuery dataset. In this case, it is a Cloud Storage Bucket.
        # See https://cloud.google.com/logging/docs/api/tasks/exporting-logs for
        # information on the destination format.
        destination = "storage.googleapis.com/{bucket}".format(bucket=destination_bucket)
    
        sink = logging_client.sink(sink_name, filter_=filter_, destination=destination)
    
        if sink.exists():
            print("Sink {} already exists.".format(sink.name))
            return
    
        sink.create()
        print("Created sink {}".format(sink.name))
    
    

### Ruby

To learn how to install and use the client library for Logging, see [Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries). 

To authenticate to Logging, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/logging"
    
    logging = Google::Cloud::[Logging](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-logging/latest/Google-Cloud-Logging.html).new
    storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).new
    # bucket_name = "name-of-my-storage-bucket"
    bucket  = storage.create_bucket bucket_name
    
    # Grant owner permission to Cloud Logging service
    email = "cloud-logs@google.com"
    bucket.acl.add_owner "group-#{email}"
    
    # sink_name = "name-of-my-sink"
    sink = logging.create_sink sink_name, "storage.googleapis.com/#{bucket.id}"
    puts "#{sink.name}: #{sink.filter} -> #{sink.destination}"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudlogging). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
