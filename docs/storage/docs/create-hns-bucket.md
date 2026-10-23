---
url: https://docs.cloud.google.com/storage/docs/create-hns-bucket/
title: Create buckets with hierarchical namespace enabled \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:17.113441+00:00
---

# Create buckets with hierarchical namespace enabled  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/create-hns-bucket/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Create buckets with hierarchical namespace enabled Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create buckets with [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview) enabled.

## Required roles

To get the permission that you need to create a bucket with hierarchical namespace enabled, ask your administrator to grant you the [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `storage.buckets.create` permission, which is required to create a bucket with hierarchical namespace enabled. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a bucket with hierarchical namespace enabled

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click add_box **Create**.
  3. On the **Create a bucket** page, enter your bucket information. After each of the following steps, click **Continue** to proceed to the next step:

     1. In the **Get started** section, do the following:

        * Enter a globally unique name that meets the [bucket name requirements](https://docs.cloud.google.com/storage/docs/buckets#naming).

     2. In the **Choose where to store your data** section, do the following:

        1. Select a [Location type](https://docs.cloud.google.com/storage/docs/locations).

        2. Use the location type's drop-down menu to select a [**Location**](https://docs.cloud.google.com/storage/docs/locations#available-locations) where object data within your bucket will be permanently stored.

           * If you select the [dual-region](https://docs.cloud.google.com/storage/docs/locations#location-dr) location type, you can also choose to enable [turbo replication](https://docs.cloud.google.com/storage/docs/availability-durability#turbo-replication) by using the relevant checkbox.

     3. In the **Choose how to store your data** section, do the following:

        1. Select a [default storage class](https://docs.cloud.google.com/storage/docs/storage-classes) for the bucket or [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass) for automatic storage class management of your bucket's data.

        2. In the **Optimize storage for data-intensive workloads** section, do the following:

           * To enable [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview), select **Enable Hierarchical namespace on this bucket**.

**Note:** Hierarchical namespace can only be enabled when you create the bucket. You can't change this setting after you create the bucket.

     4. In the **Choose how to control access to objects** section, do the following:

        1. Select whether your bucket enforces [public access prevention](https://docs.cloud.google.com/storage/docs/public-access-prevention).

**Note:** If public access prevention is already enforced by your project's [organization policy](https://docs.cloud.google.com/storage/docs/org-policy-constraints#public-access-prevention), the **Prevent public access** checkbox is locked. 
        2. Select **Uniform** to enable uniform bucket-level access on the bucket.

        3. Optionally, configure [IP filtering for the bucket](https://docs.cloud.google.com/storage/docs/ip-filtering-overview).

  4. In the **Choose how to protect object data** section, do the following:

     * Select any of the options under **Data protection** that you want to set for your bucket.

     * To change the amount of time that [soft delete](https://docs.cloud.google.com/storage/docs/soft-delete) retains objects after deletion, select the **Soft delete policy** checkbox, and then select the **Set custom retention duration** option. Then, specify how long you want to retain deleted objects.

To disable soft delete, for example if the bucket will primarily contain short-lived, temporary data, clear the **Soft delete policy** checkbox. 

     * To choose how to [encrypt](https://docs.cloud.google.com/storage/docs/encryption) your object data, click the expand_more expander arrow labeled **Data encryption** , and do the following:

       * In the **Default encryption key type** section, select the default encryption key for the bucket. If you select **Cloud KMS key** , then provide a [Cloud Key Management Service key](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys).
       * In the **Encryption enforcement rules** section, for **Key types** , select [which encryption types to allow or restrict](https://docs.cloud.google.com/storage/docs/encryption/enforce-encryption-types) for new objects in the bucket.


* Click **Create**.

To learn how to get detailed error information about failed Cloud Storage operations in the Google Cloud console, see [Troubleshooting](https://docs.cloud.google.com/storage/docs/troubleshooting#trouble-console).

### Command line

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. In your development environment, run the [`gcloud storage buckets create`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/create) command:
         
         gcloud storage buckets create gs://BUCKET_NAME --location=BUCKET_LOCATION --uniform-bucket-level-access --enable-hierarchical-namespace

Where:

     * `BUCKET_NAME` is the name you want to give your bucket, subject to [naming requirements](https://docs.cloud.google.com/storage/docs/buckets#naming). For example, `my-bucket`.
     * `BUCKET_LOCATION` is the [location](https://docs.cloud.google.com/storage/docs/locations) of your bucket. For example, `us-east1`.
     * `--uniform-bucket-level-access`: Enable [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) for the bucket.  
**Note:** Enabling uniform bucket-level access on a bucket is required for creating a bucket with hierarchical namespace enabled. 
     * `--enable-hierarchical-namespace`: Enable [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview) for the bucket. You cannot enable hierarchical namespace in an existing bucket. 

If the request is successful, the command returns the following message:
    
    Creating gs://BUCKET_NAME/...

Set the following flags to have greater control over the creation of your bucket:

     * `--project`: Specify the project ID or project number that your bucket will be associated with. For example, `my-project`.
     * `--default-storage-class`: Specify the default [storage class](https://docs.cloud.google.com/storage/docs/storage-classes) of your bucket. For example, `STANDARD`. To automatically manage the storage classes of your objects, use the `--enable-autoclass` flag instead. For more information, see [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass).

For a complete list of options for creating buckets using the Google Cloud CLI, see [`buckets create` options](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/create#FLAGS).

For example:
    
    gcloud storage buckets create gs://BUCKET_NAME --project=PROJECT_ID --default-storage-class=STORAGE_CLASS --location=BUCKET_LOCATION --uniform-bucket-level-access --enable-hierarchical-namespace




### Client Libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name) {
      auto metadata = client.CreateBucket(
          bucket_name,
          gcs::BucketMetadata()
              .set_hierarchical_namespace(gcs::BucketHierarchicalNamespace{true})
              .set_iam_configuration(gcs::BucketIamConfiguration{
                  gcs::UniformBucketLevelAccess{true, {}}, std::nullopt}));
      if (!metadata) throw std::move(metadata).status();
    
      std::cout << "Bucket " << metadata->name() << " created."
                << "\nFull Metadata: " << *metadata << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using Google.Apis.Storage.v1.Data;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class CreateBucketWithHierarchicalNamespaceEnabledSample
    {
        public Bucket CreateBucketWithHierarchicalNamespace(
            string projectId = "your-project-id",
            string bucketName = "your-unique-bucket-name")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var bucket = storage.CreateBucket(projectId,
                new Bucket
                {
                    Name = bucketName,
                    IamConfiguration = new Bucket.IamConfigurationData
                    {
                        UniformBucketLevelAccess = new Bucket.IamConfigurationData.UniformBucketLevelAccessData { Enabled = true }
                    },
                    HierarchicalNamespace = new Bucket.HierarchicalNamespaceData { Enabled = true }
                });
            Console.WriteLine($"Created {bucketName} with Hierarchical Namespace enabled.");
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
    
    // createBucketHierarchicalNamespace creates a new bucket with hierarchical
    // namespace features enabled.
    func createBucketHierarchicalNamespace(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), projectID, bucketName string) error {
    	// projectID := "my-project-id"
    	// bucketName := "bucket-name"
    
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*30)
    	defer cancel()
    
    	attrs := &storage.[BucketAttrs](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketAttrs){
    		HierarchicalNamespace: &storage.[HierarchicalNamespace](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_HierarchicalNamespace){
    			Enabled: true,
    		},
    		// Hierarchical namespace buckets must use uniform bucket-level access.
    		UniformBucketLevelAccess: storage.[UniformBucketLevelAccess](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_UniformBucketLevelAccess){
    			Enabled: true,
    		},
    	}
    	bucket := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucketName)
    	if err := bucket.[Create](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Create)(ctx, projectID, attrs); err != nil {
    		return fmt.Errorf("Bucket(%q).Create: %w", bucketName, err)
    	}
    	fmt.Fprintf(w, "Created bucket %v with hierarchical namespace enabled\n", bucketName)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html);
    import com.google.cloud.storage.[BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html).[HierarchicalNamespace](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.HierarchicalNamespace.html);
    import com.google.cloud.storage.[BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html).[IamConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.IamConfiguration.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public final class CreateHierarchicalNamespaceBucket {
    
      public static void createHierarchicalNamespaceBucket(String projectId, String bucketName)
          throws Exception {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID to give your GCS bucket
        // String bucketName = "your-unique-bucket-name";
        [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html) storageOptions = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build();
        try ([Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = storageOptions.[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)()) {
    
          [BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html) bucketInfo =
              [BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html).newBuilder(bucketName)
                  .setIamConfiguration(
                      // Hierarchical namespace buckets must use uniform bucket-level access.
                      [IamConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.IamConfiguration.html).newBuilder().[setIsUniformBucketLevelAccessEnabled](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.IamConfiguration.Builder.html#com_google_cloud_storage_BucketInfo_IamConfiguration_Builder_setIsUniformBucketLevelAccessEnabled_java_lang_Boolean_)(true).build())
                  .setHierarchicalNamespace([HierarchicalNamespace](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.HierarchicalNamespace.html).newBuilder().setEnabled(true).build())
                  .build();
    
          [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket = storage.create(bucketInfo);
    
          System.out.printf(
              "Created bucket %s with Hierarchical Namespace enabled.%n", bucket.getName());
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
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    // The bucket in the sample below will be created in the project associated with this client.
    // For more information, please see https://cloud.google.com/docs/authentication/production or https://googleapis.dev/nodejs/storage/latest/Storage.html
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function createBucketWithHierarchicalNamespace() {
      const [bucket] = await storage.createBucket(bucketName, {
        iamConfiguration: {
          uniformBucketLevelAccess: {
            enabled: true,
          },
        },
        hierarchicalNamespace: {
          enabled: true,
        },
      });
    
      console.log(
        `Created '${bucket.name}' with hierarchical namespace enabled.`
      );
    }
    
    createBucketWithHierarchicalNamespace().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Create a new bucket with Hierarchical Namespace enabled.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     */
    function create_bucket_hierarchical_namespace(string $bucketName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->createBucket($bucketName, [
            'hierarchicalNamespace' => ['enabled' => true],
            'iamConfiguration' => ['uniformBucketLevelAccess' => ['enabled' => true]]
        ]);
    
        printf('Created bucket %s with Hierarchical Namespace enabled.', $bucket->name());
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def create_bucket_hierarchical_namespace(bucket_name):
        """Creates a bucket with hierarchical namespace enabled."""
        # The ID of your GCS bucket
        # bucket_name = "your-bucket-name"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
        bucket.[iam_configuration](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_iam_configuration).[uniform_bucket_level_access_enabled](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.IAMConfiguration.html#google_cloud_storage_bucket_IAMConfiguration_uniform_bucket_level_access_enabled) = True
        bucket.[hierarchical_namespace_enabled](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_hierarchical_namespace_enabled) = True
        bucket.create()
    
        print(f"Created bucket {bucket_name} with hierarchical namespace enabled.")
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def create_bucket_hierarchical_namespace bucket_name:
      # The ID to give your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
    
      hierarchical_namespace = Google::Apis::StorageV1::[Bucket](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)::HierarchicalNamespace.[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html) enabled: true
    
      storage.[create_bucket](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Project.html) bucket_name do |b|
        b.uniform_bucket_level_access = true
        b.hierarchical_namespace = hierarchical_namespace
      end
    
      puts "Created bucket #{bucket_name} with Hierarchical Namespace enabled."
    end

### Rust
    
    
    use google_cloud_storage::{
        client::StorageControl,
        model::Bucket,
        model::bucket::iam_config::UniformBucketLevelAccess,
        model::bucket::{HierarchicalNamespace, IamConfig},
    };
    
    pub async fn sample(
        client: &StorageControl,
        project_id: &str,
        bucket_id: &str,
    ) -> anyhow::Result<()> {
        let bucket = client
            .create_bucket()
            .set_parent("projects/_")
            .set_bucket_id(bucket_id)
            .set_bucket(
                Bucket::new()
                    .set_project(format!("projects/{project_id}"))
                    .set_hierarchical_namespace(HierarchicalNamespace::new().set_enabled(true))
                    .set_iam_config(IamConfig::new().set_uniform_bucket_level_access(
                        UniformBucketLevelAccess::new().set_enabled(true),
                    )),
            )
            .send()
            .await?;
        println!("successfully created bucket {bucket:?}");
        Ok(())
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the settings for the bucket, which must include a `name` for the bucket. See the [Buckets: Insert](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/insert) documentation for a complete list of settings. The following are common settings to include:
    
    {
      "name": "BUCKET_NAME",
      "location": "BUCKET_LOCATION",
      "storageClass": "STORAGE_CLASS",
      "hierarchicalNamespace": {
        "enabled": "BOOLEAN"
      },
      "iamConfiguration": {
        "uniformBucketLevelAccess": {
          "enabled": true
      },
    },
    }

Where:

     * `BUCKET_NAME` is the name you want to give your bucket, subject to [naming requirements](https://docs.cloud.google.com/storage/docs/buckets#naming). For example, `my-bucket`.
     * `BUCKET_LOCATION` is the [location](https://docs.cloud.google.com/storage/docs/locations) where you want to store your bucket's [object data](https://docs.cloud.google.com/storage/docs/objects). For example, `US-EAST1`.
     * `STORAGE_CLASS` is the default [storage class](https://docs.cloud.google.com/storage/docs/storage-classes) of your bucket. For example, `STANDARD`.
     * `hierarchicalNamespace.enabled` is set to `TRUE` to enable [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview) for your bucket. You cannot enable hierarchical namespace in an existing bucket.
  3. `uniformBucketLevelAccess.enabled` is set to `TRUE` to enable [uniform bucket-level access for your bucket.  
**Note:** Enabling uniform bucket-level access on a bucket is required for creating a bucket with hierarchical namespace enabled. 
  4. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api): 
         
         curl -X POST --data-binary @JSON_FILE_NAME \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://storage.googleapis.com/storage/v1/b?project=PROJECT_IDENTIFIER"

Where:
     * `JSON_FILE_NAME` is name of the JSON file that contains the bucket settings.
     * `PROJECT_IDENTIFIER` is the ID or number of the project that your bucket will be associated with. For example, `my-project`. ](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access)



## What's next

  * [Understand folders](https://docs.cloud.google.com/storage/docs/folders-overview).
  * [Create and manage folders](https://docs.cloud.google.com/storage/docs/create-folders).
  * [Get a bucket's metadata](https://docs.cloud.google.com/storage/docs/getting-bucket-metadata).
  * [Get a bucket's storage layout](https://docs.cloud.google.com/storage/docs/getting-storage-layout).
  * [List](https://docs.cloud.google.com/storage/docs/listing-buckets) and [delete](https://docs.cloud.google.com/storage/docs/deleting-buckets) buckets.



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Cloud Storage performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Cloud Storage free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
