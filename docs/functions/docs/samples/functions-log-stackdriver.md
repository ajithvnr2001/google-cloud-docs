---
url: https://docs.cloud.google.com/functions/docs/samples/functions-log-stackdriver/
title: Trigger function from Cloud Logging \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:51:19.800088+00:00
---

# Trigger function from Cloud Logging  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-log-stackdriver/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  Trigger function from Cloud Logging Stay organized with collections  Save and categorize content based on your preferences. 

Triggers a function based on Cloud Logging entries.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Second-Party Triggers with Cloud Logging](https://docs.cloud.google.com/functions/1stgendocs/calling/logging)
  * [Trigger functions from log entries](https://docs.cloud.google.com/run/docs/triggering/trigger-functions-from-log-entries)



## Code sample

### Go

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### Node.js

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    exports.processLogEntry = data => {
      const dataBuffer = Buffer.from(data.data, 'base64');
    
      const logEntry = JSON.parse(dataBuffer.toString('ascii')).protoPayload;
      console.log(`Method: ${logEntry.methodName}`);
      console.log(`Resource: ${logEntry.resourceName}`);
      console.log(`Initiator: ${logEntry.authenticationInfo.principalEmail}`);
    };

### Python

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import base64
    import json
    
    def process_log_entry(data, context):
        data_buffer = base64.b64decode(data["data"])
        log_entry = json.loads(data_buffer)["protoPayload"]
    
        print(f"Method: {log_entry['methodName']}")
        print(f"Resource: {log_entry['resourceName']}")
        print(f"Initiator: {log_entry['authenticationInfo']['principalEmail']}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
