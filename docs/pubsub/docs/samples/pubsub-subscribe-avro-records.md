---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-subscribe-avro-records/
title: Receive messages of Avro schema type \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:37.311128+00:00
---

# Receive messages of Avro schema type  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-subscribe-avro-records/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  Receive messages of Avro schema type Stay organized with collections  Save and categorize content based on your preferences. 

Receive a message of Avro schema type, convert the message data to an object of a generated Avro class, and acknowledge the message.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Parse messages from a topic with a schema](https://docs.cloud.google.com/pubsub/docs/schemas-valid)



## Code sample

### C++

Before trying this sample, follow the C++ setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace pubsub = ::google::cloud::pubsub;
    using ::google::cloud::future;
    using ::google::cloud::StatusOr;
    return [](pubsub::Subscriber subscriber) {
      auto session = subscriber.Subscribe(
          [](pubsub::Message const& m, pubsub::AckHandler h) {
            std::cout << "Message contents: " << m.data() << "\n";
            std::move(h).ack();
          });
      return session;
    }

### C#

Before trying this sample, follow the C# setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using Avro.IO;
    using Avro.Specific;
    using [Google.Api.Gax](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html);
    using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
    using Newtonsoft.Json;
    using System;
    using System.IO;
    using System.Threading;
    using System.Threading.Tasks;
    
    public class PullAvroMessagesAsyncSample
    {
        public async Task<int> PullAvroMessagesAsync(string projectId, string subscriptionId, bool acknowledge)
        {
            [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html) subscriptionName = [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html).[FromProjectSubscription](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html#Google_Cloud_PubSub_V1_SubscriptionName_FromProjectSubscription_System_String_System_String_)(projectId, subscriptionId);
            int messageCount = 0;
            [SubscriberClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.html) subscriber = await new [SubscriberClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClientBuilder.html)
            {
                SubscriptionName = subscriptionName,
                Settings = new SubscriberClient.Settings
                {
                    AckExtensionWindow = TimeSpan.FromSeconds(4),
                    AckDeadline = TimeSpan.FromSeconds(10),
                    FlowControlSettings = new [FlowControlSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.FlowControlSettings.html)(maxOutstandingElementCount: 100, maxOutstandingByteCount: 10240)
                }
            }.BuildAsync();
            // SubscriberClient runs your message handle function on multiple
            // threads to maximize throughput.
            Task startTask = subscriber.[StartAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.html#Google_Cloud_PubSub_V1_SubscriberClient_StartAsync_Google_Cloud_PubSub_V1_SubscriptionHandler_)(([PubsubMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PubsubMessage.html) message, [CancellationToken](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html#Google_Api_Gax_Grpc_CallSettings_CancellationToken) cancel) =>
            {
                string encoding = message.Attributes["googclient_schemaencoding"];
                // AvroUtilities is a namespace. Below are files using the namespace.
                // https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/main/pubsub/api/Pubsub.Samples/Utilities/State.cs
                // https://github.com/GoogleCloudPlatform/dotnet-docs-samples/blob/main/pubsub/api/Pubsub.Samples/Utilities/StateUtils.cs
                AvroUtilities.State state = new AvroUtilities.State();
                switch (encoding)
                {
                    case "BINARY":
                        using (var ms = new MemoryStream(message.Data.ToByteArray()))
                        {
                            var decoder = new BinaryDecoder(ms);
                            var reader = new SpecificDefaultReader(state.Schema, state.Schema);
                            reader.Read<AvroUtilities.State>(state, decoder);
                        }
                        break;
                    case "JSON":
                        state = JsonConvert.DeserializeObject<AvroUtilities.State>(message.[Data](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PubsubMessage.html#Google_Cloud_PubSub_V1_PubsubMessage_Data).ToStringUtf8());
                        break;
                    default:
                        Console.WriteLine($"Encoding not provided in message.");
                        break;
                }
                Console.WriteLine($"Message {message.MessageId}: {state}");
                Interlocked.Increment(ref messageCount);
                return Task.FromResult(acknowledge ? [SubscriberClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.html).[Reply](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.Reply.html).[Ack](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.Reply.html#Google_Cloud_PubSub_V1_SubscriberClient_Reply_Ack) : [SubscriberClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.html).[Reply](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.Reply.html).[Nack](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.Reply.html#Google_Cloud_PubSub_V1_SubscriberClient_Reply_Nack));
            });
            // Run for 5 seconds.
            await Task.Delay(5000);
            await subscriber.[StopAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.html#Google_Cloud_PubSub_V1_SubscriberClient_StopAsync_Google_Cloud_PubSub_V1_SubscriberClient_ShutdownOptions_System_Threading_CancellationToken_)([CancellationToken](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html#Google_Api_Gax_Grpc_CallSettings_CancellationToken).None);
            // Lets make sure that the start task finished successfully after the call to stop.
            await startTask;
            return messageCount;
        }
    }

### Go

Before trying this sample, follow the Go setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://godoc.org/cloud.google.com/go/pubsub). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"os"
    	"sync"
    	"time"
    
    	"cloud.google.com/go/pubsub/v2"
    	"github.com/linkedin/goavro/v2"
    )
    
    func subscribeWithAvroSchema(w io.Writer, projectID, subID, avscFile string) error {
    	// projectID := "my-project-id"
    	// topicID := "my-topic"
    	// avscFile = "path/to/an/avro/schema/file(.avsc)/formatted/in/json"
    	ctx := context.Background()
    	client, err := pubsub.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    
    	avroSchema, err := os.ReadFile(avscFile)
    	if err != nil {
    		return fmt.Errorf("os.ReadFile err: %w", err)
    	}
    	codec, err := goavro.NewCodec(string(avroSchema))
    	if err != nil {
    		return fmt.Errorf("goavro.NewCodec err: %w", err)
    	}
    
    	sub := client.Subscriber(subID)
    	ctx2, cancel := context.WithTimeout(ctx, 10*time.Second)
    	defer cancel()
    
    	var mu sync.Mutex
    	sub.Receive(ctx2, func(ctx context.Context, msg *pubsub.Message) {
    		mu.Lock()
    		defer mu.Unlock()
    		encoding := msg.Attributes["googclient_schemaencoding"]
    
    		var state map[string]interface{}
    		if encoding == "BINARY" {
    			data, _, err := codec.NativeFromBinary(msg.Data)
    			if err != nil {
    				fmt.Fprintf(w, "codec.NativeFromBinary err: %v\n", err)
    				msg.Nack()
    				return
    			}
    			fmt.Fprintf(w, "Received a binary-encoded message:\n%#v\n", data)
    			state = data.(map[string]interface{})
    		} else if encoding == "JSON" {
    			data, _, err := codec.NativeFromTextual(msg.Data)
    			if err != nil {
    				fmt.Fprintf(w, "codec.NativeFromTextual err: %v\n", err)
    				msg.Nack()
    				return
    			}
    			fmt.Fprintf(w, "Received a JSON-encoded message:\n%#v\n", data)
    			state = data.(map[string]interface{})
    		} else {
    			fmt.Fprintf(w, "Unknown message type(%s), nacking\n", encoding)
    			msg.Nack()
    			return
    		}
    		fmt.Fprintf(w, "%s is abbreviated as %s\n", state["name"], state["post_abbr"])
    		msg.Ack()
    	})
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.pubsub.v1.[AckReplyConsumer](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html);
    import com.google.cloud.pubsub.v1.[MessageReceiver](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.MessageReceiver.html);
    import com.google.cloud.pubsub.v1.[Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import com.google.pubsub.v1.[ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html);
    import com.google.pubsub.v1.[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html);
    import java.io.ByteArrayInputStream;
    import java.io.IOException;
    import java.io.InputStream;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    import org.apache.avro.io.Decoder;
    import org.apache.avro.io.DecoderFactory;
    import org.apache.avro.specific.SpecificDatumReader;
    import utilities.State;
    
    public class SubscribeWithAvroSchemaExample {
    
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        // Use an existing subscription.
        String subscriptionId = "your-subscription-id";
    
        subscribeWithAvroSchemaExample(projectId, subscriptionId);
      }
    
      public static void subscribeWithAvroSchemaExample(String projectId, String subscriptionId) {
    
        [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html) subscriptionName =
            [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html).of(projectId, subscriptionId);
    
        // Prepare a reader for the encoded Avro records.
        SpecificDatumReader<State> reader = new SpecificDatumReader<>(State.getClassSchema());
    
        // Instantiate an asynchronous message receiver.
        [MessageReceiver](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.MessageReceiver.html) receiver =
            (PubsubMessage message, AckReplyConsumer consumer) -> {
              ByteString data = message.getData();
    
              // Get the schema encoding type.
              String encoding = message.getAttributesMap().get("googclient_schemaencoding");
    
              // Send the message data to a byte[] input stream.
              InputStream inputStream = new ByteArrayInputStream(data.toByteArray());
    
              Decoder decoder = null;
    
              // Prepare an appropriate decoder for the message data in the input stream
              // based on the schema encoding type.
              block:
              try {
                switch (encoding) {
                  case "BINARY":
                    decoder = DecoderFactory.get().directBinaryDecoder(inputStream, /* reuse= */ null);
                    System.out.println("Receiving a binary-encoded message:");
                    break;
                  case "JSON":
                    decoder = DecoderFactory.get().jsonDecoder(State.getClassSchema(), inputStream);
                    System.out.println("Receiving a JSON-encoded message:");
                    break;
                  default:
                    break block;
                }
    
                // Obtain an object of the generated Avro class using the decoder.
                State state = reader.read(null, decoder);
                System.out.println(state.getName() + " is abbreviated as " + state.getPostAbbr());
    
              } catch (IOException e) {
                System.err.println(e);
              }
    
              // Ack the message.
              consumer.ack();
            };
    
        [Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html) subscriber = null;
        try {
          subscriber = [Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html).newBuilder(subscriptionName, receiver).build();
          subscriber.[startAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html#com_google_cloud_pubsub_v1_Subscriber_startAsync__)().awaitRunning();
          System.out.printf("Listening for messages on %s:\n", subscriptionName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html#com_google_pubsub_v1_ProjectSubscriptionName_toString__)());
          subscriber.awaitTerminated(30, TimeUnit.SECONDS);
        } catch (TimeoutException timeoutException) {
          subscriber.stopAsync();
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    ]
    

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const subscriptionNameOrId = 'YOUR_SUBSCRIPTION_NAME_OR_ID';
    // const timeout = 60;
    
    // Imports the Google Cloud client library
    import {PubSub, Schema, Encodings, Message} from '@google-cloud/pubsub';
    
    // Node FS library, to load definitions
    import * as fs from 'fs';
    
    // And the Apache Avro library
    import * as avro from 'avro-js';
    
    // Creates a client; cache this for further use
    const pubSubClient = new PubSub();
    
    function listenForAvroRecords(subscriptionNameOrId: string, timeout: number) {
      // References an existing subscription
      const subscription = pubSubClient.subscription(subscriptionNameOrId);
    
      // Make an encoder using the official avro-js library.
      const definition = fs
        .readFileSync('system-test/fixtures/provinces.avsc')
        .toString();
      const type = avro.parse(definition);
    
      // Create an event handler to handle messages
      let messageCount = 0;
      const messageHandler = async (message: Message) => {
        // "Ack" (acknowledge receipt of) the message
        message.ack();
    
        // Get the schema metadata from the message.
        const schemaMetadata = Schema.metadataFromMessage(message.attributes);
    
        let result: object | undefined;
        switch (schemaMetadata.encoding) {
          case Encodings.Binary:
            result = type.fromBuffer(message.data);
            break;
          case Encodings.Json:
            result = type.fromString(message.data.toString());
            break;
          default:
            console.log(`Unknown schema encoding: ${schemaMetadata.encoding}`);
            break;
        }
    
        console.log(`Received message ${message.id}:`);
        console.log(`\tData: ${JSON.stringify(result, null, 4)}`);
        console.log(`\tAttributes: ${message.attributes}`);
        messageCount += 1;
      };
    
      // Listen for new messages until timeout is hit
      subscription.on('message', messageHandler);
    
      setTimeout(() => {
        subscription.removeListener('message', messageHandler);
        console.log(`${messageCount} message(s) received.`);
      }, timeout * 1000);
    
      use?.optional?.chaining?.();
    }

### PHP

Before trying this sample, follow the PHP setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/latest/pubsub/pubsubclient). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\PubSub\PubSubClient;
    
    /**
     * Subscribe and pull messages using an AVRO schema.
     *
     * @param string $projectId
     * @param string $subscriptionId
     */
    function subscribe_avro_records($projectId, $subscriptionId, $definitionFile)
    {
        $pubsub = new PubSubClient([
            'projectId' => $projectId,
        ]);
    
        $subscription = $pubsub->subscription($subscriptionId);
        $definition = file_get_contents($definitionFile);
        $messages = $subscription->pull();
    
        foreach ($messages as $message) {
            $decodedMessageData = '';
            $encoding = $message->attribute('googclient_schemaencoding');
            switch ($encoding) {
                case 'BINARY':
                    $io = new \AvroStringIO($message->data());
                    $schema = \AvroSchema::parse($definition);
                    $reader = new \AvroIODatumReader($schema);
                    $decoder = new \AvroIOBinaryDecoder($io);
                    $decodedMessageData = json_encode($reader->read($decoder));
                    break;
                case 'JSON':
                    $decodedMessageData = $message->data();
                    break;
            }
    
            printf('Received a %d-encoded message %s', $encoding, $decodedMessageData);
        }
    }

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # subscription_id = "your-subscription-id"
    # avsc_file = "path/to/an/avro/schema/file/(.avsc)/formatted/in/json"
    
    pubsub = Google::Cloud::[PubSub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html)
    subscriber = pubsub.[subscriber](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html) subscription_id
    
    listener = subscriber.[listen](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Subscriber.html) do |received_message|
      encoding = received_message.attributes["googclient_schemaencoding"]
      case encoding
      when "BINARY"
        require "avro"
        avro_schema = Avro::Schema.parse File.read(avsc_file)
        buffer = StringIO.[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html) received_message.data
        decoder = Avro::IO::BinaryDecoder.[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html) buffer
        reader = Avro::IO::DatumReader.[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html) avro_schema
        message_data = reader.read decoder
        puts "Received a binary-encoded message:\n#{message_data}"
      when "JSON"
        require "json"
        message_data = JSON.parse received_message.data
        puts "Received a JSON-encoded message:\n#{message_data}"
      else
        "Received a message with no encoding:\n#{received_message.message_id}"
      end
      received_message.[acknowledge!](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-ReceivedMessage.html)
    end
    
    listener.[start](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-MessageListener.html)
    # Let the main thread sleep for 60 seconds so the thread for listening
    # messages does not quit
    sleep 60
    listener.stop.wait!

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
