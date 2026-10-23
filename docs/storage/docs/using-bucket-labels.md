---
url: https://docs.cloud.google.com/storage/docs/using-bucket-labels/
title: Using bucket labels \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:20.392735+00:00
---

# Using bucket labels  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/using-bucket-labels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Using bucket labels Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to add, modify, remove, and view the [labels](https://docs.cloud.google.com/storage/docs/tags-and-labels#bucket-labels) set on a [bucket](https://docs.cloud.google.com/storage/docs/buckets) in Cloud Storage.

## Required roles

In order to get the required permissions for adding and managing bucket labels, ask your administrator to grant you the Storage Admin (`roles/storage.admin`) IAM role on the bucket.

This [predefined role](https://docs.cloud.google.com/iam/docs/understanding-roles) contains the permissions required to add and manage bucket labels. To see the exact permissions that are required, expand the **Required permissions** section:

#### Required permissions

  * `storage.buckets.get`
  * `storage.buckets.list`
    * This permission is only required if you plan on using the Google Cloud console to perform the instructions on this page.
  * `storage.buckets.update`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

For instructions on granting roles on buckets, see [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).

## Add, modify, or remove a bucket's labels

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket for which you want to add, modify, or remove labels.

  3. In the **Bucket details** page, click the **Configuration** tab.

  4. Click the **Edit** icon (_edit_) for **Labels**.

The label editor window appears.

     1. To add a label, click the _add_box_ **Add label** button, and specify a `key` and a `value` for your label.

     2. To modify an existing label, click its **Value** and a enter a new value.

     3. To remove a label, click the **Trash icon** associated with the label you want to remove.

  5. Click **Save**.




To learn how to get detailed error information about failed Cloud Storage operations in the Google Cloud console, see [Troubleshooting](https://docs.cloud.google.com/storage/docs/troubleshooting#trouble-console).

### Command line

To add a new label or update an existing label, use the [`gcloud storage buckets update`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/update) command with the `--update-labels` flag. For example:
    
    
    gcloud storage buckets update gs://BUCKET_NAME --update-labels=KEY_1=VALUE_1

Where

  * `BUCKET_NAME` is the name of the bucket that the label applies to. For example, `my-bucket`.
  * `KEY_1` is the key name for your label. For example, `pet`.
  * `VALUE_1` is the value for your label. For example, `dog`.



To remove an existing label, use the `-remove-labels` flag. For example:
    
    
    gcloud storage buckets update gs://BUCKET_NAME --remove-labels=KEY_1

You can change multiple labels using the previous commands by including the labels in a comma-separated list within the relevant flag. For example, `--update-labels=blue-key=cyan,red-key=ruby`.

To remove all labels attached to a bucket, use the following command:
    
    
    gcloud storage buckets update gs://BUCKET_NAME --clear-labels

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample adds the specified label to a bucket, or modifies the label if it already exists for the bucket:
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name,
       std::string const& label_key, std::string const& label_value) {
      StatusOr<gcs::BucketMetadata> updated = client.PatchBucket(
          bucket_name,
          gcs::BucketMetadataPatchBuilder().SetLabel(label_key, label_value));
      if (!updated) throw std::move(updated).status();
    
      std::cout << "Successfully set label " << label_key << " to " << label_value
                << " on bucket  " << updated->name() << ".";
      std::cout << " The bucket labels are now:";
      for (auto const& kv : updated->labels()) {
        std::cout << "\n  " << kv.first << ": " << kv.second;
      }
      std::cout << "\n";
    }

The following sample removes the specified label from a bucket:
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name,
       std::string const& label_key) {
      StatusOr<gcs::BucketMetadata> updated = client.PatchBucket(
          bucket_name, gcs::BucketMetadataPatchBuilder().ResetLabel(label_key));
      if (!updated) throw std::move(updated).status();
    
      std::cout << "Successfully reset label " << label_key << " on bucket  "
                << updated->name() << ".";
      if (updated->labels().empty()) {
        std::cout << " The bucket now has no labels.\n";
        return;
      }
      std::cout << " The bucket labels are now:";
      for (auto const& kv : updated->labels()) {
        std::cout << "\n  " << kv.first << ": " << kv.second;
      }
      std::cout << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample adds the specified label to a bucket, or modifies the label if it already exists for the bucket:
    
    
    using Google.Apis.Storage.v1.Data;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    using System.Collections.Generic;
    
    public class BucketAddLabelSample
    {
        public Bucket BucketAddLabel(
            string bucketName = "your-bucket-name",
            string labelKey = "label-key-to-add",
            string labelValue = "label-value-to-add")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var bucket = storage.GetBucket(bucketName);
    
            if (bucket.Labels == null)
            {
                bucket.Labels = new Dictionary<string, string>();
            }
            bucket.Labels.Add(labelKey, labelValue);
    
            bucket = storage.UpdateBucket(bucket);
            Console.WriteLine($"Added label {labelKey} with value {labelValue} to bucket {bucketName}.");
            return bucket;
        }
    }

