---
url: https://docs.cloud.google.com/storage/docs/deleting-objects/
title: Delete objects \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:56.728196+00:00
---

# Delete objects  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/deleting-objects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Delete objects Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to delete [objects](https://docs.cloud.google.com/storage/docs/objects) from your buckets in Cloud Storage. For an overview of object deletion methods, see [About object deletion](https://docs.cloud.google.com/storage/docs/object-deletion-overview).

**Note:** We generally recommend that you [keep soft delete enabled](https://docs.cloud.google.com/storage/docs/soft-delete) on your buckets, unless the bucket primarily contains short-lived, temporary data. Soft delete helps protect your data by retaining deleted objects in a soft-deleted state for a period of time before permanently deleting them. If you accidentally delete an object, you can restore it within this period. If you disable soft delete on a bucket, you can't recover deleted objects from that bucket. For more information about how to prevent accidental data deletion and manage object lifecycles, see [Options for controlling data lifecycles](https://docs.cloud.google.com/storage/docs/control-data-lifecycles).

## Required roles

To get the permissions that you need to delete objects, ask your administrator to grant you the following IAM roles on the bucket that contains the objects you want to delete: 

  * Delete objects using Google Cloud CLI or REST APIs: [Storage Object User ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectUser) (`roles/storage.objectUser`) 
  * Delete objects using the Google Cloud console: [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) 
  * Alternatively, to delete objects using the Google Cloud console: Viewer (`roles/viewer`) and Storage Object User (`roles/storage.objectUser`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to delete objects. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to delete objects:

  * Delete objects: `storage.objects.delete`
  * List objects using the Google Cloud console, or using the `--recursive` flag or wildcards in Google Cloud CLI: `storage.objects.list`
  * List buckets using the Google Cloud console: `storage.buckets.list`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Delete a single object

This section shows how to delete one object at a time.

**Note:** Deleting data might incur [early deletion charges](https://docs.cloud.google.com/storage/pricing) if the data was originally stored as Nearline storage, Coldline storage, or Archive storage. Additionally, if you have enabled [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning) for your bucket, the original object remains in your bucket until it is explicitly deleted using its [generation number](https://docs.cloud.google.com/storage/docs/using-versioned-objects#delete).

Complete the following steps to delete a single object:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket that contains the objects you want to delete.

The **Bucket details** page opens, with the **Objects** tab selected.

  3. Navigate to the object, which may be located in a folder.

  4. Select the checkbox for the object you want to delete.

  5. Click **Delete** , and then click **Delete** in the dialog that appears.




### Command line

Use the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud) command [`gcloud storage rm`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/rm):
    
    
    gcloud storage rm gs://BUCKET_NAME/OBJECT_NAME

Where:

  * `BUCKET_NAME` is the name of the bucket containing the object you want to delete. For example, `my-bucket`.
  * `OBJECT_NAME` is the name of the object you want to delete. For example, `pets/dog.png`.



If successful, the response is similar to the following example:
    
    
    Removing objects:
    Removing gs://example-bucket/file.txt...
      Completed 1/1

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    [](gcs::Client client, std::string const& bucket_name,
       std::string const& object_name) {
      google::cloud::Status status =
          client.DeleteObject(bucket_name, object_name);
    
      if (!status.ok()) throw std::runtime_error(status.message());
      std::cout << "Deleted " << object_name << " in bucket " << bucket_name
                << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class DeleteFileSample
    {
        public void DeleteFile(
            string bucketName = "your-unique-bucket-name",
            string objectName = "your-object-name")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            storage.DeleteObject(bucketName, objectName);
            Console.WriteLine($"Deleted {objectName}.");
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
    
    // deleteFile removes specified object.
    func deleteFile(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucket, object string) error {
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
    	// conditions and data corruptions. The request to delete the file is aborted
    	// if the object's generation number does not match your precondition.
    	attrs, err := o.Attrs(ctx)
    	if err != nil {
    		return fmt.Errorf("object.Attrs: %w", err)
    	}
    	o = o.If(storage.[Conditions](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Conditions){GenerationMatch: attrs.[Generation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_Generation)})
    
    	if err := o.Delete(ctx); err != nil {
    		return fmt.Errorf("Object(%q).Delete: %w", object, err)
    	}
    	fmt.Fprintf(w, "Blob %v deleted.\n", object)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html);
    import com.google.cloud.storage.[BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class DeleteObject {
      public static void deleteObject(String projectId, String bucketName, String objectName) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The ID of your GCS object
        // String objectName = "your-object-name";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        [Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html) blob = storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName, objectName);
        if (blob == null) {
          System.out.println("The object " + objectName + " wasn't found in " + bucketName);
          return;
        }
        [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html) idWithGeneration = blob.[getBlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html#com_google_cloud_storage_BlobInfo_getBlobId__)();
        // Deletes the blob specified by its id. When the generation is present and non-null it will be
        // specified in the request.
        // If versioning is enabled on the bucket and the generation is present in the delete request,
        // only the version of the object with the matching generation will be deleted.
        // If instead you want to delete the current version, the generation should be dropped by
        // performing the following.
        // BlobId idWithoutGeneration =
        //    BlobId.of(idWithGeneration.getBucket(), idWithGeneration.getName());
        // storage.delete(idWithoutGeneration);
        storage.[delete](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_delete_com_google_cloud_storage_BlobId_)(idWithGeneration);
    
        System.out.println("Object " + objectName + " was permanently deleted from " + bucketName);
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
    
    // Optional:
    // Set a generation-match precondition to avoid potential race conditions
    // and data corruptions. The request to delete is aborted if the object's
    // generation number does not match your precondition. For a destination
    // object that does not yet exist, set the ifGenerationMatch precondition to 0
    // If the destination object already exists in your bucket, set instead a
    // generation-match precondition using its generation number.
    const deleteOptions = {
      ifGenerationMatch: generationMatchPrecondition,
    };
    async function deleteFile() {
      await storage.bucket(bucketName).file(fileName).delete(deleteOptions);
    
      console.log(`gs://${bucketName}/${fileName} deleted`);
    }
    
    deleteFile().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Delete an object.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $objectName The name of your Cloud Storage object.
     *        (e.g. 'my-object')
     */
    function delete_object(string $bucketName, string $objectName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
        $object = $bucket->object($objectName);
        $object->delete();
        printf('Deleted gs://%s/%s' . PHP_EOL, $bucketName, $objectName);
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def delete_blob(bucket_name, blob_name):
        """Deletes a blob from the bucket."""
        # bucket_name = "your-bucket-name"
        # blob_name = "your-object-name"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
        blob = bucket.blob(blob_name)
        generation_match_precondition = None
    
        # Optional: set a generation-match precondition to avoid potential race conditions
        # and data corruptions. The request to delete is aborted if the object's
        # generation number does not match your precondition.
        blob.reload()  # Fetch blob metadata to use in generation_match_precondition.
        generation_match_precondition = blob.generation
    
        blob.delete(if_generation_match=generation_match_precondition)
    
        print(f"Blob {blob_name} deleted.")
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def delete_file bucket_name:, file_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      # The ID of your GCS object
      # file_name = "your-file-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket  = storage.bucket bucket_name, skip_lookup: true
      file    = bucket.[file](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) file_name
    
      file.delete
    
      puts "Deleted #{file.name}"
    end

### Rust
    
    
    use google_cloud_storage::client::StorageControl;
    
    pub async fn sample(client: &StorageControl, bucket_id: &str) -> anyhow::Result<()> {
        const NAME: &str = "deleted-object-name";
        client
            .delete_object()
            .set_bucket(format!("projects/_/buckets/{bucket_id}"))
            .set_object(NAME)
            // Consider .set_generation() to make request idempotent
            .send()
            .await?;
        println!("successfully deleted object {NAME} in bucket {bucket_id}");
        Ok(())
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`curl`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`DELETE`](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/delete) request:
         
         curl -X DELETE \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/o/OBJECT_NAME"

Where:

     * `BUCKET_NAME` is the name of the bucket containing the object you want to delete. For example, `my-bucket`.
     * `OBJECT_NAME` is the URL-encoded name of the object you want to delete. For example, `pets/dog.png`, URL-encoded as `pets%2Fdog.png`.



### XML API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`curl`](http://curl.haxx.se/) to call the [XML API](https://docs.cloud.google.com/storage/docs/xml-api/overview) with a [`DELETE Object`](https://docs.cloud.google.com/storage/docs/xml-api/delete-object) request:
         
         curl -X DELETE \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storage.googleapis.com/BUCKET_NAME/OBJECT_NAME"

Where:

     * `BUCKET_NAME` is the name of the bucket containing the object you want to delete. For example, `my-bucket`.
     * `OBJECT_NAME` is the URL-encoded name of the object you want to delete. For example, `pets/dog.png`, URL-encoded as `pets%2Fdog.png`.



## Delete objects in bulk

This section shows how to delete objects in bulk by selecting them in the Google Cloud console, by deleting objects with a common prefix using command-line tools, or by specifying a list of objects in API or client library requests.

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket that contains the objects you want to delete.

The **Bucket details** page opens, with the **Objects** tab selected.

  3. Navigate to the objects, which may be located in a folder.

  4. Select the checkbox for each object you want to delete.

You can select the checkbox for a folder, which deletes all objects contained in that folder.

  5. Click **Delete** , and then click **Delete** in the dialog that appears.




If you delete many objects at once, you can track deletion progress by clicking the **Notifications** icon in the Google Cloud console. The Google Cloud console can bulk delete up to several million objects and does so in the background.

To learn how to get detailed error information about failed Cloud Storage operations in the Google Cloud console, see [Troubleshooting](https://docs.cloud.google.com/storage/docs/troubleshooting#trouble-console).

### Command line

### Google Cloud CLI

To delete groups of objects that have the same prefix, such as objects whose names [mimic a folder structure](https://docs.cloud.google.com/storage/docs/objects#namespace), use the [`--recursive` flag](https://docs.cloud.google.com/sdk/gcloud/reference/storage/rm#--recursive) with [`gcloud storage rm`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/rm):
    
    
    gcloud storage rm --recursive gs://BUCKET_NAME/PREFIX

Where:

  * `BUCKET_NAME` is the name of the bucket. For example, `my-bucket`.
  * `PREFIX` is common prefix of the objects you want to delete. For example, `pets/`.

**Note:** If you want to bulk delete a hundred thousand or more objects, avoid using `gcloud storage`, as the process takes a long time to complete.

### Amazon S3 CLI

To delete multiple objects in Cloud Storage using the Amazon S3 CLI, use the `aws s3api delete-objects` command. You'll need to redirect the request to the Cloud Storage [multi-object delete XML API](https://docs.cloud.google.com/storage/docs/xml-api/post-bucket) by setting the `--endpoint-url` flag to `storage.googleapis.com`. For detailed parameter definitions and behavior of `delete-objects` API, see the [Amazon S3 CLI delete-objects reference documentation](https://docs.aws.amazon.com/cli/latest/reference/s3api/delete-objects.html).

### Client libraries

Cloud Storage supports the [multi-object delete XML API](https://docs.cloud.google.com/storage/docs/xml-api/post-bucket) through its Amazon S3-compatible interface. To use Amazon S3-compatible client libraries for bulk object deletion, point your request to the Google Cloud endpoint by setting the endpoint URL to `https://storage.googleapis.com` in the client configuration. This approach can be beneficial if you are performing any of the following tasks: 

  * Leveraging existing codebases or tooling already built for Amazon S3.
  * Maintaining consistency across multi-cloud environments that include both Amazon S3 and Cloud Storage.



The following example shows how to initialize a client using a [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) library to interact with Cloud Storage:
    
    
      import boto3
      def main():
      # Initialize the S3 client to point to the Google Cloud Storage endpoint
        client = boto3.client(
            service_name='s3',
            endpoint_url='https://storage.googleapis.com',
            aws_access_key_id='YOUR_ACCESS_ID',
            aws_secret_access_key='YOUR_SECRET',
        )
      # Perform delete operations as defined in the library's documentation
      # response = client.delete_objects(Bucket='BUCKET_NAME', Delete={'Objects': [...]})
      

For specific method signatures and parameter definitions, see the [`delete_objects` Boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/delete_objects.html).

### XML API

To delete up to 1,000 objects in a single request using the XML API, complete the following steps:

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create an XML document that specifies the objects to be deleted.

For a complete list of settings, see [Delete multiple objects](https://docs.cloud.google.com/storage/docs/xml-api/post-bucket) in the XML API reference documentation. The common settings to include in your XML file are as follows:
         
         <Delete>
             <Object>
               <Key>OBJECT_NAME</Key>
               <VersionId>VERSION_ID</VersionId>
             </Object>
             ...
             <Quiet>QUIET_RESPONSE_BOOLEAN</Quiet>
           </Delete>

Where:

     * `OBJECT_NAME` is the URL-encoded name of the object. For example, `pets/dog.png`, URL-encoded as `pets%2Fdog.png`. You can specify up to 1,000 objects in the XML file.
     * `VERSION_ID` is the [version ID](https://docs.cloud.google.com/storage/docs/metadata#generation-number) for the object. For example, `11111`.
     * `QUIET_RESPONSE_BOOLEAN` controls the verbosity of the API's response: 
       * Set to `False` for a verbose response. The response includes details for every object, whether it is successfully deleted or not. The multi-object delete operation using the XML API is not atomic. If a request results in partial failures, some objects might be successfully deleted but other objects might fail to be deleted, so we recommend using the verbose response to identify all object deletions. If you have [Data Access audit logs enabled](https://docs.cloud.google.com/storage/docs/audit-logging#xml-multi-object-delete-audit-logs), you can also review audit logs for failure details.
       * Set to `True` for a quiet response. The response body doesn't include information about the objects that are successfully deleted.
  3. Use [`curl`](http://curl.haxx.se/) to send a [`POST` bucket](https://docs.cloud.google.com/storage/docs/xml-api/post-bucket) request to the [XML API](https://docs.cloud.google.com/storage/docs/xml-api/overview) with the `?delete` query parameter and your XML file:
         
         curl -X POST --data-binary @XML_FILE_NAME \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storage.googleapis.com/BUCKET_NAME?delete"

Where:

     * `XML_FILE_NAME` is the name of the XML file you created.
     * `BUCKET_NAME` is the name of the bucket containing the objects to delete.

If `Quiet` mode is disabled, a verbose response might look similar to the following:
           
           <DeleteResult>
           <Deleted>
             <Key>images/photo1.jpg</Key>
             <VersionId>11111</VersionId>
           </Deleted>
           <Deleted>
             <Key>documents/report.pdf</Key>
             <VersionId>22222</VersionId>
           </Deleted>
           <Error>
             <Code>AccessDenied</Code>
             <Key>private/financial_data.xlsx</Key>
             <Message>Access Denied. You don't have permission to delete this object.</Message>
             <VersionId>33333</VersionId>
           </Error>
           </DeleteResult>
           

If `Quiet` mode is enabled, the response lists only objects that failed to delete. If all objects are successfully deleted, an empty `<DeleteResult/>` tag is returned. The following is an example of a quiet response where an error occurred:
           
           <DeleteResult>
           <Error>
             <Code>AccessDenied</Code>
             <Key>private/financial_data.xlsx</Key>
             <Message>Access Denied. You don't have permission to delete this object.</Message>
             <VersionId>33333</VersionId>
           </Error>
           </DeleteResult>




## Delete up to billions of objects

To delete millions or billions of objects with a single object deletion job, use [storage batch operations](https://docs.cloud.google.com/storage/docs/batch-operations/overview). To create a job, specify the objects to delete, either by providing a list of objects in a manifest file or by using object prefixes. After you have specified the object list, [create a batch operation job to delete the objects](https://docs.cloud.google.com/storage/docs/batch-operations/create-manage-batch-operation-jobs).

## Automatically delete objects using object lifecycle rules

If you want objects to be deleted automatically when they meet criteria that you specify, such as age or storage class, use [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle). For example, you can set a lifecycle rule to delete logs that are older than 30 days.

## Batch object deletion requests with JSON API

To reduce the number of HTTP connections needed when deleting many objects with the JSON API, use [JSON API batch requests](https://docs.cloud.google.com/storage/docs/batch). You can group up to 100 API calls into a single HTTP request to help reduce network overhead.

## What's next

  * Learn how to [restore soft-deleted objects](https://docs.cloud.google.com/storage/docs/use-soft-deleted-objects) if you deleted an object accidentally.
  * If you use [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning), understand that deleting an object might make it _noncurrent_ rather than deleting it permanently. Learn how to [manage or permanently delete noncurrent versions](https://docs.cloud.google.com/storage/docs/using-versioned-objects).
  * Configure [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle) to automate future object deletions.
  * [Delete a bucket](https://docs.cloud.google.com/storage/docs/deleting-buckets) if you no longer need it.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
