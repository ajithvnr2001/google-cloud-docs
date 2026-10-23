---
url: https://docs.cloud.google.com/storage/docs/managing-turbo-replication/
title: Managing turbo replication \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:40:56.642779+00:00
---

# Managing turbo replication  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/managing-turbo-replication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Managing turbo replication Stay organized with collections  Save and categorize content based on your preferences. 

Turbo replication lets you replicate data across regions faster in your dual-region buckets. This accelerated replication can reduce your exposure to data loss and helps support uninterrupted service after a regional outage. You can enable or disable turbo replication on a dual-region bucket.

For background information about data availability and durability in Cloud Storage, see [Data availability and durability](https://docs.cloud.google.com/storage/docs/availability-durability) and [Turbo replication](https://docs.cloud.google.com/storage/docs/availability-durability#turbo-replication).

## Required roles

In order to get the required permissions for using turbo replication, ask your administrator to grant you the Storage Admin (`roles/storage.admin`) IAM role on the bucket.

This predefined role contains the permissions required to use turbo replication. To see the exact permissions that are required, expand the **Required permissions** section:

#### Required permissions

  * `storage.buckets.get`
  * `storage.buckets.update`
  * `storage.buckets.list`
    * This permission is only required if you plan on using the Google Cloud console to perform the instructions on this page.



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/storage/docs/access-control/iam-roles).

For instructions on granting roles on buckets, see [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).

## Set turbo replication

To enable or disable turbo replication on an existing bucket, complete the following instructions:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the bucket list, click the name of the desired bucket.

  3. Click the **Configuration** tab.

  4. In the **Replication** row, click edit **Edit**.

The window that appears indicates whether you are about to **Enable turbo replication** or **Disable turbo replication**.

  5. Click **Save** to confirm the new setting.




### Command line

Use the [`gcloud storage buckets update`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/update) command with the `--rpo` flag:
    
    
    gcloud storage buckets update gs://BUCKET_NAME --rpo=STATE

