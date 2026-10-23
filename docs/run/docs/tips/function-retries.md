---
url: https://docs.cloud.google.com/run/docs/tips/function-retries/
title: Configure event-driven function retries \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:12.154948+00:00
---

# Configure event-driven function retries  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/tips/function-retries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Configure event-driven function retries Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure retries for [event-driven Cloud Run functions](https://docs.cloud.google.com/run/docs/write-functions#write-event-driven-functions).

As described in [Retry events](https://docs.cloud.google.com/eventarc/docs/retry-events#how_retries_work), when a Pub/Sub message destination can't acknowledge a message, the default Pub/Sub response is to send the message again with an exponential backoff delay. An exponential backoff lets you add progressively longer delays between retry attempts. But this might not be the behavior you want for your particular implementation.

The retries property is not implemented on the function itself but on the Eventarc trigger that invokes the function, which provides more flexibility. This means that for Cloud Run destinations (including Cloud Run functions created with either the Cloud Run Admin API or the Cloud Functions v2 API), you can configure a single delivery attempt with no retries. This is the default configuration when you create an Eventarc trigger in the Google Cloud console from the Cloud Run page. For more information, see [Create triggers with Eventarc](https://docs.cloud.google.com/run/docs/triggering/trigger-with-events).

## Why event-driven functions fail to complete

An event-driven function might fail to successfully complete due to errors thrown in the function code itself. The reasons this might happen include:

  * The function contains a bug and the runtime throws an exception.
  * The function cannot reach a service endpoint, or times out while trying to do so.
  * The function intentionally throws an exception (for example, when a parameter fails validation).
  * A Node.js function returns a rejected promise, or passes a non-`null` value to a callback.
  * On rare occasions, a function might exit prematurely due to an internal error, and by default, the function might or might not be automatically retried.



In any of these cases, the function will stop executing and return an error. Event triggers producing the messages have retry policies that you can customize to meet the needs of your function.

## Configure the retry policy

Depending on the needs of your Cloud Run function, you might want to configure the retry policy through the Pub/Sub subscription retry policy associated with your Eventarc trigger. This would allow you to set up any combination of the following:

  * Shorten the retry window from 7 days to as little as 10 minutes.
  * Change the minimum and maximum backoff time for the exponential backoff retry strategy.
  * Change the retry strategy to retry immediately.
  * Configure a [dead-letter topic](https://cloud.google.com/pubsub/docs/handling-failures#dead_letter_topic).
  * Set a maximum and minimum number of delivery attempts.



To configure the retry policy:

  1. Write an HTTP function.
  2. Use the Pub/Sub API to create a Pub/Sub subscription, specifying the URL of the function as the target.



See the [Eventarc documentation on retrying events](https://docs.cloud.google.com/eventarc/docs/retry-events) for additional best practices, such as making event-driven functions that can be retried [idempotent](https://docs.cloud.google.com/eventarc/docs/retry-events#idempotent-handlers).

See the [Pub/Sub documentation on handling failures](https://docs.cloud.google.com/pubsub/docs/handling-failures) for more information on configuring Pub/Sub directly.

## Best practices

This section describes best practices for using retries.

### Use retry to handle transient errors

Because your function is retried continuously until successful execution, permanent errors like bugs should be eliminated from your code through testing before enabling retries. Retries are best used to handle intermittent or transient failures that have a high likelihood of resolution upon retrying, such as a flaky service endpoint or timeout.

### Set an end condition to avoid infinite retry loops

It is best practice to protect your function against continuous looping when using retries. You can do this by including a well-defined end condition, _before_ the function begins processing. Note that this technique only works if your function starts successfully and is able to evaluate the end condition.

An effective approach is to discard events with timestamps older than a certain time. This helps to avoid excessive executions when failures are either persistent or longer-lived than expected.

For example, this code snippet discards all events older than 10 seconds:

###  Node.js 
    
    
    const functions = require('@google-cloud/functions-framework');
    
    /**
     * Cloud Event Function that only executes within
     * a certain time period after the triggering event
     *
     * @param {object} event The Cloud Functions event.
     * @param {function} callback The callback function.
     */
    functions.cloudEvent('avoidInfiniteRetries', (event, callback) => {
      const eventAge = Date.now() - Date.parse(event.time);
      const eventMaxAge = 10000;
    
      // Ignore events that are too old
      if (eventAge > eventMaxAge) {
        console.log(`Dropping event ${event} with age ${eventAge} ms.`);
        callback();
        return;
      }
    
      // Do what the function is supposed to do
      console.log(`Processing event ${event} with age ${eventAge} ms.`);
    
      // Retry failed function executions
      const failed = false;
      if (failed) {
        callback('some error');
      } else {
        callback();
      }
    });

###  Python 
    
    
    from datetime import datetime, timezone
    
    # The 'python-dateutil' package must be included in requirements.txt.
    from dateutil import parser
    
    import functions_framework
    
    
    @functions_framework.cloud_event
    def avoid_infinite_retries(cloud_event):
        """Cloud Event Function that only executes within a certain
        time period after the triggering event.
    
        Args:
            cloud_event: The cloud event associated with the current trigger
        Returns:
            None; output is written to Cloud Logging
        """
        timestamp = cloud_event["time"]
    
        event_time = parser.parse(timestamp)
        event_age = (datetime.now(timezone.utc) - event_time).total_seconds()
        event_age_ms = event_age * 1000
    
        # Ignore events that are too old
        max_age_ms = 10000
        if event_age_ms > max_age_ms:
            print("Dropped {} (age {}ms)".format(cloud_event["id"], event_age_ms))
            return "Timeout"
    
        # Do what the function is supposed to do
        print("Processed {} (age {}ms)".format(cloud_event["id"], event_age_ms))
        return  # To retry the execution, raise an exception here
    
    

###  Go 
    
    
    // Package tips contains tips for writing Cloud Functions in Go.
    package tips
    
    import (
    	"context"
    	"fmt"
    	"log"
    	"time"
    
    	"github.com/GoogleCloudPlatform/functions-framework-go/functions"
    	"github.com/cloudevents/sdk-go/v2/event"
    )
    
    func init() {
    	functions.CloudEvent("FiniteRetryPubSub", FiniteRetryPubSub)
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
    
    // FiniteRetryPubSub demonstrates how to avoid inifinite retries.
    func FiniteRetryPubSub(ctx context.Context, e event.Event) error {
    	var msg MessagePublishedData
    	if err := e.DataAs(&msg); err != nil {
    		return fmt.Errorf("event.DataAs: %w", err)
    	}
    
    	// Ignore events that are too old.
    	expiration := e.Time().Add(10 * time.Second)
    	if time.Now().After(expiration) {
    		log.Printf("event timeout: halting retries for expired event '%q'", e.ID())
    		return nil
    	}
    
    	// Add your message processing logic.
    	return processTheMessage(msg)
    }
    

###  Java 
    
    
    import com.google.cloud.functions.CloudEventsFunction;
    import io.cloudevents.CloudEvent;
    import java.time.Duration;
    import java.time.ZoneOffset;
    import java.time.ZonedDateTime;
    import java.util.logging.Logger;
    
    public class RetryTimeout implements CloudEventsFunction {
      private static final Logger logger = Logger.getLogger(RetryTimeout.class.getName());
      private static final long MAX_EVENT_AGE = 10_000;
    
      /**
       * Cloud Event Function that only executes within
       * a certain time period after the triggering event
       */
      @Override
      public void accept(CloudEvent event) throws Exception {
        ZonedDateTime utcNow = ZonedDateTime.now(ZoneOffset.UTC);
        ZonedDateTime timestamp = event.getTime().atZoneSameInstant(ZoneOffset.UTC);
    
        long eventAge = Duration.between(timestamp, utcNow).toMillis();
    
        // Ignore events that are too old
        if (eventAge > MAX_EVENT_AGE) {
          logger.info(String.format("Dropping event with timestamp %s.", timestamp));
          return;
        }
    
        // Process events that are recent enough
        // To retry this invocation, throw an exception here
        logger.info(String.format("Processing event with timestamp %s.", timestamp));
      }
    }

###  C# 
    
    
    using CloudNative.CloudEvents;
    using Google.Cloud.Functions.Framework;
    using Google.Events.Protobuf.Cloud.PubSub.V1;
    using Microsoft.Extensions.Logging;
    using System;
    using System.Threading;
    using System.Threading.Tasks;
    
    namespace TimeBoundedRetries;
    
    public class Function : ICloudEventFunction<MessagePublishedData>
    {
        private static readonly TimeSpan MaxEventAge = TimeSpan.FromSeconds(10);
        private readonly ILogger _logger;
    
        // Note: for additional testability, use an injectable clock abstraction.
        public Function(ILogger<Function> logger) =>
            _logger = logger;
    
        public Task HandleAsync(CloudEvent cloudEvent, MessagePublishedData data, CancellationToken cancellationToken)
        {
            string textData = data.Message.TextData;
    
            DateTimeOffset utcNow = DateTimeOffset.UtcNow;
    
            // Every PubSub CloudEvent will contain a timestamp.
            DateTimeOffset timestamp = cloudEvent.Time.Value;
            DateTimeOffset expiry = timestamp + MaxEventAge;
    
            // Ignore events that are too old.
            if (utcNow > expiry)
            {
                _logger.LogInformation("Dropping PubSub message '{text}'", textData);
                return Task.CompletedTask;
            }
    
            // Process events that are recent enough.
            // If this processing throws an exception, the message will be retried until either
            // processing succeeds or the event becomes too old and is dropped by the code above.
            _logger.LogInformation("Processing PubSub message '{text}'", textData);
            return Task.CompletedTask;
        }
    }

###  Ruby 
    
    
    require "functions_framework"
    
    FunctionsFramework.cloud_event "avoid_infinite_retries" do |event|
      # Use the event timestamp to determine the event age.
      event_age_secs = Time.now - event.time.to_time
      event_age_ms = (event_age_secs * 1000).to_i
    
      max_age_ms = 10_000
      if event_age_ms > max_age_ms
        # Ignore events that are too old.
        logger.info "Dropped #{event.id} (age #{event_age_ms}ms)"
    
      else
        # Do what the function is supposed to do.
        logger.info "Handling #{event.id} (age #{event_age_ms}ms)..."
        failed = true
    
        # Raise an exception to signal failure and trigger a retry.
        raise "I failed!" if failed
      end
    end

###  PHP 
    
    
    /**
     * This function shows an example method for avoiding infinite retries in
     * Google Cloud Functions. By default, functions configured to automatically
     * retry execution on failure will be retried indefinitely - causing an
     * infinite loop. To avoid this, we stop retrying executions (by not throwing
     * exceptions) for any events that are older than a predefined threshold.
     */
    
    use Google\CloudFunctions\CloudEvent;
    
    function avoidInfiniteRetries(CloudEvent $event): void
    {
        $log = fopen(getenv('LOGGER_OUTPUT') ?: 'php://stderr', 'wb');
    
        $eventId = $event->getId();
    
        // The maximum age of events to process.
        $maxAge = 10; // 10 seconds
    
        // The age of the event being processed.
        $eventAge = time() - strtotime($event->getTime());
    
        // Ignore events that are too old
        if ($eventAge > $maxAge) {
            fwrite($log, 'Dropping event ' . $eventId . ' with age ' . $eventAge . ' seconds' . PHP_EOL);
            return;
        }
    
        // Do what the function is supposed to do
        fwrite($log, 'Processing event: ' . $eventId . ' with age ' . $eventAge . ' seconds' . PHP_EOL);
    
        // infinite_retries failed function executions
        $failed = true;
        if ($failed) {
            throw new Exception('Event ' . $eventId . ' failed; retrying...');
        }
    }

### Distinguish between functions that can be retried and fatal errors

If your function has retries enabled, any unhandled error will trigger a retry. Make sure that your code captures any errors that shouldn't result in a retry.

###  Node.js 
    
    
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

###  Python 
    
    
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
    
    

###  Go 
    
    
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
    

###  Java 
    
    
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

###  C# 
    
    
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

###  Ruby 
    
    
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

###  PHP 
    
    
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

## Next steps

  * [Deploy a Cloud Run function](https://docs.cloud.google.com/run/docs/deploy-functions)
  * [Create triggers from Pub/Sub events](https://docs.cloud.google.com/run/docs/triggering/pubsub-triggers)
  * [Create triggers from Cloud Storage events](https://docs.cloud.google.com/run/docs/triggering/storage-triggers)
  * [Trigger functions from Pub/Sub using Eventarc](https://docs.cloud.google.com/run/docs/tutorials/pubsub-eventdriven)
  * [Trigger functions from Cloud Storage using Eventarc](https://docs.cloud.google.com/run/docs/tutorials/trigger-functions-storage)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
