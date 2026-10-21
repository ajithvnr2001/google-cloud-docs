---
url: https://docs.cloud.google.com/pubsub/docs/smts/create-subscription-smt/
title: Create a subscription with SMTs \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:46:05.919799+00:00
---

# Create a subscription with SMTs  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/smts/create-subscription-smt/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  Create a subscription with SMTs Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to create a Pub/Sub subscription with Single Message Transforms (SMTs).

Subscription SMTs allow for lightweight modifications to message data and attributes directly within Pub/Sub. This feature enables data cleaning, filtering, or format conversion before the messages are delivered to a subscriber client.

To create a subscription with SMTs, you can use the Google Cloud console, the Google Cloud CLI, the client library, or the Pub/Sub API.

## Before you begin

  * Learn about the [Pub/Sub service and its terminology](https://docs.cloud.google.com/pubsub/docs/pubsub-basics).

  * Learn about [SMTs](https://docs.cloud.google.com/pubsub/docs/smts/smts-overview).




### Required roles and permissions

To get the permissions that you need to create a subscription with SMTs, ask your administrator to grant you the [Pub/Sub Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create a subscription with SMTs. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create a subscription with SMTs:

  * Grant the create a subscription permission on the project: `pubsub.subscriptions.create`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

Depending on the subscription type, you might need additional permissions. To find out the exact list of permissions, refer to the document that discusses creating the specific subscription. For example, if you are creating a BigQuery subscription with SMTs, see [Create BigQuery subscriptions](https://docs.cloud.google.com/pubsub/docs/create-bigquery-subscription).

If you create a subscription in a different project than the topic, you must grant the `roles/pubsub.subscriber` role to the principal of the project containing the subscription in the project containing the topic.

You can configure access control at the project level and at the individual resource level.

## Create a subscription with SMTs

Before you create a subscription with SMTs, review the documentation for [Properties of a subscription](https://docs.cloud.google.com/pubsub/docs/subscription-properties).

**Note:** It is highly recommended to configure a [dead-letter topic](https://docs.cloud.google.com/pubsub/docs/handling-failures#dead-letter_topic) for subscriptions with SMTs. Messages forwarded to the dead-letter topic due to SMT failures contain an attribute `CloudPubSubDeadLetterSourceSMTErrorMessage` that has the reason the SMT failed.

To create a Pub/Sub subscription with one or more SMTs, perform the following steps. You can enable up to 5 SMTs per subscription.

### Console

  1. In the Google Cloud console, go to the Pub/Sub **Subscriptions** page.

[Go to Subscriptions](https://console.cloud.google.com/cloudpubsub/subscription)

  2. Click **Create subscription**.

  3. In the **Subscription ID** field, enter an ID for your subscription. For more information about naming subscriptions, see the [naming guidelines](https://docs.cloud.google.com/pubsub/docs/pubsub-basics#resource_names).

  4. Under **Transforms** , click **Add a transform**.

  5. Select the **Transform type**. For more information about the supported SMT types, see [Types of SMTs](https://docs.cloud.google.com/pubsub/docs/smts/smts-overview#types_of_smts).

  6. Set the configuration properties for the SMT. The set of properties depends on the type of SMT. For more information, see the documentation for that SMT type.

  7. Optional. To validate the SMT, click **Validate**. If the SMT is valid, the message `"Validation passed"` is displayed. Otherwise, an error message is displayed.

  8. To add another transform, click **Add a transform** and repeat the previous steps.

To arrange the SMTs in a specific order, click arrow_upward**Move up** or arrow_downward**Move down**. To remove an SMT, click delete **Delete**.

  9. Optional. To test an SMT on a sample message, perform the following steps:

     1. Click **Test transforms**.

     2. In the **Test transform** window, select the function that you want to test.

     3. In the **Input message** window, enter a sample message.

     4. To add an attribute to the message, click **Add an attribute** and enter the attribute's key and value. You can add multiple attributes.

     5. Click **Test**. The result of applying the SMT on the message is displayed under **Output message**.

     6. To close the **Test transforms** window, click close **Close**.

If you create more than one SMT, you can test the entire sequence of transforms as follows:

     1. Test the first SMT in the sequence, as described in the previous steps.
     2. Select the next SMT. The input message is pre-populated with the output message from the previous test.
     3. Continue testing the SMTs in order, to make sure the entire sequence works as expected.
  10. Click **Create** to create the subscription.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Create a YAML or JSON file that defines one or more SMTs. The YAML or JSON definition depends on the type of SMT. For more information, see [Types of SMTs](https://docs.cloud.google.com/pubsub/docs/smts/smts-overview#types_of_smts).

If the file includes more than one SMT, Pub/Sub executes them in the order listed.

  3. Optional. To validate an SMT, run the [`gcloud pubsub message-transforms validate`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/message-transforms/validate) command:
         
         gcloud pubsub message-transforms validate \
           --message-transform-file=TRANSFORM_FILE
         

Replace the following:

     * TRANSFORM_FILE: The path to a YAML or JSON file that defines a single SMT. If you are creating multiple SMTs, you must validate them individually.
  4. Optional. To test one or more SMTs on a sample Pub/Sub message, run the [`gcloud pubsub message-transforms test`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/message-transforms/test) command:
         
         gcloud pubsub message-transforms test \
           --message-transforms-file=TRANSFORMS_FILE \
           --message=MESSAGE \
           --attribute=ATTRIBUTES
         

Replace the following:

     * TRANSFORMS_FILE: The path to a YAML or JSON file that defines one or more SMTs.
     * MESSAGE: The body of the sample message.
     * ATTRIBUTES: Optional. A comma-separated list of message attributes. Each attribute is a key-value pair formatted as `KEY="VALUE"`.

The command executes the SMTs in order, using the output from each SMT as the input to the next. The command outputs the results of each step.

  5. To create the subscription, run the [`gcloud pubsub subscriptions create`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create) command:
         
         gcloud pubsub subscriptions create SUBSCRIPTION_ID \
             --topic=projects/PROJECT_ID/topics/TOPIC_ID \
             --message-transforms-file=TRANSFORMS_FILE
         

Replace the following:

     * SUBSCRIPTION_ID: The ID or name of the subscription you want to create. For guidelines on how to name a subscription, see [Resource names](https://docs.cloud.google.com/pubsub/docs/pubsub-basics#resource_names). The name of a subscription is immutable.

     * PROJECT_ID: The ID of the project that contains the topic.

     * TOPIC_ID: The ID of the topic to subscribe to.

     * TRANSFORMS_FILE: The path to the YAML or JSON file that defines one or more SMTs.




### C#

Before trying this sample, follow the C# setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest). 
    
    
    using [Google.Cloud.PubSub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.html);
    using System;
    
    public class CreateSubscriptionWithSingleMessageTransformSample
    {
        public Subscription CreateSubscriptionWithSingleMessageTransform(string projectId, string topicId, string subscriptionId)
        {
            [SubscriberServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html) subscriber = [SubscriberServiceApiClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html#Google_Cloud_PubSub_V1_SubscriberServiceApiClient_Create)();
            [TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html) topicName = [TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html).[FromProjectTopic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.TopicName.html#Google_Cloud_PubSub_V1_TopicName_FromProjectTopic_System_String_System_String_)(projectId, topicId);
    
            [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html) subscriptionName = [SubscriptionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html).[FromProjectSubscription](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriptionName.html#Google_Cloud_PubSub_V1_SubscriptionName_FromProjectSubscription_System_String_System_String_)(projectId, subscriptionId);
            [MessageTransform](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.MessageTransform.html) removeSSNTransform = new [MessageTransform](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.MessageTransform.html)
            {
                JavascriptUdf = new [JavaScriptUDF](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.JavaScriptUDF.html)
                {
                    FunctionName = "redactSsn",
                    Code = "function redactSsn(message, metadata) {"
                    + "   const data = JSON.parse(message.data);"
                    + "   delete data['ssn'];"
                    + "   message.data = JSON.stringify(data);"
                    + "   return message;"
                    + "}"
                },
            };
    
            var subscription = subscriber.[CreateSubscription](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.SubscriberServiceApiClient.html#Google_Cloud_PubSub_V1_SubscriberServiceApiClient_CreateSubscription_Google_Cloud_PubSub_V1_Subscription_Google_Api_Gax_Grpc_CallSettings_)(new [Subscription](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PubSub.V1/latest/Google.Cloud.PubSub.V1.Subscription.html)
            {
                SubscriptionName = subscriptionName,
                TopicAsTopicName = topicName,
                MessageTransforms = { removeSSNTransform },
            });
            Console.WriteLine($"Subscription {subscription.Name} created with SMT.");
    
            return subscription;
        }
    }

### Java

Before trying this sample, follow the Java setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 
    
    
    import com.google.cloud.pubsub.v1.[SubscriptionAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html);
    import com.google.pubsub.v1.[JavaScriptUDF](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.JavaScriptUDF.html);
    import com.google.pubsub.v1.[MessageTransform](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.MessageTransform.html);
    import com.google.pubsub.v1.[ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html);
    import com.google.pubsub.v1.[ProjectTopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectTopicName.html);
    import com.google.pubsub.v1.[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Subscription.html);
    import java.io.IOException;
    
    public class CreateSubscriptionWithSmtExample {
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String topicId = "your-topic-id";
        String subscriptionId = "your-subscription-id";
    
        createSubscriptionWithSmtExample(projectId, topicId, subscriptionId);
      }
    
      public static void createSubscriptionWithSmtExample(
          String projectId, String topicId, String subscriptionId) throws IOException {
    
        // UDF that removes the 'ssn' field, if present
        String code =
            "function redactSSN(message, metadata) {"
                + "  const data = JSON.parse(message.data);"
                + "  delete data['ssn'];"
                + "  message.data = JSON.stringify(data);"
                + "  return message;"
                + "}";
        String functionName = "redactSSN";
    
        [JavaScriptUDF](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.JavaScriptUDF.html) udf =
            [JavaScriptUDF](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.JavaScriptUDF.html).newBuilder().[setCode](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.JavaScriptUDF.Builder.html#com_google_pubsub_v1_JavaScriptUDF_Builder_setCode_java_lang_String_)(code).[setFunctionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.JavaScriptUDF.Builder.html#com_google_pubsub_v1_JavaScriptUDF_Builder_setFunctionName_java_lang_String_)(functionName).build();
        [MessageTransform](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.MessageTransform.html) transform = [MessageTransform](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.MessageTransform.html).newBuilder().[setJavascriptUdf](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.MessageTransform.Builder.html#com_google_pubsub_v1_MessageTransform_Builder_setJavascriptUdf_com_google_pubsub_v1_JavaScriptUDF_)(udf).build();
    
        try ([SubscriptionAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html) subscriptionAdminClient = [SubscriptionAdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.SubscriptionAdminClient.html).create()) {
    
          [ProjectTopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectTopicName.html) topicName = [ProjectTopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectTopicName.html).of(projectId, topicId);
          [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html) subscriptionName =
              [ProjectSubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html).of(projectId, subscriptionId);
    
          [Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Subscription.html) subscription =
              subscriptionAdminClient.createSubscription(
                  [Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.Subscription.html).newBuilder()
                      .setName(subscriptionName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectSubscriptionName.html#com_google_pubsub_v1_ProjectSubscriptionName_toString__)())
                      .setTopic(topicName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.ProjectTopicName.html#com_google_pubsub_v1_ProjectTopicName_toString__)())
                      // Add the UDF message transform
                      .addMessageTransforms(transform)
                      .build());
    
          System.out.println("Created subscription with SMT: " + subscription.getAllFields());
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/pubsub/latest). 
    
    
    from google.cloud import pubsub_v1
    from google.pubsub_v1.types import [JavaScriptUDF](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.JavaScriptUDF.html), [MessageTransform](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.MessageTransform.html)
    
    # TODO(developer): Choose an existing topic.
    # project_id = "your-project-id"
    # topic_id = "your-topic-id"
    # subscription_id = "your-subscription-id"
    
    publisher = pubsub_v1.[PublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)()
    subscriber = pubsub_v1.[SubscriberClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)()
    topic_path = publisher.topic_path(project_id, topic_id)
    subscription_path = subscriber.subscription_path(project_id, subscription_id)
    
    code = """function redactSSN(message, metadata) {
                const data = JSON.parse(message.data);
                delete data['ssn'];
                message.data = JSON.stringify(data);
                return message;
                }"""
    udf = JavaScriptUDF(code=code, function_name="redactSSN")
    transforms = [MessageTransform(javascript_udf=udf)]
    
    with subscriber:
        subscription = subscriber.create_subscription(
            request={
                "name": subscription_path,
                "topic": topic_path,
                "message_transforms": transforms,
            }
        )
        print(f"Created subscription with SMT: {subscription}")

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
    
    // createSubscriptionWithSMT creates a subscription with a single message transform function applied.
    func createSubscriptionWithSMT(w io.Writer, projectID, topicID, subID string) error {
    	// projectID := "my-project-id"
    	// topicID := "my-topic"
    	// subID := "my-sub"
    	ctx := context.Background()
    	client, err := pubsub.NewClient(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("pubsub.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	code := `function redactSSN(message, metadata) {
    			const data = JSON.parse(message.data);
    			delete data['ssn'];
    			message.data = JSON.stringify(data);
    			return message;
    		}`
    
    	transform := &pubsubpb.MessageTransform{
    		Transform: &pubsubpb.MessageTransform_JavascriptUdf{
    			JavascriptUdf: &pubsubpb.JavaScriptUDF{
    				FunctionName: "redactSSN",
    				Code:         code,
    			},
    		},
    	}
    
    	sub := &pubsubpb.Subscription{
    		Name:              fmt.Sprintf("projects/%s/subscriptions/%s", projectID, subID),
    		Topic:             fmt.Sprintf("projects/%s/topics/%s", projectID, topicID),
    		MessageTransforms: []*pubsubpb.MessageTransform{transform},
    	}
    	sub, err = client.SubscriptionAdminClient.CreateSubscription(ctx, sub)
    	if err != nil {
    		return fmt.Errorf("CreateSubscription: %w", err)
    	}
    	fmt.Fprintf(w, "Created subscription with message transform: %v\n", sub)
    	return nil
    }
    

## How SMTs interact with other subscription features

Consider the following points when using a subscription SMT.

### Filtering

If your subscription uses both SMTs and Pub/Sub's [built-in filters](https://docs.cloud.google.com/pubsub/docs/subscription-message-filter), then the filter gets applied before the SMT. This has the following implications:

  * If your SMT alters the message attributes, the Pub/Sub filter isn't applied to the new set of attributes.
  * Your SMT isn't applied to messages that are filtered out by the Pub/Sub filter.
  * If your SMT filters out messages, be aware of the impact on [monitoring your subscription backlog](https://docs.cloud.google.com/pubsub/docs/monitoring#monitoring_subscriptions_with_smts).
  * If you connect a subscription to a [Dataflow pipeline](https://docs.cloud.google.com/dataflow/docs/concepts/streaming-with-cloud-pubsub), don't use a subscription SMT to filter out messages, because it disrupts Dataflow's autoscaling.



### Message ordering

If you define an SMT on a subscription that has ordering enabled, and executing the SMT throws an error, then subsequent messages for the same ordering key aren't delivered to the subscriber. To avoid this problem, set up a [dead-letter topic](https://docs.cloud.google.com/pubsub/docs/handling-failures) on the subscription to remove the unprocessed message from the message backlog.

## What's next

  * [Troubleshoot subscription SMTs](https://docs.cloud.google.com/pubsub/docs/smt-subscription-troubleshooting)

  * [Update subscription SMTs](https://docs.cloud.google.com/pubsub/docs/smts/update-subscription-smt)

  * [Delete subscription SMTs](https://docs.cloud.google.com/pubsub/docs/smts/delete-subscription-smt)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
