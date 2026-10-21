---
url: https://docs.cloud.google.com/kms/docs/encrypt-decrypt/
title: Encrypting and decrypting data with a symmetric key \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:57.425163+00:00
---

# Encrypting and decrypting data with a symmetric key  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/encrypt-decrypt/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Encrypting and decrypting data with a symmetric key Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to use Cloud Key Management Service (Cloud KMS) to do the following symmetric key operations:

  * Encrypt text or binary content (plaintext) by using a Cloud KMS key.
  * Decrypt ciphertext that was encrypted with a Cloud KMS key.



If you want to use an asymmetric key for encryption, see [Encrypting and decrypting data with an asymmetric key](https://docs.cloud.google.com/kms/docs/encrypt-decrypt-rsa). To learn about raw symmetric encryption, see [raw symmetric encryption](https://docs.cloud.google.com/kms/docs/raw-encryption).

**Note:** For security reasons, the raw cryptographic key material represented by a Cloud KMS key can never be viewed or exported. It can only be used by an authorized user to encrypt or decrypt data when they invoke the Cloud KMS API.

## Before you begin

  1. [Create a key ring](https://docs.cloud.google.com/kms/docs/create-key-ring) and [create a key](https://docs.cloud.google.com/kms/docs/creating-keys).

  2. Ensure the user that is calling the encrypt and decrypt methods has the `cloudkms.cryptoKeyVersions.useToEncrypt` and `cloudkms.cryptoKeyVersions.useToDecrypt` permissions on the key.

One way to permit a user to encrypt or decrypt is to add the user to the `roles/cloudkms.cryptoKeyEncrypter`, `roles/cloudkms.cryptoKeyDecrypter`, or `roles/cloudkms.cryptoKeyEncrypterDecrypter` IAM roles for that key. The `roles/cloudkms.admin` role **does not** provide these two permissions. For more information, see [Permissions and Roles](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles).




## Encrypt

### gcloud

To use Cloud KMS on the command line, first [Install or upgrade to the latest version of Google Cloud CLI](https://docs.cloud.google.com/sdk/install).
    
    
    gcloud kms encrypt \
        --key KEY_NAME \
        --keyring KEY_RING \
        --location LOCATION  \
        --plaintext-file FILE_TO_ENCRYPT \
        --ciphertext-file ENCRYPTED_OUTPUT
    

Replace the following:

  * `KEY_NAME`: the name of the key that you want to use for encryption.
  * `KEY_RING`: the name of the key ring that contains the key.
  * `LOCATION`: the Cloud KMS location that contains the key ring.
  * `FILE_TO_ENCRYPT`: the path to the file that you want to encrypt.
  * `ENCRYPTED_OUTPUT`: the path where you want to save the encrypted output.



For information on all flags and possible values, run the command with the `--help` flag.

### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Cloud KMS C# SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-csharp).
    
    
    using [Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.html);
    using [Google.Protobuf](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.html);
    using System.Text;
    
    public class EncryptSymmetricSample
    {
        public byte[] EncryptSymmetric(
          string projectId = "my-project", string locationId = "us-east1", string keyRingId = "my-key-ring", string keyId = "my-key",
          string message = "Sample message")
        {
            // Create the client.
            [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_Create)();
    
            // Build the key name.
            [CryptoKeyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyName.html) keyName = new [CryptoKeyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyName.html)(projectId, locationId, keyRingId, keyId);
    
            // Convert the message into bytes. Cryptographic plaintexts and
            // ciphertexts are always byte arrays.
            byte[] plaintext = Encoding.UTF8.GetBytes(message);
    
            // Call the API.
            [EncryptResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.EncryptResponse.html) result = client.[Encrypt](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_Encrypt_Google_Api_Gax_IResourceName_Google_Protobuf_ByteString_Google_Api_Gax_Grpc_CallSettings_)(keyName, [ByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html).[CopyFrom](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html#Google_Protobuf_ByteString_CopyFrom_System_Byte___)(plaintext));
    
            // Return the ciphertext.
            return result.[Ciphertext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.EncryptResponse.html#Google_Cloud_Kms_V1_EncryptResponse_Ciphertext).ToByteArray();
        }
    }

### Go

To run this code, first [set up a Go development environment](https://docs.cloud.google.com/go/docs/setup) and [install the Cloud KMS Go SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-go).
    
    
    import (
    	"context"
    	"fmt"
    	"hash/crc32"
    	"io"
    
    	kms "cloud.google.com/go/kms/apiv1"
    	"cloud.google.com/go/kms/apiv1/kmspb"
    	"google.golang.org/protobuf/types/known/wrapperspb"
    )
    
    // encryptSymmetric encrypts the input plaintext with the specified symmetric
    // Cloud KMS key.
    func encryptSymmetric(w io.Writer, name string, message string) error {
    	// name := "projects/my-project/locations/us-east1/keyRings/my-key-ring/cryptoKeys/my-key"
    	// message := "Sample message"
    
    	// Create the client.
    	ctx := context.Background()
    	client, err := kms.[NewKeyManagementClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_NewKeyManagementClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create kms client: %w", err)
    	}
    	defer client.Close()
    
    	// Convert the message into bytes. Cryptographic plaintexts and
    	// ciphertexts are always byte arrays.
    	plaintext := []byte(message)
    
    	// Optional but recommended: Compute plaintext's CRC32C.
    	crc32c := func(data []byte) uint32 {
    		t := crc32.MakeTable(crc32.Castagnoli)
    		return crc32.Checksum(data, t)
    	}
    	plaintextCRC32C := crc32c(plaintext)
    
    	// Build the request.
    	req := &kmspb.EncryptRequest{
    		Name:            name,
    		Plaintext:       plaintext,
    		PlaintextCrc32C: wrapperspb.Int64(int64(plaintextCRC32C)),
    	}
    
    	// Call the API.
    	result, err := client.Encrypt(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to encrypt: %w", err)
    	}
    
    	// Optional, but recommended: perform integrity verification on result.
    	// For more details on ensuring E2E in-transit integrity to and from Cloud KMS visit:
    	// https://cloud.google.com/kms/docs/data-integrity-guidelines
    	if result.VerifiedPlaintextCrc32C == false {
    		return fmt.Errorf("Encrypt: request corrupted in-transit")
    	}
    	if int64(crc32c(result.Ciphertext)) != result.CiphertextCrc32C.Value {
    		return fmt.Errorf("Encrypt: response corrupted in-transit")
    	}
    
    	fmt.Fprintf(w, "Encrypted ciphertext: %s", result.Ciphertext)
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Cloud KMS Java SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-java).
    
    
    import com.google.cloud.kms.v1.[CryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html);
    import com.google.cloud.kms.v1.[EncryptResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.EncryptResponse.html);
    import com.google.cloud.kms.v1.[KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    
    public class EncryptSymmetric {
    
      public void encryptSymmetric() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "us-east1";
        String keyRingId = "my-key-ring";
        String keyId = "my-key";
        String plaintext = "Plaintext to encrypt";
        encryptSymmetric(projectId, locationId, keyRingId, keyId, plaintext);
      }
    
      // Encrypt data with a given key.
      public void encryptSymmetric(
          String projectId, String locationId, String keyRingId, String keyId, String plaintext)
          throws IOException {
        // Initialize client that will be used to send requests. This client only
        // needs to be created once, and can be reused for multiple requests. After
        // completing all of your requests, call the "close" method on the client to
        // safely clean up any remaining background resources.
        try ([KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html).create()) {
          // Build the key version name from the project, location, key ring, key,
          // and key version.
          [CryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html) keyVersionName = [CryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html).of(projectId, locationId, keyRingId, keyId);
    
          // Encrypt the plaintext.
          [EncryptResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.EncryptResponse.html) response = client.encrypt(keyVersionName, [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFromUtf8](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFromUtf8_java_lang_String_)(plaintext));
          System.out.printf("Ciphertext: %s%n", response.[getCiphertext](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.EncryptResponse.html#com_google_cloud_kms_v1_EncryptResponse_getCiphertext__)().toStringUtf8());
        }
      }
    }

### Node.js

To run this code, first [set up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup) and [install the Cloud KMS Node.js SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-nodejs).
    
    
    //
    // TODO(developer): Uncomment these variables before running the sample.
    //
    // const projectId = 'my-project';
    // const locationId = 'us-east1';
    // const keyRingId = 'my-key-ring';
    // const keyId = 'my-key';
    // const plaintextBuffer = Buffer.from('...');
    
    // Imports the Cloud KMS library
    const {KeyManagementServiceClient} = require('[@google-cloud/kms](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)');
    
    // Instantiates a client
    const client = new [KeyManagementServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)();
    
    // Build the key name
    const keyName = client.cryptoKeyPath(projectId, locationId, keyRingId, keyId);
    
    // Optional, but recommended: compute plaintext's CRC32C.
    const crc32c = require('fast-crc32c');
    const plaintextCrc32c = crc32c.calculate(plaintextBuffer);
    
    async function encryptSymmetric() {
      const [encryptResponse] = await client.encrypt({
        name: keyName,
        plaintext: plaintextBuffer,
        plaintextCrc32c: {
          value: plaintextCrc32c,
        },
      });
    
      const ciphertext = encryptResponse.ciphertext;
    
      // Optional, but recommended: perform integrity verification on encryptResponse.
      // For more details on ensuring E2E in-transit integrity to and from Cloud KMS visit:
      // https://cloud.google.com/kms/docs/data-integrity-guidelines
      if (!encryptResponse.verifiedPlaintextCrc32c) {
        throw new Error('Encrypt: request corrupted in-transit');
      }
      if (
        crc32c.calculate(ciphertext) !==
        Number(encryptResponse.ciphertextCrc32c.value)
      ) {
        throw new Error('Encrypt: response corrupted in-transit');
      }
    
      console.log(`Ciphertext: ${ciphertext.toString('base64')}`);
      return ciphertext;
    }
    
    return encryptSymmetric();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Cloud KMS PHP SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-php).
    
    
    use Google\Cloud\Kms\V1\Client\KeyManagementServiceClient;
    use Google\Cloud\Kms\V1\EncryptRequest;
    
    function encrypt_symmetric(
        string $projectId = 'my-project',
        string $locationId = 'us-east1',
        string $keyRingId = 'my-key-ring',
        string $keyId = 'my-key',
        string $plaintext = '...'
    ) {
        // Create the Cloud KMS client.
        $client = new KeyManagementServiceClient();
    
        // Build the key name.
        $keyName = $client->cryptoKeyName($projectId, $locationId, $keyRingId, $keyId);
    
        // Call the API.
        $encryptRequest = (new EncryptRequest())
            ->setName($keyName)
            ->setPlaintext($plaintext);
        $encryptResponse = $client->encrypt($encryptRequest);
        printf('Ciphertext: %s' . PHP_EOL, $encryptResponse->getCiphertext());
    
        return $encryptResponse;
    }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Cloud KMS Python SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-python).
    
    
    # Import base64 for printing the ciphertext.
    import base64
    
    # Import the client library.
    from google.cloud import kms
    
    
    def encrypt_symmetric(
        project_id: str, location_id: str, key_ring_id: str, key_id: str, plaintext: str
    ) -> bytes:
        """
        Encrypt plaintext using a symmetric key.
    
        Args:
            project_id (string): Google Cloud project ID (e.g. 'my-project').
            location_id (string): Cloud KMS location (e.g. 'us-east1').
            key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring').
            key_id (string): ID of the key to use (e.g. 'my-key').
            plaintext (string): message to encrypt
    
        Returns:
            bytes: Encrypted ciphertext.
    
        """
    
        # Convert the plaintext to bytes.
        plaintext_bytes = plaintext.encode("utf-8")
    
        # Optional, but recommended: compute plaintext's CRC32C.
        # See crc32c() function defined below.
        plaintext_crc32c = crc32c(plaintext_bytes)
    
        # Create the client.
        client = kms.[KeyManagementServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html)()
    
        # Build the key name.
        key_name = client.[crypto_key_path](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_crypto_key_path)(project_id, location_id, key_ring_id, key_id)
    
        # Call the API.
        encrypt_response = client.[encrypt](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_encrypt)(
            request={
                "name": key_name,
                "plaintext": plaintext_bytes,
                "plaintext_crc32c": plaintext_crc32c,
            }
        )
    
        # Optional, but recommended: perform integrity verification on encrypt_response.
        # For more details on ensuring E2E in-transit integrity to and from Cloud KMS visit:
        # https://cloud.google.com/kms/docs/data-integrity-guidelines
        if not encrypt_response.verified_plaintext_crc32c:
            raise Exception("The request sent to the server was corrupted in-transit.")
        if not encrypt_response.ciphertext_crc32c == crc32c(encrypt_response.ciphertext):
            raise Exception(
                "The response received from the server was corrupted in-transit."
            )
        # End integrity verification
    
        print(f"Ciphertext: {base64.b64encode(encrypt_response.ciphertext)}")
        return encrypt_response
    
    
    def crc32c(data: bytes) -> int:
        """
        Calculates the CRC32C checksum of the provided data.
    
        Args:
            data: the bytes over which the checksum should be calculated.
    
        Returns:
            An int representing the CRC32C checksum of the provided bytes.
        """
        import crcmod  # type: ignore
    
        crc32c_fun = crcmod.predefined.mkPredefinedCrcFun("crc-32c")
        return crc32c_fun(data)
    
    

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Cloud KMS Ruby SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-ruby).
    
    
    # TODO(developer): uncomment these values before running the sample.
    # project_id  = "my-project"
    # location_id = "us-east1"
    # key_ring_id = "my-key-ring"
    # key_id      = "my-key"
    # plaintext  = "..."
    
    # Require the library.
    require "google/cloud/kms"
    
    # Create the client.
    client = Google::Cloud::[Kms](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms.html).[key_management_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms/latest/Google-Cloud-Kms.html)
    
    # Build the parent key name.
    key_name = client.crypto_key_path project:    project_id,
                                      location:   location_id,
                                      key_ring:   key_ring_id,
                                      crypto_key: key_id
    
    # Call the API.
    response = client.encrypt name: key_name, plaintext: plaintext
    puts "Ciphertext: #{Base64.strict_encode64 response.ciphertext}"

### API

These examples use [curl](https://curl.haxx.se/) as an HTTP client to demonstrate using the API. For more information about access control, see [Accessing the Cloud KMS API](https://docs.cloud.google.com/kms/docs/accessing-the-api). 

When using JSON and the REST API, content must be base64 encoded before it can be encrypted by Cloud KMS.

**Tip** : You can base64-encode or decode data using the `base64` command on Linux or macOS, or the `Base64.exe` command on Windows. Programming and scripting languages typically include libraries for base64-encoding. For command-line examples, see [Base64 Encoding](https://docs.cloud.google.com/vision/docs/base64) in the Cloud Vision API documentation.

To encrypt data, make a `POST` request and provide the appropriate project and key information and specify the base64 encoded text to be encrypted in the `plaintext` field of the request body.
    
    
    curl "https://cloudkms.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME:encrypt" \
      --request "POST" \
      --header "authorization: Bearer TOKEN" \
      --header "content-type: application/json" \
      --data "{\"plaintext\": \"PLAINTEXT_TO_ENCRYPT\"}"
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the key ring and key that you want to use for encryption.
  * `LOCATION`: the Cloud KMS location that contains the key ring.
  * `KEY_RING`: the key ring that contains the key that you want to use for encryption.
  * `KEY_NAME`: the name of the key that you want to use for encryption.
  * `PLAINTEXT_TO_ENCRYPT`: the plaintext data that you want to encrypt. The plaintext must be base64 encoded before you call the `encrypt` method.



Here is an example payload with base64 encoded data:
    
    
    {
      "plaintext": "U3VwZXIgc2VjcmV0IHRleHQgdGhhdCBtdXN0IGJlIGVuY3J5cHRlZAo=",
    }

## Decrypt

### gcloud

To use Cloud KMS on the command line, first [Install or upgrade to the latest version of Google Cloud CLI](https://docs.cloud.google.com/sdk/install).
    
    
    gcloud kms decrypt \
        --key KEY_NAME \
        --keyring KEY_RING \
        --location LOCATION  \
        --ciphertext-file FILE_TO_DECRYPT \
        --plaintext-file DECRYPTED_OUTPUT
    

Replace the following:

  * `KEY_NAME`: the name of the key that you want to use for decryption.
  * `KEY_RING`: the name of the key ring that contains the key.
  * `LOCATION`: the Cloud KMS location that contains the key ring.
  * `FILE_TO_DECRYPT`: the path to the file that you want to decrypt.
  * `DECRYPTED_OUTPUT`: the path where you want to save the decrypted output.



For information on all flags and possible values, run the command with the `--help` flag.

### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Cloud KMS C# SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-csharp).
    
    
    using [Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.html);
    using [Google.Protobuf](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.html);
    using System.Text;
    
    public class DecryptSymmetricSample
    {
        public string DecryptSymmetric(
          string projectId = "my-project", string locationId = "us-east1", string keyRingId = "my-key-ring", string keyId = "my-key",
          byte[] ciphertext = null)
        {
            // Create the client.
            [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_Create)();
    
            // Build the key name.
            [CryptoKeyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyName.html) keyName = new [CryptoKeyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyName.html)(projectId, locationId, keyRingId, keyId);
    
            // Call the API.
            [DecryptResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.DecryptResponse.html) result = client.[Decrypt](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_Decrypt_Google_Cloud_Kms_V1_CryptoKeyName_Google_Protobuf_ByteString_Google_Api_Gax_Grpc_CallSettings_)(keyName, [ByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html).[CopyFrom](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html#Google_Protobuf_ByteString_CopyFrom_System_Byte___)(ciphertext));
    
            // Get the plaintext. Cryptographic plaintexts and ciphertexts are
            // always byte arrays.
            byte[] plaintext = result.[Plaintext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.DecryptResponse.html#Google_Cloud_Kms_V1_DecryptResponse_Plaintext).ToByteArray();
    
            // Return the result.
            return Encoding.UTF8.GetString(plaintext);
        }
    }

### Go

To run this code, first [set up a Go development environment](https://docs.cloud.google.com/go/docs/setup) and [install the Cloud KMS Go SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-go).
    
    
    import (
    	"context"
    	"fmt"
    	"hash/crc32"
    	"io"
    
    	kms "cloud.google.com/go/kms/apiv1"
    	"cloud.google.com/go/kms/apiv1/kmspb"
    	"google.golang.org/protobuf/types/known/wrapperspb"
    )
    
    // decryptSymmetric will decrypt the input ciphertext bytes using the specified symmetric key.
    func decryptSymmetric(w io.Writer, name string, ciphertext []byte) error {
    	// name := "projects/my-project/locations/us-east1/keyRings/my-key-ring/cryptoKeys/my-key"
    	// ciphertext := []byte("...")  // result of a symmetric encryption call
    
    	// Create the client.
    	ctx := context.Background()
    	client, err := kms.[NewKeyManagementClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_NewKeyManagementClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create kms client: %w", err)
    	}
    	defer client.Close()
    
    	// Optional, but recommended: Compute ciphertext's CRC32C.
    	crc32c := func(data []byte) uint32 {
    		t := crc32.MakeTable(crc32.Castagnoli)
    		return crc32.Checksum(data, t)
    	}
    	ciphertextCRC32C := crc32c(ciphertext)
    
    	// Build the request.
    	req := &kmspb.DecryptRequest{
    		Name:             name,
    		Ciphertext:       ciphertext,
    		CiphertextCrc32C: wrapperspb.Int64(int64(ciphertextCRC32C)),
    	}
    
    	// Call the API.
    	result, err := client.Decrypt(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to decrypt ciphertext: %w", err)
    	}
    
    	// Optional, but recommended: perform integrity verification on result.
    	// For more details on ensuring E2E in-transit integrity to and from Cloud KMS visit:
    	// https://cloud.google.com/kms/docs/data-integrity-guidelines
    	if int64(crc32c(result.Plaintext)) != result.PlaintextCrc32C.Value {
    		return fmt.Errorf("Decrypt: response corrupted in-transit")
    	}
    
    	fmt.Fprintf(w, "Decrypted plaintext: %s", result.Plaintext)
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Cloud KMS Java SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-java).
    
    
    import com.google.cloud.kms.v1.[CryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html);
    import com.google.cloud.kms.v1.[DecryptResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.DecryptResponse.html);
    import com.google.cloud.kms.v1.[KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    
    public class DecryptSymmetric {
    
      public void decryptSymmetric() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "us-east1";
        String keyRingId = "my-key-ring";
        String keyId = "my-key";
        byte[] ciphertext = null;
        decryptSymmetric(projectId, locationId, keyRingId, keyId, ciphertext);
      }
    
      // Decrypt data that was encrypted using a symmetric key.
      public void decryptSymmetric(
          String projectId, String locationId, String keyRingId, String keyId, byte[] ciphertext)
          throws IOException {
        // Initialize client that will be used to send requests. This client only
        // needs to be created once, and can be reused for multiple requests. After
        // completing all of your requests, call the "close" method on the client to
        // safely clean up any remaining background resources.
        try ([KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html).create()) {
          // Build the key version name from the project, location, key ring, and
          // key.
          [CryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html) keyName = [CryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html).of(projectId, locationId, keyRingId, keyId);
    
          // Decrypt the response.
          [DecryptResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.DecryptResponse.html) response = client.decrypt(keyName, [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(ciphertext));
          System.out.printf("Plaintext: %s%n", response.[getPlaintext](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.DecryptResponse.html#com_google_cloud_kms_v1_DecryptResponse_getPlaintext__)().toStringUtf8());
        }
      }
    }

### Node.js

To run this code, first [set up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup) and [install the Cloud KMS Node.js SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-nodejs).
    
    
    //
    // TODO(developer): Uncomment these variables before running the sample.
    //
    // const projectId = 'my-project';
    // const locationId = 'us-east1';
    // const keyRingId = 'my-key-ring';
    // const keyId = 'my-key';
    // Ciphertext must be either a Buffer object or a base-64 encoded string
    // const ciphertext = Buffer.from('...');
    
    // Imports the Cloud KMS library
    const {KeyManagementServiceClient} = require('[@google-cloud/kms](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)');
    
    // Instantiates a client
    const client = new [KeyManagementServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)();
    
    // Build the key name
    const keyName = client.cryptoKeyPath(projectId, locationId, keyRingId, keyId);
    
    // Optional, but recommended: compute ciphertext's CRC32C.
    const crc32c = require('fast-crc32c');
    const ciphertextCrc32c = crc32c.calculate(ciphertext);
    
    async function decryptSymmetric() {
      const [decryptResponse] = await client.decrypt({
        name: keyName,
        ciphertext: ciphertext,
        ciphertextCrc32c: {
          value: ciphertextCrc32c,
        },
      });
    
      // Optional, but recommended: perform integrity verification on decryptResponse.
      // For more details on ensuring E2E in-transit integrity to and from Cloud KMS visit:
      // https://cloud.google.com/kms/docs/data-integrity-guidelines
      if (
        crc32c.calculate(decryptResponse.plaintext) !==
        Number(decryptResponse.plaintextCrc32c.value)
      ) {
        throw new Error('Decrypt: response corrupted in-transit');
      }
    
      const plaintext = decryptResponse.plaintext.toString();
    
      console.log(`Plaintext: ${plaintext}`);
      return plaintext;
    }
    
    return decryptSymmetric();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Cloud KMS PHP SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-php).
    
    
    use Google\Cloud\Kms\V1\Client\KeyManagementServiceClient;
    use Google\Cloud\Kms\V1\DecryptRequest;
    
    function decrypt_symmetric(
        string $projectId = 'my-project',
        string $locationId = 'us-east1',
        string $keyRingId = 'my-key-ring',
        string $keyId = 'my-key',
        string $ciphertext = '...'
    ) {
        // Create the Cloud KMS client.
        $client = new KeyManagementServiceClient();
    
        // Build the key name.
        $keyName = $client->cryptoKeyName($projectId, $locationId, $keyRingId, $keyId);
    
        // Call the API.
        $decryptRequest = (new DecryptRequest())
            ->setName($keyName)
            ->setCiphertext($ciphertext);
        $decryptResponse = $client->decrypt($decryptRequest);
        printf('Plaintext: %s' . PHP_EOL, $decryptResponse->getPlaintext());
    
        return $decryptResponse;
    }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Cloud KMS Python SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-python).
    
    
    from google.cloud import kms
    
    
    def decrypt_symmetric(
        project_id: str, location_id: str, key_ring_id: str, key_id: str, ciphertext: bytes
    ) -> kms.DecryptResponse:
        """
        Decrypt the ciphertext using the symmetric key
    
        Args:
            project_id (string): Google Cloud project ID (e.g. 'my-project').
            location_id (string): Cloud KMS location (e.g. 'us-east1').
            key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring').
            key_id (string): ID of the key to use (e.g. 'my-key').
            ciphertext (bytes): Encrypted bytes to decrypt.
    
        Returns:
            DecryptResponse: Response including plaintext.
    
        """
    
        # Create the client.
        client = kms.[KeyManagementServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html)()
    
        # Build the key name.
        key_name = client.[crypto_key_path](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_crypto_key_path)(project_id, location_id, key_ring_id, key_id)
    
        # Optional, but recommended: compute ciphertext's CRC32C.
        # See crc32c() function defined below.
        ciphertext_crc32c = crc32c(ciphertext)
    
        # Call the API.
        decrypt_response = client.[decrypt](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_decrypt)(
            request={
                "name": key_name,
                "ciphertext": ciphertext,
                "ciphertext_crc32c": ciphertext_crc32c,
            }
        )
    
        # Optional, but recommended: perform integrity verification on decrypt_response.
        # For more details on ensuring E2E in-transit integrity to and from Cloud KMS visit:
        # https://cloud.google.com/kms/docs/data-integrity-guidelines
        if not decrypt_response.plaintext_crc32c == crc32c(decrypt_response.plaintext):
            raise Exception(
                "The response received from the server was corrupted in-transit."
            )
        # End integrity verification
    
        print(f"Plaintext: {decrypt_response.plaintext!r}")
        return decrypt_response
    
    
    def crc32c(data: bytes) -> int:
        """
        Calculates the CRC32C checksum of the provided data.
        Args:
            data: the bytes over which the checksum should be calculated.
        Returns:
            An int representing the CRC32C checksum of the provided bytes.
        """
        import crcmod  # type: ignore
    
        crc32c_fun = crcmod.predefined.mkPredefinedCrcFun("crc-32c")
        return crc32c_fun(data)
    
    

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Cloud KMS Ruby SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-ruby).
    
    
    # TODO(developer): uncomment these values before running the sample.
    # project_id  = "my-project"
    # location_id = "us-east1"
    # key_ring_id = "my-key-ring"
    # key_id      = "my-key"
    # ciphertext  = "..."
    
    # Require the library.
    require "google/cloud/kms"
    
    # Create the client.
    client = Google::Cloud::[Kms](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms.html).[key_management_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms/latest/Google-Cloud-Kms.html)
    
    # Build the parent key name.
    key_name = client.crypto_key_path project:    project_id,
                                      location:   location_id,
                                      key_ring:   key_ring_id,
                                      crypto_key: key_id
    
    # Call the API.
    response = client.decrypt name: key_name, ciphertext: ciphertext
    puts "Plaintext: #{response.plaintext}"

### API

These examples use [curl](https://curl.haxx.se/) as an HTTP client to demonstrate using the API. For more information about access control, see [Accessing the Cloud KMS API](https://docs.cloud.google.com/kms/docs/accessing-the-api). 

Decrypted text that is returned in the JSON from Cloud KMS is base64 encoded.

**Tip** : You can base64-encode or decode data using the `base64` command on Linux or macOS, or the `Base64.exe` command on Windows. Programming and scripting languages typically include libraries for base64-encoding. For command-line examples, see [Base64 Encoding](https://docs.cloud.google.com/vision/docs/base64) in the Cloud Vision API documentation.

To decrypt encrypted data, make a `POST` request and provide the appropriate project and key information and specify the encrypted text (also known as _ciphertext_) to be decrypted in the `ciphertext` field of the request body.
    
    
    curl "https://cloudkms.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME:decrypt" \
      --request "POST" \
      --header "authorization: Bearer TOKEN" \
      --header "content-type: application/json" \
      --data "{\"ciphertext\": \"ENCRYPTED_DATA\"}"
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the key ring and key that you want to use for decryption.
  * `LOCATION`: the Cloud KMS location that contains the key ring.
  * `KEY_RING`: the key ring that contains the key that you want to use for decryption.
  * `KEY_NAME`: the name of the key that you want to use for decryption.
  * `ENCRYPTED_DATA`: the encrypted data that you want to decrypt.



Here is an example payload with base64 encoded data:
    
    
    {
      "ciphertext": "CiQAhMwwBo61cHas7dDgifrUFs5zNzBJ2uZtVFq4ZPEl6fUVT4kSmQ...",
    }

## What's next

  * Read more about [raw symmetric encryption](https://docs.cloud.google.com/kms/docs/raw-encryption).
  * Read more about [envelope encryption](https://docs.cloud.google.com/kms/docs/data-encryption-keys).
  * Try the [Encrypt and decrypt data with Cloud KMS Codelab](https://codelabs.developers.google.com/codelabs/encrypt-and-decrypt-data-with-cloud-kms). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
