---
url: https://docs.cloud.google.com/storage/docs/encryption/using-customer-supplied-keys/
title: Use customer-supplied encryption keys \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:11.223289+00:00
---

# Use customer-supplied encryption keys  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/encryption/using-customer-supplied-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Use customer-supplied encryption keys Stay organized with collections  Save and categorize content based on your preferences. 

Customer-supplied encryption keys (CSEK) let you encrypt Cloud Storage objects by using cryptographic keys that you generate and control. This encryption option is best for scenarios where you have an existing key management system outside of Google Cloud and you want to use those keys to encrypt your data.

For background information about customer-supplied encryption keys, see [Customer-supplied encryption keys](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys). For information about other encryption options in Cloud Storage, see [Data encryption options](https://docs.cloud.google.com/storage/docs/encryption).

## Generate your own encryption key

There are many ways to generate a [Base64-encoded](https://datatracker.ietf.org/doc/html/rfc4648#section-4) AES-256 encryption key. Here are several examples:

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    // Create a pseudo-random number generator (PRNG), this is included for
    // demonstration purposes only. You should consult your security team about
    // best practices to initialize PRNG. In particular, you should verify that
    // the C++ library and operating system provide enough entropy to meet the
    // security policies in your organization.
    
    // Use the Mersenne-Twister Engine in this example:
    //   https://en.cppreference.com/w/cpp/numeric/random/mersenne_twister_engine
    // Any C++ PRNG can be used below, the choice is arbitrary.
    using GeneratorType = std::mt19937_64;
    
    // Create the default random device to fetch entropy.
    std::random_device rd;
    
    // Compute how much entropy we need to initialize the GeneratorType:
    constexpr auto kRequiredEntropyWords =
        GeneratorType::state_size *
        (GeneratorType::word_size / std::numeric_limits<unsigned int>::digits);
    
    // Capture the entropy bits into a vector.
    std::vector<std::uint64_t> entropy(kRequiredEntropyWords);
    std::generate(entropy.begin(), entropy.end(), [&rd] { return rd(); });
    
    // Create the PRNG with the fetched entropy.
    std::seed_seq seed(entropy.begin(), entropy.end());
    
    // initialized with enough entropy such that the encryption keys are not
    // predictable. Note that the default constructor for all the generators in
    // the C++ standard library produce predictable keys.
    std::mt19937_64 gen(seed);
    
    namespace gcs = ::google::cloud::storage;
    gcs::EncryptionKeyData data = gcs::CreateKeyFromGenerator(gen);
    
    std::cout << "Base64 encoded key = " << data.key << "\n"
              << "Base64 encoded SHA256 of key = " << data.sha256 << "\n";

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class GenerateEncryptionKeySample
    {
        public string GenerateEncryptionKey()
        {
            var encryptionKey = [EncryptionKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.EncryptionKey.html).[Generate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.EncryptionKey.html#Google_Cloud_Storage_V1_EncryptionKey_Generate)().[Base64Key](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.EncryptionKey.html#Google_Cloud_Storage_V1_EncryptionKey_Base64Key);
            Console.WriteLine($"Generated Base64-encoded AES-256 encryption key: {encryptionKey}");
            return encryptionKey;
        }
    }

### Go

For more information, see the [Cloud Storage Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storage). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import (
    	"crypto/rand"
    	"encoding/base64"
    	"fmt"
    	"io"
    )
    
    // generateEncryptionKey generates a 256 bit (32 byte) AES encryption key and
    // prints the base64 representation.
    func generateEncryptionKey(w io.Writer) error {
    	// This is included for demonstration purposes. You should generate your own
    	// key. Please remember that encryption keys should be handled with a
    	// comprehensive security policy.
    	key := make([]byte, 32)
    	if _, err := rand.Read(key); err != nil {
    		return fmt.Errorf("rand.Read: %w", err)
    	}
    	encryptionKey := base64.StdEncoding.EncodeToString(key)
    	fmt.Fprintf(w, "Generated base64-encoded encryption key: %v\n", encryptionKey)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.common.io.BaseEncoding;
    import java.security.SecureRandom;
    
    public class GenerateEncryptionKey {
      /**
       * Generates a 256 bit (32 byte) AES encryption key and prints the base64 representation. This is
       * included for demonstration purposes only. You should generate your own key, and consult your
       * security team about best practices. Please remember that encryption keys should be handled with
       * a comprehensive security policy.
       */
      public static void generateEncryptionKey() {
        byte[] key = new byte[32];
        new SecureRandom().nextBytes(key);
        String encryptionKey = BaseEncoding.base64().encode(key);
    
        System.out.println("Generated Base64-encoded AES-256 encryption key: " + encryptionKey);
      }
    }

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    const crypto = require('crypto');
    
    function generateEncryptionKey() {
      /**
       * Generates a 256 bit (32 byte) AES encryption key and prints the base64
       * representation.
       *
       * This is included for demonstration purposes. You should generate your own
       * key. Please remember that encryption keys should be handled with a
       * comprehensive security policy.
       */
      const buffer = crypto.randomBytes(32);
      const encodedKey = buffer.toString('base64');
      console.log(`Base 64 encoded encryption key: ${encodedKey}`);
    }
    generateEncryptionKey();

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    /**
     * Generate a base64 encoded encryption key for Google Cloud Storage.
     */
    function generate_encryption_key(): void
    {
        $key = random_bytes(32);
        $encodedKey = base64_encode($key);
        printf('Your encryption key: %s' . PHP_EOL, $encodedKey);
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import base64
    import os
    
    
    def generate_encryption_key():
        """Generates a 256 bit (32 byte) AES encryption key and prints the
        base64 representation.
    
        This is included for demonstration purposes. You should generate your own
        key. Please remember that encryption keys should be handled with a
        comprehensive security policy.
        """
        key = os.urandom(32)
        encoded_key = base64.b64encode(key).decode("utf-8")
    
        print(f"Base 64 encoded encryption key: {encoded_key}")
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def generate_encryption_key
      # Generates a 256 bit (32 byte) AES encryption key and prints the base64 representation.
      #
      # This is included for demonstration purposes. You should generate your own key.
      # Please remember that encryption keys should be handled with a comprehensive security policy.
      require "base64"
      require "openssl"
    
      encryption_key  = OpenSSL::Cipher.new("aes-256-cfb").encrypt.random_key
      encoded_enc_key = Base64.encode64 encryption_key
    
      puts "Sample encryption key: #{encoded_enc_key}"
    end

### Rust
    
    
    use google_cloud_storage::{error::KeyAes256Error, model_ext::KeyAes256};
    use rand::Rng;
    
    pub fn sample() -> Result<KeyAes256, KeyAes256Error> {
        // Generates a 256 bit (32 byte) AES encryption key and prints the base64 representation.
        //
        // This is included for demonstration purposes. You should generate your own key.
        // Please remember that encryption keys should be handled with a comprehensive security policy.
        let mut raw_key_bytes = [0u8; 32];
        rand::rng().fill_bytes(&mut raw_key_bytes);
        let key = KeyAes256::new(&raw_key_bytes)?;
        println!("Sample encryption key: {key}");
        Ok(key)
    }

## Upload with your encryption key

To use customer-supplied encryption keys to upload an object:

### Console

The Google Cloud console cannot be used to upload an object with a customer-supplied encryption key. Use the Google Cloud CLI or the client libraries instead.

### Command line

Use the [`gcloud storage cp`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cp) command with the `--encryption-key` flag:
    
    
    gcloud storage cp SOURCE_DATA gs://BUCKET_NAME/OBJECT_NAME --encryption-key=YOUR_ENCRYPTION_KEY

Where:

  * `SOURCE_DATA` is the source location of the data you're encrypting. This can be any source location supported by the `cp` command. For example, a local file such as `Desktop/dogs.png` or another Cloud Storage object such as `gs://my-bucket/pets/old-dog.png`.
  * `BUCKET_NAME` is the name of the destination bucket for this copy command. For example, `my-bucket`.
  * `OBJECT_NAME` is the name of the final, encrypted object. For example, `pets/new-dog.png`.
  * `YOUR_ENCRYPTION_KEY` is the [AES-256 key](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys#overview) that you want to use for encrypting the uploaded object.



### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name,
       std::string const& object_name, std::string const& base64_aes256_key) {
      StatusOr<gcs::ObjectMetadata> object_metadata = client.InsertObject(
          bucket_name, object_name, "top secret",
          gcs::EncryptionKey::FromBase64Key(base64_aes256_key));
      if (!object_metadata) throw std::move(object_metadata).status();
    
      std::cout << "The object " << object_metadata->name()
                << " was created in bucket " << object_metadata->bucket()
                << "\nFull metadata: " << *object_metadata << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    using System.IO;
    
    public class UploadEncryptedFileSample
    {
        public void UploadEncryptedFile(
            string key = "3eFsTXPvqi3BpT2ipFCGirslh1Jgc6ikjoAu2oQ5JcI=",
            string bucketName = "your-unique-bucket-name",
            string localPath = "my-local-path/my-file-name",
            string objectName = "my-file-name")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            using var fileStream = File.OpenRead(localPath);
            storage.UploadObject(bucketName, objectName, null, fileStream, new [UploadObjectOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UploadObjectOptions.html)
            {
                EncryptionKey = [EncryptionKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.EncryptionKey.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.EncryptionKey.html#Google_Cloud_Storage_V1_EncryptionKey_Create_System_Byte___)(Convert.FromBase64String(key))
            });
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
    
    // uploadEncryptedFile writes an object using AES-256 encryption key.
    func uploadEncryptedFile(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucket, object string, secretKey []byte) error {
    	// bucket := "bucket-name"
    	// object := "object-name"
    	// secretKey := []byte("secret-key")
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
    	wc := o.[Key](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_Key)(secretKey).[NewWriter](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_NewWriter)(ctx)
    	if _, err := wc.[Write](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer_Write)([]byte("top secret")); err != nil {
    		return fmt.Errorf("Writer.Write: %w", err)
    	}
    	if err := wc.Close(); err != nil {
    		return fmt.Errorf("Writer.Close: %w", err)
    	}
    	fmt.Fprintf(w, "Uploaded encrypted object %v.\n", object)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html);
    import com.google.cloud.storage.[BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import java.io.IOException;
    import java.nio.file.Files;
    import java.nio.file.Paths;
    
    public class UploadEncryptedObject {
      public static void uploadEncryptedObject(
          String projectId, String bucketName, String objectName, String filePath, String encryptionKey)
          throws IOException {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The ID of your GCS object
        // String objectName = "your-object-name";
    
        // The path to your file to upload
        // String filePath = "path/to/your/file"
    
        // The key to encrypt the object with
        // String encryptionKey = "TIbv/fjexq+VmtXzAlc63J4z5kFmWJ6NdAPQulQBT7g=";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html) blobId = [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html).of(bucketName, objectName);
        [BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html) blobInfo = [BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html).newBuilder(blobId).build();
    
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
    
        storage.[create](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_create_com_google_cloud_storage_BlobInfo_byte___com_google_cloud_storage_Storage_BlobTargetOption____)(
            blobInfo,
            Files.readAllBytes(Paths.get(filePath)),
            Storage.BlobTargetOption.encryptionKey(encryptionKey),
            precondition);
    
        System.out.println(
            "File "
                + filePath
                + " uploaded to bucket "
                + bucketName
                + " as "
                + objectName
                + " with supplied encryption key");
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
    
    // The new ID for your GCS file
    // const destFileName = 'your-new-file-name';
    
    // The key to encrypt the object with
    // const key = 'TIbv/fjexq+VmtXzAlc63J4z5kFmWJ6NdAPQulQBT7g=';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function uploadEncryptedFile() {
      const options = {
        destination: destFileName,
        encryptionKey: Buffer.from(key, '[base64](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/policydocument.html)'),
    
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
    
      console.log(
        `File ${filePath} uploaded to gs://${bucketName}/${destFileName}`
      );
    }
    
    uploadEncryptedFile().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Upload an encrypted file.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $objectName The name of your Cloud Storage object.
     *        (e.g. 'my-object')
     * @param string $source The path to the file to upload.
     *        (e.g. '/path/to/your/file')
     * @param string $base64EncryptionKey The base64 encoded encryption key.
     *        (e.g. 'TIbv/fjexq+VmtXzAlc63J4z5kFmWJ6NdAPQulQBT7g=')
     */
    function upload_encrypted_object(string $bucketName, string $objectName, string $source, string $base64EncryptionKey): void
    {
        $storage = new StorageClient();
        $file = fopen($source, 'r');
        $bucket = $storage->bucket($bucketName);
        $object = $bucket->upload($file, [
            'name' => $objectName,
            'encryptionKey' => $base64EncryptionKey,
        ]);
        printf('Uploaded encrypted %s to gs://%s/%s' . PHP_EOL,
            basename($source), $bucketName, $objectName);
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import base64
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def upload_encrypted_blob(
        bucket_name,
        source_file_name,
        destination_blob_name,
        base64_encryption_key,
    ):
        """Uploads a file to a Google Cloud Storage bucket using a custom
        encryption key.
    
        The file will be encrypted by Google Cloud Storage and only
        retrievable using the provided encryption key.
        """
        # bucket_name = "your-bucket-name"
        # source_file_name = "local/path/to/file"
        # destination_blob_name = "storage-object-name"
        # base64_encryption_key = "TIbv/fjexq+VmtXzAlc63J4z5kFmWJ6NdAPQulQBT7g="
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
    
        # Encryption key must be an AES256 key represented as a bytestring with
        # 32 bytes. Since it's passed in as a base64 encoded string, it needs
        # to be decoded.
        encryption_key = base64.b64decode(base64_encryption_key)
        blob = bucket.blob(
            destination_blob_name, encryption_key=encryption_key
        )
    
        # Optional: set a generation-match precondition to avoid potential race conditions
        # and data corruptions. The request to upload is aborted if the object's
        # generation number does not match your precondition. For a destination
        # object that does not yet exist, set the if_generation_match precondition to 0.
        # If the destination object already exists in your bucket, set instead a
        # generation-match precondition using its generation number.
        generation_match_precondition = 0
    
        blob.[upload_from_filename](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_filename)(source_file_name, if_generation_match=generation_match_precondition)
    
        print(
            f"File {source_file_name} uploaded to {destination_blob_name}."
        )
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def upload_encrypted_file bucket_name:, local_file_path:, file_name: nil, encryption_key:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      # The path to your file to upload
      # local_file_path = "/local/path/to/file.txt"
    
      # The ID of your GCS object
      # file_name = "your-file-name"
    
      # The encryption key used for securing the object must be a 32-byte key consisting of raw encrypted data.
      # Key used should not be base64 encoded.
    
      # encryption_key = "your-encryption-key"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
    
      bucket = storage.bucket bucket_name, skip_lookup: true
    
      file = bucket.[create_file](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) local_file_path, file_name, encryption_key: encryption_key
    
      puts "Uploaded #{file.name} with encryption key"
    end

### Rust
    
    
    use google_cloud_storage::client::Storage;
    use google_cloud_storage::model_ext::KeyAes256;
    
    pub async fn sample(
        client: &Storage,
        bucket: &str,
        object: &str,
        encryption_key: KeyAes256,
    ) -> Result<(), anyhow::Error> {
        let _result = client
            .write_object(format!("projects/_/buckets/{bucket}"), object, "top secret")
            .set_key(encryption_key.clone())
            .send_unbuffered()
            .await?;
    
        println!("Uploaded to {object} in bucket {bucket} with key={encryption_key}.",);
        Ok(())
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`POST` Object](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/insert) request:
         
         curl -X POST --data-binary @OBJECT \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: OBJECT_CONTENT_TYPE" \
           -H "x-goog-encryption-algorithm: AES256" \
           -H "x-goog-encryption-key: YOUR_ENCRYPTION_KEY" \
           -H "x-goog-encryption-key-sha256: HASH_OF_YOUR_KEY" \
           "https://storage.googleapis.com/upload/storage/v1/b/BUCKET_NAME/o?uploadType=media&name=OBJECT_NAME"

Where:

     * `OBJECT` is the path to the object you are uploading. For example, `Desktop/dogs.png`.
     * `OBJECT_CONTENT_TYPE` is the [content type](https://docs.cloud.google.com/storage/docs/metadata#content-type) of the object. For example, `image/png`.
     * `YOUR_ENCRYPTION_KEY` is the [AES-256 key](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys#rest-apis) used for encrypting the uploaded object.
     * `HASH_OF_YOUR_KEY` is the SHA-256 hash for your AES-256 key.
     * `BUCKET_NAME` is the name of the bucket to which you are uploading the object. For example, `my-bucket`.
     * `OBJECT_NAME` is the URL-encoded name of the object you are uploading. For example, `pets/dog.png`, URL-encoded as `pets%2Fdog.png`.



See [Encryption request headers](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys#rest-apis) for more information on encryption-specific headers.

### XML API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [XML API](https://docs.cloud.google.com/storage/docs/xml-api/overview) with a [`PUT` OBJECT](https://docs.cloud.google.com/storage/docs/xml-api/put-object-upload) request:
         
         curl -X -i PUT --data-binary @OBJECT \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: OBJECT_CONTENT_TYPE" \
           -H "x-goog-encryption-algorithm: AES256" \
           -H "x-goog-encryption-key: YOUR_ENCRYPTION_KEY" \
           -H "x-goog-encryption-key-sha256: HASH_OF_YOUR_KEY" \
           "https://storage.googleapis.com/BUCKET_NAME/OBJECT_NAME"

Where:

     * `OBJECT` is the path to the object you are uploading. For example, `Desktop/dogs.png`.
     * `OBJECT_CONTENT_TYPE` is the [content type](https://docs.cloud.google.com/storage/docs/metadata#content-type) of the object. For example, `image/png`.
     * `YOUR_ENCRYPTION_KEY` is the [AES-256 key](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys#rest-apis) used for encrypting the uploaded object.
     * `HASH_OF_YOUR_KEY` is the SHA-256 hash for your AES-256 key.
     * `BUCKET_NAME` is the name of the bucket to which you are uploading the object. For example, `my-bucket`.
     * `OBJECT_NAME` is the URL-encoded name of the object you are uploading. For example, `pets/dog.png`, URL-encoded as `pets%2Fdog.png`.



See [Encryption request headers](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys#rest-apis) for more information on encryption-specific headers.

## Download objects you've encrypted

To download an object stored in Cloud Storage that is encrypted with a customer-supplied encryption key:

### Console

The Google Cloud console cannot be used to download objects encrypted with customer-supplied encryption keys. Use the Google Cloud CLI or the client libraries instead.

### Command line

Use the [`gcloud storage cp`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cp) command with the `--decryption-keys` flag:
    
    
    gcloud storage cp gs://BUCKET_NAME/OBJECT_NAME OBJECT_DESTINATION --decryption-keys=YOUR_ENCRYPTION_KEY

Where:

  * `BUCKET_NAME` is the name of the bucket containing the object you are downloading. For example, `my-bucket`.
  * `OBJECT_NAME` is the name of the object you are downloading. For example, `pets/dog.png`.
  * `OBJECT_DESTINATION` is the location where you want to save your object. For example, `Desktop`.
  * `YOUR_ENCRYPTION_KEY` is the [AES-256 key](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys#overview) used to encrypt the object when it was uploaded.



### Client libraries

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

### Rust
    
    
    use google_cloud_storage::client::Storage;
    use google_cloud_storage::model_ext::KeyAes256;
    
    pub async fn sample(
        client: &Storage,
        bucket: &str,
        object: &str,
        encryption_key: KeyAes256,
    ) -> Result<(), anyhow::Error> {
        let mut reader = client
            .read_object(format!("projects/_/buckets/{bucket}"), object)
            .set_key(encryption_key.clone())
            .send()
            .await?;
    
        while let Some(data) = reader.next().await.transpose()? {
            println!("downloaded {} bytes", data.len())
        }
    
        println!("Downloaded {object} in bucket {bucket} with key={encryption_key}.");
        Ok(())
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`GET` Object](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/get) request:
         
         curl -X GET \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "x-goog-encryption-algorithm: AES256" \
           -H "x-goog-encryption-key: YOUR_ENCRYPTION_KEY" \
           -H "x-goog-encryption-key-sha256: HASH_OF_YOUR_KEY" \
           -o "SAVE_TO_LOCATION" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/o/OBJECT_NAME?alt=media"

Where:

     * `YOUR_ENCRYPTION_KEY` is the [AES-256 key](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys#rest-apis) you used to encrypt the object.
     * `HASH_OF_YOUR_KEY` is the SHA-256 hash for your AES-256 key.
     * `SAVE_TO_LOCATION` is the location where you want to save your object. For example, `Desktop/dog.png`.
     * `BUCKET_NAME` is the name of the bucket from which you are downloading the object. For example, `my-bucket`.
     * `OBJECT_NAME` is the URL-encoded name of the object you are downloading. For example, `pets/dog.png`, URL-encoded as `pets%2Fdog.png`.



See [Encryption request headers](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys#rest-apis) for more information on encryption-specific headers.

### XML API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [XML API](https://docs.cloud.google.com/storage/docs/xml-api/overview) with a [`GET` OBJECT](https://docs.cloud.google.com/storage/docs/xml-api/get-object-download) request:
         
         curl -X GET \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "x-goog-encryption-algorithm: AES256" \
           -H "x-goog-encryption-key: YOUR_ENCRYPTION_KEY" \
           -H "x-goog-encryption-key-sha256: HASH_OF_YOUR_KEY" \
           -o "SAVE_TO_LOCATION" \
           "https://storage.googleapis.com/BUCKET_NAME/OBJECT_NAME"

Where:

     * `YOUR_ENCRYPTION_KEY` is the [AES-256 key](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys#rest-apis) you used to encrypt the object.
     * `HASH_OF_YOUR_KEY` is the SHA-256 hash for your AES-256 key.
     * `SAVE_TO_LOCATION` is the location where you want to save your object. For example, `Desktop/dog.png`.
     * `BUCKET_NAME` is the name of the bucket from which you are downloading the object. For example, `my-bucket`.
     * `OBJECT_NAME` is the URL-encoded name of the object you are downloading. For example, `pets/dog.png`, URL-encoded as `pets%2Fdog.png`.



See [Encryption request headers](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys#rest-apis) for more information on encryption-specific headers.

## Rotate your encryption keys

To rotate a customer-supplied encryption key:

### Console

The Google Cloud console cannot be used to rotate customer-supplied encryption keys. Use the Google Cloud CLI or the client libraries instead.

### Command line

Use the [`gcloud storage objects update`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/objects/update) command with the appropriate flags:
    
    
    gcloud storage objects update gs://BUCKET_NAME/OBJECT_NAME --encryption-key=NEW_KEY --decryption-keys=OLD_KEY

Where:

  * `BUCKET_NAME` is the name of the bucket that contains the object whose key you are rotating. For example, `my-bucket`.
  * `OBJECT_NAME` is the name of the object whose key you are rotating. For example, `pets/dog.png`.
  * `NEW_KEY` is the new customer-supplied encryption key that you want to use to encrypt the object.
  * `OLD_KEY` is the current customer-supplied encryption key that is used to encrypt the object.



### Client libraries

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
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket  = storage.bucket bucket_name, skip_lookup: true
      file    = bucket.[file](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) file_name, encryption_key: current_encryption_key
    
      file.[rotate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-File.html) encryption_key:     current_encryption_key,
                  new_encryption_key: new_encryption_key
    
      puts "The encryption key for #{file.name} in #{bucket.name} was rotated."
    end

### Rust
    
    
    use google_cloud_storage::builder_ext::RewriteObjectExt;
    use google_cloud_storage::client::StorageControl;
    use google_cloud_storage::model::CommonObjectRequestParams;
    use google_cloud_storage::model_ext::KeyAes256;
    
    pub async fn sample(
        client: &StorageControl,
        bucket_id: &str,
        object_id: &str,
        old_key: KeyAes256,
        new_key: KeyAes256,
    ) -> anyhow::Result<()> {
        let old: CommonObjectRequestParams = old_key.into();
        let updated = client
            .rewrite_object()
            .set_source_bucket(format!("projects/_/buckets/{bucket_id}"))
            .set_source_object(object_id)
            .set_copy_source_encryption_algorithm(old.encryption_algorithm)
            .set_copy_source_encryption_key_bytes(old.encryption_key_bytes)
            .set_copy_source_encryption_key_sha256_bytes(old.encryption_key_sha256_bytes)
            .set_destination_bucket(format!("projects/_/buckets/{bucket_id}"))
            .set_destination_name(object_id)
            .set_common_object_request_params(new_key)
            .rewrite_until_done()
            .await?;
    
        println!(
            "successfully rotated encryption key for object {object_id} in bucket {bucket_id}: {updated:?}"
        );
        Ok(())
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`POST` Object](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/rewrite) request:
         
         curl -X POST \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Length: 0" \
           -H "x-goog-encryption-algorithm: AES256" \
           -H "x-goog-encryption-key: NEW_ENCRYPTION_KEY" \
           -H "x-goog-encryption-key-sha256: HASH_OF_NEW_KEY" \
           -H "x-goog-copy-source-encryption-algorithm: AES256" \
           -H "x-goog-copy-source-encryption-key: OLD_ENCRYPTION_KEY" \
           -H "x-goog-copy-source-encryption-key-sha256: HASH_OF_OLD_KEY" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/o/OBJECT_NAME/rewriteTo/b/BUCKET_NAME/o/OBJECT_NAME"

Where:

     * `NEW_ENCRYPTION_KEY` is the new AES-256 key used for encrypting your object.
     * `HASH_OF_NEW_KEY` is the SHA-256 hash for your new AES-256 key.
     * `OLD_ENCRYPTION_KEY` is the current AES-256 key used to encrypt your object.
     * `HASH_OF_OLD_KEY` is the current SHA-256 hash for your AES-256 key.
     * `BUCKET_NAME` is the name of the bucket containing the relevant object. For example, `my-bucket`.
     * `OBJECT_NAME` is the URL-encoded name of the object whose keys you are rotating. For example, `pets/dog.png`, URL-encoded as `pets%2Fdog.png`.



See [Encryption request headers](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys#rest-apis) for more information on encryption-specific headers.

### XML API

The XML API does not support rotating a customer-supplied encryption key through rewriting object. To apply a new customer-supplied key to an object using the XML API, you should:

  1. Download the existing object.
  2. Re-upload the object using a new key.



**Note:** Rotating encryption keys involves rewriting data, which can incur [early deletion](https://docs.cloud.google.com/storage/pricing#early-delete) charges, depending on the age and storage class of the data.

## What's next

  * Learn more about [customer-supplied encryption keys](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys).

  * Learn how to [rotate your customer-supplied encryption key to a Cloud KMS key](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys#csek-to-cmek).

  * [Configure which encryption methods are allowed or restricted](https://docs.cloud.google.com/storage/docs/encryption/enforce-encryption-types) for new objects in your buckets.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
