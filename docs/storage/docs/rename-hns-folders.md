---
url: https://docs.cloud.google.com/storage/docs/rename-hns-folders/
title: Rename and move folders \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:13.239583+00:00
---

# Rename and move folders  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/rename-hns-folders/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Rename and move folders Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to [rename or move](https://docs.cloud.google.com/storage/docs/folders-overview#rename) folders in a bucket with [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview) enabled.

The instructions on this page can only be used on folders in buckets with hierarchical namespace enabled. In buckets without hierarchical namespace, folders are [simulated from object name prefixes](https://docs.cloud.google.com/storage/docs/folder-types#simulated-folders). To rename or move simulated folders, see [Renaming or moving simulated folders](https://docs.cloud.google.com/storage/docs/objects#renaming-simulated-folders).

## Before you begin

Ensure that your bucket has hierarchical namespace enabled. For detailed instructions about enabling hierarchical namespace on a bucket, see [Create buckets with hierarchical namespace enabled](https://docs.cloud.google.com/storage/docs/create-hns-bucket).

## Required roles

In order to get the required permissions for renaming or moving folders in buckets, ask your administrator to grant you the Storage Object User (`roles/storage.objectUser`) IAM role on the bucket.

For instructions on granting roles on buckets, see [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).

To see the exact permissions that are required, expand the **Required permissions** section:

#### Required permissions

  * `storage.folders.rename`
    * This permission is needed for renaming the source folder.
  * `storage.folders.create`
    * This permission is needed for creating a folder at its destination path. Renaming a folder and moving a folder under a different parent folder creates a folder at its new location.



You can also get the preceding permissions with other [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or [predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions). For a more permissive role that lets you manage folders in addition to renaming folders, ask your administrator to grant you one of the following roles:

  * Storage Folder Admin (`roles/storage.folderAdmin`)
  * Storage Object Admin (`roles/storage.objectAdmin`)
  * Storage Admin (`roles/storage.admin`)



To see which roles are associated with which permissions, see [IAM roles for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam-roles).

## Rename or move a folder

During a folder rename operation, you can read and list the folders being renamed, but you can't run write operations on them.

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the bucket list, click the name of the bucket that contains the folder you want to move or rename.

  3. On the **Bucket details** page, in the **Folder browser** panel, find the folder that you want to move or rename.

  4. To rename the folder, do the following:

     1. Click the folder's more_vert **More actions** menu.

     2. Click **Rename**.

     3. Enter a new name for the folder.

     4. Click **Rename**.

  5. To move the folder into a different folder, do the following:

     1. Click the folder's more_vert **More actions** menu.

     2. Click **Move**.

     3. In the **Destination** field, click **Browse**.

     4. Select the destination folder for the folder you are moving.

If you want to create a new folder as the destination folder, click create_new_folder **Create new folder** , and then enter a name for the new folder.

     5. Click **Select** , and then click **Move**.




To learn how to get detailed error information about failed Cloud Storage operations in the Google Cloud console, see [Troubleshooting](https://docs.cloud.google.com/storage/docs/troubleshooting#trouble-console).

### Command line

To rename or move folders within a bucket with hierarchical namespace, run the [`gcloud storage mv`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/mv) command:
    
    
    gcloud storage mv gs://BUCKET_NAME/FOLDER1 gs://BUCKET_NAME/FOLDER2

Where:

  * `BUCKET_NAME` is the name of the bucket that contains the folder you want to rename or move. For example, `my-bucket`.
  * `FOLDER1` is the name of the original folder that you want to rename or move. For example, `my-src-folder`.
  * `FOLDER2` is the new name of the destination folder. For example, `my-dest-folder`. If the new name you choose is already being used by an existing folder, the original folder is moved inside the existing folder, becoming a child folder. For example, if you rename `my-dest-folder` to `my-dest-folder1` (and `my-dest-folder1` already exists), the result is `my-dest-folder1/my-dest-folder/`. If the new name you choose doesn't already exist, the original folder is renamed to match the new name.



The response looks like the following example:
    
    
    Copying gs://my-bucket/my-src-folder to gs://my-bucket/my-dest-folder...

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace storagecontrol = google::cloud::storagecontrol_v2;
    [](storagecontrol::StorageControlClient client,
       std::string const& bucket_name, std::string const& source_folder_id,
       std::string const& dest_folder_id) {
      auto name = std::string{"projects/_/buckets/"} + bucket_name + "/folders/" +
                  source_folder_id;
      // Start a rename operation and block until it completes. Real applications
      // may want to setup a callback, wait on a coroutine, or poll until it
      // completes.
      auto renamed = client.RenameFolder(name, dest_folder_id).get();
      if (!renamed) throw std::move(renamed).status();
    
      std::cout << "Renamed: " << source_folder_id << " to: " << dest_folder_id
                << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.Control.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.html);
    using System;
    
    public class StorageControlRenameFolderSample
    {
        public Folder StorageControlRenameFolder(string bucketName = "your-unique-bucket-name",
            string sourceFolderName = "your_folder_name", string targetFolderName = "target_folder_name")
        {
            [StorageControlClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html) storageControl = [StorageControlClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html#Google_Cloud_Storage_Control_V2_StorageControlClient_Create)();
    
            string folderResourceName =
                // Set project to "_" to signify globally scoped bucket
                [FolderName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.FolderName.html).[FormatProjectBucketFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.FolderName.html#Google_Cloud_Storage_Control_V2_FolderName_FormatProjectBucketFolder_System_String_System_String_System_String_)("_", bucketName, sourceFolderName);
    
            var operation = storageControl.[RenameFolder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html#Google_Cloud_Storage_Control_V2_StorageControlClient_RenameFolder_Google_Cloud_Storage_Control_V2_FolderName_System_String_Google_Api_Gax_Grpc_CallSettings_)(folderResourceName, targetFolderName);
            var folder = operation.PollUntilCompleted().Result;
    
            Console.WriteLine($"Renamed folder {sourceFolderName} to {targetFolderName}");
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
    
    // renameFolder changes the name of an existing folder.
    func renameFolder(w io.Writer, bucket, src, dst string) error {
    	// bucket := "bucket-name"
    	// src := "original-folder-name"
    	// dst := "new-folder-name"
    
    	ctx := context.Background()
    	client, err := control.NewStorageControlClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewStorageControlClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/control/apiv2.html#cloud_google_com_go_storage_control_apiv2_StorageControlClient_Close)()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*30)
    	defer cancel()
    
    	// Construct source folder path including the bucket name.
    	srcPath := fmt.Sprintf("projects/_/buckets/%v/folders/%v", bucket, src)
    
    	req := &controlpb.RenameFolderRequest{
    		Name:                srcPath,
    		DestinationFolderId: dst,
    	}
    	op, err := client.RenameFolder(ctx, req)
    	if err != nil {
    		return fmt.Errorf("RenameFolder(%q): %w", srcPath, err)
    	}
    
    	// Wait for long-running operation to complete.
    	f, err := op.Wait(ctx)
    	if err != nil {
    		return fmt.Errorf("waiting for RenameFolder: %w", err)
    	}
    
    	fmt.Fprintf(w, "folder %v moved to new path %v", srcPath, f.Name)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.storage.control.v2.[Folder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.Folder.html);
    import com.google.storage.control.v2.[FolderName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.FolderName.html);
    import com.google.storage.control.v2.[RenameFolderMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.RenameFolderMetadata.html);
    import com.google.storage.control.v2.[RenameFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.RenameFolderRequest.html);
    import com.google.storage.control.v2.[StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public final class RenameFolder {
    
      public static void renameFolder(
          String bucketName, String sourceFolderName, String destinationFolderName)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // The name of the bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The name of the folder within the bucket
        // String sourceFolderName = "your-unique-source-folder-name";
    
        // The new name of the folder within the bucket
        // String destinationFolderName = "your-unique-destination-folder-name";
    
        try ([StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html) storageControl = [StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html).create()) {
    
          // Set project to "_" to signify globally scoped bucket
          String sourceFolderResourceName = [FolderName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.FolderName.html).format("_", bucketName, sourceFolderName);
          [RenameFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.RenameFolderRequest.html) request =
              [RenameFolderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.RenameFolderRequest.html).newBuilder()
                  .setName(sourceFolderResourceName)
                  .setDestinationFolderId(destinationFolderName)
                  .build();
    
          OperationFuture<Folder, RenameFolderMetadata> renameOperation =
              storageControl.[renameFolderAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html#com_google_storage_control_v2_StorageControlClient_renameFolderAsync__org_jspecify_annotations_Nullable_com_google_storage_control_v2_FolderName_java_lang_String_)(request);
    
          [Folder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.Folder.html) destinationFolder = renameOperation.[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)(30, TimeUnit.SECONDS);
    
          System.out.printf(
              "Renamed folder from %s to %s%n", sourceFolderResourceName, destinationFolder.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.Folder.html#com_google_storage_control_v2_Folder_getName__)());
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
    
    // The source folder name
    // const sourceFolderName = 'currentFolderName';
    
    // The destination folder ID
    // const destinationFolderName = 'destinationFolderName';
    
    // Imports the Control library
    const {StorageControlClient} = require('[@google-cloud/storage-control](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/overview.html)').v2;
    
    // Instantiates a client
    const controlClient = new [StorageControlClient](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/storagecontrolclient.html)();
    
    async function callRenameFolder() {
      const folderPath = controlClient.[folderPath](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/storagecontrolclient.html)(
        '_',
        bucketName,
        sourceFolderName
      );
    
      // Create the request
      const request = {
        name: folderPath,
        destinationFolderId: destinationFolderName,
      };
    
      // Run request
      await controlClient.renameFolder(request);
      console.log(
        `Renamed folder ${sourceFolderName} to ${destinationFolderName}.`
      );
    }
    
    callRenameFolder();

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\Control\V2\Client\StorageControlClient;
    use Google\Cloud\Storage\Control\V2\RenameFolderRequest;
    
    /**
     * Rename a folder in an existing bucket.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $sourceFolder The source folder ID.
     *        (e.g. 'my-folder')
     * @param string $destinationFolder The destination folder ID.
     *        (e.g. 'my-folder')
     */
    function rename_folder(string $bucketName, string $sourceFolder, string $destinationFolder): void
    {
        $storageControlClient = new StorageControlClient();
    
        // Set project to "_" to signify global bucket
        $formattedName = $storageControlClient->folderName('_', $bucketName, $sourceFolder);
    
        $request = new RenameFolderRequest([
            'name' => $formattedName,
            'destination_folder_id' => $destinationFolder,
        ]);
    
        $storageControlClient->renameFolder($request);
    
        printf('Renamed folder %s to %s', $sourceFolder, $destinationFolder);
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage_control_v2](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest)
    
    
    def rename_folder(
        bucket_name: str, source_folder_name: str, destination_folder_name: str
    ) -> None:
        # The ID of your GCS bucket
        # bucket_name = "your-unique-bucket-name"
        #
        # The source folder ID
        # source_folder_name = "current-folder-name"
        #
        # The destination folder ID
        # destination_folder_name = "new-folder-name"
    
        storage_control_client = [storage_control_v2](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest).[StorageControlClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.services.storage_control.StorageControlClient.html)()
        # The storage bucket path uses the global access pattern, in which the "_"
        # denotes this bucket exists in the global namespace.
        source_folder_path = storage_control_client.[folder_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.services.storage_control.StorageControlClient.html#google_cloud_storage_control_v2_services_storage_control_StorageControlClient_folder_path)(
            project="_", bucket=bucket_name, folder=source_folder_name
        )
    
        request = [storage_control_v2](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest).[RenameFolderRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.types.RenameFolderRequest.html)(
            name=source_folder_path,
            destination_folder_id=destination_folder_name,
        )
    
        operation = storage_control_client.[rename_folder](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.services.storage_control.StorageControlClient.html#google_cloud_storage_control_v2_services_storage_control_StorageControlClient_rename_folder)(request=request)
        operation.result(60)
    
        print(f"Renamed folder {source_folder_name} to {destination_folder_name}")
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def rename_folder bucket_name:, source_folder_id:, destination_folder_id:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
      #
      # The source folder ID
      # source_folder_id = "current-folder-id"
      #
      # The destination folder ID, e.g. foo/bar/
      # destination_folder_id = "destination-folder-id"
    
      require "google/cloud/storage/control"
    
      storage_control = Google::Cloud::Storage::Control.storage_control
    
      # The storage folder path uses the global access pattern, in which the "_"
      # denotes this bucket exists in the global namespace.
      folder_path = storage_control.folder_path project: "_", bucket: bucket_name, folder: source_folder_id
    
      request = Google::Cloud::Storage::Control::V2::RenameFolderRequest.new name: folder_path,
                                                                             destination_folder_id: destination_folder_id
    
      storage_control.rename_folder request
    
      puts "Renamed folder #{source_folder_id} to #{destination_folder_id}"
    end

### Rust
    
    
    use google_cloud_lro::Poller;
    use google_cloud_storage::client::StorageControl;
    
    pub async fn sample(client: &StorageControl, bucket_id: &str) -> anyhow::Result<()> {
        const ID: &str = "example-folder-id";
        const NEW_ID: &str = "renamed-folder-id";
        let folder = client
            .rename_folder()
            .set_name(format!("projects/_/buckets/{bucket_id}/folders/{ID}"))
            .set_destination_folder_id(NEW_ID)
            .poller()
            .until_done()
            .await?;
        println!("folder successfully renamed {folder:?}");
        Ok(())
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [request to rename folders](https://docs.cloud.google.com/storage/docs/json_api/v1/folders/rename):
         
         curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/folders/SOURCE_PATH/renameTo/folders/DESTINATION_PATH"

Where:

     * `BUCKET_NAME` is the name of the bucket that contains the folder that you want to rename or move. For example, `my-bucket`.
     * `SOURCE_PATH` is the URL-encoded path of the source folder. For example, `my-src-folder/` URL-encoded as `my-src-folder%2F`.
     * `DESTINATION_PATH` is the URL-encoded path of the destination folder. For example, `my-dest-folder/` URL-encoded as `my-dest-folder%2F`.



## Next steps

  * [Create and manage folders](https://docs.cloud.google.com/storage/docs/create-folders).
  * [Use hierarchical namespace for Hadoop workloads](https://docs.cloud.google.com/storage/docs/hns-hadoop-workloads).



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Cloud Storage performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Cloud Storage free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
