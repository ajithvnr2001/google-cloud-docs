---
url: https://docs.cloud.google.com/storage/docs/deleting-buckets/
title: Delete buckets \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:29:12.425959+00:00
---

# Delete buckets  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/deleting-buckets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Delete buckets Stay organized with collections  Save and categorize content based on your preferences. 

You can delete a Cloud Storage bucket when you no longer need the bucket or the objects within it.

If you delete a bucket that has [soft delete](https://docs.cloud.google.com/storage/docs/soft-delete) enabled, you can restore the bucket or individual objects from the bucket during the soft delete retention duration. You can't recover managed folders.

**Warning:** After a bucket is deleted, anyone can reuse the bucket's name for a new bucket and potentially receive data or requests that are intended for the original bucket. Also, a soft-deleted bucket can't be restored if its name is reused. To learn how to mitigate these risks, see [Bucket name considerations](https://docs.cloud.google.com/storage/docs/buckets#considerations).

## Before you begin

In order to get the required permissions for deleting a Cloud Storage bucket, ask your administrator to grant you the Storage Admin (`roles/storage.admin`) IAM role on the bucket.

This predefined role contains the permissions required to delete a bucket. To see the exact permissions that are required, expand the **Required permissions** section:

#### Required permissions

  * `storage.buckets.delete`
  * `storage.buckets.list`
    * This permission is only required when deleting buckets using the Google Cloud console.
  * `storage.objects.delete`
    * This permission is only required if objects exist within the bucket you want to delete.
  * `storage.objects.list`
    * This permission is only required for deleting buckets using the Google Cloud console or the Google Cloud CLI.



You might also be able to get these permissions with other [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

For instructions on granting roles for buckets, see [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).

## Delete a bucket

### Console

When you delete a bucket using the Google Cloud console, resources within the bucket are also deleted, such as objects, managed folders, and caches created with Rapid Cache.

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Select the checkbox of the bucket you want to delete.

  3. Click **Delete**.

  4. In the overlay window that appears, confirm you want to delete the bucket and its contents.

  5. Click **Delete**.


**Note:** If you have a large number of objects in your buckets, the delete operation may take longer than usual to complete.

To learn how to get detailed error information about failed Cloud Storage operations in the Google Cloud console, see [Troubleshooting](https://docs.cloud.google.com/storage/docs/troubleshooting#trouble-console).

### Command line

To delete the bucket, along with all the contents within the bucket, use the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud) command [`gcloud storage rm`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/rm) with the `--recursive` flag:
    
    
    gcloud storage rm --recursive gs://BUCKET_NAME

Where `BUCKET_NAME` is the name of the bucket to delete. For example, `my-bucket`.

If successful, the response looks like the following example:
    
    
    Removing gs://my-bucket/...

If you want to avoid accidentally deleting objects or managed folders, use the `gcloud storage buckets delete` command, which only deletes a bucket if the bucket is empty.

**Note:** If you need to delete a large number of objects in your buckets, avoid using Google Cloud CLI, as the operation takes a long time to complete. Instead, use one of the following options: 

  * Use the Google Cloud console.
  * Create a [storage batch operations](https://docs.cloud.google.com/storage/docs/batch-operations/overview) job.
  * Configure [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle).



For more information about protecting your data from accidental deletion, see [Options for controlling data lifecycles](https://docs.cloud.google.com/storage/docs/control-data-lifecycles).

### Client libraries

**Note:** When you use client libraries, your bucket must be empty before you can delete it. Some client libraries, like the Python client library, provide a force delete flag or function.

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    [](gcs::Client client, std::string const& bucket_name) {
      google::cloud::Status status = client.DeleteBucket(bucket_name);
      if (!status.ok()) throw std::runtime_error(status.message());
    
      std::cout << "The bucket " << bucket_name << " was deleted successfully.\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class DeleteBucketSample
    {
        public void DeleteBucket(string bucketName = "your-unique-bucket-name")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            storage.DeleteBucket(bucketName);
            Console.WriteLine($"The bucket {bucketName} was deleted.");
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
    
    // deleteBucket deletes the bucket.
    func deleteBucket(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucketName string) error {
    	// bucketName := "bucket-name"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*30)
    	defer cancel()
    
    	bucket := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucketName)
    	if err := bucket.Delete(ctx); err != nil {
    		return fmt.Errorf("Bucket(%q).Delete: %w", bucketName, err)
    	}
    	fmt.Fprintf(w, "Bucket %v deleted\n", bucketName)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class DeleteBucket {
      public static void deleteBucket(String projectId, String bucketName) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of the bucket to delete
        // String bucketName = "your-unique-bucket-name";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket = storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName);
        bucket.[delete](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html#com_google_cloud_storage_Bucket_delete_com_google_cloud_storage_Bucket_BucketSourceOption____)();
    
        System.out.println("Bucket " + bucket.getName() + " was deleted");
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
    
    async function deleteBucket() {
      await storage.bucket(bucketName).delete();
      console.log(`Bucket ${bucketName} deleted`);
    }
    
    deleteBucket().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Delete a Cloud Storage Bucket.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     */
    function delete_bucket(string $bucketName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
        $bucket->delete();
        printf('Bucket deleted: %s' . PHP_EOL, $bucket->name());
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def delete_bucket(bucket_name):
        """Deletes a bucket. The bucket must be empty."""
        # bucket_name = "your-bucket-name"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
        bucket = storage_client.[get_bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_get_bucket)(bucket_name)
        bucket.delete()
    
        print(f"Bucket {bucket.name} deleted")
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def delete_bucket bucket_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket  = storage.bucket bucket_name, skip_lookup: true
    
      bucket.delete
    
      puts "Deleted bucket: #{bucket.name}"
    end

### Rust
    
    
    use google_cloud_storage::client::StorageControl;
    
    pub async fn sample(client: &StorageControl, bucket_id: &str) -> anyhow::Result<()> {
        client
            .delete_bucket()
            .set_name(format!("projects/_/buckets/{bucket_id}"))
            .send()
            .await?;
        println!("successfully deleted bucket {bucket_id}");
        Ok(())
    }

### REST APIs

### JSON API

**Note:** When you use the JSON API, your bucket must be empty before you can delete it.

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`DELETE` Bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/delete) request:
         
         curl -X DELETE -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME"

Where `BUCKET_NAME` is the name of the bucket to delete. For example, `my-bucket`.




If successful, the response contains a 204 status code.

### XML API

**Note:** When you use the XML API, your bucket must be empty before you can delete it.

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [XML API](https://docs.cloud.google.com/storage/docs/xml-api/overview) with a [`DELETE` Bucket](https://docs.cloud.google.com/storage/docs/xml-api/delete-bucket) request:
         
         curl -X DELETE -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storage.googleapis.com/BUCKET_NAME"

Where `BUCKET_NAME` is the name of the bucket to delete. For example, `my-bucket`.




## What's next

  * [Create a bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).
  * [Move or rename a bucket](https://docs.cloud.google.com/storage/docs/moving-buckets).
  * [List objects in a bucket](https://docs.cloud.google.com/storage/docs/listing-objects#list-objects).
  * [Delete an object](https://docs.cloud.google.com/storage/docs/deleting-objects).
  * [Restore a soft-deleted bucket](https://docs.cloud.google.com/storage/docs/use-soft-deleted-buckets).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