The following sample removes the specified label from a bucket:
    
    
    using Google.Apis.Storage.v1.Data;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class BucketRemoveLabelSample
    {
        public Bucket BucketRemoveLabel(string bucketName = "your-bucket-name", string labelKey = "label-key-to-remove")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var bucket = storage.GetBucket(bucketName);
    
            if (bucket.Labels != null && bucket.Labels.Keys.Contains(labelKey))
            {
                bucket.Labels.Remove(labelKey);
                bucket = storage.UpdateBucket(bucket);
                Console.WriteLine($"Removed label {labelKey} from bucket {bucketName}.");
            }
            else
            {
                Console.WriteLine($"No such label available on {bucketName}.");
            }
            return bucket;
        }
    }

### Go

For more information, see the [Cloud Storage Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storage). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample adds the specified label to a bucket, or modifies the label if it already exists for the bucket:
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/storage"
    )
    
    // addBucketLabel adds a label on a bucket.
    func addBucketLabel(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucketName, labelName, labelValue string) error {
    	// bucketName := "bucket-name"
    	// labelName := "label-name"
    	// labelValue := "label-value"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    
    	bucket := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucketName)
    	bucketAttrsToUpdate := storage.[BucketAttrsToUpdate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketAttrsToUpdate){}
    	bucketAttrsToUpdate.[SetLabel](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketAttrsToUpdate_SetLabel)(labelName, labelValue)
    	if _, err := bucket.Update(ctx, bucketAttrsToUpdate); err != nil {
    		return fmt.Errorf("Bucket(%q).Update: %w", bucketName, err)
    	}
    	fmt.Fprintf(w, "Added label %q with value %q to bucket %v\n", labelName, labelValue, bucketName)
    	return nil
    }
    

The following sample removes the specified label from a bucket:
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/storage"
    )
    
    // removeBucketLabel removes a label on a bucket.
    func removeBucketLabel(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucketName, labelName string) error {
    	// bucketName := "bucket-name"
    	// labelName := "label-name"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    
    	bucket := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucketName)
    	bucketAttrsToUpdate := storage.[BucketAttrsToUpdate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketAttrsToUpdate){}
    	bucketAttrsToUpdate.[DeleteLabel](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketAttrsToUpdate_DeleteLabel)(labelName)
    	if _, err := bucket.Update(ctx, bucketAttrsToUpdate); err != nil {
    		return fmt.Errorf("Bucket(%q).Update: %w", bucketName, err)
    	}
    	fmt.Fprintf(w, "Removed label %q from bucket %v\n", labelName, bucketName)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample adds the specified label to a bucket, or modifies the label if it already exists for the bucket:
    
    
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import java.util.HashMap;
    import java.util.Map;
    
    public class AddBucketLabel {
      public static void addBucketLabel(
          String projectId, String bucketName, String labelKey, String labelValue) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The key of the label to add
        // String labelKey = "label-key-to-add";
    
        // The value of the label to add
        // String labelValue = "label-value-to-add";
    
        Map<String, String> newLabels = new HashMap<>();
        newLabels.put(labelKey, labelValue);
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket = storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName);
        Map<String, String> labels = bucket.getLabels();
        if (labels != null) {
          newLabels.putAll(labels);
        }
        bucket.[toBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html#com_google_cloud_storage_Bucket_toBuilder__)().setLabels(newLabels).build().update();
    
        System.out.println(
            "Added label " + labelKey + " with value " + labelValue + " to bucket " + bucketName + ".");
      }
    }

