---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-dead-letter-update-subscription/
title: Update `DeadLetterPolicy` on subscription \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:21:11.046334+00:00
---

# Update `DeadLetterPolicy` on subscription  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-dead-letter-update-subscription/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  Update `DeadLetterPolicy` on subscription Stay organized with collections  Save and categorize content based on your preferences. 

Updates the `DeadLetterPolicy` on a subscription.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Dead-letter topics](https://docs.cloud.google.com/pubsub/docs/dead-letter-topics)



## Code sample

### C++

Before trying this sample, follow the C++ setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace pubsub_admin = ::google::cloud::pubsub_admin;
    namespace pubsub = ::google::cloud::pubsub;
    [](pubsub_admin::SubscriptionAdminClient client,
       std::string const& project_id, std::string const& subscription_id,
       std::string const& dead_letter_topic_id,
       int dead_letter_delivery_attempts) {
      google::pubsub::v1::UpdateSubscriptionRequest request;
      request.mutable_subscription()->set_name(
          pubsub::Subscription(project_id, subscription_id).FullName());
      request.mutable_subscription()
          ->mutable_dead_letter_policy()
          ->set_dead_letter_topic(
              pubsub::Topic(project_id, dead_letter_topic_id).FullName());
      request.mutable_subscription()
          ->mutable_dead_letter_policy()
          ->set_max_delivery_attempts(dead_letter_delivery_attempts);
      *request.mutable_update_mask()->add_paths() = "dead_letter_policy";
      auto sub = client.UpdateSubscription(request);
      if (!sub) throw std::move(sub).status();
    
      std::cout << "The subscription has been updated to: " << sub->DebugString()
                << "\n";
    
      std::cout << "It will forward dead letter messages to: "
                << sub->dead_letter_policy().dead_letter_topic() << "\n";
    
      std::cout << "After " << sub->dead_letter_policy().max_delivery_attempts()
                << " delivery attempts.\n";
    }

### C#

Before trying this sample, follow the C# setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    
    public class UpdateDeadLetterPolicySample
    {
        public Subscription UpdateDeadLetterPolicy(string projectId, string topicId, string subscriptionId, string deadLetterTopicId)
        {
            [SubscriberServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html) subscriber = [SubscriberServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html#Google_Cloud_PubSub_V1_SubscriberServiceApiClient_Create)();
            // This is an existing topic that the subscription with dead letter policy is attached to.
            [TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html) topicName = [TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html).[FromProjectTopic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html#Google_Cloud_PubSub_V1_TopicName_FromProjectTopic_System_String_System_String_)(projectId, topicId);
            // This is an existing subscription with a dead letter policy.
            [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html) subscriptionName = [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html).[FromProjectSubscription](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html#Google_Cloud_PubSub_V1_SubscriptionName_FromProjectSubscription_System_String_System_String_)(projectId, subscriptionId);
            // This is an existing dead letter topic that the subscription with dead letter policy forwards
            // dead letter messages to.
            var deadLetterTopic = [TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html).[FromProjectTopic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html#Google_Cloud_PubSub_V1_TopicName_FromProjectTopic_System_String_System_String_)(projectId, deadLetterTopicId).ToString();
    
    
            // Construct the subscription with the dead letter policy you expect to have after the update.
            // Here, values in the required fields (name, topic) help identify the subscription.
            var subscription = new [Subscription](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Subscription.html)
            {
                SubscriptionName = subscriptionName,
                TopicAsTopicName = topicName,
                DeadLetterPolicy = new [DeadLetterPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.DeadLetterPolicy.html)
                {
                    DeadLetterTopic = deadLetterTopic,
                    MaxDeliveryAttempts = 20,
                }
            };
    
            var request = new [UpdateSubscriptionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.UpdateSubscriptionRequest.html)
            {
                Subscription = subscription,
                // Construct a field mask to indicate which field to update in the subscription.
                UpdateMask = new [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html) { Paths = { "dead_letter_policy" } }
            };
            var updatedSubscription = subscriber.[UpdateSubscription](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html#Google_Cloud_PubSub_V1_SubscriberServiceApiClient_UpdateSubscription_Google_Cloud_PubSub_V1_Subscription_Google_Protobuf_WellKnownTypes_FieldMask_Google_Api_Gax_Grpc_CallSettings_)(request);
            return updatedSubscription;
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
    
    // updateDeadLetter updates an existing subscription with a dead letter policy.
    func updateDeadLetter(w io.Writer, projectID, subscription, deadLetterTopic string) error {
    	// projectID := "my-project-id"
    	// subID := "projects/my-project-id/subscriptions/my-sub"
    	// deadLetterTopic := "projects/my-project-id/topics/my-dead-letter-topic"
    	ctx := context.Background()
    	client, err := pubsub.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	sub, err := client.SubscriptionAdminClient.UpdateSubscription(ctx, &pubsubpb.UpdateSubscriptionRequest{
    		Subscription: &pubsubpb.Subscription{
    			Name: subscription,
    			DeadLetterPolicy: &pubsubpb.DeadLetterPolicy{
    				MaxDeliveryAttempts: 20,
    				DeadLetterTopic:     deadLetterTopic,
    			},
    		},
    		UpdateMask: &fieldmaskpb.FieldMask{
    			Paths: []string{"dead_letter_policy"},
    		},
    	})
    	if err != nil {
    		return fmt.Errorf("UpdateSubscription: %w", err)
    	}
    	fmt.Fprintf(w, "Updated subscription: %+v\n", sub)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.pubsub.v1.[SubscriptionAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import com.google.pubsub.v1.[DeadLetterPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.DeadLetterPolicy.html);
    import com.google.pubsub.v1.[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Subscription.html);
    import com.google.pubsub.v1.[SubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SubscriptionName.html);
    import com.google.pubsub.v1.[TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html);
    import com.google.pubsub.v1.[UpdateSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.UpdateSubscriptionRequest.html);
    import java.io.IOException;
    
    public class UpdateDeadLetterPolicyExample {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        // This is an existing subscription with a dead letter policy.
        String subscriptionId = "your-subscription-id";
        // This is an existing topic that the subscription with dead letter policy is attached to.
        String topicId = "your-topic-id";
        // This is an existing dead letter topic that the subscription with dead letter policy forwards
        // dead letter messages to.
        String deadLetterTopicId = "your-dead-letter-topic-id";
    
        UpdateDeadLetterPolicyExample.updateDeadLetterPolicyExample(
            projectId, subscriptionId, topicId, deadLetterTopicId);
      }
    
      public static void updateDeadLetterPolicyExample(
          String projectId, String subscriptionId, String topicId, String deadLetterTopicId)
          throws IOException {
        try ([SubscriptionAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html) subscriptionAdminClient = [SubscriptionAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html).create()) {
    
          [SubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SubscriptionName.html) subscriptionName = [SubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SubscriptionName.html).of(projectId, subscriptionId);
    
          System.out.println(
              "Before: " + subscriptionAdminClient.getSubscription(subscriptionName).getAllFields());
    
          [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) topicName = [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html).of(projectId, topicId);
          [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) deadLetterTopicName = [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html).of(projectId, deadLetterTopicId);
    
          // Construct the dead letter policy you expect to have after the update.
          [DeadLetterPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.DeadLetterPolicy.html) deadLetterPolicy =
              [DeadLetterPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.DeadLetterPolicy.html).newBuilder()
                  .[setDeadLetterTopic](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.DeadLetterPolicy.Builder.html#com_google_pubsub_v1_DeadLetterPolicy_Builder_setDeadLetterTopic_java_lang_String_)(deadLetterTopicName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html#com_google_pubsub_v1_TopicName_toString__)())
                  .[setMaxDeliveryAttempts](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.DeadLetterPolicy.Builder.html#com_google_pubsub_v1_DeadLetterPolicy_Builder_setMaxDeliveryAttempts_int_)(20)
                  .build();
    
          // Construct the subscription with the dead letter policy you expect to have
          // after the update. Here, values in the required fields (name, topic) help
          // identify the subscription.
          [Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Subscription.html) subscription =
              [Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Subscription.html).newBuilder()
                  .setName(subscriptionName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SubscriptionName.html#com_google_pubsub_v1_SubscriptionName_toString__)())
                  .setTopic(topicName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html#com_google_pubsub_v1_TopicName_toString__)())
                  .[setDeadLetterPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Subscription.Builder.html#com_google_pubsub_v1_Subscription_Builder_setDeadLetterPolicy_com_google_pubsub_v1_DeadLetterPolicy_)(deadLetterPolicy)
                  .build();
    
          // Construct a field mask to indicate which field to update in the subscription.
          [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) updateMask =
              [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("dead_letter_policy.max_delivery_attempts").build();
    
          [UpdateSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.UpdateSubscriptionRequest.html) request =
              [UpdateSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.UpdateSubscriptionRequest.html).newBuilder()
                  .setSubscription(subscription)
                  .setUpdateMask(updateMask)
                  .build();
    
          [Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Subscription.html) response = subscriptionAdminClient.updateSubscription(request);
    
          System.out.println("After: " + response.getAllFields());
          System.out.println(
              "Max delivery attempts is now "
                  + response.[getDeadLetterPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Subscription.html#com_google_pubsub_v1_Subscription_getDeadLetterPolicy__)().getMaxDeliveryAttempts());
        }
      }
    }

### PHP

Before trying this sample, follow the PHP setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/latest/pubsub/pubsubclient). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\PubSub\PubSubClient;
    
    /**
     * Set the dead letter policy on an existing subscription.
     *
     * @param string $projectId  The Google project ID.
     * @param string $topicName  The Pub/Sub topic name.
     * @param string $deadLetterTopicName The Pub/Sub topic to use for dead letter policy.
     */
    function dead_letter_update_subscription(
        string $projectId,
        string $topicName,
        string $subscriptionName,
        string $deadLetterTopicName
    ): void {
        $pubsub = new PubSubClient([
            'projectId' => $projectId,
        ]);
    
        $topic = $pubsub->topic($topicName);
        $deadLetterTopic = $pubsub->topic($deadLetterTopicName);
    
        $subscription = $topic->subscription($subscriptionName);
        $subscription->update([
            'deadLetterPolicy' => [
                'deadLetterTopic' => $deadLetterTopic
            ]
        ]);
    
        printf(
            'Subscription %s updated with dead letter topic %s' . PHP_EOL,
            $subscription->name(),
            $deadLetterTopic->name()
        );
    }

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # subscription_id       = "your-subscription-id"
    # role                  = "roles/pubsub.publisher"
    # service_account_email =
    # "serviceAccount:account_name@project_name.iam.gserviceaccount.com"
    
    pubsub = Google::Cloud::[PubSub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html)
    subscription_admin = pubsub.[subscription_admin](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html)
    
    subscription = subscription_admin.get_subscription \
      subscription: pubsub.subscription_path(subscription_id)
    subscription.[dead_letter_policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-Subscription.html).[max_delivery_attempts](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-DeadLetterPolicy.html) = 20
    
    subscription_admin.update_subscription subscription: subscription,
                                           update_mask: {
                                             paths: ["dead_letter_policy"]
                                           }
    
    puts "Max delivery attempts is now " \
         "#{subscription.[dead_letter_policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-Subscription.html).[max_delivery_attempts](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-DeadLetterPolicy.html)}."

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
