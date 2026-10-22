---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-create-cloud-storage-subscription/
title: Create a Cloud Storage subscription \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:59.690117+00:00
---

# Create a Cloud Storage subscription  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-create-cloud-storage-subscription/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  Create a Cloud Storage subscription Stay organized with collections  Save and categorize content based on your preferences. 

Create a Cloud Storage subscription where messages published to a topic populates a Cloud Storage bucket

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create Cloud Storage subscriptions](https://docs.cloud.google.com/pubsub/docs/create-cloudstorage-subscription)



## Code sample

### C++

Before trying this sample, follow the C++ setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace pubsub = ::google::cloud::pubsub;
    namespace pubsub_admin = ::google::cloud::pubsub_admin;
    [](pubsub_admin::SubscriptionAdminClient client,
       std::string const& project_id, std::string const& topic_id,
       std::string const& subscription_id, std::string const& bucket) {
      google::pubsub::v1::Subscription request;
      request.set_name(
          pubsub::Subscription(project_id, subscription_id).FullName());
      request.set_topic(pubsub::Topic(project_id, topic_id).FullName());
      request.mutable_cloud_storage_config()->set_bucket(bucket);
      auto sub = client.CreateSubscription(request);
      if (!sub) {
        if (sub.status().code() == google::cloud::StatusCode::kAlreadyExists) {
          std::cout << "The subscription already exists\n";
          return;
        }
        throw std::move(sub).status();
      }
    
      std::cout << "The subscription was successfully created: "
                << sub->DebugString() << "\n";
    }

### C#

Before trying this sample, follow the C# setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using System;
    
    public class CreateCloudStorageSubscriptionSample
    {
        public Subscription CreateCloudStorageSubscription(string projectId, string topicId, string subscriptionId,
            string bucket, string filenamePrefix, string filenameSuffix, TimeSpan maxDuration)
        {
            [SubscriberServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html) subscriber = [SubscriberServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html#Google_Cloud_PubSub_V1_SubscriberServiceApiClient_Create)();
            [TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html) topicName = [TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html).[FromProjectTopic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html#Google_Cloud_PubSub_V1_TopicName_FromProjectTopic_System_String_System_String_)(projectId, topicId);
            [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html) subscriptionName = [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html).[FromProjectSubscription](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html#Google_Cloud_PubSub_V1_SubscriptionName_FromProjectSubscription_System_String_System_String_)(projectId, subscriptionId);
    
            var subscriptionRequest = new [Subscription](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Subscription.html)
            {
                SubscriptionName = subscriptionName,
                TopicAsTopicName = topicName,
                CloudStorageConfig = new [CloudStorageConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.CloudStorageConfig.html)
                {
                    Bucket = bucket,
                    FilenamePrefix = filenamePrefix,
                    FilenameSuffix = filenameSuffix,
                    MaxDuration = [Duration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html).[FromTimeSpan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html#Google_Protobuf_WellKnownTypes_Duration_FromTimeSpan_System_TimeSpan_)(maxDuration)
                }
            };
            var subscription = subscriber.[CreateSubscription](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html#Google_Cloud_PubSub_V1_SubscriberServiceApiClient_CreateSubscription_Google_Cloud_PubSub_V1_Subscription_Google_Api_Gax_Grpc_CallSettings_)(subscriptionRequest);
            return subscription;
        }
    }

### Go

Before trying this sample, follow the Go setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://godoc.org/cloud.google.com/go/pubsub). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/pubsub/v2"
    	"cloud.google.com/go/pubsub/v2/apiv1/pubsubpb"
    	"google.golang.org/protobuf/types/known/durationpb"
    )
    
    // createCloudStorageSubscription creates a Pub/Sub subscription that exports messages to Cloud Storage.
    func createCloudStorageSubscription(w io.Writer, projectID, topic, subscription, bucket string) error {
    	// projectID := "my-project-id"
    	// topic := "projects/my-project-id/topics/my-topic"
    	// subscription := "projects/my-project/subscriptions/my-sub"
    	// bucket := "my-bucket" // bucket must not have the gs:// prefix
    	ctx := context.Background()
    	client, err := pubsub.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	sub, err := client.SubscriptionAdminClient.CreateSubscription(ctx, &pubsubpb.Subscription{
    		Name:  subscription,
    		Topic: topic,
    		CloudStorageConfig: &pubsubpb.CloudStorageConfig{
    			Bucket:         bucket,
    			FilenamePrefix: "log_events_",
    			FilenameSuffix: ".avro",
    			OutputFormat: &pubsubpb.CloudStorageConfig_AvroConfig_{
    				AvroConfig: &pubsubpb.CloudStorageConfig_AvroConfig{
    					WriteMetadata: true,
    				},
    			},
    			MaxDuration: durationpb.New(1 * time.Minute),
    			MaxBytes:    1e8,
    		},
    	})
    	if err != nil {
    		return fmt.Errorf("failed to create cloud storage sub: %w", err)
    	}
    	fmt.Fprintf(w, "Created Cloud Storage subscription: %v\n", sub)
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.pubsub.v1.[SubscriptionAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html);
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import com.google.pubsub.v1.[CloudStorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.CloudStorageConfig.html);
    import com.google.pubsub.v1.[ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html);
    import com.google.pubsub.v1.[ProjectTopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectTopicName.html);
    import com.google.pubsub.v1.[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Subscription.html);
    import java.io.IOException;
    
    public class CreateCloudStorageSubscriptionExample {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String topicId = "your-topic-id";
        String subscriptionId = "your-subscription-id";
        String bucket = "your-bucket";
        String filenamePrefix = "log_events_";
        String filenameSuffix = ".text";
        [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html) maxDuration = [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(300).build();
    
        createCloudStorageSubscription(
            projectId, topicId, subscriptionId, bucket, filenamePrefix, filenameSuffix, maxDuration);
      }
    
      public static void createCloudStorageSubscription(
          String projectId,
          String topicId,
          String subscriptionId,
          String bucket,
          String filenamePrefix,
          String filenameSuffix,
          [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html) maxDuration)
          throws IOException {
        try ([SubscriptionAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html) subscriptionAdminClient = [SubscriptionAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html).create()) {
    
          [ProjectTopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectTopicName.html) topicName = [ProjectTopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectTopicName.html).of(projectId, topicId);
          [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html) subscriptionName =
              [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html).of(projectId, subscriptionId);
    
          [CloudStorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.CloudStorageConfig.html) cloudStorageConfig =
              [CloudStorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.CloudStorageConfig.html).newBuilder()
                  .setBucket(bucket)
                  .[setFilenamePrefix](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.CloudStorageConfig.Builder.html#com_google_pubsub_v1_CloudStorageConfig_Builder_setFilenamePrefix_java_lang_String_)(filenamePrefix)
                  .[setFilenameSuffix](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.CloudStorageConfig.Builder.html#com_google_pubsub_v1_CloudStorageConfig_Builder_setFilenameSuffix_java_lang_String_)(filenameSuffix)
                  .[setMaxDuration](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.CloudStorageConfig.Builder.html#com_google_pubsub_v1_CloudStorageConfig_Builder_setMaxDuration_com_google_protobuf_Duration_)(maxDuration)
                  .build();
    
          [Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Subscription.html) subscription =
              subscriptionAdminClient.createSubscription(
                  [Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Subscription.html).newBuilder()
                      .setName(subscriptionName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html#com_google_pubsub_v1_ProjectSubscriptionName_toString__)())
                      .setTopic(topicName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectTopicName.html#com_google_pubsub_v1_ProjectTopicName_toString__)())
                      .[setCloudStorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Subscription.Builder.html#com_google_pubsub_v1_Subscription_Builder_setCloudStorageConfig_com_google_pubsub_v1_CloudStorageConfig_)(cloudStorageConfig)
                      .build());
    
          System.out.println("Created a CloudStorage subscription: " + subscription.getAllFields());
        }
      }
    }

### PHP

Before trying this sample, follow the PHP setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/latest/pubsub/pubsubclient). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\PubSub\PubSubClient;
    
    /**
     * Creates a Pub/Sub GCS subscription.
     *
     * @param string $projectId  The Google project ID.
     * @param string $topicName  The Pub/Sub topic name.
     * @param string $subscriptionName  The Pub/Sub subscription name.
     * @param string $bucket The Cloud Storage bucket name without any prefix like "gs://".
     */
    function create_cloud_storage_subscription($projectId, $topicName, $subscriptionName, $bucket)
    {
        $pubsub = new PubSubClient([
            'projectId' => $projectId,
        ]);
        $topic = $pubsub->topic($topicName);
        $subscription = $topic->subscription($subscriptionName);
        $config = ['bucket' => $bucket];
        $subscription->create([
            'cloudStorageConfig' => $config
        ]);
    
        printf('Subscription created: %s' . PHP_EOL, $subscription->name());
    }

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # topic_id        = "your-topic-id"
    # subscription_id = "your-subscription-id"
    # bucket = "your-bucket"
    
    pubsub = Google::Cloud::[Pubsub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud.html).new
    subscription_admin = pubsub.subscription_admin
    
    subscription = subscription_admin.create_subscription \
      name: pubsub.subscription_path(subscription_id),
      topic: pubsub.topic_path(topic_id),
      cloud_storage_config: {
        bucket: bucket
      }
    
    puts "Cloud storage subscription #{subscription_id} created."

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
