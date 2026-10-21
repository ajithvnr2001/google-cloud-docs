---
url: https://docs.cloud.google.com/pubsub/docs/manage-subscriptions/
title: Change subscription types \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:21:02.054263+00:00
---

# Change subscription types  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/manage-subscriptions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Change subscription types Stay organized with collections  Save and categorize content based on your preferences. 

After you create a subscription, you can change the delivery method to push, pull, or export.

## Before you begin

  * Create one of the [supported subscriptions](https://docs.cloud.google.com/pubsub/docs/subscription-overview#push_pull).



## Required roles and permissions

To get the permission that you need to change a subscription type, ask your administrator to grant you the [Pub/Sub Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`) IAM role on the subscription. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `pubsub.subscriptions.update` permission, which is required to change a subscription type. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

You can configure access control at the project level and at the individual resource level. You can create a subscription in one project and attach it to a topic located in a different project. Ensure that you have the required permissions for each project.

## Change the delivery type of a subscription

To change a subscription's delivery type, perform the following steps.

### Console

  1. In the Google Cloud console, go to the **Subscriptions** page.

[Go to Subscriptions](https://console.cloud.google.com/cloudpubsub/subscription)

  2. Click the name of the subscription that you want to update.

  3. In the subscription details page, click **Edit**.

  4. For **Delivery type** , select the new delivery type.

  5. Fill in the properties for the new subscription type. For more information, see the following topics:

     * [Create a pull subscription](https://docs.cloud.google.com/pubsub/docs/create-subscription)
     * [Create a push subscription](https://docs.cloud.google.com/pubsub/docs/create-push-subscription)
     * [Create a Bigtable subscription](https://docs.cloud.google.com/pubsub/docs/create-bigtable-subscription)
     * [Create a BigQuery subscription](https://docs.cloud.google.com/pubsub/docs/create-bigquery-subscription)
     * [Create a Cloud Storage subscription](https://docs.cloud.google.com/pubsub/docs/create-cloudstorage-subscription)
  6. Optional. Update other subscription properties as required.

  7. Click **Update**.




###  gcloud 

To change the delivery type, use the [`gcloud pubsub subscriptions update`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update) command. Clear the configuration for the current delivery type and set the configuration for the new type, as follows:
    
    
    gcloud pubsub subscriptions update SUBSCRIPTION_ID \
      CLEAR_CONFIG_FLAG \
      NEW_CONFIG_FLAGS
    

Replace the following:

  * SUBSCRIPTION_ID: The name of the subscription to update.

  * CLEAR_CONFIG_FLAG: A flag to clear the existing configuration for the delivery type. Use one of the following flags, depending on the current delivery type:

    * Pull subscription: `--no-enable-exactly-once-delivery`

    * Push subscription: `--push-endpoint=""`

    * BigQuery subscription: `--clear-bigquery-config`

    * Bigtable subscription: `--clear-bigtable-config`

    * Cloud Storage subscription: `--clear-cloud-storage-config`

  * NEW_CONFIG_FLAGS: Flags to configure the new delivery type. For more information, see the documentation for the [`gcloud pubsub subscriptions update`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/update) command.




### Examples

Change a BigQuery subscription to a pull subscription:
    
    
    gcloud pubsub subscriptions update SUBSCRIPTION_ID \
      --clear-bigquery-config
    

Change a push subscription to a BigQuery subscription:
    
    
    gcloud pubsub subscriptions update SUBSCRIPTION_ID \
      --push-endpoint="" \
      --bigquery-table=BIGQUERY_TABLE
    

## Update a push subscription endpoint

To update the [endpoint URL](https://docs.cloud.google.com/pubsub/docs/create-push-subscription#endpoint) on a push subscription, perform the following steps.

### Console

To modify the endpoint URL, complete the following steps.

  1. In the Google Cloud console, go to the **Subscriptions** page. 

[Go to Subscriptions](https://console.cloud.google.com/cloudpubsub/subscription)

  2. Click _more_vert_ next to the subscription to update. 
  3. In the **Delivery type** , choose a delivery option.
  4. Fill in other subscription properties as required.
  5. Click **Update**.



### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To modify the endpoint URL, run the [`gcloud pubsub subscriptions modify-push-config`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/modify-push-config) command:
         
         gcloud pubsub subscriptions modify-push-config SUBSCRIPTION_ID \
           --push-endpoint=PUSH_ENDPOINT

If the subscription is already using pull delivery, setting the push endpoint switches the delivery method to push delivery.

You can switch from push to pull delivery by changing the push endpoint to an empty string.




### REST

To modify the push configurations of a subscription, use the [`projects.subscriptions.modifyPushConfig`](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions/modifyPushConfig) method:

Request:

The request must be authenticated with an access token in the `Authorization` header. To obtain an access token for the current Application Default Credentials: [`gcloud auth application-default print-access-token`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/print-access-token).
    
    
    POST https://pubsub.googleapis.com/v1/projects/PROJECT_ID/subscriptions/SUBSCRIPTION_ID:modifyPushConfig
    Authorization: Bearer ACCESS_TOKEN
      

Request body:
    
    
    {
    "pushConfig": {
      "pushEndpoint": "PUSH_ENDPOINT"
    }
    }

Where:

* PROJECT_ID is your project ID.
* SUBSCRIPTION_ID is your subscription ID.
* PUSH_ENDPOINT is a modified URL that you want to apply as your new push endpoint. For example, `https://myproject.appspot.com/myhandler`.

Response:

If the request is successful, the response is an empty JSON object.

### C++

Before trying this sample, follow the C++ setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C++ API reference documentation](https://googleapis.dev/cpp/google-cloud-pubsub/latest/). 
    
    
    namespace pubsub_admin = ::google::cloud::pubsub_admin;
    namespace pubsub = ::google::cloud::pubsub;
    [](pubsub_admin::SubscriptionAdminClient client,
       std::string const& project_id, std::string const& subscription_id,
       std::string const& endpoint) {
      google::pubsub::v1::ModifyPushConfigRequest request;
      request.set_subscription(
          pubsub::Subscription(project_id, subscription_id).FullName());
      request.mutable_push_config()->set_push_endpoint(endpoint);
      auto status = client.ModifyPushConfig(request);
      if (!status.ok()) throw std::runtime_error(status.message());
    
      std::cout << "The subscription push configuration was successfully"
                << " modified\n";
    }

### C#

Before trying this sample, follow the C# setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 
    
    
    using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
    
    public class UpdatePushConfigurationSample
    {
        public void UpdatePushConfiguration(string projectId, string subscriptionId, string pushEndpoint)
        {
            [SubscriberServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html) subscriber = [SubscriberServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html#Google_Cloud_PubSub_V1_SubscriberServiceApiClient_Create)();
            [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html) subscriptionName = [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html).[FromProjectSubscription](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html#Google_Cloud_PubSub_V1_SubscriptionName_FromProjectSubscription_System_String_System_String_)(projectId, subscriptionId);
    
            [PushConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PushConfig.html) pushConfig = new [PushConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.PushConfig.html) { PushEndpoint = pushEndpoint };
    
            subscriber.[ModifyPushConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html#Google_Cloud_PubSub_V1_SubscriberServiceApiClient_ModifyPushConfig_Google_Cloud_PubSub_V1_ModifyPushConfigRequest_Google_Api_Gax_Grpc_CallSettings_)(subscriptionName, pushConfig);
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
    	"google.golang.org/protobuf/types/known/fieldmaskpb"
    )
    
    func updateEndpoint(w io.Writer, projectID, subscriptionName, endpoint string) error {
    	// projectID := "my-project-id"
    	// subscriptionName := "projects/my-project/subscriptions/my-sub"
    	// endpoint := "https://my-test-project.appspot.com/push"
    	ctx := context.Background()
    	client, err := pubsub.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	req := &pubsubpb.UpdateSubscriptionRequest{
    		Subscription: &pubsubpb.Subscription{
    			Name: subscriptionName,
    			PushConfig: &pubsubpb.PushConfig{
    				PushEndpoint: endpoint,
    			},
    		},
    		UpdateMask: &fieldmaskpb.FieldMask{
    			Paths: []string{"push_config"},
    		},
    	}
    	subConfig, err := client.SubscriptionAdminClient.UpdateSubscription(ctx, req)
    	if err != nil {
    		return fmt.Errorf("Update: %w", err)
    	}
    	fmt.Fprintf(w, "Updated subscription config: %v\n", subConfig)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 
    
    
    import com.google.cloud.pubsub.v1.[SubscriptionAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html);
    import com.google.pubsub.v1.[PushConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PushConfig.html);
    import com.google.pubsub.v1.[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Subscription.html);
    import com.google.pubsub.v1.[SubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SubscriptionName.html);
    import java.io.IOException;
    
    public class UpdatePushConfigurationExample {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String subscriptionId = "your-subscription-id";
        String pushEndpoint = "https://my-test-project.appspot.com/push";
    
        updatePushConfigurationExample(projectId, subscriptionId, pushEndpoint);
      }
    
      public static void updatePushConfigurationExample(
          String projectId, String subscriptionId, String pushEndpoint) throws IOException {
        try ([SubscriptionAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html) subscriptionAdminClient = [SubscriptionAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html).create()) {
          [SubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SubscriptionName.html) subscriptionName = [SubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.SubscriptionName.html).of(projectId, subscriptionId);
          [PushConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PushConfig.html) pushConfig = [PushConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PushConfig.html).newBuilder().[setPushEndpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PushConfig.Builder.html#com_google_pubsub_v1_PushConfig_Builder_setPushEndpoint_java_lang_String_)(pushEndpoint).build();
          subscriptionAdminClient.modifyPushConfig(subscriptionName, pushConfig);
          [Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Subscription.html) subscription = subscriptionAdminClient.getSubscription(subscriptionName);
          System.out.println(
              "Updated push endpoint to: " + subscription.[getPushConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Subscription.html#com_google_pubsub_v1_Subscription_getPushConfig__)().getPushEndpoint());
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const topicNameOrId = 'YOUR_TOPIC_NAME_OR_ID';
    // const subscriptionNameOrId = 'YOUR_SUBSCRIPTION_NAME_OR_ID';
    
    // Imports the Google Cloud client library
    const {PubSub} = require('@google-cloud/pubsub');
    
    // Creates a client; cache this for further use
    const pubSubClient = new PubSub();
    
    async function modifyPushConfig(topicNameOrId, subscriptionNameOrId) {
      const options = {
        // Set to an HTTPS endpoint of your choice. If necessary, register
        // (authorize) the domain on which the server is hosted.
        pushEndpoint: `https://${pubSubClient.projectId}.appspot.com/push`,
      };
    
      await pubSubClient
        .topic(topicNameOrId)
        .subscription(subscriptionNameOrId)
        .modifyPushConfig(options);
      console.log(`Modified push config for subscription ${subscriptionNameOrId}.`);
    }

### Node.ts

Before trying this sample, follow the Node.js setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Node.js API reference documentation](https://googleapis.dev/nodejs/pubsub/latest). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const topicNameOrId = 'YOUR_TOPIC_NAME_OR_ID';
    // const subscriptionNameOrId = 'YOUR_SUBSCRIPTION_NAME_OR_ID';
    
    // Imports the Google Cloud client library
    import {PubSub, CreateSubscriptionOptions} from '@google-cloud/pubsub';
    
    // Creates a client; cache this for further use
    const pubSubClient = new PubSub();
    
    async function modifyPushConfig(
      topicNameOrId: string,
      subscriptionNameOrId: string,
    ) {
      const options: CreateSubscriptionOptions = {
        // Set to an HTTPS endpoint of your choice. If necessary, register
        // (authorize) the domain on which the server is hosted.
        pushEndpoint: `https://${pubSubClient.projectId}.appspot.com/push`,
      };
    
      await pubSubClient
        .topic(topicNameOrId)
        .subscription(subscriptionNameOrId)
        .modifyPushConfig(options);
      console.log(`Modified push config for subscription ${subscriptionNameOrId}.`);
    }

### Python

Before trying this sample, follow the Python setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/pubsub/latest). 
    
    
    from google.cloud import pubsub_v1
    
    # TODO(developer)
    # project_id = "your-project-id"
    # topic_id = "your-topic-id"
    # subscription_id = "your-subscription-id"
    # endpoint = "https://my-test-project.appspot.com/push"
    
    subscriber = pubsub_v1.[SubscriberClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)()
    subscription_path = subscriber.subscription_path(project_id, subscription_id)
    
    push_config = pubsub_v1.types.[PushConfig](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.PushConfig.html)(push_endpoint=endpoint)
    
    subscription = pubsub_v1.types.[Subscription](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.Subscription.html)(
        name=subscription_path, topic=topic_id, push_config=push_config
    )
    
    update_mask = {"paths": {"push_config"}}
    
    # Wrap the subscriber in a 'with' block to automatically call close() to
    # close the underlying gRPC channel when done.
    with subscriber:
        result = subscriber.update_subscription(
            request={"subscription": subscription, "update_mask": update_mask}
        )
    
    print(f"Subscription updated: {subscription_path}")
    print(f"New endpoint for subscription is: {result.push_config}.")

### Ruby

The following sample uses Ruby Pub/Sub client library v3. If you are still using the v2 library, see [ the migration guide to v3](https://github.com/googleapis/google-cloud-ruby/blob/main/google-cloud-pubsub/MIGRATION_GUIDE.md). To see a list of Ruby v2 code samples, see [ the deprecated code samples](https://docs.cloud.google.com/pubsub/docs/samples?language=ruby&text=deprecated).

Before trying this sample, follow the Ruby setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-pubsub/latest/Google/Cloud/PubSub.html). 
    
    
    # subscription_id   = "your-subscription-id"
    # new_endpoint      = "Endpoint where your app receives messages""
    
    pubsub = Google::Cloud::[PubSub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html)
    subscription_admin = pubsub.[subscription_admin](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub-Project.html)
    
    subscription = subscription_admin.get_subscription \
      subscription: pubsub.subscription_path(subscription_id)
    subscription.push_config = Google::Cloud::[PubSub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub.html)::[V1](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub-v1/latest/Google-Cloud-PubSub-V1.html)::PushConfig.[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-pubsub/latest/Google-Cloud-PubSub.html) \
      push_endpoint: new_endpoint
    
    subscription_admin.update_subscription subscription: subscription,
                                           update_mask: {
                                             paths: ["push_config"]
                                           }
    
    puts "Push endpoint updated."

**Note:** Switching from a push to a pull subscription takes several minutes to complete. In this interval, pull requests might generate errors and push requests might continue.

## What's next

  * Create or modify a subscription with [`gcloud` commands](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions).
  * Create or modify a subscription with [REST APIs](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
