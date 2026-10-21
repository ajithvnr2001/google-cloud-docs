---
url: https://docs.cloud.google.com/storage/docs/samples/storage-control-update-anywhere-cache/
title: Storage Control Update Anywhere Cache \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:17:03.800498+00:00
---

# Storage Control Update Anywhere Cache  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-control-update-anywhere-cache/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Storage Control Update Anywhere Cache Stay organized with collections  Save and categorize content based on your preferences. 

Storage Control Update Anywhere Cache

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
      google::storage::control::v2::AnywhereCache cache;
      google::protobuf::FieldMask field_mask;
      field_mask.add_paths("ttl");
      cache.set_name(cache_name);
      cache.mutable_ttl()->set_seconds(86400);
      // Start an update operation and block until it completes. Real applications
      // may want to setup a callback, wait on a coroutine, or poll until it
      // completes.
      auto anywhere_cache = client.UpdateAnywhereCache(cache, field_mask).get();
      if (!anywhere_cache) throw std::move(anywhere_cache).status();
      std::cout << "Updated anywhere cache: " << anywhere_cache->name() << "\n";
    }

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import com.google.storage.control.v2.[AnywhereCache](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.AnywhereCache.html);
    import com.google.storage.control.v2.[StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html);
    import com.google.storage.control.v2.[UpdateAnywhereCacheMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.UpdateAnywhereCacheMetadata.html);
    import com.google.storage.control.v2.[UpdateAnywhereCacheRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.UpdateAnywhereCacheRequest.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    
    public final class AnywhereCacheUpdate {
    
      public static void anywhereCacheUpdate(String cacheName, String admissionPolicy)
          throws InterruptedException, ExecutionException, IOException {
        try ([StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html) storageControl = [StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html).create()) {
    
          [AnywhereCache](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.AnywhereCache.html) pendingUpdate =
              [AnywhereCache](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.AnywhereCache.html).newBuilder().setName(cacheName).setAdmissionPolicy(admissionPolicy).build();
    
          [UpdateAnywhereCacheRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.UpdateAnywhereCacheRequest.html) request =
              [UpdateAnywhereCacheRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.UpdateAnywhereCacheRequest.html).newBuilder()
                  .setAnywhereCache(pendingUpdate)
                  .setUpdateMask([FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("admission_policy").build())
                  .build();
    
          // Start a long-running operation (LRO).
          OperationFuture<AnywhereCache, UpdateAnywhereCacheMetadata> operation =
              storageControl.[updateAnywhereCacheAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html#com_google_storage_control_v2_StorageControlClient_updateAnywhereCacheAsync_com_google_storage_control_v2_AnywhereCache_com_google_protobuf_FieldMask_)(request);
    
          // Await the LROs completion.
          [AnywhereCache](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.AnywhereCache.html) updatedAnywhereCache = operation.get();
          System.out.printf("Updated anywhere cache: %s%n", updatedAnywhereCache.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.AnywhereCache.html#com_google_storage_control_v2_AnywhereCache_getName__)());
        }
      }
    }

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\Control\V2\AnywhereCache;
    use Google\Cloud\Storage\Control\V2\Client\StorageControlClient;
    use Google\Cloud\Storage\Control\V2\UpdateAnywhereCacheRequest;
    use Google\Protobuf\FieldMask;
    
    /**
     * Updates an Anywhere Cache instance.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $anywhereCacheId Uniquely identifies the cache.
     *        (e.g. 'us-east1-b')
     * @param string $admission_policy The cache's admission policy.
     *        (e.g. 'admit-on-first-miss')
     */
    function update_anywhere_cache(string $bucketName, string $anywhereCacheId, string $admission_policy): void
    {
        $storageControlClient = new StorageControlClient();
    
        // Set project to "_" to signify global bucket
        $formattedName = $storageControlClient->anywhereCacheName('_', $bucketName, $anywhereCacheId);
    
        $anywhereCache = new AnywhereCache([
            'name' => $formattedName,
            'admission_policy' => $admission_policy,
        ]);
    
        $updateMask = new FieldMask([
            'paths' => ['admission_policy'],
        ]);
    
        $request = new UpdateAnywhereCacheRequest([
            'anywhere_cache' => $anywhereCache,
            'update_mask' => $updateMask,
        ]);
    
        // Start an update operation. This returns an Operation object which can be polled.
        $operation = $storageControlClient->updateAnywhereCache($request);
    
        printf('Waiting for operation %s to complete...' . PHP_EOL, $operation->getName());
        $operation->pollUntilComplete([
            'totalPollTimeoutMillis' => 5400000,
            'initialPollDelayMillis' => 1000, // Start with 1 second delay
            'pollDelayMultiplier' => 2,      // Double delay each time
            'maxPollDelayMillis' => 60000,   // Max 60 seconds delay between polls
        ]);
    
        $anywhereCacheResult = $operation->getResult();
        printf('Updated anywhere cache: %s', $anywhereCacheResult->getName());
    }

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    require "google/cloud/storage/control"
    
    # Updates an existing Anywhere Cache for a specified
    # bucket. After initiating the update, it polls the cache's status with
    # exponential backoff until the cache state becomes "running".
    #
    # @param bucket_name [String] The name of the GCS bucket containing the cache.
    # @param anywhere_cache_id [String] The unique identifier for the Anywhere Cache.
    #   e.g. "us-east1-b"
    #
    # @example
    #   update_anywhere_cache(
    #     bucket_name: "your-unique-bucket-name",
    #     anywhere_cache_id: "us-east1-b"
    #   )
    #
    def update_anywhere_cache bucket_name:, anywhere_cache_id:
      # Create a client object. The client can be reused for multiple calls.
      storage_control_client = Google::Cloud::Storage::Control.storage_control
      # Set project to "_" to signify global bucket
      parent = "projects/_/buckets/#{bucket_name}"
      name = "#{parent}/anywhereCaches/#{anywhere_cache_id}"
      ttl_in_seconds = 7200
    
      anywhere_cache = Google::Cloud::Storage::Control::V2::AnywhereCache.new(
        name: name,
        ttl: ttl_in_seconds
      )
      mask = Google::Protobuf::[FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-binary_authorization-v1/latest/Google-Protobuf-FieldMask.html).new paths: ["ttl"]
      # Create a request.
      request = Google::Cloud::Storage::Control::V2::UpdateAnywhereCacheRequest.new(
        anywhere_cache: anywhere_cache,
        update_mask: mask
      )
      # The request updates the cache in the specified bucket.
      # The cache is identified by the specified ID.
      begin
        operation = storage_control_client.update_anywhere_cache request
        puts "AnywhereCache operation created - #{operation.name}"
        get_request = Google::Cloud::Storage::Control::V2::GetAnywhereCacheRequest.new(
          name: name
        )
        result = storage_control_client.get_anywhere_cache get_request
        min_delay = 30 # 30 seconds
        max_delay = 600 # 10 minutes
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
        puts "Successfully updated anywhereCache - #{result.name}."
      rescue Google::Cloud::Error => e
        puts "Failed to update AnywhereCache. Error: #{e.message}"
      end
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
