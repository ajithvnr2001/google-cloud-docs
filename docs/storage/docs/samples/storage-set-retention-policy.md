---
url: https://docs.cloud.google.com/storage/docs/samples/storage-set-retention-policy/
title: Set a retention policy \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:34:45.281907+00:00
---

# Set a retention policy  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-set-retention-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Set a retention policy Stay organized with collections  Save and categorize content based on your preferences. 

An example of how to set a retention policy on a bucket.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Use and lock retention policies](https://docs.cloud.google.com/storage/docs/using-bucket-lock)



## Code sample

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
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

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
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
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
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

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
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

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
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

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
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
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def set_retention_policy bucket_name:, retention_period:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      # The retention period for objects in bucket
      # retention_period = 3600 # 1 hour in seconds
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket  = storage.bucket bucket_name
    
      bucket.[retention_period](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) = retention_period
    
      puts "Retention period for #{bucket_name} is now #{bucket.[retention_period](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)} seconds."
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
