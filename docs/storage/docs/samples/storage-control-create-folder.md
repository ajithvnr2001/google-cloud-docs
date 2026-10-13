---
url: https://docs.cloud.google.com/storage/docs/samples/storage-control-create-folder/
title: Storage Control Create Folder \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:05:36.912702+00:00
---

# Storage Control Create Folder  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-control-create-folder/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Storage Control Create Folder Stay organized with collections  Save and categorize content based on your preferences. 

Sample to create folder in Storage Control

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
      auto const parent = std::string{"projects/_/buckets/"} + bucket_name;
      auto folder = client.CreateFolder(
          parent, google::storage::control::v2::Folder{}, folder_id);
      if (!folder) throw std::move(folder).status();
    
      std::cout << "Created folder: " << folder->name() << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.Control.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.html);
    using System;
    
    public class StorageControlCreateFolderSample
    {
        public Folder StorageControlCreateFolder(string bucketName = "your-unique-bucket-name",
            string folderName = "your_folder_name")
        {
            [StorageControlClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html) storageControl = [StorageControlClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html#Google_Cloud_Storage_Control_V2_StorageControlClient_Create)();
    
            var request = new [CreateFolderRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.CreateFolderRequest.html)
            {
                // Set project to "_" to signify globally scoped bucket
                Parent = [BucketName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.BucketName.html).[FormatProjectBucket](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.BucketName.html#Google_Cloud_Storage_Control_V2_BucketName_FormatProjectBucket_System_String_System_String_)("_", bucketName),
                FolderId = folderName
            };
    
            [Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder.html) folder = storageControl.[CreateFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html#Google_Cloud_Storage_Control_V2_StorageControlClient_CreateFolder_Google_Cloud_Storage_Control_V2_BucketName_Google_Cloud_Storage_Control_V2_Folder_System_String_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            Console.WriteLine($"Folder {folderName} created in bucket {bucketName}");
            return folder;
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
    
    // createFolder creates a folder in the bucket with the given name.
    func createFolder(w io.Writer, bucket, folder string) error {
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
    
    	req := &controlpb.CreateFolderRequest{
    		Parent:   fmt.Sprintf("projects/_/buckets/%v", bucket),
    		FolderId: folder,
    	}
    	f, err := client.CreateFolder(ctx, req)
    	if err != nil {
    		return fmt.Errorf("CreateFolder(%q): %w", folder, err)
    	}
    
    	fmt.Fprintf(w, "created folder with path %q", f.Name)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.storage.control.v2.[BucketName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.BucketName.html);
    import com.google.storage.control.v2.[CreateFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.CreateFolderRequest.html);
    import com.google.storage.control.v2.[Folder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.Folder.html);
    import com.google.storage.control.v2.[StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html);
    import java.io.IOException;
    
    public final class CreateFolder {
    
      public static void createFolder(String bucketName, String folderName) throws IOException {
        // The name of the bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The name of the folder within the bucket
        // String folderName = "your-unique-folder-name";
    
        try ([StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html) storageControl = [StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html).create()) {
    
          [CreateFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.CreateFolderRequest.html) request =
              [CreateFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.CreateFolderRequest.html).newBuilder()
                  // Set project to "_" to signify globally scoped bucket
                  .setParent([BucketName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.BucketName.html).format("_", bucketName))
                  .setFolderId(folderName)
                  .build();
    
          [Folder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.Folder.html) newFolder = storageControl.createFolder(request);
    
          System.out.printf("Created folder: %s%n", newFolder.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.Folder.html#com_google_storage_control_v2_Folder_getName__)());
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
    
    // The name of the folder to be created
    // const folderName = 'folderName';
    
    // Imports the Control library
    const {StorageControlClient} = require('[@google-cloud/storage-control](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/overview.html)').v2;
    
    // Instantiates a client
    const controlClient = new [StorageControlClient](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/storagecontrolclient.html)();
    
    async function callCreateFolder() {
      const bucketPath = controlClient.[bucketPath](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/storagecontrolclient.html)('_', bucketName);
    
      // Create the request
      const request = {
        parent: bucketPath,
        folderId: folderName,
      };
    
      // Run request
      const [response] = await controlClient.createFolder(request);
      console.log(`Created folder: ${response.name}.`);
    }
    
    callCreateFolder();

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\Control\V2\Client\StorageControlClient;
    use Google\Cloud\Storage\Control\V2\CreateFolderRequest;
    
    /**
     * Create a new folder in an existing bucket.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $folderName The name of your folder inside the bucket.
     *        (e.g. 'my-folder')
     */
    function create_folder(string $bucketName, string $folderName): void
    {
        $storageControlClient = new StorageControlClient();
    
        // Set project to "_" to signify global bucket
        $formattedName = $storageControlClient->bucketName('_', $bucketName);
    
        $request = new CreateFolderRequest([
            'parent' => $formattedName,
            'folder_id' => $folderName,
        ]);
    
        $folder = $storageControlClient->createFolder($request);
    
        printf('Created folder: %s', $folder->getName());
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage_control_v2](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest)
    
    
    def create_folder(bucket_name: str, folder_name: str) -> None:
        # The ID of your GCS bucket
        # bucket_name = "your-unique-bucket-name"
    
        # The name of the folder to be created
        # folder_name = "folder-name"
    
        storage_control_client = [storage_control_v2](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest).[StorageControlClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.services.storage_control.StorageControlClient.html)()
        # The storage bucket path uses the global access pattern, in which the "_"
        # denotes this bucket exists in the global namespace.
        project_path = storage_control_client.[common_project_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.services.storage_control.StorageControlClient.html#google_cloud_storage_control_v2_services_storage_control_StorageControlClient_common_project_path)("_")
        bucket_path = f"{project_path}/buckets/{bucket_name}"
    
        request = [storage_control_v2](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest).[CreateFolderRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.types.CreateFolderRequest.html)(
            parent=bucket_path,
            folder_id=folder_name,
        )
        response = storage_control_client.[create_folder](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.services.storage_control.StorageControlClient.html#google_cloud_storage_control_v2_services_storage_control_StorageControlClient_create_folder)(request=request)
    
        print(f"Created folder: {response.name}")
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def create_folder bucket_name:, folder_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      # The name of the folder to be created
      # folder_name = "folder-name"
    
      require "google/cloud/storage/control"
    
      storage_control = Google::Cloud::Storage::Control.storage_control
    
      # The storage bucket path uses the global access pattern, in which the "_"
      # denotes this bucket exists in the global namespace.
      bucket_path = storage_control.bucket_path project: "_", bucket: bucket_name
    
      request = Google::Cloud::Storage::Control::V2::CreateFolderRequest.new parent: bucket_path, folder_id: folder_name
    
      response = storage_control.create_folder request
    
      puts "Created folder: #{response.name}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
