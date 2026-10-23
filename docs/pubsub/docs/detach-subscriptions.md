---
url: https://docs.cloud.google.com/pubsub/docs/detach-subscriptions/
title: Detach subscriptions \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:03:58.020048+00:00
---

# Detach subscriptions  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/detach-subscriptions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Detach subscriptions Stay organized with collections  Save and categorize content based on your preferences. 

When you create a subscription, you attach the subscription to a topic, and subscribers can receive messages from the subscription. To stop subscribers from receiving messages, you can detach subscriptions from the topic.

## Before you begin

  * Learn about [subscriptions](https://docs.cloud.google.com/pubsub/docs/subscription-overview).
  * Create one of the following subscriptions, [pull](https://docs.cloud.google.com/pubsub/docs/create-subscription), [push](https://docs.cloud.google.com/pubsub/docs/create-push-subscription), or [BigQuery](https://docs.cloud.google.com/pubsub/docs/create-bigquery-subscription).



## Required roles and permissions

To get the permission that you need to detach subscriptions, ask your administrator to grant you the [Pub/Sub Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`) IAM role on the topic. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `pubsub.topics.detachSubscription` permission, which is required to detach subscriptions. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

You can configure access control at the project level and at the individual resource level. You can create a subscription in one project and attach it to a topic located in a different project. Ensure that you have the required permissions for each project.

## Detach a subscription from a topic

You can detach a subscription from a topic using the Google Cloud console, the Google Cloud CLI, the client library, or the Pub/Sub API.

### Console

To detach a subscription, follow these steps:

  1. In the Google Cloud console, go to the **Topics** page.

[Go to Topics](https://console.cloud.google.com/cloudpubsub/topic)

  2. Select the topic from which you want to detach a subscription.

  3. In the **Subscriptions** tab, select the subscription to detach.

  4. In the **Subscription details** page, click **Detach**.

  5. In the dialog that appears, click **Detach** again.




### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To detach a subscription, use the [`gcloud pubsub topics detach-subscription`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/topics/detach-subscription) command:
         
         gcloud pubsub topics detach-subscription SUBSCRIPTION_ID

If the request is successful, the command line displays a confirmation:
         
         Detached subscription [SUBSCRIPTION_ID].




### REST

To detach a subscription, use the [`projects.subscriptions.detach`](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions/detach) method.

Request:

The request must be authenticated with an access token in the `Authorization` header. To obtain an access token for the current Application Default Credentials, use the [ `gcloud auth application-default print-access-token`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token) command.
    
    
    POST https://pubsub.googleapis.com/v1/projects/PROJECT_ID/subscriptions/SUBSCRIPTION_ID:detach
    Authorization: Bearer ACCESS_TOKEN
    

Where:

  * PROJECT_ID is your project ID.
  * SUBSCRIPTION_ID is your subscription ID.



Response:

If the request is successful, the response is an empty JSON object.

### C++

Before trying this sample, follow the C++ setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 
    
    
    namespace pubsub = ::google::cloud::pubsub;
    namespace pubsub_admin = ::google::cloud::pubsub_admin;
    [](pubsub_admin::TopicAdminClient client, std::string const& project_id,
       std::string const& subscription_id) {
      google::pubsub::v1::DetachSubscriptionRequest request;
      request.set_subscription(
          pubsub::Subscription(project_id, subscription_id).FullName());
      auto response = client.DetachSubscription(request);
      if (!response.ok()) throw std::move(response).status();
    
      std::cout << "The subscription was successfully detached: "
                << response->DebugString() << "\n";
    }

### C#

Before trying this sample, follow the C# setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 
    
    
    using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
    using System;
    
    public class DetachSubscriptionSample
    {
        public void DetachSubscription(string projectId, string subscriptionId)
        {
            [PublisherServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html) publisher = [PublisherServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html#Google_Cloud_PubSub_V1_PublisherServiceApiClient_Create)();
    
            [DetachSubscriptionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.DetachSubscriptionRequest.html) detachSubscriptionRequest = new [DetachSubscriptionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.DetachSubscriptionRequest.html)
            {
                SubscriptionAsSubscriptionName = [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html).[FromProjectSubscription](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html#Google_Cloud_PubSub_V1_SubscriptionName_FromProjectSubscription_System_String_System_String_)(projectId, subscriptionId),
            };
    
            publisher.[DetachSubscription](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PublisherServiceApiClient.html#Google_Cloud_PubSub_V1_PublisherServiceApiClient_DetachSubscription_Google_Cloud_PubSub_V1_DetachSubscriptionRequest_Google_Api_Gax_Grpc_CallSettings_)(detachSubscriptionRequest);
    
            Console.WriteLine($"Subscription {subscriptionId} is detached.");
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
    )
    
    func detachSubscription(w io.Writer, projectID, subName string) error {
    	// projectID is the project which contains the topic you manage.
    	// This might differ from the project which contains the subscription
    	// you wish to detach, which can exist in any GCP project.
    	// projectID := "my-project-id"
    	// subName := "projects/some-project/subscriptions/my-sub"
    	ctx := context.Background()
    	client, err := pubsub.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	// Call DetachSubscription, which detaches a subscription from
    	// a topic. This can only be done if you have the
    	// `pubsub.topics.detachSubscription` role on the topic the
    	// subscription is attached to.
    	req := &pubsubpb.DetachSubscriptionRequest{
    		Subscription: subName,
    	}
    	_, err = client.TopicAdminClient.DetachSubscription(ctx, req)
    	if err != nil {
    		return fmt.Errorf("detach subscription failed: %w", err)
    	}
    
    	fmt.Fprintf(w, "Detached subscription %s", subName)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 
    
    
    import com.google.cloud.pubsub.v1.[SubscriptionAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html);
    import com.google.cloud.pubsub.v1.[TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html);
    import com.google.pubsub.v1.[DetachSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.DetachSubscriptionRequest.html);
    import com.google.pubsub.v1.[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Subscription.html);
    import com.google.pubsub.v1.[SubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SubscriptionName.html);
    import java.io.IOException;
    
    public class DetachSubscriptionExample {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        // Choose an existing subscription.
        String subscriptionId = "your-subscription-id";
    
        detachSubscriptionExample(projectId, subscriptionId);
      }
    
      public static void detachSubscriptionExample(String projectId, String subscriptionId)
          throws IOException {
        [SubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SubscriptionName.html) subscriptionName = [SubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SubscriptionName.html).of(projectId, subscriptionId);
    
        try ([TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html) topicAdminClient = [TopicAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.TopicAdminClient.html).create()) {
          topicAdminClient.detachSubscription(
              [DetachSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.DetachSubscriptionRequest.html).newBuilder()
                  .setSubscription(subscriptionName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SubscriptionName.html#com_google_pubsub_v1_SubscriptionName_toString__)())
                  .build());
        }
    
        try ([SubscriptionAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html) subscriptionAdminClient = [SubscriptionAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html).create()) {
          [Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Subscription.html) subscription = subscriptionAdminClient.getSubscription(subscriptionName);
          if (subscription.[getDetached](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Subscription.html#com_google_pubsub_v1_Subscription_getDetached__)()) {
            System.out.println("Subscription is detached.");
          } else {
            System.out.println("Subscription is NOT detached.");
          }
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const subscriptionNameOrId = 'YOUR_EXISTING_SUBSCRIPTION_NAME_OR_ID';
    
    // Imports the Google Cloud client library
    const {PubSub} = require('@google-cloud/pubsub');
    
    // Creates a client; cache this for further use
    const pubSubClient = new PubSub();
    
    async function detachSubscription(subscriptionNameOrId) {
      // Gets the status of the existing subscription
      const sub = pubSubClient.subscription(subscriptionNameOrId);
      const [detached] = await sub.detached();
      console.log(
        `Subscription ${subscriptionNameOrId} 'before' detached status: ${detached}`,
      );
    
      await pubSubClient.detachSubscription(subscriptionNameOrId);
      console.log(`Subscription ${subscriptionNameOrId} detach request was sent.`);
    
      const [updatedDetached] = await sub.detached();
      console.log(
        `Subscription ${subscriptionNameOrId} 'after' detached status: ${updatedDetached}`,
      );
    }

### Node.ts

Before trying this sample, follow the Node.js setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const subscriptionNameOrId = 'YOUR_EXISTING_SUBSCRIPTION_NAME_OR_ID';
    
    // Imports the Google Cloud client library
    import {PubSub} from '@google-cloud/pubsub';
    
    // Creates a client; cache this for further use
    const pubSubClient = new PubSub();
    
    async function detachSubscription(subscriptionNameOrId: string) {
      // Gets the status of the existing subscription
      const sub = pubSubClient.subscription(subscriptionNameOrId);
      const [detached] = await sub.detached();
      console.log(
        `Subscription ${subscriptionNameOrId} 'before' detached status: ${detached}`,
      );
    
      await pubSubClient.detachSubscription(subscriptionNameOrId);
      console.log(`Subscription ${subscriptionNameOrId} detach request was sent.`);
    
      const [updatedDetached] = await sub.detached();
      console.log(
        `Subscription ${subscriptionNameOrId} 'after' detached status: ${updatedDetached}`,
      );
    }

### PHP

Before trying this sample, follow the PHP setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub PHP API reference documentation](https://cloud.google.com/php/docs/reference/cloud-pubsub/latest). 
    
    
    use Google\Cloud\PubSub\PubSubClient;
    
    /**
     * Detach a Pub/Sub subscription from a topic.
     *
     * @param string $projectId  The Google project ID.
     * @param string $subscriptionName  The Pub/Sub subscription name.
     */
    function detach_subscription($projectId, $subscriptionName)
    {
        $pubsub = new PubSubClient([
            'projectId' => $projectId,
        ]);
        $subscription = $pubsub->subscription($subscriptionName);
        $subscription->detach();
    
        printf('Subscription detached: %s' . PHP_EOL, $subscription->name());
    }

### Python

Before trying this sample, follow the Python setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/pubsub/latest). 
    
    
    from google.api_core.exceptions import GoogleAPICallError, RetryError
    from google.cloud import pubsub_v1
    
    # TODO(developer): Choose an existing subscription.
    # project_id = "your-project-id"
    # subscription_id = "your-subscription-id"
    
    publisher_client = pubsub_v1.[PublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)()
    subscriber_client = pubsub_v1.[SubscriberClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)()
    subscription_path = [subscriber_client](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.html).subscription_path(project_id, subscription_id)
    
    try:
        [publisher_client](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.html).[detach_subscription](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.publisher.client.Client.html#google_cloud_pubsub_v1_publisher_client_Client_detach_subscription)(
            request={"subscription": subscription_path}
        )
    except (GoogleAPICallError, RetryError, ValueError, Exception) as err:
        print(err)
    
    subscription = [subscriber_client](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.html).get_subscription(
        request={"subscription": subscription_path}
    )
    if subscription.detached:
        print(f"{subscription_path} is detached.")
    else:
        print(f"{subscription_path} is NOT detached.")

### Ruby

The following sample uses Ruby Pub/Sub client library v3. If you are still using the v2 library, see [ the migration guide to v3](https://github.com/googleapis/google-cloud-ruby/blob/main/google-cloud-pubsub/MIGRATION_GUIDE.md). To see a list of Ruby v2 code samples, see [ the deprecated code samples](https://docs.cloud.google.com/pubsub/docs/samples?language=ruby&text=deprecated).

Before trying this sample, follow the Ruby setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 
    
    
    # subscription_id = "your-subscription-id"
    
    pubsub = Google::Cloud::[PubSub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html)
    topic_admin = pubsub.[topic_admin](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html)
    subscription_admin = pubsub.[subscription_admin](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html)
    subscription_path = pubsub.subscription_path subscription_id
    
    topic_admin.detach_subscription subscription: subscription_path
    sleep 120
    subscription = subscription_admin.get_subscription \
      subscription: subscription_path
    
    if subscription.[detached](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1-Subscription.html)
      puts "Subscription is detached."
    else
      puts "Subscription is NOT detached."
    end

The Pub/Sub service might take several minutes to finish detaching the subscription from the topic.

After the Pub/Sub service detaches the subscription from the topic, the Pub/Sub service deletes any messages that it retains for the subscription. You can't retrieve these messages from the subscription or reattach the subscription to a topic. To free up your Google Cloud project quota, [delete the subscription](https://docs.cloud.google.com/pubsub/docs/delete-subscriptions).

If the subscription and the topic are in different Google Cloud projects, the Pub/Sub service adds an entry to the audit logs of both projects.

## What's next

  * Create or modify a subscription with [`gcloud` commands](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions).
  * Create or modify a subscription with [REST APIs](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
