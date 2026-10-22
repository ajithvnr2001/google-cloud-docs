---
url: https://docs.cloud.google.com/storage/docs/using-public-access-prevention/
title: Use public access prevention \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:29:24.430194+00:00
---

# Use public access prevention  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/using-public-access-prevention/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Use public access prevention Stay organized with collections  Save and categorize content based on your preferences. 

[Overview](https://docs.cloud.google.com/storage/docs/public-access-prevention)

This page describes how to use the public access prevention bucket setting and the public access prevention organization policy constraint. Public access prevention lets you restrict public access to your buckets and objects.

## Before you begin

Before using public access prevention in Cloud Storage, make sure you have the required IAM role and review the considerations for enforcing public access prevention.

### Get required roles

To manage the public access prevention organization policy at the project, folder, or organization level, ask your administrator to grant you the Organization Policy Administrator (`roles/orgpolicy.policyAdmin`) role on the organization. This predefined role contains the permissions required to manage public access prevention at the project, folder, or organization level. For information about the permissions that are included in this role, refer to [details about the Organization Administrator role](https://docs.cloud.google.com/resource-manager/docs/access-control-org#resourcemanager.organizationAdmin).

**Note:** The Organization Policy Administrator role is configured at the organization node, so Project IAM Admins don't have the permissions associated with the role by default.

To manage the public access prevention setting on a bucket, ask your administrator to grant you the Storage Admin (`roles/storage.admin`) role on the bucket. This role contains the permissions required to manage public access prevention on a bucket. To see the exact permissions that are required, expand the **Required permissions** section:

#### Required permissions

  * `storage.buckets.update`
  * `storage.buckets.setIamPolicy`



For information about the other permissions that are included in the Storage Admin role, refer to [details about the Storage Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin).

**Note:** If the bucket's parent project has public access prevention enforced through an organization policy, Storage Admins can't exempt the bucket from public access prevention.

### Review considerations

Before you begin, it's recommended that you ensure no workflows break as a result of blocking public access. See [Considerations when enforcing on existing resources](https://docs.cloud.google.com/storage/docs/public-access-prevention#enforcing) for more details.

## Use the bucket setting

This section shows how to enforce and remove public access prevention for individual buckets, as well as how to check the status of individual buckets.

### Set public access prevention

**Important:** When you set public access prevention to `inherited` for an individual bucket, the bucket might still be subject to public access prevention due to an [organization policy](https://docs.cloud.google.com/storage/docs/org-policy-constraints#public-access-prevention). To ensure that public access prevention is disabled for a bucket with an `inherited` setting, make sure public access prevention is also disabled for its parent project.

To change the public access prevention setting for an individual bucket:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket for which you want to enforce or remove public access prevention.

  3. In the **Bucket details** page, click the **Permissions** tab.

  4. In the **Public access** card, click **Prevent public access** to enforce public access prevention, or click **Allow public access** to remove public access prevention.

  5. Click **Confirm**.




To learn how to get detailed error information about failed Cloud Storage operations in the Google Cloud console, see [Troubleshooting](https://docs.cloud.google.com/storage/docs/troubleshooting#trouble-console).

### Command line

Use the [`gcloud storage buckets update`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/update) command with the appropriate flag:
    
    
    gcloud storage buckets update gs://BUCKET_NAME FLAG

Where:

  * `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.

  * `FLAG` is either `--public-access-prevention` to enable public access prevention or `--no-public-access-prevention` to disable it.




If successful, the response looks similar to the following example:
    
    
    Updating gs://my-bucket/...
      Completed 1  

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample enforces public access prevention on a bucket:
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name) {
      gcs::BucketIamConfiguration configuration;
      configuration.public_access_prevention =
          gcs::PublicAccessPreventionEnforced();
      StatusOr<gcs::BucketMetadata> updated = client.PatchBucket(
          bucket_name, gcs::BucketMetadataPatchBuilder().SetIamConfiguration(
                           std::move(configuration)));
      if (!updated) throw std::move(updated).status();
    
      std::cout << "Public Access Prevention is set to 'enforced' for "
                << updated->name() << "\n";
    }

The following sample sets public access prevention to `inherited` for a bucket:
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name) {
      gcs::BucketIamConfiguration configuration;
      configuration.public_access_prevention =
          gcs::PublicAccessPreventionInherited();
      auto updated = client.PatchBucket(
          bucket_name, gcs::BucketMetadataPatchBuilder().SetIamConfiguration(
                           std::move(configuration)));
      if (!updated) throw std::move(updated).status();
    
      std::cout << "Public Access Prevention is set to 'inherited' for "
                << updated->name() << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample enforces public access prevention on a bucket:
    
    
    using Google.Apis.Storage.v1.Data;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class SetPublicAccessPreventionEnforcedSample
    {
        public Bucket SetPublicAccessPreventionEnforced(string bucketName = "your-unique-bucket-name")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var bucket = storage.GetBucket(bucketName);
    
            // Set public access prevention to "enforced" for the bucket.
            bucket.IamConfiguration.PublicAccessPrevention = "enforced";
            bucket = storage.UpdateBucket(bucket);
    
            Console.WriteLine($"Public access prevention is 'enforced' for {bucketName}.");
            return bucket;
        }
    }

The following sample sets public access prevention to `inherited` for a bucket:
    
    
    using Google.Apis.Storage.v1.Data;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class SetPublicAccessPreventionInheritedSample
    {
        public Bucket SetPublicAccessPreventionInherited(string bucketName = "your-unique-bucket-name")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var bucket = storage.GetBucket(bucketName);
    
            // Sets public access prevention to "inherited" for the bucket.
            bucket.IamConfiguration.PublicAccessPrevention = "inherited";
            bucket = storage.UpdateBucket(bucket);
    
            Console.WriteLine($"Public access prevention is 'inherited' for {bucketName}.");
            return bucket;
        }
    }

### Go

For more information, see the [Cloud Storage Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storage). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample enforces public access prevention on a bucket:
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/storage"
    )
    
    // setPublicAccessPreventionEnforced sets public access prevention to
    // "enforced" for the bucket.
    func setPublicAccessPreventionEnforced(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucketName string) error {
    	// bucketName := "bucket-name"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    
    	bucket := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucketName)
    	setPublicAccessPrevention := storage.[BucketAttrsToUpdate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketAttrsToUpdate){
    		PublicAccessPrevention: storage.[PublicAccessPreventionEnforced](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_PublicAccessPreventionUnknown_PublicAccessPreventionUnspecified_PublicAccessPreventionEnforced_PublicAccessPreventionInherited),
    	}
    	if _, err := bucket.Update(ctx, setPublicAccessPrevention); err != nil {
    		return fmt.Errorf("Bucket(%q).Update: %w", bucketName, err)
    	}
    	fmt.Fprintf(w, "Public access prevention is 'enforced' for %v", bucketName)
    	return nil
    }
    

The following sample sets public access prevention to `inherited` for a bucket:
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/storage"
    )
    
    // setPublicAccessPreventionInherited sets public access prevention to
    // "inherited" for the bucket.
    func setPublicAccessPreventionInherited(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucketName string) error {
    	// bucketName := "bucket-name"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    
    	bucket := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucketName)
    	setPublicAccessPrevention := storage.[BucketAttrsToUpdate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketAttrsToUpdate){
    		PublicAccessPrevention: storage.[PublicAccessPreventionInherited](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_PublicAccessPreventionUnknown_PublicAccessPreventionUnspecified_PublicAccessPreventionEnforced_PublicAccessPreventionInherited),
    	}
    	if _, err := bucket.Update(ctx, setPublicAccessPrevention); err != nil {
    		return fmt.Errorf("Bucket(%q).Update: %w", bucketName, err)
    	}
    	fmt.Fprintf(w, "Public access prevention is 'inherited' for %v", bucketName)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample enforces public access prevention on a bucket:
    
    
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class SetPublicAccessPreventionEnforced {
      public static void setPublicAccessPreventionEnforced(String projectId, String bucketName) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket = storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName);
    
        // Enforces public access prevention for the bucket
        bucket.[toBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html#com_google_cloud_storage_Bucket_toBuilder__)()
            .setIamConfiguration(
                [BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html).IamConfiguration.newBuilder()
                    .[setPublicAccessPrevention](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.IamConfiguration.Builder.html#com_google_cloud_storage_BucketInfo_IamConfiguration_Builder_setPublicAccessPrevention_com_google_cloud_storage_BucketInfo_PublicAccessPrevention_)([BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html).PublicAccessPrevention.ENFORCED)
                    .build())
            .build()
            .update();
    
        System.out.println("Public access prevention is set to enforced for " + bucketName);
      }
    }

The following sample sets public access prevention to `inherited` for a bucket:
    
    
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class SetPublicAccessPreventionInherited {
      public static void setPublicAccessPreventionInherited(String projectId, String bucketName) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket = storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName);
    
        // Sets public access prevention to 'inherited' for the bucket
        bucket.[toBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html#com_google_cloud_storage_Bucket_toBuilder__)()
            .setIamConfiguration(
                [BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html).IamConfiguration.newBuilder()
                    .[setPublicAccessPrevention](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.IamConfiguration.Builder.html#com_google_cloud_storage_BucketInfo_IamConfiguration_Builder_setPublicAccessPrevention_com_google_cloud_storage_BucketInfo_PublicAccessPrevention_)([BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html).PublicAccessPrevention.INHERITED)
                    .build())
            .build()
            .update();
    
        System.out.println("Public access prevention is set to 'inherited' for " + bucketName);
      }
    }

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample enforces public access prevention on a bucket:
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The name of your GCS bucket
    // const bucketName = 'Name of a bucket, e.g. my-bucket';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    // Enforces public access prevention for the bucket
    async function setPublicAccessPreventionEnforced() {
      await storage.bucket(bucketName).setMetadata({
        iamConfiguration: {
          publicAccessPrevention: 'enforced',
        },
      });
    
      console.log(
        `Public access prevention is set to enforced for ${bucketName}.`
      );
    }
    
    setPublicAccessPreventionEnforced();

The following sample sets public access prevention to `inherited` for a bucket:
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The name of your GCS bucket
    // const bucketName = 'Name of a bucket, e.g. my-bucket';
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    async function setPublicAccessPreventionInherited() {
      // Sets public access prevention to 'inherited' for the bucket
      await storage.bucket(bucketName).setMetadata({
        iamConfiguration: {
          publicAccessPrevention: 'inherited',
        },
      });
    
      console.log(`Public access prevention is 'inherited' for ${bucketName}.`);
    }
    
    setPublicAccessPreventionInherited();

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample enforces public access prevention on a bucket:
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Set the bucket Public Access Prevention to enforced.
     *
     * @param string $bucketName the name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     */
    function set_public_access_prevention_enforced(string $bucketName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
    
        $bucket->update([
            'iamConfiguration' => [
                'publicAccessPrevention' => 'enforced'
            ]
        ]);
    
        printf(
            'Public Access Prevention has been set to enforced for %s.' . PHP_EOL,
            $bucketName
        );
    }

The following sample sets public access prevention to `inherited` for a bucket:
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Set the bucket Public Access Prevention to inherited.
     *
     * @param string $bucketName the name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     */
    function set_public_access_prevention_inherited(string $bucketName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
    
        $bucket->update([
            'iamConfiguration' => [
                'publicAccessPrevention' => 'inherited'
            ]
        ]);
    
        printf(
            'Public Access Prevention has been set to inherited for %s.' . PHP_EOL,
            $bucketName
        );
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample enforces public access prevention on a bucket:
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    from google.cloud.storage.constants import PUBLIC_ACCESS_PREVENTION_ENFORCED
    
    
    def set_public_access_prevention_enforced(bucket_name):
        """Enforce public access prevention for a bucket."""
        # The ID of your GCS bucket
        # bucket_name = "my-bucket"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[get_bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_get_bucket)(bucket_name)
    
        bucket.[iam_configuration](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_iam_configuration).[public_access_prevention](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.IAMConfiguration.html#google_cloud_storage_bucket_IAMConfiguration_public_access_prevention) = (
            PUBLIC_ACCESS_PREVENTION_ENFORCED
        )
        bucket.patch()
    
        print(f"Public access prevention is set to enforced for {bucket.name}.")
    
    

The following sample sets public access prevention to `inherited` for a bucket:
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    from google.cloud.storage.constants import PUBLIC_ACCESS_PREVENTION_INHERITED
    
    
    def set_public_access_prevention_inherited(bucket_name):
        """Sets the public access prevention status to inherited, so that the bucket inherits its setting from its parent project."""
        # The ID of your GCS bucket
        # bucket_name = "my-bucket"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[get_bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_get_bucket)(bucket_name)
    
        bucket.[iam_configuration](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_iam_configuration).[public_access_prevention](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.IAMConfiguration.html#google_cloud_storage_bucket_IAMConfiguration_public_access_prevention) = (
            PUBLIC_ACCESS_PREVENTION_INHERITED
        )
        bucket.patch()
    
        print(f"Public access prevention is 'inherited' for {bucket.name}.")
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample enforces public access prevention on a bucket:
    
    
    def set_public_access_prevention_enforced bucket_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket  = storage.bucket bucket_name
    
      bucket.[public_access_prevention](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) = :enforced
    
      puts "Public access prevention is set to enforced for #{bucket_name}."
    end

The following sample sets public access prevention to `inherited` for a bucket:
    
    
    def set_public_access_prevention_inherited bucket_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket  = storage.bucket bucket_name
    
      bucket.[public_access_prevention](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) = :inherited
    
      puts "Public access prevention is 'inherited' for #{bucket_name}."
    end

### Rust

The following sample enforces public access prevention on a bucket:
    
    
    use google_cloud_storage::client::StorageControl;
    use google_cloud_storage::model::bucket::IamConfig;
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
            .set_bucket(
                bucket.set_iam_config(IamConfig::new().set_public_access_prevention("enforced")),
            )
            .set_if_metageneration_match(metageneration)
            .set_update_mask(FieldMask::default().set_paths(["iam_config.public_access_prevention"]))
            .send()
            .await?;
        println!("Public access prevention is enforced for bucket {bucket_id}: {bucket:?}");
        Ok(())
    }

The following sample sets public access prevention to `inherited` for a bucket:
    
    
    use google_cloud_storage::client::StorageControl;
    use google_cloud_storage::model::bucket::IamConfig;
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
            .set_bucket(
                bucket.set_iam_config(IamConfig::new().set_public_access_prevention("inherited")),
            )
            .set_if_metageneration_match(metageneration)
            .set_update_mask(FieldMask::default().set_paths(["iam_config.public_access_prevention"]))
            .send()
            .await?;
        println!("Public access prevention is inherited for bucket {bucket_id}: {bucket:?}");
        Ok(())
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the following information:
         
         {
             "iamConfiguration": {
               "publicAccessPrevention": "STATE",
             }
           }
         

Where `<var>STATE</var>` is either `enforced` or `inherited`.

  3. Use [`cURL`](http://curl.haxx.se/) to call the JSON API with a [`PATCH` Bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/patch) request that includes the desired `fields`:
         
         curl -X PATCH --data-binary @JSON_FILE_NAME \
             -H "Authorization: Bearer $(gcloud auth print-access-token)" \
             -H "Content-Type: application/json" \
             "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME?fields=iamConfiguration"

Where:

     * `JSON_FILE_NAME` is the path for the JSON file that you created in the previous step.
     * `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.



### XML API

The XML API cannot be used to manage public access prevention. Use one of the other Cloud Storage tools, such as the Google Cloud console, instead.

### View public access prevention status

To view the public access prevention status for an individual bucket:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click the name of the bucket for which you want to view the public access prevention status.

  3. Click the **Permissions** tab.

  4. The **Public access** card shows the status for your bucket.




To learn how to get detailed error information about failed Cloud Storage operations in the Google Cloud console, see [Troubleshooting](https://docs.cloud.google.com/storage/docs/troubleshooting#trouble-console).

### Command line

Use the [`gcloud storage buckets describe`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/describe) command with the `--format` flag:
    
    
    gcloud storage buckets describe gs://BUCKET_NAME --format="default(public_access_prevention)"

Where `BUCKET_NAME` is the name of the bucket whose status you want to view. For example, `my-bucket`.

If successful, the response looks similar to the following example:
    
    
    public_access_prevention:inherited

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name) {
      StatusOr<gcs::BucketMetadata> bucket_metadata =
          client.GetBucketMetadata(bucket_name);
      if (!bucket_metadata) throw std::move(bucket_metadata).status();
    
      if (bucket_metadata->has_iam_configuration() &&
          bucket_metadata->iam_configuration()
              .public_access_prevention.has_value()) {
        std::cout
            << "Public Access Prevention is "
            << *bucket_metadata->iam_configuration().public_access_prevention
            << " for bucket " << bucket_metadata->name() << "\n";
      } else {
        std::cout << "Public Access Prevention is not set for "
                  << bucket_metadata->name() << "\n";
      }
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using Google.Apis.Storage.v1.Data;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class GetPublicAccessPreventionSample
    {
        public string GetPublicAccessPrevention(string bucketName = "your-unique-bucket-name")
        {
            // Gets Bucket Metadata and prints publicAccessPrevention value (either "unspecified" or "enforced").
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var bucket = storage.GetBucket(bucketName);
            var publicAccessPrevention = bucket.IamConfiguration.PublicAccessPrevention;
    
            Console.WriteLine($"Public access prevention is {publicAccessPrevention} for {bucketName}.");
            return publicAccessPrevention;
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
    
    // getPublicAccessPrevention gets the current public access prevention setting
    // for the bucket, either "enforced" or "inherited".
    func getPublicAccessPrevention(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucketName string) error {
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
    	fmt.Fprintf(w, "Public access prevention is %s for %v", attrs.[PublicAccessPrevention](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_PublicAccessPrevention), bucketName)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class GetPublicAccessPrevention {
      public static void getPublicAccessPrevention(String projectId, String bucketName) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket = storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName);
    
        // Gets Bucket Metadata and prints publicAccessPrevention value (either 'inherited' or
        // 'enforced').
        [BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html).[PublicAccessPrevention](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.PublicAccessPrevention.html) publicAccessPrevention =
            bucket.[getIamConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_getIamConfiguration__)().[getPublicAccessPrevention](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.IamConfiguration.html#com_google_cloud_storage_BucketInfo_IamConfiguration_getPublicAccessPrevention__)();
    
        System.out.println(
            "Public access prevention is set to "
                + publicAccessPrevention.getValue()
                + " for "
                + bucketName);
      }
    }

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The name of your GCS bucket
    // const bucketName = 'Name of a bucket, e.g. my-bucket';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function getPublicAccessPrevention() {
      // Gets Bucket Metadata and prints publicAccessPrevention value (either 'inherited' or 'enforced').
      const [metadata] = await storage.bucket(bucketName).getMetadata();
      console.log(
        `Public access prevention is ${metadata.[iamConfiguration](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/bucketmetadata.html).publicAccessPrevention} for ${bucketName}.`
      );
    }
    
    getPublicAccessPrevention();
    

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Get the Public Access Prevention setting for a bucket
     *
     * @param string $bucketName the name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     */
    function get_public_access_prevention(string $bucketName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
    
        $iamConfiguration = $bucket->info()['iamConfiguration'];
    
        printf(
            'The bucket public access prevention is %s for %s.' . PHP_EOL,
            $iamConfiguration['publicAccessPrevention'],
            $bucketName
        );
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def get_public_access_prevention(bucket_name):
        """Gets the public access prevention setting (either 'inherited' or 'enforced') for a bucket."""
        # The ID of your GCS bucket
        # bucket_name = "my-bucket"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[get_bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_get_bucket)(bucket_name)
        iam_configuration = bucket.[iam_configuration](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_iam_configuration)
    
        print(
            f"Public access prevention is {[iam_configuration](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_iam_configuration).[public_access_prevention](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.IAMConfiguration.html#google_cloud_storage_bucket_IAMConfiguration_public_access_prevention)} for {bucket.name}."
        )
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def get_public_access_prevention bucket_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket  = storage.bucket bucket_name
    
      puts "Public access prevention is '#{bucket.[public_access_prevention](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)}' for #{bucket_name}."
    end

### Rust
    
    
    use google_cloud_storage::client::StorageControl;
    
    pub async fn sample(client: &StorageControl, bucket_id: &str) -> anyhow::Result<()> {
        let bucket = client
            .get_bucket()
            .set_name(format!("projects/_/buckets/{bucket_id}"))
            .send()
            .await?;
        println!(
            "Public access prevention is {:?} for bucket {}",
            bucket.iam_config.map(|c| c.public_access_prevention),
            bucket_id
        );
        Ok(())
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the JSON API with a [`GET` Bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/get) request that includes the desired `fields`:
         
         curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME?fields=iamConfiguration"

Where `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.

The response looks like the following example:
         
         {
           "iamConfiguration": {
               ...
               "publicAccessPrevention": "FLAG"
             }
           }

Where `FLAG` is either `inherited` or `enforced`.




### XML API

The XML API cannot be used to manage public access prevention. Use one of the other Cloud Storage tools, such as the Google Cloud console, instead.

## Use the organization policy

This section shows how to enforce and remove the public access prevention organization policy, as well as how to check the status of the policy.

### Set public access prevention

To set public access prevention at the project, folder, or organization level:

### Console

Follow the instructions at [Creating and managing organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies) using the `storage.publicAccessPrevention` constraint.

To learn how to get detailed error information about failed Cloud Storage operations in the Google Cloud console, see [Troubleshooting](https://docs.cloud.google.com/storage/docs/troubleshooting#trouble-console).

### Command line

Use the `gcloud beta resource-manager org-policies` command:
    
    
    gcloud beta resource-manager org-policies STATE \
      constraints/storage.publicAccessPrevention \
      --RESOURCE RESOURCE_ID

Where:

  * `STATE` can have the following values:

    * `enable-enforce`: Enforce public access prevention for the resource.
    * `disable-enforce`: Disable public access prevention for the resource.
    * `delete`: Remove the organization policy constraint from the resource, so that the resource inherits the value of its parent resource.
  * `RESOURCE` is the resource for which you want to set public access prevention. For example, `organization`, `project`, or `folder`.

  * `RESOURCE_ID` is the ID for resource. For example, `123456789012` for an [organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization), `245321` for a [folder ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders), or `my-pet-project` for a [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).




See [Using constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#set_up_enforcement_on_the_organization_resource) for more instructions.

The following is an example of the output when you use `disable-enforce`:
    
    
    etag: BwVJi0OOESU=
    booleanPolicy: {}
    constraint: constraints/storage.publicAccessPrevention

### View public access prevention status

To view the public access prevention status at the project, folder, organization level:

### Console

Follow the instructions at [Creating and managing organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies) using the `storage.publicAccessPrevention` constraint.

To learn how to get detailed error information about failed Cloud Storage operations in the Google Cloud console, see [Troubleshooting](https://docs.cloud.google.com/storage/docs/troubleshooting#trouble-console).

### Command line

Use the `describe --effective` command:
    
    
    gcloud beta resource-manager org-policies describe \
      constraints/storage.publicAccessPrevention --effective \
      --RESOURCE RESOURCE_ID

Where:

  * `RESOURCE` is the resource for which you want to view the public access prevention status. For example, `organization`, `project`, or `folder`.

  * `RESOURCE_ID` is the ID for the resource. For example, `123456789012` for an [organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization), `245321` for a [folder ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders), and `my-pet-project` for a [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).




See [Using constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#set_up_enforcement_on_the_organization_resource) for more instructions.

## What's next

  * [Learn more about public access prevention](https://docs.cloud.google.com/storage/docs/public-access-prevention).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
