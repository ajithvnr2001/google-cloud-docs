---
url: https://docs.cloud.google.com/storage/docs/samples/storage-control-list-anywhere-caches/
title: Storage Control List Anywhere Caches \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:17:05.024075+00:00
---

# Storage Control List Anywhere Caches  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-control-list-anywhere-caches/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Storage Control List Anywhere Caches Stay organized with collections  Save and categorize content based on your preferences. 

Storage Control List Anywhere Caches

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create and manage Anywhere Cache caches](https://docs.cloud.google.com/storage/docs/rapid/use-rapid-cache)



## Code sample

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace storagecontrol = google::cloud::storagecontrol_v2;
    [](storagecontrol::StorageControlClient client,
       std::string const& bucket_name) {
      auto const parent = std::string{"projects/_/buckets/"} + bucket_name;
      for (auto anywhere_cache : client.ListAnywhereCaches(parent)) {
        if (!anywhere_cache) throw std::move(anywhere_cache).status();
        std::cout << anywhere_cache->name() << "\n";
      }
    }

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.storage.control.v2.[AnywhereCache](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.AnywhereCache.html);
    import com.google.storage.control.v2.[BucketName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.BucketName.html);
    import com.google.storage.control.v2.[ListAnywhereCachesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.ListAnywhereCachesRequest.html);
    import com.google.storage.control.v2.[StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html);
    import com.google.storage.control.v2.[StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html).[ListAnywhereCachesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.ListAnywhereCachesPagedResponse.html);
    import java.io.IOException;
    
    public final class AnywhereCacheList {
    
      public static void anywhereCacheList(String bucketName) throws IOException {
        try ([StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html) storageControl = [StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html).create()) {
    
          [ListAnywhereCachesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.ListAnywhereCachesRequest.html) request =
              [ListAnywhereCachesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.ListAnywhereCachesRequest.html).newBuilder()
                  .setParent([BucketName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.BucketName.html).format("_", bucketName))
                  .build();
    
          [ListAnywhereCachesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.ListAnywhereCachesPagedResponse.html) page = storageControl.listAnywhereCaches(request);
          for ([AnywhereCache](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.AnywhereCache.html) anywhereCache : page.iterateAll()) {
            System.out.println(anywhereCache.getName());
          }
        }
      }
    }

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    const {StorageControlClient} = require('[@google-cloud/storage-control](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/overview.html)');
    const {status} = require('@grpc/grpc-js');
    
    const client = new [StorageControlClient](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/storagecontrolclient.html)();
    
    /**
     * Lists all Anywhere Cache instances for a given bucket.
     *
     * Anywhere Cache provides a way to cache frequently accessed objects closer to
     * your applications, reducing latency and egress costs.
     *
     * @param {string} bucketName The name of the bucket to list Anywhere Caches for.
     */
    async function listAnywhereCaches(bucketName) {
      const parent = `projects/_/buckets/${bucketName}`;
    
      const request = {
        parent: parent,
      };
    
      try {
        const [anywhereCaches] = await client.listAnywhereCaches(request);
    
        if (anywhereCaches.length === 0) {
          console.log(`No Anywhere Caches found for bucket ${bucketName}.`);
          return;
        }
    
        console.log('Anywhere Caches:');
        for (const cache of anywhereCaches) {
          console.log(`- Name: ${cache.name}`);
          console.log(`  Zone: ${cache.zone}`);
          console.log(`  State: ${cache.state}`);
          console.log(`  TTL: ${cache.ttl ? cache.ttl.seconds + 's' : 'N/A'}`);
          console.log(`  Admission Policy: ${cache.admissionPolicy || 'N/A'}`);
          if (cache.createTime) {
            const createTime = new [Date](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.type.date.html)(
              cache.createTime.seconds * 1000 + cache.createTime.nanos / 1000000,
            );
            console.log(`  Create Time: ${createTime}`);
          }
        }
      } catch (err) {
        if (err.code === status.NOT_FOUND) {
          console.error(
            `Error: The specified bucket '${bucketName}' was not found.`,
          );
          console.error(
            'Please ensure the bucket exists and is accessible within the project.',
          );
        } else if (err.code === status.PERMISSION_DENIED) {
          console.error(
            `Error: Permission denied. Ensure the service account has the necessary permissions (e.g., storage.anywhereCaches.list) for bucket '${bucketName}'.`,
          );
        } else {
          console.error('Error listing Anywhere Caches:', err);
        }
      }
    }

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\Control\V2\Client\StorageControlClient;
    use Google\Cloud\Storage\Control\V2\ListAnywhereCachesRequest;
    
    /**
     * Lists Anywhere Cache instances for a given bucket.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     */
    function list_anywhere_caches(string $bucketName): void
    {
        $storageControlClient = new StorageControlClient();
    
        // Set project to "_" to signify global bucket
        $formattedName = $storageControlClient->bucketName('_', $bucketName);
    
        $request = new ListAnywhereCachesRequest([
            'parent' => $formattedName,
        ]);
    
        $response = $storageControlClient->listAnywhereCaches($request);
    
        foreach ($response as $anywhereCache) {
            printf('Anywhere cache name: %s' . PHP_EOL, $anywhereCache->getName());
        }
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import google.api_core.exceptions
    from google.cloud import [storage_control_v2](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest)
    
    
    def list_anywhere_caches(
        bucket_name: str,
    ) -> None:
        """Lists Anywhere Cache instances for a given bucket.
    
        Args:
            bucket_name: The name of the bucket to list Anywhere Caches for.
        """
        client = [storage_control_v2](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest).[StorageControlClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.services.storage_control.StorageControlClient.html)()
    
        parent = f"projects/_/buckets/{bucket_name}"
    
        try:
            anywhere_caches = client.[list_anywhere_caches](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.services.storage_control.StorageControlClient.html#google_cloud_storage_control_v2_services_storage_control_StorageControlClient_list_anywhere_caches)(parent=parent)
    
            found_caches = False
            print(f"Anywhere Caches for bucket '{bucket_name}':")
            for cache in anywhere_caches:
                found_caches = True
                print(f"  Name: {cache.name}")
                print(f"  Zone: {cache.zone}")
                print(f"  State: {cache.state}")
                print(f"  TTL: {cache.ttl.seconds} seconds")
                print(f"  Admission Policy: {cache.admission_policy}")
                print("----------------------------------------")
    
            if not found_caches:
                print("  No Anywhere Cache instances found for this bucket.")
    
        except google.api_core.exceptions.NotFound:
            print(f"Error: Bucket '{bucket_name}' not found.")
            print("Please ensure the bucket name is correct and the bucket exists.")
        except google.api_core.exceptions.PermissionDenied:
            print(
                f"Error: Permission denied to list Anywhere Caches for bucket '{bucket_name}'."
            )
            print(
                "Please ensure the authenticated service account has 'storage.anywhereCaches.list' permission."
            )
        except google.api_core.exceptions.GoogleAPIError as e:
            print(f"An unexpected API error occurred: {e}")
            print("Please check the error details and your project/bucket configuration.")
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    require "google/cloud/storage/control"
    
    def list_anywhere_caches bucket_name:
      # The Name of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      # Create a client object. The client can be reused for multiple calls.
      storage_control_client = Google::Cloud::Storage::Control.storage_control
      # Set project to "_" to signify global bucket
      parent = "projects/_/buckets/#{bucket_name}"
    
      # Create a request.
      request = Google::Cloud::Storage::Control::V2::ListAnywhereCachesRequest.new(
        parent: parent
      )
      # The request lists all caches in the specified bucket.
      # The caches are identified by the specified bucket name.
      begin
        result = storage_control_client.list_anywhere_caches request
        result.response.anywhere_caches.each do |item|
          puts "AnywhereCache #{item.name} found in list."
        end
      rescue Google::Cloud::Error => e
        puts "Failed to list AnywhereCaches. Error: #{e.message}"
      end
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
