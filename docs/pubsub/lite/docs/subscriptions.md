---
url: https://docs.cloud.google.com/pubsub/lite/docs/subscriptions/
title: Create and manage Lite subscriptions \u00a0|\u00a0 Pub/Sub Lite \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:45:48.156174+00:00
---

# Create and manage Lite subscriptions  |  Pub/Sub Lite  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/lite/docs/subscriptions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Pub/Sub Lite ](https://docs.cloud.google.com/pubsub/lite/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/lite/docs/publish-receive-messages-console)



Send feedback 

#  Create and manage Lite subscriptions Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Pub/Sub Lite is deprecated. Effective January 31, 2027, Pub/Sub Lite will be turned down.   


  * Current customers: Pub/Sub Lite remains functional until January 31, 2027.   
If you have not used Pub/Sub Lite within the 90-day period preceding July 15, 2025 (April 15, 2025 - July 15, 2025), you won't be able to access Pub/Sub Lite starting on July 15, 2025. 
  * New customers: Pub/Sub Lite is no longer available for new customers after September 24, 2024.



You can migrate your Pub/Sub Lite service to [Google Cloud Managed Service for Apache Kafka](https://docs.cloud.google.com/pubsub/lite/docs/migrate-pubsub-lite-to-managed-service-for-apache-kafka) or [Pub/Sub](https://docs.cloud.google.com/pubsub/lite/docs/migrate-pubsub-lite-to-pubsub).

Subscribers use a Lite subscription to read messages from a Lite topic. When you create a Lite subscription, you attach it to a Lite topic. You can attach many Lite subscriptions to a single Lite topic.

**Key Point:** Understand why you need a Lite subscription, the properties required to create a Lite subscription, and then use the Google Cloud console, the Google Cloud CLI, or the Pub/Sub Lite API to create and manage a Lite subscription.

There are two types of subscription:

  * **Standard subscription**. Create a standard subscription when you have a client that needs to read messages from the Lite topic topic.
  * **Export subscription**. Create an export subscription when you need to export Lite messages to Pub/Sub. For more information, see [Export Pub/Sub Lite messages to Pub/Sub](https://docs.cloud.google.com/pubsub/lite/docs/export-pubsub).



## Properties of a Lite subscription

A subscription for a zonal Lite topic has identical properties to a subscription for a regional Lite topic, except for the following:

  * Location type, a zone or a region, used in the resource name. An example of a region location is `us-central1`; an example of a zone location is `us-central1-a`.

  * Reliability. See [Data replication in a Lite topic](https://docs.cloud.google.com/pubsub/lite/docs/topics#data_replication_in_a_lite_topic) to learn more about reliability differences between regional and zonal topics.




## Delivery requirement for messages

A temporary failure in writing a message to storage causes the publisher to retry sending the message. These retries are transparent to the end-user. Lite subscriptions have a _delivery requirement_ property that changes how subscriptions react to these message retries. You can set this property to one of the following two options:

  * **Deliver messages immediately.** With this option enabled, the subscriber clients receive all messages after they arrive at the server. This process is not dependent on the status of the messages being written to disk. Offsets are not reused, but messages with offsets that are not written to storage might not be re-readable following a [seek](https://docs.cloud.google.com/pubsub/lite/docs/seek) operation.

  * **Deliver messages after stored.** With this option enabled, the subscriber does not receive messages until they are written to disk. The messages are guaranteed to be re-readable after a seek operation. Enabling this option increases the end-to-end latency for receiving messages from the publisher to the subscriber.




## Guidelines to name a subscription

A Pub/Sub Lite resource name uniquely identifies a Pub/Sub Lite resource, such as a topic, subscription, or reservation. The resource name must fit the following format:

`projects/project-identifier/collection/ID`

  * `project-identifier`: Must be the project ID or project number, available from the Google Cloud console. For example, `my-cool-project` is a project ID. `123456789123` is a project number.

  * `collection`: Must be one of `topics`, `subscriptions`, or `reservations`.

  * `ID`: Must conform to the following guidelines:

    * Not begin with the string `goog`
    * Start with a letter
    * Contain between 3 and 255 characters
    * Contain only the following characters: Letters `[A-Za-z]`, numbers `[0-9]`, dashes `-`, underscores `_`, periods `.`, tildes `~`, plus signs `+`, and percent signs `%`

You can use the special characters in the preceding list in resource names without URL-encoding. However, you must ensure that any other special characters are properly encoded or decoded when you use them in URLs. For example, `mi-tópico` is an invalid _ID_. However, `mi-t%C3%B3pico` is valid. This format is important when you make REST calls.




**Note:** The [ client libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries) can take different approaches to naming resources, such as specifying the _project-identifier_ and the _ID_ in separate fields.

## Create a Lite subscription

A Lite subscription must be in the same project and location as the Lite topic to which the Lite subscription is attached.

To create a Lite topic, see [Create and manage a Lite topic](https://docs.cloud.google.com/pubsub/lite/docs/topics).

For a list of the available locations, see [Pub/Sub Lite locations](https://docs.cloud.google.com/pubsub/lite/docs/locations).

You can create a Lite subscription with the Google Cloud console, the Google Cloud CLI, or the Pub/Sub Lite API.

For information about creating an export subscription, see [Export Pub/Sub Lite messages to Pub/Sub](https://docs.cloud.google.com/pubsub/lite/docs/export-pubsub).

### Console

  1. Go to the **Lite Subscriptions** page.

[Go to Lite Subscriptions](https://console.cloud.google.com/cloudpubsub/liteSubscription)

  2. Click **Create Lite subscription**.

  3. Enter a **Lite subscription ID**.

  4. Choose a Lite topic to receive messages from.

  5. Choose **Deliver messages immediately** or **Deliver messages after stored**.

  6. Choose a type of **Starting offset**.

  7. Choose a **Delivery type**.

  8. Click **Create**.




### gcloud

To create a Lite subscription, use the [`gcloud pubsub lite-subscriptions create`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/create) command:
    
    
    gcloud pubsub lite-subscriptions create SUBSCRIPTION_ID \
      --location=LOCATION \
      --topic=TOPIC_ID \
      --delivery-requirement=DELIVERY_REQUIREMENT

Replace the following:

  * SUBSCRIPTION_ID: the ID of the Lite subscription

  * LOCATION: the name of [a location that Pub/Sub Lite supports](https://docs.cloud.google.com/pubsub/lite/docs/locations)

  * TOPIC_ID: the ID of the Lite topic to attach to the Lite subscription

  * DELIVERY_REQUIREMENT: `deliver-after-stored` or `deliver-immediately`




If the request is successful, the command line displays a confirmation:
    
    
    Created [SUBSCRIPTION_ID].
    

### Protocol

To create a Lite subscription, send a `POST` request like the following:
    
    
    POST https://REGION-pubsublite.googleapis.com/v1/admin/projects/PROJECT_NUMBER/locations/LOCATION/subscriptions/SUBSCRIPTION_ID
    Authorization: Bearer $(gcloud auth print-access-token)
    

Replace the following:

  * REGION: the region to store the Lite subscription in

  * PROJECT_NUMBER: the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) of the project to create the Lite subscription in

  * LOCATION: the name of [a location that Pub/Sub Lite supports](https://docs.cloud.google.com/pubsub/lite/docs/locations)

  * SUBSCRIPTION_ID: the ID of the Lite subscription




Specify the following fields in the request body:
    
    
    {
      "topic": projects/PROJECT_NUMBER/locations/LOCATION/topics/TOPIC_ID,
      "deliveryConfig": {
        "deliveryRequirement": DELIVERY_REQUIREMENT,
       }
    }

Replace DELIVERY_REQUIREMENT with `deliver-after-stored` or `deliver-immediately`.

If the request is successful, the response is the Lite subscription in JSON format:
    
    
    {
      "deliveryConfig": {
        "deliveryRequirement": DELIVERY_REQUIREMENT,
       }
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/subscriptions/SUBSCRIPTION_ID",
      "topic": "projects/PROJECT_NUMBER/locations/LOCATION/topics/TOPIC_ID",
    }
    

### Go

Before running this sample, follow the Go setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/pubsublite"
    )
    
    func createSubscription(w io.Writer, projectID, region, location, topicID, subID string) error {
    	// projectID := "my-project-id"
    	// region := "us-central1"
    	// NOTE: location can be either a region ("us-central1") or a zone ("us-central1-a")
    	// For a list of valid locations, see https://cloud.google.com/pubsub/lite/docs/locations.
    	// location := "us-central1"
    	// NOTE: topic and subscription must be in the same region/zone (e.g. "us-central1-a")
    	// topicID := "my-topic"
    	// subID := "my-subscription"
    	ctx := context.Background()
    	client, err := pubsublite.NewAdminClient(ctx, region)
    	if err != nil {
    		return fmt.Errorf("pubsublite.NewAdminClient: %w", err)
    	}
    	defer client.Close()
    
    	sub, err := client.CreateSubscription(ctx, pubsublite.[SubscriptionConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsublite/latest/index.html#cloud_google_com_go_pubsublite_SubscriptionConfig){
    		Name:                fmt.Sprintf("projects/%s/locations/%s/subscriptions/%s", projectID, location, subID),
    		Topic:               fmt.Sprintf("projects/%s/locations/%s/topics/%s", projectID, location, topicID),
    		DeliveryRequirement: pubsublite.[DeliverImmediately](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsublite/latest/index.html#cloud_google_com_go_pubsublite_UnspecifiedDeliveryRequirement_DeliverImmediately_DeliverAfterStored), // can also be DeliverAfterStored
    	})
    	if err != nil {
    		return fmt.Errorf("client.CreateSubscription got err: %w", err)
    	}
    	fmt.Fprintf(w, "Created subscription: %s\n", sub.Name)
    	return nil
    }
    

### Java

Before running this sample, follow the Java setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
    import com.google.api.gax.rpc.[AlreadyExistsException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.AlreadyExistsException.html);
    import com.google.cloud.pubsublite.[AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html);
    import com.google.cloud.pubsublite.[AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html);
    import com.google.cloud.pubsublite.[CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html);
    import com.google.cloud.pubsublite.[CloudRegionOrZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegionOrZone.html);
    import com.google.cloud.pubsublite.[CloudZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudZone.html);
    import com.google.cloud.pubsublite.[ProjectNumber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectNumber.html);
    import com.google.cloud.pubsublite.[SubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.SubscriptionName.html);
    import com.google.cloud.pubsublite.[SubscriptionPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath.html);
    import com.google.cloud.pubsublite.[TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.TopicName.html);
    import com.google.cloud.pubsublite.[TopicPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath.html);
    import com.google.cloud.pubsublite.proto.[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Subscription.html);
    import com.google.cloud.pubsublite.proto.[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Subscription.html).DeliveryConfig;
    import com.google.cloud.pubsublite.proto.[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Subscription.html).DeliveryConfig.DeliveryRequirement;
    import java.util.concurrent.ExecutionException;
    
    public class CreateSubscriptionExample {
    
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String cloudRegion = "your-cloud-region";
        char zoneId = 'b';
        String topicId = "your-topic-id";
        String subscriptionId = "your-subscription-id";
        long projectNumber = Long.parseLong("123456789");
        // True if using a regional location. False if using a zonal location.
        // https://cloud.google.com/pubsub/lite/docs/topics
        boolean regional = false;
    
        createSubscriptionExample(
            cloudRegion, zoneId, projectNumber, topicId, subscriptionId, regional);
      }
    
      public static void createSubscriptionExample(
          String cloudRegion,
          char zoneId,
          long projectNumber,
          String topicId,
          String subscriptionId,
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
                .setName([subscriptionPath](https://docs.cloud.google.com/java/docs/reference/pubsublite-spark-sql-streaming/latest/com.google.cloud.pubsublite.spark.PslReadDataSourceOptions.html#com_google_cloud_pubsublite_spark_PslReadDataSourceOptions_subscriptionPath__).[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath.html#com_google_cloud_pubsublite_SubscriptionPath_toString__)())
                .setTopic([topicPath](https://docs.cloud.google.com/java/docs/reference/pubsublite-spark-sql-streaming/latest/com.google.cloud.pubsublite.spark.PslWriteDataSourceOptions.html#com_google_cloud_pubsublite_spark_PslWriteDataSourceOptions_topicPath__).[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath.html#com_google_cloud_pubsublite_TopicPath_toString__)())
                .build();
    
        [AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html) adminClientSettings =
            [AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html).newBuilder().setRegion([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(cloudRegion)).build();
    
        try ([AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html) adminClient = [AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html).create(adminClientSettings)) {
          [Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Subscription.html) response = adminClient.createSubscription(subscription).get();
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
    from google.cloud.pubsublite import [AdminClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.admin_client.AdminClient.html), Subscription
    from google.cloud.pubsublite.types import (
        [CloudRegion](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.CloudRegion.html),
        [CloudZone](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.CloudZone.html),
        [SubscriptionPath](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.SubscriptionPath.html),
        [TopicPath](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.TopicPath.html),
    )
    
    # TODO(developer):
    # project_number = 1122334455
    # cloud_region = "us-central1"
    # zone_id = "a"
    # topic_id = "your-topic-id"
    # subscription_id = "your-subscription-id"
    # regional = True
    
    if regional:
        location = CloudRegion(cloud_region)
    else:
        location = CloudZone(CloudRegion(cloud_region), zone_id)
    
    topic_path = TopicPath(project_number, location, topic_id)
    subscription_path = SubscriptionPath(project_number, location, subscription_id)
    
    subscription = Subscription(
        name=str(subscription_path),
        topic=str(topic_path),
        delivery_config=Subscription.DeliveryConfig(
            # Possible values for delivery_requirement:
            # - `DELIVER_IMMEDIATELY`
            # - `DELIVER_AFTER_STORED`
            # You may choose whether to wait for a published message to be successfully written
            # to storage before the server delivers it to subscribers. `DELIVER_IMMEDIATELY` is
            # suitable for applications that need higher throughput.
            delivery_requirement=Subscription.DeliveryConfig.DeliveryRequirement.DELIVER_IMMEDIATELY,
        ),
    )
    
    client = AdminClient(cloud_region)
    try:
        response = client.[create_subscription](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.admin_client.AdminClient.html#google_cloud_pubsublite_admin_client_AdminClient_create_subscription)(subscription)
        print(f"{response.name} created successfully.")
    except AlreadyExists:
        print(f"{subscription_path} already exists.")

After creating a Lite subscription to a Lite topic, you can [receive messages](https://docs.cloud.google.com/pubsub/lite/docs/subscribing) from the Lite subscription.

## Update a Lite subscription

You can update Lite subscriptions with the Google Cloud console, the Google Cloud CLI, or the Pub/Sub Lite API.

### Console

  1. Go to the **Lite Subscriptions** page.

[Go to Lite Subscriptions](https://console.cloud.google.com/cloudpubsub/liteSubscription)

  2. Click the Lite subscription ID.

  3. In the **Lite subscription details** page, click **Edit**.




### gcloud

To update a Lite subscription, use the [`gcloud pubsub lite-subscriptions update`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/update) command:
    
    
    gcloud pubsub lite-subscriptions update SUBSCRIPTION_ID \
      --location=LOCATION \
      --delivery-requirement=DELIVERY_REQUIREMENT

Replace the following:

  * SUBSCRIPTION_ID: the ID of the Lite subscription

  * LOCATION: the name of the location that the Lite subscription is in

  * DELIVERY_REQUIREMENT: `deliver-after-stored` or `deliver-immediately`




If the request is successful, the command line displays the Lite subscription:
    
    
    deliveryConfig:
      deliveryRequirement: DELIVERY_REQUIREMENT
    name: projects/PROJECT_NUMBER/locations/LOCATION/subscriptions/SUBSCRIPTION_ID
    topic: projects/PROJECT_NUMBER/locations/LOCATION/topics/TOPIC_ID
    

### Protocol

To update a Lite subscription, send a `PATCH` request like the following:
    
    
    PATCH https://REGION-pubsublite.googleapis.com/v1/admin/projects/PROJECT_NUMBER/locations/LOCATION/subscriptions/SUBSCRIPTION_ID?updateMask=deliveryConfig.deliveryRequirement
    Authorization: Bearer $(gcloud auth print-access-token)
    

Replace the following:

  * REGION: the region to store the Lite subscription in

  * PROJECT_NUMBER: the project number of the project with the Lite subscription

  * LOCATION: the name of the location that the Lite subscription is in

  * SUBSCRIPTION_ID: the ID of the Lite subscription




Specify the following fields in the request body:
    
    
    {
      "deliveryConfig": {
        "deliveryRequirement": DELIVERY_REQUIREMENT,
       }
    }

Replace DELIVERY_REQUIREMENT with `deliver-after-stored` or `deliver-immediately`.

If the request is successful, the response is the Lite subscription in JSON format:
    
    
    {
      "deliveryConfig": {
        "deliveryRequirement": DELIVERY_REQUIREMENT,
       }
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/subscriptions/SUBSCRIPTION_ID",
      "topic": "projects/PROJECT_NUMBER/locations/LOCATION/topics/TOPIC_ID",
    }
    

### Go

Before running this sample, follow the Go setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/pubsublite"
    )
    
    func updateSubscription(w io.Writer, projectID, region, location, subID string) error {
    	// projectID := "my-project-id"
    	// region := "us-central1"
    	// NOTE: location can be either a region ("us-central1") or a zone ("us-central1-a")
    	// For a list of valid locations, see https://cloud.google.com/pubsub/lite/docs/locations.
    	// location := "us-central1"
    	// subID := "my-subscription"
    	ctx := context.Background()
    	client, err := pubsublite.NewAdminClient(ctx, region)
    	if err != nil {
    		return fmt.Errorf("pubsublite.NewAdminClient: %w", err)
    	}
    	defer client.Close()
    
    	subPath := fmt.Sprintf("projects/%s/locations/%s/subscriptions/%s", projectID, location, subID)
    	config := pubsublite.[SubscriptionConfigToUpdate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsublite/latest/index.html#cloud_google_com_go_pubsublite_SubscriptionConfigToUpdate){
    		Name:                subPath,
    		DeliveryRequirement: pubsublite.[DeliverAfterStored](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsublite/latest/index.html#cloud_google_com_go_pubsublite_UnspecifiedDeliveryRequirement_DeliverImmediately_DeliverAfterStored),
    	}
    	updatedCfg, err := client.UpdateSubscription(ctx, config)
    	if err != nil {
    		return fmt.Errorf("client.UpdateSubscription got err: %w", err)
    	}
    	fmt.Fprintf(w, "Updated subscription: %#v\n", updatedCfg)
    	return nil
    }
    

### Java

Before running this sample, follow the Java setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
    import com.google.api.gax.rpc.[NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html);
    import com.google.cloud.pubsublite.[AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html);
    import com.google.cloud.pubsublite.[AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html);
    import com.google.cloud.pubsublite.[CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html);
    import com.google.cloud.pubsublite.[CloudRegionOrZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegionOrZone.html);
    import com.google.cloud.pubsublite.[CloudZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudZone.html);
    import com.google.cloud.pubsublite.[ProjectNumber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectNumber.html);
    import com.google.cloud.pubsublite.[SubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.SubscriptionName.html);
    import com.google.cloud.pubsublite.[SubscriptionPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath.html);
    import com.google.cloud.pubsublite.proto.[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Subscription.html);
    import com.google.cloud.pubsublite.proto.[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Subscription.html).DeliveryConfig;
    import com.google.cloud.pubsublite.proto.[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Subscription.html).DeliveryConfig.DeliveryRequirement;
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import java.util.concurrent.ExecutionException;
    
    public class UpdateSubscriptionExample {
    
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String cloudRegion = "your-cloud-region";
        char zoneId = 'b';
        // Choose an existing subscription.
        String subscriptionId = "your-subscription-id";
        long projectNumber = Long.parseLong("123456789");
        // True if using a regional location. False if using a zonal location.
        // https://cloud.google.com/pubsub/lite/docs/topics
        boolean regional = false;
    
        updateSubscriptionExample(cloudRegion, zoneId, projectNumber, subscriptionId, regional);
      }
    
      public static void updateSubscriptionExample(
          String cloudRegion, char zoneId, long projectNumber, String subscriptionId, boolean regional)
          throws Exception {
    
        [CloudRegionOrZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegionOrZone.html) location;
        if (regional) {
          location = [CloudRegionOrZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegionOrZone.html).of([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(cloudRegion));
        } else {
          location = [CloudRegionOrZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegionOrZone.html).of([CloudZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudZone.html).of([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(cloudRegion), zoneId));
        }
    
        [SubscriptionPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath.html) subscriptionPath =
            [SubscriptionPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath.html).newBuilder()
                .setLocation(location)
                .setProject([ProjectNumber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectNumber.html).of(projectNumber))
                .setName([SubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.SubscriptionName.html).of(subscriptionId))
                .build();
    
        [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) fieldMask =
            [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("delivery_config.delivery_requirement").build();
    
        [Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Subscription.html) subscription =
            [Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Subscription.html).newBuilder()
                .setDeliveryConfig(
                    // Possible values for DeliveryRequirement:
                    // - `DELIVER_IMMEDIATELY`
                    // - `DELIVER_AFTER_STORED`
                    // `DELIVER_AFTER_STORED` requires a published message to be successfully written
                    // to storage before the server delivers it to subscribers.
                    DeliveryConfig.newBuilder()
                        .setDeliveryRequirement(DeliveryRequirement.DELIVER_AFTER_STORED))
                .setName([subscriptionPath](https://docs.cloud.google.com/java/docs/reference/pubsublite-spark-sql-streaming/latest/com.google.cloud.pubsublite.spark.PslReadDataSourceOptions.html#com_google_cloud_pubsublite_spark_PslReadDataSourceOptions_subscriptionPath__).[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath.html#com_google_cloud_pubsublite_SubscriptionPath_toString__)())
                .build();
    
        [AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html) adminClientSettings =
            [AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html).newBuilder().setRegion([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(cloudRegion)).build();
    
        try ([AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html) adminClient = [AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html).create(adminClientSettings)) {
          [Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Subscription.html) subscriptionBeforeUpdate = adminClient.getSubscription(subscriptionPath).get();
          System.out.println("Before update: " + subscriptionBeforeUpdate.getAllFields());
    
          [Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Subscription.html) subscriptionAfterUpdate =
              adminClient.updateSubscription(subscription, fieldMask).get();
          System.out.println("After update: " + subscriptionAfterUpdate.getAllFields());
        } catch (ExecutionException e) {
          try {
            throw e.getCause();
          } catch ([NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html) notFound) {
            System.out.println("This subscription is not found.");
          } catch (Throwable throwable) {
            throwable.printStackTrace();
          }
        }
      }
    }

### Python

Before running this sample, follow the Python setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
    from google.api_core.exceptions import NotFound
    from google.cloud.pubsublite import [AdminClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.admin_client.AdminClient.html), Subscription
    from google.cloud.pubsublite.types import [CloudRegion](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.CloudRegion.html), [CloudZone](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.CloudZone.html), [SubscriptionPath](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.SubscriptionPath.html)
    from google.protobuf.field_mask_pb2 import FieldMask
    
    # TODO(developer):
    # project_number = 1122334455
    # cloud_region = "us-central1"
    # zone_id = "a"
    # topic_id = "your-topic-id"
    # subscription_id = "your-subscription-id"
    # regional = True
    
    if regional:
        location = CloudRegion(cloud_region)
    else:
        location = CloudZone(CloudRegion(cloud_region), zone_id)
    
    subscription_path = SubscriptionPath(project_number, location, subscription_id)
    field_mask = FieldMask(paths=["delivery_config.delivery_requirement"])
    
    subscription = Subscription(
        name=str(subscription_path),
        delivery_config=Subscription.DeliveryConfig(
            # Possible values for delivery_requirement:
            # - `DELIVER_IMMEDIATELY`
            # - `DELIVER_AFTER_STORED`
            # `DELIVER_AFTER_STORED` requires a published message to be successfully written
            # to storage before the server delivers it to subscribers.
            delivery_requirement=Subscription.DeliveryConfig.DeliveryRequirement.DELIVER_AFTER_STORED,
        ),
    )
    
    client = AdminClient(cloud_region)
    try:
        response = client.[update_subscription](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.admin_client.AdminClient.html#google_cloud_pubsublite_admin_client_AdminClient_update_subscription)(subscription, field_mask)
        print(f"{response.name} updated successfully.")
    except NotFound:
        print(f"{subscription_path} not found.")

## View Lite subscription details

You can get details about a Lite subscription using the Google Cloud console, the Google Cloud CLI, or the Pub/Sub Lite API.

### Console

  1. Go to the **Lite Subscriptions** page.

[Go to Lite Subscriptions](https://console.cloud.google.com/cloudpubsub/liteSubscription)

  2. Click the Lite subscription ID.

  3. In the Lite subscription details page, click the **Details** tab.




### gcloud

To get details about a Lite subscription, use the [`gcloud pubsub lite-subscriptions describe`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/describe) command:
    
    
    gcloud pubsub lite-subscriptions describe SUBSCRIPTION_ID \
      --location=LOCATION

Replace the following:

  * SUBSCRIPTION_ID: the ID of the Lite subscription

  * LOCATION: the name of the location that the Lite subscription is in




If the request is successful, the command line displays the Lite topic:
    
    
    deliveryConfig:
      deliveryRequirement: DELIVERY_REQUIREMENT
    name: projects/PROJECT_NUMBER/locations/LOCATION/subscriptions/SUBSCRIPTION_ID
    topic: projects/PROJECT_NUMBER/locations/LOCATION/topics/TOPIC_ID
    

### Protocol

To get details about a Lite subscription, send a `GET` request like the following:
    
    
    GET https://REGION-pubsublite.googleapis.com/v1/admin/projects/PROJECT_NUMBER/locations/LOCATION/subscriptions/SUBSCRIPTION_ID
    Authorization: Bearer $(gcloud auth print-access-token)
    

Replace the following:

  * REGION: the region to store the Lite subscription in

  * PROJECT_NUMBER: the project number of the project with the Lite subscription

  * LOCATION: the name of the location that the Lite subscription is in

  * SUBSCRIPTION_ID: the ID of the Lite subscription




If the request is successful, the response is the Lite topic in JSON format:
    
    
    {
      "deliveryConfig": {
        "deliveryRequirement": DELIVERY_REQUIREMENT,
       }
      "name": "projects/PROJECT_NUMBER/locations/LOCATION/subscriptions/SUBSCRIPTION_ID",
      "topic": "projects/PROJECT_NUMBER/locations/LOCATION/topics/TOPIC_ID",
    }
    

### Go

Before running this sample, follow the Go setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/pubsublite"
    )
    
    func getSubscription(w io.Writer, projectID, region, location, subID string) error {
    	// projectID := "my-project-id"
    	// region := "us-central1"
    	// NOTE: location can be either a region ("us-central1") or a zone ("us-central1-a")
    	// For a list of valid locations, see https://cloud.google.com/pubsub/lite/docs/locations.
    	// location := "us-central1"
    	// subID := "my-subscription"
    	ctx := context.Background()
    	client, err := pubsublite.NewAdminClient(ctx, region)
    	if err != nil {
    		return fmt.Errorf("pubsublite.NewAdminClient: %w", err)
    	}
    	defer client.Close()
    
    	subPath := fmt.Sprintf("projects/%s/locations/%s/subscriptions/%s", projectID, location, subID)
    	sub, err := client.Subscription(ctx, subPath)
    	if err != nil {
    		return fmt.Errorf("client.Subscription got err: %w", err)
    	}
    	fmt.Fprintf(w, "Got subscription: %#v\n", sub)
    	return nil
    }
    

### Java

Before running this sample, follow the Java setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
    import com.google.api.gax.rpc.[NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html);
    import com.google.cloud.pubsublite.[AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html);
    import com.google.cloud.pubsublite.[AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html);
    import com.google.cloud.pubsublite.[CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html);
    import com.google.cloud.pubsublite.[CloudRegionOrZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegionOrZone.html);
    import com.google.cloud.pubsublite.[CloudZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudZone.html);
    import com.google.cloud.pubsublite.[ProjectNumber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectNumber.html);
    import com.google.cloud.pubsublite.[SubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.SubscriptionName.html);
    import com.google.cloud.pubsublite.[SubscriptionPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath.html);
    import com.google.cloud.pubsublite.proto.[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Subscription.html);
    import java.util.concurrent.ExecutionException;
    
    public class GetSubscriptionExample {
    
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String cloudRegion = "your-cloud-region";
        char zoneId = 'b';
        // Choose an existing subscription.
        String subscriptionId = "your-subscription-id";
        long projectNumber = Long.parseLong("123456789");
        // True if using a regional location. False if using a zonal location.
        // https://cloud.google.com/pubsub/lite/docs/topics
        boolean regional = false;
    
        getSubscriptionExample(cloudRegion, zoneId, projectNumber, subscriptionId, regional);
      }
    
      public static void getSubscriptionExample(
          String cloudRegion, char zoneId, long projectNumber, String subscriptionId, boolean regional)
          throws Exception {
    
        [CloudRegionOrZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegionOrZone.html) location;
        if (regional) {
          location = [CloudRegionOrZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegionOrZone.html).of([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(cloudRegion));
        } else {
          location = [CloudRegionOrZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegionOrZone.html).of([CloudZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudZone.html).of([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(cloudRegion), zoneId));
        }
    
        [SubscriptionPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath.html) subscriptionPath =
            [SubscriptionPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath.html).newBuilder()
                .setLocation(location)
                .setProject([ProjectNumber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectNumber.html).of(projectNumber))
                .setName([SubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.SubscriptionName.html).of(subscriptionId))
                .build();
    
        [AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html) adminClientSettings =
            [AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html).newBuilder().setRegion([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(cloudRegion)).build();
    
        try ([AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html) adminClient = [AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html).create(adminClientSettings)) {
          [Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Subscription.html) subscription = adminClient.getSubscription(subscriptionPath).get();
          System.out.println(subscription.getAllFields());
        } catch (ExecutionException e) {
          try {
            throw e.getCause();
          } catch ([NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html) notFound) {
            System.out.println("This subscription is not found.");
          } catch (Throwable throwable) {
            throwable.printStackTrace();
          }
        }
      }
    }

### Python

Before running this sample, follow the Python setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
    from google.api_core.exceptions import NotFound
    from google.cloud.pubsublite import [AdminClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.admin_client.AdminClient.html)
    from google.cloud.pubsublite.types import [CloudRegion](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.CloudRegion.html), [CloudZone](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.CloudZone.html), [SubscriptionPath](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.SubscriptionPath.html)
    
    # TODO(developer):
    # project_number = 1122334455
    # cloud_region = "us-central1"
    # zone_id = "a"
    # subscription_id = "your-subscription-id"
    # regional = True
    
    if regional:
        location = CloudRegion(cloud_region)
    else:
        location = CloudZone(CloudRegion(cloud_region), zone_id)
    
    subscription_path = SubscriptionPath(project_number, location, subscription_id)
    
    client = AdminClient(cloud_region)
    try:
        response = client.[get_subscription](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.admin_client.AdminClient.html#google_cloud_pubsublite_admin_client_AdminClient_get_subscription)(subscription_path)
        print(f"{response.name} exists.")
    except NotFound:
        print(f"{subscription_path} not found.")

## List Lite subscriptions

You can list the Lite subscriptions in a project or the Lite subscriptions to a Lite topic.

### List Lite subscriptions in a project

You can list Lite subscriptions in a project using the Google Cloud console, the Google Cloud CLI, or the Pub/Sub Lite API.

### Console

  * Go to the **Lite Subscriptions** page.

[Go to Lite Subscriptions](https://console.cloud.google.com/cloudpubsub/liteSubscription)




### gcloud

  * To list the Lite subscriptions in a project, use the [`gcloud pubsub lite-subscriptions list`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/list) command:


    
    
    gcloud pubsub lite-subscriptions list \
      --location=LOCATION

Replace LOCATION with the name of the location that the Lite subscriptions are in.

If the request is successful, the command line displays the Lite subscriptions:
    
    
    ---
    deliveryConfig:
      deliveryRequirement: DELIVERY_REQUIREMENT
    name: projects/PROJECT_NUMBER/locations/LOCATION/subscriptions/SUBSCRIPTION_ID
    topic: projects/PROJECT_NUMBER/locations/LOCATION/topics/TOPIC_ID
    ---
    deliveryConfig:
      deliveryRequirement: DELIVERY_REQUIREMENT
    name: projects/PROJECT_NUMBER/locations/LOCATION/subscriptions/SUBSCRIPTION_ID
    topic: projects/PROJECT_NUMBER/locations/LOCATION/topics/TOPIC_ID

### Protocol

  * To list the Lite subscriptions in a project, send a `GET` request like the following:


    
    
    GET https://REGION-pubsublite.googleapis.com/v1/admin/projects/PROJECT_NUMBER/subscriptions
    Authorization: Bearer $(gcloud auth print-access-token)
    

Replace the following:

  * REGION: the region to store the Lite subscription in

  * PROJECT_NUMBER: the project number of the project with the Lite subscription




If the request is successful, the response is the Lite topic in JSON format:
    
    
    {
      "subscriptions": [
          {
              "name": "projects/PROJECT_NUMBER/locations/LOCATION/subscriptions/SUBSCRIPTION_ID"
          },
          {
              "name": "projects/PROJECT_NUMBER/locations/LOCATION/subscriptions/SUBSCRIPTION_ID"
          }
      ]
    }
    

### Go

Before running this sample, follow the Go setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/pubsublite"
    	"google.golang.org/api/iterator"
    )
    
    func listSubscriptionsInProject(w io.Writer, projectID, region, location string) error {
    	// projectID := "my-project-id"
    	// region := "us-central1"
    	// NOTE: location can be either a region ("us-central1") or a zone ("us-central1-a")
    	// For a list of valid locations, see https://cloud.google.com/pubsub/lite/docs/locations.
    	// location := "us-central1"
    	ctx := context.Background()
    	client, err := pubsublite.NewAdminClient(ctx, region)
    	if err != nil {
    		return fmt.Errorf("pubsublite.NewAdminClient: %w", err)
    	}
    	defer client.Close()
    
    	// To list topics in a region, set location to a cloud region instead.
    	parent := fmt.Sprintf("projects/%s/locations/%s", projectID, location)
    	subIter := client.[Subscriptions](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsublite/latest/index.html#cloud_google_com_go_pubsublite_AdminClient_Subscriptions)(ctx, parent)
    	for {
    		sub, err := subIter.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("subIter.Next() got err: %w", err)
    		}
    		fmt.Fprintf(w, "Got subscription config: %v", sub)
    	}
    	return nil
    }
    

### Java

Before running this sample, follow the Java setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
    import com.google.cloud.pubsublite.[AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html);
    import com.google.cloud.pubsublite.[AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html);
    import com.google.cloud.pubsublite.[CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html);
    import com.google.cloud.pubsublite.[CloudRegionOrZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegionOrZone.html);
    import com.google.cloud.pubsublite.[CloudZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudZone.html);
    import com.google.cloud.pubsublite.[LocationPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.LocationPath.html);
    import com.google.cloud.pubsublite.[ProjectNumber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectNumber.html);
    import com.google.cloud.pubsublite.proto.[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Subscription.html);
    import java.util.List;
    
    public class ListSubscriptionsInProjectExample {
    
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String cloudRegion = "your-cloud-region";
        char zoneId = 'b';
        long projectNumber = Long.parseLong("123456789");
        // True if using a regional location. False if using a zonal location.
        // https://cloud.google.com/pubsub/lite/docs/topics
        boolean regional = true;
    
        listSubscriptionsInProjectExample(cloudRegion, zoneId, projectNumber, regional);
      }
    
      public static void listSubscriptionsInProjectExample(
          String cloudRegion, char zoneId, long projectNumber, boolean regional) throws Exception {
    
        [AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html) adminClientSettings =
            [AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html).newBuilder().setRegion([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(cloudRegion)).build();
    
        [CloudRegionOrZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegionOrZone.html) location;
        if (regional) {
          location = [CloudRegionOrZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegionOrZone.html).of([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(cloudRegion));
        } else {
          location = [CloudRegionOrZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegionOrZone.html).of([CloudZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudZone.html).of([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(cloudRegion), zoneId));
        }
    
        [LocationPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.LocationPath.html) locationPath =
            [LocationPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.LocationPath.html).newBuilder()
                .setProject([ProjectNumber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectNumber.html).of(projectNumber))
                .setLocation(location)
                .build();
    
        try ([AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html) adminClient = [AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html).create(adminClientSettings)) {
          List<Subscription> subscriptions = adminClient.listSubscriptions(locationPath).get();
          for ([Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.Subscription.html) subscription : subscriptions) {
            System.out.println(subscription.getAllFields());
          }
          System.out.println(subscriptions.size() + " subscription(s) listed in the project.");
        }
      }
    }

### Python

Before running this sample, follow the Python setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
    from google.cloud.pubsublite import [AdminClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.admin_client.AdminClient.html)
    from google.cloud.pubsublite.types import [CloudRegion](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.CloudRegion.html), [CloudZone](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.CloudZone.html), [LocationPath](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.LocationPath.html)
    
    # TODO(developer):
    # project_number = 1122334455
    # cloud_region = "us-central1"
    # zone_id = "a"
    # regional = True
    
    if regional:
        location = CloudRegion(cloud_region)
    else:
        location = CloudZone(CloudRegion(cloud_region), zone_id)
    
    location_path = LocationPath(project_number, location)
    
    client = AdminClient(cloud_region)
    response = client.[list_subscriptions](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.admin_client.AdminClient.html#google_cloud_pubsublite_admin_client_AdminClient_list_subscriptions)(location_path)
    
    for subscription in response:
        print(subscription.name)
    
    print(f"{len(response)} subscription(s) listed in your project and location.")

### Listing Lite subscriptions to a Lite topic

You can list Lite subscriptions to a Lite topic using the Google Cloud console, the Google Cloud CLI, or the Pub/Sub Lite API.

### Console

  1. Go to the **Lite Topics** page.

[Go to Lite Topics](https://console.cloud.google.com/cloudpubsub/liteTopic)

  2. Select a Lite topic ID.

  3. In the **Lite topics** details page, the **Lite subscriptions** section includes a list of Lite subscriptions to the Lite topic.




### gcloud

  * To list the Lite subscriptions to a topic, use the [`gcloud pubsub lite-topics list-subscriptions`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/list-subscriptions) command:


    
    
    gcloud pubsub lite-topics list-subscriptions TOPIC_ID \
      --location=LOCATION

Replace the following:

  * TOPIC_ID: the ID of the Lite topic that the Lite subscriptions are attached to

  * LOCATION: the name of the location that the Lite subscription is in




If the request is successful, the command line displays the Lite subscriptions:
    
    
    ---
    deliveryConfig:
      deliveryRequirement: DELIVERY_REQUIREMENT
    name: projects/PROJECT_NUMBER/locations/LOCATION/subscriptions/SUBSCRIPTION_ID
    topic: projects/PROJECT_NUMBER/locations/LOCATION/topics/TOPIC_ID
    ---
    deliveryConfig:
      deliveryRequirement: DELIVERY_REQUIREMENT
    name: projects/PROJECT_NUMBER/locations/LOCATION/subscriptions/SUBSCRIPTION_ID
    topic: projects/PROJECT_NUMBER/locations/LOCATION/topics/TOPIC_ID

### Protocol

  * To list the Lite subscriptions to a Lite topic, send a `GET` request like the following:


    
    
    GET https://REGION-pubsublite.googleapis.com/v1/admin/projects/PROJECT_NUMBER/lite-topics/TOPIC_ID/subscriptions
    Authorization: Bearer $(gcloud auth print-access-token)
    

Replace the following:

  * REGION: the region to store the Lite subscription in

  * PROJECT_NUMBER: the project number of the project with the Lite subscription

  * LOCATION: the name of the location that the Lite subscription is in

  * TOPIC_ID: the ID of the Lite topic that the Lite subscriptions are attached to




If the request is successful, the response is a list of Lite subscriptions in JSON format:
    
    
    {
      "subscriptions": [
          {
              "name": "projects/PROJECT_NUMBER/locations/LOCATION/subscriptions/SUBSCRIPTION_ID"
          },
          {
              "name": "projects/PROJECT_NUMBER/locations/LOCATION/subscriptions/SUBSCRIPTION_ID"
          }
      ]
    }
    

### Go

Before running this sample, follow the Go setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/pubsublite"
    	"google.golang.org/api/iterator"
    )
    
    func listSubscriptionsInTopic(w io.Writer, projectID, region, location, topicID string) error {
    	// projectID := "my-project-id"
    	// region := "us-central1"
    	// NOTE: location can be either a region ("us-central1") or a zone ("us-central1-a")
    	// For a list of valid locations, see https://cloud.google.com/pubsub/lite/docs/locations.
    	// location := "us-central"
    	// topicID := "my-topic"
    	ctx := context.Background()
    	client, err := pubsublite.NewAdminClient(ctx, region)
    	if err != nil {
    		return fmt.Errorf("pubsublite.NewAdminClient: %w", err)
    	}
    	defer client.Close()
    
    	topicPath := fmt.Sprintf("projects/%s/locations/%s/topics/%s", projectID, location, topicID)
    	subPathIter := client.[TopicSubscriptions](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsublite/latest/index.html#cloud_google_com_go_pubsublite_AdminClient_TopicSubscriptions)(ctx, topicPath)
    	for {
    		subPath, err := subPathIter.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("subPathIter.Next got err: %w", err)
    		}
    		fmt.Fprintf(w, "Got subscription: %s\n", subPath)
    	}
    	return nil
    }
    

### Java

Before running this sample, follow the Java setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
    import com.google.cloud.pubsublite.[AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html);
    import com.google.cloud.pubsublite.[AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html);
    import com.google.cloud.pubsublite.[CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html);
    import com.google.cloud.pubsublite.[CloudRegionOrZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegionOrZone.html);
    import com.google.cloud.pubsublite.[CloudZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudZone.html);
    import com.google.cloud.pubsublite.[ProjectNumber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectNumber.html);
    import com.google.cloud.pubsublite.[SubscriptionPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath.html);
    import com.google.cloud.pubsublite.[TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.TopicName.html);
    import com.google.cloud.pubsublite.[TopicPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath.html);
    import java.util.List;
    
    public class ListSubscriptionsInTopicExample {
    
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String cloudRegion = "your-cloud-region";
        char zoneId = 'b';
        long projectNumber = Long.parseLong("123456789");
        String topicId = "your-topic-id";
        // True if using a regional location. False if using a zonal location.
        // https://cloud.google.com/pubsub/lite/docs/topics
        boolean regional = false;
    
        listSubscriptionsInTopicExample(cloudRegion, zoneId, projectNumber, topicId, regional);
      }
    
      public static void listSubscriptionsInTopicExample(
          String cloudRegion, char zoneId, long projectNumber, String topicId, boolean regional)
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
    
        [AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html) adminClientSettings =
            [AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html).newBuilder().setRegion([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(cloudRegion)).build();
    
        try ([AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html) adminClient = [AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html).create(adminClientSettings)) {
          List<SubscriptionPath> subscriptionPaths =
              adminClient.listTopicSubscriptions(topicPath).get();
          for ([SubscriptionPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath.html) subscription : subscriptionPaths) {
            System.out.println(subscription.toString());
          }
          if (regional) {
            System.out.println(
                subscriptionPaths.size()
                    + " subscription(s) listed in the regional topic "
                    + topicPath);
          } else {
            System.out.println(
                subscriptionPaths.size() + " subscription(s) listed in the zonal topic " + topicPath);
          }
        }
      }
    }

### Python

Before running this sample, follow the Python setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
    from google.cloud.pubsublite import [AdminClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.admin_client.AdminClient.html)
    from google.cloud.pubsublite.types import [CloudRegion](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.CloudRegion.html), [CloudZone](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.CloudZone.html), [TopicPath](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.TopicPath.html)
    
    # TODO(developer):
    # project_number = 1122334455
    # cloud_region = "us-central1"
    # zone_id = "a"
    # topic_id = "your-topic-id"
    # regional = True
    
    if regional:
        location = CloudRegion(cloud_region)
    else:
        location = CloudZone(CloudRegion(cloud_region), zone_id)
    
    topic_path = TopicPath(project_number, location, topic_id)
    
    client = AdminClient(cloud_region)
    response = client.[list_topic_subscriptions](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.admin_client.AdminClient.html#google_cloud_pubsublite_admin_client_AdminClient_list_topic_subscriptions)(topic_path)
    
    for subscription_path in response:
        print(subscription_path)
    
    print(f"{len(response)} subscription(s) listed in your topic.")

## Delete a Lite subscription

You can delete Lite subscriptions with the Google Cloud console, the Google Cloud CLI, or the Pub/Sub Lite API.

**Caution:** Deletion is permanent. Once deleted, subscriptions cannot be restored.

### Console

  1. Go to the **Lite Subscriptions** page.

[Go to Lite Subscriptions](https://console.cloud.google.com/cloudpubsub/liteSubscription)

  2. Click the Lite subscription ID.

  3. In the **Lite subscription details** page, click **Delete**.

  4. In the dialog that appears, click **Delete** to confirm that you want to delete the Lite subscription.




### gcloud

To delete a Lite subscription, use the [`gcloud pubsub lite-subscriptions delete`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/delete) command:

  1. Run the `delete` command:
         
         gcloud pubsub lite-subscriptions delete SUBSCRIPTION_ID \
          --location=LOCATION

Replace the following:

     * SUBSCRIPTION_ID: the ID of the Lite subscription

     * LOCATION: the name of the location that the Lite subscription is in

  2. To confirm, type `Y`.




If the request is successful, the command line displays a confirmation:
    
    
    Deleted subscription [SUBSCRIPTION_ID].
    

### Protocol

  * To delete a Lite topic, send a `DELETE` request like the following:


    
    
    DELETE https://REGION-pubsublite.googleapis.com/v1/admin/projects/PROJECT_NUMBER/locations/LOCATION/subscriptions/SUBSCRIPTION_ID
    Authorization: Bearer $(gcloud auth print-access-token)
    

Replace the following:

  * REGION: the region to store the Lite subscription in

  * PROJECT_NUMBER: the project number of the project with the Lite subscription

  * LOCATION: the name of the location that the Lite subscription is in

  * SUBSCRIPTION_ID: the ID of the Lite subscription




If the request is successful, the response is an empty JSON object.

### Go

Before running this sample, follow the Go setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/pubsublite"
    )
    
    func deleteSubscription(w io.Writer, projectID, region, location, subID string) error {
    	// projectID := "my-project-id"
    	// region := "us-central1"
    	// NOTE: location can be either a region ("us-central1") or a zone ("us-central1-a")
    	// For a list of valid locations, see https://cloud.google.com/pubsub/lite/docs/locations.
    	// location := "us-central1"
    	// subID := "my-subscription"
    	ctx := context.Background()
    	client, err := pubsublite.NewAdminClient(ctx, region)
    	if err != nil {
    		return fmt.Errorf("pubsublite.NewAdminClient: %w", err)
    	}
    	defer client.Close()
    
    	err = client.DeleteSubscription(ctx, fmt.Sprintf("projects/%s/locations/%s/subscriptions/%s", projectID, location, subID))
    	if err != nil {
    		return fmt.Errorf("client.DeleteSubscription got err: %w", err)
    	}
    	fmt.Fprintf(w, "Deleted subscription\n")
    	return nil
    }
    

### Java

Before running this sample, follow the Java setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
    import com.google.api.gax.rpc.[NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html);
    import com.google.cloud.pubsublite.[AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html);
    import com.google.cloud.pubsublite.[AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html);
    import com.google.cloud.pubsublite.[CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html);
    import com.google.cloud.pubsublite.[CloudRegionOrZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegionOrZone.html);
    import com.google.cloud.pubsublite.[CloudZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudZone.html);
    import com.google.cloud.pubsublite.[ProjectNumber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectNumber.html);
    import com.google.cloud.pubsublite.[SubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.SubscriptionName.html);
    import com.google.cloud.pubsublite.[SubscriptionPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath.html);
    import java.util.concurrent.ExecutionException;
    
    public class DeleteSubscriptionExample {
    
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String cloudRegion = "your-cloud-region";
        char zoneId = 'b';
        // Choose an existing subscription.
        String subscriptionId = "your-subscription-id";
        long projectNumber = Long.parseLong("123456789");
        // True if using a regional location. False if using a zonal location.
        // https://cloud.google.com/pubsub/lite/docs/topics
        boolean regional = false;
    
        deleteSubscriptionExample(cloudRegion, zoneId, projectNumber, subscriptionId, regional);
      }
    
      public static void deleteSubscriptionExample(
          String cloudRegion, char zoneId, long projectNumber, String subscriptionId, boolean regional)
          throws Exception {
    
        [CloudRegionOrZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegionOrZone.html) location;
        if (regional) {
          location = [CloudRegionOrZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegionOrZone.html).of([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(cloudRegion));
        } else {
          location = [CloudRegionOrZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegionOrZone.html).of([CloudZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudZone.html).of([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(cloudRegion), zoneId));
        }
    
        [SubscriptionPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath.html) subscriptionPath =
            [SubscriptionPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath.html).newBuilder()
                .setLocation(location)
                .setProject([ProjectNumber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectNumber.html).of(projectNumber))
                .setName([SubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.SubscriptionName.html).of(subscriptionId))
                .build();
    
        [AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html) adminClientSettings =
            [AdminClientSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClientSettings.html).newBuilder().setRegion([CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html).of(cloudRegion)).build();
    
        try ([AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html) adminClient = [AdminClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.AdminClient.html).create(adminClientSettings)) {
          adminClient.deleteSubscription(subscriptionPath).get();
          System.out.println(subscriptionPath + " deleted successfully.");
        } catch (ExecutionException e) {
          try {
            throw e.getCause();
          } catch ([NotFoundException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.NotFoundException.html) notFound) {
            System.out.println("This subscription is not found.");
          } catch (Throwable throwable) {
            throwable.printStackTrace();
          }
        }
      }
    }

### Python

Before running this sample, follow the Python setup instructions in [Pub/Sub Lite Client Libraries](https://docs.cloud.google.com/pubsub/lite/docs/reference/libraries). 
    
    
    from google.api_core.exceptions import NotFound
    from google.cloud.pubsublite import [AdminClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.admin_client.AdminClient.html)
    from google.cloud.pubsublite.types import [CloudRegion](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.CloudRegion.html), [CloudZone](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.CloudZone.html), [SubscriptionPath](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.SubscriptionPath.html)
    
    # TODO(developer):
    # project_number = 1122334455
    # cloud_region = "us-central1"
    # zone_id = "a"
    # subscription_id = "your-subscription-id"
    # regional = True
    
    if regional:
        location = CloudRegion(cloud_region)
    else:
        location = CloudZone(CloudRegion(cloud_region), zone_id)
    
    subscription_path = SubscriptionPath(project_number, location, subscription_id)
    
    client = AdminClient(cloud_region)
    try:
        client.[delete_subscription](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.admin_client.AdminClient.html#google_cloud_pubsublite_admin_client_AdminClient_delete_subscription)(subscription_path)
        print(f"{subscription_path} deleted successfully.")
    except NotFound:
        print(f"{subscription_path} not found.")

## What's Next

  * [Create and manage a Lite topic](https://docs.cloud.google.com/pubsub/lite/docs/topics).
  * [Publish messages](https://docs.cloud.google.com/pubsub/lite/docs/publishing) to a Lite topic.
  * [Receive messages](https://docs.cloud.google.com/pubsub/lite/docs/subscribing) from a Lite subscription.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
