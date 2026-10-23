---
url: https://docs.cloud.google.com/storage/docs/samples/storage-control-managed-folder-create/
title: Storage Control Create a Managed Folder \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:00.679332+00:00
---

# Storage Control Create a Managed Folder  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-control-managed-folder-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Storage Control Create a Managed Folder Stay organized with collections  Save and categorize content based on your preferences. 

Storage Control Create a Managed Folder

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
      auto const parent = std::string{"projects/_/buckets/"} + bucket_name;
      auto managed_folder = client.CreateManagedFolder(
          parent, google::storage::control::v2::ManagedFolder{},
          managed_folder_id);
      if (!managed_folder) throw std::move(managed_folder).status();
    
      std::cout << "Created managed folder: " << managed_folder->name() << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.Control.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.html);
    using System;
    
    public class StorageControlCreateManagedFolderSample
    {
        public ManagedFolder StorageControlCreateManagedFolder(string bucketId = "your-unique-bucket-name",
            string managedFolderId = "your_managed_folder_id")
        {
            [StorageControlClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html) storageControl = [StorageControlClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html#Google_Cloud_Storage_Control_V2_StorageControlClient_Create)();
    
            [ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder.html) managedFolder = storageControl.[CreateManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html#Google_Cloud_Storage_Control_V2_StorageControlClient_CreateManagedFolder_Google_Cloud_Storage_Control_V2_BucketName_Google_Cloud_Storage_Control_V2_ManagedFolder_System_String_Google_Api_Gax_Grpc_CallSettings_)(
                // Set project to "_" to signify globally scoped bucket
                new [BucketName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.BucketName.html)("_", bucketId),
                new [ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder.html)(),
                managedFolderId
            );
    
            Console.WriteLine($"Managed Folder {managedFolderId} created in bucket {bucketId}");
            return managedFolder;
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
    
    // createManagedFolder creates a managed folder in the bucket with the given name.
    func createManagedFolder(w io.Writer, bucket, folder string) error {
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
    	mf := &controlpb.ManagedFolder{}
    
    	req := &controlpb.CreateManagedFolderRequest{
    		Parent:          fmt.Sprintf("projects/_/buckets/%v", bucket),
    		ManagedFolder:   mf,
    		ManagedFolderId: folder,
    	}
    	f, err := client.CreateManagedFolder(ctx, req)
    	if err != nil {
    		return fmt.Errorf("CreateManagedFolder(%q): %w", folder, err)
    	}
    
    	fmt.Fprintf(w, "created Managed Folder with path %q", f.Name)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.storage.control.v2.[BucketName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.BucketName.html);
    import com.google.storage.control.v2.[CreateManagedFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.CreateManagedFolderRequest.html);
    import com.google.storage.control.v2.[ManagedFolder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.ManagedFolder.html);
    import com.google.storage.control.v2.[StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html);
    
    public class CreateManagedFolder {
      public static void managedFolderCreate(String bucketName, String managedFolderId)
          throws Exception {
    
        // Instantiates a client in a try-with-resource to automatically cleanup underlying resources
        try ([StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html) storageControlClient = [StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html).create()) {
          [CreateManagedFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.CreateManagedFolderRequest.html) request =
              [CreateManagedFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.CreateManagedFolderRequest.html).newBuilder()
                  // Set project to "_" to signify global bucket
                  .setParent([BucketName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.BucketName.html).format("_", bucketName))
                  .setManagedFolder([ManagedFolder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.ManagedFolder.html).newBuilder().build())
                  .[setManagedFolderId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.CreateManagedFolderRequest.Builder.html#com_google_storage_control_v2_CreateManagedFolderRequest_Builder_setManagedFolderId_java_lang_String_)(managedFolderId)
                  .build();
          String response = storageControlClient.createManagedFolder(request).getName();
          System.out.printf("Performed createManagedFolder request for %s%n", response);
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
    
    // The name of the managed folder to be created
    // const managedFolderName = 'managedFolderName';
    
    // Imports the Control library
    const {StorageControlClient} = require('[@google-cloud/storage-control](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/overview.html)').v2;
    
    // Instantiates a client
    const controlClient = new [StorageControlClient](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/storagecontrolclient.html)();
    
    async function callCreateManagedFolder() {
      const bucketPath = controlClient.[bucketPath](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/storagecontrolclient.html)('_', bucketName);
    
      // Create the request
      const request = {
        parent: bucketPath,
        managedFolderId: managedFolderName,
      };
    
      // Run request
      const [response] = await controlClient.createManagedFolder(request);
      console.log(`Created managed folder: ${response.name}.`);
    }
    
    callCreateManagedFolder();

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\Control\V2\Client\StorageControlClient;
    use Google\Cloud\Storage\Control\V2\CreateManagedFolderRequest;
    use Google\Cloud\Storage\Control\V2\ManagedFolder;
    
    /**
     * Create a new folder in an existing bucket.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $managedFolderId The name of your folder inside the bucket.
     *        (e.g. 'my-folder')
     */
    function managed_folder_create(string $bucketName, string $managedFolderId): void
    {
        $storageControlClient = new StorageControlClient();
    
        // Set project to "_" to signify global bucket
        $formattedName = $storageControlClient->bucketName('_', $bucketName);
    
        // $request = new CreateManagedFolderRequest([
        //     'parent' => $formattedName,
        //     'managedFolder' => new ManagedFolder(),
        //     'managedFolderId' => $managedFolderId,
        // ]);
        $request = CreateManagedFolderRequest::build($formattedName, new ManagedFolder(), $managedFolderId);
    
        $managedFolder = $storageControlClient->createManagedFolder($request);
    
        printf('Performed createManagedFolder request for %s', $managedFolder->getName());
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage_control_v2](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest)
    
    
    def create_managed_folder(bucket_name: str, managed_folder_id: str) -> None:
        # The ID of your GCS bucket
        # bucket_name = "your-unique-bucket-name"
    
        # The name of the managed folder to be created
        # managed_folder_id = "managed-folder-name"
    
        storage_control_client = [storage_control_v2](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest).[StorageControlClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.services.storage_control.StorageControlClient.html)()
        # The storage bucket path uses the global access pattern, in which the "_"
        # denotes this bucket exists in the global namespace.
        project_path = storage_control_client.[common_project_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.services.storage_control.StorageControlClient.html#google_cloud_storage_control_v2_services_storage_control_StorageControlClient_common_project_path)("_")
        bucket_path = f"{project_path}/buckets/{bucket_name}"
    
        request = [storage_control_v2](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest).[CreateManagedFolderRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.types.CreateManagedFolderRequest.html)(
            parent=bucket_path,
            managed_folder_id=managed_folder_id,
        )
        response = storage_control_client.[create_managed_folder](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.services.storage_control.StorageControlClient.html#google_cloud_storage_control_v2_services_storage_control_StorageControlClient_create_managed_folder)(request=request)
    
        print(f"Created managed folder: {response.name}")
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def create_managed_folder bucket_name:, managed_folder_id:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      # The name of the managed folder to be created
      # managed_folder_id = "managed-folder-name"
    
      require "google/cloud/storage/control"
    
      storage_control = Google::Cloud::Storage::Control.storage_control
    
      # The storage bucket path uses the global access pattern, in which the "_"
      # denotes this bucket exists in the global namespace.
      bucket_path = storage_control.bucket_path project: "_", bucket: bucket_name
    
      request = Google::Cloud::Storage::Control::V2::CreateManagedFolderRequest.new parent: bucket_path,
                                                                                    managed_folder_id: managed_folder_id
    
      response = storage_control.create_managed_folder request
    
      puts "Created managed folder: #{response.name}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
