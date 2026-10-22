---
url: https://docs.cloud.google.com/functions/docs/samples/functions-cloudevent-tips-retry/
title: Toggle retries for Cloud Functions \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:51:24.345614+00:00
---

# Toggle retries for Cloud Functions  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-cloudevent-tips-retry/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  Toggle retries for Cloud Functions Stay organized with collections  Save and categorize content based on your preferences. 

This sample demonstrates how to toggle retries for Cloud Functions using the error reporting client.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Configure event-driven function retries](https://docs.cloud.google.com/run/docs/tips/function-retries)



## Code sample

### Go

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    package tips
    
    import (
    	"context"
    	"errors"
    	"fmt"
    	"log"
    
    	"github.com/GoogleCloudPlatform/functions-framework-go/functions"
    	"github.com/cloudevents/sdk-go/v2/event"
    )
    
    func init() {
    	functions.CloudEvent("RetryPubSub", RetryPubSub)
    }
    
    // MessagePublishedData contains the full Pub/Sub message
    // See the documentation for more details:
    // https://cloud.google.com/eventarc/docs/cloudevents#pubsub
    type MessagePublishedData struct {
    	Message PubSubMessage
    }
    
    // PubSubMessage is the payload of a Pub/Sub event.
    // See the documentation for more details:
    // https://cloud.google.com/pubsub/docs/reference/rest/v1/PubsubMessage
    type PubSubMessage struct {
    	Data []byte `json:"data"`
    }
    
    // RetryPubSub demonstrates how to toggle using retries.
    func RetryPubSub(ctx context.Context, e event.Event) error {
    	var msg MessagePublishedData
    	if err := e.DataAs(&msg); err != nil {
    		return fmt.Errorf("event.DataAs: %w", err)
    	}
    
    	name := string(msg.Message.Data)
    	if name == "" {
    		name = "World"
    	}
    
    	// A misconfigured client will stay broken until the function is redeployed.
    	client, err := MisconfiguredDataClient()
    	if err != nil {
    		log.Printf("MisconfiguredDataClient (retry denied):  %v", err)
    		// A nil return indicates that the function does not need a retry.
    		return nil
    	}
    
    	// Runtime error might be resolved with a new attempt.
    	if err = FailedWriteOperation(client, name); err != nil {
    		log.Printf("FailedWriteOperation (retry expected): %v", err)
    		// A non-nil return indicates that a retry is needed.
    		return err
    	}
    
    	return nil
    }
    

### Java

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.functions.CloudEventsFunction;
    import com.google.gson.Gson;
    import com.google.gson.JsonElement;
    import com.google.gson.JsonObject;
    import functions.eventpojos.PubSubBody;
    import io.cloudevents.CloudEvent;
    import java.nio.charset.StandardCharsets;
    import java.util.Base64;
    import java.util.logging.Logger;
    
    public class RetryPubSub implements CloudEventsFunction {
      private static final Logger logger = Logger.getLogger(RetryPubSub.class.getName());
    
      // Use Gson (https://github.com/google/gson) to parse JSON content.
      private static final Gson gson = new Gson();
    
      @Override
      public void accept(CloudEvent event) throws Exception {
        if (event.getData() == null) {
          logger.warning("No data found in event!");
          return;
        }
    
        // Extract Cloud Event data and convert to PubSubBody
        String cloudEventData = new String(event.getData().toBytes(), StandardCharsets.UTF_8);
        PubSubBody body = gson.fromJson(cloudEventData, PubSubBody.class);
    
        String encodedData = body.getMessage().getData();
        String decodedData =
            new String(Base64.getDecoder().decode(encodedData), StandardCharsets.UTF_8);
    
        // Retrieve and decode PubSubMessage data into a JsonElement.
        // Function is expecting a user-supplied JSON message which determines whether
        // to retry or not.
        JsonElement jsonPubSubMessageElement = gson.fromJson(decodedData, JsonElement.class);
    
        boolean retry = false;
        // Get the value of the "retry" JSON parameter, if one exists
        if (jsonPubSubMessageElement != null && jsonPubSubMessageElement.isJsonObject()) {
          JsonObject jsonPubSubMessageObject = jsonPubSubMessageElement.getAsJsonObject();
    
          if (jsonPubSubMessageObject.has("retry")
              && jsonPubSubMessageObject.get("retry").getAsBoolean()) {
            retry = true;
          }
        }
    
        // Retry if appropriate
        if (retry) {
          // Throwing an exception causes the execution to be retried
          throw new RuntimeException("Retrying...");
        } else {
          logger.info("Not retrying...");
        }
      }
    }

### Node.js

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const functions = require('@google-cloud/functions-framework');
    
    /**
     * Register a Cloud Event Function that demonstrates
     * how to toggle retries using a promise
     *
     * @param {object} event The Cloud Event for the function trigger.
     */
    functions.cloudEvent('retryPromise', cloudEvent => {
      // The Pub/Sub event payload is passed as the CloudEvent's data payload.
      // See the documentation for more details:
      // https://cloud.google.com/eventarc/docs/cloudevents#pubsub
      const base64PubsubMessage = cloudEvent.data.message.data;
      const jsonString = Buffer.from(base64PubsubMessage, 'base64').toString();
    
      const tryAgain = JSON.parse(jsonString).retry;
    
      if (tryAgain) {
        throw new Error('Retrying...');
      } else {
        console.error('Not retrying...');
        return Promise.resolve();
      }
    });
    
    /**
     * Cloud Event Function that demonstrates
     * how to toggle retries using a callback
     *
     * @param {object} event The Cloud Event for the function trigger.
     * @param {function} callback The callback function.
     */
    functions.cloudEvent('retryCallback', (cloudEvent, callback) => {
      // The Pub/Sub event payload is passed as the CloudEvent's data payload.
      // See the documentation for more details:
      // https://cloud.google.com/eventarc/docs/cloudevents#pubsub
      const base64PubsubMessage = cloudEvent.data.message.data;
      const jsonString = Buffer.from(base64PubsubMessage, 'base64').toString();
    
      const tryAgain = JSON.parse(jsonString).retry;
      const err = new Error('Error!');
    
      if (tryAgain) {
        console.error('Retrying:', err);
        callback(err);
      } else {
        console.error('Not retrying:', err);
        callback();
      }
    });

### Python

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import base64
    import json
    
    import functions_framework
    from google.cloud import error_reporting
    
    
    error_client = error_reporting.[Client](https://docs.cloud.google.com/python/docs/reference/clouderrorreporting/latest/google.cloud.error_reporting.client.Client.html)()
    
    
    @functions_framework.cloud_event
    def retry_or_not(cloud_event):
        """Cloud Event Function that demonstrates how to toggle retries.
    
        Args:
            cloud_event: The cloud event with a Pub/Sub data payload
        Returns:
            None; output is written to Cloud Logging
        """
    
        # The Pub/Sub event payload is passed as the CloudEvent's data payload.
        # See the documentation for more details:
        # https://cloud.google.com/eventarc/docs/cloudevents#pubsub
        encoded_pubsub_message = cloud_event.data["message"]["data"]
    
        # Retry based on a user-defined parameter
        try_again = json.loads(base64.b64decode(encoded_pubsub_message).decode())["retry"]
    
        try:
            raise RuntimeError("I failed you")
        except RuntimeError:
            error_client.[report_exception](https://docs.cloud.google.com/python/docs/reference/clouderrorreporting/latest/google.cloud.error_reporting.client.Client.html#google_cloud_error_reporting_client_Client_report_exception)()
            if try_again:
                raise  # Raise the exception and try again
            else:
                pass  # Swallow the exception and don't retry
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
