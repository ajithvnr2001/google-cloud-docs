---
url: https://docs.cloud.google.com/storage/docs/samples/storage-get-bucket-metadata/
title: Get a bucket's metadata \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:50.409950+00:00
---

# Get a bucket's metadata  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-get-bucket-metadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Get a bucket's metadata Stay organized with collections  Save and categorize content based on your preferences. 

Retrieve metadata from a Cloud Storage bucket.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Enable and use object retention configurations](https://docs.cloud.google.com/storage/docs/using-object-lock)
  * [Get bucket metadata](https://docs.cloud.google.com/storage/docs/getting-bucket-metadata)
  * [Manage object lifecycles](https://docs.cloud.google.com/storage/docs/managing-lifecycles)
  * [Set up and view CORS configurations](https://docs.cloud.google.com/storage/docs/using-cors)
  * [Use customer-managed encryption keys](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys)
  * [Using bucket labels](https://docs.cloud.google.com/storage/docs/using-bucket-labels)



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
    
      std::cout << "The metadata for bucket " << bucket_metadata->name() << " is "
                << *bucket_metadata << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
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
    
    // getBucketMetadata gets the bucket metadata.
    func getBucketMetadata(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucketName string) (*storage.[BucketAttrs](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketAttrs), error) {
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
    	fmt.Fprintf(w, "BucketName: %v\n", attrs.Name)
    	fmt.Fprintf(w, "Location: %v\n", attrs.Location)
    	fmt.Fprintf(w, "LocationType: %v\n", attrs.LocationType)
    	fmt.Fprintf(w, "StorageClass: %v\n", attrs.StorageClass)
    	fmt.Fprintf(w, "Turbo replication (RPO): %v\n", attrs.[RPO](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_RPO))
    	fmt.Fprintf(w, "TimeCreated: %v\n", attrs.Created)
    	fmt.Fprintf(w, "Metageneration: %v\n", attrs.MetaGeneration)
    	fmt.Fprintf(w, "PredefinedACL: %v\n", attrs.PredefinedACL)
    	if attrs.Encryption != nil {
    		fmt.Fprintf(w, "DefaultKmsKeyName: %v\n", attrs.Encryption.DefaultKMSKeyName)
    	}
    	if attrs.Website != nil {
    		fmt.Fprintf(w, "IndexPage: %v\n", attrs.Website.MainPageSuffix)
    		fmt.Fprintf(w, "NotFoundPage: %v\n", attrs.Website.NotFoundPage)
    	}
    	fmt.Fprintf(w, "DefaultEventBasedHold: %v\n", attrs.DefaultEventBasedHold)
    	if attrs.[RetentionPolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_RetentionPolicy) != nil {
    		fmt.Fprintf(w, "RetentionEffectiveTime: %v\n", attrs.[RetentionPolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_RetentionPolicy).EffectiveTime)
    		fmt.Fprintf(w, "RetentionPeriod: %v\n", attrs.[RetentionPolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_RetentionPolicy).RetentionPeriod)
    		fmt.Fprintf(w, "RetentionPolicyIsLocked: %v\n", attrs.[RetentionPolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_RetentionPolicy).IsLocked)
    	}
    	fmt.Fprintf(w, "ObjectRetentionMode: %v\n", attrs.ObjectRetentionMode)
    	fmt.Fprintf(w, "RequesterPays: %v\n", attrs.RequesterPays)
    	fmt.Fprintf(w, "VersioningEnabled: %v\n", attrs.VersioningEnabled)
    	if attrs.Logging != nil {
    		fmt.Fprintf(w, "LogBucket: %v\n", attrs.Logging.LogBucket)
    		fmt.Fprintf(w, "LogObjectPrefix: %v\n", attrs.Logging.LogObjectPrefix)
    	}
    	if attrs.[CORS](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_CORS) != nil {
    		fmt.Fprintln(w, "CORS:")
    		for _, v := range attrs.[CORS](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_CORS) {
    			fmt.Fprintf(w, "\tMaxAge: %v\n", v.MaxAge)
    			fmt.Fprintf(w, "\tMethods: %v\n", v.Methods)
    			fmt.Fprintf(w, "\tOrigins: %v\n", v.Origins)
    			fmt.Fprintf(w, "\tResponseHeaders: %v\n", v.ResponseHeaders)
    		}
    	}
    	if attrs.Labels != nil {
    		fmt.Fprintf(w, "\n\n\nLabels:")
    		for key, value := range attrs.Labels {
    			fmt.Fprintf(w, "\t%v = %v\n", key, value)
    		}
    	}
    	return attrs, nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
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
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def get_bucket_metadata bucket_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket  = storage.bucket bucket_name
    
      puts "ID:                       #{bucket.id}"
      puts "Name:                     #{bucket.name}"
      puts "Storage Class:            #{bucket.storage_class}"
      puts "Location:                 #{bucket.location}"
      puts "Location Type:            #{bucket.location_type}"
      puts "Cors:                     #{bucket.cors}"
      puts "Default Event Based Hold: #{bucket.[default_event_based_hold?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)}"
      puts "Default KMS Key Name:     #{bucket.[default_kms_key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)}"
      puts "Logging Bucket:           #{bucket.[logging_bucket](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)}"
      puts "Logging Prefix:           #{bucket.[logging_prefix](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)}"
      puts "Metageneration:           #{bucket.metageneration}"
      puts "Retention Effective Time: #{bucket.[retention_effective_at](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)}"
      puts "Retention Period:         #{bucket.[retention_period](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)}"
      puts "Retention Policy Locked:  #{bucket.[retention_policy_locked?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)}"
      puts "Requester Pays:           #{bucket.[requester_pays](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)}"
      puts "Self Link:                #{bucket.api_url}"
      puts "Time Created:             #{bucket.created_at}"
      puts "Versioning Enabled:       #{bucket.[versioning?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)}"
      puts "Index Page:               #{bucket.[website_main](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)}"
      puts "Not Found Page:           #{bucket.[website_404](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html)}"
      puts "Labels:"
      bucket.labels.[each](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Policy-Bindings.html) do |key, value|
        puts " - #{key} = #{value}"
      end
      puts "Lifecycle Rules:"
      bucket.lifecycle.[each](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Policy-Bindings.html) do |rule|
        puts "#{rule.[action](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket-Lifecycle-Rule.html)} - #{rule.storage_class} - #{rule.[age](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket-Lifecycle-Rule.html)} - #{rule.[matches_storage_class](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket-Lifecycle-Rule.html)}"
      end
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
