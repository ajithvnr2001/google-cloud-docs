---
url: https://docs.cloud.google.com/pubsub/lite/docs/export-pubsub/
title: Export Pub/Sub Lite messages to Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:39:10.668786+00:00
---

# Export Pub/Sub Lite messages to Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/lite/docs/export-pubsub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Pub/Sub Lite ](https://docs.cloud.google.com/pubsub/lite/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/lite/docs/publish-receive-messages-console)



Send feedback 

#  Export Pub/Sub Lite messages to Pub/Sub Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Pub/Sub Lite is deprecated. Effective January 31, 2027, Pub/Sub Lite will be turned down.   


  * Current customers: Pub/Sub Lite remains functional until January 31, 2027.   
If you have not used Pub/Sub Lite within the 90-day period preceding July 15, 2025 (April 15, 2025 - July 15, 2025), you won't be able to access Pub/Sub Lite starting on July 15, 2025. 
  * New customers: Pub/Sub Lite is no longer available for new customers after September 24, 2024.



You can migrate your Pub/Sub Lite service to [Google Cloud Managed Service for Apache Kafka](https://docs.cloud.google.com/pubsub/lite/docs/migrate-pubsub-lite-to-managed-service-for-apache-kafka) or [Pub/Sub](https://docs.cloud.google.com/pubsub/lite/docs/migrate-pubsub-lite-to-pubsub).

This document describes how to set up automatic exporting of Pub/Sub Lite messages to Pub/Sub.

Here are some scenarios where you might use this feature:

  * Interoperate between workloads that use a mix of Pub/Sub Lite and Pub/Sub.
  * Migrate a Pub/Sub Lite workload to Pub/Sub.
  * Use advanced Pub/Sub features, such as push subscriptions and filtering, from an existing application that is based on Pub/Sub Lite.
  * Consolidate multiple data pipelines.



## Overview

To export messages from Pub/Sub Lite to Pub/Sub, you create a special type of subscription called an _export subscription_. An export subscription receives messages from a Lite topic, converts them to Pub/Sub messages, and sends the converted messages to a destination Pub/Sub topic.

![Diagram of exporting Pub/Sub Lite messages](https://docs.cloud.google.com/static/pubsub/images/export-subscription.png)

A Lite topic can have a combination of both export subscriptions and standard subscriptions. The two subscription types are identical in terms of [quota usage](https://docs.cloud.google.com/pubsub/lite/quotas) and [reservation throughput](https://docs.cloud.google.com/pubsub/lite/docs/reservations). An export subscription consumes Lite subscription throughput capacity and is charged for Pub/Sub publishing throughput.

An export subscription connects a Lite topic to exactly one Pub/Sub topic. However, a Lite topic can have multiple export subscriptions that connect to different Pub/Sub topics (fan-out architecture). You can also export from multiple Lite topics to the same Pub/Sub topic (fan-in architecture).

## Authentication

An export subscription accesses both Pub/Sub Lite and Pub/Sub resources. To create an export subscription, you need the following permissions:

  * `pubsublite.subscriptions.create`. The following predefined roles contain this permission:

    * `roles/pubsublite.admin`
    * `roles/pubsublite.editor`

See [Access Control for Pub/Sub Lite](https://docs.cloud.google.com/pubsub/lite/docs/access-control).

  * `pubsub.topics.get`. The following predefined roles contain this permission:

    * `roles/pubsub.admin`
    * `roles/pubsub.editor`
    * `roles/pubsub.viewer`

See [Access Control for Pub/Sub](https://docs.cloud.google.com/pubsub/docs/access-control).




### Service agents

An export subscription publishes to a Pub/Sub topic on your behalf. To do this, it uses a [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents).

After you create the first export subscription in a project, a Pub/Sub Lite service agent is automatically created. If you create additional export subscriptions in the same project, they use the same service agent. The service agent has the following naming scheme: `service-<your_project_number>@gcp-sa-pubsublite.iam.gserviceaccount.com`.

The service agent is created with permissions to publish to all Pub/Sub and Pub/Sub Lite topics within the same project as the export subscription. If your destination Pub/Sub topic is in a different project than the export subscription, you must grant the service agent additional permissions by adding the **Pub/Sub Publisher** role (`roles/pubsub.publisher`). You can grant permissions for an entire project or an individual topic. We recommend granting permissions at the topic level, following the principle of least privilege.

For more information, see [Controlling access through the Google Cloud console](https://docs.cloud.google.com/pubsub/docs/access-control#console). You can also use the [`gcloud projects add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding) command to add IAM roles:
    
    
    gcloud pubsub topics add-iam-policy-binding TOPIC_NAME \
     --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-pubsublite.iam.gserviceaccount.com
     --role=roles/pubsub.publisher

Replace the following:

  * TOPIC_NAME: The name of the destination Pub/Sub topic to add the IAM policy binding.
  * PROJECT_NUMBER: The project number of the Pub/Sub Lite export subscription's project.



## Create an export subscription

You can create a Lite export subscription with the Google Cloud console, the Google Cloud CLI, or the Pub/Sub Lite API.

A Lite export subscription must be in the same project and location as the Lite topic to which it is attached. To create the Lite topic, see [Create and manage Lite topics](https://docs.cloud.google.com/pubsub/lite/docs/topics).

If you attach an export subscription to a Lite topic, make sure that all messages published to the Lite topic are compatible with Pub/Sub. For more information, see Message compatibility.

Once it has been created, you cannot change an export subscription to a standard subscription, or vice versa.

### Console

  1. Go to the **Lite Subscriptions** page.

[Go to Lite Subscriptions](https://console.cloud.google.com/cloudpubsub/liteSubscription)

  2. Click **Create Lite subscription**.

  3. Enter a Lite subscription ID.

  4. Select a Lite topic to receive messages from.

  5. Select **Deliver messages immediately** or **Deliver messages after stored**.

  6. Choose a type of **Starting offset**.

  7. Select **Export to Pub/Sub topic**.

  8. In the **Destination topic** list, choose a Pub/Sub topic to receive the exported Lite messages.

  9. Optional. Specify a dead-letter topic.

     1. Select the **Enable dead lettering** checkbox.
     2. Select a Lite topic to use as the dead-letter topic, or click **Create Lite Topic** to create a new dead-letter topic. The dead-letter topic must be in the same location (zone or region) and project as the export subscription.
  10. Click **Create**.




### gcloud

To create an export subscription, use the [`gcloud pubsub lite-subscriptions create`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/create) command:
    
    
    gcloud pubsub lite-subscriptions create SUBSCRIPTION_ID \
      --location=LOCATION \
      --topic=TOPIC_ID \
      --export-pubsub-topic=PUBSUB_TOPIC_NAME \
      --export-dead-letter-topic=DEAD_LETTER_TOPIC_ID \
      --export-desired-state=DESIRED_STATE

Replace the following:

  * SUBSCRIPTION_ID: The ID of the Lite subscription to create.
  * LOCATION: The [location](https://docs.cloud.google.com/pubsub/lite/docs/locations) of the Lite subscription.
  * TOPIC_ID: The ID of the Lite topic to attach to the Lite subscription.
  * PUBSUB_TOPIC_NAME: The name of Pub/Sub topic to export to. Specify the full name if the topic is in a different project: `projects/my-project-id/topics/my-topic-id`.
  * DEAD_LETTER_TOPIC_ID: Optional. The ID of a Lite topic to use as the dead-letter topic. The dead-letter topic must be in the same location (zone or region) and project as the export subscription.
  * DESIRED_STATE: Optional. The starting state of the subscription. The following values are supported: 
    * `active`: The subscription exports Lite messages to Pub/Sub. (Default.)
    * `paused`: Exporting of Lite messages is suspended.



If the request is successful, the command line displays a confirmation:
    
    
    Created [SUBSCRIPTION_ID].

### Protocol

To create a Lite export subscription, send a `POST` request like the following:
    
    
    POST https://REGION-pubsublite.googleapis.com/v1/admin/projects/PROJECT_NUMBER/locations/LOCATION/subscriptions/SUBSCRIPTION_ID
    Authorization: Bearer $(gcloud auth print-access-token)
    

Replace the following:

  * REGION: The region to store the Lite subscription in.
  * PROJECT_NUMBER: The project number of the project to create the Lite subscription in.
  * LOCATION: The name of a location that Pub/Sub Lite supports.
  * SUBSCRIPTION_ID: The ID of the Lite subscription.



Specify the following fields in the request body:
    
    
    {
      "topic": "projects/PROJECT_NUMBER/locations/LOCATION/topics/TOPIC_ID",
      "deliveryConfig": {
          "deliveryRequirement": "DELIVERY_REQUIREMENT",
      },
      "exportConfig": {
          "desiredState": "DESIRED_STATE",
          "deadLetterTopic": "projects/PROJECT_NUMBER/locations/LOCATION/topics/DEAD_LETTER_TOPIC_ID",
          "pubsubConfig": {
              "topic": "PUBSUB_TOPIC_NAME"
          }
      }
    }

Replace the following:

  * DELIVERY_REQUIREMENT: The delivery requirement, either `DELIVER_AFTER_STORED` or `DELIVER_IMMEDIATELY`.
  * DESIRED_STATE: The starting state for the subscription. The following values are supported: 
    * `ACTIVE`: The subscription exports Lite messages to Pub/Sub.
    * `PAUSED`: Exporting of Lite messages is suspended.
  * DEAD_LETTER_TOPIC_ID: The ID of an existing Lite topic to use as a dead-letter topic. The topic must be in the same location (zone or region) and project as the export subscription itself.
  * PUBSUB_TOPIC_NAME: The name of the Pub/Sub topic to export to. Example format: `projects/my-project-id/topics/my-topic-id`.



If the request is successful, the response is the Lite subscription in JSON format:
    
    
    {
      "deliveryConfig": {
          "deliveryRequirement": "DELIVERY_REQUIREMENT",
      },
      "exportConfig": {
          "desiredState": "DESIRED_STATE",
          "deadLetterTopic": "projects/PROJECT_NUMBER/locations/LOCATION/topics/DEAD_LETTER_TOPIC_ID",
          "pubsubConfig": {
              "topic": "PUBSUB_TOPIC_NAME"
          },
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/subscriptions/SUBSCRIPTION_ID",
      "topic": "projects/PROJECT_NUMBER/locations/LOCATION/topics/TOPIC_ID",
    }
    

### Go

The following sample uses the major version of the Go Pub/Sub client library (v2). If you are still using the v1 library, see [the migration guide to v2](https://github.com/googleapis/google-cloud-go/blob/main/pubsub/MIGRATING.md). To see a list of v1 code samples, see [ the deprecated code samples](https://docs.cloud.google.com/pubsub/docs/samples?language=golang&text=deprecated).

Before trying this sample, follow the Go setup instructions in [Quickstart: Using Client Libraries](https://docs.cloud.google.com/pubsub/docs/create-topic-client-libraries). For more information, see the [Pub/Sub Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/pubsub/v2).
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/pubsublite"
    )
    
    func createPubsubExportSubscription(w io.Writer, projectID, region, location, topicID, subID, pubsubTopicID string) error {
    	// projectID := "my-project-id"
    	// region := "us-central1"
    	// NOTE: location can be either a region ("us-central1") or a zone ("us-central1-a")
    	// For a list of valid locations, see https://cloud.google.com/pubsub/lite/docs/locations.
    	// location := "us-central1"
    	// NOTE: topic and subscription must be in the same region/zone (e.g. "us-central1-a")
    	// topicID := "my-topic"
    	// subID := "my-subscription"
    	// pubsubTopicID := "destination-topic-id"
    	ctx := context.Background()
    	client, err := pubsublite.NewAdminClient(ctx, region)
    	if err != nil {
    		return fmt.Errorf("pubsublite.NewAdminClient: %w", err)
    	}
    	defer client.Close()
    
    	// Initialize the subscription to the oldest retained messages for each
    	// partition.
    	targetLocation := pubsublite.[AtTargetLocation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsublite/latest/index.html#cloud_google_com_go_pubsublite_CreateSubscriptionOption_AtTargetLocation)(pubsublite.[Beginning](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsublite/latest/index.html#cloud_google_com_go_pubsublite_End_Beginning))
    
    	sub, err := client.CreateSubscription(ctx, pubsublite.[SubscriptionConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsublite/latest/index.html#cloud_google_com_go_pubsublite_SubscriptionConfig){
    		Name:                fmt.Sprintf("projects/%s/locations/%s/subscriptions/%s", projectID, location, subID),
    		Topic:               fmt.Sprintf("projects/%s/locations/%s/topics/%s", projectID, location, topicID),
    		DeliveryRequirement: pubsublite.[DeliverImmediately](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsublite/latest/index.html#cloud_google_com_go_pubsublite_UnspecifiedDeliveryRequirement_DeliverImmediately_DeliverAfterStored), // Can also be DeliverAfterStored.
    		// Configures an export subscription that writes messages to a Pub/Sub topic.
    		ExportConfig: &pubsublite.ExportConfig{
    			DesiredState: pubsublite.[ExportActive](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsublite/latest/index.html#cloud_google_com_go_pubsublite_UnspecifiedExportState_ExportActive_ExportPaused_ExportPermissionDenied_ExportResourceNotFound), // Can also be ExportPaused.
    			Destination: &pubsublite.[PubSubDestinationConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsublite/latest/index.html#cloud_google_com_go_pubsublite_PubSubDestinationConfig){
    				Topic: fmt.Sprintf("projects/%s/topics/%s", projectID, pubsubTopicID),
    			},
    		},
    	}, targetLocation)
    	if err != nil {
    		return fmt.Errorf("client.CreateSubscription got err: %w", err)
    	}
    	fmt.Fprintf(w, "Created export subscription: %s\n", sub.Name)
    	return nil
    }
    

### Java

Before running this sample, follow the Java setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
    import com.google.api.gax.rpc.[AlreadyExistsException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.AlreadyExistsException.html);
    import com.google.cloud.pubsublite.[AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html);
    import com.google.cloud.pubsublite.[AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html);
    import com.google.cloud.pubsublite.[BacklogLocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.BacklogLocation.html);
    import com.google.cloud.pubsublite.[CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html);
    import com.google.cloud.pubsublite.[CloudRegionOrZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegionOrZone.html);
    import com.google.cloud.pubsublite.[CloudZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudZone.html);
    import com.google.cloud.pubsublite.[ProjectNumber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectNumber.html);
    import com.google.cloud.pubsublite.[SeekTarget](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SeekTarget.html);
    import com.google.cloud.pubsublite.[SubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.SubscriptionName.html);
    import com.google.cloud.pubsublite.[SubscriptionPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath.html);
    import com.google.cloud.pubsublite.[TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.TopicName.html);
    import com.google.cloud.pubsublite.[TopicPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath.html);
    import com.google.cloud.pubsublite.proto.[ExportConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.ExportConfig.html);
    import com.google.cloud.pubsublite.proto.[ExportConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.ExportConfig.html).PubSubConfig;
    import com.google.cloud.pubsublite.proto.[ExportConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.ExportConfig.html).State;
    import com.google.cloud.pubsublite.proto.[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Subscription.html);
    import com.google.cloud.pubsublite.proto.[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Subscription.html).DeliveryConfig;
    import com.google.cloud.pubsublite.proto.[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Subscription.html).DeliveryConfig.DeliveryRequirement;
    import java.util.concurrent.ExecutionException;
    
    public class CreatePubsubExportSubscriptionExample {
    
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String cloudRegion = "your-cloud-region";
        char zoneId = 'b';
        String topicId = "your-topic-id";
        String subscriptionId = "your-subscription-id";
        String pubsubTopicId = "destination-topic-id";
        long projectNumber = Long.parseLong("123456789");
        // True if using a regional location. False if using a zonal location.
        // https://cloud.google.com/pubsub/lite/docs/topics
        boolean regional = false;
    
        createPubsubExportSubscriptionExample(
            cloudRegion, zoneId, projectNumber, topicId, subscriptionId, pubsubTopicId, regional);
      }
    
      public static void createPubsubExportSubscriptionExample(
          String cloudRegion,
          char zoneId,
          long projectNumber,
          String topicId,
          String subscriptionId,
          String pubsubTopicId,
          boolean regional)
          throws Exception {
    
        [CloudRegionOrZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegionOrZone.html) location;
        if (regional) {
          location = [CloudRegionOrZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegionOrZone.html).of([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(cloudRegion));
        } else {
          location = [CloudRegionOrZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegionOrZone.html).of([CloudZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudZone.html).of([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(cloudRegion), zoneId));
        }
    
        [TopicPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath.html) topicPath =
            [TopicPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath.html).newBuilder()
                .setProject([ProjectNumber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectNumber.html).of(projectNumber))
                .setLocation(location)
                .setName([TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.TopicName.html).of(topicId))
                .build();
    
        [SubscriptionPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath.html) subscriptionPath =
            [SubscriptionPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath.html).newBuilder()
                .setLocation(location)
                .setProject([ProjectNumber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectNumber.html).of(projectNumber))
                .setName([SubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.SubscriptionName.html).of(subscriptionId))
                .build();
    
        com.google.pubsub.v1.[TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.TopicName.html) pubsubTopicName =
            com.google.pubsub.v1.TopicName.of(String.valueOf(projectNumber), pubsubTopicId);
    
        [Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Subscription.html) subscription =
            [Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Subscription.html).newBuilder()
                .setDeliveryConfig(
                    // Possible values for DeliveryRequirement:
                    // - `DELIVER_IMMEDIATELY`
                    // - `DELIVER_AFTER_STORED`
                    // You may choose whether to wait for a published message to be successfully written
                    // to storage before the server delivers it to subscribers. `DELIVER_IMMEDIATELY` is
                    // suitable for applications that need higher throughput.
                    DeliveryConfig.newBuilder()
                        .setDeliveryRequirement(DeliveryRequirement.DELIVER_IMMEDIATELY))
                .setExportConfig(
                    // Configures an export subscription that writes messages to a Pub/Sub topic.
                    [ExportConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.ExportConfig.html).newBuilder()
                        // Possible values for State:
                        // - `ACTIVE`: enable message processing.
                        // - `PAUSED`: suspend message processing.
                        .setDesiredState(State.ACTIVE)
                        .setPubsubConfig(
                            PubSubConfig.newBuilder().setTopic(pubsubTopicName.toString())))
                .setName([subscriptionPath](https://docs.cloud.google.com/java/docs/reference/pubsublite-spark-sql-streaming/latest/com.google.cloud.pubsublite.spark.PslReadDataSourceOptions.html#com_google_cloud_pubsublite_spark_PslReadDataSourceOptions_subscriptionPath__).[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath.html#com_google_cloud_pubsublite_SubscriptionPath_toString__)())
                .setTopic([topicPath](https://docs.cloud.google.com/java/docs/reference/pubsublite-spark-sql-streaming/latest/com.google.cloud.pubsublite.spark.PslWriteDataSourceOptions.html#com_google_cloud_pubsublite_spark_PslWriteDataSourceOptions_topicPath__).[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath.html#com_google_cloud_pubsublite_TopicPath_toString__)())
                .build();
    
        // Target location within the message backlog that the subscription should be initialized to.
        [SeekTarget](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SeekTarget.html) initialLocation = [SeekTarget](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SeekTarget.html).of([BacklogLocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.BacklogLocation.html).BEGINNING);
    
        [AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html) adminClientSettings =
            [AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html).newBuilder().setRegion(location.[extractRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegionOrZone.html#com_google_cloud_pubsublite_CloudRegionOrZone_extractRegion__)()).build();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources, or
        // use "try-with-close" statement to do this automatically.
        try ([AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html) adminClient = [AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html).create(adminClientSettings)) {
          [Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Subscription.html) response = adminClient.createSubscription(subscription, initialLocation).get();
          System.out.println(response.getAllFields() + " created successfully.");
        } catch (ExecutionException e) {
          try {
            throw e.getCause();
          } catch ([AlreadyExistsException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.AlreadyExistsException.html) alreadyExists) {
            System.out.println("This subscription already exists.");
          } catch (Throwable throwable) {
            throwable.printStackTrace();
          }
        }
      }
    }

### Python

Before running this sample, follow the Python setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
    from google.api_core.exceptions import AlreadyExists
    from google.cloud.pubsub_v1 import PublisherClient
    from google.cloud.pubsublite import AdminClient, [Subscription](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.Subscription.html), ExportConfig
    from google.cloud.pubsublite.types import (
        BacklogLocation,
        CloudRegion,
        CloudZone,
        SubscriptionPath,
        TopicPath,
    )
    
    
    def create_lite_pubsub_export_subscription(
        project_number,
        cloud_region="us-central1",
        zone_id="a",
        topic_id="my-topic-id",
        subscription_id="my-subscription-id",
        pubsub_topic_id="destination-topic-id",
        regional=True,
        target_location=BacklogLocation.BEGINNING,
    ):
        if regional:
            location = CloudRegion(cloud_region)
        else:
            location = CloudZone(CloudRegion(cloud_region), zone_id)
    
        topic_path = TopicPath(project_number, location, topic_id)
        subscription_path = SubscriptionPath(project_number, location, subscription_id)
        destination_topic_path = PublisherClient.topic_path(project_number, pubsub_topic_id)
    
        subscription = Subscription(
            name=str(subscription_path),
            topic=str(topic_path),
            delivery_config=[Subscription](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.Subscription.html).DeliveryConfig(
                # Possible values for delivery_requirement:
                # - `DELIVER_IMMEDIATELY`
                # - `DELIVER_AFTER_STORED`
                # You may choose whether to wait for a published message to be successfully written
                # to storage before the server delivers it to subscribers. `DELIVER_IMMEDIATELY` is
                # suitable for applications that need higher throughput.
                delivery_requirement=[Subscription](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.types.Subscription.html).DeliveryConfig.DeliveryRequirement.DELIVER_IMMEDIATELY,
            ),
            # Configures an export subscription that writes messages to a Pub/Sub topic.
            export_config=ExportConfig(
                # Possible values for desired_state:
                # - `ACTIVE`: enable message processing.
                # - `PAUSED`: suspend message processing.
                desired_state=ExportConfig.State.ACTIVE,
                pubsub_config=ExportConfig.PubSubConfig(
                    topic=destination_topic_path,
                ),
            ),
        )
    
        # Initialize client that will be used to send requests across threads. This
        # client only needs to be created once, and can be reused for multiple requests.
        client = AdminClient(cloud_region)
        try:
            response = client.[create_subscription](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.admin_client.AdminClient.html#google_cloud_pubsublite_admin_client_AdminClient_create_subscription)(subscription, target_location)
            print(f"{response.name} created successfully.")
        except AlreadyExists:
            print(f"{subscription_path} already exists.")
    
    

## Update an export subscription

You can update Lite subscriptions with the Google Cloud console, the Google Cloud CLI, or the Pub/Sub Lite API. It can take up to 30 seconds for the new settings to be applied.

### Console

  1. Go to the **Lite Subscriptions** page.

[Go to Lite Subscriptions](https://console.cloud.google.com/cloudpubsub/liteSubscription)

  2. Click the Lite subscription ID.

  3. In the **Lite subscription details** page, click **Edit**.




### gcloud

To update a Lite subscription, use the [`gcloud pubsub lite-subscriptions update`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/update) command:
    
    
    gcloud pubsub lite-subscriptions update SUBSCRIPTION_ID \
    --location=LOCATION \
    --delivery-requirement=DELIVERY_REQUIREMENT \
    --export-pubsub-topic=PUBSUB_TOPIC_NAME \
    --export-dead-letter-topic=DEAD_LETTER_TOPIC_ID \
    --export-desired-state=DESIRED_STATE

Replace the following:

  * SUBSCRIPTION_ID: The ID of the Lite subscription
  * LOCATION: The [location](https://docs.cloud.google.com/pubsub/lite/docs/locations) of the Lite subscription.
  * DELIVERY_REQUIREMENT: Optional. The delivery requirement, either `deliver-after-stored` or `deliver-immediately`.
  * PUBSUB_TOPIC_NAME: Optional. The name of the Pub/Sub topic to export to. Specify the full name if the topic is in a different project: `projects/my-project-id/topics/my-topic-id`.
  * DEAD_LETTER_TOPIC_ID: The ID of an existing Lite topic to use as a dead-letter topic. The topic must be in the same location (zone or region) and project as the export subscription itself.
  * DESIRED_STATE: Optional. The desired state of the subscription. The following values are supported: 
    * `active`: The subscription exports Lite messages to Pub/Sub. (Default.)
    * `paused`: Exporting of Lite messages is suspended.



If the request is successful, the command line displays the Lite subscription:
    
    
    Updated subscription [SUBSCRIPTION_ID].
    deliveryConfig:
    deliveryRequirement: DELIVERY_REQUIREMENT
    exportConfig:
    currentState: DESIRED_STATE
    deadLetterTopic: projects/PROJECT_NUMBER/locations/LOCATION/topics/DEAD_LETTER_TOPIC_ID
    desiredState: DESIRED_STATE
    pubsubConfig:
      topic: PUBSUB_TOPIC_NAME
    name: projects/PROJECT_NUMBER/locations/LOCATION/subscriptions/SUBSCRIPTION_ID
    topic: projects/PROJECT_NUMBER/locations/LOCATION/topics/TOPIC_ID

### Protocol

To update a Lite subscription, send a `PATCH` request like the following:
    
    
    PATCH https://REGION-pubsublite.googleapis.com/v1/admin/projects/PROJECT_NUMBER/locations/LOCATION/subscriptions/SUBSCRIPTION_ID?updateMask=deliveryConfig.deliveryRequirement,exportConfig
    Authorization: Bearer $(gcloud auth print-access-token)
    

Replace the following:

  * REGION: The region where the Lite subscription was created.
  * PROJECT_NUMBER: The project number of project where the Lite subscription was created.
  * LOCATION: The location where the Lite subscription was created.
  * SUBSCRIPTION_ID: The ID of the Lite subscription.



Specify the following fields in the request body:
    
    
    {
      "deliveryConfig": {
          "deliveryRequirement": "DELIVERY_REQUIREMENT",
      },
      "exportConfig": {
          "desiredState": "DESIRED_STATE",
          "deadLetterTopic": "projects/PROJECT_NUMBER/locations/LOCATION/topics/DEAD_LETTER_TOPIC_ID",
          "pubsubConfig": {
              "topic": "PUBSUB_TOPIC_NAME"
          }
      }
    }

Replace the following:

  * DELIVERY_REQUIREMENT: The delivery requirement, either `DELIVER_AFTER_STORED` or `DELIVER_IMMEDIATELY`.
  * DESIRED_STATE: The desired state for the subscription. The following values are supported: 
    * `ACTIVE`: The subscription exports Lite messages to Pub/Sub.
    * `PAUSED`: Exporting of Lite messages is suspended.
  * DEAD_LETTER_TOPIC_ID: The ID of an existing Lite topic to use as a dead-letter topic. The topic must be in the same location (zone or region) and project as the export subscription itself.
  * PUBSUB_TOPIC_NAME: The name of the destination Pub/Sub topic. Example format: `projects/my-project-id/topics/my-topic-id`.



If the request is successful, the response is the Lite subscription in JSON format:
    
    
    {
    "deliveryConfig": {
      "deliveryRequirement": "DELIVERY_REQUIREMENT",
    },
    "exportConfig": {
      "desiredState": "DESIRED_STATE",
      "deadLetterTopic": "projects/PROJECT_NUMBER/locations/LOCATION/topics/DEAD_LETTER_TOPIC_ID",
      "pubsubConfig": { "topic": "PUBSUB_TOPIC_NAME" }
    },
    "name": "projects/PROJECT_NUMBER/locations/LOCATION/subscriptions/SUBSCRIPTION_ID",
    "topic": "projects/PROJECT_NUMBER/locations/LOCATION/topics/TOPIC_ID",
    }
    

## Pause or start an export subscription

Export subscriptions have a setting called _desired state_ , which has one of two values:

  * **Active** : The subscription exports Lite messages to Pub/Sub.
  * **Paused** : Exporting of Lite messages is suspended.



To change the desired state in the Google Cloud console:

  1. Go to the **Lite Subscriptions** page.

[Go to Lite Subscriptions](https://console.cloud.google.com/cloudpubsub/liteSubscription)

  2. Click the Lite subscription ID.

  3. In the **Lite subscription details** page, click **Pause** or **Start**.




You can also update the desired state by using the Google Cloud CLI or the Pub/Sub Lite API. See Update an export subscription.

## Best practices

This section describes some best practices when using export subscriptions.

### Reservations

We recommend using an export subscription with a [reservation](https://docs.cloud.google.com/pubsub/lite/docs/reservations), rather than explicitly setting the throughput capacity of the subscription.

### Message compatibility

If a Pub/Sub Lite message is not compatible with Pub/Sub, the export subscription does not publish the message to Pub/Sub. Instead, it places the message in the dead-letter topic, if one was assigned. If no dead-letter topic was assigned, incompatible messages are simply dropped.

When publishing messages to the Lite topic, be aware of the following compatibility issues:

  * **Keys**. Pub/Sub Lite keys have type `bytes`, while Pub/Sub ordering keys are type `string`. To be compatible, the Pub/Sub Lite key must contain only UTF-8 characters.

  * **Attributes**. Message attributes have the following requirements:

    * In order to be compatible, all Pub/Sub Lite message attributes must have a single value. Pub/Sub Lite supports message attributes with multiple values, but Pub/Sub only supports single-value attributes.
    * The message attributes must not exceed the [Pub/Sub message limits](https://docs.cloud.google.com/pubsub/quotas#resource_limits), including maximum attributes per message, and maximum key and value size per attribute.



### Dead-letter topic

To retain and handle incompatible messages, we recommend using a dead-letter topic. You can assign a dead-letter topic when you create the export subscription, or you can update an existing export subscription to use a dead-letter topic. If the subscription receives a message that is incompatible with Pub/Sub, it publishes the message to the dead-letter topic.

A dead-letter topic is a regular Pub/Sub Lite topic. It must be in the same location and project as the export subscription, and it must be a different topic from the source topic.

Typically, a dead-letter topic has low throughput utilization. Therefore, we recommend assigning a reservation to the dead-letter topic, rather than allocate throughput to the topic.

### Delivery errors

An export subscription attempts to deliver all compatible messages to the destination Pub/Sub topic. If message delivery fails, the export subscription is suspended. To find the category of error, check the `subscription/export_status` metric. The following values indicate an error:

  * `PERMISSION_DENIED`: Insufficient permissions to export messages.
  * `NOT_FOUND`: One or more resources was not found; for example, the destination topic does not exist.



For more information on troubleshooting, see Troubleshoot export subscriptions.

After you resolve the error, the export subscription is automatically restarted due to periodic retries.

## Pricing

You are charged for the Pub/Sub Lite and Pub/Sub resources that the export subscription consumes. Specifically, you are charged for the allocated subscription throughput and storage on the Pub/Sub Lite subscription, which are configured for the Pub/Sub Lite topic. You are also charged for publishing to the destination Pub/Sub topic. See [Pub/Sub pricing](https://cloud.google.com/pubsub/pricing).

There are no additional charges for using the export feature, and there is no price difference between Pub/Sub Lite export subscriptions and standard subscriptions.

## Troubleshoot export subscriptions

This section describes some troubleshooting tips for export subscriptions.

### The export subscription is paused

If the subscription is paused, no messages are exported.

To detect this issue:

  * Google Cloud console: View the subscription details. If the subscription is paused, **Desired state** and **Current state** are `Paused`.

  * Metrics: The `subscription/export_status` metric is `PAUSED`.




To resolve this issue, start the subscription.

### The destination topic or dead-letter topic was deleted

If you delete the Pub/Sub topic attached to an export subscription, or delete the dead-letter topic, an error occurs.

To detect this issue:

  * Google Cloud console: View the subscription details. If the topic was deleted, the **Current state** is `Not found`.

  * Metrics: The `subscription/export_status` metric. If the topic was deleted, the value is `NOT_FOUND`.




To resolve this issue, check the destination Pub/Sub topic and the dead-letter topic (if one was configured).

If the destination Pub/Sub was deleted, recreate the topic with the same name. The export subscription resumes publishing, assuming the permissions did not change.

If the dead-letter topic was deleted, create a new dead-letter topic and update the export subscription to reference it.

### Incompatible messages

If messages are incompatible with Pub/Sub, they are not exported.

To detect this issue:

  * Metrics: The `subscription/unexportable_message_count` metric shows the count of incompatible messages that could not be exported.



To resolve this issue, use a dead-letter topic to retain the incompatible messages. Examine the messages to determine the cause, then transform and republish them if necessary. See Message compatibility.

### Export is throttled

To detect this issue:

  * Metrics: The `subscription/flow_control_status` metric shows a flow-control reason of `NO_CLIENT_TOKENS`, which indicates that the per-partition limit of outstanding bytes or messages has been reached. Until the issue is resolved, the backlog will increase for associated export subscriptions.



This error has several possible root causes. Most of the possible causes occur on the back end, but check for the following:

  * Ensure that you publish Lite messages sharing the same key at a rate of less than 1 MiB/s per key. The export subscription writes Lite message keys as Pub/Sub ordering keys, and Pub/Sub has a 1 MiB/s [limit](https://docs.cloud.google.com/pubsub/quotas#resource_limits) on each ordering key. Exceeding this limit can cause throttling.



### User not authorized to perform this action

The Pub/Sub Lite service agent must have permissions to publish to the destination Pub/Sub topic.

To detect this issue:

  * Google Cloud console: View the subscription details. If there are permission errors, the **Current state** is `Permission denied`.

  * Metrics: The `subscription/export_status` metric is `PERMISSION_DENIED`.




For example, the following situations can cause this error:

  * The Pub/Sub Lite service agent is missing the correct permission or role to publish messages to the destination Pub/Sub topic in a different project.
  * The service agent was removed from the IAM policy of the export subscription's parent project.
  * The Pub/Sub Lite service agent is still being set up. A service agent is automatically created when you create the first export subscription in a project. The permission error should be automatically resolved within 10 minutes.



To resolve the issue, check if the service agent was granted the correct permission or role. See Service agents.

## What's next

[Choose between Pub/Sub or Pub/Sub Lite](https://docs.cloud.google.com/pubsub/docs/choosing-pubsub-or-lite).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
