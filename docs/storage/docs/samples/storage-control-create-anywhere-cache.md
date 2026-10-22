---
url: https://docs.cloud.google.com/storage/docs/samples/storage-control-create-anywhere-cache/
title: Storage Control Create Anywhere Cache \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:31:33.505701+00:00
---

# Storage Control Create Anywhere Cache  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-control-create-anywhere-cache/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Storage Control Create Anywhere Cache Stay organized with collections  Save and categorize content based on your preferences. 

Storage Control Create Anywhere Cache

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create and manage Anywhere Cache caches](https://docs.cloud.google.com/storage/docs/rapid/use-rapid-cache)



## Code sample

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace storagecontrol = google::cloud::storagecontrol_v2;
    [](storagecontrol::StorageControlClient client,
       std::string const& bucket_name, std::string const& cache_name,
       std::string const& zone_name) {
      google::storage::control::v2::AnywhereCache cache;
      cache.set_name(cache_name);
      cache.set_zone(zone_name);
    
      google::storage::control::v2::CreateAnywhereCacheRequest request;
      request.set_parent(std::string{"projects/_/buckets/"} + bucket_name);
      *request.mutable_anywhere_cache() = cache;
    
      // Start a create operation and block until it completes. Real applications
      // may want to setup a callback, wait on a coroutine, or poll until it
      // completes.
      auto anywhere_cache = client.CreateAnywhereCache(request).get();
      if (!anywhere_cache) throw std::move(anywhere_cache).status();
      std::cout << "Created anywhere cache: " << anywhere_cache->name() << "\n";
    }

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.storage.control.v2.[AnywhereCache](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.AnywhereCache.html);
    import com.google.storage.control.v2.[BucketName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.BucketName.html);
    import com.google.storage.control.v2.[CreateAnywhereCacheMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.CreateAnywhereCacheMetadata.html);
    import com.google.storage.control.v2.[CreateAnywhereCacheRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.CreateAnywhereCacheRequest.html);
    import com.google.storage.control.v2.[StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    
    public final class AnywhereCacheCreate {
    
      public static void anywhereCacheCreate(String bucketName, String cacheName, String zoneName)
          throws InterruptedException, ExecutionException, IOException {
        try ([StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html) storageControl = [StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html).create()) {
    
          [CreateAnywhereCacheRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.CreateAnywhereCacheRequest.html) request =
              [CreateAnywhereCacheRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.CreateAnywhereCacheRequest.html).newBuilder()
                  // Set project to "_" to signify globally scoped bucket
                  .setParent([BucketName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.BucketName.html).format("_", bucketName))
                  .setAnywhereCache(
                      [AnywhereCache](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.AnywhereCache.html).newBuilder().setName(cacheName).setZone(zoneName).build())
                  .build();
    
          // Start a long-running operation (LRO).
          OperationFuture<AnywhereCache, CreateAnywhereCacheMetadata> operation =
              storageControl.[createAnywhereCacheAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html#com_google_storage_control_v2_StorageControlClient_createAnywhereCacheAsync__org_jspecify_annotations_Nullable_com_google_storage_control_v2_BucketName_com_google_storage_control_v2_AnywhereCache_)(request);
    
          // Await the LROs completion.
          [AnywhereCache](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.AnywhereCache.html) anywhereCache = operation.[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)();
          System.out.printf("Created anywhere cache: %s%n", anywhereCache.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.AnywhereCache.html#com_google_storage_control_v2_AnywhereCache_getName__)());
        }
      }
    }

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\Control\V2\AnywhereCache;
    use Google\Cloud\Storage\Control\V2\Client\StorageControlClient;
    use Google\Cloud\Storage\Control\V2\CreateAnywhereCacheRequest;
    
    /**
     * Creates an Anywhere Cache instance.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $zone The zone in which the cache instance is running.
     *        (e.g. 'us-east1-b')
     */
    function create_anywhere_cache(string $bucketName, string $zone): void
    {
        $storageControlClient = new StorageControlClient();
    
        // Set project to "_" to signify global bucket
        $formattedName = $storageControlClient->bucketName('_', $bucketName);
    
        $anywhereCache = new AnywhereCache([
            'zone' => $zone,
        ]);
    
        $request = new CreateAnywhereCacheRequest([
            'parent' => $formattedName,
            'anywhere_cache' => $anywhereCache,
        ]);
    
        // Start a create operation and block until it completes. Real applications
        // may want to setup a callback, wait on a coroutine, or poll until it
        // completes.
        $operation = $storageControlClient->createAnywhereCache($request);
    
        printf('Waiting for operation %s to complete...' . PHP_EOL, $operation->getName());
        $operation->pollUntilComplete([
            'totalPollTimeoutMillis' => 5400000,
            'initialPollDelayMillis' => 1000, // Start with 1 second delay
            'pollDelayMultiplier' => 2,      // Double delay each time
            'maxPollDelayMillis' => 60000,   // Max 60 seconds delay between polls
        ]);
    
        /** @var AnywhereCache $anywhereCacheResult */
        $anywhereCacheResult = $operation->getResult();
        printf('Created anywhere cache: %s' . PHP_EOL, $anywhereCacheResult->getName());
    }

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    require "google/cloud/storage/control"
    
    # Creates a new Anywhere Cache for a specified bucket and waits for it
    # to become active.
    #
    # This method initiates the creation of an Anywhere Cache in the given zone for
    # the specified bucket. After sending the creation request, it polls the status
    # of the cache with an exponential backoff strategy until the cache's state is
    # "running". Progress and final status are printed to the console.
    #
    # @param bucket_name [String] The name of the bucket.
    # @param zone [String] The zone where the Anywhere Cache instance should be
    #   located (e.g., "us-east1-b").
    #
    # @example
    #   create_anywhere_cache(
    #     bucket_name: "your-unique-bucket-name",
    #     zone: "us-east1-b"
    #   )
    #
    def create_anywhere_cache bucket_name:, zone:
      # Create a client object. The client can be reused for multiple calls.
      storage_control_client = Google::Cloud::Storage::Control.storage_control
      # Set project to "_" to signify global bucket
      parent = "projects/_/buckets/#{bucket_name}"
      name = "#{parent}/anywhereCaches/#{zone}"
    
      anywhere_cache = Google::Cloud::Storage::Control::V2::AnywhereCache.new(
        name: name,
        zone: zone
      )
      # Create a request.
      request = Google::Cloud::Storage::Control::V2::CreateAnywhereCacheRequest.new(
        parent: parent,
        anywhere_cache: anywhere_cache
      )
      # The request creates a new cache in the specified zone.
      # The cache is created in the specified bucket.
      begin
        operation = storage_control_client.create_anywhere_cache request
        puts "AnywhereCache operation created - #{operation.name}"
        get_request = Google::Cloud::Storage::Control::V2::GetAnywhereCacheRequest.new(
          name: name
        )
        result = storage_control_client.get_anywhere_cache get_request
        min_delay = 30 # 30 seconds
        max_delay = 900 # 15 minutes
        while result.state&.downcase != "running"
          unless ["paused", "disabled", "creating"].include? result.state&.downcase
            raise Google::Cloud::Error,
                  "AnywhereCache operation failed on the backend with state #{result.state&.downcase}."
          end
          puts "Cache not running yet, current state is #{result.state&.downcase}. Retrying in #{min_delay} seconds."
          sleep min_delay
          min_delay = [min_delay * 2, max_delay].min # Exponential backoff with a max delay
          result = storage_control_client.get_anywhere_cache get_request
        end
        puts "Successfully created anywhereCache - #{result.name}."
      rescue Google::Cloud::Error => e
        puts "Failed to create AnywhereCache. Error: #{e.message}"
      end
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
