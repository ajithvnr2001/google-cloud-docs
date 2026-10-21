---
url: https://docs.cloud.google.com/storage/docs/samples/storage-control-delete-folder/
title: Storage Control Delete Folder \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:17:05.221997+00:00
---

# Storage Control Delete Folder  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-control-delete-folder/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Storage Control Delete Folder Stay organized with collections  Save and categorize content based on your preferences. 

How to delete a folder in an HNS bucket.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create and manage folders](https://docs.cloud.google.com/storage/docs/create-folders)



## Code sample

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace storagecontrol = google::cloud::storagecontrol_v2;
    [](storagecontrol::StorageControlClient client,
       std::string const& bucket_name, std::string const& folder_id) {
      auto const name = std::string{"projects/_/buckets/"} + bucket_name +
                        "/folders/" + folder_id;
      auto status = client.DeleteFolder(name);
      if (!status.ok()) throw std::move(status);
    
      std::cout << "Deleted folder: " << folder_id << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.Control.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.html);
    using System;
    
    public class StorageControlDeleteFolderSample
    {
        public void StorageControlDeleteFolder(string bucketName = "your-unique-bucket-name",
            string folderName = "your_folder_name")
        {
            [StorageControlClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html) storageControl = [StorageControlClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html#Google_Cloud_Storage_Control_V2_StorageControlClient_Create)();
    
            string folderResourceName =
                // Set project to "_" to signify globally scoped bucket
                [FolderName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.FolderName.html).[FormatProjectBucketFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.FolderName.html#Google_Cloud_Storage_Control_V2_FolderName_FormatProjectBucketFolder_System_String_System_String_System_String_)("_", bucketName, folderName);
    
            storageControl.[DeleteFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html#Google_Cloud_Storage_Control_V2_StorageControlClient_DeleteFolder_Google_Cloud_Storage_Control_V2_DeleteFolderRequest_Google_Api_Gax_Grpc_CallSettings_)(folderResourceName);
    
            Console.WriteLine($"Deleted folder {folderName} from bucket {bucketName}");
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
    
    // deleteFolder deletes the folder with the given name.
    func deleteFolder(w io.Writer, bucket, folder string) error {
    	// bucket := "bucket-name"
    	// folder := "folder-name"
    
    	ctx := context.Background()
    	client, err := control.NewStorageControlClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewStorageControlClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/control/apiv2.html#cloud_google_com_go_storage_control_apiv2_StorageControlClient_Close)()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*30)
    	defer cancel()
    
    	// Construct folder path including the bucket name.
    	folderPath := fmt.Sprintf("projects/_/buckets/%v/folders/%v", bucket, folder)
    
    	req := &controlpb.DeleteFolderRequest{
    		Name: folderPath,
    	}
    	if err := client.DeleteFolder(ctx, req); err != nil {
    		return fmt.Errorf("DeleteFolder(%q): %w", folderPath, err)
    	}
    
    	fmt.Fprintf(w, "deleted folder %q", folderPath)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.storage.control.v2.[DeleteFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.DeleteFolderRequest.html);
    import com.google.storage.control.v2.[FolderName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.FolderName.html);
    import com.google.storage.control.v2.[StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html);
    import java.io.IOException;
    
    public final class DeleteFolder {
    
      public static void deleteFolder(String bucketName, String folderName) throws IOException {
        // The name of the bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The name of the folder within the bucket
        // String folderName = "your-unique-folder-name";
    
        try ([StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html) storageControl = [StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html).create()) {
    
          // Set project to "_" to signify globally scoped bucket
          String folderResourceName = [FolderName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.FolderName.html).format("_", bucketName, folderName);
          [DeleteFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.DeleteFolderRequest.html) request =
              [DeleteFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.DeleteFolderRequest.html).newBuilder().setName(folderResourceName).build();
    
          storageControl.deleteFolder(request);
    
          System.out.printf("Deleted folder: %s%n", folderResourceName);
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
    // const folderName = 'folderName';
    
    // Imports the Control library
    const {StorageControlClient} = require('[@google-cloud/storage-control](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/overview.html)').v2;
    
    // Instantiates a client
    const controlClient = new [StorageControlClient](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/storagecontrolclient.html)();
    
    async function callDeleteFolder() {
      const folderPath = controlClient.[folderPath](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/storagecontrolclient.html)('_', bucketName, folderName);
    
      // Create the request
      const request = {
        name: folderPath,
      };
    
      // Run request
      await controlClient.deleteFolder(request);
      console.log(`Deleted folder: ${folderName}.`);
    }
    
    callDeleteFolder();

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\Control\V2\Client\StorageControlClient;
    use Google\Cloud\Storage\Control\V2\DeleteFolderRequest;
    
    /**
     * Delete a folder in an existing bucket.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $folderName The name of your folder inside the bucket.
     *        (e.g. 'my-folder')
     */
    function delete_folder(string $bucketName, string $folderName): void
    {
        $storageControlClient = new StorageControlClient();
    
        // Set project to "_" to signify global bucket
        $formattedName = $storageControlClient->folderName('_', $bucketName, $folderName);
    
        $request = new DeleteFolderRequest([
            'name' => $formattedName,
        ]);
    
        $storageControlClient->deleteFolder($request);
    
        printf('Deleted folder: %s', $folderName);
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage_control_v2](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest)
    
    
    def delete_folder(bucket_name: str, folder_name: str) -> None:
        # The ID of your GCS bucket
        # bucket_name = "your-unique-bucket-name"
    
        # The name of the folder to be deleted
        # folder_name = "folder-name"
    
        storage_control_client = [storage_control_v2](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest).[StorageControlClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.services.storage_control.StorageControlClient.html)()
        # The storage bucket path uses the global access pattern, in which the "_"
        # denotes this bucket exists in the global namespace.
        folder_path = storage_control_client.[folder_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.services.storage_control.StorageControlClient.html#google_cloud_storage_control_v2_services_storage_control_StorageControlClient_folder_path)(
            project="_", bucket=bucket_name, folder=folder_name
        )
    
        request = [storage_control_v2](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest).[DeleteFolderRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.types.DeleteFolderRequest.html)(
            name=folder_path,
        )
        storage_control_client.[delete_folder](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.services.storage_control.StorageControlClient.html#google_cloud_storage_control_v2_services_storage_control_StorageControlClient_delete_folder)(request=request)
    
        print(f"Deleted folder {folder_name}")
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def delete_folder bucket_name:, folder_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
      #
      # Name of the folder you want to delete
      # folder_name = "name-of-the-folder"
    
      require "google/cloud/storage/control"
    
      storage_control = Google::Cloud::Storage::Control.storage_control
    
      # The storage folder path uses the global access pattern, in which the "_"
      # denotes this bucket exists in the global namespace.
      folder_path = storage_control.folder_path project: "_", bucket: bucket_name, folder: folder_name
    
      request = Google::Cloud::Storage::Control::V2::DeleteFolderRequest.new name: folder_path
    
      storage_control.delete_folder request
    
      puts "Deleted folder: #{folder_name}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
