---
url: https://docs.cloud.google.com/storage/docs/samples/storage-control-managed-folder-delete/
title: Storage Control delete a managed folder \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:17:04.661271+00:00
---

# Storage Control delete a managed folder  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-control-managed-folder-delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Storage Control delete a managed folder Stay organized with collections  Save and categorize content based on your preferences. 

Storage Control delete a managed folder

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create and manage managed folders](https://docs.cloud.google.com/storage/docs/creating-managing-managed-folders)



## Code sample

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace storagecontrol = google::cloud::storagecontrol_v2;
    [](storagecontrol::StorageControlClient client,
       std::string const& bucket_name, std::string const& managed_folder_id) {
      auto const name = std::string{"projects/_/buckets/"} + bucket_name +
                        "/managedFolders/" + managed_folder_id;
      auto status = client.DeleteManagedFolder(name);
      if (!status.ok()) throw std::move(status);
    
      std::cout << "Deleted managed folder: " << managed_folder_id << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.Control.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.html);
    using System;
    
    public class StorageControlDeleteManagedFolderSample
    {
        public void StorageControlDeleteManagedFolder(string bucketId = "your-unique-bucket-name",
            string managedFolderId = "your_managed_folder_id")
        {
            [StorageControlClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html) storageControl = [StorageControlClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html#Google_Cloud_Storage_Control_V2_StorageControlClient_Create)();
    
            [ManagedFolderName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolderName.html) managedFolderResourceName =
                // Set project to "_" to signify globally scoped bucket
                new [ManagedFolderName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolderName.html)("_", bucketId, managedFolderId);
    
            storageControl.[DeleteManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html#Google_Cloud_Storage_Control_V2_StorageControlClient_DeleteManagedFolder_Google_Cloud_Storage_Control_V2_DeleteManagedFolderRequest_Google_Api_Gax_Grpc_CallSettings_)(managedFolderResourceName);
    
            Console.WriteLine($"Deleted managed folder {managedFolderId} from bucket {bucketId}");
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
    
    	control "cloud.google.com/go/storage/control/apiv2"
    	"cloud.google.com/go/storage/control/apiv2/controlpb"
    )
    
    // deleteManagedFolder deletes the managed folder with the given name.
    func deleteManagedFolder(w io.Writer, bucket, folder string) error {
    	// bucket := "bucket-name"
    	// folder := "managed-folder-name"
    
    	ctx := context.Background()
    	client, err := control.NewStorageControlClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewStorageControlClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/control/apiv2.html#cloud_google_com_go_storage_control_apiv2_StorageControlClient_Close)()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*30)
    	defer cancel()
    
    	// Construct folder path including the bucket name.
    	folderPath := fmt.Sprintf("projects/_/buckets/%v/managedFolders/%v/", bucket, folder)
    
    	req := &controlpb.DeleteManagedFolderRequest{
    		Name: folderPath,
    	}
    	if err := client.DeleteManagedFolder(ctx, req); err != nil {
    		return fmt.Errorf("DeleteManagedFolder(%q): %w", folderPath, err)
    	}
    
    	fmt.Fprintf(w, "deleted managed folder %q", folderPath)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.storage.control.v2.[BucketName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.BucketName.html);
    import com.google.storage.control.v2.[DeleteManagedFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.DeleteManagedFolderRequest.html);
    import com.google.storage.control.v2.[ManagedFolderName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.ManagedFolderName.html);
    import com.google.storage.control.v2.[StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html);
    
    class DeleteManagedFolder {
      public static void managedFolderDelete(String bucketName, String managedFolderId)
          throws Exception {
        // Instantiates a client in a try-with-resource to automatically cleanup underlying resources
        try ([StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html) storageControlClient = [StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html).create()) {
          // Set project to "_" to signify global bucket
          [BucketName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.BucketName.html) resourceBucketName = [BucketName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.BucketName.html).of("_", bucketName);
          [DeleteManagedFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.DeleteManagedFolderRequest.html) deleteManagedFolderRequest =
              [DeleteManagedFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.DeleteManagedFolderRequest.html).newBuilder()
                  .setName(
                      [ManagedFolderName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.ManagedFolderName.html).format(
                          resourceBucketName.[getProject](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.BucketName.html#com_google_storage_control_v2_BucketName_getProject__)(),
                          resourceBucketName.[getBucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.BucketName.html#com_google_storage_control_v2_BucketName_getBucket__)(),
                          managedFolderId))
                  .build();
          storageControlClient.deleteManagedFolder(deleteManagedFolderRequest);
          System.out.printf("Deleted Managed Folder %s%n", managedFolderId);
        }
      }
    }
    

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    
    // The name of your GCS bucket
    // const bucketName = 'bucketName';
    
    // The name of the folder to be deleted
    // const managedFolderName = 'managedFolderName';
    
    // Imports the Control library
    const {StorageControlClient} = require('[@google-cloud/storage-control](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/overview.html)').v2;
    
    // Instantiates a client
    const controlClient = new [StorageControlClient](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/storagecontrolclient.html)();
    
    async function callDeleteManagedFolder() {
      const managedFolderPath = controlClient.[managedFolderPath](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/storagecontrolclient.html)(
        '_',
        bucketName,
        managedFolderName
      );
    
      // Create the request
      const request = {
        name: managedFolderPath,
      };
    
      // Run request
      await controlClient.deleteManagedFolder(request);
      console.log(`Deleted managed folder: ${managedFolderName}.`);
    }
    
    callDeleteManagedFolder();

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\Control\V2\Client\StorageControlClient;
    use Google\Cloud\Storage\Control\V2\DeleteManagedFolderRequest;
    
    /**
     * Delete a folder in an existing bucket.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $managedFolderId The id of your folder inside the bucket.
     *        (e.g. 'my-folder')
     */
    function managed_folder_delete(string $bucketName, string $managedFolderId): void
    {
        $storageControlClient = new StorageControlClient();
    
        // Set project to "_" to signify global bucket
        $formattedName = $storageControlClient->managedFolderName('_', $bucketName, $managedFolderId);
    
        $request = DeleteManagedFolderRequest::build($formattedName);
    
        $storageControlClient->deleteManagedFolder($request);
    
        printf('Deleted Managed Folder %s', $managedFolderId);
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage_control_v2](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest)
    
    
    def delete_managed_folder(bucket_name: str, managed_folder_id: str) -> None:
        # The ID of your GCS bucket
        # bucket_name = "your-unique-bucket-name"
    
        # The name of the managed folder to be deleted
        # managed_folder_id = "managed-folder-name"
    
        storage_control_client = [storage_control_v2](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest).[StorageControlClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.services.storage_control.StorageControlClient.html)()
        # The storage bucket path uses the global access pattern, in which the "_"
        # denotes this bucket exists in the global namespace.
        folder_path = storage_control_client.[managed_folder_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.services.storage_control.StorageControlClient.html#google_cloud_storage_control_v2_services_storage_control_StorageControlClient_managed_folder_path)(
            "_", bucket_name, managed_folder_id
        )
    
        request = [storage_control_v2](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest).[DeleteManagedFolderRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.types.DeleteManagedFolderRequest.html)(
            name=folder_path,
        )
        storage_control_client.[delete_managed_folder](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.services.storage_control.StorageControlClient.html#google_cloud_storage_control_v2_services_storage_control_StorageControlClient_delete_managed_folder)(request=request)
    
        print(f"Deleted managed folder: {managed_folder_id}")
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def delete_managed_folder bucket_name:, managed_folder_id:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      # The name of the managed folder to be created
      # managed_folder_id = "managed-folder-name"
    
      require "google/cloud/storage/control"
    
      storage_control = Google::Cloud::Storage::Control.storage_control
    
      # The storage bucket path uses the global access pattern, in which the "_"
      # denotes this bucket exists in the global namespace.
      folder_path = storage_control.managed_folder_path project: "_",
                                                        bucket: bucket_name,
                                                        managed_folder: managed_folder_id
    
      request = Google::Cloud::Storage::Control::V2::DeleteManagedFolderRequest.new name: folder_path
    
      storage_control.delete_managed_folder request
    
      puts "Deleted managed folder: #{managed_folder_id}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
