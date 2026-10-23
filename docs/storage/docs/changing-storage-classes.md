---
url: https://docs.cloud.google.com/storage/docs/changing-storage-classes/
title: Change object storage classes \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:08.284936+00:00
---

# Change object storage classes  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/changing-storage-classes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Change object storage classes Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to change the [storage class](https://docs.cloud.google.com/storage/docs/storage-classes) of objects within a bucket through rewriting the object.

  * To learn how to change object storage classes without rewriting an object, see the [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle) feature.
  * To learn how Cloud Storage can automatically manage your object's storage classes, see the [Autoclass feature](https://docs.cloud.google.com/storage/docs/autoclass).



## Required roles

In order to get the required permissions for changing the storage class of an object through rewriting the object, ask your administrator to grant you the Storage Object User (`roles/storage.objectUser`) role on the bucket.

This role contains the permissions required to change the storage class of an object. To see the exact permissions that are required, expand the **Required permissions** section:

#### Required permissions

  * `storage.objects.create`
  * `storage.objects.delete`
  * `storage.objects.get`
  * `storage.objects.list`



You might also be able to get these permissions with other [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles) or [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

For instructions on granting roles on buckets, see [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).

## Change an object's storage class

Complete the following steps to change an object's storage class:

### Console

Individual object storage classes cannot be set through the [Google Cloud console](https://docs.cloud.google.com/storage/docs/lifecycle-configurations#change_an_objects_storage_class). Instead, use the Google Cloud CLI.

### Command line

Use the [`gcloud storage objects update`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/objects/update) command with the `--storage-class` flag. For example:
    
    
    gcloud storage objects update gs://BUCKET_NAME/OBJECT_NAME --storage-class=STORAGE_CLASS

Where:

  * `BUCKET_NAME` is the name of the bucket containing the object whose class you want to change. For example, `my-bucket`.
  * `OBJECT_NAME` is the name of the object whose class you want to change. For example, `pets/dog.png`.
  * `STORAGE_CLASS` is the new [storage class](https://docs.cloud.google.com/storage/docs/storage-classes) for your object. For example, `nearline`.



### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name,
       std::string const& object_name, std::string const& storage_class) {
      StatusOr<gcs::ObjectMetadata> object_metadata =
          client.RewriteObjectBlocking(
              bucket_name, object_name, bucket_name, object_name,
              gcs::WithObjectMetadata(
                  gcs::ObjectMetadata().set_storage_class(storage_class)));
      if (!object_metadata) throw std::move(object_metadata).status();
    
      std::cout << "Changed storage class of object " << object_metadata->name()
                << " in bucket " << object_metadata->bucket() << " to "
                << object_metadata->storage_class() << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class ChangeFileStorageClassSample
    {
        public Google.Apis.Storage.v1.Data.Object ChangeFileStorageClass(
            string bucketName = "your-bucket-name",
            string objectName = "your-object-name",
            string storageClass = [StorageClasses](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClasses.html).[Standard](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClasses.html#Google_Cloud_Storage_V1_StorageClasses_Standard))
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
    
            // Changing storage class requires a rewrite operation, which can only be done
            // by the underlying service
            var obj = new Google.Apis.Storage.v1.Data.Object { StorageClass = storageClass };
            storage.Service.Objects.Rewrite(obj, bucketName, objectName, bucketName, objectName).Execute();
    
            var file = storage.GetObject(bucketName, objectName);
            Console.WriteLine($"Object {objectName} in bucket {bucketName} had" +
                $" its storage class set to {storageClass}.");
    
            return file;
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
    
    // changeObjectStorageClass changes the storage class of a single object.
    func changeObjectStorageClass(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucket, object string) error {
    	// bucket := "bucket-name"
    	// object := "object-name"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    
    	o := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucket).[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)(object)
    
    	// Optional: set a generation-match precondition to avoid potential race
    	// conditions and data corruptions. The request to copy is aborted if the
    	// object's generation number does not match your precondition.
    	attrs, err := o.Attrs(ctx)
    	if err != nil {
    		return fmt.Errorf("object.Attrs: %w", err)
    	}
    	o = o.If(storage.[Conditions](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Conditions){GenerationMatch: attrs.[Generation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_Generation)})
    
    	// See the StorageClass documentation for other valid storage classes:
    	// https://cloud.google.com/storage/docs/storage-classes
    	newStorageClass := "COLDLINE"
    	// You can't change an object's storage class directly, the only way is
    	// to rewrite the object with the desired storage class.
    	copier := o.[CopierFrom](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_CopierFrom)(o)
    	copier.StorageClass = newStorageClass
    	if _, err := copier.Run(ctx); err != nil {
    		return fmt.Errorf("copier.Run: %w", err)
    	}
    	fmt.Fprintf(w, "Object %v in bucket %v had its storage class set to %v\n", object, bucket, newStorageClass)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html);
    import com.google.cloud.storage.[BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html);
    import com.google.cloud.storage.[BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageClass.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class ChangeObjectStorageClass {
      public static void changeObjectStorageClass(
          String projectId, String bucketName, String objectName) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The ID of your GCS object
        // String objectName = "your-object-name";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html) blobId = [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html).of(bucketName, objectName);
        [Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html) sourceBlob = storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(blobId);
        if (sourceBlob == null) {
          System.out.println("The object " + objectName + " wasn't found in " + bucketName);
          return;
        }
    
        // See the StorageClass documentation for other valid storage classes:
        // https://googleapis.dev/java/google-cloud-clients/latest/com/google/cloud/storage/StorageClass.html
        [StorageClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageClass.html) storageClass = [StorageClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageClass.html).COLDLINE;
    
        // You can't change an object's storage class directly, the only way is to rewrite the object
        // with the desired storage class
    
        [BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html) targetBlob = [BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html).newBuilder(blobId).setStorageClass(storageClass).build();
    
        // Optional: set a generation-match precondition to avoid potential race
        // conditions and data corruptions. The request to upload returns a 412 error if
        // the object's generation number does not match your precondition.
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobSourceOption precondition =
            [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobSourceOption.generationMatch(sourceBlob.getGeneration());
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).[CopyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.CopyRequest.html) request =
            [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).CopyRequest.newBuilder()
                .setSource(blobId)
                .setSourceOptions(precondition) // delete this line to run without preconditions
                .setTarget(targetBlob)
                .build();
        [Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html) updatedBlob = storage.[copy](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_copy_com_google_cloud_storage_Storage_CopyRequest_)(request).getResult();
    
        System.out.println(
            "Object "
                + objectName
                + " in bucket "
                + bucketName
                + " had its storage class set to "
                + updatedBlob.getStorageClass().[name](https://docs.cloud.google.com/java/docs/reference/google-cloud-nio/latest/com.google.cloud.storage.contrib.nio.CloudStorageFileAttributeView.html#com_google_cloud_storage_contrib_nio_CloudStorageFileAttributeView_name__)());
      }
    }

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The ID of your GCS bucket
    // const bucketName = 'your-unique-bucket-name';
    
    // The ID of your GCS file
    // const fileName = 'your-file-name';
    
    // The name of a storage class
    // See the StorageClass documentation for other valid storage classes:
    // https://googleapis.dev/java/google-cloud-clients/latest/com/google/cloud/storage/StorageClass.html
    // const storageClass = 'coldline';
    
    async function fileChangeStorageClass() {
      // Optional:
      // Set a generation-match precondition to avoid potential race conditions
      // and data corruptions. The request to copy is aborted if the object's
      // generation number does not match your precondition. For a destination
      // object that does not yet exist, set the ifGenerationMatch precondition to 0
      // If the destination object already exists in your bucket, set instead a
      // generation-match precondition using its generation number.
      const setStorageClassOptions = {
        ifGenerationMatch: generationMatchPrecondition,
      };
    
      await storage
        .bucket(bucketName)
        .file(fileName)
        .setStorageClass(storageClass, setStorageClassOptions);
    
      console.log(`${fileName} has been set to ${storageClass}`);
    }
    
    fileChangeStorageClass().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Change the storage class of the given file.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $objectName The name of your Cloud Storage object.
     *        (e.g. 'my-object')
     * @param string $storageClass The storage class of the new object.
     *        (e.g. 'COLDLINE')
     */
    function change_file_storage_class(string $bucketName, string $objectName, string $storageClass): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
        $object = $bucket->object($objectName);
    
        // Storage class cannot be changed directly. But we can rewrite the object
        // using the new storage class.
    
        $newObject = $object->rewrite($bucket, [
            'storageClass' => $storageClass,
        ]);
    
        printf(
            'Object %s in bucket %s had its storage class set to %s',
            $objectName,
            $bucketName,
            $newObject->info()['storageClass']
        );
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def change_file_storage_class(bucket_name, blob_name):
        """Change the default storage class of the blob"""
        # bucket_name = "your-bucket-name"
        # blob_name = "your-object-name"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
        blob = bucket.blob(blob_name)
        generation_match_precondition = None
    
        # Optional: set a generation-match precondition to avoid potential race
        # conditions and data corruptions. The request is aborted if the
        # object's generation number does not match your precondition.
        blob.reload()  # Fetch blob metadata to use in generation_match_precondition.
        generation_match_precondition = blob.generation
    
        blob.[update_storage_class](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_update_storage_class)("NEARLINE", if_generation_match=generation_match_precondition)
    
        print(
            "Blob {} in bucket {} had its storage class set to {}".format(
                blob_name,
                bucket_name,
                blob.storage_class
            )
        )
        return blob

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def change_file_storage_class bucket_name:, file_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      # The ID of your GCS object
      # file_name = "your-file-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket = storage.bucket bucket_name, skip_lookup: true
    
      file = bucket.[file](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) file_name
    
      file.storage_class = "NEARLINE"
    
      puts "File #{file_name} in bucket #{bucket_name} had its storage class set to #{file.storage_class}"
    end

### Rust
    
    
    use google_cloud_storage::builder_ext::RewriteObjectExt;
    use google_cloud_storage::client::StorageControl;
    use google_cloud_storage::model::Object;
    
    pub async fn sample(client: &StorageControl, bucket_id: &str) -> anyhow::Result<()> {
        const NAME: &str = "update-storage-class";
        let updated = client
            .rewrite_object()
            .set_source_bucket(format!("projects/_/buckets/{bucket_id}"))
            .set_source_object(NAME)
            .set_destination_bucket(format!("projects/_/buckets/{bucket_id}"))
            .set_destination_name(NAME)
            // For other valid storage classes, refer to the documentation:
            // https://cloud.google.com/storage/docs/storage-classes
            .set_destination(Object::new().set_storage_class("NEARLINE"))
            .rewrite_until_done()
            .await?;
        println!(
            "successfully updated storage class for object {NAME} in bucket {bucket_id}: {updated:?}"
        );
        Ok(())
    }

### REST APIs

### JSON API

**Caution:** ACLs that you want to retain from the original object must be included in the object resource that you provide in the request body.

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the following information:
         
         {
           "storageClass": "STORAGE_CLASS"
         }

Where:

     * `STORAGE_CLASS` is the new [storage class](https://docs.cloud.google.com/storage/docs/storage-classes) for your object. For example, `nearline`.
  3. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`POST` Object](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/rewrite), request:
         
         curl -X POST --data-binary @JSON_FILE_NAME \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/o/OBJECT_NAME/rewriteTo/b/BUCKET_NAME/o/OBJECT_NAME"

Where:

     * `JSON_FILE_NAME` is the path for the JSON file that you created in Step 2.
     * `BUCKET_NAME` is the name of the bucket containing the original object. For example, `my-bucket`.
     * `OBJECT_NAME` is the URL-encoded name of the object. For example, `pets/dog.png`, URL-encoded as `pets%2Fdog.png`.



### XML API

**Caution:** Metadata that you want to retain from the original object, such as custom metadata, must be included in the headers that you provide in the request. Additionally, any ACLs for the object that differ from the containing bucket's default object ACLs must be reapplied after the object is uploaded.

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [XML API](https://docs.cloud.google.com/storage/docs/xml-api/overview) with a [`PUT` Object](https://docs.cloud.google.com/storage/docs/xml-api/put-object-upload) request:
         
         curl -X PUT --data-binary @OBJECT \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: OBJECT_CONTENT_TYPE" \
           -H "x-goog-storage-class: STORAGE_CLASS" \
           "https://storage.googleapis.com/BUCKET_NAME/OBJECT_NAME"

Where:

     * `OBJECT` is the local path to the object whose storage class you want to change (you must re-upload the object when changing storage class with the XML API). For example, `Desktop/dog.png`.
     * `OBJECT_CONTENT_TYPE` is the [content type](https://docs.cloud.google.com/storage/docs/metadata#content-type) of the object. For example, `image/png`.
     * `STORAGE_CLASS` is the new [storage class](https://docs.cloud.google.com/storage/docs/storage-classes) for your object. For example, `nearline`.
     * `BUCKET_NAME` is the name of the bucket containing the object you are rewriting. For example, `my-bucket`.
     * `OBJECT_NAME` is the URL-encoded name of the object you are rewriting. For example, `pets/dog.png`, URL-encoded as `pets%2Fdog.png`.



**Note:** This guide involves rewriting data, which is a [Class A operation](https://docs.cloud.google.com/storage/pricing#operations-pricing) and which might incur additional charges, depending on the age, location, and storage class of the data. For more information, see [Cloud Storage pricing](https://docs.cloud.google.com/storage/pricing). Also note that if you have enabled [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning) for your bucket, the original object remains in your bucket until it is explicitly deleted.

## What's next

  * Learn about available [storage classes](https://docs.cloud.google.com/storage/docs/storage-classes).
  * [Change object storage classes with Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle-configurations#change_an_objects_storage_class).
  * Explore other Cloud Storage [data lifecycle features](https://docs.cloud.google.com/storage/docs/control-data-lifecycles).
  * Learn about [object metadata](https://docs.cloud.google.com/storage/docs/metadata).
  * Learn how to use [request preconditions](https://docs.cloud.google.com/storage/docs/request-preconditions) to prevent race conditions.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
