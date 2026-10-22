---
url: https://docs.cloud.google.com/storage/docs/create-folders/
title: Create and manage folders \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:31:01.887916+00:00
---

# Create and manage folders  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/create-folders/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Create and manage folders Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create and manage [folders](https://docs.cloud.google.com/storage/docs/folders-overview) in buckets with [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview) enabled. Specifically, this page shows you how to create, list, and delete your folders, as well as how to get a folder's metadata.

For more information about these folder operations, see [Folder operations](https://docs.cloud.google.com/storage/docs/folders-overview#folder-operations).

## Before you begin

To follow these instructions, your bucket must have hierarchical namespace enabled. If you need to create a bucket with this feature, see [Create buckets with hierarchical namespace enabled](https://docs.cloud.google.com/storage/docs/create-hns-bucket).

## Create a folder

This section describes how to create a new folder in your bucket.

#### Roles required

In order to get the required permissions for creating folders, ask your administrator to grant you the Storage Object User (`roles/storage.objectUser`) IAM role on the bucket. This role contains the `storage.folders.create` permission, which is required to create a folder.

For instructions on granting roles on buckets, see [Use IAM with buckets.](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions)

You might also be able to get this permission with other [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or [predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions). For a more permissive role that lets you manage folders in addition to creating folders, ask your administrator to grant you any one of the following roles:

  * Storage Folder Admin (`roles/storage.folderAdmin`)
  * Storage Object Admin (`roles/storage.objectAdmin`)
  * Storage Admin (`roles/storage.admin`)



To see which roles are associated with which permissions, refer to [IAM roles for Cloud Storage.](https://docs.cloud.google.com/storage/docs/access-control/iam-roles)

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the bucket list, click the name of the bucket you want to create the folder in. 
  3. In the **Bucket details** page, click **Create folder** to create an empty folder. 
  4. In the **Name** field, enter a name for your folder. For naming considerations, see [Considerations](https://docs.cloud.google.com/storage/docs/folders-overview#considerations). 
  5. Click **Create**. 

Your newly created folder appears in the **Folder browser** pane.




### Command line

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. In your development environment, run the [`gcloud storage folders create`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/folders/create) command:
         
         gcloud storage folders create --recursive gs://BUCKET_NAME/FOLDER_NAME

Where:

     * `BUCKET_NAME` is the name of your bucket. For example, `my-bucket`.
     * `FOLDER_NAME` is the name of the folder you want to create. For example, `my-folder/`. For information about folder names, see the [folders overview documentation](https://docs.cloud.google.com/storage/docs/folders-overview#considerations).
     * `--recursive` is a flag that automatically creates all non-existent parent folders along with the folder. This setting is optional when parent folders already exist.

If the request is successful, the command returns the following message:
    
    Completed 1/1




### Client Libraries

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

### Rust
    
    
    use google_cloud_storage::{client::StorageControl, model::Folder};
    
    pub async fn sample(client: &StorageControl, bucket_id: &str) -> anyhow::Result<()> {
        const ID: &str = "example-folder-id";
        let folder = client
            .create_folder()
            .set_parent(format!("projects/_/buckets/{bucket_id}"))
            .set_folder_id(ID)
            .set_folder(Folder::new())
            .send()
            .await?;
        println!("folder successfully created {folder:?}");
        Ok(())
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the settings for the folder, which must include a `name` for the folder. See the [Folders: Insert](https://docs.cloud.google.com/storage/docs/json_api/v1/folders/insert) documentation for a complete list of settings. The following are required settings to include: 
         
         {
           "name": "FOLDER_NAME",
         }

Where FOLDER_NAME is the name of the folder you want to create. For example, `my-folder/`. For information about folder names, see the [folders overview documentation](https://docs.cloud.google.com/storage/docs/folders-overview#considerations).

  3. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api): 
         
         curl -X POST --data-binary @JSON_FILE_NAME \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/folders?recursive=true"

Where:

     * `JSON_FILE_NAME` is the name of the JSON file that contains the settings for the folder.
     * `BUCKET_NAME` is the name of the bucket where you want to create the folder. 
     * `recursive` is set to true to automatically create all the non-existent parent folders along with the folder. This setting is optional when parent folders already exist.



## Upload a folder

This section describes how to upload folders to a bucket. Uploading a folder uses an underlying create folder operation with batch object upload operations.

#### Roles required

In order to get the required permissions for uploading folders, ask your administrator to grant you the Storage Object User (`roles/storage.objectUser`) IAM role on the bucket. This role contains the `storage.folders.create` permission, which is required to upload a folder.

For instructions on granting roles on buckets, see [Use IAM with buckets.](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions)

You might also be able to get this permission with other [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or [predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions). For a more permissive role that lets you manage folders in addition to uploading folders, ask your administrator to grant you any one of the following roles:

  * Storage Folder Admin (`roles/storage.folderAdmin`)
  * Storage Object Admin (`roles/storage.objectAdmin`)
  * Storage Admin (`roles/storage.admin`)



To see which roles are associated with which permissions, refer to [IAM roles for Cloud Storage.](https://docs.cloud.google.com/storage/docs/access-control/iam-roles)

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket you want to upload the folder to.

  3. In the **Bucket details** tab, perform one of the following actions:

     * Drag folders from your desktop or file manager to the main pane in the Google Cloud console.

     * Click **Upload > Upload folder**, select the folder that you want to upload in the dialog that appears, then click **Open**.




To learn how to get detailed error information about failed Cloud Storage operations in the Google Cloud console, see [Troubleshooting](https://docs.cloud.google.com/storage/docs/troubleshooting#trouble-console).

###  Command line 

Use the [`gcloud storage cp`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cp) command with the `--recursive` flag:
    
    
    gcloud storage cp --recursive FOLDER_LOCATION gs://DESTINATION_BUCKET_NAME

Where:

  * `FOLDER_LOCATION` is the local path to your folder you want to upload. For example, `../uploads/my-folder/`.

  * `DESTINATION_BUCKET_NAME` is the name of the bucket to which you are uploading your folder. For example, `my-bucket`.




If successful, the response looks like the following example:
    
    
    Copying file://DIR/OBJ1 at 10.06.32 PM.png to gs://BUCKET_NAME/DIR/OBJ1 at 10.06.32 PM.png
    Copying file://DIR/OBJ1 at 10.06.32 PM.png to gs://BUCKET_NAME/DIR/OBJ1 at 10.06.32 PM.png
    Completed files 2/2 | 1.7MiB/1.7MiB

## List folders

This section describes how to list folders.

#### Roles required

In order to get the required permissions for listing folders, ask your administrator to grant you the Storage Object Viewer (`roles/storage.objectViewer`) IAM role on the bucket. This role contains the `storage.folders.list` permission, which is required to list folders.

For instructions on granting roles on buckets, see [Use IAM with buckets.](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions)

You might also be able to get this permission with other [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or [predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions). For a more permissive role that lets you manage folders in addition to listing folders, ask your administrator to grant you any one of the following roles:

  * Storage Folder Admin (`roles/storage.folderAdmin`)
  * Storage Object Admin (`roles/storage.objectAdmin`)
  * Storage Object User (`roles/storage.objectUser`)
  * Storage Admin (`roles/storage.admin`)



To see which roles are associated with which permissions, refer to [IAM roles for Cloud Storage.](https://docs.cloud.google.com/storage/docs/access-control/iam-roles)

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the bucket list, click the name of the bucket whose folders you want to list.

  3. From the **Folder browser** pane, use the expander arrow arrow_right to expand the list of folders within your bucket.

A list displays the folders, simulated folders, and managed folders in your bucket.




### Command line

To list all folders in a bucket, run the [`gcloud storage folders list`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/folders/list) command:
    
    
    gcloud storage folders list gs://BUCKET_NAME/

Where:

  * `BUCKET_NAME` is the name of the bucket that contains the folders you want to list. For example, `my-bucket`.



A successful response looks like the following example:
    
    
    bucket: hns-bucket
    id: hns-bucket/A/
    kind: storage#folder
    name: A/
    selfLink: https://www.googleapis.com/storage/v1/b/hns-bucket/f/A
    timeCreated: '2023-05-05T16:32:08.878000+00:00'
    updated: '2023-05-05T16:32:08.878000+00:00'
    ---
    bucket: hns-bucket
    id: hns-bucket/B/
    kind: storage#folder
    name: B/
    selfLink: https://www.googleapis.com/storage/v1/b/hns-bucket/f/B
    timeCreated: '2023-05-05T16:32:08.878000+00:00'
    updated: '2023-05-05T16:32:08.878000+00:00'
    ---
    bucket: hns-bucket
    id: hns-bucket/B/D/
    kind: storage#folder
    name: D/
    selfLink: https://www.googleapis.com/storage/v1/b/hns-bucket/f/B/D
    timeCreated: '2023-05-05T16:32:08.878000+00:00'
    updated: '2023-05-05T16:32:08.878000+00:00'
    ---
    bucket: hns-bucket
    id: hns-bucket/C/
    kind: storage#folder
    name: C/
    selfLink: https://www.googleapis.com/storage/v1/b/hns-bucket/f/C
    timeCreated: '2023-05-05T16:32:08.878000+00:00'
    updated: '2023-05-05T16:32:08.878000+00:00'
    ---
    bucket: hns-bucket
    id: hns-bucket/C/E/
    kind: storage#folder
    name: E/
    selfLink: https://www.googleapis.com/storage/v1/b/hns-bucket/f/C/E
    timeCreated: '2023-05-05T16:32:08.878000+00:00'
    updated: '2023-05-05T16:32:08.878000+00:00'
    ...

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace storagecontrol = google::cloud::storagecontrol_v2;
    [](storagecontrol::StorageControlClient client,
       std::string const& bucket_name) {
      auto const parent = std::string{"projects/_/buckets/"} + bucket_name;
      for (auto folder : client.ListFolders(parent)) {
        if (!folder) throw std::move(folder).status();
        std::cout << folder->name() << "\n";
      }
    
      std::cout << bucket_name << std::endl;
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.Control.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.html);
    using System;
    using System.Collections.Generic;
    
    public class StorageControlListFoldersSample
    {
        public IEnumerable<Folder> StorageControlListFolders(string bucketName = "your-unique-bucket-name")
        {
            [StorageControlClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html) storageControl = [StorageControlClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html#Google_Cloud_Storage_Control_V2_StorageControlClient_Create)();
    
            // Use "_" for project ID to signify globally scoped bucket
            string bucketResourceName = [BucketName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.BucketName.html).[FormatProjectBucket](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.BucketName.html#Google_Cloud_Storage_Control_V2_BucketName_FormatProjectBucket_System_String_System_String_)("_", bucketName);
            var folders = storageControl.[ListFolders](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html#Google_Cloud_Storage_Control_V2_StorageControlClient_ListFolders_Google_Cloud_Storage_Control_V2_BucketName_System_String_System_Nullable_System_Int32__Google_Api_Gax_Grpc_CallSettings_)(bucketResourceName);
    
            foreach (var folder in folders)
            {
                Console.Write(folder.Name);
            }
            return folders;
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
    
    // listFolders lists all folders present in the bucket.
    func listFolders(w io.Writer, bucket string) error {
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
    
    	// Construct bucket path for a bucket containing folders.
    	bucketPath := fmt.Sprintf("projects/_/buckets/%v", bucket)
    
    	// List all folders present.
    	req := &controlpb.ListFoldersRequest{
    		Parent: bucketPath,
    	}
    	it := client.ListFolders(ctx, req)
    	for {
    		f, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("ListFolders(%q): %w", bucketPath, err)
    		}
    		fmt.Fprintf(w, "got folder %v\n", f.Name)
    	}
    
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.storage.control.v2.[BucketName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.BucketName.html);
    import com.google.storage.control.v2.[Folder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.Folder.html);
    import com.google.storage.control.v2.[ListFoldersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.ListFoldersRequest.html);
    import com.google.storage.control.v2.[StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html);
    import java.io.IOException;
    
    public final class ListFolders {
    
      public static void listFolders(String bucketName) throws IOException {
        // The name of the bucket
        // String bucketName = "your-unique-bucket-name";
    
        try ([StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html) storageControl = [StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html).create()) {
    
          [ListFoldersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.ListFoldersRequest.html) request =
              [ListFoldersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.ListFoldersRequest.html).newBuilder()
                  // Set project to "_" to signify globally scoped bucket
                  .setParent([BucketName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.BucketName.html).format("_", bucketName))
                  .build();
    
          Iterable<Folder> folders = storageControl.listFolders(request).iterateAll();
          for ([Folder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.Folder.html) folder : folders) {
            System.out.printf("Found folder: %s%n", folder.getName());
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
    
    async function callListFolders() {
      const bucketPath = controlClient.[bucketPath](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/storagecontrolclient.html)('_', bucketName);
    
      // Create the request
      const request = {
        parent: bucketPath,
      };
    
      // Run request
      const [folders] = await controlClient.listFolders(request);
      for (const curFolder of folders) {
        console.log(curFolder.name);
      }
    }
    
    callListFolders();

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\Control\V2\Client\StorageControlClient;
    use Google\Cloud\Storage\Control\V2\ListFoldersRequest;
    
    /**
     * List folders in an existing bucket.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     */
    function list_folders(string $bucketName): void
    {
        $storageControlClient = new StorageControlClient();
    
        // Set project to "_" to signify global bucket
        $formattedName = $storageControlClient->bucketName('_', $bucketName);
    
        $request = new ListFoldersRequest([
            'parent' => $formattedName,
        ]);
    
        $folders = $storageControlClient->listFolders($request);
    
        foreach ($folders as $folder) {
            printf('Folder name: %s' . PHP_EOL, $folder->getName());
        }
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage_control_v2](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest)
    
    
    def list_folders(bucket_name: str) -> None:
        # The ID of your GCS bucket
        # bucket_name = "your-unique-bucket-name"
    
        storage_control_client = [storage_control_v2](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest).[StorageControlClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.services.storage_control.StorageControlClient.html)()
        # The storage bucket path uses the global access pattern, in which the "_"
        # denotes this bucket exists in the global namespace.
        project_path = storage_control_client.[common_project_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.services.storage_control.StorageControlClient.html#google_cloud_storage_control_v2_services_storage_control_StorageControlClient_common_project_path)("_")
        bucket_path = f"{project_path}/buckets/{bucket_name}"
    
        request = [storage_control_v2](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest).[ListFoldersRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.types.ListFoldersRequest.html)(
            parent=bucket_path,
        )
    
        page_result = storage_control_client.[list_folders](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.services.storage_control.StorageControlClient.html#google_cloud_storage_control_v2_services_storage_control_StorageControlClient_list_folders)(request=request)
        for folder in page_result:
            print(folder)
    
        print(f"Listed folders in bucket {bucket_name}")
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def list_folders bucket_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      require "google/cloud/storage/control"
    
      storage_control = Google::Cloud::Storage::Control.storage_control
    
      # The storage bucket path uses the global access pattern, in which the "_"
      # denotes this bucket exists in the global namespace.
      bucket_path = storage_control.bucket_path project: "_", bucket: bucket_name
    
      request = Google::Cloud::Storage::Control::V2::ListFoldersRequest.new parent: bucket_path
    
      response = storage_control.list_folders request
    
      puts response.response.folders
    end

### Rust
    
    
    use google_cloud_gax::paginator::ItemPaginator;
    use google_cloud_storage::client::StorageControl;
    
    pub async fn sample(client: &StorageControl, bucket_id: &str) -> anyhow::Result<()> {
        let mut items = client
            .list_folders()
            .set_parent(format!("projects/_/buckets/{bucket_id}"))
            .by_item();
        println!("Listing folders in bucket {bucket_id}");
        while let Some(folder) = items.next().await.transpose()? {
            println!("{folder:?}");
        }
        println!("DONE");
        Ok(())
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](https://docs.cloud.google.com/storage/docs/json_api) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api/v1/folders/getfoldermetadata) with a [request to list folders](https://docs.cloud.google.com/storage/docs/json_api/v1/folders/list):
         
         curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/folders"

Where `BUCKET_NAME` is the name of the bucket that contains the folders you want to list. For example, `my-bucket`.




## Delete a folder

This section describes how to delete folders.

#### Roles required

In order to get the required permissions for deleting folders, ask your administrator to grant you the Storage Object User (`roles/storage.objectUser`) IAM role on the bucket. This role contains the following permissions, which are required to delete a folder:

  * `storage.folders.delete`
  * `storage.managedFolders.delete` (Only required if a managed folder exists with the same path as the folder)

For instructions on granting roles on buckets, see [Use IAM with buckets.](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions)

You might also be able to get these permissions with other [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or [predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions). For a more permissive role that lets you manage folders in addition to deleting folders, ask your administrator to grant you any one of the following roles:

    * Storage Folder Admin (`roles/storage.folderAdmin`)
    * Storage Object Admin (`roles/storage.objectAdmin`)
    * Storage Admin (`roles/storage.admin`)

To see which roles are associated with which permissions, refer to [IAM roles for Cloud Storage.](https://docs.cloud.google.com/storage/docs/access-control/iam-roles)




**Note:** If you delete a folder that has a [managed folder](https://docs.cloud.google.com/storage/docs/managed-folders) at the same path, the managed folder is also deleted. If the delete request fails to delete the managed folder, you can see the managed folder name, even if you don't have explicit `storage.managedFolders.get` or `storage.managedFolders.list` permissions. The managed folder name appears in the error message and the Cloud Audit Logs of the failed request. When you grant the `storage.folders.delete` permission, consider that on failure of the folder deletion request the existence of the managed folder is revealed.

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the bucket list, click the name of the bucket whose folders you want to delete.

  3. From the **Folder browser** pane, use the expander arrow arrow_right to expand the list of folders within your bucket.

  4. Find the folder you want to delete.

  5. Click the folder's more_vert **More actions** menu.

  6. Click **Delete folder**.

  7. To confirm that you want to delete the folder, type `DELETE` in **Delete** field.

  8. Click **Delete**.

The folder and its contents, including stored objects and other managed folders, are deleted from your Cloud Storage bucket.




### Command line

To delete an empty folder, run the [`gcloud storage folders delete`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/folders/delete) command:
    
    
    gcloud storage folders delete gs://BUCKET_NAME/FOLDER_NAME

Where:

  * `BUCKET_NAME` is the name of the bucket. For example, `my-bucket`.

  * `FOLDER_NAME` is the name of the folder you want to delete. For example, `my-folder/`.




### Client libraries

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

### Rust
    
    
    use google_cloud_storage::client::StorageControl;
    
    pub async fn sample(client: &StorageControl, bucket_id: &str) -> anyhow::Result<()> {
        const ID: &str = "deleted-folder-id";
        client
            .delete_folder()
            .set_name(format!("projects/_/buckets/{bucket_id}/folders/{ID}"))
            .send()
            .await?;
        println!("folder successfully deleted");
        Ok(())
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`DELETE` Folder](https://docs.cloud.google.com/storage/docs/json_api/v1/folders/delete) request:
         
         curl -X DELETE -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/folders/FOLDER_NAME"

Where:

     * `BUCKET_NAME` is the name of the bucket that contains the folder you want to delete. For example, `my-bucket`.

     * `FOLDER_NAME` is the URL-encoded name of the folder you want to delete. For example, `my-folder/`, URL-encoded as `my-folder%2F`.




## Get the metadata of a folder

This section describes how to get the [metadata](https://docs.cloud.google.com/storage/docs/json_api/v1/folders/getfoldermetadata) of a folder.

#### Roles required

In order to get the required permissions for getting the metadata of a folder, ask your administrator to grant you the Storage Object Viewer (`roles/storage.objectViewer`) IAM role on the bucket. This role contains the `storage.folders.get` permission, which is required to get the metadata of a folder.

For instructions on granting roles on buckets, see [Use IAM with buckets.](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions)

You might also be able to get this permission with other [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or [predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions). For a more permissive role that lets you manage folders in addition to getting the metadata of a folder, ask your administrator to grant you any one of the following roles:

  * Storage Folder Admin (`roles/storage.folderAdmin`)
  * Storage Object Admin (`roles/storage.objectAdmin`)
  * Storage Object User (`roles/storage.objectUser`)
  * Storage Admin (`roles/storage.admin`)



To see which roles are associated with which permissions, refer to [IAM roles for Cloud Storage.](https://docs.cloud.google.com/storage/docs/access-control/iam-roles)

### Command line

To get the metadata of a folder, run the [`gcloud storage folders describe`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/folders/describe) command:
    
    
    gcloud storage folders describe gs://BUCKET_NAME/FOLDER_NAME

Where:

  * `BUCKET_NAME` is the name of the bucket that contains the folder whose metadata you want to retrieve. For example, `my-bucket`.
  * `FOLDER_NAME` is the name of the folder whose metadata you want to retrieve. For example, `my-folder/`.



### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace storagecontrol = google::cloud::storagecontrol_v2;
    [](storagecontrol::StorageControlClient client,
       std::string const& bucket_name, std::string const& folder_id) {
      auto const name = std::string{"projects/_/buckets/"} + bucket_name +
                        "/folders/" + folder_id;
      auto folder = client.GetFolder(name);
      if (!folder) throw std::move(folder).status();
    
      std::cout << "Got folder: " << folder->name() << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.Control.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.html);
    using System;
    
    public class StorageControlGetFolderSample
    {
        public Folder StorageControlGetFolder(string bucketName = "your-unique-bucket-name",
            string folderName = "your_folder_name")
        {
            [StorageControlClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html) storageControl = [StorageControlClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html#Google_Cloud_Storage_Control_V2_StorageControlClient_Create)();
    
            string folderResourceName =
                // Set project to "_" to signify globally scoped bucket
                [FolderName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.FolderName.html).[FormatProjectBucketFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.FolderName.html#Google_Cloud_Storage_Control_V2_FolderName_FormatProjectBucketFolder_System_String_System_String_System_String_)("_", bucketName, folderName);
    
            [Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder.html) folder = storageControl.[GetFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html#Google_Cloud_Storage_Control_V2_StorageControlClient_GetFolder_Google_Cloud_Storage_Control_V2_FolderName_Google_Api_Gax_Grpc_CallSettings_)(folderResourceName);
    
            Console.WriteLine($"Got folder: {folder.[Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.Folder.html#Google_Cloud_Storage_Control_V2_Folder_Name)}");
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
    
    // getFolder gets metadata for the folder with the given name.
    func getFolder(w io.Writer, bucket, folder string) error {
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
    
    	req := &controlpb.GetFolderRequest{
    		Name: folderPath,
    	}
    	f, err := client.GetFolder(ctx, req)
    	if err != nil {
    		return fmt.Errorf("GetFolder(%q): %w", folderPath, err)
    	}
    
    	fmt.Fprintf(w, "got folder metadata: %+v", f)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.storage.control.v2.[Folder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.Folder.html);
    import com.google.storage.control.v2.[FolderName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.FolderName.html);
    import com.google.storage.control.v2.[GetFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.GetFolderRequest.html);
    import com.google.storage.control.v2.[StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html);
    import java.io.IOException;
    
    public final class GetFolder {
    
      public static void getFolder(String bucketName, String folderName) throws IOException {
        // The name of the bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The name of the folder within the bucket
        // String folderName = "your-unique-folder-name";
    
        try ([StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html) storageControl = [StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html).create()) {
    
          [GetFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.GetFolderRequest.html) request =
              [GetFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.GetFolderRequest.html).newBuilder()
                  // Set project to "_" to signify globally scoped bucket
                  .setName([FolderName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.FolderName.html).format("_", bucketName, folderName))
                  .build();
    
          [Folder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.Folder.html) newFolder = storageControl.getFolder(request);
    
          System.out.printf("Got folder: %s%n", newFolder.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.Folder.html#com_google_storage_control_v2_Folder_getName__)());
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
    
    // The name of the folder to get
    // const folderName = 'folderName';
    
    // Imports the Control library
    const {StorageControlClient} = require('[@google-cloud/storage-control](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/overview.html)').v2;
    
    // Instantiates a client
    const controlClient = new [StorageControlClient](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/storagecontrolclient.html)();
    
    async function callGetFolder() {
      const folderPath = controlClient.[folderPath](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/storagecontrolclient.html)('_', bucketName, folderName);
    
      // Create the request
      const request = {
        name: folderPath,
      };
    
      // Run request
      const [response] = await controlClient.getFolder(request);
      console.log(`Got folder: ${response.name}.`);
    }
    
    callGetFolder();

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\Control\V2\Client\StorageControlClient;
    use Google\Cloud\Storage\Control\V2\GetFolderRequest;
    
    /**
     * Get a folder in an existing bucket.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $folderName The name of your folder inside the bucket.
     *        (e.g. 'my-folder')
     */
    function get_folder(string $bucketName, string $folderName): void
    {
        $storageControlClient = new StorageControlClient();
    
        // Set project to "_" to signify global bucket
        $formattedName = $storageControlClient->folderName('_', $bucketName, $folderName);
    
        $request = new GetFolderRequest([
            'name' => $formattedName,
        ]);
    
        $folder = $storageControlClient->getFolder($request);
    
        printf($folder->getName());
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage_control_v2](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest)
    
    
    def get_folder(bucket_name: str, folder_name: str) -> None:
        # The ID of your GCS bucket
        # bucket_name = "your-unique-bucket-name"
    
        # The name of the folder
        # folder_name = "folder-name"
    
        storage_control_client = [storage_control_v2](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest).[StorageControlClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.services.storage_control.StorageControlClient.html)()
        # The storage bucket path uses the global access pattern, in which the "_"
        # denotes this bucket exists in the global namespace.
        folder_path = storage_control_client.[folder_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.services.storage_control.StorageControlClient.html#google_cloud_storage_control_v2_services_storage_control_StorageControlClient_folder_path)(
            project="_", bucket=bucket_name, folder=folder_name
        )
    
        request = [storage_control_v2](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest).[GetFolderRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.types.GetFolderRequest.html)(
            name=folder_path,
        )
        response = storage_control_client.[get_folder](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.services.storage_control.StorageControlClient.html#google_cloud_storage_control_v2_services_storage_control_StorageControlClient_get_folder)(request=request)
    
        print(f"Got folder: {response.name}")
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def get_folder bucket_name:, folder_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      # The name of the folder to be created
      # folder_name = "folder-name"
    
      require "google/cloud/storage/control"
    
      storage_control = Google::Cloud::Storage::Control.storage_control
    
      # The storage folder path uses the global access pattern, in which the "_"
      # denotes this bucket exists in the global namespace.
      folder_path = storage_control.folder_path project: "_", bucket: bucket_name, folder: folder_name
    
      request = Google::Cloud::Storage::Control::V2::GetFolderRequest.new name: folder_path
    
      response = storage_control.get_folder request
    
      puts "Got folder #{response.name}"
    end

### Rust
    
    
    use google_cloud_storage::client::StorageControl;
    
    pub async fn sample(client: &StorageControl, bucket_id: &str) -> anyhow::Result<()> {
        const ID: &str = "example-folder-id";
        let folder = client
            .get_folder()
            .set_name(format!("projects/_/buckets/{bucket_id}/folders/{ID}"))
            .send()
            .await?;
        println!("folder metadata successfully retrieved {folder:?}");
        Ok(())
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`GET` Folder](https://docs.cloud.google.com/storage/docs/json_api/v1/folders/getfoldermetadata) request:
         
         curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/folders/FOLDER_NAME"

Where:

     * `BUCKET_NAME` is the name of the bucket that contains the folder whose metadata you want to retrieve. For example, `my-bucket`.

     * `FOLDER_NAME` is the URL-encoded name of the folder whose metadata you want to retrieve. For example, `my-folder/`, URL-encoded as `my-folder%2F`.




## Manage access on a folder

This section describes how to manage access on your folder by setting [ Identity and Access Management (IAM) policies](https://docs.cloud.google.com/iam/docs/policies), so you can get fine-grained access control over specific groups of objects within a bucket.

To manage access on your folder, follow these steps:

  1. Enable management on your folder by creating a [managed folder](https://docs.cloud.google.com/storage/docs/managed-folders) with the same name as your existing folder. For detailed instructions, see [Create a managed folder](https://docs.cloud.google.com/storage/docs/creating-managing-managed-folders#create).

  2. [Set and manage Identity and Access Management (IAM) policies on the managed folder you created](https://docs.cloud.google.com/storage/docs/access-control/using-iam-for-managed-folders).




## What's next

  * [Rename folders](https://docs.cloud.google.com/storage/docs/rename-hns-folders).
  * [Create buckets with hierarchical namespace enabled](https://docs.cloud.google.com/storage/docs/create-hns-bucket).
  * [Use hierarchical namespace for Hadoop workloads](https://docs.cloud.google.com/storage/docs/hns-hadoop-workloads).
  * [Optimize folder management](https://docs.cloud.google.com/storage/docs/hns-buckets-best-practices#folder-management).



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Cloud Storage performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Cloud Storage free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
