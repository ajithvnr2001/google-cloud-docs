---
url: https://docs.cloud.google.com/storage/docs/samples/storage-download-encrypted-file/
title: Download a CSEK-encrypted object \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:50.785048+00:00
---

# Download a CSEK-encrypted object  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-download-encrypted-file/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Download a CSEK-encrypted object Stay organized with collections  Save and categorize content based on your preferences. 

Download a CSEK-encrypted object.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Use customer-supplied encryption keys](https://docs.cloud.google.com/storage/docs/encryption/using-customer-supplied-keys)



## Code sample

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    [](gcs::Client client, std::string const& bucket_name,
       std::string const& object_name, std::string const& base64_aes256_key) {
      gcs::ObjectReadStream stream =
          client.ReadObject(bucket_name, object_name,
                            gcs::EncryptionKey::FromBase64Key(base64_aes256_key));
    
      std::string data(std::istreambuf_iterator<char>{stream}, {});
      if (stream.bad()) throw google::cloud::Status(stream.status());
      std::cout << "The object contents are: " << data << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    using System.IO;
    
    public class DownloadEncryptedFileSample
    {
        public void DownloadEncryptedFile(
            string key = "3eFsTXPvqi3BpT2ipFCGirslh1Jgc6ikjoAu2oQ5JcI=",
            string bucketName = "your-unique-bucket-name",
            string objectName = "my-file-name",
            string localPath = "my-local-path/my-file-name")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            using var outputFile = File.OpenWrite(localPath);
            storage.DownloadObject(bucketName, objectName, outputFile, new [DownloadObjectOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.DownloadObjectOptions.html)
            {
                EncryptionKey = [EncryptionKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.EncryptionKey.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.EncryptionKey.html#Google_Cloud_Storage_V1_EncryptionKey_Create_System_Byte___)(Convert.FromBase64String(key))
            });
            Console.WriteLine($"Downloaded {objectName} to {localPath}.");
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
    
    // downloadEncryptedFile reads an encrypted object.
    func downloadEncryptedFile(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucket, object string, secretKey []byte) ([]byte, error) {
    	// bucket := "bucket-name"
    	// object := "object-name"
    	// key := []byte("secret-encryption-key")
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	obj := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucket).[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)(object)
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*50)
    	defer cancel()
    
    	rc, err := obj.[Key](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_Key)(secretKey).[NewReader](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_NewReader)(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("Object(%q).Key(%q).NewReader: %w", object, secretKey, err)
    	}
    	defer rc.Close()
    
    	data, err := io.ReadAll(rc)
    	if err != nil {
    		return nil, fmt.Errorf("io.ReadAll: %w", err)
    	}
    	fmt.Fprintf(w, "File %v downloaded with encryption key.\n", object)
    	return data, nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import java.io.IOException;
    import java.nio.file.Path;
    
    public class DownloadEncryptedObject {
      public static void downloadEncryptedObject(
          String projectId,
          String bucketName,
          String objectName,
          Path destFilePath,
          String decryptionKey)
          throws IOException {
    
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The ID of your GCS object
        // String objectName = "your-object-name";
    
        // The path to which the file should be downloaded
        // Path destFilePath = Paths.get("/local/path/to/file.txt");
    
        // The Base64 encoded decryption key, which should be the same key originally used to encrypt
        // the object
        // String decryptionKey = "TIbv/fjexq+VmtXzAlc63J4z5kFmWJ6NdAPQulQBT7g=";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
    
        [Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html) blob = storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName, objectName);
        blob.[downloadTo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html#com_google_cloud_storage_Blob_downloadTo_java_io_OutputStream_com_google_cloud_storage_Blob_BlobSourceOption____)(destFilePath, Blob.BlobSourceOption.decryptionKey(decryptionKey));
    
        System.out.println(
            "Downloaded object "
                + objectName
                + " from bucket name "
                + bucketName
                + " to "
                + destFilePath
                + " using customer-supplied encryption key");
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
    // const srcFileName = 'your-file-name';
    
    // The path to which the file should be downloaded
    // const destFileName = '/local/path/to/file.txt';
    
    // The Base64 encoded decryption key, which should be the same key originally
    // used to encrypt the file
    // const encryptionKey = 'TIbv/fjexq+VmtXzAlc63J4z5kFmWJ6NdAPQulQBT7g=';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function downloadEncryptedFile() {
      const options = {
        destination: destFileName,
      };
    
      // Decrypts and downloads the file. This can only be done with the key used
      // to encrypt and upload the file.
      await storage
        .bucket(bucketName)
        .file(srcFileName)
        .[setEncryptionKey](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/file_2.html)(Buffer.from(encryptionKey, '[base64](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/policydocument.html)'))
        .[download](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/file_2.html)(options);
    
      console.log(`File ${srcFileName} downloaded to ${destFileName}`);
    }
    
    downloadEncryptedFile().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Download an encrypted file
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $objectName The name of your Cloud Storage object.
     *        (e.g. 'my-object')
     * @param string $destination The local destination to save the encrypted file.
     *        (e.g. '/path/to/your/file')
     * @param string $base64EncryptionKey The base64 encoded encryption key. Should
     *        (e.g. 'TIbv/fjexq+VmtXzAlc63J4z5kFmWJ6NdAPQulQBT7g=')
     *     be the same key originally used to encrypt the object.
     */
    function download_encrypted_object(string $bucketName, string $objectName, string $destination, string $base64EncryptionKey): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
        $object = $bucket->object($objectName);
        $object->downloadToFile($destination, [
            'encryptionKey' => $base64EncryptionKey,
        ]);
        printf('Encrypted object gs://%s/%s downloaded to %s' . PHP_EOL,
            $bucketName, $objectName, basename($destination));
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import base64
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def download_encrypted_blob(
        bucket_name,
        source_blob_name,
        destination_file_name,
        base64_encryption_key,
    ):
        """Downloads a previously-encrypted blob from Google Cloud Storage.
    
        The encryption key provided must be the same key provided when uploading
        the blob.
        """
        # bucket_name = "your-bucket-name"
        # source_blob_name = "storage-object-name"
        # destination_file_name = "local/path/to/file"
        # base64_encryption_key = "base64-encoded-encryption-key"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
    
        # Encryption key must be an AES256 key represented as a bytestring with
        # 32 bytes. Since it's passed in as a base64 encoded string, it needs
        # to be decoded.
        encryption_key = base64.b64decode(base64_encryption_key)
        blob = bucket.blob(source_blob_name, encryption_key=encryption_key)
    
        blob.[download_to_filename](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_download_to_filename)(destination_file_name)
    
        print(
            f"Blob {source_blob_name} downloaded to {destination_file_name}."
        )
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def download_encrypted_file bucket_name:, file_name:, local_file_path:, encryption_key:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      # The ID of your GCS object
      # file_name = "your-file-name"
    
      # The path to which the file should be downloaded
      # local_file_path = "/local/path/to/file.txt"
    
      # The Base64 encoded decryption key, which should be the same key originally used to encrypt the object
      # encryption_key = "TIbv/fjexq+VmtXzAlc63J4z5kFmWJ6NdAPQulQBT7g="
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
    
      bucket = storage.bucket bucket_name, skip_lookup: true
    
      file = bucket.[file](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) file_name, encryption_key: encryption_key
      file.[download](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-File.html) local_file_path, encryption_key: encryption_key
    
      puts "Downloaded encrypted #{file.name} to #{local_file_path}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
