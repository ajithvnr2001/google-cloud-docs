---
url: https://docs.cloud.google.com/storage/docs/using-bucket-lock/
title: Use and lock retention policies \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:27:55.306568+00:00
---

# Use and lock retention policies  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/using-bucket-lock/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Use and lock retention policies Stay organized with collections  Save and categorize content based on your preferences. 

[Overview](https://docs.cloud.google.com/storage/docs/bucket-lock)

This page describes how to use the Bucket Lock feature, including working with retention policies and permanently locking them on buckets.

## Before you begin

Before you can use the Bucket Lock feature, make sure the steps in the following sections have been completed.

### Get required roles

To get the permissions that you need to use Bucket Lock, ask your administrator to grant you the Storage Admin (`roles/storage.admin`) role on the bucket. This [predefined role](https://docs.cloud.google.com/iam/docs/roles-overview#predefined) contains the permissions required to use Bucket Lock. To see the exact permissions required, expand the **Required permissions** section:

#### Required permissions

  * `storage.buckets.get`
  * `storage.buckets.list`
    * This permission is only required if you plan on using the Google Cloud console to perform the instructions on this page.
  * `storage.buckets.update`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

For information about granting roles on buckets, see [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).

## Set a retention policy on a bucket

To add, modify, or remove a retention policy on a bucket:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket whose retention policy you want to change.

  3. Select the **Protection** tab near the top of the page.

  4. In the **Retention policy** section, set your retention policy:

     1. If no retention policy currently applies to the bucket, click the _add_box_ **Set Retention Policy** link. Choose a unit of time and a length of time for your retention period.

     2. If a retention policy currently applies to a bucket, it appears in the section. Click **Edit** to modify the retention time or **Delete** to remove the retention policy entirely.

See [Retention periods](https://docs.cloud.google.com/storage/docs/bucket-lock#retention-periods) for information about how the Google Cloud console converts between different units of time.




To learn how to get detailed error information about failed Cloud Storage operations in the Google Cloud console, see [Troubleshooting](https://docs.cloud.google.com/storage/docs/troubleshooting#trouble-console).

### Command line

Use the [`gcloud storage buckets update`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/update) command with the appropriate flag:
    
    
    gcloud storage buckets update gs://BUCKET_NAME FLAG

Where:

  * `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.

  * `FLAG` is the desired setting for the bucket's retention period. Use one of the following formats:

    * `--retention-period` and a [retention period](https://docs.cloud.google.com/storage/docs/bucket-lock#retention-periods), if you want to add or change a retention policy. For example, `--retention-period=1d43200s`.
    * `--clear-retention-period`, if you want to remove the retention policy on the bucket.



If successful, the response looks like:
    
    
    Updating gs://my-bucket/...
      Completed 1  

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample sets a retention policy on a bucket:
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name,
       std::chrono::seconds period) {
      StatusOr<gcs::BucketMetadata> original =
          client.GetBucketMetadata(bucket_name);
      if (!original) throw std::move(original).status();
    
      StatusOr<gcs::BucketMetadata> patched = client.PatchBucket(
          bucket_name,
          gcs::BucketMetadataPatchBuilder().SetRetentionPolicy(period),
          gcs::IfMetagenerationMatch(original->metageneration()));
      if (!patched) throw std::move(patched).status();
    
      if (!patched->has_retention_policy()) {
        std::cout << "The bucket " << patched->name()
                  << " does not have a retention policy set.\n";
        return;
      }
    
      std::cout << "The bucket " << patched->name()
                << " retention policy is set to " << patched->retention_policy()
                << "\n";
    }

The following sample removes the retention policy from a bucket:
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name) {
      StatusOr<gcs::BucketMetadata> original =
          client.GetBucketMetadata(bucket_name);
      if (!original) throw std::move(original).status();
    
      StatusOr<gcs::BucketMetadata> patched = client.PatchBucket(
          bucket_name, gcs::BucketMetadataPatchBuilder().ResetRetentionPolicy(),
          gcs::IfMetagenerationMatch(original->metageneration()));
      if (!patched) throw std::move(patched).status();
    
      if (!patched->has_retention_policy()) {
        std::cout << "The bucket " << patched->name()
                  << " does not have a retention policy set.\n";
        return;
      }
    
      std::cout << "The bucket " << patched->name()
                << " retention policy is set to " << patched->retention_policy()
                << ". This is unexpected, maybe a concurrent change by another"
                << " application?\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample sets a retention policy on a bucket:
    
    
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    using static Google.Apis.Storage.v1.Data.Bucket;
    
    public class SetRetentionPolicySample
    {
        /// <summary>
        /// Sets the bucket's retention policy.
        /// </summary>
        /// <param name="bucketName">The name of the bucket.</param>
        /// <param name="retentionPeriod">The duration in seconds that objects need to be retained. The retention policy enforces a minimum retention
        /// time for all objects contained in the bucket, based on their creation time. Any
        /// attempt to overwrite or delete objects younger than the retention period will
        /// result in a PERMISSION_DENIED error. An unlocked retention policy can be modified
        /// or removed from the bucket via a storage.buckets.update operation. A locked retention
        /// policy cannot be removed or shortened in duration for the lifetime of the bucket.
        /// Attempting to remove or decrease the period of a locked retention policy will result
        /// in a PERMISSION_DENIED error.</param>
        public RetentionPolicyData SetRetentionPolicy(
            string bucketName = "your-unique-bucket-name",
            long retentionPeriod = 10)
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var bucket = storage.GetBucket(bucketName);
            bucket.RetentionPolicy = new RetentionPolicyData { RetentionPeriod = retentionPeriod };
    
            bucket = storage.UpdateBucket(bucket);
    
            Console.WriteLine($"Retention policy for {bucketName} was set to {retentionPeriod}");
            return bucket.RetentionPolicy;
        }
    }

The following sample removes the retention policy from a bucket:
    
    
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class RemoveRetentionPolicySample
    {
        public void RemoveRetentionPolicy(string bucketName = "your-unique-bucket-name")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var bucket = storage.GetBucket(bucketName);
            if (bucket.RetentionPolicy != null)
            {
                bool isLocked = bucket.RetentionPolicy.IsLocked ?? false;
                if (isLocked)
                {
                    throw new Exception("Retention Policy is locked.");
                }
    
                bucket.RetentionPolicy.RetentionPeriod = null;
                storage.UpdateBucket(bucket);
    
                Console.WriteLine($"Retention period for {bucketName} has been removed.");
            }
        }
    }

### Go

For more information, see the [Cloud Storage Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storage). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample sets a retention policy on a bucket:
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/storage"
    )
    
    // setRetentionPolicy sets the bucket retention period.
    func setRetentionPolicy(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucketName string, retentionPeriod time.Duration) error {
    	// bucketName := "bucket-name"
    	// retentionPeriod := time.Second
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
    		RetentionPolicy: &storage.[RetentionPolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_RetentionPolicy){
    			RetentionPeriod: retentionPeriod,
    		},
    	}
    	if _, err := bucket.Update(ctx, bucketAttrsToUpdate); err != nil {
    		return fmt.Errorf("Bucket(%q).Update: %w", bucketName, err)
    	}
    	fmt.Fprintf(w, "Retention policy for %v was set to %v\n", bucketName, bucketAttrsToUpdate.[RetentionPolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_RetentionPolicy).RetentionPeriod)
    	return nil
    }
    

The following sample removes the retention policy from a bucket:
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/storage"
    )
    
    // removeRetentionPolicy removes bucket retention policy.
    func removeRetentionPolicy(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucketName string) error {
    	// bucketName := "bucket-name"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*50)
    	defer cancel()
    
    	bucket := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucketName)
    	attrs, err := bucket.Attrs(ctx)
    	if err != nil {
    		return fmt.Errorf("Bucket(%q).Attrs: %w", bucketName, err)
    	}
    	if attrs.[RetentionPolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_RetentionPolicy).IsLocked {
    		return fmt.Errorf("retention policy is locked")
    	}
    
    	bucketAttrsToUpdate := storage.[BucketAttrsToUpdate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketAttrsToUpdate){
    		RetentionPolicy: &storage.[RetentionPolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_RetentionPolicy){},
    	}
    	if _, err := bucket.Update(ctx, bucketAttrsToUpdate); err != nil {
    		return fmt.Errorf("Bucket(%q).Update: %w", bucketName, err)
    	}
    	fmt.Fprintf(w, "Retention period for %v has been removed\n", bucketName)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample sets a retention policy on a bucket:
    
    
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).[BucketTargetOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.BucketTargetOption.html);
    import com.google.cloud.storage.[StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import java.time.Duration;
    
    public class SetRetentionPolicy {
      public static void setRetentionPolicy(
          String projectId, String bucketName, Long retentionPeriodSeconds) throws [StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The retention period for objects in bucket
        // Long retentionPeriodSeconds = 3600L; // 1 hour in seconds
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
    
        // first look up the bucket so we will have its metageneration
        [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket = storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName);
        [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucketWithRetentionPolicy =
            storage.[update](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_update_com_google_cloud_storage_BlobInfo_)(
                bucket.toBuilder()
                    .setRetentionPeriodDuration(Duration.ofSeconds(retentionPeriodSeconds))
                    .build(),
                BucketTargetOption.metagenerationMatch());
    
        System.out.println(
            "Retention period for "
                + bucketName
                + " is now "
                + bucketWithRetentionPolicy.[getRetentionPeriodDuration](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_getRetentionPeriodDuration__)());
      }
    }

The following sample removes the retention policy from a bucket:
    
    
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class RemoveRetentionPolicy {
      public static void removeRetentionPolicy(String projectId, String bucketName)
          throws [StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html), IllegalArgumentException {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
    
        [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket =
            storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(
                bucketName, Storage.BucketGetOption.fields(Storage.BucketField.RETENTION_POLICY));
        if (bucket.[retentionPolicyIsLocked](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_retentionPolicyIsLocked__)() != null && bucket.[retentionPolicyIsLocked](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_retentionPolicyIsLocked__)()) {
          throw new IllegalArgumentException(
              "Unable to remove retention policy as retention policy is locked.");
        }
    
        bucket.[toBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html#com_google_cloud_storage_Bucket_toBuilder__)().setRetentionPeriod(null).build().update();
    
        System.out.println("Retention policy for " + bucketName + " has been removed");
      }
    }

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample sets a retention policy on a bucket:
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The ID of your GCS bucket
    // const bucketName = 'your-unique-bucket-name';
    
    // The retention period for objects in bucket
    // const retentionPeriod = 3600; // 1 hour in seconds
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function setRetentionPolicy() {
      const [metadata] = await storage
        .bucket(bucketName)
        .[setRetentionPeriod](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/bucket.html)(retentionPeriod);
      console.log(
        `Bucket ${bucketName} retention period set for ${metadata.retentionPolicy.retentionPeriod} seconds.`
      );
    }
    
    setRetentionPolicy().catch(console.error);

The following sample removes the retention policy from a bucket:
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The ID of your GCS bucket
    // const bucketName = 'your-unique-bucket-name';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function removeRetentionPolicy() {
      const [metadata] = await storage.bucket(bucketName).getMetadata();
      if (metadata.retentionPolicy && metadata.retentionPolicy.isLocked) {
        console.log(
          'Unable to remove retention period as retention policy is locked.'
        );
        return null;
      } else {
        const results = await storage.bucket(bucketName).[removeRetentionPeriod](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/bucket.html)();
        console.log(`Removed bucket ${bucketName} retention policy.`);
        return results;
      }
    }
    
    removeRetentionPolicy().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample sets a retention policy on a bucket:
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Sets a bucket's retention policy.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param int $retentionPeriod The retention period for objects in bucket, in seconds.
     *        (e.g. 3600)
     */
    function set_retention_policy(string $bucketName, int $retentionPeriod): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
        $bucket->update([
            'retentionPolicy' => [
                'retentionPeriod' => $retentionPeriod
            ]]);
        printf('Bucket %s retention period set to %s seconds' . PHP_EOL, $bucketName,
            $retentionPeriod);
    }

The following sample removes the retention policy from a bucket:
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Removes a bucket's retention policy.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     */
    function remove_retention_policy(string $bucketName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
        $bucket->reload();
    
        if (array_key_exists('isLocked', $bucket->info()['retentionPolicy']) &&
            $bucket->info()['retentionPolicy']['isLocked']) {
            printf('Unable to remove retention period as retention policy is locked.' . PHP_EOL);
            return;
        }
    
        $bucket->update([
            'retentionPolicy' => []
        ]);
        printf('Removed bucket %s retention policy' . PHP_EOL, $bucketName);
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample sets a retention policy on a bucket:
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def set_retention_policy(bucket_name, retention_period):
        """Defines a retention policy on a given bucket"""
        # bucket_name = "my-bucket"
        # retention_period = 10
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
    
        bucket.[retention_period](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_retention_period) = retention_period
        bucket.patch()
    
        print(
            "Bucket {} retention period set for {} seconds".format(
                bucket.name, bucket.[retention_period](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_retention_period)
            )
        )
    
    

The following sample removes the retention policy from a bucket:
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def remove_retention_policy(bucket_name):
        """Removes the retention policy on a given bucket"""
        # bucket_name = "my-bucket"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
        bucket.reload()
    
        if bucket.[retention_policy_locked](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_retention_policy_locked):
            print(
                "Unable to remove retention period as retention policy is locked."
            )
            return
    
        bucket.[retention_period](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_retention_period) = None
        bucket.patch()
    
        print(f"Removed bucket {bucket.name} retention policy")
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample sets a retention policy on a bucket:
    
    
    def set_retention_policy bucket_name:, retention_period:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      # The retention period for objects in bucket
      # retention_period = 3600 # 1 hour in seconds
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket  = storage.bucket bucket_name
    
      bucket.[retention_period](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) = retention_period
    
      puts "Retention period for #{bucket_name} is now #{bucket.[retention_period](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)} seconds."
    end

The following sample removes the retention policy from a bucket:
    
    
    def remove_retention_policy bucket_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket  = storage.bucket bucket_name
    
      if !bucket.[retention_policy_locked?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)
        bucket.[retention_period](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) = nil
        puts "Retention policy for #{bucket_name} has been removed."
      else
        puts "Policy is locked and retention policy can't be removed."
      end
    end

### Rust

The following sample sets a retention policy on a bucket:
    
    
    use google_cloud_storage::client::StorageControl;
    use google_cloud_storage::model::bucket::RetentionPolicy;
    use google_cloud_wkt::{Duration, FieldMask};
    
    pub async fn sample(
        client: &StorageControl,
        bucket_id: &str,
        retention_period: i64,
    ) -> anyhow::Result<()> {
        let bucket = client
            .get_bucket()
            .set_name(format!("projects/_/buckets/{bucket_id}"))
            .send()
            .await?;
        let metageneration = bucket.metageneration;
        let retention_policy =
            RetentionPolicy::new().set_retention_duration(Duration::new(retention_period, 0)?);
        let bucket = client
            .update_bucket()
            .set_bucket(bucket.set_retention_policy(retention_policy))
            .set_if_metageneration_match(metageneration)
            .set_update_mask(FieldMask::default().set_paths(["retention_policy"]))
            .send()
            .await?;
        println!(
            "Retention policy for bucket {bucket_id} set to: {:?}",
            bucket.retention_policy
        );
        Ok(())
    }

The following sample removes the retention policy from a bucket:
    
    
    use google_cloud_storage::client::StorageControl;
    use google_cloud_storage::model::bucket::RetentionPolicy;
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
            .set_bucket(bucket.set_retention_policy(RetentionPolicy::new()))
            .set_if_metageneration_match(metageneration)
            .set_update_mask(FieldMask::default().set_paths(["retention_policy"]))
            .send()
            .await?;
        println!(
            "Retention policy for bucket {bucket_id} removed: {:?}",
            bucket.retention_policy
        );
        Ok(())
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the following information:
         
         {
           "retentionPolicy": {
             "retentionPeriod": "TIME_IN_SECONDS"
           }
         }

Where `TIME_IN_SECONDS` is the amount of time in seconds that objects in the bucket must be retained. For example, `2678400`. See [Retention periods](https://docs.cloud.google.com/storage/docs/bucket-lock#retention-periods) for information about how different units of time are measured using seconds.

To remove the retention policy from a bucket, use the following in the JSON file:
         
         {
           "retentionPolicy": null
         }

  3. Use [`cURL`](http://curl.haxx.se/) to call the JSON API with a [`PATCH` Bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/patch) request:
         
         curl -X PATCH --data-binary @JSON_FILE_NAME \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME?fields=retentionPolicy"

Where:

     * `JSON_FILE_NAME` is the path for the JSON file that you created in Step 2.
     * `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.



### XML API

The XML API cannot be used to set or remove a retention policy on an existing bucket. It can only be used to [include a retention policy with a new bucket](https://docs.cloud.google.com/storage/docs/xml-api/put-bucket-create).

## Lock a bucket

**Caution:** Locking a bucket is an irreversible action. Once you lock a bucket: 

  * You cannot remove the retention policy from the bucket.
  * You cannot decrease the retention period for the policy.

For more information, see [Retention policy locks](https://docs.cloud.google.com/storage/docs/bucket-lock#policy-locks).

To lock a bucket and permanently restrict edits to the bucket's retention policy:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket that you want to lock the retention policy for.

  3. Select the **Protection** tab near the top of the page.

  4. In the **Retention policy** section, click the **Lock** button.

The **Lock retention policy?** dialog box appears.

  5. Read the **Permanent** notice.

  6. In the **Bucket name** text box, type in the name of your bucket.

  7. Click **Lock policy**.




To learn how to get detailed error information about failed Cloud Storage operations in the Google Cloud console, see [Troubleshooting](https://docs.cloud.google.com/storage/docs/troubleshooting#trouble-console).

### Command line

Use the [`gcloud storage buckets update`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/update) command with the `--lock-retention-period` flag:
    
    
    gcloud storage buckets update gs://BUCKET_NAME --lock-retention-period

Where `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.

If successful, the response looks similar to the following example:
    
    
    Updating gs://my-bucket/...
      Completed 1  

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name) {
      StatusOr<gcs::BucketMetadata> original =
          client.GetBucketMetadata(bucket_name);
      if (!original) throw std::move(original).status();
    
      StatusOr<gcs::BucketMetadata> updated_metadata =
          client.LockBucketRetentionPolicy(bucket_name,
                                           original->metageneration());
      if (!updated_metadata) throw std::move(updated_metadata).status();
    
      if (!updated_metadata->has_retention_policy()) {
        std::cerr << "The bucket " << updated_metadata->name()
                  << " does not have a retention policy, even though the"
                  << " operation to set it was successful.\n"
                  << "This is unexpected, and may indicate that another"
                  << " application has modified the bucket concurrently.\n";
        return;
      }
    
      std::cout << "Retention policy successfully locked for bucket "
                << updated_metadata->name() << "\nNew retention policy is: "
                << updated_metadata->retention_policy()
                << "\nFull metadata: " << *updated_metadata << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class LockRetentionPolicySample
    {
        /// <summary>
        /// Locks the retention policy of a bucket. This is a one-way process: once a retention
        /// policy is locked, it cannot be shortened, removed or unlocked, although it can
        /// be increased in duration. The lock persists until the bucket is deleted.
        /// </summary>
        /// <param name="bucketName">The name of the bucket whose retention policy should be locked.</param>
        public bool? LockRetentionPolicy(string bucketName = "your-unique-bucket-name")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var bucket = storage.GetBucket(bucketName);
            storage.LockBucketRetentionPolicy(bucketName, bucket.Metageneration.Value);
            bucket = storage.GetBucket(bucketName);
            Console.WriteLine($"Retention policy for {bucketName} is now locked");
            Console.WriteLine($"Retention policy effective as of {bucket.RetentionPolicy.EffectiveTime}");
    
            return bucket.RetentionPolicy.IsLocked;
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
    
    // lockRetentionPolicy locks bucket retention policy.
    func lockRetentionPolicy(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucketName string) error {
    	// bucketName := "bucket-name"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*50)
    	defer cancel()
    
    	bucket := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucketName)
    	attrs, err := bucket.Attrs(ctx)
    	if err != nil {
    		return fmt.Errorf("Bucket(%q).Attrs: %w", bucketName, err)
    	}
    
    	conditions := storage.[BucketConditions](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketConditions){
    		MetagenerationMatch: attrs.MetaGeneration,
    	}
    	if err := bucket.If(conditions).[LockRetentionPolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_LockRetentionPolicy)(ctx); err != nil {
    		return fmt.Errorf("Bucket(%q).LockRetentionPolicy: %w", bucketName, err)
    	}
    
    	lockedAttrs, err := bucket.Attrs(ctx)
    	if err != nil {
    		return fmt.Errorf("Bucket(%q).Attrs: lockedAttrs: %w", bucketName, err)
    	}
    
    	fmt.Fprintf(w, "Retention policy for %v is now locked\n", bucketName)
    	fmt.Fprintf(w, "Retention policy effective as of %v\n", lockedAttrs.[RetentionPolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_RetentionPolicy).EffectiveTime)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import java.util.Date;
    
    public class LockRetentionPolicy {
      public static void lockRetentionPolicy(String projectId, String bucketName)
          throws [StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket =
            storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName, Storage.BucketGetOption.fields(Storage.BucketField.METAGENERATION));
        [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) lockedBucket =
            bucket.[lockRetentionPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html#com_google_cloud_storage_Bucket_lockRetentionPolicy_com_google_cloud_storage_Storage_BucketTargetOption____)(Storage.BucketTargetOption.metagenerationMatch());
    
        System.out.println("Retention period for " + bucketName + " is now locked");
        System.out.println(
            "Retention policy effective as of " + new Date(lockedBucket.[getRetentionEffectiveTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_getRetentionEffectiveTime__)()));
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
    
    async function lockRetentionPolicy() {
      // Gets the current metageneration value for the bucket, required by
      // lock_retention_policy
      const [unlockedMetadata] = await storage.bucket(bucketName).getMetadata();
    
      // Warning: Once a retention policy is locked, it cannot be unlocked. The
      // retention period can only be increased
      const [lockedMetadata] = await storage
        .bucket(bucketName)
        .[lock](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/bucket.html)(unlockedMetadata.metageneration);
      console.log(`Retention policy for ${bucketName} is now locked`);
      console.log(
        `Retention policy effective as of ${lockedMetadata.retentionPolicy.effectiveTime}`
      );
    
      return lockedMetadata;
    }
    
    lockRetentionPolicy().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Locks a bucket's retention policy.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     */
    function lock_retention_policy(string $bucketName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
        $bucket->reload();
        $bucket->lockRetentionPolicy();
        printf('Bucket %s retention policy locked' . PHP_EOL, $bucketName);
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def lock_retention_policy(bucket_name):
        """Locks the retention policy on a given bucket"""
        # bucket_name = "my-bucket"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        # get_bucket gets the current metageneration value for the bucket,
        # required by lock_retention_policy.
        bucket = storage_client.[get_bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_get_bucket)(bucket_name)
    
        # Warning: Once a retention policy is locked it cannot be unlocked
        # and retention period can only be increased.
        bucket.[lock_retention_policy](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_lock_retention_policy)()
    
        print(f"Retention policy for {bucket_name} is now locked")
        print(
            f"Retention policy effective as of {bucket.[retention_policy_effective_time](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_retention_policy_effective_time)}"
        )
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def lock_retention_policy bucket_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket  = storage.bucket bucket_name
    
      # Warning: Once a retention policy is locked it cannot be unlocked
      # and retention period can only be increased.
      # Uses Bucket#metageneration as a precondition.
      bucket.[lock_retention_policy!](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)
    
      puts "Retention policy for #{bucket_name} is now locked."
      puts "Retention policy effective as of #{bucket.[retention_effective_at](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)}."
    end

### Rust
    
    
    use google_cloud_storage::client::StorageControl;
    
    pub async fn sample(client: &StorageControl, bucket_id: &str) -> anyhow::Result<()> {
        let bucket = client
            .get_bucket()
            .set_name(format!("projects/_/buckets/{bucket_id}"))
            .send()
            .await?;
        let metageneration = bucket.metageneration;
        let bucket = client
            .lock_bucket_retention_policy()
            .set_if_metageneration_match(metageneration)
            .set_bucket(bucket.name)
            .send()
            .await?;
        println!(
            "Retention policy for bucket {bucket_id} locked: {:?}",
            bucket.retention_policy
        );
        Ok(())
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the JSON API with a [`POST` Bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/lockRetentionPolicy) request:
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/lockRetentionPolicy?ifMetagenerationMatch=BUCKET_METAGENERATION_NUMBER"

Where:

     * `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.
     * `BUCKET_METAGENERATION_NUMBER` is the [metageneration value](https://docs.cloud.google.com/storage/docs/bucket-metadata#non-editable) for the bucket. For example, `8`. You can find the metageneration value for your bucket by calling the JSON API with a [`GET` Bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/get) request.



### XML API

The XML API cannot be used to lock a bucket. Use one of the other Cloud Storage tools, such as the Google Cloud console, instead.

## View a bucket's retention policy and lock status

To view what, if any, retention policy is set on a bucket and whether that retention policy is locked:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click the name of the bucket whose status you want to view.

If a bucket has a retention policy, the retention period is displayed in the **Protection** field for the bucket. If the retention policy is not locked, a lock icon appears next to the retention period in an unlocked state. If the retention policy is locked, a lock icon appears next to the retention period in a locked state.




### Command line

Use the [`gcloud storage buckets describe`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/describe) command with the `--format` flag:
    
    
    gcloud storage buckets describe gs://BUCKET_NAME --format="default(retention_policy)"

Where `BUCKET_NAME` is the name of the bucket whose retention policy you want to view. For example, `my-bucket`.

If successful and a retention policy exists for the bucket, the response is similar to the following:
    
    
    retention_policy:
      effectiveTime: '2022-10-04T18:51:22.161000+00:00'
      retentionPeriod: '129600'

If successful and a retention policy does not exist for the bucket, the response is similar to the following:
    
    
    null

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
    
      if (!bucket_metadata->has_retention_policy()) {
        std::cout << "The bucket " << bucket_metadata->name()
                  << " does not have a retention policy set.\n";
        return;
      }
    
      std::cout << "The bucket " << bucket_metadata->name()
                << " retention policy is set to "
                << bucket_metadata->retention_policy() << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    using static Google.Apis.Storage.v1.Data.Bucket;
    
    public class GetRetentionPolicySample
    {
        public RetentionPolicyData GetRetentionPolicy(string bucketName = "your-unique-bucket-name")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var bucket = storage.GetBucket(bucketName);
    
            if (bucket.RetentionPolicy != null)
            {
                Console.WriteLine("Retention policy:");
                Console.WriteLine($"Period: {bucket.RetentionPolicy.RetentionPeriod}");
                Console.WriteLine($"Effective time: {bucket.RetentionPolicy.EffectiveTime}");
                bool isLocked = bucket.RetentionPolicy.IsLocked ?? false;
                Console.WriteLine($"Policy locked: {isLocked}");
            }
            return bucket.RetentionPolicy;
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
    
    // getRetentionPolicy gets bucket retention policy.
    func getRetentionPolicy(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucketName string) (*storage.[BucketAttrs](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketAttrs), error) {
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
    	if attrs.[RetentionPolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_RetentionPolicy) != nil {
    		fmt.Fprintln(w, "Retention Policy")
    		fmt.Fprintf(w, "period: %v\n", attrs.[RetentionPolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_RetentionPolicy).RetentionPeriod)
    		fmt.Fprintf(w, "effective time: %v\n", attrs.[RetentionPolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_RetentionPolicy).EffectiveTime)
    		fmt.Fprintf(w, "policy locked: %v\n", attrs.[RetentionPolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_RetentionPolicy).IsLocked)
    	}
    	return attrs, nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import java.util.Date;
    
    public class GetRetentionPolicy {
      public static void getRetentionPolicy(String projectId, String bucketName)
          throws [StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket =
            storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(
                bucketName, Storage.BucketGetOption.fields(Storage.BucketField.RETENTION_POLICY));
    
        System.out.println("Retention Policy for " + bucketName);
        System.out.println("Retention Period: " + bucket.[getRetentionPeriod](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_getRetentionPeriod__)());
        if (bucket.[retentionPolicyIsLocked](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_retentionPolicyIsLocked__)() != null && bucket.[retentionPolicyIsLocked](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_retentionPolicyIsLocked__)()) {
          System.out.println("Retention Policy is locked");
        }
        if (bucket.[getRetentionEffectiveTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_getRetentionEffectiveTime__)() != null) {
          System.out.println("Effective Time: " + new Date(bucket.[getRetentionEffectiveTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_getRetentionEffectiveTime__)()));
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
    
    async function getRetentionPolicy() {
      const [metadata] = await storage.bucket(bucketName).getMetadata();
      if (metadata.retentionPolicy) {
        const retentionPolicy = metadata.retentionPolicy;
        console.log('A retention policy exists!');
        console.log(`Period: ${retentionPolicy.retentionPeriod}`);
        console.log(`Effective time: ${retentionPolicy.effectiveTime}`);
        if (retentionPolicy.isLocked) {
          console.log('Policy is locked');
        } else {
          console.log('Policy is unlocked');
        }
      }
    }
    
    getRetentionPolicy().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Gets a bucket's retention policy.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     */
    function get_retention_policy(string $bucketName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
        $bucket->reload();
    
        printf('Retention Policy for ' . $bucketName . PHP_EOL);
        printf('Retention Period: ' . $bucket->info()['retentionPolicy']['retentionPeriod'] . PHP_EOL);
        if (array_key_exists('isLocked', $bucket->info()['retentionPolicy']) &&
            $bucket->info()['retentionPolicy']['isLocked']) {
            printf('Retention Policy is locked' . PHP_EOL);
        }
        if ($bucket->info()['retentionPolicy']['effectiveTime']) {
            printf('Effective Time: ' . $bucket->info()['retentionPolicy']['effectiveTime'] . PHP_EOL);
        }
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def get_retention_policy(bucket_name):
        """Gets the retention policy on a given bucket"""
        # bucket_name = "my-bucket"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
        bucket.reload()
    
        print(f"Retention Policy for {bucket_name}")
        print(f"Retention Period: {bucket.[retention_period](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_retention_period)}")
        if bucket.[retention_policy_locked](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_retention_policy_locked):
            print("Retention Policy is locked")
    
        if bucket.[retention_policy_effective_time](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_retention_policy_effective_time):
            print(
                f"Effective Time: {bucket.[retention_policy_effective_time](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_retention_policy_effective_time)}"
            )
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def get_retention_policy bucket_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket  = storage.bucket bucket_name
    
      puts "Retention policy:"
      puts "period: #{bucket.[retention_period](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)}"
      puts "effective time: #{bucket.[retention_effective_at](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)}"
      puts "policy locked: #{bucket.[retention_policy_locked?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)}"
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
            "Retention policy for bucket {bucket_id}: {:?}",
            bucket.retention_policy
        );
        Ok(())
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the JSON API with a [`GET` Bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/get) request that includes the desired `fields`:
         
         curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME?fields=retentionPolicy"

Where `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.

If the bucket has a retention policy set on it, the response looks like the following example:
         
         {
           "retentionPolicy": {
               "retentionPeriod": "TIME_IN_SECONDS",
               "effectiveTime": "DATETIME",
               "isLocked": "BOOLEAN"
            },
         }




### XML API

The XML API cannot be used to view the retention policy on a bucket. Use one of the other Cloud Storage tools, such as the Google Cloud console, instead.

## What's next

  * Learn more about [retention policies](https://docs.cloud.google.com/storage/docs/bucket-lock).
  * Learn how to [use object holds](https://docs.cloud.google.com/storage/docs/holding-objects).
  * Learn about [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle), which can automatically delete files once they reach their retention period.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
