---
url: https://docs.cloud.google.com/storage/docs/holding-objects/
title: Use object holds \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:48.326887+00:00
---

# Use object holds  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/holding-objects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Use object holds Stay organized with collections  Save and categorize content based on your preferences. 

[Overview](https://docs.cloud.google.com/storage/docs/object-holds)

You can help protect your Cloud Storage data from deletion or replacement by using [object holds](https://docs.cloud.google.com/storage/docs/object-holds). These holds help you meet regulatory compliance or legal discovery requirements. You can apply event-based and temporary holds to individual objects. Additionally, you can configure buckets to apply event-based holds to new objects by default.

This page describes how to use object holds, including placing holds by default on new objects and placing holds on individual objects.

## Required permissions

Before using this feature in Cloud Storage, you must have sufficient permission to view and update buckets and objects in Cloud Storage:

  * If you own the project that contains the bucket, you most likely have the necessary permissions.

  * If you use IAM, you should have `storage.buckets.update`, `storage.buckets.get`, `storage.objects.update`, and `storage.objects.get` permissions on the relevant bucket. See [Using IAM Permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions) for instructions on how to get a role, such as **Storage Admin** , that has these permissions.

  * If you use ACLs, you should have OWNER permission on the relevant bucket and on the objects within it. See [Setting ACLs](https://docs.cloud.google.com/storage/docs/access-control/create-manage-lists#set-an-acl) for instructions on how to do this.




## Use the default event-based hold property

The following tasks show you how to set and view the [default event-based hold property](https://docs.cloud.google.com/storage/docs/object-holds#default-holds) on a bucket. When this property is enabled, new objects added to the bucket automatically get an event-based hold placed on them.

### Set the default event-based hold property

To enable or disable the default event-based hold property for a bucket:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket that you want to set the default event-based hold property for.

  3. Select the **Protection** tab near the top of the page.

The current status for the bucket appears in the **Default event-based hold option** section.

  4. In the **Default event-based hold option** section, click the current status to change it.

The status appears as either **Enabled** or **Disabled**.




To learn how to get detailed error information about failed Cloud Storage operations in the Google Cloud console, see [Troubleshooting](https://docs.cloud.google.com/storage/docs/troubleshooting#trouble-console).

### Command line

Use the [`gcloud storage buckets update`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/update) command with the appropriate flag:
    
    
    gcloud storage buckets update gs://BUCKET_NAME FLAG

Where:

  * `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.

  * `FLAG` is either `--default-event-based-hold` to enable default event-based object holds or `--no-default-event-based-hold` to disable them.




### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample enables default event-based holds on a bucket:
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name) {
      StatusOr<gcs::BucketMetadata> original =
          client.GetBucketMetadata(bucket_name);
      if (!original) throw std::move(original).status();
    
      StatusOr<gcs::BucketMetadata> patched = client.PatchBucket(
          bucket_name,
          gcs::BucketMetadataPatchBuilder().SetDefaultEventBasedHold(true),
          gcs::IfMetagenerationMatch(original->metageneration()));
      if (!patched) throw std::move(patched).status();
    
      std::cout << "The default event-based hold for objects in bucket "
                << bucket_name << " is "
                << (patched->default_event_based_hold() ? "enabled" : "disabled")
                << "\n";
    }

The following sample disables default event-based holds on a bucket:
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name) {
      StatusOr<gcs::BucketMetadata> original =
          client.GetBucketMetadata(bucket_name);
    
      if (!original) throw std::move(original).status();
      StatusOr<gcs::BucketMetadata> patched = client.PatchBucket(
          bucket_name,
          gcs::BucketMetadataPatchBuilder().SetDefaultEventBasedHold(false),
          gcs::IfMetagenerationMatch(original->metageneration()));
      if (!patched) throw std::move(patched).status();
    
      std::cout << "The default event-based hold for objects in bucket "
                << bucket_name << " is "
                << (patched->default_event_based_hold() ? "enabled" : "disabled")
                << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample enables default event-based holds on a bucket:
    
    
    using Google.Apis.Storage.v1.Data;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class EnableBucketDefaultEventBasedHoldSample
    {
        public Bucket EnableBucketDefaultEventBasedHold(string bucketName = "your-unique-bucket-name")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var bucket = storage.GetBucket(bucketName);
            bucket.DefaultEventBasedHold = true;
            bucket = storage.UpdateBucket(bucket);
            Console.WriteLine($"Default event-based hold was enabled for {bucketName}");
            return bucket;
        }
    }

The following sample disables default event-based holds on a bucket:
    
    
    using Google.Apis.Storage.v1.Data;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class DisableDefaultEventBasedHoldSample
    {
        public Bucket DisableDefaultEventBasedHold(string bucketName = "your-unique-bucket-name")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var bucket = storage.GetBucket(bucketName);
            bucket.DefaultEventBasedHold = false;
            bucket = storage.UpdateBucket(bucket);
            Console.WriteLine($"Default event-based hold was disabled for {bucketName}");
            return bucket;
        }
    }

### Go

For more information, see the [Cloud Storage Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storage). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample enables default event-based holds on a bucket:
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/storage"
    )
    
    // enableDefaultEventBasedHold sets event-based hold to true.
    func enableDefaultEventBasedHold(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucketName string) error {
    	// bucketName := "bucket-name"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    
    	bucket := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucketName)
    	bucketAttrsToUpdate := storage.[BucketAttrsToUpdate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketAttrsToUpdate){
    		DefaultEventBasedHold: true,
    	}
    	if _, err := bucket.Update(ctx, bucketAttrsToUpdate); err != nil {
    		return fmt.Errorf("Bucket(%q).Update: %w", bucketName, err)
    	}
    	fmt.Fprintf(w, "Default event-based hold was enabled for %v\n", bucketName)
    	return nil
    }
    

The following sample disables default event-based holds on a bucket:
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/storage"
    )
    
    // disableDefaultEventBasedHold sets event-based hold to false.
    func disableDefaultEventBasedHold(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucketName string) error {
    	// bucketName := "bucket-name"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    
    	bucket := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucketName)
    	bucketAttrsToUpdate := storage.[BucketAttrsToUpdate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketAttrsToUpdate){
    		DefaultEventBasedHold: false,
    	}
    	if _, err := bucket.Update(ctx, bucketAttrsToUpdate); err != nil {
    		return fmt.Errorf("Bucket(%q).Update: %w", bucketName, err)
    	}
    	fmt.Fprintf(w, "Default event-based hold was disabled for %v\n", bucketName)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample enables default event-based holds on a bucket:
    
    
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).[BucketTargetOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.BucketTargetOption.html);
    import com.google.cloud.storage.[StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class EnableDefaultEventBasedHold {
      public static void enableDefaultEventBasedHold(String projectId, String bucketName)
          throws [StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        // first look up the bucket, so we will have its metageneration
        [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket = storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName);
        storage.[update](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_update_com_google_cloud_storage_BlobInfo_)(
            bucket.toBuilder().setDefaultEventBasedHold(true).build(),
            BucketTargetOption.metagenerationMatch());
    
        System.out.println("Default event-based hold was enabled for " + bucketName);
      }
    }

The following sample disables default event-based holds on a bucket:
    
    
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).[BucketTargetOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.BucketTargetOption.html);
    import com.google.cloud.storage.[StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class DisableDefaultEventBasedHold {
      public static void disableDefaultEventBasedHold(String projectId, String bucketName)
          throws [StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        // first look up the bucket, so we will have its metageneration
        [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket = storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName);
        storage.[update](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_update_com_google_cloud_storage_BlobInfo_)(
            bucket.toBuilder().setDefaultEventBasedHold(false).build(),
            BucketTargetOption.metagenerationMatch());
    
        System.out.println("Default event-based hold was disabled for " + bucketName);
      }
    }

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample enables default event-based holds on a bucket:
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The ID of your GCS bucket
    // const bucketName = 'your-unique-bucket-name';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function enableDefaultEventBasedHold() {
      // Enables a default event-based hold for the bucket.
      await storage.bucket(bucketName).setMetadata({
        defaultEventBasedHold: true,
      });
    
      console.log(`Default event-based hold was enabled for ${bucketName}.`);
    }
    
    enableDefaultEventBasedHold().catch(console.error);

The following sample disables default event-based holds on a bucket:
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The ID of your GCS bucket
    // const bucketName = 'your-unique-bucket-name';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function disableDefaultEventBasedHold() {
      // Disables a default event-based hold for a bucket.
      await storage.bucket(bucketName).setMetadata({
        defaultEventBasedHold: false,
      });
      console.log(`Default event-based hold was disabled for ${bucketName}.`);
    }
    
    disableDefaultEventBasedHold().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample enables default event-based holds on a bucket:
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Enables a default event-based hold for a bucket.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     */
    function enable_default_event_based_hold(string $bucketName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
        $bucket->update(['defaultEventBasedHold' => true]);
        printf('Default event-based hold was enabled for %s' . PHP_EOL, $bucketName);
    }

The following sample disables default event-based holds on a bucket:
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Disables a default event-based hold for a bucket.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     */
    function disable_default_event_based_hold(string $bucketName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
        $bucket->update(['defaultEventBasedHold' => false]);
        printf('Default event-based hold was disabled for %s' . PHP_EOL, $bucketName);
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample enables default event-based holds on a bucket:
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def enable_default_event_based_hold(bucket_name):
        """Enables the default event based hold on a given bucket"""
        # bucket_name = "my-bucket"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
        bucket.[default_event_based_hold](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_default_event_based_hold) = True
        bucket.patch()
    
        print(f"Default event based hold was enabled for {bucket_name}")
    
    

The following sample disables default event-based holds on a bucket:
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def disable_default_event_based_hold(bucket_name):
        """Disables the default event based hold on a given bucket"""
        # bucket_name = "my-bucket"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
        bucket = storage_client.[get_bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_get_bucket)(bucket_name)
        bucket.[default_event_based_hold](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_default_event_based_hold) = False
        bucket.patch()
    
        print(f"Default event based hold was disabled for {bucket_name}")
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample enables default event-based holds on a bucket:
    
    
    def enable_default_event_based_hold bucket_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket  = storage.bucket bucket_name
    
      bucket.update do |b|
        b.default_event_based_hold = true
      end
    
      puts "Default event-based hold was enabled for #{bucket_name}."
    end

The following sample disables default event-based holds on a bucket:
    
    
    def disable_default_event_based_hold bucket_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket  = storage.bucket bucket_name
    
      bucket.update do |b|
        b.default_event_based_hold = false
      end
    
      puts "Default event-based hold was disabled for #{bucket_name}."
    end

### Rust

The following sample enables default event-based holds on a bucket:
    
    
    use google_cloud_storage::client::StorageControl;
    use google_cloud_wkt::FieldMask;
    
    pub async fn sample(client: &StorageControl, bucket_id: &str) -> anyhow::Result<()> {
        let bucket = client
            .get_bucket()
            .set_name(format!("projects/_/buckets/{bucket_id}"))
            .send()
            .await?;
        let metageneration = bucket.metageneration;
        let bucket = client
            .update_bucket()
            .set_bucket(bucket.set_default_event_based_hold(true))
            .set_if_metageneration_match(metageneration)
            .set_update_mask(FieldMask::default().set_paths(["default_event_based_hold"]))
            .send()
            .await?;
        println!("Default event-based hold was enabled for bucket {bucket_id}: {bucket:?}");
        Ok(())
    }

The following sample disables default event-based holds on a bucket:
    
    
    use google_cloud_storage::client::StorageControl;
    use google_cloud_wkt::FieldMask;
    
    pub async fn sample(client: &StorageControl, bucket_id: &str) -> anyhow::Result<()> {
        let bucket = client
            .get_bucket()
            .set_name(format!("projects/_/buckets/{bucket_id}"))
            .send()
            .await?;
        let metageneration = bucket.metageneration;
        let bucket = client
            .update_bucket()
            .set_bucket(bucket.set_default_event_based_hold(false))
            .set_if_metageneration_match(metageneration)
            .set_update_mask(FieldMask::default().set_paths(["default_event_based_hold"]))
            .send()
            .await?;
        println!("Default event-based hold was disabled for bucket {bucket_id}: {bucket:?}");
        Ok(())
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the following information:
         
         {
           "defaultEventBasedHold": STATE
         }

Where STATE is either `true` or `false`.

  3. Use [`cURL`](http://curl.haxx.se/) to call the JSON API with a [`PATCH` Bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/patch) request:
         
         curl -X PATCH --data-binary @JSON_FILE_NAME \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME?fields=defaultEventBasedHold"

Where:

     * `JSON_FILE_NAME` is the path for the file that you created in Step 2.
     * `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.



### XML API

The XML API cannot be used to work with object holds. Use one of the other Cloud Storage tools, such as the gcloud CLI, instead.

### Get the default hold status of a bucket

To view whether a bucket places event-based holds on new objects by default:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket that you want to check the default event-based status for.

  3. Select the **Protection** tab near the top of the page.

  4. The status appears in the **Default event-based hold option** section.




To learn how to get detailed error information about failed Cloud Storage operations in the Google Cloud console, see [Troubleshooting](https://docs.cloud.google.com/storage/docs/troubleshooting#trouble-console).

### Command line

Use the [`gcloud storage buckets describe`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/describe) command with the `--format` flag:
    
    
    gcloud storage buckets describe gs://BUCKET_NAME --format="default(default_event_based_hold)"

Where `BUCKET_NAME` is the name of the bucket whose status you want to view. For example, `my-bucket`.

If successful, the response looks similar to the following example:
    
    
    default_event_based_hold: true

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name) {
      StatusOr<gcs::BucketMetadata> bucket_metadata =
          client.GetBucketMetadata(bucket_name);
      if (!bucket_metadata) throw std::move(bucket_metadata).status();
    
      std::cout << "The default event-based hold for objects in bucket "
                << bucket_metadata->name() << " is "
                << (bucket_metadata->default_event_based_hold() ? "enabled"
                                                                : "disabled")
                << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class GetDefaultEventBasedHoldSample
    {
        public bool GetDefaultEventBasedHold(string bucketName = "your-unique-bucket-name")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var bucket = storage.GetBucket(bucketName);
            bool defaultEventBasedHold = bucket.DefaultEventBasedHold ?? false;
            Console.WriteLine($"Default event-based hold: {defaultEventBasedHold}");
            return defaultEventBasedHold;
        }
    }

### Go

For more information, see the [Cloud Storage Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storage). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/storage"
    )
    
    // getDefaultEventBasedHold gets default event-based hold state.
    func getDefaultEventBasedHold(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucketName string) (*storage.[BucketAttrs](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketAttrs), error) {
    	// bucketName := "bucket-name"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    
    	attrs, err := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucketName).Attrs(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("Bucket(%q).Attrs: %w", bucketName, err)
    	}
    	fmt.Fprintf(w, "Default event-based hold enabled? %t\n", attrs.DefaultEventBasedHold)
    	return attrs, nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class GetDefaultEventBasedHold {
      public static void getDefaultEventBasedHold(String projectId, String bucketName)
          throws [StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket =
            storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(
                bucketName,
                Storage.BucketGetOption.fields(Storage.BucketField.DEFAULT_EVENT_BASED_HOLD));
    
        if (bucket.[getDefaultEventBasedHold](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_getDefaultEventBasedHold__)() != null && bucket.[getDefaultEventBasedHold](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_getDefaultEventBasedHold__)()) {
          System.out.println("Default event-based hold is enabled for " + bucketName);
        } else {
          System.out.println("Default event-based hold is not enabled for " + bucketName);
        }
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
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function getDefaultEventBasedHold() {
      const [metadata] = await storage.bucket(bucketName).getMetadata();
      console.log(`Default event-based hold: ${metadata.defaultEventBasedHold}.`);
    }
    
    getDefaultEventBasedHold().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Enables a default event-based hold for a bucket.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     */
    function get_default_event_based_hold(string $bucketName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
    
        if ($bucket->info()['defaultEventBasedHold']) {
            printf('Default event-based hold is enabled for ' . $bucketName . PHP_EOL);
        } else {
            printf('Default event-based hold is not enabled for ' . $bucketName . PHP_EOL);
        }
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def get_default_event_based_hold(bucket_name):
        """Gets the default event based hold on a given bucket"""
        # bucket_name = "my-bucket"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
        bucket = storage_client.[get_bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_get_bucket)(bucket_name)
    
        if bucket.[default_event_based_hold](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_default_event_based_hold):
            print(f"Default event-based hold is enabled for {bucket_name}")
        else:
            print(
                f"Default event-based hold is not enabled for {bucket_name}"
            )
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def get_default_event_based_hold bucket_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket  = storage.bucket bucket_name
    
      if bucket.[default_event_based_hold?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)
        puts "Default event-based hold is enabled for #{bucket_name}."
      else
        puts "Default event-based hold is not enabled for #{bucket_name}."
      end
    end

### Rust
    
    
    use google_cloud_storage::client::StorageControl;
    
    pub async fn sample(client: &StorageControl, bucket_id: &str) -> anyhow::Result<()> {
        let bucket = client
            .get_bucket()
            .set_name(format!("projects/_/buckets/{bucket_id}"))
            .send()
            .await?;
        println!(
            "The default event-based hold for bucket \"{}\" is {}.",
            bucket_id,
            if bucket.default_event_based_hold {
                "enabled"
            } else {
                "disabled"
            }
        );
        Ok(())
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the JSON API with a [`GET` Bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/get) request that includes the desired `fields`:
         
         curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME?fields=defaultEventBasedHold"

Where `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.

If the bucket has a default event-based hold enabled for it, the response looks like the following example:
         
         {
           "defaultEventBasedHold": true
         }




### XML API

The XML API cannot be used to work with object holds. Use one of the other Cloud Storage tools, such as the gcloud CLI, instead.

## Manage individual object holds

The following tasks show you how to modify and view [holds](https://docs.cloud.google.com/storage/docs/object-holds) on individual objects.

### Place or release an object hold

To place or release a hold on an object in your bucket:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket that has the objects you want to place or remove holds on.

  3. Select the checkbox next to the names of objects you want to place or remove holds on.

  4. Click the **Manage holds** button.

The _Manage holds_ window appears.

  5. Toggle the checkboxes for each hold type as desired.

  6. Click **Save hold settings**.




To learn how to get detailed error information about failed Cloud Storage operations in the Google Cloud console, see [Troubleshooting](https://docs.cloud.google.com/storage/docs/troubleshooting#trouble-console).

### Command line

Use the [`gcloud storage objects update`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/objects/update) command with the appropriate flag::
    
    
    gcloud storage objects update gs://BUCKET_NAME/OBJECT_NAME FLAG

Where:

  * `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.
  * `OBJECT_NAME` is the name of the relevant object. For example, `pets/dog.png`.
  * `FLAG` is one of the following:

    * `--event-based-hold` to enable an event based hold on the object.
    * `--no-event-based-hold` to disable any event based hold on the object.
    * `--temporary-hold` to enable a temporary hold on the object.
    * `--no-temporary-hold` to disable any temporary hold on the object.



See [Object holds](https://docs.cloud.google.com/storage/docs/object-holds) for more information about hold types.

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample sets an event-based hold on an object:
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name,
       std::string const& object_name) {
      StatusOr<gcs::ObjectMetadata> original =
          client.GetObjectMetadata(bucket_name, object_name);
      if (!original) throw std::move(original).status();
    
      StatusOr<gcs::ObjectMetadata> updated = client.PatchObject(
          bucket_name, object_name,
          gcs::ObjectMetadataPatchBuilder().SetEventBasedHold(true),
          gcs::IfMetagenerationMatch(original->metageneration()));
      if (!updated) throw std::move(updated).status();
    
      std::cout << "The event hold for object " << updated->name()
                << " in bucket " << updated->bucket() << " is "
                << (updated->event_based_hold() ? "enabled" : "disabled") << "\n";
    }

The following sample releases an event-based hold on an object:
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name,
       std::string const& object_name) {
      StatusOr<gcs::ObjectMetadata> original =
          client.GetObjectMetadata(bucket_name, object_name);
      if (!original) throw std::move(original).status();
    
      StatusOr<gcs::ObjectMetadata> updated = client.PatchObject(
          bucket_name, object_name,
          gcs::ObjectMetadataPatchBuilder().SetEventBasedHold(false),
          gcs::IfMetagenerationMatch(original->metageneration()));
      if (!updated) throw std::move(updated).status();
    
      std::cout << "The event hold for object " << updated->name()
                << " in bucket " << updated->bucket() << " is "
                << (updated->event_based_hold() ? "enabled" : "disabled") << "\n";
    }

The following sample sets a temporary hold on an object:
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name,
       std::string const& object_name) {
      StatusOr<gcs::ObjectMetadata> original =
          client.GetObjectMetadata(bucket_name, object_name);
      if (!original) throw std::move(original).status();
    
      StatusOr<gcs::ObjectMetadata> updated = client.PatchObject(
          bucket_name, object_name,
          gcs::ObjectMetadataPatchBuilder().SetTemporaryHold(true),
          gcs::IfMetagenerationMatch(original->metageneration()));
      if (!updated) throw std::move(updated).status();
    
      std::cout << "The temporary hold for object " << updated->name()
                << " in bucket " << updated->bucket() << " is "
                << (updated->temporary_hold() ? "enabled" : "disabled") << "\n";
    }

The following sample releases a temporary hold on an object:
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name,
       std::string const& object_name) {
      StatusOr<gcs::ObjectMetadata> original =
          client.GetObjectMetadata(bucket_name, object_name);
    
      if (!original) throw std::move(original).status();
      StatusOr<gcs::ObjectMetadata> updated = client.PatchObject(
          bucket_name, object_name,
          gcs::ObjectMetadataPatchBuilder().SetTemporaryHold(false),
          gcs::IfMetagenerationMatch(original->metageneration()));
    
      if (!updated) throw std::move(updated).status();
      std::cout << "The temporary hold for object " << updated->name()
                << " in bucket " << updated->bucket() << " is "
                << (updated->temporary_hold() ? "enabled" : "disabled") << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample sets an event-based hold on an object:
    
    
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class SetEventBasedHoldSample
    {
        public void SetEventBasedHold(
            string bucketName = "your-unique-bucket-name",
            string objectName = "your-object-name")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var storageObject = storage.GetObject(bucketName, objectName);
            storageObject.EventBasedHold = true;
            storage.UpdateObject(storageObject);
            Console.WriteLine($"Event-based hold was set for {objectName}.");
        }
    }

The following sample releases an event-based hold on an object:
    
    
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class ReleaseEventBasedHoldSample
    {
        public void ReleaseEventBasedHold(
            string bucketName = "your-unique-bucket-name",
            string objectName = "your-object-name")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var storageObject = storage.GetObject(bucketName, objectName);
            storageObject.EventBasedHold = false;
            storage.UpdateObject(storageObject);
            Console.WriteLine($"Event-based hold was released for {objectName}.");
        }
    }

The following sample sets a temporary hold on an object:
    
    
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    
    public class SetTemporaryHoldSample
    {
        public void SetTemporaryHold(
            string bucketName = "your-unique-bucket-name",
            string objectName = "your-object-name")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var storageObject = storage.GetObject(bucketName, objectName);
            storageObject.TemporaryHold = true;
            storage.UpdateObject(storageObject);
            System.Console.WriteLine($"Temporary hold was set for {objectName}.");
        }
    }

The following sample releases a temporary hold on an object:
    
    
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class ReleaseTemporaryHoldSample
    {
        public void ReleaseTemporaryHold(
            string bucketName = "your-unique-bucket-name",
            string objectName = "your-object-name")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var storageObject = storage.GetObject(bucketName, objectName);
            storageObject.TemporaryHold = false;
            storage.UpdateObject(storageObject);
            Console.WriteLine($"Temporary hold was released for {objectName}.");
        }
    }

### Go

For more information, see the [Cloud Storage Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storage). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample sets an event-based hold on an object:
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/storage"
    )
    
    // setEventBasedHold sets EventBasedHold flag of an object to true.
    func setEventBasedHold(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucket, object string) error {
    	// bucket := "bucket-name"
    	// object := "object-name"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    
    	o := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucket).[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)(object)
    
    	// Optional: set a metageneration-match precondition to avoid potential race
    	// conditions and data corruptions. The request to update is aborted if the
    	// object's metageneration does not match your precondition.
    	attrs, err := o.Attrs(ctx)
    	if err != nil {
    		return fmt.Errorf("object.Attrs: %w", err)
    	}
    	o = o.If(storage.[Conditions](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Conditions){MetagenerationMatch: attrs.Metageneration})
    
    	// Update the object to add the object hold.
    	objectAttrsToUpdate := storage.[ObjectAttrsToUpdate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectAttrsToUpdate){
    		EventBasedHold: true,
    	}
    	if _, err := o.Update(ctx, objectAttrsToUpdate); err != nil {
    		return fmt.Errorf("Object(%q).Update: %w", object, err)
    	}
    	fmt.Fprintf(w, "Default event based hold was enabled for %v.\n", object)
    	return nil
    }
    

