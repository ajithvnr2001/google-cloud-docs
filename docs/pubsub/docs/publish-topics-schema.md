---
url: https://docs.cloud.google.com/pubsub/docs/publish-topics-schema/
title: Publish messages to a topic with a schema \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:03:59.783183+00:00
---

# Publish messages to a topic with a schema  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/publish-topics-schema/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Publish messages to a topic with a schema Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to publish messages to a topic with a schema.

## Before you begin

Before configuring the publish workflow, ensure you have completed the following tasks:

  * Understand how [Pub/Sub schemas work](https://docs.cloud.google.com/pubsub/docs/schemas).
  * [Associate a schema with a topic](https://docs.cloud.google.com/pubsub/docs/associate-schema-topic).



### Required roles

To get the permissions that you need to publish messages to a topic, ask your administrator to grant you the [Pub/Sub Publisher ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.publisher) (`roles/pubsub.publisher`) IAM role on the topic. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

You need [additional permissions](https://docs.cloud.google.com/pubsub/docs/access-control) to create or update topics and subscriptions. 

### Publish messages with schema

You can publish messages to a topic that is associated with a schema. You must encode the messages in the schema and format that you specified when you [created the topic](https://docs.cloud.google.com/pubsub/docs/create-topic). A message matches the schema associated with the topic if it matches any of the schema's revision in the [allowed range of revisions](https://docs.cloud.google.com/pubsub/docs/associate-schema-topic#schema-validation-logic). Messages are evaluated against revisions in order from the most recent allowed revision until either a match is found or the oldest allowed revision is reached. Pub/Sub adds the following attributes to a message successfully published to a topic associated with a schema:

  * `googclient_schemaname`: The name of the schema used for validation.

  * `googclient_schemaencoding`: The encoding of the message, either JSON or BINARY.

  * `googclient_schemarevisionid`: The revision ID of the schema used to parse and validate the message. Each revision has a unique revision ID associated with it. The revision ID is an auto-generated eight-character UUID.




When a message does not match any of the schema revisions allowed by the topic, Pub/Sub returns an `INVALID_ARGUMENT` error to the publish request. 

Pub/Sub only evaluates messages against schema revisions at publish time. [Committing a new schema revision](https://docs.cloud.google.com/pubsub/docs/commit-schema-revision) or [changing the schema associated with a topic](https://docs.cloud.google.com/pubsub/docs/associate-schema-topic#edit-schema-association) after publishing a message does not re-evaluate that message nor change any of the attached schema message attributes.

**Caution:** Deleting a schema or a schema revision is permanent. Any messages that validated against a deleted schema revision at the time of publish cannot be written to BigQuery using a [BigQuery subscription](https://docs.cloud.google.com/pubsub/docs/create-bigquery-subscription) with **Use topic schema** enabled. Instead of deleting a schema or revision, consider [rolling back a schema](https://docs.cloud.google.com/pubsub/docs/roll-back-schemas).

You can publish messages to a topic with an associated schema in a Google Cloud project using the Google Cloud console, the gcloud CLI, the Pub/Sub API, or the Cloud Client Libraries.

### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Publish a sample message using the [gcloud pubsub topics publish](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics/publish) command.
         
         gcloud pubsub topics publish TOPIC_ID \
             --message=MESSAGE
         

Replace the following:



  * TOPIC_ID: Name of the topic that you already created.

  * MESSAGE: Message published to the topic. A sample message can be `{"name": "Alaska", "post_abbr": "AK"}`.




### C++

Before trying this sample, follow the C++ setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 

**Avro**
    
    
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

**Proto**
    
    
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

Before trying this sample, follow the C# setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 

**Avro**
    
    
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

**Proto**
    
    
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

The following sample uses the major version of the Go Pub/Sub client library (v2). If you are still using the v1 library, see [the migration guide to v2](https://github.com/googleapis/google-cloud-go/blob/main/pubsub/MIGRATING.md). To see a list of v1 code samples, see [ the deprecated code samples](https://docs.cloud.google.com/pubsub/docs/samples?language=golang&text=deprecated).

Before trying this sample, follow the Go setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/pubsub/v2).

**Avro**
    
    
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
    

**Proto**
    
    
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

**Note:** To learn how to compile your Avro/Proto schema to a Java class, see the [Avro](https://avro.apache.org/docs/1.10.1/gettingstartedjava.html#Compiling+the+schema) or [Protocol Buffer](https://developers.google.com/protocol-buffers/docs/javatutorial#compiling-your-protocol-buffers) documentation.

Before trying this sample, follow the Java setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 

**Avro**
    
    
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

**Proto**
    
    
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

### Node.js

Before trying this sample, follow the Node.js setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 

**Avro**
    
    
    /**
     * TODO(developer): Uncomment this variable before running the sample.
     */
    // const topicNameOrId = 'YOUR_TOPIC_NAME_OR_ID';
    
    // Imports the Google Cloud client library
    const {PubSub, Encodings} = require('[@google-cloud/pubsub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html)');
    
    // And the Apache Avro library
    const avro = require('avro-js');
    const fs = require('fs');
    
    // Creates a client; cache this for further use
    const pubSubClient = new [PubSub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)();
    
    async function publishAvroRecords(topicNameOrId) {
      // Cache topic objects (publishers) and reuse them.
      const topic = pubSubClient.topic(topicNameOrId);
    
      // Get the topic metadata to learn about its schema encoding.
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
      const province = {
        name: 'Ontario',
        post_abbr: 'ON',
      };
      let dataBuffer;
      switch (schemaEncoding) {
        case [Encodings](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html).Binary:
          dataBuffer = type.toBuffer(province);
          break;
        case [Encodings](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html).Json:
          dataBuffer = Buffer.[from](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/duration.html)(type.toString(province));
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

**Protocol Buffer**
    
    
    /**
     * TODO(developer): Uncomment this variable before running the sample.
     */
    // const topicNameOrId = 'YOUR_TOPIC_NAME_OR_ID';
    
    // Imports the Google Cloud client library
    const {PubSub, Encodings} = require('[@google-cloud/pubsub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html)');
    
    // And the protobufjs library
    const protobuf = require('protobufjs');
    
    // Creates a client; cache this for further use
    const pubSubClient = new [PubSub](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/pubsub.html)();
    
    async function publishProtobufMessages(topicNameOrId) {
      // Cache topic objects (publishers) and reuse them.
      const topic = pubSubClient.topic(topicNameOrId);
    
      // Get the topic metadata to learn about its schema.
      const [topicMetadata] = await topic.getMetadata();
      const topicSchemaMetadata = topicMetadata.schemaSettings;
    
      if (!topicSchemaMetadata) {
        console.log(`Topic ${topicNameOrId} doesn't seem to have a schema.`);
        return;
      }
      const schemaEncoding = topicSchemaMetadata.encoding;
    
      // Encode the message.
      const province = {
        name: 'Ontario',
        postAbbr: 'ON',
      };
    
      // Make an encoder using the protobufjs library.
      //
      // Since we're providing the test message for a specific schema here, we'll
      // also code in the path to a sample proto definition.
      const root = await protobuf.load('system-test/fixtures/provinces.proto');
      const Province = root.lookupType('utilities.Province');
      const message = Province.create(province);
    
      let dataBuffer;
      switch (schemaEncoding) {
        case [Encodings](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html).Binary:
          dataBuffer = Buffer.[from](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/duration.html)(Province.encode(message).finish());
          break;
        case [Encodings](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/overview.html).Json:
          dataBuffer = Buffer.[from](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/duration.html)(JSON.stringify(message.toJSON()));
          break;
        default:
          console.log(`Unknown schema encoding: ${schemaEncoding}`);
          break;
      }
      if (!dataBuffer) {
        console.log(`Invalid encoding ${schemaEncoding} on the topic.`);
        return;
      }
    
      const messageId = await topic.[publishMessage](https://docs.cloud.google.com/nodejs/docs/reference/pubsub/latest/pubsub/topic.html)({data: dataBuffer});
      console.log(`Protobuf message ${messageId} published.`);
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 

**Avro**
    
    
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
      // Cache topic objects (publishers) and reuse them.
      const topic = pubSubClient.topic(topicNameOrId);
    
      // Get the topic metadata to learn about its schema encoding.
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

**Protocol Buffer**
    
    
    /**
     * TODO(developer): Uncomment this variable before running the sample.
     */
    // const topicNameOrId = 'YOUR_TOPIC_NAME_OR_ID';
    
    // Imports the Google Cloud client library
    import {PubSub, Encodings} from '@google-cloud/pubsub';
    
    // And the protobufjs library
    import * as protobuf from 'protobufjs';
    
    // Creates a client; cache this for further use
    const pubSubClient = new PubSub();
    
    interface ProvinceObject {
      name: string;
      postAbbr: string;
    }
    
    async function publishProtobufMessages(topicNameOrId: string) {
      // Cache topic objects (publishers) and reuse them.
      const topic = pubSubClient.topic(topicNameOrId);
    
      // Get the topic metadata to learn about its schema.
      const [topicMetadata] = await topic.getMetadata();
      const topicSchemaMetadata = topicMetadata.schemaSettings;
    
      if (!topicSchemaMetadata) {
        console.log(`Topic ${topicNameOrId} doesn't seem to have a schema.`);
        return;
      }
      const schemaEncoding = topicSchemaMetadata.encoding;
    
      // Encode the message.
      const province: ProvinceObject = {
        name: 'Ontario',
        postAbbr: 'ON',
      };
    
      // Make an encoder using the protobufjs library.
      //
      // Since we're providing the test message for a specific schema here, we'll
      // also code in the path to a sample proto definition.
      const root = await protobuf.load('system-test/fixtures/provinces.proto');
      const Province = root.lookupType('utilities.Province');
      const message = Province.create(province);
    
      let dataBuffer: Buffer | undefined;
      switch (schemaEncoding) {
        case Encodings.Binary:
          dataBuffer = Buffer.from(Province.encode(message).finish());
          break;
        case Encodings.Json:
          dataBuffer = Buffer.from(JSON.stringify(message.toJSON()));
          break;
        default:
          console.log(`Unknown schema encoding: ${schemaEncoding}`);
          break;
      }
      if (!dataBuffer) {
        console.log(`Invalid encoding ${schemaEncoding} on the topic.`);
        return;
      }
    
      const messageId = await topic.publishMessage({data: dataBuffer});
      console.log(`Protobuf message ${messageId} published.`);
    }

### PHP

Before trying this sample, follow the PHP setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub PHP API reference documentation](https://cloud.google.com/php/docs/reference/cloud-pubsub/latest). 

**Avro**
    
    
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

**Protocol Buffer**
    
    
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

### Python

Before trying this sample, follow the Python setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/pubsub/latest). 

**Avro**
    
    
    from avro.io import BinaryEncoder, DatumWriter
    import avro.schema as schema
    import io
    import json
    from google.api_core.exceptions import NotFound
    from google.cloud.pubsub import [PublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)
    from google.pubsub_v1.types import Encoding
    
    # TODO(developer): Replace these variables before running the sample.
    # project_id = "your-project-id"
    # topic_id = "your-topic-id"
    # avsc_file = "path/to/an/avro/schema/file/(.avsc)/formatted/in/json"
    
    publisher_client = PublisherClient()
    topic_path = [publisher_client](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.html).topic_path(project_id, topic_id)
    
    # Prepare to write Avro records to the binary output stream.
    with open(avsc_file, "rb") as file:
        avro_schema = schema.parse(file.read())
    writer = DatumWriter(avro_schema)
    bout = io.BytesIO()
    
    # Prepare some data using a Python dictionary that matches the Avro schema
    record = {"name": "Alaska", "post_abbr": "AK"}
    
    try:
        # Get the topic encoding type.
        topic = [publisher_client](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.html).get_topic(request={"topic": topic_path})
        encoding = topic.schema_settings.encoding
    
        # Encode the data according to the message serialization type.
        if encoding == Encoding.BINARY:
            encoder = BinaryEncoder(bout)
            writer.write(record, encoder)
            data = bout.getvalue()
            print(f"Preparing a binary-encoded message:\n{[data](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_data).decode()}")
        elif encoding == Encoding.JSON:
            data_str = json.dumps(record)
            print(f"Preparing a JSON-encoded message:\n{data_str}")
            data = data_str.encode("utf-8")
        else:
            print(f"No encoding specified in {topic_path}. Abort.")
            exit(0)
    
        future = [publish](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)er_client.[publish](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)(topic_path, data)
        print(f"Published message ID: {future.result()}")
    
    except NotFound:
        print(f"{topic_id} not found.")

**Protocol Buffer**
    
    
    from google.api_core.exceptions import NotFound
    from google.cloud.pubsub import [PublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)
    from google.protobuf.json_format import MessageToJson
    from google.pubsub_v1.types import Encoding
    
    from utilities import us_states_pb2  # type: ignore
    
    # TODO(developer): Replace these variables before running the sample.
    # project_id = "your-project-id"
    # topic_id = "your-topic-id"
    
    publisher_client = PublisherClient()
    topic_path = [publisher_client](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.html).topic_path(project_id, topic_id)
    
    try:
        # Get the topic encoding type.
        topic = [publisher_client](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.html).get_topic(request={"topic": topic_path})
        encoding = topic.schema_settings.encoding
    
        # Instantiate a protoc-generated class defined in `us-states.proto`.
        state = us_states_pb2.StateProto()
        state.name = "Alaska"
        state.post_abbr = "AK"
    
        # Encode the data according to the message serialization type.
        if encoding == Encoding.BINARY:
            data = state.SerializeToString()
            print(f"Preparing a binary-encoded message:\n{[data](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_data)}")
        elif encoding == Encoding.JSON:
            json_object = MessageToJson(state)
            data = str(json_object).encode("utf-8")
            print(f"Preparing a JSON-encoded message:\n{[data](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message.html#google_cloud_pubsub_v1_subscriber_message_Message_data)}")
        else:
            print(f"No encoding specified in {topic_path}. Abort.")
            exit(0)
    
        future = [publish](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)er_client.[publish](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)(topic_path, data)
        print(f"Published message ID: {future.result()}")
    
    except NotFound:
        print(f"{topic_id} not found.")

### Ruby

The following sample uses Ruby Pub/Sub client library v3. If you are still using the v2 library, see [ the migration guide to v3](https://github.com/googleapis/google-cloud-ruby/blob/main/google-cloud-pubsub/MIGRATION_GUIDE.md). To see a list of Ruby v2 code samples, see [ the deprecated code samples](https://docs.cloud.google.com/pubsub/docs/samples?language=ruby&text=deprecated).

Before trying this sample, follow the Ruby setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 

**Avro**
    
    
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

**Protocol Buffer**
    
    
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

  * To restrict the locations in which Pub/Sub stores message data, see [Restricting Pub/Sub resource locations](https://docs.cloud.google.com/pubsub/docs/resource-location-restriction).

  * To learn more about receiving messages, see [Choose a subscription type](https://docs.cloud.google.com/pubsub/docs/subscriber).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
