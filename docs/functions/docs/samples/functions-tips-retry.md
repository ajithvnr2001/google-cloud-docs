---
url: https://docs.cloud.google.com/functions/docs/samples/functions-tips-retry/
title: Retry on error \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:51:54.401983+00:00
---

# Retry on error  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-tips-retry/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  Retry on error Stay organized with collections  Save and categorize content based on your preferences. 

Tells your function whether or not to retry execution when an error happens.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Configure event-driven function retries](https://docs.cloud.google.com/run/docs/tips/function-retries)
  * [Enable event-driven function retries (1st gen)](https://docs.cloud.google.com/functions/1stgendocs/bestpractices/retries)



## Code sample

### C#

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using CloudNative.CloudEvents;
    using Google.Cloud.Functions.Framework;
    using Google.Events.Protobuf.Cloud.PubSub.V1;
    using Microsoft.Extensions.Logging;
    using System;
    using System.Text.Json;
    using System.Threading;
    using System.Threading.Tasks;
    
    namespace Retry;
    
    public class Function : ICloudEventFunction<MessagePublishedData>
    {
        private readonly ILogger _logger;
    
        public Function(ILogger<Function> logger) =>
            _logger = logger;
    
        public Task HandleAsync(CloudEvent cloudEvent, MessagePublishedData data, CancellationToken cancellationToken)
        {
            bool retry = false;
            string text = data.Message?.TextData;
    
            // Get the value of the "retry" JSON parameter, if one exists.
            if (!string.IsNullOrEmpty(text))
            {
                JsonElement element = JsonSerializer.Deserialize<JsonElement>(data.Message.TextData);
    
                retry = element.TryGetProperty("retry", out var property) &&
                    property.ValueKind == JsonValueKind.True;
            }
    
            // Throwing an exception causes the execution to be retried.
            if (retry)
            {
                throw new InvalidOperationException("Retrying...");
            }
            else
            {
                _logger.LogInformation("Not retrying...");
            }
            return Task.CompletedTask;
        }
    }

### Go

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Package tips contains tips for writing Cloud Functions in Go.
    package tips
    
    import (
    	"context"
    	"errors"
    	"log"
    )
    
    // PubSubMessage is the payload of a Pub/Sub event.
    // See the documentation for more details:
    // https://cloud.google.com/pubsub/docs/reference/rest/v1/PubsubMessage
    type PubSubMessage struct {
    	Data []byte `json:"data"`
    }
    
    // RetryPubSub demonstrates how to toggle using retries.
    func RetryPubSub(ctx context.Context, m PubSubMessage) error {
    	name := string(m.Data)
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
    
    
    import com.google.cloud.functions.BackgroundFunction;
    import com.google.cloud.functions.Context;
    import com.google.gson.Gson;
    import com.google.gson.JsonElement;
    import com.google.gson.JsonObject;
    import functions.eventpojos.PubsubMessage;
    import java.nio.charset.StandardCharsets;
    import java.util.Base64;
    import java.util.logging.Logger;
    
    public class RetryPubSub implements BackgroundFunction<PubsubMessage> {
      private static final Logger logger = Logger.getLogger(RetryPubSub.class.getName());
    
      // Use Gson (https://github.com/google/gson) to parse JSON content.
      private static final Gson gson = new Gson();
    
      @Override
      public void accept(PubsubMessage message, Context context) {
        String bodyJson = new String(
            Base64.getDecoder().decode(message.getData()), StandardCharsets.UTF_8);
        JsonElement bodyElement = gson.fromJson(bodyJson, JsonElement.class);
    
        // Get the value of the "retry" JSON parameter, if one exists
        boolean retry = false;
        if (bodyElement != null && bodyElement.isJsonObject()) {
          JsonObject body = bodyElement.getAsJsonObject();
    
          if (body.has("retry") && body.get("retry").getAsBoolean()) {
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
    
    
    /**
     * Background Cloud Function that demonstrates
     * how to toggle retries using a promise
     *
     * @param {object} event The Cloud Functions event.
     * @param {object} event.data Data included with the event.
     * @param {object} event.data.retry User-supplied parameter that tells the function whether to retry.
     */
    exports.retryPromise = event => {
      const tryAgain = !!event.data.retry;
    
      if (tryAgain) {
        throw new Error('Retrying...');
      } else {
        console.error('Not retrying...');
        return Promise.resolve();
      }
    };
    
    /**
     * Background Cloud Function that demonstrates
     * how to toggle retries using a callback
     *
     * @param {object} event The Cloud Functions event.
     * @param {object} event.data Data included with the event.
     * @param {object} event.data.retry User-supplied parameter that tells the function whether to retry.
     * @param {function} callback The callback function.
     */
    exports.retryCallback = (event, callback) => {
      const tryAgain = !!event.data.retry;
      const err = new Error('Error!');
    
      if (tryAgain) {
        console.error('Retrying:', err);
        callback(err);
      } else {
        console.error('Not retrying:', err);
        callback();
      }
    };

### PHP

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\CloudFunctions\CloudEvent;
    
    function tipsRetry(CloudEvent $event): void
    {
        $cloudEventData = $event->getData();
        $pubSubData = $cloudEventData['message']['data'];
    
        $json = json_decode(base64_decode($pubSubData), true);
    
        // Determine whether to retry the invocation based on a parameter
        $tryAgain = $json['some_parameter'];
    
        if ($tryAgain) {
            /**
             * Functions with automatic retries enabled should throw exceptions to
             * indicate intermittent failures that a retry might fix. In this
             * case, a thrown exception will cause the original function
             * invocation to be re-sent.
             */
            throw new Exception('Intermittent failure occurred; retrying...');
        }
    
        /**
         * If a function with retries enabled encounters a non-retriable
         * failure, it should return *without* throwing an exception.
         */
        $log = fopen(getenv('LOGGER_OUTPUT') ?: 'php://stderr', 'wb');
        fwrite($log, 'Not retrying' . PHP_EOL);
    }

### Python

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import error_reporting
    
    
    error_client = error_reporting.[Client](https://docs.cloud.google.com/python/docs/reference/clouderrorreporting/latest/google.cloud.error_reporting.client.Client.html)()
    
    
    def retry_or_not(data, context):
        """Background Cloud Function that demonstrates how to toggle retries.
    
        Args:
            data (dict): The event payload.
            context (google.cloud.functions.Context): The event metadata.
        Returns:
            None; output is written to Cloud Logging
        """
    
        # Retry based on a user-defined parameter
        try_again = data.data.get("retry") is not None
    
        try:
            raise RuntimeError("I failed you")
        except RuntimeError:
            error_client.[report_exception](https://docs.cloud.google.com/python/docs/reference/clouderrorreporting/latest/google.cloud.error_reporting.client.Client.html#google_cloud_error_reporting_client_Client_report_exception)()
            if try_again:
                raise  # Raise the exception and try again
            else:
                pass  # Swallow the exception and don't retry
    
    

### Ruby

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "functions_framework"
    
    FunctionsFramework.cloud_event "retry_or_not" do |event|
      try_again = event.data["retry"]
    
      begin
        # Simulate a failure
        raise "I failed!"
      rescue RuntimeError => e
        logger.warn "Caught an error: #{e}"
        if try_again
          # Raise an exception to return a 500 and trigger a retry.
          logger.info "Trying again..."
          raise ex
        else
          # Return normally to end processing of this event.
          logger.info "Giving up."
        end
      end
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
