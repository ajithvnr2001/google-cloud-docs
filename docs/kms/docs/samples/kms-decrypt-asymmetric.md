---
url: https://docs.cloud.google.com/kms/docs/samples/kms-decrypt-asymmetric/
title: Decrypt with an asymmetric key \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:37:05.925423+00:00
---

# Decrypt with an asymmetric key  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/samples/kms-decrypt-asymmetric/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Samples ](https://docs.cloud.google.com/kms/docs/samples)



#  Decrypt with an asymmetric key Stay organized with collections  Save and categorize content based on your preferences. 

Decrypt the ciphertext by using an asymmetric key.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Encrypting and decrypting data with an asymmetric key](https://docs.cloud.google.com/kms/docs/encrypt-decrypt-rsa)



## Code sample

### C#

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.html);
    using [Google.Protobuf](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.html);
    using System.Text;
    
    public class DecryptAsymmetricSample
    {
        public string DecryptAsymmetric(
          string projectId = "my-project", string locationId = "us-east1", string keyRingId = "my-key-ring", string keyId = "my-key", string keyVersionId = "123",
          byte[] ciphertext = null)
        {
            // Create the client.
            [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_Create)();
    
            // Build the key version name.
            [CryptoKeyVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersionName.html) keyVersionName = new [CryptoKeyVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersionName.html)(projectId, locationId, keyRingId, keyId, keyVersionId);
    
            // Call the API.
            [AsymmetricDecryptResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AsymmetricDecryptResponse.html) result = client.[AsymmetricDecrypt](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_AsymmetricDecrypt_Google_Cloud_Kms_V1_AsymmetricDecryptRequest_Google_Api_Gax_Grpc_CallSettings_)(keyVersionName, [ByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html).[CopyFrom](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html#Google_Protobuf_ByteString_CopyFrom_System_Byte___)(ciphertext));
    
            // Get the plaintext. Cryptographic plaintexts and ciphertexts are
            // always byte arrays.
            byte[] plaintext = result.[Plaintext](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AsymmetricDecryptResponse.html#Google_Cloud_Kms_V1_AsymmetricDecryptResponse_Plaintext).ToByteArray();
    
            // Return the result.
            return Encoding.UTF8.GetString(plaintext);
        }
    }

### Go

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"hash/crc32"
    	"io"
    
    	kms "cloud.google.com/go/kms/apiv1"
    	"cloud.google.com/go/kms/apiv1/kmspb"
    	"google.golang.org/protobuf/types/known/wrapperspb"
    )
    
    // decryptAsymmetric will attempt to decrypt a given ciphertext with an
    // 'RSA_DECRYPT_OAEP_2048_SHA256' key from Cloud KMS.
    func decryptAsymmetric(w io.Writer, name string, ciphertext []byte) error {
    	// name := "projects/my-project/locations/us-east1/keyRings/my-key-ring/cryptoKeys/my-key/cryptoKeyVersions/123"
    	// ciphertext := []byte("...")  // result of an asymmetric encryption call
    
    	// Create the client.
    	ctx := context.Background()
    	client, err := kms.[NewKeyManagementClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_NewKeyManagementClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create kms client: %w", err)
    	}
    	defer client.Close()
    
    	// Optional but recommended: Compute ciphertext's CRC32C.
    	crc32c := func(data []byte) uint32 {
    		t := crc32.MakeTable(crc32.Castagnoli)
    		return crc32.Checksum(data, t)
    	}
    	ciphertextCRC32C := crc32c(ciphertext)
    
    	// Build the request.
    	req := &kmspb.AsymmetricDecryptRequest{
    		Name:             name,
    		Ciphertext:       ciphertext,
    		CiphertextCrc32C: wrapperspb.Int64(int64(ciphertextCRC32C)),
    	}
    
    	// Call the API.
    	result, err := client.AsymmetricDecrypt(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to decrypt ciphertext: %w", err)
    	}
    
    	// Optional, but recommended: perform integrity verification on result.
    	// For more details on ensuring E2E in-transit integrity to and from Cloud KMS visit:
    	// https://cloud.google.com/kms/docs/data-integrity-guidelines
    	if result.VerifiedCiphertextCrc32C == false {
    		return fmt.Errorf("AsymmetricDecrypt: request corrupted in-transit")
    	}
    	if int64(crc32c(result.Plaintext)) != result.PlaintextCrc32C.Value {
    		return fmt.Errorf("AsymmetricDecrypt: response corrupted in-transit")
    	}
    
    	fmt.Fprintf(w, "Decrypted plaintext: %s", result.Plaintext)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.kms.v1.[AsymmetricDecryptResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.AsymmetricDecryptResponse.html);
    import com.google.cloud.kms.v1.[CryptoKeyVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionName.html);
    import com.google.cloud.kms.v1.[KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    
    public class DecryptAsymmetric {
    
      public void decryptAsymmetric() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "us-east1";
        String keyRingId = "my-key-ring";
        String keyId = "my-key";
        String keyVersionId = "123";
        byte[] ciphertext = null;
        decryptAsymmetric(projectId, locationId, keyRingId, keyId, keyVersionId, ciphertext);
      }
    
      // Decrypt data that was encrypted using the public key component of the given
      // key version.
      public void decryptAsymmetric(
          String projectId,
          String locationId,
          String keyRingId,
          String keyId,
          String keyVersionId,
          byte[] ciphertext)
          throws IOException {
        // Initialize client that will be used to send requests. This client only
        // needs to be created once, and can be reused for multiple requests. After
        // completing all of your requests, call the "close" method on the client to
        // safely clean up any remaining background resources.
        try ([KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html).create()) {
          // Build the key version name from the project, location, key ring, key,
          // and key version.
          [CryptoKeyVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionName.html) keyVersionName =
              [CryptoKeyVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionName.html).of(projectId, locationId, keyRingId, keyId, keyVersionId);
    
          // Decrypt the ciphertext.
          [AsymmetricDecryptResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.AsymmetricDecryptResponse.html) response =
              client.asymmetricDecrypt(keyVersionName, [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(ciphertext));
          System.out.printf("Plaintext: %s%n", response.[getPlaintext](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.AsymmetricDecryptResponse.html#com_google_cloud_kms_v1_AsymmetricDecryptResponse_getPlaintext__)().toStringUtf8());
        }
      }
    }

### Node.js

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //
    // TODO(developer): Uncomment these variables before running the sample.
    //
    // const projectId = 'my-project';
    // const locationId = 'us-east1';
    // const keyRingId = 'my-key-ring';
    // const keyId = 'my-key';
    // const versionId = '123';
    // const ciphertext = Buffer.from('...');
    
    // Imports the Cloud KMS library
    const {KeyManagementServiceClient} = require('[@google-cloud/kms](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)');
    
    // Instantiates a client
    const client = new [KeyManagementServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)();
    
    // Build the key version name
    const versionName = client.cryptoKeyVersionPath(
      projectId,
      locationId,
      keyRingId,
      keyId,
      versionId
    );
    
    // Optional, but recommended: compute plaintext's CRC32C.
    const crc32c = require('fast-crc32c');
    const ciphertextCrc32c = crc32c.calculate(ciphertext);
    
    async function decryptAsymmetric() {
      const [decryptResponse] = await client.asymmetricDecrypt({
        name: versionName,
        ciphertext: ciphertext,
        ciphertextCrc32c: {
          value: ciphertextCrc32c,
        },
      });
    
      // Optional, but recommended: perform integrity verification on decryptResponse.
      // For more details on ensuring E2E in-transit integrity to and from Cloud KMS visit:
      // https://cloud.google.com/kms/docs/data-integrity-guidelines
      if (!decryptResponse.verifiedCiphertextCrc32c) {
        throw new Error('AsymmetricDecrypt: request corrupted in-transit');
      }
      if (
        crc32c.calculate(decryptResponse.plaintext) !==
        Number(decryptResponse.plaintextCrc32c.value)
      ) {
        throw new Error('AsymmetricDecrypt: response corrupted in-transit');
      }
    
      // NOTE: The ciphertext must be properly formatted. In Node < 12, the
      // crypto.publicEncrypt() function does not properly consume the OAEP
      // padding and thus produces invalid ciphertext. If you are using Node to do
      // public key encryption, please use version 12+.
      const plaintext = decryptResponse.plaintext.toString('utf8');
    
      console.log(`Plaintext: ${plaintext}`);
      return plaintext;
    }
    
    return decryptAsymmetric();

### PHP

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Kms\V1\AsymmetricDecryptRequest;
    use Google\Cloud\Kms\V1\Client\KeyManagementServiceClient;
    
    function decrypt_asymmetric(
        string $projectId = 'my-project',
        string $locationId = 'us-east1',
        string $keyRingId = 'my-key-ring',
        string $keyId = 'my-key',
        string $versionId = '123',
        string $ciphertext = '...'
    ) {
        // Create the Cloud KMS client.
        $client = new KeyManagementServiceClient();
    
        // Build the key version name.
        $keyVersionName = $client->cryptoKeyVersionName($projectId, $locationId, $keyRingId, $keyId, $versionId);
    
        // Call the API.
        $asymmetricDecryptRequest = (new AsymmetricDecryptRequest())
            ->setName($keyVersionName)
            ->setCiphertext($ciphertext);
        $decryptResponse = $client->asymmetricDecrypt($asymmetricDecryptRequest);
        printf('Plaintext: %s' . PHP_EOL, $decryptResponse->getPlaintext());
    
        return $decryptResponse;
    }

### Python

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import kms
    
    
    def decrypt_asymmetric(
        project_id: str,
        location_id: str,
        key_ring_id: str,
        key_id: str,
        version_id: str,
        ciphertext: bytes,
    ) -> kms.DecryptResponse:
        """
        Decrypt the ciphertext using an asymmetric key.
    
        Args:
            project_id (string): Google Cloud project ID (e.g. 'my-project').
            location_id (string): Cloud KMS location (e.g. 'us-east1').
            key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring').
            key_id (string): ID of the key to use (e.g. 'my-key').
            version_id (string): ID of the key version to use (e.g. '1').
            ciphertext (bytes): Encrypted bytes to decrypt.
    
        Returns:
            DecryptResponse: Response including plaintext.
    
        """
    
        # Create the client.
        client = kms.[KeyManagementServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html)()
    
        # Build the key version name.
        key_version_name = client.[crypto_key_version_path](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_crypto_key_version_path)(
            project_id, location_id, key_ring_id, key_id, version_id
        )
    
        # Optional, but recommended: compute ciphertext's CRC32C.
        # See crc32c() function defined below.
        ciphertext_crc32c = crc32c(ciphertext)
    
        # Call the API.
        decrypt_response = client.[asymmetric_decrypt](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_asymmetric_decrypt)(
            request={
                "name": key_version_name,
                "ciphertext": ciphertext,
                "ciphertext_crc32c": ciphertext_crc32c,
            }
        )
    
        # Optional, but recommended: perform integrity verification on decrypt_response.
        # For more details on ensuring E2E in-transit integrity to and from Cloud KMS visit:
        # https://cloud.google.com/kms/docs/data-integrity-guidelines
        if not decrypt_response.verified_ciphertext_crc32c:
            raise Exception("The request sent to the server was corrupted in-transit.")
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

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # TODO(developer): uncomment these values before running the sample.
    # project_id  = "my-project"
    # location_id = "us-east1"
    # key_ring_id = "my-key-ring"
    # key_id      = "my-key"
    # version_id  = "123"
    # ciphertext  = "..."
    
    # Require the library.
    require "google/cloud/kms"
    
    # Create the client.
    client = Google::Cloud::[Kms](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms.html).[key_management_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms/latest/Google-Cloud-Kms.html)
    
    # Build the key version name.
    key_version_name = client.[crypto_key_version_path](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-KeyManagementService-Paths.html) project:            project_id,
                                                      location:           location_id,
                                                      key_ring:           key_ring_id,
                                                      crypto_key:         key_id,
                                                      crypto_key_version: version_id
    
    # Call the API.
    response = client.asymmetric_decrypt key_version_name, ciphertext
    puts "Plaintext: #{response.plaintext}"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudkeymanagementservice). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
