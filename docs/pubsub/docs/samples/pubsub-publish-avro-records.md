---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-publish-avro-records/
title: Publish messages of Avro schema type \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:21:14.216524+00:00
---

# Publish messages of Avro schema type  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-publish-avro-records/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  Publish messages of Avro schema type Stay organized with collections  Save and categorize content based on your preferences. 

Publish messages that conform to an Avro schema to a topic with an Avro schema attached.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Publish messages to a topic with a schema](https://docs.cloud.google.com/pubsub/docs/publish-topics-schema)



## Code sample

### C++

Before trying this sample, follow the C++ setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace pubsub = ::google::cloud::pubsub;
    using ::google::cloud::future;
    using ::google::cloud::StatusOr;
    [](pubsub::Publisher publisher) {
      auto constexpr kNewYork =
          R"js({ "name": "New York", "post_abbr": "NY" })js";
      auto constexpr kPennsylvania =
          R"js({ "name": "Pennsylvania", "post_abbr": "PA" })js";
      std::vector<future<void>> done;
      auto handler = [](future<StatusOr<std::string>> f) {
        auto id = f.get();
        if (!id) throw std::move(id).status();
      };
      for (auto const* data : {kNewYork, kPennsylvania}) {
        done.push_back(
            publisher.Publish(pubsub::MessageBuilder{}.SetData(data).Build())
                .then(handler));
      }
      // Block until all messages are published.
      for (auto& d : done) d.get();
    }

### C#

Before trying this sample, follow the C# setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using Avro.IO;
    using Avro.Specific;
    using Google.Cloud.PubSub.V1;
    using System;
    using System.Collections.Generic;
    using System.IO;
    using System.Linq;
    using System.Threading;
    using System.Threading.Tasks;
    
    public class PublishAvroMessagesAsyncSample
    {
        public async Task<int> PublishAvroMessagesAsync(string projectId, string topicId, IEnumerable<AvroUtilities.State> messageStates)
        {
            TopicName topicName = TopicName.FromProjectTopic(projectId, topicId);
            PublisherClient publisher = await PublisherClient.CreateAsync(topicName);
    
            PublisherServiceApiClient publishApi = PublisherServiceApiClient.Create();
            var topic = publishApi.GetTopic(topicName);
    
            int publishedMessageCount = 0;
            var publishTasks = messageStates.Select(async state =>
            {
    
                try
                {
                    string messageId = null;
                    switch (topic.SchemaSettings.Encoding)
                    {
                        case Encoding.Binary:
                            using (var ms = new MemoryStream())
                            {
                                var encoder = new BinaryEncoder(ms);
                                var writer = new SpecificDefaultWriter(state.Schema);
                                writer.Write(state, encoder);
                                messageId = await publisher.PublishAsync(ms.ToArray());
                            }
                            break;
                        case Encoding.Json:
                            var jsonMessage = AvroUtilities.StateUtils.StateToJsonString(state);
                            messageId = await publisher.PublishAsync(jsonMessage);
                            break;
                    }
                    Console.WriteLine($"Published message {messageId}");
                    Interlocked.Increment(ref publishedMessageCount);
                }
                catch (Exception exception)
                {
                    Console.WriteLine($"An error occurred when publishing message {state}: {exception.Message}");
                }
            });
            await Task.WhenAll(publishTasks);
            // PublisherClient instance should be shutdown after use.
            // The TimeSpan specifies for how long to attempt to publish locally queued messages.
            await publisher.ShutdownAsync(TimeSpan.FromSeconds(15));
            return publishedMessageCount;
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
    
    	"cloud.google.com/go/pubsub/v2"
    	"cloud.google.com/go/pubsub/v2/apiv1/pubsubpb"
    	"github.com/linkedin/goavro/v2"
    )
    
    func publishAvroRecords(w io.Writer, projectID, topicID, avscFile string) error {
    	// projectID := "my-project-id"
    	// topicID := "my-topic"
    	// avscFile = "path/to/an/avro/schema/file(.avsc)/formatted/in/json"
    	ctx := context.Background()
    	client, err := pubsub.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    
    	avroSource, err := os.ReadFile(avscFile)
    	if err != nil {
    		return fmt.Errorf("os.ReadFile err: %w", err)
    	}
    	codec, err := goavro.NewCodec(string(avroSource))
    	if err != nil {
    		return fmt.Errorf("goavro.NewCodec err: %w", err)
    	}
    	record := map[string]interface{}{"name": "Alaska", "post_abbr": "AK"}
    
    	// Get the topic encoding type.
    	req := &pubsubpb.GetTopicRequest{
    		Topic: fmt.Sprintf("projects/%s/topics/%s", projectID, topicID),
    	}
    	t, err := client.TopicAdminClient.GetTopic(ctx, req)
    	if err != nil {
    		return fmt.Errorf("got err in GetTopic: %w", err)
    	}
    	encoding := t.SchemaSettings.Encoding
    
    	var msg []byte
    	switch encoding {
    	case pubsubpb.Encoding_BINARY:
    		msg, err = codec.BinaryFromNative(nil, record)
    		if err != nil {
    			return fmt.Errorf("codec.BinaryFromNative err: %w", err)
    		}
    	case pubsubpb.Encoding_JSON:
    		msg, err = codec.TextualFromNative(nil, record)
    		if err != nil {
    			return fmt.Errorf("codec.TextualFromNative err: %w", err)
    		}
    	default:
    		return fmt.Errorf("invalid encoding: %v", encoding)
    	}
    
    	// client.Publisher can be passed a topic ID (e.g. "my-topic") or
    	// a fully qualified name (e.g. "projects/my-project/topics/my-topic").
    	// If a topic ID is provided, the project ID from the client is used.
    	publisher := client.Publisher(topicID)
    	result := publisher.Publish(ctx, &pubsub.Message{
    		Data: msg,
    	})
    	_, err = result.Get(ctx)
    	if err != nil {
    		return fmt.Errorf("result.Get: %w", err)
    	}
    	fmt.Fprintf(w, "Published avro record: %s\n", string(msg))
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.cloud.pubsub.v1.[Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html);
    import com.google.cloud.pubsub.v1.[TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import com.google.pubsub.v1.[Encoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Encoding.html);
    import com.google.pubsub.v1.[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html);
    import com.google.pubsub.v1.[TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html);
    import java.io.ByteArrayOutputStream;
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import org.apache.avro.io.Encoder;
    import org.apache.avro.io.EncoderFactory;
    import utilities.State;
    
    public class PublishAvroRecordsExample {
    
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        // Use a topic created with an Avro schema.
        String topicId = "your-topic-id";
    
        publishAvroRecordsExample(projectId, topicId);
      }
    
      public static void publishAvroRecordsExample(String projectId, String topicId)
          throws IOException, ExecutionException, InterruptedException {
    
        [Encoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Encoding.html) encoding = null;
    
        [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) topicName = [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html).of(projectId, topicId);
    
        // Get the topic encoding type.
        try ([TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html) topicAdminClient = [TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html).create()) {
          encoding = topicAdminClient.getTopic(topicName).getSchemaSettings().getEncoding();
        }
    
        // Instantiate an avro-tools-generated class defined in `us-states.avsc`.
        State state = State.newBuilder().setName("Alaska").setPostAbbr("AK").build();
    
        [Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html) publisher = null;
    
        block:
        try {
          publisher = [Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html).newBuilder(topicName).build();
    
          // Prepare to serialize the object to the output stream.
          ByteArrayOutputStream byteStream = new ByteArrayOutputStream();
    
          Encoder encoder = null;
    
          // Prepare an appropriate encoder for publishing to the topic.
          switch (encoding) {
            case BINARY:
              System.out.println("Preparing a BINARY encoder...");
              encoder = EncoderFactory.get().directBinaryEncoder(byteStream, /* reuse= */ null);
              break;
    
            case JSON:
              System.out.println("Preparing a JSON encoder...");
              encoder = EncoderFactory.get().jsonEncoder(State.getClassSchema(), byteStream);
              break;
    
            default:
              break block;
          }
    
          // Encode the object and write it to the output stream.
          state.customEncode(encoder);
          encoder.[flush](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedOutputStream.html#com_google_protobuf_CodedOutputStream_flush__)();
    
          // Publish the encoded object as a Pub/Sub message.
          [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) data = [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(byteStream.toByteArray());
          [PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html) message = [PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html).newBuilder().[setData](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.Builder.html#com_google_pubsub_v1_PubsubMessage_Builder_setData_com_google_protobuf_ByteString_)(data).build();
          System.out.println("Publishing message: " + message);
    
          ApiFuture<String> future = [publish](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_publish_com_google_pubsub_v1_PubsubMessage_)er.[publish](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_publish_com_google_pubsub_v1_PubsubMessage_)(message);
          System.out.println("Published message ID: " + future.get());
    
        } finally {
          if (publisher != null) {
            publisher.[shutdown](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_shutdown__)();
            publisher.[awaitTermination](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_awaitTermination_long_java_util_concurrent_TimeUnit_)(1, TimeUnit.MINUTES);
          }
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
     * TODO(developer): Uncomment this variable before running the sample.
     */
    // const topicNameOrId = 'YOUR_TOPIC_NAME_OR_ID';
    
    // Imports the Google Cloud client library
    import {PubSub, Encodings} from '@google-cloud/pubsub';
    
    // And the Apache Avro library
    import * as avro from 'avro-js';
    import * as fs from 'fs';
    
    // Creates a client; cache this for further use
    const pubSubClient = new PubSub();
    
    interface ProvinceObject {
      name: string;
      post_abbr: string;
    }
    
    async function publishAvroRecords(topicNameOrId: string) {
      // Get the topic metadata to learn about its schema encoding.
      const topic = pubSubClient.topic(topicNameOrId);
      const [topicMetadata] = await topic.getMetadata();
      const topicSchemaMetadata = topicMetadata.schemaSettings;
    
      if (!topicSchemaMetadata) {
        console.log(`Topic ${topicNameOrId} doesn't seem to have a schema.`);
        return;
      }
      const schemaEncoding = topicSchemaMetadata.encoding;
    
      // Make an encoder using the official avro-js library.
      const definition = fs
        .readFileSync('system-test/fixtures/provinces.avsc')
        .toString();
      const type = avro.parse(definition);
    
      // Encode the message.
      const province: ProvinceObject = {
        name: 'Ontario',
        post_abbr: 'ON',
      };
      let dataBuffer: Buffer | undefined;
      switch (schemaEncoding) {
        case Encodings.Binary:
          dataBuffer = type.toBuffer(province);
          break;
        case Encodings.Json:
          dataBuffer = Buffer.from(type.toString(province));
          break;
        default:
          console.log(`Unknown schema encoding: ${schemaEncoding}`);
          break;
      }
      if (!dataBuffer) {
        console.log(`Invalid encoding ${schemaEncoding} on the topic.`);
        return;
      }
    
      const messageId = await topic.publish(dataBuffer);
      console.log(`Avro record ${messageId} published.`);
    }

### PHP

Before trying this sample, follow the PHP setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/latest/pubsub/pubsubclient). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\PubSub\PubSubClient;
    use Google\Cloud\PubSub\V1\Encoding;
    
    use AvroStringIO;
    use AvroSchema;
    use AvroIODatumWriter;
    use AvroIOBinaryEncoder;
    
    /**
     * Publish a message using an AVRO schema.
     *
     * This sample uses `wikimedia/avro` for AVRO encoding.
     *
     * @param string $projectId
     * @param string $topicId
     * @param string $definitionFile
     */
    function publish_avro_records($projectId, $topicId, $definitionFile)
    {
        $pubsub = new PubSubClient([
            'projectId' => $projectId,
        ]);
    
        $definition = (string) file_get_contents($definitionFile);
    
        $messageData = [
            'name' => 'Alaska',
            'post_abbr' => 'AK',
        ];
    
        $topic = $pubsub->topic($topicId);
    
        // get the encoding type.
        $topicInfo = $topic->info();
        $encoding = '';
        if (isset($topicInfo['schemaSettings']['encoding'])) {
            $encoding = $topicInfo['schemaSettings']['encoding'];
        }
    
        // if encoding is not set, we can't continue.
        if ($encoding === '') {
            printf('Topic %s does not have schema enabled', $topicId);
            return;
        }
    
        // If you are using gRPC, encoding may be an integer corresponding to an
        // enum value on Google\Cloud\PubSub\V1\Encoding.
        if (!is_string($encoding)) {
            $encoding = Encoding::name($encoding);
        }
    
        $encodedMessageData = '';
        if ($encoding == 'BINARY') {
            // encode as AVRO binary.
            $io = new AvroStringIO();
            $schema = AvroSchema::parse($definition);
            $writer = new AvroIODatumWriter($schema);
            $encoder = new AvroIOBinaryEncoder($io);
            $writer->write($messageData, $encoder);
    
            $encodedMessageData = $io->string();
        } else {
            // encode as JSON.
            $encodedMessageData = json_encode($messageData);
        }
    
        $topic->publish(['data' => $encodedMessageData]);
    
        printf('Published message with %s encoding', $encoding);
    }

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # topic_id = "your-topic-id"
    # avsc_file = "path/to/an/avro/schema/file/(.avsc)/formatted/in/json"
    
    pubsub = Google::Cloud::[PubSub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html)
    topic_admin = pubsub.[topic_admin](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html)
    publisher = pubsub.[publisher](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html) topic_id
    record = { "name" => "Alaska", "post_abbr" => "AK" }
    
    topic = topic_admin.get_topic topic: pubsub.topic_path(topic_id)
    encoding = topic.[schema_settings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-Topic.html).encoding
    
    case encoding
    when :BINARY
      require "avro"
      avro_schema = Avro::Schema.parse File.read(avsc_file)
      writer = Avro::IO::DatumWriter.[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html) avro_schema
      buffer = StringIO.[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html)
      encoder = Avro::IO::BinaryEncoder.[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html) buffer
      writer.write record, encoder
      publisher.publish buffer
      puts "Published binary-encoded AVRO message."
    when :JSON
      require "json"
      publisher.publish record.to_json
      puts "Published JSON-encoded AVRO message."
    else
      raise "No encoding specified in #{topic.name}."
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
