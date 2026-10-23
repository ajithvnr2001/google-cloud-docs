---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-publish-proto-messages/
title: Publish messages of protobuf schema type \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:11.359485+00:00
---

# Publish messages of protobuf schema type  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-publish-proto-messages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  Publish messages of protobuf schema type Stay organized with collections  Save and categorize content based on your preferences. 

Publish messages that conform to a protocol buffer schema to a topic with a protocol buffer schema attached.

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
      std::vector<std::pair<std::string, std::string>> states{
          {"New York", "NY"},
          {"Pennsylvania", "PA"},
      };
      std::vector<future<void>> done;
      auto handler = [](future<StatusOr<std::string>> f) {
        auto id = f.get();
        if (!id) throw std::move(id).status();
      };
      for (auto& data : states) {
        google::cloud::pubsub::samples::State state;
        state.set_name(data.first);
        state.set_post_abbr(data.second);
        done.push_back(publisher
                           .Publish(pubsub::MessageBuilder{}
                                        .SetData(state.SerializeAsString())
                                        .Build())
                           .then(handler));
      }
      // Block until all messages are published.
      for (auto& d : done) d.get();
    }

### C#

Before trying this sample, follow the C# setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using Google.Cloud.PubSub.V1;
    using Google.Protobuf;
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Threading;
    using System.Threading.Tasks;
    
    public class PublishProtoMessagesAsyncSample
    {
        public async Task<int> PublishProtoMessagesAsync(string projectId, string topicId, IEnumerable<Utilities.State> messageStates)
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
                            var binaryMessage = state.ToByteString();
                            messageId = await publisher.PublishAsync(binaryMessage);
                            break;
                        case Encoding.Json:
                            var jsonMessage = JsonFormatter.Default.Format(state);
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
    
    	"cloud.google.com/go/pubsub/v2"
    	"cloud.google.com/go/pubsub/v2/apiv1/pubsubpb"
    	statepb "github.com/GoogleCloudPlatform/golang-samples/internal/pubsub/schemas"
    	"google.golang.org/protobuf/encoding/protojson"
    	"google.golang.org/protobuf/proto"
    )
    
    func publishProtoMessages(w io.Writer, projectID, topicID string) error {
    	// projectID := "my-project-id"
    	// topicID := "my-topic"
    	ctx := context.Background()
    	client, err := pubsub.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    
    	state := &statepb.State{
    		Name:     "Alaska",
    		PostAbbr: "AK",
    	}
    
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
    		msg, err = proto.Marshal(state)
    		if err != nil {
    			return fmt.Errorf("proto.Marshal err: %w", err)
    		}
    	case pubsubpb.Encoding_JSON:
    		msg, err = protojson.Marshal(state)
    		if err != nil {
    			return fmt.Errorf("protojson.Marshal err: %w", err)
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
    	fmt.Fprintf(w, "Published proto message with %#v encoding: %s\n", encoding, string(msg))
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.cloud.pubsub.v1.[Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html);
    import com.google.cloud.pubsub.v1.[TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import com.google.protobuf.util.[JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html);
    import com.google.pubsub.v1.[Encoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Encoding.html);
    import com.google.pubsub.v1.[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html);
    import com.google.pubsub.v1.[TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import utilities.StateProto.State;
    
    public class PublishProtobufMessagesExample {
    
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        // Use a topic created with a proto schema.
        String topicId = "your-topic-id";
    
        publishProtobufMessagesExample(projectId, topicId);
      }
    
      public static void publishProtobufMessagesExample(String projectId, String topicId)
          throws IOException, ExecutionException, InterruptedException {
    
        [Encoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Encoding.html) encoding = null;
    
        [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) topicName = [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html).of(projectId, topicId);
    
        // Get the topic encoding type.
        try ([TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html) topicAdminClient = [TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html).create()) {
          encoding = topicAdminClient.getTopic(topicName).getSchemaSettings().getEncoding();
        }
    
        [Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html) publisher = null;
    
        // Instantiate a protoc-generated class defined in `us-states.proto`.
        State state = State.newBuilder().setName("Alaska").setPostAbbr("AK").build();
    
        block:
        try {
          publisher = [Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html).newBuilder(topicName).build();
    
          [PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html).Builder message = [PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html).newBuilder();
    
          // Prepare an appropriately formatted message based on topic encoding.
          switch (encoding) {
            case BINARY:
              message.[setData](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.Builder.html#com_google_pubsub_v1_PubsubMessage_Builder_setData_com_google_protobuf_ByteString_)(state.toByteString());
              System.out.println("Publishing a BINARY-formatted message:\n" + message);
              break;
    
            case JSON:
              String jsonString = [JsonFormat](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.JsonFormat.html).printer().omittingInsignificantWhitespace().print(state);
              message.[setData](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.Builder.html#com_google_pubsub_v1_PubsubMessage_Builder_setData_com_google_protobuf_ByteString_)([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFromUtf8](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFromUtf8_java_lang_String_)(jsonString));
              System.out.println("Publishing a JSON-formatted message:\n" + message);
              break;
    
            default:
              break block;
          }
    
          // Publish the message.
          ApiFuture<String> future = [publish](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_publish_com_google_pubsub_v1_PubsubMessage_)er.[publish](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_publish_com_google_pubsub_v1_PubsubMessage_)(message.build());
          System.out.println("Published message ID: " + future.get());
    
        } finally {
          if (publisher != null) {
            publisher.[shutdown](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_shutdown__)();
            publisher.[awaitTermination](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Publisher.html#com_google_cloud_pubsub_v1_Publisher_awaitTermination_long_java_util_concurrent_TimeUnit_)(1, TimeUnit.MINUTES);
          }
        }
      }
    }

### PHP

Before trying this sample, follow the PHP setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/latest/pubsub/pubsubclient). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\PubSub\PubSubClient;
    use Google\Cloud\PubSub\V1\Encoding;
    
    use Utilities\StateProto;
    
    /**
     * Publish a message using a protocol buffer schema.
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
     * @param string $topicId
     * @return void
     */
    function publish_proto_messages($projectId, $topicId)
    {
        $pubsub = new PubSubClient([
            'projectId' => $projectId,
        ]);
    
        $messageData = new StateProto([
            'name' => 'Alaska',
            'post_abbr' => 'AK',
        ]);
    
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
            // encode as protobuf binary.
            $encodedMessageData = $messageData->serializeToString();
        } else {
            // encode as JSON.
            $encodedMessageData = $messageData->serializeToJsonString();
        }
    
        $topic->publish(['data' => $encodedMessageData]);
    
        printf('Published message with %s encoding', $encoding);
    }

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # topic_id = "your-topic-id"
    
    pubsub = Google::Cloud::[PubSub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html)
    topic_admin = pubsub.[topic_admin](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html)
    publisher = pubsub.[publisher](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html) topic_id
    state = Utilities::StateProto.[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html) name: "Alaska", post_abbr: "AK"
    
    topic = topic_admin.get_topic topic: pubsub.topic_path(topic_id)
    encoding = topic.[schema_settings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-Topic.html).encoding
    
    case encoding
    when :BINARY
      publisher.publish Utilities::StateProto.encode(state)
      puts "Published binary-encoded protobuf message."
    when :JSON
      publisher.publish Utilities::StateProto.encode_json(state)
      puts "Published JSON-encoded protobuf message."
    else
      raise "No encoding specified in #{topic.name}."
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
