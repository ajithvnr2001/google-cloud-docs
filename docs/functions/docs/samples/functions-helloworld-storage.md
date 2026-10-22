---
url: https://docs.cloud.google.com/functions/docs/samples/functions-helloworld-storage/
title: Cloud Storage (1st Gen) Hello World \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:03.997570+00:00
---

# Cloud Storage (1st Gen) Hello World  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-helloworld-storage/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  Cloud Storage (1st Gen) Hello World Stay organized with collections  Save and categorize content based on your preferences. 

Example Storage-triggered function that runs on Cloud Functions (1st Gen).

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Cloud Storage Tutorial (1st gen)](https://docs.cloud.google.com/functions/1stgendocs/tutorials/storage-1st-gen)



## Code sample

### C#

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using CloudNative.CloudEvents;
    using Google.Cloud.Functions.Framework;
    using Google.Events.Protobuf.Cloud.Storage.V1;
    using Microsoft.Extensions.Logging;
    using System.Threading;
    using System.Threading.Tasks;
    
    namespace HelloGcs;
    
     /// <summary>
     /// Example Cloud Storage-triggered function.
     /// This function can process any event from Cloud Storage.
     /// </summary>
    public class Function : ICloudEventFunction<StorageObjectData>
    {
        private readonly ILogger _logger;
    
        public Function(ILogger<Function> logger) =>
            _logger = logger;
    
        public Task HandleAsync(CloudEvent cloudEvent, StorageObjectData data, CancellationToken cancellationToken)
        {
            _logger.LogInformation("Event: {event}", cloudEvent.Id);
            _logger.LogInformation("Event Type: {type}", cloudEvent.Type);
            _logger.LogInformation("Bucket: {bucket}", data.Bucket);
            _logger.LogInformation("File: {file}", data.Name);
            _logger.LogInformation("Metageneration: {metageneration}", data.Metageneration);
            _logger.LogInformation("Created: {created:s}", data.TimeCreated?.ToDateTimeOffset());
            _logger.LogInformation("Updated: {updated:s}", data.Updated?.ToDateTimeOffset());
            return Task.CompletedTask;
        }
    }

### Go

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Package helloworld provides a set of Cloud Functions samples.
    package helloworld
    
    import (
    	"context"
    	"fmt"
    	"log"
    	"time"
    
    	"cloud.google.com/go/functions/metadata"
    )
    
    // GCSEvent is the payload of a GCS event.
    type GCSEvent struct {
    	Kind                    string                 `json:"kind"`
    	ID                      string                 `json:"id"`
    	SelfLink                string                 `json:"selfLink"`
    	Name                    string                 `json:"name"`
    	Bucket                  string                 `json:"bucket"`
    	Generation              string                 `json:"generation"`
    	Metageneration          string                 `json:"metageneration"`
    	ContentType             string                 `json:"contentType"`
    	TimeCreated             time.Time              `json:"timeCreated"`
    	Updated                 time.Time              `json:"updated"`
    	TemporaryHold           bool                   `json:"temporaryHold"`
    	EventBasedHold          bool                   `json:"eventBasedHold"`
    	RetentionExpirationTime time.Time              `json:"retentionExpirationTime"`
    	StorageClass            string                 `json:"storageClass"`
    	TimeStorageClassUpdated time.Time              `json:"timeStorageClassUpdated"`
    	Size                    string                 `json:"size"`
    	MD5Hash                 string                 `json:"md5Hash"`
    	MediaLink               string                 `json:"mediaLink"`
    	ContentEncoding         string                 `json:"contentEncoding"`
    	ContentDisposition      string                 `json:"contentDisposition"`
    	CacheControl            string                 `json:"cacheControl"`
    	Metadata                map[string]interface{} `json:"metadata"`
    	CRC32C                  string                 `json:"crc32c"`
    	ComponentCount          int                    `json:"componentCount"`
    	Etag                    string                 `json:"etag"`
    	CustomerEncryption      struct {
    		EncryptionAlgorithm string `json:"encryptionAlgorithm"`
    		KeySha256           string `json:"keySha256"`
    	}
    	KMSKeyName    string `json:"kmsKeyName"`
    	ResourceState string `json:"resourceState"`
    }
    
    // HelloGCS consumes a(ny) GCS event.
    func HelloGCS(ctx context.Context, e GCSEvent) error {
    	meta, err := metadata.[FromContext](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/functions/latest/metadata.html#cloud_google_com_go_functions_metadata_Metadata_FromContext)(ctx)
    	if err != nil {
    		return fmt.Errorf("metadata.FromContext: %w", err)
    	}
    	log.Printf("Event ID: %v\n", meta.EventID)
    	log.Printf("Event type: %v\n", meta.EventType)
    	log.Printf("Bucket: %v\n", e.Bucket)
    	log.Printf("File: %v\n", e.Name)
    	log.Printf("Metageneration: %v\n", e.Metageneration)
    	log.Printf("Created: %v\n", e.TimeCreated)
    	log.Printf("Updated: %v\n", e.Updated)
    	return nil
    }
    

### Java

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.functions.BackgroundFunction;
    import com.google.cloud.functions.Context;
    import functions.eventpojos.GcsEvent;
    import java.util.logging.Logger;
    
    /**
     * Example Cloud Storage-triggered function.
     * This function can process any event from Cloud Storage.
     */
    public class HelloGcs implements BackgroundFunction<GcsEvent> {
      private static final Logger logger = Logger.getLogger(HelloGcs.class.getName());
    
      @Override
      public void accept(GcsEvent event, Context context) {
        logger.info("Event: " + context.eventId());
        logger.info("Event Type: " + context.eventType());
        logger.info("Bucket: " + event.getBucket());
        logger.info("File: " + event.getName());
        logger.info("Metageneration: " + event.getMetageneration());
        logger.info("Created: " + event.getTimeCreated());
        logger.info("Updated: " + event.getUpdated());
      }
    }
    

### Node.js

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Generic background Cloud Function to be triggered by Cloud Storage.
     * This sample works for all Cloud Storage CRUD operations.
     *
     * @param {object} file The Cloud Storage file metadata.
     * @param {object} context The event metadata.
     */
    exports.helloGCS = (file, context) => {
      console.log(`  Event: ${context.eventId}`);
      console.log(`  Event Type: ${context.eventType}`);
      console.log(`  Bucket: ${file.bucket}`);
      console.log(`  File: ${file.name}`);
      console.log(`  Metageneration: ${file.metageneration}`);
      console.log(`  Created: ${file.timeCreated}`);
      console.log(`  Updated: ${file.updated}`);
    };

### PHP

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use CloudEvents\V1\CloudEventInterface;
    use Google\CloudFunctions\FunctionsFramework;
    
    // Register the function with Functions Framework.
    // This enables omitting the `FUNCTIONS_SIGNATURE_TYPE=cloudevent` environment
    // variable when deploying. The `FUNCTION_TARGET` environment variable should
    // match the first parameter.
    FunctionsFramework::cloudEvent('helloGCS', 'helloGCS');
    
    function helloGCS(CloudEventInterface $cloudevent)
    {
        // This function supports all Cloud Storage event types.
        $log = fopen(getenv('LOGGER_OUTPUT') ?: 'php://stderr', 'wb');
        $data = $cloudevent->getData();
        fwrite($log, 'Event: ' . $cloudevent->getId() . PHP_EOL);
        fwrite($log, 'Event Type: ' . $cloudevent->getType() . PHP_EOL);
        fwrite($log, 'Bucket: ' . $data['bucket'] . PHP_EOL);
        fwrite($log, 'File: ' . $data['name'] . PHP_EOL);
        fwrite($log, 'Metageneration: ' . $data['metageneration'] . PHP_EOL);
        fwrite($log, 'Created: ' . $data['timeCreated'] . PHP_EOL);
        fwrite($log, 'Updated: ' . $data['updated'] . PHP_EOL);
    }
    

### Python

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def hello_gcs(event, context):
        """Background Cloud Function to be triggered by Cloud Storage.
           This generic function logs relevant data when a file is changed,
           and works for all Cloud Storage CRUD operations.
        Args:
            event (dict):  The dictionary with data specific to this type of event.
                           The `data` field contains a description of the event in
                           the Cloud Storage `object` format described here:
                           https://cloud.google.com/storage/docs/json_api/v1/objects#resource
            context (google.cloud.functions.Context): Metadata of triggering event.
        Returns:
            None; the output is written to Cloud Logging
        """
    
        print(f"Event ID: {context.event_id}")
        print(f"Event type: {context.event_type}")
        print("Bucket: {}".format(event["bucket"]))
        print("File: {}".format(event["name"]))
        print("Metageneration: {}".format(event["metageneration"]))
        print("Created: {}".format(event["timeCreated"]))
        print("Updated: {}".format(event["updated"]))
    
    

### Ruby

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "functions_framework"
    
    FunctionsFramework.cloud_event "hello_gcs" do |event|
      # This function supports all Cloud Storage events.
      # The `event` parameter is a CloudEvents::Event::V1 object.
      # See https://cloudevents.github.io/sdk-ruby/latest/CloudEvents/Event/V1.html
      payload = event.data
    
      logger.info "Event: #{event.id}"
      logger.info "Event Type: #{event.type}"
      logger.info "Bucket: #{payload['bucket']}"
      logger.info "File: #{payload['name']}"
      logger.info "Metageneration: #{payload['metageneration']}"
      logger.info "Created: #{payload['timeCreated']}"
      logger.info "Updated: #{payload['updated']}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
