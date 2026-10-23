---
url: https://docs.cloud.google.com/storage/docs/samples/storage-enable-bucket-lifecycle-management/
title: Enable lifecycle management for a bucket \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:30.382631+00:00
---

# Enable lifecycle management for a bucket  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-enable-bucket-lifecycle-management/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Enable lifecycle management for a bucket Stay organized with collections  Save and categorize content based on your preferences. 

Enable lifecycle management for a Cloud Storage bucket.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Manage object lifecycles](https://docs.cloud.google.com/storage/docs/managing-lifecycles)



## Code sample

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name) {
      gcs::BucketLifecycle bucket_lifecycle_rules = gcs::BucketLifecycle{
          {gcs::LifecycleRule(gcs::LifecycleRule::ConditionConjunction(
                                  gcs::LifecycleRule::MaxAge(30),
                                  gcs::LifecycleRule::IsLive(true)),
                              gcs::LifecycleRule::Delete())}};
    
      StatusOr<gcs::BucketMetadata> updated_metadata = client.PatchBucket(
          bucket_name,
          gcs::BucketMetadataPatchBuilder().SetLifecycle(bucket_lifecycle_rules));
      if (!updated_metadata) throw std::move(updated_metadata).status();
    
      if (!updated_metadata->has_lifecycle() ||
          updated_metadata->lifecycle().rule.empty()) {
        std::cout << "Bucket lifecycle management is not enabled for bucket "
                  << updated_metadata->name() << ".\n";
        return;
      }
      std::cout << "Successfully enabled bucket lifecycle management for bucket "
                << updated_metadata->name() << ".\n";
      std::cout << "The bucket lifecycle rules are";
      for (auto const& kv : updated_metadata->lifecycle().rule) {
        std::cout << "\n " << kv.condition() << ", " << kv.action();
      }
      std::cout << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using Google.Apis.Storage.v1.Data;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    using System.Collections.Generic;
    
    public class EnableBucketLifecycleManagementSample
    {
        public Bucket EnableBucketLifecycleManagement(string bucketName = "your-unique-bucket-name")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var bucket = storage.GetBucket(bucketName);
            bucket.Lifecycle = new Bucket.LifecycleData
            {
                Rule = new List<Bucket.LifecycleData.RuleData>
                {
                    new Bucket.LifecycleData.RuleData
                    {
                        Condition = new Bucket.LifecycleData.RuleData.ConditionData { Age = 100 },
                        Action = new Bucket.LifecycleData.RuleData.ActionData { Type = "Delete" }
                    }
                }
            };
            bucket = storage.UpdateBucket(bucket);
    
            Console.WriteLine($"Lifecycle management is enabled for bucket {bucketName} and the rules are:");
            foreach (var rule in bucket.Lifecycle.Rule)
            {
                Console.WriteLine("Action:");
                Console.WriteLine($"Type: {rule.Action.Type}");
                Console.WriteLine($"Storage Class: {rule.Action.StorageClass}");
    
                Console.WriteLine("Condition:");
                Console.WriteLine($"Age: \t{rule.Condition.Age}");
                Console.WriteLine($"Created Before: \t{rule.Condition.CreatedBefore}");
                Console.WriteLine($"Time Before: \t{rule.Condition.CustomTimeBefore}");
                Console.WriteLine($"Days Since Custom Time: \t{rule.Condition.DaysSinceCustomTime}");
                Console.WriteLine($"Days Since Non-current Time: \t{rule.Condition.DaysSinceNoncurrentTime}");
                Console.WriteLine($"IsLive: \t{rule.Condition.IsLive}");
                Console.WriteLine($"Storage Class: \t{rule.Condition.MatchesStorageClass}");
                Console.WriteLine($"Noncurrent Time Before: \t{rule.Condition.NoncurrentTimeBefore}");
                Console.WriteLine($"Newer Versions: \t{rule.Condition.NumNewerVersions}");
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
    
    // enableBucketLifecycleManagement adds a lifecycle delete rule with the
    // condition that the object is 100 days old.
    func enableBucketLifecycleManagement(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucketName string) error {
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
    	bucketAttrsToUpdate := storage.[BucketAttrsToUpdate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketAttrsToUpdate){
    		Lifecycle: &storage.[Lifecycle](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Lifecycle){
    			Rules: []storage.[LifecycleRule](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_LifecycleRule){
    				{
    					Action: storage.[LifecycleAction](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_LifecycleAction){Type: "Delete"},
    					Condition: storage.[LifecycleCondition](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_LifecycleCondition){
    						AgeInDays: 100,
    					},
    				},
    			},
    		},
    	}
    
    	attrs, err := bucket.Update(ctx, bucketAttrsToUpdate)
    	if err != nil {
    		return fmt.Errorf("Bucket(%q).Update: %w", bucketName, err)
    	}
    	fmt.Fprintf(w, "Lifecycle management is enabled for bucket %v\n and the rules are:\n", bucketName)
    	for _, rule := range attrs.[Lifecycle](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Lifecycle).Rules {
    		fmt.Fprintf(w, "Action: %v\n", rule.Action)
    		fmt.Fprintf(w, "Condition: %v\n", rule.Condition)
    	}
    
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import static com.google.cloud.storage.[BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html).[LifecycleRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.LifecycleRule.html).[LifecycleAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.LifecycleRule.LifecycleAction.html);
    import static com.google.cloud.storage.[BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html).[LifecycleRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.LifecycleRule.html).[LifecycleCondition](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.LifecycleRule.LifecycleCondition.html);
    
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html).[LifecycleRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.LifecycleRule.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import com.google.common.collect.ImmutableList;
    
    public class EnableLifecycleManagement {
      public static void enableLifecycleManagement(String projectId, String bucketName) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket = storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName);
    
        // See the LifecycleRule documentation for additional info on what you can do with lifecycle
        // management rules. This one deletes objects that are over 100 days old.
        // https://googleapis.dev/java/google-cloud-clients/latest/com/google/cloud/storage/BucketInfo.LifecycleRule.html
        bucket.[toBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html#com_google_cloud_storage_Bucket_toBuilder__)()
            .setLifecycleRules(
                ImmutableList.of(
                    new [LifecycleRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.LifecycleRule.html)(
                        [LifecycleAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.LifecycleRule.LifecycleAction.html).[newDeleteAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.LifecycleRule.LifecycleAction.html#com_google_cloud_storage_BucketInfo_LifecycleRule_LifecycleAction_newDeleteAction__)(),
                        [LifecycleCondition](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.LifecycleRule.LifecycleCondition.html).newBuilder().[setAge](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.LifecycleRule.LifecycleCondition.Builder.html#com_google_cloud_storage_BucketInfo_LifecycleRule_LifecycleCondition_Builder_setAge_java_lang_Integer_)(100).build())))
            .build()
            .update();
    
        System.out.println("Lifecycle management was enabled and configured for bucket " + bucketName);
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
    
    async function enableBucketLifecycleManagement() {
      const [metadata] = await storage.bucket(bucketName).[addLifecycleRule](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/bucket.html)({
        action: {
          type: 'Delete',
        },
        condition: {age: 100},
      });
    
      console.log(
        `Lifecycle management is enabled for bucket ${bucketName} and the rules are:`
      );
    
      console.log(metadata.lifecycle.rule);
    }
    
    enableBucketLifecycleManagement().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    use Google\Cloud\Storage\Bucket;
    
    /**
     * Enable bucket lifecycle management.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     */
    function enable_bucket_lifecycle_management(string $bucketName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
    
        $lifecycle = Bucket::lifecycle()
            ->addDeleteRule([
                'age' => 100
            ]);
    
        $bucket->update([
            'lifecycle' => $lifecycle
        ]);
    
        $lifecycle = $bucket->currentLifecycle();
    
        printf('Lifecycle management is enabled for bucket %s and the rules are:' . PHP_EOL, $bucketName);
        foreach ($lifecycle as $rule) {
            print_r($rule);
            print(PHP_EOL);
        }
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def enable_bucket_lifecycle_management(bucket_name):
        """Enable lifecycle management for a bucket"""
        # bucket_name = "my-bucket"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
        bucket = storage_client.[get_bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_get_bucket)(bucket_name)
        rules = bucket.[lifecycle_rules](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_lifecycle_rules)
    
        print(f"Lifecycle management rules for bucket {bucket_name} are {list(rules)}")
        bucket.[add_lifecycle_delete_rule](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_add_lifecycle_delete_rule)(age=2)
        bucket.patch()
    
        rules = bucket.[lifecycle_rules](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_lifecycle_rules)
        print(f"Lifecycle management is enable for bucket {bucket_name} and the rules are {list(rules)}")
    
        return bucket
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def enable_bucket_lifecycle_management bucket_name:
      # Enable lifecycle management for a bucket
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket = storage.bucket bucket_name
    
      rules = bucket.lifecycle do |l|
        l.[add_delete_rule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket-Lifecycle.html) age: 2
      end
    
      puts "Lifecycle management is enabled for bucket #{bucket_name} and the rules are #{rules}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
