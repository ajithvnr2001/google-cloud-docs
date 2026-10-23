---
url: https://docs.cloud.google.com/storage/docs/samples/storage-print-pubsub-bucket-notification/
title: Get a Pub/Sub notification \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:34:44.615946+00:00
---

# Get a Pub/Sub notification  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-print-pubsub-bucket-notification/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Get a Pub/Sub notification Stay organized with collections  Save and categorize content based on your preferences. 

Provides an example of how to get Pub/Sub notification metadata.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Configure Pub/Sub notifications for Cloud Storage](https://docs.cloud.google.com/storage/docs/reporting-changes)



## Code sample

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name,
       std::string const& notification_id) {
      StatusOr<gcs::NotificationMetadata> notification =
          client.GetNotification(bucket_name, notification_id);
      if (!notification) throw std::move(notification).status();
    
      std::cout << "Notification " << notification->id() << " for bucket "
                << bucket_name << "\n";
      if (notification->object_name_prefix().empty()) {
        std::cout << "This notification is sent for all objects in the bucket\n";
      } else {
        std::cout << "This notification is sent only for objects starting with"
                  << " the prefix " << notification->object_name_prefix() << "\n";
      }
      std::cout << "Full details for the notification:\n"
                << *notification << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using Google.Apis.Storage.v1.Data;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class GetPubSubNotificationSample
    {
        public Notification GetPubSubNotification(
            string bucketName = "your-unique-bucket-name",
            string notificationId = "notificationId")
        {
            [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html) storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            Notification notification = storage.[GetNotification](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_GetNotification_System_String_System_String_Google_Cloud_Storage_V1_GetNotificationOptions_)(bucketName, notificationId);
    
            Console.WriteLine("ID: " + notification.Id);
            Console.WriteLine("Topic: " + notification.Topic);
            Console.WriteLine("EventTypes: " + notification.EventTypes);
            Console.WriteLine("CustomAttributes: " + notification.CustomAttributes);
            Console.WriteLine("PayloadFormat: " + notification.PayloadFormat);
            Console.WriteLine("ObjectNamePrefix: " + notification.ObjectNamePrefix);
            Console.WriteLine("ETag: " + notification.ETag);
            Console.WriteLine("SelfLink: " + notification.SelfLink);
            Console.WriteLine("Kind: " + notification.Kind);
    
            return notification;
        }
    }
    

### Go

For more information, see the [Cloud Storage Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storage). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/storage"
    )
    
    // printPubsubBucketNotification gets a notification configuration for a bucket.
    func printPubsubBucketNotification(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucketName, notificationID string) error {
    	// bucketName := "bucket-name"
    	// notificationID := "notification-id"
    
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	notifications, err := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucketName).[Notifications](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Notifications)(ctx)
    	if err != nil {
    		return fmt.Errorf("Bucket.Notifications: %w", err)
    	}
    
    	n := notifications[notificationID]
    	fmt.Fprintf(w, "Notification: %+v", n)
    
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[Notification](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Notification.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class PrintPubSubNotification {
    
      public static void printPubSubNotification(String bucketName, String notificationId) {
        // The ID to give your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The Pub/Sub topic you would like to find
        // String notificationId = "your-unique-notification-id"
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        [Notification](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Notification.html) notification = storage.[getNotification](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_getNotification_java_lang_String_java_lang_String_)(bucketName, notificationId);
        System.out.println(
            "Found notification " + notification.[getTopic](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.NotificationInfo.html#com_google_cloud_storage_NotificationInfo_getTopic__)() + " for bucket " + bucketName);
      }
    }

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The ID of your GCS bucket
    // const bucketName = 'your-unique-bucket-name';
    
    // The ID of the notification
    // const notificationId = '1';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function getMetadata() {
      // Get the notification metadata
      const [metadata] = await storage
        .bucket(bucketName)
        .[notification](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/bucket.html)(notificationId)
        .getMetadata();
    
      console.log(`ID: ${metadata.id}`);
      console.log(`Topic: ${metadata.[topic](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/notificationmetadata.html)}`);
      console.log(`Event Types: ${metadata.[event_types](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/notificationmetadata.html)}`);
      console.log(`Custom Attributes: ${metadata.[custom_attributes](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/notificationmetadata.html)}`);
      console.log(`Payload Format: ${metadata.[payload_format](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/notificationmetadata.html)}`);
      console.log(`Object Name Prefix: ${metadata.[object_name_prefix](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/notificationmetadata.html)}`);
      console.log(`Etag: ${metadata.etag}`);
      console.log(`Self Link: ${metadata.selfLink}`);
      console.log(`Kind: ${metadata.kind}`);
    }
    
    getMetadata().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Lists notification configurations for a bucket.
     * This sample is used on this page:
     *   https://cloud.google.com/storage/docs/reporting-changes
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'your-bucket')
     * @param string $notificationId The ID of the notification.
     *        (e.g. 'your-notification-id')
     */
    function print_pubsub_bucket_notification(
        string $bucketName,
        string $notificationId
    ): void {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
        $notification = $bucket->notification($notificationId);
        $notificationInfo = $notification->info();
    
        printf(
            <<<EOF
    Notification ID: %s
    Topic Name: %s
    Event Types: %s
    Custom Attributes: %s
    Payload Format: %s
    Blob Name Prefix: %s
    Etag: %s
    Self Link: %s
    EOF . PHP_EOL,
            $notification->id(),
            $notificationInfo['topic'],
            $notificationInfo['event_types'] ?? '',
            $notificationInfo['custom_attributes'] ?? '',
            $notificationInfo['payload_format'],
            $notificationInfo['blob_name_prefix'] ?? '',
            $notificationInfo['etag'],
            $notificationInfo['selfLink']
        );
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def print_pubsub_bucket_notification(bucket_name, notification_id):
        """Gets a notification configuration for a bucket."""
        # The ID of your GCS bucket
        # bucket_name = "your-bucket-name"
        # The ID of the notification
        # notification_id = "your-notification-id"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
        notification = bucket.[get_notification](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_get_notification)(notification_id)
    
        print(f"Notification ID: {notification.[notification_id](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.notification.BucketNotification.html#google_cloud_storage_notification_BucketNotification_notification_id)}")
        print(f"Topic Name: {notification.[topic_name](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.notification.BucketNotification.html#google_cloud_storage_notification_BucketNotification_topic_name)}")
        print(f"Event Types: {notification.[event_types](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.notification.BucketNotification.html#google_cloud_storage_notification_BucketNotification_event_types)}")
        print(f"Custom Attributes: {notification.[custom_attributes](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.notification.BucketNotification.html#google_cloud_storage_notification_BucketNotification_custom_attributes)}")
        print(f"Payload Format: {notification.[payload_format](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.notification.BucketNotification.html#google_cloud_storage_notification_BucketNotification_payload_format)}")
        print(f"Blob Name Prefix: {notification.[blob_name_prefix](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.notification.BucketNotification.html#google_cloud_storage_notification_BucketNotification_blob_name_prefix)}")
        print(f"Etag: {notification.etag}")
        print(f"Self Link: {notification.self_link}")
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    require "google/cloud/storage"
    
    def print_pubsub_bucket_notification bucket_name:, notification_id:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      # The ID of your notification configured for the bucket
      # notification_id = "your-notification-id"
    
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket  = storage.bucket bucket_name
      notification = bucket.[notification](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) notification_id
    
      puts "Notification ID: #{notification.id}"
      puts "Topic Name: #{notification.[topic](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Notification.html)}"
      puts "Event Types: #{notification.event_types}"
      puts "Kind of Notification: #{notification.kind}"
      puts "Custom Attributes: #{notification.[custom_attrs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Notification.html)}"
      puts "Payload Format: #{notification.[payload](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Notification.html)}"
      puts "Blob Name Prefix: #{notification.prefix}"
      puts "Self Link: #{notification.api_url}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
