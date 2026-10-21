---
url: https://docs.cloud.google.com/functions/1stgendocs/bestpractices/retries/
title: Enable event-driven function retries (1st gen) \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:34.406674+00:00
---

# Enable event-driven function retries (1st gen)  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/bestpractices/retries/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Enable event-driven function retries (1st gen)

This document describes how to enable retrying for [event-driven functions](https://docs.cloud.google.com/functions/1stgendocs/writing/write-event-driven-functions). Automatic retrying is not available for HTTP functions.

**Note:** The type of event-driven function you use (CloudEvent function or background function) is determined by the runtime your function will run on.

## Semantics of retry

Cloud Run functions provides at-least-once execution of an event-driven function for each event emitted by an event source. By default, if a function invocation terminates with an error, the function is not invoked again and the event is dropped. When you enable retries on an event-driven function, Cloud Run functions retries a failed function invocation until it completes successfully or the retry window expires.

This retry window expires expires after 7 days. Cloud Run functions retries newly created event-driven functions using an exponential backoff strategy, with an increasing backoff of between 10 and 600 seconds. This policy is applied to new functions the first time you deploy them. It is not retroactively applied to existing functions that were first deployed before the changes described in [this release note](https://docs.cloud.google.com/functions/docs/release-notes#April_20_2023) took effect, even if you redeploy the functions.

When retries are not enabled for a function, which is the default, the function always reports that it executed successfully, and `200 OK` response codes might appear in its logs. This occurs even if the function encountered an error. To make it clear when your function encounters an error, be sure to [report errors](https://docs.cloud.google.com/functions/1stgendocs/monitoring/error-reporting) appropriately.

## Why event-driven functions fail to complete

On rare occasions, a function might exit prematurely due to an internal error, and by default the function might or might not be automatically retried.

More typically, an event-driven function might fail to successfully complete due to errors thrown in the function code itself. The reasons this might happen include:

  * The function contains a bug and the runtime throws an exception.
  * The function cannot reach a service endpoint, or times out while trying to do so.
  * The function intentionally throws an exception (for example, when a parameter fails validation).
  * A Node.js function returns a rejected promise, or passes a non-`null` value to a callback.



In any of these cases, the function stops executing by default and the event is discarded. To retry the function when an error occurs, you can change the default retry policy by setting the "retry on failure" property. This causes the event to be retried repeatedly until the function successfully completes or the retry timeout expires.

**Warning:** Setting "retry on failure" causes your function to be retried repeatedly until it either successfully executes or the maximum retry period has elapsed, which can be multiple days. If the failure is due to a bug or any other sort of permanent error, your function can get stuck in a retry loop. You should only use this setting when dealing with transient failures (such as an unreliable endpoint or intermittent timeouts), and only after pressure-testing your code without this property set. If your function does become stuck in a retry loop, you must either redeploy it or delete it to end execution.

## Enable or disable retries

To enable or disable retries, you can either use the `gcloud` command-line tool or the Google Cloud console. By default, retries are disabled.

### Configure retries from the `gcloud` command-line tool

To enable retries using the `gcloud` command-line tool, include the `--retry` flag when deploying your function:
    
    
    gcloud functions deploy FUNCTION_NAME --retry FLAGS...

To disable retries, re-deploy the function without the `--retry` flag:
    
    
    gcloud functions deploy FUNCTION_NAME FLAGS...

### Configure retries from the console

If you're creating a new function:

  1. From the [Create Function](https://console.cloud.google.com/functions/add) screen, under **Trigger** and choose the type of event to act as a trigger for your function.
  2. Select the **Retry on failure** checkbox to enable retries.



If you're updating an existing function:

  1. From the [Cloud Run functions Overview](https://console.cloud.google.com/functions/list) page, click the name of the function you're updating to open its **Function details** screen, then choose **Edit** from the menu bar to display **Trigger** pane.
  2. Select or clear the **Retry on failure** checkbox to enable or disable retries.



## Best practices

This section describes best practices for using retries.

### Use retry to handle transient errors

Because your function is retried continuously until successful execution, permanent errors like bugs should be eliminated from your code through testing before enabling retries. Retries are best used to handle intermittent or transient failures that have a high likelihood of resolution upon retrying, such as a flaky service endpoint or timeout.

### Set an end condition to avoid infinite retry loops

It is best practice to protect your function against continuous looping when using retries. You can do this by including a well-defined end condition, _before_ the function begins processing. Note that this technique only works if your function starts successfully and is able to evaluate the end condition.

A simple yet effective approach is to discard events with timestamps older than a certain time. This helps to avoid excessive executions when failures are either persistent or longer-lived than expected.

For example, this code snippet discards all events older than 10 seconds:

###  Node.js 
    
    
    /**
     * Background Cloud Function that only executes within
     * a certain time period after the triggering event
     *
     * @param {object} event The Cloud Functions event.
     * @param {function} callback The callback function.
     */
    exports.avoidInfiniteRetries = (event, callback) => {
      const eventAge = Date.now() - Date.parse(event.timestamp);
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
    };

###  Python 
    
    
    from datetime import datetime, timezone
    
    # The 'python-dateutil' package must be included in requirements.txt.
    from dateutil import parser
    
    
    def avoid_infinite_retries(data, context):
        """Background Cloud Function that only executes within a certain
        time period after the triggering event.
    
        Args:
            data (dict): The event payload.
            context (google.cloud.functions.Context): The event metadata.
        Returns:
            None; output is written to Stackdriver Logging
        """
    
        timestamp = context.timestamp
    
        event_time = parser.parse(timestamp)
        event_age = (datetime.now(timezone.utc) - event_time).total_seconds()
        event_age_ms = event_age * 1000
    
        # Ignore events that are too old
        max_age_ms = 10000
        if event_age_ms > max_age_ms:
            print(f"Dropped {context.event_id} (age {event_age_ms}ms)")
            return "Timeout"
    
        # Do what the function is supposed to do
        print(f"Processed {context.event_id} (age {event_age_ms}ms)")
        return  # To retry the execution, raise an exception here
    
    

###  Go 
    
    
    // Package tips contains tips for writing Cloud Functions in Go.
    package tips
    
    import (
    	"context"
    	"fmt"
    	"log"
    	"time"
    
    	"cloud.google.com/go/functions/metadata"
    )
    
    // PubSubMessage is the payload of a Pub/Sub event.
    // See the documentation for more details:
    // https://cloud.google.com/pubsub/docs/reference/rest/v1/PubsubMessage
    type PubSubMessage struct {
    	Data []byte `json:"data"`
    }
    
    // FiniteRetryPubSub demonstrates how to avoid inifinite retries.
    func FiniteRetryPubSub(ctx context.Context, m PubSubMessage) error {
    	meta, err := metadata.[FromContext](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/functions/latest/metadata.html#cloud_google_com_go_functions_metadata_Metadata_FromContext)(ctx)
    	if err != nil {
    		// Assume an error on the function invoker and try again.
    		return fmt.Errorf("metadata.FromContext: %w", err)
    	}
    
    	// Ignore events that are too old.
    	expiration := meta.Timestamp.Add(10 * time.Second)
    	if time.Now().After(expiration) {
    		log.Printf("event timeout: halting retries for expired event '%q'", meta.EventID)
    		return nil
    	}
    
    	// Add your message processing logic.
    	return processTheMessage(m)
    }
    

###  Java 
    
    
    import com.google.cloud.functions.BackgroundFunction;
    import com.google.cloud.functions.Context;
    import com.google.gson.Gson;
    import functions.eventpojos.PubsubMessage;
    import java.time.Duration;
    import java.time.ZoneOffset;
    import java.time.ZonedDateTime;
    import java.util.logging.Logger;
    
    public class RetryTimeout implements BackgroundFunction<PubsubMessage> {
      private static final Logger logger = Logger.getLogger(RetryTimeout.class.getName());
      private static final long MAX_EVENT_AGE = 10_000;
    
      // Use Gson (https://github.com/google/gson) to parse JSON content.
      private static final Gson gson = new Gson();
    
      /**
       * Background Cloud Function that only executes within
       * a certain time period after the triggering event
       */
      @Override
      public void accept(PubsubMessage message, Context context) {
        ZonedDateTime utcNow = ZonedDateTime.now(ZoneOffset.UTC);
        ZonedDateTime timestamp = ZonedDateTime.parse(context.timestamp());
    
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

###  Python 
    
    
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
    
    

###  Go 
    
    
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
    

###  Java 
    
    
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

### Make retryable event-driven functions idempotent

Event-driven functions that can be retried must be idempotent. Here are some general guidelines for making such a function idempotent:

  * Many external APIs (such as Stripe) let you supply an idempotency key as a parameter. If you are using such an API, you should use the event ID as the idempotency key.
  * Idempotency works well with at-least-once delivery, because it makes it safe to retry. So a general best practice for writing reliable code is to combine idempotency with retries.
  * Make sure that your code is internally idempotent. For example: 
    * Make sure that mutations can happen more than once without changing the outcome.
    * Query database state in a transaction before mutating the state.
    * Make sure that all side effects are themselves idempotent.
  * Impose a transactional check outside the function, independent of the code. For example, persist state somewhere recording that a given event ID has already been processed.
  * Deal with duplicate function calls out-of-band. For example, have a separate clean up process that cleans up after duplicate function calls.



## Configure the retry policy

Depending on the needs of your function, you may want to configure the retry policy directly. This would allow you to set up any combination of the following:

  * Shorten the retry window from 7 days to as little as 10 minutes.
  * Change the minimum and maximum backoff time for the exponential backoff retry strategy.
  * Change the retry strategy to retry immediately.
  * Configure a [dead-letter topic](https://cloud.google.com/pubsub/docs/handling-failures#dead_letter_topic).
  * Set a maximum and minimum number of delivery attempts.



To configure the retry policy:

  1. Write an HTTP function.
  2. Use the Pub/Sub API to create a Pub/Sub subscription, specifying the URL of the function as the target.



See [Pub/Sub documentation on handling failures](https://cloud.google.com/pubsub/docs/handling-failures) for a more information on configuring Pub/Sub directly.

## Next steps

  * [Deploying Cloud Run functions](https://docs.cloud.google.com/functions/1stgendocs/deploy).
  * [Calling Pub/Sub Trigger Functions](https://docs.cloud.google.com/functions/1stgendocs/calling/pubsub).
  * [Calling Cloud Storage Trigger Functions](https://docs.cloud.google.com/functions/1stgendocs/calling/storage).
  * [Cloud Run functions with Pub/Sub Tutorial](https://docs.cloud.google.com/functions/1stgendocs/tutorials/pubsub-1st-gen).
  * [Cloud Run functions with Cloud Storage Tutorial](https://docs.cloud.google.com/functions/1stgendocs/tutorials/storage-1st-gen).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
