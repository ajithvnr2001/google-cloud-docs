---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-subscribe-avro-records-with-revisions/
title: Receive messages that could be for different schema revisions \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:21:10.150248+00:00
---

# Receive messages that could be for different schema revisions  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-subscribe-avro-records-with-revisions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  Receive messages that could be for different schema revisions Stay organized with collections  Save and categorize content based on your preferences. 

Receive messages that could be for different schema revisions

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Parse messages from a topic with a schema](https://docs.cloud.google.com/pubsub/docs/schemas-valid)



## Code sample

### C++

Before trying this sample, follow the C++ setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    auto subscriber = pubsub::Subscriber(pubsub::MakeSubscriberConnection(
        pubsub::Subscription(project_id, subscription_id)));
    
    // Create a schema client.
    auto schema_client =
        pubsub::SchemaServiceClient(pubsub::MakeSchemaServiceConnection());
    
    // Read the reader schema. This is the schema you want the messages to be
    // evaluated using.
    std::ifstream ifs(avro_file);
    avro::ValidSchema reader_schema;
    avro::compileJsonSchema(ifs, reader_schema);
    
    std::unordered_map<std::string, avro::ValidSchema> revisions_to_schemas;
    auto session = subscriber.Subscribe(
        [&](pubsub::Message const& message, pubsub::AckHandler h) {
          // Get the reader schema revision for the message.
          auto schema_name = message.attributes()["googclient_schemaname"];
          auto schema_revision_id =
              message.attributes()["googclient_schemarevisionid"];
          // If we haven't received a message with this schema, look it up.
          if (revisions_to_schemas.find(schema_revision_id) ==
              revisions_to_schemas.end()) {
            auto schema_path = schema_name + "@" + schema_revision_id;
            // Use the schema client to get the path.
            auto schema = schema_client.GetSchema(schema_path);
            if (!schema) {
              std::cout << "Schema not found:" << schema_path << "\n";
              return;
            }
            avro::ValidSchema writer_schema;
            std::stringstream in;
            in << schema.value().definition();
            avro::compileJsonSchema(in, writer_schema);
            revisions_to_schemas[schema_revision_id] = writer_schema;
          }
          auto writer_schema = revisions_to_schemas[schema_revision_id];
    
          auto encoding = message.attributes()["googclient_schemaencoding"];
          if (encoding == "JSON") {
            std::stringstream in;
            in << message.data();
            auto avro_in = avro::istreamInputStream(in);
            avro::DecoderPtr decoder = avro::resolvingDecoder(
                writer_schema, reader_schema, avro::jsonDecoder(writer_schema));
            decoder->init(*avro_in);
    
            v2::State state;
            avro::decode(*decoder, state);
            std::cout << "Name: " << state.name << "\n";
            std::cout << "Postal Abbreviation: " << state.post_abbr << "\n";
            std::cout << "Population: " << state.population << "\n";
          } else {
            std::cout << "Unable to decode. Received message using encoding"
                      << encoding << "\n";
          }
          std::move(h).ack();
        });

### C#

Before trying this sample, follow the C# setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using Avro.Generic;
    using Avro.IO;
    using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
    using System;
    using System.Collections.Concurrent;
    using System.IO;
    using System.Threading;
    using System.Threading.Tasks;
    
    public class SubscribeAvroRecordsWithRevisionsSample
    {
        public async Task<(int, int)> SubscribeAvroRecordsWithRevisions(string projectId, string subscriptionId)
        {
            SchemaServiceClient schemaService = SchemaServiceClient.Create();
    
            var schemaCache = new ConcurrentDictionary<(string, string), Avro.Schema>();
    
            SubscriptionName subscriptionName = SubscriptionName.FromProjectSubscription(projectId, subscriptionId);
            SubscriberClient subscriber = await SubscriberClient.CreateAsync(subscriptionName);
            int messageCount = 0;
            Task startTask = subscriber.StartAsync((PubsubMessage message, CancellationToken cancel) =>
            {
                // Get the schema name, revision ID and encoding type from the message.
                string encoding = message.Attributes["googclient_schemaencoding"];
                string schemaName = message.Attributes["googclient_schemaname"];
                string revision = message.Attributes["googclient_schemarevisionid"];
    
                // Fetch the schema if we don't already have it.
                var avroSchema = schemaCache.GetOrAdd((schemaName, revision), key =>
                {
                    var pubSubSchema = schemaService.GetSchema($"{schemaName}@{revision}");
                    return Avro.Schema.Parse(pubSubSchema.Definition);
                });
    
                // Read the message.
                if (encoding == "BINARY")
                {
                    using var ms = new MemoryStream(message.Data.ToByteArray());
                    var decoder = new BinaryDecoder(ms);
                    var reader = new DefaultReader(avroSchema, avroSchema);
                    var record = reader.Read<GenericRecord>(null, decoder);
                    Console.WriteLine($"Message {message.MessageId}: {record.GetValue(0)}");
                    Interlocked.Increment(ref messageCount);
                }
                else
                {
                    Console.WriteLine("Expected only binary messages in this sample");
                }
                return Task.FromResult([SubscriberClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.html).[Reply](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.Reply.html).[Ack](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.Reply.html#Google_Cloud_PubSub_V1_SubscriberClient_Reply_Ack));
            });
            // Run for 10 seconds.
            await Task.Delay(10_000);
            await subscriber.[StopAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberClient.html#Google_Cloud_PubSub_V1_SubscriberClient_StopAsync_Google_Cloud_PubSub_V1_SubscriberClient_ShutdownOptions_System_Threading_CancellationToken_)(CancellationToken.None);
            // Lets make sure that the start task finished successfully after the call to stop.
            await startTask;
            return (messageCount, schemaCache.Count);
        }
    }
    

### Go

Before trying this sample, follow the Go setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://godoc.org/cloud.google.com/go/pubsub). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

Before trying this sample, follow the Java setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # subscription_id = "your-subscription-id"
    
    pubsub = Google::Cloud::[PubSub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html)
    subscriber = pubsub.[subscriber](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html) subscription_id
    
    # Cache for the parsed Avro schemas mapped by revision ID.
    schema_cache = {}
    cache_mutex = Mutex.[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html)
    
    listener = subscriber.[listen](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Subscriber.html) do |received_message|
      schema_name = received_message.attributes["googclient_schemaname"]
      revision_id = received_message.attributes["googclient_schemarevisionid"]
      encoding = received_message.attributes["googclient_schemaencoding"]
    
      # Prevent concurrent threads from racing to fetch and parse the same schema.
      avro_schema = cache_mutex.synchronize { schema_cache[revision_id] }
    
      if avro_schema.nil?
        begin
          require "avro"
          # The resource name format is projects/{project}/schemas/{schema}@{revision}.
          schema_resource = pubsub.schemas.get_schema name: "#{schema_name}@#{revision_id}"
    
          avro_schema = Avro::Schema.parse schema_resource.[definition](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-Schema.html)
    
          cache_mutex.synchronize { schema_cache[revision_id] = avro_schema }
        rescue StandardError => e
          puts "Could not get schema for revision #{revision_id}: #{e.message}"
          received_message.[reject!](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-ReceivedMessage.html)
          next
        end
      end
    
      begin
        case encoding
        when "BINARY"
          require "avro"
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
          puts "Unknown message encoding: #{encoding}. Rejecting message."
          received_message.[reject!](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-ReceivedMessage.html)
          next
        end
    
        received_message.[acknowledge!](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-ReceivedMessage.html)
      rescue StandardError => e
        puts "Failed to process message: #{e.message}"
        received_message.[reject!](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-ReceivedMessage.html)
      end
    end
    
    listener.[start](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-MessageListener.html)
    
    # Let the main thread sleep for 60 seconds so the thread for listening
    # messages does not quit.
    sleep 60
    listener.stop.wait!

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
