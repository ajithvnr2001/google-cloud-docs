---
url: https://docs.cloud.google.com/storage/docs/creating-buckets/
title: Create a bucket \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:30:27.316924+00:00
---

# Create a bucket  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/creating-buckets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Create a bucket Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to create a Cloud Storage [bucket](https://docs.cloud.google.com/storage/docs/buckets). If not otherwise specified in your request, buckets are created in the [`US` multi-region](https://docs.cloud.google.com/storage/docs/locations) with a default storage class of [Standard storage](https://docs.cloud.google.com/storage/docs/storage-classes) and have a seven-day [soft delete](https://docs.cloud.google.com/storage/docs/soft-delete) retention duration.

If you're creating a bucket for the first time, see [Discover object storage with the Google Cloud console](https://docs.cloud.google.com/storage/docs/discover-object-storage-console) or [Discover object storage with the Google Cloud CLI](https://docs.cloud.google.com/storage/docs/discover-object-storage-gcloud) for a more comprehensive walkthrough of the tasks you can perform with Cloud Storage.

**Note:** A bucket's name is [non-editable metadata](https://docs.cloud.google.com/storage/docs/bucket-metadata#non-editable). If you need to designate a specific name, it must be specified at bucket creation.

## Required roles

**Note:** The following content describes the required IAM roles and permissions for creating a bucket with basic settings. If you want to set up [cross-bucket replication](https://docs.cloud.google.com/storage/docs/availability-durability#cross-bucket-replication) as part of creating your bucket, you need additional roles and permissions. Refer to [Before you begin](https://docs.cloud.google.com/storage/docs/using-cross-bucket-replication#before-you-begin) in the cross-bucket replication user guide for information on the roles and permissions required.

In order to get the required permissions for creating a Cloud Storage bucket, ask your administrator to grant you the Storage Admin (`roles/storage.admin`) IAM role for the project.

This [predefined role](https://docs.cloud.google.com/iam/docs/understanding-roles) contains the permission required to create a bucket. To see the exact permissions that are required, expand the **Required permissions** section:

#### Required permissions

  * `storage.buckets.create`
  * `storage.buckets.enableObjectRetention` (only required if enabling [object retention configurations](https://docs.cloud.google.com/storage/docs/object-lock) for the bucket)
  * `storage.buckets.list` (only required if creating a bucket using the Google Cloud console.)
  * `resourcemanager.projects.get` (only required if creating a bucket using the Google Cloud console)



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other predefined roles. To see which roles are associated with which permissions, refer to [IAM roles for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam-roles).

For instructions on granting roles for projects, see [Manage access to projects](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Create a new bucket

To create a bucket with specific settings or advanced configurations, complete the following steps.

**Note:** To create a zonal bucket that uses the Rapid storage class, see [Create a zonal bucket](https://docs.cloud.google.com/storage/docs/rapid/create-zonal-buckets).

### Console

When creating a bucket using the Google Cloud console, you are only required to set a globally unique name for your bucket; all other steps are either optional or have default settings.

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
        2. Select an [access control model](https://docs.cloud.google.com/storage/docs/access-control) for your bucket's objects. We recommend that you select **Uniform** to enable uniform bucket-level access on the bucket.

        3. To configure [IP filtering for the bucket](https://docs.cloud.google.com/storage/docs/ip-filtering-overview), do the following:

           1. In the **IP filtering** section, click add_box **Configure**.

           2. To allow access from public IP addresses, do the following:

              1. Click **Public internet**.
              2. In the **Allowed IP range(s)** field, specify one or more IPv4 address ranges or IPv6 CIDR ranges to allow. For example, `192.0.2.0/24` or `2001:db8::/32`.

To avoid being locked out of your bucket, include your own IP address.

           3. To allow access from VPC networks, do the following:

              1. Click **VPC network(s)**.
              2. Do the following for each network:

                 1. Click **Add VPC network**.
                 2. In the **New VPC network** section, specify the following information:

                    * In the **Project ID** field, enter your project ID.
                    * In the **Network name** field, enter your network name.
                    * In the **Allowed IP range(s)** field, enter one or more IPv4 or IPv6 CIDR ranges, such as `192.0.2.0/24` or `2001:db8::/32`.

To avoid being locked out of your bucket, include your own IP address.

                 3. Click **Done**.
           4. To permit trusted Google Cloud service agents and VPC networks from other organizations to bypass your IP filtering configuration, do the following:

              1. Click **Additional settings**.
              2. In the **Google Cloud service agent access** section, select one of the following options:

                 * **Allow service agent access** : enables Google Cloud services such as BigLake, Storage Insights, Vertex AI, and BigQuery to bypass the IP filtering validation when they need to access this bucket.
                 * **Deny service agent access** : enforces the IP filter rules for Google Cloud service agents.
              3. In the **Cross-organization VPC access** section, do one of the following: 
                 * To permit access from specified VPC networks located in different Google Cloud organizations, click the toggle to the **Allow** position.
                 * To block access from VPC networks outside of your Google Cloud organization, click the toggle to **Deny** (default state) position.
           5. Click **Review** , and then click **Save**.
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

**Note:** Cloud Shell provisions a temporary virtual machine. If you want to upload objects to Cloud Storage or download objects from Cloud Storage, use a local development environment.

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. In your development environment, run the [`gcloud storage buckets create`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/create) command:
         
         gcloud storage buckets create gs://BUCKET_NAME --location=BUCKET_LOCATION

Where:

     * `BUCKET_NAME` is the name you want to give your bucket, subject to [naming requirements](https://docs.cloud.google.com/storage/docs/buckets#naming). For example, `my-bucket`.
     * `BUCKET_LOCATION` is the [location](https://docs.cloud.google.com/storage/docs/locations) of your bucket. For example, `US`.

**Note:** When creating a [configurable dual-region](https://docs.cloud.google.com/storage/docs/locations#location-dr), you must set the `--location` flag to be the _location code_ associated with the underlying regions, and you must use the [`--placement` flag](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/create#--placement) with a valid pair of regions. For example, `--location=ASIA --placement=ASIA-EAST1,ASIA-SOUTHEAST1`.

If the request is successful, the command returns the following message:
    
    Creating gs://BUCKET_NAME/...

Set the following flags to have greater control over the creation of your bucket:

     * `--project`: Specify the project ID or project number with which your bucket will be associated. For example, `my-project`.
     * `--default-storage-class`: Specify the default [storage class](https://docs.cloud.google.com/storage/docs/storage-classes) of your bucket. For example, `STANDARD`.
     * `--uniform-bucket-level-access`: Enable [uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) for your bucket.
     * `--soft-delete-duration`: Specify a [soft delete](https://docs.cloud.google.com/storage/docs/soft-delete) retention duration, which is the number of days you want to retain objects after they get deleted. For example, `10d`.
     * `--encryption-enforcement-file`: Provide a file that defines [which encryption methods are restricted or allowed](https://docs.cloud.google.com/storage/docs/encryption/enforce-encryption-types) for new objects in the bucket.

For example:
    
    gcloud storage buckets create gs://BUCKET_NAME --project=PROJECT_ID --default-storage-class=STORAGE_CLASS --location=BUCKET_LOCATION --uniform-bucket-level-access
    --soft-delete-duration=RETENTION_DURATION --encryption-enforcement-file=ENCRYPTION_ENFORCEMENT_FILE
    

For a complete list of options for bucket creation using the gcloud CLI, see [`buckets create` options](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/create#FLAGS).




### Client libraries

**Note:** Other options for creating a new bucket can be found in the JSON API reference for [ `bucket.insert`](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/insert#request-body)

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name,
       std::string const& storage_class, std::string const& location) {
      StatusOr<gcs::BucketMetadata> bucket_metadata =
          client.CreateBucket(bucket_name, gcs::BucketMetadata()
                                               .set_storage_class(storage_class)
                                               .set_location(location));
      if (!bucket_metadata) throw std::move(bucket_metadata).status();
    
      std::cout << "Bucket " << bucket_metadata->name() << " created."
                << "\nFull Metadata: " << *bucket_metadata << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using Google.Apis.Storage.v1.Data;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class CreateRegionalBucketSample
    {
        /// <summary>
        /// Creates a storage bucket with region.
        /// </summary>
        /// <param name="projectId">The ID of the project to create the buckets in.</param>
        /// <param name="location">The location of the bucket. Object data for objects in the bucket resides in 
        /// physical storage within this region. Defaults to US.</param>
        /// <param name="bucketName">The name of the bucket to create.</param>
        /// <param name="storageClass">The bucket's default storage class, used whenever no storageClass is specified
        /// for a newly-created object. This defines how objects in the bucket are stored
        /// and determines the SLA and the cost of storage. Values include MULTI_REGIONAL,
        /// REGIONAL, STANDARD, NEARLINE, COLDLINE, ARCHIVE, and DURABLE_REDUCED_AVAILABILITY.
        /// If this value is not specified when the bucket is created, it will default to
        /// STANDARD.</param>
        public Bucket CreateRegionalBucket(
            string projectId = "your-project-id",
            string bucketName = "your-unique-bucket-name",
            string location = "us-west1",
            string storageClass = "REGIONAL")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            Bucket bucket = new Bucket
            {
                Location = location,
                Name = bucketName,
                StorageClass = storageClass
            };
            var newlyCreatedBucket = storage.CreateBucket(projectId, bucket);
            Console.WriteLine($"Created {bucketName}.");
            return newlyCreatedBucket;
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
    
    // createBucketClassLocation creates a new bucket in the project with Storage class and
    // location.
    func createBucketClassLocation(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), projectID, bucketName string) error {
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
    
    	storageClassAndLocation := &storage.[BucketAttrs](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketAttrs){
    		StorageClass: "COLDLINE",
    		Location:     "asia",
    	}
    	bucket := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucketName)
    	if err := bucket.[Create](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Create)(ctx, projectID, storageClassAndLocation); err != nil {
    		return fmt.Errorf("Bucket(%q).Create: %w", bucketName, err)
    	}
    	fmt.Fprintf(w, "Created bucket %v in %v with storage class %v\n", bucketName, storageClassAndLocation.Location, storageClassAndLocation.StorageClass)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageClass.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class CreateBucketWithStorageClassAndLocation {
      public static void createBucketWithStorageClassAndLocation(String projectId, String bucketName) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID to give your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
    
        // See the StorageClass documentation for other valid storage classes:
        // https://googleapis.dev/java/google-cloud-clients/latest/com/google/cloud/storage/StorageClass.html
        [StorageClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageClass.html) storageClass = [StorageClass](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageClass.html).COLDLINE;
    
        // See this documentation for other valid locations:
        // http://g.co/cloud/storage/docs/bucket-locations#location-mr
        String location = "ASIA";
    
        [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket =
            storage.[create](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_create_com_google_cloud_storage_BlobInfo_byte___com_google_cloud_storage_Storage_BlobTargetOption____)(
                BucketInfo.newBuilder(bucketName)
                    .setStorageClass(storageClass)
                    .setLocation(location)
                    .build());
    
        System.out.println(
            "Created bucket "
                + bucket.getName()
                + " in "
                + bucket.getLocation()
                + " with storage class "
                + bucket.getStorageClass());
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
    
    // The name of a storage class
    // See the StorageClass documentation for other valid storage classes:
    // https://googleapis.dev/java/google-cloud-clients/latest/com/google/cloud/storage/StorageClass.html
    // const storageClass = 'coldline';
    
    // The name of a location
    // See this documentation for other valid locations:
    // http://g.co/cloud/storage/docs/locations#location-mr
    // const location = 'ASIA';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    // The bucket in the sample below will be created in the project associated with this client.
    // For more information, please see https://cloud.google.com/docs/authentication/production or https://googleapis.dev/nodejs/storage/latest/Storage.html
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function createBucketWithStorageClassAndLocation() {
      // For default values see: https://cloud.google.com/storage/docs/locations and
      // https://cloud.google.com/storage/docs/storage-classes
      const [bucket] = await storage.createBucket(bucketName, {
        location,
        [storageClass]: true,
      });
    
      console.log(
        `${bucket.name} created with ${storageClass} class in ${location}`
      );
    }
    
    createBucketWithStorageClassAndLocation().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Create a new bucket with a custom default storage class and location.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     */
    function create_bucket_class_location(string $bucketName): void
    {
        $storage = new StorageClient();
        $storageClass = 'COLDLINE';
        $location = 'ASIA';
        $bucket = $storage->createBucket($bucketName, [
            'storageClass' => $storageClass,
            'location' => $location,
        ]);
    
        $objects = $bucket->objects([
            'encryption' => [
                'defaultKmsKeyName' => null,
            ]
        ]);
    
        printf('Created bucket %s in %s with storage class %s', $bucketName, $storageClass, $location);
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def create_bucket_class_location(bucket_name):
        """
        Create a new bucket in the US region with the coldline storage
        class
        """
        # bucket_name = "your-new-bucket-name"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
        bucket.storage_class = "COLDLINE"
        new_bucket = storage_client.[create_bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_create_bucket)(bucket, location="us")
    
        print(
            "Created bucket {} in {} with storage class {}".format(
                new_bucket.name, new_bucket.[location](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_location), new_bucket.storage_class
            )
        )
        return new_bucket
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def create_bucket_class_location bucket_name:
      # The ID to give your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket  = storage.[create_bucket](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Project.html) bucket_name,
                                      location:      "ASIA",
                                      storage_class: "COLDLINE"
    
      puts "Created bucket #{bucket.name} in #{bucket.location} with #{bucket.storage_class} class"
    end

### Rust
    
    
    use google_cloud_storage::{client::StorageControl, model::Bucket};
    
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
                    .set_storage_class("NEARLINE")
                    .set_location("US-CENTRAL1"),
            )
            .send()
            .await?;
        println!("successfully created bucket {bucket:?}");
        Ok(())
    }

### Terraform

You can use a [Terraform resource to create a storage bucket](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket).
    
    
    # Create new storage bucket in the US multi-region
    # with coldline storage
    resource "random_id" "bucket_prefix" {
      byte_length = 8
    }
    
    resource "google_storage_bucket" "static" {
      name          = "${random_id.bucket_prefix.hex}-new-bucket"
      location      = "US"
      storage_class = "COLDLINE"
    
      uniform_bucket_level_access = true
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the settings for the bucket, which must include a `name` for the bucket. See the [Buckets:Insert](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/insert) documentation for a complete list of settings. The following are common settings to include:
         
         {
           "name": "BUCKET_NAME",
           "location": "BUCKET_LOCATION",
           "storageClass": "STORAGE_CLASS",
           "iamConfiguration": {
             "uniformBucketLevelAccess": {
               "enabled": true
             },
           }
         }

Where:

     * `BUCKET_NAME` is the name you want to give your bucket, subject to [naming requirements](https://docs.cloud.google.com/storage/docs/buckets#naming). For example, `my-bucket`.

     * `BUCKET_LOCATION` is the [location](https://docs.cloud.google.com/storage/docs/locations) where you want to store your bucket's [object data](https://docs.cloud.google.com/storage/docs/objects). For example, `US`.

**Note:** When creating a [configurable dual-region](https://docs.cloud.google.com/storage/docs/locations#location-dr), you must set the `location` parameter to be the _location code_ associated with the underlying regions, and you must also include a `customPlacementConfig` parameter.
     * `STORAGE_CLASS` is the default [storage class](https://docs.cloud.google.com/storage/docs/storage-classes) of your bucket. For example, `STANDARD`.

  3. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api):
         
         curl -X POST --data-binary @JSON_FILE_NAME \
          -H "Authorization: Bearer $(gcloud auth print-access-token)" \
          -H "Content-Type: application/json" \
          "https://storage.googleapis.com/storage/v1/b?project=PROJECT_IDENTIFIER"

Where:

     * `JSON_FILE_NAME` is name of the JSON file you created in Step 2.
     * `PROJECT_IDENTIFIER` is the ID or number of the project with which your bucket will be associated. For example, `my-project`.



### XML API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create an XML file that contains settings for the bucket. See the [XML: Create a bucket](https://docs.cloud.google.com/storage/docs/xml-api/put-bucket-create) documentation for a complete list of settings. The following are common settings to include:
         
         <CreateBucketConfiguration>
           <StorageClass>STORAGE_CLASS</StorageClass>
           <LocationConstraint>BUCKET_LOCATION</LocationConstraint>
         </CreateBucketConfiguration>

Where:

     * `STORAGE_CLASS` is the default [storage class](https://docs.cloud.google.com/storage/docs/storage-classes) of your bucket. For example, `STANDARD`.

     * `BUCKET_LOCATION` is the [location](https://docs.cloud.google.com/storage/docs/locations) where you want to store your bucket's [object data](https://docs.cloud.google.com/storage/docs/objects). For example, `US`.

**Note:** When creating a [configurable dual-region](https://docs.cloud.google.com/storage/docs/locations#location-dr), you must set the `<LocationConstraint>` element to be the _location code_ associated with the underlying regions, and you must also include a `<CustomPlacementConfig>` element.
  3. Use [`cURL`](http://curl.haxx.se/) to call the [XML API](https://docs.cloud.google.com/storage/docs/xml-api/put-bucket-create):
         
         curl -X PUT --data-binary @XML_FILE_NAME \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "x-goog-project-id: PROJECT_ID" \
           "https://storage.googleapis.com/BUCKET_NAME"

Where:

     * `XML_FILE_NAME` is name of the XML file you created in Step 2.
     * `PROJECT_ID` is the ID of the project with which your bucket will be associated. For example, `my-project`.
     * `BUCKET_NAME` is the name you want to give your bucket, subject to [naming requirements](https://docs.cloud.google.com/storage/docs/buckets#naming). For example, `my-bucket`.

If the request was successful, a response is not returned.




## What's next

  * [List buckets in a project](https://docs.cloud.google.com/storage/docs/listing-buckets).
  * Learn about the [metadata associated with a bucket](https://docs.cloud.google.com/storage/docs/bucket-metadata).
  * [Move or rename a bucket](https://docs.cloud.google.com/storage/docs/moving-buckets).
  * [Delete a bucket](https://docs.cloud.google.com/storage/docs/deleting-buckets).
  * [Upload an object to your bucket](https://docs.cloud.google.com/storage/docs/uploading-objects).
  * Create and configure buckets declaratively with the [Kubernetes Config Connector](https://docs.cloud.google.com/config-connector/docs/overview), which lets you describe Google Cloud resources using Kubernetes tooling, APIs, and configurations. For more information, see the [Config Connector API documentation](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/storage/storagebucket). 
  * Automate bucket creation and configuration with AI coding assistants using the [Cloud Storage bucket architect skill](https://docs.cloud.google.com/storage/docs/agents-skills-overview#bucket-architect-skill) or the [Cloud Storage basics skill](https://docs.cloud.google.com/storage/docs/agents-skills-overview#basics-skill). 



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Cloud Storage performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Cloud Storage free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
