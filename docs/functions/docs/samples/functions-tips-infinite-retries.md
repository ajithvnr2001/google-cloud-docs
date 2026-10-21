---
url: https://docs.cloud.google.com/functions/docs/samples/functions-tips-infinite-retries/
title: Avoid infinite retries \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:03:32.709761+00:00
---

# Avoid infinite retries  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-tips-infinite-retries/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  Avoid infinite retries Stay organized with collections  Save and categorize content based on your preferences. 

Discards all events older than 10 seconds.

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

### Go

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    

### Java

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### Node.js

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### PHP

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### Python

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    
    

### Ruby

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
