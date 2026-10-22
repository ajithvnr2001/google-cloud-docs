---
url: https://docs.cloud.google.com/storage/docs/creating-managing-managed-folders/
title: Create and manage managed folders \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:29:17.950861+00:00
---

# Create and manage managed folders  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/creating-managing-managed-folders/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Create and manage managed folders Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create, list, get, update, and delete [managed folders](https://docs.cloud.google.com/storage/docs/managed-folders).

Managed folders let you control access to groups of objects in your Cloud Storage buckets by selectively setting IAM policies to objects that have a common prefix in their object name paths. This approach helps you meet data security and compliance requirements.

Managed folders can also be used to enable Rapid Cache caches to ingest data on write selectively by object name prefix. For more information, see [Ingest-on-write](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache#ingest-on-write).

## Before you begin

To create and manage managed folders, you must first enable uniform bucket-level access and get the required IAM roles.

### Enable uniform bucket-level access

If you haven't already, [enable uniform bucket-level access](https://docs.cloud.google.com/storage/docs/using-uniform-bucket-level-access).

### Get required roles

To get the permissions that you need to create and manage managed folders, ask your administrator to grant you the [Storage Folder Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.folderAdmin) (`roles/storage.folderAdmin`) IAM role on the bucket. 

This predefined role contains the permissions required to create and manage managed folders. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create and manage managed folders:

  * To create managed folders: `storage.managedFolders.create`
  * To validate newly created managed folders by listing them: `storage.objects.list`
  * To list managed folders: `storage.managedFolders.list`
  * To get managed folders: `storage.managedFolders.get`
  * To move managed folders: 
    * `storage.managedFolders.delete` (on the source bucket)
    * `storage.managedFolders.create` (on the destination bucket)
  * To update managed folders: `storage.managedFolders.update`
  * To delete managed folders: `storage.managedFolders.delete`



For information about granting roles on buckets, see [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).

## Create a managed folder

### Console

When using the Google Cloud console, you create managed folders by enabling management on folders or simulated folders. The following steps describe how to create a folder or a simulated folder and then enable folder management:

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket you want to create managed folders in.

  3. In the **Bucket details** page, click **Create folder** to create a new folder. If the folder you want to convert to a managed folder already exists, skip to the step describing how to access the **More options** more_vert menu.

  4. In the **Name** field, enter a name for your folder. For naming considerations, see [Managed folder names](https://docs.cloud.google.com/storage/docs/managed-folders#managed_folder_names).

  5. Click **Create**.

Your newly created folder appears in the **Folder browser** pane.

  6. In the **Folder browser** pane, click the **More options** more_vert menu next to the folder you want to convert to a managed folder and click **Edit access**.

The **Enable folder management?** dialog appears.

  7. Click **Enable**.

Your folder converts to a managed folder. A **Permissions for` MANAGED_FOLDER_NAME`** pane appears that displays the IAM policies on the folder by principal and role. To create new IAM policies, see [Set an IAM policy on a managed folder](https://docs.cloud.google.com/storage/docs/access-control/using-iam-for-managed-folders#managed-folder-set-policy).




### Command line

To create a managed folder, run the [`gcloud storage managed-folders create` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/managed-folders/create):
    
    
    gcloud storage managed-folders create gs://BUCKET_NAME/MANAGED_FOLDER_NAME

Where:

  * `BUCKET_NAME` is the name of the bucket in which you want to create a managed folder. For example, `my-bucket`.

  * `MANAGED_FOLDER_NAME` is the name of the managed folder you want to create. For example, `my-managed-folder/`.




To confirm that the managed folder was created, run the `gcloud storage managed-folders describe` command:
    
    
    gcloud storage managed-folders describe gs://BUCKET_NAME/MANAGED_FOLDER_NAME

Where:

  * `BUCKET_NAME` is the name of the bucket in which you created a managed folder.

  * `MANAGED_FOLDER_NAME` is the name of the managed folder you created.




### Client libraries

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

For more information, see the [Cloud Storage Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2). 

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

### Rust
    
    
    use google_cloud_storage::{client::StorageControl, model::ManagedFolder};
    
    pub async fn sample(client: &StorageControl, bucket_id: &str) -> anyhow::Result<()> {
        const ID: &str = "example001";
        let folder = client
            .create_managed_folder()
            .set_parent(format!("projects/_/buckets/{bucket_id}"))
            .set_managed_folder_id(ID)
            .set_managed_folder(ManagedFolder::new())
            .send()
            .await?;
        println!("folder successfully created {folder:?}");
        Ok(())
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`POST` ManagedFolder](https://docs.cloud.google.com/storage/docs/json_api/v1/managedFolder/insert) request:
         
         curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -d '{ "name": "MANAGED_FOLDER_NAME" }' \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/managedFolders"

Where:

     * `MANAGED_FOLDER_NAME` is the name of the managed folder you want to create. For example, `my-managed-folder/`.

     * `BUCKET_NAME` is the name of the bucket in which you want to create a managed folder. For example, `my-bucket`.

### Create a managed folder to enable Rapid Cache ingest-on-write

This section describes how to create a managed folder with settings that enable the Rapid Cache ingest-on-write feature at the prefix level. If you don't use Rapid Cache or its ingest-on-write feature, skip this section.

If you want to create a managed folder to enable [prefix-level ingest on write](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache#ingest-on-write) for caches created with Rapid Cache:

     1. Read [Understanding how to enable ingest-on-write](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache#ingest-on-write-requirements) to familiarize yourself with how prefix-level ingest-on-write is configured.

     2. Ensure that the cache's `ingestOnWrite` property is set to `false`. For instructions, see [Update a cache](https://docs.cloud.google.com/storage/docs/rapid/use-rapid-cache#update-cache-rest).

     3. Include a `rapidCacheConfig` configuration in your request:
    
    curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "name": "MANAGED_FOLDER_NAME",
        "rapidCacheConfig": {
          "policies": {
            "RAPID_CACHE_ID": {
              "rapidCacheId": "RAPID_CACHE_ID",
              "ingestOnWrite": "enabled"
            }
          }
        }
      }' \
      "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/managedFolders"

Where:

     * `MANAGED_FOLDER_NAME` is the name of the managed folder you want to create. The cache uses this managed folder name to selectively ingest objects on write. For example, if you specify `my-managed-folder/` as the managed folder's name, the cache will only ingest objects in the bucket whose name includes `my-managed-folder/` in its path.

     * `RAPID_CACHE_ID` is the identifier for the cache, which is the zone of the cache. For example, `us-east1-b`. The cache you specify must be associated with the bucket in which the managed folder is being created. To find the caches associated with a bucket, [list the caches for the bucket](https://docs.cloud.google.com/storage/docs/rapid/use-rapid-cache#list-caches).

     * `BUCKET_NAME` is the name of the bucket that's associated with the cache. For example, `my-cached-bucket`. The managed folder will be created in this bucket. 




## List managed folders

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. From the **Folder browser** pane, use the **toggle node** arrow_right to expand the list of folders within your bucket.




A list displays the folders, simulated folders, and managed folders in your bucket.

### Command line

To list managed folders, run the [`gcloud storage managed-folders list` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/managed-folders/list):
    
    
    gcloud storage managed-folders list gs://BUCKET_NAME

Where:

  * `BUCKET_NAME` is the name of the bucket that contains the managed folders you want to list. For example, `my-bucket`.



Note that you can also specify a folder path instead of a bucket name. For example:
    
    
    gcloud storage managed-folders list gs://my-bucket/folder/

### Client libraries

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

For more information, see the [Cloud Storage Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2). 

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

### Rust
    
    
    use google_cloud_gax::paginator::ItemPaginator;
    use google_cloud_storage::client::StorageControl;
    
    pub async fn sample(client: &StorageControl, bucket_id: &str) -> anyhow::Result<()> {
        let mut items = client
            .list_managed_folders()
            .set_parent(format!("projects/_/buckets/{bucket_id}"))
            .by_item();
        println!("Listing managed folders in bucket {bucket_id}");
        while let Some(folder) = items.next().await.transpose()? {
            println!("{folder:?}");
        }
        println!("DONE");
        Ok(())
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [request to list managed folders](https://docs.cloud.google.com/storage/docs/json_api/v1/managedFolder/list):
         
         curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/managedFolders"

Where `BUCKET_NAME` is the name of the bucket that contains the managed folders you want to list. For example, `my-bucket`.




## Get the metadata of a managed folder

### Command line

To get the metadata of a managed folder, run the [`gcloud storage managed-folders describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/managed-folders/describe):
    
    
      gcloud storage managed-folders describe gs://BUCKET_NAME/MANAGED_FOLDER_NAME
    

Where:

  * `BUCKET_NAME` is the name of the bucket that contains the managed folders you want to list. For example, `my-bucket`.

  * `MANAGED_FOLDER_NAME` is the name of the managed folder you want to retrieve metadata for.




### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace storagecontrol = google::cloud::storagecontrol_v2;
    [](storagecontrol::StorageControlClient client,
       std::string const& bucket_name, std::string const& managed_folder_id) {
      auto const name = std::string{"projects/_/buckets/"} + bucket_name +
                        "/managedFolders/" + managed_folder_id;
      auto managed_folder = client.GetManagedFolder(name);
      if (!managed_folder) throw std::move(managed_folder).status();
    
      std::cout << "Got managed folder: " << managed_folder->name() << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.Control.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.html);
    using System;
    
    public class StorageControlGetManagedFolderSample
    {
        public ManagedFolder StorageControlGetManagedFolder(string bucketId = "your-unique-bucket-name",
            string managedFolderId = "your_managed_folder_Id")
        {
            [StorageControlClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html) storageControl = [StorageControlClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html#Google_Cloud_Storage_Control_V2_StorageControlClient_Create)();
    
            [ManagedFolderName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolderName.html) managedFolderResourceName =
                // Set project to "_" to signify globally scoped bucket
                new [ManagedFolderName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolderName.html)("_", bucketId, managedFolderId);
    
            [ManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder.html) managedFolder = storageControl.[GetManagedFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html#Google_Cloud_Storage_Control_V2_StorageControlClient_GetManagedFolder_Google_Cloud_Storage_Control_V2_GetManagedFolderRequest_Google_Api_Gax_Grpc_CallSettings_)(managedFolderResourceName);
    
            Console.WriteLine($"Got managed folder: {managedFolder.[Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ManagedFolder.html#Google_Cloud_Storage_Control_V2_ManagedFolder_Name)}");
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
    
    // getManagedFolder gets metadata for the managed folder with the given name.
    func getManagedFolder(w io.Writer, bucket, folder string) error {
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
    
    	req := &controlpb.GetManagedFolderRequest{
    		Name: folderPath,
    	}
    	f, err := client.GetManagedFolder(ctx, req)
    	if err != nil {
    		return fmt.Errorf("GetManagedFolder(%q): %w", folderPath, err)
    	}
    
    	fmt.Fprintf(w, "got managed folder metadata: %+v", f)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.storage.control.v2.[BucketName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.BucketName.html);
    import com.google.storage.control.v2.[GetManagedFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.GetManagedFolderRequest.html);
    import com.google.storage.control.v2.[ManagedFolder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.ManagedFolder.html);
    import com.google.storage.control.v2.[ManagedFolderName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.ManagedFolderName.html);
    import com.google.storage.control.v2.[StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html);
    
    class GetManagedFolder {
    
      public static void managedFolderGet(String bucketName, String managedFolderId) throws Exception {
        // Instantiates a client in a try-with-resource to automatically cleanup underlying resources
        try ([StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html) storageControlClient = [StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html).create()) {
          // Set project to "_" to signify global bucket
          [BucketName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.BucketName.html) resourceBucketName = [BucketName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.BucketName.html).of("_", bucketName);
          [GetManagedFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.GetManagedFolderRequest.html) getManagedFolderRequest =
              [GetManagedFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.GetManagedFolderRequest.html).newBuilder()
                  .setName(
                      [ManagedFolderName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.ManagedFolderName.html).format(
                          resourceBucketName.[getProject](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.BucketName.html#com_google_storage_control_v2_BucketName_getProject__)(),
                          resourceBucketName.[getBucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.BucketName.html#com_google_storage_control_v2_BucketName_getBucket__)(),
                          managedFolderId))
                  .build();
          [ManagedFolder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.ManagedFolder.html) managedFolder = storageControlClient.getManagedFolder(getManagedFolderRequest);
          System.out.printf("Got Managed Folder %s%n", managedFolder.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.ManagedFolder.html#com_google_storage_control_v2_ManagedFolder_getName__)());
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
    
    // The name of the managed folder to get
    // const managedFolderName = 'managedFolderName';
    
    // Imports the Control library
    const {StorageControlClient} = require('[@google-cloud/storage-control](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/overview.html)').v2;
    
    // Instantiates a client
    const controlClient = new [StorageControlClient](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/storagecontrolclient.html)();
    
    async function callGetManagedFolder() {
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
      const [response] = await controlClient.getManagedFolder(request);
      console.log(`Got managed folder: ${response.name}.`);
    }
    
    callGetManagedFolder();

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\Control\V2\Client\StorageControlClient;
    use Google\Cloud\Storage\Control\V2\GetManagedFolderRequest;
    
    /**
     * Get a folder in an existing bucket.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $managedFolderId The name of your folder inside the bucket.
     *        (e.g. 'my-folder')
     */
    function managed_folder_get(string $bucketName, string $managedFolderId): void
    {
        $storageControlClient = new StorageControlClient();
    
        // Set project to "_" to signify global bucket
        $formattedName = $storageControlClient->managedFolderName('_', $bucketName, $managedFolderId);
    
        $request = new GetManagedFolderRequest([
            'name' => $formattedName,
        ]);
    
        $managedFolder = $storageControlClient->getManagedFolder($request);
    
        printf('Got Managed Folder %s', $managedFolder->getName());
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage_control_v2](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest)
    
    
    def get_managed_folder(bucket_name: str, managed_folder_id: str) -> None:
        # The ID of your GCS bucket
        # bucket_name = "your-unique-bucket-name"
    
        # The name of the managed folder
        # managed_folder_id = "managed-folder-name"
    
        storage_control_client = [storage_control_v2](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest).[StorageControlClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.services.storage_control.StorageControlClient.html)()
        # The storage bucket path uses the global access pattern, in which the "_"
        # denotes this bucket exists in the global namespace.
        folder_path = storage_control_client.[managed_folder_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.services.storage_control.StorageControlClient.html#google_cloud_storage_control_v2_services_storage_control_StorageControlClient_managed_folder_path)(
            "_", bucket_name, managed_folder_id
        )
    
        request = [storage_control_v2](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest).[GetManagedFolderRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.types.GetManagedFolderRequest.html)(
            name=folder_path,
        )
        response = storage_control_client.[get_managed_folder](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.services.storage_control.StorageControlClient.html#google_cloud_storage_control_v2_services_storage_control_StorageControlClient_get_managed_folder)(request=request)
    
        print(f"Got managed folder: {response.name}")
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def get_managed_folder bucket_name:, managed_folder_id:
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
    
      request = Google::Cloud::Storage::Control::V2::GetManagedFolderRequest.new name: folder_path
    
      response = storage_control.get_managed_folder request
    
      puts "Got managed folder: #{response.name}"
    end

### Rust
    
    
    use google_cloud_storage::client::StorageControl;
    
    pub async fn sample(client: &StorageControl, bucket_id: &str) -> anyhow::Result<()> {
        const ID: &str = "example001";
        let folder = client
            .get_managed_folder()
            .set_name(format!(
                "projects/_/buckets/{bucket_id}/managedFolders/{ID}"
            ))
            .send()
            .await?;
        println!("successfully retrieved managed folder metadata: {folder:?}");
        Ok(())
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [request to get managed folders](https://docs.cloud.google.com/storage/docs/json_api/v1/managedFolder/get):
         
         curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/managedFolders/MANAGED_FOLDER_NAME"

Where:

     * `BUCKET_NAME` is the name of the bucket that contains the managed folders you want to get. For example, `my-bucket`.

     * `MANAGED_FOLDER_NAME` is the name of the managed folder expressed as a path. For example, `example-dir/`. If the managed folder is nested, the slash (`/`) character in the managed folder path must be escaped. For example, `example-dir1%2Fexample-dir2`.




## Move a managed folder

### Console

  1. Create a new managed folder in the destination bucket.

  2. [Copy the IAM policies](https://docs.cloud.google.com/storage/docs/access-control/using-iam-for-managed-folders) from the original managed folder in the source bucket into the new managed folder in the destination bucket.

  3. [Copy the objects](https://docs.cloud.google.com/storage/docs/copying-renaming-moving-objects) from the original managed folder in the source bucket to the new managed folder in the destination bucket.

  4. [Delete the original managed folder](https://docs.cloud.google.com/storage/docs/creating-managing-managed-folders#delete) from the source bucket.




### Command line

To move managed folders and the objects they contain, run the [`gcloud storage mv` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/mv) with the `--include-managed-folders` option:
    
    
    gcloud storage mv --include-managed-folders gs://SOURCE_BUCKET_NAME/MANAGED_FOLDER_NAME gs://DESTINATION_BUCKET_NAME/MANAGED_FOLDER_NAME

Where:

  * `SOURCE_BUCKET` is the name of your original bucket. For example, `my-source-bucket``.

  * `DESTINATION_BUCKET` is the name of the bucket you are moving your managed folder to. For example, `my-destination-bucket`.

  * `MANAGED_FOLDER_NAME` is the name of the managed folder you're moving. For example, `my-managed-folder/`.




### REST APIs

### JSON API

To move managed folders from one bucket to another, complete the following steps:

  1. Create a new managed folder in the destination bucket.

  2. [Copy the IAM policies](https://docs.cloud.google.com/storage/docs/access-control/using-iam-for-managed-folders) from the original managed folder in the source bucket to the new managed folder in the destination bucket.

  3. [Copy the objects](https://docs.cloud.google.com/storage/docs/copying-renaming-moving-objects) from the original managed folder in the source bucket to the new managed folder in the destination bucket.

  4. Delete the original managed folder from the source bucket.




## Update the Rapid Cache ingest-on-write policy on a managed folder

This section describes how to enable or disable the Rapid Cache ingest-on-write setting at the prefix level, which uses managed folders as an underlying mechanism. If you don't use Rapid Cache or its ingest-on-write feature, skip this section.

To enable or disable the Rapid Cache [ingest-on-write policy](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache#ingest-on-write) for objects that share a managed folder prefix, you must update the `rapidCacheConfig` configuration of the managed folder. These instructions are only required when you use the JSON API to update a cache's ingest-on-write policy.

For more details on how to enable or disable ingest-on-write at the prefix level, see [Understanding ingest-on-write](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache#ingest-on-write-requirements).

### REST APIs

### JSON API

To add, modify, or delete the Rapid Cache ingest-on-write policy on a managed folder:

  1. Ensure that you've [set the `ingestOnWrite` property in the cache's configuration](https://docs.cloud.google.com/storage/docs/rapid/use-rapid-cache#update-cache-rest). Refer to [Understanding ingest-on-write](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache#ingest-on-write-requirements) for which value to set the property to.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a `PATCH` ManagedFolder request. The request body differs depending on your use case:

### Enable or disable the ingest on write policy for a managed folder

To update the ingest on write configuration for one or multiple caches, use the following command:
         
         curl -X PATCH -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -d '{
          "rapidCacheConfig": {
            "policies": {
              "RAPID_CACHE_ID": {
                "rapidCacheId": "RAPID_CACHE_ID",
                "ingestOnWrite": "INGEST_VALUE"
              }
            }
          }
         }' \
         "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/managedFolders/MANAGED_FOLDER_NAME"

Replace:

     * `BUCKET_NAME`: with the name of the bucket containing the managed folder.

     * `MANAGED_FOLDER_NAME`: with the name of the managed folder.

     * `RAPID_CACHE_ID`: with the identifier for the cache, which is the zone of the cache. For example, `us-east1-b`.

     * `INGEST_VALUE`: with the ingestion behavior of the cache. When the value is `enabled`, ingest-on-write for managed folder prefixes is enabled. When the value is `unspecified`, the cache's ingest-on-write behavior is inherited either from a parent managed folder if it exists, or from the cache configuration on the bucket. For more information on the behaviors set by these values, see [Ingest-on-write requirements](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache#ingest-on-write-requirements). Carefully read about [ingest-on-write inheritance](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache#ingest-on-write-inheritance) to understand how a cache's ingest-on-write policy can be affected when the `ingestOnWrite` setting for the cache is set to `unspecified`.

To configure ingest on write for multiple caches at a time, include multiple `policies` maps in your request. For example:
    
    "rapidCacheConfig": {
    "policies": {
      "us-east1-a": {
        "rapidCacheId": "us-east1-a",
        "ingestOnWrite": "unspecified"
      }
      "us-east1-b": {
        "rapidCacheId": "us-east1-b",
        "ingestOnWrite": "enabled"
      }
    }
    }
    

To disable prefix-level ingest on write for individual caches, remove the `policies` map for the cache from the `rapidCacheConfig` configuration.

### Delete an ingest-on-write policy on a managed folder

You can delete the ingest-on-write policy on a managed folder by using the instructions in this section. When you delete the ingest-on-write policy on a managed folder, the caches you specify in your request won't ingest objects on write by their managed folder prefix, and the ingestion behavior for objects in the bucket will be determined by the `ingestOnWrite` field of the cache configuration. To learn how the ingest-on-write behavior is determined by the `ingestOnWrite` field of a managed folder versus a cache configuration, see [Understanding how to enable ingest-on-write](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache#ingest-on-write-requirements) and [Ingest-on-write inheritance](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache#ingest-on-write-inheritance).

To delete the ingest-on-write policy for a managed folder, use the following command. The following command disables prefix-level ingest-on-write on individual caches for the managed folder resource that contains this configuration:
    
    curl -X PATCH -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -d '{
    "rapidCacheConfig": {
      "policies": {
        "us-east1-a": null
      }
    }
    }'
    "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/managedFolders/MANAGED_FOLDER_NAME"

Replace:

     * `BUCKET_NAME`: with the name of the bucket containing the managed folder.

     * `MANAGED_FOLDER_NAME`: with the name of the managed folder.

     * `RAPID_CACHE_ID`: with the identifier for the cache, which is the zone of the cache. For example, `us-east1-b`. This field must be set to `null`.

Alternatively, to delete the prefix-level ingest-on-write policy on a managed folder, set the `policies` map to `null` in your request:
    
    "rapidCacheConfig": {
    "policies": null
    }




## Delete a managed folder

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket that contains the managed folder you want to delete.

  3. In the **Bucket details** page, click the **More options** icon more_vert next to the managed folder you want to delete.

  4. Click **Delete folder**.

  5. To confirm that you want to delete the managed folder, type **`DELETE`** in **Delete** field.

  6. Click **Delete**.

The managed folder and its contents, including stored objects and other managed folders, are deleted from your Cloud Storage bucket.




### Command line

To delete a managed folder and the objects it contains, run the [`gcloud storage rm` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/rm):
    
    
    gcloud storage rm -r gs://BUCKET_NAME/MANAGED_FOLDER_NAME

Where:

  * `BUCKET_NAME` is the name of the bucket that contains the managed folder you want to delete. For example, `my-bucket`.

  * `MANAGED_FOLDER_NAME` is the name of the managed folder you want to delete. For example, `my-managed-folder/`.




### Client libraries

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

For more information, see the [Cloud Storage Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2). 

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

### Rust
    
    
    use google_cloud_storage::client::StorageControl;
    
    pub async fn sample(client: &StorageControl, bucket_id: &str) -> anyhow::Result<()> {
        const ID: &str = "example001";
        client
            .delete_managed_folder()
            .set_name(format!(
                "projects/_/buckets/{bucket_id}/managedFolders/{ID}"
            ))
            .send()
            .await?;
        println!("folder successfully deleted");
        Ok(())
    }

### REST APIs

### JSON API

To delete a managed folder, you must first [delete the objects](https://docs.cloud.google.com/storage/docs/deleting-objects) within the managed folder.

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`DELETE` ManagedFolder](https://docs.cloud.google.com/storage/docs/json_api/v1/managedFolder/delete) request:
         
         curl -X DELETE -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/managedFolders/MANAGED_FOLDER_NAME"

Where:

     * `BUCKET_NAME` is the name of the bucket that contains the managed folder you want to delete. For example, `my-bucket`.

     * `MANAGED_FOLDER_NAME` is the name of the managed folder you want to delete. For example, `my-managed-folder/`.

By default, managed folders must be empty before they can be deleted. To delete a non-empty managed folder, include `allowNonEmpty=true` as a query parameter in your request.




## Troubleshooting

For help creating and managing managed folders, refer to the [Troubleshooting page](https://docs.cloud.google.com/storage/docs/troubleshooting#folders).

## What's next

  * [Set an IAM policy on a managed folder](https://docs.cloud.google.com/storage/docs/access-control/using-iam-for-managed-folders).

  * [List objects in managed folders](https://docs.cloud.google.com/storage/docs/listing-objects#list-objects-json).

  * Learn about the [best practices for using managed folders](https://docs.cloud.google.com/storage/docs/access-control#best-practices).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
