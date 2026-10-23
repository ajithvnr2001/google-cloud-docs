---
url: https://docs.cloud.google.com/storage/docs/samples/storage-get-uniform-bucket-level-access/
title: Get uniform bucket-level access \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:05.785165+00:00
---

# Get uniform bucket-level access  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-get-uniform-bucket-level-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Get uniform bucket-level access Stay organized with collections  Save and categorize content based on your preferences. 

Get uniform bucket-level access.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Use uniform bucket-level access](https://docs.cloud.google.com/storage/docs/using-uniform-bucket-level-access)



## Code sample

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
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket  = storage.bucket bucket_name
    
      if bucket.[uniform_bucket_level_access?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)
        puts "Uniform bucket-level access is enabled for #{bucket_name}."
        puts "Bucket will be locked on #{bucket.[uniform_bucket_level_access_locked_at](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)}."
      else
        puts "Uniform bucket-level access is disabled for #{bucket_name}."
      end
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
