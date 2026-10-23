---
url: https://docs.cloud.google.com/pubsub/docs/list-subscriptions/
title: List subscriptions \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:03:55.688461+00:00
---

# List subscriptions  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/list-subscriptions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  List subscriptions Stay organized with collections  Save and categorize content based on your preferences. 

You can list the subscriptions in a Google Cloud project with the Google Cloud console, Google Cloud CLI, client library, or Pub/Sub API.

## Before you begin

  * Learn about [subscriptions](https://docs.cloud.google.com/pubsub/docs/subscription-overview).
  * Create one of the following subscriptions, [pull](https://docs.cloud.google.com/pubsub/docs/create-subscription), [push](https://docs.cloud.google.com/pubsub/docs/create-push-subscription), or [BigQuery](https://docs.cloud.google.com/pubsub/docs/create-bigquery-subscription).



## Required roles and permissions

To get the permissions that you need to list subscriptions, ask your administrator to grant you the [Pub/Sub Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to list subscriptions. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to list subscriptions:

  * List subscriptions in a project: `pubsub.subscriptions.list` on the project 
  * List subscriptions in a topic: `pubsub.topics.get` on the topic 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## List the subscriptions in a project

You can list the subscriptions in a Google Cloud project with the Google Cloud console, Google Cloud CLI, client library, or Pub/Sub API.

### Console

To list the subscriptions in a project, go to the **Subscriptions** page.

[Go to Subscriptions](https://console.cloud.google.com/cloudpubsub/subscription)

Your subscriptions are listed in the table on the page.

### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To list the subscriptions in a Google Cloud project, run the [`gcloud pubsub subscriptions list`](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions/list) command:
         
         gcloud pubsub subscriptions list [--project=PROJECT_ID]

By default, this command returns a maximum of 100 results per query. To return more results, use the `--page-size` flag:
         
         gcloud pubsub subscriptions list --page-size=PAGE_SIZE

Replace `PAGE_SIZE` with the maximum number of results to return. The value can't exceed 1000.




### REST

To list subscriptions in a project, use the [`projects.subscriptions.list`](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions/list) method:

Request:

The request must be authenticated with an access token in the `Authorization` header. To obtain an access token for the current Application Default Credentials: [`gcloud auth application-default print-access-token`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token).
    
    
    GET https://pubsub.googleapis.com/v1/projects/PROJECT_ID/subscriptions
    Authorization: Bearer ACCESS_TOKEN
    

Where:

  * PROJECT_ID is your project ID.



Response:
    
    
    {
    "subscriptions": [
    {
      "name": "projects/PROJECT_ID/topics/mysubscription1",
      "topic": "projects/PROJECT_ID/topics/TOPIC_ID",
      "pushConfig": {},
      "ackDeadlineSeconds": 10,
      "retainAckedMessages": true,
      "messageRetentionDuration": "604800s",
      "expirationPolicy": {}
    },
    {
      "name": "projects/PROJECT_ID/topics/mysubscription2",
      "topic": "projects/PROJECT_ID/topics/TOPIC_ID",
      "pushConfig": {
        "pushEndpoint": "https://PROJECT_ID.appspot.com/myhandler",
        "attributes": {
          "x-goog-version": "v1"
        }
      },
      "ackDeadlineSeconds": 10,
      "retainAckedMessages": true,
      "messageRetentionDuration": "604800s",
      "expirationPolicy": {}
    }
    ]
    }

### C++

Before trying this sample, follow the C++ setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 
    
    
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

Before trying this sample, follow the C# setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 
    
    
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

The following sample uses the major version of the Go Pub/Sub client library (v2). If you are still using the v1 library, see [the migration guide to v2](https://github.com/googleapis/google-cloud-go/blob/main/pubsub/MIGRATING.md). To see a list of v1 code samples, see [ the deprecated code samples](https://docs.cloud.google.com/pubsub/docs/samples?language=golang&text=deprecated).

Before trying this sample, follow the Go setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/pubsub/v2).
    
    
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

Before trying this sample, follow the Java setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 
    
    
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

### Node.js

Before trying this sample, follow the Node.js setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 
    
    
    // Imports the Google Cloud client library
    const {PubSub} = require('@google-cloud/pubsub');
    
    // Creates a client; cache this for further use
    const pubSubClient = new PubSub();
    
    async function listSubscriptions() {
      // Lists all subscriptions in the current project
      const [subscriptions] = await pubSubClient.getSubscriptions();
      console.log('Subscriptions:');
      subscriptions.forEach(subscription => console.log(subscription.name));
    }

### Node.ts

Before trying this sample, follow the Node.js setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 
    
    
    // Imports the Google Cloud client library
    import {PubSub, Subscription} from '@google-cloud/pubsub';
    
    // Creates a client; cache this for further use
    const pubSubClient = new PubSub();
    
    async function listSubscriptions() {
      // Lists all subscriptions in the current project
      const [subscriptions] = await pubSubClient.getSubscriptions();
      console.log('Subscriptions:');
      subscriptions.forEach((subscription: Subscription) =>
        console.log(subscription.name),
      );
    }

### PHP

Before trying this sample, follow the PHP setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub PHP API reference documentation](https://cloud.google.com/php/docs/reference/cloud-pubsub/latest). 
    
    
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

### Python

Before trying this sample, follow the Python setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/pubsub/latest). 
    
    
    from google.cloud import pubsub_v1
    
    # TODO(developer)
    # project_id = "your-project-id"
    
    subscriber = pubsub_v1.[SubscriberClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)()
    project_path = f"projects/{project_id}"
    
    # Wrap the subscriber in a 'with' block to automatically call close() to
    # close the underlying gRPC channel when done.
    with subscriber:
        for subscription in subscriber.list_subscriptions(
            request={"project": project_path}
        ):
            print(subscription.name)

### Ruby

The following sample uses Ruby Pub/Sub client library v3. If you are still using the v2 library, see [ the migration guide to v3](https://github.com/googleapis/google-cloud-ruby/blob/main/google-cloud-pubsub/MIGRATION_GUIDE.md). To see a list of Ruby v2 code samples, see [ the deprecated code samples](https://docs.cloud.google.com/pubsub/docs/samples?language=ruby&text=deprecated).

Before trying this sample, follow the Ruby setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 
    
    
    pubsub = Google::Cloud::[PubSub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html)
    subscription_admin = pubsub.[subscription_admin](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html)
    
    subscriptions = subscription_admin.list_subscriptions \
      project: pubsub.project_path
    
    puts "Subscriptions:"
    subscriptions.each do |subscription|
      puts subscription.name
    end

### Rust

Before trying this sample, follow the Rust setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Rust API reference documentation](https://docs.rs/google-cloud-pubsub). 
    
    
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

## List subscriptions to a topic

You can list the subscriptions to a topic with the Google Cloud console, Google Cloud CLI, or Pub/Sub API.

### Console

  1. In the Google Cloud console, go to the **Topics** page. 

[Go to Topics](https://console.cloud.google.com/cloudpubsub/topic)

  2. Select a topic ID to open the **Topic details** page. The **Subscriptions** section of the page includes a list of subscriptions to the topic.



### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To list the subscriptions in a Google Cloud project, run the [`gcloud pubsub topics list-subscriptions`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics/list-subscriptions) command:
         
         gcloud pubsub topics list-subscriptions TOPIC_ID

By default, this command returns a maximum of 100 results per query. To return more results, use the `--page-size` flag:
    
    gcloud pubsub subscriptions list --page-size=PAGE_SIZE

Replace `PAGE_SIZE` with the maximum number of results to return. The value can't exceed 1000.




### REST

To list subscriptions in a topic, use the [`projects.subscriptions.list`](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions/list) method:

Request:

The request must be authenticated with an access token in the `Authorization` header. To obtain an access token for the current Application Default Credentials: [`gcloud auth application-default print-access-token`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token).
    
    
    GET https://pubsub.googleapis.com/v1/projects/PROJECT_ID/topics/TOPIC_ID/subscriptions
    Authorization: Bearer ACCESS_TOKEN
    

Where:

  * PROJECT_ID is your project ID.
  * TOPIC_ID is your topic ID.



Response:
    
    
    {
    "subscriptions": [
    "projects/PROJECT_ID/subscriptions/mysubscription1",
    "projects/PROJECT_ID/subscriptions/mysubscription2"
    ]
    }

### C++

Before trying this sample, follow the C++ setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 
    
    
    namespace pubsub_admin = ::google::cloud::pubsub_admin;
    namespace pubsub = ::google::cloud::pubsub;
    [](pubsub_admin::TopicAdminClient client, std::string const& project_id,
       std::string const& topic_id) {
      auto const topic = pubsub::Topic(project_id, topic_id);
      std::cout << "Subscription list for topic " << topic << ":\n";
      for (auto& name : client.ListTopicSubscriptions(topic.FullName())) {
        if (!name) throw std::move(name).status();
        std::cout << "  " << *name << "\n";
      }
    }

### C#

Before trying this sample, follow the C# setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 
    
    
    using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
    using System.Collections.Generic;
    
    public class ListSubscriptionsInTopicSample
    {
        public IEnumerable<string> ListSubscriptionsInTopic(string projectId, string topicId)
        {
            [PublisherServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html) publisher = [PublisherServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html#Google_Cloud_PubSub_V1_PublisherServiceApiClient_Create)();
            [TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html) topicName = [TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html).[FromProjectTopic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html#Google_Cloud_PubSub_V1_TopicName_FromProjectTopic_System_String_System_String_)(projectId, topicId);
            IEnumerable<string> subscriptions = publisher.[ListTopicSubscriptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html#Google_Cloud_PubSub_V1_PublisherServiceApiClient_ListTopicSubscriptions_Google_Cloud_PubSub_V1_ListTopicSubscriptionsRequest_Google_Api_Gax_Grpc_CallSettings_)(topicName);
            return subscriptions;
        }
    }

### Go

The following sample uses the major version of the Go Pub/Sub client library (v2). If you are still using the v1 library, see [the migration guide to v2](https://github.com/googleapis/google-cloud-go/blob/main/pubsub/MIGRATING.md). To see a list of v1 code samples, see [ the deprecated code samples](https://docs.cloud.google.com/pubsub/docs/samples?language=golang&text=deprecated).

Before trying this sample, follow the Go setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/pubsub/v2).
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/pubsub/v2"
    	"cloud.google.com/go/pubsub/v2/apiv1/pubsubpb"
    	"google.golang.org/api/iterator"
    )
    
    func listSubscriptions(w io.Writer, projectID, topicID string) error {
    	// projectID := "my-project-id"
    	// topicName := "projects/sample-248520/topics/ocr-go-test-topic"
    	ctx := context.Background()
    	client, err := pubsub.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	req := &pubsubpb.ListTopicSubscriptionsRequest{
    		Topic: fmt.Sprintf("projects/%s/topics/%s", projectID, topicID),
    	}
    	it := client.TopicAdminClient.ListTopicSubscriptions(ctx, req)
    	for {
    		sub, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("error listing topic subscriptions: %w", err)
    		}
    		fmt.Fprintf(w, "got subscription: %s\n", sub)
    	}
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 
    
    
    import com.google.cloud.pubsub.v1.[TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html);
    import com.google.pubsub.v1.[TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html);
    import java.io.IOException;
    
    public class ListSubscriptionsInTopicExample {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String topicId = "your-topic-id";
    
        listSubscriptionInTopicExample(projectId, topicId);
      }
    
      public static void listSubscriptionInTopicExample(String projectId, String topicId)
          throws IOException {
        try ([TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html) topicAdminClient = [TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html).create()) {
          [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html) topicName = [TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.TopicName.html).of(projectId, topicId);
          for (String subscription : topicAdminClient.listTopicSubscriptions(topicName).iterateAll()) {
            System.out.println(subscription);
          }
          System.out.println("Listed all the subscriptions in the topic.");
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 
    
    
    /**
     * TODO(developer): Uncomment this variable before running the sample.
     */
    // const topicNameOrId = 'YOUR_TOPIC_NAME_OR_ID';
    
    // Imports the Google Cloud client library
    const {PubSub} = require('@google-cloud/pubsub');
    
    // Creates a client; cache this for further use
    const pubSubClient = new PubSub();
    
    async function listTopicSubscriptions(topicNameOrId) {
      // Lists all subscriptions for the topic
      const [subscriptions] = await pubSubClient
        .topic(topicNameOrId)
        .getSubscriptions();
    
      console.log(`Subscriptions for ${topicNameOrId}:`);
      subscriptions.forEach(subscription => console.log(subscription.name));
    }

### Node.ts

Before trying this sample, follow the Node.js setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 
    
    
    /**
     * TODO(developer): Uncomment this variable before running the sample.
     */
    // const topicNameOrId = 'YOUR_TOPIC_NAME_OR_ID';
    
    // Imports the Google Cloud client library
    import {PubSub, Subscription} from '@google-cloud/pubsub';
    
    // Creates a client; cache this for further use
    const pubSubClient = new PubSub();
    
    async function listTopicSubscriptions(topicNameOrId: string) {
      // Lists all subscriptions for the topic
      const [subscriptions] = await pubSubClient
        .topic(topicNameOrId)
        .getSubscriptions();
    
      console.log(`Subscriptions for ${topicNameOrId}:`);
      subscriptions.forEach((subscription: Subscription) =>
        console.log(subscription.name),
      );
    }

### Python

Before trying this sample, follow the Python setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/pubsub/latest). 
    
    
    from google.cloud import pubsub_v1
    
    # TODO(developer)
    # project_id = "your-project-id"
    # topic_id = "your-topic-id"
    
    publisher = pubsub_v1.[PublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)()
    topic_path = publisher.topic_path(project_id, topic_id)
    
    response = publisher.list_topic_subscriptions(request={"topic": topic_path})
    for subscription in response:
        print(subscription)

### Ruby

The following sample uses Ruby Pub/Sub client library v3. If you are still using the v2 library, see [ the migration guide to v3](https://github.com/googleapis/google-cloud-ruby/blob/main/google-cloud-pubsub/MIGRATION_GUIDE.md). To see a list of Ruby v2 code samples, see [ the deprecated code samples](https://docs.cloud.google.com/pubsub/docs/samples?language=ruby&text=deprecated).

Before trying this sample, follow the Ruby setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 
    
    
    # topic_id = "your-topic-id"
    
    pubsub = Google::Cloud::[PubSub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html)
    topic_admin = pubsub.[topic_admin](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html)
    
    response = topic_admin.list_topic_subscriptions \
      topic: pubsub.topic_path(topic_id)
    
    puts "Subscriptions in topic #{topic_id}:"
    response.subscriptions.each do |subscription_name|
      puts subscription_name
    end

### Rust

Before trying this sample, follow the Rust setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Rust API reference documentation](https://docs.rs/google-cloud-pubsub). 
    
    
    use google_cloud_gax::paginator::ItemPaginator;
    use google_cloud_pubsub::client::TopicAdmin;
    
    pub async fn sample(client: &TopicAdmin, project_id: &str, topic_id: &str) -> anyhow::Result<()> {
        let mut subscriptions = client
            .list_topic_subscriptions()
            .set_topic(format!("projects/{project_id}/topics/{topic_id}"))
            .by_item();
    
        println!("listing topic subscriptions");
        while let Some(subscription) = subscriptions.next().await.transpose()? {
            println!("{subscription:?}");
        }
        println!("DONE");
        Ok(())
    }

## What's next

  * Create or modify a subscription with [`gcloud` commands](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions).
  * Create or modify a subscription with [REST APIs](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
