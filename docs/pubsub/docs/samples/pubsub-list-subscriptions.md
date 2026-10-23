---
url: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-list-subscriptions/
title: List subscriptions in project \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:04:01.393094+00:00
---

# List subscriptions in project  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/samples/pubsub-list-subscriptions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/docs/samples)



#  List subscriptions in project Stay organized with collections  Save and categorize content based on your preferences. 

Lists subscriptions in a project.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [List subscriptions](https://docs.cloud.google.com/pubsub/docs/list-subscriptions)



## Code sample

### C++

Before trying this sample, follow the C++ setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace pubsub_admin = ::google::cloud::pubsub_admin;
    [](pubsub_admin::SubscriptionAdminClient client,
       std::string const& project_id) {
      int count = 0;
      google::pubsub::v1::ListSubscriptionsRequest request;
      request.set_project(google::cloud::Project(project_id).FullName());
      for (auto& subscription : client.ListSubscriptions(request)) {
        if (!subscription) throw std::move(subscription).status();
        std::cout << "Subscription Name: " << subscription->name() << "\n";
        ++count;
      }
      if (count == 0) {
        std::cout << "No subscriptions found in project " << project_id << "\n";
      }
    }

### C#

Before trying this sample, follow the C# setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
    using System.Collections.Generic;
    
    public class ListSubscriptionsSample
    {
        public IEnumerable<Subscription> ListSubscriptions(string projectId)
        {
            [SubscriberServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html) subscriber = [SubscriberServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html#Google_Cloud_PubSub_V1_SubscriberServiceApiClient_Create)();
            [ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html) projectName = [ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html).[FromProject](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html#Google_Api_Gax_ResourceNames_ProjectName_FromProject_System_String_)(projectId);
            var subscriptions = subscriber.[ListSubscriptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html#Google_Cloud_PubSub_V1_SubscriberServiceApiClient_ListSubscriptions_Google_Api_Gax_ResourceNames_ProjectName_System_String_System_Nullable_System_Int32__Google_Api_Gax_Grpc_CallSettings_)(projectName);
            return subscriptions;
        }
    }

### Go

Before trying this sample, follow the Go setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://godoc.org/cloud.google.com/go/pubsub). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    
    	"cloud.google.com/go/pubsub/v2"
    	"cloud.google.com/go/pubsub/v2/apiv1/pubsubpb"
    	"google.golang.org/api/iterator"
    )
    
    func list(projectID string) ([]*pubsubpb.Subscription, error) {
    	// projectID := "my-project-id"
    	ctx := context.Background()
    	client, err := pubsub.NewClient(ctx, projectID)
    	if err != nil {
    		return nil, fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	var subs []*pubsubpb.Subscription
    	req := &pubsubpb.ListSubscriptionsRequest{
    		Project: fmt.Sprintf("projects/%s", projectID),
    	}
    	it := client.SubscriptionAdminClient.ListSubscriptions(ctx, req)
    	for {
    		s, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return nil, fmt.Errorf("Next: %w", err)
    		}
    		subs = append(subs, s)
    	}
    	return subs, nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.pubsub.v1.[SubscriptionAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html);
    import com.google.pubsub.v1.[ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectName.html);
    import com.google.pubsub.v1.[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Subscription.html);
    import java.io.IOException;
    
    public class ListSubscriptionsInProjectExample {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
    
        listSubscriptionInProjectExample(projectId);
      }
    
      public static void listSubscriptionInProjectExample(String projectId) throws IOException {
        try ([SubscriptionAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html) subscriptionAdminClient = [SubscriptionAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html).create()) {
          [ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectName.html) projectName = [ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectName.html).of(projectId);
          for ([Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Subscription.html) subscription :
              subscriptionAdminClient.listSubscriptions(projectName).iterateAll()) {
            System.out.println(subscription.getName());
          }
          System.out.println("Listed all the subscriptions in the project.");
        }
      }
    }

### PHP

Before trying this sample, follow the PHP setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/latest/pubsub/pubsubclient). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\PubSub\PubSubClient;
    
    /**
     * Lists all Pub/Sub subscriptions.
     *
     * @param string $projectId  The Google project ID.
     */
    function list_subscriptions($projectId)
    {
        $pubsub = new PubSubClient([
            'projectId' => $projectId,
        ]);
        foreach ($pubsub->subscriptions() as $subscription) {
            printf('Subscription: %s' . PHP_EOL, $subscription->name());
        }
    }

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Pub/Sub quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 

To authenticate to Pub/Sub, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    pubsub = Google::Cloud::[PubSub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html)
    subscription_admin = pubsub.[subscription_admin](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html)
    
    subscriptions = subscription_admin.list_subscriptions \
      project: pubsub.project_path
    
    puts "Subscriptions:"
    subscriptions.each do |subscription|
      puts subscription.name
    end

### Rust
    
    
    use google_cloud_gax::paginator::ItemPaginator;
    use google_cloud_pubsub::client::SubscriptionAdmin;
    
    pub async fn sample(client: &SubscriptionAdmin, project: &str) -> anyhow::Result<()> {
        let mut subscriptions = client
            .list_subscriptions()
            .set_project(format!("projects/{}", project))
            .by_item();
    
        println!("listing subscriptions");
        while let Some(subscription) = subscriptions.next().await.transpose()? {
            println!("{subscription:?}");
        }
        println!("DONE");
        Ok(())
    }

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsub). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
