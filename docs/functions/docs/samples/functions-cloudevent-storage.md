---
url: https://docs.cloud.google.com/functions/docs/samples/functions-cloudevent-storage/
title: Cloud Storage (2nd Gen) \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:03:34.130832+00:00
---

# Cloud Storage (2nd Gen)  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-cloudevent-storage/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  Cloud Storage (2nd Gen) Stay organized with collections  Save and categorize content based on your preferences. 

Process a Cloud Storage event using Cloud Functions (2nd Gen) and Eventarc

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Trigger functions from Cloud Storage using Eventarc](https://docs.cloud.google.com/run/docs/tutorials/trigger-functions-storage)



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
    	"strings"
    
    	"github.com/GoogleCloudPlatform/functions-framework-go/functions"
    	"github.com/cloudevents/sdk-go/v2/event"
    	"github.com/googleapis/google-cloudevents-go/cloud/storagedata"
    	"google.golang.org/protobuf/encoding/protojson"
    )
    
    func init() {
    	functions.CloudEvent("HelloStorage", helloStorage)
    }
    
    // helloStorage consumes a CloudEvent message and logs details about the changed object.
    func helloStorage(ctx context.Context, e event.Event) error {
    	log.Printf("Event ID: %s", e.ID())
    	log.Printf("Event Type: %s", e.Type())
    
    	var data storagedata.StorageObjectData
    	err := protojson.Unmarshal(e.Data(), &data)
    
    	// Unmarshal() returns an unexported error.
    	// Parse the error string to determine whether there is an unknown field.
    	if err != nil && strings.Contains(err.Error(), "unknown field") {
    		log.Println(err.Error())
    		options := protojson.UnmarshalOptions{
    			DiscardUnknown: true,
    		}
    		err = options.Unmarshal(e.Data(), &data)
    	}
    	if err != nil {
    		return fmt.Errorf("protojson.Unmarshal: %w", err)
    	}
    
    	log.Printf("Bucket: %s", data.GetBucket())
    	log.Printf("File: %s", data.GetName())
    	log.Printf("Metageneration: %d", data.GetMetageneration())
    	log.Printf("Created: %s", data.GetTimeCreated().AsTime())
    	log.Printf("Updated: %s", data.GetUpdated().AsTime())
    	return nil
    }
    

### Java

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.functions.CloudEventsFunction;
    import com.google.events.cloud.storage.v1.[StorageObjectData](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.storage.v1.StorageObjectData.html);
    import com.google.protobuf.[InvalidProtocolBufferException](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html);
    import com.google.protobuf.util.[JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html);
    import io.cloudevents.CloudEvent;
    import java.nio.charset.StandardCharsets;
    import java.util.logging.Logger;
    
    public class HelloGcs implements CloudEventsFunction {
      private static final Logger logger = Logger.getLogger(HelloGcs.class.getName());
    
      @Override
      public void accept(CloudEvent event) throws [InvalidProtocolBufferException](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html) {
        logger.info("Event: " + event.getId());
        logger.info("Event Type: " + event.getType());
    
        if (event.getData() == null) {
          logger.warning("No data found in cloud event payload!");
          return;
        }
    
        String cloudEventData = new String(event.getData().toBytes(), StandardCharsets.UTF_8);
        [StorageObjectData](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.storage.v1.StorageObjectData.html).Builder builder = [StorageObjectData](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.storage.v1.StorageObjectData.html).newBuilder();
    
        // If you do not ignore unknown fields, then JsonFormat.Parser returns an
        // error when encountering a new or unknown field. Note that you might lose
        // some event data in the unmarshaling process by ignoring unknown fields.
        [JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html).[Parser](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Parser.html) parser = [JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html).parser().ignoringUnknownFields();
        parser.merge(cloudEventData, builder);
        [StorageObjectData](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.storage.v1.StorageObjectData.html) data = [builder](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TextFormatParseInfoTree.html#com_google_protobuf_TextFormatParseInfoTree_builder__).build();
    
        logger.info("Bucket: " + data.[getBucket](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.storage.v1.StorageObjectData.html#com_google_events_cloud_storage_v1_StorageObjectData_getBucket__)());
        logger.info("File: " + data.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.storage.v1.StorageObjectData.html#com_google_events_cloud_storage_v1_StorageObjectData_getName__)());
        logger.info("Metageneration: " + data.[getMetageneration](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.storage.v1.StorageObjectData.html#com_google_events_cloud_storage_v1_StorageObjectData_getMetageneration__)());
        logger.info("Created: " + data.[getTimeCreated](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.storage.v1.StorageObjectData.html#com_google_events_cloud_storage_v1_StorageObjectData_getTimeCreated__)());
        logger.info("Updated: " + data.[getUpdated](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.storage.v1.StorageObjectData.html#com_google_events_cloud_storage_v1_StorageObjectData_getUpdated__)());
      }
    }
    

### Node.js

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const functions = require('@google-cloud/functions-framework');
    
    // Register a CloudEvent callback with the Functions Framework that will
    // be triggered by Cloud Storage.
    functions.cloudEvent('helloGCS', cloudEvent => {
      console.log(`Event ID: ${cloudEvent.id}`);
      console.log(`Event Type: ${cloudEvent.type}`);
    
      const file = cloudEvent.data;
      console.log(`Bucket: ${file.bucket}`);
      console.log(`File: ${file.name}`);
      console.log(`Metageneration: ${file.metageneration}`);
      console.log(`Created: ${file.timeCreated}`);
      console.log(`Updated: ${file.updated}`);
    });

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
    
    
    from cloudevents.http import CloudEvent
    
    import functions_framework
    
    
    # Triggered by a change in a storage bucket
    @functions_framework.cloud_event
    def hello_gcs(cloud_event: CloudEvent) -> tuple:
        """This function is triggered by a change in a storage bucket.
    
        Args:
            cloud_event: The CloudEvent that triggered this function.
        Returns:
            The event ID, event type, bucket, name, metageneration, and timeCreated.
        """
        data = cloud_event.data
    
        event_id = cloud_event["id"]
        event_type = cloud_event["type"]
    
        bucket = data["bucket"]
        name = data["name"]
        metageneration = data["metageneration"]
        timeCreated = data["timeCreated"]
        updated = data["updated"]
    
        print(f"Event ID: {event_id}")
        print(f"Event type: {event_type}")
        print(f"Bucket: {bucket}")
        print(f"File: {name}")
        print(f"Metageneration: {metageneration}")
        print(f"Created: {timeCreated}")
        print(f"Updated: {updated}")
    
        return event_id, event_type, bucket, name, metageneration, timeCreated, updated
    
    

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
