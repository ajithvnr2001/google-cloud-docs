---
url: https://docs.cloud.google.com/storage/docs/samples/storage-download-byte-range/
title: Download an object using a byte range \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:29:30.145218+00:00
---

# Download an object using a byte range  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-download-byte-range/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Download an object using a byte range Stay organized with collections  Save and categorize content based on your preferences. 

Download an object using a byte range from a Cloud Storage bucket.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Download objects](https://docs.cloud.google.com/storage/docs/downloading-objects)



## Code sample

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    [](gcs::Client client, std::string const& bucket_name,
       std::string const& object_name, std::int64_t start, std::int64_t end) {
      gcs::ObjectReadStream stream =
          client.ReadObject(bucket_name, object_name, gcs::ReadRange(start, end));
    
      int count = 0;
      std::string line;
      while (std::getline(stream, line, '\n')) {
        std::cout << line << "\n";
        ++count;
      }
      if (stream.bad()) throw google::cloud::Status(stream.status());
    
      std::cout << "The requested range has " << count << " lines\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using Google.Apis.Storage.v1;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    using System.IO;
    using System.Net.Http;
    using System.Net.Http.Headers;
    using System.Threading.Tasks;
    
    public class DownloadByteRangeAsyncSample
    {
        public async Task DownloadByteRangeAsync(
            string bucketName = "your-unique-bucket-name",
            string objectName = "my-file-name",
            long firstByte = 0,
            long lastByte = 20,
            string localPath = "my-local-path/my-file-name")
        {
            var storageClient = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
    
            // Create an HTTP request for the media, for a limited byte range.
            StorageService storage = storageClient.Service;
            var uri = new Uri($"{storage.BaseUri}b/{bucketName}/o/{objectName}?alt=media");
    
            var request = new HttpRequestMessage { RequestUri = uri };
            request.Headers.[Range](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.DownloadObjectOptions.html#Google_Cloud_Storage_V1_DownloadObjectOptions_Range) = new RangeHeaderValue(firstByte, lastByte);
    
            using var outputFile = File.OpenWrite(localPath);
            // Use the HttpClient in the storage object because it supplies
            // all the authentication headers we need.
            var response = await storage.HttpClient.SendAsync(request);
            await response.Content.CopyToAsync(outputFile, null);
            Console.WriteLine($"Downloaded {objectName} to {localPath}.");
        }
    }

### Go

For more information, see the [Cloud Storage Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storage). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"os"
    	"time"
    
    	"cloud.google.com/go/storage"
    )
    
    // downloadByteRange downloads a specific byte range of an object to a file.
    func downloadByteRange(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucket, object string, startByte int64, endByte int64, destFileName string) error {
    	// bucket := "bucket-name"
    	// object := "object-name"
    	// startByte := 0
    	// endByte := 20
    	// destFileName := "file.txt"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*50)
    	defer cancel()
    
    	f, err := os.[Create](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Create)(destFileName)
    	if err != nil {
    		return fmt.Errorf("os.Create: %w", err)
    	}
    
    	length := endByte - startByte
    	rc, err := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucket).[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)(object).[NewRangeReader](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_NewRangeReader)(ctx, startByte, length)
    	if err != nil {
    		return fmt.Errorf("Object(%q).NewReader: %w", object, err)
    	}
    	defer rc.Close()
    
    	if _, err := io.Copy(f, rc); err != nil {
    		return fmt.Errorf("io.Copy: %w", err)
    	}
    
    	if err = f.Close(); err != nil {
    		return fmt.Errorf("f.Close: %w", err)
    	}
    
    	fmt.Fprintf(w, "Bytes %v to %v of blob %v downloaded to local file %v\n", startByte, startByte+length, object, destFileName)
    
    	return nil
    
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.[ReadChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.ReadChannel.html);
    import com.google.cloud.storage.[BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import com.google.common.io.ByteStreams;
    import java.io.IOException;
    import java.nio.channels.FileChannel;
    import java.nio.file.Paths;
    import java.nio.file.StandardOpenOption;
    
    public class DownloadByteRange {
    
      public static void downloadByteRange(
          [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) projectId,
          [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) bucketName,
          [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) blobName,
          long startByte,
          long endBytes,
          [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) destFileName)
          throws IOException {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The name of the blob/file that you wish to modify permissions on
        // String blobName = "your-blob-name";
    
        // The starting byte at which to begin the download
        // long startByte = 0;
    
        // The ending byte at which to end the download
        // long endByte = 20;
    
        // The path to which the file should be downloaded
        // String destFileName = '/local/path/to/file.txt';
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().getService();
        [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html) blobId = [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html).of(bucketName, blobName);
        try ([ReadChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.ReadChannel.html) from = storage.[reader](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_reader_com_google_cloud_storage_BlobId_com_google_cloud_storage_Storage_BlobSourceOption____)(blobId);
            FileChannel to = FileChannel.open(Paths.get(destFileName), StandardOpenOption.WRITE)) {
          from.seek(startByte);
          from.limit(endBytes);
    
          ByteStreams.copy(from, to);
    
          System.out.printf(
              "%s downloaded to %s from byte %d to byte %d%n",
              blobId.[toGsUtilUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html#com_google_cloud_storage_BlobId_toGsUtilUri__)(), destFileName, startByte, endBytes);
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
    
    // The ID of your GCS file
    // const fileName = 'your-file-name';
    
    // The starting byte at which to begin the download
    // const startByte = 0;
    
    // The ending byte at which to end the download
    // const endByte = 20;
    
    // The path to which the file should be downloaded
    // const destFileName = '/local/path/to/file.txt';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function downloadByteRange() {
      const options = {
        destination: destFileName,
        start: startByte,
        end: endByte,
      };
    
      // Downloads the file from the starting byte to the ending byte specified in options
      await storage.bucket(bucketName).file(fileName).[download](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/file_2.html)(options);
    
      console.log(
        `gs://${bucketName}/${fileName} downloaded to ${destFileName} from byte ${startByte} to byte ${endByte}.`
      );
    }
    
    downloadByteRange();

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Download a byte range from Cloud Storage and save it as a local file.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $objectName The name of your Cloud Storage object.
     *        (e.g. 'my-object')
     * @param int $startByte The starting byte at which to begin the download.
     *        (e.g. 1)
     * @param int $endByte The ending byte at which to end the download. (e.g. 5)
     * @param string $destination The local destination to save the object.
     *        (e.g. '/path/to/your/file')
     */
    function download_byte_range(
        string $bucketName,
        string $objectName,
        int $startByte,
        int $endByte,
        string $destination
    ): void {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
        $object = $bucket->object($objectName);
        $object->downloadToFile($destination, [
            'restOptions' => [
                'headers' => [
                    'Range' => "bytes=$startByte-$endByte",
                ],
            ],
        ]);
        printf(
            'Downloaded gs://%s/%s to %s' . PHP_EOL,
            $bucketName,
            $objectName,
            basename($destination)
        );
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def download_byte_range(
        bucket_name, source_blob_name, start_byte, end_byte, destination_file_name
    ):
        """Downloads a blob from the bucket."""
        # The ID of your GCS bucket
        # bucket_name = "your-bucket-name"
    
        # The ID of your GCS object
        # source_blob_name = "storage-object-name"
    
        # The starting byte at which to begin the download
        # start_byte = 0
    
        # The ending byte at which to end the download
        # end_byte = 20
    
        # The path to which the file should be downloaded
        # destination_file_name = "local/path/to/file"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
    
        # Construct a client side representation of a blob.
        # Note `Bucket.blob` differs from `Bucket.get_blob` as it doesn't retrieve
        # any content from Google Cloud Storage. As we don't need additional data,
        # using `Bucket.blob` is preferred here.
        blob = bucket.blob(source_blob_name)
        blob.[download_to_filename](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_to_filename)(destination_file_name, start=start_byte, end=end_byte)
    
        print(
            "Downloaded bytes {} to {} of object {} from bucket {} to local file {}.".format(
                start_byte, end_byte, source_blob_name, bucket_name, destination_file_name
            )
        )
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    # The ID of your GCS bucket
    # bucket_name = "your-unique-bucket-name"
    
    # file_name = "Name of a file in the Storage bucket"
    
    # The starting byte at which to begin the download
    # start_byte = 0
    
    # The ending byte at which to end the download
    # end_byte = 20
    
    # The path to which the file should be downloaded
    # local_file_path = "/local/path/to/file.txt"
    
    require "google/cloud/storage"
    
    storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
    bucket  = storage.bucket bucket_name
    file    = bucket.[file](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) file_name
    
    file.[download](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-File.html) local_file_path, range: start_byte..end_byte
    
    puts "Downloaded bytes #{start_byte} to #{end_byte} of object #{file_name} from bucket #{bucket_name}" \
         + " to local file #{local_file_path}."

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
