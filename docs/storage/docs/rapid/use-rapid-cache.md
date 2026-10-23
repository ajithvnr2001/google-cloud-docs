---
url: https://docs.cloud.google.com/storage/docs/rapid/use-rapid-cache/
title: Create and manage caches with Rapid Cache \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:36:36.520167+00:00
---

# Create and manage caches with Rapid Cache  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/rapid/use-rapid-cache/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Create and manage caches with Rapid Cache Stay organized with collections  Save and categorize content based on your preferences. 

**Important:** Anywhere Cache is now renamed Rapid Cache. When using Rapid Cache with certain tools, you might still see the name Anywhere Cache being referenced in the tool's interface or surface. 

You can create and manage cache instances with [Rapid Cache](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache) to reduce latency and optimize data access for objects stored in Cloud Storage. This caching solution helps improve the performance of your applications by accelerating data retrieval.

This page shows you how to create and manage cache instances with Rapid Cache. For information on how to use and manage long-running operations that get initiated from Rapid Cache [asynchronous cache operations](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache#cache-operations), see [Use long-running operations](https://docs.cloud.google.com/storage/docs/using-long-running-operations).

Before using Rapid Cache, review the [Limitations and restrictions](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache#limitations-restrictions).

## Before you begin

Before you begin creating and managing caches, complete the following sections.

### Get required roles

To get the permissions that you need to create and manage Rapid Cache caches, ask your administrator to grant you the [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) IAM role on the bucket for which you want to create caches. 

This predefined role contains the permissions required to create and manage Rapid Cache caches. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create and manage Rapid Cache caches:

  * `storage.anywhereCaches.create` (required for creating caches) 
  * `storage.anywhereCaches.disable` (required for disabling caches) 
  * `storage.anywhereCaches.get` (required for getting caches) 
  * `storage.anywhereCaches.list` (required for listing caches) 
  * `storage.anywhereCaches.resume` (required for resuming caches) 
  * `storage.anywhereCaches.update` (required for updating caches) 
  * `storage.managedFolders.create` (only required to enable the ingest-on-write behavior for a cache) 
  * `storage.managedFolders.update` (only required to update the ingest-on-write behavior of a cache) 



You can also get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

For information about granting roles on buckets, see [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).

In order to manage [long-running operations](https://google.aip.dev/151) that get initiated from Rapid Cache methods, you might need additional roles and permissions. See [required roles for long-running operations](https://docs.cloud.google.com/storage/docs/using-long-running-operations#required-roles) to learn more.

### Understand ingest-on-write settings

When you create or update a cache, you can optionally enable the cache to [ingest data the moment the data is written to the bucket](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache#ingest-on-write). This capability is known as "ingest-on-write". If you plan to enable ingest-on-write by using the JSON API, we recommend that you first understand the [behaviors of configured settings used for ingest-on-write](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache#ingest-on-write-requirements).

## Create a cache

### Console

**Create a cache for an existing bucket**

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket for which you want to cache data.

  3. On the **Bucket details** page, click the **Configuration** tab.

  4. In the **Rapid Cache** section, click **Configure cache**.

The **Configure cache** page appears for your bucket.

  5. In the **Cache regions** section, click the region that contains the zones in which you want to create a cache.

  6. In the **Cache zones** section, select the zones in which you want to create a cache. For each cache you create in a zone, optionally complete the following steps:

     * Optional: You can set a custom Time to Live (TTL) that determines when data gets evicted from the cache from its last read. By default, a cache's TTL is set to one day.

To set a custom TTL:

       1. In the **Time to live** column, specify a duration value (for example: `48`) and a unit of time (for example: `hours`).

       2. Click **Save configuration**.

     * Optional: You can enable the cache to ingest data on write in addition to ingesting data at first read. By default, caches are configured only to ingest data at first read.

To enable the cache to ingest data on write:

       1. In the **Ingestion criteria** column, click **Edit cache ingestion criteria** edit.

The **Set ingestion criteria** page appears.

       2. Select the **Ingest data on write** checkbox.

          * To enable ingest-on-write for all objects that are newly written to the bucket, click **Entire bucket**.

          * To enable ingest-on-write only for newly written objects that have a specific prefix in their name, click **Selected folders** , then enter the object name prefix. The object name prefix is also referred to as the "folder path".

You can enter multiple object name prefixes by clicking **Add** add.

To remove a prefix, click **Delete item** delete.

       3. Click **Done**.

  7. Click **Save configuration**.

  8. In the dialog that appears, click **Confirm**.

The **Operations** tab in the **Bucket details** page opens, which shows you the job status of your create cache operation.




**Create a cache for a new bucket**

To create a cache as part of creating a new bucket, follow the instructions in [Create a new bucket](https://docs.cloud.google.com/storage/docs/creating-buckets#create-bucket).

To view the status of a bucket's cache from the **Buckets list** page:

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click the **View Column** icon (view_column), select **Cache** , then click **OK**.




### Command line

Use the [`gcloud storage buckets anywhere-caches create`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/anywhere-caches/create) command:
    
    
    gcloud storage buckets anywhere-caches create gs://BUCKET_NAME CACHE_ZONE \
    [--ttl=TTL] [--enable-ingest-on-write]

Replace:

  * `BUCKET_NAME` with the name of the bucket for which you want to cache data. For example, `my-bucket`.

  * `CACHE_ZONE` with the zone in which the cache will run. For example, `us-east1-b`.

To create multiple caches at once, you can specify multiple zones. For example, `us-east1-b us-east1-c us-east1-d`.

  * `TTL` (optional) with the time to live (TTL) of the data in the cache. The value can be between 1 day and 7 days, inclusive. The value can be expressed in seconds, minutes, hours, and days. For example:

    * `86400s` for 86,400 seconds
    * `1440m` for 1,440 minutes
    * `24h` for 24 hours
    * `1d` for 1 day

If unspecified, defaults to `86400s` (1 day).




To configure the cache to ingest data the moment the data is written to the bucket, specify the optional `--enable-ingest-on-write` flag. This flag enables the cache to ingest all objects when they're written to the bucket.

If successful, the command returns the ID of the long-running operation associated with the AnywhereCache Create operation. You can [get details](https://docs.cloud.google.com/storage/docs/using-long-running-operations#get) about the long-running operation or [cancel](https://docs.cloud.google.com/storage/docs/using-long-running-operations#cancel) the long-running operation to stop the AnywhereCaches Create operation before it completes.

### Client libraries

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

### Rust
    
    
    use google_cloud_lro::Poller;
    use google_cloud_storage::client::StorageControl;
    use google_cloud_storage::model::AnywhereCache;
    
    pub async fn sample(client: &StorageControl, bucket_id: &str, zone: &str) -> anyhow::Result<()> {
        let cache = client
            .create_anywhere_cache()
            .set_parent(format!("projects/_/buckets/{bucket_id}"))
            .set_anywhere_cache(AnywhereCache::new().set_zone(zone).set_name(format!(
                "projects/_/buckets/{bucket_id}/anywhereCaches/{zone}"
            )))
            .poller()
            .until_done()
            .await?;
        println!("Created anywhere cache: {cache:?}");
        Ok(())
    }

### Terraform

See the [`google_storage_anywhere_cache` Terraform documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_anywhere_cache) for details on how to use Rapid Cache with Terraform.

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the following information:
         
         {
            "zone": "ZONE",
            "ttl": "TIME_TO_LIVE",
            "ingestOnWrite": INGEST_SETTING
         }

Replace:

     * `ZONE` with the zone in which the cache will run. For example, `us-east1-b`.

     * `TIME_TO_LIVE` with the time to live (TTL) of the data in the cache. The value must be expressed in seconds (for example: `172800s` for 172,800 seconds, which equates to 2 days).

The minimum value is `86400s` (1 day) and the maximum value is `604800s` (7 days). If unspecified, defaults to `86400s`.

     * `INGEST_SETTING` with `true` or `false` to specify whether or not the cache will ingest data on write.

If set to `true`, ingest-on-write is enabled for all objects that are written to the bucket. If set to `false`, ingest-on-write can be enabled selectively for objects that are written under a prefix, or it can be disabled for the entire bucket.

To learn about the settings used to configure the enablement of ingest-on-write, see the [requirements for enabling ingest-on-write](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache#ingest-on-write-requirements).

To enable ingest-on-write at the bucket level or at the prefix level, or to disable ingest-on-write entirely, use one of the following sets of instructions.

### Enable ingest-on-write for the bucket

       1. To enable ingest-on-write for all objects written to the bucket, set the value of `INGEST_SETTINGS` to `true`.

       2. Complete your cache request by following step 3.

### Enable ingest-on-write selectively for objects under a prefix

       1. Set the value of `INGEST_SETTINGS` to `false`.

       2. Complete your cache request by following step 3.

       3. [Create a managed folder](https://docs.cloud.google.com/storage/docs/creating-managing-managed-folders#create) that uses the prefix as a name, if the managed folder doesn't already exist.

       4. Send a managed folder `PATCH` request that includes a `rapidCacheConfig` configuration. Set field values in the configuration by using the guidance in [Understanding how to use ingest-on-write](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache#ingest-on-write-requirements).

For detailed instructions on how to use a `rapidCacheConfig` configuration, see [Update ingest-on-write on a managed folder](https://docs.cloud.google.com/storage/docs/creating-managing-managed-folders#enable-disable-ingest-on-write).

### Create a cache without enabling ingest-on-write

       1. Set the value of `INGEST_SETTINGS` to `false`.

       2. Complete your cache request by following step 3.

  3. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [request to create a cache](https://docs.cloud.google.com/storage/docs/json_api/v1/AnywhereCaches/create):
         
         curl -X POST --data-binary @JSON_FILE_NAME \
             -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             -H "Content-Type: application/json" \
             "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/anywhereCaches"

Replace:

     * `JSON_FILE_NAME` with the name of the JSON file you created in Step 2.

     * `BUCKET_NAME` with the name of the bucket for which you want to cache data. For example, `my-bucket`.




If successful, the operation returns a `google.longrunning.Operation`. You can [get details](https://docs.cloud.google.com/storage/docs/using-long-running-operations#get) about the long-running operation or [cancel](https://docs.cloud.google.com/storage/docs/using-long-running-operations#cancel) the long-running operation to stop the AnywhereCaches Create operation before it completes.

## View a cache

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket associated with the cache you want to view.

  3. On the **Bucket details** page, click the **Configuration** tab.

  4. In the **Rapid Cache** section, click edit **Edit** next to the **Cache** field.

  5. In the **Edit configuration** page that appears, select a region to view all the caches within the region's zones.

In the **Cache zones** pane, you can then view details about each available cache.




### Command line

Use the [`gcloud storage buckets anywhere-caches describe`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/anywhere-caches/describe) command:
    
    
    gcloud storage buckets anywhere-caches describe CACHE_ID

Replace:

  * `CACHE_ID` with the identifier of the cache instance, formulated as `BUCKET_NAME/CACHE_ZONE`. For example, `my-bucket/us-east1-b`.



Use the optional `raw` flag to output a raw API response instead of a standardized API response.

If successful, the command returns an [AnywhereCache resource](https://docs.cloud.google.com/storage/docs/json_api/v1/AnywhereCache).

### Client libraries

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

### Rust
    
    
    use google_cloud_storage::client::StorageControl;
    
    pub async fn sample(
        client: &StorageControl,
        bucket_id: &str,
        cache_id: &str,
    ) -> anyhow::Result<()> {
        let cache = client
            .get_anywhere_cache()
            .set_name(format!(
                "projects/_/buckets/{bucket_id}/anywhereCaches/{cache_id}"
            ))
            .send()
            .await?;
        println!("Got anywhere cache: {:?}", cache);
        Ok(())
    }

### Terraform

See the [`google_storage_anywhere_cache` Terraform documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_anywhere_cache) for details on how to use Rapid Cache with Terraform.

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [request to get a cache](https://docs.cloud.google.com/storage/docs/json_api/v1/AnywhereCaches/get):
         
         curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/anywhereCaches/RAPID_CACHE_ID"

Replace:

     * `BUCKET_NAME` with the name of the bucket associated with the cache you want to retrieve. For example, `my-bucket`.

     * `RAPID_CACHE_ID` with the zone in which the cache is located. For example, `us-east1-b`.




If successful, this operation returns an [AnywhereCache resource](https://docs.cloud.google.com/storage/docs/json_api/v1/AnywhereCache).

## List caches

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket associated with the caches you want to view.

  3. On the **Bucket details** page, click the **Configuration** tab.

  4. In the **Rapid Cache** section, click edit **Edit** next to the **Cache** field.

  5. In the **Edit configuration** page that appears, select a region to view all the caches within that region's zones.

All available caches for zones within the region appear in the **Cache zones** pane.




### Command line

Use the [`gcloud storage buckets anywhere-caches list`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/anywhere-caches/list) command:
    
    
    gcloud storage buckets anywhere-caches list gs://BUCKET_NAME

Replace:

  * `BUCKET_NAME` with the name of the bucket associated with the caches you want to list. For example, `my-bucket`.



If successful, the command returns a list of [AnywhereCache resources](https://docs.cloud.google.com/storage/docs/json_api/v1/AnywhereCache).

You can optionally use the `--raw` flag to return a raw API response instead of a standardized response. For more information about controlling listing behaviors, such as paginating results, see the [`gcloud storage ls` documentation](https://docs.cloud.google.com/sdk/gcloud/reference/storage/ls).

### Client libraries

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

### Rust
    
    
    use google_cloud_gax::paginator::ItemPaginator;
    use google_cloud_storage::client::StorageControl;
    
    pub async fn sample(client: &StorageControl, bucket_id: &str) -> anyhow::Result<()> {
        let mut stream = client
            .list_anywhere_caches()
            .set_parent(format!("projects/_/buckets/{}", bucket_id))
            .by_item();
        while let Some(cache) = stream.next().await {
            println!("Found cache: {:?}", cache?);
        }
        Ok(())
    }

### Terraform

See the [`google_storage_anywhere_cache` Terraform documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_anywhere_cache) for details on how to use Rapid Cache with Terraform.

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [request to list caches](https://docs.cloud.google.com/storage/docs/json_api/v1/AnywhereCaches/list):
         
         curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/anywhereCaches"

Replace:

     * `BUCKET_NAME` with the name of the bucket associated with the caches you want to retrieve. For example, `my-bucket`.

When listing multiple caches, you can [paginate results](https://docs.cloud.google.com/storage/docs/paginate-results).




If successful, this operation returns a list of [AnywhereCache resources](https://docs.cloud.google.com/storage/docs/json_api/v1/AnywhereCache). For details on the structure of this response, see the [response in the AnywhereCaches List documentation](https://docs.cloud.google.com/storage/docs/json_api/v1/AnywhereCaches/list).

## Update a cache

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket associated with the cache you want to update.

  3. On the **Bucket details** page, click the **Configuration** tab.

  4. In the **Rapid Cache** section, click edit **Manage caches**.

  5. In the **Manage caches** pane, click edit **Edit or create caches**.

  6. In the **Edit configuration** page that appears, update the properties of the cache:

     * To update the TTL of the cache, locate the **Time to live** column, then specify a time duration and select a time unit (for example, **minutes**).

     * To configure the ingest-on-write behavior of the cache, including whether all objects written are cached or only selective objects written under a prefix are cached:

       1. Locate the **Ingestion criteria** column, then click edit **Edit cache ingestion criteria**.

       2. In the **Set ingestion criteria** pane:

       * To enable or disable ingest-on-write, select or clear the **Ingest data on write** checkbox, then click **Done**.

       * To update the cache to ingest all objects in the bucket on write, make sure the **Ingest data on write** checkbox is selected, then select **Entire bucket**. Then, click **Done**.

       * To update the cache to ingest only objects that contain a specified prefix in their name, make sure the **Ingest data on write** checkbox is selected, then select **Selected folders**.

         * To specify a prefix, enter one or multiple prefixes in the folder path field, then click **Done**.

         * To remove a prefix, click **Delete item** delete next to the prefix.

  7. In the **Edit configuration** page, click **Save**.

  8. In the dialog that appears, click **Confirm**.




### Command line

Use the [`gcloud storage buckets anywhere-caches update`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/anywhere-caches/update) command:
    
    
    gcloud storage buckets anywhere-caches update CACHE_ID \
    [--ttl=TTL] [--[no-]enable-ingest-on-write]

Replace:

  * `CACHE_ID` with the identifier of the cache instance, formulated as `BUCKET_NAME/CACHE_ZONE`. For example, `my-bucket/us-east1-b`.

To update multiple caches at once, you can specify multiple identifiers. For example, `my-bucket/us-east1-b my-bucket/us-east1-c`.

  * `TTL` (optional) with the time to live (TTL) of the data in the cache. The value can be between 1 day and 7 days, inclusive. The value can be expressed in seconds, minutes, hours, and days. For example:

    * `86400s` for 86,400 seconds
    * `1440m` for 1,440 minutes
    * `24h` for 24 hours
    * `1d` for 1 day



To configure the cache to ingest data the moment the data is written to the bucket, specify the `--enable-ingest-on-write` flag. This flag enables the cache to ingest all objects when they're written to the bucket. To disable the cache from ingesting data on write, specify the `--no-enable-ingest-on-write` flag.

If successful, the command returns the ID of the raw long-running operation associated with the AnywhereCache Update operation. You can [get details](https://docs.cloud.google.com/storage/docs/using-long-running-operations#get) about the long-running operation.

### Client libraries

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

### Rust
    
    
    use google_cloud_lro::Poller;
    use google_cloud_storage::client::StorageControl;
    use google_cloud_storage::model::AnywhereCache;
    use google_cloud_wkt::FieldMask;
    
    pub async fn sample(
        client: &StorageControl,
        bucket_id: &str,
        cache_id: &str,
    ) -> anyhow::Result<()> {
        let anywhere_cache = AnywhereCache::new()
            .set_name(format!(
                "projects/_/buckets/{}/anywhereCaches/{}",
                bucket_id, cache_id
            ))
            .set_admission_policy("ADMIT_ON_SECOND_MISS".to_string());
        let operation = client
            .update_anywhere_cache()
            .set_anywhere_cache(anywhere_cache)
            .set_update_mask(FieldMask::default().set_paths(["admission_policy"]))
            .poller()
            .until_done()
            .await?;
        println!("Updated anywhere cache: {:?}", operation);
        Ok(())
    }

### Terraform

See the [`google_storage_anywhere_cache` Terraform documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_anywhere_cache) for details on how to use Rapid Cache with Terraform.

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that includes changes to the cache properties you want to update.
         
         {
            "ttl": "TIME_TO_LIVE",
            "ingestOnWrite": INGEST_SETTING
         }

Replace:

     * `TIME_TO_LIVE` with the TTL of the data in the cache. The value can be between 1 day and 7 days, inclusive. The value can be expressed in seconds, minutes, hours, and days. For example:

       * `86400s` for 86,400 seconds
       * `1440m` for 1,440 minutes
       * `24h` for 24 hours
       * `1d` for 1 day
     * `INGEST_SETTING` with `true` or `false` to specify whether or not the cache ingests data on write.

If set to `true`, ingest-on-write is enabled for all objects that are written to the bucket. If set to `false`, ingest-on-write can be enabled selectively for objects that are written under a prefix, or it can be disabled entirely.

To learn about the settings used to configure the enablement of ingest-on-write at the bucket or prefix level, see [Understanding how to enable ingest-on-write](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache#ingest-on-write-requirements).

To enable ingest-on-write at the bucket level or at the prefix level, or to disable ingest-on-write entirely, use one of the following sets of instructions.

### Enable ingest-on-write for the bucket

       1. To enable ingest-on-write for all objects written to the bucket, set the value of `INGEST_SETTINGS` to `true`.

       2. Complete your cache request by following step 3.

       3. If ingest-on-write was previously enabled for a prefix, a managed folder with a `rapidCacheConfig` configuration exists. Make a managed folder `PATCH` request that sets the `policies` map in the `rapidCacheConfig` configuration to `null`.

For detailed instructions on how to use a `rapidCacheConfig` configuration, see [Update ingest-on-write on a managed folder](https://docs.cloud.google.com/storage/docs/creating-managing-managed-folders#enable-disable-ingest-on-write).

### Enable ingest-on-write selectively for objects under a prefix

       1. Set the value of `INGEST_SETTINGS` to `false`.

       2. Complete your cache request by following step 3.

       3. [Create a managed folder](https://docs.cloud.google.com/storage/docs/creating-managing-managed-folders#create) that uses the prefix as a name, if the managed folder doesn't already exist.

       4. Send a managed folder `PATCH` request that includes a `rapidCacheConfig` configuration. Set field values in the configuration by using the guidance in the [ingest-on-write settings and behaviors](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache#ingest-on-write-requirements).

The `policies` map of a `rapidCacheConfig` configuration can contain one or multiple cache IDs (for example, `us-east1-a` and `us-east1-b`). To enable ingest-on-write for certain caches, set the individual cache's `ingestOnWrite` setting to `enabled`. To disable ingest-on-write for certain caches, set the individual cache's `ingestOnWrite` setting to `unspecified`. Carefully read about [ingest-on-write inheritance](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache#ingest-on-write-inheritance) to understand how a cache's ingest-on-write policy can be affected when the `ingestOnWrite` setting for the cache is set to `unspecified`.

For detailed instructions on how to use a `rapidCacheConfig` configuration, see [Update ingest-on-write on a managed folder](https://docs.cloud.google.com/storage/docs/creating-managing-managed-folders#enable-disable-ingest-on-write).

### Disable ingest-on-write

       1. Set the value of `INGEST_SETTINGS` to `false`. This setting disables ingest-on-write at the bucket level.

       2. Complete your cache request by following step 3.

       3. To disable ingest-on-write at the prefix level, locate the managed folder where prefix-level ingest-on-write is configured. Make a managed folder `PATCH` request that sets the `policies` map in the `rapidCacheConfig` configuration to `null`. Alternatively, delete the `rapidCacheConfig` configuration from the managed folder resource in a `PATCH` request.

For detailed instructions on how to use a `rapidCacheConfig` configuration, see [Update ingest-on-write on a managed folder](https://docs.cloud.google.com/storage/docs/creating-managing-managed-folders#enable-disable-ingest-on-write).

The following example updates the cache's TTL to 2 days and enables ingest-on-write for all objects written to the bucket:
    
    {
       "ttl": "172800s",
       "ingestOnWrite": true
    }

  3. To apply the new properties, use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [request to update the cache](https://docs.cloud.google.com/storage/docs/json_api/v1/AnywhereCaches/update):
         
         curl -X PATCH --data-binary @JSON_FILE_NAME \
             -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             -H "Content-Type: application/json" \
             "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/anywhereCaches/RAPID_CACHE_ID"

Replace:

     * `JSON_FILE_NAME` with the name of the JSON file you created in Step 2.

     * `BUCKET_NAME` with the name of the bucket associated with the cache you want to update. For example, `my-bucket`.

     * `RAPID_CACHE_ID` with the identifier of the cache. For example, `us-east1-b`.




If successful, the operation returns a `google.longrunning.Operation`. You can [get details](https://docs.cloud.google.com/storage/docs/using-long-running-operations#get) about the long-running operation.

## Resume a cache

### Console

To resume a cache that's been paused or disabled, complete the following instructions:

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket associated with the cache you want to resume.

  3. On the **Bucket details** page, click the **Configuration** tab.

  4. In the **Rapid Cache** section, click edit **Manage caches**.

  5. In the **Manage caches** pane, click the **Resume cache** icon (play_arrow).

  6. Click **Close**.




### Command line

Use the [`gcloud storage buckets anywhere-caches resume`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/anywhere-caches/resume) command:
    
    
    gcloud storage buckets anywhere-caches resume CACHE_ID

Replace:

  * `CACHE_ID` with the identifier of the cache instance, formulated as `BUCKET_NAME/CACHE_ZONE`. For example, `my-bucket/us-east1-b`.

To resume multiple caches at once, you can specify multiple identifiers. For example, `my-bucket/us-east1-b my-bucket/us-east1-c`.




If successful, the command returns a formatted [AnywhereCache resource](https://docs.cloud.google.com/storage/docs/json_api/v1/AnywhereCache).

### Client libraries

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

### Rust
    
    
    use google_cloud_storage::client::StorageControl;
    
    pub async fn sample(
        client: &StorageControl,
        bucket_id: &str,
        cache_id: &str,
    ) -> anyhow::Result<()> {
        let cache = client
            .resume_anywhere_cache()
            .set_name(format!(
                "projects/_/buckets/{}/anywhereCaches/{}",
                bucket_id, cache_id
            ))
            .send()
            .await?;
        println!("Resumed anywhere cache: {:?}", cache);
        Ok(())
    }

### Terraform

See the [`google_storage_anywhere_cache` Terraform documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_anywhere_cache) for details on how to use Rapid Cache with Terraform.

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [request to resume a cache](https://docs.cloud.google.com/storage/docs/json_api/v1/AnywhereCaches/resume):
         
         curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/anywhereCaches/RAPID_CACHE_ID/resume"

Replace:

     * `BUCKET_NAME` with the name of the bucket associated with the cache you want to resume. For example, `my-bucket`.

     * `RAPID_CACHE_ID` with the identifier of the cache. For example, `us-east1-b`.




If successful, the operation returns a formatted [AnywhereCache resource](https://docs.cloud.google.com/storage/docs/json_api/v1/AnywhereCache).

## Disable a cache

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket associated with the cache you want to disable.

  3. On the **Bucket details** page, click the **Configuration** tab.

  4. In the **Rapid Cache** section, click edit **Manage caches**.

  5. In the **Manage caches** pane, click the **Disable cache** icon (delete).

  6. In the dialog that appears, click **Confirm**.

  7. Click **Close**.




### Command line

Use the [`gcloud storage buckets anywhere-caches disable`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/anywhere-caches/disable) command:
    
    
    gcloud storage buckets anywhere-caches disable CACHE_ID

Replace:

  * `CACHE_ID` with the identifier of the cache instance, formulated as `BUCKET_NAME/CACHE_ZONE`. For example, `my-bucket/us-east1-b`.

To disable multiple caches at once, you can specify multiple identifiers. For example, `my-bucket/us-east1-b my-bucket/us-east1-c`.




If successful, the command returns a formatted [AnywhereCache resource](https://docs.cloud.google.com/storage/docs/json_api/v1/AnywhereCache).

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace storagecontrol = google::cloud::storagecontrol_v2;
    [](storagecontrol::StorageControlClient client,
       std::string const& cache_name) {
      auto anywhere_cache = client.DisableAnywhereCache(cache_name);
      if (!anywhere_cache) throw std::move(anywhere_cache).status();
      std::cout << "Disabled anywhere cache: " << anywhere_cache->name() << "\n";
    }

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.storage.control.v2.[AnywhereCache](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.AnywhereCache.html);
    import com.google.storage.control.v2.[DisableAnywhereCacheRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.DisableAnywhereCacheRequest.html);
    import com.google.storage.control.v2.[StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html);
    import java.io.IOException;
    
    public final class AnywhereCacheDisable {
    
      public static void anywhereCacheDisable(String cacheName) throws IOException {
        try ([StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html) storageControl = [StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html).create()) {
    
          [DisableAnywhereCacheRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.DisableAnywhereCacheRequest.html) request =
              [DisableAnywhereCacheRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.DisableAnywhereCacheRequest.html).newBuilder().setName(cacheName).build();
    
          [AnywhereCache](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.AnywhereCache.html) anywhereCache = storageControl.disableAnywhereCache(request);
    
          System.out.printf("Disabled anywhere cache: %s%n", anywhereCache.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.AnywhereCache.html#com_google_storage_control_v2_AnywhereCache_getName__)());
        }
      }
    }

### Rust
    
    
    use google_cloud_storage::client::StorageControl;
    
    pub async fn sample(
        client: &StorageControl,
        bucket_id: &str,
        cache_id: &str,
    ) -> anyhow::Result<()> {
        let cache = client
            .disable_anywhere_cache()
            .set_name(format!(
                "projects/_/buckets/{}/anywhereCaches/{}",
                bucket_id, cache_id
            ))
            .send()
            .await?;
        println!("Disabled anywhere cache: {:?}", cache);
        Ok(())
    }

### Terraform

See the [`google_storage_anywhere_cache` Terraform documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_anywhere_cache) for details on how to use Rapid Cache with Terraform.

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [request to disable a cache](https://docs.cloud.google.com/storage/docs/json_api/v1/AnywhereCaches/disable):
         
         curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/anywhereCaches/RAPID_CACHE_ID/disable"

Replace:

     * `BUCKET_NAME` with the name of the bucket associated with the cache you want to disable. For example, `my-bucket`.

     * `RAPID_CACHE_ID` with the identifier of the cache. For example, `us-east1-b`.




If successful, the command returns a formatted [AnywhereCache resource](https://docs.cloud.google.com/storage/docs/json_api/v1/AnywhereCache).

## Monitor cache performance

The Cloud Storage portion of the Google Cloud console provides monitoring charts that let you track the performance of your caches using metrics. These monitoring charts can also be viewed using [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview).

### Available charts

Chart | Resource hierarchy level | Description  
---|---|---  
**Byte eviction rate** | Bucket | The rate of bytes evicted from the cache, sampled every hour. This data is refreshed more than once an hour to allow time for post processing the data.  
**Byte eviction rate** | Project | The rate of bytes evicted from all the caches of a bucket, sampled every hour. This data is refreshed more than once an hour to allow time for post processing the data.  
**Bytes in cache** | Bucket | The number of the bytes in the cache, sampled every hour. This data is refreshed more than once an hour to allow time for post processing the data.  
**Bytes in cache** | Project | The number of bytes in all the caches of a bucket, sampled every hour. This data is refreshed more than once an hour to allow time for post processing the data.  
**Cache throughput benefit** | Project | The rate of the data transfer bandwidth quota for the region, dual-region, or multi-region, usage of the quota, and extra throughput served by the cache. The extra throughput served by the cache doesn't count towards the quota, therefore, using the cache enables projects to exceed the throughput allowed by the quota.  
**Hit rate operations** | Bucket | The percentage of cache operations serving the requested data from the cache relative to the total cache eligible operations, sampled every 60 seconds. If a read is completely returned from cache the operation counts as a hit. If the read is not returned from the cache or only partially returned from the cache, the operation counts as a miss.  
**Hit rate operations** | Project | The percentage of cache operations serving the requested data from all caches for a bucket relative to the total cache eligible operations, sampled 60 seconds. If a read is completely returned from cache, the operation counts as a hit. If the read is not returned from the cache or only partially returned from the cache, the operation counts as a miss.  
**Hit rate bytes** | Bucket | The percentage of bytes that are served from the cache relative to the total cache eligible bytes, sampled every 60 seconds.  
**Hit rate bytes** | Project | The percentage of bytes that are served from all caches for a bucket relative to the total cache eligible bytes, sampled every 60 seconds.  
**Ingestion rate raw bytes** | Bucket | The rate of raw bytes ingested into each cache, sampled every 60 seconds. All ingested bytes, including non-billable bytes, are used in calculating the value of this metric. This metric is reported in real time.  
**Ingestion rate raw bytes** | Project | The rate of raw bytes ingested into all the caches of a bucket, sampled every 60 seconds. All ingested bytes, including non-billable bytes, are used in calculating the value of this metric. This metric is reported in real time.  
**Throughput - Cache hit** | Bucket | The throughput served from the cache, sampled every 60 seconds.  
**Throughput - Cache hit** | Project | The throughput served from all caches for a bucket, sampled every 60 seconds.  
**Throughput - Cache miss** | Bucket | The throughput that's not served from the cache, sampled every 60 seconds.  
**Throughput - Cache miss** | Project | The throughput that's not served from any of the caches of a bucket, sampled every 60 seconds.  
  
### Access charts

Monitoring charts capture data either for individual buckets or for all buckets within a project. The resource hierarchy level that a chart captures determines where you can access the chart.

#### Access bucket-level charts

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket for which you want to see monitoring charts.

  3. In the **Bucket details** page, click the **Observability** tab.

  4. In the navigation menu, select **Rapid Cache**.

Monitoring charts are displayed.




#### Access project-level charts

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the **Cloud Storage** navigation pane, click **Monitoring**.

  3. In the menu bar, click **Rapid Cache**.

Monitoring charts are displayed.




## Use long-running operations

When successfully run, the [AnywhereCaches Create](https://docs.cloud.google.com/storage/docs/json_api/v1/AnywhereCaches/create) and [Update](https://docs.cloud.google.com/storage/docs/json_api/v1/AnywhereCaches/update) operations initiate a [long-running operation](https://google.aip.dev/151). You can get and list long-running operations in order to view the details and status of the underlying AnywhereCaches operation, or cancel a long-running operation in order to cancel the underlying AnywhereCaches operation while it's in progress.

**Note:** You can only cancel long-running operations that get initiated from AnywhereCaches Create operations. AnywhereCaches Update operations initiate long-running operations that can be viewed and listed, but cannot be cancelled.

For instructions on using long-running operations for Rapid Cache, see [Use long-running operations](https://docs.cloud.google.com/storage/docs/using-long-running-operations).

The following example shows a long-running operation that's initiated from an AnywhereCaches Create operation:
    
    
    done: false
    kind: storage#operation
    metadata:
      '@type': type.googleapis.com/google.storage.control.v2.CreateAnywhereCacheMetadata
      anywhereCacheId: us-central1-c
      zone: us-central1-c
      ttl: 172800s
      commonMetadata:
        createTime: '2023-12-14T20:52:00.032Z'
        progressPercent: -1
        requestedCancellation: false
        type: create-anywhere-cache
        updateTime: '2023-12-14T20:52:00.032Z'
    name: projects/_/buckets/my-bucket/operations/AULf_KhQxxsWRSn56wv4jfmn3pOu_dKTz9FoYx6S0EzMw5ssR0cXIiorCvHRwqxZnQmWj9jnGpKb3Y6iCD3XM9KLc8EHBm7uig
    selfLink: https://www.googleapis.com/storage/v1/b/my-bucket/operations/AULf_KhQxxsWRSn56wv4jfmn3pOu_dKTz9FoYx6S0EzMw5ssR0cXIiorCvHRwqxZnQmWj9jnGpKb3Y6iCD3XM9KLc8EHBm7uig

## Retries

Asynchronous AnywhereCaches APIs are [idempotent](https://docs.cloud.google.com/storage/docs/retry-strategy#idempotency) by default. This means that you can safely retry asynchronous AnywhereCaches API calls without concern about modifying resources unintentionally.

For example, say you perform an AnywhereCaches Create operation to create a cache in `us-central1-a`, which succeeds. If you perform a subsequent AnywhereCaches Create operation using the same zone that succeeds, the request returns the same long-running operation as the previous request. Note that this behavior only occurs if you include a `request_id` as part of your create cache request. If a `request_id` isn't included, you get an `ANYWHERE_CACHE_ALREADY_EXISTS` error when attempting to create a cache that already exists. For information about how to include a `request_id`, see [Request identification](https://google.aip.dev/155).

## What's next

Get [recommendations](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache-recommender) about which buckets and zones to create a cache for.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
