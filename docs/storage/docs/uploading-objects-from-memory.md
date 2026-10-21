---
url: https://docs.cloud.google.com/storage/docs/uploading-objects-from-memory/
title: Upload objects from memory \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:21.969594+00:00
---

# Upload objects from memory  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/uploading-objects-from-memory/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Upload objects from memory Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to upload objects from memory to your Cloud Storage bucket by using client libraries. Uploading from memory is useful for when you want to avoid unnecessary writes from memory to your local file system.

An uploaded object consists of the data you want to store along with any associated metadata. For a conceptual overview, including how to choose the optimal upload method based on your file size, see [Object uploads](https://docs.cloud.google.com/storage/docs/uploads).

## Required roles

To get the permissions that you need to upload objects from memory to a bucket, ask your administrator to grant you the Storage Object User (`roles/storage.objectUser`) IAM role on the bucket. This [predefined role](https://docs.cloud.google.com/iam/docs/roles-permissions) contains the permissions required to upload an object to a bucket. To see the exact permissions that are required, expand the **Required permissions** section:

#### Required permissions

  * `storage.objects.create`
  * `storage.objects.delete`
    * This permission is only required for uploads that overwrite an existing object.



You can also get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

For information about granting roles on buckets, see [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).

## Upload an object from memory

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name,
       std::string const& object_name) {
      std::string const text = "Lorem ipsum dolor sit amet";
      // For small uploads where the data is contiguous in memory use
      // `InsertObject()`. For more specific size recommendations see
      //     https://cloud.google.com/storage/docs/uploads-downloads#size
      auto metadata = client.InsertObject(bucket_name, object_name, text);
      if (!metadata) throw std::move(metadata).status();
      std::cout << "Successfully wrote to object " << metadata->name()
                << " its size is: " << metadata->size() << "\n";
    
      // For larger uploads, or uploads where the data is not contiguous in
      // memory, use `WriteObject()`. Consider using `std::ostream::write()` for
      // best performance.
      std::vector<std::string> v(100, text);
      gcs::ObjectWriteStream stream =
          client.WriteObject(bucket_name, object_name);
      std::copy(v.begin(), v.end(), std::ostream_iterator<std::string>(stream));
      stream.Close();
    
      metadata = std::move(stream).metadata();
      if (!metadata) throw std::move(metadata).status();
      std::cout << "Successfully wrote to object " << metadata->name()
                << " its size is: " << metadata->size()
                << "\nFull metadata: " << *metadata << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    using System.IO;
    using System.Text;
    
    public class UploadObjectFromMemorySample
    {
        public void UploadObjectFromMemory(
            string bucketName = "unique-bucket-name",
            string objectName = "file-name",
            string contents = "Hello world!")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            byte[] byteArray = Encoding.UTF8.GetBytes(contents);
            MemoryStream stream = new MemoryStream(byteArray);
            storage.UploadObject(bucketName, objectName, "application/octet-stream" , stream);
    
            Console.WriteLine($" {objectName} uploaded to bucket {bucketName} with contents: {contents}");
        }
    }
    

### Go

For more information, see the [Cloud Storage Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storage). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import (
    	"bytes"
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/storage"
    )
    
    // streamFileUpload uploads an object via a stream.
    func streamFileUpload(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucket, object string) error {
    	// bucket := "bucket-name"
    	// object := "object-name"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	b := []byte("Hello world.")
    	buf := bytes.NewBuffer(b)
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*50)
    	defer cancel()
    
    	// Upload an object with storage.Writer.
    	wc := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucket).[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)(object).[NewWriter](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_NewWriter)(ctx)
    	wc.ChunkSize = 0 // note retries are not supported for chunk size 0.
    
    	if _, err = io.Copy(wc, buf); err != nil {
    		return fmt.Errorf("io.Copy: %w", err)
    	}
    	// Data can continue to be added to the file until the writer is closed.
    	if err := wc.Close(); err != nil {
    		return fmt.Errorf("Writer.Close: %w", err)
    	}
    	fmt.Fprintf(w, "%v uploaded to %v.\n", object, bucket)
    
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html);
    import com.google.cloud.storage.[BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import java.io.IOException;
    import java.nio.charset.StandardCharsets;
    
    public class UploadObjectFromMemory {
      public static void uploadObjectFromMemory(
          String projectId, String bucketName, String objectName, String contents) throws IOException {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The ID of your GCS object
        // String objectName = "your-object-name";
    
        // The string of contents you wish to upload
        // String contents = "Hello world!";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html) blobId = [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html).of(bucketName, objectName);
        [BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html) blobInfo = [BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html).newBuilder(blobId).build();
        byte[] content = contents.getBytes(StandardCharsets.UTF_8);
    
        // Optional: set a generation-match precondition to enable automatic retries, avoid potential
        // race
        // conditions and data corruptions. The request returns a 412 error if the
        // preconditions are not met.
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobTargetOption precondition;
        if (storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName, objectName) == null) {
          // For a target object that does not yet exist, set the DoesNotExist precondition.
          // This will cause the request to fail if the object is created before the request runs.
          precondition = [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobTargetOption.doesNotExist();
        } else {
          // If the destination already exists in your bucket, instead set a generation-match
          // precondition. This will cause the request to fail if the existing object's generation
          // changes before the request runs.
          precondition =
              [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobTargetOption.generationMatch(
                  storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName, objectName).getGeneration());
        }
        storage.[create](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_create_com_google_cloud_storage_BlobInfo_byte___com_google_cloud_storage_Storage_BlobTargetOption____)(blobInfo, content, precondition);
    
        System.out.println(
            "Object "
                + objectName
                + " uploaded to bucket "
                + bucketName
                + " with contents "
                + contents);
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
    
    // The contents that you want to upload
    // const contents = 'these are my contents';
    
    // The new ID for your GCS file
    // const destFileName = 'your-new-file-name';
    
    // Imports the Google Cloud Node.js client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function uploadFromMemory() {
      await storage.bucket(bucketName).file(destFileName).[save](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/file_2.html)(contents);
    
      console.log(
        `${destFileName} with contents ${contents} uploaded to ${bucketName}.`
      );
    }
    
    uploadFromMemory().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Upload an object from memory buffer.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $objectName The name of your Cloud Storage object.
     *        (e.g. 'my-object')
     * @param string $contents The contents to upload to the file.
     *        (e.g. 'these are my contents')
     */
    function upload_object_from_memory(
        string $bucketName,
        string $objectName,
        string $contents
    ): void {
        $storage = new StorageClient();
        if (!$stream = fopen('data://text/plain,' . $contents, 'r')) {
            throw new \InvalidArgumentException('Unable to open file for reading');
        }
        $bucket = $storage->bucket($bucketName);
        $bucket->upload($stream, [
            'name' => $objectName,
        ]);
        printf('Uploaded %s to gs://%s/%s' . PHP_EOL, $contents, $bucketName, $objectName);
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def upload_blob_from_memory(bucket_name, contents, destination_blob_name):
        """Uploads a file to the bucket."""
    
        # The ID of your GCS bucket
        # bucket_name = "your-bucket-name"
    
        # The contents to upload to the file
        # contents = "these are my contents"
    
        # The ID of your GCS object
        # destination_blob_name = "storage-object-name"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
        blob = bucket.blob(destination_blob_name)
    
        blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(contents)
    
        print(
            f"{destination_blob_name} with contents {contents} uploaded to {bucket_name}."
        )
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    # The ID of your GCS bucket
    # bucket_name = "your-unique-bucket-name"
    
    # The ID of your GCS object
    # file_name = "your-file-name"
    
    # The contents to upload to your file
    # file_content = "Hello, world!"
    
    require "google/cloud/storage"
    
    storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
    bucket  = storage.bucket bucket_name, skip_lookup: true
    
    file = bucket.[create_file](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) StringIO.[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)(file_content), file_name
    
    puts "Uploaded file #{file.name} to bucket #{bucket_name} with content: #{file_content}"

### Rust
    
    
    use google_cloud_storage::client::Storage;
    
    pub async fn sample(client: &Storage, bucket: &str) -> Result<(), anyhow::Error> {
        const NAME: &str = "object-to-upload.txt";
        let data: bytes::Bytes = bytes::Bytes::from("Hello, world!");
        let _result = client
            .write_object(format!("projects/_/buckets/{bucket}"), NAME, data)
            .send_unbuffered()
            .await?;
    
        println!("Uploaded to {NAME} in bucket {bucket} from memory.");
        Ok(())
    }

## What's next

  * Learn about [naming requirements for objects](https://docs.cloud.google.com/storage/docs/objects#naming).
  * [List the objects](https://docs.cloud.google.com/storage/docs/listing-objects) that have been successfully uploaded to the bucket.
  * [Control who has access](https://docs.cloud.google.com/storage/docs/access-control) to your objects and buckets.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
