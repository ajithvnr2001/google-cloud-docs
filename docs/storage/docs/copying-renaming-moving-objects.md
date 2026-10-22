---
url: https://docs.cloud.google.com/storage/docs/copying-renaming-moving-objects/
title: Copy, rename, and move objects \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:26:41.899154+00:00
---

# Copy, rename, and move objects  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/copying-renaming-moving-objects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Copy, rename, and move objects Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to copy, rename, and move objects. While some tools perform atomic object move operations, other tools simulate an object move operation by copying the object to a new specified location and then deleting the original object.

  * For instructions on copying objects, see Copy objects.
  * For instructions on moving or renaming objects by copying them, see Move or rename objects by copying.
  * For instructions on renaming objects atomically, see Rename objects atomically.

**Caution:** Because moving objects by copying them includes deleting the original objects from the source bucket, using this method to move objects whose storage class is Nearline storage, Coldline storage, or Archive storage can incur [early deletion charges](https://docs.cloud.google.com/storage/pricing#early-delete). If you move objects atomically, no early deletion charges are incurred, regardless of the storage class of the objects being moved.

We recommend using [Storage Transfer Service to move more than 1 TB of data between buckets](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/rewrite).

## Before you begin

In order to copy, rename, or move objects, you must get the required IAM roles. The following sections describe IAM requirements for different use cases.

### Copy objects (including moving or renaming by copying)

To get the permissions that you need to copy objects, ask your administrator to grant you the following IAM roles on the source bucket that contains the objects you want to move, or the destination bucket where you want to move the objects to: 

  * Storage Object Viewer (`roles/storage.objectViewer`) on the source bucket 
  * Storage Object User (`roles/storage.objectUser`) on the destination bucket 
  * To copy objects using the Google Cloud console: Viewer basic role (`roles/viewer`) on both the source bucket and destination bucket, in addition to `roles/storage.objectViewer` and `roles/storage.objectUser`



These predefined roles contain the permissions required to copy objects. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to copy objects:

  * `storage.objects.get` on the source bucket
  * `storage.objects.create` on the destination bucket
  * `storage.objects.delete` (required only if you're replacing or overwriting an object in the destination bucket as part of an object copy or move operation) on the destination bucket
  * `storage.objects.delete` (required only if you're moving an object using an underlying copy and delete operation) on the source bucket
  * `storage.folders.create` (required only if the object you're moving is located in a folder that you want to create in the destination bucket) on the destination bucket
  * `storage.objects.list` (required only if you're copying, moving, or renaming an object using the Google Cloud console) on the source and destination buckets
  * `storage.buckets.list` (required only if you're copying, moving, or renaming an object using the Google Cloud console) on the project that contains the source and destination buckets



You can also get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

For information about granting roles on buckets, see [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions). For information about granting roles on projects, see [Manage access to projects](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

If the object you want to copy has certain features enabled, you might need additional or alternative roles. For example, if the object you want to copy has an object retention configuration you want to retain, you'll need a role on the destination bucket that includes the `storage.objects.setRetention` permission, such as the Storage Object Admin (`roles/storage.objectAdmin`) role. For more information, see [IAM permissions for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam-permissions).

### Rename objects atomically

To get the permissions that you need to rename objects atomically, ask your administrator to grant you the [Storage Object User ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`) IAM role on the bucket that contains the object you want to rename. 

This predefined role contains the permissions required to rename objects atomically. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to rename objects atomically:

  * `storage.objects.move`
  * `storage.objects.create`
  * `storage.objects.delete` (required only if you're overwriting or replacing an object) 



You can also get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

For information about granting roles on buckets, see [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).

## Copy objects

This section describes how to copy objects. You can copy objects from one bucket to another.

**Note:** If you are copying an object larger than 2 GB across different regions or storage classes, we recommend you use the gcloud CLI for optimal performance.

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket that contains the object you want to copy.

The **Bucket details** page opens, with the **Objects** tab selected.

  3. Navigate to the object, which may be located in a folder.

  4. Click the **Object overflow** menu (_more_vert_) associated with the object.

  5. Click **Copy**.

The **Copy object** pane appears.

  6. In the **Destination** field, type the name of the destination bucket and the name for the copied object.

You can alternatively click **Browse** to select your destination, but browse options are limited to buckets in the current project.

  7. Click **Copy**.




To learn how to get detailed error information about failed Cloud Storage operations in the Google Cloud console, see [Troubleshooting](https://docs.cloud.google.com/storage/docs/troubleshooting#trouble-console).

### Command line

Use the [`gcloud storage cp`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cp) command:
    
    
    gcloud storage cp gs://SOURCE_BUCKET_NAME/SOURCE_OBJECT_NAME gs://DESTINATION_BUCKET_NAME/NAME_OF_COPY

Where:

  * `SOURCE_BUCKET_NAME` is the name of the bucket containing the object you want to copy. For example, `my-bucket`.
  * `SOURCE_OBJECT_NAME` is the name of the object you want to copy. For example, `pets/dog.png`.
  * `DESTINATION_BUCKET_NAME` is the name of the bucket where you want to copy your object. For example, `another-bucket`.
  * `NAME_OF_COPY` is the name you want to give the copy of your object. For example, `shiba.png`.



If successful, the response is similar to the following example:
    
    
    Copying gs://example-bucket/file.txt to gs://other-bucket/file-copy.txt
      Completed files 1/1 | 164.3kiB/164.3kiB 

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& source_bucket_name,
       std::string const& source_object_name,
       std::string const& destination_bucket_name,
       std::string const& destination_object_name) {
      StatusOr<gcs::ObjectMetadata> new_copy_meta =
          client.CopyObject(source_bucket_name, source_object_name,
                            destination_bucket_name, destination_object_name);
      if (!new_copy_meta) throw std::move(new_copy_meta).status();
    
      std::cout << "Successfully copied " << source_object_name << " in bucket "
                << source_bucket_name << " to bucket " << new_copy_meta->bucket()
                << " with name " << new_copy_meta->name()
                << ".\nThe full metadata after the copy is: " << *new_copy_meta
                << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class CopyFileSample
    {
        public void CopyFile(
            string sourceBucketName = "source-bucket-name",
            string sourceObjectName = "source-file",
            string destBucketName = "destination-bucket-name",
            string destObjectName = "destination-file-name")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            storage.CopyObject(sourceBucketName, sourceObjectName, destBucketName, destObjectName);
    
            Console.WriteLine($"Copied {sourceBucketName}/{sourceObjectName} to " + $"{destBucketName}/{destObjectName}.");
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
    
    // copyFile copies an object into specified bucket.
    func copyFile(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), dstBucket, srcBucket, srcObject string) error {
    	// dstBucket := "bucket-1"
    	// srcBucket := "bucket-2"
    	// srcObject := "object"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    
    	dstObject := srcObject + "-copy"
    	src := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(srcBucket).[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)(srcObject)
    	dst := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(dstBucket).[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)(dstObject)
    
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
    
    	if _, err := dst.[CopierFrom](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_CopierFrom)(src).Run(ctx); err != nil {
    		return fmt.Errorf("Object(%q).CopierFrom(%q).Run: %w", dstObject, srcObject, err)
    	}
    	fmt.Fprintf(w, "Blob %v in bucket %v copied to blob %v in bucket %v.\n", srcObject, srcBucket, dstObject, dstBucket)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html);
    import com.google.cloud.storage.[BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html);
    import com.google.cloud.storage.[CopyWriter](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.CopyWriter.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).[CopyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.CopyRequest.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class CopyObject {
      public static void copyObject(
          String projectId, String sourceBucketName, String objectName, String targetBucketName)
          throws Exception {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of the bucket the original object is in
        // String sourceBucketName = "your-source-bucket";
    
        // The ID of the GCS object to copy
        // String objectName = "your-object-name";
    
        // The ID of the bucket to copy the object to
        // String targetBucketName = "target-object-bucket";
    
        try ([Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage =
            [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)()) {
          [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html) sourceId = [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html).of(sourceBucketName, objectName);
          // you could change "objectName" to rename the object
          [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html) targetId = [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html).of(targetBucketName, objectName);
    
          // Recommended: set a generation-match precondition to avoid potential race
          // conditions and data corruptions. The request returns a 412 error if the
          // preconditions are not met.
          [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobTargetOption precondition;
          [BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html) existingTarget = storage.get(targetBucketName, objectName);
          if (existingTarget == null) {
            // For a target object that does not yet exist, set the DoesNotExist precondition.
            // This will cause the request to fail if the object is created before the request runs.
            precondition = [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobTargetOption.doesNotExist();
          } else {
            // If the destination already exists in your bucket, instead set a generation-match
            // precondition. This will cause the request to fail if the existing object's generation
            // changes before the request runs.
            precondition = [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobTargetOption.generationMatch(existingTarget.[getGeneration](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html#com_google_cloud_storage_BlobInfo_getGeneration__)());
          }
    
          [CopyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.CopyRequest.html) copyRequest =
              [CopyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.CopyRequest.html).newBuilder()
                  .setSource(sourceId)
                  .setTarget(targetId, precondition)
                  // limit the number of bytes Cloud Storage will attempt to copy before responding to
                  // an individual request.
                  // If you see Read Timeout errors, try reducing this value.
                  .[setMegabytesCopiedPerChunk](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.CopyRequest.Builder.html#com_google_cloud_storage_Storage_CopyRequest_Builder_setMegabytesCopiedPerChunk_java_lang_Long_)(2048L) // 2GiB
                  .build();
          [CopyWriter](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.CopyWriter.html) copyWriter = storage.copy(copyRequest);
          [BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html) successfulCopyResult = copyWriter.[getResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.CopyWriter.html#com_google_cloud_storage_CopyWriter_getResult__)();
    
          System.out.printf(
              "Copied object gs://%s/%s to %s%n",
              sourceBucketName,
              objectName,
              successfulCopyResult.[getBlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html#com_google_cloud_storage_BlobInfo_getBlobId__)().[toGsUtilUriWithGeneration](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html#com_google_cloud_storage_BlobId_toGsUtilUriWithGeneration__)());
        }
      }
    }

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The ID of the bucket the original file is in
    // const srcBucketName = 'your-source-bucket';
    
    // The ID of the GCS file to copy
    // const srcFilename = 'your-file-name';
    
    // The ID of the bucket to copy the file to
    // const destBucketName = 'target-file-bucket';
    
    // The ID of the GCS file to create
    // const destFileName = 'target-file-name';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function copyFile() {
      const copyDestination = storage.bucket(destBucketName).file(destFileName);
    
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
    
      // Copies the file to the other bucket
      await storage
        .bucket(srcBucketName)
        .file(srcFilename)
        .[copy](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/file_2.html)(copyDestination, copyOptions);
    
      console.log(
        `gs://${srcBucketName}/${srcFilename} copied to gs://${destBucketName}/${destFileName}`
      );
    }
    
    copyFile().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Copy an object to a new name and/or bucket.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $objectName The name of your Cloud Storage object.
     *        (e.g. 'my-object')
     * @param string $newBucketName The destination bucket name.
     *        (e.g. 'my-other-bucket')
     * @param string $newObjectName The destination object name.
     *        (e.g. 'my-other-object')
     */
    function copy_object(string $bucketName, string $objectName, string $newBucketName, string $newObjectName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
        $object = $bucket->object($objectName);
        $object->copy($newBucketName, ['name' => $newObjectName]);
        printf('Copied gs://%s/%s to gs://%s/%s' . PHP_EOL,
            $bucketName, $objectName, $newBucketName, $newObjectName);
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def copy_blob(
        bucket_name, blob_name, destination_bucket_name, destination_blob_name,
    ):
        """Copies a blob from one bucket to another with a new name."""
        # bucket_name = "your-bucket-name"
        # blob_name = "your-object-name"
        # destination_bucket_name = "destination-bucket-name"
        # destination_blob_name = "destination-object-name"
    
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
        # There is also an `if_source_generation_match` parameter, which is not used in this example.
        destination_generation_match_precondition = 0
    
        blob_copy = source_bucket.[copy_blob](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_copy_blob)(
            source_blob, destination_bucket, destination_blob_name, if_generation_match=destination_generation_match_precondition,
        )
    
        print(
            "Blob {} in bucket {} copied to blob {} in bucket {}.".format(
                source_blob.name,
                source_bucket.name,
                blob_copy.name,
                destination_bucket.name,
            )
        )
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def copy_file source_bucket_name:, source_file_name:, destination_bucket_name:, destination_file_name:
      # The ID of the bucket the original object is in
      # source_bucket_name = "source-bucket-name"
    
      # The ID of the GCS object to copy
      # source_file_name = "source-file-name"
    
      # The ID of the bucket to copy the object to
      # destination_bucket_name = "destination-bucket-name"
    
      # The ID of the new GCS object
      # destination_file_name = "destination-file-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket  = storage.bucket source_bucket_name, skip_lookup: true
      file    = bucket.[file](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) source_file_name
    
      destination_bucket = storage.bucket destination_bucket_name
      destination_file   = file.[copy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-File.html) destination_bucket.name, destination_file_name
    
      puts "#{file.name} in #{bucket.name} copied to " \
           "#{destination_file.name} in #{destination_bucket.name}"
    end

### Rust
    
    
    use google_cloud_storage::builder_ext::RewriteObjectExt;
    use google_cloud_storage::client::StorageControl;
    
    pub async fn sample(
        client: &StorageControl,
        source_bucket_id: &str,
        dest_bucket_id: &str,
    ) -> anyhow::Result<()> {
        const SOURCE_NAME: &str = "object-to-copy";
        const DEST_NAME: &str = "copied-object";
        let copied = client
            .rewrite_object()
            .set_source_bucket(format!("projects/_/buckets/{source_bucket_id}"))
            .set_source_object(SOURCE_NAME)
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

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`POST` Object](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/rewrite) request:
         
         curl -X POST \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Length: 0" \
           "https://storage.googleapis.com/storage/v1/b/SOURCE_BUCKET_NAME/o/SOURCE_OBJECT_NAME/rewriteTo/b/DESTINATION_BUCKET_NAME/o/NAME_OF_COPY"

Where:

     * `SOURCE_BUCKET_NAME` is the name of the bucket containing the object you want to copy. For example, `my-bucket`.
     * `SOURCE_OBJECT_NAME` is the URL-encoded name of the object you want to copy. For example, `pets/dog.png`, URL-encoded as `pets%2Fdog.png`.
     * `DESTINATION_BUCKET_NAME` is the name of the bucket where you want to copy your object. For example, `another-bucket`.
     * `NAME_OF_COPY` is the URL-encoded name you want to give the copy of your object. For example, `shiba.png`.

Since the `rewrite` method copies data in limited-sized chunks, your copy might require multiple requests, especially for large objects.

For example, the following response to a `rewrite` request indicates that you need to make additional `rewrite` requests:
    
    {
      "kind": "storage#rewriteResponse",
      "totalBytesRewritten": 1048576,
      "objectSize": 10000000000,
      "done": false,
      "rewriteToken": TOKEN_VALUE
    }

  3. Use the `rewriteToken` in a subsequent request to continue copying data:
         
         curl -X POST \
          -H "Authorization: Bearer $(gcloud auth print-access-token)" \
          -H "Content-Length: 0" \
          -d '{"rewriteToken": "TOKEN_VALUE"}' \
          "https://storage.googleapis.com/storage/v1/b/SOURCE_BUCKET_NAME/o/SOURCE_OBJECT_NAME/rewriteTo/b/DESTINATION_BUCKET_NAME/o/NAME_OF_COPY"

Where:

     * `TOKEN_VALUE` is the `rewriteToken` value returned in the previous request.
     * All other values match those used in the previous request.

When the object is fully is copied, the last response has a `done` property set to `true`, there is no `rewriteToken` property, and the metadata of the copy is included in the `resource` property.
    
    {
     "kind": "storage#rewriteResponse",
     "totalBytesRewritten": 10000000000,
     "objectSize": 10000000000,
     "done": true,
     "resource": [objects Resource](https://docs.cloud.google.com/storage/docs/json_api/v1/objects#resource)
    }




### XML API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [XML API](https://docs.cloud.google.com/storage/docs/xml-api/overview) with a [`PUT` Object](https://docs.cloud.google.com/storage/docs/xml-api/put-object-copy) request:
         
         curl -X PUT \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "x-goog-copy-source: SOURCE_BUCKET_NAME/SOURCE_OBJECT_NAME" \
           "https://storage.googleapis.com/DESTINATION_BUCKET_NAME/NAME_OF_COPY"

Where:

     * `SOURCE_BUCKET_NAME` is the name of the bucket containing the object you want to copy. For example, `my-bucket`.
     * `SOURCE_OBJECT_NAME` is the name of the object you want to copy. For example, `pets/dog.png`.
     * `DESTINATION_BUCKET_NAME` is the name of the bucket where you want to copy your object. For example, `another-bucket`.
     * `NAME_OF_COPY` is the URL-encoded name you want to give the copy of your object. For example, `shiba.png`.



## Move or rename objects by copying

This section describes how to move or rename objects by using underlying object copy operations. The tools described in this section perform object moves and renames by copying the original object to another namespace and then deleting the original object.

**Note:** If you are moving an object larger than 2 GB across different regions or storage classes, we recommend you use the gcloud CLI for optimal performance.

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket that contains the object you want to move.

The **Bucket details** page opens, with the **Objects** tab selected.

  3. Navigate to the object, which may be located in a folder.

  4. Click the **Object overflow** menu (_more_vert_) associated with the object.

  5. If you want to give the object a new name in the same bucket, click **Rename**.

     1. In the overlay window that appears, enter a new name for the object.

     2. Click **Rename**.

  6. If you want to move the object to a different bucket, click **Move**.

     1. In the overlay window that appears, click **Browse**.

     2. Select the destination for the object you are moving.

     3. Click **Select**.

     4. Click **Move**.




To learn how to get detailed error information about failed Cloud Storage operations in the Google Cloud console, see [Troubleshooting](https://docs.cloud.google.com/storage/docs/troubleshooting#trouble-console).

### Command line

Use the [`gcloud storage mv`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/mv) command:
    
    
    gcloud storage mv gs://SOURCE_BUCKET_NAME/SOURCE_OBJECT_NAME gs://DESTINATION_BUCKET_NAME/DESTINATION_OBJECT_NAME

Where:

  * `SOURCE_BUCKET_NAME` is the name of the bucket containing the object you want to move or rename. For example, `my-bucket`.
  * `SOURCE_OBJECT_NAME` is the name of the object you want to move or rename. For example, `pets/dog.png`.
  * `DESTINATION_BUCKET_NAME` is the name of the bucket you want to move the object to. For example, `another-bucket`.
  * `DESTINATION_OBJECT_NAME` is the name you want your object to have after the move or rename. For example, `shiba.png`.



If successful, the response is similar to the following example:
    
    
    Copying gs://example-bucket/old-file.txt to gs://new-bucket/new-file.txt
    Removing gs://example-bucket/old-file.txt...
      Completed files 1/1 | 164.3kiB/164.3kiB 

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name,
       std::string const& old_object_name, std::string const& new_object_name) {
      StatusOr<gcs::ObjectMetadata> metadata = client.RewriteObjectBlocking(
          bucket_name, old_object_name, bucket_name, new_object_name);
      if (!metadata) throw std::move(metadata).status();
    
      google::cloud::Status status =
          client.DeleteObject(bucket_name, old_object_name);
      if (!status.ok()) throw std::runtime_error(status.message());
    
      std::cout << "Renamed " << old_object_name << " to " << new_object_name
                << " in bucket " << bucket_name << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class MoveFileSample
    {
        public void MoveFile(
            string sourceBucketName = "your-unique-bucket-name",
            string sourceObjectName = "your-object-name",
            string targetBucketName = "target-object-bucket",
            string targetObjectName = "target-object-name")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            storage.CopyObject(sourceBucketName, sourceObjectName, targetBucketName, targetObjectName);
            storage.DeleteObject(sourceBucketName, sourceObjectName);
            Console.WriteLine($"Moved {sourceObjectName} to {targetObjectName}.");
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
    
    // moveFile moves an object into another location.
    func moveFile(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucket, object string) error {
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
    
    	dstName := object + "-rename"
    	src := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucket).[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)(object)
    	dst := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucket).[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)(dstName)
    
    	// Optional: set a generation-match precondition to avoid potential race
    	// conditions and data corruptions. The request to copy the file is aborted
    	// if the object's generation number does not match your precondition.
    	// For a dst object that does not yet exist, set the DoesNotExist precondition.
    	dst = dst.If(storage.[Conditions](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Conditions){DoesNotExist: true})
    	// If the destination object already exists in your bucket, set instead a
    	// generation-match precondition using its generation number.
    	// attrs, err := dst.Attrs(ctx)
    	// if err != nil {
    	// 	return fmt.Errorf("object.Attrs: %w", err)
    	// }
    	// dst = dst.If(storage.Conditions{GenerationMatch: attrs.Generation})
    
    	if _, err := dst.[CopierFrom](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_CopierFrom)(src).Run(ctx); err != nil {
    		return fmt.Errorf("Object(%q).CopierFrom(%q).Run: %w", dstName, object, err)
    	}
    	if err := src.Delete(ctx); err != nil {
    		return fmt.Errorf("Object(%q).Delete: %w", object, err)
    	}
    	fmt.Fprintf(w, "Blob %v moved to %v.\n", object, dstName)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html);
    import com.google.cloud.storage.[BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html);
    import com.google.cloud.storage.[BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class CopyDeleteObject {
      public static void copyDeleteObject(
          String projectId,
          String sourceBucketName,
          String sourceObjectName,
          String targetBucketName,
          String targetObjectName) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String sourceBucketName = "your-unique-bucket-name";
    
        // The ID of your GCS object
        // String sourceObjectName = "your-object-name";
    
        // The ID of the bucket to move the object objectName to
        // String targetBucketName = "target-object-bucket"
    
        // The ID of your GCS object
        // String targetObjectName = "your-new-object-name";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html) source = [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html).of(sourceBucketName, sourceObjectName);
        [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html) target = [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html).of(targetBucketName, targetObjectName);
    
        // Optional: set a generation-match precondition to avoid potential race
        // conditions and data corruptions. The request returns a 412 error if the
        // preconditions are not met.
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobTargetOption precondition;
        [BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html) existingTarget = storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(tar[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)BucketName, tar[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)ObjectName);
        if (existingTarget == null) {
          // For a target object that does not yet exist, set the DoesNotExist precondition.
          // This will cause the request to fail if the object is created before the request runs.
          precondition = [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobTargetOption.doesNotExist();
        } else {
          // If the destination already exists in your bucket, instead set a generation-match
          // precondition. This will cause the request to fail if the existing object's generation
          // changes before the request runs.
          precondition = [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobTargetOption.generationMatch(existingTarget.[getGeneration](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html#com_google_cloud_storage_BlobInfo_getGeneration__)());
        }
    
        // Copy source object to target object
        storage.[copy](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_copy_com_google_cloud_storage_Storage_CopyRequest_)(
            Storage.CopyRequest.newBuilder().setSource(source).setTarget(target, precondition).build());
        [Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html) copiedObject = storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(tar[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_));
        // Delete the original blob now that we've copied to where we want it, finishing the "move"
        // operation
        storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(source).delete();
    
        System.out.println(
            "Moved object "
                + sourceObjectName
                + " from bucket "
                + sourceBucketName
                + " to "
                + targetObjectName
                + " in bucket "
                + copiedObject.getBucket());
      }
    }

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The ID of your GCS bucket
    // const bucketName = 'your-source-bucket';
    
    // The ID of your GCS file
    // const srcFileName = 'your-file-name';
    
    // The new ID for your GCS file
    // const destFileName = 'your-new-file-name';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function moveFile() {
      // Optional:
      // Set a generation-match precondition to avoid potential race conditions
      // and data corruptions. The request to copy is aborted if the object's
      // generation number does not match your precondition. For a destination
      // object that does not yet exist, set the ifGenerationMatch precondition to 0
      // If the destination object already exists in your bucket, set instead a
      // generation-match precondition using its generation number.
      const moveOptions = {
        preconditionOpts: {
          ifGenerationMatch: destinationGenerationMatchPrecondition,
        },
      };
    
      // Moves the file within the bucket
      await storage
        .bucket(bucketName)
        .file(srcFileName)
        .[move](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/file_2.html)(destFileName, moveOptions);
    
      console.log(
        `gs://${bucketName}/${srcFileName} moved to gs://${bucketName}/${destFileName}`
      );
    }
    
    moveFile().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Move an object to a new name and/or bucket.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $objectName The name of your Cloud Storage object.
     *        (e.g. 'my-object')
     * @param string $newBucketName the destination bucket name.
     *        (e.g. 'my-other-bucket')
     * @param string $newObjectName the destination object name.
     *        (e.g. 'my-other-object')
     */
    function move_object(string $bucketName, string $objectName, string $newBucketName, string $newObjectName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
        $object = $bucket->object($objectName);
        $object->copy($newBucketName, ['name' => $newObjectName]);
        $object->delete();
        printf('Moved gs://%s/%s to gs://%s/%s' . PHP_EOL,
            $bucketName,
            $objectName,
            $newBucketName,
            $newObjectName);
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def move_blob(bucket_name, blob_name, destination_bucket_name, destination_blob_name,):
        """Moves a blob from one bucket to another with a new name."""
        # The ID of your GCS bucket
        # bucket_name = "your-bucket-name"
        # The ID of your GCS object
        # blob_name = "your-object-name"
        # The ID of the bucket to move the object to
        # destination_bucket_name = "destination-bucket-name"
        # The ID of your new GCS object (optional)
        # destination_blob_name = "destination-object-name"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
        source_bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
        source_blob = source_bucket.blob(blob_name)
        destination_bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(destination_bucket_name)
    
        # Optional: set a generation-match precondition to avoid potential race conditions
        # and data corruptions. The request is aborted if the object's
        # generation number does not match your precondition. For a destination
        # object that does not yet exist, set the if_generation_match precondition to 0.
        # If the destination object already exists in your bucket, set instead a
        # generation-match precondition using its generation number.
        # There is also an `if_source_generation_match` parameter, which is not used in this example.
        destination_generation_match_precondition = 0
    
        blob_copy = source_bucket.[copy_blob](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_copy_blob)(
            source_blob, destination_bucket, destination_blob_name, if_generation_match=destination_generation_match_precondition,
        )
        source_bucket.[delete_blob](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_delete_blob)(blob_name)
    
        print(
            "Blob {} in bucket {} moved to blob {} in bucket {}.".format(
                source_blob.name,
                source_bucket.name,
                blob_copy.name,
                destination_bucket.name,
            )
        )
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def move_file bucket_name:, file_name:, new_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      # The ID of your GCS object
      # file_name = "your-file-name"
    
      # The ID of your new GCS object
      # new_name = "your-new-file-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket  = storage.bucket bucket_name, skip_lookup: true
      file    = bucket.[file](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) file_name
    
      renamed_file = file.[copy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-File.html) new_name
    
      file.delete
    
      puts "#{file_name} has been renamed to #{renamed_file.name}"
    end

### Rust
    
    
    use google_cloud_storage::builder_ext::RewriteObjectExt;
    use google_cloud_storage::client::StorageControl;
    
    pub async fn sample(
        client: &StorageControl,
        source_bucket_id: &str,
        dest_bucket_id: &str,
    ) -> anyhow::Result<()> {
        const SOURCE_NAME: &str = "object-to-move";
        const DEST_NAME: &str = "moved-object";
        let moved = client
            .rewrite_object()
            .set_source_bucket(format!("projects/_/buckets/{source_bucket_id}"))
            .set_source_object(SOURCE_NAME)
            .set_destination_bucket(format!("projects/_/buckets/{dest_bucket_id}"))
            .set_destination_name(DEST_NAME)
            .rewrite_until_done()
            .await?;
    
        client
            .delete_object()
            .set_bucket(format!("projects/_/buckets/{source_bucket_id}"))
            .set_object(SOURCE_NAME)
            .send()
            .await?;
        println!(
            "successfully moved {source_bucket_id}/{SOURCE_NAME} to {dest_bucket_id}/{DEST_NAME}: {moved:?}"
        );
    
        Ok(())
    }

### REST APIs

### JSON API

For JSON API instructions on moving or renaming objects by copying, see Copy objects.

### XML API

For XML API instructions on moving or renaming objects by copying, see Copy objects.

## Rename objects atomically

This section describes how to atomically rename objects within a bucket. To rename an object, you can use the `Objects: move` method in the Cloud Storage JSON API.

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`Objects: move`](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/move) request:
         
         curl -X POST \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Length: 0" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/o/SOURCE_OBJECT_NAME/moveTo/o/DESTINATION_OBJECT_NAME"

Where:

     * `BUCKET_NAME` is the name of the bucket containing the object you want to rename. For example, `my-bucket`.
     * `SOURCE_OBJECT_NAME` is the URL-encoded name of the object you want to rename. For example, `pets/dog.png`, URL-encoded as `pets%2Fdog.png`.
     * `DESTINATION_OBJECT_NAME` is the URL-encoded name you want to use. For example, `pets/cat.png`, URL-encoded as `pets%2Fcat.png`.



## What's next

  * [Change the storage class of an object](https://docs.cloud.google.com/storage/docs/changing-storage-classes).
  * [Edit an object's metadata](https://docs.cloud.google.com/storage/docs/viewing-editing-metadata#edit).
  * [Make objects and buckets publicly accessible](https://docs.cloud.google.com/storage/docs/access-control/making-data-public).
  * Learn more about [object naming requirements](https://docs.cloud.google.com/storage/docs/objects#naming).
  * Learn about using [request preconditions](https://docs.cloud.google.com/storage/docs/request-preconditions) to prevent race conditions.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