Where:

  * `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.

  * `STATE` is `ASYNC_TURBO` for enabling Turbo Replication or `DEFAULT` for disabling Turbo Replication.




If successful, the response looks like:
    
    
    Updating gs://my-bucket/...
      Completed 1  

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample enables turbo replication on a bucket:
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name) {
      auto updated = client.PatchBucket(
          bucket_name,
          gcs::BucketMetadataPatchBuilder().SetRpo(gcs::RpoAsyncTurbo()));
      if (!updated) throw std::move(updated).status();
    
      std::cout << "RPO is set to 'ASYNC_TURBO' for " << updated->name() << "\n";
    }

The following sample enables default replication on a bucket:
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name) {
      auto updated = client.PatchBucket(
          bucket_name,
          gcs::BucketMetadataPatchBuilder().SetRpo(gcs::RpoDefault()));
      if (!updated) throw std::move(updated).status();
    
      std::cout << "RPO is set to 'default' for " << updated->name() << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample enables turbo replication on a bucket:
    
    
    using System;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    
    public class SetRpoAsyncTurboSample
    {
        public void SetRpoAsyncTurbo(string bucketName = "your-unique-bucket-name")
        {
            // Enabling turbo replication requires a bucket with dual-region configuration
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var bucket = storage.GetBucket(bucketName);
            bucket.Rpo = "ASYNC_TURBO";
            storage.UpdateBucket(bucket);
    
            Console.WriteLine($"Turbo replication enabled for bucket {bucketName}");
        }
    }
    

The following sample enables default replication on a bucket:
    
    
    using System;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    
    public class SetRpoDefaultSample
    {
        public void SetRpoDefault(string bucketName = "your-unique-bucket-name")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var bucket = storage.GetBucket(bucketName);
            bucket.Rpo = "DEFAULT";
            storage.UpdateBucket(bucket);
    
            Console.WriteLine($"Turbo replication disabled for bucket {bucketName}");
        }
    }
    

### Go

For more information, see the [Cloud Storage Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storage). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample enables turbo replication on a bucket:
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/storage"
    )
    
    // setRPOAsyncTurbo enables turbo replication for the bucket by setting RPO to
    // "ASYNC_TURBO". The bucket must be dual-region to use this feature.
    func setRPOAsyncTurbo(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucketName string) error {
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
    	setRPO := storage.[BucketAttrsToUpdate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketAttrsToUpdate){
    		RPO: storage.[RPOAsyncTurbo](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_RPOUnknown_RPODefault_RPOAsyncTurbo),
    	}
    	if _, err := bucket.Update(ctx, setRPO); err != nil {
    		return fmt.Errorf("Bucket(%q).Update: %w", bucketName, err)
    	}
    	fmt.Fprintf(w, "Turbo replication enabled for %v", bucketName)
    	return nil
    }
    

The following sample enables default replication on a bucket:
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/storage"
    )
    
    // setRPODefault disables turbo replication for the bucket by setting RPO to
    // "DEFAULT".
    func setRPODefault(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucketName string) error {
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
    	setRPO := storage.[BucketAttrsToUpdate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketAttrsToUpdate){
    		RPO: storage.[RPODefault](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_RPOUnknown_RPODefault_RPOAsyncTurbo),
    	}
    	if _, err := bucket.Update(ctx, setRPO); err != nil {
    		return fmt.Errorf("Bucket(%q).Update: %w", bucketName, err)
    	}
    	fmt.Fprintf(w, "Turbo replication disabled for %v", bucketName)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample enables turbo replication on a bucket:
    
    
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[Rpo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Rpo.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class SetAsyncTurboRpo {
      public static void setAsyncTurboRpo(String projectId, String bucketName) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket = storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName);
    
        bucket.[toBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html#com_google_cloud_storage_Bucket_toBuilder__)().setRpo([Rpo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Rpo.html).ASYNC_TURBO).build().update();
    
        System.out.println("Turbo replication was enabled for " + bucketName);
      }
    }

The following sample enables default replication on a bucket:
    
    
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[Rpo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Rpo.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class SetDefaultRpo {
      public static void setDefaultRpo(String projectId, String bucketName) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket = storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName);
    
        bucket.[toBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html#com_google_cloud_storage_Bucket_toBuilder__)().setRpo([Rpo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Rpo.html).DEFAULT).build().update();
    
        System.out.println("Replication was set to default for " + bucketName);
      }
    }

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample enables turbo replication on a bucket:
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The name of your GCS bucket in a dual-region
    // const bucketName = 'Name of a bucket, e.g. my-bucket';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    // Enable turbo replication for the bucket by setting rpo to ASYNC_TURBO.
    // The bucket must be a dual-region bucket.
    async function setRPOAsyncTurbo() {
      await storage.bucket(bucketName).setMetadata({
        rpo: 'ASYNC_TURBO',
      });
    
      console.log(`Turbo replication enabled for ${bucketName}.`);
    }
    
    setRPOAsyncTurbo();

The following sample enables default replication on a bucket:
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The name of your GCS bucket in a dual-region
    // const bucketName = 'Name of a bucket, e.g. my-bucket';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    // Disable turbo replication for the bucket by setting RPO to default.
    // The bucket must be a dual-region bucket.
    async function setRPODefault() {
      await storage.bucket(bucketName).setMetadata({
        rpo: 'DEFAULT',
      });
    
      console.log(`Turbo replication disabled for ${bucketName}.`);
    }
    
    setRPODefault();

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample enables turbo replication on a bucket:
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Set the bucket's Turbo Replication(rpo) setting to `ASYNC_TURBO`.
     * The bucket must be a dual-region bucket.
     *
     * @param string $bucketName the name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     */
    function set_rpo_async_turbo(string $bucketName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
        $rpo = 'ASYNC_TURBO';
    
        $bucket->update([
            'rpo' => $rpo
        ]);
    
        printf(
            'The replication behavior or recovery point objective (RPO) has been set to ASYNC_TURBO for %s.' . PHP_EOL,
            $bucketName
        );
    }

The following sample enables default replication on a bucket:
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Set the bucket's replication behavior or recovery point objective (RPO) to `DEFAULT`.
     *
     * @param string $bucketName the name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     */
    function set_rpo_default(string $bucketName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
        $rpo = 'DEFAULT';
    
        // Updating the rpo value of a multi-region bucket to DEFAULT has no effect
        // and updating the rpo value of a regional bucket will throw an exception.
        $bucket->update([
            'rpo' => $rpo
        ]);
    
        printf(
            'The replication behavior or recovery point objective (RPO) has been set to DEFAULT for %s.' . PHP_EOL,
            $bucketName
        );
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample enables turbo replication on a bucket:
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    from google.cloud.storage.constants import RPO_ASYNC_TURBO
    
    
    def set_rpo_async_turbo(bucket_name):
        """Sets the RPO to ASYNC_TURBO, enabling the turbo replication feature"""
        # The ID of your GCS bucket
        # bucket_name = "my-bucket"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
    
        bucket.[rpo](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_rpo) = RPO_ASYNC_TURBO
        bucket.patch()
    
        print(f"RPO is set to ASYNC_TURBO for {bucket.name}.")
    
    

The following sample enables default replication on a bucket:
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    from google.cloud.storage.constants import RPO_DEFAULT
    
    
    def set_rpo_default(bucket_name):
        """Sets the RPO to DEFAULT, disabling the turbo replication feature"""
        # The ID of your GCS bucket
        # bucket_name = "my-bucket"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
    
        bucket.[rpo](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_rpo) = RPO_DEFAULT
        bucket.patch()
    
        print(f"RPO is set to DEFAULT for {bucket.name}.")
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample enables turbo replication on a bucket:
    
    
    def set_rpo_async_turbo bucket_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket  = storage.bucket bucket_name,
                               location: "ASIA"
    
      bucket.[rpo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) = :ASYNC_TURBO
    
      puts "Turbo replication is enabled for #{bucket_name}."
    end

The following sample enables default replication on a bucket:
    
    
    def set_rpo_default bucket_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket  = storage.bucket bucket_name
    
      bucket.[rpo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) = :DEFAULT
    
      puts "The replication behavior or recovery point objective (RPO) for #{bucket_name} is set to default."
    end

### Rust

The following sample enables turbo replication on a bucket:
    
    
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
            .set_bucket(bucket.set_rpo("ASYNC_TURBO"))
            .set_if_metageneration_match(metageneration)
            .set_update_mask(FieldMask::default().set_paths(["rpo"]))
            .send()
            .await?;
        println!("successfully updated bucket RPO to ASYNC_TURBO: {bucket:?}");
        Ok(())
    }

The following sample enables default replication on a bucket:
    
    
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
            .set_bucket(bucket.set_rpo("DEFAULT"))
            .set_if_metageneration_match(metageneration)
            .set_update_mask(FieldMask::default().set_paths(["rpo"]))
            .send()
            .await?;
        println!("successfully updated bucket RPO to DEFAULT: {bucket:?}");
        Ok(())
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the following information:
         
         {
           "rpo": "STATE"
         }

Where `STATE` is `ASYNC_TURBO` for enabling Turbo Replication or `DEFAULT` for disabling Turbo Replication.

  3. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`PATCH` Bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/patch) request:
         
         curl -X PATCH --data-binary @JSON_FILE_NAME \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME?fields=rpo"

Where:

     * `JSON_FILE_NAME` is the path for the JSON file that you created in Step 2.
     * `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.