The following sample removes the specified label from a bucket:
    
    
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import java.util.HashMap;
    import java.util.Map;
    
    public class RemoveBucketLabel {
      public static void removeBucketLabel(String projectId, String bucketName, String labelKey) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The key of the label to remove from the bucket
        // String labelKey = "label-key-to-remove";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
    
        Map<String, String> labelsToRemove = new HashMap<>();
        labelsToRemove.put(labelKey, null);
    
        [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket = storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName);
        Map<String, String> labels;
        if (bucket.getLabels() == null) {
          labels = new HashMap<>();
        } else {
          labels = new HashMap(bucket.getLabels());
        }
        labels.putAll(labelsToRemove);
        bucket.[toBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html#com_google_cloud_storage_Bucket_toBuilder__)().setLabels(labels).build().update();
    
        System.out.println("Removed label " + labelKey + " from bucket " + bucketName);
      }
    }

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample adds the specified label to a bucket, or modifies the label if it already exists for the bucket:
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The ID of your GCS bucket
    // const bucketName = 'your-unique-bucket-name';
    
    // The key of the label to add
    // const labelKey = 'label-key-to-add';
    
    // The value of the label to add
    // const labelValue = 'label-value-to-add';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    const labels = {
      [labelKey]: labelValue,
    };
    
    async function addBucketLabel() {
      await storage.bucket(bucketName).setMetadata({labels});
      console.log(`Added label to bucket ${bucketName}`);
    }
    
    addBucketLabel().catch(console.error);

The following sample removes the specified label from a bucket:
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The ID of your GCS bucket
    // const bucketName = 'your-unique-bucket-name';
    
    // The key of the label to remove from the bucket
    // const labelKey = 'label-key-to-remove';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function removeBucketLabel() {
      const labels = {};
      // To remove a label set the value of the key to null.
      labels[labelKey] = null;
      await storage.bucket(bucketName).setMetadata({labels});
      console.log(`Removed labels from bucket ${bucketName}`);
    }
    
    removeBucketLabel().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample adds the specified label to a bucket, or modifies the label if it already exists for the bucket:
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Adds or updates a bucket label.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $labelName The name of the label to add.
     *        (e.g. 'label-key-to-add')
     * @param string $labelValue The value of the label to add.
     *        (e.g. 'label-value-to-add')
     */
    function add_bucket_label(string $bucketName, string $labelName, string $labelValue): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
        $newLabels = [$labelName => $labelValue];
        $bucket->update(['labels' => $newLabels]);
        printf('Added label %s (%s) to %s' . PHP_EOL, $labelName, $labelValue, $bucketName);
    }

