---
url: https://docs.cloud.google.com/kms/docs/samples/kms-get-key-version-attestation/
title: Get a key version's attestation \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:30.738792+00:00
---

# Get a key version's attestation  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/samples/kms-get-key-version-attestation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Samples ](https://docs.cloud.google.com/kms/docs/samples)



#  Get a key version's attestation Stay organized with collections  Save and categorize content based on your preferences. 

Get an HSM-backend key's attestation.

## Code sample

### C#

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.html);
    using System;
    
    public class GetKeyVersionAttestationSample
    {
        public byte[] GetKeyVersionAttestation(
          string projectId = "my-project", string locationId = "us-east1", string keyRingId = "my-key-ring", string keyId = "my-key", string keyVersionId = "123")
        {
            // Create the client.
            [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_Create)();
    
            // Build the key name.
            [CryptoKeyVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersionName.html) keyVersionName = new [CryptoKeyVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersionName.html)(projectId, locationId, keyRingId, keyId, keyVersionId);
    
            // Call the API.
            [CryptoKeyVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.html) result = client.[GetCryptoKeyVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_GetCryptoKeyVersion_Google_Cloud_Kms_V1_CryptoKeyVersionName_Google_Api_Gax_Grpc_CallSettings_)(keyVersionName);
    
            // Only HSM keys have an attestation. For other key types, the attestion
            // will be nil.
            [KeyOperationAttestation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyOperationAttestation.html) attestation = result.[Attestation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.html#Google_Cloud_Kms_V1_CryptoKeyVersion_Attestation);
            if (attestation == null)
            {
                throw new InvalidOperationException("no attestation");
            }
    
            // Return the attestation.
            return attestation.[Content](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyOperationAttestation.html#Google_Cloud_Kms_V1_KeyOperationAttestation_Content).ToByteArray();
        }
    }

### Go

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	kms "cloud.google.com/go/kms/apiv1"
    	"cloud.google.com/go/kms/apiv1/kmspb"
    )
    
    // getKeyVersionAttestation gets the attestation on a key version, if one
    // exists.
    func getKeyVersionAttestation(w io.Writer, name string) error {
    	// name := "projects/my-project/locations/us-east1/keyRings/my-key-ring/cryptoKeys/my-key/cryptoKeyVersions/123"
    
    	// Create the client.
    	ctx := context.Background()
    	client, err := kms.[NewKeyManagementClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_NewKeyManagementClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create kms client: %w", err)
    	}
    
    	// Build the request.
    	req := &kmspb.GetCryptoKeyVersionRequest{
    		Name: name,
    	}
    
    	// Call the API.
    	result, err := client.GetCryptoKeyVersion(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to get key: %w", err)
    	}
    
    	// Only HSM keys have an attestation. For other key types, the attestion will
    	// be nil.
    	attestation := result.Attestation
    	if attestation == nil {
    		return fmt.Errorf("no attestation for %s", name)
    	}
    
    	// Print the attestation, hex-encoded.
    	fmt.Fprintf(w, "%s: %x", attestation.Format, attestation.Content)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.kms.v1.[CryptoKeyVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html);
    import com.google.cloud.kms.v1.[CryptoKeyVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionName.html);
    import com.google.cloud.kms.v1.[KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html);
    import com.google.cloud.kms.v1.[KeyOperationAttestation](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyOperationAttestation.html);
    import java.io.IOException;
    import java.util.Base64;
    
    public class GetKeyVersionAttestation {
    
      public void getKeyVersionAttestation() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "us-east1";
        String keyRingId = "my-key-ring";
        String keyId = "my-key";
        String keyVersionId = "123";
        getKeyVersionAttestation(projectId, locationId, keyRingId, keyId, keyVersionId);
      }
    
      // Get the attestations for a key version
      public void getKeyVersionAttestation(
          String projectId, String locationId, String keyRingId, String keyId, String keyVersionId)
          throws IOException {
        // Initialize client that will be used to send requests. This client only
        // needs to be created once, and can be reused for multiple requests. After
        // completing all of your requests, call the "close" method on the client to
        // safely clean up any remaining background resources.
        try ([KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html).create()) {
          // Build the name from the project, location, key ring, and keyId.
          [CryptoKeyVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionName.html) keyVersionName =
              [CryptoKeyVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionName.html).of(projectId, locationId, keyRingId, keyId, keyVersionId);
    
          // Get the key version.
          [CryptoKeyVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html) keyVersion = client.getCryptoKeyVersion(keyVersionName);
    
          // Only HSM keys have an attestation. For other key types, the attestion
          // will be nil.
          if (!keyVersion.[hasAttestation](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html#com_google_cloud_kms_v1_CryptoKeyVersion_hasAttestation__)()) {
            System.out.println("no attestation");
            return;
          }
    
          // Print the attestation, base64-encoded.
          [KeyOperationAttestation](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyOperationAttestation.html) attestation = keyVersion.[getAttestation](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html#com_google_cloud_kms_v1_CryptoKeyVersion_getAttestation__)();
          String format = attestation.[getFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyOperationAttestation.html#com_google_cloud_kms_v1_KeyOperationAttestation_getFormat__)().toString();
          byte[] content = attestation.[getContent](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyOperationAttestation.html#com_google_cloud_kms_v1_KeyOperationAttestation_getContent__)().toByteArray();
          System.out.printf("%s: %s", format, Base64.getEncoder().encodeToString(content));
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
    
    async function getKeyVersionAttestation() {
      const [version] = await client.getCryptoKeyVersion({
        name: versionName,
      });
    
      // Only HSM keys have an attestation. For other key types, the attestion
      // will be nil.
      const attestation = version.attestation;
      if (!attestation) {
        throw new Error('no attestation');
      }
    
      console.log(`Attestation: ${attestation.toString('base64')}`);
      return attestation.content;
    }
    
    return getKeyVersionAttestation();

### PHP

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Kms\V1\Client\KeyManagementServiceClient;
    use Google\Cloud\Kms\V1\GetCryptoKeyVersionRequest;
    
    function get_key_version_attestation(
        string $projectId = 'my-project',
        string $locationId = 'us-east1',
        string $keyRingId = 'my-key-ring',
        string $keyId = 'my-key',
        string $versionId = '123'
    ) {
        // Create the Cloud KMS client.
        $client = new KeyManagementServiceClient();
    
        // Build the key name.
        $keyVersionName = $client->cryptokeyVersionName($projectId, $locationId, $keyRingId, $keyId, $versionId);
    
        // Call the API.
        $getCryptoKeyVersionRequest = (new GetCryptoKeyVersionRequest())
            ->setName($keyVersionName);
        $version = $client->getCryptoKeyVersion($getCryptoKeyVersionRequest);
    
        // Only HSM keys have an attestation. For other key types, the attestion
        // will be NULL.
        $attestation = $version->getAttestation();
        if (!$attestation) {
            throw new Exception('no attestation - attestations only exist on HSM keys');
        }
    
        printf('Got key attestation: %s' . PHP_EOL, $attestation->getContent());
    
        return $attestation;
    }

### Python

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import kms
    
    
    def get_key_version_attestation(
        project_id: str, location_id: str, key_ring_id: str, key_id: str, version_id: str
    ) -> kms.KeyOperationAttestation:
        """
        Get an HSM-backend key's attestation.
    
        Args:
            project_id (string): Google Cloud project ID (e.g. 'my-project').
            location_id (string): Cloud KMS location (e.g. 'us-east1').
            key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring').
            key_id (string): ID of the key to use (e.g. 'my-key').
            version_id (string): ID of the version to use (e.g. '1').
    
        Returns:
            Attestation: Cloud KMS key attestation.
    
        """
    
        # Import base64 for printing the attestation.
        import base64
    
        # Create the client.
        client = kms.[KeyManagementServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html)()
    
        # Build the key version name.
        key_version_name = client.[crypto_key_version_path](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_crypto_key_version_path)(
            project_id, location_id, key_ring_id, key_id, version_id
        )
    
        # Call the API.
        version = client.[get_crypto_key_version](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_get_crypto_key_version)(request={"name": key_version_name})
    
        # Only HSM keys have an attestation. For other key types, the attestion
        # will be None.
        attestation = version.attestation
        if not attestation:
            raise "no attestation - attestations only exist on HSM keys"
    
        encoded_attestation = base64.b64encode(attestation.content)
        print(f"Got key attestation: {encoded_attestation!r}")
        return attestation
    
    

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
    version = client.get_crypto_key_version name: key_version_name
    
    # Only HSM keys have an attestation. For other key types, the attestion will
    # be nil.
    attestation = version.attestation
    unless attestation
      raise "no attestation"
    end
    
    puts "Attestation: #{Base64.strict_encode64 attestation.[content](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-KeyOperationAttestation.html)}"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudkeymanagementservice). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
