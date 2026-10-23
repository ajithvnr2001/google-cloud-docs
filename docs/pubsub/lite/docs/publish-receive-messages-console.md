---
url: https://docs.cloud.google.com/pubsub/lite/docs/publish-receive-messages-console/
title: Quickstart: Publish and receive messages in Pub/Sub by using the client libraries \u00a0|\u00a0 Pub/Sub Lite \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:17.309631+00:00
---

# Quickstart: Publish and receive messages in Pub/Sub by using the client libraries  |  Pub/Sub Lite  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/lite/docs/publish-receive-messages-console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Pub/Sub Lite ](https://docs.cloud.google.com/pubsub/lite/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/lite/docs/publish-receive-messages-console)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Publish and receive messages in Pub/Sub by using the client libraries

**Note:** Pub/Sub Lite is deprecated. Effective January 31, 2027, Pub/Sub Lite will be turned down.   


  * Current customers: Pub/Sub Lite remains functional until January 31, 2027.   
If you have not used Pub/Sub Lite within the 90-day period preceding July 15, 2025 (April 15, 2025 - July 15, 2025), you won't be able to access Pub/Sub Lite starting on July 15, 2025. 
  * New customers: Pub/Sub Lite is no longer available for new customers after September 24, 2024.



You can migrate your Pub/Sub Lite service to [Google Cloud Managed Service for Apache Kafka](https://docs.cloud.google.com/pubsub/lite/docs/migrate-pubsub-lite-to-managed-service-for-apache-kafka) or [Pub/Sub](https://docs.cloud.google.com/pubsub/lite/docs/migrate-pubsub-lite-to-pubsub).

This page shows you how to do the following:

  * Create a project, enable billing, and enable the Pub/Sub Lite API using the Google Cloud CLI.

  * Create Lite reservations, Lite topics, and Lite subscriptions using the Google Cloud CLI.

  * Send and receive messages using the Pub/Sub Lite client library for Go, Java, and Python.




## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Pub/Sub Lite API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable pubsublite.googleapis.com

  8. Create local authentication credentials for your user account: 
         
         gcloud auth application-default login

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  9. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/pubsublite.admin`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.

  10. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  11. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  12. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  13. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  14. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  15. Enable the Pub/Sub Lite API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable pubsublite.googleapis.com

  16. Create local authentication credentials for your user account: 
         
         gcloud auth application-default login

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  17. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/pubsublite.admin`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.




## Install the client library

### Go
    
    
    go get cloud.google.com/go/pubsublite

### Java

If you are using [Maven](https://maven.apache.org/), add the following to your `pom.xml` file. For more information about BOMs, see [The Google Cloud Platform Libraries BOM](https://cloud.google.com/java/docs/bom).
    
    
    <!-- {x-version-update-start:google-cloud-pubsublite:current} -->
    <dependency>
      <groupId>com.google.cloud</groupId>
      <artifactId>google-cloud-pubsublite</artifactId>
      <version>1.17.1-SNAPSHOT</version>
    </dependency>
    <!-- {x-version-update-end} -->
    <dependency>
      <groupId>com.google.cloud</groupId>
      <artifactId>google-cloud-pubsub</artifactId>
      <version>1.151.0</version>
    </dependency>
    

If you are using [Gradle](https://gradle.org/), add the following to your dependencies:
    
    
    implementation 'com.google.cloud:google-cloud-pubsublite:1.17.0'

If you are using [sbt](https://www.scala-sbt.org/), add the following to your dependencies:
    
    
    libraryDependencies += "com.google.cloud" % "google-cloud-pubsublite" % "1.17.0"

If you're using Visual Studio Code or IntelliJ, you can add client libraries to your project using the following IDE plugins:

  * [Cloud Code for VS Code](https://docs.cloud.google.com/code/docs/vscode/client-libraries)
  * [Cloud Code for IntelliJ](https://docs.cloud.google.com/code/docs/intellij/client-libraries)



The plugins provide additional functionality, such as key management for service accounts. Refer to each plugin's documentation for details.

**Note:** Cloud Java client libraries do not currently support Android.

### Python
    
    
    pip install --upgrade google-cloud-pubsublite

## Create a Lite reservation

To create a Lite reservation, use the [`gcloud pubsub lite-reservations create`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/lite-reservations/create) command. The following sample creates a reservation called `testRes`.
    
    
    gcloud pubsub lite-reservations create testRes \
        --location=us-central1 \
        --throughput-capacity=1

## Create a regional Lite topic

To create a regional Lite topic, use the [`gcloud pubsub lite-topics create`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/lite-topics/create) command. The following sample creates a topic called `testTopic`.
    
    
    gcloud pubsub lite-topics create testTopic \
        --location=us-central1 \
        --partitions=1 \
        --per-partition-bytes=30GiB \
        --throughput-reservation=projects/PROJECT_ID/locations/us-central1/reservations/testRes \

Replace the following:

PROJECT_ID: the ID of the project

## Create a Lite subscription

To create a Lite subscription, use the [`gcloud pubsub lite-subscriptions create`](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/lite-subscriptions/create) command. The following sample creates a subscription called `testSub`.
    
    
    gcloud pubsub lite-subscriptions create testSub \
        --location=us-central1 \
        --topic=testTopic \
        --delivery-requirement=deliver-immediately

## Send messages

Send messages to the Lite topic using the following publisher application:

### Go

Before trying this sample, follow the Go setup instructions in the [Pub/Sub Lite quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Lite Go API reference documentation](https://godoc.org/cloud.google.com/go/pubsub). 

To authenticate to Pub/Sub Lite, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    package main
    
    import (
    	"context"
    	"flag"
    	"fmt"
    	"log"
    	"sync"
    
    	"cloud.google.com/go/pubsub"
    	"cloud.google.com/go/pubsublite/pscompat"
    	"golang.org/x/sync/errgroup"
    )
    
    func main() {
    	// NOTE: Set these flags for an existing Pub/Sub Lite topic when running this
    	// sample.
    	projectID := flag.String("project_id", "", "Cloud Project ID")
    	zone := flag.String("zone", "", "Cloud Zone where the topic resides, e.g. us-central1-a")
    	topicID := flag.String("topic_id", "", "Existing Pub/Sub Lite topic")
    	messageCount := flag.Int("message_count", 100, "The number of messages to send")
    	flag.Parse()
    
    	ctx := context.Background()
    	topicPath := fmt.Sprintf("projects/%s/locations/%s/topics/%s", *projectID, *zone, *topicID)
    
    	// Create the publisher client.
    	publisher, err := pscompat.NewPublisherClient(ctx, topicPath)
    	if err != nil {
    		log.Fatalf("pscompat.NewPublisherClient error: %v", err)
    	}
    
    	// Ensure the publisher will be shut down.
    	defer publisher.Stop()
    
    	// Collect any messages that need to be republished with a new publisher
    	// client.
    	var toRepublish []*pubsub.Message
    	var toRepublishMu sync.Mutex
    
    	// Publish messages. Messages are automatically batched.
    	g := new(errgroup.Group)
    	for i := 0; i < *messageCount; i++ {
    		msg := &pubsub.Message{
    			Data: []byte(fmt.Sprintf("message-%d", i)),
    		}
    		result := publisher.Publish(ctx, msg)
    
    		g.Go(func() error {
    			// Get blocks until the result is ready.
    			id, err := result.Get(ctx)
    			if err != nil {
    				// NOTE: A failed PublishResult indicates that the publisher client
    				// encountered a fatal error and has permanently terminated. After the
    				// fatal error has been resolved, a new publisher client instance must
    				// be created to republish failed messages.
    				fmt.Printf("Publish error: %v\n", err)
    				toRepublishMu.Lock()
    				toRepublish = append(toRepublish, msg)
    				toRepublishMu.Unlock()
    				return err
    			}
    
    			// Metadata decoded from the id contains the partition and offset.
    			metadata, err := pscompat.ParseMessageMetadata(id)
    			if err != nil {
    				fmt.Printf("Failed to parse message metadata %q: %v\n", id, err)
    				return err
    			}
    			fmt.Printf("Published: partition=%d, offset=%d\n", metadata.Partition, metadata.Offset)
    			return nil
    		})
    	}
    	if err := g.Wait(); err != nil {
    		fmt.Printf("Publishing finished with error: %v\n", err)
    	}
    	fmt.Printf("Published %d messages\n", *messageCount-len(toRepublish))
    
    	// Print the error that caused the publisher client to terminate (if any),
    	// which may contain more context than PublishResults.
    	if err := publisher.Error(); err != nil {
    		fmt.Printf("Publisher client terminated due to error: %v\n", publisher.Error())
    	}
    }
    

### Java
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.api.core.[ApiFutures](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFutures.html);
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.pubsublite.[CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html);
    import com.google.cloud.pubsublite.[CloudRegionOrZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegionOrZone.html);
    import com.google.cloud.pubsublite.[CloudZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudZone.html);
    import com.google.cloud.pubsublite.[MessageMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.MessageMetadata.html);
    import com.google.cloud.pubsublite.[ProjectNumber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectNumber.html);
    import com.google.cloud.pubsublite.[TopicName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.TopicName.html);
    import com.google.cloud.pubsublite.[TopicPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.TopicPath.html);
    import com.google.cloud.pubsublite.cloudpubsub.[Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.Publisher.html);
    import com.google.cloud.pubsublite.cloudpubsub.[PublisherSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.PublisherSettings.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import com.google.pubsub.v1.[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html);
    import java.util.ArrayList;
    import java.util.List;
    import java.util.concurrent.ExecutionException;
    
    public class PublisherExample {
    
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String cloudRegion = "your-cloud-region";
        char zoneId = 'b';
        // Choose an existing topic for the publish example to work.
        String topicId = "your-topic-id";
        long projectNumber = Long.parseLong("123456789");
        int messageCount = 100;
        // True if using a regional location. False if using a zonal location.
        // https://cloud.google.com/pubsub/lite/docs/topics
        boolean regional = false;
    
        publisherExample(cloudRegion, zoneId, projectNumber, topicId, messageCount, regional);
      }
    
      // Publish messages to a topic.
      public static void publisherExample(
          String cloudRegion,
          char zoneId,
          long projectNumber,
          String topicId,
          int messageCount,
          boolean regional)
          throws [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html), ExecutionException, InterruptedException {
    
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
    
        [Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.Publisher.html) publisher = null;
        List<ApiFuture<String>> futures = new ArrayList<>();
    
        try {
          [PublisherSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.PublisherSettings.html) publisherSettings =
              [PublisherSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.PublisherSettings.html).newBuilder().setTopicPath(topicPath).build();
    
          publisher = [Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.Publisher.html).create(publisherSettings);
    
          // Start the publisher. Upon successful starting, its state will become RUNNING.
          publisher.startAsync().awaitRunning();
    
          for (int i = 0; i < messageCount; i++) {
            String message = "message-" + i;
    
            // Convert the message to a byte string.
            [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) data = [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFromUtf8](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFromUtf8_java_lang_String_)(message);
            [PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html) pubsubMessage = [PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html).newBuilder().setData(data).build();
    
            // Publish a message. Messages are automatically batched.
            ApiFuture<String> future = [publish](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.Publisher.html#com_google_cloud_pubsublite_internal_Publisher_publish_com_google_cloud_pubsublite_proto_PubSubMessage_)er.[publish](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.Publisher.html#com_google_cloud_pubsublite_internal_Publisher_publish_com_google_cloud_pubsublite_proto_PubSubMessage_)(pubsubMessage);
            futures.add(future);
          }
        } finally {
          ArrayList<MessageMetadata> metadata = new ArrayList<>();
          List<String> ackIds = [ApiFutures](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFutures.html).[allAsList](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFutures.html#com_google_api_core_ApiFutures__V_allAsList_java_lang_Iterable___extends_com_google_api_core_ApiFuture___extends_V___)(futures).get();
          for (String id : ackIds) {
            // Decoded metadata contains partition and offset.
            metadata.add([MessageMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.MessageMetadata.html).[decode](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.MessageMetadata.html#com_google_cloud_pubsublite_MessageMetadata_decode_java_lang_String_)(id));
          }
          System.out.println(metadata + "\nPublished " + ackIds.size() + " messages.");
    
          if (publisher != null) {
            // Shut down the publisher.
            publisher.stopAsync().awaitTerminated();
            System.out.println("Publisher is shut down.");
          }
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Pub/Sub Lite quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Lite Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/pubsub/latest). 

To authenticate to Pub/Sub Lite, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud.pubsublite.cloudpubsub import [PublisherClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.PublisherClient.html)
    from google.cloud.pubsublite.types import (
        CloudRegion,
        CloudZone,
        MessageMetadata,
        TopicPath,
    )
    
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
    
    # PublisherClient() must be used in a `with` block or have __enter__() called before use.
    with PublisherClient() as publisher_client:
        data = "Hello world!"
        api_future = [publisher_client](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.publisher_client.html).publish(topic_path, data.encode("utf-8"))
        # result() blocks. To resolve API futures asynchronously, use add_done_callback().
        message_id = api_future.result()
        message_metadata = MessageMetadata.decode(message_id)
        print(
            f"Published a message to {topic_path} with partition {message_metadata.partition.value} and offset {message_metadata.cursor.offset}."
        )

The publisher sends 100 messages to a Lite topic and prints the number of messages that the Pub/Sub Lite service receives.

## Receive messages

Receive messages from the Lite subscription using the following subscriber application:

### Go

Before trying this sample, follow the Go setup instructions in the [Pub/Sub Lite quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Lite Go API reference documentation](https://godoc.org/cloud.google.com/go/pubsub). 

To authenticate to Pub/Sub Lite, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    package main
    
    import (
    	"context"
    	"flag"
    	"fmt"
    	"log"
    	"sync/atomic"
    	"time"
    
    	"cloud.google.com/go/pubsub"
    	"cloud.google.com/go/pubsublite/pscompat"
    )
    
    func main() {
    	// NOTE: Set these flags for an existing Pub/Sub Lite subscription containing
    	// published messages when running this sample.
    	projectID := flag.String("project_id", "", "Cloud Project ID")
    	zone := flag.String("zone", "", "Cloud Zone where the topic resides, e.g. us-central1-a")
    	subscriptionID := flag.String("subscription_id", "", "Existing Pub/Sub Lite subscription")
    	timeout := flag.Duration("timeout", 90*time.Second, "The duration to receive messages")
    	flag.Parse()
    
    	ctx := context.Background()
    	subscriptionPath := fmt.Sprintf("projects/%s/locations/%s/subscriptions/%s", *projectID, *zone, *subscriptionID)
    
    	// Configure flow control settings. These settings apply per partition.
    	// The message stream is paused based on the maximum size or number of
    	// messages that the subscriber has already received, whichever condition is
    	// met first.
    	settings := pscompat.ReceiveSettings{
    		// 10 MiB. Must be greater than the allowed size of the largest message
    		// (1 MiB).
    		MaxOutstandingBytes: 10 * 1024 * 1024,
    		// 1,000 outstanding messages. Must be > 0.
    		MaxOutstandingMessages: 1000,
    	}
    
    	// Create the subscriber client.
    	subscriber, err := pscompat.NewSubscriberClientWithSettings(ctx, subscriptionPath, settings)
    	if err != nil {
    		log.Fatalf("pscompat.NewSubscriberClientWithSettings error: %v", err)
    	}
    
    	// Listen for messages until the timeout expires.
    	log.Printf("Listening to messages on %s for %v...\n", subscriptionPath, *timeout)
    	cctx, cancel := context.WithTimeout(ctx, *timeout)
    	defer cancel()
    	var receiveCount int32
    
    	// Receive blocks until the context is cancelled or an error occurs.
    	if err := subscriber.Receive(cctx, func(ctx context.Context, msg *pubsub.Message) {
    		// NOTE: May be called concurrently; synchronize access to shared memory.
    		atomic.AddInt32(&receiveCount, 1)
    
    		// Metadata decoded from the message ID contains the partition and offset.
    		metadata, err := pscompat.ParseMessageMetadata(msg.ID)
    		if err != nil {
    			log.Fatalf("Failed to parse %q: %v", msg.ID, err)
    		}
    
    		fmt.Printf("Received (partition=%d, offset=%d): %s\n", metadata.Partition, metadata.Offset, string(msg.Data))
    		msg.Ack()
    	}); err != nil {
    		log.Fatalf("SubscriberClient.Receive error: %v", err)
    	}
    
    	fmt.Printf("Received %d messages\n", receiveCount)
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Pub/Sub Lite quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Lite Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/overview). 

To authenticate to Pub/Sub Lite, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.rpc.[ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html);
    import com.google.cloud.pubsub.v1.[AckReplyConsumer](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.AckReplyConsumer.html);
    import com.google.cloud.pubsub.v1.[MessageReceiver](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.MessageReceiver.html);
    import com.google.cloud.pubsublite.[CloudRegion](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegion.html);
    import com.google.cloud.pubsublite.[CloudRegionOrZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudRegionOrZone.html);
    import com.google.cloud.pubsublite.[CloudZone](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.CloudZone.html);
    import com.google.cloud.pubsublite.[MessageMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.MessageMetadata.html);
    import com.google.cloud.pubsublite.[ProjectNumber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.ProjectNumber.html);
    import com.google.cloud.pubsublite.[SubscriptionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.proto.SubscriptionName.html);
    import com.google.cloud.pubsublite.[SubscriptionPath](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath.html);
    import com.google.cloud.pubsublite.cloudpubsub.[FlowControlSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.FlowControlSettings.html);
    import com.google.cloud.pubsublite.cloudpubsub.[MessageTransforms](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.MessageTransforms.html);
    import com.google.cloud.pubsublite.cloudpubsub.[Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.Subscriber.html);
    import com.google.cloud.pubsublite.cloudpubsub.[SubscriberSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.SubscriberSettings.html);
    import com.google.protobuf.[Timestamp](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html);
    import com.google.pubsub.v1.[PubsubMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.pubsub.v1.PubsubMessage.html);
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class SubscriberExample {
    
      public static void main(String... args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String cloudRegion = "your-cloud-region";
        char zoneId = 'b';
        // Choose an existing subscription for the subscribe example to work.
        String subscriptionId = "your-subscription-id";
        long projectNumber = Long.parseLong("123456789");
        // True if using a regional location. False if using a zonal location.
        // https://cloud.google.com/pubsub/lite/docs/topics
        boolean regional = false;
    
        subscriberExample(cloudRegion, zoneId, projectNumber, subscriptionId, regional);
      }
    
      public static void subscriberExample(
          String cloudRegion, char zoneId, long projectNumber, String subscriptionId, boolean regional)
          throws [ApiException](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException.html) {
    
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
    
        // The message stream is paused based on the maximum size or number of messages that the
        // subscriber has already received, whichever condition is met first.
        [FlowControlSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.FlowControlSettings.html) flowControlSettings =
            [FlowControlSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.FlowControlSettings.html).builder()
                // 10 MiB. Must be greater than the allowed size of the largest message (1 MiB).
                .setBytesOutstanding(10 * 1024 * 1024L)
                // 1,000 outstanding messages. Must be >0.
                .setMessagesOutstanding(1000L)
                .build();
    
        [MessageReceiver](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.MessageReceiver.html) receiver =
            (PubsubMessage message, AckReplyConsumer consumer) -> {
              System.out.println("Id : " + [MessageMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.MessageMetadata.html).[decode](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.MessageMetadata.html#com_google_cloud_pubsublite_MessageMetadata_decode_java_lang_String_)([message](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SequencedMessage.html#com_google_cloud_pubsublite_SequencedMessage_message__).getMessageId()));
              System.out.println("Data : " + [message](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SequencedMessage.html#com_google_cloud_pubsublite_SequencedMessage_message__).getData().toStringUtf8());
              System.out.println("Ordering key : " + [message](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SequencedMessage.html#com_google_cloud_pubsublite_SequencedMessage_message__).getOrderingKey());
              System.out.println("Attributes : ");
              [message](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SequencedMessage.html#com_google_cloud_pubsublite_SequencedMessage_message__)
                  .getAttributesMap()
                  .forEach(
                      (key, value) -> {
                        if (key == MessageTransforms.PUBSUB_LITE_EVENT_TIME_TIMESTAMP_PROTO) {
                          Timestamp ts = MessageTransforms.decodeAttributeEventTime(value);
                          System.out.println(key + " = " + ts.toString());
                        } else {
                          System.out.println(key + " = " + value);
                        }
                      });
    
              // Acknowledge the message.
              consumer.ack();
            };
    
        [SubscriberSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.SubscriberSettings.html) subscriberSettings =
            [SubscriberSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.SubscriberSettings.html).newBuilder()
                .setSubscriptionPath(subscriptionPath)
                .setReceiver(receiver)
                // Flow control settings are set at the partition level.
                .setPerPartitionFlowControlSettings(flowControlSettings)
                .build();
    
        [Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.Subscriber.html) subscriber = [Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.Subscriber.html).create(subscriberSettings);
    
        // Start the subscriber. Upon successful starting, its state will become RUNNING.
        subscriber.[startAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsub/latest/com.google.cloud.pubsub.v1.Subscriber.html#com_google_cloud_pubsub_v1_Subscriber_startAsync__)().awaitRunning();
    
        System.out.println("Listening to messages on " + [subscriptionPath](https://docs.cloud.google.com/java/docs/reference/pubsublite-spark-sql-streaming/latest/com.google.cloud.pubsublite.spark.PslReadDataSourceOptions.html#com_google_cloud_pubsublite_spark_PslReadDataSourceOptions_subscriptionPath__).[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.SubscriptionPath.html#com_google_cloud_pubsublite_SubscriptionPath_toString__)() + "...");
    
        try {
          System.out.println(subscriber.state());
          // Wait 90 seconds for the subscriber to reach TERMINATED state. If it encounters
          // unrecoverable errors before then, its state will change to FAILED and an
          // IllegalStateException will be thrown.
          subscriber.awaitTerminated(90, TimeUnit.SECONDS);
        } catch (TimeoutException t) {
          // Shut down the subscriber. This will change the state of the subscriber to TERMINATED.
          subscriber.[stopAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.wire.ApiServiceUtils.html#com_google_cloud_pubsublite_internal_wire_ApiServiceUtils_stopAsync_java_lang_Iterable___extends_com_google_api_core_ApiService__)().awaitTerminated();
          System.out.println("Subscriber is shut down: " + subscriber.state());
        }
      }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Pub/Sub Lite quickstart using client libraries](https://docs.cloud.google.com/pubsub/docs/quickstart-client-libraries). For more information, see the [Pub/Sub Lite Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/pubsub/latest). 

To authenticate to Pub/Sub Lite, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from concurrent.futures._base import TimeoutError
    from google.pubsub_v1 import PubsubMessage
    from google.cloud.pubsublite.cloudpubsub import [SubscriberClient](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.SubscriberClient.html)
    from google.cloud.pubsublite.types import (
        CloudRegion,
        CloudZone,
        FlowControlSettings,
        MessageMetadata,
        SubscriptionPath,
    )
    
    # TODO(developer):
    # project_number = 1122334455
    # cloud_region = "us-central1"
    # zone_id = "a"
    # subscription_id = "your-subscription-id"
    # timeout = 90
    # regional = True
    
    if regional:
        location = CloudRegion(cloud_region)
    else:
        location = CloudZone(CloudRegion(cloud_region), zone_id)
    
    subscription_path = SubscriptionPath(project_number, location, subscription_id)
    # Configure when to pause the message stream for more incoming messages based on the
    # maximum size or number of messages that a single-partition subscriber has received,
    # whichever condition is met first.
    per_partition_flow_control_settings = FlowControlSettings(
        # 1,000 outstanding messages. Must be >0.
        messages_outstanding=1000,
        # 10 MiB. Must be greater than the allowed size of the largest message (1 MiB).
        bytes_outstanding=10 * 1024 * 1024,
    )
    
    def callback(message: PubsubMessage):
        message_data = message.data.decode("utf-8")
        metadata = MessageMetadata.decode(message.message_id)
        print(
            f"Received {message_data} of ordering key {message.ordering_key} with id {metadata}."
        )
        message.ack()
    
    # SubscriberClient() must be used in a `with` block or have __enter__() called before use.
    with SubscriberClient() as subscriber_client:
    
        streaming_pull_future = [subscriber_client](https://docs.cloud.google.com/python/docs/reference/pubsublite/latest/google.cloud.pubsublite.cloudpubsub.subscriber_client.html).subscribe(
            subscription_path,
            callback=callback,
            per_partition_flow_control_settings=per_partition_flow_control_settings,
        )
    
        print(f"Listening for messages on {str(subscription_path)}...")
    
        try:
            streaming_pull_future.result(timeout=timeout)
        except TimeoutError or KeyboardInterrupt:
            streaming_pull_future.cancel()
            assert streaming_pull_future.done()

After the subscriber receives a message, the subscriber prints the message ID and the message data.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, delete the Google Cloud project with the resources. 

  1. To avoid incurring charges to your Google Cloud account for the resources used in this guide, delete the topic and subscription. 
         
         gcloud pubsub lite-subscriptions delete testSub --location=us-central1
         gcloud pubsub lite-topics delete testTopic --location=us-central1

  2. Optional: Revoke the authentication credentials that you created, and delete the local credential file. 
         
         gcloud auth application-default revoke

  3. Optional: Revoke credentials from the gcloud CLI. 
         
         gcloud auth revoke




## What's next

  * Learn more about [Lite topics](https://docs.cloud.google.com/pubsub/lite/docs/topics) and [Lite subscriptions](https://docs.cloud.google.com/pubsub/lite/docs/topics).
  * Learn more about [sending](https://docs.cloud.google.com/pubsub/lite/docs/publishing) and [receiving](https://docs.cloud.google.com/pubsub/lite/docs/subscribing) messages.
  * Look through [code samples for the client library](https://github.com/googleapis/java-pubsublite).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
