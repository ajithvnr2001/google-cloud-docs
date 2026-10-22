---
url: https://docs.cloud.google.com/storage/docs/samples/storage-object-csek-to-cmek/
title: Convert CSEK to CMEK \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:31:08.559078+00:00
---

# Convert CSEK to CMEK  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-object-csek-to-cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Convert CSEK to CMEK Stay organized with collections  Save and categorize content based on your preferences. 

Sample converts CSEK to CMEK.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Use customer-managed encryption keys](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys)



## Code sample

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name,
       std::string const& object_name, std::string const& old_csek_key_base64,
       std::string const& new_cmek_key_name) {
      StatusOr<gcs::ObjectMetadata> metadata = client.RewriteObjectBlocking(
          bucket_name, object_name, bucket_name, object_name,
          gcs::SourceEncryptionKey::FromBase64Key(old_csek_key_base64),
          gcs::DestinationKmsKeyName(new_cmek_key_name));
      if (!metadata) throw std::move(metadata).status();
    
      std::cout << "Changed object " << metadata->name() << " in bucket "
                << metadata->bucket()
                << " from using CSEK to CMEK key.\nFull Metadata: " << *metadata
                << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    using System.IO;
    
    public class ObjectCsekToCmekSample
    {
        public void ObjectCsekToCmek(
            string projectId = "your-project-id",
            string bucketName = "your-unique-bucket-name",
            string objectName = "your-object-name",
            string currrentEncryptionKey = "TIbv/fjexq+VmtXzAlc63J4z5kFmWJ6NdAPQulQBT7g=",
            string keyLocation = "us-west1",
            string kmsKeyRing = "kms-key-ring",
            string kmsKeyName = "key-name")
        {
            string keyPrefix = $"projects/{projectId}/locations/{keyLocation}";
            string fullKeyringName = $"{keyPrefix}/keyRings/{kmsKeyRing}";
            string fullKeyName = $"{fullKeyringName}/cryptoKeys/{kmsKeyName}";
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
    
            using var outputStream = new MemoryStream();
            storage.DownloadObject(bucketName, objectName, outputStream, new [DownloadObjectOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.DownloadObjectOptions.html)()
            {
                EncryptionKey = [EncryptionKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.EncryptionKey.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.EncryptionKey.html#Google_Cloud_Storage_V1_EncryptionKey_Create_System_Byte___)(Convert.FromBase64String(currrentEncryptionKey))
            });
    
            outputStream.Position = 0;
    
            storage.UploadObject(bucketName, objectName, null, outputStream, new [UploadObjectOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UploadObjectOptions.html)()
            {
                KmsKeyName = fullKeyName
            });
    
            Console.WriteLine($"Object {objectName} in bucket {bucketName} is now managed" +
                $" by the KMS key ${kmsKeyName}  instead of a customer-supplied encryption key");
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
    
    // сhangeObjectCSEKtoKMS changes the key used to encrypt an object from
    // a customer-supplied encryption key to a customer-managed encryption key.
    func сhangeObjectCSEKToKMS(w io.Wr[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer)bucket, object string, encryptionKey []byte, kmsKeyName string) error {
    	// bucket := "bucket-name"
    	// object := "object-name"
    
    	// encryptionKey is the Base64 encoded decryption key, which should be the same
    	// key originally used to encrypt the object.
    	// encryptionKey := []byte("TIbv/fjexq+VmtXzAlc63J4z5kFmWJ6NdAPQulQBT7g=")
    
    	// kmsKeyName is the name of the KMS key to manage this object with.
    	// kmsKeyName := "projects/projectId/locations/global/keyRings/keyRingID/cryptoKeys/cryptoKeyID"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    
    	o := clclient.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucket).[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)bject)
    
    	// Optional: set a generation-match precondition to avoid potential race
    	// conditions and data corruptions. The request to copy is aborted if the
    	// object's generation number does not match your precondition.
    	attrs, err := o.Attrs(ctx)
    	if err != nil {
    		return fmt.Errorf("object.Attrs: %w", err)
    	}
    	o = o.If(storage.Co[Conditions](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Conditions)enerationMatch: atattrs.[Generation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_Generation)
    
    	// You can't change an object's encryption key directly. Instead, you must
    	// rewrite the object using the new key.
    	src := o.o.[Key](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_Key)ncryptionKey)
    	c := o.o.[CopierFrom](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_CopierFrom)rc)
    	c.DestinationKMSKeyName = kmsKeyName
    	if _, err := c.Run(ctx); err != nil {
    		return fmt.Errorf("Copier.Run: %w", err)
    	}
    	fmt.Fprintf(w, "Object %v in bucket %v is now managed by the KMS key %v instead of a customer-supplied encryption key\n", object, bucket, kmsKeyName)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html);
    import com.google.cloud.storage.[BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class ChangeObjectCsekToKms {
      public static void changeObjectFromCsekToKms(
          String projectId,
          String bucketName,
          String objectName,
          String decryptionKey,
          String kmsKeyName) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The ID of your GCS object
        // String objectName = "your-object-name";
    
        // The Base64 encoded decryption key, which should be the same key originally used to encrypt
        // the object
        // String decryptionKey = "TIbv/fjexq+VmtXzAlc63J4z5kFmWJ6NdAPQulQBT7g=";
    
        // The name of the KMS key to manage this object with
        // String kmsKeyName =
        // "projects/your-project-id/locations/global/keyRings/your-key-ring/cryptoKeys/your-key";
    
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
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).[CopyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.CopyRequest.html) request =
            [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).CopyRequest.newBuilder()
                .setSource(blobId)
                .setSourceOptions([Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobSourceOption.decryptionKey(decryptionKey), precondition)
                .setTarget(blobId, [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobTargetOption.kmsKeyName(kmsKeyName))
                .build();
        storage.[copy](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_copy_com_google_cloud_storage_Storage_CopyRequest_)(request);
    
        System.out.println(
            "Object "
                + objectName
                + " in bucket "
                + bucketName
                + " is now managed by the KMS key "
                + kmsKeyName
                + " instead of a customer-supplied encryption key");
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
    
    // The Base64 encoded decryption key, which should be the same key originally
    // used to encrypt the file
    // const encryptionKey = 'TIbv/fjexq+VmtXzAlc63J4z5kFmWJ6NdAPQulQBT7g=';
    
    // The name of the KMS key to manage this file with
    // const kmsKeyName = 'projects/your-project-id/locations/global/keyRings/your-key-ring/cryptoKeys/your-key';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function changeFileCSEKToCMEK() {
      const rotateEncryptionKeyOptions = {
        kmsKeyName,
        // Optional: set a generation-match precondition to avoid potential race
        // conditions and data corruptions. The request to copy is aborted if the
        // object's generation number does not match your precondition.
        preconditionOpts: {
          ifGenerationMatch: generationMatchPrecondition,
        },
      };
    
      console.log(rotateEncryptionKeyOptions);
    
      await storage
        .bucket(bucketName)
        .file(fileName, {
          encryptionKey: Buffer.from(encryptionKey, '[base64](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/policydocument.html)'),
        })
        .[rotateEncryptionKey](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/file_2.html)({
          rotateEncryptionKeyOptions,
        });
    
      console.log(
        `file ${fileName} in bucket ${bucketName} is now managed by KMS key ${kmsKeyName} instead of customer-supplied encryption key`
      );
    }
    
    changeFileCSEKToCMEK().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Migrate an object from a Customer-Specified Encryption Key to a Customer-Managed
     * Encryption Key.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $objectName The name of your Cloud Storage object.
     *        (e.g. 'my-object')
     * @param string $decryptionKey The Base64 encoded decryption key, which should
     *        (e.g. 'TIbv/fjexq+VmtXzAlc63J4z5kFmWJ6NdAPQulQBT7g=')
     *     be the same key originally used to encrypt the object.
     * @param string $kmsKeyName The name of the KMS key to manage this object.
     *     Key names are provided in the following format:
     *     `projects/<PROJECT>/locations/<LOCATION>/keyRings/<RING_NAME>/cryptoKeys/<KEY_NAME>`.
     */
    function object_csek_to_cmek(string $bucketName, string $objectName, string $decryptionKey, string $kmsKeyName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
    
        $object = $bucket->object($objectName, [
            'encryptionKey' => $decryptionKey,
        ]);
    
        $object->rewrite($bucketName, [
            'destinationKmsKeyName' => $kmsKeyName,
        ]);
    
        printf(
            'Object %s in bucket %s is now managed by the KMS key %s instead of a customer-supplied encryption key',
            $objectName,
            $bucketName,
            $kmsKeyName
        );
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def object_csek_to_cmek(bucket_name, blob_name, encryption_key, kms_key_name):
        """Change a blob's customer-supplied encryption key to KMS key"""
        # bucket_name = "your-bucket-name"
        # blob_name = "your-object-name"
        # encryption_key = "TIbv/fjexq+VmtXzAlc63J4z5kFmWJ6NdAPQulQBT7g="
        # kms_key_name = "projects/PROJ/locations/LOC/keyRings/RING/cryptoKey/KEY"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
    
        current_encryption_key = base64.b64decode(encryption_key)
        source_blob = bucket.blob(blob_name, encryption_key=current_encryption_key)
        destination_blob = bucket.blob(blob_name, kms_key_name=kms_key_name)
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
    
        print(
            "Blob {} in bucket {} is now managed by the KMS key {} instead of a customer-supplied encryption key".format(
                blob_name, bucket_name, kms_key_name
            )
        )
        return destination_blob
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def object_csek_to_cmek bucket_name:, file_name:, encryption_key:, kms_key_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      # The ID of your GCS object
      # file_name = "your-file-name"
    
      # The Base64 encoded encryption key, which should be the same key originally used to encrypt the object
      # encryption_key = "TIbv/fjexq+VmtXzAlc63J4z5kFmWJ6NdAPQulQBT7g="
    
      # The name of the KMS key to manage this object with
      # kms_key_name = "projects/your-project-id/locations/global/keyRings/your-key-ring/cryptoKeys/your-key"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket = storage.bucket bucket_name, skip_lookup: true
    
      file = bucket.[file](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) file_name, encryption_key: encryption_key
    
      file.[rotate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-File.html) encryption_key: encryption_key, new_kms_key: kms_key_name
    
      puts "File #{file_name} in bucket #{bucket_name} is now managed by the KMS key #{kms_key_name} instead of a " \
           "customer-supplied encryption key"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
