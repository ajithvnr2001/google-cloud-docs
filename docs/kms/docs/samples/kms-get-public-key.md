---
url: https://docs.cloud.google.com/kms/docs/samples/kms-get-public-key/
title: Get the public key for an asymmetric key \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:42.734890+00:00
---

# Get the public key for an asymmetric key  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/samples/kms-get-public-key/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Samples ](https://docs.cloud.google.com/kms/docs/samples)



#  Get the public key for an asymmetric key Stay organized with collections  Save and categorize content based on your preferences. 

Get the public key for an asymmetric key.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create a key](https://docs.cloud.google.com/kms/docs/create-key)
  * [Retrieve a public key](https://docs.cloud.google.com/kms/docs/retrieve-public-key)



## Code sample

### C#

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.html);
    
    public class GetPublicKeySample
    {
        public PublicKey GetPublicKey(string projectId = "my-project", string locationId = "us-east1", string keyRingId = "my-key-ring", string keyId = "my-key", string keyVersionId = "123")
        {
            // Create the client.
            [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_Create)();
    
            // Build the key version name.
            [CryptoKeyVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersionName.html) keyVersionName = new [CryptoKeyVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersionName.html)(projectId, locationId, keyRingId, keyId, keyVersionId);
    
            // Call the API.
            [PublicKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.PublicKey.html) result = client.[GetPublicKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_GetPublicKey_Google_Cloud_Kms_V1_CryptoKeyVersionName_Google_Api_Gax_Grpc_CallSettings_)(keyVersionName);
    
            // Return the ciphertext.
            return result;
        }
    }

### Go

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"crypto/x509"
    	"encoding/pem"
    	"fmt"
    	"hash/crc32"
    	"io"
    
    	kms "cloud.google.com/go/kms/apiv1"
    	"cloud.google.com/go/kms/apiv1/kmspb"
    )
    
    // getPublicKey retrieves the public key from an asymmetric key pair on
    // Cloud KMS.
    func getPublicKey(w io.Writer, name string) error {
    	// name := "projects/my-project/locations/us-east1/keyRings/my-key-ring/cryptoKeys/my-key/cryptoKeyVersions/123"
    
    	// Create the client.
    	ctx := context.Background()
    	client, err := kms.[NewKeyManagementClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_NewKeyManagementClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create kms client: %w", err)
    	}
    	defer client.Close()
    
    	// Build the request.
    	req := &kmspb.GetPublicKeyRequest{
    		Name: name,
    	}
    
    	// Call the API.
    	result, err := client.GetPublicKey(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to get public key: %w", err)
    	}
    
    	// The 'Pem' field is the raw string representation of the public key.
    	// Convert 'Pem' into bytes for further processing.
    	key := []byte(result.Pem)
    
    	// Optional, but recommended: perform integrity verification on result.
    	// For more details on ensuring E2E in-transit integrity to and from Cloud KMS visit:
    	// https://cloud.google.com/kms/docs/data-integrity-guidelines
    	crc32c := func(data []byte) uint32 {
    		t := crc32.MakeTable(crc32.Castagnoli)
    		return crc32.Checksum(data, t)
    	}
    	if int64(crc32c(key)) != result.PemCrc32C.Value {
    		return fmt.Errorf("getPublicKey: response corrupted in-transit")
    	}
    
    	// Optional - parse the public key. This transforms the string key into a Go
    	// PublicKey.
    	block, _ := pem.Decode(key)
    	publicKey, err := x509.ParsePKIXPublicKey(block.Bytes)
    	if err != nil {
    		return fmt.Errorf("failed to parse public key: %w", err)
    	}
    	fmt.Fprintf(w, "Retrieved public key: %v\n", publicKey)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.kms.v1.[CryptoKeyVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionName.html);
    import com.google.cloud.kms.v1.[KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html);
    import com.google.cloud.kms.v1.[PublicKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.PublicKey.html);
    import java.io.IOException;
    import java.security.GeneralSecurityException;
    
    public class GetPublicKey {
    
      public void getPublicKey() throws IOException, GeneralSecurityException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "us-east1";
        String keyRingId = "my-key-ring";
        String keyId = "my-key";
        String keyVersionId = "123";
        getPublicKey(projectId, locationId, keyRingId, keyId, keyVersionId);
      }
    
      // Get the public key associated with an asymmetric key.
      public void getPublicKey(
          String projectId, String locationId, String keyRingId, String keyId, String keyVersionId)
          throws IOException, GeneralSecurityException {
        // Initialize client that will be used to send requests. This client only
        // needs to be created once, and can be reused for multiple requests. After
        // completing all of your requests, call the "close" method on the client to
        // safely clean up any remaining background resources.
        try ([KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html).create()) {
          // Build the key version name from the project, location, key ring, key,
          // and key version.
          [CryptoKeyVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionName.html) keyVersionName =
              [CryptoKeyVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionName.html).of(projectId, locationId, keyRingId, keyId, keyVersionId);
    
          // Get the public key.
          [PublicKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.PublicKey.html) publicKey = client.getPublicKey(keyVersionName);
          System.out.printf("Public key: %s%n", publicKey.[getPem](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.PublicKey.html#com_google_cloud_kms_v1_PublicKey_getPem__)());
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
    
    async function getPublicKey() {
      const [publicKey] = await client.getPublicKey({
        name: versionName,
      });
    
      // Optional, but recommended: perform integrity verification on publicKey.
      // For more details on ensuring E2E in-transit integrity to and from Cloud KMS visit:
      // https://cloud.google.com/kms/docs/data-integrity-guidelines
      const crc32c = require('fast-crc32c');
      if (publicKey.name !== versionName) {
        throw new Error('GetPublicKey: request corrupted in-transit');
      }
      if (crc32c.calculate(publicKey.pem) !== Number(publicKey.pemCrc32c.value)) {
        throw new Error('GetPublicKey: response corrupted in-transit');
      }
    
      console.log(`Public key pem: ${publicKey.pem}`);
    
      return publicKey;
    }
    
    return getPublicKey();

### PHP

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Kms\V1\Client\KeyManagementServiceClient;
    use Google\Cloud\Kms\V1\GetPublicKeyRequest;
    
    function get_public_key(
        string $projectId = 'my-project',
        string $locationId = 'us-east1',
        string $keyRingId = 'my-key-ring',
        string $keyId = 'my-key',
        string $versionId = '123'
    ) {
        // Create the Cloud KMS client.
        $client = new KeyManagementServiceClient();
    
        // Build the key version name.
        $keyVersionName = $client->cryptoKeyVersionName($projectId, $locationId, $keyRingId, $keyId, $versionId);
    
        // Call the API.
        $getPublicKeyRequest = (new GetPublicKeyRequest())
            ->setName($keyVersionName);
        $publicKey = $client->getPublicKey($getPublicKeyRequest);
        printf('Public key: %s' . PHP_EOL, $publicKey->getPem());
    
        return $publicKey;
    }

### Python

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import kms
    
    
    def get_public_key(
        project_id: str, location_id: str, key_ring_id: str, key_id: str, version_id: str
    ) -> kms.PublicKey:
        """
        Get the public key for an asymmetric key.
    
        Args:
            project_id (string): Google Cloud project ID (e.g. 'my-project').
            location_id (string): Cloud KMS location (e.g. 'us-east1').
            key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring').
            key_id (string): ID of the key to use (e.g. 'my-key').
            version_id (string): ID of the key to use (e.g. '1').
    
        Returns:
            PublicKey: Cloud KMS public key response.
    
        """
    
        # Create the client.
        client = kms.[KeyManagementServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html)()
    
        # Build the key version name.
        key_version_name = client.[crypto_key_version_path](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_crypto_key_version_path)(
            project_id, location_id, key_ring_id, key_id, version_id
        )
    
        # Call the API.
        public_key = client.[get_public_key](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_get_public_key)(request={"name": key_version_name})
    
        # Optional, but recommended: perform integrity verification on public_key.
        # For more details on ensuring E2E in-transit integrity to and from Cloud KMS visit:
        # https://cloud.google.com/kms/docs/data-integrity-guidelines
        if not public_key.name == key_version_name:
            raise Exception("The request sent to the server was corrupted in-transit.")
        # See crc32c() function defined below.
        if not public_key.pem_crc32c == crc32c(public_key.pem.encode("utf-8")):
            raise Exception(
                "The response received from the server was corrupted in-transit."
            )
        # End integrity verification
    
        print(f"Public key: {public_key.pem}")
        return public_key
    
    
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
    public_key = client.get_public_key name: key_version_name
    puts "Public key: #{public_key.pem}"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudkeymanagementservice). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
