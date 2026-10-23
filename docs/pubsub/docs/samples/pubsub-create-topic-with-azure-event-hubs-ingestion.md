---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-create-topic-with-azure-event-hubs-ingestion/
title: Create topic with Azure Event Hubs ingestion \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:20.896912+00:00
---

# Create topic with Azure Event Hubs ingestion  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-create-topic-with-azure-event-hubs-ingestion/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  Create topic with Azure Event Hubs ingestion Stay organized with collections  Save and categorize content based on your preferences. 

Create topic with Azure Event Hubs ingestion

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create an Azure Event Hubs import topic](https://docs.cloud.google.com/pubsub/docs/create-azure-event-hub-import-topic)



## Code sample

### C++

Before trying this sample, follow the C++ setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace pubsub = ::google::cloud::pubsub;
    namespace pubsub_admin = ::google::cloud::pubsub_admin;
    [](pubsub_admin::TopicAdminClient client, std::string project_id,
       std::string topic_id, std::string const& resource_group,
       std::string const& event_hubs_namespace, std::string const& event_hub,
       std::string const& client_id, std::string const& tenant_id,
       std::string const& subscription_id,
       std::string const& gcp_service_account) {
      google::pubsub::v1::Topic request;
      request.set_name(
          pubsub::Topic(std::move(project_id), std::move(topic_id)).FullName());
      auto* azure_event_hubs = request.mutable_ingestion_data_source_settings()
                                   ->mutable_azure_event_hubs();
      azure_event_hubs->set_resource_group(resource_group);
      azure_event_hubs->set_namespace_(event_hubs_namespace);
      azure_event_hubs->set_event_hub(event_hub);
      azure_event_hubs->set_client_id(client_id);
      azure_event_hubs->set_tenant_id(tenant_id);
      azure_event_hubs->set_subscription_id(subscription_id);
      azure_event_hubs->set_gcp_service_account(gcp_service_account);
    
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
    
    public class CreateTopicWithAzureEventHubsIngestionSample
    {
        public Topic CreateTopicWithAzureEventHubsIngestion(string projectId, string topicId, string resourceGroup, string nameSpace, string eventHub, string clientId, string tenantId, string subscriptionId, string gcpServiceAccount)
        {
            // Define settings for Azure Event Hubs ingestion
            [IngestionDataSourceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.IngestionDataSourceSettings.html) ingestionDataSourceSettings = new [IngestionDataSourceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.IngestionDataSourceSettings.html)
            {
                AzureEventHubs = new IngestionDataSourceSettings.Types.AzureEventHubs
                {
                    ResourceGroup = resourceGroup,
                    Namespace = nameSpace,
                    EventHub = eventHub,
                    ClientId = clientId,
                    TenantId = tenantId,
                    SubscriptionId = subscriptionId,
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
    
    func createTopicWithAzureEventHubsIngestion(w io.Writer, projectID, topicID, resourceGroup, namespace, eventHub, clientID, tenantID, subID, gcpSA string) error {
    	// projectID := "my-project-id"
    	// topicID := "my-topic"
    
    	// // Azure Event Hubs ingestion settings.
    	// resourceGroup := "resource-group"
    	// namespace := "namespace"
    	// eventHub := "event-hub"
    	// clientID := "client-id"
    	// tenantID := "tenant-id"
    	// subID := "subscription-id"
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
    			Source: &pubsubpb.IngestionDataSourceSettings_AzureEventHubs_{
    				AzureEventHubs: &pubsubpb.IngestionDataSourceSettings_AzureEventHubs{
    					ResourceGroup:     resourceGroup,
    					Namespace:         namespace,
    					EventHub:          eventHub,
    					ClientId:          clientID,
    					TenantId:          tenantID,
    					SubscriptionId:    subID,
    					GcpServiceAccount: gcpSA,
    				},
    			},
    		},
    	}
    	topic, err := client.TopicAdminClient.CreateTopic(ctx, topicpb)
    	if err != nil {
    		return fmt.Errorf("CreateTopic: %w", err)
    	}
    	fmt.Fprintf(w, "Created topic with Azure Event Hubs ingestion: %v\n", topic)
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
    
    public class CreateTopicWithAzureEventHubsIngestionExample {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String topicId = "your-topic-id";
        // Azure Event Hubs ingestion settings.
        String resourceGroup = "resource-group";
        String namespace = "namespace";
        String eventHub = "event-hub";
        String clientId = "client-id";
        String tenantId = "tenant-id";
        String subscriptionId = "subscription-id";
        String gcpServiceAccount = "gcp-service-account";
    
        createTopicWithAzureEventHubsIngestionExample(
            projectId,
            topicId,
            resourceGroup,
            namespace,
            eventHub,
            clientId,
            tenantId,
            subscriptionId,
            gcpServiceAccount);
      }
    
      public static void createTopicWithAzureEventHubsIngestionExample(
          String projectId,
          String topicId,
          String resourceGroup,
          String namespace,
          String eventHub,
          String clientId,
          String tenantId,
          String subscriptionId,
          String gcpServiceAccount)
          throws IOException {
        try ([TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html) topicAdminClient = [TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html).create()) {
          [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) topicName = [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html).of(projectId, topicId);
    
          [IngestionDataSourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.html).[AzureEventHubs](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.AzureEventHubs.html) azureEventHubs =
              [IngestionDataSourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.html).AzureEventHubs.newBuilder()
                  .[setResourceGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.AzureEventHubs.Builder.html#com_google_pubsub_v1_IngestionDataSourceSettings_AzureEventHubs_Builder_setResourceGroup_java_lang_String_)(resourceGroup)
                  .setNamespace(namespace)
                  .setEventHub(eventHub)
                  .setClientId(clientId)
                  .[setTenantId](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.AzureEventHubs.Builder.html#com_google_pubsub_v1_IngestionDataSourceSettings_AzureEventHubs_Builder_setTenantId_java_lang_String_)(tenantId)
                  .[setSubscriptionId](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.AzureEventHubs.Builder.html#com_google_pubsub_v1_IngestionDataSourceSettings_AzureEventHubs_Builder_setSubscriptionId_java_lang_String_)(subscriptionId)
                  .setGcpServiceAccount(gcpServiceAccount)
                  .build();
          [IngestionDataSourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.html) ingestionDataSourceSettings =
              [IngestionDataSourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.html).newBuilder().[setAzureEventHubs](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.IngestionDataSourceSettings.Builder.html#com_google_pubsub_v1_IngestionDataSourceSettings_Builder_setAzureEventHubs_com_google_pubsub_v1_IngestionDataSourceSettings_AzureEventHubs_)(azureEventHubs).build();
    
          [Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html) topic =
              topicAdminClient.createTopic(
                  [Topic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.html).newBuilder()
                      .setName(topicName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html#com_google_pubsub_v1_TopicName_toString__)())
                      .[setIngestionDataSourceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Topic.Builder.html#com_google_pubsub_v1_Topic_Builder_setIngestionDataSourceSettings_com_google_pubsub_v1_IngestionDataSourceSettings_)(ingestionDataSourceSettings)
                      .build());
    
          System.out.println(
              "Created topic with Azure Event Hubs ingestion settings: " + topic.getAllFields());
        }
      }
    }

### PHP

Before trying this sample, follow the PHP setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/latest/pubsub/pubsubclient). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\PubSub\PubSubClient;
    
    /**
     * Creates a Pub/Sub topic with Azure Event Hubs ingestion.
     *
     * @param string $projectId  The Google project ID.
     * @param string $topicName  The Pub/Sub topic name.
     * @param string $resourceGroup  The name of the resource group within the azure subscription.
     * @param string $namespace  The name of the Event Hubs namespace.
     * @param string $eventHub  The name of the Event Hub.
     * @param string $clientId  The client id of the Azure application that is being used to authenticate Pub/Sub.
     * @param string $tenantId  The tenant id of the Azure application that is being used to authenticate Pub/Sub.
     * @param string $subscriptionId  The Azure subscription id.
     * @param string $gcpServiceAccount  The GCP service account to be used for Federated Identity authentication.
     */
    function create_topic_with_azure_event_hubs_ingestion(
        string $projectId,
        string $topicName,
        string $resourceGroup,
        string $namespace,
        string $eventHub,
        string $clientId,
        string $tenantId,
        string $subscriptionId,
        string $gcpServiceAccount
    ): void {
        $pubsub = new PubSubClient([
            'projectId' => $projectId,
        ]);
    
        $topic = $pubsub->createTopic($topicName, [
            'ingestionDataSourceSettings' => [
                'azure_event_hubs' => [
                    'resource_group' => $resourceGroup,
                    'namespace' => $namespace,
                    'event_hub' => $eventHub,
                    'client_id' => $clientId,
                    'tenant_id' => $tenantId,
                    'subscription_id' => $subscriptionId,
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
    # resource_group = "resource-group"
    # namespace = "namespace"
    # event_hub = "event-hub"
    # client_id = "11111111-1111-1111-1111-11111111111"
    # tenant_id = "22222222-2222-2222-2222-222222222222"
    # subscription_id = "33333333-3333-3333-3333-333333333333"
    # gcp_service_account = "service-account@project.iam.gserviceaccount.com"
    
    pubsub = Google::Cloud::[Pubsub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud.html).new
    topic_admin = pubsub.topic_admin
    
    topic = topic_admin.create_topic name: pubsub.topic_path(topic_id),
                                     ingestion_data_source_settings: {
                                       azure_event_hubs: {
                                         resource_group: resource_group,
                                         namespace: namespace,
                                         event_hub: event_hub,
                                         client_id: client_id,
                                         tenant_id: tenant_id,
                                         subscription_id: subscription_id,
                                         gcp_service_account: gcp_service_account
                                       }
                                     }
    
    puts "Topic with Azure Event Hubs Ingestion #{topic.name} created."

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
