---
url: https://docs.cloud.google.com/storage/docs/samples/storage-rotate-encryption-key/
title: Rotate an encryption key \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:52.424761+00:00
---

# Rotate an encryption key  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-rotate-encryption-key/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Rotate an encryption key Stay organized with collections  Save and categorize content based on your preferences. 

Rotate an encryption key.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Use customer-supplied encryption keys](https://docs.cloud.google.com/storage/docs/encryption/using-customer-supplied-keys)



## Code sample

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name,
       std::string const& object_name, std::string const& old_key_base64,
       std::string const& new_key_base64) {
      StatusOr<gcs::ObjectMetadata> object_metadata =
          client.RewriteObjectBlocking(
              bucket_name, object_name, bucket_name, object_name,
              gcs::SourceEncryptionKey::FromBase64Key(old_key_base64),
              gcs::EncryptionKey::FromBase64Key(new_key_base64));
      if (!object_metadata) throw std::move(object_metadata).status();
    
      std::cout << "Rotated key on object " << object_metadata->name()
                << " in bucket " << object_metadata->bucket()
                << "\nFull Metadata: " << *object_metadata << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    using System.IO;
    
    public class ObjectRotateEncryptionKeySample
    {
        public void ObjectRotateEncryptionKey(
            string bucketName = "your-unique-bucket-name",
            string objectName = "your-object-name",
            string currrentEncryptionKey = "TIbv/fjexq+VmtXzAlc63J4z5kFmWJ6NdAPQulQBT7g=",
            string newEncryptionKey = "ARbt/judaq+VmtXzAsc83J4z5kFmWJ6NdAPQuleuB7g=")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
    
            using var outputStream = new MemoryStream();
            storage.DownloadObject(bucketName, objectName, outputStream, new [DownloadObjectOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.DownloadObjectOptions.html)()
            {
                EncryptionKey = [EncryptionKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.EncryptionKey.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.EncryptionKey.html#Google_Cloud_Storage_V1_EncryptionKey_Create_System_Byte___)(Convert.FromBase64String(currrentEncryptionKey))
            });
    
            outputStream.Position = 0;
    
            storage.UploadObject(bucketName, objectName, null, outputStream, new [UploadObjectOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UploadObjectOptions.html)()
            {
                EncryptionKey = [EncryptionKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.EncryptionKey.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.EncryptionKey.html#Google_Cloud_Storage_V1_EncryptionKey_Create_System_Byte___)(Convert.FromBase64String(newEncryptionKey))
            });
    
            Console.WriteLine($"Rotated encryption key for object  {objectName} in bucket {bucketName}");
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
    
    // rotateEncryptionKey encrypts an object with the newKey.
    func rotateEncryptionKey(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucket, object string, key, newKey []byte) error {
    	// bucket := "bucket-name"
    	// object := "object-name"
    	// key := []byte("encryption-key")
    	// newKey := []byte("new-encryption-key")
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    
    	o := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucket).[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)(object)
    
    	// Optional: set a generation-match precondition to avoid potential race
    	// conditions and data corruptions. The request to copy is aborted if the
    	// object's generation number does not match your precondition.
    	attrs, err := o.Attrs(ctx)
    	if err != nil {
    		return fmt.Errorf("object.Attrs: %w", err)
    	}
    	o = o.If(storage.[Conditions](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Conditions){GenerationMatch: attrs.[Generation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_Generation)})
    
    	// You can't change an object's encryption key directly, you must rewrite the
    	// object using the new key.
    	_, err = o.[Key](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_Key)(newKey).[CopierFrom](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_CopierFrom)(o.[Key](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_Key)(key)).Run(ctx)
    	if err != nil {
    		return fmt.Errorf("Key(%q).CopierFrom(%q).Run: %w", newKey, key, err)
    	}
    	fmt.Fprintf(w, "Key rotation complete for blob %v.\n", object)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html);
    import com.google.cloud.storage.[BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class RotateObjectEncryptionKey {
      public static void rotateObjectEncryptionKey(
          String projectId,
          String bucketName,
          String objectName,
          String oldEncryptionKey,
          String newEncryptionKey) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The ID of your GCS object
        // String objectName = "your-object-name";
    
        // The Base64 encoded AES-256 encryption key originally used to encrypt the object. See the
        // documentation
        // on Customer-Supplied Encryption keys for more info:
        // https://cloud.google.com/storage/docs/encryption/using-customer-supplied-keys
        // String oldEncryptionKey = "TIbv/fjexq+VmtXzAlc63J4z5kFmWJ6NdAPQulQBT7g="
    
        // The new encryption key to use
        // String newEncryptionKey = "0mMWhFvQOdS4AmxRpo8SJxXn5MjFhbz7DkKBUdUIef8="
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html) blobId = [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html).of(bucketName, objectName);
        [Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html) blob = storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(blobId);
        if (blob == null) {
          System.out.println("The object " + objectName + " wasn't found in " + bucketName);
          return;
        }
    
        // Optional: set a generation-match precondition to avoid potential race
        // conditions and data corruptions. The request to upload returns a 412 error if
        // the object's generation number does not match your precondition.
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobSourceOption precondition =
            [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobSourceOption.generationMatch(blob.getGeneration());
    
        // You can't change an object's encryption key directly, the only way is to overwrite the object
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).[CopyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.CopyRequest.html) request =
            [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).CopyRequest.newBuilder()
                .setSource(blobId)
                .setSourceOptions(
                    [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobSourceOption.decryptionKey(oldEncryptionKey), precondition)
                .setTarget(blobId, [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobTargetOption.encryptionKey(newEncryptionKey))
                .build();
        storage.[copy](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_copy_com_google_cloud_storage_Storage_CopyRequest_)(request);
    
        System.out.println(
            "Rotated encryption key for object " + objectName + "in bucket " + bucketName);
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
    
    // The ID of your GCS file
    // const fileName = 'your-file-name';
    
    // The Base64 encoded AES-256 encryption key originally used to encrypt the
    // object. See the documentation on Customer-Supplied Encryption keys for
    // more info:
    // https://cloud.google.com/storage/docs/encryption/using-customer-supplied-keys
    // The Base64 encoded AES-256 encryption key originally used to encrypt the
    // const oldKey = 'TIbv/fjexq+VmtXzAlc63J4z5kFmWJ6NdAPQulQBT7g=';
    
    // The new encryption key to use
    // const newKey = '0mMWhFvQOdS4AmxRpo8SJxXn5MjFhbz7DkKBUdUIef8=';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function rotateEncryptionKey() {
      const rotateEncryptionKeyOptions = {
        encryptionKey: Buffer.from(newKey, '[base64](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/policydocument.html)'),
    
        // Optional: set a generation-match precondition to avoid potential race
        // conditions and data corruptions. The request to copy is aborted if the
        // object's generation number does not match your precondition.
        preconditionOpts: {
          ifGenerationMatch: generationMatchPrecondition,
        },
      };
      await storage
        .bucket(bucketName)
        .file(fileName, {
          encryptionKey: Buffer.from(oldKey, '[base64](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/policydocument.html)'),
        })
        .[rotateEncryptionKey](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/file_2.html)({
          rotateEncryptionKeyOptions,
        });
    
      console.log('Encryption key rotated successfully');
    }
    
    rotateEncryptionKey().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Change the encryption key used to store an existing object.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $objectName The name of your Cloud Storage object.
     *        (e.g. 'my-object')
     * @param string $oldBase64EncryptionKey The Base64 encoded AES-256 encryption
     *     key originally used to encrypt the object. See the documentation on
     *     Customer-Supplied Encryption keys for more info:
     *     https://cloud.google.com/storage/docs/encryption/using-customer-supplied-keys
     *        (e.g. 'TIbv/fjexq+VmtXzAlc63J4z5kFmWJ6NdAPQulQBT7g=')
     * @param string $newBase64EncryptionKey The new base64 encoded encryption key.
     *        (e.g. '0mMWhFvQOdS4AmxRpo8SJxXn5MjFhbz7DkKBUdUIef8=')
     */
    function rotate_encryption_key(
        string $bucketName,
        string $objectName,
        string $oldBase64EncryptionKey,
        string $newBase64EncryptionKey
    ): void {
        $storage = new StorageClient();
        $object = $storage->bucket($bucketName)->object($objectName);
    
        $rewrittenObject = $object->rewrite($bucketName, [
            'encryptionKey' => $oldBase64EncryptionKey,
            'destinationEncryptionKey' => $newBase64EncryptionKey,
        ]);
    
        printf('Rotated encryption key for object gs://%s/%s' . PHP_EOL,
            $bucketName, $objectName);
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import base64
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def rotate_encryption_key(
        bucket_name, blob_name, base64_encryption_key, base64_new_encryption_key
    ):
        """Performs a key rotation by re-writing an encrypted blob with a new
        encryption key."""
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
        current_encryption_key = base64.b64decode(base64_encryption_key)
        new_encryption_key = base64.b64decode(base64_new_encryption_key)
    
        # Both source_blob and destination_blob refer to the same storage object,
        # but destination_blob has the new encryption key.
        source_blob = bucket.blob(
            blob_name, encryption_key=current_encryption_key
        )
        destination_blob = bucket.blob(
            blob_name, encryption_key=new_encryption_key
        )
        generation_match_precondition = None
        token = None
    
        # Optional: set a generation-match precondition to avoid potential race conditions
        # and data corruptions. The request to rewrite is aborted if the object's
        # generation number does not match your precondition.
        source_blob.reload()  # Fetch blob metadata to use in generation_match_precondition.
        generation_match_precondition = source_blob.generation
    
        while True:
            token, bytes_rewritten, total_bytes = destination_blob.[rewrite](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_rewrite)(
                source_blob, token=token, if_generation_match=generation_match_precondition
            )
            if token is None:
                break
    
        print(f"Key rotation complete for Blob {blob_name}")
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def rotate_encryption_key bucket_name:, file_name:, current_encryption_key:, new_encryption_key:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      # The ID of your GCS object
      # file_name = "your-file-name"
    
      # The Base64 encoded AES-256 encryption key originally used to encrypt the object.
      # See the documentation on Customer-Supplied Encryption keys for more info:
      # https://cloud.google.com/storage/docs/encryption/using-customer-supplied-keys
      # current_encryption_key = "TIbv/fjexq+VmtXzAlc63J4z5kFmWJ6NdAPQulQBT7g="
    
      # The new encryption key to use
      # new_encryption_key = "0mMWhFvQOdS4AmxRpo8SJxXn5MjFhbz7DkKBUdUIef8="
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket  = storage.bucket bucket_name, skip_lookup: true
      file    = bucket.[file](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) file_name, encryption_key: current_encryption_key
    
      file.[rotate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-File.html) encryption_key:     current_encryption_key,
                  new_encryption_key: new_encryption_key
    
      puts "The encryption key for #{file.name} in #{bucket.name} was rotated."
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
