---
url: https://docs.cloud.google.com/storage/docs/samples/storage-control-managed-folder-list/
title: Storage Control List Managed Folders \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:30:30.905284+00:00
---

# Storage Control List Managed Folders  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-control-managed-folder-list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Storage Control List Managed Folders Stay organized with collections  Save and categorize content based on your preferences. 

Storage Control List Managed Folders

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create and manage managed folders](https://docs.cloud.google.com/storage/docs/creating-managing-managed-folders)



## Code sample

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace storagecontrol = google::cloud::storagecontrol_v2;
    [](storagecontrol::StorageControlClient client,
       std::string const& bucket_name) {
      auto const parent = std::string{"projects/_/buckets/"} + bucket_name;
      for (auto managed_folder : client.ListManagedFolders(parent)) {
        if (!managed_folder) throw std::move(managed_folder).status();
        std::cout << managed_folder->name() << "\n";
      }
    
      std::cout << bucket_name << std::endl;
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.Control.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.html);
    using System;
    using System.Collections.Generic;
    
    public class StorageControlListManagedFoldersSample
    {
        public IEnumerable<ManagedFolder> StorageControlListManagedFolders(string bucketId = "your-unique-bucket-name")
        {
            [StorageControlClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html) storageControl = [StorageControlClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html#Google_Cloud_Storage_Control_V2_StorageControlClient_Create)();
    
            // Use "_" for project ID to signify globally scoped bucket
            [BucketName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.BucketName.html) bucketResourceName = new [BucketName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.BucketName.html)("_", bucketId);
            var managedFolders = storageControl.[ListManagedFolders](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html#Google_Cloud_Storage_Control_V2_StorageControlClient_ListManagedFolders_Google_Cloud_Storage_Control_V2_BucketName_System_String_System_Nullable_System_Int32__Google_Api_Gax_Grpc_CallSettings_)(bucketResourceName);
    
            foreach (var managedFolder in managedFolders)
            {
                Console.Write(managedFolder.Name);
            }
            return managedFolders;
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
    	"google.golang.org/api/iterator"
    )
    
    // listManagedFolders lists all managed folders present in the bucket.
    func listManagedFolders(w io.Writer, bucket string) error {
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
    
    	// Construct bucket path for a bucket containing folders.
    	bucketPath := fmt.Sprintf("projects/_/buckets/%v", bucket)
    
    	// List all folders present.
    	req := &controlpb.ListManagedFoldersRequest{
    		Parent: bucketPath,
    	}
    	it := client.ListManagedFolders(ctx, req)
    	for {
    		f, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("ListManagedFolders(%q): %w", bucketPath, err)
    		}
    		fmt.Fprintf(w, "got managed folder %v\n", f.Name)
    	}
    
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.storage.control.v2.[BucketName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.BucketName.html);
    import com.google.storage.control.v2.[ListManagedFoldersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.ListManagedFoldersRequest.html);
    import com.google.storage.control.v2.[ManagedFolder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.ManagedFolder.html);
    import com.google.storage.control.v2.[StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html);
    
    class ListManagedFolders {
    
      public static void managedFolderList(String bucketName) throws Exception {
        // Instantiates a client in a try-with-resource to automatically cleanup underlying resources
        try ([StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html) storageControlClient = [StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html).create()) {
          [ListManagedFoldersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.ListManagedFoldersRequest.html) listManagedFoldersRequest =
              [ListManagedFoldersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.ListManagedFoldersRequest.html).newBuilder()
                  // Set project to "_" to signify global bucket
                  .setParent([BucketName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.BucketName.html).format("_", bucketName))
                  .build();
          Iterable<ManagedFolder> managedFolders =
              storageControlClient.listManagedFolders(listManagedFoldersRequest).iterateAll();
          for ([ManagedFolder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.ManagedFolder.html) folder : managedFolders) {
            System.out.printf("%s bucket has managed folder %s%n", bucketName, folder.getName());
          }
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
    
    // Imports the Control library
    const {StorageControlClient} = require('[@google-cloud/storage-control](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/overview.html)').v2;
    
    // Instantiates a client
    const controlClient = new [StorageControlClient](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/storagecontrolclient.html)();
    
    async function callListManagedFolders() {
      const bucketPath = controlClient.[bucketPath](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/storagecontrolclient.html)('_', bucketName);
    
      // Create the request
      const request = {
        parent: bucketPath,
      };
    
      // Run request
      const [folders] = await controlClient.listManagedFolders(request);
      for (const curManagedFolder of folders) {
        console.log(curManagedFolder.name);
      }
    }
    
    callListManagedFolders();

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\Control\V2\Client\StorageControlClient;
    use Google\Cloud\Storage\Control\V2\ListManagedFoldersRequest;
    
    /**
     * List folders in an existing bucket.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     */
    function managed_folders_list(string $bucketName): void
    {
        $storageControlClient = new StorageControlClient();
    
        // Set project to "_" to signify global bucket
        $formattedName = $storageControlClient->bucketName('_', $bucketName);
    
        $request = new ListManagedFoldersRequest([
            'parent' => $formattedName,
        ]);
    
        $folders = $storageControlClient->listManagedFolders($request);
    
        foreach ($folders as $folder) {
            printf('%s bucket has managed folder %s' . PHP_EOL, $bucketName, $folder->getName());
        }
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage_control_v2](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest)
    
    
    def list_managed_folders(bucket_name: str = "your-bucket-name") -> None:
        """Lists all managed folders in a Google Cloud Storage bucket.
    
        Args:
            bucket_name: The name of the Google Cloud Storage bucket.
    
        Returns:
            None. The function prints the name of each managed folder to the
            console.
    
        Example:
            >>> list_managed_folders(bucket_name="my-test-bucket")
            Managed folders in bucket projects/_/buckets/my-test-bucket:
                projects/_/buckets/my-test-bucket/managedFolders/folder-one
                projects/_/buckets/my-test-bucket/managedFolders/folder-two
        """
        client = [storage_control_v2](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest).[StorageControlClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.services.storage_control.StorageControlClient.html)()
    
        # The storage bucket path uses the global access pattern,
        # in which the "_" denotes this bucket exists in the global namespace.
        GLOBAL_NAMESPACE_PATTERN = "_"
        bucket_resource_name = (
            f"projects/{GLOBAL_NAMESPACE_PATTERN}/buckets/{bucket_name}"
        )
    
        managed_folders = client.[list_managed_folders](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.services.storage_control.StorageControlClient.html#google_cloud_storage_control_v2_services_storage_control_StorageControlClient_list_managed_folders)(parent=bucket_resource_name)
    
        print(f"Managed folders in bucket {bucket_resource_name}:")
        for managed_folder in managed_folders:
            print(f"\t{managed_folder.name}")
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def list_managed_folders bucket_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      require "google/cloud/storage/control"
    
      storage_control = Google::Cloud::Storage::Control.storage_control
    
      # The storage bucket path uses the global access pattern, in which the "_"
      # denotes this bucket exists in the global namespace.
      bucket_path = storage_control.bucket_path project: "_", bucket: bucket_name
    
      request = Google::Cloud::Storage::Control::V2::ListManagedFoldersRequest.new parent: bucket_path
    
      managed_folders = storage_control.list_managed_folders request
      managed_folders.each do |managed_folder|
        puts managed_folder
      end
    
      puts "Listed managed folders in bucket #{bucket_name}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
