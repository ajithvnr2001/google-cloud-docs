---
url: https://docs.cloud.google.com/run/docs/triggering/trigger-functions-from-log-entries/
title: Trigger functions from log entries \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:42:05.085172+00:00
---

# Trigger functions from log entries  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/triggering/trigger-functions-from-log-entries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Trigger functions from log entries Stay organized with collections  Save and categorize content based on your preferences. 

[Many Google Cloud events](https://docs.cloud.google.com/logging/docs/audit/services) are logged in Cloud Audit Logs. You can filter these logs and forward them to Pub/Sub topics using [sinks](https://docs.cloud.google.com/logging/docs/export). These Pub/Sub topics can then send notifications that [trigger](https://docs.cloud.google.com/run/docs/triggering/pubsub-triggers) Cloud Run functions. You can create custom events from any Google Cloud service that produces [audit logs](https://docs.cloud.google.com/logging/docs/audit/services).

This page shows an example of how to trigger functions from log entries routed to a Pub/Sub topic.

## Event structure of Pub/Sub-triggered functions

Like all [Pub/Sub-triggered functions](https://docs.cloud.google.com/run/docs/triggering/pubsub-triggers), functions triggered by Cloud Logging log entries receive a [`PubsubMessage`](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/PubsubMessage) object whose `data` parameter is a `base64`-encoded string. For Cloud Logging log events, decoding this value returns the relevant log entry as a JSON string.

## Before you begin

The sample code forwards Cloud Audit Logs to a Cloud Run function. Before you run the sample code, you'll need the following:

  * [Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/create-topic-console#create_a_topic)
  * [Cloud Logging sink](https://docs.cloud.google.com/logging/docs/export/configure_export_v2#dest-create)



See the [Pub/Sub triggers guide](https://docs.cloud.google.com/run/docs/triggering/pubsub-triggers) for the APIs to enable and the required roles for deploying functions that are triggered by Pub/Sub.

## Sample code

You can use a [Pub/Sub-triggered function](https://docs.cloud.google.com/run/docs/triggering/pubsub-triggers) to detect and respond to exported Cloud Logging logs:

### Node.js
    
    
    exports.processLogEntry = data => {
      const dataBuffer = Buffer.from(data.data, 'base64');
    
      const logEntry = JSON.parse(dataBuffer.toString('ascii')).protoPayload;
      console.log(`Method: ${logEntry.methodName}`);
      console.log(`Resource: ${logEntry.resourceName}`);
      console.log(`Initiator: ${logEntry.authenticationInfo.principalEmail}`);
    };

### Python
    
    
    import base64
    import json
    
    def process_log_entry(data, context):
        data_buffer = base64.b64decode(data["data"])
        log_entry = json.loads(data_buffer)["protoPayload"]
    
        print(f"Method: {log_entry['methodName']}")
        print(f"Resource: {log_entry['resourceName']}")
        print(f"Initiator: {log_entry['authenticationInfo']['principalEmail']}")
    
    

### Go
    
    
    // Package log contains examples for handling Cloud Functions logs.
    package log
    
    import (
    	"context"
    	"log"
    )
    
    // PubSubMessage is the payload of a Pub/Sub event.
    // See the documentation for more details:
    // https://cloud.google.com/pubsub/docs/reference/rest/v1/PubsubMessage
    type PubSubMessage struct {
    	Data []byte `json:"data"`
    }
    
    // ProcessLogEntry processes a Pub/Sub message from Cloud Logging.
    func ProcessLogEntry(ctx context.Context, m PubSubMessage) error {
    	log.Printf("Log entry data: %s", string(m.Data))
    	return nil
    }
    

### Java
    
    
    import com.google.cloud.functions.BackgroundFunction;
    import com.google.cloud.functions.Context;
    import functions.eventpojos.PubsubMessage;
    import java.nio.charset.StandardCharsets;
    import java.util.Base64;
    import java.util.logging.Logger;
    
    public class StackdriverLogging implements BackgroundFunction<PubsubMessage> {
      private static final Logger logger = Logger.getLogger(StackdriverLogging.class.getName());
    
      @Override
      public void accept(PubsubMessage message, Context context) {
        String name = "World";
    
        if (!message.getData().isEmpty()) {
          name = new String(Base64.getDecoder().decode(
              message.getData().getBytes(StandardCharsets.UTF_8)), StandardCharsets.UTF_8);
        }
        String res = String.format("Hello, %s", name);
        logger.info(res);
      }
    }

## Deploy and trigger a function

To configure a trigger during function deployment:

  1. Run the following command in the directory that contains the sample code to deploy your function:

###  Node.js 
         
         gcloud run deploy nodejs-log-function \
               --source . \
               --function processLogEntry \
               --base-image nodejs20 \
               --region REGION
         

###  Python 
         
         gcloud run deploy python-log-function \
               --source . \
               --function process_log_entry \
               --base-image python312 \
               --region REGION
         

###  Go 
         
         gcloud run deploy go-log-function \
               --source . \
               --function ProcessLogEntry \
               --base-image go122 \
               --region REGION
         

###  Java 
         
         gcloud run deploy java-log-function \
               --source . \
               --function StackdriverLogging \
               --base-image java21 \
               --region REGION
         

Replace:

     * REGION with the Google Cloud [region](https://docs.cloud.google.com/run/docs/locations) where you want to deploy your function. For example, `europe-west1`.

     * The `--function` flag specifies the entry point to the function in example source code. This is the code Cloud Run executes when your function runs. The value of this flag must be a function name or fully-qualified class name that exists in your source code.

     * The `--base-image` flag specifies the base image environment for your function. For more details about base images and the packages included in each image, see [Runtimes base images](https://docs.cloud.google.com/run/docs/configuring/services/runtime-base-images#how_to_obtain_base_images).

  2. Run the following command to create a trigger that filters events:
         
         gcloud eventarc triggers create TRIGGER_NAME  \
             --location=EVENTARC_TRIGGER_LOCATION \
             --destination-run-service=SERVICE  \
             --destination-run-region=REGION \
             --event-filters="type=google.cloud.pubsub.topic.v1.messagePublished" \
             --service-account=PROJECT_NUMBER-compute@developer.gserviceaccount.com
         

Replace:

     * TRIGGER_NAME with the name for your trigger.

     * EVENTARC_TRIGGER_LOCATION with the location for the Eventarc trigger. In general, the location of an Eventarc trigger should match the location of the Google Cloud resource that you want to monitor for events. In most scenarios, you should also deploy your function in the same region. See [Understand Eventarc locations](https://docs.cloud.google.com/eventarc/docs/understand-locations) for more details about Eventarc trigger locations.

     * SERVICE with the name of the function you are deploying.

     * REGION with the Cloud Run [region](https://docs.cloud.google.com/run/docs/locations) of the function.

     * PROJECT_NUMBER with your Google Cloud project number. Eventarc triggers are linked to service accounts to use as an identity when invoking your function. Your Eventarc trigger's service account must have the permission to invoke your function. By default, Cloud Run uses the Default compute service account.

     * The `--event-filters` flag specifies the event filters that the trigger monitors. An event that matches all the `event-filters`, filters triggers calls to your function. Each trigger must have a supported [event type](https://docs.cloud.google.com/eventarc/docs/reference/supported-events#directly-from-a-google-cloud-source). You can't change the event filter type after creation. To change the event filter type, you must create a new trigger and delete the old one. Optionally, you can repeat the `--event-filters` flag with a supported filter in the form `ATTRIBUTE=VALUE` to add more filters.




## Cloud log entry

When a Cloud log entry that matches one of your filters is created, the corresponding log entries for your function in the [Google Cloud console](https://console.cloud.google.com/logs/viewer?resource=cloud_run_revision) should look as follows:
    
    
    Method: METHOD
    Resource: projects/YOUR_GCLOUD_PROJECT/...
    Initiator: YOUR_EMAIL_ADDRESS

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