If the request is successful, no response is returned.




### XML API

This feature cannot be managed through the XML API. Use the JSON API instead.

## Check a bucket's replication status

To check the [recovery point objective (RPO)](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide#basics_of_dr_planning) or replication status of a bucket, complete the following instructions:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the bucket list, click the name of the bucket you want to verify.

  3. Click the **Configuration** tab.

  4. If turbo replication is enabled on the bucket, **Replication** is set to **Turbo**.




### Command line

Use the [`gcloud storage buckets describe`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/describe) command with the `--format` flag:
    
    
    gcloud storage buckets describe gs://BUCKET_NAME --format="default(rpo)"

Where:

  * `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.



If successful, the response looks like the following example:
    
    
    rpo: ASYNC_TURBO

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name) {
      auto metadata = client.GetBucketMetadata(bucket_name);
      if (!metadata) throw std::move(metadata).status();
    
      std::cout << "RPO is " << metadata->rpo() << " for bucket "
                << metadata->name() << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using System;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    
    public class GetRpoSample
    {
        public string GetRpo(string bucketName = "your-unique-bucket-name")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var rpo = storage.GetBucket(bucketName).Rpo;
            Console.WriteLine($"The RPO Setting of bucket {bucketName} is {rpo}.");
    
            return rpo;
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
    
    // getRPO gets the current RPO (Recovery Point Objective) setting
    // for the bucket, either "DEFAULT" or "ASYNC_TURBO".
    func getRPO(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucketName string) error {
    	// bucketName := "bucket-name"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    
    	attrs, err := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucketName).Attrs(ctx)
    	if err != nil {
    		return fmt.Errorf("Bucket(%q).Attrs: %w", bucketName, err)
    	}
    	fmt.Fprintf(w, "RPO is %s for %v", attrs.[RPO](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_RPO), bucketName)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class GetBucketRpo {
      public static void getBucketRpo(String projectId, String bucketName) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket = storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName);
        String rpo = bucket.[getRpo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_getRpo__)().toString();
    
        System.out.println("The RPO setting of bucket " + bucketName + " is " + rpo);
      }
    }

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The name of your GCS bucket in a dual-region
    // const bucketName = 'Name of a bucket, e.g. my-bucket';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function getRPO() {
      // Gets Bucket Metadata and prints RPO value (either 'default' or 'async_turbo').
      // If RPO is undefined, the bucket is a single region bucket
      const [metadata] = await storage.bucket(bucketName).getMetadata();
      console.log(`RPO is ${metadata.rpo} for ${bucketName}.`);
    }
    
    getRPO();
    

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Get the bucket's recovery point objective (RPO) setting.
     *
     * @param string $bucketName the name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     */
    function get_rpo(string $bucketName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
    
        printf(
            'The bucket\'s RPO value is: %s.' . PHP_EOL,
            $bucket->info()['rpo']
        );
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def get_rpo(bucket_name):
        """Gets the RPO of the bucket"""
        # The ID of your GCS bucket
        # bucket_name = "my-bucket"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[get_bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_get_bucket)(bucket_name)
        rpo = bucket.[rpo](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_rpo)
    
        print(f"RPO for {bucket.name} is {[rpo](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_rpo)}.")
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def get_rpo bucket_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket  = storage.bucket bucket_name
    
      puts "The RPO setting of bucket '#{bucket_name}' is #{bucket.[rpo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)}."
    end

### Rust
    
    
    use google_cloud_storage::client::StorageControl;
    
    pub async fn sample(client: &StorageControl, bucket_id: &str) -> anyhow::Result<()> {
        let bucket = client
            .get_bucket()
            .set_name(format!("projects/_/buckets/{bucket_id}"))
            .send()
            .await?;
        println!("successfully obtained bucket metadata {bucket:?}");
        Ok(())
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`GET` Bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/get) request:
         
         curl -X GET \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME?fields=rpo"

Where `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.

The response looks like the following example:
         
         {
           "name": "my-bucket",
           "projectNumber": "234...",
           ...
           "rpo": "ASYNC_TURBO"
         }

Notice the [`rpo`](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#resource-representations) key. The value `ASYNC_TURBO` indicates that turbo replication is enabled. `DEFAULT` indicates that default replication is applied. The `rpo` field is always present for dual- and multi-region buckets, but is absent from single-region buckets.




### XML API

This feature cannot be managed through the XML API. Use the JSON API instead.

## What's next

  * Learn more about [turbo replication](https://docs.cloud.google.com/storage/docs/availability-durability#turbo-replication).


  * Learn more about [turbo replication pricing](https://docs.cloud.google.com/storage/pricing#inter-region-replication).


  * Learn about [metrics that monitor your bucket's performance](https://docs.cloud.google.com/storage/docs/monitoring), including replication performance.
  * Learn how [Cloud Monitoring alerting](https://docs.cloud.google.com/monitoring/alerts) can be used to create altering policies based on specified metrics and manage notifications associated with them.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