The following sample removes the specified label from a bucket:
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Removes a label from a bucket.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $labelName The name of the label to remove.
     *        (e.g. 'label-key-to-remove')
     */
    function remove_bucket_label(string $bucketName, string $labelName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
        $labels = [$labelName => null];
        $bucket->update(['labels' => $labels]);
        printf('Removed label %s from %s' . PHP_EOL, $labelName, $bucketName);
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample adds the specified label to a bucket, or modifies the label if it already exists for the bucket:
    
    
    import pprint
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def add_bucket_label(bucket_name):
        """Add a label to a bucket."""
        # bucket_name = "your-bucket-name"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
        bucket = storage_client.[get_bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_get_bucket)(bucket_name)
        labels = bucket.[labels](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_labels)
        labels["example"] = "label"
        bucket.[labels](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_labels) = labels
        bucket.patch()
    
        print(f"Updated labels on {bucket.name}.")
        pprint.pprint(bucket.[labels](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_labels))
    
    

The following sample removes the specified label from a bucket:
    
    
    import pprint
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def remove_bucket_label(bucket_name):
        """Remove a label from a bucket."""
        # bucket_name = "your-bucket-name"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[get_bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_get_bucket)(bucket_name)
    
        labels = bucket.[labels](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_labels)
    
        if "example" in labels:
            del labels["example"]
    
        bucket.[labels](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_labels) = labels
        bucket.patch()
    
        print(f"Removed labels on {bucket.name}.")
        pprint.pprint(bucket.[labels](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_labels))
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample adds the specified label to a bucket, or modifies the label if it already exists for the bucket:
    
    
    def add_bucket_label bucket_name:, label_key:, label_value:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      # The key of the label to add
      # label_key = "label-key-to-add"
    
      # The value of the label to add
      # label_value = "label-value-to-add"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket  = storage.bucket bucket_name
    
      bucket.update do |bucket|
        bucket.labels[label_key] = label_value
      end
    
      puts "Added label #{label_key} with value #{label_value} to #{bucket_name}"
    end

The following sample removes the specified label from a bucket:
    
    
    def remove_bucket_label bucket_name:, label_key:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      # The key of the label to remove from the bucket
      # label_key = "label-key-to-remove"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket  = storage.bucket bucket_name
    
      bucket.update do |bucket|
        bucket.labels[label_key] = nil
      end
    
      puts "Deleted label #{label_key} from #{bucket_name}"
    end

### Rust

The following sample adds the specified label to a bucket, or modifies the label if it already exists for the bucket:
    
    
    use google_cloud_storage::client::StorageControl;
    use google_cloud_wkt::FieldMask;
    
    pub async fn sample(
        client: &StorageControl,
        bucket_id: &str,
        label_key: &str,
        label_value: &str,
    ) -> anyhow::Result<()> {
        let bucket = client
            .get_bucket()
            .set_name(format!("projects/_/buckets/{bucket_id}"))
            .send()
            .await?;
        let metageneration = bucket.metageneration;
        let mut labels = bucket.labels.clone();
        labels.insert(label_key.to_string(), label_value.to_string());
    
        let bucket = client
            .update_bucket()
            .set_bucket(bucket.set_labels(labels))
            .set_if_metageneration_match(metageneration)
            .set_update_mask(FieldMask::default().set_paths(["labels"]))
            .send()
            .await?;
        println!("Successfully added label {label_key}={label_value} to bucket {bucket_id}");
        println!("{:?}", bucket.labels);
        Ok(())
    }

The following sample removes the specified label from a bucket:
    
    
    use google_cloud_storage::client::StorageControl;
    use google_cloud_wkt::FieldMask;
    
    pub async fn sample(
        client: &StorageControl,
        bucket_id: &str,
        label_key: &str,
    ) -> anyhow::Result<()> {
        let bucket = client
            .get_bucket()
            .set_name(format!("projects/_/buckets/{bucket_id}"))
            .send()
            .await?;
        let metageneration = bucket.metageneration;
        let mut labels = bucket.labels.clone();
        labels.remove(label_key);
    
        let bucket = client
            .update_bucket()
            .set_bucket(bucket.set_labels(labels))
            .set_if_metageneration_match(metageneration)
            .set_update_mask(FieldMask::default().set_paths(["labels"]))
            .send()
            .await?;
        println!("Successfully removed label {label_key} from bucket {bucket_id}");
        println!("{:?}", bucket.labels);
        Ok(())
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the following information:
         
         {
           "labels": {
             "KEY_1": "VALUE_1"
           }
         }

Where

     * `KEY_1` is the key name for your label. For example, `pet`.
     * `VALUE_1` is the value for your label. For example, `dog`. If you want to remove a key, use `null` in place of `"<var>VALUE_1</var>"`.
  3. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`PATCH` Bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/patch) request:
         
         curl -X PATCH --data-binary @JSON_FILE_NAME \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME?fields=labels"

Where:

     * `JSON_FILE_NAME` is the path for the JSON file that you created in Step 2.
     * `BUCKET_NAME` is the name of the bucket that the label applies to. For example, `my-bucket`.



You can add, edit, or remove multiple `key:value` pairs in a request.

### XML API

**Note:** A label setting request using the XML API replaces all existing labels applied to the specified bucket with the labels included in the request. If there are labels applied to the bucket that you want to keep, specify them in your request.

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create an XML file that contains the following information:
         
         <Tagging>
           <TagSet>
             <Tag>
               <Key>KEY_1</Key>
               <Value>VALUE_1</Value>
             </Tag>
           </TagSet>
         </Tagging>

Where:

     * `KEY_1` is the key name for your label. For example, `pet`.
     * `VALUE_1` is the value for your label. For example, `dog`.

Note that you can add multiple `<Tag>` elements in a request. If you want to remove all labels on a bucket, use a single, empty `<Tag>` element in the file:
    
    <Tagging>
      <TagSet>
        <Tag>
        </Tag>
      </TagSet>
    </Tagging>

  3. Use [`cURL`](http://curl.haxx.se/) to call the [XML API](https://docs.cloud.google.com/storage/docs/xml-api/overview) with a [`PUT` Bucket](https://docs.cloud.google.com/storage/docs/xml-api/put-bucket-metadata) request and `tagging` query string parameter:
         
         curl -X PUT --data-binary @XML_FILE_NAME \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storage.googleapis.com/BUCKET_NAME?tagging"

Where:

     * `XML_FILE_NAME` is the path for the XML file that you created in Step 2.
     * `BUCKET_NAME` is the name of the bucket that the label applies to. For example, `my-bucket`.



## View bucket labels

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click the name of the bucket whose labels you want to view.

  3. Click the **Configuration** tab.




The labels set on the bucket are listed in the **Labels** field.

To learn how to get detailed error information about failed Cloud Storage operations in the Google Cloud console, see [Troubleshooting](https://docs.cloud.google.com/storage/docs/troubleshooting#trouble-console).

### Command line

Use the [`gcloud storage buckets describe`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/describe) command with the `--format` flag:
    
    
    gcloud storage buckets describe gs://BUCKET_NAME --format="default(labels)"

Where `BUCKET_NAME` is the name of the bucket whose labels you want to view. For example, `my-bucket`.

If successful and labels exist for the bucket, the response is similar to the following:
    
    
    labels:
      red-key: ruby
      blue-key: cyan

If successful and labels to not exist for the bucket, the response is similar to the following:
    
    
    null

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

To view a bucket's labels, follow the instructions for displaying a bucket's metadata and look for the label field in the response. 
    
    
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

To view a bucket's labels, follow the instructions for displaying a bucket's metadata and look for the label field in the response. 
    
    
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

To view a bucket's labels, follow the instructions for displaying a bucket's metadata and look for the label field in the response. 
    
    
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

To view a bucket's labels, follow the instructions for displaying a bucket's metadata and look for the label field in the response. 
    
    
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

To view a bucket's labels, follow the instructions for displaying a bucket's metadata and look for the label field in the response. 
    
    
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

To view a bucket's labels, follow the instructions for displaying a bucket's metadata and look for the label field in the response. 
    
    
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

To view a bucket's labels, follow the instructions for displaying a bucket's metadata and look for the label field in the response. 
    
    
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

To view a bucket's labels, follow the instructions for displaying a bucket's metadata and look for the label field in the response. 
    
    
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

### Rust

To view a bucket's labels, follow the instructions for displaying a bucket's metadata and look for the label field in the response. 
    
    
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

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`GET` Bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/get) request that includes the `fields=labels` query string parameter:
         
         curl -X GET \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME?fields=labels"

Where `BUCKET_NAME` is the name of the bucket whose labels you want to view. For example, `my-bucket`.




The response looks like the following example:
    
    
    {
      "labels" : {
         (your_label_key): your_label_value
       },
    }

### XML API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [XML API](https://docs.cloud.google.com/storage/docs/xml-api/overview) with a [`GET` Bucket](https://docs.cloud.google.com/storage/docs/xml-api/get-bucket-metadata) request and `tagging` query string parameter:
         
         curl -X GET \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storage.googleapis.com/BUCKET_NAME?tagging"

Where `BUCKET_NAME` is the name of the bucket whose labels you want to view. For example, `my-bucket`.




The response looks like the following example:
    
    
    <Tagging>
      <TagSet>
        <Tag>
          <Key>your_label_key</Key>
          <Value>your_label_value</Value>
        </Tag>
      </TagSet>
    </Tagging>

## What's next

  * Learn about [bucket tags](https://docs.cloud.google.com/storage/docs/tags-and-labels#tags).
  * [Get additional bucket metadata](https://docs.cloud.google.com/storage/docs/getting-bucket-metadata).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
