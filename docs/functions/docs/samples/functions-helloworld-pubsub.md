---
url: https://docs.cloud.google.com/functions/docs/samples/functions-helloworld-pubsub/
title: Cloud Functions (1st Gen): Pub/Sub Hello World \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:03:32.908219+00:00
---

# Cloud Functions (1st Gen): Pub/Sub Hello World  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/samples/functions-helloworld-pubsub/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Samples ](https://docs.cloud.google.com/functions/docs/samples)



#  Cloud Functions (1st Gen): Pub/Sub Hello World Stay organized with collections  Save and categorize content based on your preferences. 

Example Pub/Sub-triggered function that runs on Cloud Functions (1st Gen).

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Call Cloud Run functions directly](https://docs.cloud.google.com/functions/1stgendocs/running/direct)
  * [Cloud Pub/Sub Tutorial (1st gen)](https://docs.cloud.google.com/functions/1stgendocs/tutorials/pubsub-1st-gen)
  * [JVM Languages](https://docs.cloud.google.com/functions/1stgendocs/concepts/jvm-langs)
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
    	"log"
    )
    
    // PubSubMessage is the payload of a Pub/Sub event.
    // See the documentation for more details:
    // https://cloud.google.com/pubsub/docs/reference/rest/v1/PubsubMessage
    type PubSubMessage struct {
    	Data []byte `json:"data"`
    }
    
    // HelloPubSub consumes a Pub/Sub message.
    func HelloPubSub(ctx context.Context, m PubSubMessage) error {
    	name := string(m.Data) // Automatically decoded from base64.
    	if name == "" {
    		name = "World"
    	}
    	log.Printf("Hello, %s!", name)
    	return nil
    }
    

### Java

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.functions.BackgroundFunction;
    import com.google.cloud.functions.Context;
    import functions.eventpojos.PubsubMessage;
    import java.nio.charset.StandardCharsets;
    import java.util.Base64;
    import java.util.logging.Level;
    import java.util.logging.Logger;
    
    public class HelloPubSub implements BackgroundFunction<PubsubMessage> {
      private static final Logger logger = Logger.getLogger(HelloPubSub.class.getName());
    
      @Override
      public void accept(PubsubMessage message, Context context) {
        String name = "world";
        if (message != null && message.getData() != null) {
          name = new String(
              Base64.getDecoder().decode(message.getData().getBytes(StandardCharsets.UTF_8)),
              StandardCharsets.UTF_8);
        }
        logger.info(String.format("Hello %s!", name));
        return;
      }
    }

### Kotlin
    
    
    import com.google.cloud.functions.BackgroundFunction
    import com.google.cloud.functions.Context
    import functions.eventpojos.PubsubMessage
    import java.nio.charset.StandardCharsets
    import java.util.Base64
    import java.util.logging.Logger
    
    
    class KotlinHelloPubSub : BackgroundFunction<PubsubMessage> {
        override fun accept(message: PubsubMessage, context: Context) {
            // name's default value is "world"
            var name = "world"
            if (message?.data != null) {
                name = String(
                        Base64.getDecoder().decode(message.data!!.toByteArray(StandardCharsets.UTF_8)),
                        StandardCharsets.UTF_8)
            }
            LOGGER.info(String.format("Hello %s!", name))
            return;
        }
    
        companion object {
            private val LOGGER = Logger.getLogger(KotlinHelloPubSub::class.java.name)
        }
    }

### Node.js

To authenticate to Cloud Run functions, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Background Cloud Function to be triggered by Pub/Sub.
     * This function is exported by index.js, and executed when
     * the trigger topic receives a message.
     *
     * @param {object} message The Pub/Sub message.
     * @param {object} context The event metadata.
     */
    exports.helloPubSub = (message, context) => {
      const name = message.data
        ? Buffer.from(message.data, 'base64').toString()
        : 'World';
    
      console.log(`Hello, ${name}!`);
    };

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
    
    
    def hello_pubsub(event, context):
        """Background Cloud Function to be triggered by Pub/Sub.
        Args:
             event (dict):  The dictionary with data specific to this type of
                            event. The `@type` field maps to
                             `type.googleapis.com/google.pubsub.v1.PubsubMessage`.
                            The `data` field maps to the PubsubMessage data
                            in a base64-encoded string. The `attributes` field maps
                            to the PubsubMessage attributes if any is present.
             context (google.cloud.functions.Context): Metadata of triggering event
                            including `event_id` which maps to the PubsubMessage
                            messageId, `timestamp` which maps to the PubsubMessage
                            publishTime, `event_type` which maps to
                            `google.pubsub.topic.publish`, and `resource` which is
                            a dictionary that describes the service API endpoint
                            pubsub.googleapis.com, the triggering topic's name, and
                            the triggering event type
                            `type.googleapis.com/google.pubsub.v1.PubsubMessage`.
        Returns:
            None. The output is written to Cloud Logging.
        """
        import base64
    
        print(
            """This Function was triggered by messageId {} published at {} to {}
        """.format(
                context.event_id, context.timestamp, context.resource["name"]
            )
        )
    
        if "data" in event:
            name = base64.b64decode(event["data"]).decode("utf-8")
        else:
            name = "World"
        print(f"Hello {name}!")
    
    

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
