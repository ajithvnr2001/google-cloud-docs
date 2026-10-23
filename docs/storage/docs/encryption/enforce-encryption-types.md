---
url: https://docs.cloud.google.com/storage/docs/encryption/enforce-encryption-types/
title: Enforce or restrict the encryption types for a bucket \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:08:29.684840+00:00
---

# Enforce or restrict the encryption types for a bucket  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/encryption/enforce-encryption-types/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Enforce or restrict the encryption types for a bucket Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure which encryption methods are allowed or restricted for new objects in a Cloud Storage bucket. You can configure a bucket to enforce or restrict the use of standard encryption (Google default encryption), customer-managed encryption keys (CMEK), or customer-supplied encryption keys (CSEK) for any new objects that are created within the bucket.

For example, to help meet your compliance requirements about encryption key management, you can require that all new objects are encrypted with either standard encryption or CMEK, and restrict the use of customer-supplied encryption keys.

For more information about the encryption methods that are available, see [Data encryption options](https://docs.cloud.google.com/storage/docs/encryption).

Cloud Storage enforces the encryption configuration for all actions that create a new object, such as uploading an object, copying an object, composing objects, and restoring a soft-deleted object.

## Before you begin

To get the permissions that you need to configure encryption enforcement for a bucket, ask your administrator to grant you the [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) IAM role on bucket. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to configure encryption enforcement for a bucket. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to configure encryption enforcement for a bucket:

  * Set the configuration when creating a new bucket: `storage.buckets.create`
  * Update the configuration for an existing bucket: `storage.buckets.update`
  * If you use the Google Cloud console to perform the steps on this page: 
    * `storage.buckets.get`
    * `storage.buckets.list`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a bucket that enforces encryption types

You can specify the encryption methods that are allowed or restricted for the objects in a bucket when you [create a new bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).

If you [set a default Cloud KMS key](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys) for the bucket, then you must also allow encryption using CMEKs or customer-supplied encryption keys.

###  Console 

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click add_box **Create**.
  3. On the **Create a bucket** page, enter your bucket information. After each of the following steps, click **Continue** to proceed to the next step:

     1. In the **Get started** section, do the following:

        * Enter a globally unique name that meets the [bucket name requirements](https://docs.cloud.google.com/storage/docs/buckets#naming).

        * To add a [bucket label](https://docs.cloud.google.com/storage/docs/tags-and-labels#bucket-labels), click the expand_more expander arrow to expand the **Labels** section, click _add_box_ **Add label** , and specify a `key` and a `value` for your label.

     2. In the **Choose where to store your data** section, do the following:

        1. Select a [Location type](https://docs.cloud.google.com/storage/docs/locations).

        2. Use the location type's drop-down menu to select a [**Location**](https://docs.cloud.google.com/storage/docs/locations#available-locations) where object data within your bucket will be permanently stored.

           * If you select the [dual-region](https://docs.cloud.google.com/storage/docs/locations#location-dr) location type, you can also choose to enable [turbo replication](https://docs.cloud.google.com/storage/docs/availability-durability#turbo-replication) by using the relevant checkbox.

        3. To set up [cross-bucket replication](https://docs.cloud.google.com/storage/docs/availability-durability#cross-bucket-replication), select **Add cross-bucket replication via Storage Transfer Service** and follow the steps:

#### Set up cross-bucket replication

           1. In the **Bucket** menu, select a bucket.
           2. In the **Replication settings** section, click **Configure** to configure settings for the replication job.

The **Configure cross-bucket replication** pane appears.

              * To filter objects to replicate by object name prefix, enter a prefix with which you want to include or exclude objects, then click add **Add a prefix**.
              * To set a storage class for the replicated objects, select a storage class from the **Storage class** menu. If you skip this step, the replicated objects will use the destination bucket's storage class by default.
              * Click **Done**.

     3. In the **Choose how to store your data** section, do the following:

        1. Select a [default storage class](https://docs.cloud.google.com/storage/docs/storage-classes) for the bucket or [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass) for automatic storage class management of your bucket's data.

        2. In the **Optimize storage for data-intensive workloads** section, do the following:

           * To enable [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview), select **Enable Hierarchical namespace on this bucket**.

**Note:** Hierarchical namespace can only be enabled when you create the bucket. You can't change this setting after you create the bucket.

           * To enable [Rapid Cache](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache), select **Enable Rapid Cache** and follow the steps: 
             1. To create caches, click **Configure**.

             2. In the **Configure cache settings** dialog that appears, click the drop-down arrow next to the listed regions and select the zones where you want to create caches.

             3. Click **Done**.

**Note:** [Additional permissions](https://docs.cloud.google.com/storage/docs/rapid/use-rapid-cache#before-you-begin) are required to enable Rapid Cache.

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

###  gcloud 

  1. Create a JSON file that contains the following information:
         
         {
           "gmekEnforcement": {"restrictionMode": "STANDARD_ENCRYPTION_RESTRICTION_MODE"},
           "cmekEnforcement": {"restrictionMode": "CMEK_RESTRICTION_MODE"},
           "csekEnforcement": {"restrictionMode": "CSEK_RESTRICTION_MODE"}
         }

Replace the following:

     * `STANDARD_ENCRYPTION_RESTRICTION_MODE`: Whether encryption using standard encryption (Google default encryption) is allowed when creating objects in this bucket. The following values are supported: 
       * `NotRestricted`: new objects can use standard encryption.
       * `FullyRestricted`: new objects can't use standard encryption.
     * `CMEK_RESTRICTION_MODE`: Whether encryption using CMEKs is allowed when creating objects in this bucket. The following values are supported: 
       * `NotRestricted`: new objects can use CMEKs.
       * `FullyRestricted`: new objects can't use CMEKs.
     * `CSEK_RESTRICTION_MODE`: Whether encryption using customer-supplied encryption keys is allowed when creating objects in this bucket. The following values are supported: 
       * `NotRestricted`: new objects can use customer-supplied encryption keys.
       * `FullyRestricted`: new objects can't use customer-supplied encryption keys.

You must allow at least one encryption type. If you omit the enforcement configuration for a specific encryption type, then that encryption type is allowed by default.

  2. Use the [`gcloud storage buckets create`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/create) command with the `--encryption-enforcement-file` flag:
         
         gcloud storage buckets create gs://BUCKET_NAME \
           --encryption-enforcement-file=ENCRYPTION_ENFORCEMENT_FILE

Replace the following:

     * `BUCKET_NAME`: the name of the bucket.
     * `ENCRYPTION_ENFORCEMENT_FILE`: the path to the JSON file that you created in the previous step.



### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& project_id,
       std::string const& bucket_name) {
      auto create_bucket = [&](std::string const& name,
                               gcs::BucketEncryption encryption) {
        StatusOr<gcs::BucketMetadata> bucket = client.CreateBucketForProject(
            name, project_id, gcs::BucketMetadata().set_encryption(encryption));
        if (!bucket) throw std::move(bucket).status();
        return bucket;
      };
    
      // Example 1: Enforce GMEK Only
      gcs::BucketEncryption gmek_encryption;
      gmek_encryption.google_managed_encryption_enforcement_config
          .restriction_mode = "NotRestricted";
      gmek_encryption.customer_managed_encryption_enforcement_config
          .restriction_mode = "FullyRestricted";
      gmek_encryption.customer_supplied_encryption_enforcement_config
          .restriction_mode = "FullyRestricted";
      std::cout << "Bucket "
                << create_bucket("g-" + bucket_name, gmek_encryption)->name()
                << " created with GMEK-only enforcement policy.\n";
    
      // In GCS, a single project cannot create or delete buckets more often than
      // once every two seconds. We pause to avoid rate limiting.
      std::this_thread::sleep_for(std::chrono::seconds(2));
    
      // Example 2: Enforce CMEK Only
      gcs::BucketEncryption cmek_encryption;
      cmek_encryption.google_managed_encryption_enforcement_config
          .restriction_mode = "FullyRestricted";
      cmek_encryption.customer_managed_encryption_enforcement_config
          .restriction_mode = "NotRestricted";
      cmek_encryption.customer_supplied_encryption_enforcement_config
          .restriction_mode = "FullyRestricted";
      std::cout << "Bucket "
                << create_bucket("c-" + bucket_name, cmek_encryption)->name()
                << " created with CMEK-only enforcement policy.\n";
    
      // In GCS, a single project cannot create or delete buckets more often than
      // once every two seconds. We pause to avoid rate limiting.
      std::this_thread::sleep_for(std::chrono::seconds(2));
    
      // Example 3: Restrict CSEK (Ransomware Protection)
      gcs::BucketEncryption csek_encryption;
      csek_encryption.customer_supplied_encryption_enforcement_config
          .restriction_mode = "FullyRestricted";
      std::cout << "Bucket "
                << create_bucket("rc-" + bucket_name, csek_encryption)->name()
                << " created with a policy to restrict CSEK.\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using Google.Apis.Storage.v1.Data;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class BucketSetEncryptionEnforcementConfigSample
    {
        /// <summary>
        /// Set the encryption enforcement configuration for a bucket.
        /// </summary>
        /// <param name="bucketName">The name of the bucket.</param>
        /// <param name="kmsKeyName">
        /// The full resource name of the Cloud KMS key (CMEK). 
        /// Required if <paramref name="enforceCmek"/> is true.
        /// </param>
        /// <param name="enforceCmek">If true, enforces Customer-Managed Encryption Key.</param>
        /// <param name="enforceGmek">If true, enforces Google-Managed Encryption Key.</param>
        /// <param name="enforceCsek">If true, enforces Customer-Supplied Encryption Key.</param>
        public Bucket.EncryptionData SetBucketEncryptionEnforcementConfig(
            string bucketName = "your-unique-bucket-name",
            string kmsKeyName = null,
            bool enforceCmek = false,
            bool enforceGmek = false,
            bool enforceCsek = false)
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var bucket = storage.GetBucket(bucketName);
    
            if (bucket.Encryption == null)
            {
                bucket.Encryption = new Bucket.EncryptionData();
            }
    
            if (!string.IsNullOrEmpty(kmsKeyName))
            {
                bucket.Encryption.DefaultKmsKeyName = kmsKeyName;
                Console.WriteLine($"Default Key Set: {kmsKeyName}");
            }
            else
            {
                bucket.Encryption.DefaultKmsKeyName = null;
                Console.WriteLine("Default Key Set: None");
            }
    
            string cmek = (enforceGmek || enforceCsek) ? "FullyRestricted" : "NotRestricted";
            string gmek = (enforceCmek || enforceCsek) ? "FullyRestricted" : "NotRestricted";
            string csek = (enforceCmek || enforceGmek) ? "FullyRestricted" : "NotRestricted";
    
            string message = enforceCmek ? "CMEK-only enforcement policy"
                : enforceGmek ? "GMEK-only enforcement policy"
                : enforceCsek ? "CSEK-only enforcement policy"
                : "no encryption enforcement policy";
    
            bucket.Encryption.CustomerManagedEncryptionEnforcementConfig = new Bucket.EncryptionData.CustomerManagedEncryptionEnforcementConfigData { RestrictionMode = cmek };
            bucket.Encryption.CustomerSuppliedEncryptionEnforcementConfig = new Bucket.EncryptionData.CustomerSuppliedEncryptionEnforcementConfigData { RestrictionMode = csek };
            bucket.Encryption.GoogleManagedEncryptionEnforcementConfig = new Bucket.EncryptionData.GoogleManagedEncryptionEnforcementConfigData { RestrictionMode = gmek };
    
            if (message != null)
            {
                Console.WriteLine($"Bucket {bucketName} updated with {message}");
            }
    
            var updatedBucket = storage.UpdateBucket(bucket);
            return updatedBucket.Encryption;
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
    
    // setBucketEncryptionEnforcementConfig sets a bucket's encryption enforcement configuration.
    func setBucketEncryptionEnforcementConfig(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), projectID, bucketName string) error {
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
    
    	bucket := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucketName)
    	if err := bucket.[Create](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Create)(ctx, projectID, &storage.[BucketAttrs](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketAttrs){
    		GoogleManagedEncryptionEnforcementConfig: &storage.[EncryptionEnforcementConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_EncryptionEnforcementConfig){
    			RestrictionMode: storage.[FullyRestricted](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_NotRestricted_FullyRestricted),
    		},
    		CustomerManagedEncryptionEnforcementConfig: &storage.[EncryptionEnforcementConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_EncryptionEnforcementConfig){
    			RestrictionMode: storage.[NotRestricted](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_NotRestricted_FullyRestricted),
    		},
    		CustomerSuppliedEncryptionEnforcementConfig: &storage.[EncryptionEnforcementConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_EncryptionEnforcementConfig){
    			RestrictionMode: storage.[FullyRestricted](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_NotRestricted_FullyRestricted),
    		},
    	}); err != nil {
    		return fmt.Errorf("Bucket(%q).Create: %w", bucketName, err)
    	}
    	fmt.Fprintf(w, "Bucket %v encryption enforcement policies set.\n", bucketName)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html);
    import com.google.cloud.storage.[BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html).[CustomerManagedEncryptionEnforcementConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.CustomerManagedEncryptionEnforcementConfig.html);
    import com.google.cloud.storage.[BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html).[CustomerSuppliedEncryptionEnforcementConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.CustomerSuppliedEncryptionEnforcementConfig.html);
    import com.google.cloud.storage.[BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html).[EncryptionEnforcementRestrictionMode](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.EncryptionEnforcementRestrictionMode.html);
    import com.google.cloud.storage.[BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html).[GoogleManagedEncryptionEnforcementConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.GoogleManagedEncryptionEnforcementConfig.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class SetBucketEncryptionEnforcementConfig {
      public static void setBucketEncryptionEnforcementConfig(String projectId, String bucketName)
          throws Exception {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        try ([Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage =
            [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)()) {
    
          // Example 1: Enforce GMEK Only
          setGmekEnforcedPolicy(storage, "g-" + bucketName);
    
          // Example 2: Enforce CMEK Only
          setCmekEnforcedPolicy(storage, "c-" + bucketName);
    
          // Example 3: Restrict CSEK (Ransomware Protection)
          restrictCsekPolicy(storage, "rc-" + bucketName);
        }
      }
    
      public static void setGmekEnforcedPolicy([Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage, String bucketName) {
        [GoogleManagedEncryptionEnforcementConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.GoogleManagedEncryptionEnforcementConfig.html) gmekConfig =
            [GoogleManagedEncryptionEnforcementConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.GoogleManagedEncryptionEnforcementConfig.html).of(
                [EncryptionEnforcementRestrictionMode](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.EncryptionEnforcementRestrictionMode.html).NOT_RESTRICTED);
        [CustomerManagedEncryptionEnforcementConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.CustomerManagedEncryptionEnforcementConfig.html) cmekConfig =
            [CustomerManagedEncryptionEnforcementConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.CustomerManagedEncryptionEnforcementConfig.html).of(
                [EncryptionEnforcementRestrictionMode](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.EncryptionEnforcementRestrictionMode.html).FULLY_RESTRICTED);
        [CustomerSuppliedEncryptionEnforcementConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.CustomerSuppliedEncryptionEnforcementConfig.html) csekConfig =
            [CustomerSuppliedEncryptionEnforcementConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.CustomerSuppliedEncryptionEnforcementConfig.html).of(
                [EncryptionEnforcementRestrictionMode](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.EncryptionEnforcementRestrictionMode.html).FULLY_RESTRICTED);
    
        [BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html) bucketInfo =
            [BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html).newBuilder(bucketName)
                .setGoogleManagedEncryptionEnforcementConfig(gmekConfig)
                .setCustomerManagedEncryptionEnforcementConfig(cmekConfig)
                .setCustomerSuppliedEncryptionEnforcementConfig(csekConfig)
                .build();
    
        [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket = storage.[create](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_create_com_google_cloud_storage_BlobInfo_byte___com_google_cloud_storage_Storage_BlobTargetOption____)(bucketInfo);
        System.out.println(
            "Bucket " + bucket.getName() + " created with GMEK-only enforcement policy.");
      }
    
      public static void setCmekEnforcedPolicy([Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage, String bucketName) {
        [GoogleManagedEncryptionEnforcementConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.GoogleManagedEncryptionEnforcementConfig.html) gmekConfig =
            [GoogleManagedEncryptionEnforcementConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.GoogleManagedEncryptionEnforcementConfig.html).of(
                [EncryptionEnforcementRestrictionMode](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.EncryptionEnforcementRestrictionMode.html).FULLY_RESTRICTED);
        [CustomerManagedEncryptionEnforcementConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.CustomerManagedEncryptionEnforcementConfig.html) cmekConfig =
            [CustomerManagedEncryptionEnforcementConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.CustomerManagedEncryptionEnforcementConfig.html).of(
                [EncryptionEnforcementRestrictionMode](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.EncryptionEnforcementRestrictionMode.html).NOT_RESTRICTED);
        [CustomerSuppliedEncryptionEnforcementConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.CustomerSuppliedEncryptionEnforcementConfig.html) csekConfig =
            [CustomerSuppliedEncryptionEnforcementConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.CustomerSuppliedEncryptionEnforcementConfig.html).of(
                [EncryptionEnforcementRestrictionMode](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.EncryptionEnforcementRestrictionMode.html).FULLY_RESTRICTED);
    
        [BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html) bucketInfo =
            [BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html).newBuilder(bucketName)
                .setGoogleManagedEncryptionEnforcementConfig(gmekConfig)
                .setCustomerManagedEncryptionEnforcementConfig(cmekConfig)
                .setCustomerSuppliedEncryptionEnforcementConfig(csekConfig)
                .build();
    
        [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket = storage.[create](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_create_com_google_cloud_storage_BlobInfo_byte___com_google_cloud_storage_Storage_BlobTargetOption____)(bucketInfo);
        System.out.println(
            "Bucket " + bucket.getName() + " created with CMEK-only enforcement policy.");
      }
    
      public static void restrictCsekPolicy([Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage, String bucketName) {
        [CustomerSuppliedEncryptionEnforcementConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.CustomerSuppliedEncryptionEnforcementConfig.html) csekConfig =
            [CustomerSuppliedEncryptionEnforcementConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.CustomerSuppliedEncryptionEnforcementConfig.html).of(
                [EncryptionEnforcementRestrictionMode](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.EncryptionEnforcementRestrictionMode.html).FULLY_RESTRICTED);
    
        [BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html) bucketInfo =
            [BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html).newBuilder(bucketName)
                .setCustomerSuppliedEncryptionEnforcementConfig(csekConfig)
                .build();
    
        [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket = storage.[create](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_create_com_google_cloud_storage_BlobInfo_byte___com_google_cloud_storage_Storage_BlobTargetOption____)(bucketInfo);
        System.out.println("Bucket " + bucket.getName() + " created with a policy to restrict CSEK.");
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
    
    // The name of the KMS key to be used as the default
    // const defaultKmsKeyName = 'my-key';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function setBucketEncryptionEnforcementConfig() {
      const options = {
        encryption: {
          defaultKmsKeyName,
          googleManagedEncryptionEnforcementConfig: {
            restrictionMode: 'FullyRestricted',
          },
          customerSuppliedEncryptionEnforcementConfig: {
            restrictionMode: 'FullyRestricted',
          },
          customerManagedEncryptionEnforcementConfig: {
            restrictionMode: 'NotRestricted',
          },
        },
      };
    
      const [metadata] = await storage.bucket(bucketName).setMetadata(options);
    
      console.log(
        `Encryption enforcement configuration updated for bucket ${bucketName}.`
      );
      const enc = metadata.encryption;
      if (enc) {
        console.log(`Default KMS Key: ${enc.defaultKmsKeyName}`);
    
        const logEnforcement = (label, config) => {
          if (config) {
            console.log(`${label}:`);
            console.log(`  Mode: ${config.restrictionMode}`);
            console.log(`  Effective: ${config.effectiveTime}`);
          }
        };
    
        logEnforcement(
          'Google Managed (GMEK) Enforcement',
          enc.googleManagedEncryptionEnforcementConfig
        );
        logEnforcement(
          'Customer Managed (CMEK) Enforcement',
          enc.customerManagedEncryptionEnforcementConfig
        );
        logEnforcement(
          'Customer Supplied (CSEK) Enforcement',
          enc.customerSuppliedEncryptionEnforcementConfig
        );
      }
    }
    
    setBucketEncryptionEnforcementConfig().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Creates a bucket with specific encryption enforcement (e.g., CMEK-only).
     *
     * @param string $bucketName The ID of your GCS bucket (e.g. "my-bucket").
     * @param string $kmsKeyName The name of the KMS key to be used as the default (e.g. "projects/my-project/...").
     */
    function set_bucket_encryption_enforcement_config(string $bucketName, string $kmsKeyName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
    
        // This configuration enforces that all objects uploaded to the bucket
        // must use Customer Managed Encryption Keys (CMEK).
        $options = [
            'encryption' => [
                'defaultKmsKeyName' => $kmsKeyName,
                'googleManagedEncryptionEnforcementConfig' => [
                    'restrictionMode' => 'FullyRestricted',
                ],
                'customerSuppliedEncryptionEnforcementConfig' => [
                    'restrictionMode' => 'FullyRestricted',
                ],
                'customerManagedEncryptionEnforcementConfig' => [
                    'restrictionMode' => 'NotRestricted',
                ],
            ],
        ];
        $storage->createBucket($bucketName, $options);
    
        printf('Bucket %s created with encryption enforcement configuration.' . PHP_EOL, $bucketName);
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    from google.cloud.storage.bucket import [EncryptionEnforcementConfig](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.EncryptionEnforcementConfig.html)
    
    
    def set_bucket_encryption_enforcement_config(bucket_name):
        """Creates a bucket with encryption enforcement configuration."""
        # The ID of your GCS bucket
        # bucket_name = "your-unique-bucket-name"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
    
        # Setting restriction_mode to "FullyRestricted" for Google-managed encryption (GMEK)
        # means objects cannot be created using the default Google-managed keys.
        bucket.[encryption](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_encryption).[google_managed_encryption_enforcement_config](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.BucketEncryption.html#google_cloud_storage_bucket_BucketEncryption_google_managed_encryption_enforcement_config) = (
            EncryptionEnforcementConfig(restriction_mode="FullyRestricted")
        )
    
        # Setting restriction_mode to "NotRestricted" for Customer-managed encryption (CMEK)
        # ensures that objects ARE permitted to be created using Cloud KMS keys.
        bucket.[encryption](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_encryption).[customer_managed_encryption_enforcement_config](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.BucketEncryption.html#google_cloud_storage_bucket_BucketEncryption_customer_managed_encryption_enforcement_config) = (
            EncryptionEnforcementConfig(restriction_mode="NotRestricted")
        )
    
        # Setting restriction_mode to "FullyRestricted" for Customer-supplied encryption (CSEK)
        # prevents objects from being created using raw, client-side provided keys.
        bucket.[encryption](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_encryption).[customer_supplied_encryption_enforcement_config](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.BucketEncryption.html#google_cloud_storage_bucket_BucketEncryption_customer_supplied_encryption_enforcement_config) = (
            EncryptionEnforcementConfig(restriction_mode="FullyRestricted")
        )
    
        bucket.create()
    
        print(f"Created bucket {bucket.name} with Encryption Enforcement Config.")
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def set_bucket_encryption_enforcement_config bucket_name:
      # The ID to give your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
    
      customer_managed_config = { restriction_mode: "NotRestricted" }
      customer_supplied_config = { restriction_mode: "FullyRestricted" }
      google_managed_config = { restriction_mode: "FullyRestricted" }
    
      bucket = storage.[create_bucket](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Project.html) bucket_name do |b|
        b.[customer_managed_encryption_enforcement_config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) = customer_managed_config
        b.[customer_supplied_encryption_enforcement_config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) = customer_supplied_config
        b.[google_managed_encryption_enforcement_config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) = google_managed_config
      end
      puts "Created bucket #{bucket.name} with Encryption Enforcement Config."
    end

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the settings for the bucket. For a complete list of settings, see the [Buckets: Insert](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/insert) documentation. The following settings define only the bucket name and encryption:
         
         {
           "name": "BUCKET_NAME",
           "encryption": {
             "googleManagedEncryptionEnforcementConfig": {
               "restrictionMode": "STANDARD_ENCRYPTION_RESTRICTION_MODE"
             },
             "customerManagedEncryptionEnforcementConfig": {
               "restrictionMode": "CMEK_RESTRICTION_MODE"
             },
             "customerSuppliedEncryptionEnforcementConfig": {
               "restrictionMode": "CSEK_RESTRICTION_MODE"
             }
           }
         }

Replace the following:

     * `BUCKET_NAME`: The name of the bucket.
     * `STANDARD_ENCRYPTION_RESTRICTION_MODE`: Whether encryption using standard encryption (Google default encryption) is allowed when creating objects in this bucket. The following values are supported: 
       * `NotRestricted`: new objects can use standard encryption.
       * `FullyRestricted`: new objects can't use standard encryption.
     * `CMEK_RESTRICTION_MODE`: Whether encryption using CMEKs is allowed when creating objects in this bucket. The following values are supported: 
       * `NotRestricted`: new objects can use CMEKs.
       * `FullyRestricted`: new objects can't use CMEKs.
     * `CSEK_RESTRICTION_MODE`: Whether encryption using customer-supplied encryption keys is allowed when creating objects in this bucket. The following values are supported: 
       * `NotRestricted`: new objects can use customer-supplied encryption keys.
       * `FullyRestricted`: new objects can't use customer-supplied encryption keys.

You must allow at least one encryption type. If you omit the enforcement configuration for a specific encryption type, then that encryption type is allowed by default.

  3. Use `cURL` to call the JSON API with a [`POST` Bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/insert) request:
         
         curl -X POST --data-binary @JSON_FILE_NAME \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://storage.googleapis.com/storage/v1/b?project=PROJECT_ID"

Replace the following:

     * `JSON_FILE_NAME`: the path to the JSON file that you created in the previous step.
     * `PROJECT_ID`: the ID or number of the project for your bucket.



### XML API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create an XML file that contains the settings for the bucket. For a complete list of settings, see the [XML: Create a bucket](https://docs.cloud.google.com/storage/docs/xml-api/put-bucket-create) documentation. The following settings define only the encryption enforcement:
         
         <CreateBucketConfiguration>
           <EncryptionConfiguration>
             <GoogleManagedEncryptionEnforcement>
               <RestrictionMode>STANDARD_ENCRYPTION_RESTRICTION_MODE</RestrictionMode>
             </GoogleManagedEncryptionEnforcement>
             <CustomerManagedEncryptionEnforcement>
               <RestrictionMode>CMEK_RESTRICTION_MODE</RestrictionMode>
             </CustomerManagedEncryptionEnforcement>
             <CustomerSuppliedEncryptionEnforcement>
               <RestrictionMode>CSEK_RESTRICTION_MODE</RestrictionMode>
             </CustomerSuppliedEncryptionEnforcement>
           </EncryptionConfiguration>
         </CreateBucketConfiguration>

Replace the following:

     * `STANDARD_ENCRYPTION_RESTRICTION_MODE`: Whether encryption using standard encryption (Google default encryption) is allowed when creating objects in this bucket. The following values are supported: 
       * `NotRestricted`: new objects can use standard encryption.
       * `FullyRestricted`: new objects can't use standard encryption.
     * `CMEK_RESTRICTION_MODE`: Whether encryption using CMEKs is allowed when creating objects in this bucket. The following values are supported: 
       * `NotRestricted`: new objects can use CMEKs.
       * `FullyRestricted`: new objects can't use CMEKs.
     * `CSEK_RESTRICTION_MODE`: Whether encryption using customer-supplied encryption keys is allowed when creating objects in this bucket. The following values are supported: 
       * `NotRestricted`: new objects can use customer-supplied encryption keys.
       * `FullyRestricted`: new objects can't use customer-supplied encryption keys.

You must allow at least one encryption type. If you omit the enforcement configuration for a specific encryption type, then that encryption type is allowed by default.

  3. Use `cURL` to call the XML API with a [`PUT` Bucket](https://docs.cloud.google.com/storage/docs/xml-api/put-bucket-create) request:
         
         curl -X PUT --data-binary @XML_FILE_NAME \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "x-goog-project-id: PROJECT_ID" \
           "https://storage.googleapis.com/BUCKET_NAME"

Replace the following:

     * `XML_FILE_NAME`: the path to the XML file that you created in the previous step.
     * `PROJECT_ID`: the ID or number of the project for your bucket.
     * `BUCKET_NAME`: the name of the bucket.



## Update the encryption types that are allowed for a bucket

To update which encryption methods are allowed for new objects in an existing bucket, complete the following steps.

**Caution:** Updating a bucket's encryption enforcement configuration doesn't affect the encryption type of any objects that already exist in the bucket.

If the bucket has a default KMS key set, then you can't restrict both CMEK and customer-supplied encryption keys because that would prevent new objects from being created. Either allow CMEK or CSEK on such a bucket, or remove the [default Cloud KMS key](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys) from the bucket.

###  Console 

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket.

  3. Click the **Configuration** tab.

  4. In the **Protection** section, click edit **Edit encryption**.

  5. In the **Encryption enforcement rules** section, for **Key types** , select which encryption types to allow or restrict for new objects in the bucket.

  6. Click **Save**.




###  gcloud 

  1. Create a JSON file that contains the following information:
         
         {
           "gmekEnforcement": {"restrictionMode": "STANDARD_ENCRYPTION_RESTRICTION_MODE"},
           "cmekEnforcement": {"restrictionMode": "CMEK_RESTRICTION_MODE"},
           "csekEnforcement": {"restrictionMode": "CSEK_RESTRICTION_MODE"}
         }

Replace the following:

     * `STANDARD_ENCRYPTION_RESTRICTION_MODE`: Whether encryption using standard encryption (Google default encryption) is allowed when creating objects in this bucket. The following values are supported: 
       * `NotRestricted`: new objects can use standard encryption.
       * `FullyRestricted`: new objects can't use standard encryption.
     * `CMEK_RESTRICTION_MODE`: Whether encryption using CMEKs is allowed when creating objects in this bucket. The following values are supported: 
       * `NotRestricted`: new objects can use CMEKs.
       * `FullyRestricted`: new objects can't use CMEKs.
     * `CSEK_RESTRICTION_MODE`: Whether encryption using customer-supplied encryption keys is allowed when creating objects in this bucket. The following values are supported: 
       * `NotRestricted`: new objects can use customer-supplied encryption keys.
       * `FullyRestricted`: new objects can't use customer-supplied encryption keys.

You must allow at least one encryption type. If you omit an encryption type, the existing configuration is retained.

  2. Use the [`gcloud storage buckets update`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/update) command with the `--encryption-enforcement-file` flag:
         
         gcloud storage buckets update gs://BUCKET_NAME \
           --encryption-enforcement-file=ENCRYPTION_ENFORCEMENT_FILE

Replace the following:

     * `BUCKET_NAME`: the name of the bucket.
     * `ENCRYPTION_ENFORCEMENT_FILE`: the path to the JSON file that you created in the previous step.

It might take up to two minutes for the updated configuration to take effect.




### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name) {
      StatusOr<gcs::BucketMetadata> original =
          client.GetBucketMetadata(bucket_name);
    
      gcs::BucketMetadata updated_metadata = *original;
      gcs::BucketEncryption encryption;
      if (original->has_encryption()) {
        encryption = original->encryption();
      }
    
      // 1. Update a specific type (e.g., change GMEK to FullyRestricted)
      encryption.google_managed_encryption_enforcement_config.restriction_mode =
          "FullyRestricted";
      // 2. Remove a specific type (e.g., remove CMEK enforcement)
      encryption.customer_managed_encryption_enforcement_config.restriction_mode =
          "NotRestricted";
      // For the update, need to specify all three configs, so keeping this same
      // as before
      encryption.customer_supplied_encryption_enforcement_config
          .restriction_mode = "FullyRestricted";
    
      updated_metadata.set_encryption(encryption);
    
      StatusOr<gcs::BucketMetadata> updated =
          client.PatchBucket(bucket_name, *original, updated_metadata);
      if (!updated) throw std::move(updated).status();
    
      std::cout << "Encryption enforcement policy updated for bucket "
                << updated->name() << "\n"
                << "GMEK is now fully restricted, and CMEK enforcement has been "
                   "removed.\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using Google.Apis.Storage.v1.Data;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class BucketUpdateEncryptionEnforcementConfigSample
    {
        /// <summary>
        /// Updates the encryption enforcement configuration of the bucket.
        /// </summary>
        /// <param name="bucketName">The name of the bucket.</param>
        /// <param name="encryptionData">The encryption configuration for the bucket.</param>
        public Bucket.EncryptionData BucketUpdateEncryptionEnforcementConfig(string bucketName = "your-unique-bucket-name", Bucket.EncryptionData encryptionData = null)
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var bucket = storage.GetBucket(bucketName);
    
            if (bucket.Encryption is null
                || (bucket.Encryption.CustomerManagedEncryptionEnforcementConfig is null
                    && bucket.Encryption.CustomerSuppliedEncryptionEnforcementConfig is null
                    && bucket.Encryption.GoogleManagedEncryptionEnforcementConfig is null))
            {
                Console.WriteLine($"No Encryption Enforcement Configuration found for bucket {bucketName}");
                return bucket.Encryption;
            }
    
            bucket.Encryption = encryptionData;
            bucket = storage.UpdateBucket(bucket);
            Console.WriteLine($"The Encryption Enforcement Configuration has been updated for the bucket {bucketName}");
            return bucket.Encryption;
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
    
    // updateBucketEncryptionEnforcementConfig updates a bucket's encryption enforcement configuration.
    func updateBucketEncryptionEnforcementConfig(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucketName string) error {
    	// bucketName := "bucket-name"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*30)
    	defer cancel()
    
    	bucket := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucketName)
    	if _, err := bucket.Update(ctx, storage.[BucketAttrsToUpdate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketAttrsToUpdate){
    		GoogleManagedEncryptionEnforcementConfig: &storage.[EncryptionEnforcementConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_EncryptionEnforcementConfig){
    			RestrictionMode: storage.[NotRestricted](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_NotRestricted_FullyRestricted),
    		},
    		CustomerManagedEncryptionEnforcementConfig: &storage.[EncryptionEnforcementConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_EncryptionEnforcementConfig){
    			RestrictionMode: storage.[FullyRestricted](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_NotRestricted_FullyRestricted),
    		},
    		CustomerSuppliedEncryptionEnforcementConfig: &storage.[EncryptionEnforcementConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_EncryptionEnforcementConfig){
    			RestrictionMode: storage.[FullyRestricted](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_NotRestricted_FullyRestricted),
    		},
    	}); err != nil {
    		return fmt.Errorf("Bucket(%q).Update: %w", bucketName, err)
    	}
    	fmt.Fprintf(w, "Bucket %v encryption enforcement policies updated.\n", bucketName)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html).[CustomerManagedEncryptionEnforcementConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.CustomerManagedEncryptionEnforcementConfig.html);
    import com.google.cloud.storage.[BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html).[CustomerSuppliedEncryptionEnforcementConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.CustomerSuppliedEncryptionEnforcementConfig.html);
    import com.google.cloud.storage.[BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html).[EncryptionEnforcementRestrictionMode](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.EncryptionEnforcementRestrictionMode.html);
    import com.google.cloud.storage.[BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html).[GoogleManagedEncryptionEnforcementConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.GoogleManagedEncryptionEnforcementConfig.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class UpdateBucketEncryptionEnforcementConfig {
      public static void updateBucketEncryptionEnforcementConfig(String projectId, String bucketName)
          throws Exception {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket with CMEK and CSEK restricted
        // String bucketName = "your-unique-bucket-name";
    
        try ([Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage =
            [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)()) {
    
          [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket = storage.get(bucketName);
          if (bucket == null) {
            System.out.println("Bucket " + bucketName + " not found.");
            return;
          }
    
          // 1. Update a specific type (e.g., change GMEK to FULLY_RESTRICTED)
          [GoogleManagedEncryptionEnforcementConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.GoogleManagedEncryptionEnforcementConfig.html) newGmekConfig =
              [GoogleManagedEncryptionEnforcementConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.GoogleManagedEncryptionEnforcementConfig.html).of(
                  [EncryptionEnforcementRestrictionMode](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.EncryptionEnforcementRestrictionMode.html).FULLY_RESTRICTED);
    
          // 2. Remove a specific type (e.g., remove CMEK enforcement)
          [CustomerManagedEncryptionEnforcementConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.CustomerManagedEncryptionEnforcementConfig.html) newCmekConfig =
              [CustomerManagedEncryptionEnforcementConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.CustomerManagedEncryptionEnforcementConfig.html).of(
                  [EncryptionEnforcementRestrictionMode](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.EncryptionEnforcementRestrictionMode.html).NOT_RESTRICTED);
    
          // For the update, need to specify all three configs, so keeping this same as before
          [CustomerSuppliedEncryptionEnforcementConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.CustomerSuppliedEncryptionEnforcementConfig.html) sameCsekConfig =
              [CustomerSuppliedEncryptionEnforcementConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.CustomerSuppliedEncryptionEnforcementConfig.html).of(
                  [EncryptionEnforcementRestrictionMode](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.EncryptionEnforcementRestrictionMode.html).FULLY_RESTRICTED);
    
          bucket.[toBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html#com_google_cloud_storage_Bucket_toBuilder__)()
              .setGoogleManagedEncryptionEnforcementConfig(newGmekConfig)
              .setCustomerManagedEncryptionEnforcementConfig(newCmekConfig)
              .setCustomerSuppliedEncryptionEnforcementConfig(sameCsekConfig)
              .build()
              .update();
    
          System.out.println("Encryption enforcement policy updated for bucket " + bucketName);
          System.out.println("GMEK is now fully restricted, and CMEK enforcement has been removed.");
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
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function updateBucketEncryptionEnforcementConfig() {
      const bucket = storage.bucket(bucketName);
    
      // Update a specific encryption type's restriction mode
      // This partial update preserves other existing encryption settings.
      const updateOptions = {
        encryption: {
          googleManagedEncryptionEnforcementConfig: {
            restrictionMode: 'FullyRestricted',
          },
        },
      };
    
      await bucket.setMetadata(updateOptions);
      console.log(
        `Google-managed encryption enforcement set to FullyRestricted for ${bucketName}.`
      );
    
      // Remove all encryption enforcement configurations altogether
      // Setting these values to null removes the policies from the bucket metadata.
      const clearOptions = {
        encryption: {
          defaultKmsKeyName: null,
          googleManagedEncryptionEnforcementConfig: null,
          customerSuppliedEncryptionEnforcementConfig: null,
          customerManagedEncryptionEnforcementConfig: null,
        },
      };
    
      await bucket.setMetadata(clearOptions);
      console.log(
        `All encryption enforcement configurations removed from bucket ${bucketName}.`
      );
    }
    
    updateBucketEncryptionEnforcementConfig().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Updates or removes encryption enforcement configurations from a bucket.
     *
     * @param string $bucketName The ID of your GCS bucket (e.g. "my-bucket").
     */
    function update_bucket_encryption_enforcement_config(string $bucketName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
    
        // Update a specific encryption type's restriction mode
        // This partial update preserves other existing encryption settings.
        $updateOptions = [
            'encryption' => [
                'googleManagedEncryptionEnforcementConfig' => [
                    'restrictionMode' => 'FullyRestricted'
                ]
            ]
        ];
        $bucket->update($updateOptions);
        printf('Google-managed encryption enforcement set to FullyRestricted for %s.' . PHP_EOL, $bucketName);
    
        // Remove all encryption enforcement configurations altogether
        // Setting these values to null removes the policies from the bucket metadata.
        $clearOptions = [
            'encryption' => [
                'defaultKmsKeyName' => null,
                'googleManagedEncryptionEnforcementConfig' => null,
                'customerSuppliedEncryptionEnforcementConfig' => null,
                'customerManagedEncryptionEnforcementConfig' => null,
            ],
        ];
    
        $bucket->update($clearOptions);
        printf('All encryption enforcement configurations removed from bucket %s.' . PHP_EOL, $bucketName);
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    from google.cloud.storage.bucket import [EncryptionEnforcementConfig](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.EncryptionEnforcementConfig.html)
    
    
    def update_bucket_encryption_enforcement_config(bucket_name):
        """Updates the encryption enforcement policy for a bucket."""
        # The ID of your GCS bucket with GMEK and CSEK restricted
        # bucket_name = "your-unique-bucket-name"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[get_bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_get_bucket)(bucket_name)
    
        # Update a specific type (e.g., change GMEK to NotRestricted)
        bucket.[encryption](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_encryption).[google_managed_encryption_enforcement_config](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.BucketEncryption.html#google_cloud_storage_bucket_BucketEncryption_google_managed_encryption_enforcement_config) = (
            EncryptionEnforcementConfig(restriction_mode="NotRestricted")
        )
    
        # Update another type (e.g., change CMEK to FullyRestricted)
        bucket.[encryption](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_encryption).[customer_managed_encryption_enforcement_config](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.BucketEncryption.html#google_cloud_storage_bucket_BucketEncryption_customer_managed_encryption_enforcement_config) = (
            EncryptionEnforcementConfig(restriction_mode="FullyRestricted")
        )
    
        # Keeping CSEK unchanged
        bucket.[encryption](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_encryption).[customer_supplied_encryption_enforcement_config](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.BucketEncryption.html#google_cloud_storage_bucket_BucketEncryption_customer_supplied_encryption_enforcement_config) = (
            EncryptionEnforcementConfig(restriction_mode="FullyRestricted")
        )
    
        bucket.patch()
    
        print(f"Encryption enforcement policy updated for bucket {bucket.name}.")
    
        gmek = bucket.[encryption](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_encryption).[google_managed_encryption_enforcement_config](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.BucketEncryption.html#google_cloud_storage_bucket_BucketEncryption_google_managed_encryption_enforcement_config)
        cmek = bucket.[encryption](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_encryption).[customer_managed_encryption_enforcement_config](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.BucketEncryption.html#google_cloud_storage_bucket_BucketEncryption_customer_managed_encryption_enforcement_config)
        csek = bucket.[encryption](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_encryption).[customer_supplied_encryption_enforcement_config](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.BucketEncryption.html#google_cloud_storage_bucket_BucketEncryption_customer_supplied_encryption_enforcement_config)
    
        print(f"GMEK restriction mode: {gmek.[restriction_mode](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.EncryptionEnforcementConfig.html#google_cloud_storage_bucket_EncryptionEnforcementConfig_restriction_mode) if gmek else 'None'}")
        print(f"CMEK restriction mode: {cmek.[restriction_mode](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.EncryptionEnforcementConfig.html#google_cloud_storage_bucket_EncryptionEnforcementConfig_restriction_mode) if cmek else 'None'}")
        print(f"CSEK restriction mode: {csek.[restriction_mode](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.EncryptionEnforcementConfig.html#google_cloud_storage_bucket_EncryptionEnforcementConfig_restriction_mode) if csek else 'None'}")
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def update_bucket_encryption_enforcement_config bucket_name:
      # The ID to give your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket = storage.bucket bucket_name
      # Update a specific type (e.g., change GMEK to NotRestricted)
      new_config =  { restriction_mode: "NotRestricted" }
    
      bucket.update do |b|
        b.[google_managed_encryption_enforcement_config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) = new_config
      end
      puts "Updated google_managed_config to " \
           "#{bucket.[google_managed_encryption_enforcement_config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html).restriction_mode} " \
           "for bucket #{bucket.name}."
    end

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the following information:
         
         {
           "encryption": {
             "googleManagedEncryptionEnforcementConfig": {
               "restrictionMode": "STANDARD_ENCRYPTION_RESTRICTION_MODE"
             },
             "customerManagedEncryptionEnforcementConfig": {
               "restrictionMode": "CMEK_RESTRICTION_MODE"
             },
             "customerSuppliedEncryptionEnforcementConfig": {
               "restrictionMode": "CSEK_RESTRICTION_MODE"
             }
           }
         }

Replace the following:

     * `STANDARD_ENCRYPTION_RESTRICTION_MODE`: Whether encryption using standard encryption (Google default encryption) is allowed when creating objects in this bucket. The following values are supported: 
       * `NotRestricted`: new objects can use standard encryption.
       * `FullyRestricted`: new objects can't use standard encryption.
     * `CMEK_RESTRICTION_MODE`: Whether encryption using CMEKs is allowed when creating objects in this bucket. The following values are supported: 
       * `NotRestricted`: new objects can use CMEKs.
       * `FullyRestricted`: new objects can't use CMEKs.
     * `CSEK_RESTRICTION_MODE`: Whether encryption using customer-supplied encryption keys is allowed when creating objects in this bucket. The following values are supported: 
       * `NotRestricted`: new objects can use customer-supplied encryption keys.
       * `FullyRestricted`: new objects can't use customer-supplied encryption keys.

You must allow at least one encryption type. If you omit an encryption type, the existing configuration is retained.

  3. Use `cURL` to call the JSON API with a [`PATCH` Bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/patch) request:
         
         curl -X PATCH --data-binary @JSON_FILE_NAME \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME?fields=encryption"

Replace the following:

     * `JSON_FILE_NAME`: the path to the JSON file that you created in the previous step.
     * `BUCKET_NAME`: the name of the bucket.

It might take up to two minutes for the updated configuration to take effect.




### XML API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create an XML file that contains the encryption settings for the bucket. The following settings define only the encryption enforcement configuration.

**Caution:** The contents of the request body replace any existing settings, so include all values that you want to apply. For a complete list of encryption settings, see the [`EncryptionConfiguration` request body elements](https://docs.cloud.google.com/storage/docs/xml-api/put-bucket-metadata#encryptionconfig-body).
         
         <EncryptionConfiguration>
           <GoogleManagedEncryptionEnforcement>
             <RestrictionMode>STANDARD_ENCRYPTION_RESTRICTION_MODE</RestrictionMode>
           </GoogleManagedEncryptionEnforcement>
           <CustomerManagedEncryptionEnforcement>
             <RestrictionMode>CMEK_RESTRICTION_MODE</RestrictionMode>
           </CustomerManagedEncryptionEnforcement>
           <CustomerSuppliedEncryptionEnforcement>
             <RestrictionMode>CSEK_RESTRICTION_MODE</RestrictionMode>
           </CustomerSuppliedEncryptionEnforcement>
         </EncryptionConfiguration>

Replace the following:

     * `STANDARD_ENCRYPTION_RESTRICTION_MODE`: Whether encryption using standard encryption (Google default encryption) is allowed when creating objects in this bucket. The following values are supported: 
       * `NotRestricted`: new objects can use standard encryption.
       * `FullyRestricted`: new objects can't use standard encryption.
     * `CMEK_RESTRICTION_MODE`: Whether encryption using CMEKs is allowed when creating objects in this bucket. The following values are supported: 
       * `NotRestricted`: new objects can use CMEKs.
       * `FullyRestricted`: new objects can't use CMEKs.
     * `CSEK_RESTRICTION_MODE`: Whether encryption using customer-supplied encryption keys is allowed when creating objects in this bucket. The following values are supported: 
       * `NotRestricted`: new objects can use customer-supplied encryption keys.
       * `FullyRestricted`: new objects can't use customer-supplied encryption keys.

You must allow at least one encryption type.

  3. Use `cURL` to call the XML API with a [`PUT` Bucket](https://docs.cloud.google.com/storage/docs/xml-api/put-bucket-metadata) request scoped to `?encryptionConfig`:
         
         curl -X PUT --data-binary @XML_FILE_NAME \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storage.googleapis.com/BUCKET_NAME?encryptionConfig"

Replace the following:

     * `XML_FILE_NAME`: the path to the XML file that you created in the previous step.
     * `BUCKET_NAME`: the name of the bucket.

It might take up to two minutes for the updated configuration to take effect.




## View the encryption settings for a bucket

For steps to view which encryption methods are allowed for a bucket, see [Get bucket metadata](https://docs.cloud.google.com/storage/docs/getting-bucket-metadata).

## What's next

  * [Set a default Cloud KMS key on a bucket](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys).
  * Learn how to [use custom constraints to enforce encryption types](https://docs.cloud.google.com/storage/docs/custom-constraints).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