The following sample releases an event-based hold on an object:
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/storage"
    )
    
    // releaseEventBasedHold releases an object with event-based hold.
    func releaseEventBasedHold(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucket, object string) error {
    	// bucket := "bucket-name"
    	// object := "object-name"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    
    	o := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucket).[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)(object)
    
    	// Optional: set a metageneration-match precondition to avoid potential race
    	// conditions and data corruptions. The request to update is aborted if the
    	// object's metageneration does not match your precondition.
    	attrs, err := o.Attrs(ctx)
    	if err != nil {
    		return fmt.Errorf("object.Attrs: %w", err)
    	}
    	o = o.If(storage.[Conditions](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Conditions){MetagenerationMatch: attrs.Metageneration})
    
    	// Update the object to release the object hold.
    	objectAttrsToUpdate := storage.[ObjectAttrsToUpdate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectAttrsToUpdate){
    		EventBasedHold: false,
    	}
    	if _, err := o.Update(ctx, objectAttrsToUpdate); err != nil {
    		return fmt.Errorf("Object(%q).Update: %w", object, err)
    	}
    	fmt.Fprintf(w, "Event based hold was released for %v.\n", object)
    	return nil
    }
    

The following sample sets a temporary hold on an object:
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/storage"
    )
    
    // setTemporaryHold sets TemporaryHold flag of an object to true.
    func setTemporaryHold(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucket, object string) error {
    	// bucket := "bucket-name"
    	// object := "object-name"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    
    	o := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucket).[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)(object)
    
    	// Optional: set a metageneration-match precondition to avoid potential race
    	// conditions and data corruptions. The request to update is aborted if the
    	// object's metageneration does not match your precondition.
    	attrs, err := o.Attrs(ctx)
    	if err != nil {
    		return fmt.Errorf("object.Attrs: %w", err)
    	}
    	o = o.If(storage.[Conditions](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Conditions){MetagenerationMatch: attrs.Metageneration})
    
    	// Update the object to set the object hold.
    	objectAttrsToUpdate := storage.[ObjectAttrsToUpdate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectAttrsToUpdate){
    		TemporaryHold: true,
    	}
    	if _, err := o.Update(ctx, objectAttrsToUpdate); err != nil {
    		return fmt.Errorf("Object(%q).Update: %w", object, err)
    	}
    	fmt.Fprintf(w, "Temporary hold was enabled for %v.\n", object)
    	return nil
    }
    

