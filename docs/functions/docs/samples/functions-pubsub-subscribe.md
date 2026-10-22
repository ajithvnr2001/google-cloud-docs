---
url: https://docs.cloud.google.com/functions/docs/samples/functions-pubsub-subscribe/
title: Pub/Sub Subscribe to a Topic \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:51:36.337989+00:00
---

# Pub/Sub Subscribe to a Topic  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-pubsub-subscribe/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  Pub/Sub Subscribe to a Topic Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to subscribe to a topic and parse the received event with Pub/Sub from Cloud Functions.

## Code sample

### Java

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.functions.BackgroundFunction;
    import com.google.cloud.functions.Context;
    import functions.eventpojos.PubsubMessage;
    import java.nio.charset.StandardCharsets;
    import java.util.Base64;
    import java.util.logging.Logger;
    
    public class SubscribeToTopic implements BackgroundFunction<PubsubMessage> {
      private static final Logger logger = Logger.getLogger(SubscribeToTopic.class.getName());
    
      @Override
      public void accept(PubsubMessage message, Context context) {
        if (message.getData() == null) {
          logger.info("No message provided");
          return;
        }
    
        String messageString = new String(
            Base64.getDecoder().decode(message.getData().getBytes(StandardCharsets.UTF_8)),
            StandardCharsets.UTF_8);
        logger.info(messageString);
      }
    }

### Node.js

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Triggered from a message on a Cloud Pub/Sub topic.
     *
     * @param {object} pubsubMessage The Cloud Pub/Sub Message object.
     * @param {string} pubsubMessage.data The "data" property of the Cloud Pub/Sub Message.
     */
    exports.subscribe = pubsubMessage => {
      // Print out the data from Pub/Sub, to prove that it worked
      console.log(Buffer.from(pubsubMessage.data, 'base64').toString());
    };

### Python

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Triggered from a message on a Cloud Pub/Sub topic.
    def subscribe(event, context):
        # Print out the data from Pub/Sub, to prove that it worked
        print(base64.b64decode(event["data"]))
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
