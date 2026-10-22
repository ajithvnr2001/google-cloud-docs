---
url: https://docs.cloud.google.com/storage/docs/samples/storage-copy-file-archived-generation/
title: Copy an archived object \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:29:46.746974+00:00
---

# Copy an archived object  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-copy-file-archived-generation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Copy an archived object Stay organized with collections  Save and categorize content based on your preferences. 

Copy an archived generation of an object in a Cloud Storage bucket.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Use versioned objects](https://docs.cloud.google.com/storage/docs/using-versioned-objects)



## Code sample

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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
