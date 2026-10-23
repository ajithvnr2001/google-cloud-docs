---
url: https://docs.cloud.google.com/kms/docs/samples/kms-create-key-for-import/
title: Create a key for import \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:50.650956+00:00
---

# Create a key for import  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/samples/kms-create-key-for-import/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Samples ](https://docs.cloud.google.com/kms/docs/samples)



#  Create a key for import Stay organized with collections  Save and categorize content based on your preferences. 

Set up an empty key for importing your own crypto key.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Import a key version into Cloud KMS](https://docs.cloud.google.com/kms/docs/importing-a-key)



## Code sample

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
    
    // createKeyForImport creates a new asymmetric signing key in Cloud HSM.
    func createKeyForImport(w io.Writer, parent, id string) error {
    	// parent := "projects/my-project/locations/us-east1/keyRings/my-key-ring"
    	// id := "my-imported-key"
    
    	// Create the client.
    	ctx := context.Background()
    	client, err := kms.[NewKeyManagementClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_NewKeyManagementClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create kms client: %w", err)
    	}
    	defer client.Close()
    
    	// Build the request.
    	req := &kmspb.CreateCryptoKeyRequest{
    		Parent:      parent,
    		CryptoKeyId: id,
    		CryptoKey: &kmspb.CryptoKey{
    			Purpose: kmspb.[CryptoKey_ASYMMETRIC_SIGN](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1/kmspb.html#cloud_google_com_go_kms_apiv1_kmspb_CryptoKey_CRYPTO_KEY_PURPOSE_UNSPECIFIED_CryptoKey_ENCRYPT_DECRYPT_CryptoKey_ASYMMETRIC_SIGN_CryptoKey_ASYMMETRIC_DECRYPT_CryptoKey_RAW_ENCRYPT_DECRYPT_CryptoKey_MAC_CryptoKey_KEY_ENCAPSULATION_CryptoKey_AES_WRAPPING),
    			VersionTemplate: &kmspb.CryptoKeyVersionTemplate{
    				ProtectionLevel: kmspb.[ProtectionLevel_HSM](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1/kmspb.html#cloud_google_com_go_kms_apiv1_kmspb_ProtectionLevel_PROTECTION_LEVEL_UNSPECIFIED_ProtectionLevel_SOFTWARE_ProtectionLevel_HSM_ProtectionLevel_EXTERNAL_ProtectionLevel_EXTERNAL_VPC_ProtectionLevel_HSM_SINGLE_TENANT),
    				Algorithm:       kmspb.[CryptoKeyVersion_EC_SIGN_P256_SHA256](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1/kmspb.html#cloud_google_com_go_kms_apiv1_kmspb_CryptoKeyVersion_CRYPTO_KEY_VERSION_ALGORITHM_UNSPECIFIED_CryptoKeyVersion_GOOGLE_SYMMETRIC_ENCRYPTION_CryptoKeyVersion_AES_128_GCM_CryptoKeyVersion_AES_256_GCM_CryptoKeyVersion_AES_128_CBC_CryptoKeyVersion_AES_256_CBC_CryptoKeyVersion_AES_128_CTR_CryptoKeyVersion_AES_256_CTR_CryptoKeyVersion_RSA_SIGN_PSS_2048_SHA256_CryptoKeyVersion_RSA_SIGN_PSS_3072_SHA256_CryptoKeyVersion_RSA_SIGN_PSS_4096_SHA256_CryptoKeyVersion_RSA_SIGN_PSS_4096_SHA512_CryptoKeyVersion_RSA_SIGN_PKCS1_2048_SHA256_CryptoKeyVersion_RSA_SIGN_PKCS1_3072_SHA256_CryptoKeyVersion_RSA_SIGN_PKCS1_4096_SHA256_CryptoKeyVersion_RSA_SIGN_PKCS1_4096_SHA512_CryptoKeyVersion_RSA_SIGN_RAW_PKCS1_2048_CryptoKeyVersion_RSA_SIGN_RAW_PKCS1_3072_CryptoKeyVersion_RSA_SIGN_RAW_PKCS1_4096_CryptoKeyVersion_RSA_DECRYPT_OAEP_2048_SHA256_CryptoKeyVersion_RSA_DECRYPT_OAEP_3072_SHA256_CryptoKeyVersion_RSA_DECRYPT_OAEP_4096_SHA256_CryptoKeyVersion_RSA_DECRYPT_OAEP_4096_SHA512_CryptoKeyVersion_RSA_DECRYPT_OAEP_2048_SHA1_CryptoKeyVersion_RSA_DECRYPT_OAEP_3072_SHA1_CryptoKeyVersion_RSA_DECRYPT_OAEP_4096_SHA1_CryptoKeyVersion_EC_SIGN_P256_SHA256_CryptoKeyVersion_EC_SIGN_P384_SHA384_CryptoKeyVersion_EC_SIGN_SECP256K1_SHA256_CryptoKeyVersion_EC_SIGN_ED25519_CryptoKeyVersion_HMAC_SHA256_CryptoKeyVersion_HMAC_SHA1_CryptoKeyVersion_HMAC_SHA384_CryptoKeyVersion_HMAC_SHA512_CryptoKeyVersion_HMAC_SHA224_CryptoKeyVersion_EXTERNAL_SYMMETRIC_ENCRYPTION_CryptoKeyVersion_ML_KEM_768_CryptoKeyVersion_ML_KEM_1024_CryptoKeyVersion_KEM_XWING_CryptoKeyVersion_PQ_SIGN_ML_DSA_44_CryptoKeyVersion_PQ_SIGN_ML_DSA_65_CryptoKeyVersion_PQ_SIGN_ML_DSA_87_CryptoKeyVersion_PQ_SIGN_SLH_DSA_SHA2_128S_CryptoKeyVersion_PQ_SIGN_HASH_SLH_DSA_SHA2_128S_SHA256_CryptoKeyVersion_PQ_SIGN_ML_DSA_44_EXTERNAL_MU_CryptoKeyVersion_PQ_SIGN_ML_DSA_65_EXTERNAL_MU_CryptoKeyVersion_PQ_SIGN_ML_DSA_87_EXTERNAL_MU_CryptoKeyVersion_AES_256_KWP),
    			},
    			// Ensure that only imported versions may be added to this key.
    			ImportOnly: true,
    		},
    		SkipInitialVersionCreation: true,
    	}
    
    	// Call the API.
    	result, err := client.CreateCryptoKey(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to create key: %w", err)
    	}
    	fmt.Fprintf(w, "Created key: %s\n", result.Name)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.kms.v1.[CreateCryptoKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CreateCryptoKeyRequest.html);
    import com.google.cloud.kms.v1.[CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html);
    import com.google.cloud.kms.v1.[CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html).[CryptoKeyPurpose](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.html);
    import com.google.cloud.kms.v1.[CryptoKeyVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html).[CryptoKeyVersionAlgorithm](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionAlgorithm.html);
    import com.google.cloud.kms.v1.[CryptoKeyVersionTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionTemplate.html);
    import com.google.cloud.kms.v1.[KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html);
    import com.google.cloud.kms.v1.[KeyRingName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRingName.html);
    import com.google.cloud.kms.v1.[ProtectionLevel](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ProtectionLevel.html);
    import java.io.IOException;
    
    public class CreateKeyForImport {
    
      public void createKeyForImport() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "us-east1";
        String keyRingId = "my-key-ring";
        String id = "my-import-key";
        createKeyForImport(projectId, locationId, keyRingId, id);
      }
    
      // Create a new crypto key to hold imported key versions.
      public void createKeyForImport(String projectId, String locationId, String keyRingId, String id)
          throws IOException {
        // Initialize client that will be used to send requests. This client only
        // needs to be created once, and can be reused for multiple requests. After
        // completing all of your requests, call the "close" method on the client to
        // safely clean up any remaining background resources.
        try ([KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html).create()) {
          // Build the parent name from the project, location, and key ring.
          [KeyRingName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRingName.html) keyRingName = [KeyRingName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRingName.html).of(projectId, locationId, keyRingId);
    
          // Create the crypto key.
          [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html) createdKey =
              client.createCryptoKey(
                  [CreateCryptoKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CreateCryptoKeyRequest.html).newBuilder()
                      .setParent(keyRingName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRingName.html#com_google_cloud_kms_v1_KeyRingName_toString__)())
                      .[setCryptoKeyId](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CreateCryptoKeyRequest.Builder.html#com_google_cloud_kms_v1_CreateCryptoKeyRequest_Builder_setCryptoKeyId_java_lang_String_)(id)
                      .setCryptoKey(
                          [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html).newBuilder()
                              .[setPurpose](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.Builder.html#com_google_cloud_kms_v1_CryptoKey_Builder_setPurpose_com_google_cloud_kms_v1_CryptoKey_CryptoKeyPurpose_)([CryptoKeyPurpose](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.html).ASYMMETRIC_SIGN)
                              .[setVersionTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.Builder.html#com_google_cloud_kms_v1_CryptoKey_Builder_setVersionTemplate_com_google_cloud_kms_v1_CryptoKeyVersionTemplate_)(
                                  [CryptoKeyVersionTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionTemplate.html).newBuilder()
                                      .setProtectionLevel([ProtectionLevel](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ProtectionLevel.html).HSM)
                                      .setAlgorithm([CryptoKeyVersionAlgorithm](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionAlgorithm.html).EC_SIGN_P256_SHA256))
                              // Ensure that only imported versions may be
                              // added to this key.
                              .[setImportOnly](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.Builder.html#com_google_cloud_kms_v1_CryptoKey_Builder_setImportOnly_boolean_)(true))
                      .[setSkipInitialVersionCreation](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CreateCryptoKeyRequest.Builder.html#com_google_cloud_kms_v1_CreateCryptoKeyRequest_Builder_setSkipInitialVersionCreation_boolean_)(true)
                      .build());
    
          System.out.printf("Created crypto key %s%n", createdKey.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html#com_google_cloud_kms_v1_CryptoKey_getName__)());
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
    // const id = 'my-imported-key';
    
    // Imports the Cloud KMS library
    const {KeyManagementServiceClient} = require('[@google-cloud/kms](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)');
    
    // Instantiates a client
    const client = new [KeyManagementServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)();
    
    // Build the parent key ring name
    const keyRingName = client.keyRingPath(projectId, locationId, keyRingId);
    
    async function createKeyForImport() {
      const [key] = await client.createCryptoKey({
        parent: keyRingName,
        cryptoKeyId: id,
        cryptoKey: {
          purpose: 'ENCRYPT_DECRYPT',
          versionTemplate: {
            algorithm: 'GOOGLE_SYMMETRIC_ENCRYPTION',
            protectionLevel: 'HSM',
          },
          // Optional: ensure that only imported versions may be added to this
          // key.
          importOnly: true,
        },
        // Do not allow KMS to generate an initial version of this key.
        skipInitialVersionCreation: true,
      });
    
      console.log(`Created key for import: ${key.name}`);
      return key;
    }
    
    return createKeyForImport();

### Python

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import kms
    
    
    def create_key_for_import(
        project_id: str, location_id: str, key_ring_id: str, crypto_key_id: str
    ) -> None:
        """
    
        Sets up an empty CryptoKey within a KeyRing for import.
    
    
        Args:
            project_id (string): Google Cloud project ID (e.g. 'my-project').
            location_id (string): Cloud KMS location (e.g. 'us-east1').
            key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring').
            crypto_key_id (string): ID of the key to import (e.g. 'my-asymmetric-signing-key').
        """
    
        # Create the client.
        client = kms.[KeyManagementServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html)()
    
        # Build the key. For more information regarding allowed values of these fields, see:
        # https://googleapis.dev/python/cloudkms/latest/_modules/google/cloud/kms_v1/types/resources.html
        purpose = kms.[CryptoKey](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKey.html).[CryptoKeyPurpose](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKey.CryptoKeyPurpose.html).ASYMMETRIC_SIGN
        algorithm = kms.[CryptoKeyVersion](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKeyVersion.html).[CryptoKeyVersionAlgorithm](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKeyVersion.CryptoKeyVersionAlgorithm.html).EC_SIGN_P256_SHA256
        protection_level = kms.[ProtectionLevel](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.ProtectionLevel.html).HSM
        key = {
            "purpose": purpose,
            "version_template": {
                "algorithm": algorithm,
                "protection_level": protection_level,
            },
        }
    
        # Build the parent key ring name.
        key_ring_name = client.[key_ring_path](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_key_ring_path)(project_id, location_id, key_ring_id)
    
        # Call the API.
        created_key = client.[create_crypto_key](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_create_crypto_key)(
            request={
                "parent": key_ring_name,
                "crypto_key_id": crypto_key_id,
                "crypto_key": key,
                # Do not allow KMS to generate an initial version of this key.
                "skip_initial_version_creation": True,
            }
        )
        print(f"Created hsm key: {created_key.name}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudkeymanagementservice). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
