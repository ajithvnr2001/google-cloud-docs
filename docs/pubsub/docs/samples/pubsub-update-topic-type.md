---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-update-topic-type/
title: Change the type of a topic \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:37.108055+00:00
---

# Change the type of a topic  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-update-topic-type/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  Change the type of a topic Stay organized with collections  Save and categorize content based on your preferences. 

Change the type of a topic between ingestion and non-ingestion

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Change topic type](https://docs.cloud.google.com/pubsub/docs/change-topic-type)



## Code sample

### C++

Before trying this sample, follow the C++ setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace pubsub = ::google::cloud::pubsub;
    namespace pubsub_admin = ::google::cloud::pubsub_admin;
    [](pubsub_admin::TopicAdminClient client, std::string project_id,
       std::string topic_id, std::string stream_arn, std::string consumer_arn,
       std::string aws_role_arn, std::string gcp_service_account) {
      google::pubsub::v1::UpdateTopicRequest request;
    
      request.mutable_topic()->set_name(
          pubsub::Topic(std::move(project_id), std::move(topic_id)).FullName());
      auto* aws_kinesis = request.mutable_topic()
                              ->mutable_ingestion_data_source_settings()
                              ->mutable_aws_kinesis();
      aws_kinesis->set_stream_arn(stream_arn);
      aws_kinesis->set_consumer_arn(consumer_arn);
      aws_kinesis->set_aws_role_arn(aws_role_arn);
      aws_kinesis->set_gcp_service_account(gcp_service_account);
      *request.mutable_update_mask()->add_paths() =
          "ingestion_data_source_settings";
    
      auto topic = client.UpdateTopic(request);
      if (!topic) throw std::move(topic).status();
    
      std::cout << "The topic was successfully updated: " << topic->DebugString()
                << "\n";
    }

### C#

Before trying this sample, follow the C# setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using System;
    
    public class UpdateTopicTypeSample
    {
        public Topic UpdateTopicType(string projectId, string topicId, string streamArn, string consumerArn, string awsRoleArn, string gcpServiceAccount)
        {
            // Define settings for Kinesis ingestion
            [IngestionDataSourceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.IngestionDataSourceSettings.html) ingestionDataSourceSettings = new [IngestionDataSourceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.IngestionDataSourceSettings.html)
            {
                AwsKinesis = new IngestionDataSourceSettings.Types.AwsKinesis
                {
                    AwsRoleArn = awsRoleArn,
                    ConsumerArn = consumerArn,
                    GcpServiceAccount = gcpServiceAccount,
                    StreamArn = streamArn
                }
            };
            // Construct Topic with Kinesis ingestion settings
            [Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Topic.html) topic = new [Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Topic.html)()
            {
                Name = [TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html).[FormatProjectTopic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html#Google_Cloud_PubSub_V1_TopicName_FormatProjectTopic_System_String_System_String_)(projectId, topicId),
                IngestionDataSourceSettings = ingestionDataSourceSettings
            };
    
            [PublisherServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html) client = [PublisherServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html#Google_Cloud_PubSub_V1_PublisherServiceApiClient_Create)();
            [UpdateTopicRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.UpdateTopicRequest.html) updateTopicRequest = new [UpdateTopicRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.UpdateTopicRequest.html)
            {
                Topic = topic,
                //Construct a field mask to indicate which field to update in the topic.
                UpdateMask = new [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html) { Paths = { "ingestion_data_source_settings" } }
            };
            [Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Topic.html) updatedTopic = client.[UpdateTopic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html#Google_Cloud_PubSub_V1_PublisherServiceApiClient_UpdateTopic_Google_Cloud_PubSub_V1_Topic_Google_Protobuf_WellKnownTypes_FieldMask_Google_Api_Gax_Grpc_CallSettings_)(updateTopicRequest);
            Console.WriteLine($"Topic {topic.[Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Topic.html#Google_Cloud_PubSub_V1_Topic_Name)} updated.");
    
            return updatedTopic;
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
    	"google.golang.org/protobuf/types/known/fieldmaskpb"
    )
    
    func updateTopicType(w io.Writer, projectID, topic string) error {
    	// projectID := "my-project-id"
    	// topic := "projects/my-project-id/topics/my-topic"
    	streamARN := "stream-arn"
    	consumerARN := "consumer-arn"
    	awsRoleARN := "aws-role-arn"
    	gcpServiceAccount := "gcp-service-account"
    
    	ctx := context.Background()
    	client, err := pubsub.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	pbTopic := &pubsubpb.Topic{
    		Name: topic,
    		IngestionDataSourceSettings: &pubsubpb.IngestionDataSourceSettings{
    			Source: &pubsubpb.IngestionDataSourceSettings_AwsKinesis_{
    				AwsKinesis: &pubsubpb.IngestionDataSourceSettings_AwsKinesis{
    					StreamArn:         streamARN,
    					ConsumerArn:       consumerARN,
    					AwsRoleArn:        awsRoleARN,
    					GcpServiceAccount: gcpServiceAccount,
    				},
    			},
    		},
    	}
    	updateReq := &pubsubpb.UpdateTopicRequest{
    		Topic: pbTopic,
    		UpdateMask: &fieldmaskpb.FieldMask{
    			Paths: []string{"ingestion_data_source_settings"},
    		},
    	}
    	topicCfg, err := client.TopicAdminClient.UpdateTopic(ctx, updateReq)
    	if err != nil {
    		return fmt.Errorf("topic.Update: %w", err)
    	}
    	fmt.Fprintf(w, "Topic updated with kinesis source: %v\n", topicCfg)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.pubsub.v1.[TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import com.google.pubsub.v1.[IngestionDataSourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.html);
    import com.google.pubsub.v1.[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html);
    import com.google.pubsub.v1.[TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html);
    import com.google.pubsub.v1.[UpdateTopicRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.UpdateTopicRequest.html);
    import java.io.IOException;
    
    public class UpdateTopicTypeExample {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String topicId = "your-topic-id";
        // Kinesis ingestion settings.
        String streamArn = "stream-arn";
        String consumerArn = "consumer-arn";
        String awsRoleArn = "aws-role-arn";
        String gcpServiceAccount = "gcp-service-account";
    
        UpdateTopicTypeExample.updateTopicTypeExample(
            projectId, topicId, streamArn, consumerArn, awsRoleArn, gcpServiceAccount);
      }
    
      public static void updateTopicTypeExample(
          String projectId,
          String topicId,
          String streamArn,
          String consumerArn,
          String awsRoleArn,
          String gcpServiceAccount)
          throws IOException {
        try ([TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html) topicAdminClient = [TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html).create()) {
          [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) topicName = [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html).of(projectId, topicId);
    
          [IngestionDataSourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.html).[AwsKinesis](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.AwsKinesis.html) awsKinesis =
              [IngestionDataSourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.html).AwsKinesis.newBuilder()
                  .setStreamArn(streamArn)
                  .[setConsumerArn](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.AwsKinesis.Builder.html#com_google_pubsub_v1_IngestionDataSourceSettings_AwsKinesis_Builder_setConsumerArn_java_lang_String_)(consumerArn)
                  .setAwsRoleArn(awsRoleArn)
                  .setGcpServiceAccount(gcpServiceAccount)
                  .build();
          [IngestionDataSourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.html) ingestionDataSourceSettings =
              [IngestionDataSourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.html).newBuilder().[setAwsKinesis](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.Builder.html#com_google_pubsub_v1_IngestionDataSourceSettings_Builder_setAwsKinesis_com_google_pubsub_v1_IngestionDataSourceSettings_AwsKinesis_)(awsKinesis).build();
    
          // Construct the topic with Kinesis ingestion settings.
          [Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html) topic =
              [Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html).newBuilder()
                  .setName(topicName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html#com_google_pubsub_v1_TopicName_toString__)())
                  .[setIngestionDataSourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.Builder.html#com_google_pubsub_v1_Topic_Builder_setIngestionDataSourceSettings_com_google_pubsub_v1_IngestionDataSourceSettings_)(ingestionDataSourceSettings)
                  .build();
    
          // Construct a field mask to indicate which field to update in the topic.
          [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) updateMask =
              [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("ingestion_data_source_settings").build();
    
          [UpdateTopicRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.UpdateTopicRequest.html) request =
              [UpdateTopicRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.UpdateTopicRequest.html).newBuilder().setTopic(topic).setUpdateMask(updateMask).build();
    
          [Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html) response = topicAdminClient.updateTopic(request);
    
          System.out.println(
              "Updated topic with Kinesis ingestion settings: " + response.getAllFields());
        }
      }
    }

### PHP

Before trying this sample, follow the PHP setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/latest/pubsub/pubsubclient). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\PubSub\PubSubClient;
    
    /**
     * Changes the type of a Pub/Sub topic.
     *
     * @param string $projectId  The Google project ID.
     * @param string $topicName  The Pub/Sub topic name.
     * @param string $streamArn  The Kinesis stream ARN to ingest data from.
     * @param string $consumerArn  The Kinesis consumer ARN to used for ingestion in Enhanced Fan-Out mode. The consumer must be already created and ready to be used.
     * @param string $awsRoleArn  AWS role ARN to be used for Federated Identity authentication with Kinesis. Check the Pub/Sub docs for how to set up this role and the required permissions that need to be attached to it.
     * @param string $gcpServiceAccount  The GCP service account to be used for Federated Identity authentication with Kinesis (via a AssumeRoleWithWebIdentity call for the provided role). The $awsRoleArn must be set up with accounts.google.com:sub equals to this service account number.
     */
    function update_topic_type(
        string $projectId,
        string $topicName,
        string $streamArn,
        string $consumerArn,
        string $awsRoleArn,
        string $gcpServiceAccount
    ): void {
        $pubsub = new PubSubClient([
            'projectId' => $projectId,
        ]);
    
        $topic = $pubsub->topic($topicName);
    
        $topic->update([
            'ingestionDataSourceSettings' => [
                'aws_kinesis' => [
                    'stream_arn' => $streamArn,
                    'consumer_arn' => $consumerArn,
                    'aws_role_arn' => $awsRoleArn,
                    'gcp_service_account' => $gcpServiceAccount
                ]
            ]
        ], [
            'updateMask' => [
                'ingestionDataSourceSettings'
            ]
        ]);
    
        printf('Topic updated: %s' . PHP_EOL, $topic->name());
    }

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # topic_id = "your-topic-id"
    # stream_arn = "arn:aws:kinesis:us-west-2:111111111111:stream/stream-name"
    # consumer_arn =
    # "arn:aws:kinesis:us-west-2:111111111111:stream/x/consumer/y:1111111111"
    # aws_role_arn = "arn:aws:iam::111111111111:role/role-name"
    # gcp_service_account = "service-account@project.iam.gserviceaccount.com"
    
    pubsub = Google::Cloud::[Pubsub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud.html).new
    topic_admin = pubsub.topic_admin
    
    ingestion_data_source_settings =
      Google::Cloud::PubSub::V1::IngestionDataSourceSettings.new \
        aws_kinesis: {
          stream_arn: stream_arn,
          consumer_arn: consumer_arn,
          aws_role_arn: aws_role_arn,
          gcp_service_account: gcp_service_account
        }
    topic = topic_admin.get_topic topic: pubsub.topic_path(topic_id)
    topic.ingestion_data_source_settings = ingestion_data_source_settings
    
    topic = topic_admin.update_topic topic: topic,
                                     update_mask: {
                                       paths: ["ingestion_data_source_settings"]
                                     }
    
    puts "Topic #{topic.name} updated."

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
