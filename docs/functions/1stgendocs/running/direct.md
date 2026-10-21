---
url: https://docs.cloud.google.com/functions/1stgendocs/running/direct/
title: Call Cloud Run functions directly \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:34.157269+00:00
---

# Call Cloud Run functions directly  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/running/direct/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Call Cloud Run functions directly

To support quick iteration and debugging, Cloud Run functions provides a `call` command in the command-line interface and testing functionality in the Google Cloud console UI. This allows you to directly invoke a function to ensure it is behaving as expected. This causes the function to execute immediately, even though it may have been deployed to respond to a specific event.

**Note:** Direct function invocations use the [call method](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions/call). This method has a limited [quota](https://docs.cloud.google.com/functions/quotas) that cannot be increased. It is intended for testing and shouldn't be used in production.

## Test your function with Google Cloud CLI

To directly invoke a function using the gcloud CLI, use the `gcloud functions call` command and supply any data your function expects as JSON in the `--data` argument. For example:
    
    
    gcloud functions call YOUR_FUNCTION_NAME --data '{"name":"Tristan"}'

where `YOUR_FUNCTION_NAME` is the name of the function you want to execute. The `--data` argument is sent to your function as follows:

  * **For HTTP functions,** the data you supply is sent as the body of a POST request.
  * **For background functions,** the data is passed directly as the event data to your function.
  * **For CloudEvent functions,** the data is passed directly as the event data to your function.



For more information, see the [`gcloud functions call`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/call) documentation.

## Test your function with the Google Cloud Console

To directly invoke a function from the Google Cloud console, follow these steps:

  1. [Go to the Cloud Run functions Overview page](https://console.cloud.google.com/functions/list).

  2. Click the name of the function you want to invoke.

  3. Click the **Testing** tab.

  4. In the **Configure Triggering Event** field, enter any data your function expects as JSON.

  5. Click **Test the function**.




Your function's response appears in the **Output** field, and logs for the individual execution appear in the **Logs** field.

## Cloud Pub/Sub event-driven function example

This example shows how to directly invoke an event-driven function triggered by Cloud Pub/Sub events:

###  Node.js 
    
    
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

###  Python 
    
    
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
    
    

###  Go 
    
    
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
    

###  Java 
    
    
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

###  C# 
    
    
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

###  Ruby 
    
    
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

###  PHP 
    
    
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

To invoke the function directly, send a [`PubsubMessage`](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/PubsubMessage), which expects base64-encoded data, as the event data:

###  Node.js 
    
    
    DATA=$(printf 'Hello!'|base64) && gcloud functions call helloPubSub --data '{"data":"'$DATA'"}'

###  Python 
    
    
    DATA=$(printf 'Hello!'|base64) && gcloud functions call hello_pubsub --data '{"data":"'$DATA'"}'

###  Go 
    
    
    DATA=$(printf 'Hello!'|base64) && gcloud functions call HelloPubSub --data '{"data":"'$DATA'"}'

###  Java 
    
    
    DATA=$(printf 'Hello!'|base64) && gcloud functions call java-hello-pubsub --data '{"data":"'$DATA'"}'

###  C# 
    
    
    DATA=$(printf 'Hello!'|base64) && gcloud functions call csharp-hello-pubsub --data '{"data":"'$DATA'"}'

###  Ruby 
    
    
    DATA=$(printf 'Hello!'|base64) && gcloud functions call hello_pubsub --data '{"data":"'$DATA'"}'

###  PHP 
    
    
    DATA=$(printf 'Hello!'|base64) && gcloud functions call helloworldPubsub --data '{"data":"'$DATA'"}'

This CLI example uses `bash` or `sh` syntax. It works in Linux and Mac environments but not Windows.

You can also invoke the function from the Google Cloud console by using the same event data in the **Triggering event** field.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
