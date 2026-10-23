---
url: https://docs.cloud.google.com/storage/docs/using-object-lock/
title: Enable and use object retention configurations \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:41.706920+00:00
---

# Enable and use object retention configurations  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/using-object-lock/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Enable and use object retention configurations Stay organized with collections  Save and categorize content based on your preferences. 

[Overview](https://docs.cloud.google.com/storage/docs/object-lock)

This page describes how to use the Object Retention Lock feature, including enabling it for a bucket and setting retention configurations for objects within the bucket.

## Required roles

To get the permissions that you need to enable the Object Retention Lock feature for a bucket and set retention configurations on objects, ask your administrator to grant you the Storage Admin (`roles/storage.admin`) IAM role on the bucket or the project that contains the bucket. This [predefined role](https://docs.cloud.google.com/iam/docs/roles-permissions) contains the permissions required to set and manage retention configurations. To see the exact permissions that are required, expand the **Required permissions** section:

#### Required permissions

  * `storage.buckets.create`
  * `storage.buckets.enableObjectRetention`
  * `storage.buckets.get`
  * `storage.buckets.list`
    * This permission is only required if you plan on using the Google Cloud console to perform the instructions on this page.
  * `storage.objects.get`
  * `storage.objects.list`
    * This permission is only required if you plan on using the Google Cloud console to perform the instructions on this page.
  * `storage.objects.overrideUnlockedRetention`
    * This permission is only required if you plan on locking or shortening an existing retention configuration.
  * `storage.objects.setRetention`
  * `storage.objects.update`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

For information about granting roles on buckets, see [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions). For information about granting roles on projects, see [Manage access to projects](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Enable object retentions for a bucket

**Important:** Once the ability to set object retention configurations is enabled on a bucket, it cannot be disabled.

Use the following instructions to allow retention configurations for objects in a bucket. If you want to enable object retention configurations for an existing bucket, you must follow the Google Cloud console instructions.

### Console

**To enable object retention configurations for a new bucket** :

  1. [Create a bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) as you normally would, and in the **Choose how to protect object data** step, select **Retention (For compliance)** followed by **Enable object retention**.



**To enable object retention configurations for an existing bucket** :

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket for which you want to enable object retentions.

  3. Select the **Protection** tab near the top of the page.

The bucket's object retention status is displayed in the **Object retention** section.

  4. In the **Object retention** section, click **Object Retention Not Enabled**.

  5. In the dialog that appears, click **Confirm**.




### Command line

[Create a bucket](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/create) as you normally would, and include the `--enable-per-object-retention` flag in the command.

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    //! [create-bucket-with-object-retention]
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name,
       std::string const& project_id) {
      auto bucket = client.CreateBucket(bucket_name, gcs::BucketMetadata{},
                                        gcs::EnableObjectRetention(true),
                                        gcs::OverrideDefaultProject(project_id));
      if (!bucket) throw std::move(bucket).status();
    
      if (!bucket->has_object_retention()) {
        throw std::runtime_error("missing object retention in new bucket");
      }
      std::cout << "Successfully created bucket " << bucket_name
                << " with object retention: " << bucket->object_retention()
                << "\n";
    }
    //! [create-bucket-with-object-retention]

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using Google.Apis.Storage.v1.Data;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class CreateBucketWithObjectRetentionSample
    {
        public Bucket CreateBucketWithObjectRetention(
            string projectId = "your-project-id",
            string bucketName = "your-unique-bucket-name")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var bucket = storage.CreateBucket(projectId, bucketName, new [CreateBucketOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.CreateBucketOptions.html)
            {
                ObjectRetentionEnabled = true
            });
            Console.WriteLine($"Created {bucketName}, with Object Retention enabled.");
            return bucket;
        }
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class CreateBucketWithObjectRetention {
      public static void createBucketWithObjectRetention(String projectId, String bucketName) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID to give your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
    
        [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket =
            storage.[create](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_create_com_google_cloud_storage_BlobInfo_byte___com_google_cloud_storage_Storage_BlobTargetOption____)(
                BucketInfo.of(bucketName), Storage.BucketTargetOption.enableObjectRetention(true));
    
        System.out.println(
            "Created bucket "
                + bucket.getName()
                + " with object retention enabled setting: "
                + bucket.getObjectRetention().getMode().toString());
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
    
    async function createBucketWithObjectRetention() {
      const [bucket] = await storage.createBucket(bucketName, {
        enableObjectRetention: true,
      });
    
      console.log(
        `Created '${bucket.name}' with object retention enabled setting: ${bucket.metadata.objectRetention.mode}`
      );
    }
    
    createBucketWithObjectRetention().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Create a Cloud Storage bucket with the object retention enabled.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     */
    function create_bucket_with_object_retention(string $bucketName): void
    {
        $storage = new StorageClient();
    
        $bucket = $storage->createBucket($bucketName, [
            'enableObjectRetention' => true
        ]);
        printf(
            'Created bucket %s with object retention enabled setting: %s' . PHP_EOL,
            $bucketName,
            $bucket->info()['objectRetention']['mode']
        );
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def create_bucket_object_retention(bucket_name):
        """Creates a bucket with object retention enabled."""
        # The ID of your GCS bucket
        # bucket_name = "your-bucket-name"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[create_bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_create_bucket)(bucket_name, enable_object_retention=True)
    
        print(f"Created bucket {bucket_name} with object retention enabled setting: {bucket.[object_retention_mode](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_object_retention_mode)}")
    
    

### Rust
    
    
    use google_cloud_storage::{client::StorageControl, model::Bucket, model::bucket::ObjectRetention};
    
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
                    .set_object_retention(ObjectRetention::new().set_enabled(true)),
            )
            .send()
            .await?;
        println!("successfully created bucket {bucket:?}");
        Ok(())
    }

### REST APIs

### JSON API

[Create a bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/insert) as you normally would, and include the query parameter `enableObjectRetention=true` as part of the request.

### XML API

[Create a bucket](https://docs.cloud.google.com/storage/docs/xml-api/put-bucket-create) as you normally would, and include the header `x-goog-bucket-object-lock-enabled: True` as part of the request.

## View a bucket's object retention status

To see if retention configurations can be set for objects in a bucket:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click the name of the bucket whose status you want to check.

  3. Click the **Protection** tab.

  4. The bucket's object retention status is displayed in the **Object retention** section.




### Command line

Use the [`gcloud storage buckets describe`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/describe) command with the `--format` flag:
    
    
    gcloud storage buckets describe gs://BUCKET_NAME --format="default(per_object_retention)"

Where `BUCKET_NAME` is the name of the bucket whose retention policy you want to view. For example, `my-bucket`.

If successful and a retention policy exists for the bucket, the response is similar to the following:
    
    
    per_object_retention:
      mode: Enabled
    

If successful and a retention policy does not exist for the bucket, the response is similar to the following:
    
    
    null

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

To view a bucket's object retention configuration, follow the instructions for displaying a bucket's metadata and look for the object retention field in the response. 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name) {
      StatusOr<gcs::BucketMetadata> bucket_metadata =
          client.GetBucketMetadata(bucket_name);
      if (!bucket_metadata) throw std::move(bucket_metadata).status();
    
      std::cout << "The metadata for bucket " << bucket_metadata->name() << " is "
                << *bucket_metadata << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

To view a bucket's object retention configuration, follow the instructions for displaying a bucket's metadata and look for the object retention field in the response. 
    
    
    using Google.Apis.Storage.v1.Data;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class GetBucketMetadataSample
    {
        public Bucket GetBucketMetadata(string bucketName = "your-unique-bucket-name")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var bucket = storage.GetBucket(bucketName, new [GetBucketOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.GetBucketOptions.html) { Projection = [Projection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.Projection.html).[Full](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.Projection.html#Google_Cloud_Storage_V1_Projection_Full) });
            Console.WriteLine($"Bucket:\t{bucket.Name}");
            Console.WriteLine($"Acl:\t{bucket.[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UrlSigner.PostPolicyStandardElement.html#Google_Cloud_Storage_V1_UrlSigner_PostPolicyStandardElement_Acl)}");
            Console.WriteLine($"Billing:\t{bucket.Billing}");
            Console.WriteLine($"Cors:\t{bucket.Cors}");
            Console.WriteLine($"DefaultEventBasedHold:\t{bucket.DefaultEventBasedHold}");
            Console.WriteLine($"DefaultObjectAcl:\t{bucket.DefaultObjectAcl}");
            Console.WriteLine($"Encryption:\t{bucket.Encryption}");
            if (bucket.Encryption != null)
            {
                Console.WriteLine($"KmsKeyName:\t{bucket.Encryption.DefaultKmsKeyName}");
            }
            Console.WriteLine($"Id:\t{bucket.Id}");
            Console.WriteLine($"Kind:\t{bucket.Kind}");
            Console.WriteLine($"Lifecycle:\t{bucket.Lifecycle}");
            Console.WriteLine($"Location:\t{bucket.Location}");
            Console.WriteLine($"LocationType:\t{bucket.LocationType}");
            Console.WriteLine($"Logging:\t{bucket.Logging}");
            Console.WriteLine($"Metageneration:\t{bucket.Metageneration}");
            Console.WriteLine($"ObjectRetention:\t{bucket.ObjectRetention}");
            Console.WriteLine($"Owner:\t{bucket.Owner}");
            Console.WriteLine($"ProjectNumber:\t{bucket.ProjectNumber}");
            Console.WriteLine($"RetentionPolicy:\t{bucket.RetentionPolicy}");
            Console.WriteLine($"SelfLink:\t{bucket.SelfLink}");
            Console.WriteLine($"StorageClass:\t{bucket.StorageClass}");
            Console.WriteLine($"TimeCreated:\t{bucket.TimeCreated}");
            Console.WriteLine($"Updated:\t{bucket.Updated}");
            Console.WriteLine($"Versioning:\t{bucket.Versioning}");
            Console.WriteLine($"Website:\t{bucket.Website}");
            Console.WriteLine($"TurboReplication:\t{bucket.Rpo}");
            if (bucket.Labels != null)
            {
                Console.WriteLine("Labels:");
                foreach (var label in bucket.Labels)
                {
                    Console.WriteLine($"{label.[Key](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UrlSigner.PostPolicyStandardElement.html#Google_Cloud_Storage_V1_UrlSigner_PostPolicyStandardElement_Key)}:\t{label.Value}");
                }
            }
            return bucket;
        }
    }

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

To view a bucket's object retention configuration, follow the instructions for displaying a bucket's metadata and look for the object retention field in the response. 
    
    
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import java.util.Map;
    
    public class GetBucketMetadata {
      public static void getBucketMetadata(String projectId, String bucketName) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
    
        // Select all fields. Fields can be selected individually e.g. Storage.BucketField.NAME
        [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket =
            storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName, Storage.BucketGetOption.fields(Storage.BucketField.values()));
    
        // Print bucket metadata
        System.out.println("BucketName: " + bucket.getName());
        System.out.println("DefaultEventBasedHold: " + bucket.[getDefaultEventBasedHold](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_getDefaultEventBasedHold__)());
        System.out.println("DefaultKmsKeyName: " + bucket.[getDefaultKmsKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_getDefaultKmsKeyName__)());
        System.out.println("Id: " + bucket.getGeneratedId());
        System.out.println("IndexPage: " + bucket.[getIndexPage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_getIndexPage__)());
        System.out.println("Location: " + bucket.getLocation());
        System.out.println("LocationType: " + bucket.[getLocationType](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_getLocationType__)());
        System.out.println("Metageneration: " + bucket.getMetageneration());
        System.out.println("NotFoundPage: " + bucket.[getNotFoundPage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_getNotFoundPage__)());
        System.out.println("RetentionEffectiveTime: " + bucket.[getRetentionEffectiveTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_getRetentionEffectiveTime__)());
        System.out.println("RetentionPeriod: " + bucket.[getRetentionPeriod](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_getRetentionPeriod__)());
        System.out.println("RetentionPolicyIsLocked: " + bucket.[retentionPolicyIsLocked](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_retentionPolicyIsLocked__)());
        System.out.println("RequesterPays: " + bucket.requesterPays());
        System.out.println("SelfLink: " + bucket.getSelfLink());
        System.out.println("StorageClass: " + bucket.getStorageClass().[name](https://docs.cloud.google.com/java/docs/reference/google-cloud-nio/latest/com.google.cloud.storage.contrib.nio.CloudStorageFileAttributeView.html#com_google_cloud_storage_contrib_nio_CloudStorageFileAttributeView_name__)());
        System.out.println("TimeCreated: " + bucket.getCreateTime());
        System.out.println("VersioningEnabled: " + bucket.[versioningEnabled](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_versioningEnabled__)());
        System.out.println("ObjectRetention: " + bucket.getObjectRetention());
        if (bucket.getLabels() != null) {
          System.out.println("\n\n\nLabels:");
          for (Map.Entry<String, String> label : bucket.getLabels().entrySet()) {
            System.out.println(label.getKey() + "=" + label.getValue());
          }
        }
        if (bucket.getLifecycleRules() != null) {
          System.out.println("\n\n\nLifecycle Rules:");
          for (BucketInfo.LifecycleRule rule : bucket.getLifecycleRules()) {
            System.out.println(rule);
          }
        }
      }
    }

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

To view a bucket's object retention configuration, follow the instructions for displaying a bucket's metadata and look for the object retention field in the response. 
    
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function getBucketMetadata() {
      /**
       * TODO(developer): Uncomment the following lines before running the sample.
       */
      // The ID of your GCS bucket
      // const bucketName = 'your-unique-bucket-name';
    
      // Get Bucket Metadata
      const [metadata] = await storage.bucket(bucketName).getMetadata();
    
      console.log([JSON](https://docs.cloud.google.com/nodejs/docs/reference/storage-transfer/latest/storage-transfer/protos.google.storagetransfer.v1.notificationconfig.payloadformat.html).stringify(metadata, null, 2));
    }

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

To view a bucket's object retention configuration, follow the instructions for displaying a bucket's metadata and look for the object retention field in the response. 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Get bucket metadata.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     */
    function get_bucket_metadata(string $bucketName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
        $info = $bucket->info();
    
        printf('Bucket Metadata: %s' . PHP_EOL, print_r($info, true));
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

To view a bucket's object retention configuration, follow the instructions for displaying a bucket's metadata and look for the object retention field in the response. 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def bucket_metadata(bucket_name):
        """Prints out a bucket's metadata."""
        # bucket_name = 'your-bucket-name'
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[get_bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_get_bucket)(bucket_name)
    
        print(f"ID: {bucket.id}")
        print(f"Name: {bucket.name}")
        print(f"Storage Class: {bucket.storage_class}")
        print(f"Location: {bucket.[location](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_location)}")
        print(f"Location Type: {bucket.[location_type](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_location_type)}")
        print(f"Cors: {bucket.[cors](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_cors)}")
        print(f"Default Event Based Hold: {bucket.[default_event_based_hold](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_default_event_based_hold)}")
        print(f"Default KMS Key Name: {bucket.default_kms_key_name}")
        print(f"Metageneration: {bucket.metageneration}")
        print(
            f"Public Access Prevention: {bucket.[iam_configuration](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_iam_configuration).[public_access_prevention](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.IAMConfiguration.html#google_cloud_storage_bucket_IAMConfiguration_public_access_prevention)}"
        )
        print(f"Retention Effective Time: {bucket.[retention_policy_effective_time](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_retention_policy_effective_time)}")
        print(f"Retention Period: {bucket.[retention_period](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_retention_period)}")
        print(f"Retention Policy Locked: {bucket.[retention_policy_locked](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_retention_policy_locked)}")
        print(f"Object Retention Mode: {bucket.[object_retention_mode](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_object_retention_mode)}")
        print(f"Requester Pays: {bucket.[requester_pays](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_requester_pays)}")
        print(f"Self Link: {bucket.self_link}")
        print(f"Time Created: {bucket.time_created}")
        print(f"Versioning Enabled: {bucket.[versioning_enabled](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_versioning_enabled)}")
        print(f"Labels: {bucket.[labels](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_labels)}")
    
    

### Rust

To view a bucket's object retention configuration, follow the instructions for displaying a bucket's metadata and look for the object retention field in the response. 
    
    
    use google_cloud_storage::client::StorageControl;
    
    pub async fn sample(client: &StorageControl, bucket_id: &str) -> anyhow::Result<()> {
        let bucket = client
            .get_bucket()
            .set_name(format!("projects/_/buckets/{bucket_id}"))
            .send()
            .await?;
        println!("successfully obtained bucket metadata {bucket:?}");
        Ok(())
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the JSON API with a [`GET` Bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/get) request that includes the `objectRetention` field:
         
         curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME?fields=objectRetention"

Where `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.




### XML API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the XML API with a [`GET` Bucket](https://docs.cloud.google.com/storage/docs/xml-api/get-bucket-metadata) request scoped to `?object-lock`:
         
         curl -X GET \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storage.googleapis.com/BUCKET_NAME?object-lock"

Where `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.




## Set an object's retention configuration

**Caution:** Setting the mode of a retention configuration to `Locked` (`COMPLIANCE` in the XML API) is an irreversible action. If you do so: 

  * You cannot remove the retention configuration from the object.
  * You cannot decrease the retention time for the object.



In order to set a retention configuration for an object, the object must be stored in a bucket for which object retentions are enabled. To set a retention configuration for an object:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket that contains the object whose retention configuration you want to set or modify.

The **Bucket details** page opens, with the **Objects** tab selected.

  3. Navigate to the object, which might be located in a folder.

  4. Click the name of the object.

The **Object details** page opens, which displays object metadata.

  5. In the **Protection** section, click the **Edit** icon (_edit_) associated with **From object retention configuration**.

The **Edit retention** pane opens.

  6. In the **Object retention configuration** section, click **Enabled** or **Disabled**.

     1. If the retention configuration is enabled, select a date and time for the configuration in the **Retain until time** section, and click **Unlocked** or **Locked** in the **Retention mode** section.
  7. Click **Confirm**.


**Note:** You can also set a retention configuration for an object at the time the object is uploaded to the bucket. If the bucket you're uploading the object to has the object retention feature enabled, a panel appears during the upload that lets you specify a retention configuration for the object.

### Command line

Use the [`gcloud storage objects update`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/objects/update) command with the appropriate flags. To add or modify a retention configuration, use the following command. Note that you must additionally include the `--override-unlocked-retention` flag if you are modifying an existing configuration in a way that locks it or shortens its retain-until time:
    
    
    gcloud storage objects update gs://BUCKET_NAME/OBJECT_NAME --retain-until=DATETIME --retention-mode=STATE

Where:

  * `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.

  * `OBJECT_NAME` is the name of the relevant object. For example, `kitten.png`.

  * `DATETIME` is the earliest date and time that the object can be deleted. For example, `2028-02-15T05:30:00Z`.

  * `STATE` is either `Locked` or `Unlocked`.




If successful, the response looks similar to the following example:
    
    
    Updating gs://my-bucket/kitten.png...
      Completed 1  

To remove a retention configuration from an object, use the following command:
    
    
    gcloud storage objects update gs://BUCKET_NAME/OBJECT_NAME --clear-retention --override-unlocked-retention

Where:

  * `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.

  * `OBJECT_NAME` is the name of the relevant object. For example, `kitten.png`.


**Note:** You can also set a retention configuration for an object at the time the object is written to the bucket. See command documentation, such as [`gcloud storage cp`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cp) for more information.

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name,
       std::string const& object_name) {
      auto original = client.GetObjectMetadata(bucket_name, object_name);
      if (!original) throw std::move(original).status();
    
      auto const until =
          std::chrono::system_clock::now() + std::chrono::hours(24);
      auto updated = client.PatchObject(
          bucket_name, object_name,
          gcs::ObjectMetadataPatchBuilder().SetRetention(
              gcs::ObjectRetention{gcs::ObjectRetentionUnlocked(), until}),
          gcs::OverrideUnlockedRetention(true),
          gcs::IfMetagenerationMatch(original->metageneration()));
      if (!updated) throw std::move(updated).status();
    
      std::cout << "Successfully updated object retention configuration: "
                << *updated << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    using Object = Google.Apis.Storage.v1.Data.Object;
    
    public class SetObjectRetentionPolicySample
    {
        public Google.Apis.Storage.v1.Data.Object SetObjectRetentionPolicy(
            string bucketName = "your-unique-bucket-name", // A bucket that has object retention enabled
            string objectName = "your-object-name") // An object that does not have a retention policy set
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var file = storage.GetObject(bucketName, objectName);
    
    
            file.Retention = new Object.RetentionData
            {
                Mode = "Unlocked", RetainUntilTimeDateTimeOffset = DateTimeOffset.UtcNow.AddDays(10)
            };
    
            file = storage.UpdateObject(file);
    
            Console.WriteLine($"The retention policy for object {objectName} was set to:");
            Console.WriteLine("Mode: " + file.Retention.Mode);
            Console.WriteLine("RetainUntilTime: " + file.Retention.RetainUntilTimeDateTimeOffset.ToString());
    
            // To modify an existing policy on an Unlocked object, pass in the override parameter
            file.Retention = new Object.RetentionData
            {
                Mode = "Unlocked", RetainUntilTimeDateTimeOffset = DateTimeOffset.UtcNow.AddDays(9)
            };
    
            file = storage.UpdateObject(file, new [UpdateObjectOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UpdateObjectOptions.html) { OverrideUnlockedRetention = true });
    
            Console.WriteLine($"The retention policy for object {objectName} was updated to:");
            Console.WriteLine("Mode: " + file.Retention.Mode);
            Console.WriteLine("RetainUntilTime: " + file.Retention.RetainUntilTimeDateTimeOffset.ToString());
    
            return file;
        }
    }

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import static java.time.OffsetDateTime.now;
    
    import com.google.cloud.storage.[Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html);
    import com.google.cloud.storage.[BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html);
    import com.google.cloud.storage.[BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html).[Retention](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.Retention.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class SetObjectRetentionPolicy {
      public static void setObjectRetentionPolicy(
          String projectId, String bucketName, String objectName) throws [StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket that has object retention enabled
        // String bucketName = "your-unique-bucket-name";
    
        // The ID of your GCS object
        // String objectName = "your-object-name";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html) blobId = [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html).of(bucketName, objectName);
        [Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html) blob = storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(blobId);
        if (blob == null) {
          System.out.println("The object " + objectName + " was not found in " + bucketName);
          return;
        }
    
        [Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html) updated =
            blob.[toBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html#com_google_cloud_storage_Blob_toBuilder__)()
                .setRetention(
                    [Retention](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.Retention.html).newBuilder()
                        .setMode([Retention](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.Retention.html).Mode.UNLOCKED)
                        .setRetainUntilTime(now().plusDays(10))
                        .build())
                .build()
                .update();
    
        System.out.println("Retention policy for object " + objectName + " was set to:");
        System.out.println(updated.[getRetention](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html#com_google_cloud_storage_BlobInfo_getRetention__)().toString());
    
        // To modify an existing policy on an Unlocked object, pass in the override parameter
        blob.[toBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html#com_google_cloud_storage_Blob_toBuilder__)()
            .setRetention(
                updated.[getRetention](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html#com_google_cloud_storage_BlobInfo_getRetention__)().toBuilder().setRetainUntilTime(now().plusDays(9)).build())
            .build()
            .update([Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobTargetOption.overrideUnlockedRetention(true));
    
        System.out.println("Retention policy for object " + objectName + " was updated to:");
        System.out.println(storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(blobId).[getRetention](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html#com_google_cloud_storage_BlobInfo_getRetention__)().toString());
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
    
    // The new ID for your GCS file
    // const destFileName = 'your-new-file-name';
    
    // The content to be uploaded in the GCS file
    // const contents = 'your file content';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    // The bucket in the sample below will be created in the project associated with this client.
    // For more information, please see https://cloud.google.com/docs/authentication/production or https://googleapis.dev/nodejs/storage/latest/Storage.html
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function setObjectRetentionPolicy() {
      // Get a reference to the bucket
      const myBucket = storage.bucket(bucketName);
    
      // Create a reference to a file object
      const file = myBucket.file(destFileName);
    
      // Save the file data
      await file.[save](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/file_2.html)(contents);
    
      // Set the retention policy for the file
      const retentionDate = new Date();
      retentionDate.setDate(retentionDate.getDate() + 10);
      const [metadata] = await file.setMetadata({
        retention: {
          mode: 'Unlocked',
          retainUntilTime: retentionDate.toISOString(),
        },
      });
    
      console.log(
        `Retention policy for file ${file.name} was set to: ${metadata.retention.mode}`
      );
    
      // To modify an existing policy on an unlocked file object, pass in the override parameter
      const newRetentionDate = new Date(retentionDate.getDate());
      newRetentionDate.setDate(newRetentionDate.getDate() + 9);
      const [newMetadata] = await file.setMetadata({
        retention: {
          mode: 'Unlocked',
          retainUntilTime: newRetentionDate,
        },
        overrideUnlockedRetention: true,
      });
    
      console.log(
        `Retention policy for file ${file.name} was updated to: ${newMetadata.retention.retainUntilTime}`
      );
    }
    
    setObjectRetentionPolicy().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Sets a bucket's retention policy.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $objectName The name of your Cloud Storage object.
     *        (e.g. 'my-object')
     */
    function set_object_retention_policy(string $bucketName, string $objectName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
        $object = $bucket->object($objectName);
        $expires = (new \DateTime)->add(
            \DateInterval::createFromDateString('+10 days')
        );
        // To modify an existing policy on an Unlocked object, pass the override parameter
        $object->update([
            'retention' => [
                'mode' => 'Unlocked',
                'retainUntilTime' => $expires->format(\DateTime::RFC3339)
            ],
            'overrideUnlockedRetention' => true
        ]);
        printf(
            'Retention policy for object %s was updated to: %s' . PHP_EOL,
            $objectName,
            $object->info()['retention']['retainUntilTime']
        );
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def set_object_retention_policy(bucket_name, contents, destination_blob_name):
        """Set the object retention policy of a file."""
    
        # The ID of your GCS bucket
        # bucket_name = "your-bucket-name"
    
        # The contents to upload to the file
        # contents = "these are my contents"
    
        # The ID of your GCS object
        # destination_blob_name = "storage-object-name"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.[upload_from_string](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string)(contents)
    
        # Set the retention policy for the file.
        blob.[retention](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_retention).[mode](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Retention.html#google_cloud_storage_blob_Retention_mode) = "Unlocked"
        retention_date = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=10)
        blob.[retention](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_retention).[retain_until_time](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Retention.html#google_cloud_storage_blob_Retention_retain_until_time) = retention_date
        blob.patch()
        print(
            f"Retention policy for file {destination_blob_name} was set to: {blob.[retention](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_retention).[mode](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Retention.html#google_cloud_storage_blob_Retention_mode)}."
        )
    
        # To modify an existing policy on an unlocked file object, pass in the override parameter.
        new_retention_date = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=9)
        blob.[retention](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_retention).[retain_until_time](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Retention.html#google_cloud_storage_blob_Retention_retain_until_time) = new_retention_date
        blob.patch(override_unlocked_retention=True)
        print(
            f"Retention policy for file {destination_blob_name} was updated to: {blob.[retention](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_retention).[retain_until_time](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Retention.html#google_cloud_storage_blob_Retention_retain_until_time)}."
        )
    
    

### Rust
    
    
    use google_cloud_storage::{client::StorageControl, model::object::Retention};
    use google_cloud_wkt::{FieldMask, Timestamp};
    use std::time::SystemTime;
    
    pub async fn sample(client: &StorageControl, bucket_id: &str) -> anyhow::Result<()> {
        const NAME: &str = "object-to-update";
        let object = client
            .get_object()
            .set_bucket(format!("projects/_/buckets/{bucket_id}"))
            .set_object(NAME)
            .send()
            .await?;
    
        let now = Timestamp::try_from(SystemTime::now())?;
        let then = Timestamp::clamp(now.seconds() + 24 * 60 * 60, now.nanos());
        let metageneration = object.metageneration;
        let updated = client
            .update_object()
            .set_if_metageneration_match(metageneration)
            .set_object(
                object.set_retention(
                    Retention::new()
                        .set_mode("UNLOCKED")
                        .set_retain_until_time(then),
                ),
            )
            .set_override_unlocked_retention(true)
            .set_update_mask(FieldMask::default().set_paths(["retention"]))
            .send()
            .await?;
        println!("successfully set retention for object {NAME} in bucket {bucket_id}: {updated:?}");
        Ok(())
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the following information:
         
         {
           "retention": {
             "mode": STATE,
             "retainUntilTime": "DATETIME"
           }
         }

Where:

     * `STATE` is either `Locked` or `Unlocked`.

     * `DATETIME` is the earliest date and time that the object can be deleted. For example, `2028-02-15T05:30:00Z`.

  3. Use [`cURL`](http://curl.haxx.se/) to call the JSON API with a [`PATCH` Object](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/patch) request:
         
         curl -X PATCH --data-binary @JSON_FILE_NAME \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/o/OBJECT_NAME?overrideUnlockedRetention=BOOLEAN"

Where:

     * `JSON_FILE_NAME` is the path for the file that you created in Step 2.
     * `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.
     * `OBJECT_NAME` is the URL-encoded name of the relevant object. For example, `pets/kitten.png`, URL-encoded as `pets%2Fkitten.png`.
     * `BOOLEAN` must be `true` if the request shortens, removes, or locks an existing retention configuration. Otherwise, the `overrideUnlockedRetention` parameter can be excluded from the request entirely.

**Note:** You can also set a retention configuration for an object at the time the object is written to the bucket. See request documentation, such as [Objects: Insert](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/insert) for more information.

### XML API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create an XML file that contains the following information:
         
         <Retention>
           <Mode>
             STATE
           </Mode>
           <RetainUntilDate>
             DATETIME
           </RetainUntilDate>
         </Retention>

Where:

     * `STATE` is either `GOVERNANCE` or `COMPLIANCE`.

     * `DATETIME` is the earliest date and time that the object can be deleted. For example, `2028-02-15T05:30:00Z`.

  3. Use [`cURL`](http://curl.haxx.se/) to call the XML API with a [`PUT` Object](https://docs.cloud.google.com/storage/docs/xml-api/put-object-retention) request scoped to `?retention`:
         
         curl -X PUT --data-binary @XML_FILE_NAME \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "x-goog-bypass-governance-retention: BOOLEAN" \
           "https://storage.googleapis.com/BUCKET_NAME/OBJECT_NAME?retention"

Where:

     * `XML_FILE_NAME` is the path for the XML file that you created in Step 2.
     * `BOOLEAN` must be `true` if the request shortens, removes, or locks an existing retention configuration. Otherwise, the `x-goog-bypass-governance-retention` header can be excluded from the request entirely.
     * `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.
     * `OBJECT_NAME` is the URL-encoded name of the relevant object. For example, `pets/kitten.png`, URL-encoded as `pets%2Fkitten.png`.

**Note:** You can also set a retention configuration for an object at the time the object is written to the bucket. See request documentation, such as [`PUT Object`](https://docs.cloud.google.com/storage/docs/xml-api/put-object-upload) for more information.

## Set or update retention configurations in bulk

To set or update retention configurations for millions or billions of objects with a single job, use [storage batch operations](https://docs.cloud.google.com/storage/docs/batch-operations/overview). To create a job, specify the objects whose retention configuration you want to set or update, either by providing a list of objects in a manifest file or by using object prefixes. After you have specified the object list, [create a storage batch operations job](https://docs.cloud.google.com/storage/docs/batch-operations/create-manage-batch-operation-jobs#create-batch-operation-job) to set or update retention configurations.

## View an object's retention configuration

To view what, if any, retention configuration is set on an object:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket that contains the object whose retention configuration you want to view.

The **Bucket details** page opens, with the **Objects** tab selected.

  3. Navigate to the object, which might be located in a folder.

  4. Click the name of the object.

The **Object details** page opens, which displays object metadata. Information about any retention configuration the object has is shown in the **Protection** section.




### Command line

Use the [`gcloud storage objects describe`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/objects/describe) command with the `--format` flag:
    
    
    gcloud storage objects describe gs://BUCKET_NAME/OBJECT_NAME --format="default(retention_settings)"

Where:

  * `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.

  * `OBJECT_NAME` is the name of the relevant object. For example, `kitten.png`.




If successful and a retention configuration exists for the object, the response is similar to the following:
    
    
    retention_settings:
      mode: Unlocked
      retainUntilTime: '2028-11-30T14:11:14+00:00'
    

If successful and a retention configuration does not exist for the object, the response is similar to the following:
    
    
    null

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

To view an object's retention configuration, follow the instructions for displaying a object's metadata and look for the retention field in the response. 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name,
       std::string const& object_name) {
      StatusOr<gcs::ObjectMetadata> object_metadata =
          client.GetObjectMetadata(bucket_name, object_name);
      if (!object_metadata) throw std::move(object_metadata).status();
    
      std::cout << "The metadata for object " << object_metadata->name()
                << " in bucket " << object_metadata->bucket() << " is "
                << *object_metadata << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

To view an object's retention configuration, follow the instructions for displaying a object's metadata and look for the retention field in the response. 
    
    
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class GetMetadataSample
    {
        public Google.Apis.Storage.v1.Data.Object GetMetadata(
            string bucketName = "your-unique-bucket-name",
            string objectName = "your-object-name")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var storageObject = storage.GetObject(bucketName, objectName, new [GetObjectOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.GetObjectOptions.html) { Projection = [Projection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.Projection.html).[Full](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.Projection.html#Google_Cloud_Storage_V1_Projection_Full) });
            Console.WriteLine($"Bucket:\t{storageObject.Bucket}");
            Console.WriteLine($"CacheControl:\t{storageObject.[CacheControl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UrlSigner.PostPolicyStandardElement.html#Google_Cloud_Storage_V1_UrlSigner_PostPolicyStandardElement_CacheControl)}");
            Console.WriteLine($"ComponentCount:\t{storageObject.ComponentCount}");
            Console.WriteLine($"ContentDisposition:\t{storageObject.[ContentDisposition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UrlSigner.PostPolicyStandardElement.html#Google_Cloud_Storage_V1_UrlSigner_PostPolicyStandardElement_ContentDisposition)}");
            Console.WriteLine($"ContentEncoding:\t{storageObject.[ContentEncoding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UrlSigner.PostPolicyStandardElement.html#Google_Cloud_Storage_V1_UrlSigner_PostPolicyStandardElement_ContentEncoding)}");
            Console.WriteLine($"ContentLanguage:\t{storageObject.ContentLanguage}");
            Console.WriteLine($"ContentType:\t{storageObject.[ContentType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UrlSigner.PostPolicyStandardElement.html#Google_Cloud_Storage_V1_UrlSigner_PostPolicyStandardElement_ContentType)}");
            Console.WriteLine($"Crc32c:\t{storageObject.Crc32c}");
            Console.WriteLine($"ETag:\t{storageObject.ETag}");
            Console.WriteLine($"Generation:\t{storageObject.Generation}");
            Console.WriteLine($"Id:\t{storageObject.Id}");
            Console.WriteLine($"Kind:\t{storageObject.Kind}");
            Console.WriteLine($"KmsKeyName:\t{storageObject.KmsKeyName}");
            Console.WriteLine($"Md5Hash:\t{storageObject.Md5Hash}");
            Console.WriteLine($"MediaLink:\t{storageObject.MediaLink}");
            Console.WriteLine($"Metageneration:\t{storageObject.Metageneration}");
            Console.WriteLine($"Name:\t{storageObject.Name}");
            Console.WriteLine($"Retention:\t{storageObject.Retention}");
            Console.WriteLine($"Size:\t{storageObject.Size}");
            Console.WriteLine($"StorageClass:\t{storageObject.StorageClass}");
            Console.WriteLine($"TimeCreated:\t{storageObject.TimeCreated}");
            Console.WriteLine($"Updated:\t{storageObject.Updated}");
            bool eventBasedHold = storageObject.EventBasedHold ?? false;
            Console.WriteLine("Event-based hold enabled? {0}", eventBasedHold);
            bool temporaryHold = storageObject.TemporaryHold ?? false;
            Console.WriteLine("Temporary hold enabled? {0}", temporaryHold);
            Console.WriteLine($"RetentionExpirationTime\t{storageObject.RetentionExpirationTime}");
            if (storageObject.Metadata != null)
            {
                Console.WriteLine("Metadata: ");
                foreach (var metadata in storageObject.Metadata)
                {
                    Console.WriteLine($"{metadata.[Key](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UrlSigner.PostPolicyStandardElement.html#Google_Cloud_Storage_V1_UrlSigner_PostPolicyStandardElement_Key)}:\t{metadata.Value}");
                }
            }
            Console.WriteLine($"CustomTime:\t{storageObject.CustomTime}");
            return storageObject;
        }
    }

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

To view an object's retention configuration, follow the instructions for displaying a object's metadata and look for the retention field in the response. 
    
    
    import com.google.cloud.storage.[Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import java.util.Date;
    import java.util.Map;
    
    public class GetObjectMetadata {
      public static void getObjectMetadata(String projectId, String bucketName, String blobName)
          throws [StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The ID of your GCS object
        // String objectName = "your-object-name";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
    
        // Select all fields
        // Fields can be selected individually e.g. Storage.BlobField.CACHE_CONTROL
        [Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html) blob =
            storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName, blobName, Storage.BlobGetOption.fields(Storage.BlobField.values()));
    
        // Print blob metadata
        System.out.println("Bucket: " + blob.getBucket());
        System.out.println("CacheControl: " + blob.getCacheControl());
        System.out.println("ComponentCount: " + blob.[getComponentCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html#com_google_cloud_storage_BlobInfo_getComponentCount__)());
        System.out.println("ContentDisposition: " + blob.getContentDisposition());
        System.out.println("ContentEncoding: " + blob.getContentEncoding());
        System.out.println("ContentLanguage: " + blob.getContentLanguage());
        System.out.println("ContentType: " + blob.getContentType());
        System.out.println("CustomTime: " + blob.getCustomTime());
        System.out.println("Crc32c: " + blob.[getCrc32c](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html#com_google_cloud_storage_BlobInfo_getCrc32c__)());
        System.out.println("Crc32cHexString: " + blob.[getCrc32cToHexString](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html#com_google_cloud_storage_BlobInfo_getCrc32cToHexString__)());
        System.out.println("ETag: " + blob.getEtag());
        System.out.println("Generation: " + blob.getGeneration());
        System.out.println("Id: " + blob.[getBlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html#com_google_cloud_storage_BlobInfo_getBlobId__)());
        System.out.println("KmsKeyName: " + blob.[getKmsKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html#com_google_cloud_storage_BlobInfo_getKmsKeyName__)());
        System.out.println("Md5Hash: " + blob.[getMd5](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html#com_google_cloud_storage_BlobInfo_getMd5__)());
        System.out.println("Md5HexString: " + blob.[getMd5ToHexString](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html#com_google_cloud_storage_BlobInfo_getMd5ToHexString__)());
        System.out.println("MediaLink: " + blob.[getMediaLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html#com_google_cloud_storage_BlobInfo_getMediaLink__)());
        System.out.println("Metageneration: " + blob.getMetageneration());
        System.out.println("Name: " + blob.getName());
        System.out.println("Size: " + blob.[getSize](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html#com_google_cloud_storage_BlobInfo_getSize__)());
        System.out.println("StorageClass: " + blob.getStorageClass());
        System.out.println("TimeCreated: " + new Date(blob.getCreateTime()));
        System.out.println("Last Metadata Update: " + new Date(blob.getUpdateTime()));
        System.out.println("Object Retention Policy: " + blob.[getRetention](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html#com_google_cloud_storage_BlobInfo_getRetention__)());
        Boolean temporaryHoldIsEnabled = (blob.getTemporaryHold() != null && blob.getTemporaryHold());
        System.out.println("temporaryHold: " + (temporaryHoldIsEnabled ? "enabled" : "disabled"));
        Boolean eventBasedHoldIsEnabled =
            (blob.getEventBasedHold() != null && blob.getEventBasedHold());
        System.out.println("eventBasedHold: " + (eventBasedHoldIsEnabled ? "enabled" : "disabled"));
        if (blob.[getRetentionExpirationTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html#com_google_cloud_storage_BlobInfo_getRetentionExpirationTime__)() != null) {
          System.out.println("retentionExpirationTime: " + new Date(blob.[getRetentionExpirationTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html#com_google_cloud_storage_BlobInfo_getRetentionExpirationTime__)()));
        }
        if (blob.getMetadata() != null) {
          System.out.println("\n\n\nUser metadata:");
          for (Map.Entry<String, String> userMetadata : blob.getMetadata().entrySet()) {
            System.out.println(userMetadata.getKey() + "=" + userMetadata.getValue());
          }
        }
      }
    }

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

To view an object's retention configuration, follow the instructions for displaying a object's metadata and look for the retention field in the response. 
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The ID of your GCS bucket
    // const bucketName = 'your-unique-bucket-name';
    
    // The ID of your GCS file
    // const fileName = 'your-file-name';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function getMetadata() {
      // Gets the metadata for the file
      const [metadata] = await storage
        .bucket(bucketName)
        .file(fileName)
        .getMetadata();
    
      console.log(`Bucket: ${metadata.bucket}`);
      console.log(`CacheControl: ${metadata.cacheControl}`);
      console.log(`ComponentCount: ${metadata.componentCount}`);
      console.log(`ContentDisposition: ${metadata.contentDisposition}`);
      console.log(`ContentEncoding: ${metadata.contentEncoding}`);
      console.log(`ContentLanguage: ${metadata.contentLanguage}`);
      console.log(`ContentType: ${metadata.contentType}`);
      console.log(`CustomTime: ${metadata.customTime}`);
      console.log(`Crc32c: ${metadata.crc32c}`);
      console.log(`ETag: ${metadata.etag}`);
      console.log(`Generation: ${metadata.generation}`);
      console.log(`Id: ${metadata.id}`);
      console.log(`KmsKeyName: ${metadata.kmsKeyName}`);
      console.log(`Md5Hash: ${metadata.md5Hash}`);
      console.log(`MediaLink: ${metadata.[mediaLink](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/filemetadata.html)}`);
      console.log(`Metageneration: ${metadata.metageneration}`);
      console.log(`Name: ${metadata.name}`);
      console.log(`Size: ${metadata.size}`);
      console.log(`StorageClass: ${metadata.storageClass}`);
      console.log(`TimeCreated: ${new Date(metadata.timeCreated)}`);
      console.log(`Last Metadata Update: ${new Date(metadata.updated)}`);
      console.log(`TurboReplication: ${metadata.rpo}`);
      console.log(
        `temporaryHold: ${metadata.temporaryHold ? 'enabled' : 'disabled'}`
      );
      console.log(
        `eventBasedHold: ${metadata.eventBasedHold ? 'enabled' : 'disabled'}`
      );
      if (metadata.[retentionExpirationTime](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/filemetadata.html)) {
        console.log(
          `retentionExpirationTime: ${new Date(metadata.[retentionExpirationTime](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/filemetadata.html))}`
        );
      }
      if (metadata.metadata) {
        console.log('\n\n\nUser metadata:');
        for (const key in metadata.metadata) {
          console.log(`${key}=${metadata.metadata[key]}`);
        }
      }
    }
    
    getMetadata().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

To view an object's retention configuration, follow the instructions for displaying a object's metadata and look for the retention field in the response. 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * List object metadata.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $objectName The name of your Cloud Storage object.
     *        (e.g. 'my-object')
     */
    function object_metadata(string $bucketName, string $objectName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
        $object = $bucket->object($objectName);
        $info = $object->info();
        if (isset($info['name'])) {
            printf('Blob: %s' . PHP_EOL, $info['name']);
        }
        if (isset($info['bucket'])) {
            printf('Bucket: %s' . PHP_EOL, $info['bucket']);
        }
        if (isset($info['storageClass'])) {
            printf('Storage class: %s' . PHP_EOL, $info['storageClass']);
        }
        if (isset($info['id'])) {
            printf('ID: %s' . PHP_EOL, $info['id']);
        }
        if (isset($info['size'])) {
            printf('Size: %s' . PHP_EOL, $info['size']);
        }
        if (isset($info['updated'])) {
            printf('Updated: %s' . PHP_EOL, $info['updated']);
        }
        if (isset($info['generation'])) {
            printf('Generation: %s' . PHP_EOL, $info['generation']);
        }
        if (isset($info['metageneration'])) {
            printf('Metageneration: %s' . PHP_EOL, $info['metageneration']);
        }
        if (isset($info['etag'])) {
            printf('Etag: %s' . PHP_EOL, $info['etag']);
        }
        if (isset($info['crc32c'])) {
            printf('Crc32c: %s' . PHP_EOL, $info['crc32c']);
        }
        if (isset($info['md5Hash'])) {
            printf('MD5 Hash: %s' . PHP_EOL, $info['md5Hash']);
        }
        if (isset($info['contentType'])) {
            printf('Content-type: %s' . PHP_EOL, $info['contentType']);
        }
        if (isset($info['temporaryHold'])) {
            printf('Temporary hold: %s' . PHP_EOL, ($info['temporaryHold'] ? 'enabled' : 'disabled'));
        }
        if (isset($info['eventBasedHold'])) {
            printf('Event-based hold: %s' . PHP_EOL, ($info['eventBasedHold'] ? 'enabled' : 'disabled'));
        }
        if (isset($info['retentionExpirationTime'])) {
            printf('Retention Expiration Time: %s' . PHP_EOL, $info['retentionExpirationTime']);
        }
        if (isset($info['retention'])) {
            printf('Retention mode: %s' . PHP_EOL, $info['retention']['mode']);
            printf('Retain until time is: %s' . PHP_EOL, $info['retention']['retainUntilTime']);
        }
        if (isset($info['customTime'])) {
            printf('Custom Time: %s' . PHP_EOL, $info['customTime']);
        }
        if (isset($info['metadata'])) {
            printf('Metadata: %s' . PHP_EOL, print_r($info['metadata'], true));
        }
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

To view an object's retention configuration, follow the instructions for displaying a object's metadata and look for the retention field in the response. 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def blob_metadata(bucket_name, blob_name):
        """Prints out a blob's metadata."""
        # bucket_name = 'your-bucket-name'
        # blob_name = 'your-object-name'
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
    
        # Retrieve a blob, and its metadata, from Google Cloud Storage.
        # Note that `get_blob` differs from `Bucket.blob`, which does not
        # make an HTTP request.
        blob = bucket.[get_blob](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_get_blob)(blob_name)
    
        print(f"Blob: {blob.name}")
        print(f"Blob finalization: {blob.[finalized_time](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_finalized_time)}")
        print(f"Bucket: {blob.bucket.name}")
        print(f"Storage class: {blob.storage_class}")
        print(f"ID: {blob.id}")
        print(f"Size: {blob.[size](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_size)} bytes")
        print(f"Updated: {blob.updated}")
        print(f"Generation: {blob.generation}")
        print(f"Metageneration: {blob.metageneration}")
        print(f"Etag: {blob.etag}")
        print(f"Owner: {blob.owner}")
        print(f"Component count: {blob.[component_count](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_component_count)}")
        print(f"Crc32c: {blob.[crc32c](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_crc32c)}")
        print(f"md5_hash: {blob.[md5_hash](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_md5_hash)}")
        print(f"Cache-control: {blob.[cache_control](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_cache_control)}")
        print(f"Content-type: {blob.[content_type](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_content_type)}")
        print(f"Content-disposition: {blob.[content_disposition](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_content_disposition)}")
        print(f"Content-encoding: {blob.[content_encoding](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_content_encoding)}")
        print(f"Content-language: {blob.[content_language](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_content_language)}")
        print(f"Metadata: {blob.[metadata](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_metadata)}")
        print(f"Medialink: {blob.[media_link](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_media_link)}")
        print(f"Custom Time: {blob.[custom_time](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_custom_time)}")
        print("Temporary hold: ", "enabled" if blob.[temporary_hold](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_temporary_hold) else "disabled")
        print(
            "Event based hold: ",
            "enabled" if blob.[event_based_hold](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_event_based_hold) else "disabled",
        )
        print(f"Retention mode: {blob.[retention](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_retention).[mode](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Retention.html#google_cloud_storage_blob_Retention_mode)}")
        print(f"Retention retain until time: {blob.[retention](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_retention).[retain_until_time](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Retention.html#google_cloud_storage_blob_Retention_retain_until_time)}")
        if blob.retention_expiration_time:
            print(
                f"retentionExpirationTime: {blob.retention_expiration_time}"
            )
    
    

### Rust

To view an object's retention configuration, follow the instructions for displaying a object's metadata and look for the retention field in the response. 
    
    
    use google_cloud_storage::client::StorageControl;
    
    pub async fn sample(client: &StorageControl, bucket_id: &str) -> anyhow::Result<()> {
        const NAME: &str = "object-to-read";
        let object = client
            .get_object()
            .set_bucket(format!("projects/_/buckets/{bucket_id}"))
            .set_object(NAME)
            .send()
            .await?;
    
        let object_metadata = object.metadata;
        println!(
            "successfully retrieved object {NAME} metadata in bucket {bucket_id}: {:?}",
            object_metadata
        );
        Ok(())
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the JSON API with a [`GET` Object](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/get) request that includes the `retention` field:
         
         curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/OBJECT_NAME?fields=retention"

Where:

     * `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.
     * `OBJECT_NAME` is the name of the relevant object. For example, `kitten.png`.



### XML API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the XML API with a [`GET` Object](https://docs.cloud.google.com/storage/docs/xml-api/get-object-retention) request scoped to `?retention`:
         
         curl -X GET \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storage.googleapis.com/BUCKET_NAME/OBJECT_NAME?retention"

Where:

     * `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.
     * `OBJECT_NAME` is the name of the relevant object. For example, `kitten.png`.



## What's next

  * Learn more about [retention configurations](https://docs.cloud.google.com/storage/docs/object-lock).
  * Learn about other [features that protect your Cloud Storage data](https://docs.cloud.google.com/storage/docs/control-data-lifecycles).
  * Learn about [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle), which can automatically delete files once they reach their retention period.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
