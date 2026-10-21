---
url: https://docs.cloud.google.com/storage/docs/sliced-object-downloads/
title: Sliced object downloads \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:33.527744+00:00
---

# Sliced object downloads  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/sliced-object-downloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Sliced object downloads Stay organized with collections  Save and categorize content based on your preferences. 

One strategy for downloading large files is called _sliced object downloads_. In such a download, ranged `GET` requests are made in parallel, storing data within a temporary, pre-allocated destination file. Once all slices have completed downloading, the temporary file is renamed to the destination file.

Sliced object downloads are designed to accelerate the download of an entire object by transferring its parts concurrently. You can't use sliced object downloads to download only a specific slice or byte range of an object. To download or read a specific portion of an object, see [Download a portion of an object](https://docs.cloud.google.com/storage/docs/downloading-objects#downloading-an-object-portion) or [Read objects](https://docs.cloud.google.com/storage/docs/rapid/use-objects-in-zonal-buckets#read-objects).

Sliced object downloads can be significantly faster if network and disk speed are not limiting factors; however, sliced object downloads cause multiple writes to occur at various locations on disk, so this download strategy can degrade performance for disks with slow seek times, especially when breaking a download into a large number of slices. Tools such as the Google Cloud CLI have low default values for the number of slices they create to minimize the possibility of performance impacts.

## Verify data integrity

Sliced object downloads should always use a fast composable checksum (CRC32C) to verify the data integrity of the slices. To perform sliced object downloads, tools such as the gcloud CLI require a compiled version of crcmod on the machine performing the download. If compiled crcmod is not available, the gcloud CLI performs non-sliced object downloads instead.

For more information on how to perform data validation for object reads, see [Checksums for data reads](https://docs.cloud.google.com/storage/docs/data-validation#reads).

## How tools and APIs use sliced object downloads

Depending on how you interact with Cloud Storage, sliced object downloads might be managed automatically on your behalf. This section describes the sliced object download behavior for different tools and provides information for how you can modify the behavior.

### Console

The Google Cloud console does not perform sliced object downloads.

### Command line

By default, [`gcloud storage cp`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cp) enables sliced object downloads. You can control how and when the gcloud CLI performs sliced object downloads by modifying the following properties:

  * **`storage/sliced_object_download_threshold`** : The minimum total file size for performing a sliced object download. You can disable all sliced object downloads by setting this value to `0`.

  * **`storage/sliced_object_download_max_components`** : The maximum number of slices to use in the download. Set `0` for no limit, in which case the number of slices is determined solely by `storage/sliced_object_download_component_size`.

  * **`storage/sliced_object_download_component_size`** : The target size for each download slice. This property is ignored if the total file size is so large that downloading slices of this size would require more slices than allowed, as set in `storage/sliced_object_download_max_components`.




You can modify these properties by creating a [named configuration](https://docs.cloud.google.com/sdk/gcloud/reference/topic/configurations) and applying the configuration either on a per-command basis by using the [`--configuration` project-wide flag](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration) or for all gcloud CLI commands by using the [`gcloud config set` command](https://docs.cloud.google.com/sdk/gcloud/reference/config/set).

No additional local disk space is required when using the gcloud CLI to perform sliced object downloads. If the download fails prior to completion, run the command again to resume the slices that failed. Slices that were downloaded successfully before the failure are not re-downloaded when you retry, except in the case where the source object has changed between download attempts.

Temporary downloaded objects appear in the destination directory with the suffix `_.gstmp` in their name.

### Client libraries

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

You can perform sliced object downloads by setting `AllowDivideAndConquer` to `true`. For example:
    
    
    import com.google.cloud.storage.[BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html);
    import com.google.cloud.storage.transfermanager.[DownloadResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.DownloadResult.html);
    import com.google.cloud.storage.transfermanager.[ParallelDownloadConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.ParallelDownloadConfig.html);
    import com.google.cloud.storage.transfermanager.[TransferManager](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManager.html);
    import com.google.cloud.storage.transfermanager.[TransferManagerConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html);
    import java.nio.file.Path;
    import java.util.List;
    
    class AllowDivideAndConquerDownload {
    
      public static void divideAndConquerDownloadAllowed(
          List<BlobInfo> blobs, String bucketName, Path destinationDirectory) {
        [TransferManager](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManager.html) transferManager =
            [TransferManagerConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html).newBuilder()
                .setAllowDivideAndConquerDownload(true)
                .build()
                .getService();
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

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

You can perform sliced object downloads using the [`downloadFileInChunks`](https://googleapis.dev/nodejs/storage/latest/TransferManager.html#downloadFileInChunks) method. For example:
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The ID of your GCS bucket
    // const bucketName = 'your-unique-bucket-name';
    
    // The ID of the GCS file to download
    // const fileName = 'your-file-name';
    
    // The path to which the file should be downloaded
    // const destFileName = '/local/path/to/file.txt';
    
    // The size of each chunk to be downloaded
    // const chunkSize = 1024;
    
    // Imports the Google Cloud client library
    const {Storage, TransferManager} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    // Creates a transfer manager client
    const transferManager = new [TransferManager](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/transfermanager.html)(storage.bucket(bucketName));
    
    async function downloadFileInChunksWithTransferManager() {
      // Downloads the files
      await transferManager.[downloadFileInChunks](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/transfermanager.html)(fileName, {
        destination: destFileName,
        chunkSizeBytes: chunkSize,
      });
    
      console.log(
        `gs://${bucketName}/${fileName} downloaded to ${destFileName}.`
      );
    }
    
    downloadFileInChunksWithTransferManager().catch(console.error);

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

You can perform sliced object downloads using the [`download_chunks_concurrently`](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.transfer_manager#google_cloud_storage_transfer_manager_download_chunks_concurrently) method. For example:
    
    
    def download_chunks_concurrently(
        bucket_name, blob_name, filename, chunk_size=32 * 1024 * 1024, workers=8
    ):
        """Download a single file in chunks, concurrently in a process pool."""
    
        # The ID of your GCS bucket
        # bucket_name = "your-bucket-name"
    
        # The file to be downloaded
        # blob_name = "target-file"
    
        # The destination filename or path
        # filename = ""
    
        # The size of each chunk. The performance impact of this value depends on
        # the use case. The remote service has a minimum of 5 MiB and a maximum of
        # 5 GiB.
        # chunk_size = 32 * 1024 * 1024 (32 MiB)
    
        # The maximum number of processes to use for the operation. The performance
        # impact of this value depends on the use case, but smaller files usually
        # benefit from a higher number of processes. Each additional process occupies
        # some CPU and memory resources until finished. Threads can be used instead
        # of processes by passing `worker_type=transfer_manager.THREAD`.
        # workers=8
    
        from google.cloud.storage import [Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html), [transfer_manager](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.transfer_manager.html)
    
        storage_client = Client()
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
        blob = bucket.blob(blob_name)
    
        [transfer_manager](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.transfer_manager.html).[download_chunks_concurrently](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.transfer_manager.html)(
            blob, filename, chunk_size=chunk_size, max_workers=workers
        )
    
        print("Downloaded {} to {}.".format(blob_name, filename))
    
    

### REST APIs

Both the [JSON API](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters#range) and [XML API](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#range) support ranged `GET` requests, which means you can use either API to implement your own sliced object download strategy.

In order to protect against data corruption due to the source object changing during the download, you should provide the [generation number](https://docs.cloud.google.com/storage/docs/metadata#generation-number) of the source object in each download request for a slice of the object.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
