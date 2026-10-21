---
url: https://docs.cloud.google.com/storage/docs/samples/storage-download-public-file/
title: Download a public object without credentials \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:16:58.654073+00:00
---

# Download a public object without credentials  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-download-public-file/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Download a public object without credentials Stay organized with collections  Save and categorize content based on your preferences. 

Download an object from a public data set object.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Access public data](https://docs.cloud.google.com/storage/docs/access-public-data)



## Code sample

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    [](std::string const& bucket_name, std::string const& object_name) {
      // Create a client that does not authenticate with the server.
      auto client = gcs::Client{
          google::cloud::Options{}.set<google::cloud::UnifiedCredentialsOption>(
              google::cloud::MakeInsecureCredentials())};
    
      // Read an object, the object must have been made public.
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
    
    public class DownloadPublicFileSample
    {
        public string DownloadPublicFile(
            string bucketName = "your-bucket-name",
            string objectName = "your-object-name",
            string localPath = "path/to/download/object/to")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[CreateUnauthenticated](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_CreateUnauthenticated)();
    
            using var outputFile = File.OpenWrite(localPath);
            storage.DownloadObject(bucketName, objectName, outputFile);
    
            Console.WriteLine($"Downloaded public file {objectName} from bucket {bucketName} to {localPath}.");
            return localPath;
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
    	"google.golang.org/api/option"
    )
    
    // downloadPublicFile downloads a public object.
    func downloadPublicFile(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucket, object string) ([]byte, error) {
    	// bucket := "bucket-name"
    	// object := "object-name"
    	ctx := context.Background()
    	// Create a client that does not authenticate with the server.
    	client, err := storage.NewClient(ctx, option.WithoutAuthentication())
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
    
    
    import com.google.cloud.storage.[BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import java.nio.file.Path;
    
    public class DownloadPublicObject {
      public static void downloadPublicObject(
          String bucketName, String publicObjectName, Path destFilePath) {
        // The name of the bucket to access
        // String bucketName = "my-bucket";
    
        // The name of the remote public file to download
        // String publicObjectName = "publicfile.txt";
    
        // The path to which the file should be downloaded
        // Path destFilePath = Paths.get("/local/path/to/file.txt");
    
        // Instantiate an anonymous Google Cloud Storage client, which can only access public files
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).[getUnauthenticatedInstance](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html#com_google_cloud_storage_StorageOptions_getUnauthenticatedInstance__)().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
    
        storage.[downloadTo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_downloadTo_com_google_cloud_storage_BlobId_java_io_OutputStream_com_google_cloud_storage_Storage_BlobSourceOption____)(BlobId.of(bucketName, publicObjectName), destFilePath);
    
        System.out.println(
            "Downloaded public object "
                + publicObjectName
                + " from bucket name "
                + bucketName
                + " to "
                + destFilePath);
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
    // const srcFilename = 'your-file-name';
    
    // The path to which the file should be downloaded
    // const destFileName = '/local/path/to/file.txt';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function downloadPublicFile() {
      const options = {
        destination: destFileName,
      };
    
      // Download public file.
      await storage.bucket(bucketName).file(srcFileName).[download](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/file_2.html)(options);
    
      console.log(
        `Downloaded public file ${srcFileName} from bucket name ${bucketName} to ${destFileName}`
      );
    }
    
    downloadPublicFile().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Download a public file using anonymous credentials.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $objectName The name of your Cloud Storage object.
     *        (e.g. 'my-object')
     * @param string $destination The local destination to save the object.
     *        (e.g. '/home/admin/downloads/my-object')
     */
    function download_public_file(string $bucketName, string $objectName, string $destination): void
    {
        // create a storage client without authentication
        $storage = new StorageClient([
        ]);
    
        $bucket = $storage->bucket($bucketName);
        $object = $bucket->object($objectName);
    
        // set `shouldSignRequest` to false to force the client to not authenticate.
        // if you do not have any client configuration enabled (i.e. application
        // default credentials), that option can be omitted.
        $object->downloadToFile($destination, [
            'shouldSignRequest' => false,
        ]);
    
        printf(
            'Downloaded public object %s from bucket %s to %s',
            $objectName,
            $bucketName,
            $destination
        );
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def download_public_file(bucket_name, source_blob_name, destination_file_name):
        """Downloads a public blob from the bucket."""
        # bucket_name = "your-bucket-name"
        # source_blob_name = "storage-object-name"
        # destination_file_name = "local/path/to/file"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html).[create_anonymous_client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_create_anonymous_client)()
    
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(source_blob_name)
        blob.[download_to_filename](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_to_filename)(destination_file_name)
    
        print(
            "Downloaded public blob {} from bucket {} to {}.".format(
                source_blob_name, bucket.name, destination_file_name
            )
        )
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def download_public_file bucket_name:, file_name:, local_file_path:
      # The name of the bucket to access
      # bucket_name = "my-bucket"
    
      # The name of the remote public file to download
      # file_name = "publicfile.txt"
    
      # The path to which the file should be downloaded
      # local_file_path = "/local/path/to/file.txt"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[anonymous](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket  = storage.bucket bucket_name, skip_lookup: true
      file    = bucket.[file](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) file_name
    
      file.[download](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-File.html) local_file_path
    
      puts "Downloaded public object #{file.name} from bucket #{bucket} to #{local_file_path}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
