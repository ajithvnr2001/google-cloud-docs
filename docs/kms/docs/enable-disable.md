---
url: https://docs.cloud.google.com/kms/docs/enable-disable/
title: Enable and disable key versions \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:41.118653+00:00
---

# Enable and disable key versions  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/enable-disable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Enable and disable key versions Stay organized with collections  Save and categorize content based on your preferences. 

In Cloud KMS, the cryptographic key material that you use to encrypt, decrypt, sign, and verify data is stored in a key version. A key has zero or more key versions. When you rotate a key, you create a new key version.

This document shows how to disable a key version. During the time that a key is disabled, data that was encrypted with the key can't be accessed. To access the data, you can re-enable the key version.

Unless otherwise specified in the [Service Health dashboard](https://status.cloud.google.com/), disabling a key version is typically [consistent](https://docs.cloud.google.com/kms/docs/consistency) within one minute. Enabling a key version is nearly instant. You can also manage access to a key version using Identity and Access Management (IAM). IAM operations are consistent within seconds. For more information, see [Using IAM](https://docs.cloud.google.com/kms/docs/iam).

**Caution:** Disabling a key version that is required to start a container or instance can result in service outages. It is the customer's responsibility to ensure that a key version is safe to disable. Google is not responsible for outages, loss of data, or compliance issues which result from a customer disabling a key version.

You can also permanently [destroy a key version](https://docs.cloud.google.com/kms/docs/destroy-restore). Depending on your organization policies, you might need to disable a key version before you can destroy it. For more information see [Control key version destruction](https://docs.cloud.google.com/kms/docs/control-key-destruction).

**Note:** Key rings can't be deleted. You can [delete keys and key versions](https://docs.cloud.google.com/kms/docs/delete-kms-resources) in some circumstances, but names of deleted keys can't be reused. This ensures that the [resource identifier](https://docs.cloud.google.com/kms/docs/getting-resource-ids) of a key version is unique and always points to the original key material for that key version unless it has been destroyed. You can store an unlimited number of key rings, enabled or disabled keys, and enabled, disabled, or destroyed key versions. For more information, see [Pricing](https://docs.cloud.google.com/kms/pricing) and [Quotas](https://docs.cloud.google.com/kms/quotas). 

## Disable a key version

You can disable a key version in the enabled [state](https://docs.cloud.google.com/kms/docs/key-states). Before disabling a key version, we recommend that you check whether the key is still in use. You can [view key usage tracking details](https://docs.cloud.google.com/kms/docs/view-key-usage) for the key to see whether it is protecting CMEK resources. If any resources are protected by the key version that you want to disable, re-encrypt them with another key version before disabling the key.

**Caution:** Key usage tracking details can be delayed or incomplete. Familiarize yourself with the [limitations](https://docs.cloud.google.com/kms/docs/view-key-usage#limitations) of this data.

### Console

  1. In the Google Cloud console, go to the **Key Management** page.

[Go to Key Management](https://console.cloud.google.com/security/kms)

  2. Click the name of the key ring that contains the key whose key version you will disable.

  3. Click the key whose key version you want to disable.

  4. Check the box next to the key version(s) that you want to disable.

  5. Click **Disable** in the header.

  6. In the confirmation prompt, click **Disable**.




### gcloud

To use Cloud KMS on the command line, first [Install or upgrade to the latest version of Google Cloud CLI](https://docs.cloud.google.com/sdk/install).
    
    
    gcloud kms keys versions disable key-version \
        --key key \
        --keyring key-ring \
        --location location
    

Replace key-version with the version of the key to disable. Replace key with the name of the key. Replace key-ring with the name of the key ring where the key is located. Replace location with the Cloud KMS location for the key ring.

For information on all flags and possible values, run the command with the `--help` flag.

### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Cloud KMS C# SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-csharp).
    
    
    using [Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    
    public class DisableKeyVersionSample
    {
        public CryptoKeyVersion DisableKeyVersion(string projectId = "my-project", string locationId = "us-east1", string keyRingId = "my-key-ring", string keyId = "my-key", string keyVersionId = "123")
        {
            // Create the client.
            [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_Create)();
    
            // Build the key version.
            [CryptoKeyVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.html) keyVersion = new [CryptoKeyVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.html)
            {
                CryptoKeyVersionName = new [CryptoKeyVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersionName.html)(projectId, locationId, keyRingId, keyId, keyVersionId),
                State = [CryptoKeyVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.Types.html).[CryptoKeyVersionState](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.Types.CryptoKeyVersionState.html).[Disabled](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.Types.CryptoKeyVersionState.html#Google_Cloud_Kms_V1_CryptoKeyVersion_Types_CryptoKeyVersionState_Disabled),
            };
    
            // Build the update mask.
            [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html) fieldMask = new [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)
            {
                Paths = { "state" },
            };
    
            // Call the API.
            [CryptoKeyVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.html) result = client.[UpdateCryptoKeyVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_UpdateCryptoKeyVersion_Google_Cloud_Kms_V1_CryptoKeyVersion_Google_Protobuf_WellKnownTypes_FieldMask_Google_Api_Gax_Grpc_CallSettings_)(keyVersion, fieldMask);
    
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
    	fieldmask "google.golang.org/genproto/protobuf/field_mask"
    )
    
    // disableKeyVersion disables the specified key version on Cloud KMS.
    func disableKeyVersion(w io.Writer, name string) error {
    	// name := "projects/my-project/locations/us-east1/keyRings/my-key-ring/cryptoKeys/my-key/cryptoKeyVersions/123"
    
    	// Create the client.
    	ctx := context.Background()
    	client, err := kms.[NewKeyManagementClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_NewKeyManagementClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create kms client: %w", err)
    	}
    	defer client.Close()
    
    	// Build the request.
    	req := &kmspb.UpdateCryptoKeyVersionRequest{
    		CryptoKeyVersion: &kmspb.CryptoKeyVersion{
    			Name:  name,
    			State: kmspb.[CryptoKeyVersion_DISABLED](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1/kmspb.html#cloud_google_com_go_kms_apiv1_kmspb_CryptoKeyVersion_CRYPTO_KEY_VERSION_STATE_UNSPECIFIED_CryptoKeyVersion_PENDING_GENERATION_CryptoKeyVersion_ENABLED_CryptoKeyVersion_DISABLED_CryptoKeyVersion_DESTROYED_CryptoKeyVersion_DESTROY_SCHEDULED_CryptoKeyVersion_PENDING_IMPORT_CryptoKeyVersion_IMPORT_FAILED_CryptoKeyVersion_GENERATION_FAILED_CryptoKeyVersion_PENDING_EXTERNAL_DESTRUCTION_CryptoKeyVersion_EXTERNAL_DESTRUCTION_FAILED),
    		},
    		UpdateMask: &fieldmask.FieldMask{
    			Paths: []string{"state"},
    		},
    	}
    
    	// Call the API.
    	result, err := client.UpdateCryptoKeyVersion(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to update key version: %w", err)
    	}
    	fmt.Fprintf(w, "Disabled key version: %s\n", result)
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Cloud KMS Java SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-java).
    
    
    import com.google.cloud.kms.v1.[CryptoKeyVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html);
    import com.google.cloud.kms.v1.[CryptoKeyVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html).[CryptoKeyVersionState](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.html);
    import com.google.cloud.kms.v1.[CryptoKeyVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionName.html);
    import com.google.cloud.kms.v1.[KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import com.google.protobuf.util.[FieldMaskUtil](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.FieldMaskUtil.html);
    import java.io.IOException;
    
    public class DisableKeyVersion {
    
      public void disableKeyVersion() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "us-east1";
        String keyRingId = "my-key-ring";
        String keyId = "my-key";
        String keyVersionId = "123";
        disableKeyVersion(projectId, locationId, keyRingId, keyId, keyVersionId);
      }
    
      // Disable a key version from use.
      public void disableKeyVersion(
          String projectId, String locationId, String keyRingId, String keyId, String keyVersionId)
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
    
          // Build the updated key version, setting it to disbaled.
          [CryptoKeyVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html) keyVersion =
              [CryptoKeyVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html).newBuilder()
                  .setName(keyVersionName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionName.html#com_google_cloud_kms_v1_CryptoKeyVersionName_toString__)())
                  .setState([CryptoKeyVersionState](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.html).DISABLED)
                  .build();
    
          // Create a field mask of updated values.
          [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) fieldMask = [FieldMaskUtil](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.FieldMaskUtil.html).fromString("state");
    
          // Disable the key version.
          [CryptoKeyVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html) response = client.updateCryptoKeyVersion(keyVersion, fieldMask);
          System.out.printf("Disabled key version: %s%n", response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html#com_google_cloud_kms_v1_CryptoKeyVersion_getName__)());
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
    
    // Build the key version name
    const versionName = client.cryptoKeyVersionPath(
      projectId,
      locationId,
      keyRingId,
      keyId,
      versionId
    );
    
    async function disableKeyVersion() {
      const [version] = await client.updateCryptoKeyVersion({
        cryptoKeyVersion: {
          name: versionName,
          state: 'DISABLED',
        },
        updateMask: {
          paths: ['state'],
        },
      });
    
      console.log(`Disabled key version: ${version.name}`);
      return version;
    }
    
    return disableKeyVersion();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Cloud KMS PHP SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-php).
    
    
    use Google\Cloud\Kms\V1\Client\KeyManagementServiceClient;
    use Google\Cloud\Kms\V1\CryptoKeyVersion;
    use Google\Cloud\Kms\V1\CryptoKeyVersion\CryptoKeyVersionState;
    use Google\Cloud\Kms\V1\UpdateCryptoKeyVersionRequest;
    use Google\Protobuf\FieldMask;
    
    function disable_key_version(
        string $projectId = 'my-project',
        string $locationId = 'us-east1',
        string $keyRingId = 'my-key-ring',
        string $keyId = 'my-key',
        string $versionId = '123'
    ): CryptoKeyVersion {
        // Create the Cloud KMS client.
        $client = new KeyManagementServiceClient();
    
        // Build the key version name.
        $keyVersionName = $client->cryptoKeyVersionName($projectId, $locationId, $keyRingId, $keyId, $versionId);
    
        // Create the updated version.
        $keyVersion = (new CryptoKeyVersion())
            ->setName($keyVersionName)
            ->setState(CryptoKeyVersionState::DISABLED);
    
        // Create the field mask.
        $updateMask = (new FieldMask())
            ->setPaths(['state']);
    
        // Call the API.
        $updateCryptoKeyVersionRequest = (new UpdateCryptoKeyVersionRequest())
            ->setCryptoKeyVersion($keyVersion)
            ->setUpdateMask($updateMask);
        $disabledVersion = $client->updateCryptoKeyVersion($updateCryptoKeyVersionRequest);
        printf('Disabled key version: %s' . PHP_EOL, $disabledVersion->getName());
    
        return $disabledVersion;
    }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Cloud KMS Python SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-python).
    
    
    from google.cloud import kms
    
    
    def disable_key_version(
        project_id: str, location_id: str, key_ring_id: str, key_id: str, version_id: str
    ) -> kms.CryptoKeyVersion:
        """
        Disable a key.
    
        Args:
            project_id (string): Google Cloud project ID (e.g. 'my-project').
            location_id (string): Cloud KMS location (e.g. 'us-east1').
            key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring').
            key_id (string): ID of the key to use (e.g. 'my-key').
            version_id (string): ID of the key version to disable (e.g. '1').
    
        Returns:
            CryptoKeyVersion: The version.
    
        """
    
        # Create the client.
        client = kms.[KeyManagementServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html)()
    
        # Build the key version name.
        key_version_name = client.[crypto_key_version_path](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_crypto_key_version_path)(
            project_id, location_id, key_ring_id, key_id, version_id
        )
    
        key_version = {
            "name": key_version_name,
            "state": kms.[CryptoKeyVersion](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKeyVersion.html).[CryptoKeyVersionState](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKeyVersion.CryptoKeyVersionState.html).DISABLED,
        }
    
        # Build the update mask.
        update_mask = {"paths": ["state"]}
    
        # Call the API.
        disabled_version = client.[update_crypto_key_version](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_update_crypto_key_version)(
            request={"crypto_key_version": key_version, "update_mask": update_mask}
        )
        print(f"Disabled key version: {disabled_version.name}")
        return disabled_version
    
    

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
    
    # Build the key version name.
    key_version_name = client.[crypto_key_version_path](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-KeyManagementService-Paths.html) project:            project_id,
                                                      location:           location_id,
                                                      key_ring:           key_ring_id,
                                                      crypto_key:         key_id,
                                                      crypto_key_version: version_id
    
    # Create the updated version.
    version = {
      name:  key_version_name,
      state: :DISABLED
    }
    
    # Create the field mask.
    update_mask = { paths: ["state"] }
    
    # Call the API.
    disabled_version = client.update_crypto_key_version crypto_key_version: version, update_mask: update_mask
    puts "Disabled key version: #{disabled_version.name}"

After you submit the request, the state of the key version changes to disabled.

Disabled key versions are billed resources.

### Disable or destroy an external key

To temporarily disable the association between a Cloud EKM key and an external key, you can [disable](https://docs.cloud.google.com/kms/docs/enable-disable) the Cloud EKM key or key version. Disabling all key versions is recommended. Disabling a key takes effect within three hours.

When you disable a key, you should also [revoke access to the key](https://docs.cloud.google.com/kms/docs/iam). IAM operations are consistent within seconds. Also consider revoking the Google Cloud service account's access in the external key management partner system.

To **permanently** remove the association between a Cloud EKM key and an external key, you can [schedule the Cloud EKM key version for destruction](https://docs.cloud.google.com/kms/docs/destroy-restore). After the scheduled-for-destruction period, the key is destroyed. Destroying a key version is permanent. After the key version is destroyed, you can no longer encrypt data or decrypt data that was encrypted with the Cloud EKM key version. You cannot recreate a Cloud EKM key version that has been destroyed, even if you use the same external key URI or key path. When destroying external key material, we recommend first destroying the key or key version in Google Cloud and then, only after the Cloud EKM key is destroyed, destroying the key material in the external key manager.

Disabling a key or key version in Cloud KMS doesn't modify the key in the external key management partner system.

Destroying a _manually managed key_ version in Cloud KMS doesn't modify the key in the external key management partner system. Destroying a _coordinated external key_ version in Cloud KMS destroys the internal key material and sends a request to the external key management partner system to destroy the external key material.

## Enable a key version

You can enable a key version in the disabled [state](https://docs.cloud.google.com/kms/docs/key-states).

### Console

  1. In the Google Cloud console, go to the **Key Management** page.

[Go to Key Management](https://console.cloud.google.com/security/kms)

  2. Click the name of the key ring that contains the key whose key version you will enable.

  3. Click the key whose key version you want to enable.

  4. Check the box next to the key version(s) that you want to enable.

  5. Click **Enable** in the header.

  6. In the confirmation prompt, click **Enable**.




### gcloud

To use Cloud KMS on the command line, first [Install or upgrade to the latest version of Google Cloud CLI](https://docs.cloud.google.com/sdk/install).
    
    
    gcloud kms keys versions enable key-version \
        --key key \
        --keyring key-ring \
        --location location
    

Replace key-version with the version of the key to enable. Replace key with the key name. Replace key-ring with the name of the key ring where the key is located. Replace location with the Cloud KMS location for the key ring.

For information on all flags and possible values, run the command with the `--help` flag.

### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Cloud KMS C# SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-csharp).
    
    
    using [Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    
    public class EnableKeyVersionSample
    {
        public CryptoKeyVersion EnableKeyVersion(string projectId = "my-project", string locationId = "us-east1", string keyRingId = "my-key-ring", string keyId = "my-key", string keyVersionId = "123")
        {
            // Create the client.
            [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_Create)();
    
            // Build the key version.
            [CryptoKeyVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.html) keyVersion = new [CryptoKeyVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.html)
            {
                CryptoKeyVersionName = new [CryptoKeyVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersionName.html)(projectId, locationId, keyRingId, keyId, keyVersionId),
                State = [CryptoKeyVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.Types.html).[CryptoKeyVersionState](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.Types.CryptoKeyVersionState.html).[Enabled](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.Types.CryptoKeyVersionState.html#Google_Cloud_Kms_V1_CryptoKeyVersion_Types_CryptoKeyVersionState_Enabled),
            };
    
            // Build the update mask.
            [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html) fieldMask = new [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)
            {
                Paths = { "state" },
            };
    
            // Call the API.
            [CryptoKeyVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.html) result = client.[UpdateCryptoKeyVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_UpdateCryptoKeyVersion_Google_Cloud_Kms_V1_CryptoKeyVersion_Google_Protobuf_WellKnownTypes_FieldMask_Google_Api_Gax_Grpc_CallSettings_)(keyVersion, fieldMask);
    
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
    	fieldmask "google.golang.org/genproto/protobuf/field_mask"
    )
    
    // enableKeyVersion disables the specified key version on Cloud KMS.
    func enableKeyVersion(w io.Writer, name string) error {
    	// name := "projects/my-project/locations/us-east1/keyRings/my-key-ring/cryptoKeys/my-key/cryptoKeyVersions/123"
    
    	// Create the client.
    	ctx := context.Background()
    	client, err := kms.[NewKeyManagementClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_NewKeyManagementClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create kms client: %w", err)
    	}
    	defer client.Close()
    
    	// Build the request.
    	req := &kmspb.UpdateCryptoKeyVersionRequest{
    		CryptoKeyVersion: &kmspb.CryptoKeyVersion{
    			Name:  name,
    			State: kmspb.[CryptoKeyVersion_ENABLED](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1/kmspb.html#cloud_google_com_go_kms_apiv1_kmspb_CryptoKeyVersion_CRYPTO_KEY_VERSION_STATE_UNSPECIFIED_CryptoKeyVersion_PENDING_GENERATION_CryptoKeyVersion_ENABLED_CryptoKeyVersion_DISABLED_CryptoKeyVersion_DESTROYED_CryptoKeyVersion_DESTROY_SCHEDULED_CryptoKeyVersion_PENDING_IMPORT_CryptoKeyVersion_IMPORT_FAILED_CryptoKeyVersion_GENERATION_FAILED_CryptoKeyVersion_PENDING_EXTERNAL_DESTRUCTION_CryptoKeyVersion_EXTERNAL_DESTRUCTION_FAILED),
    		},
    		UpdateMask: &fieldmask.FieldMask{
    			Paths: []string{"state"},
    		},
    	}
    
    	// Call the API.
    	result, err := client.UpdateCryptoKeyVersion(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to update key version: %w", err)
    	}
    	fmt.Fprintf(w, "Enabled key version: %s\n", result)
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Cloud KMS Java SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-java).
    
    
    import com.google.cloud.kms.v1.[CryptoKeyVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html);
    import com.google.cloud.kms.v1.[CryptoKeyVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html).[CryptoKeyVersionState](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.html);
    import com.google.cloud.kms.v1.[CryptoKeyVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionName.html);
    import com.google.cloud.kms.v1.[KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import com.google.protobuf.util.[FieldMaskUtil](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.FieldMaskUtil.html);
    import java.io.IOException;
    
    public class EnableKeyVersion {
    
      public void enableKeyVersion() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "us-east1";
        String keyRingId = "my-key-ring";
        String keyId = "my-key";
        String keyVersionId = "123";
        enableKeyVersion(projectId, locationId, keyRingId, keyId, keyVersionId);
      }
    
      // Enable a disabled key version to be used again.
      public void enableKeyVersion(
          String projectId, String locationId, String keyRingId, String keyId, String keyVersionId)
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
    
          // Build the updated key version, setting it to enabled.
          [CryptoKeyVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html) keyVersion =
              [CryptoKeyVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html).newBuilder()
                  .setName(keyVersionName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionName.html#com_google_cloud_kms_v1_CryptoKeyVersionName_toString__)())
                  .setState([CryptoKeyVersionState](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.html).ENABLED)
                  .build();
    
          // Create a field mask of updated values.
          [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) fieldMask = [FieldMaskUtil](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.FieldMaskUtil.html).fromString("state");
    
          // Enable the key version.
          [CryptoKeyVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html) response = client.updateCryptoKeyVersion(keyVersion, fieldMask);
          System.out.printf("Enabled key version: %s%n", response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.html#com_google_cloud_kms_v1_CryptoKeyVersion_getName__)());
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
    
    // Build the key version name
    const versionName = client.cryptoKeyVersionPath(
      projectId,
      locationId,
      keyRingId,
      keyId,
      versionId
    );
    
    async function enableKeyVersion() {
      const [version] = await client.updateCryptoKeyVersion({
        cryptoKeyVersion: {
          name: versionName,
          state: 'ENABLED',
        },
        updateMask: {
          paths: ['state'],
        },
      });
    
      console.log(`Enabled key version: ${version.name}`);
      return version;
    }
    
    return enableKeyVersion();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Cloud KMS PHP SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-php).
    
    
    use Google\Cloud\Kms\V1\Client\KeyManagementServiceClient;
    use Google\Cloud\Kms\V1\CryptoKeyVersion;
    use Google\Cloud\Kms\V1\CryptoKeyVersion\CryptoKeyVersionState;
    use Google\Cloud\Kms\V1\UpdateCryptoKeyVersionRequest;
    use Google\Protobuf\FieldMask;
    
    function enable_key_version(
        string $projectId = 'my-project',
        string $locationId = 'us-east1',
        string $keyRingId = 'my-key-ring',
        string $keyId = 'my-key',
        string $versionId = '123'
    ): CryptoKeyVersion {
        // Create the Cloud KMS client.
        $client = new KeyManagementServiceClient();
    
        // Build the key version name.
        $keyVersionName = $client->cryptoKeyVersionName($projectId, $locationId, $keyRingId, $keyId, $versionId);
    
        // Create the updated version.
        $keyVersion = (new CryptoKeyVersion())
            ->setName($keyVersionName)
            ->setState(CryptoKeyVersionState::ENABLED);
    
        // Create the field mask.
        $updateMask = (new FieldMask())
            ->setPaths(['state']);
    
        // Call the API.
        $updateCryptoKeyVersionRequest = (new UpdateCryptoKeyVersionRequest())
            ->setCryptoKeyVersion($keyVersion)
            ->setUpdateMask($updateMask);
        $enabledVersion = $client->updateCryptoKeyVersion($updateCryptoKeyVersionRequest);
        printf('Enabled key version: %s' . PHP_EOL, $enabledVersion->getName());
    
        return $enabledVersion;
    }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Cloud KMS Python SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-python).
    
    
    from google.cloud import kms
    
    
    def enable_key_version(
        project_id: str, location_id: str, key_ring_id: str, key_id: str, version_id: str
    ) -> kms.CryptoKeyVersion:
        """
        Enable a key.
    
        Args:
            project_id (string): Google Cloud project ID (e.g. 'my-project').
            location_id (string): Cloud KMS location (e.g. 'us-east1').
            key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring').
            key_id (string): ID of the key to use (e.g. 'my-key').
            version_id (string): ID of the key version to enable (e.g. '1').
    
        Returns:
            CryptoKeyVersion: The version.
    
        """
        # Create the client.
        client = kms.[KeyManagementServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html)()
    
        # Build the key version name.
        key_version_name = client.[crypto_key_version_path](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_crypto_key_version_path)(
            project_id, location_id, key_ring_id, key_id, version_id
        )
    
        key_version = {
            "name": key_version_name,
            "state": kms.[CryptoKeyVersion](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKeyVersion.html).[CryptoKeyVersionState](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.CryptoKeyVersion.CryptoKeyVersionState.html).ENABLED,
        }
    
        # Build the update mask.
        update_mask = {"paths": ["state"]}
    
        # Call the API.
        enabled_version = client.[update_crypto_key_version](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_update_crypto_key_version)(
            request={"crypto_key_version": key_version, "update_mask": update_mask}
        )
        print(f"Enabled key version: {enabled_version.name}")
        return enabled_version
    
    

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
    
    # Build the key version name.
    key_version_name = client.[crypto_key_version_path](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-KeyManagementService-Paths.html) project:            project_id,
                                                      location:           location_id,
                                                      key_ring:           key_ring_id,
                                                      crypto_key:         key_id,
                                                      crypto_key_version: version_id
    
    # Create the updated version.
    version = {
      name:  key_version_name,
      state: :ENABLED
    }
    
    # Create the field mask.
    update_mask = { paths: ["state"] }
    
    # Call the API.
    enabled_version = client.update_crypto_key_version crypto_key_version: version, update_mask: update_mask
    puts "Enabled key version: #{enabled_version.name}"

After you submit the request, the state of the key version changes to enabled.

## Required IAM permissions

To enable or disable a key version, the caller needs the `cloudkms.cryptoKeyVersions.update` IAM permission on the key, the key ring, or the project, folder, or organization.

This permission is granted to the Cloud KMS Admin role (`roles/cloudkms.admin`).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
