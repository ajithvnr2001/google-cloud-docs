---
url: https://docs.cloud.google.com/storage/docs/using-autoclass/
title: Use Autoclass \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:23:19.046760+00:00
---

# Use Autoclass  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/using-autoclass/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Use Autoclass Stay organized with collections  Save and categorize content based on your preferences. 

[Overview](https://docs.cloud.google.com/storage/docs/autoclass)

This page shows you how to enable, disable, and check the status of the [Autoclass feature](https://docs.cloud.google.com/storage/docs/autoclass), which is set on a bucket in Cloud Storage.

## Required roles

To get the permissions that you need to set and manage Autoclass on a bucket, ask your administrator to grant you the Storage Admin (`roles/storage.admin`) IAM role on the bucket. This [predefined role](https://docs.cloud.google.com/iam/docs/understanding-roles) contains the permissions required to set and manage Autoclass on a bucket. To see the exact permissions that are required, expand the **Required permissions** section:

#### Required permissions

  * `storage.buckets.get`
  * `storage.buckets.list`
    * This permission is only required for using the Google Cloud console to perform the tasks on this page.
  * `storage.buckets.update`



You can also get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

For information about granting roles on buckets, see [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).

## Set Autoclass for a bucket

To set Autoclass for a bucket, complete the following instructions:

### Console

**Note:** Autoclass can also be enabled in the **Choose a default storage class for your data** when you [create the bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the desired bucket.

  3. In the **Bucket details** page, click the **Configuration** tab.

  4. Click the **Edit** icon (_edit_) for **Default storage class**.

  5. In the overlay window, select **Autoclass** to enable Autoclass. To disable Autoclass, select **Set a default class** , and then select a default storage class for the bucket.

  6. Click **Confirm**.

  7. To switch the terminal storage class for a bucket that has Autoclass enabled, click the **Edit** icon (_edit_) for **Included classes** , and click **Confirm** in the overlay window that appears.




### Command line

**Note:** Autoclass can also be enabled when you [create the bucket](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/create), by using the `--enable-autoclass` flag.

Use the [`gcloud storage buckets update`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/update) command with the appropriate flags:
    
    
    gcloud storage buckets update gs://BUCKET_NAME --default-storage-class=DEFAULT_CLASS AUTOCLASS_FLAG

Where:

  * `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.

  * `DEFAULT_CLASS` sets the storage class metadata for the bucket. When enabling Autoclass, `STANDARD` is the only valid value and is required if the bucket currently uses a different storage class.

  * `AUTOCLASS_FLAG` is one of the following:

    * `--enable-autoclass` to enable Autoclass.
    * `--no-enable-autoclass` to disable Autoclass.
    * `--autoclass-terminal-storage-class=CLASS` to set the terminal storage class for Autoclass. CLASS can be either `NEARLINE` or `ARCHIVE`. When using this flag on a bucket with Autoclass disabled, also include the `--enable-autoclass` flag in the command.



If successful, the response looks similar to the following example:
    
    
    Updating gs://my-bucket/...
      Completed 1  

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    [](gcs::Client client, std::string const& bucket_name, bool enabled) {
      auto metadata = client.PatchBucket(
          bucket_name, gcs::BucketMetadataPatchBuilder().SetAutoclass(
                           gcs::BucketAutoclass{enabled}));
      if (!metadata) throw google::cloud::Status(std::move(metadata).status());
    
      std::cout << "The autoclass configuration for bucket " << bucket_name
                << " was successfully updated.";
      if (!metadata->has_autoclass()) {
        std::cout << " The bucket no longer has an autoclass configuration.\n";
        return;
      }
      std::cout << " The new configuration is " << metadata->autoclass() << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using Google.Apis.Storage.v1.Data;
    using static Google.Apis.Storage.v1.Data.Bucket;
    using System;
    
    public class SetAutoclassSample
    {
        public Bucket SetAutoclass(string bucketName)
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var bucket = storage.GetBucket(bucketName);
            bucket.Autoclass = new AutoclassData { Enabled = true, TerminalStorageClass = "ARCHIVE" };
            storage.PatchBucket(bucket);
            Console.WriteLine($"Autoclass enabled is set to {bucket.Autoclass.Enabled} for {bucketName} at {bucket.Autoclass.ToggleTimeDateTimeOffset}.");
            Console.WriteLine($"Autoclass terminal storage class is {bucket.Autoclass.TerminalStorageClass}.");
            return bucket;
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
    
    // setAutoclass sets the Autoclass configuration for a bucket.
    func setAutoclass(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucketName string) error {
    	// bucketName := "bucket-name"
    
    	// To update the configuration for Autoclass.TerminalStorageClass,
    	// Autoclass.Enabled must also be set to true.
    	// To disable autoclass on the bucket, set to an empty &Autoclass{}.
    	enabled := true
    	terminalStorageClass := "ARCHIVE"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    
    	bucket := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucketName)
    	bucketAttrsToUpdate := storage.[BucketAttrsToUpdate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketAttrsToUpdate){
    		Autoclass: &storage.[Autoclass](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Autoclass){
    			Enabled:              enabled,
    			TerminalStorageClass: terminalStorageClass,
    		},
    	}
    	if _, err := bucket.Update(ctx, bucketAttrsToUpdate); err != nil {
    		return fmt.Errorf("Bucket(%q).Update: %w", bucketName, err)
    	}
    	fmt.Fprintf(w, "Autoclass enabled was set to %v on bucket %q \n", bucketAttrsToUpdate.[Autoclass](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Autoclass).Enabled, bucketName)
    	fmt.Fprintf(w, "Autoclass terminal storage class was last updated to %v at %v", bucketAttrsToUpdate.[Autoclass](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Autoclass).TerminalStorageClass, bucketAttrsToUpdate.[Autoclass](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Autoclass).TerminalStorageClassUpdateTime)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html).[Autoclass](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.Autoclass.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).[BucketTargetOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.BucketTargetOption.html);
    import com.google.cloud.storage.[StorageClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageClass.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class SetBucketAutoclass {
      public static void setBucketAutoclass(
          String projectId, String bucketName, [StorageClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageClass.html) storageClass) throws Exception {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The storage class that objects in an Autoclass bucket eventually transition to if not read
        // for a certain length of time
        // StorageClass storageClass = StorageClass.ARCHIVE;
    
        // Configure the Autoclass setting for a bucket.
    
        // Note:  terminal_storage_class field is optional and defaults to NEARLINE if not otherwise
        // specified. Valid terminal_storage_class values are NEARLINE and ARCHIVE.
        boolean enabled = true;
    
        try ([Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage =
            [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)()) {
          [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket = storage.get(bucketName);
    
          [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) toUpdate =
              bucket.[toBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html#com_google_cloud_storage_Bucket_toBuilder__)()
                  .setAutoclass(
                      [Autoclass](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.Autoclass.html).newBuilder()
                          .setEnabled(enabled)
                          .[setTerminalStorageClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.Autoclass.Builder.html#com_google_cloud_storage_BucketInfo_Autoclass_Builder_setTerminalStorageClass_com_google_cloud_storage_StorageClass_)(storageClass)
                          .build())
                  .build();
    
          [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) updated = storage.update(toUpdate, [BucketTargetOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.BucketTargetOption.html).metagenerationMatch());
    
          System.out.println(
              "Autoclass for bucket "
                  + bucketName
                  + " was "
                  + (updated.[getAutoclass](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_getAutoclass__)().getEnabled() ? "enabled." : "disabled."));
          System.out.println(
              "Autoclass terminal storage class is "
                  + updated.[getAutoclass](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_getAutoclass__)().[getTerminalStorageClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.Autoclass.html#com_google_cloud_storage_BucketInfo_Autoclass_getTerminalStorageClass__)().toString());
        }
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
    
    // The terminal storage class to be set on your GCS bucket. Valid values are NEARLINE and ARCHIVE.
    // const terminalStorageClass = 'NEARLINE';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function setAutoclass() {
      // Configure the Autoclass setting for a bucket.
      // terminalStorageClass field is optional and defaults to NEARLINE if not otherwise specified.
      // Valid terminalStorageClass values are NEARLINE and ARCHIVE.
      const [metadata] = await storage.bucket(bucketName).setMetadata({
        autoclass: {
          enabled: toggle,
          terminalStorageClass,
        },
      });
    
      console.log(
        `Autoclass terminal storage class is ${metadata.autoclass.terminalStorageClass}.`
      );
    }
    
    setAutoclass().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Updates an existing bucket with provided autoclass config.
     *
     * @param string $bucketName The name of your Cloud Storage bucket (e.g. 'my-bucket').
     * @param bool $autoclassStatus If true, enables Autoclass. Disables otherwise.
     * @param string $terminalStorageClass This field is optional and defaults to `NEARLINE`.
     *        Valid values are `NEARLINE` and `ARCHIVE`.
     */
    function set_bucket_autoclass(
        string $bucketName,
        bool $autoclassStatus,
        string $terminalStorageClass
    ): void {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
    
        $bucket->update([
            'autoclass' => [
                'enabled' => $autoclassStatus,
                'terminalStorageClass' => $terminalStorageClass
            ],
        ]);
    
        $info = $bucket->info();
        printf(
            'Updated bucket %s with autoclass set to %s.' . PHP_EOL,
            $info['name'],
            $autoclassStatus ? 'true' : 'false'
        );
        printf(
            'Autoclass terminal storage class is %s.' . PHP_EOL,
            $info['autoclass']['terminalStorageClass']
        );
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def set_autoclass(bucket_name):
        """Configure the Autoclass setting for a bucket.
    
        terminal_storage_class field is optional and defaults to NEARLINE if not otherwise specified.
        Valid terminal_storage_class values are NEARLINE and ARCHIVE.
        """
        # The ID of your GCS bucket
        # bucket_name = "my-bucket"
        # Enable Autoclass for a bucket. Set enabled to false to disable Autoclass.
        # Set Autoclass.TerminalStorageClass, valid values are NEARLINE and ARCHIVE.
        enabled = True
        terminal_storage_class = "ARCHIVE"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
    
        bucket.[autoclass_enabled](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_autoclass_enabled) = enabled
        bucket.[autoclass_terminal_storage_class](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_autoclass_terminal_storage_class) = terminal_storage_class
        bucket.patch()
        print(f"Autoclass enabled is set to {bucket.[autoclass_enabled](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_autoclass_enabled)} for {bucket.name} at {bucket.[autoclass_toggle_time](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_autoclass_toggle_time)}.")
        print(f"Autoclass terminal storage class is {bucket.[autoclass_terminal_storage_class](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_autoclass_terminal_storage_class)}.")
    
        return bucket
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    require "google/cloud/storage"
    
    ##
    # This is a snippet for showcasing how to set the autoclass
    # configuration of a bucket.
    #
    # @param bucket_name [String] The ID of your GCS bucket (e.g. "your-unique-bucket-name")
    # @param toggle [Boolean] if true, enables Autoclass; if false, disables Autoclass
    #
    def set_autoclass bucket_name:, toggle:, terminal_storage_class: nil
      # Initialize client
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
    
      # Fetch the GCS bucket
      bucket = storage.bucket bucket_name
    
      # Update the autoclass configuration
      bucket.[update_autoclass](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)({ enabled: toggle, terminal_storage_class: terminal_storage_class })
      terminal_class_update_time = bucket.[autoclass_terminal_storage_class_update_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)
    
      # Get autoclass config of the bucket
      puts "Bucket #{bucket.name} has autoclass config set to #{bucket.[autoclass_enabled](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)}."
      puts "Bucket #{bucket.name} has autoclass toggle time set to #{bucket.[autoclass_toggle_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)}."
      puts "Bucket #{bucket.name} has autoclass terminal storage class set to #{bucket.[autoclass_terminal_storage_class](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)}."
      puts "Bucket #{bucket.name} has autoclass terminal storage class update time set to #{terminal_class_update_time}."
    end
    

### Rust
    
    
    use google_cloud_storage::client::StorageControl;
    use google_cloud_storage::model::bucket::Autoclass;
    use google_cloud_wkt::FieldMask;
    
    pub async fn sample(client: &StorageControl, bucket_id: &str) -> anyhow::Result<()> {
        let bucket = client
            .get_bucket()
            .set_name(format!("projects/_/buckets/{bucket_id}"))
            .send()
            .await?;
        let metageneration = bucket.metageneration;
        let bucket = client
            .update_bucket()
            .set_bucket(bucket.set_autoclass(Autoclass::new().set_enabled(true)))
            .set_if_metageneration_match(metageneration)
            .set_update_mask(FieldMask::default().set_paths(["autoclass"]))
            .send()
            .await?;
        println!(
            "successfully updated autoclass for bucket {bucket_id}: {:?}",
            bucket.autoclass
        );
        Ok(())
    }

### REST APIs

### JSON API

**Note:** Autoclass can also be enabled when you [create the bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/insert), by using the `autoclass` property.

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the following information:
         
         {
           "storageClass": "DEFAULT_CLASS",
           "autoclass": {
             "enabled": BOOLEAN,
             "terminalStorageClass":TERMINAL_CLASS
           }
         }

Where:

     * `DEFAULT_CLASS` sets the storage class metadata for the bucket. When enabling Autoclass, `STANDARD` is the only valid value and is required if the bucket currently uses a different storage class.

     * `BOOLEAN` is `true` to enable Autoclass or `false` to disable Autoclass.

     * `TERMINAL_CLASS` is the [terminal storage class](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets#autoclass.terminalStorageClass) to use when Autoclass is enabled.

  3. Use [`cURL`](http://curl.haxx.se/) to call the JSON API with a [`PATCH` Bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/patch) request:
         
         curl -X PATCH --data-binary @JSON_FILE_NAME \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME?fields=autoclass"

Where:

     * `JSON_FILE_NAME` is the path for the JSON file that you created in Step 2.
     * `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.



### XML API

This feature cannot be managed through the XML API. Use the Google Cloud console or another tool instead.

## View a bucket's Autoclass status

To view the Autoclass status for an individual bucket:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click the name of the bucket whose status you want to check.

  3. Click the **Configuration** tab.

  4. The status for Autoclass is displayed in the **Default storage class** field.

If Autoclass is enabled, the field reads **Managed with Autoclass** , and the **Included classes** field displays the storage classes that objects can transition between.




### Command line

Use the [`gcloud storage buckets describe`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/describe) command with the `--format` flag:
    
    
    gcloud storage buckets describe gs://BUCKET_NAME --format="default(autoclass)"

Where `BUCKET_NAME` is the name of the bucket whose status you want to view. For example, `my-bucket`.

If successful, the response looks similar to the following example:
    
    
    autoclass:
      enabled: true
      terminalStorageClass: ARCHIVE
      terminalStorageClassUpdateTime: '2023-02-10T16:11:02.384000+00:00'
      toggleTime: '2022-11-09T16:01:40.775000+00:00'

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    [](gcs::Client client, std::string const& bucket_name) {
      auto metadata = client.GetBucketMetadata(bucket_name);
      if (!metadata) throw google::cloud::Status(std::move(metadata).status());
    
      if (!metadata->has_autoclass()) {
        std::cout << "The bucket " << metadata->name() << " does not have an"
                  << " autoclass configuration.\n";
        return;
      }
    
      std::cout << "Autoclass is "
                << (metadata->autoclass().enabled ? "enabled" : "disabled")
                << " for bucket " << metadata->name() << ". "
                << " The bucket's full autoclass configuration is "
                << metadata->autoclass() << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    using static Google.Apis.Storage.v1.Data.Bucket;
    
    public class GetAutoclassSample
    {
        public AutoclassData GetAutoclass(string bucketName)
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var bucket = storage.GetBucket(bucketName);
            Console.WriteLine($"Autoclass enabled is set to {bucket.Autoclass.Enabled} for {bucketName} at {bucket.Autoclass.ToggleTimeDateTimeOffset}.");
            Console.WriteLine($"Autoclass terminal storage class is set to {bucket.Autoclass.TerminalStorageClass} for {bucketName} at {bucket.Autoclass.TerminalStorageClassUpdateTimeDateTimeOffset}.");
            return bucket.Autoclass;
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
    
    // getAutoclass gets the Autoclass configuration for a bucket.
    // See https://cloud.google.com/storage/docs/using-autoclass for more information.
    func getAutoclass(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucketName string) error {
    	// bucketName := "bucket-name"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    
    	attrs, err := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucketName).Attrs(ctx)
    	if err != nil {
    		return fmt.Errorf("Bucket(%q).Attrs: %w", bucketName, err)
    	}
    	fmt.Fprintf(w, "Autoclass enabled was set to %v on bucket %q at %v", attrs.[Autoclass](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Autoclass).Enabled, bucketName, attrs.[Autoclass](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Autoclass).ToggleTime)
    	fmt.Fprintf(w, "Autoclass terminal storage class was last updated to %v at %v", attrs.[Autoclass](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Autoclass).TerminalStorageClass, attrs.[Autoclass](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Autoclass).TerminalStorageClassUpdateTime)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html).[Autoclass](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.Autoclass.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageClass.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import java.time.OffsetDateTime;
    
    public class GetBucketAutoclass {
      public static void getBucketAutoclass(String projectId, String bucketName) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        [Autoclass](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.Autoclass.html) autoclass = storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName).[getAutoclass](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_getAutoclass__)();
        String status = autoclass.getEnabled() ? "enabled" : "disabled";
        String toggleTime = autoclass.[getToggleTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.Autoclass.html#com_google_cloud_storage_BucketInfo_Autoclass_getToggleTime__)().toString();
        [StorageClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageClass.html) terminalStorageClass = autoclass.[getTerminalStorageClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.Autoclass.html#com_google_cloud_storage_BucketInfo_Autoclass_getTerminalStorageClass__)();
        OffsetDateTime terminalStorageClassUpdateTime = autoclass.[getTerminalStorageClassUpdateTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.Autoclass.html#com_google_cloud_storage_BucketInfo_Autoclass_getTerminalStorageClassUpdateTime__)();
    
        System.out.println(
            "Autoclass is currently "
                + status
                + " for bucket "
                + bucketName
                + " and was last changed at "
                + toggleTime
                + ". The terminal storage class is set to be "
                + terminalStorageClass.[name](https://docs.cloud.google.com/java/docs/reference/google-cloud-nio/latest/com.google.cloud.storage.contrib.nio.CloudStorageFileAttributeView.html#com_google_cloud_storage_contrib_nio_CloudStorageFileAttributeView_name__)()
                + " last updated at "
                + terminalStorageClassUpdateTime.toString());
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
    
    async function getAutoclass() {
      const [metadata] = await storage.bucket(bucketName).getMetadata();
      console.log(
        `Autoclass is ${
          metadata.autoclass.enabled ? 'enabled' : 'disabled'
        } for ${metadata.name} at ${metadata.autoclass.toggleTime}.
     Autoclass terminal storage class is last updated to ${
       metadata.autoclass.terminalStorageClass
     } at ${metadata.autoclass.terminalStorageClassUpdateTime}.`
      );
    }
    
    getAutoclass().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Print a bucket autoclass configuration.
     *
     * @param string $bucketName The name of your Cloud Storage bucket (e.g. 'my-bucket').
     */
    function get_bucket_autoclass(string $bucketName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
    
        $info = $bucket->info();
    
        if (isset($info['autoclass'])) {
            printf('Bucket %s has autoclass enabled: %s' . PHP_EOL,
                $bucketName,
                $info['autoclass']['enabled']
            );
            printf('Bucket %s has autoclass toggle time: %s' . PHP_EOL,
                $bucketName,
                $info['autoclass']['toggleTime']
            );
            printf(
                'Autoclass terminal storage class is set to %s for %s at %s.' . PHP_EOL,
                $info['autoclass']['terminalStorageClass'],
                $info['name'],
                $info['autoclass']['terminalStorageClassUpdateTime'],
            );
        }
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def get_autoclass(bucket_name):
        """Get the Autoclass setting for a bucket."""
        # The ID of your GCS bucket
        # bucket_name = "my-bucket"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[get_bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_get_bucket)(bucket_name)
        autoclass_enabled = bucket.[autoclass_enabled](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_autoclass_enabled)
        autoclass_toggle_time = bucket.[autoclass_toggle_time](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_autoclass_toggle_time)
        terminal_storage_class = bucket.[autoclass_terminal_storage_class](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_autoclass_terminal_storage_class)
        tsc_update_time = bucket.[autoclass_terminal_storage_class_update_time](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_autoclass_terminal_storage_class_update_time)
    
        print(f"Autoclass enabled is set to {[autoclass_enabled](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_autoclass_enabled)} for {bucket.name} at {[autoclass_toggle_time](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_autoclass_toggle_time)}.")
        print(f"Autoclass terminal storage class is set to {terminal_storage_class} for {bucket.name} at {tsc_update_time}.")
    
        return bucket
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    require "google/cloud/storage"
    
    ##
    # This is a snippet for showcasing how to access the autoclass
    # configuration of a bucket.
    #
    # @param bucket_name [String] The ID of your GCS bucket (e.g. "your-unique-bucket-name")
    #
    def get_autoclass bucket_name:
      # Initialize client
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
    
      # Fetch the GCS bucket
      bucket = storage.bucket bucket_name
      terminal_class_update_time = bucket.[autoclass_terminal_storage_class_update_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)
    
      # Get autoclass config of the bucket
      puts "Bucket #{bucket.name} has autoclass config set to #{bucket.[autoclass_enabled](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)}."
      puts "Bucket #{bucket.name} has autoclass toggle time set to #{bucket.[autoclass_toggle_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)}."
      puts "Bucket #{bucket.name} has autoclass terminal storage class set to #{bucket.[autoclass_terminal_storage_class](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)}."
      puts "Bucket #{bucket.name} has autoclass terminal storage class update time set to #{terminal_class_update_time}."
    end
    

### Rust
    
    
    use google_cloud_storage::client::StorageControl;
    
    pub async fn sample(client: &StorageControl, bucket_id: &str) -> anyhow::Result<()> {
        let bucket = client
            .get_bucket()
            .set_name(format!("projects/_/buckets/{bucket_id}"))
            .send()
            .await?;
        println!("Autoclass for bucket {bucket_id}: {:?}", bucket.autoclass);
        Ok(())
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the JSON API with a [`GET` Bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/get) request that includes the `autoclass` field:
         
         curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME?fields=autoclass"

Where `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.

If the bucket has Autoclass enabled, the response looks like the following example:
         
         {
           "autoclass": {
               "enabled": "BOOLEAN",
               "toggleTime": "DATETIME",
               "terminalStorageClass": "STORAGE_CLASS",
               "terminalStorageClassUpdateTime": "DATETIME"
            },
         }




### XML API

This feature cannot be managed through the XML API. Use the Google Cloud console or another tool instead.

## What's next

  * Learn more about [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass).
  * Learn about [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle), which automatically changes an object's storage class when it meets criteria you specify.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
