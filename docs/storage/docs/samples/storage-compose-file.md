---
url: https://docs.cloud.google.com/storage/docs/samples/storage-compose-file/
title: Compose multiple objects \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:17:06.078879+00:00
---

# Compose multiple objects  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-compose-file/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Compose multiple objects Stay organized with collections  Save and categorize content based on your preferences. 

Compose multiple objects into a single object in a Cloud Storage bucket.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Compose objects](https://docs.cloud.google.com/storage/docs/composing-objects)



## Code sample

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name,
       std::string const& destination_object_name,
       std::vector<gcs::ComposeSourceObject> const& compose_objects,
       bool delete_source_objects) {
      StatusOr<gcs::ObjectMetadata> composed_object = client.ComposeObject(
          bucket_name, compose_objects, destination_object_name,
          gcs::DeleteSourceObjects(delete_source_objects));
      if (!composed_object) throw std::move(composed_object).status();
    
      std::cout << "Composed new object " << composed_object->name()
                << " in bucket " << composed_object->bucket()
                << "\nFull metadata: " << *composed_object << "\n";
      if (delete_source_objects) {
        std::cout << "The source objects were deleted.\n";
      }
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using Google.Apis.Storage.v1.Data;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    using System.Collections.Generic;
    
    public class ComposeObjectSample
    {
        /// <summary>
        /// Combines multiple source objects into a single target object within a specified bucket,
        /// with the option to delete the original source objects upon successful composition.
        /// </summary>
        /// <param name="bucketName">The name of the bucket containing the source objects.</param>
        /// <param name="firstObjectName">The name of the first source object to be composed.</param>
        /// <param name="secondObjectName">The name of the second source object to be composed.</param>
        /// <param name="targetObjectName">The name for the newly created composite object.</param>
        /// <param name="deleteSourceObjects">If set to <c>true</c>, the method will automatically delete <paramref name="firstObjectName"/> and <paramref name="secondObjectName"/> upon successful composition.
        /// Defaults to <c>false</c>.</param>
        public void ComposeObject(
            string bucketName = "your-bucket-name",
            string firstObjectName = "your-first-object-name",
            string secondObjectName = "your-second-object-name",
            string targetObjectName = "new-composite-object-name",
            bool deleteSourceObjects = false)
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
    
            var sourceObjects = new List<ComposeRequest.SourceObjectsData>
            {
                new ComposeRequest.SourceObjectsData { Name = firstObjectName },
                new ComposeRequest.SourceObjectsData { Name = secondObjectName }
            };
            //You could add as many sourceObjects as you want here, up to the max of 32.
    
            storage.Service.Objects.Compose(new ComposeRequest
            {
                DeleteSourceObjects = deleteSourceObjects,
                SourceObjects = sourceObjects,
                Destination = new Google.Apis.Storage.v1.Data.Object { ContentType = "text/plain" }
            }, bucketName, targetObjectName).Execute();
    
            string deletionMessage = deleteSourceObjects ? " and the source objects were deleted." : ".";
            Console.WriteLine($"New composite file {targetObjectName} was created in bucket {bucketName}" +
                $" by combining {firstObjectName} and {secondObjectName}{deletionMessage}");
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
    
    // composeFile composes source objects to create a composite object.
    func composeFile(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucket, object1, object2, toObject string, deleteSourceObjects bool) error {
    	// bucket := "bucket-name"
    	// object1 := "object-name-1"
    	// object2 := "object-name-2"
    	// toObject := "object-name-3"
    	// deleteSourceObjects := true
    
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    
    	src1 := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucket).[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)(object1)
    	src2 := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucket).[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)(object2)
    	dst := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucket).[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)(toObject)
    
    	// ComposerFrom takes varargs, so you can put up to 32 source objects.
    	composer := dst.[ComposerFrom](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_ComposerFrom)(src1, src2)
    	composer.DeleteSourceObjects = deleteSourceObjects
    	_, err = composer.Run(ctx)
    	if err != nil {
    		return fmt.Errorf("ComposerFrom: %w", err)
    	}
    	status := "Source objects were not deleted."
    	if deleteSourceObjects {
    		status = "The source objects were deleted."
    	}
    	fmt.Fprintf(w, "New composite object %v was created by combining %v and %v. %s\n", toObject, object1, object2, status)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html);
    import com.google.cloud.storage.[BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class ComposeObject {
      public static void composeObject(
          String bucketName,
          String firstObjectName,
          String secondObjectName,
          String targetObjectName,
          String projectId) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The ID of the first GCS object to compose
        // String firstObjectName = "your-first-object-name";
    
        // The ID of the second GCS object to compose
        // String secondObjectName = "your-second-object-name";
    
        // The ID to give the new composite object
        // String targetObjectName = "new-composite-object-name";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
    
        // Optional: set a generation-match precondition to avoid potential race
        // conditions and data corruptions. The request returns a 412 error if the
        // preconditions are not met.
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobTargetOption precondition;
        if (storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName, tar[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)ObjectName) == null) {
          // For a target object that does not yet exist, set the DoesNotExist precondition.
          // This will cause the request to fail if the object is created before the request runs.
          precondition = [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobTargetOption.doesNotExist();
        } else {
          // If the destination already exists in your bucket, instead set a generation-match
          // precondition. This will cause the request to fail if the existing object's generation
          // changes before the request runs.
          precondition =
              [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobTargetOption.generationMatch(
                  storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName, tar[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)ObjectName).getGeneration());
        }
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).[ComposeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.ComposeRequest.html) composeRequest =
            [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).ComposeRequest.newBuilder()
                // addSource takes varargs, so you can put as many objects here as you want, up to the
                // max of 32
                .[addSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.ComposeRequest.Builder.html#com_google_cloud_storage_Storage_ComposeRequest_Builder_addSource_java_lang_Iterable_java_lang_String__)(firstObjectName, secondObjectName)
                .setTarget([BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html).newBuilder(bucketName, targetObjectName).build())
                .setTargetOptions(precondition)
                .build();
    
        [Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html) compositeObject = storage.[compose](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_compose_com_google_cloud_storage_Storage_ComposeRequest_)([compose](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_compose_com_google_cloud_storage_Storage_ComposeRequest_)Request);
    
        System.out.println(
            "New composite object "
                + compositeObject.getName()
                + " was created by combining "
                + firstObjectName
                + " and "
                + secondObjectName);
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
    
    // The ID of the first GCS file to compose
    // const firstFileName = 'your-first-file-name';
    
    // The ID of the second GCS file to compose
    // const secondFileName = 'your-second-file-name';
    
    // The ID to give the new composite file
    // const destinationFileName = 'new-composite-file-name';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function composeFile() {
      const bucket = storage.bucket(bucketName);
      const sources = [firstFileName, secondFileName];
    
      // Optional:
      // Set a generation-match precondition to avoid potential race conditions
      // and data corruptions. The request to compose is aborted if the object's
      // generation number does not match your precondition. For a destination
      // object that does not yet exist, set the ifGenerationMatch precondition to 0
      // If the destination object already exists in your bucket, set instead a
      // generation-match precondition using its generation number.
      const combineOptions = {
        ifGenerationMatch: destinationGenerationMatchPrecondition,
      };
      await bucket.[combine](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/bucket.html)(sources, destinationFileName, combineOptions);
    
      console.log(
        `New composite file ${destinationFileName} was created by combining ${firstFileName} and ${secondFileName}`
      );
    }
    
    composeFile().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Compose two objects into a single target object.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $firstObjectName The name of the first GCS object to compose.
     *        (e.g. 'my-object-1')
     * @param string $secondObjectName The name of the second GCS object to compose.
     *        (e.g. 'my-object-2')
     * @param string $targetObjectName The name of the object to be created.
     *        (e.g. 'composed-my-object-1-my-object-2')
     * @param bool $deleteSourceObjects Whether to delete the source objects after composition.
     *        (e.g. false)
     */
    function compose_file(string $bucketName, string $firstObjectName, string $secondObjectName, string $targetObjectName, bool $deleteSourceObjects = false): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
    
        // In this example, we are composing only two objects, but Cloud Storage supports
        // composition of up to 32 objects.
        $objectsToCompose = [$firstObjectName, $secondObjectName];
    
        $targetObject = $bucket->compose($objectsToCompose, $targetObjectName, [
            'destination' => [
                'contentType' => 'application/octet-stream'
            ]
        ]);
    
        if ($targetObject->exists()) {
            printf(
                'New composite object %s was created by combining %s and %s',
                $targetObject->name(),
                $firstObjectName,
                $secondObjectName
            );
    
            if ($deleteSourceObjects) {
                foreach ($objectsToCompose as $sourceObject) {
                    $bucket->object($sourceObject)->delete();
                }
                printf(' and source objects were deleted');
            }
            printf(PHP_EOL);
        }
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def compose_file(bucket_name, first_blob_name, second_blob_name, destination_blob_name):
        """Concatenate source blobs into destination blob."""
        # bucket_name = "your-bucket-name"
        # first_blob_name = "first-object-name"
        # second_blob_name = "second-blob-name"
        # destination_blob_name = "destination-object-name"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
        destination = bucket.blob(destination_blob_name)
        destination.[content_type](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_content_type) = "text/plain"
    
        # Note sources is a list of Blob instances, up to the max of 32 instances per request
        sources = [bucket.blob(first_blob_name), bucket.blob(second_blob_name)]
    
        # Optional: set a generation-match precondition to avoid potential race conditions
        # and data corruptions. The request to compose is aborted if the object's
        # generation number does not match your precondition. For a destination
        # object that does not yet exist, set the if_generation_match precondition to 0.
        # If the destination object already exists in your bucket, set instead a
        # generation-match precondition using its generation number.
        # There is also an `if_source_generation_match` parameter, which is not used in this example.
        destination_generation_match_precondition = 0
    
        destination.[compose](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_compose)(sources, if_generation_match=destination_generation_match_precondition)
    
        print(
            "New composite object {} in the bucket {} was created by combining {} and {}".format(
                destination_blob_name, bucket_name, first_blob_name, second_blob_name
            )
        )
        return destination
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def compose_file bucket_name:, first_file_name:, second_file_name:, destination_file_name:, delete_source_objects: false
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      # The ID of the first GCS object to compose
      # first_file_name = "your-first-file-name"
    
      # The ID of the second GCS object to compose
      # second_file_name = "your-second-file-name"
    
      # The ID to give the new composite object
      # destination_file_name = "new-composite-file-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket = storage.bucket bucket_name, skip_lookup: true
    
      destination = bucket.[compose](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) [first_file_name, second_file_name], destination_file_name, delete_source_objects: delete_source_objects do |f|
        f.content_type = "text/plain"
      end
    
      puts "Composed new file #{destination.name} in the bucket #{bucket_name} " \
           "by combining #{first_file_name} and #{second_file_name}"
      puts "Source objects were deleted" if delete_source_objects
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
