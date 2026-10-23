---
url: https://docs.cloud.google.com/storage/docs/samples/storage-transfer-manager-download-chunks-concurrently/
title: Download a file in chunks concurrently \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:59.551550+00:00
---

# Download a file in chunks concurrently  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-transfer-manager-download-chunks-concurrently/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Download a file in chunks concurrently Stay organized with collections  Save and categorize content based on your preferences. 

Use Transfer Manager to download a single large file in chunks, with concurrency.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Sliced object downloads](https://docs.cloud.google.com/storage/docs/sliced-object-downloads)



## Code sample

### Go

For more information, see the [Cloud Storage Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storage). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    package transfermanager
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"os"
    
    	"cloud.google.com/go/storage"
    	"cloud.google.com/go/storage/transfermanager"
    )
    
    // downloadChunksConcurrently downloads a single file in chunks, concurrently in a process pool.
    func downloadChunksConcurrently(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucketName, blobName, filename string) error {
    	// bucketName := "your-bucket-name"
    	// blobName := "target-file"
    	// filename := "path/to/your/local/file.txt"
    
    	// The chunkSize is the size of each chunk to be downloaded.
    	// The performance impact of this value depends on the use case.
    	// For example, for a slow network, using a smaller chunkSize may be better.
    	// Providing this parameter is optional and the default value is 32 MiB.
    	chunkSize := 16 * 1024 * 1024 // 16 MiB
    
    	// The maximum number of workers to use for the operation.
    	// Please note, providing this parameter is optional.
    	// The performance impact of this value depends on the use case.
    	// To download one large file, the default value: NumCPU / 2 is usually fine.
    	workers := 8
    
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	d, err := transfermanager.NewDownloader(client, transfermanager.WithPartSize(int64(chunkSize)), transfermanager.WithWorkers(workers))
    	if err != nil {
    		return fmt.Errorf("transfermanager.NewDownloader: %w", err)
    	}
    
    	f, err := os.[Create](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Create)(filename)
    	if err != nil {
    		return fmt.Errorf("os.Create: %w", err)
    	}
    	defer f.Close()
    
    	in := &transfermanager.DownloadObjectInput{
    		Bucket:      bucketName,
    		Object:      blobName,
    		Destination: f,
    	}
    
    	if err := d.DownloadObject(ctx, in); err != nil {
    		return fmt.Errorf("d.DownloadObject: %w", err)
    	}
    
    	// Wait for all downloads to complete and close the downloader.
    	// This allows to synchronize the download processes.
    	results, err := d.WaitAndClose()
    	if err != nil {
    		return fmt.Errorf("d.WaitAndClose: %w", err)
    	}
    
    	// Process the downloader result.
    	if len(results) != 1 {
    		return fmt.Errorf("expected 1 result, got %d", len(results))
    	}
    	result := results[0]
    	if result.Err != nil {
    		fmt.Fprintf(w, "download of %v failed with error %v\n", result.[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object), result.Err)
    		return result.Err
    	}
    	fmt.Fprintf(w, "Downloaded %v to %v.\n", blobName, filename)
    
    	return nil
    }
    

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
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
