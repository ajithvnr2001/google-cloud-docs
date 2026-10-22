---
url: https://docs.cloud.google.com/pubsub/lite/docs/samples/pubsublite-seek-subscription/
title: Seek to a location in a Pub/Sub Lite subscription \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:07.840346+00:00
---

# Seek to a location in a Pub/Sub Lite subscription  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/lite/docs/samples/pubsublite-seek-subscription/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Pub/Sub Lite ](https://docs.cloud.google.com/pubsub/lite/docs)
  * [ Samples ](https://docs.cloud.google.com/pubsub/lite/docs/samples)



#  Seek to a location in a Pub/Sub Lite subscription Stay organized with collections  Save and categorize content based on your preferences. 

Seek to a location in a Pub/Sub Lite subscription to start receiving messages from that location.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Replaying and purging Pub/Sub Lite messages](https://docs.cloud.google.com/pubsub/lite/docs/seek)



## Code sample

### Go

To authenticate to Pub/Sub Lite, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/pubsublite"
    )
    
    // seekSubscription initiates a seek operation for a subscription.
    func seekSubscription(w io.Writer, projectID, region, zone, subID string, seekTarget pubsublite.[SeekTarget](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/pubsublite/latest/index.html#cloud_google_com_go_pubsublite_SeekTarget), waitForOperation bool) error {
    	// projectID := "my-project-id"
    	// region := "us-central1"
    	// zone := "us-central1-a"
    	// subID := "my-subscription"
    	// seekTarget := pubsublite.Beginning
    	// waitForOperation := false
    
    	// Possible values for seekTarget:
    	// - pubsublite.Beginning: replays from the beginning of all retained
    	//   messages.
    	// - pubsublite.End: skips past all current published messages.
    	// - pubsublite.PublishTime(<time>): delivers messages with publish time
    	//   greater than or equal to the specified timestamp.
    	// - pubsublite.EventTime(<time>): seeks to the first message with event
    	//   time greater than or equal to the specified timestamp.
    
    	// Waiting for the seek operation to complete is optional. It indicates when
    	// subscribers for all partitions are receiving messages from the seek
    	// target. If subscribers are offline, the operation will complete once they
    	// are online.
    
    	ctx := context.Background()
    	client, err := pubsublite.NewAdminClient(ctx, region)
    	if err != nil {
    		return fmt.Errorf("pubsublite.NewAdminClient: %w", err)
    	}
    	defer client.Close()
    
    	// Initiate an out-of-band seek for a subscription to the specified target.
    	// If an operation is returned, the seek has been successfully registered
    	// and will eventually propagate to subscribers.
    	subPath := fmt.Sprintf("projects/%s/locations/%s/subscriptions/%s", projectID, zone, subID)
    	seekOp, err := client.SeekSubscription(ctx, subPath, seekTarget)
    	if err != nil {
    		return fmt.Errorf("client.SeekSubscription got err: %w", err)
    	}
    	fmt.Fprintf(w, "Seek operation initiated: %s\n", seekOp.Name())
    
    	if waitForOperation {
    		_, err = seekOp.Wait(ctx)
    		if err != nil {
    			return fmt.Errorf("seekOp.Wait got err: %w", err)
    		}
    		metadata, err := seekOp.Metadata()
    		if err != nil {
    			return fmt.Errorf("seekOp.Metadata got err: %w", err)
    		}
    		fmt.Fprintf(w, "Seek operation completed with metadata: %v\n", metadata)
    	}
    	return nil
    }
    

### Java

To authenticate to Pub/Sub Lite, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
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
    import com.google.cloud.pubsublite.proto.[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.OperationMetadata.html);
    import com.google.cloud.pubsublite.proto.[SeekSubscriptionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.SeekSubscriptionResponse.html);
    
    public class SeekSubscriptionExample {
    
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
    
        // Choose a target location within the message backlog to seek a subscription to.
        // Possible values for SeekTarget:
        // - SeekTarget.of(BacklogLocation.BEGINNING): replays from the beginning of all retained
        //   messages.
        // - SeekTarget.of(BacklogLocation.END): skips past all current published messages.
        // - SeekTarget.ofPublishTime(<timestamp>): delivers messages with publish time greater than
        //   or equal to the specified timestamp.
        // - SeekTarget.ofEventTime(<timestamp>): seeks to the first message with event time greater
        //   than or equal to the specified timestamp.
        [SeekTarget](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SeekTarget.html) target = [SeekTarget](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SeekTarget.html).of([BacklogLocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.BacklogLocation.html).BEGINNING);
    
        // Optional: Wait for the seek operation to complete, which indicates when subscribers for all
        // partitions are receiving messages from the seek target. If subscribers are offline, the
        // operation will complete once they are online.
        boolean waitForOperation = false;
    
        seekSubscriptionExample(
            cloudRegion, zoneId, projectNumber, subscriptionId, target, waitForOperation, regional);
      }
    
      public static void seekSubscriptionExample(
          String cloudRegion,
          char zoneId,
          long projectNumber,
          String subscriptionId,
          [SeekTarget](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SeekTarget.html) target,
          boolean waitForOperation,
          boolean regional)
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
          // Initiate an out-of-band seek for a subscription to the specified target. If an operation
          // is returned, the seek has been successfully registered and will eventually propagate to
          // subscribers.
          OperationFuture<SeekSubscriptionResponse, OperationMetadata> seekFuture =
              adminClient.seekSubscription(subscriptionPath, target);
          System.out.println("Seek operation " + seekFuture.getName() + " initiated successfully.");
    
          if (waitForOperation) {
            System.out.println("Waiting for operation to complete...");
            seekFuture.get();
            System.out.println("Operation completed. Metadata:\n" + seekFuture.getMetadata().get());
          }
        }
      }
    }

