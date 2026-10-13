---
url: https://docs.cloud.google.com/pubsub/docs/schemas-valid/
title: Parse messages from a topic with a schema \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:49:16.662108+00:00
---

# Parse messages from a topic with a schema  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/schemas-valid/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Parse messages from a topic with a schema Stay organized with collections  Save and categorize content based on your preferences. 

Topics may use schemas to define a format that their messages must follow. When subscribing to a topic with a schema, the messages sent to the subscriber are guaranteed to be valid messages. These messages conform to the type and encoding specified in the schema settings associated with the topic.

The subscriber can determine the schema settings associated with a topic by looking at the following attributes:

  * `googclient_schemaname`: The name of the schema used for validation. If the schema is deleted, the name is `_deleted-schema_`.

  * `googclient_schemaencoding`: The encoding of the message, either JSON or BINARY.

  * `googclient_schemarevisionid`: The revision ID of the schema used to parse and validate the message. Each revision has a unique revision ID associated with it. The revision ID is an auto-generated eight-character UUID. If the revision is deleted, the ID is `_deleted-schema-revision_`.




To learn more about schemas, see [Schema overview](https://docs.cloud.google.com/pubsub/docs/schemas).

## Code samples for subscribing to topics associated with a schema

These samples show how to process messages when subscribing to [topics configured with schema](https://docs.cloud.google.com/pubsub/docs/associate-schema-topic).

### C++

Before trying this sample, follow the C++ setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 

**Avro**
    
    
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

**Proto**
    
    
    namespace pubsub = ::google::cloud::pubsub;
    using ::google::cloud::future;
    using ::google::cloud::StatusOr;
    return [](pubsub::Subscriber subscriber) {
      auto session = subscriber.Subscribe(
          [](pubsub::Message const& m, pubsub::AckHandler h) {
            google::cloud::pubsub::samples::State state;
            (void)state.ParseFromString(std::string{m.data()});
            std::cout << "Message contents: " << state.DebugString() << "\n";
            std::move(h).ack();
          });
      return session;
    }

### C#

Before trying this sample, follow the C# setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 

**Avro**
    
    
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

**Proto**
    
    
    using [Google.Api.Gax](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html);
    using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
    using System;
    using System.Threading;
    using System.Threading.Tasks;
    
    public class PullProtoMessagesAsyncSample
    {
        public async Task<int> PullProtoMessagesAsync(string projectId, string subscriptionId, bool acknowledge)
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
                Utilities.State state = null;
                switch (encoding)
                {
                    case "BINARY":
                        state = Utilities.State.Parser.ParseFrom(message.Data.ToByteArray());
                        break;
                    case "JSON":
                        state = Utilities.State.Parser.ParseJson(message.Data.ToStringUtf8());
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

The following sample uses the major version of the Go Pub/Sub client library (v2). If you are still using the v1 library, see [the migration guide to v2](https://github.com/googleapis/google-cloud-go/blob/main/pubsub/MIGRATING.md). To see a list of v1 code samples, see [ the deprecated code samples](https://docs.cloud.google.com/pubsub/docs/samples?language=golang&text=deprecated).

Before trying this sample, follow the Go setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/pubsub/v2).

**Avro**
    
    
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
    

**Proto**
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"sync"
    	"time"
    
    	"cloud.google.com/go/pubsub/v2"
    	statepb "github.com/GoogleCloudPlatform/golang-samples/internal/pubsub/schemas"
    	"google.golang.org/protobuf/encoding/protojson"
    	"google.golang.org/protobuf/proto"
    )
    
    func subscribeWithProtoSchema(w io.Writer, projectID, subID string) error {
    	// projectID := "my-project-id"
    	// subID := "my-sub"
    	ctx := context.Background()
    	client, err := pubsub.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    
    	// Create an instance of the message to be decoded (a single U.S. state).
    	state := &statepb.State{}
    
    	sub := client.Subscriber(subID)
    	ctx2, cancel := context.WithTimeout(ctx, 10*time.Second)
    	defer cancel()
    
    	var mu sync.Mutex
    	sub.Receive(ctx2, func(ctx context.Context, msg *pubsub.Message) {
    		mu.Lock()
    		defer mu.Unlock()
    		encoding := msg.Attributes["googclient_schemaencoding"]
    
    		if encoding == "BINARY" {
    			if err := proto.Unmarshal(msg.Data, state); err != nil {
    				fmt.Fprintf(w, "proto.Unmarshal err: %v\n", err)
    				msg.Nack()
    				return
    			}
    			fmt.Printf("Received a binary-encoded message:\n%#v\n", state)
    		} else if encoding == "JSON" {
    			if err := protojson.Unmarshal(msg.Data, state); err != nil {
    				fmt.Fprintf(w, "proto.Unmarshal err: %v\n", err)
    				msg.Nack()
    				return
    			}
    			fmt.Fprintf(w, "Received a JSON-encoded message:\n%#v\n", state)
    		} else {
    			fmt.Fprintf(w, "Unknown message type(%s), nacking\n", encoding)
    			msg.Nack()
    			return
    		}
    		fmt.Fprintf(w, "%s is abbreviated as %s\n", state.Name, state.PostAbbr)
    		msg.Ack()
    	})
    	return nil
    }
    

### Java

The following sample uses the major version of the Go Pub/Sub client library (v2). If you are still using the v1 library, see [the migration guide to v2](https://github.com/googleapis/google-cloud-go/blob/main/pubsub/MIGRATING.md). To see a list of v1 code samples, see [ the deprecated code samples](https://docs.cloud.google.com/pubsub/docs/samples?language=golang&text=deprecated).

Before trying this sample, follow the Go setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/pubsub/v2).

**Avro**
    
    
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

**Protocol Buffer**
    
    
    import com.google.cloud.pubsub.v1.[AckReplyConsumer](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html);
    import com.google.cloud.pubsub.v1.[MessageReceiver](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.MessageReceiver.html);
    import com.google.cloud.pubsub.v1.[Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import com.google.protobuf.[InvalidProtocolBufferException](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html);
    import com.google.protobuf.util.[JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html);
    import com.google.pubsub.v1.[ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html);
    import com.google.pubsub.v1.[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html);
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    import utilities.StateProto.State;
    
    public class SubscribeWithProtoSchemaExample {
    
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        // Use an existing subscription.
        String subscriptionId = "your-subscription-id";
    
        subscribeWithProtoSchemaExample(projectId, subscriptionId);
      }
    
      public static void subscribeWithProtoSchemaExample(String projectId, String subscriptionId) {
    
        [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html) subscriptionName =
            [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html).of(projectId, subscriptionId);
    
        [MessageReceiver](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.MessageReceiver.html) receiver =
            (PubsubMessage message, AckReplyConsumer consumer) -> {
              ByteString data = message.getData();
    
              // Get the schema encoding type.
              String encoding = message.getAttributesMap().get("googclient_schemaencoding");
    
              block:
              try {
                switch (encoding) {
                  case "BINARY":
                    // Obtain an object of the generated proto class.
                    State state = State.parseFrom(data);
                    System.out.println("Received a BINARY-formatted message: " + state);
                    break;
    
                  case "JSON":
                    State.Builder stateBuilder = State.newBuilder();
                    [JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html).parser().merge(data.toStringUtf8(), stateBuilder);
                    System.out.println("Received a JSON-formatted message:" + stateBuilder.build());
                    break;
    
                  default:
                    break block;
                }
              } catch ([InvalidProtocolBufferException](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html) e) {
                e.printStackTrace();
              }
    
              consumer.ack();
              System.out.println("Ack'ed the message");
            };
    
        // Create subscriber client.
        [Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html) subscriber = [Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html).newBuilder(subscriptionName, receiver).build();
    
        try {
          subscriber.[startAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html#com_google_cloud_pubsub_v1_Subscriber_startAsync__)().awaitRunning();
          System.out.printf("Listening for messages on %s:\n", subscriptionName);
          subscriber.awaitTerminated(30, TimeUnit.SECONDS);
        } catch (TimeoutException timeoutException) {
          subscriber.stopAsync();
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 

**Avro**
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const subscriptionNameOrId = 'YOUR_SUBSCRIPTION_NAME_OR_ID';
    // const timeout = 60;
    
    // Imports the Google Cloud client library
    const {PubSub, Schema, Encodings} = require('[@google-cloud/pubsub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html)');
    
    // Node FS library, to load definitions
    const fs = require('fs');
    
    // And the Apache Avro library
    const avro = require('avro-js');
    
    // Creates a client; cache this for further use
    const pubSubClient = new [PubSub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)();
    
    function listenForAvroRecords(subscriptionNameOrId, timeout) {
      // References an existing subscription
      const subscription = pubSubClient.subscription(subscriptionNameOrId);
    
      // Make an encoder using the official avro-js library.
      const definition = fs
        .readFileSync('system-test/fixtures/provinces.avsc')
        .toString();
      const type = avro.parse(definition);
    
      // Create an event handler to handle messages
      let messageCount = 0;
      const messageHandler = async message => {
        // "Ack" ([ack](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/message.html)nowledge receipt of) the message
        message.[ack](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/message.html)();
    
        // Get the schema metadata from the message.
        const schemaMetadata = [Schema](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/schema.html).[metadataFromMessage](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/schema.html)(message.attributes);
    
        let result;
        switch (schemaMetadata.encoding) {
          case [Encodings](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html).Binary:
            result = type.fromBuffer(message.data);
            break;
          case [Encodings](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html).Json:
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
      subscripti[on](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/subscription-interface.html).[on](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/subscription-interface.html)('message', messageHandler);
    
      setTimeout(() => {
        subscription.removeListener('message', messageHandler);
        console.log(`${messageCount} message(s) received.`);
      }, timeout * 1000);
    }

**Protocol Buffer**
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const subscriptionNameOrId = 'YOUR_SUBSCRIPTION_NAME_OR_ID';
    // const timeout = 60;
    
    // Imports the Google Cloud client library
    const {PubSub, Schema, Encodings} = require('[@google-cloud/pubsub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html)');
    
    // And the protobufjs library
    const protobuf = require('protobufjs');
    
    // Creates a client; cache this for further use
    const pubSubClient = new [PubSub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)();
    
    async function listenForProtobufMessages(subscriptionNameOrId, timeout) {
      // References an existing subscription
      const subscription = pubSubClient.subscription(subscriptionNameOrId);
    
      // Make an decoder using the protobufjs library.
      //
      // Since we're providing the test message for a specific schema here, we'll
      // also code in the path to a sample proto definition.
      const root = protobuf.loadSync('system-test/fixtures/provinces.proto');
      const Province = root.lookupType('utilities.Province');
    
      // Create an event handler to handle messages
      let messageCount = 0;
      const messageHandler = async message => {
        // "Ack" ([ack](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/message.html)nowledge receipt of) the message
        message.[ack](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/message.html)();
    
        // Get the schema metadata from the message.
        const schemaMetadata = [Schema](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/schema.html).[metadataFromMessage](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/schema.html)(message.attributes);
    
        let result;
        switch (schemaMetadata.encoding) {
          case [Encodings](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html).Binary:
            result = Province.decode(message.data);
            break;
          case [Encodings](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html).Json:
            // This doesn't require decoding with the protobuf library,
            // since it's plain JSON. But you can still validate it against
            // your schema.
            result = JSON.parse(message.data.toString());
            console.log(`Validation of JSON: ${Province.verify(result)}`);
            break;
          default:
            console.log(`Unknown schema encoding: ${schemaMetadata.encoding}`);
            break;
        }
    
        console.log(`Received message ${message.id}:`);
        console.log(`\tData: ${JSON.stringify(result, null, 4)}`);
        console.log(`\tAttributes: ${JSON.stringify(message.attributes, null, 4)}`);
        messageCount += 1;
      };
    
      // Listen for new messages until timeout is hit
      subscripti[on](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/subscription-interface.html).[on](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/subscription-interface.html)('message', messageHandler);
    
      setTimeout(() => {
        subscription.removeListener('message', messageHandler);
        console.log(`${messageCount} message(s) received.`);
      }, timeout * 1000);
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 

**Avro**
    
    
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
    }

**Protocol Buffer**
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const subscriptionNameOrId = 'YOUR_SUBSCRIPTION_NAME_OR_ID';
    // const timeout = 60;
    
    // Imports the Google Cloud client library
    import {PubSub, Schema, Encodings, Message} from '@google-cloud/pubsub';
    
    // And the protobufjs library
    import * as protobuf from 'protobufjs';
    
    // Creates a client; cache this for further use
    const pubSubClient = new PubSub();
    
    async function listenForProtobufMessages(
      subscriptionNameOrId: string,
      timeout: number,
    ) {
      // References an existing subscription
      const subscription = pubSubClient.subscription(subscriptionNameOrId);
    
      // Make an decoder using the protobufjs library.
      //
      // Since we're providing the test message for a specific schema here, we'll
      // also code in the path to a sample proto definition.
      const root = protobuf.loadSync('system-test/fixtures/provinces.proto');
      const Province = root.lookupType('utilities.Province');
    
      // Create an event handler to handle messages
      let messageCount = 0;
      const messageHandler = async (message: Message) => {
        // "Ack" (acknowledge receipt of) the message
        message.ack();
    
        // Get the schema metadata from the message.
        const schemaMetadata = Schema.metadataFromMessage(message.attributes);
    
        let result;
        switch (schemaMetadata.encoding) {
          case Encodings.Binary:
            result = Province.decode(message.data);
            break;
          case Encodings.Json:
            // This doesn't require decoding with the protobuf library,
            // since it's plain JSON. But you can still validate it against
            // your schema.
            result = JSON.parse(message.data.toString());
            console.log(`Validation of JSON: ${Province.verify(result)}`);
            break;
          default:
            console.log(`Unknown schema encoding: ${schemaMetadata.encoding}`);
            break;
        }
    
        console.log(`Received message ${message.id}:`);
        console.log(`\tData: ${JSON.stringify(result, null, 4)}`);
        console.log(`\tAttributes: ${JSON.stringify(message.attributes, null, 4)}`);
        messageCount += 1;
      };
    
      // Listen for new messages until timeout is hit
      subscription.on('message', messageHandler);
    
      setTimeout(() => {
        subscription.removeListener('message', messageHandler);
        console.log(`${messageCount} message(s) received.`);
      }, timeout * 1000);
    }

### PHP

Before trying this sample, follow the PHP setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub PHP API reference documentation](https://cloud.google.com/php/docs/reference/cloud-pubsub/latest). 

**Avro**
    
    
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

**Protocol Buffer**
    
    
    use Google\Cloud\PubSub\PubSubClient;
    
    /**
     * Subscribe and pull messages using a protocol buffer schema.
     *
     * Relies on a proto message of the following form:
     * ```
     * syntax = "proto3";
     *
     * package utilities;
     *
     * message StateProto {
     *   string name = 1;
     *   string post_abbr = 2;
     * }
     * ```
     *
     * @param string $projectId
     * @param string $subscriptionId
     */
    function subscribe_proto_messages($projectId, $subscriptionId)
    {
        $pubsub = new PubSubClient([
            'projectId' => $projectId,
        ]);
    
        $subscription = $pubsub->subscription($subscriptionId);
        $messages = $subscription->pull();
    
        foreach ($messages as $message) {
            $decodedMessageData = '';
            $encoding = $message->attribute('googclient_schemaencoding');
            switch ($encoding) {
                case 'BINARY':
                    $protobufMessage = new \Utilities\StateProto();
                    $protobufMessage->mergeFromString($message->data());
    
                    $decodedMessageData = $protobufMessage->serializeToJsonString();
                    break;
                case 'JSON':
                    $decodedMessageData = $message->data();
                    break;
            }
    
            printf('Received a %d-encoded message %s', $encoding, $decodedMessageData);
        }
    }

### Python

Before trying this sample, follow the Python setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/pubsub/latest). 

**Avro**
    
    
    import avro.schema as schema
    from avro.io import BinaryDecoder, DatumReader
    from concurrent.futures import TimeoutError
    import io
    import json
    from google.cloud.pubsub import [SubscriberClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)
    
    # TODO(developer)
    # project_id = "your-project-id"
    # subscription_id = "your-subscription-id"
    # avsc_file = "path/to/an/avro/schema/file/(.avsc)/formatted/in/json"
    # Number of seconds the subscriber listens for messages
    # timeout = 5.0
    
    subscriber = SubscriberClient()
    subscription_path = subscriber.subscription_path(project_id, subscription_id)
    
    with open(avsc_file, "rb") as file:
        avro_schema = schema.parse(file.read())
    
    def callback(message: pubsub_v1.subscriber.message.[Message](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html)) -> None:
        # Get the message serialization type.
        encoding = message.[attributes](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_attributes).get("googclient_schemaencoding")
        # Deserialize the message data accordingly.
        if encoding == "BINARY":
            bout = io.BytesIO(message.[data](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_data))
            decoder = BinaryDecoder(bout)
            reader = DatumReader(avro_schema)
            message_data = reader.read(decoder)
            print(f"Received a binary-encoded message:\n{message_data}")
        elif encoding == "JSON":
            message_data = json.loads(message.[data](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_data))
            print(f"Received a JSON-encoded message:\n{message_data}")
        else:
            print(f"Received a message with no encoding:\n{message}")
    
        message.[ack](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_ack)()
    
    streaming_pull_future = [subscribe](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)r.[subscribe](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)(subscription_path, callback=callback)
    print(f"Listening for messages on {subscription_path}..\n")
    
    # Wrap subscriber in a 'with' block to automatically call close() when done.
    with subscriber:
        try:
            # When `timeout` is not set, result() will block indefinitely,
            # unless an exception occurs first.
            streaming_pull_future.result(timeout=timeout)
        except TimeoutError:
            streaming_pull_future.cancel()  # Trigger the shutdown.
            streaming_pull_future.result()  # Block until the shutdown is complete.

**Protocol Buffer**
    
    
    from concurrent.futures import TimeoutError
    from google.cloud.pubsub import [SubscriberClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)
    from google.protobuf.json_format import Parse
    
    from utilities import us_states_pb2
    
    # TODO(developer)
    # project_id = "your-project-id"
    # subscription_id = "your-subscription-id"
    # Number of seconds the subscriber listens for messages
    # timeout = 5.0
    
    subscriber = SubscriberClient()
    subscription_path = subscriber.subscription_path(project_id, subscription_id)
    
    # Instantiate a protoc-generated class defined in `us-states.proto`.
    state = us_states_pb2.StateProto()
    
    def callback(message: pubsub_v1.subscriber.message.[Message](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html)) -> None:
        # Get the message serialization type.
        encoding = message.[attributes](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_attributes).get("googclient_schemaencoding")
        # Deserialize the message data accordingly.
        if encoding == "BINARY":
            state.ParseFromString(message.[data](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_data))
            print(f"Received a binary-encoded message:\n{state}")
        elif encoding == "JSON":
            Parse(message.[data](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_data), state)
            print(f"Received a JSON-encoded message:\n{state}")
        else:
            print(f"Received a message with no encoding:\n{message}")
    
        message.[ack](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_ack)()
    
    streaming_pull_future = [subscribe](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)r.[subscribe](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)(subscription_path, callback=callback)
    print(f"Listening for messages on {subscription_path}..\n")
    
    # Wrap subscriber in a 'with' block to automatically call close() when done.
    with subscriber:
        try:
            # When `timeout` is not set, result() will block indefinitely,
            # unless an exception occurs first.
            streaming_pull_future.result(timeout=timeout)
        except TimeoutError:
            streaming_pull_future.cancel()  # Trigger the shutdown.
            streaming_pull_future.result()  # Block until the shutdown is complete.

### Ruby

The following sample uses Ruby Pub/Sub client library v3. If you are still using the v2 library, see [ the migration guide to v3](https://github.com/googleapis/google-cloud-ruby/blob/main/google-cloud-pubsub/MIGRATION_GUIDE.md). To see a list of Ruby v2 code samples, see [ the deprecated code samples](https://docs.cloud.google.com/pubsub/docs/samples?language=ruby&text=deprecated).

Before trying this sample, follow the Ruby setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 

**Avro**
    
    
    # subscription_id = "your-subscription-id"
    # avsc_file = "path/to/an/avro/schema/file/(.avsc)/formatted/in/json"
    
    pubsub = Google::Cloud::[PubSub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html)
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

**Protocol Buffer**
    
    
    # subscription_id = "your-subscription-id"
    
    pubsub = Google::Cloud::[PubSub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html)
    subscriber = pubsub.[subscriber](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html) subscription_id
    
    listener = subscriber.[listen](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Subscriber.html) do |received_message|
      encoding = received_message.attributes["googclient_schemaencoding"]
      case encoding
      when "BINARY"
        state = Utilities::StateProto.decode received_message.data
        puts "Received a binary-encoded message:\n#{state}"
      when "JSON"
        require "json"
        state = Utilities::StateProto.decode_json received_message.data
        puts "Received a JSON-encoded message:\n#{state}"
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

## Subscribe to a topic associated with an Avro schema with revisions

Avro requires messages to be parsed using the schema with which they are encoded. You can also translate messages to a different schema by using [Avro schema resolution](https://avro.apache.org/docs/current/specification/#schema-resolution).

Pub/Sub ensures that all schema revisions are forward and backward compatible with all other revisions. This compatibility lets any revision be used as the reader or writer schema.

When parsing a message encoded with a different schema revision than the one your subscriber uses, you might need to get the original schema and pass it in as the writer schema.

It's best to cache the Avro reader object that can parse messages for each schema revision encountered in order to minimize latency and minimize the number of calls to the `GetSchema` API.

The following code shows these functions:

  * Read the attributes discussed in the previous section to determine which schema revision is used to encode the message.

  * Fetch the schema revision and cache a reader generated with it.

  * Parse the message into the schema that your subscriber uses.




### Go

The following sample uses the major version of the Go Pub/Sub client library (v2). If you are still using the v1 library, see [the migration guide to v2](https://github.com/googleapis/google-cloud-go/blob/main/pubsub/MIGRATING.md). To see a list of v1 code samples, see [ the deprecated code samples](https://docs.cloud.google.com/pubsub/docs/samples?language=golang&text=deprecated).

Before trying this sample, follow the Go setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/pubsub/v2).
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"sync"
    	"time"
    
    	"cloud.google.com/go/pubsub/v2"
    	schema "cloud.google.com/go/pubsub/v2/apiv1"
    	"cloud.google.com/go/pubsub/v2/apiv1/pubsubpb"
    	"github.com/linkedin/goavro/v2"
    )
    
    func subscribeWithAvroSchemaRevisions(w io.Writer, projectID, subID string) error {
    	// projectID := "my-project-id"
    	// topicID := "my-topic"
    	ctx := context.Background()
    	client, err := pubsub.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    
    	schemaClient, err := schema.NewSchemaClient(ctx)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewSchemaClient: %w", err)
    	}
    
    	// Create the cache for the codecs for different revision IDs.
    	revisionCodecs := make(map[string]*goavro.Codec)
    
    	sub := client.Subscriber(subID)
    	ctx2, cancel := context.WithTimeout(ctx, 10*time.Second)
    	defer cancel()
    
    	var mu sync.Mutex
    	sub.Receive(ctx2, func(ctx context.Context, msg *pubsub.Message) {
    		mu.Lock()
    		defer mu.Unlock()
    		name := msg.Attributes["googclient_schemaname"]
    		revision := msg.Attributes["googclient_schemarevisionid"]
    
    		codec, ok := revisionCodecs[revision]
    		// If the codec doesn't exist in the map, this is the first time we
    		// are seeing this revision. We need to fetch the schema and cache the
    		// codec. It would be more typical to do this asynchronously, but is
    		// shown here in a synchronous way to ease readability.
    		if !ok {
    			s := &pubsubpb.GetSchemaRequest{
    				Name: fmt.Sprintf("%s@%s", name, revision),
    				View: pubsubpb.SchemaView_FULL,
    			}
    			schema, err := schemaClient.GetSchema(ctx, s)
    			if err != nil {
    				fmt.Fprintf(w, "Nacking, cannot read message without schema: %v\n", err)
    				msg.Nack()
    				return
    			}
    			codec, err = goavro.NewCodec(schema.Definition)
    			if err != nil {
    				msg.Nack()
    				fmt.Fprintf(w, "goavro.NewCodec err: %v\n", err)
    			}
    			revisionCodecs[revision] = codec
    		}
    
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

Before trying this sample, follow the Java setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 
    
    
    import com.google.cloud.pubsub.v1.[AckReplyConsumer](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html);
    import com.google.cloud.pubsub.v1.[MessageReceiver](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.MessageReceiver.html);
    import com.google.cloud.pubsub.v1.[SchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SchemaServiceClient.html);
    import com.google.cloud.pubsub.v1.[Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import com.google.pubsub.v1.[ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html);
    import com.google.pubsub.v1.[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html);
    import com.google.pubsub.v1.[Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.html);
    import java.io.ByteArrayInputStream;
    import java.io.IOException;
    import java.io.InputStream;
    import java.util.HashMap;
    import java.util.Map;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    import org.apache.avro.io.Decoder;
    import org.apache.avro.io.DecoderFactory;
    import org.apache.avro.specific.SpecificDatumReader;
    import utilities.State;
    
    public class SubscribeWithAvroSchemaRevisionsExample {
    
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        // Use an existing subscription.
        String subscriptionId = "your-subscription-id";
    
        subscribeWithAvroSchemaRevisionsExample(projectId, subscriptionId);
      }
    
      static [SchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SchemaServiceClient.html) getSchemaServiceClient() {
        try {
          return [SchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SchemaServiceClient.html).create();
        } catch (IOException e) {
          System.out.println("Could not get schema client: " + e);
          return null;
        }
      }
    
      public static void subscribeWithAvroSchemaRevisionsExample(
          String projectId, String subscriptionId) {
        // Used to get the schemas for revsions.
        final [SchemaServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SchemaServiceClient.html) schemaServiceClient = getSchemaServiceClient();
        if (schemaServiceClient == null) {
          return;
        }
    
        // Cache for the readers for different revision IDs.
        Map<String, SpecificDatumReader<State>> revisionReaders =
            new HashMap<String, SpecificDatumReader<State>>();
    
        [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html) subscriptionName =
            [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html).of(projectId, subscriptionId);
    
        // Instantiate an asynchronous message receiver.
        [MessageReceiver](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.MessageReceiver.html) receiver =
            (PubsubMessage message, AckReplyConsumer consumer) -> {
              // Get the schema encoding type.
              String name = message.getAttributesMap().get("googclient_schemaname");
              String revision = message.getAttributesMap().get("googclient_schemarevisionid");
    
              SpecificDatumReader<State> reader = null;
              synchronized (revisionReaders) {
                reader = revisionReaders.get(revision);
              }
              if (reader == null) {
                // This is the first time we are seeing this revision. We need to
                // fetch the schema and cache its decoder. It would be more typical
                // to do this asynchronously, but is shown here in a synchronous
                // way to ease readability.
                try {
                  [Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.html) schema = schemaServiceClient.[getSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SchemaServiceClient.html#com_google_cloud_pubsub_v1_SchemaServiceClient_getSchema__org_jspecify_annotations_Nullable_com_google_pubsub_v1_SchemaName_)(name + "@" + revision);
                  org.apache.avro.[Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.html) avroSchema =
                      new org.apache.avro.[Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.html).[Parser](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Parser.html)().parse(schema.[getDefinition](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Schema.html#com_google_pubsub_v1_Schema_getDefinition__)());
                  reader = new SpecificDatumReader<State>(avroSchema, State.getClassSchema());
                  synchronized (revisionReaders) {
                    revisionReaders.put(revision, reader);
                  }
                } catch (Exception e) {
                  System.out.println("Could not get schema: " + e);
                  // Without the schema, we cannot read the message, so nack it.
                  consumer.nack();
                  return;
                }
              }
    
              [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) data = message.getData();
              // Send the message data to a byte[] input stream.
              InputStream inputStream = new ByteArrayInputStream(data.[toByteArray](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_toByteArray__)());
    
              String encoding = message.getAttributesMap().get("googclient_schemaencoding");
    
              Decoder decoder = null;
    
              // Prepare an appropriate decoder for the message data in the input stream
              // based on the schema encoding type.
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
                    System.out.println("Unknown message type; nacking.");
                    consumer.nack();
                    break;
                }
    
                // Obtain an object of the generated Avro class using the decoder.
                State state = reader.read(null, decoder);
                System.out.println(state.getName() + " is abbreviated as " + state.getPostAbbr());
    
                // Ack the message.
                consumer.ack();
              } catch (IOException e) {
                System.err.println(e);
                // If we failed to process the message, nack it.
                consumer.nack();
              }
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

### Python

Before trying this sample, follow the Python setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/pubsub/latest). 
    
    
    import avro.schema as schema
    from avro.io import BinaryDecoder, DatumReader
    from concurrent.futures import TimeoutError
    import io
    import json
    from google.api_core.exceptions import NotFound
    from google.cloud.pubsub import SchemaServiceClient, [SubscriberClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)
    
    schema_client = SchemaServiceClient()
    
    # TODO(developer)
    # project_id = "your-project-id"
    # subscription_id = "your-subscription-id"
    # avsc_file = "path/to/an/avro/schema/file/(.avsc)/formatted/in/json"
    # Number of seconds the subscriber listens for messages
    # timeout = 5.0
    
    subscriber = SubscriberClient()
    subscription_path = subscriber.subscription_path(project_id, subscription_id)
    
    with open(avsc_file, "rb") as file:
        reader_avro_schema = schema.parse(file.read())
    # Dict to keep readers for different schema revisions.
    revisions_to_readers = {}
    
    def callback(message: pubsub_v1.subscriber.message.[Message](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html)) -> None:
        # Get the message serialization type.
        schema_name = message.[attributes](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_attributes).get("googclient_schemaname")
        schema_revision_id = message.[attributes](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_attributes).get("googclient_schemarevisionid")
        encoding = message.[attributes](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_attributes).get("googclient_schemaencoding")
    
        if schema_revision_id not in revisions_to_readers:
            schema_path = schema_name + "@" + schema_revision_id
            try:
                received_avro_schema = schema_client.get_schema(
                    request={"name": schema_path}
                )
            except NotFound:
                print(f"{[schema_path](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.publisher.client.Client.html#google_cloud_pubsub_v1_publisher_client_Client_schema_path)} not found.")
                message.[nack](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_nack)()
                return
            writer_avro_schema = schema.parse(received_avro_schema.definition)
            revisions_to_readers[schema_revision_id] = DatumReader(
                writer_avro_schema, reader_avro_schema
            )
        reader = revisions_to_readers[schema_revision_id]
    
        # Deserialize the message data accordingly.
        if encoding == "BINARY":
            bout = io.BytesIO(message.[data](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_data))
            decoder = BinaryDecoder(bout)
            message_data = reader.read(decoder)
            print(f"Received a binary-encoded message:\n{message_data}")
        elif encoding == "JSON":
            message_data = json.loads(message.[data](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_data))
            print(f"Received a JSON-encoded message:\n{message_data}")
        else:
            print(f"Received a message with no encoding:\n{message}")
            message.[nack](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_nack)()
    
        message.[ack](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_ack)()
    
    streaming_pull_future = [subscribe](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)r.[subscribe](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)(subscription_path, callback=callback)
    print(f"Listening for messages on {subscription_path}..\n")
    
    # Wrap subscriber in a 'with' block to automatically call close() when done.
    with subscriber:
        try:
            # When `timeout` is not set, result() will block indefinitely,
            # unless an exception occurs first.
            streaming_pull_future.result(timeout=timeout)
        except TimeoutError:
            streaming_pull_future.cancel()  # Trigger the shutdown.
            streaming_pull_future.result()  # Block until the shutdown is complete.

## Required roles

To get the permissions you need to validate a message against a schema, complete one of the following steps:

  * Grant one of the following predefined roles to a service account: `roles/pubsub.admin`, `roles/pubsub.editor`, or `roles/pubsub.viewer`.
  * Create a custom role for a service account and add the following permissions `pubsub.schemas.validate` and `pubsub.schemas.get`.

To learn more about custom roles, see [Create and manage Custom IAM roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
