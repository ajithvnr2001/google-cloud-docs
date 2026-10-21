---
url: https://docs.cloud.google.com/storage/docs/samples/storage-create-bucket-dual-region/
title: Create a dual-region bucket \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:17:03.645496+00:00
---

# Create a dual-region bucket  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-create-bucket-dual-region/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Create a dual-region bucket Stay organized with collections  Save and categorize content based on your preferences. 

Create a dual-region bucket

## Code sample

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name,
       std::string const& region_a, std::string const& region_b) {
      auto metadata = client.CreateBucket(
          bucket_name,
          gcs::BucketMetadata().set_custom_placement_config(
              gcs::BucketCustomPlacementConfig{{region_a, region_b}}));
      if (!metadata) throw std::move(metadata).status();
    
      std::cout << "Bucket " << metadata->name() << " created."
                << "\nFull Metadata: " << *metadata << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using Google.Apis.Storage.v1.Data;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class CreateDualRegionBucketSample
    {
        public Bucket CreateDualRegionBucket(
            string projectId = "your-project-id",
            string bucketName = "your-unique-bucket-name",
            string location = "your-location",
            string region1 = "your-region1-name",
            string region2 = "your-region2-name")
        {
            var client = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
    
            var bucket = new Bucket
            {
                Name = bucketName,
                Location = location,
                CustomPlacementConfig = new Bucket.CustomPlacementConfigData
                {
                    DataLocations = new[] { region1, region2 }
                }
            };
    
            var storageBucket = client.CreateBucket(projectId, bucket);
    
            Console.WriteLine($"Created storage bucket {storageBucket.Name}" +
                $" in {storageBucket.Location}" +
                $" with location-type {storageBucket.LocationType} and" +
                $" dataLocations {string.Join(",", storageBucket.CustomPlacementConfig.DataLocations)}.");
    
            return storageBucket;
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
    
    // createBucketDualRegion creates a new dual-region bucket in the project in the
    // provided location and regions.
    // See https://cloud.google.com/storage/docs/locations#location-dr for more information.
    func createBucketDualRegion(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), projectID, bucketName string) error {
    	// projectID := "my-project-id"
    	// bucketName := "bucket-name"
    	location := "US"
    	region1 := "US-EAST1"
    	region2 := "US-WEST1"
    
    	ctx := context.Background()
    
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*30)
    	defer cancel()
    
    	storageDualRegion := &storage.[BucketAttrs](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketAttrs){
    		Location: location,
    		CustomPlacementConfig: &storage.[CustomPlacementConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_CustomPlacementConfig){
    			DataLocations: []string{region1, region2},
    		},
    	}
    	bucket := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucketName)
    	if err := bucket.[Create](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Create)(ctx, projectID, storageDualRegion); err != nil {
    		return fmt.Errorf("Bucket(%q).Create: %w", bucketName, err)
    	}
    
    	attrs, err := bucket.Attrs(ctx)
    	if err != nil {
    		return fmt.Errorf("Bucket(%q).Attrs: %w", bucketName, err)
    	}
    	fmt.Fprintf(w, "Created bucket %v", bucketName)
    	fmt.Fprintf(w, " - location: %v", attrs.Location)
    	fmt.Fprintf(w, " - locationType: %v", attrs.LocationType)
    	fmt.Fprintf(w, " - customPlacementConfig.dataLocations: %v", attrs.[CustomPlacementConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_CustomPlacementConfig).DataLocations)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html);
    import com.google.cloud.storage.[BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html).[CustomPlacementConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.CustomPlacementConfig.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import java.util.Arrays;
    
    public class CreateBucketDualRegion {
    
      public static void createBucketDualRegion(
          String projectId,
          String bucketName,
          String location,
          String firstRegion,
          String secondRegion) {
        // The ID of your GCP project.
        // String projectId = "your-project-id";
    
        // The ID to give your GCS bucket.
        // String bucketName = "your-unique-bucket-name";
    
        // The location your dual regions will be located in.
        // String location = "US";
    
        // One of the regions the dual region bucket is to be created in.
        // String firstRegion = "US-EAST1";
    
        // The second region the dual region bucket is to be created in.
        // String secondRegion = "US-WEST1";
    
        // See this documentation for other valid locations and regions:
        // https://cloud.google.com/storage/docs/locations
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
    
        [CustomPlacementConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.CustomPlacementConfig.html) config =
            [CustomPlacementConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.CustomPlacementConfig.html).newBuilder()
                .[setDataLocations](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.CustomPlacementConfig.Builder.html#com_google_cloud_storage_BucketInfo_CustomPlacementConfig_Builder_setDataLocations_java_util_List_java_lang_String__)(Arrays.asList(firstRegion, secondRegion))
                .build();
    
        [BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html) bucketInfo =
            [BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html).newBuilder(bucketName)
                .setLocation(location)
                .setCustomPlacementConfig(config)
                .build();
    
        [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket = storage.[create](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_create_com_google_cloud_storage_BlobInfo_byte___com_google_cloud_storage_Storage_BlobTargetOption____)(bucketInfo);
    
        System.out.println(
            "Created bucket "
                + bucket.getName()
                + " in location "
                + bucket.getLocation()
                + " with location type "
                + bucket.[getLocationType](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_getLocationType__)()
                + " with Custom Placement Config "
                + bucket.[getCustomPlacementConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_getCustomPlacementConfig__)().toString());
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
    
    // The bucket's pair of regions. Case-insensitive.
    // See this documentation for other valid locations:
    // https://cloud.google.com/storage/docs/locations
    // const location = 'US';
    // const region1 = 'US-EAST1';
    // const region2 = 'US-WEST1';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    // The bucket in the sample below will be created in the project associated with this client.
    // For more information, please see https://cloud.google.com/docs/authentication/production or https://googleapis.dev/nodejs/storage/latest/Storage.html
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function createDualRegionBucket() {
      // For regions supporting dual-regions see: https://cloud.google.com/storage/docs/locations
      const [bucket] = await storage.createBucket(bucketName, {
        location,
        customPlacementConfig: {
          dataLocations: [region1, region2],
        },
      });
    
      console.log(`Created '${bucket.name}'`);
      console.log(`- location: '${bucket.metadata.location}'`);
      console.log(`- locationType: '${bucket.metadata.locationType}'`);
      console.log(
        `- customPlacementConfig: '${[JSON](https://docs.cloud.google.com/nodejs/docs/reference/storage-transfer/latest/storage-transfer/protos.google.storagetransfer.v1.notificationconfig.payloadformat.html).stringify(
          bucket.metadata.customPlacementConfig
        )}'`
      );
    }
    
    createDualRegionBucket().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Create a new bucket with a custom default storage class and location.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $location Location for the bucket's regions. Case-insensitive.
     *        (e.g. 'US')
     * @param string $region1 First region for the bucket's regions. Case-insensitive.
     *        (e.g. 'US-EAST1')
     * @param string $region2 Second region for the bucket's regions. Case-insensitive.
     *        (e.g. 'US-WEST1')
     */
    function create_bucket_dual_region(string $bucketName, string $location, string $region1, string $region2): void
    {
        $storage = new StorageClient();
        $bucket = $storage->createBucket($bucketName, [
            'location' => $location,
            'customPlacementConfig' => [
                'dataLocations' => [$region1, $region2],
            ],
        ]);
    
        $info = $bucket->info();
    
        printf("Created '%s':", $bucket->name());
        printf("- location: '%s'", $info['location']);
        printf("- locationType: '%s'", $info['locationType']);
        printf("- customPlacementConfig: '%s'" . PHP_EOL, print_r($info['customPlacementConfig'], true));
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def create_bucket_dual_region(bucket_name, location, region_1, region_2):
        """Creates a Dual-Region Bucket with provided location and regions.."""
        # The ID of your GCS bucket
        # bucket_name = "your-bucket-name"
    
        # The bucket's pair of regions. Case-insensitive.
        # See this documentation for other valid locations:
        # https://cloud.google.com/storage/docs/locations
        # region_1 = "US-EAST1"
        # region_2 = "US-WEST1"
        # location = "US"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[create_bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_create_bucket)(bucket_name, location=location, data_locations=[region_1, region_2])
    
        print(f"Created bucket {bucket_name}")
        print(f" - location: {bucket.[location](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_location)}")
        print(f" - location_type: {bucket.[location_type](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_location_type)}")
        print(f" - customPlacementConfig data_locations: {bucket.[data_locations](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_data_locations)}")
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    
    # The bucket's pair of regions. Case-insensitive.
    # See this documentation for other valid locations:
    # https://cloud.google.com/storage/docs/locations
    # region_1 = "US-EAST1"
    # region_2 = "US-WEST1"
    
    require "google/cloud/storage"
    
    storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
    bucket  = storage.[create_bucket](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Project.html) bucket_name,
                                    custom_placement_config: { data_locations: [region_1, region_2] }
    
    puts "Bucket #{bucket.name} created:"
    puts "- location: #{bucket.location}"
    puts "- location_type: #{bucket.location_type}"
    puts "- custom_placement_config:"
    puts "  - data_locations: #{bucket.data_locations}"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
