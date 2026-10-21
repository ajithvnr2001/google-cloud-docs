---
url: https://docs.cloud.google.com/storage/docs/samples/storage-create-bucket-turbo-replication/
title: Create a dual-region bucket with turbo replication \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:17:02.759046+00:00
---

# Create a dual-region bucket with turbo replication  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-create-bucket-turbo-replication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Create a dual-region bucket with turbo replication Stay organized with collections  Save and categorize content based on your preferences. 

Create a dual-region bucket with turbo replication

## Code sample

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name) {
      auto bucket =
          client.CreateBucket(bucket_name, gcs::BucketMetadata()
                                               .set_rpo(gcs::RpoAsyncTurbo())
                                               .set_location("NAM4"));
      if (!bucket) throw std::move(bucket).status();
    
      std::cout << "Created bucket " << bucket->name() << " with RPO set to "
                << bucket->rpo() << " in " << bucket->location() << ".\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using Google.Apis.Storage.v1.Data;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class CreateBucketWithTurboReplicationSample
    {
        public Bucket CreateBucketWithTurboReplication(
            string projectId = "your-project-id",
            string location = "your-bucket-location",
            string bucketName = "bucket-name")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            // Enabling turbo replication requires a bucket with dual-region configuration
            var bucket = storage.CreateBucket(projectId, new Bucket { Name = bucketName , Location = location, Rpo = "ASYNC_TURBO" });
    
            Console.WriteLine($"Created {bucket.Name} in {bucket.Location} with RPO Setting {bucket.Rpo}.");
            return bucket;
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
    
    // createBucketTurboReplication creates a new dual-region bucket with
    // turbo replication enabled.
    func createBucketTurboReplication(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), projectID, bucketName, location string) error {
    	// projectID := "my-project-id"
    	// bucketName := "bucket-name"
    	// location := "NAM4" // the name of a dual-region location
    	// See this documentation for other valid locations:
    	// https://cloud.google.com/storage/docs/locations#location-dr
    
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*30)
    	defer cancel()
    
    	storageLocationAndRPO := &storage.[BucketAttrs](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketAttrs){
    		Location: location,
    		RPO:      storage.[RPOAsyncTurbo](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_RPOUnknown_RPODefault_RPOAsyncTurbo),
    	}
    	bucket := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucketName)
    	if err := bucket.[Create](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Create)(ctx, projectID, storageLocationAndRPO); err != nil {
    		return fmt.Errorf("Bucket(%q).Create: %w", bucketName, err)
    	}
    	fmt.Fprintf(w, "Created bucket %v with turbo replication in %v\n", bucketName, storageLocationAndRPO.Location)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html);
    import com.google.cloud.storage.[Rpo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Rpo.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class CreateBucketWithTurboReplication {
      public static void createBucketWithTurboReplication(
          String projectId, String bucketName, String location) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID to give your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The dual-region location to create your bucket in
        // String location = "NAM4"
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
    
        [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket =
            storage.[create](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_create_com_google_cloud_storage_BlobInfo_byte___com_google_cloud_storage_Storage_BlobTargetOption____)(
                BucketInfo.newBuilder(bucketName)
                    .setLocation(location)
                    .setRpo(Rpo.ASYNC_TURBO)
                    .build());
    
        System.out.println(
            "Created bucket "
                + bucket.getName()
                + " in "
                + bucket.getLocation()
                + " with RPO setting"
                + bucket.[getRpo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_getRpo__)());
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
    
    // The name of a dual-region location
    // See this documentation for other valid locations:
    // https://cloud.google.com/storage/docs/locations#location-dr
    // const location = 'NAM4';
    
    // Flag to enable turbo replication for this bucket
    const rpo = 'ASYNC_TURBO';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    // The bucket in the sample below will be created in the project associated with this client.
    // For more information, please see https://cloud.google.com/docs/authentication/production or https://googleapis.dev/nodejs/storage/latest/Storage.html
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function createBucketWithTurboReplication() {
      // For default values see: https://cloud.google.com/storage/docs/locations and
      // https://cloud.google.com/storage/docs/storage-classes
      const [bucket] = await storage.createBucket(bucketName, {
        location,
        rpo,
      });
    
      console.log(
        `${bucket.name} created with the recovery point objective (RPO) set to ${rpo} in ${location}.`
      );
    }
    
    createBucketWithTurboReplication();

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Create a Cloud Storage bucket with the recovery point objective (RPO) set to `ASYNC_TURBO`.
     * The bucket must be a dual-region bucket for this setting to take effect.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $location The Dual-Region location where you want your bucket to reside (e.g. "US-CENTRAL1+US-WEST1").
                                               Read more at https://cloud.google.com/storage/docs/locations#location-dr
     */
    function create_bucket_turbo_replication(string $bucketName, string $location = 'nam4'): void
    {
        $storage = new StorageClient();
        $rpo = 'ASYNC_TURBO';
    
        // providing a location which is a dual-region location
        // makes sure the locationType is set to 'dual-region' implicitly
        // we can pass 'locationType' => 'dual-region'
        // to make it explicit
        $bucket = $storage->createBucket($bucketName, [
            'location' => $location,
            'rpo' => $rpo
        ]);
        printf('Bucket with recovery point objective (RPO) set to \'ASYNC_TURBO\' created: %s' . PHP_EOL, $bucket->name());
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    from google.cloud.storage.constants import RPO_ASYNC_TURBO
    
    
    def create_bucket_turbo_replication(bucket_name):
        """Creates dual-region bucket with turbo replication enabled."""
        # The ID of your GCS bucket
        # bucket_name = "my-bucket"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
        bucket_location = "NAM4"
        bucket.[rpo](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_rpo) = RPO_ASYNC_TURBO
        bucket.create(location=bucket_location)
    
        print(f"{bucket.name} created with the recovery point objective (RPO) set to {bucket.[rpo](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_rpo)} in {bucket.[location](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_location)}.")
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def create_bucket_turbo_replication bucket_name:
      # The ID to give your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket  = storage.[create_bucket](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Project.html) bucket_name,
                                      location: "ASIA1",
                                      rpo:      "ASYNC_TURBO"
    
      puts "Created bucket #{bucket.name} in #{bucket.location} with "
      + "the recovery point objective (RPO) set to #{bucket.[rpo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)}."
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
