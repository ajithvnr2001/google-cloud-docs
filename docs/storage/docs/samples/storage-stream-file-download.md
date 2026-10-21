---
url: https://docs.cloud.google.com/storage/docs/samples/storage-stream-file-download/
title: Read Object as a Stream \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:50.188660+00:00
---

# Read Object as a Stream  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-stream-file-download/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Read Object as a Stream Stay organized with collections  Save and categorize content based on your preferences. 

Read Object as a Stream

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Streaming downloads](https://docs.cloud.google.com/storage/docs/streaming-downloads)



## Code sample

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    [](gcs::Client client, std::string const& bucket_name,
       std::string const& object_name) {
      gcs::ObjectReadStream stream = client.ReadObject(bucket_name, object_name);
    
      int count = 0;
      std::string line;
      while (std::getline(stream, line, '\n')) {
        ++count;
      }
      if (stream.bad()) throw google::cloud::Status(stream.status());
    
      std::cout << "The object has " << count << " lines\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    using System.IO;
    
    public class DownloadFileSample
    {
        public void DownloadFile(
            string bucketName = "your-unique-bucket-name",
            string objectName = "my-file-name",
            string localPath = "my-local-path/my-file-name")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            using var outputFile = File.OpenWrite(localPath);
            storage.DownloadObject(bucketName, objectName, outputFile);
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
    	"time"
    
    	"cloud.google.com/go/storage"
    )
    
    // downloadFileIntoMemory downloads an object.
    func downloadFileIntoMemory(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucket, object string) ([]byte, error) {
    	// bucket := "bucket-name"
    	// object := "object-name"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*50)
    	defer cancel()
    
    	rc, err := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucket).[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)(object).[NewReader](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_NewReader)(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("Object(%q).NewReader: %w", object, err)
    	}
    	defer rc.Close()
    
    	data, err := io.ReadAll(rc)
    	if err != nil {
    		return nil, fmt.Errorf("io.ReadAll: %w", err)
    	}
    	fmt.Fprintf(w, "Blob %v downloaded.\n", object)
    	return data, nil
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
    import java.nio.file.[Path](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.Path.html);
    import java.nio.file.Paths;
    import java.nio.file.StandardOpenOption;
    
    public class StreamObjectDownload {
    
      public static void streamObjectDownload(
          [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) projectId, [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) bucketName, [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) objectName, [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) targetFile)
          throws IOException {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The ID of your GCS object
        // String objectName = "your-object-name";
    
        // The path to the file to download the object to
        // String targetFile = "path/to/your/file";
        [Path](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.Path.html) targetFilePath = Paths.get(targetFile);
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().getService();
        try ([ReadChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.ReadChannel.html) reader = storage.[reader](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_reader_com_google_cloud_storage_BlobId_com_google_cloud_storage_Storage_BlobSourceOption____)(BlobId.of(bucketName, objectName));
            FileChannel targetFileChannel =
                FileChannel.open(targetFilePath, StandardOpenOption.WRITE)) {
    
          ByteStreams.copy(reader, targetFileChannel);
    
          System.out.println(
              "Downloaded object "
                  + objectName
                  + " from bucket "
                  + bucketName
                  + " to "
                  + targetFile
                  + " using a ReadChannel.");
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
    
    // The filename and file path where you want to download the file
    // const destFileName = '/local/path/to/file.txt';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function streamFileDownload() {
      // The example below demonstrates how we can reference a remote file, then
      // pipe its contents to a local file.
      // Once the stream is created, the data can be piped anywhere (process, sdout, etc)
      await storage
        .bucket(bucketName)
        .file(fileName)
        .[createReadStream](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/file_2.html)() //stream is created
        .pipe(fs.[createWriteStream](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/file_2.html)(destFileName))
        .on('finish', () => {
          // The file download is complete
        });
    
      console.log(
        `gs://${bucketName}/${fileName} downloaded to ${destFileName}.`
      );
    }
    
    streamFileDownload().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Download an object from Cloud Storage and save it as a local file.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $objectName The name of your Cloud Storage object.
     *        (e.g. 'my-object')
     * @param string $destination The local destination to save the object.
     *        (e.g. '/path/to/your/file')
     */
    function download_object(string $bucketName, string $objectName, string $destination): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
        $object = $bucket->object($objectName);
        $object->downloadToFile($destination);
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
    
    
    def download_blob_to_stream(bucket_name, source_blob_name, file_obj):
        """Downloads a blob to a stream or other file-like object."""
    
        # The ID of your GCS bucket
        # bucket_name = "your-bucket-name"
    
        # The ID of your GCS object (blob)
        # source_blob_name = "storage-object-name"
    
        # The stream or file (file-like object) to which the blob will be written
        # import io
        # file_obj = io.BytesIO()
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
    
        # Construct a client-side representation of a blob.
        # Note `Bucket.blob` differs from `Bucket.get_blob` in that it doesn't
        # retrieve metadata from Google Cloud Storage. As we don't use metadata in
        # this example, using `Bucket.blob` is preferred here.
        blob = bucket.blob(source_blob_name)
        blob.[download_to_file](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_to_file)(file_obj)
    
        print(f"Downloaded blob {source_blob_name} to file-like object.")
    
        return file_obj
        # Before reading from file_obj, remember to rewind with file_obj.seek(0).
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    # Downloads a blob to a stream or other file-like object.
    
    # The ID of your GCS bucket
    # bucket_name = "your-unique-bucket-name"
    
    # Name of a file in the Storage bucket
    # file_name   = "some_file.txt"
    
    # The stream or file (file-like object) to which the contents will be written
    # local_file_obj = StringIO.new
    
    require "google/cloud/storage"
    
    storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
    bucket  = storage.bucket bucket_name
    file    = bucket.[file](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) file_name
    
    file.[download](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-File.html) local_file_obj, verify: :none
    
    # rewind the object before starting to read the downloaded contents
    local_file_obj.rewind
    puts "The full downloaded file contents are: #{local_file_obj.read.inspect}"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
