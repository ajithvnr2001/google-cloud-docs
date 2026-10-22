---
url: https://docs.cloud.google.com/storage/docs/reading-objects/
title: Read objects \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:26:41.556291+00:00
---

# Read objects  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/reading-objects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Read objects Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to read object data from your Cloud Storage buckets directly into application memory or interactively in your web browser or command-line terminal. Reading objects into memory or interactively is recommended when you want to stream, inspect, or process data in a way that avoids the CPU, disk I/O, and latency overhead associated with writing files into a persistent local file system.

For instructions on downloading objects into persistent or local storage, see [Download objects](https://docs.cloud.google.com/storage/docs/downloading-objects). For a conceptual overview of object reads and downloads, see [Object reads and downloads](https://docs.cloud.google.com/storage/docs/reads-and-downloads).

## Required roles

To get the permissions that you need to read object data, ask your administrator to grant you the following IAM roles: 

  * [Storage Object Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`) on the bucket
  * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) on the project (only required for reading object data by using the Google Cloud console)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

The Storage Object Viewer (`roles/storage.objectViewer`) role contains the `storage.objects.get` permission, which is required for reading objects. The Storage Admin (`roles/storage.admin`) role contains the `storage.buckets.list` and `storage.buckets.get` permissions, in addition to the `storage.objects.get` permission. These permissions are required for listing the buckets in a project and viewing information about the buckets. The Storage Admin (`roles/storage.admin`) role that includes these permissions is only required when you want to read objects interactively using the Google Cloud console. 

You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For instructions on granting roles on buckets, see [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).

## Read objects programmatically into memory

This section describes how to read object data by streaming the object bytes directly into application memory.

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    [](gcs::Client client, std::string const& bucket_name,
       std::string const& object_name) {
      gcs::ObjectReadStream stream = client.ReadObject(bucket_name, object_name);
      std::string buffer{std::istreambuf_iterator<char>(stream),
                         std::istreambuf_iterator<char>()};
      if (stream.bad()) throw google::cloud::Status(stream.status());
    
      std::cout << "The object has " << buffer.size() << " characters\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    using System.IO;
    
    public class DownloadObjectIntoMemorySample
    {
        public Stream DownloadObjectIntoMemory(
            string bucketName = "unique-bucket-name",
            string objectName = "file-name")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            Stream stream = new MemoryStream();
            storage.DownloadObject(bucketName, objectName, stream);
    
            Console.WriteLine($"The contents of {objectName} from bucket {bucketName} are downloaded");
            return stream;
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
    
    
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import java.nio.charset.StandardCharsets;
    
    public class DownloadObjectIntoMemory {
      public static void downloadObjectIntoMemory(
          String projectId, String bucketName, String objectName) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The ID of your GCS object
        // String objectName = "your-object-name";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        byte[] content = storage.[readAllBytes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_readAllBytes_com_google_cloud_storage_BlobId_com_google_cloud_storage_Storage_BlobSourceOption____)(bucketName, objectName);
        System.out.println(
            "The contents of "
                + objectName
                + " from bucket name "
                + bucketName
                + " are: "
                + new String(content, StandardCharsets.UTF_8));
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
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function downloadIntoMemory() {
      // Downloads the file into a buffer in memory.
      const contents = await storage.bucket(bucketName).file(fileName).[download](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/file_2.html)();
    
      console.log(
        `Contents of gs://${bucketName}/${fileName} are ${contents.toString()}.`
      );
    }
    
    downloadIntoMemory().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Download an object from Cloud Storage and save into a buffer in memory.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $objectName The name of your Cloud Storage object.
     *        (e.g. 'my-object')
     */
    function download_object_into_memory(
        string $bucketName,
        string $objectName
    ): void {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
        $object = $bucket->object($objectName);
        $contents = $object->downloadAsString();
        printf(
            'Downloaded %s from gs://%s/%s' . PHP_EOL,
            $contents,
            $bucketName,
            $objectName
        );
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def download_blob_into_memory(bucket_name, blob_name):
        """Downloads a blob into memory."""
        # The ID of your GCS bucket
        # bucket_name = "your-bucket-name"
    
        # The ID of your GCS object
        # blob_name = "storage-object-name"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
    
        # Construct a client side representation of a blob.
        # Note `Bucket.blob` differs from `Bucket.get_blob` as it doesn't retrieve
        # any content from Google Cloud Storage. As we don't need additional data,
        # using `Bucket.blob` is preferred here.
        blob = bucket.blob(blob_name)
        contents = blob.[download_as_bytes](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_as_bytes)()
    
        print(
            "Downloaded storage object {} from bucket {} as the following bytes object: {}.".format(
                blob_name, bucket_name, contents.decode("utf-8")
            )
        )
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    # The name of the bucket to access
    # bucket_name = "my-bucket"
    
    # The name of the remote file to download
    # file_name = "file.txt"
    
    require "google/cloud/storage"
    
    storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
    bucket  = storage.bucket bucket_name, skip_lookup: true
    file    = bucket.[file](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) file_name
    
    downloaded = file.[download](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-File.html)
    downloaded.rewind # Optional - not needed on first read
    contents = downloaded.read
    
    puts "Contents of storage object #{file.name} in bucket #{bucket_name} are: #{contents}"

### Rust
    
    
    use google_cloud_storage::client::Storage;
    
    pub async fn sample(client: &Storage, bucket: &str) -> Result<(), anyhow::Error> {
        const NAME: &str = "object-to-download.txt";
        let mut reader = client
            .read_object(format!("projects/_/buckets/{bucket}"), NAME)
            .send()
            .await?;
    
        let mut content = Vec::new();
        while let Some(data) = reader.next().await.transpose()? {
            content.extend_from_slice(&data);
        }
    
        println!(
            "Downloaded {} bytes of object {NAME} in bucket {bucket}.",
            content.len()
        );
        Ok(())
    }

## Read objects interactively

This section describes how to read objects interactively in your Google Cloud console browser window or command-line terminal `stdout`.

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the bucket list, click the name of the bucket whose contents you want to view.

  3. On the **Objects** tab, click the name of the object you want to read.

  4. On the **Object details** page, click the public URL or the authenticated URL of the object to read its data.




### Command line

To stream an object's byte payload directly into your terminal `stdout`, use the [`gcloud storage cat`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cat) command:
    
    
    gcloud storage cat gs://BUCKET_NAME/OBJECT_NAME

Replace the following:

  * `BUCKET_NAME`: the name of the bucket that contains the object you want to read. For example, `my-bucket`.

  * `OBJECT_NAME`: the name of the object that you want to read. For example, `dog.png`.




### REST APIs

To read an object's bytes and direct the output stream to your terminal `stdout`, use the following instructions.

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use `cURL` to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with an [`objects.get`](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/get) request that includes the `-o -` option and the `alt=media` query parameter:
         
         curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -o - \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/o/OBJECT_NAME?alt=media"

Replace the following:

     * `BUCKET_NAME`: the name of the bucket that contains the object you want to read. For example, `my-bucket`.

     * `OBJECT_NAME`: the URL-encoded name of the object you want to read. For example, `pets/dog.png`, URL-encoded as `pets%2Fdog.png`.




### XML API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use `cURL` to call the [XML API](https://docs.cloud.google.com/storage/docs/xml-api/overview) with a [`GET` Object](https://docs.cloud.google.com/storage/docs/xml-api/get-object-download) request:
         
         curl -X GET \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storage.googleapis.com/BUCKET_NAME/OBJECT_NAME"

Replace the following:

     * `BUCKET_NAME`: the name of the bucket containing the object you want to read. For example, `my-bucket`.

     * `OBJECT_NAME`: the URL-encoded name of the object you want to read. For example, `pets/dog.png`, URL-encoded as `pets%2Fdog.png`.




## What's next

  * [Transfer data from cloud providers or other online sources](https://docs.cloud.google.com/storage-transfer/docs/create-manage-transfer-console), such as URL lists.


  * [Transfer objects to your Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/transfer-files#gcstransfer).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
