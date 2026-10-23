---
url: https://docs.cloud.google.com/storage/docs/samples/storage-control-get-anywhere-cache/
title: Storage Control Get Anywhere Cache \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:55.838739+00:00
---

# Storage Control Get Anywhere Cache  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-control-get-anywhere-cache/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Storage Control Get Anywhere Cache Stay organized with collections  Save and categorize content based on your preferences. 

Storage Control Get Anywhere Cache

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create and manage Anywhere Cache caches](https://docs.cloud.google.com/storage/docs/rapid/use-rapid-cache)



## Code sample

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace storagecontrol = google::cloud::storagecontrol_v2;
    [](storagecontrol::StorageControlClient client,
       std::string const& cache_name) {
      auto anywhere_cache = client.GetAnywhereCache(cache_name);
      if (!anywhere_cache) throw std::move(anywhere_cache).status();
      std::cout << "Got anywhere cache: " << anywhere_cache->name() << "\n";
    }

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.storage.control.v2.[AnywhereCache](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.AnywhereCache.html);
    import com.google.storage.control.v2.[GetAnywhereCacheRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.GetAnywhereCacheRequest.html);
    import com.google.storage.control.v2.[StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html);
    import java.io.IOException;
    
    public final class AnywhereCacheGet {
    
      public static void anywhereCacheGet(String cacheName) throws IOException {
        try ([StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html) storageControl = [StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html).create()) {
    
          [GetAnywhereCacheRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.GetAnywhereCacheRequest.html) request =
              [GetAnywhereCacheRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.GetAnywhereCacheRequest.html).newBuilder().setName(cacheName).build();
    
          [AnywhereCache](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.AnywhereCache.html) anywhereCache = storageControl.getAnywhereCache(request);
    
          System.out.printf("Got anywhere cache: %s%n", anywhereCache.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.AnywhereCache.html#com_google_storage_control_v2_AnywhereCache_getName__)());
        }
      }
    }

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    const {StorageControlClient} = require('[@google-cloud/storage-control](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/overview.html)').v2;
    
    const client = new [StorageControlClient](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/storagecontrolclient.html)();
    
    /**
     * Gets an Anywhere Cache instance.
     *
     * @param {string} bucketName Name of the bucket (e.g., 'my-bucket')
     * @param {string} anywhereCacheZone The zone of the Anywhere Cache instance (e.g., 'us-central1-a')
     */
    async function getAnywhereCacheSample(
      bucketName,
      anywhereCacheZone = 'us-central1-a',
    ) {
      const name = client.[anywhereCachePath](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/storagecontrolclient.html)('_', bucketName, anywhereCacheZone);
    
      const request = {
        name,
      };
    
      try {
        const [anywhereCache] = await client.getAnywhereCache(request);
        console.log(`Anywhere Cache ${anywhereCache.name} retrieved successfully.`);
        console.log(`  State: ${anywhereCache.state}`);
        console.log(`  TTL: ${anywhereCache.ttl?.seconds} seconds`);
        console.log(`  Admission Policy: ${anywhereCache.admissionPolicy}`);
        console.log(`  Zone: ${anywhereCache.zone}`);
      } catch (err) {
        if (err.code === status.NOT_FOUND) {
          console.error(
            `Error: Anywhere Cache in zone '${anywhereCacheZone}' not found in bucket '${bucketName}'.`,
          );
          console.error(
            'Please ensure the Anywhere Cache zone and bucket name are correct and the cache exists.',
          );
        } else {
          console.error(`Error getting Anywhere Cache:`, err);
        }
      }
    }

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\Control\V2\Client\StorageControlClient;
    use Google\Cloud\Storage\Control\V2\GetAnywhereCacheRequest;
    
    /**
     * Gets an Anywhere Cache instance.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $anywhereCacheId Uniquely identifies the cache.
     *        (e.g. 'us-east1-b')
     */
    function get_anywhere_cache(string $bucketName, string $anywhereCacheId): void
    {
        $storageControlClient = new StorageControlClient();
    
        // Set project to "_" to signify global bucket
        $formattedName = $storageControlClient->anywhereCacheName('_', $bucketName, $anywhereCacheId);
    
        $request = new GetAnywhereCacheRequest([
            'name' => $formattedName,
        ]);
    
        $response = $storageControlClient->getAnywhereCache($request);
    
        printf('Got anywhere cache: %s', $response->getName());
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import google.api_core.exceptions
    from google.cloud import [storage_control_v2](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest)
    
    
    def get_anywhere_cache(
        bucket_name: str,
        anywhere_cache_zone: str,
    ) -> None:
        """Retrieves the metadata for a specific Anywhere Cache instance.
    
        Args:
            bucket_name: The name of the bucket where the Anywhere Cache is located.
            anywhere_cache_zone: The ID zone of the Anywhere Cache instance to retrieve.
                               Example: "us-central1-a"
        """
        client = [storage_control_v2](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest).[StorageControlClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.services.storage_control.StorageControlClient.html)()
    
        anywhere_cache_name = client.[anywhere_cache_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.services.storage_control.StorageControlClient.html#google_cloud_storage_control_v2_services_storage_control_StorageControlClient_anywhere_cache_path)(
            project="_",
            bucket=bucket_name,
            anywhere_cache=anywhere_cache_zone,
        )
    
        try:
            anywhere_cache = client.[get_anywhere_cache](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.services.storage_control.StorageControlClient.html#google_cloud_storage_control_v2_services_storage_control_StorageControlClient_get_anywhere_cache)(name=anywhere_cache_name)
    
            print(f"Successfully retrieved Anywhere Cache: {anywhere_cache.name}")
            print(f"  Zone: {anywhere_cache.zone}")
            print(f"  State: {anywhere_cache.state}")
            print(f"  TTL: {anywhere_cache.ttl.seconds} seconds")
            print(f"  Admission Policy: {anywhere_cache.admission_policy}")
            print(f"  Create Time: {anywhere_cache.create_time}")
            print(f"  Update Time: {anywhere_cache.update_time}")
    
        except google.api_core.exceptions.NotFound:
            print(
                f"Error: Anywhere Cache '{anywhere_cache_zone}' not found in bucket "
                f"'{bucket_name}'. "
                "Please ensure the Anywhere Cache ID and bucket name are correct."
            )
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    require "google/cloud/storage/control"
    
    # Retrieves an Anywhere Cache configuration for a given bucket.
    #
    # @param bucket_name [String] The name of the bucket.
    # @param anywhere_cache_id [String] A value that, along with the bucket's
    #   name, uniquely identifies the cache. (e.g. "us-east1-b")
    #
    # @example
    #   get_anywhere_cache(
    #     bucket_name: "your-unique-bucket-name",
    #     anywhere_cache_id: "us-east1-b"
    #   )
    #
    def get_anywhere_cache bucket_name:, anywhere_cache_id:
      # Create a client object. The client can be reused for multiple calls.
      storage_control_client = Google::Cloud::Storage::Control.storage_control
      # Set project to "_" to signify global bucket
      parent = "projects/_/buckets/#{bucket_name}"
      name = "#{parent}/anywhereCaches/#{anywhere_cache_id}"
    
      # Create a request.
      request = Google::Cloud::Storage::Control::V2::GetAnywhereCacheRequest.new(
        name: name
      )
      # The request retrieves the cache in the specified bucket.
      # The cache is identified by the specified ID.
      # The cache is in the specified bucket.
    
      begin
        result = storage_control_client.get_anywhere_cache request
        puts "Successfully fetched anywhereCache - #{result.name}."
      rescue Google::Cloud::Error => e
        puts "Failed to fetch AnywhereCache. Error: #{e.message}"
      end
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
