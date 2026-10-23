---
url: https://docs.cloud.google.com/functions/docs/samples/functions-cloudevent-pubsub/
title: Cloud Pub/Sub (2nd Gen) \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:08:52.345516+00:00
---

# Cloud Pub/Sub (2nd Gen)  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-cloudevent-pubsub/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  Cloud Pub/Sub (2nd Gen) Stay organized with collections  Save and categorize content based on your preferences. 

Process a Cloud Pub/Sub message using Cloud Functions (2nd Gen) and Eventarc

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [The Go Runtime](https://docs.cloud.google.com/functions/1stgendocs/concepts/go-runtime)
  * [The Go runtime](https://docs.cloud.google.com/run/docs/runtimes/go)
  * [Trigger functions from Pub/Sub using Eventarc](https://docs.cloud.google.com/run/docs/tutorials/pubsub-eventdriven)



## Code sample

### C#

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using CloudNative.CloudEvents;
    using Google.Cloud.Functions.Framework;
    using Google.Events.Protobuf.Cloud.PubSub.V1;
    using Microsoft.Extensions.Logging;
    using System.Threading;
    using System.Threading.Tasks;
    
    namespace HelloPubSub;
    
    public class Function : ICloudEventFunction<MessagePublishedData>
    {
        private readonly ILogger _logger;
    
        public Function(ILogger<Function> logger) =>
            _logger = logger;
    
        public Task HandleAsync(CloudEvent cloudEvent, MessagePublishedData data, CancellationToken cancellationToken)
        {
            string nameFromMessage = data.Message?.TextData;
            string name = string.IsNullOrEmpty(nameFromMessage) ? "world" : nameFromMessage;
            _logger.LogInformation("Hello {name}", name);
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
    
    	"github.com/GoogleCloudPlatform/functions-framework-go/functions"
    	"github.com/cloudevents/sdk-go/v2/event"
    )
    
    func init() {
    	functions.CloudEvent("HelloPubSub", helloPubSub)
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
    
    // helloPubSub consumes a CloudEvent message and extracts the Pub/Sub message.
    func helloPubSub(ctx context.Context, e event.Event) error {
    	var msg MessagePublishedData
    	if err := e.DataAs(&msg); err != nil {
    		return fmt.Errorf("event.DataAs: %w", err)
    	}
    
    	name := string(msg.Message.Data) // Automatically decoded from base64.
    	if name == "" {
    		name = "World"
    	}
    	log.Printf("Hello, %s!", name)
    	return nil
    }
    

### Java

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.functions.CloudEventsFunction;
    import com.google.gson.Gson;
    import functions.eventpojos.PubSubBody;
    import io.cloudevents.CloudEvent;
    import java.nio.charset.StandardCharsets;
    import java.util.Base64;
    import java.util.logging.Logger;
    
    public class SubscribeToTopic implements CloudEventsFunction {
      private static final Logger logger = Logger.getLogger(SubscribeToTopic.class.getName());
    
      @Override
      public void accept(CloudEvent event) {
        // The Pub/Sub message is passed as the CloudEvent's data payload.
        if (event.getData() != null) {
          // Extract Cloud Event data and convert to PubSubBody
          String cloudEventData = new String(event.getData().toBytes(), StandardCharsets.UTF_8);
          Gson gson = new Gson();
          PubSubBody body = gson.fromJson(cloudEventData, PubSubBody.class);
          // Retrieve and decode PubSub message data
          String encodedData = body.getMessage().getData();
          String decodedData =
              new String(Base64.getDecoder().decode(encodedData), StandardCharsets.UTF_8);
          logger.info("Hello, " + decodedData + "!");
        }
      }
    }

### Node.js

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const functions = require('@google-cloud/functions-framework');
    
    // Register a CloudEvent callback with the Functions Framework that will
    // be executed when the Pub/Sub trigger topic receives a message.
    functions.cloudEvent('helloPubSub', cloudEvent => {
      // The Pub/Sub message is passed as the CloudEvent's data payload.
      const base64name = cloudEvent.data.message.data;
    
      const name = base64name
        ? Buffer.from(base64name, 'base64').toString()
        : 'World';
    
      console.log(`Hello, ${name}!`);
    });

### PHP

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use CloudEvents\V1\CloudEventInterface;
    use Google\CloudFunctions\FunctionsFramework;
    
    // Register the function with Functions Framework.
    // This enables omitting the `FUNCTIONS_SIGNATURE_TYPE=cloudevent` environment
    // variable when deploying. The `FUNCTION_TARGET` environment variable should
    // match the first parameter.
    FunctionsFramework::cloudEvent('helloworldPubsub', 'helloworldPubsub');
    
    function helloworldPubsub(CloudEventInterface $event): void
    {
        $log = fopen(getenv('LOGGER_OUTPUT') ?: 'php://stderr', 'wb');
    
        $cloudEventData = $event->getData();
        $pubSubData = base64_decode($cloudEventData['message']['data']);
    
        $name = $pubSubData ? htmlspecialchars($pubSubData) : 'World';
        fwrite($log, "Hello, $name!" . PHP_EOL);
    }

### Python

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import base64
    
    from cloudevents.http import CloudEvent
    import functions_framework
    
    
    # Triggered from a message on a Cloud Pub/Sub topic.
    @functions_framework.cloud_event
    def subscribe(cloud_event: CloudEvent) -> None:
        # Print out the data from Pub/Sub, to prove that it worked
        print(
            "Hello, " + base64.b64decode(cloud_event.data["message"]["data"]).decode() + "!"
        )
    
    

### Ruby

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "functions_framework"
    require "base64"
    
    FunctionsFramework.cloud_event "hello_pubsub" do |event|
      # The event parameter is a CloudEvents::Event::V1 object.
      # See https://cloudevents.github.io/sdk-ruby/latest/CloudEvents/Event/V1.html
      name = Base64.decode64 event.data["message"]["data"] rescue "World"
    
      # A cloud_event function does not return a response, but you can log messages
      # or cause side effects such as sending additional events.
      logger.info "Hello, #{name}!"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudfunctions). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
