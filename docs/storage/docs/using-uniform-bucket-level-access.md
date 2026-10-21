---
url: https://docs.cloud.google.com/storage/docs/using-uniform-bucket-level-access/
title: Use uniform bucket-level access \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:15.634133+00:00
---

# Use uniform bucket-level access  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/using-uniform-bucket-level-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Use uniform bucket-level access Stay organized with collections  Save and categorize content based on your preferences. 

[Overview](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access)

You can use [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) to unify access control for your Cloud Storage resources under a single permission system. When you enable uniform bucket-level access on a bucket, only bucket-level Identity and Access Management (IAM) roles grant access to the bucket and its objects, and individual object [Access Control Lists (ACLs)](https://docs.cloud.google.com/storage/docs/access-control/lists) no longer apply. Enabling uniform bucket-level access helps simplify how you grant access to Cloud Storage resources and is required to use some features, such as managed folders.

This page shows you how to enable, disable, and check the status of uniform bucket-level access on a bucket in Cloud Storage.

## Required roles

To get the permissions that you need to set and manage uniform bucket-level access on a bucket, ask your administrator to grant you the Storage Admin (`roles/storage.admin`) role on the bucket. This predefined role contains the permissions required to set and manage uniform bucket-level access. To see the exact permissions that are required, expand the **Required permissions** section:

#### Required permissions

  * `storage.buckets.get`
  * `storage.buckets.list`
    * This permission is only required if you plan on using the Google Cloud console to perform the instructions on this page.
  * `storage.buckets.update`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

For information about granting roles on buckets, see [Use IAM with buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).

## Check for ACL usage

Before you enable uniform bucket-level access, use Cloud Monitoring to ensure your bucket is not using ACLs for any workflows. For more information, see [Check object ACL usage](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access#acl-check).

### Console

To view the metrics for a monitored resource by using the Metrics Explorer, do the following:

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or the app-enabled folder's management project.
  3. In the **Metric** element, expand the **Select a metric** menu, enter `ACLs usage` in the filter bar, and then use the submenus to select a specific resource type and metric: 
     1. In the **Active resources** menu, select **GCS Bucket**.
     2. In the **Active metric categories** menu, select **Authz**.
     3. In the **Active metrics** menu, select **ACLs usage**. 
     4. Click **Apply**.
The fully qualified name for this metric is **storage.googleapis.com/authz/acl_operations_count**.. 
  4. To add filters, which remove time series from the query results, use the [**Filter** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#filter-option).

  5. Configure how the data is viewed. For example, to view your data by the ACL operation, for the **Aggregation** element, set the first menu to **Sum** and the second menu to **acl_operation**. 

For more information about configuring a chart, see [Select metrics when using Metrics Explorer.](https://docs.cloud.google.com/monitoring/charts/metrics-selector)




See [`storage`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-storage) for a complete list of metrics available for Cloud Storage. For information about time series, see [Metrics, time series, and resources](https://docs.cloud.google.com/monitoring/api/v3/metrics).

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [Monitoring](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list) JSON API:
         
         curl \
         'https://monitoring.googleapis.com/v3/projects/PROJECT_ID/timeSeries?filter=metric.type%20%3D%20%22storage.googleapis.com%2Fauthz%2Facl_operations_count%22&interval.endTime=END_TIME&interval.startTime=START_TIME' \
         --header 'Authorization: Bearer $(gcloud auth print-access-token)' \
         --header 'Accept: application/json'

Where:

     * `PROJECT_ID` is the project ID or number for which you want to view ACL usage. For example, `my-project`.
     * `END_TIME` is the end of the time range for which you want to view ACL usage. For example, `2019-11-02T15:01:23.045123456Z`.
     * `START_TIME` is the start of the time range for which you want to view ACL usage. For example, `2016-10-02T15:01:23.045123456Z`.



If the request returns an empty object `{}`, there is no recent ACL usage for your project.

## Set uniform bucket-level access

**Note:** There are several requirements that must be met before you can disable uniform bucket-level access. To review the requirements, see [Requirements for disabling uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access#requirements-for-disabling).

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket for which you want to enable or disable uniform bucket-level access.

  3. Select the **Permissions** tab near the top of the page.

  4. In the field named **Access Control** , click the **Switch to** link.

  5. In the menu that appears, select **Uniform** or **Fine-grained**.

  6. Click **Save**.




To learn how to get detailed error information about failed Cloud Storage operations in the Google Cloud console, see [Troubleshooting](https://docs.cloud.google.com/storage/docs/troubleshooting#trouble-console).

### Command line

Use the [`gcloud storage buckets update`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/update) command:
    
    
    gcloud storage buckets update gs://BUCKET_NAME --STATE

Where:

  * `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.
  * `STATE` is either `uniform-bucket-level-access` to enable uniform bucket-level access or `no-uniform-bucket-level-access` to disable it.



### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample enables uniform bucket-level access on a bucket:
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name) {
      gcs::BucketIamConfiguration configuration;
      configuration.uniform_bucket_level_access =
          gcs::UniformBucketLevelAccess{true, {}};
      StatusOr<gcs::BucketMetadata> updated = client.PatchBucket(
          bucket_name, gcs::BucketMetadataPatchBuilder().SetIamConfiguration(
                           std::move(configuration)));
      if (!updated) throw std::move(updated).status();
    
      std::cout << "Successfully enabled Uniform Bucket Level Access on bucket "
                << updated->name() << "\n";
    }

The following sample disables uniform bucket-level access on a bucket:
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name) {
      gcs::BucketIamConfiguration configuration;
      configuration.uniform_bucket_level_access =
          gcs::UniformBucketLevelAccess{false, {}};
      StatusOr<gcs::BucketMetadata> updated = client.PatchBucket(
          bucket_name, gcs::BucketMetadataPatchBuilder().SetIamConfiguration(
                           std::move(configuration)));
      if (!updated) throw std::move(updated).status();
    
      std::cout << "Successfully disabled Uniform Bucket Level Access on bucket "
                << updated->name() << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample enables uniform bucket-level access on a bucket:
    
    
    using Google.Apis.Storage.v1.Data;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class EnableUniformBucketLevelAccessSample
    {
        public Bucket EnableUniformBucketLevelAccess(string bucketName = "your-unique-bucket-name")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var bucket = storage.GetBucket(bucketName);
            bucket.IamConfiguration.UniformBucketLevelAccess.Enabled = true;
            bucket = storage.UpdateBucket(bucket);
    
            Console.WriteLine($"Uniform bucket-level access was enabled for {bucketName}.");
            return bucket;
        }
    }

The following sample disables uniform bucket-level access on a bucket:
    
    
    using Google.Apis.Storage.v1.Data;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class DisableUniformBucketLevelAccessSample
    {
        public Bucket DisableUniformBucketLevelAccess(string bucketName = "your-unique-bucket-name")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var bucket = storage.GetBucket(bucketName);
            bucket.IamConfiguration.UniformBucketLevelAccess.Enabled = false;
            bucket.IamConfiguration.BucketPolicyOnly.Enabled = false;
            bucket = storage.UpdateBucket(bucket);
    
            Console.WriteLine($"Uniform bucket-level access was disabled for {bucketName}.");
            return bucket;
        }
    }

### Go

For more information, see the [Cloud Storage Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storage). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample enables uniform bucket-level access on a bucket:
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/storage"
    )
    
    // enableUniformBucketLevelAccess sets uniform bucket-level access to true.
    func enableUniformBucketLevelAccess(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucketName string) error {
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
    	enableUniformBucketLevelAccess := storage.[BucketAttrsToUpdate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketAttrsToUpdate){
    		UniformBucketLevelAccess: &storage.[UniformBucketLevelAccess](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_UniformBucketLevelAccess){
    			Enabled: true,
    		},
    	}
    	if _, err := bucket.Update(ctx, enableUniformBucketLevelAccess); err != nil {
    		return fmt.Errorf("Bucket(%q).Update: %w", bucketName, err)
    	}
    	fmt.Fprintf(w, "Uniform bucket-level access was enabled for %v\n", bucketName)
    	return nil
    }
    

The following sample disables uniform bucket-level access on a bucket:
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/storage"
    )
    
    // disableUniformBucketLevelAccess sets uniform bucket-level access to false.
    func disableUniformBucketLevelAccess(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucketName string) error {
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
    	disableUniformBucketLevelAccess := storage.[BucketAttrsToUpdate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketAttrsToUpdate){
    		UniformBucketLevelAccess: &storage.[UniformBucketLevelAccess](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_UniformBucketLevelAccess){
    			Enabled: false,
    		},
    	}
    	if _, err := bucket.Update(ctx, disableUniformBucketLevelAccess); err != nil {
    		return fmt.Errorf("Bucket(%q).Update: %w", bucketName, err)
    	}
    	fmt.Fprintf(w, "Uniform bucket-level access was disabled for %v\n", bucketName)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample enables uniform bucket-level access on a bucket:
    
    
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).[BucketTargetOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.BucketTargetOption.html);
    import com.google.cloud.storage.[StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class EnableUniformBucketLevelAccess {
      public static void enableUniformBucketLevelAccess(String projectId, String bucketName)
          throws [StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
    
        // first look up the bucket, so we will have its metageneration
        [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket = storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName);
    
        [BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html).[IamConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.IamConfiguration.html) iamConfiguration =
            [BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html).IamConfiguration.newBuilder().[setIsUniformBucketLevelAccessEnabled](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.IamConfiguration.Builder.html#com_google_cloud_storage_BucketInfo_IamConfiguration_Builder_setIsUniformBucketLevelAccessEnabled_java_lang_Boolean_)(true).build();
    
        storage.[update](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_update_com_google_cloud_storage_BlobInfo_)(
            bucket.toBuilder()
                .setIamConfiguration(iamConfiguration)
                .setAcl(null)
                .setDefaultAcl(null)
                .build(),
            BucketTargetOption.metagenerationMatch());
    
        System.out.println("Uniform bucket-level access was enabled for " + bucketName);
      }
    }

The following sample disables uniform bucket-level access on a bucket:
    
    
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).[BucketTargetOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.BucketTargetOption.html);
    import com.google.cloud.storage.[StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class DisableUniformBucketLevelAccess {
      public static void disableUniformBucketLevelAccess(String projectId, String bucketName)
          throws [StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
    
        // first look up the bucket, so we will have its metageneration
        [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket = storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName);
    
        [BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html).[IamConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.IamConfiguration.html) iamConfiguration =
            [BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html).IamConfiguration.newBuilder()
                .[setIsUniformBucketLevelAccessEnabled](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.IamConfiguration.Builder.html#com_google_cloud_storage_BucketInfo_IamConfiguration_Builder_setIsUniformBucketLevelAccessEnabled_java_lang_Boolean_)(false)
                .build();
    
        storage.[update](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_update_com_google_cloud_storage_BlobInfo_)(
            bucket.toBuilder().setIamConfiguration(iamConfiguration).build(),
            BucketTargetOption.metagenerationMatch());
    
        System.out.println("Uniform bucket-level access was disabled for " + bucketName);
      }
    }

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample enables uniform bucket-level access on a bucket:
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The ID of your GCS bucket
    // const bucketName = 'your-unique-bucket-name';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    // Enables uniform bucket-level access for the bucket
    async function enableUniformBucketLevelAccess() {
      await storage.bucket(bucketName).setMetadata({
        iamConfiguration: {
          uniformBucketLevelAccess: {
            enabled: true,
          },
        },
      });
    
      console.log(`Uniform bucket-level access was enabled for ${bucketName}.`);
    }
    
    enableUniformBucketLevelAccess().catch(console.error);

The following sample disables uniform bucket-level access on a bucket:
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The ID of your GCS bucket
    // const bucketName = 'your-unique-bucket-name';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    async function disableUniformBucketLevelAccess() {
      // Disables uniform bucket-level access for the bucket
      await storage.bucket(bucketName).setMetadata({
        iamConfiguration: {
          uniformBucketLevelAccess: {
            enabled: false,
          },
        },
      });
    
      console.log(`Uniform bucket-level access was disabled for ${bucketName}.`);
    }
    
    disableUniformBucketLevelAccess().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample enables uniform bucket-level access on a bucket:
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Enable uniform bucket-level access.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     */
    function enable_uniform_bucket_level_access(string $bucketName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
        $bucket->update([
            'iamConfiguration' => [
                'uniformBucketLevelAccess' => [
                    'enabled' => true
                ],
            ]
        ]);
        printf('Uniform bucket-level access was enabled for %s' . PHP_EOL, $bucketName);
    }

The following sample disables uniform bucket-level access on a bucket:
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Enable uniform bucket-level access.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     */
    function disable_uniform_bucket_level_access(string $bucketName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
        $bucket->update([
            'iamConfiguration' => [
                'uniformBucketLevelAccess' => [
                    'enabled' => false
                ],
            ]
        ]);
        printf('Uniform bucket-level access was disabled for %s' . PHP_EOL, $bucketName);
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample enables uniform bucket-level access on a bucket:
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def enable_uniform_bucket_level_access(bucket_name):
        """Enable uniform bucket-level access for a bucket"""
        # bucket_name = "my-bucket"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[get_bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_get_bucket)(bucket_name)
    
        bucket.[iam_configuration](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_iam_configuration).[uniform_bucket_level_access_enabled](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.IAMConfiguration.html#google_cloud_storage_bucket_IAMConfiguration_uniform_bucket_level_access_enabled) = True
        bucket.patch()
    
        print(
            f"Uniform bucket-level access was enabled for {bucket.name}."
        )
    
    

The following sample disables uniform bucket-level access on a bucket:
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def disable_uniform_bucket_level_access(bucket_name):
        """Disable uniform bucket-level access for a bucket"""
        # bucket_name = "my-bucket"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[get_bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_get_bucket)(bucket_name)
    
        bucket.[iam_configuration](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_iam_configuration).[uniform_bucket_level_access_enabled](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.IAMConfiguration.html#google_cloud_storage_bucket_IAMConfiguration_uniform_bucket_level_access_enabled) = False
        bucket.patch()
    
        print(
            f"Uniform bucket-level access was disabled for {bucket.name}."
        )
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample enables uniform bucket-level access on a bucket:
    
    
    def enable_uniform_bucket_level_access bucket_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket  = storage.bucket bucket_name
    
      bucket.uniform_bucket_level_access = true
    
      puts "Uniform bucket-level access was enabled for #{bucket_name}."
    end

The following sample disables uniform bucket-level access on a bucket:
    
    
    def disable_uniform_bucket_level_access bucket_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket  = storage.bucket bucket_name
    
      bucket.uniform_bucket_level_access = false
    
      puts "Uniform bucket-level access was disabled for #{bucket_name}."
    end

### Rust

The following sample enables uniform bucket-level access on a bucket:
    
    
    use google_cloud_storage::client::StorageControl;
    use google_cloud_storage::model::bucket::IamConfig;
    use google_cloud_storage::model::bucket::iam_config::UniformBucketLevelAccess;
    use google_cloud_wkt::FieldMask;
    
    pub async fn sample(client: &StorageControl, bucket_id: &str) -> anyhow::Result<()> {
        let bucket = client
            .get_bucket()
            .set_name(format!("projects/_/buckets/{bucket_id}"))
            .send()
            .await?;
        let metageneration = bucket.metageneration;
        let iam_config = IamConfig::new()
            .set_uniform_bucket_level_access(UniformBucketLevelAccess::new().set_enabled(true));
        let bucket = client
            .update_bucket()
            .set_bucket(bucket.set_iam_config(iam_config))
            .set_if_metageneration_match(metageneration)
            .set_update_mask(FieldMask::default().set_paths(["iam_config.uniform_bucket_level_access"]))
            .send()
            .await?;
        println!(
            "Uniform bucket-level access enabled for bucket {bucket_id}: {:?}",
            bucket.iam_config
        );
        Ok(())
    }

The following sample disables uniform bucket-level access on a bucket:
    
    
    use google_cloud_storage::client::StorageControl;
    use google_cloud_storage::model::bucket::IamConfig;
    use google_cloud_storage::model::bucket::iam_config::UniformBucketLevelAccess;
    use google_cloud_wkt::FieldMask;
    
    pub async fn sample(client: &StorageControl, bucket_id: &str) -> anyhow::Result<()> {
        let bucket = client
            .get_bucket()
            .set_name(format!("projects/_/buckets/{bucket_id}"))
            .send()
            .await?;
        let metageneration = bucket.metageneration;
        let iam_config = IamConfig::new()
            .set_uniform_bucket_level_access(UniformBucketLevelAccess::new().set_enabled(false));
        let bucket = client
            .update_bucket()
            .set_bucket(bucket.set_iam_config(iam_config))
            .set_if_metageneration_match(metageneration)
            .set_update_mask(FieldMask::default().set_paths(["iam_config.uniform_bucket_level_access"]))
            .send()
            .await?;
        println!(
            "Uniform bucket-level access disabled for bucket {bucket_id}: {:?}",
            bucket.iam_config
        );
        Ok(())
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the following information:
         
         {
           "iamConfiguration": {
               "uniformBucketLevelAccess": {
                 "enabled": STATE
               }
           }
         }

Where STATE is either `true` or `false`.

  3. Use [`cURL`](http://curl.haxx.se/) to call the JSON API with a [`PATCH` Bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/patch) request:
         
         curl -X PATCH --data-binary @JSON_FILE_NAME \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME?fields=iamConfiguration"

Where:

     * `JSON_FILE_NAME` is the path for the file that you created in Step 2.
     * `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.



### XML API

The XML API cannot be used to work with uniform bucket-level access. Use one of the other Cloud Storage tools, such as the gcloud CLI, instead.

## View uniform bucket-level access status

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click the name of the bucket whose status you want to view.

  3. Click the **Configuration** tab.

The uniform bucket-level access status for the bucket is found in the **Access control** field.




To learn how to get detailed error information about failed Cloud Storage operations in the Google Cloud console, see [Troubleshooting](https://docs.cloud.google.com/storage/docs/troubleshooting#trouble-console).

### Command line

Use the [`gcloud storage buckets describe`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/describe) command with the `--format` flag:
    
    
    gcloud storage buckets describe gs://BUCKET_NAME --format="default(uniform_bucket_level_access)"

Where `BUCKET_NAME` is the name of the relevant bucket. For example, `my-bucket`.

If successful, the response looks like:
    
    
    uniform_bucket_level_access: true

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
              .uniform_bucket_level_access.has_value()) {
        gcs::UniformBucketLevelAccess uniform_bucket_level_access =
            *bucket_metadata->iam_configuration().uniform_bucket_level_access;
    
        std::cout << "Uniform Bucket Level Access is enabled for "
                  << bucket_metadata->name() << "\n";
        std::cout << "Bucket will be locked on " << uniform_bucket_level_access
                  << "\n";
      } else {
        std::cout << "Uniform Bucket Level Access is not enabled for "
                  << bucket_metadata->name() << "\n";
      }
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    using static Google.Apis.Storage.v1.Data.Bucket.IamConfigurationData;
    
    public class GetUniformBucketLevelAccessSample
    {
        public UniformBucketLevelAccessData GetUniformBucketLevelAccess(
            string bucketName = "your-unique-bucket-name")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var bucket = storage.GetBucket(bucketName);
            var uniformBucketLevelAccess = bucket.IamConfiguration.UniformBucketLevelAccess;
    
            bool uniformBucketLevelAccessEnabled = uniformBucketLevelAccess.Enabled ?? false;
            if (uniformBucketLevelAccessEnabled)
            {
                Console.WriteLine($"Uniform bucket-level access is enabled for {bucketName}.");
                Console.WriteLine(
                    $"Uniform bucket-level access will be locked on {uniformBucketLevelAccess.LockedTime}.");
            }
            else
            {
                Console.WriteLine($"Uniform bucket-level access is not enabled for {bucketName}.");
            }
            return uniformBucketLevelAccess;
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
    
    // getUniformBucketLevelAccess gets uniform bucket-level access.
    func getUniformBucketLevelAccess(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucketName string) (*storage.[BucketAttrs](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketAttrs), error) {
    	// bucketName := "bucket-name"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    
    	attrs, err := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucketName).Attrs(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("Bucket(%q).Attrs: %w", bucketName, err)
    	}
    	uniformBucketLevelAccess := attrs.[UniformBucketLevelAccess](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_UniformBucketLevelAccess)
    	if uniformBucketLevelAccess.Enabled {
    		fmt.Fprintf(w, "Uniform bucket-level access is enabled for %q.\n", attrs.Name)
    		fmt.Fprintf(w, "Bucket will be locked on %q.\n", uniformBucketLevelAccess.LockedTime)
    	} else {
    		fmt.Fprintf(w, "Uniform bucket-level access is not enabled for %q.\n", attrs.Name)
    	}
    	return attrs, nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import java.util.Date;
    
    public class GetUniformBucketLevelAccess {
      public static void getUniformBucketLevelAccess(String projectId, String bucketName)
          throws [StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket =
            storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(
                bucketName, Storage.BucketGetOption.fields(Storage.BucketField.IAMCONFIGURATION));
        [BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html).[IamConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.IamConfiguration.html) iamConfiguration = bucket.[getIamConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_getIamConfiguration__)();
    
        Boolean enabled = iamConfiguration.[isUniformBucketLevelAccessEnabled](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.IamConfiguration.html#com_google_cloud_storage_BucketInfo_IamConfiguration_isUniformBucketLevelAccessEnabled__)();
        Date lockedTime = new Date(iamConfiguration.[getUniformBucketLevelAccessLockedTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.IamConfiguration.html#com_google_cloud_storage_BucketInfo_IamConfiguration_getUniformBucketLevelAccessLockedTime__)());
    
        if (enabled != null && enabled) {
          System.out.println("Uniform bucket-level access is enabled for " + bucketName);
          System.out.println("Bucket will be locked on " + lockedTime);
        } else {
          System.out.println("Uniform bucket-level access is disabled for " + bucketName);
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
    
    async function getUniformBucketLevelAccess() {
      // Gets Bucket Metadata and checks if uniform bucket-level access is enabled.
      const [metadata] = await storage.bucket(bucketName).getMetadata();
    
      if (metadata.[iamConfiguration](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/bucketmetadata.html)) {
        const uniformBucketLevelAccess =
          metadata.[iamConfiguration](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/bucketmetadata.html).uniformBucketLevelAccess;
        console.log(`Uniform bucket-level access is enabled for ${bucketName}.`);
        console.log(
          `Bucket will be locked on ${uniformBucketLevelAccess.lockedTime}.`
        );
      } else {
        console.log(
          `Uniform bucket-level access is not enabled for ${bucketName}.`
        );
      }
    }
    
    getUniformBucketLevelAccess().catch(console.error);
    

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Enable uniform bucket-level access.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     */
    function get_uniform_bucket_level_access(string $bucketName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
        $bucketInformation = $bucket->info();
        $ubla = $bucketInformation['iamConfiguration']['uniformBucketLevelAccess'];
        if ($ubla['enabled']) {
            printf('Uniform bucket-level access is enabled for %s' . PHP_EOL, $bucketName);
            printf('Uniform bucket-level access will be locked on %s' . PHP_EOL, $ubla['LockedTime']);
        } else {
            printf('Uniform bucket-level access is disabled for %s' . PHP_EOL, $bucketName);
        }
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def get_uniform_bucket_level_access(bucket_name):
        """Get uniform bucket-level access for a bucket"""
        # bucket_name = "my-bucket"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[get_bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_get_bucket)(bucket_name)
        iam_configuration = bucket.[iam_configuration](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_iam_configuration)
    
        if [iam_configuration](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_iam_configuration).[uniform_bucket_level_access_enabled](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.IAMConfiguration.html#google_cloud_storage_bucket_IAMConfiguration_uniform_bucket_level_access_enabled):
            print(
                f"Uniform bucket-level access is enabled for {bucket.name}."
            )
            print(
                "Bucket will be locked on {}.".format(
                    [iam_configuration](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_iam_configuration).uniform_bucket_level_locked_time
                )
            )
        else:
            print(
                f"Uniform bucket-level access is disabled for {bucket.name}."
            )
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def get_uniform_bucket_level_access bucket_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket  = storage.bucket bucket_name
    
      if bucket.[uniform_bucket_level_access?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)
        puts "Uniform bucket-level access is enabled for #{bucket_name}."
        puts "Bucket will be locked on #{bucket.[uniform_bucket_level_access_locked_at](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)}."
      else
        puts "Uniform bucket-level access is disabled for #{bucket_name}."
      end
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
            "IAM Config for bucket {bucket_id} is: {:?}",
            bucket.iam_config
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

If the bucket has uniform bucket-level access enabled, the response looks like the following example:
         
         {
           "iamConfiguration": {
               "uniformBucketLevelAccess": {
                 "enabled": true,
                 "lockedTime": "LOCK_DATE"
               }
             }
           }




### XML API

The XML API cannot be used to work with uniform bucket-level access. Use one of the other Cloud Storage tools, such as the gcloud CLI, instead.

## What's next

  * [Learn more about uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access).
  * [Set IAM permissions on buckets and projects](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
