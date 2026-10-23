---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-create-topic-with-aws-msk-ingestion/
title: Create topic with AWS MSK ingestion \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:03:58.728940+00:00
---

# Create topic with AWS MSK ingestion  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-create-topic-with-aws-msk-ingestion/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  Create topic with AWS MSK ingestion Stay organized with collections  Save and categorize content based on your preferences. 

Create topic with AWS MSK ingestion

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create an Amazon Managed Streaming for Apache Kafka import topic](https://docs.cloud.google.com/pubsub/docs/create-amazon-msk-import-topic)



## Code sample

### C++

Before trying this sample, follow the C++ setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace pubsub = ::google::cloud::pubsub;
    namespace pubsub_admin = ::google::cloud::pubsub_admin;
    [](pubsub_admin::TopicAdminClient client, std::string project_id,
       std::string topic_id, std::string const& cluster_arn,
       std::string const& msk_topic, std::string const& aws_role_arn,
       std::string const& gcp_service_account) {
      google::pubsub::v1::Topic request;
      request.set_name(
          pubsub::Topic(std::move(project_id), std::move(topic_id)).FullName());
      auto* aws_msk =
          request.mutable_ingestion_data_source_settings()->mutable_aws_msk();
      aws_msk->set_cluster_arn(cluster_arn);
      aws_msk->set_topic(msk_topic);
      aws_msk->set_aws_role_arn(aws_role_arn);
      aws_msk->set_gcp_service_account(gcp_service_account);
    
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
    using System;
    
    public class CreateTopicWithAwsMskIngestionSample
    {
        public Topic CreateTopicWithAwsMskIngestion(string projectId, string topicId, string clusterArn, string mskTopic, string awsRoleArn, string gcpServiceAccount)
        {
            // Define settings for Amazon MSK ingestion
            [IngestionDataSourceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.IngestionDataSourceSettings.html) ingestionDataSourceSettings = new [IngestionDataSourceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.IngestionDataSourceSettings.html)
            {
                AwsMsk = new IngestionDataSourceSettings.Types.AwsMsk
                {
                    ClusterArn = clusterArn,
                    Topic = mskTopic,
                    AwsRoleArn = awsRoleArn,
                    GcpServiceAccount = gcpServiceAccount
                }
            };
    
            [PublisherServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html) publisher = [PublisherServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html#Google_Cloud_PubSub_V1_PublisherServiceApiClient_Create)();
            [Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Topic.html) topic = new [Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Topic.html)()
            {
                Name = [TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html).[FormatProjectTopic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html#Google_Cloud_PubSub_V1_TopicName_FormatProjectTopic_System_String_System_String_)(projectId, topicId),
                IngestionDataSourceSettings = ingestionDataSourceSettings
            };
            [Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Topic.html) createdTopic = publisher.[CreateTopic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html#Google_Cloud_PubSub_V1_PublisherServiceApiClient_CreateTopic_Google_Cloud_PubSub_V1_Topic_Google_Api_Gax_Grpc_CallSettings_)(topic);
            Console.WriteLine($"Topic {topic.[Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Topic.html#Google_Cloud_PubSub_V1_Topic_Name)} created.");
    
            return createdTopic;
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
    
    func createTopicWithAWSMSKIngestion(w io.Writer, projectID, topicID, clusterARN, mskTopic, awsRoleARN, gcpSA string) error {
    	// projectID := "my-project-id"
    	// topicID := "my-topic"
    
    	// // AWS MSK ingestion settings.
    	// clusterARN := "cluster-arn"
    	// mskTopic := "msk-topic"
    	// awsRoleARN := "aws-role-arn"
    	// gcpSA := "gcp-service-account"
    
    	ctx := context.Background()
    	client, err := pubsub.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	topicpb := &pubsubpb.Topic{
    		Name: fmt.Sprintf("projects/%s/topics/%s", projectID, topicID),
    		IngestionDataSourceSettings: &pubsubpb.IngestionDataSourceSettings{
    			Source: &pubsubpb.IngestionDataSourceSettings_AwsMsk_{
    				AwsMsk: &pubsubpb.IngestionDataSourceSettings_AwsMsk{
    					ClusterArn:        clusterARN,
    					Topic:             mskTopic,
    					AwsRoleArn:        awsRoleARN,
    					GcpServiceAccount: gcpSA,
    				},
    			},
    		},
    	}
    	topic, err := client.TopicAdminClient.CreateTopic(ctx, topicpb)
    	if err != nil {
    		return fmt.Errorf("CreateTopic: %w", err)
    	}
    	fmt.Fprintf(w, "Created topic with AWS MSK ingestion settings: %v\n", topic)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.pubsub.v1.[TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html);
    import com.google.pubsub.v1.[IngestionDataSourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.html);
    import com.google.pubsub.v1.[Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html);
    import com.google.pubsub.v1.[TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html);
    import java.io.IOException;
    
    public class CreateTopicWithAwsMskIngestionExample {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String topicId = "your-topic-id";
        // AWS MSK ingestion settings.
        String clusterArn = "cluster-arn";
        String mskTopic = "msk-topic";
        String awsRoleArn = "aws-role-arn";
        String gcpServiceAccount = "gcp-service-account";
    
        createTopicWithAwsMskIngestionExample(
            projectId, topicId, clusterArn, mskTopic, awsRoleArn, gcpServiceAccount);
      }
    
      public static void createTopicWithAwsMskIngestionExample(
          String projectId,
          String topicId,
          String clusterArn,
          String mskTopic,
          String awsRoleArn,
          String gcpServiceAccount)
          throws IOException {
        try ([TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html) topicAdminClient = [TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html).create()) {
          [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) topicName = [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html).of(projectId, topicId);
    
          [IngestionDataSourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.html).[AwsMsk](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.AwsMsk.html) awsMsk =
              [IngestionDataSourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.html).AwsMsk.newBuilder()
                  .setClusterArn(clusterArn)
                  .setTopic(mskTopic)
                  .setAwsRoleArn(awsRoleArn)
                  .setGcpServiceAccount(gcpServiceAccount)
                  .build();
          [IngestionDataSourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.html) ingestionDataSourceSettings =
              [IngestionDataSourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.html).newBuilder().[setAwsMsk](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.Builder.html#com_google_pubsub_v1_IngestionDataSourceSettings_Builder_setAwsMsk_com_google_pubsub_v1_IngestionDataSourceSettings_AwsMsk_)(awsMsk).build();
    
          [Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html) topic =
              topicAdminClient.createTopic(
                  [Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html).newBuilder()
                      .setName(topicName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html#com_google_pubsub_v1_TopicName_toString__)())
                      .[setIngestionDataSourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.Builder.html#com_google_pubsub_v1_Topic_Builder_setIngestionDataSourceSettings_com_google_pubsub_v1_IngestionDataSourceSettings_)(ingestionDataSourceSettings)
                      .build());
    
          System.out.println("Created topic with AWS MSK ingestion settings: " + topic.getAllFields());
        }
      }
    }

### PHP

Before trying this sample, follow the PHP setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/latest/pubsub/pubsubclient). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\PubSub\PubSubClient;
    
    /**
     * Creates a Pub/Sub topic with AWS MSK ingestion.
     *
     * @param string $projectId  The Google project ID.
     * @param string $topicName  The Pub/Sub topic name.
     * @param string $clusterArn  The Amazon Resource Name (ARN) that uniquely identifies the cluster.
     * @param string $mskTopic  The name of the topic in the Amazon MSK cluster that Pub/Sub will import from.
     * @param string $awsRoleArn  AWS role ARN to be used for Federated Identity authentication with Amazon MSK.
     *               Check the Pub/Sub docs for how to set up this role and the required permissions that need to be
     *               attached to it.
     * @param string $gcpServiceAccount  The GCP service account to be used for Federated Identity authentication
     *               with Amazon MSK (via a AssumeRoleWithWebIdentity call for the provided role). The aws_role_arn
     *               must be set up with accounts.google.com:sub equals to this service account number.
     */
    function create_topic_with_aws_msk_ingestion(
        string $projectId,
        string $topicName,
        string $clusterArn,
        string $mskTopic,
        string $awsRoleArn,
        string $gcpServiceAccount
    ): void {
        $pubsub = new PubSubClient([
            'projectId' => $projectId,
        ]);
    
        $topic = $pubsub->createTopic($topicName, [
            'ingestionDataSourceSettings' => [
                'aws_msk' => [
                    'cluster_arn' => $clusterArn,
                    'topic' => $mskTopic,
                    'aws_role_arn' => $awsRoleArn,
                    'gcp_service_account' => $gcpServiceAccount
                ]
            ]
        ]);
    
        printf('Topic created: %s' . PHP_EOL, $topic->name());
    }

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # topic_id = "your-topic-id"
    # cluster_arn =
    # "arn:aws:kafka:us-east-1:111111111111:cluster/cluster-name/11111111-1111-1"
    # msk_topic = "msk-topic-name"
    # aws_role_arn = "arn:aws:iam::111111111111:role/role-name"
    # gcp_service_account = "service-account@project.iam.gserviceaccount.com"
    
    pubsub = Google::Cloud::[Pubsub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud.html).new
    topic_admin = pubsub.topic_admin
    
    topic = topic_admin.create_topic name: pubsub.topic_path(topic_id),
                                     ingestion_data_source_settings: {
                                       aws_msk: {
                                         cluster_arn: cluster_arn,
                                         topic: msk_topic,
                                         aws_role_arn: aws_role_arn,
                                         gcp_service_account: gcp_service_account
                                       }
                                     }
    
    puts "Topic with Aws MSK Ingestion #{topic.name} created."

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
