---
url: https://docs.cloud.google.com/pubsub/lite/docs/samples/pubsublite-create-pubsub-export-subscription/
title: Create a Lite subscription that writes messages to a Pub/Sub topic \u00a0|\u00a0 Pub/Sub Lite \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:16.778176+00:00
---

# Create a Lite subscription that writes messages to a Pub/Sub topic  |  Pub/Sub Lite  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/lite/docs/samples/pubsublite-create-pubsub-export-subscription/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Pub/Sub Lite ](https://docs.cloud.google.com/pubsub/lite/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/lite/docs/samples)



#  Create a Lite subscription that writes messages to a Pub/Sub topic Stay organized with collections  Save and categorize content based on your preferences. 

Create a Lite subscription that writes messages to a Pub/Sub topic

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Export Pub/Sub Lite messages to Pub/Sub](https://docs.cloud.google.com/pubsub/lite/docs/export-pubsub)



## Code sample

### Go

To authenticate to Pub/Sub Lite, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

To authenticate to Pub/Sub Lite, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

To authenticate to Pub/Sub Lite, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsublite). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
