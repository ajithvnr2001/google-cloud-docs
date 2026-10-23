---
url: https://docs.cloud.google.com/kms/docs/rotate-key/
title: Rotate a key \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:47.875464+00:00
---

# Rotate a key  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/rotate-key/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Rotate a key Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to automatically or manually rotate a key. For more information about key rotation in general, see [Key rotation](https://docs.cloud.google.com/kms/docs/key-rotation).

## Required roles

To get the permissions that you need to rotate keys, ask your administrator to grant you the following IAM roles on your key: 

  * [Cloud KMS Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.admin) (`roles/cloudkms.admin`)
  * Re-encrypt data: [Cloud KMS CryptoKey Encrypter/Decrypter ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.cryptoKeyEncrypterDecrypter) (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to rotate keys. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to rotate keys:

  * Change primary key version: `cloudkms.cryptoKeys.update`
  * Change or disable auto-rotate: `cloudkms.cryptoKeys.update`
  * Create new key version: `cloudkms.cryptoKeyVersions.create`
  * Disable old key versions: `cloudkms.cryptoKeyVersions.update`
  * Re-encrypt data: 
    * `cloudkms.cryptoKeyVersions.useToDecrypt`
    * `cloudkms.cryptoKeyVersions.useToEncrypt`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

A single user with a custom role containing all of these permissions can rotate keys and re-encrypt data on their own. Users in the Cloud KMS Admin role and Cloud KMS CryptoKey Encrypter/Decrypter role can work together to rotate keys and re-encrypt data. Follow the principle of [least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege) when assigning roles. For more details, see [Permissions and roles](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles).

When you rotate a key, data that was encrypted with previous key versions isn't automatically re-encrypted. To learn more, see [decrypt and re-encrypt](https://docs.cloud.google.com/kms/docs/re-encrypt-data). Rotating a key does not automatically [disable](https://docs.cloud.google.com/kms/docs/enable-disable) or [destroy](https://docs.cloud.google.com/kms/docs/destroy-restore) any existing key versions. Destroying key versions that are no longer needed helps to reduce costs.

## Configure automatic rotation

**Note:** Automatic rotation isn't supported for asymmetric signing or asymmetric encryption keys. For more information, see [Considerations for asymmetric keys](https://docs.cloud.google.com/kms/docs/key-rotation#asymmetric).

### Create a new key with a custom rotation schedule

To configure automatic rotation when creating a new key:

### Console

When you use the Google Cloud console to create a key, Cloud KMS sets the rotation period and next rotation time automatically. You can choose to use the default values or specify different values.

To specify a different rotation period and starting time, when you're [creating your key](https://docs.cloud.google.com/kms/docs/creating-keys#create_a_key), but _before_ you click the **Create** button:

  1. For **Key rotation period** , select an option.

  2. For **Starting on** , select the date when you want the first automatic rotation to happen. You can leave **Starting on** at its default value to start the first automatic rotation one key rotation period from when you create the key.




### gcloud

To use Cloud KMS on the command line, first [Install or upgrade to the latest version of Google Cloud CLI](https://docs.cloud.google.com/sdk/install).
    
    
    gcloud kms keys create KEY_NAME \
        --keyring KEY_RING \
        --location LOCATION \
        --purpose "encryption" \
        --rotation-period ROTATION_PERIOD \
        --next-rotation-time NEXT_ROTATION_TIME
    

Replace the following:

  * `KEY_NAME`: the name of the key.
  * `KEY_RING`: the name of the key ring that contains the key.
  * `LOCATION`: the Cloud KMS location of the key ring.
  * `ROTATION_PERIOD`: the interval to rotate the key—for example, `30d` to rotate the key every 30 days. The rotation period must be at least 1 day and at most 100 years. For more information, see [CryptoKey.rotationPeriod](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey.FIELDS.rotation_period).
  * `NEXT_ROTATION_TIME`: the timestamp at which to complete the first rotation—for example, `2023-01-01T01:02:03`. You can omit `--next-rotation-time` to schedule the first rotation for one rotation period from when you run the command. For more information, see [`CryptoKey.nextRotationTime`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey.FIELDS.next_rotation_time).



For information on all flags and possible values, run the command with the `--help` flag.

### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Cloud KMS C# SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-csharp).
    
    
    using [Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using System;
    
    public class CreateKeyRotationScheduleSample
    {
        public CryptoKey CreateKeyRotationSchedule(
          string projectId = "my-project", string locationId = "us-east1", string keyRingId = "my-key-ring",
          string id = "my-key-with-rotation-schedule")
        {
            // Create the client.
            [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_Create)();
    
            // Build the parent key ring name.
            [KeyRingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyRingName.html) keyRingName = new [KeyRingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyRingName.html)(projectId, locationId, keyRingId);
    
            // Build the key.
            [CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html) key = new [CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html)
            {
                Purpose = [CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.Types.html).[CryptoKeyPurpose](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.Types.CryptoKeyPurpose.html).[EncryptDecrypt](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.Types.CryptoKeyPurpose.html#Google_Cloud_Kms_V1_CryptoKey_Types_CryptoKeyPurpose_EncryptDecrypt),
                VersionTemplate = new [CryptoKeyVersionTemplate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersionTemplate.html)
                {
                    Algorithm = [CryptoKeyVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.Types.html).[CryptoKeyVersionAlgorithm](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.Types.CryptoKeyVersionAlgorithm.html).[GoogleSymmetricEncryption](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.Types.CryptoKeyVersionAlgorithm.html#Google_Cloud_Kms_V1_CryptoKeyVersion_Types_CryptoKeyVersionAlgorithm_GoogleSymmetricEncryption),
                },
    
                // Rotate the key every 30 days.
                RotationPeriod = new [Duration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)
                {
                    Seconds = 60 * 60 * 24 * 30, // 30 days
                },
    
                // Start the first rotation in 24 hours.
                NextRotationTime = new [Timestamp](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)
                {
                    Seconds = new DateTimeOffset(DateTime.UtcNow.AddHours(24)).ToUnixTimeSeconds(),
                }
            };
    
            // Call the API.
            [CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html) result = client.[CreateCryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_CreateCryptoKey_Google_Cloud_Kms_V1_CreateCryptoKeyRequest_Google_Api_Gax_Grpc_CallSettings_)(keyRingName, id, key);
    
            // Return the result.
            return result;
        }
    }

### Go

To run this code, first [set up a Go development environment](https://docs.cloud.google.com/go/docs/setup) and [install the Cloud KMS Go SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-go).
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	kms "cloud.google.com/go/kms/apiv1"
    	"cloud.google.com/go/kms/apiv1/kmspb"
    	"google.golang.org/protobuf/types/known/durationpb"
    	"google.golang.org/protobuf/types/known/timestamppb"
    )
    
    // createKeyRotationSchedule creates a key with a rotation schedule.
    func createKeyRotationSchedule(w io.Writer, parent, id string) error {
    	// name := "projects/my-project/locations/us-east1/keyRings/my-key-ring"
    	// id := "my-key-with-rotation-schedule"
    
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
    			Purpose: kmspb.[CryptoKey_ENCRYPT_DECRYPT](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1/kmspb.html#cloud_google_com_go_kms_apiv1_kmspb_CryptoKey_CRYPTO_KEY_PURPOSE_UNSPECIFIED_CryptoKey_ENCRYPT_DECRYPT_CryptoKey_ASYMMETRIC_SIGN_CryptoKey_ASYMMETRIC_DECRYPT_CryptoKey_RAW_ENCRYPT_DECRYPT_CryptoKey_MAC_CryptoKey_KEY_ENCAPSULATION_CryptoKey_AES_WRAPPING),
    			VersionTemplate: &kmspb.CryptoKeyVersionTemplate{
    				Algorithm: kmspb.[CryptoKeyVersion_GOOGLE_SYMMETRIC_ENCRYPTION](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1/kmspb.html#cloud_google_com_go_kms_apiv1_kmspb_CryptoKeyVersion_CRYPTO_KEY_VERSION_ALGORITHM_UNSPECIFIED_CryptoKeyVersion_GOOGLE_SYMMETRIC_ENCRYPTION_CryptoKeyVersion_AES_128_GCM_CryptoKeyVersion_AES_256_GCM_CryptoKeyVersion_AES_128_CBC_CryptoKeyVersion_AES_256_CBC_CryptoKeyVersion_AES_128_CTR_CryptoKeyVersion_AES_256_CTR_CryptoKeyVersion_RSA_SIGN_PSS_2048_SHA256_CryptoKeyVersion_RSA_SIGN_PSS_3072_SHA256_CryptoKeyVersion_RSA_SIGN_PSS_4096_SHA256_CryptoKeyVersion_RSA_SIGN_PSS_4096_SHA512_CryptoKeyVersion_RSA_SIGN_PKCS1_2048_SHA256_CryptoKeyVersion_RSA_SIGN_PKCS1_3072_SHA256_CryptoKeyVersion_RSA_SIGN_PKCS1_4096_SHA256_CryptoKeyVersion_RSA_SIGN_PKCS1_4096_SHA512_CryptoKeyVersion_RSA_SIGN_RAW_PKCS1_2048_CryptoKeyVersion_RSA_SIGN_RAW_PKCS1_3072_CryptoKeyVersion_RSA_SIGN_RAW_PKCS1_4096_CryptoKeyVersion_RSA_DECRYPT_OAEP_2048_SHA256_CryptoKeyVersion_RSA_DECRYPT_OAEP_3072_SHA256_CryptoKeyVersion_RSA_DECRYPT_OAEP_4096_SHA256_CryptoKeyVersion_RSA_DECRYPT_OAEP_4096_SHA512_CryptoKeyVersion_RSA_DECRYPT_OAEP_2048_SHA1_CryptoKeyVersion_RSA_DECRYPT_OAEP_3072_SHA1_CryptoKeyVersion_RSA_DECRYPT_OAEP_4096_SHA1_CryptoKeyVersion_EC_SIGN_P256_SHA256_CryptoKeyVersion_EC_SIGN_P384_SHA384_CryptoKeyVersion_EC_SIGN_SECP256K1_SHA256_CryptoKeyVersion_EC_SIGN_ED25519_CryptoKeyVersion_HMAC_SHA256_CryptoKeyVersion_HMAC_SHA1_CryptoKeyVersion_HMAC_SHA384_CryptoKeyVersion_HMAC_SHA512_CryptoKeyVersion_HMAC_SHA224_CryptoKeyVersion_EXTERNAL_SYMMETRIC_ENCRYPTION_CryptoKeyVersion_ML_KEM_768_CryptoKeyVersion_ML_KEM_1024_CryptoKeyVersion_KEM_XWING_CryptoKeyVersion_PQ_SIGN_ML_DSA_44_CryptoKeyVersion_PQ_SIGN_ML_DSA_65_CryptoKeyVersion_PQ_SIGN_ML_DSA_87_CryptoKeyVersion_PQ_SIGN_SLH_DSA_SHA2_128S_CryptoKeyVersion_PQ_SIGN_HASH_SLH_DSA_SHA2_128S_SHA256_CryptoKeyVersion_PQ_SIGN_ML_DSA_44_EXTERNAL_MU_CryptoKeyVersion_PQ_SIGN_ML_DSA_65_EXTERNAL_MU_CryptoKeyVersion_PQ_SIGN_ML_DSA_87_EXTERNAL_MU_CryptoKeyVersion_AES_256_KWP),
    			},
    
    			// Rotate the key every 30 days
    			RotationSchedule: &kmspb.CryptoKey_RotationPeriod{
    				RotationPeriod: &durationpb.Duration{
    					Seconds: int64(60 * 60 * 24 * 30), // 30 days
    				},
    			},
    
    			// Start the first rotation in 24 hours
    			NextRotationTime: &timestamppb.Timestamp{
    				Seconds: time.Now().Add(24 * time.Hour).Unix(),
    			},
    		},
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

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Cloud KMS Java SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-java).
    
    
    import com.google.cloud.kms.v1.[CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html);
    import com.google.cloud.kms.v1.[CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html).[CryptoKeyPurpose](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.html);
    import com.google.cloud.kms.v1.[CryptoKeyVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html).[CryptoKeyVersionAlgorithm](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionAlgorithm.html);
    import com.google.cloud.kms.v1.[CryptoKeyVersionTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionTemplate.html);
    import com.google.cloud.kms.v1.[KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html);
    import com.google.cloud.kms.v1.[KeyRingName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRingName.html);
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import com.google.protobuf.[Timestamp](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html);
    import java.io.IOException;
    import java.time.temporal.ChronoUnit;
    
    public class CreateKeyRotationSchedule {
    
      public void createKeyRotationSchedule() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "us-east1";
        String keyRingId = "my-key-ring";
        String id = "my-key";
        createKeyRotationSchedule(projectId, locationId, keyRingId, id);
      }
    
      // Create a new key that automatically rotates on a schedule.
      public void createKeyRotationSchedule(
          String projectId, String locationId, String keyRingId, String id) throws IOException {
        // Initialize client that will be used to send requests. This client only
        // needs to be created once, and can be reused for multiple requests. After
        // completing all of your requests, call the "close" method on the client to
        // safely clean up any remaining background resources.
        try ([KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html).create()) {
          // Build the parent name from the project, location, and key ring.
          [KeyRingName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRingName.html) keyRingName = [KeyRingName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRingName.html).of(projectId, locationId, keyRingId);
    
          // Calculate the date 24 hours from now (this is used below).
          long tomorrow = java.time.Instant.now().plus(24, ChronoUnit.HOURS).getEpochSecond();
    
          // Build the key to create with a rotation schedule.
          [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html) key =
              [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html).newBuilder()
                  .[setPurpose](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.Builder.html#com_google_cloud_kms_v1_CryptoKey_Builder_setPurpose_com_google_cloud_kms_v1_CryptoKey_CryptoKeyPurpose_)([CryptoKeyPurpose](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.html).ENCRYPT_DECRYPT)
                  .[setVersionTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.Builder.html#com_google_cloud_kms_v1_CryptoKey_Builder_setVersionTemplate_com_google_cloud_kms_v1_CryptoKeyVersionTemplate_)(
                      [CryptoKeyVersionTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionTemplate.html).newBuilder()
                          .setAlgorithm([CryptoKeyVersionAlgorithm](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionAlgorithm.html).GOOGLE_SYMMETRIC_ENCRYPTION))
    
                  // Rotate every 30 days.
                  .[setRotationPeriod](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.Builder.html#com_google_cloud_kms_v1_CryptoKey_Builder_setRotationPeriod_com_google_protobuf_Duration_)(
                      [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(java.time.Duration.ofDays(30).getSeconds()))
    
                  // Start the first rotation in 24 hours.
                  .[setNextRotationTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.Builder.html#com_google_cloud_kms_v1_CryptoKey_Builder_setNextRotationTime_com_google_protobuf_Timestamp_)([Timestamp](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html).newBuilder().setSeconds(tomorrow))
                  .build();
    
          // Create the key.
          [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html) createdKey = client.createCryptoKey(keyRingName, id, key);
          System.out.printf("Created key with rotation schedule %s%n", createdKey.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html#com_google_cloud_kms_v1_CryptoKey_getName__)());
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
    // const id = 'my-rotating-encryption-key';
    
    // Imports the Cloud KMS library
    const {KeyManagementServiceClient} = require('[@google-cloud/kms](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)');
    
    // Instantiates a client
    const client = new [KeyManagementServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)();
    
    // Build the parent key ring name
    const keyRingName = client.keyRingPath(projectId, locationId, keyRingId);
    
    async function createKeyRotationSchedule() {
      const [key] = await client.createCryptoKey({
        parent: keyRingName,
        cryptoKeyId: id,
        cryptoKey: {
          purpose: 'ENCRYPT_DECRYPT',
          versionTemplate: {
            algorithm: 'GOOGLE_SYMMETRIC_ENCRYPTION',
          },
    
          // Rotate the key every 30 days.
          rotationPeriod: {
            seconds: 60 * 60 * 24 * 30,
          },
    
          // Start the first rotation in 24 hours.
          nextRotationTime: {
            seconds: new Date().getTime() / 1000 + 60 * 60 * 24,
          },
        },
      });
    
      console.log(`Created rotating key: ${key.name}`);
      return key;
    }
    
    return createKeyRotationSchedule();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Cloud KMS PHP SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-php).
    
    
    use Google\Cloud\Kms\V1\Client\KeyManagementServiceClient;
    use Google\Cloud\Kms\V1\CreateCryptoKeyRequest;
    use Google\Cloud\Kms\V1\CryptoKey;
    use Google\Cloud\Kms\V1\CryptoKey\CryptoKeyPurpose;
    use Google\Cloud\Kms\V1\CryptoKeyVersion\CryptoKeyVersionAlgorithm;
    use Google\Cloud\Kms\V1\CryptoKeyVersionTemplate;
    use Google\Protobuf\Duration;
    use Google\Protobuf\Timestamp;
    
    function create_key_rotation_schedule(
        string $projectId = 'my-project',
        string $locationId = 'us-east1',
        string $keyRingId = 'my-key-ring',
        string $id = 'my-key-with-rotation-schedule'
    ): CryptoKey {
        // Create the Cloud KMS client.
        $client = new KeyManagementServiceClient();
    
        // Build the parent key ring name.
        $keyRingName = $client->keyRingName($projectId, $locationId, $keyRingId);
    
        // Build the key.
        $key = (new CryptoKey())
            ->setPurpose(CryptoKeyPurpose::ENCRYPT_DECRYPT)
            ->setVersionTemplate((new CryptoKeyVersionTemplate())
                ->setAlgorithm(CryptoKeyVersionAlgorithm::GOOGLE_SYMMETRIC_ENCRYPTION))
    
            // Rotate the key every 30 days.
            ->setRotationPeriod((new Duration())
                ->setSeconds(60 * 60 * 24 * 30)
            )
    
            // Start the first rotation in 24 hours.
            ->setNextRotationTime((new Timestamp())
                ->setSeconds(time() + 60 * 60 * 24)
            );
    
        // Call the API.
        $createCryptoKeyRequest = (new CreateCryptoKeyRequest())
            ->setParent($keyRingName)
            ->setCryptoKeyId($id)
            ->setCryptoKey($key);
        $createdKey = $client->createCryptoKey($createCryptoKeyRequest);
        printf('Created key with rotation: %s' . PHP_EOL, $createdKey->getName());
    
        return $createdKey;
    }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Cloud KMS Python SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-python).
    
    
    import time
    
    from google.cloud import kms
    
    
    def create_key_rotation_schedule(
        project_id: str, location_id: str, key_ring_id: str, key_id: str
    ) -> kms.CryptoKey:
        """
        Creates a new key in Cloud KMS that automatically rotates.
    
        Args:
            project_id (string): Google Cloud project ID (e.g. 'my-project').
            location_id (string): Cloud KMS location (e.g. 'us-east1').
            key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring').
            key_id (string): ID of the key to create (e.g. 'my-rotating-key').
    
        Returns:
            CryptoKey: Cloud KMS key.
    
        """
    
        # Create the client.
        client = kms.[KeyManagementServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html)()
    
        # Build the parent key ring name.
        key_ring_name = client.[key_ring_path](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_key_ring_path)(project_id, location_id, key_ring_id)
    
        # Build the key.
        purpose = kms.[CryptoKey](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKey.html).[CryptoKeyPurpose](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKey.CryptoKeyPurpose.html).ENCRYPT_DECRYPT
        algorithm = (
            kms.[CryptoKeyVersion](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKeyVersion.html).[CryptoKeyVersionAlgorithm](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKeyVersion.CryptoKeyVersionAlgorithm.html).GOOGLE_SYMMETRIC_ENCRYPTION
        )
        key = {
            "purpose": purpose,
            "version_template": {
                "algorithm": algorithm,
            },
            # Rotate the key every 30 days.
            "rotation_period": {"seconds": 60 * 60 * 24 * 30},
            # Start the first rotation in 24 hours.
            "next_rotation_time": {"seconds": int(time.time()) + 60 * 60 * 24},
        }
    
        # Call the API.
        created_key = client.[create_crypto_key](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_create_crypto_key)(
            request={"parent": key_ring_name, "crypto_key_id": key_id, "crypto_key": key}
        )
        print(f"Created labeled key: {created_key.name}")
        return created_key
    
    

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Cloud KMS Ruby SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-ruby).
    
    
    # TODO(developer): uncomment these values before running the sample.
    # project_id  = "my-project"
    # location_id = "us-east1"
    # key_ring_id = "my-key-ring"
    # id          = "my-key-with-rotation"
    
    # Require the library.
    require "google/cloud/kms"
    
    # Create the client.
    client = Google::Cloud::[Kms](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms.html).[key_management_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms/latest/Google-Cloud-Kms.html)
    
    # Build the parent key ring name.
    key_ring_name = client.[key_ring_path](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-KeyManagementService-Paths.html) project: project_id, location: location_id, key_ring: key_ring_id
    
    # Build the key.
    key = {
      purpose:            :ENCRYPT_DECRYPT,
      version_template:   {
        algorithm: :GOOGLE_SYMMETRIC_ENCRYPTION
      },
    
      # Rotate the key every 30 days.
      rotation_period:    {
        seconds: 60 * 60 * 24 * 30
      },
    
      # Start the first rotation in 24 hours.
      next_rotation_time: {
        seconds: (Time.now + (60 * 60 * 24)).to_i
      }
    }
    
    # Call the API.
    created_key = client.create_crypto_key parent: key_ring_name, crypto_key_id: id, crypto_key: key
    puts "Created rotating key: #{created_key.name}"

### API

These examples use [curl](https://curl.haxx.se/) as an HTTP client to demonstrate using the API. For more information about access control, see [Accessing the Cloud KMS API](https://docs.cloud.google.com/kms/docs/accessing-the-api). 

To create a key, use the [`CryptoKey.create`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/create) method:
    
    
    curl "https://cloudkms.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys?crypto_key_id=KEY_NAME" \
        --request "POST" \
        --header "authorization: Bearer TOKEN" \
        --header "content-type: application/json" \
        --data '{
                "purpose": "PURPOSE", "rotationPeriod": "ROTATION_PERIOD",
                "nextRotationTime": "NEXT_ROTATION_TIME"
                }'
    

Replace the following:

  * `PURPOSE`: the [purpose](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKeyPurpose) of the key.
  * `ROTATION_PERIOD`: the interval to rotate the key—for example, `30d` to rotate the key every 30 days. The rotation period must be at least 1 day and at most 100 years. For more information, see [CryptoKey.rotationPeriod](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey.FIELDS.rotation_period).
  * `NEXT_ROTATION_TIME`: the timestamp at which to complete the first rotation—for example, `2023-01-01T01:02:03`. For more information, see [`CryptoKey.nextRotationTime`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey.FIELDS.next_rotation_time). 



### Update an existing key to add a rotation schedule

To configure automatic rotation on an existing key:

### Console

  1. In the Google Cloud console, go to the **Key Management** page.

[Go to Key Management](https://console.cloud.google.com/security/kms)

  2. Click the name of the key ring that contains the key for which you want to add a rotation schedule.

  3. Click the key you want to add a rotation schedule to.

  4. In the header, click **Edit Rotation Period**.

  5. In the prompt, choose new values for the **Rotation period** and **Starting on** fields.

  6. In the prompt, click **Save**.




### gcloud

To use Cloud KMS on the command line, first [Install or upgrade to the latest version of Google Cloud CLI](https://docs.cloud.google.com/sdk/install).
    
    
    gcloud kms keys update KEY_NAME \
        --location LOCATION \
        --keyring KEY_RING \
        --rotation-period ROTATION_PERIOD \
        --next-rotation-time NEXT_ROTATION_TIME
    

Replace the following:

  * `KEY_NAME`: the name of the key.
  * `KEY_RING`: the name of the key ring that contains the key.
  * `LOCATION`: the Cloud KMS location of the key ring.
  * `ROTATION_PERIOD`: the interval to rotate the key—for example, `30d` to rotate the key every 30 days. The rotation period must be at least 1 day and at most 100 years. For more information, see [CryptoKey.rotationPeriod](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey.FIELDS.rotation_period).
  * `NEXT_ROTATION_TIME`: the timestamp at which to complete the next rotation—for example, `2023-01-01T01:02:03`. You can omit `--next-rotation-time` to schedule the next rotation for one rotation period from when you run the command. For more information, see [`CryptoKey.nextRotationTime`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey.FIELDS.next_rotation_time).



For information on all flags and possible values, run the command with the `--help` flag.

### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Cloud KMS C# SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-csharp).
    
    
    using [Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using System;
    
    public class UpdateKeyAddRotationSample
    {
        public CryptoKey UpdateKeyAddRotation(string projectId = "my-project", string locationId = "us-east1", string keyRingId = "my-key-ring", string keyId = "my-key")
        {
            // Create the client.
            [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_Create)();
    
            // Build the key.
            [CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html) key = new [CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html)
            {
                // Provide the name of the key to update.
                CryptoKeyName = new [CryptoKeyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyName.html)(projectId, locationId, keyRingId, keyId),
    
                // Rotate the key every 30 days.
                RotationPeriod = new [Duration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)
                {
                    Seconds = 60 * 60 * 24 * 30, // 30 days
                },
    
                // Start the first rotation in 24 hours.
                NextRotationTime = new [Timestamp](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)
                {
                    Seconds = new DateTimeOffset(DateTime.UtcNow.AddHours(24)).ToUnixTimeSeconds(),
                }
            };
    
            // Build the update mask.
            [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html) fieldMask = new [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)
            {
                Paths = { "rotation_period", "next_rotation_time" },
            };
    
            // Call the API.
            [CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html) result = client.[UpdateCryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_UpdateCryptoKey_Google_Cloud_Kms_V1_CryptoKey_Google_Protobuf_WellKnownTypes_FieldMask_Google_Api_Gax_Grpc_CallSettings_)(key, fieldMask);
    
            // Return the updated key.
            return result;
        }
    }

### Go

To run this code, first [set up a Go development environment](https://docs.cloud.google.com/go/docs/setup) and [install the Cloud KMS Go SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-go).
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	kms "cloud.google.com/go/kms/apiv1"
    	"cloud.google.com/go/kms/apiv1/kmspb"
    	fieldmask "google.golang.org/genproto/protobuf/field_mask"
    	"google.golang.org/protobuf/types/known/durationpb"
    	"google.golang.org/protobuf/types/known/timestamppb"
    )
    
    // addRotationSchedule updates a key to add a rotation schedule. If the key
    // already has a rotation schedule, it is overwritten.
    func addRotationSchedule(w io.Writer, name string) error {
    	// name := "projects/my-project/locations/us-east1/keyRings/my-key-ring/cryptoKeys/my-key"
    
    	// Create the client.
    	ctx := context.Background()
    	client, err := kms.[NewKeyManagementClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_NewKeyManagementClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create kms client: %w", err)
    	}
    	defer client.Close()
    
    	// Build the request.
    	req := &kmspb.UpdateCryptoKeyRequest{
    		CryptoKey: &kmspb.CryptoKey{
    			// Provide the name of the key to update
    			Name: name,
    
    			// Rotate the key every 30 days
    			RotationSchedule: &kmspb.CryptoKey_RotationPeriod{
    				RotationPeriod: &durationpb.Duration{
    					Seconds: int64(60 * 60 * 24 * 30), // 30 days
    				},
    			},
    
    			// Start the first rotation in 24 hours
    			NextRotationTime: &timestamppb.Timestamp{
    				Seconds: time.Now().Add(24 * time.Hour).Unix(),
    			},
    		},
    		UpdateMask: &fieldmask.FieldMask{
    			Paths: []string{"rotation_period", "next_rotation_time"},
    		},
    	}
    
    	// Call the API.
    	result, err := client.UpdateCryptoKey(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to update key: %w", err)
    	}
    	fmt.Fprintf(w, "Updated key: %s\n", result.Name)
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Cloud KMS Java SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-java).
    
    
    import com.google.cloud.kms.v1.[CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html);
    import com.google.cloud.kms.v1.[CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html).[CryptoKeyPurpose](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.html);
    import com.google.cloud.kms.v1.[CryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html);
    import com.google.cloud.kms.v1.[CryptoKeyVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html).[CryptoKeyVersionAlgorithm](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionAlgorithm.html);
    import com.google.cloud.kms.v1.[CryptoKeyVersionTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionTemplate.html);
    import com.google.cloud.kms.v1.[KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html);
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import com.google.protobuf.[Timestamp](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html);
    import com.google.protobuf.util.[FieldMaskUtil](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.FieldMaskUtil.html);
    import java.io.IOException;
    import java.time.temporal.ChronoUnit;
    
    public class UpdateKeyAddRotation {
    
      public void updateKeyAddRotation() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "us-east1";
        String keyRingId = "my-key-ring";
        String keyId = "my-key";
        updateKeyAddRotation(projectId, locationId, keyRingId, keyId);
      }
    
      // Update a key to add or change a rotation schedule.
      public void updateKeyAddRotation(
          String projectId, String locationId, String keyRingId, String keyId) throws IOException {
        // Initialize client that will be used to send requests. This client only
        // needs to be created once, and can be reused for multiple requests. After
        // completing all of your requests, call the "close" method on the client to
        // safely clean up any remaining background resources.
        try ([KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html).create()) {
          // Build the name from the project, location, and key ring.
          [CryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html) cryptoKeyName = [CryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html).of(projectId, locationId, keyRingId, keyId);
    
          // Calculate the date 24 hours from now (this is used below).
          long tomorrow = java.time.Instant.now().plus(24, ChronoUnit.HOURS).getEpochSecond();
    
          // Build the key to update with a rotation schedule.
          [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html) key =
              [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html).newBuilder()
                  .setName(cryptoKeyName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html#com_google_cloud_kms_v1_CryptoKeyName_toString__)())
                  .[setPurpose](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.Builder.html#com_google_cloud_kms_v1_CryptoKey_Builder_setPurpose_com_google_cloud_kms_v1_CryptoKey_CryptoKeyPurpose_)([CryptoKeyPurpose](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.html).ENCRYPT_DECRYPT)
                  .[setVersionTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.Builder.html#com_google_cloud_kms_v1_CryptoKey_Builder_setVersionTemplate_com_google_cloud_kms_v1_CryptoKeyVersionTemplate_)(
                      [CryptoKeyVersionTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionTemplate.html).newBuilder()
                          .setAlgorithm([CryptoKeyVersionAlgorithm](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionAlgorithm.html).GOOGLE_SYMMETRIC_ENCRYPTION))
    
                  // Rotate every 30 days.
                  .[setRotationPeriod](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.Builder.html#com_google_cloud_kms_v1_CryptoKey_Builder_setRotationPeriod_com_google_protobuf_Duration_)(
                      [Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(java.time.Duration.ofDays(30).getSeconds()))
    
                  // Start the first rotation in 24 hours.
                  .[setNextRotationTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.Builder.html#com_google_cloud_kms_v1_CryptoKey_Builder_setNextRotationTime_com_google_protobuf_Timestamp_)([Timestamp](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html).newBuilder().setSeconds(tomorrow))
                  .build();
    
          // Construct the field mask.
          [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) fieldMask = [FieldMaskUtil](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.FieldMaskUtil.html).fromString("rotation_period,next_rotation_time");
    
          // Update the key.
          [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html) updatedKey = client.updateCryptoKey(key, fieldMask);
          System.out.printf("Updated key %s%n", updatedKey.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html#com_google_cloud_kms_v1_CryptoKey_getName__)());
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
    // const versionId = '123';
    
    // Imports the Cloud KMS library
    const {KeyManagementServiceClient} = require('[@google-cloud/kms](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)');
    
    // Instantiates a client
    const client = new [KeyManagementServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)();
    
    // Build the key name
    const keyName = client.cryptoKeyPath(projectId, locationId, keyRingId, keyId);
    
    async function updateKeyAddRotation() {
      const [key] = await client.updateCryptoKey({
        cryptoKey: {
          name: keyName,
    
          // Rotate the key every 30 days.
          rotationPeriod: {
            seconds: 60 * 60 * 24 * 30,
          },
    
          // Start the first rotation in 24 hours.
          nextRotationTime: {
            seconds: new Date().getTime() / 1000 + 60 * 60 * 24,
          },
        },
        updateMask: {
          paths: ['rotation_period', 'next_rotation_time'],
        },
      });
    
      console.log(`Updated rotation for: ${key.name}`);
      return key;
    }
    
    return updateKeyAddRotation();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Cloud KMS PHP SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-php).
    
    
    use Google\Cloud\Kms\V1\Client\KeyManagementServiceClient;
    use Google\Cloud\Kms\V1\CryptoKey;
    use Google\Cloud\Kms\V1\UpdateCryptoKeyRequest;
    use Google\Protobuf\Duration;
    use Google\Protobuf\FieldMask;
    use Google\Protobuf\Timestamp;
    
    function update_key_add_rotation(
        string $projectId = 'my-project',
        string $locationId = 'us-east1',
        string $keyRingId = 'my-key-ring',
        string $keyId = 'my-key'
    ): CryptoKey {
        // Create the Cloud KMS client.
        $client = new KeyManagementServiceClient();
    
        // Build the key name.
        $keyName = $client->cryptoKeyName($projectId, $locationId, $keyRingId, $keyId);
    
        // Build the key.
        $key = (new CryptoKey())
            ->setName($keyName)
    
            // Rotate the key every 30 days.
            ->setRotationPeriod((new Duration())
                ->setSeconds(60 * 60 * 24 * 30)
            )
    
            // Start the first rotation in 24 hours.
            ->setNextRotationTime((new Timestamp())
                ->setSeconds(time() + 60 * 60 * 24)
            );
    
        // Create the field mask.
        $updateMask = (new FieldMask())
            ->setPaths(['rotation_period', 'next_rotation_time']);
    
        // Call the API.
        $updateCryptoKeyRequest = (new UpdateCryptoKeyRequest())
            ->setCryptoKey($key)
            ->setUpdateMask($updateMask);
        $updatedKey = $client->updateCryptoKey($updateCryptoKeyRequest);
        printf('Updated key: %s' . PHP_EOL, $updatedKey->getName());
    
        return $updatedKey;
    }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Cloud KMS Python SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-python).
    
    
    import time
    
    from google.cloud import kms
    
    
    def update_key_add_rotation(
        project_id: str, location_id: str, key_ring_id: str, key_id: str
    ) -> kms.CryptoKey:
        """
        Add a rotation schedule to an existing key.
    
        Args:
            project_id (string): Google Cloud project ID (e.g. 'my-project').
            location_id (string): Cloud KMS location (e.g. 'us-east1').
            key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring').
            key_id (string): ID of the key to use (e.g. 'my-key').
    
        Returns:
            CryptoKey: Updated Cloud KMS key.
    
        """
    
        # Create the client.
        client = kms.[KeyManagementServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html)()
    
        # Build the key name.
        key_name = client.[crypto_key_path](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_crypto_key_path)(project_id, location_id, key_ring_id, key_id)
    
        key = {
            "name": key_name,
            "rotation_period": {
                "seconds": 60 * 60 * 24 * 30  # Rotate the key every 30 days.
            },
            "next_rotation_time": {
                "seconds": int(time.time())
                + 60 * 60 * 24  # Start the first rotation in 24 hours.
            },
        }
    
        # Build the update mask.
        update_mask = {"paths": ["rotation_period", "next_rotation_time"]}
    
        # Call the API.
        updated_key = client.[update_crypto_key](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_update_crypto_key)(
            request={"crypto_key": key, "update_mask": update_mask}
        )
        print(f"Updated key: {updated_key.name}")
        return updated_key
    
    

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Cloud KMS Ruby SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-ruby).
    
    
    # TODO(developer): uncomment these values before running the sample.
    # project_id  = "my-project"
    # location_id = "us-east1"
    # key_ring_id = "my-key-ring"
    # key_id      = "my-key"
    
    # Require the library.
    require "google/cloud/kms"
    
    # Create the client.
    client = Google::Cloud::[Kms](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms.html).[key_management_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms/latest/Google-Cloud-Kms.html)
    
    # Build the parent key name.
    key_name = client.crypto_key_path project:    project_id,
                                      location:   location_id,
                                      key_ring:   key_ring_id,
                                      crypto_key: key_id
    
    # Build the key.
    key = {
      name:               key_name,
    
      # Rotate the key every 30 days.
      rotation_period:    {
        seconds: 60 * 60 * 24 * 30
      },
    
      # Start the first rotation in 24 hours.
      next_rotation_time: {
        seconds: (Time.now + (60 * 60 * 24)).to_i
      }
    }
    
    # Build the field mask.
    update_mask = { paths: ["rotation_period", "next_rotation_time"] }
    
    # Call the API.
    updated_key = client.update_crypto_key crypto_key: key, update_mask: update_mask
    puts "Updated key: #{updated_key.name}"

### API

These examples use [curl](https://curl.haxx.se/) as an HTTP client to demonstrate using the API. For more information about access control, see [Accessing the Cloud KMS API](https://docs.cloud.google.com/kms/docs/accessing-the-api). 

To update a key, use the [`CryptoKey.patch`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/patch) method:
    
    
    curl "https://cloudkms.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME?updateMask=rotationPeriod,nextRotationTime" \
        --request "PATCH" \
        --header "authorization: Bearer TOKEN" \
        --header "content-type: application/json" \
        --data '{"rotationPeriod": "ROTATION_PERIOD", "nextRotationTime": "NEXT_ROTATION_TIME"}'
    

Replace the following:

  * `ROTATION_PERIOD`: the interval to rotate the key—for example, `30d` to rotate the key every 30 days. The rotation period must be at least 1 day and at most 100 years. For more information, see [CryptoKey.rotationPeriod](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey.FIELDS.rotation_period).
  * `NEXT_ROTATION_TIME`: the timestamp at which to complete the next rotation—for example, `2023-01-01T01:02:03`. For more information, see [`CryptoKey.nextRotationTime`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKey.FIELDS.next_rotation_time). 



## Manually rotate a key

First, create a new key version:

### Console

  1. In the Google Cloud console, go to the **Key Management** page.

[Go to Key Management](https://console.cloud.google.com/security/kms)

  2. Click the name of the key ring that contains the key for which you will create a new key version.

  3. Click the key for which you will create a new key version.

  4. In the header, click **Rotate**.

  5. In the prompt, click **Rotate** to confirm.




### gcloud

To use Cloud KMS on the command line, first [Install or upgrade to the latest version of Google Cloud CLI](https://docs.cloud.google.com/sdk/install).
    
    
    gcloud kms keys versions create \
        --key KEY_NAME \
        --keyring KEY_RING \
        --location LOCATION
    

Replace the following:

  * `KEY_NAME`: the name of the key.
  * `KEY_RING`: the name of the key ring that contains the key.
  * `LOCATION`: the Cloud KMS location of the key ring.



Key versions are numbered sequentially.

For information on all flags and possible values, run the command with the `--help` flag.

### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Cloud KMS C# SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-csharp).
    
    
    using [Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.html);
    
    public class CreateKeyVersionSample
    {
        public CryptoKeyVersion CreateKeyVersion(string projectId = "my-project", string locationId = "us-east1", string keyRingId = "my-key-ring", string keyId = "my-key")
        {
            // Create the client.
            [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_Create)();
    
            // Build the parent key name.
            [CryptoKeyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyName.html) keyName = new [CryptoKeyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyName.html)(projectId, locationId, keyRingId, keyId);
    
            // Build the key version.
            [CryptoKeyVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.html) keyVersion = new [CryptoKeyVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.html) { };
    
            // Call the API.
            [CryptoKeyVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.html) result = client.[CreateCryptoKeyVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_CreateCryptoKeyVersion_Google_Cloud_Kms_V1_CreateCryptoKeyVersionRequest_Google_Api_Gax_Grpc_CallSettings_)(keyName, keyVersion);
    
            // Return the result.
            return result;
        }
    }

### Go

To run this code, first [set up a Go development environment](https://docs.cloud.google.com/go/docs/setup) and [install the Cloud KMS Go SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-go).
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	kms "cloud.google.com/go/kms/apiv1"
    	"cloud.google.com/go/kms/apiv1/kmspb"
    )
    
    // createKeyVersion creates a new key version for the given key.
    func createKeyVersion(w io.Writer, parent string) error {
    	// parent := "projects/my-project/locations/us-east1/keyRings/my-key-ring/cryptoKeys/my-key"
    
    	// Create the client.
    	ctx := context.Background()
    	client, err := kms.[NewKeyManagementClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_NewKeyManagementClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create kms client: %w", err)
    	}
    	defer client.Close()
    
    	// Build the request.
    	req := &kmspb.CreateCryptoKeyVersionRequest{
    		Parent: parent,
    	}
    
    	// Call the API.
    	result, err := client.CreateCryptoKeyVersion(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to create key version: %w", err)
    	}
    	fmt.Fprintf(w, "Created key version: %s\n", result.Name)
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Cloud KMS Java SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-java).
    
    
    import com.google.cloud.kms.v1.[CryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html);
    import com.google.cloud.kms.v1.[CryptoKeyVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html);
    import com.google.cloud.kms.v1.[KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html);
    import java.io.IOException;
    
    public class CreateKeyVersion {
    
      public void createKeyVersion() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "us-east1";
        String keyRingId = "my-key-ring";
        String keyId = "my-key";
        createKeyVersion(projectId, locationId, keyRingId, keyId);
      }
    
      // Create a new key version.
      public void createKeyVersion(String projectId, String locationId, String keyRingId, String keyId)
          throws IOException {
        // Initialize client that will be used to send requests. This client only
        // needs to be created once, and can be reused for multiple requests. After
        // completing all of your requests, call the "close" method on the client to
        // safely clean up any remaining background resources.
        try ([KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html).create()) {
          // Build the parent name from the project, location, and key ring.
          [CryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html) cryptoKeyName = [CryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html).of(projectId, locationId, keyRingId, keyId);
    
          // Build the key version to create.
          [CryptoKeyVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html) keyVersion = [CryptoKeyVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html).newBuilder().build();
    
          // Create the key.
          [CryptoKeyVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html) createdVersion = client.createCryptoKeyVersion(cryptoKeyName, keyVersion);
          System.out.printf("Created key version %s%n", createdVersion.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html#com_google_cloud_kms_v1_CryptoKeyVersion_getName__)());
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
    
    // Imports the Cloud KMS library
    const {KeyManagementServiceClient} = require('[@google-cloud/kms](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)');
    
    // Instantiates a client
    const client = new [KeyManagementServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)();
    
    // Build the parent key name
    const keyName = client.cryptoKeyPath(projectId, locationId, keyRingId, keyId);
    
    async function createKeyVersion() {
      const [version] = await client.createCryptoKeyVersion({
        parent: keyName,
      });
    
      console.log(`Created key version: ${version.name}`);
      return version;
    }
    
    return createKeyVersion();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Cloud KMS PHP SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-php).
    
    
    use Google\Cloud\Kms\V1\Client\KeyManagementServiceClient;
    use Google\Cloud\Kms\V1\CreateCryptoKeyVersionRequest;
    use Google\Cloud\Kms\V1\CryptoKeyVersion;
    
    function create_key_version(
        string $projectId = 'my-project',
        string $locationId = 'us-east1',
        string $keyRingId = 'my-key-ring',
        string $keyId = 'my-key'
    ): CryptoKeyVersion {
        // Create the Cloud KMS client.
        $client = new KeyManagementServiceClient();
    
        // Build the parent key name.
        $keyName = $client->cryptoKeyName($projectId, $locationId, $keyRingId, $keyId);
    
        // Build the key version.
        $version = new CryptoKeyVersion();
    
        // Call the API.
        $createCryptoKeyVersionRequest = (new CreateCryptoKeyVersionRequest())
            ->setParent($keyName)
            ->setCryptoKeyVersion($version);
        $createdVersion = $client->createCryptoKeyVersion($createCryptoKeyVersionRequest);
        printf('Created key version: %s' . PHP_EOL, $createdVersion->getName());
    
        return $createdVersion;
    }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Cloud KMS Python SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-python).
    
    
    from google.cloud import kms
    
    
    def create_key_version(
        project_id: str, location_id: str, key_ring_id: str, key_id: str
    ) -> kms.CryptoKey:
        """
        Creates a new version of the given key.
    
        Args:
            project_id (string): Google Cloud project ID (e.g. 'my-project').
            location_id (string): Cloud KMS location (e.g. 'us-east1').
            key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring').
            key_id (string): ID of the key for which to create a new version (e.g. 'my-key').
    
        Returns:
            CryptoKeyVersion: Cloud KMS key version.
    
        """
    
        # Create the client.
        client = kms.[KeyManagementServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html)()
    
        # Build the parent key name.
        key_name = client.[crypto_key_path](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_crypto_key_path)(project_id, location_id, key_ring_id, key_id)
    
        # Build the key version.
        version = {}
    
        # Call the API.
        created_version = client.[create_crypto_key_version](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_create_crypto_key_version)(
            request={"parent": key_name, "crypto_key_version": version}
        )
        print(f"Created key version: {created_version.name}")
        return created_version
    
    

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Cloud KMS Ruby SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-ruby).
    
    
    # TODO(developer): uncomment these values before running the sample.
    # project_id  = "my-project"
    # location_id = "us-east1"
    # key_ring_id = "my-key-ring"
    # key_id      = "my-key"
    
    # Require the library.
    require "google/cloud/kms"
    
    # Create the client.
    client = Google::Cloud::[Kms](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms.html).[key_management_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms/latest/Google-Cloud-Kms.html)
    
    # Build the parent key name.
    key_name = client.crypto_key_path project:    project_id,
                                      location:   location_id,
                                      key_ring:   key_ring_id,
                                      crypto_key: key_id
    
    # Build the version.
    version = {}
    
    # Call the API.
    created_version = client.create_crypto_key_version parent: key_name, crypto_key_version: version
    puts "Created key version: #{created_version.name}"

### API

These examples use [curl](https://curl.haxx.se/) as an HTTP client to demonstrate using the API. For more information about access control, see [Accessing the Cloud KMS API](https://docs.cloud.google.com/kms/docs/accessing-the-api). 

To manually rotate a key, first create a new key version by calling the [CryptoKeyVersions.create](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/create) method.
    
    
    curl "https://cloudkms.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME/cryptoKeyVersions" \
        --request "POST" \
        --header "authorization: Bearer TOKEN"
    

This command creates a new key version, but doesn't set it as the primary version.

To set your new key version as primary, see [Setting an existing version as the primary key version](https://docs.cloud.google.com/kms/docs/rotate-key#set_primary).

If necessary, [re-encrypt data](https://docs.cloud.google.com/kms/docs/re-encrypt-data) that was encrypted using the previous key version.

## Set an existing version as the primary key version

To set different key version as the primary version for a key, update the key with the new primary version information. A key version must be enabled before you can configure it as the primary version.

### Console

  1. In the Google Cloud console, go to the **Key Management** page.

[Go to Key Management](https://console.cloud.google.com/security/kms)

  2. Click the name of the key ring that contains the key whose primary version you want to update.

  3. Click the key whose primary version you want to update.

  4. On the row corresponding to the key version you want to make primary, click **View More more_vert**.

  5. Click **Make primary version** in menu.

  6. In the confirmation prompt, click **Make primary**.




### gcloud

To use Cloud KMS on the command line, first [Install or upgrade to the latest version of Google Cloud CLI](https://docs.cloud.google.com/sdk/install).
    
    
    gcloud kms keys update KEY_NAME \
        --keyring KEY_RING \
        --location LOCATION \
        **--primary-version KEY_VERSION**
    

Replace the following:

  * `KEY_NAME`: the name of the key.
  * `KEY_RING`: the name of the key ring that contains the key.
  * `LOCATION`: the Cloud KMS location of the key ring.
  * KEY_VERSION: the version number of the new primary key version.



For information on all flags and possible values, run the command with the `--help` flag.

### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Cloud KMS C# SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-csharp).
    
    
    using [Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.html);
    
    public class UpdateKeySetPrimarySample
    {
        public CryptoKey UpdateKeySetPrimary(
          string projectId = "my-project", string locationId = "us-east1", string keyRingId = "my-key-ring", string keyId = "my-key",
          string keyVersionId = "123")
        {
            // Create the client.
            [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_Create)();
    
            // Build the key name.
            [CryptoKeyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyName.html) keyName = new [CryptoKeyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyName.html)(projectId, locationId, keyRingId, keyId);
    
            // Call the API.
            [CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html) result = client.[UpdateCryptoKeyPrimaryVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_UpdateCryptoKeyPrimaryVersion_Google_Cloud_Kms_V1_CryptoKeyName_System_String_Google_Api_Gax_Grpc_CallSettings_)(keyName, keyVersionId);
    
            // Return the updated key.
            return result;
        }
    }

### Go

To run this code, first [set up a Go development environment](https://docs.cloud.google.com/go/docs/setup) and [install the Cloud KMS Go SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-go).
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	kms "cloud.google.com/go/kms/apiv1"
    	"cloud.google.com/go/kms/apiv1/kmspb"
    )
    
    // updateKeySetPrimary updates the primary key version on a Cloud KMS key.
    func updateKeySetPrimary(w io.Writer, name, version string) error {
    	// name := "projects/my-project/locations/us-east1/keyRings/my-key-ring/cryptoKeys/my-key"
    	// version := "123"
    
    	// Create the client.
    	ctx := context.Background()
    	client, err := kms.[NewKeyManagementClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_NewKeyManagementClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create kms client: %w", err)
    	}
    	defer client.Close()
    
    	// Build the request.
    	req := &kmspb.UpdateCryptoKeyPrimaryVersionRequest{
    		Name:               name,
    		CryptoKeyVersionId: version,
    	}
    
    	// Call the API.
    	result, err := client.UpdateCryptoKeyPrimaryVersion(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to update key: %w", err)
    	}
    	fmt.Fprintf(w, "Updated key primary: %s\n", result.Name)
    
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Cloud KMS Java SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-java).
    
    
    import com.google.cloud.kms.v1.[CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html);
    import com.google.cloud.kms.v1.[CryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html);
    import com.google.cloud.kms.v1.[KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html);
    import java.io.IOException;
    
    public class UpdateKeySetPrimary {
    
      public void updateKeySetPrimary() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "us-east1";
        String keyRingId = "my-key-ring";
        String keyId = "my-key";
        String keyVersionId = "123";
        updateKeySetPrimary(projectId, locationId, keyRingId, keyId, keyVersionId);
      }
    
      // Update a key's primary version.
      public void updateKeySetPrimary(
          String projectId, String locationId, String keyRingId, String keyId, String keyVersionId)
          throws IOException {
        // Initialize client that will be used to send requests. This client only
        // needs to be created once, and can be reused for multiple requests. After
        // completing all of your requests, call the "close" method on the client to
        // safely clean up any remaining background resources.
        try ([KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html).create()) {
          // Build the name from the project, location, key ring, and keyId.
          [CryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html) cryptoKeyName = [CryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html).of(projectId, locationId, keyRingId, keyId);
    
          // Create the key.
          [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html) createdKey = client.updateCryptoKeyPrimaryVersion(cryptoKeyName, keyVersionId);
          System.out.printf("Updated key primary version %s%n", createdKey.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html#com_google_cloud_kms_v1_CryptoKey_getName__)());
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
    // const versionId = '123';
    
    // Imports the Cloud KMS library
    const {KeyManagementServiceClient} = require('[@google-cloud/kms](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)');
    
    // Instantiates a client
    const client = new [KeyManagementServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)();
    
    // Build the key name
    const keyName = client.cryptoKeyPath(projectId, locationId, keyRingId, keyId);
    
    async function updateKeySetPrimary() {
      const [key] = await client.updateCryptoKeyPrimaryVersion({
        name: keyName,
        cryptoKeyVersionId: versionId,
      });
    
      console.log(`Set primary to ${versionId}`);
      return key;
    }
    
    return updateKeySetPrimary();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Cloud KMS PHP SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-php).
    
    
    use Google\Cloud\Kms\V1\Client\KeyManagementServiceClient;
    use Google\Cloud\Kms\V1\UpdateCryptoKeyPrimaryVersionRequest;
    
    function update_key_set_primary(
        string $projectId = 'my-project',
        string $locationId = 'us-east1',
        string $keyRingId = 'my-key-ring',
        string $keyId = 'my-key',
        string $versionId = '123'
    ) {
        // Create the Cloud KMS client.
        $client = new KeyManagementServiceClient();
    
        // Build the key name.
        $keyName = $client->cryptoKeyName($projectId, $locationId, $keyRingId, $keyId);
    
        // Call the API.
        $updateCryptoKeyPrimaryVersionRequest = (new UpdateCryptoKeyPrimaryVersionRequest())
            ->setName($keyName)
            ->setCryptoKeyVersionId($versionId);
        $updatedKey = $client->updateCryptoKeyPrimaryVersion($updateCryptoKeyPrimaryVersionRequest);
        printf('Updated primary %s to %s' . PHP_EOL, $updatedKey->getName(), $versionId);
    
        return $updatedKey;
    }

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Cloud KMS Ruby SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-ruby).
    
    
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
    
    # Build the parent key name.
    key_name = client.crypto_key_path project:    project_id,
                                      location:   location_id,
                                      key_ring:   key_ring_id,
                                      crypto_key: key_id
    
    # Call the API.
    updated_key = client.update_crypto_key_primary_version name: key_name, crypto_key_version_id: version_id
    puts "Updated primary #{updated_key.name} to #{version_id}"

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Cloud KMS Python SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-python).
    
    
    from google.cloud import kms
    
    
    def update_key_set_primary(
        project_id: str, location_id: str, key_ring_id: str, key_id: str, version_id: str
    ) -> kms.CryptoKey:
        """
        Update the primary version of a key.
    
        Args:
            project_id (string): Google Cloud project ID (e.g. 'my-project').
            location_id (string): Cloud KMS location (e.g. 'us-east1').
            key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring').
            key_id (string): ID of the key to use (e.g. 'my-key').
            version_id (string): ID of the key to make primary (e.g. '2').
    
        Returns:
            CryptoKey: Updated Cloud KMS key.
    
        """
    
        # Create the client.
        client = kms.[KeyManagementServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html)()
    
        # Build the key name.
        key_name = client.[crypto_key_path](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_crypto_key_path)(project_id, location_id, key_ring_id, key_id)
    
        # Call the API.
        updated_key = client.[update_crypto_key_primary_version](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_update_crypto_key_primary_version)(
            request={"name": key_name, "crypto_key_version_id": version_id}
        )
        print(f"Updated {updated_key.name} primary to {version_id}")
        return updated_key
    
    

### API

These examples use [curl](https://curl.haxx.se/) as an HTTP client to demonstrate using the API. For more information about access control, see [Accessing the Cloud KMS API](https://docs.cloud.google.com/kms/docs/accessing-the-api). 

Change the primary key version by calling the [CryptoKey.updatePrimaryVersion](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/updatePrimaryVersion) method.
    
    
    curl "https://cloudkms.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME:updatePrimaryVersion" \
        --request "POST" \
        --header "authorization: Bearer TOKEN" \
        --header "content-type: application/json" \
        --data '{"cryptoKeyVersionId": "KEY_VERSION"}'
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the key ring.
  * `LOCATION`: the Cloud KMS location of the key ring.
  * `KEY_RING`: the name of the key ring that contains the key.
  * `KEY_NAME`: the name of the key.
  * KEY_VERSION: the version number of the new primary key version. 



When you change the primary key version, the change typically becomes consistent within 1 minute. However, this change can take up to 3 hours to propagate in exceptional cases. During this time, the prior primary version might be used to encrypt data. For more information, see [Cloud KMS resource consistency](https://docs.cloud.google.com/kms/docs/consistency).

## Disable automatic rotation

To disable automatic rotation on a key, clear the rotation schedule of the key:

### Console

  1. In the Google Cloud console, go to the **Key Management** page.

[Go to Key Management](https://console.cloud.google.com/security/kms)

  2. Click the name of the key ring that contains the key for which you want to remove the rotation schedule.

  3. Click the key you want to remove the rotation schedule from.

  4. In the header, click **Edit Rotation Period**.

  5. In the prompt, click the **Rotation period** field and select **Never (manual rotation)**.

  6. In the prompt, click **Save**.




### gcloud

To use Cloud KMS on the command line, first [Install or upgrade to the latest version of Google Cloud CLI](https://docs.cloud.google.com/sdk/install).
    
    
    gcloud kms keys update KEY_NAME \
        --keyring KEY_RING \
        --location LOCATION \
        **--remove-rotation-schedule**
    

Replace the following:

  * `KEY_NAME`: the name of the key.
  * `KEY_RING`: the name of the key ring that contains the key.
  * `LOCATION`: the Cloud KMS location of the key ring.



For information on all flags and possible values, run the command with the `--help` flag.

### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Cloud KMS C# SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-csharp).
    
    
    using [Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    
    public class UpdateKeyRemoveRotationSample
    {
        public CryptoKey UpdateKeyRemoveRotation(string projectId = "my-project", string locationId = "us-east1", string keyRingId = "my-key-ring", string keyId = "my-key")
        {
            // Create the client.
            [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_Create)();
    
            // Build the key.
            [CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html) key = new [CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html)
            {
                CryptoKeyName = new [CryptoKeyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyName.html)(projectId, locationId, keyRingId, keyId),
                RotationPeriod = null,
                NextRotationTime = null,
            };
    
            // Build the update mask.
            [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html) fieldMask = new [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)
            {
                Paths = { "rotation_period", "next_rotation_time" },
            };
    
            // Call the API.
            [CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.html) result = client.[UpdateCryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_UpdateCryptoKey_Google_Cloud_Kms_V1_CryptoKey_Google_Protobuf_WellKnownTypes_FieldMask_Google_Api_Gax_Grpc_CallSettings_)(key, fieldMask);
    
            // Return the updated key.
            return result;
        }
    }

### Go

To run this code, first [set up a Go development environment](https://docs.cloud.google.com/go/docs/setup) and [install the Cloud KMS Go SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-go).
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	kms "cloud.google.com/go/kms/apiv1"
    	"cloud.google.com/go/kms/apiv1/kmspb"
    	fieldmask "google.golang.org/genproto/protobuf/field_mask"
    )
    
    // removeRotationSchedule updates a key to remove a rotation schedule, if one
    // exists.
    func removeRotationSchedule(w io.Writer, name string) error {
    	// name := "projects/my-project/locations/us-east1/keyRings/my-key-ring/cryptoKeys/my-key"
    
    	// Create the client.
    	ctx := context.Background()
    	client, err := kms.[NewKeyManagementClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_NewKeyManagementClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create kms client: %w", err)
    	}
    	defer client.Close()
    
    	// Build the request.
    	req := &kmspb.UpdateCryptoKeyRequest{
    		CryptoKey: &kmspb.CryptoKey{
    			// Provide the name of the key to update
    			Name: name,
    
    			// Remove any rotation fields.
    			RotationSchedule: nil,
    			NextRotationTime: nil,
    		},
    		UpdateMask: &fieldmask.FieldMask{
    			Paths: []string{"rotation_period", "next_rotation_time"},
    		},
    	}
    
    	// Call the API.
    	result, err := client.UpdateCryptoKey(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to update key: %w", err)
    	}
    	fmt.Fprintf(w, "Updated key: %s\n", result.Name)
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Cloud KMS Java SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-java).
    
    
    import com.google.cloud.kms.v1.[CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html);
    import com.google.cloud.kms.v1.[CryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html);
    import com.google.cloud.kms.v1.[KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import com.google.protobuf.util.[FieldMaskUtil](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.FieldMaskUtil.html);
    import java.io.IOException;
    
    public class UpdateKeyRemoveRotation {
    
      public void updateKeyRemoveRotation() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "us-east1";
        String keyRingId = "my-key-ring";
        String keyId = "my-key";
        updateKeyRemoveRotation(projectId, locationId, keyRingId, keyId);
      }
    
      // Update a key to remove all labels.
      public void updateKeyRemoveRotation(
          String projectId, String locationId, String keyRingId, String keyId) throws IOException {
        // Initialize client that will be used to send requests. This client only
        // needs to be created once, and can be reused for multiple requests. After
        // completing all of your requests, call the "close" method on the client to
        // safely clean up any remaining background resources.
        try ([KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html).create()) {
          // Build the name from the project, location, key ring, and keyId.
          [CryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html) cryptoKeyName = [CryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html).of(projectId, locationId, keyRingId, keyId);
    
          // Build an empty key with no labels.
          [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html) key =
              [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html).newBuilder()
                  .setName(cryptoKeyName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyName.html#com_google_cloud_kms_v1_CryptoKeyName_toString__)())
                  .[clearRotationPeriod](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.Builder.html#com_google_cloud_kms_v1_CryptoKey_Builder_clearRotationPeriod__)()
                  .[clearNextRotationTime](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.Builder.html#com_google_cloud_kms_v1_CryptoKey_Builder_clearNextRotationTime__)()
                  .build();
    
          // Construct the field mask.
          [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) fieldMask = [FieldMaskUtil](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.FieldMaskUtil.html).fromString("rotation_period,next_rotation_time");
    
          // Create the key.
          [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html) createdKey = client.updateCryptoKey(key, fieldMask);
          System.out.printf("Updated key %s%n", createdKey.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html#com_google_cloud_kms_v1_CryptoKey_getName__)());
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
    
    // Imports the Cloud KMS library
    const {KeyManagementServiceClient} = require('[@google-cloud/kms](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)');
    
    // Instantiates a client
    const client = new [KeyManagementServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)();
    
    // Build the key name
    const keyName = client.cryptoKeyPath(projectId, locationId, keyRingId, keyId);
    
    async function updateKeyRemoveRotation() {
      const [key] = await client.updateCryptoKey({
        cryptoKey: {
          name: keyName,
          rotationPeriod: null,
          nextRotationTime: null,
        },
        updateMask: {
          paths: ['rotation_period', 'next_rotation_time'],
        },
      });
    
      console.log(`Removed rotation for: ${key.name}`);
      return key;
    }
    
    return updateKeyRemoveRotation();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Cloud KMS PHP SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-php).
    
    
    use Google\Cloud\Kms\V1\Client\KeyManagementServiceClient;
    use Google\Cloud\Kms\V1\CryptoKey;
    use Google\Cloud\Kms\V1\UpdateCryptoKeyRequest;
    use Google\Protobuf\FieldMask;
    
    function update_key_remove_rotation(
        string $projectId = 'my-project',
        string $locationId = 'us-east1',
        string $keyRingId = 'my-key-ring',
        string $keyId = 'my-key'
    ): CryptoKey {
        // Create the Cloud KMS client.
        $client = new KeyManagementServiceClient();
    
        // Build the key name.
        $keyName = $client->cryptoKeyName($projectId, $locationId, $keyRingId, $keyId);
    
        // Build the key.
        $key = (new CryptoKey())
            ->setName($keyName);
    
        // Create the field mask.
        $updateMask = (new FieldMask())
            ->setPaths(['rotation_period', 'next_rotation_time']);
    
        // Call the API.
        $updateCryptoKeyRequest = (new UpdateCryptoKeyRequest())
            ->setCryptoKey($key)
            ->setUpdateMask($updateMask);
        $updatedKey = $client->updateCryptoKey($updateCryptoKeyRequest);
        printf('Updated key: %s' . PHP_EOL, $updatedKey->getName());
    
        return $updatedKey;
    }

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Cloud KMS Ruby SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-ruby).
    
    
    # TODO(developer): uncomment these values before running the sample.
    # project_id  = "my-project"
    # location_id = "us-east1"
    # key_ring_id = "my-key-ring"
    # key_id      = "my-key"
    
    # Require the library.
    require "google/cloud/kms"
    
    # Create the client.
    client = Google::Cloud::[Kms](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms.html).[key_management_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms/latest/Google-Cloud-Kms.html)
    
    # Build the parent key name.
    key_name = client.crypto_key_path project:    project_id,
                                      location:   location_id,
                                      key_ring:   key_ring_id,
                                      crypto_key: key_id
    
    # Build the key.
    key = {
      name:               key_name,
      rotation_period:    nil,
      next_rotation_time: nil
    }
    
    # Build the field mask.
    update_mask = { paths: ["rotation_period", "next_rotation_time"] }
    
    # Call the API.
    updated_key = client.update_crypto_key crypto_key: key, update_mask: update_mask
    puts "Updated key: #{updated_key.name}"

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Cloud KMS Python SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-python).
    
    
    from google.cloud import kms
    
    
    def update_key_remove_rotation(
        project_id: str, location_id: str, key_ring_id: str, key_id: str
    ) -> kms.CryptoKey:
        """
        Remove a rotation schedule from an existing key.
    
        Args:
            project_id (string): Google Cloud project ID (e.g. 'my-project').
            location_id (string): Cloud KMS location (e.g. 'us-east1').
            key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring').
            key_id (string): ID of the key to use (e.g. 'my-key').
    
        Returns:
            CryptoKey: Updated Cloud KMS key.
    
        """
    
        # Create the client.
        client = kms.[KeyManagementServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html)()
    
        # Build the key name.
        key_name = client.[crypto_key_path](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_crypto_key_path)(project_id, location_id, key_ring_id, key_id)
    
        key = {"name": key_name}
    
        # Build the update mask.
        update_mask = {"paths": ["rotation_period", "next_rotation_time"]}
    
        # Call the API.
        updated_key = client.[update_crypto_key](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_update_crypto_key)(
            request={"crypto_key": key, "update_mask": update_mask}
        )
        print(f"Updated key: {updated_key.name}")
        return updated_key
    
    

### API

These examples use [curl](https://curl.haxx.se/) as an HTTP client to demonstrate using the API. For more information about access control, see [Accessing the Cloud KMS API](https://docs.cloud.google.com/kms/docs/accessing-the-api). 

To update a key, use the [`CryptoKey.patch`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/patch) method:
    
    
    curl "https://cloudkms.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME?updateMask=rotationPeriod,nextRotationTime" \
        --request "PATCH" \
        --header "authorization: Bearer TOKEN" \
        --header "content-type: application/json" \
        --data '{"rotationPeriod": null, "nextRotationTime": null}'
    

For additional details about `rotationPeriod` and `nextRotationTime`, see [`keyRings.cryptoKeys`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys). 

## Rotate an external key

### Rotate a coordinated external key

You can configure automatic rotation for symmetric coordinated external keys. You can also manually create a new key version for symmetric or asymmetric coordinated external keys.

Rotating or creating a new key version causes all newly created data protected with that key to be encrypted with the new key version. Data protected with a previous key version isn't re-encrypted. As a result, your external key manager must continue to make the key material of the previous key version available to be used.

To create a new key version for a coordinated external key, complete the following steps:

### Console

  1. In the Google Cloud console, go to the **Key Management** page.

[Go to Key Management](https://console.cloud.google.com/security/kms)

  2. Select the key ring, and then select the key.

  3. Click **Create version**. A message indicates that your new key version will be generated in both Cloud KMS and your EKM. If you see a **Key path** or **Key URI** field, the selected key isn't a coordinated external key.

  4. To confirm that you want to create a new key version, click **Create version**.




The new key version appears in **Pending generation** state. For symmetric keys, manually created key versions aren't automatically set as the primary key version. You can [set your new key version as primary](https://docs.cloud.google.com/kms/docs/rotate-key#set_primary). 

### gcloud

To use Cloud KMS on the command line, first [Install or upgrade to the latest version of Google Cloud CLI](https://docs.cloud.google.com/sdk/install).

To create a new symmetric key version and set it as the primary key version, use the `kms keys versions create` command with the `--primary` flag:
    
    
    gcloud kms keys versions create \
      --key KEY_NAME \
      --keyring KEY_RING \
      --location LOCATION \
      --primary
    

Replace the following:

  * `KEY_NAME`: the name of the key.
  * `KEY_RING`: the name of the key ring that contains the key.
  * `LOCATION`: the Cloud KMS location of the key ring.



To create a new asymmetric key version or to create a new symmetric key version that isn't the primary key version, use the `kms keys versions create` command:
    
    
    gcloud kms keys versions create \
      --key KEY_NAME \
      --keyring KEY_RING \
      --location LOCATION
    

Replace the following:

  * `KEY_NAME`: the name of the key.
  * `KEY_RING`: the name of the key ring that contains the key.
  * `LOCATION`: the Cloud KMS location of the key ring.



### Rotate a manually managed Cloud EKM over VPC key

First, rotate the external key material on your external key manager. If that results in a new key path, you need to rotate or create a new Cloud EKM key version with the new key path. For symmetric encryption keys, _rotate_ the Cloud EKM key and specify the new key path from your external key manager. For asymmetric keys, _create a new key version_ and specify the new key path.

Rotating or creating a new key version causes all newly created data protected with that key to be encrypted with the new key version. Data protected with a previous key version isn't re-encrypted. As a result, your external key manager must continue to make the key material of the previous key version available to be used.

If the key material in the external key management partner system doesn't change, but the key path changes, you can [update the key's external path](https://docs.cloud.google.com/kms/docs/update-external-key-path) without rotating the key.

### Console

  1. In the Google Cloud console, go to the **Key Management** page.

[Go to Key Management](https://console.cloud.google.com/security/kms)

  2. Select the key ring, and then select the key.

  3. Click **Rotate key**.

  4. For **Key path** , enter the key path for the new version.

  5. Click **Rotate Key** to confirm.




### gcloud

To use Cloud KMS on the command line, first [Install or upgrade to the latest version of Google Cloud CLI](https://docs.cloud.google.com/sdk/install).

To create a new symmetric key version and set it as the primary key version, use the `kms keys versions create` command with the `--primary` flag:
    
    
    gcloud kms keys versions create \
        --key KEY_NAME \
        --keyring KEY_RING \
        --location LOCATION \
        --ekm-connection-key-path EXTERNAL_KEY_PATH \
        --primary
    

Replace the following:

  * `KEY_NAME`: the name of the key.
  * `KEY_RING`: the name of the key ring that contains the key.
  * `LOCATION`: the Cloud KMS location of the key ring.
  * `EXTERNAL_KEY_PATH`: the path to the new external key version.



To create a new asymmetric key version or to create a new symmetric key version that isn't the primary key version, use the `kms keys versions create` command:
    
    
    gcloud kms keys versions create \
        --key KEY_NAME \
        --keyring KEY_RING \
        --location LOCATION \
        --ekm-connection-key-path EXTERNAL_KEY_PATH
    

Replace the following:

  * `KEY_NAME`: the name of the key.
  * `KEY_RING`: the name of the key ring that contains the key.
  * `LOCATION`: the Cloud KMS location of the key ring.
  * `EXTERNAL_KEY_PATH`: the path to the new external key version.



For information on all flags and possible values, run the command with the `--help` flag.

After the key version is successfully created, you can use it just as you would use any other Cloud KMS key version.

### Rotate a manually managed Cloud EKM over the internet key

First, rotate the external key material on your external key manager. If that results in a new URI, you need to rotate or create a new Cloud EKM key version with the new URI. For symmetric encryption keys, _rotate_ the Cloud EKM key and specify the new key URI from your external key manager. For asymmetric keys, _create a new key version_ and specify the new key URI.

Rotating or creating a new key version causes all newly created data protected with that key to be encrypted with the new key version. Data protected with a previous key version isn't re-encrypted. As a result, your external key manager must continue to make the key material of the previous key version available to be used.

If the key material in the external key management partner system doesn't change, but the URI changes, you can [update the key's external URI](https://docs.cloud.google.com/kms/docs/update-external-key-path) without rotating the key.

### Console

  1. In the Google Cloud console, go to the **Key Management** page.

[Go to Key Management](https://console.cloud.google.com/security/kms)

  2. Select the key ring, and then select the key.

  3. Select **Rotate key** for symmetric keys or **Create version** for asymmetric keys.

  4. Enter the new key URI, then select **Rotate Key** for symmetric keys or **Create version** for asymmetric keys.




The new key version becomes the primary version.

### gcloud

To use Cloud KMS on the command line, first [Install or upgrade to the latest version of Google Cloud CLI](https://docs.cloud.google.com/sdk/install).

To create a new symmetric key version and set it as the primary key version, use the `kms keys versions create` command with the `--primary` flag:
    
    
    gcloud kms keys versions create \
      --key KEY_NAME \
      --keyring KEY_RING \
      --location LOCATION \
      --external-key-uri EXTERNAL_KEY_URI \
      --primary
    

Replace the following:

  * `KEY_NAME`: the name of the key.
  * `KEY_RING`: the name of the key ring that contains the key.
  * `LOCATION`: the Cloud KMS location of the key ring.
  * `EXTERNAL_KEY_URI`: the key URI of the new external key version.



To create a new asymmetric key version or to create a new symmetric key version that isn't the primary key version, use the `kms keys versions create` command:
    
    
    gcloud kms keys versions create \
      --key KEY_NAME \
      --keyring KEY_RING \
      --location LOCATION \
      --external-key-uri EXTERNAL_KEY_URI
    

Replace the following:

  * `KEY_NAME`: the name of the key.
  * `KEY_RING`: the name of the key ring that contains the key.
  * `LOCATION`: the Cloud KMS location of the key ring.
  * `EXTERNAL_KEY_URI`: the key URI of the new external key version.



## What's next

  * After rotating a key, you can [re-encrypt data](https://docs.cloud.google.com/kms/docs/re-encrypt-data) that was encrypted with that key.
  * After you re-encrypt your data, you can [check whether the key version is in use](https://docs.cloud.google.com/kms/docs/destroy-restore#pre-destroy-checklist).
  * After you have confirmed that a key version is no longer in use, you can [destroy a key version](https://docs.cloud.google.com/kms/docs/destroy-restore#destroy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
