---
url: https://docs.cloud.google.com/storage/docs/samples/storage-transfer-manager-download-many/
title: Download many objects \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:32:29.974658+00:00
---

# Download many objects  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-transfer-manager-download-many/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Download many objects Stay organized with collections  Save and categorize content based on your preferences. 

Use Transfer Manager to download many objects with concurrency.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Download objects](https://docs.cloud.google.com/storage/docs/downloading-objects)



## Code sample

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html);
    import com.google.cloud.storage.transfermanager.[DownloadResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.DownloadResult.html);
    import com.google.cloud.storage.transfermanager.[ParallelDownloadConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.ParallelDownloadConfig.html);
    import com.google.cloud.storage.transfermanager.[TransferManager](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManager.html);
    import com.google.cloud.storage.transfermanager.[TransferManagerConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html);
    import java.nio.file.Path;
    import java.util.List;
    
    class DownloadMany {
    
      public static void downloadManyBlobs(
          String bucketName, List<BlobInfo> blobs, Path destinationDirectory) throws Exception {
    
        try ([TransferManager](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManager.html) transferManager =
            [TransferManagerConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html).newBuilder().build().getService()) {
          [ParallelDownloadConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.ParallelDownloadConfig.html) parallelDownloadConfig =
              [ParallelDownloadConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.ParallelDownloadConfig.html).newBuilder()
                  .setBucketName(bucketName)
                  .setDownloadDirectory(destinationDirectory)
                  .build();
    
          List<DownloadResult> results =
              transferManager.downloadBlobs(blobs, parallelDownloadConfig).getDownloadResults();
    
          for ([DownloadResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.DownloadResult.html) result : results) {
            System.out.println(
                "Download of "
                    + [result](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.spi.v1.StorageRpc.RewriteResponse.html#com_google_cloud_storage_spi_v1_StorageRpc_RewriteResponse_result).getInput().getName()
                    + " completed with status "
                    + [result](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.spi.v1.StorageRpc.RewriteResponse.html#com_google_cloud_storage_spi_v1_StorageRpc_RewriteResponse_result).getStatus());
          }
        }
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
    
    // The ID of the first GCS file to download
    // const firstFileName = 'your-first-file-name';
    
    // The ID of the second GCS file to download
    // const secondFileName = 'your-second-file-name;
    
    // Imports the Google Cloud client library
    const {Storage, TransferManager} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    // Creates a transfer manager client
    const transferManager = new [TransferManager](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/transfermanager.html)(storage.bucket(bucketName));
    
    async function downloadManyFilesWithTransferManager() {
      // Downloads the files
      await transferManager.[downloadManyFiles](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/transfermanager.html)([firstFileName, secondFileName]);
    
      for (const fileName of [firstFileName, secondFileName]) {
        console.log(`gs://${bucketName}/${fileName} downloaded to ${fileName}.`);
      }
    }
    
    downloadManyFilesWithTransferManager().catch(console.error);

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def download_many_blobs_with_transfer_manager(
        bucket_name, blob_names, destination_directory="", blob_name_prefix="", workers=8
    ):
        """Download blobs in a list by name, concurrently in a process pool.
    
        The filename of each blob once downloaded is derived from the blob name and
        the `destination_directory `parameter. For complete control of the filename
        of each blob, use transfer_manager.download_many() instead.
    
        Directories will be created automatically as needed to accommodate blob
        names that include slashes.
        """
    
        # The ID of your GCS bucket
        # bucket_name = "your-bucket-name"
    
        # The list of blob names to download. The names of each blobs will also
        # be the name of each destination file (use transfer_manager.download_many()
        # instead to control each destination file name). If there is a "/" in the
        # blob name, then corresponding directories will be created on download.
        # blob_names = ["myblob", "myblob2"]
    
        # The directory on your computer to which to download all of the files. This
        # string is prepended to the name of each blob to form the full path using
        # pathlib. Relative paths and absolute paths are both accepted. An empty
        # string means "the current working directory". Note that this parameter
        # will NOT allow files to escape the destination_directory and will skip
        # downloads that attempt directory traversal outside of it.
        # destination_directory = ""
    
        # The maximum number of processes to use for the operation. The performance
        # impact of this value depends on the use case, but smaller files usually
        # benefit from a higher number of processes. Each additional process occupies
        # some CPU and memory resources until finished. Threads can be used instead
        # of processes by passing `worker_type=transfer_manager.THREAD`.
        # workers=8
    
        from google.cloud.storage import [Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html), [transfer_manager](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.transfer_manager.html)
    
        storage_client = Client()
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
    
        results = [transfer_manager](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.transfer_manager.html).[download_many_to_path](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.transfer_manager.html)(
            bucket,
            blob_names,
            destination_directory=destination_directory,
            blob_name_prefix=blob_name_prefix,
            max_workers=workers,
        )
    
        for name, result in zip(blob_names, results):
            # The results list is either `None`, an exception, or a warning for each blob in
            # the input list, in order.
            if isinstance(result, UserWarning):
                print("Skipped download for {} due to warning: {}".format(name, result))
            elif isinstance(result, Exception):
                print("Failed to download {} due to exception: {}".format(name, result))
            else:
                print(
                    "Downloaded {} inside {} directory.".format(name, destination_directory)
                )
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
