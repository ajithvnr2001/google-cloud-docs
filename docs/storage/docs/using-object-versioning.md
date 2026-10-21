---
url: https://docs.cloud.google.com/storage/docs/using-object-versioning/
title: Use Object Versioning \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:08.624323+00:00
---

# Use Object Versioning  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/using-object-versioning/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Use Object Versioning Stay organized with collections  Save and categorize content based on your preferences. 

[Overview](https://docs.cloud.google.com/storage/docs/object-versioning) [Usage](https://docs.cloud.google.com/storage/docs/using-versioned-objects)

This page describes how to enable, disable, and check the status of Object Versioning on a bucket. See [Using versioned objects](https://docs.cloud.google.com/storage/docs/using-versioned-objects) to learn how to list, restore, and delete the objects that are retained by Object Versioning.

**Important:** There is no default limit on the number of object versions you can have. Each noncurrent version of an object is charged at the same rate as the live version of the object. If you enable versioning, consider using [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle), which can remove the oldest versions of an object as newer versions become noncurrent.

## Required roles

To get the permissions that you need to set and manage Object Versioning on a bucket, ask your administrator to grant you the Storage Admin (`roles/storage.admin`) IAM role on the bucket or the project that contains the bucket. This [predefined role](https://docs.cloud.google.com/iam/docs/roles-permissions) contains the permissions required to set and manage Object Versioning for a bucket. To see the exact permissions that are required, expand the **Required permissions** section:

#### Required permissions

  * `storage.buckets.get`
  * `storage.buckets.update`
  * `storage.buckets.list`
    * This permission is only required if you plan on using the Google Cloud console to perform the instructions on this page.



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

For information about granting roles on buckets, see [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions). For information about granting roles on projects, see [Manage access to projects](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Set Object Versioning on a bucket

You enable or disable Object Versioning by setting the feature on a bucket. After Object Versioning is enabled, each time a live object version is replaced or deleted, that version becomes a [_noncurrent_ version](https://docs.cloud.google.com/storage/docs/object-versioning).

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket for which you want to enable or disable Object Versioning.

  3. Select the **Protection** tab near the top of the page.

The current status of Object versioning is found in the **Object versioning** section.

  4. In the **Object versioning** section, click the current status to make changes to it.

The **Object versioning** dialog appears.

     1. If you're enabling Object Versioning and you want to minimize storage costs, select the **Add recommended lifecycle rules to manage version costs** checkbox.
  5. Click **Confirm**.




### Command line

Use the [`gcloud storage buckets update`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/update) command with the appropriate flag:
    
    
    gcloud storage buckets update gs://BUCKET_NAME FLAG

Where:

  * `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.

  * `FLAG` is either `--versioning` to enable Object Versioning or `--no-versioning` to disable it.




If successful, the response looks similar to the following example:
    
    
    Updating gs://my-bucket/...
      Completed 1  

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample enables Object Versioning on a bucket:
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name) {
      StatusOr<gcs::BucketMetadata> original =
          client.GetBucketMetadata(bucket_name);
      if (!original) throw std::move(original).status();
    
      StatusOr<gcs::BucketMetadata> patched = client.PatchBucket(
          bucket_name,
          gcs::BucketMetadataPatchBuilder().SetVersioning(
              gcs::BucketVersioning{true}),
          gcs::IfMetagenerationMatch(original->metageneration()));
      if (!patched) throw std::move(patched).status();
    
      if (patched->versioning().has_value()) {
        std::cout << "Object versioning for bucket " << bucket_name << " is "
                  << (patched->versioning()->enabled ? "enabled" : "disabled")
                  << "\n";
      } else {
        std::cout << "Object versioning for bucket " << bucket_name
                  << " is disabled.\n";
      }
    }

The following sample disables Object Versioning on a bucket:
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name) {
      StatusOr<gcs::BucketMetadata> original =
          client.GetBucketMetadata(bucket_name);
      if (!original) throw std::move(original).status();
    
      StatusOr<gcs::BucketMetadata> patched = client.PatchBucket(
          bucket_name,
          gcs::BucketMetadataPatchBuilder().SetVersioning(
              gcs::BucketVersioning{false}),
          gcs::IfMetagenerationMatch(original->metageneration()));
      if (!patched) throw std::move(patched).status();
    
      auto versioning =
          patched->versioning().value_or(gcs::BucketVersioning{false});
      std::cout << "Object versioning for bucket " << bucket_name << " is "
                << (versioning.enabled ? "enabled" : "disabled") << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample enables Object Versioning on a bucket:
    
    
    using Google.Apis.Storage.v1.Data;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class BucketEnableVersioningSample
    {
    	public Bucket BucketEnableVersioning(string bucketName = "your-bucket-name")
    	{
    		var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
    		var bucket = storage.GetBucket(bucketName);
    
    		if (bucket.Versioning == null)
    		{
    			bucket.Versioning = new Bucket.VersioningData();
    		}
    		bucket.Versioning.Enabled = true;
    
    		bucket = storage.UpdateBucket(bucket);
    		Console.WriteLine($"Versioning is now enabled for bucket {bucketName}.");
    		return bucket;
    	}
    }

The following sample disables Object Versioning on a bucket:
    
    
    using Google.Apis.Storage.v1.Data;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class BucketDisableVersioningSample
    {
    	public Bucket BucketDisableVersioning(string bucketName = "your-bucket-name")
    	{
    		var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
    		var bucket = storage.GetBucket(bucketName);
    
    		if (bucket.Versioning?.Enabled != true)
    		{
    			Console.WriteLine($"Versioning already disabled for bucket {bucketName}.");
    		}
    		else
    		{
            	    bucket.Versioning.Enabled = false;
    
    		    bucket = storage.UpdateBucket(bucket);
                        Console.WriteLine($"Versioning is now disabled for bucket {bucketName}.");
                    }
    		return bucket;
    	}
    }

### Go

For more information, see the [Cloud Storage Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storage). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample enables Object Versioning on a bucket:
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/storage"
    )
    
    // enableVersioning enables object versioning on a bucket.
    func enableVersioning(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucketName string) error {
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
    		VersioningEnabled: true,
    	}
    	if _, err := bucket.Update(ctx, bucketAttrsToUpdate); err != nil {
    		return fmt.Errorf("Bucket(%q).Update: %w", bucketName, err)
    	}
    	fmt.Fprintf(w, "Versioning was enabled for %v\n", bucketName)
    	return nil
    }
    

The following sample disables Object Versioning on a bucket:
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/storage"
    )
    
    // disableVersioning disables object versioning on a bucket.
    func disableVersioning(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucketName string) error {
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
    		VersioningEnabled: false,
    	}
    	if _, err := bucket.Update(ctx, bucketAttrsToUpdate); err != nil {
    		return fmt.Errorf("Bucket(%q).Update: %w", bucketName, err)
    	}
    	fmt.Fprintf(w, "Versioning was disabled for %v\n", bucketName)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample enables Object Versioning on a bucket:
    
    
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class EnableBucketVersioning {
      public static void enableBucketVersioning(String projectId, String bucketName) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket = storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName);
        bucket.[toBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html#com_google_cloud_storage_Bucket_toBuilder__)().setVersioningEnabled(true).build().update();
    
        System.out.println("Versioning is now enabled for bucket " + bucketName);
      }
    }

The following sample disables Object Versioning on a bucket:
    
    
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class DisableBucketVersioning {
      public static void disableBucketVersioning(String projectId, String bucketName) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket = storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName);
        bucket.[toBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html#com_google_cloud_storage_Bucket_toBuilder__)().setVersioningEnabled(false).build().update();
    
        System.out.println("Versioning is now disabled for bucket " + bucketName);
      }
    }

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample enables Object Versioning on a bucket:
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The ID of your GCS bucket
    // const bucketName = 'your-unique-bucket-name';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function enableBucketVersioning() {
      await storage.bucket(bucketName).setMetadata({
        versioning: {
          enabled: true,
        },
      });
    
      console.log(`Versioning is enabled for bucket ${bucketName}`);
    }
    
    enableBucketVersioning().catch(console.error);

The following sample disables Object Versioning on a bucket:
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The ID of your GCS bucket
    // const bucketName = 'your-unique-bucket-name';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function disableBucketVersioning() {
      await storage.bucket(bucketName).setMetadata({
        versioning: {
          enabled: false,
        },
      });
    
      console.log(`Versioning is disabled for bucket ${bucketName}`);
    }
    
    disableBucketVersioning().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample enables Object Versioning on a bucket:
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Enable versioning on the specified bucket.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     */
    function enable_versioning(string $bucketName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
        $bucket->update([
            'versioning' => [
                'enabled' => true,
            ]
        ]);
    
        printf('Versioning is now enabled for bucket %s', $bucketName);
    }

The following sample disables Object Versioning on a bucket:
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Disable versioning of the given bucket.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     */
    function disable_versioning(string $bucketName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
        $bucket->update([
            'versioning' => [
                'enabled' => false,
            ]
        ]);
    
        printf('Versioning is now disabled for bucket %s', $bucketName);
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample enables Object Versioning on a bucket:
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def enable_versioning(bucket_name):
        """Enable versioning for this bucket."""
        # bucket_name = "my-bucket"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
        bucket = storage_client.[get_bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_get_bucket)(bucket_name)
        bucket.[versioning_enabled](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_versioning_enabled) = True
        bucket.patch()
    
        print(f"Versioning was enabled for bucket {bucket.name}")
        return bucket
    
    

The following sample disables Object Versioning on a bucket:
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def disable_versioning(bucket_name):
        """Disable versioning for this bucket."""
        # bucket_name = "my-bucket"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
        bucket = storage_client.[get_bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_get_bucket)(bucket_name)
        bucket.[versioning_enabled](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_versioning_enabled) = False
        bucket.patch()
    
        print(f"Versioning was disabled for bucket {bucket}")
        return bucket
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample enables Object Versioning on a bucket:
    
    
    def enable_versioning bucket_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket = storage.bucket bucket_name
    
      bucket.versioning = true
    
      puts "Versioning was enabled for bucket #{bucket_name}"
    end

The following sample disables Object Versioning on a bucket:
    
    
    def disable_versioning bucket_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket = storage.bucket bucket_name
    
      bucket.versioning = false
    
      puts "Versioning was disabled for bucket #{bucket_name}"
    end

### Rust

The following sample enables Object Versioning on a bucket:
    
    
    use google_cloud_storage::client::StorageControl;
    use google_cloud_storage::model::bucket::Versioning;
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
            .set_bucket(bucket.set_versioning(Versioning::new().set_enabled(true)))
            .set_if_metageneration_match(metageneration)
            .set_update_mask(FieldMask::default().set_paths(["versioning"]))
            .send()
            .await?;
        println!("Versioning enabled for bucket {bucket_id}: {bucket:?}");
        Ok(())
    }

The following sample disables Object Versioning on a bucket:
    
    
    use google_cloud_storage::client::StorageControl;
    use google_cloud_storage::model::bucket::Versioning;
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
            .set_bucket(bucket.set_versioning(Versioning::new().set_enabled(false)))
            .set_if_metageneration_match(metageneration)
            .set_update_mask(FieldMask::default().set_paths(["versioning"]))
            .send()
            .await?;
        println!("Versioning disabled for bucket {bucket_id}: {bucket:?}");
        Ok(())
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the following information:
         
         {
           "versioning": {
             "enabled": STATE
           }
         }

Where STATE is either `true` or `false`.

  3. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`PATCH` Bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/patch) request:
         
         curl -X PATCH --data-binary @JSON_FILE_NAME \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME?fields=versioning"

Where:

     * `JSON_FILE_NAME` is the path for the JSON file that you created in Step 2.
     * `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.



### XML API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create an XML file that contains the following information:
         
         <VersioningConfiguration>
           <Status>STATE</Status>
         </VersioningConfiguration>

Where STATE is either `Enabled` or `Suspended`.

  3. Use [`cURL`](http://curl.haxx.se/) to call the [XML API](https://docs.cloud.google.com/storage/docs/xml-api/overview), with a [`PUT` Bucket](https://docs.cloud.google.com/storage/docs/xml-api/put-bucket-metadata) request and `versioning` query string parameter:
         
         curl -X PUT --data-binary @XML_FILE_NAME \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storage.googleapis.com/BUCKET_NAME?versioning"

Where:

     * `XML_FILE_NAME` is the path for the XML file that you created in Step 2.
     * `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.



## Check whether Object Versioning is enabled

To check whether Object Versioning is enabled on a bucket:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, the Object Versioning status of each bucket is found in the **Protection** column.




If enabled, the text **Object versioning** appears.

### Command line

Use the [`gcloud storage buckets describe`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/describe) command with the `--format` flag:
    
    
    gcloud storage buckets describe gs://BUCKET_NAME --format="default(versioning_enabled)"

Where `BUCKET_NAME` is the name of the bucket whose status you want to view. For example, `my-bucket`.

If successful and Object Versioning is enabled, the response looks similar to the following example:
    
    
    versioning:
      enabled: true

If successful and Object Versioning is not enabled, the response looks similar to the following example:
    
    
    null

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`GET` Bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/get) request:
         
         curl -X GET \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME?fields=versioning"

Where `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.




If successful and Object Versioning is enabled, the response looks similar to the following example:
    
    
    {
      "versioning": {
        "enabled": true
      }
    }

If successful and Object Versioning is not enabled, the response looks similar to the following example:
    
    
    {}

### XML API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [XML API](https://docs.cloud.google.com/storage/docs/xml-api/overview), with a [`GET` Bucket](https://docs.cloud.google.com/storage/docs/xml-api/get-bucket-metadata) request and `versioning` query string parameter:
         
         curl -X GET \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storage.googleapis.com/BUCKET_NAME?versioning"

Where `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.




If successful and Object Versioning is enabled, the response looks similar to the following example:
    
    
    <VersioningConfiguration>
      <Status>Enabled</Status>
    </VersioningConfiguration>

If successful and Object Versioning is not enabled, the response looks similar to the following example:
    
    
    <VersioningConfiguration/>

## What's next

  * Learn more about [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning).
  * Learn how to [work with noncurrent objects](https://docs.cloud.google.com/storage/docs/using-versioned-objects).
  * Learn how to [use Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/managing-lifecycles) to automatically manage object versions.
  * Learn how to use [request preconditions](https://docs.cloud.google.com/storage/docs/request-preconditions) to prevent race conditions.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