The following sample releases a temporary hold on an object:
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/storage"
    )
    
    // releaseTemporaryHold releases an object with temporary hold.
    func releaseTemporaryHold(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucket, object string) error {
    	// bucket := "bucket-name"
    	// object := "object-name"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    
    	o := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucket).[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)(object)
    
    	// Optional: set a metageneration-match precondition to avoid potential race
    	// conditions and data corruptions. The request to update is aborted if the
    	// object's metageneration does not match your precondition.
    	attrs, err := o.Attrs(ctx)
    	if err != nil {
    		return fmt.Errorf("object.Attrs: %w", err)
    	}
    	o = o.If(storage.[Conditions](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Conditions){MetagenerationMatch: attrs.Metageneration})
    
    	// Update the object to release the hold.
    	objectAttrsToUpdate := storage.[ObjectAttrsToUpdate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectAttrsToUpdate){
    		TemporaryHold: false,
    	}
    	if _, err := o.Update(ctx, objectAttrsToUpdate); err != nil {
    		return fmt.Errorf("Object(%q).Update: %w", object, err)
    	}
    	fmt.Fprintf(w, "Temporary hold was released for %v.\n", object)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample sets an event-based hold on an object:
    
    
    import com.google.cloud.storage.[Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html);
    import com.google.cloud.storage.[BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class SetEventBasedHold {
      public static void setEventBasedHold(String projectId, String bucketName, String objectName)
          throws [StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The ID of your GCS object
        // String objectName = "your-object-name";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html) blobId = [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html).of(bucketName, objectName);
        [Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html) blob = storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(blobId);
        if (blob == null) {
          System.out.println("The object " + objectName + " was not found in " + bucketName);
          return;
        }
    
        // Optional: set a generation-match precondition to avoid potential race
        // conditions and data corruptions. The request to upload returns a 412 error if
        // the object's generation number does not match your precondition.
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobTargetOption precondition = [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobTargetOption.generationMatch();
    
        blob.[toBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html#com_google_cloud_storage_Blob_toBuilder__)().setEventBasedHold(true).build().update(precondition);
    
        System.out.println("Event-based hold was set for " + objectName);
      }
    }

The following sample releases an event-based hold on an object:
    
    
    import com.google.cloud.storage.[Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html);
    import com.google.cloud.storage.[BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class ReleaseEventBasedHold {
      public static void releaseEventBasedHold(String projectId, String bucketName, String objectName)
          throws [StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The ID of your GCS object
        // String objectName = "your-object-name";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html) blobId = [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html).of(bucketName, objectName);
        [Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html) blob = storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(blobId);
        if (blob == null) {
          System.out.println("The object " + objectName + " was not found in " + bucketName);
          return;
        }
    
        // Optional: set a generation-match precondition to avoid potential race
        // conditions and data corruptions. The request to upload returns a 412 error if
        // the object's generation number does not match your precondition.
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobTargetOption precondition = [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobTargetOption.generationMatch();
    
        blob.[toBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html#com_google_cloud_storage_Blob_toBuilder__)().setEventBasedHold(false).build().update(precondition);
    
        System.out.println("Event-based hold was released for " + objectName);
      }
    }

The following sample sets a temporary hold on an object:
    
    
    import com.google.cloud.storage.[Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html);
    import com.google.cloud.storage.[BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class SetTemporaryHold {
      public static void setTemporaryHold(String projectId, String bucketName, String objectName)
          throws [StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The ID of your GCS object
        // String objectName = "your-object-name";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html) blobId = [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html).of(bucketName, objectName);
        [Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html) blob = storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(blobId);
        if (blob == null) {
          System.out.println("The object " + objectName + " was not found in " + bucketName);
          return;
        }
    
        // Optional: set a generation-match precondition to avoid potential race
        // conditions and data corruptions. The request to upload returns a 412 error if
        // the object's generation number does not match your precondition.
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobTargetOption precondition = [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobTargetOption.generationMatch();
    
        blob.[toBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html#com_google_cloud_storage_Blob_toBuilder__)().setTemporaryHold(true).build().update(precondition);
    
        System.out.println("Temporary hold was set for " + objectName);
      }
    }

The following sample releases a temporary hold on an object:
    
    
    import com.google.cloud.storage.[Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html);
    import com.google.cloud.storage.[BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class ReleaseTemporaryHold {
      public static void releaseTemporaryHold(String projectId, String bucketName, String objectName)
          throws [StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The ID of your GCS object
        // String objectName = "your-object-name";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
    
        [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html) blobId = [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html).of(bucketName, objectName);
        [Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html) blob = storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(blobId);
        if (blob == null) {
          System.out.println("The object " + objectName + " was not found in " + bucketName);
          return;
        }
    
        // Optional: set a generation-match precondition to avoid potential race
        // conditions and data corruptions. The request to upload returns a 412 error if
        // the object's generation number does not match your precondition.
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobTargetOption precondition = [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobTargetOption.generationMatch();
    
        blob.[toBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html#com_google_cloud_storage_Blob_toBuilder__)().setTemporaryHold(false).build().update(precondition);
    
        System.out.println("Temporary hold was released for " + objectName);
      }
    }

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample sets an event-based hold on an object:
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The ID of your GCS bucket
    // const bucketName = 'your-unique-bucket-name';
    
    // The ID of your GCS file
    // const fileName = 'your-file-name';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function setEventBasedHold() {
      // Optional: set a meta-generation-match precondition to avoid potential race
      // conditions and data corruptions. The request to set metadata is aborted if the
      // object's metageneration number does not match your precondition.
      const options = {
        ifMetagenerationMatch: metagenerationMatchPrecondition,
      };
    
      // Set event-based hold
      await storage.bucket(bucketName).file(fileName).setMetadata(
        {
          eventBasedHold: true,
        },
        options
      );
      console.log(`Event-based hold was set for ${fileName}.`);
    }
    
    setEventBasedHold().catch(console.error);

The following sample releases an event-based hold on an object:
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The ID of your GCS bucket
    // const bucketName = 'your-unique-bucket-name';
    
    // The ID of your GCS file
    // const fileName = 'your-file-name';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function releaseEventBasedHold() {
      // Optional: set a meta-generation-match precondition to avoid potential race
      // conditions and data corruptions. The request to set metadata is aborted if the
      // object's metageneration number does not match your precondition.
      const options = {
        ifMetagenerationMatch: metagenerationMatchPrecondition,
      };
    
      await storage.bucket(bucketName).file(fileName).setMetadata(
        {
          eventBasedHold: false,
        },
        options
      );
      console.log(`Event-based hold was released for ${fileName}.`);
    }
    
    releaseEventBasedHold().catch(console.error);

The following sample sets a temporary hold on an object:
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The ID of your GCS bucket
    // const bucketName = 'your-unique-bucket-name';
    
    // The ID of your GCS file
    // const fileName = 'your-file-name';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function setTemporaryHold() {
      // Optional: set a meta-generation-match precondition to avoid potential race
      // conditions and data corruptions. The request to set metadata is aborted if the
      // object's metageneration number does not match your precondition.
      const options = {
        ifMetagenerationMatch: metagenerationMatchPrecondition,
      };
    
      await storage.bucket(bucketName).file(fileName).setMetadata(
        {
          temporaryHold: true,
        },
        options
      );
      console.log(`Temporary hold was set for ${fileName}.`);
    }
    
    setTemporaryHold().catch(console.error);

The following sample releases a temporary hold on an object:
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The ID of your GCS bucket
    // const bucketName = 'your-unique-bucket-name';
    
    // The ID of your GCS file
    // const fileName = 'your-file-name';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function releaseTemporaryHold() {
      // Optional: set a meta-generation-match precondition to avoid potential race
      // conditions and data corruptions. The request to set metadata is aborted if the
      // object's metageneration number does not match your precondition.
      const options = {
        ifMetagenerationMatch: metagenerationMatchPrecondition,
      };
    
      await storage.bucket(bucketName).file(fileName).setMetadata(
        {
          temporaryHold: false,
        },
        options
      );
      console.log(`Temporary hold was released for ${fileName}.`);
    }
    
    releaseTemporaryHold().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample sets an event-based hold on an object:
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Sets an event-based hold for an object.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $objectName The name of your Cloud Storage object.
     *        (e.g. 'my-object')
     */
    function set_event_based_hold(string $bucketName, string $objectName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
        $object = $bucket->object($objectName);
        $object->update(['eventBasedHold' => true]);
        printf('Event-based hold was set for %s' . PHP_EOL, $objectName);
    }

The following sample releases an event-based hold on an object:
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Releases an event-based hold for an object.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $objectName The name of your Cloud Storage object.
     *        (e.g. 'my-object')
     */
    function release_event_based_hold(string $bucketName, string $objectName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
        $object = $bucket->object($objectName);
        $object->update(['eventBasedHold' => false]);
        printf('Event-based hold was released for %s' . PHP_EOL, $objectName);
    }

The following sample sets a temporary hold on an object:
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Sets a temporary hold for an object.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $objectName The name of your Cloud Storage object.
     *        (e.g. 'my-object')
     */
    function set_temporary_hold(string $bucketName, string $objectName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
        $object = $bucket->object($objectName);
        $object->update(['temporaryHold' => true]);
        printf('Temporary hold was set for %s' . PHP_EOL, $objectName);
    }

The following sample releases a temporary hold on an object:
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Releases a temporary hold for an object.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $objectName The name of your Cloud Storage object.
     *        (e.g. 'my-object')
     */
    function release_temporary_hold(string $bucketName, string $objectName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
        $object = $bucket->object($objectName);
        $object->update(['temporaryHold' => false]);
        printf('Temporary hold was released for %s' . PHP_EOL, $objectName);
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample sets an event-based hold on an object:
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def set_event_based_hold(bucket_name, blob_name):
        """Sets a event based hold on a given blob"""
        # bucket_name = "my-bucket"
        # blob_name = "my-blob"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
        blob = bucket.blob(blob_name)
        metageneration_match_precondition = None
    
        # Optional: set a metageneration-match precondition to avoid potential race
        # conditions and data corruptions. The request to patch is aborted if the
        # object's metageneration does not match your precondition.
        blob.reload()  # Fetch blob metadata to use in metageneration_match_precondition.
        metageneration_match_precondition = blob.metageneration
    
        blob.[event_based_hold](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_event_based_hold) = True
        blob.patch(if_metageneration_match=metageneration_match_precondition)
    
        print(f"Event based hold was set for {blob_name}")
    
    

The following sample releases an event-based hold on an object:
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def release_event_based_hold(bucket_name, blob_name):
        """Releases the event based hold on a given blob"""
    
        # bucket_name = "my-bucket"
        # blob_name = "my-blob"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
        blob = bucket.blob(blob_name)
        metageneration_match_precondition = None
    
        # Optional: set a metageneration-match precondition to avoid potential race
        # conditions and data corruptions. The request to patch is aborted if the
        # object's metageneration does not match your precondition.
        blob.reload()  # Fetch blob metadata to use in metageneration_match_precondition.
        metageneration_match_precondition = blob.metageneration
    
        blob.[event_based_hold](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_event_based_hold) = False
        blob.patch(if_metageneration_match=metageneration_match_precondition)
    
        print(f"Event based hold was released for {blob_name}")
    
    

The following sample sets a temporary hold on an object:
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def set_temporary_hold(bucket_name, blob_name):
        """Sets a temporary hold on a given blob"""
        # bucket_name = "my-bucket"
        # blob_name = "my-blob"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
        blob = bucket.blob(blob_name)
        metageneration_match_precondition = None
    
        # Optional: set a metageneration-match precondition to avoid potential race
        # conditions and data corruptions. The request to patch is aborted if the
        # object's metageneration does not match your precondition.
        blob.reload()  # Fetch blob metadata to use in metageneration_match_precondition.
        metageneration_match_precondition = blob.metageneration
    
        blob.[temporary_hold](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_temporary_hold) = True
        blob.patch(if_metageneration_match=metageneration_match_precondition)
    
        print("Temporary hold was set for #{blob_name}")
    
    

The following sample releases a temporary hold on an object:
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def release_temporary_hold(bucket_name, blob_name):
        """Releases the temporary hold on a given blob"""
    
        # bucket_name = "my-bucket"
        # blob_name = "my-blob"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
        blob = bucket.blob(blob_name)
        metageneration_match_precondition = None
    
        # Optional: set a metageneration-match precondition to avoid potential race
        # conditions and data corruptions. The request to patch is aborted if the
        # object's metageneration does not match your precondition.
        blob.reload()  # Fetch blob metadata to use in metageneration_match_precondition.
        metageneration_match_precondition = blob.metageneration
    
        blob.[temporary_hold](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_temporary_hold) = False
        blob.patch(if_metageneration_match=metageneration_match_precondition)
    
        print("Temporary hold was release for #{blob_name}")
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample sets an event-based hold on an object:
    
    
    def set_event_based_hold bucket_name:, file_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      # The ID of your GCS object
      # file_name = "your-file-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket  = storage.bucket bucket_name, skip_lookup: true
      file    = bucket.[file](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) file_name
    
      file.[set_event_based_hold!](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-File.html)
    
      puts "Event-based hold was set for #{file_name}."
    end

The following sample releases an event-based hold on an object:
    
    
    def release_event_based_hold bucket_name:, file_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      # The ID of your GCS object
      # file_name = "your-file-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket  = storage.bucket bucket_name, skip_lookup: true
      file    = bucket.[file](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) file_name
    
      file.[release_event_based_hold!](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-File.html)
    
      puts "Event-based hold was released for #{file_name}."
    end

The following sample sets a temporary hold on an object:
    
    
    def set_temporary_hold bucket_name:, file_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      # The ID of your GCS object
      # file_name = "your-file-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket  = storage.bucket bucket_name, skip_lookup: true
      file    = bucket.[file](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) file_name
    
      file.[set_temporary_hold!](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-File.html)
    
      puts "Temporary hold was set for #{file_name}."
    end

The following sample releases a temporary hold on an object:
    
    
    def release_temporary_hold bucket_name:, file_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      # The ID of your GCS object
      # file_name = "your-file-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket  = storage.bucket bucket_name, skip_lookup: true
      file    = bucket.[file](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) file_name
    
      file.[release_temporary_hold!](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-File.html)
    
      puts "Temporary hold was released for #{file_name}."
    end

### Rust

The following sample sets an event-based hold on an object:
    
    
    use google_cloud_storage::client::StorageControl;
    use google_cloud_wkt::FieldMask;
    
    pub async fn sample(client: &StorageControl, bucket_id: &str) -> anyhow::Result<()> {
        const NAME: &str = "object-to-update";
        let object = client
            .get_object()
            .set_bucket(format!("projects/_/buckets/{bucket_id}"))
            .set_object(NAME)
            .send()
            .await?;
    
        let metageneration = object.metageneration;
        let updated = client
            .update_object()
            .set_if_metageneration_match(metageneration)
            .set_object(object.set_event_based_hold(true))
            .set_update_mask(FieldMask::default().set_paths(["event_based_hold"]))
            .send()
            .await?;
        println!(
            "successfully set event_based hold on object {NAME} in bucket {bucket_id}: {updated:?}"
        );
        Ok(())
    }

The following sample releases an event-based hold on an object:
    
    
    use google_cloud_storage::client::StorageControl;
    use google_cloud_wkt::FieldMask;
    
    pub async fn sample(client: &StorageControl, bucket_id: &str) -> anyhow::Result<()> {
        const NAME: &str = "object-to-update";
        let object = client
            .get_object()
            .set_bucket(format!("projects/_/buckets/{bucket_id}"))
            .set_object(NAME)
            .send()
            .await?;
    
        let metageneration = object.metageneration;
        let updated = client
            .update_object()
            .set_if_metageneration_match(metageneration)
            .set_object(object.set_event_based_hold(false))
            .set_update_mask(FieldMask::default().set_paths(["event_based_hold"]))
            .send()
            .await?;
        println!(
            "successfully released event_based hold on object {NAME} in bucket {bucket_id}: {updated:?}"
        );
        Ok(())
    }

The following sample sets a temporary hold on an object:
    
    
    use google_cloud_storage::client::StorageControl;
    use google_cloud_wkt::FieldMask;
    
    pub async fn sample(client: &StorageControl, bucket_id: &str) -> anyhow::Result<()> {
        const NAME: &str = "object-to-update";
        let object = client
            .get_object()
            .set_bucket(format!("projects/_/buckets/{bucket_id}"))
            .set_object(NAME)
            .send()
            .await?;
    
        let metageneration = object.metageneration;
        let updated = client
            .update_object()
            .set_if_metageneration_match(metageneration)
            .set_object(object.set_temporary_hold(true))
            .set_update_mask(FieldMask::default().set_paths(["temporary_hold"]))
            .send()
            .await?;
        println!("successfully set temporary hold on object {NAME} in bucket {bucket_id}: {updated:?}");
        Ok(())
    }

The following sample releases a temporary hold on an object:
    
    
    use google_cloud_storage::client::StorageControl;
    use google_cloud_wkt::FieldMask;
    
    pub async fn sample(client: &StorageControl, bucket_id: &str) -> anyhow::Result<()> {
        const NAME: &str = "object-to-update";
        let object = client
            .get_object()
            .set_bucket(format!("projects/_/buckets/{bucket_id}"))
            .set_object(NAME)
            .send()
            .await?;
    
        let metageneration = object.metageneration;
        let updated = client
            .update_object()
            .set_if_metageneration_match(metageneration)
            .set_object(object.set_temporary_hold(false))
            .set_update_mask(FieldMask::default().set_paths(["temporary_hold"]))
            .send()
            .await?;
        println!(
            "successfully released temporary hold on object {NAME} in bucket {bucket_id}: {updated:?}"
        );
        Ok(())
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the following information:
         
         {
           "HOLD_TYPE": STATE
         }

Where:

     * `HOLD_TYPE` is the type of hold you want to set or release on your object. For example, `temporaryHold` or `eventBasedHold`. See [Object holds](https://docs.cloud.google.com/storage/docs/object-holds) for more information about hold types.
     * `STATE` is either `true` to place the hold or `false` to release the hold.
  3. Use [`cURL`](http://curl.haxx.se/) to call the JSON API with a [`PATCH` Object](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/patch) request:
         
         curl -X PATCH --data-binary @JSON_FILE_NAME \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/o/OBJECT_NAME"

Where:

     * `JSON_FILE_NAME` is the path for the file that you created in Step 2.
     * `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.
     * `OBJECT_NAME` is the URL-encoded name of the relevant object. For example, `pets/dog.png`, URL-encoded as `pets%2Fdog.png`.



### XML API

The XML API cannot be used to work with object holds. Use one of the other Cloud Storage tools, such as the gcloud CLI, instead.

### Get the hold status for an object

**Note:** You cannot view object holds using the XML API. Use one of the other Cloud Storage tools, such as the gcloud CLI, instead.

To view what, if any, holds exist on an object, follow the general instructions for [viewing object metadata](https://docs.cloud.google.com/storage/docs/viewing-editing-metadata#view).

## Place or release object holds in bulk

To place or release holds on millions or billions of objects with a single job, use [Storage batch operations](https://docs.cloud.google.com/storage/docs/batch-operations/overview). To create a job, specify the objects on which you want to place or release holds, either by providing a list of objects in a manifest file or by using object prefixes. After you have specified the object list, [create a batch operation job to update object holds](https://docs.cloud.google.com/storage/docs/batch-operations/create-manage-batch-operation-jobs).

## What's next

  * Learn more about [object holds](https://docs.cloud.google.com/storage/docs/object-holds), including the different types of holds that an object can have.
  * Learn how to use [retention policies](https://docs.cloud.google.com/storage/docs/using-bucket-lock).
  * Learn how to use [request preconditions](https://docs.cloud.google.com/storage/docs/request-preconditions) to prevent race conditions.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
