---
url: https://docs.cloud.google.com/storage/docs/samples/storage-transfer-manager-download-bucket/
title: Download all objects in a bucket \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:50.787053+00:00
---

# Download all objects in a bucket  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-transfer-manager-download-bucket/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Download all objects in a bucket Stay organized with collections  Save and categorize content based on your preferences. 

Use Transfer Manager to download all of the files in a bucket with concurrency.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Download objects](https://docs.cloud.google.com/storage/docs/downloading-objects)



## Code sample

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import com.google.cloud.storage.transfermanager.[DownloadResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.DownloadResult.html);
    import com.google.cloud.storage.transfermanager.[ParallelDownloadConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.ParallelDownloadConfig.html);
    import com.google.cloud.storage.transfermanager.[TransferManager](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManager.html);
    import com.google.cloud.storage.transfermanager.[TransferManagerConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html);
    import java.nio.file.Path;
    import java.util.List;
    import java.util.stream.Collectors;
    
    class DownloadBucket {
    
      public static void downloadBucketContents(
          String projectId, String bucketName, Path destinationDirectory) {
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().getService();
        List<BlobInfo> blobs =
            storage
                .list(bucketName)
                .streamAll()
                .map(blob -> blob.[asBlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html#com_google_cloud_storage_Blob_asBlobInfo__)())
                .collect(Collectors.toList());
        [TransferManager](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManager.html) transferManager = [TransferManagerConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html).newBuilder().build().getService();
        [ParallelDownloadConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.ParallelDownloadConfig.html) parallelDownloadConfig =
            [ParallelDownloadConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.ParallelDownloadConfig.html).newBuilder()
                .setBucketName(bucketName)
                .setDownloadDirectory(destinationDirectory)
                .build();
    
        List<DownloadResult> results =
            transferManager.[downloadBlobs](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManager.html#com_google_cloud_storage_transfermanager_TransferManager_downloadBlobs_java_util_List_com_google_cloud_storage_BlobInfo__com_google_cloud_storage_transfermanager_ParallelDownloadConfig_)(blobs, parallelDownloadConfig).getDownloadResults();
    
        for ([DownloadResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.DownloadResult.html) result : results) {
          System.out.println(
              "Download of "
                  + [result](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.spi.v1.StorageRpc.RewriteResponse.html#com_google_cloud_storage_spi_v1_StorageRpc_RewriteResponse_result).getInput().getName()
                  + " completed with status "
                  + [result](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.spi.v1.StorageRpc.RewriteResponse.html#com_google_cloud_storage_spi_v1_StorageRpc_RewriteResponse_result).getStatus());
        }
      }
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def download_bucket_with_transfer_manager(
        bucket_name, destination_directory="", workers=8, max_results=1000
    ):
        """Download all of the blobs in a bucket, concurrently in a process pool.
    
        The filename of each blob once downloaded is derived from the blob name and
        the `destination_directory `parameter. For complete control of the filename
        of each blob, use transfer_manager.download_many() instead.
    
        Directories will be created automatically as needed, for instance to
        accommodate blob names that include slashes.
        """
    
        # The ID of your GCS bucket
        # bucket_name = "your-bucket-name"
    
        # The directory on your computer to which to download all of the files. This
        # string is prepended (with os.path.join()) to the name of each blob to form
        # the full path. Relative paths and absolute paths are both accepted. An
        # empty string means "the current working directory". Note that this
        # parameter allows accepts directory traversal ("../" etc.) and is not
        # intended for unsanitized end user input.
        # destination_directory = ""
    
        # The maximum number of processes to use for the operation. The performance
        # impact of this value depends on the use case, but smaller files usually
        # benefit from a higher number of processes. Each additional process occupies
        # some CPU and memory resources until finished. Threads can be used instead
        # of processes by passing `worker_type=transfer_manager.THREAD`.
        # workers=8
    
        # The maximum number of results to fetch from bucket.list_blobs(). This
        # sample code fetches all of the blobs up to max_results and queues them all
        # for download at once. Though they will still be executed in batches up to
        # the processes limit, queueing them all at once can be taxing on system
        # memory if buckets are very large. Adjust max_results as needed for your
        # system environment, or set it to None if you are sure the bucket is not
        # too large to hold in memory easily.
        # max_results=1000
    
        from google.cloud.storage import [Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html), [transfer_manager](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.transfer_manager.html)
    
        storage_client = Client()
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
    
        blob_names = [blob.name for blob in bucket.list_blobs(max_results=max_results)]
    
        results = [transfer_manager](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.transfer_manager.html).[download_many_to_path](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.transfer_manager.html)(
            bucket, blob_names, destination_directory=destination_directory, max_workers=workers
        )
    
        for name, result in zip(blob_names, results):
            # The results list is either `None` or an exception for each blob in
            # the input list, in order.
    
            if isinstance(result, Exception):
                print("Failed to download {} due to exception: {}".format(name, result))
            else:
                print("Downloaded {} to {}.".format(name, destination_directory + name))

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
