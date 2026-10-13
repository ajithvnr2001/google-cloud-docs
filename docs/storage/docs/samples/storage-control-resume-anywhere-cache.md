---
url: https://docs.cloud.google.com/storage/docs/samples/storage-control-resume-anywhere-cache/
title: Storage Control Resume Anywhere Cache \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:13:44.365784+00:00
---

# Storage Control Resume Anywhere Cache  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-control-resume-anywhere-cache/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Storage Control Resume Anywhere Cache Stay organized with collections  Save and categorize content based on your preferences. 

Storage Control Resume Anywhere Cache

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
      auto anywhere_cache = client.ResumeAnywhereCache(cache_name);
      if (!anywhere_cache) throw std::move(anywhere_cache).status();
      std::cout << "Resumed anywhere cache: " << anywhere_cache->name() << "\n";
    }

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.storage.control.v2.[AnywhereCache](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.AnywhereCache.html);
    import com.google.storage.control.v2.[ResumeAnywhereCacheRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.ResumeAnywhereCacheRequest.html);
    import com.google.storage.control.v2.[StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html);
    import java.io.IOException;
    
    public final class AnywhereCacheResume {
    
      public static void anywhereCacheResume(String cacheName) throws IOException {
        try ([StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html) storageControl = [StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html).create()) {
    
          [ResumeAnywhereCacheRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.ResumeAnywhereCacheRequest.html) request =
              [ResumeAnywhereCacheRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.ResumeAnywhereCacheRequest.html).newBuilder().setName(cacheName).build();
    
          [AnywhereCache](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.AnywhereCache.html) anywhereCache = storageControl.resumeAnywhereCache(request);
    
          System.out.printf("Resumed anywhere cache: %s%n", anywhereCache.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.AnywhereCache.html#com_google_storage_control_v2_AnywhereCache_getName__)());
        }
      }
    }

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\Control\V2\Client\StorageControlClient;
    use Google\Cloud\Storage\Control\V2\ResumeAnywhereCacheRequest;
    
    /**
     * Resumes a disabled or paused Anywhere Cache instance.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $anywhereCacheId Uniquely identifies the cache.
     *        (e.g. 'us-east1-b')
     */
    function resume_anywhere_cache(string $bucketName, string $anywhereCacheId): void
    {
        $storageControlClient = new StorageControlClient();
    
        // Set project to "_" to signify global bucket
        $formattedName = $storageControlClient->anywhereCacheName('_', $bucketName, $anywhereCacheId);
    
        $request = new ResumeAnywhereCacheRequest([
            'name' => $formattedName
        ]);
    
        $response = $storageControlClient->resumeAnywhereCache($request);
    
        printf('Resumed anywhere cache: %s', $response->getName());
    }

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    require "google/cloud/storage/control"
    
    # Resumes a paused Anywhere Cache instance.
    #
    # This method sends a request to the Storage Control API to resume a
    # specific Anywhere Cache that was previously paused.
    #
    # @param bucket_name [String] The name of the bucket
    #   containing the cache.
    # @param anywhere_cache_id [String] The unique identifier for the Anywhere
    #   Cache instance within the bucket. For example: "us-east1-b".
    #
    # @example
    #   resume_anywhere_cache(
    #     bucket_name: "your-unique-bucket-name",
    #     anywhere_cache_id: "us-east1-b"
    #   )
    #
    def resume_anywhere_cache bucket_name:, anywhere_cache_id:
      # Create a client object. The client can be reused for multiple calls.
      storage_control_client = Google::Cloud::Storage::Control.storage_control
      # Set project to "_" to signify global bucket
      parent = "projects/_/buckets/#{bucket_name}"
      name = "#{parent}/anywhereCaches/#{anywhere_cache_id}"
    
      # Create a request.
      request = Google::Cloud::Storage::Control::V2::ResumeAnywhereCacheRequest.new(
        name: name
      )
      # The request resumes the cache, which was previously paused.
      # The cache is resumed in the specified bucket.
      # The cache is identified by the specified ID.
      begin
        result = storage_control_client.resume_anywhere_cache request
        puts "Successfully resumed anywhereCache - #{result.name}."
      rescue Google::Cloud::Error => e
        puts "Failed to resume AnywhereCache. Error: #{e.message}"
      end
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