### Python

To authenticate to Pub/Sub Lite, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.api_core.exceptions import NotFound
    from google.cloud.pubsublite import [AdminClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.admin_client.AdminClient.html)
    from google.cloud.pubsublite.types import [CloudRegion](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.CloudRegion.html), [CloudZone](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.CloudZone.html), [SubscriptionPath](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.types.SubscriptionPath.html)
    
    # TODO(developer):
    # project_number = 1122334455
    # cloud_region = "us-central1"
    # zone_id = "a"
    # subscription_id = "your-subscription-id"
    # seek_target = BacklogLocation.BEGINNING
    # wait_for_operation = False
    # regional = True
    
    # Possible values for seek_target:
    # - BacklogLocation.BEGINNING: replays from the beginning of all retained
    #   messages.
    # - BacklogLocation.END: skips past all current published messages.
    # - PublishTime(<datetime>): delivers messages with publish time greater
    #   than or equal to the specified timestamp.
    # - EventTime(<datetime>): seeks to the first message with event time
    #   greater than or equal to the specified timestamp.
    
    # Waiting for the seek operation to complete is optional. It indicates when
    # subscribers for all partitions are receiving messages from the seek
    # target. If subscribers are offline, the operation will complete once they
    # are online.
    
    if regional:
        location = CloudRegion(cloud_region)
    else:
        location = CloudZone(CloudRegion(cloud_region), zone_id)
    
    subscription_path = SubscriptionPath(project_number, location, subscription_id)
    
    client = AdminClient(cloud_region)
    try:
        # Initiate an out-of-band seek for a subscription to the specified
        # target. If an operation is returned, the seek has been successfully
        # registered and will eventually propagate to subscribers.
        seek_operation = client.[seek_subscription](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.admin_client.AdminClient.html#google_cloud_pubsublite_admin_client_AdminClient_seek_subscription)(subscription_path, seek_target)
        print(f"Seek operation: {seek_operation.operation.name}")
    except NotFound:
        print(f"{subscription_path} not found.")
        return
    
    if wait_for_operation:
        print("Waiting for operation to complete...")
        seek_operation.result()
        print(f"Operation completed. Metadata:\n{seek_operation.metadata}")

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=pubsublite). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
