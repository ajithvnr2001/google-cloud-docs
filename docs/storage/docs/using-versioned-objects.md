---
url: https://docs.cloud.google.com/storage/docs/using-versioned-objects/
title: Use versioned objects \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:01.471127+00:00
---

# Use versioned objects  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/using-versioned-objects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Use versioned objects Stay organized with collections  Save and categorize content based on your preferences. 

[Overview](https://docs.cloud.google.com/storage/docs/object-versioning) [Setup](https://docs.cloud.google.com/storage/docs/using-object-versioning)

This page describes how to list, access, restore, and delete noncurrent objects, which typically applies to buckets with [Object Versioning enabled](https://docs.cloud.google.com/storage/docs/using-object-versioning). Noncurrent objects are also referred to as versioned objects.

## Before you begin

To work with noncurrent objects, complete the following prerequisite steps.

### Enable Object Versioning

If you haven't already, [enable Object Versioning](https://docs.cloud.google.com/storage/docs/using-object-versioning#set) on your bucket.

### Get required roles

To get the permissions that you need to manage noncurrent objects, ask your administrator to grant you the Storage Object User (`roles/storage.objectUser`) IAM role on the project. This [predefined role](https://docs.cloud.google.com/iam/docs/roles-permissions) contains the permissions required to manage noncurrent objects. To see the exact permissions that are required, expand the **Required permissions** section:

#### Required permissions

  * `storage.objects.create`
  * `storage.objects.delete`
  * `storage.objects.get`
  * `storage.objects.list`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

For information about granting roles on projects, see [Manage access to projects](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

Depending on your use case, you might need additional permissions or alternative roles:

  * If you plan on using the Google Cloud console to perform the tasks on this page, you'll also need the `storage.buckets.list` permission, which is not included in the Storage Object User (`roles/storage.objectUser`) role. To get this permission, ask your administrator to grant you the Storage Admin (`roles/storage.admin`) role on the project.

  * If uniform bucket-level access is disabled for your bucket, you need additional permissions in the following scenarios:

    * If you plan on returning noncurrent objects along with their ACLs, you also need the `storage.objects.getIamPolicy` permission, which is not included in the Storage Object User (`roles/storage.objectUser`) role. To get this permission, ask your administrator to grant you the Storage Object Admin (`roles/storage.objectAdmin`) role on the project.

    * If you plan on renaming or restoring noncurrent objects that have ACLs, you also need the `storage.objects.setIamPolicy` permission, which is not included in the Storage Object User (`roles/storage.objectUser`) role. To get this permission, ask your administrator to grant you the Storage Object Admin (`roles/storage.objectAdmin`) role on the project.




## List noncurrent object versions

To list both live and noncurrent versions of objects and view their [`generation` numbers](https://docs.cloud.google.com/storage/docs/metadata#generation-number):

### Console

**Note:** The Google Cloud console has a limit of 1000 versions of an object that it can list. To see more versions for an object, use the gcloud CLI.

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket that contains the wanted object.

The **Bucket details** page opens, with the **Objects** tab selected.

  3. To view noncurrent objects, click the **Show** drop-down and select **Live and noncurrent objects**.

  4. In the list of objects, click the name of the object whose versions you want to see.

The **Object details** page opens, with the **Live Object** tab selected.

  5. Click the **Version history** tab to see all versions of the object.




### Command line

Use the [`gcloud storage ls --all-versions`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/ls) command:
    
    
    gcloud storage ls --all-versions gs://BUCKET_NAME

Where `BUCKET_NAME` is the name of the bucket that contains the objects. For example, `my-bucket`.

The response looks like the following example:
    
    
    gs://BUCKET_NAME/OBJECT_NAME1#GENERATION_NUMBER1
    gs://BUCKET_NAME/OBJECT_NAME2#GENERATION_NUMBER2
    gs://BUCKET_NAME/OBJECT_NAME3#GENERATION_NUMBER3
    ...

**Note:** Use the `--long` flag along with the `--all-versions` flag to get metageneration numbers in the response. Use the `--full` flag along with the `--all-versions` flag to get the `Noncurrent Time` for noncurrent versions of an object.

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    [](gcs::Client client, std::string const& bucket_name) {
      for (auto&& object_metadata :
           client.ListObjects(bucket_name, gcs::Versions{true})) {
        if (!object_metadata) throw std::move(object_metadata).status();
    
        std::cout << "bucket_name=" << object_metadata->bucket()
                  << ", object_name=" << object_metadata->name()
                  << ", generation=" << object_metadata->generation() << "\n";
      }
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    using System.Collections.Generic;
    
    public class ListFileArchivedGenerationSample
    {
    	public IEnumerable<Google.Apis.Storage.v1.Data.Object> ListFileArchivedGeneration(string bucketName = "your-bucket-name")
    	{
    		var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
    
    		var storageObjects = storage.ListObjects(bucketName, options: new [ListObjectsOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.ListObjectsOptions.html)
    		{
    			Versions = true
    		});
    
    		foreach (var storageObject in storageObjects)
    		{
    			Console.WriteLine($"Filename: {storageObject.Name}, Generation: {storageObject.Generation}");
    		}
    
    		return storageObjects;
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
    	"google.golang.org/api/iterator"
    )
    
    // listFilesAllVersion lists both live and noncurrent versions of objects within specified bucket.
    func listFilesAllVersion(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucket string) error {
    	// bucket := "bucket-name"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    
    	it := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucket).[Objects](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Objects)(ctx, &storage.[Query](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Query){
    		// Versions true to output all generations of objects
    		Versions: true,
    	})
    	for {
    		attrs, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("Bucket(%q).Objects(): %w", bucket, err)
    		}
    		fmt.Fprintln(w, attrs.Name, attrs.[Generation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_Generation), attrs.Metageneration)
    	}
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.api.gax.paging.[Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html);
    import com.google.cloud.storage.[Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html);
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class ListObjectsWithOldVersions {
      public static void listObjectsWithOldVersions(String projectId, String bucketName) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket = storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName);
        Page<Blob> blobs = bucket.[list](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html#com_google_cloud_storage_Bucket_list_com_google_cloud_storage_Storage_BlobListOption____)(Storage.BlobListOption.versions(true));
    
        for ([Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html) blob : blobs.iterateAll()) {
          System.out.println(blob.getName() + "," + blob.getGeneration());
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
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function listFilesWithOldVersions() {
      const [files] = await storage.bucket(bucketName).[getFiles](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/bucket.html)({
        versions: true,
      });
    
      console.log('Files:');
      files.forEach(file => {
        console.log(file.name, file.generation);
      });
    }
    
    listFilesWithOldVersions().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * List objects in a specified bucket with all archived generations.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     */
    function list_file_archived_generations(string $bucketName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
    
        $objects = $bucket->objects([
            'versions' => true,
        ]);
    
        foreach ($objects as $object) {
            print($object->name() . ',' . $object->info()['generation'] . PHP_EOL);
        }
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def list_file_archived_generations(bucket_name):
        """Lists all the blobs in the bucket with generation."""
        # bucket_name = "your-bucket-name"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
        blobs = storage_client.[list_blobs](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_list_blobs)(bucket_name, versions=True)
    
        for blob in blobs:
            print(f"{blob.name},{blob.generation}")
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def list_file_archived_generations bucket_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket = storage.bucket bucket_name
    
      bucket.[files](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html).[each](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Policy-Bindings.html) do |file|
        puts "#{file.name},#{file.generation}"
      end
    end

### Rust
    
    
    use google_cloud_gax::paginator::ItemPaginator;
    use google_cloud_storage::client::StorageControl;
    
    pub async fn sample(client: &StorageControl, bucket_id: &str) -> anyhow::Result<()> {
        let mut objects = client
            .list_objects()
            .set_parent(format!("projects/_/buckets/{bucket_id}"))
            .set_versions(true)
            .by_item();
        println!("listing objects in bucket {bucket_id}");
        while let Some(object) = objects.next().await.transpose()? {
            println!("{object:?}");
        }
        println!("DONE");
        Ok(())
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](https://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with an [Objects: list](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/list) request:
         
         curl -X GET \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/o?versions=true"

Where `BUCKET_NAME` is the name of the bucket that contains the objects. For example, `my-bucket`.




Noncurrent versions of objects have a `timeDeleted` property.

### XML API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](https://curl.haxx.se/) to call the [XML API](https://docs.cloud.google.com/storage/docs/xml-api/overview), with a [`GET` Bucket](https://docs.cloud.google.com/storage/docs/xml-api/get-bucket-list) request and `versions` query string parameter:
         
         curl -X GET \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storage.googleapis.com/BUCKET_NAME?versions&list-type=2"

Where `BUCKET_NAME` is the name of the bucket that contains the objects. For example, `my-bucket`.




There are a few differences in the results of the `GET` request when using the `versions` query parameter compared to not using it. Specifically, Cloud Storage returns the following information when you include a `versions` query parameter in your request:

  * A `Version` element that contains information about each object.
  * A `DeletedTime` element that contains the time the object version became noncurrent (deleted or replaced).
  * An `IsLatest` element that indicates if the specific object is the latest version.
  * A `NextGenerationMarker` element is returned if the listing of objects is a partial listing, which occurs when you have many object versions in a bucket. Use the value of this element in the `generationmarker` query parameter of subsequent requests in order to resume from your last point. The `generationmarker` query parameter is used in the same way that you use the `marker` query parameter to page through a listing for a nonversioned bucket.



## Access noncurrent object versions

To use the noncurrent version of an object when performing tasks such as downloading the object, viewing its metadata, or updating its metadata:

### Console

General access to a noncurrent version is not available in the Google Cloud console. Using the Google Cloud console, you can only move, copy, restore or delete a noncurrent version. These actions are performed from the version history list for an object.

### Command line

  1. Append the [generation number](https://docs.cloud.google.com/storage/docs/metadata#generation-number) of the noncurrent version to the object name:
         
         OBJECT_NAME#GENERATION_NUMBER

Where:

     * `OBJECT_NAME` is the name of the noncurrent version. For example, `pets/dog.png`.
     * `GENERATION_NUMBER` is the generation number for the noncurrent version. For example, `1560468815691234`.
  2. Using the string from the previous step, proceed as you normally would for the live version of the object. For example, to view the metadata of a noncurrent object version, use the [`gcloud storage objects describe`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/objects/describe) command:
         
         gcloud storage objects describe gs://my-bucket/pets/dog.png#1560468815691234




### REST APIs

### JSON API

  1. Append the [generation number](https://docs.cloud.google.com/storage/docs/metadata#generation-number) of the noncurrent version to the URI for the object:
         
         https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/o/OBJECT_NAME?generation=GENERATION_NUMBER

Where:

     * `BUCKET_NAME` is the name of the bucket containing the noncurrent version. For example, `my-bucket`.
     * `OBJECT_NAME` is the URL-encoded name of the noncurrent version. For example, `pets/dog.png`, URL-encoded as `pets%2Fdog.png`.
     * `GENERATION_NUMBER` is the generation number for the noncurrent version. For example, `1560468815691234`.
  2. Using the URI from the previous step, proceed as you normally would for the live version of the object. For example, to view the metadata of a noncurrent object version, use [cURL](https://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with an [Objects: get](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/get) request:
         
         curl -X GET \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storage.googleapis.com/storage/v1/b/my-bucket/o/pets/dog.png?generation=1560468815691234"




### XML API

  1. Append the [generation number](https://docs.cloud.google.com/storage/docs/metadata#generation-number) of the noncurrent version to the URI for the object:
         
         https://storage.googleapis.com/BUCKET_NAME/OBJECT_NAME?generation=GENERATION_NUMBER

Where:

     * `BUCKET_NAME` is the name of the bucket containing the noncurrent version. For example, `my-bucket`.
     * `OBJECT_NAME` is the URL-encoded name of the noncurrent version. For example, `pets/dog.png`, URL-encoded as `pets%2Fdog.png`.
     * `GENERATION_NUMBER` is the generation number for the noncurrent version. For example, `1560468815691234`.
  2. Using the URI from the previous step, proceed as you normally would for the live version of the object. For example, to view the metadata of a noncurrent object version, use [`cURL`](https://curl.haxx.se/) to call the [XML API](https://docs.cloud.google.com/storage/docs/xml-api/overview) with a [`HEAD` Object](https://docs.cloud.google.com/storage/docs/xml-api/head-object) request:
         
         curl -I GET \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storage.googleapis.com/my-bucket/pets/dog.png?generation=1560468815691234"




**Note:** You cannot make requests that overwrite or rewrite a noncurrent object, because Cloud Storage does not support specifying a generation number for the destination object.

## Restore noncurrent object versions

In Cloud Storage, restoring a noncurrent object version means making a copy of it. When you do so, the copy becomes the live version, effectively restoring the version. If there is already a live version and the bucket has Object Versioning enabled, restoring the noncurrent version causes the pre-existing live version to become noncurrent.

### Console

**Note:** The Google Cloud console has a limit of 1000 versions of an object that it can list.

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket that contains the wanted object.

The **Bucket details** page opens, with the **Objects** tab selected.

  3. To view noncurrent objects, click the **Show** drop-down and select **Live and noncurrent objects**.

  4. In the list of objects, click the name of the object version you want to restore.

The **Object details** page opens, with the **Live Object** tab selected.

  5. Click the **Version history** tab.

  6. Click the **Restore** button for the wanted version.

The restore object version pane opens.

  7. Click **Confirm**.




### Command line

Use the [`gcloud storage cp`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cp) command:
    
    
    gcloud storage cp gs://BUCKET_NAME/OBJECT_NAME#GENERATION_NUMBER gs://BUCKET_NAME

Where:

  * `BUCKET_NAME` is the name of the bucket containing the noncurrent version you want to restore. For example, `my-bucket`.
  * `OBJECT_NAME` is the name of the noncurrent version you want to restore. For example, `pets/dog.png`.
  * `GENERATION_NUMBER` is the [generation number](https://docs.cloud.google.com/storage/docs/metadata#generation-number) for the noncurrent version you want to restore. For example, `1560468815691234`.



If successful, the response looks like the following example:
    
    
    Operation completed over 1 objects/58.8 KiB.

**Note:** Some shells, such as zsh when the `extendedglob` option is enabled, treat the hash character, `#`, as a special character. If this is the case for your shell, you should enclose that argument in single quotes (or double quotes for Windows).

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& source_bucket_name,
       std::string const& source_object_name,
       std::string const& destination_bucket_name,
       std::string const& destination_object_name,
       std::int64_t source_object_generation) {
      StatusOr<gcs::ObjectMetadata> copy =
          client.CopyObject(source_bucket_name, source_object_name,
                            destination_bucket_name, destination_object_name,
                            gcs::SourceGeneration{source_object_generation});
      if (!copy) throw std::move(copy).status();
    
      std::cout << "Successfully copied " << source_object_name << " generation "
                << source_object_generation << " in bucket " << source_bucket_name
                << " to bucket " << copy->bucket() << " with name "
                << copy->name()
                << ".\nThe full metadata after the copy is: " << *copy << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class CopyFileArchivedGenerationSample
    {
        public Google.Apis.Storage.v1.Data.Object CopyFileArchivedGeneration(
            string sourceBucketName = "source-bucket-name",
            string sourceObjectName = "source-file",
            string destBucketName = "destination-bucket-name",
            string destObjectName = "destination-file-name",
            long? generation = 1579287380533984)
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var copyOptions = new [CopyObjectOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.CopyObjectOptions.html)
            {
                SourceGeneration = generation
            };
    
            var copiedFile = storage.CopyObject(sourceBucketName, sourceObjectName,
                destBucketName, destObjectName, copyOptions);
    
            Console.WriteLine($"Generation {generation} of the object {sourceBucketName}/{sourceObjectName} " +
                $"was copied to to {destBucketName}/{destObjectName}.");
    
            return copiedFile;
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
    
    // copyOldVersionOfObject copies a noncurrent version of an object.
    func copyOldVersionOfObject(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucket, srcObject, dstObject string, gen int64) error {
    	// bucket := "bucket-name"
    	// srcObject := "source-object-name"
    	// dstObject := "destination-object-name"
    
    	// gen is the generation of srcObject to copy.
    	// gen := 1587012235914578
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    
    	src := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucket).[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)(srcObject)
    	dst := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucket).[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)(dstObject)
    
    	// Optional: set a generation-match precondition to avoid potential race
    	// conditions and data corruptions. The request to copy is aborted if the
    	// object's generation number does not match your precondition.
    	// For a dst object that does not yet exist, set the DoesNotExist precondition.
    	dst = dst.If(storage.[Conditions](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Conditions){DoesNotExist: true})
    	// If the destination object already exists in your bucket, set instead a
    	// generation-match precondition using its generation number.
    	// attrs, err := dst.Attrs(ctx)
    	// if err != nil {
    	// 	return fmt.Errorf("object.Attrs: %w", err)
    	// }
    	// dst = dst.If(storage.Conditions{GenerationMatch: attrs.Generation})
    
    	if _, err := dst.[CopierFrom](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_CopierFrom)(src.[Generation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_Generation)(gen)).Run(ctx); err != nil {
    		return fmt.Errorf("Object(%q).CopierFrom(%q).Generation(%v).Run: %w", dstObject, srcObject, gen, err)
    	}
    	fmt.Fprintf(w, "Generation %v of object %v in bucket %v was copied to %v\n", gen, srcObject, bucket, dstObject)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class CopyOldVersionOfObject {
      public static void copyOldVersionOfObject(
          String projectId,
          String bucketName,
          String objectToCopy,
          long generationToCopy,
          String newObjectName) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The ID of the GCS object to copy an old version of
        // String objectToCopy = "your-object-name";
    
        // The generation of objectToCopy to copy
        // long generationToCopy = 1579287380533984;
    
        // What to name the new object with the old data from objectToCopy
        // String newObjectName = "your-new-object";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
    
        // Optional: set a generation-match precondition to avoid potential race
        // conditions and data corruptions. The request returns a 412 error if the
        // preconditions are not met.
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobTargetOption precondition;
        if (storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName, newObjectName) == null) {
          // For a target object that does not yet exist, set the DoesNotExist precondition.
          // This will cause the request to fail if the object is created before the request runs.
          precondition = [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobTargetOption.doesNotExist();
        } else {
          // If the destination already exists in your bucket, instead set a generation-match
          // precondition. This will cause the request to fail if the existing object's generation
          // changes before the request runs.
          precondition =
              [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobTargetOption.generationMatch(
                  storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName, newObjectName).getGeneration());
        }
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).[CopyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.CopyRequest.html) copyRequest =
            [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).CopyRequest.newBuilder()
                .setSource([BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html).of(bucketName, objectToCopy, generationToCopy))
                .setTarget([BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html).of(bucketName, newObjectName), precondition)
                .build();
        storage.[copy](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_copy_com_google_cloud_storage_Storage_CopyRequest_)([copy](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_copy_com_google_cloud_storage_Storage_CopyRequest_)Request);
    
        System.out.println(
            "Generation "
                + generationToCopy
                + " of object "
                + objectToCopy
                + " in bucket "
                + bucketName
                + " was copied to "
                + newObjectName);
      }
    }

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The ID of your GCS bucket
    // const srcBucketName = "your-unique-bucket-name";
    
    // The ID of the GCS file to copy an old version of
    // const srcFilename = "your-file-name";
    
    // The generation of fileToCopy to copy
    // const generation = 1579287380533984;
    
    // The ID of the bucket to copy the file to
    // const destBucketName = 'target-file-bucket';
    
    // What to name the new file with the old data from srcFilename
    // const destFileName = "your-new-file";
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function copyOldVersionOfFile() {
      // Copies the file to the other bucket
    
      // Optional:
      // Set a generation-match precondition to avoid potential race conditions
      // and data corruptions. The request to copy is aborted if the object's
      // generation number does not match your precondition. For a destination
      // object that does not yet exist, set the ifGenerationMatch precondition to 0
      // If the destination object already exists in your bucket, set instead a
      // generation-match precondition using its generation number.
      const copyOptions = {
        preconditionOpts: {
          ifGenerationMatch: destinationGenerationMatchPrecondition,
        },
      };
    
      await storage
        .bucket(srcBucketName)
        .file(srcFilename, {
          generation,
        })
        .[copy](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/file_2.html)(storage.bucket(destBucketName).file(destFileName), copyOptions);
    
      console.log(
        `Generation ${generation} of file ${srcFilename} in bucket ${srcBucketName} was copied to ${destFileName} in bucket ${destBucketName}`
      );
    }
    
    copyOldVersionOfFile().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Copy archived generation of a given object to a new object.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $objectToCopy The name of the object to copy.
     *        (e.g. 'my-object')
     * @param string $generationToCopy The generation of the object to copy.
     *        (e.g. 1579287380533984)
     * @param string $newObjectName The name of the target object.
     *        (e.g. 'my-object-1579287380533984')
     */
    function copy_file_archived_generation(string $bucketName, string $objectToCopy, string $generationToCopy, string $newObjectName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
    
        $object = $bucket->object($objectToCopy, [
            'generation' => $generationToCopy,
        ]);
    
        $object->copy($bucket, [
            'name' => $newObjectName,
        ]);
    
        printf(
            'Generation %s of object %s in bucket %s was copied to %s',
            $generationToCopy,
            $objectToCopy,
            $bucketName,
            $newObjectName
        );
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def copy_file_archived_generation(
            bucket_name, blob_name, destination_bucket_name, destination_blob_name, generation
    ):
        """Copies a blob from one bucket to another with a new name with the same generation."""
        # bucket_name = "your-bucket-name"
        # blob_name = "your-object-name"
        # destination_bucket_name = "destination-bucket-name"
        # destination_blob_name = "destination-object-name"
        # generation = 1579287380533984
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
        source_bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
        source_blob = source_bucket.blob(blob_name)
        destination_bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(destination_bucket_name)
    
        # Optional: set a generation-match precondition to avoid potential race conditions
        # and data corruptions. The request to copy is aborted if the object's
        # generation number does not match your precondition. For a destination
        # object that does not yet exist, set the if_generation_match precondition to 0.
        # If the destination object already exists in your bucket, set instead a
        # generation-match precondition using its generation number.
        destination_generation_match_precondition = 0
    
        # source_generation selects a specific revision of the source object, as opposed to the latest version.
        blob_copy = source_bucket.[copy_blob](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_copy_blob)(
            source_blob, destination_bucket, destination_blob_name, source_generation=generation, if_generation_match=destination_generation_match_precondition
        )
    
        print(
            "Generation {} of the blob {} in bucket {} copied to blob {} in bucket {}.".format(
                generation,
                source_blob.name,
                source_bucket.name,
                blob_copy.name,
                destination_bucket.name,
            )
        )
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def copy_file_archived_generation source_bucket_name:,
                                      source_file_name:,
                                      generation:,
                                      destination_bucket_name:,
                                      destination_file_name:
      # The ID of the bucket the original object is in
      # source_bucket_name = "source-bucket-name"
    
      # The ID of the GCS object to copy
      # source_file_name = "source-file-name"
    
      # The generation of your GCS object to copy
      # generation = 1579287380533984
    
      # The ID of the bucket to copy the object to
      # destination_bucket_name = "destination-bucket-name"
    
      # The ID of the new GCS object
      # destination_file_name = "destination-file-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
    
      source_bucket = storage.bucket source_bucket_name, skip_lookup: true
      source_file = source_bucket.[file](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) source_file_name
      destination_bucket = storage.bucket destination_bucket_name, skip_lookup: true
    
      destination_file = source_file.[copy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-File.html) destination_bucket, destination_file_name, generation: generation
    
      puts "Generation #{generation} of the file #{source_file.name} in bucket #{source_bucket.name} copied to file " \
           "#{destination_file.name} in bucket #{destination_bucket.name}"
    end

### Rust
    
    
    use google_cloud_storage::builder_ext::RewriteObjectExt;
    use google_cloud_storage::client::StorageControl;
    
    pub async fn sample(
        client: &StorageControl,
        source_bucket_id: &str,
        dest_bucket_id: &str,
        generation: i64,
    ) -> anyhow::Result<()> {
        const SOURCE_NAME: &str = "object-generation-to-copy";
        const DEST_NAME: &str = "copied-object";
        let copied = client
            .rewrite_object()
            .set_source_bucket(format!("projects/_/buckets/{source_bucket_id}"))
            .set_source_object(SOURCE_NAME)
            .set_source_generation(generation)
            .set_destination_bucket(format!("projects/_/buckets/{dest_bucket_id}"))
            .set_destination_name(DEST_NAME)
            .rewrite_until_done()
            .await?;
        println!(
            "successfully copied {source_bucket_id}/{SOURCE_NAME} to {dest_bucket_id}/{DEST_NAME}: {copied:?}"
        );
        Ok(())
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](https://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`POST` Object](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/rewrite) request:
         
         curl -X POST \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Length: 0" \
           "https://storage.googleapis.com/upload/storage/v1/b/BUCKET_NAME/o/OBJECT_NAME/rewriteTo/b/BUCKET_NAME/o/OBJECT_NAME?sourceGeneration=GENERATION_NUMBER"

Where:

     * `BUCKET_NAME` is the name of the bucket containing the noncurrent version you want to restore. For example, `my-bucket`.
     * `OBJECT_NAME` is the URL-encoded name of the noncurrent version you want to restore. For example, `pets/dog.png`, URL-encoded as `pets%2Fdog.png`.
     * `GENERATION_NUMBER` is the [generation number](https://docs.cloud.google.com/storage/docs/metadata#generation-number) for the noncurrent version you want to restore. For example, `1560468815691234`.



### XML API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](https://curl.haxx.se/) to call the [XML API](https://docs.cloud.google.com/storage/docs/xml-api/overview), with a [`PUT` Object](https://docs.cloud.google.com/storage/docs/xml-api/put-object-copy) request:
         
         curl -X PUT \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "x-goog-copy-source: BUCKET_NAME/OBJECT_NAME" \
           -H "x-goog-copy-source-generation:GENERATION_NUMBER" \
           "https://storage.googleapis.com/BUCKET_NAME/OBJECT_NAME"

Where:

     * `BUCKET_NAME` is the name of the bucket containing the noncurrent version you want to restore. For example, `my-bucket`.
     * `OBJECT_NAME` is the URL-encoded name of the noncurrent version you want to restore. For example, `pets/dog.png`, URL-encoded as `pets%2Fdog.png`.
     * `GENERATION_NUMBER` is the [generation number](https://docs.cloud.google.com/storage/docs/metadata#generation-number) for the noncurrent version you want to restore. For example, `1560468815691234`.



After restoring the object version, the original noncurrent version continues to exist in the bucket. If you no longer need the noncurrent version, you can subsequently delete it or configure [Object Lifecycyle Management](https://docs.cloud.google.com/storage/docs/lifecycle) to remove it when it meets the conditions you specify.

## Delete noncurrent object versions

### Console

**Note:** The Google Cloud console has a limit of 1000 versions of an object that it can list.

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket that contains the wanted object.

The **Bucket details** page opens, with the **Objects** tab selected.

  3. To view noncurrent objects, click the **Show** drop-down and select **Live and noncurrent objects**.

  4. Navigate to the object, which may be located in a folder.

  5. In the list of objects, click the name of the object whose version you want to delete.

The **Object details** page opens, with the **Live Object** tab selected.

  6. Click the **Version history** tab.

  7. Select the checkbox for the wanted version.

  8. Click the **Delete** button.

The delete version pane opens.

  9. Confirm you want to delete the object by typing `delete` into the text field.

  10. Click **Delete**.




### Command line

Use the [`gcloud storage rm`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/rm) command:
    
    
    gcloud storage rm gs://BUCKET_NAME/OBJECT_NAME#GENERATION_NUMBER

Where:

  * `BUCKET_NAME` is the name of the bucket containing the noncurrent version you want to delete. For example, `my-bucket`.
  * `OBJECT_NAME` is the name of the noncurrent version you want to delete. For example, `pets/dog.png`.
  * `GENERATION_NUMBER` is the [generation number](https://docs.cloud.google.com/storage/docs/metadata#generation-number) for the noncurrent version you want to delete. For example, `1560468815691234`.



If successful, the response looks like the following example:
    
    
    Operation completed over 1 objects.

**Note:** You can remove **all** versions of an object, including live and noncurrent versions, by using the `--all-versions` flag and omitting the `#GENERATION_NUMBER`. You can remove **all** versions of **all** objects (and potentially the bucket itself) by using the `--recursive` flag.

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    [](gcs::Client client, std::string const& bucket_name,
       std::string const& object_name, std::int64_t object_generation) {
      google::cloud::Status status = client.DeleteObject(
          bucket_name, object_name, gcs::Generation{object_generation});
      if (!status.ok()) throw std::runtime_error(status.message());
    
      std::cout << "Deleted " << object_name << " generation "
                << object_generation << " in bucket " << bucket_name << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class DeleteFileArchivedGenerationSample
    {
        public void DeleteFileArchivedGeneration(
            string bucketName = "your-bucket-name",
            string objectName = "your-object-name",
            long? generation = 1579287380533984)
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
    
            storage.DeleteObject(bucketName, objectName, new [DeleteObjectOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.DeleteObjectOptions.html)
            {
                Generation = generation
            });
    
            Console.WriteLine($"Generation ${generation} of file {objectName} was deleted from bucket {bucketName}.");
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
    
    // deleteOldVersionOfObject deletes a noncurrent version of an object.
    func deleteOldVersionOfObject(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucketName, objectName string, gen int64) error {
    	// bucketName := "bucket-name"
    	// objectName := "object-name"
    
    	// gen is the generation of objectName to delete.
    	// gen := 1587012235914578
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    
    	obj := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucketName).[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)(objectName)
    	if err := obj.[Generation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_Generation)(gen).Delete(ctx); err != nil {
    		return fmt.Errorf("Bucket(%q).Object(%q).Generation(%v).Delete: %w", bucketName, objectName, gen, err)
    	}
    	fmt.Fprintf(w, "Generation %v of object %v was deleted from %v\n", gen, objectName, bucketName)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class DeleteOldVersionOfObject {
      public static void deleteOldVersionOfObject(
          String projectId, String bucketName, String objectName, long generationToDelete) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The ID of your GCS object
        // String objectName = "your-object-name";
    
        // The generation of objectName to delete
        // long generationToDelete = 1579287380533984;
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        storage.[delete](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_delete_com_google_cloud_storage_BlobId_)(BlobId.of(bucketName, objectName, generationToDelete));
    
        System.out.println(
            "Generation "
                + generationToDelete
                + " of object "
                + objectName
                + " was deleted from "
                + bucketName);
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
    
    // The generation of fileName to delete
    // const generation = 1579287380533984;
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function deleteOldVersionOfFile() {
      // Deletes the file from the bucket with given version
      await storage
        .bucket(bucketName)
        .file(fileName, {
          generation,
        })
        .delete();
    
      console.log(
        `Generation ${generation} of file ${fileName} was deleted from ${bucketName}`
      );
    }
    
    deleteOldVersionOfFile().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Delete an archived generation of the given object.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $objectName The name of your Cloud Storage object.
     *        (e.g. 'my-object')
     * @param string $generationToDelete the generation of the object to delete.
     *        (e.g. 1579287380533984)
     */
    function delete_file_archived_generation(string $bucketName, string $objectName, string $generationToDelete): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
    
        $object = $bucket->object($objectName, [
            'generation' => $generationToDelete,
        ]);
    
        $object->delete();
    
        printf(
            'Generation %s of object %s was deleted from %s',
            $generationToDelete,
            $objectName,
            $bucketName
        );
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def delete_file_archived_generation(bucket_name, blob_name, generation):
        """Delete a blob in the bucket with the given generation."""
        # bucket_name = "your-bucket-name"
        # blob_name = "your-object-name"
        # generation = 1579287380533984
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
        bucket = storage_client.[get_bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_get_bucket)(bucket_name)
        bucket.[delete_blob](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_delete_blob)(blob_name, generation=generation)
        print(
            f"Generation {generation} of blob {blob_name} was deleted from {bucket_name}"
        )
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def delete_file_archived_generation bucket_name:, file_name:, generation:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      # The ID of your GCS object
      # file_name = "your-file-name"
    
      # The generation of the file to delete
      # generation = 1579287380533984
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket = storage.bucket bucket_name, skip_lookup: true
    
      file = bucket.[file](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) file_name
    
      file.delete generation: generation
    
      puts "Generation #{generation} of file #{file_name} was deleted from #{bucket_name}"
    end

### Rust
    
    
    use google_cloud_storage::client::StorageControl;
    
    pub async fn sample(
        client: &StorageControl,
        bucket_id: &str,
        generation: i64,
    ) -> anyhow::Result<()> {
        const NAME: &str = "object-generation-to-delete";
        client
            .delete_object()
            .set_bucket(format!("projects/_/buckets/{bucket_id}"))
            .set_object(NAME)
            .set_generation(generation)
            .send()
            .await?;
        println!("successfully deleted object {NAME} in bucket {bucket_id}");
        Ok(())
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](https://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`DELETE` Object](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/delete) request:
         
         curl -X DELETE \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/o/OBJECT_NAME?generation=GENERATION_NUMBER"

Where:

     * `BUCKET_NAME` is the name of the bucket containing the noncurrent version you want to delete. For example, `my-bucket`.
     * `OBJECT_NAME` is the URL-encoded name of the noncurrent version you want to delete. For example, `pets/dog.png`, URL-encoded as `pets%2Fdog.png`.
     * `GENERATION_NUMBER` is the [generation number](https://docs.cloud.google.com/storage/docs/metadata#generation-number) for the noncurrent version you want to delete. For example, `1560468815691234`.



### XML API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](https://curl.haxx.se/) to call the [XML API](https://docs.cloud.google.com/storage/docs/xml-api/overview), with a [`DELETE` Object](https://docs.cloud.google.com/storage/docs/xml-api/delete-object) request:
         
         curl -X DELETE \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storage.googleapis.com/BUCKET_NAME/OBJECT_NAME?generation=GENERATION_NUMBER"

Where:

     * `BUCKET_NAME` is the name of the bucket containing the noncurrent version you want to delete. For example, `my-bucket`.
     * `OBJECT_NAME` is the URL-encoded name of the noncurrent version you want to delete. For example, `pets/dog.png`, URL-encoded as `pets%2Fdog.png`.
     * `GENERATION_NUMBER` is the [generation number](https://docs.cloud.google.com/storage/docs/metadata#generation-number) for the noncurrent version you want to delete. For example, `1560468815691234`.



## What's next

  * Learn more about [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning), including an [in-depth example](https://docs.cloud.google.com/storage/docs/object-versioning#example).
  * Learn how to [disable Object Versioning](https://docs.cloud.google.com/storage/docs/using-object-versioning) on a bucket.
  * Learn how to [use Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/managing-lifecycles) to automatically manage object versions.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
