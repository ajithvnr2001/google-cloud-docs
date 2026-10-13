---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-create-topic-with-schema/
title: Create a schema when you create a topic \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:57:33.231591+00:00
---

# Create a schema when you create a topic  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-create-topic-with-schema/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  Create a schema when you create a topic Stay organized with collections  Save and categorize content based on your preferences. 

Create a topic and also create a schema.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Associate a schema with a topic](https://docs.cloud.google.com/pubsub/docs/associate-schema-topic)



## Code sample

### C++

Before trying this sample, follow the C++ setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace pubsub = ::google::cloud::pubsub;
    namespace pubsub_admin = ::google::cloud::pubsub_admin;
    [](pubsub_admin::TopicAdminClient client, std::string project_id,
       std::string topic_id, std::string schema_id, std::string const& encoding) {
      google::pubsub::v1::Topic request;
      request.set_name(pubsub::Topic(project_id, std::move(topic_id)).FullName());
      request.mutable_schema_settings()->set_schema(
          pubsub::Schema(std::move(project_id), std::move(schema_id)).FullName());
      request.mutable_schema_settings()->set_encoding(
          encoding == "JSON" ? google::pubsub::v1::JSON
                             : google::pubsub::v1::BINARY);
      auto topic = client.CreateTopic(request);
    
      // Note that kAlreadyExists is a possible error when the library retries.
      if (topic.status().code() == google::cloud::StatusCode::kAlreadyExists) {
        std::cout << "The topic already exists\n";
        return;
      }
      if (!topic) throw std::move(topic).status();
    
      std::cout << "The topic was successfully created: " << topic->DebugString()
                << "\n";
    }

### C#

Before trying this sample, follow the C# setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
    using [Grpc.Core](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.html);
    using System;
    
    public class CreateTopicWithSchemaSample
    {
        public Topic CreateTopicWithSchema(string projectId, string topicId, string schemaId, [Encoding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Encoding.html) encoding)
        {
            [PublisherServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html) publisher = [PublisherServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html#Google_Cloud_PubSub_V1_PublisherServiceApiClient_Create)();
            var topicName = [TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html).[FromProjectTopic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html#Google_Cloud_PubSub_V1_TopicName_FromProjectTopic_System_String_System_String_)(projectId, topicId);
            [Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Topic.html) topic = new [Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Topic.html)
            {
                TopicName = topicName,
                SchemaSettings = new [SchemaSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SchemaSettings.html)
                {
                    SchemaAsSchemaName = [SchemaName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SchemaName.html).[FromProjectSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SchemaName.html#Google_Cloud_PubSub_V1_SchemaName_FromProjectSchema_System_String_System_String_)(projectId, schemaId),
                    Encoding = encoding
                }
            };
    
            [Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Topic.html) receivedTopic = null;
            try
            {
                receivedTopic = publisher.[CreateTopic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html#Google_Cloud_PubSub_V1_PublisherServiceApiClient_CreateTopic_Google_Cloud_PubSub_V1_Topic_Google_Api_Gax_Grpc_CallSettings_)(topic);
                Console.WriteLine($"Topic {topic.[Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Topic.html#Google_Cloud_PubSub_V1_Topic_Name)} created.");
            }
            catch ([RpcException](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.RpcException.html) e) when (e.[Status](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.Status.html).[StatusCode](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html) == [StatusCode](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html).[AlreadyExists](https://docs.cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.StatusCode.html#Grpc_Core_StatusCode_AlreadyExists))
            {
                Console.WriteLine($"Topic {topicName} already exists.");
            }
            return receivedTopic;
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
    )
    
    func createTopicWithSchema(w io.Writer, projectID, topicID, schemaID string, encoding pubsubpb.Encoding) error {
    	// projectID := "my-project-id"
    	// topicID := "my-topic"
    	// schemaID := "my-schema-id"
    	// encoding := pubsub.EncodingJSON
    	ctx := context.Background()
    	client, err := pubsub.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    
    	topic := &pubsubpb.Topic{
    		Name: fmt.Sprintf("projects/%s/topics/%s", projectID, topicID),
    		SchemaSettings: &pubsubpb.SchemaSettings{
    			Schema:   fmt.Sprintf("projects/%s/schemas/%s", projectID, schemaID),
    			Encoding: encoding,
    		},
    	}
    	t, err := client.TopicAdminClient.CreateTopic(ctx, topic)
    	if err != nil {
    		return fmt.Errorf("CreateTopicWithConfig: %w", err)
    	}
    	fmt.Fprintf(w, "Topic with schema created: %#v\n", t)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.rpc.[AlreadyExistsException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.AlreadyExistsException.html);
    import com.google.cloud.pubsub.v1.[TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html);
    import com.google.pubsub.v1.[Encoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Encoding.html);
    import com.google.pubsub.v1.[SchemaName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaName.html);
    import com.google.pubsub.v1.[SchemaSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaSettings.html);
    import com.google.pubsub.v1.[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html);
    import com.google.pubsub.v1.[TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html);
    import java.io.IOException;
    
    public class CreateTopicWithSchemaExample {
    
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String topicId = "your-topic-id";
        // Use an existing schema.
        String schemaId = "your-schema-id";
        // Choose either BINARY or JSON message serialization in this topic.
        [Encoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Encoding.html) encoding = [Encoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Encoding.html).BINARY;
    
        createTopicWithSchemaExample(projectId, topicId, schemaId, encoding);
      }
    
      public static void createTopicWithSchemaExample(
          String projectId, String topicId, String schemaId, [Encoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Encoding.html) encoding) throws IOException {
        [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) topicName = [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html).of(projectId, topicId);
        [SchemaName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaName.html) schemaName = [SchemaName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaName.html).of(projectId, schemaId);
    
        [SchemaSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaSettings.html) schemaSettings =
            [SchemaSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaSettings.html).newBuilder().setSchema(schemaName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SchemaName.html#com_google_pubsub_v1_SchemaName_toString__)()).setEncoding(encoding).build();
    
        try ([TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html) topicAdminClient = [TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html).create()) {
    
          [Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html) topic =
              topicAdminClient.createTopic(
                  [Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html).newBuilder()
                      .setName(topicName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html#com_google_pubsub_v1_TopicName_toString__)())
                      .[setSchemaSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.Builder.html#com_google_pubsub_v1_Topic_Builder_setSchemaSettings_com_google_pubsub_v1_SchemaSettings_)(schemaSettings)
                      .build());
    
          System.out.println("Created topic with schema: " + topic.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html#com_google_pubsub_v1_Topic_getName__)());
        } catch ([AlreadyExistsException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.AlreadyExistsException.html) e) {
          System.out.println(schemaName + "already exists.");
        }
      }
    }

### PHP

Before trying this sample, follow the PHP setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/latest/pubsub/pubsubclient). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\PubSub\PubSubClient;
    use Google\Cloud\PubSub\Schema;
    
    /**
     * Create a topic with a schema.
     *
     * @param string $projectId
     * @param string $topicId
     * @param string $schemaId
     * @param string $encoding
     */
    function create_topic_with_schema($projectId, $topicId, $schemaId, $encoding)
    {
        $pubsub = new PubSubClient([
            'projectId' => $projectId,
        ]);
    
        $schema = $pubsub->schema($schemaId);
    
        $topic = $pubsub->createTopic($topicId, [
            'schemaSettings' => [
                // The schema may be provided as an instance of the schema type,
                // or by using the schema ID directly.
                'schema' => $schema,
                // Encoding may be either `BINARY` or `JSON`.
                // Provide a string or a constant from Google\Cloud\PubSub\V1\Encoding.
                'encoding' => $encoding,
            ]
        ]);
    
        printf('Topic %s created', $topic->name());
    }

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # topic_id = "your-topic-id"
    # schema_id = "your-schema-id"
    # Choose either BINARY or JSON as valid message encoding in this topic.
    # message_encoding = :BINARY
    
    pubsub = Google::Cloud::[PubSub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html)
    topic_admin = pubsub.[topic_admin](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html)
    
    topic = topic_admin.create_topic name: pubsub.topic_path(topic_id),
                                     schema_settings: {
                                       schema: pubsub.schema_path(schema_id),
                                       encoding: message_encoding
                                     }
    
    puts "Topic #{topic.name} created."

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
