---
url: https://docs.cloud.google.com/storage/docs/samples/storage-transfer-manager-upload-many/
title: Upload many objects \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:30:15.584824+00:00
---

# Upload many objects  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-transfer-manager-upload-many/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Upload many objects Stay organized with collections  Save and categorize content based on your preferences. 

Use Transfer Manager to upload many files with concurrency.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Host a static website](https://docs.cloud.google.com/storage/docs/hosting-static-website)
  * [Hosting a static website using HTTP](https://docs.cloud.google.com/storage/docs/hosting-static-website-http)
  * [Upload objects from a file system](https://docs.cloud.google.com/storage/docs/uploading-objects)



## Code sample

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.transfermanager.[ParallelUploadConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.ParallelUploadConfig.html);
    import com.google.cloud.storage.transfermanager.[TransferManager](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManager.html);
    import com.google.cloud.storage.transfermanager.[TransferManagerConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html);
    import com.google.cloud.storage.transfermanager.[UploadResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.UploadResult.html);
    import java.io.IOException;
    import java.nio.file.Path;
    import java.util.List;
    
    class UploadMany {
    
      public static void uploadManyFiles(String bucketName, List<Path> files) throws IOException {
        [TransferManager](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManager.html) transferManager = [TransferManagerConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html).newBuilder().build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        [ParallelUploadConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.ParallelUploadConfig.html) parallelUploadConfig =
            [ParallelUploadConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.ParallelUploadConfig.html).newBuilder().setBucketName(bucketName).build();
        List<UploadResult> results =
            transferManager.[uploadFiles](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManager.html#com_google_cloud_storage_transfermanager_TransferManager_uploadFiles_java_util_List_java_nio_file_Path__com_google_cloud_storage_transfermanager_ParallelUploadConfig_)(files, parallelUploadConfig).[getUploadResults](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.UploadJob.html#com_google_cloud_storage_transfermanager_UploadJob_getUploadResults__)();
        for ([UploadResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.UploadResult.html) result : results) {
          System.out.println(
              "Upload for "
                  + result.getInput().getName()
                  + " completed with status "
                  + result.getStatus());
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
    
    // The ID of the first GCS file to upload
    // const firstFilePath = 'your-first-file-name';
    
    // The ID of the second GCS file to upload
    // const secondFilePath = 'your-second-file-name';
    
    // Imports the Google Cloud client library
    const {Storage, TransferManager} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    // Creates a transfer manager client
    const transferManager = new [TransferManager](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/transfermanager.html)(storage.bucket(bucketName));
    
    async function uploadManyFilesWithTransferManager() {
      // Uploads the files
      await transferManager.[uploadManyFiles](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/transfermanager.html)([firstFilePath, secondFilePath]);
    
      for (const filePath of [firstFilePath, secondFilePath]) {
        console.log(`${filePath} uploaded to ${bucketName}.`);
      }
    }
    
    uploadManyFilesWithTransferManager().catch(console.error);

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def upload_many_blobs_with_transfer_manager(
        bucket_name, filenames, source_directory="", workers=8
    ):
        """Upload every file in a list to a bucket, concurrently in a process pool.
    
        Each blob name is derived from the filename, not including the
        `source_directory` parameter. For complete control of the blob name for each
        file (and other aspects of individual blob metadata), use
        transfer_manager.upload_many() instead.
        """
    
        # The ID of your GCS bucket
        # bucket_name = "your-bucket-name"
    
        # A list (or other iterable) of filenames to upload.
        # filenames = ["file_1.txt", "file_2.txt"]
    
        # The directory on your computer that is the root of all of the files in the
        # list of filenames. This string is prepended (with os.path.join()) to each
        # filename to get the full path to the file. Relative paths and absolute
        # paths are both accepted. This string is not included in the name of the
        # uploaded blob; it is only used to find the source files. An empty string
        # means "the current working directory". Note that this parameter allows
        # directory traversal (e.g. "/", "../") and is not intended for unsanitized
        # end user input.
        # source_directory=""
    
        # The maximum number of processes to use for the operation. The performance
        # impact of this value depends on the use case, but smaller files usually
        # benefit from a higher number of processes. Each additional process occupies
        # some CPU and memory resources until finished. Threads can be used instead
        # of processes by passing `worker_type=transfer_manager.THREAD`.
        # workers=8
    
        from google.cloud.storage import [Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html), [transfer_manager](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.transfer_manager.html)
    
        storage_client = Client()
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
    
        results = [transfer_manager](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.transfer_manager.html).[upload_many_from_filenames](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.transfer_manager.html)(
            bucket, filenames, source_directory=source_directory, max_workers=workers
        )
    
        for name, result in zip(filenames, results):
            # The results list is either `None` or an exception for each filename in
            # the input list, in order.
    
            if isinstance(result, Exception):
                print("Failed to upload {} due to exception: {}".format(name, result))
            else:
                print("Uploaded {} to {}.".format(name, bucket.name))

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
