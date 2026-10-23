---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-create-topic-with-confluent-cloud-ingestion/
title: Create topic with Confluent Cloud ingestion \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:03.219586+00:00
---

# Create topic with Confluent Cloud ingestion  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-create-topic-with-confluent-cloud-ingestion/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  Create topic with Confluent Cloud ingestion Stay organized with collections  Save and categorize content based on your preferences. 

Create topic with Confluent Cloud ingestion

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create a Confluent Cloud import topic](https://docs.cloud.google.com/pubsub/docs/create-confluent-cloud-import-topic)



## Code sample

### C++

Before trying this sample, follow the C++ setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace pubsub = ::google::cloud::pubsub;
    namespace pubsub_admin = ::google::cloud::pubsub_admin;
    [](pubsub_admin::TopicAdminClient client, std::string project_id,
       std::string topic_id, std::string const& bootstrap_server,
       std::string const& cluster_id, std::string const& confluent_topic,
       std::string const& identity_pool_id,
       std::string const& gcp_service_account) {
      google::pubsub::v1::Topic request;
      request.set_name(
          pubsub::Topic(std::move(project_id), std::move(topic_id)).FullName());
      auto* confluent_cloud = request.mutable_ingestion_data_source_settings()
                                  ->mutable_confluent_cloud();
      confluent_cloud->set_bootstrap_server(bootstrap_server);
      confluent_cloud->set_cluster_id(cluster_id);
      confluent_cloud->set_topic(confluent_topic);
      confluent_cloud->set_identity_pool_id(identity_pool_id);
      confluent_cloud->set_gcp_service_account(gcp_service_account);
    
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
    
    public class CreateTopicWithConfluentCloudIngestionSample
    {
        public Topic CreateTopicWithConfluentCloudIngestion(string projectId, string topicId, string bootstrapServer, string clusterId, string confluentTopic, string identityPoolId, string gcpServiceAccount)
        {
            // Define settings for Confluent Cloud ingestion
            [IngestionDataSourceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.IngestionDataSourceSettings.html) ingestionDataSourceSettings = new [IngestionDataSourceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.IngestionDataSourceSettings.html)
            {
                ConfluentCloud = new IngestionDataSourceSettings.Types.ConfluentCloud
                {
                    BootstrapServer = bootstrapServer,
                    ClusterId = clusterId,
                    Topic = confluentTopic,
                    IdentityPoolId = identityPoolId,
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
    
    func createTopicWithConfluentCloudIngestion(w io.Writer, projectID, topicID, bootstrapServer, clusterID, confluentTopic, poolID, gcpSA string) error {
    	// projectID := "my-project-id"
    	// topicID := "my-topic"
    
    	// // Confluent Cloud ingestion settings.
    	// bootstrapServer := "bootstrap-server"
    	// clusterID := "cluster-id"
    	// confluentTopic := "confluent-topic"
    	// poolID := "identity-pool-id"
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
    			Source: &pubsubpb.IngestionDataSourceSettings_ConfluentCloud_{
    				ConfluentCloud: &pubsubpb.IngestionDataSourceSettings_ConfluentCloud{
    					BootstrapServer:   bootstrapServer,
    					ClusterId:         clusterID,
    					Topic:             confluentTopic,
    					IdentityPoolId:    poolID,
    					GcpServiceAccount: gcpSA,
    				},
    			},
    		},
    	}
    	topic, err := client.TopicAdminClient.CreateTopic(ctx, topicpb)
    	if err != nil {
    		return fmt.Errorf("CreateTopic: %w", err)
    	}
    	fmt.Fprintf(w, "Created topic with Confluent Cloud ingestion: %v\n", topic)
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
    
    public class CreateTopicWithConfluentCloudIngestionExample {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String topicId = "your-topic-id";
        // Confluent Cloud ingestion settings.
        String bootstrapServer = "bootstrap-server";
        String clusterId = "cluster-id";
        String confluentTopic = "confluent-topic";
        String identityPoolId = "identity-pool-id";
        String gcpServiceAccount = "gcp-service-account";
    
        createTopicWithConfluentCloudIngestionExample(
            projectId,
            topicId,
            bootstrapServer,
            clusterId,
            confluentTopic,
            identityPoolId,
            gcpServiceAccount);
      }
    
      public static void createTopicWithConfluentCloudIngestionExample(
          String projectId,
          String topicId,
          String bootstrapServer,
          String clusterId,
          String confluentTopic,
          String identityPoolId,
          String gcpServiceAccount)
          throws IOException {
        try ([TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html) topicAdminClient = [TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html).create()) {
          [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) topicName = [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html).of(projectId, topicId);
    
          [IngestionDataSourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.html).[ConfluentCloud](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.ConfluentCloud.html) confluentCloud =
              [IngestionDataSourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.html).ConfluentCloud.newBuilder()
                  .[setBootstrapServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.ConfluentCloud.Builder.html#com_google_pubsub_v1_IngestionDataSourceSettings_ConfluentCloud_Builder_setBootstrapServer_java_lang_String_)(bootstrapServer)
                  .setClusterId(clusterId)
                  .setTopic(confluentTopic)
                  .[setIdentityPoolId](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.ConfluentCloud.Builder.html#com_google_pubsub_v1_IngestionDataSourceSettings_ConfluentCloud_Builder_setIdentityPoolId_java_lang_String_)(identityPoolId)
                  .setGcpServiceAccount(gcpServiceAccount)
                  .build();
          [IngestionDataSourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.html) ingestionDataSourceSettings =
              [IngestionDataSourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.html).newBuilder().[setConfluentCloud](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.Builder.html#com_google_pubsub_v1_IngestionDataSourceSettings_Builder_setConfluentCloud_com_google_pubsub_v1_IngestionDataSourceSettings_ConfluentCloud_)(confluentCloud).build();
    
          [Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html) topic =
              topicAdminClient.createTopic(
                  [Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html).newBuilder()
                      .setName(topicName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html#com_google_pubsub_v1_TopicName_toString__)())
                      .[setIngestionDataSourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.Builder.html#com_google_pubsub_v1_Topic_Builder_setIngestionDataSourceSettings_com_google_pubsub_v1_IngestionDataSourceSettings_)(ingestionDataSourceSettings)
                      .build());
    
          System.out.println(
              "Created topic with Confluent Cloud ingestion settings: " + topic.getAllFields());
        }
      }
    }

### PHP

Before trying this sample, follow the PHP setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/latest/pubsub/pubsubclient). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\PubSub\PubSubClient;
    
    /**
     * Creates a Pub/Sub topic with Confluent Cloud ingestion.
     *
     * @param string $projectId  The Google project ID.
     * @param string $topicName  The Pub/Sub topic name.
     * @param string $bootstrapServer  The address of the bootstrap server. The format is url:port.
     * @param string $clusterId  The id of the cluster.
     * @param string $confluentTopic  The name of the topic in the Confluent Cloud cluster that Pub/Sub will import from.
     * @param string $identityPoolId  The id of the identity pool to be used for Federated Identity authentication with Confluent Cloud.
     * @param string $gcpServiceAccount  The GCP service account to be used for Federated Identity authentication with identity_pool_id.
     */
    function create_topic_with_confluent_cloud_ingestion(
        string $projectId,
        string $topicName,
        string $bootstrapServer,
        string $clusterId,
        string $confluentTopic,
        string $identityPoolId,
        string $gcpServiceAccount
    ): void {
        $pubsub = new PubSubClient([
            'projectId' => $projectId,
        ]);
    
        $topic = $pubsub->createTopic($topicName, [
            'ingestionDataSourceSettings' => [
                'confluent_cloud' => [
                    'bootstrap_server' => $bootstrapServer,
                    'cluster_id' => $clusterId,
                    'topic' => $confluentTopic,
                    'identity_pool_id' => $identityPoolId,
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
    # bootstrap_server = "bootstrap-server-id.us-south1.gcp.confluent.cloud:9092"
    # cluster_id = "cluster-id"
    # confluent_topic = "confluent-topic-name"
    # identity_pool_id = "identity-pool-id"
    # gcp_service_account = "service-account@project.iam.gserviceaccount.com"
    
    pubsub = Google::Cloud::[Pubsub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud.html).new
    topic_admin = pubsub.topic_admin
    
    topic = topic_admin.create_topic name: pubsub.topic_path(topic_id),
                                     ingestion_data_source_settings: {
                                       confluent_cloud: {
                                         bootstrap_server: bootstrap_server,
                                         cluster_id: cluster_id,
                                         topic: confluent_topic,
                                         identity_pool_id: identity_pool_id,
                                         gcp_service_account: gcp_service_account
                                       }
                                     }
    
    puts "Topic with Confluent Cloud Ingestion #{topic.name} created."

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
