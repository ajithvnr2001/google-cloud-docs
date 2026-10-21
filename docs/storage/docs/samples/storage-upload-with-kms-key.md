---
url: https://docs.cloud.google.com/storage/docs/samples/storage-upload-with-kms-key/
title: Upload an object with a specified KMS key \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:30:14.412184+00:00
---

# Upload an object with a specified KMS key  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-upload-with-kms-key/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Upload an object with a specified KMS key Stay organized with collections  Save and categorize content based on your preferences. 

Upload an object with a specified CMEK KMS key.

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
       std::string const& object_name, std::string const& kms_key_name) {
      gcs::ObjectWriteStream stream = client.WriteObject(
          bucket_name, object_name, gcs::KmsKeyName(kms_key_name));
    
      // Line numbers start at 1.
      for (int lineno = 1; lineno <= 10; ++lineno) {
        stream << lineno << ": placeholder text for CMEK example.\n";
      }
    
      stream.Close();
    
      StatusOr<gcs::ObjectMetadata> metadata = std::move(stream).metadata();
      if (!metadata) throw std::move(metadata).status();
    
      std::cout << "Successfully wrote to object " << metadata->name()
                << " its size is: " << metadata->size()
                << "\nFull metadata: " << *metadata << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    using System.IO;
    
    public class UploadFileWithKmsKeySample
    {
        public void UploadFileWithKmsKey(
            string projectId = "your-project-id",
            string bucketName = "your-unique-bucket-name",
            string keyLocation = "us-west1",
            string kmsKeyRing = "kms-key-ring",
            string kmsKeyName = "key-name",
            string localPath = "my-local-path/my-file-name",
            string objectName = "my-file-name")
        {
            // KMS Key identifier of an already created KMS key.
            // If you use the Google.Cloud.Kms.V1 library, you can construct these names using helper class CryptoKeyName.
            // var fullKeyName = new CryptoKeyName(projectId, keyLocation, kmsKeyRing, kmsKeyName).ToString();
            string keyPrefix = $"projects/{projectId}/locations/{keyLocation}";
            string fullKeyringName = $"{keyPrefix}/keyRings/{kmsKeyRing}";
            string fullKeyName = $"{fullKeyringName}/cryptoKeys/{kmsKeyName}";
    
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            using var fileStream = File.OpenRead(localPath);
            storage.UploadObject(bucketName, objectName, null, fileStream, new [UploadObjectOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UploadObjectOptions.html) { KmsKeyName = fullKeyName });
            Console.WriteLine($"Uploaded {objectName}.");
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
    
    // uploadWithKMSKey writes an object using Cloud KMS encryption.
    func uploadWithKMSKey(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucket, object, keyName string) error {
    	// bucket := "bucket-name"
    	// object := "object-name"
    	// keyName := "projects/projectId/locations/global/keyRings/keyRingID/cryptoKeys/cryptoKeyID"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*50)
    	defer cancel()
    
    	o := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucket).[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)(object)
    
    	// Optional: set a generation-match precondition to avoid potential race
    	// conditions and data corruptions. The request to upload is aborted if the
    	// object's generation number does not match your precondition.
    	// For an object that does not yet exist, set the DoesNotExist precondition.
    	o = o.If(storage.[Conditions](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Conditions){DoesNotExist: true})
    	// If the live object already exists in your bucket, set instead a
    	// generation-match precondition using the live object's generation number.
    	// attrs, err := o.Attrs(ctx)
    	// if err != nil {
    	// 	return fmt.Errorf("object.Attrs: %w", err)
    	// }
    	// o = o.If(storage.Conditions{GenerationMatch: attrs.Generation})
    
    	// Encrypt the object's contents.
    	wc := o.[NewWriter](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_NewWriter)(ctx)
    	wc.KMSKeyName = keyName
    	if _, err := wc.[Write](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer_Write)([]byte("top secret")); err != nil {
    		return fmt.Errorf("Writer.Write: %w", err)
    	}
    	if err := wc.Close(); err != nil {
    		return fmt.Errorf("Writer.Close: %w", err)
    	}
    	fmt.Fprintf(w, "Uploaded blob %v with KMS key.\n", object)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import static java.nio.charset.StandardCharsets.UTF_8;
    
    import com.google.cloud.storage.[BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html);
    import com.google.cloud.storage.[BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class UploadKmsEncryptedObject {
      public static void uploadKmsEncryptedObject(
          String projectId, String bucketName, String objectName, String kmsKeyName) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The ID of your GCS object
        // String objectName = "your-object-name";
    
        // The name of the KMS key to encrypt with
        // String kmsKeyName = "projects/my-project/locations/us/keyRings/my_key_ring/cryptoKeys/my_key"
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        byte[] data = "Hello, World!".getBytes(UTF_8);
    
        [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html) blobId = [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html).of(bucketName, objectName);
        [BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html) blobInfo = [BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html).newBuilder(blobId).setContentType("text/plain").build();
    
        // Optional: set a generation-match precondition to avoid potential race
        // conditions and data corruptions. The request returns a 412 error if the
        // preconditions are not met.
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobTargetOption precondition;
        if (storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName, objectName) == null) {
          // For a target object that does not yet exist, set the DoesNotExist precondition.
          // This will cause the request to fail if the object is created before the request runs.
          precondition = [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobTargetOption.doesNotExist();
        } else {
          // If the destination already exists in your bucket, instead set a generation-match
          // precondition. This will cause the request to fail if the existing object's generation
          // changes before the request runs.
          precondition =
              [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobTargetOption.generationMatch(
                  storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName, objectName).getGeneration());
        }
    
        storage.[create](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_create_com_google_cloud_storage_BlobInfo_byte___com_google_cloud_storage_Storage_BlobTargetOption____)(blobInfo, data, Storage.BlobTargetOption.kmsKeyName(kmsKeyName), precondition);
    
        System.out.println(
            "Uploaded object "
                + objectName
                + " in bucket "
                + bucketName
                + " encrypted with "
                + kmsKeyName);
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
    
    // The path to your file to upload
    // const filePath = 'path/to/your/file';
    
    // The name of the KMS-key
    // const kmsKeyName = 'my-key';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function uploadFileWithKmsKey() {
      const options = {
        kmsKeyName,
        // Optional:
        // Set a generation-match precondition to avoid potential race conditions
        // and data corruptions. The request to upload is aborted if the object's
        // generation number does not match your precondition. For a destination
        // object that does not yet exist, set the ifGenerationMatch precondition to 0
        // If the destination object already exists in your bucket, set instead a
        // generation-match precondition using its generation number.
        preconditionOpts: {ifGenerationMatch: generationMatchPrecondition},
      };
    
      await storage.bucket(bucketName).[upload](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/bucket.html)(filePath, options);
    
      console.log(`${filePath} uploaded to ${bucketName} using ${kmsKeyName}.`);
    }
    
    uploadFileWithKmsKey().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Upload a file using KMS encryption.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $objectName The name of your Cloud Storage object.
     *        (e.g. 'my-object')
     * @param string $source The path to the file to upload.
     *        (e.g. '/path/to/your/file')
     * @param string $kmsKeyName The KMS key used to encrypt objects server side.
     *     Key names are provided in the following format:
     *     `projects/<PROJECT>/locations/<LOCATION>/keyRings/<RING_NAME>/cryptoKeys/<KEY_NAME>`.
     */
    function upload_with_kms_key(string $bucketName, string $objectName, string $source, string $kmsKeyName): void
    {
        $storage = new StorageClient();
        if (!$file = fopen($source, 'r')) {
            throw new \InvalidArgumentException('Unable to open file for reading');
        }
        $bucket = $storage->bucket($bucketName);
        $object = $bucket->upload($file, [
            'name' => $objectName,
            'destinationKmsKeyName' => $kmsKeyName,
        ]);
        printf('Uploaded %s to gs://%s/%s using encryption key %s' . PHP_EOL,
            basename($source),
            $bucketName,
            $objectName,
            $kmsKeyName);
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def upload_blob_with_kms(
        bucket_name, source_file_name, destination_blob_name, kms_key_name,
    ):
        """Uploads a file to the bucket, encrypting it with the given KMS key."""
        # bucket_name = "your-bucket-name"
        # source_file_name = "local/path/to/file"
        # destination_blob_name = "storage-object-name"
        # kms_key_name = "projects/PROJ/locations/LOC/keyRings/RING/cryptoKey/KEY"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
        blob = bucket.blob(destination_blob_name, kms_key_name=kms_key_name)
    
        # Optional: set a generation-match precondition to avoid potential race conditions
        # and data corruptions. The request to upload is aborted if the object's
        # generation number does not match your precondition. For a destination
        # object that does not yet exist, set the if_generation_match precondition to 0.
        # If the destination object already exists in your bucket, set instead a
        # generation-match precondition using its generation number.
        generation_match_precondition = 0
    
        blob.[upload_from_filename](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_filename)(source_file_name, if_generation_match=generation_match_precondition)
    
        print(
            "File {} uploaded to {} with encryption key {}.".format(
                source_file_name, destination_blob_name, kms_key_name
            )
        )
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def upload_with_kms_key bucket_name:, local_file_path:, file_name: nil, kms_key:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      # The path to your file to upload
      # local_file_path = "/local/path/to/file.txt"
    
      # The ID of your GCS object
      # file_name = "your-file-name"
    
      # The name of the KMS key to manage this object with
      # kms_key = "projects/your-project-id/locations/global/keyRings/your-key-ring/cryptoKeys/your-key"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
    
      bucket = storage.bucket bucket_name, skip_lookup: true
    
      file = bucket.[create_file](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) local_file_path, file_name, kms_key: kms_key
    
      puts "Uploaded #{file.name} and encrypted service side using #{file.kms_key}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
