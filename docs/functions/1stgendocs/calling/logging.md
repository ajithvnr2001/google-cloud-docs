---
url: https://docs.cloud.google.com/functions/1stgendocs/calling/logging/
title: Second-Party Triggers with Cloud Logging \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:38.117186+00:00
---

# Second-Party Triggers with Cloud Logging  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/calling/logging/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Second-Party Triggers with Cloud Logging

[Many Google Cloud events](https://docs.cloud.google.com/logging/docs/audit/services) are logged in Cloud Audit Logs. You can filter these logs and forward them to Pub/Sub topics using [sinks](https://docs.cloud.google.com/logging/docs/export). These Pub/Sub topics can then send notifications that [trigger](https://docs.cloud.google.com/functions/1stgendocs/calling/pubsub) Cloud Run functions. This lets you create custom events from any Google Cloud service that produces [audit logs](https://docs.cloud.google.com/logging/docs/audit/services).

## Configuration

To run the sample in this document, you'll need a [Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/create-topic-console#create_a_topic) and a [Cloud Logging sink](https://docs.cloud.google.com/logging/docs/export/configure_export_v2#dest-create). The sample uses them to forward Cloud Audit Logs to a Cloud Run function.

## Event structure

Like all [Pub/Sub-triggered functions](https://docs.cloud.google.com/functions/1stgendocs/calling/pubsub), functions triggered by Cloud log entries receive a [`PubsubMessage`](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/PubsubMessage) object whose `data` parameter is a `base64`-encoded string. For Cloud log events, decoding this value returns the relevant log entry as a JSON string.

## Sample code

You can use a [Pub/Sub-triggered function](https://docs.cloud.google.com/functions/1stgendocs/calling/pubsub) to detect and respond to exported Cloud logs:

###  Node.js 
    
    
    exports.processLogEntry = data => {
      const dataBuffer = Buffer.from(data.data, 'base64');
    
      const logEntry = JSON.parse(dataBuffer.toString('ascii')).protoPayload;
      console.log(`Method: ${logEntry.methodName}`);
      console.log(`Resource: ${logEntry.resourceName}`);
      console.log(`Initiator: ${logEntry.authenticationInfo.principalEmail}`);
    };

###  Python 
    
    
    import base64
    import json
    
    def process_log_entry(data, context):
        data_buffer = base64.b64decode(data["data"])
        log_entry = json.loads(data_buffer)["protoPayload"]
    
        print(f"Method: {log_entry['methodName']}")
        print(f"Resource: {log_entry['resourceName']}")
        print(f"Initiator: {log_entry['authenticationInfo']['principalEmail']}")
    
    

###  Go 
    
    
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
    

###  Java 
    
    
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

## Deploying a function

Use the following command to deploy the function:

###  Node.js 
    
    
    gcloud functions deploy processLogEntry \
    --runtime nodejs22 \  
    --trigger-topic YOUR_PUBSUB_TOPIC/  
    FLAGS...

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Node.js version](https://docs.cloud.google.com/static/functions/docs/runtime-support#node.js) to run your function. 

###  Python 
    
    
    gcloud functions deploy process_log_entry \
    --runtime python312 \  
    --trigger-topic YOUR_PUBSUB_TOPIC/  
    FLAGS...

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Python version](https://docs.cloud.google.com/functions/docs/runtime-support#python) to run your function. 

###  Go 
    
    
    gcloud functions deploy ProcessLogEntry \
    --runtime go121 \  
    --trigger-topic YOUR_PUBSUB_TOPIC/  
    FLAGS...

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Go version](https://docs.cloud.google.com/functions/docs/runtime-support#go) to run your function. 

###  Java 
    
    
    gcloud functions deploy java-log-function \
    --entry-point StackdriverLogging \
    --runtime java17 \
    --memory 512MB \  
    --trigger-topic YOUR_PUBSUB_TOPIC/  
    FLAGS...

Use the [`--runtime`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--runtime) flag to specify the runtime ID of a [supported Java version](https://docs.cloud.google.com/functions/docs/runtime-support#java) to run your function. 

## Triggering a function

When a Cloud log entry that matches one of your filters is created, you [should see](https://console.cloud.google.com/logs/viewer?resource=cloud_function) corresponding log entries for your function:
    
    
    Method: METHOD
    Resource: projects/YOUR_GCLOUD_PROJECT/...
    Initiator: YOUR_EMAIL_ADDRESS

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
