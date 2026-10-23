---
url: https://docs.cloud.google.com/kms/docs/hsm/
title: Cloud HSM \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:23.656167+00:00
---

# Cloud HSM  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/hsm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Cloud HSM Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of Cloud HSM and shows you how to create and use HSM-protected encryption keys in Cloud Key Management Service.

## What is Cloud HSM?

Cloud HSM is a cloud-hosted Hardware Security Module (HSM) service that lets you host encryption keys and perform cryptographic operations in a cluster of [FIPS 140-2 Level 3](https://csrc.nist.gov/publications/detail/fips/140/2/final) certified HSMs. Google manages the HSM cluster for you, so you don't need to worry about clustering, scaling, or patching. Because Cloud HSM uses Cloud KMS as its front end, you can leverage all the conveniences and features that Cloud KMS provides.

**Note:** When you use HSM-backed keys and key versions for cryptographic operations, the Google Cloud project that makes the cryptographic request incurs [cryptographic operation](https://docs.cloud.google.com/kms/quotas#cryptographic_requests) quota usage, and the Google Cloud project that contains the HSM keys incurs [HSM QPM quota usage](https://docs.cloud.google.com/kms/quotas#cloud_hsm_quotas). For more information about Cloud KMS, see [Quotas](https://docs.cloud.google.com/kms/quotas).

## Create a key ring

When you create a key, you add it to a key ring in a given Google Cloud location. You can create a new key ring or use an existing one. In this topic, you create a new key ring and add a new key to it.

Create a key ring in a Google Cloud [location](https://docs.cloud.google.com/kms/docs/locations) that supports Cloud HSM.

**Note:** Key rings with the same name can exist in different [locations](https://docs.cloud.google.com/kms/docs/locations), so you must always specify the location.

### Console

  1. In the Google Cloud console, go to the **Key Management** page.

[Go to Key Management](https://console.cloud.google.com/security/kms)

  2. Click **Create key ring**.

  3. For **Key ring name** , enter a name for your key ring.

  4. For **Key ring location** , select a location like `"us-east1"`.

**Note:** Choose a location that is near the resources you want to protect. For CMEK usage, your key ring should be in the same location as the resources you use it with. For Cloud EKM keys, the location must be physically close to your external key manager (EKM) vendor.
  5. Click **Create**.




### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. In your environment, run the `gcloud kms keyrings create` command: 
         
         gcloud kms keyrings create KEY_RING \
             --location LOCATION
         

Replace the following:

     * `KEY_RING`: the name of the key ring that contains the key.
     * `LOCATION`: the Cloud KMS location of the key ring.

For information on all flags and possible values, run the command with the `--help` flag.




### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Cloud KMS C# SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-csharp).
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.html);
    
    public class CreateKeyRingSample
    {
        public KeyRing CreateKeyRing(
          string projectId = "my-project", string locationId = "us-east1",
          string id = "my-key-ring")
        {
            // Create the client.
            [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_Create)();
    
            // Build the parent location name.
            [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html) locationName = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, locationId);
    
            // Build the key ring.
            [KeyRing](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyRing.html) keyRing = new [KeyRing](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyRing.html) { };
    
            // Call the API.
            [KeyRing](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyRing.html) result = client.[CreateKeyRing](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_CreateKeyRing_Google_Api_Gax_ResourceNames_LocationName_System_String_Google_Cloud_Kms_V1_KeyRing_Google_Api_Gax_Grpc_CallSettings_)(locationName, id, keyRing);
    
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
    
    // createKeyRing creates a new ring to store keys on KMS.
    func createKeyRing(w io.Writer, parent, id string) error {
    	// parent := "projects/PROJECT_ID/locations/global"
    	// id := "my-key-ring"
    
    	// Create the client.
    	ctx := context.Background()
    	client, err := kms.[NewKeyManagementClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_NewKeyManagementClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create kms client: %w", err)
    	}
    	defer client.Close()
    
    	// Build the request.
    	req := &kmspb.CreateKeyRingRequest{
    		Parent:    parent,
    		KeyRingId: id,
    	}
    
    	// Call the API.
    	result, err := client.CreateKeyRing(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to create key ring: %w", err)
    	}
    	fmt.Fprintf(w, "Created key ring: %s\n", result.Name)
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Cloud KMS Java SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-java).
    
    
    import com.google.cloud.kms.v1.[KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html);
    import com.google.cloud.kms.v1.[KeyRing](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRing.html);
    import com.google.cloud.kms.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.LocationName.html);
    import java.io.IOException;
    
    public class CreateKeyRing {
    
      public void createKeyRing() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "us-east1";
        String id = "my-asymmetric-signing-key";
        createKeyRing(projectId, locationId, id);
      }
    
      // Create a new key ring.
      public void createKeyRing(String projectId, String locationId, String id) throws IOException {
        // Initialize client that will be used to send requests. This client only
        // needs to be created once, and can be reused for multiple requests. After
        // completing all of your requests, call the "close" method on the client to
        // safely clean up any remaining background resources.
        try ([KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html).create()) {
          // Build the parent name from the project and location.
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.LocationName.html) locationName = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.LocationName.html).of(projectId, locationId);
    
          // Build the key ring to create.
          [KeyRing](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRing.html) keyRing = [KeyRing](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRing.html).newBuilder().build();
    
          // Create the key ring.
          [KeyRing](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRing.html) createdKeyRing = client.createKeyRing(locationName, id, keyRing);
          System.out.printf("Created key ring %s%n", createdKeyRing.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRing.html#com_google_cloud_kms_v1_KeyRing_getName__)());
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
    // const id = 'my-key-ring';
    
    // Imports the Cloud KMS library
    const {KeyManagementServiceClient} = require('[@google-cloud/kms](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)');
    
    // Instantiates a client
    const client = new [KeyManagementServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)();
    
    // Build the parent location name
    const locationName = client.locationPath(projectId, locationId);
    
    async function createKeyRing() {
      const [keyRing] = await client.createKeyRing({
        parent: locationName,
        keyRingId: id,
      });
    
      console.log(`Created key ring: ${keyRing.name}`);
      return keyRing;
    }
    
    return createKeyRing();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Cloud KMS PHP SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-php).
    
    
    use Google\Cloud\Kms\V1\Client\KeyManagementServiceClient;
    use Google\Cloud\Kms\V1\CreateKeyRingRequest;
    use Google\Cloud\Kms\V1\KeyRing;
    
    function create_key_ring(
        string $projectId = 'my-project',
        string $locationId = 'us-east1',
        string $id = 'my-key-ring'
    ): KeyRing {
        // Create the Cloud KMS client.
        $client = new KeyManagementServiceClient();
    
        // Build the parent location name.
        $locationName = $client->locationName($projectId, $locationId);
    
        // Build the key ring.
        $keyRing = new KeyRing();
    
        // Call the API.
        $createKeyRingRequest = (new CreateKeyRingRequest())
            ->setParent($locationName)
            ->setKeyRingId($id)
            ->setKeyRing($keyRing);
        $createdKeyRing = $client->createKeyRing($createKeyRingRequest);
        printf('Created key ring: %s' . PHP_EOL, $createdKeyRing->getName());
    
        return $createdKeyRing;
    }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Cloud KMS Python SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-python).
    
    
    from google.cloud import kms
    
    
    def create_key_ring(
        project_id: str, location_id: str, key_ring_id: str
    ) -> kms.CryptoKey:
        """
        Creates a new key ring in Cloud KMS
    
        Args:
            project_id (string): Google Cloud project ID (e.g. 'my-project').
            location_id (string): Cloud KMS location (e.g. 'us-east1').
            key_ring_id (string): ID of the key ring to create (e.g. 'my-key-ring').
    
        Returns:
            KeyRing: Cloud KMS key ring.
    
        """
    
        # Create the client.
        client = kms.[KeyManagementServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html)()
    
        # Build the parent location name.
        location_name = f"projects/{project_id}/locations/{location_id}"
    
        # Build the key ring.
        key_ring = {}
    
        # Call the API.
        created_key_ring = client.[create_key_ring](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_create_key_ring)(
            request={
                "parent": location_name,
                "key_ring_id": key_ring_id,
                "key_ring": key_ring,
            }
        )
        print(f"Created key ring: {created_key_ring.name}")
        return created_key_ring
    
    

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Cloud KMS Ruby SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-ruby).
    
    
    # TODO(developer): uncomment these values before running the sample.
    # project_id  = "my-project"
    # location_id = "us-east1"
    # id = "my-key-ring"
    
    # Require the library.
    require "google/cloud/kms"
    
    # Create the client.
    client = Google::Cloud::[Kms](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms.html).[key_management_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms/latest/Google-Cloud-Kms.html)
    
    # Build the parent location name.
    location_name = client.location_path project: project_id, location: location_id
    
    # Build the key ring.
    key_ring = {}
    
    # Call the API.
    created_key_ring = client.create_key_ring parent: location_name, key_ring_id: id, key_ring: key_ring
    puts "Created key ring: #{created_key_ring.name}"

### API

These examples use [curl](https://curl.haxx.se/) as an HTTP client to demonstrate using the API. For more information about access control, see [Accessing the Cloud KMS API](https://docs.cloud.google.com/kms/docs/accessing-the-api). 
    
    
    curl "https://cloudkms.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/keyRings?key_ring_id=KEY_RING" \
        --request "POST" \
        --header "authorization: Bearer TOKEN"
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the key ring.
  * `KEY_RING`: the name of the key ring that contains the key.
  * `LOCATION`: the Cloud KMS location of the key ring.



See the [`KeyRing.create` API documentation](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings/create) for more information.

## Create a key

Follow these steps to create a Cloud HSM key on the specified key ring and location.

### Console

  1. In the Google Cloud console, go to the **Key Management** page.

[Go to Key Management](https://console.cloud.google.com/security/kms)

  2. Click the name of the key ring for which you will create a key.

  3. Click **Create key**.

  4. In the **What type of key do you want to create?** , choose **Generated key**.

  5. In the **Key name** field, enter the name for your key.

  6. Click the **Protection level** dropdown and select **HSM** or **Single-tenant HSM**.

  7. If you selected **Single-tenant HSM** , then select the **Single-tenant HSM instance** where you want to create the key.

  8. Click the **Purpose** dropdown and select **Symmetric encrypt/decrypt**.

  9. Accept the default values for **Rotation period** and **Starting on**.

  10. Click **Create**.




### gcloud

To use Cloud KMS on the command line, first [Install or upgrade to the latest version of Google Cloud CLI](https://docs.cloud.google.com/sdk/install).

To create a Multi-tenant Cloud HSM key, run the `kms keys create` command with the `hsm` protection level.
    
    
    gcloud kms keys create KEY_NAME \
        --keyring KEY_RING \
        --location LOCATION \
        --purpose "encryption" \
        --protection-level "hsm"
    

Replace the following:

  * `KEY_NAME`: the name that you want to use for the key.
  * `KEY_RING`: the name of the key ring where you want to create the key.
  * `LOCATION`: the location of the key ring.



For information about all flags and possible values, run the command with the `--help` flag.

To create a Single-tenant Cloud HSM key, run the `kms keys create` command with the `hsm-single-tenant` protection level and specify the Single-tenant Cloud HSM instance where you want to create the key. The Single-tenant Cloud HSM instance must be in the same location as the key ring.
    
    
    gcloud kms keys create KEY_NAME \
        --keyring KEY_RING \
        --location LOCATION \
        --purpose "encryption" \
        --protection-level "hsm-single-tenant" \
        --crypto-key-backend="projects/INSTANCE_PROJECT/locations/LOCATION/singleTenantHsmInstances/INSTANCE_NAME"
    

Replace the following:

  * `KEY_NAME`: the name that you want to use for the key.
  * `KEY_RING`: the name of the key ring where you want to create the key.
  * `LOCATION`: the location of the key ring.
  * `PROTECTION_LEVEL`: the protection level of the key that you want to create.
  * `INSTANCE_PROJECT`: the identifier of the project where your Single-tenant Cloud HSM instance is located.
  * `INSTANCE_NAME`: the name of the Single-tenant Cloud HSM instance where you want to create the key. For more information about Single-tenant Cloud HSM instances, see [Create and manage a Single-tenant Cloud HSM instance](https://docs.cloud.google.com/kms/docs/create-manage-single-tenant-hsm).



### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Cloud KMS C# SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-csharp).
    
    
    using [Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    
    public class CreateKeyHsmSample
    {
        public CryptoKey CreateKeyHsm(
          string projectId = "my-project", string locationId = "us-east1", string keyRingId = "my-key-ring",
          string id = "my-hsm-encryption-key")
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
                    ProtectionLevel = [ProtectionLevel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ProtectionLevel.html).[Hsm](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ProtectionLevel.html#Google_Cloud_Kms_V1_ProtectionLevel_Hsm),
                    Algorithm = [CryptoKeyVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.Types.html).[CryptoKeyVersionAlgorithm](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.Types.CryptoKeyVersionAlgorithm.html).[GoogleSymmetricEncryption](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.Types.CryptoKeyVersionAlgorithm.html#Google_Cloud_Kms_V1_CryptoKeyVersion_Types_CryptoKeyVersionAlgorithm_GoogleSymmetricEncryption),
                },
    
                // Optional: customize how long key versions should be kept before destroying.
                DestroyScheduledDuration = new [Duration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)
                {
                    Seconds = 24 * 60 * 60,
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
    )
    
    // createKeyHSM creates a new symmetric encrypt/decrypt key on Cloud KMS.
    func createKeyHSM(w io.Writer, parent, id string) error {
    	// parent := "projects/my-project/locations/us-east1/keyRings/my-key-ring"
    	// id := "my-hsm-encryption-key"
    
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
    				ProtectionLevel: kmspb.[ProtectionLevel_HSM](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1/kmspb.html#cloud_google_com_go_kms_apiv1_kmspb_ProtectionLevel_PROTECTION_LEVEL_UNSPECIFIED_ProtectionLevel_SOFTWARE_ProtectionLevel_HSM_ProtectionLevel_EXTERNAL_ProtectionLevel_EXTERNAL_VPC_ProtectionLevel_HSM_SINGLE_TENANT),
    				Algorithm:       kmspb.[CryptoKeyVersion_GOOGLE_SYMMETRIC_ENCRYPTION](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1/kmspb.html#cloud_google_com_go_kms_apiv1_kmspb_CryptoKeyVersion_CRYPTO_KEY_VERSION_ALGORITHM_UNSPECIFIED_CryptoKeyVersion_GOOGLE_SYMMETRIC_ENCRYPTION_CryptoKeyVersion_AES_128_GCM_CryptoKeyVersion_AES_256_GCM_CryptoKeyVersion_AES_128_CBC_CryptoKeyVersion_AES_256_CBC_CryptoKeyVersion_AES_128_CTR_CryptoKeyVersion_AES_256_CTR_CryptoKeyVersion_RSA_SIGN_PSS_2048_SHA256_CryptoKeyVersion_RSA_SIGN_PSS_3072_SHA256_CryptoKeyVersion_RSA_SIGN_PSS_4096_SHA256_CryptoKeyVersion_RSA_SIGN_PSS_4096_SHA512_CryptoKeyVersion_RSA_SIGN_PKCS1_2048_SHA256_CryptoKeyVersion_RSA_SIGN_PKCS1_3072_SHA256_CryptoKeyVersion_RSA_SIGN_PKCS1_4096_SHA256_CryptoKeyVersion_RSA_SIGN_PKCS1_4096_SHA512_CryptoKeyVersion_RSA_SIGN_RAW_PKCS1_2048_CryptoKeyVersion_RSA_SIGN_RAW_PKCS1_3072_CryptoKeyVersion_RSA_SIGN_RAW_PKCS1_4096_CryptoKeyVersion_RSA_DECRYPT_OAEP_2048_SHA256_CryptoKeyVersion_RSA_DECRYPT_OAEP_3072_SHA256_CryptoKeyVersion_RSA_DECRYPT_OAEP_4096_SHA256_CryptoKeyVersion_RSA_DECRYPT_OAEP_4096_SHA512_CryptoKeyVersion_RSA_DECRYPT_OAEP_2048_SHA1_CryptoKeyVersion_RSA_DECRYPT_OAEP_3072_SHA1_CryptoKeyVersion_RSA_DECRYPT_OAEP_4096_SHA1_CryptoKeyVersion_EC_SIGN_P256_SHA256_CryptoKeyVersion_EC_SIGN_P384_SHA384_CryptoKeyVersion_EC_SIGN_SECP256K1_SHA256_CryptoKeyVersion_EC_SIGN_ED25519_CryptoKeyVersion_HMAC_SHA256_CryptoKeyVersion_HMAC_SHA1_CryptoKeyVersion_HMAC_SHA384_CryptoKeyVersion_HMAC_SHA512_CryptoKeyVersion_HMAC_SHA224_CryptoKeyVersion_EXTERNAL_SYMMETRIC_ENCRYPTION_CryptoKeyVersion_ML_KEM_768_CryptoKeyVersion_ML_KEM_1024_CryptoKeyVersion_KEM_XWING_CryptoKeyVersion_PQ_SIGN_ML_DSA_44_CryptoKeyVersion_PQ_SIGN_ML_DSA_65_CryptoKeyVersion_PQ_SIGN_ML_DSA_87_CryptoKeyVersion_PQ_SIGN_SLH_DSA_SHA2_128S_CryptoKeyVersion_PQ_SIGN_HASH_SLH_DSA_SHA2_128S_SHA256_CryptoKeyVersion_PQ_SIGN_ML_DSA_44_EXTERNAL_MU_CryptoKeyVersion_PQ_SIGN_ML_DSA_65_EXTERNAL_MU_CryptoKeyVersion_PQ_SIGN_ML_DSA_87_EXTERNAL_MU_CryptoKeyVersion_AES_256_KWP),
    			},
    
    			// Optional: customize how long key versions should be kept before destroying.
    			DestroyScheduledDuration: durationpb.New(24 * time.Hour),
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
    import com.google.cloud.kms.v1.[ProtectionLevel](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ProtectionLevel.html);
    import com.google.protobuf.[Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html);
    import java.io.IOException;
    
    public class CreateKeyHsm {
    
      public void createKeyHsm() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "us-east1";
        String keyRingId = "my-key-ring";
        String id = "my-hsm-key";
        createKeyHsm(projectId, locationId, keyRingId, id);
      }
    
      // Create a new key that is stored in an HSM.
      public void createKeyHsm(String projectId, String locationId, String keyRingId, String id)
          throws IOException {
        // Initialize client that will be used to send requests. This client only
        // needs to be created once, and can be reused for multiple requests. After
        // completing all of your requests, call the "close" method on the client to
        // safely clean up any remaining background resources.
        try ([KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html).create()) {
          // Build the parent name from the project, location, and key ring.
          [KeyRingName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRingName.html) keyRingName = [KeyRingName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyRingName.html).of(projectId, locationId, keyRingId);
    
          // Build the hsm key to create.
          [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html) key =
              [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html).newBuilder()
                  .[setPurpose](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.Builder.html#com_google_cloud_kms_v1_CryptoKey_Builder_setPurpose_com_google_cloud_kms_v1_CryptoKey_CryptoKeyPurpose_)([CryptoKeyPurpose](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.html).ENCRYPT_DECRYPT)
                  .[setVersionTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.Builder.html#com_google_cloud_kms_v1_CryptoKey_Builder_setVersionTemplate_com_google_cloud_kms_v1_CryptoKeyVersionTemplate_)(
                      [CryptoKeyVersionTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersionTemplate.html).newBuilder()
                          .setProtectionLevel([ProtectionLevel](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ProtectionLevel.html).HSM)
                          .setAlgorithm([CryptoKeyVersionAlgorithm](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionAlgorithm.html).GOOGLE_SYMMETRIC_ENCRYPTION))
    
                  // Optional: customize how long key versions should be kept before destroying.
                  .[setDestroyScheduledDuration](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.Builder.html#com_google_cloud_kms_v1_CryptoKey_Builder_setDestroyScheduledDuration_com_google_protobuf_Duration_)([Duration](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html).newBuilder().setSeconds(24 * 60 * 60))
                  .build();
    
          // Create the key.
          [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html) createdKey = client.createCryptoKey(keyRingName, id, key);
          System.out.printf("Created hsm key %s%n", createdKey.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CryptoKey.html#com_google_cloud_kms_v1_CryptoKey_getName__)());
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
    // const id = 'my-hsm-encryption-key';
    
    // Imports the Cloud KMS library
    const {KeyManagementServiceClient} = require('[@google-cloud/kms](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)');
    
    // Instantiates a client
    const client = new [KeyManagementServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)();
    
    // Build the parent key ring name
    const keyRingName = client.keyRingPath(projectId, locationId, keyRingId);
    
    async function createKeyHsm() {
      const [key] = await client.createCryptoKey({
        parent: keyRingName,
        cryptoKeyId: id,
        cryptoKey: {
          purpose: 'ENCRYPT_DECRYPT',
          versionTemplate: {
            algorithm: 'GOOGLE_SYMMETRIC_ENCRYPTION',
            protectionLevel: 'HSM',
          },
    
          // Optional: customize how long key versions should be kept before
          // destroying.
          destroyScheduledDuration: {seconds: 60 * 60 * 24},
        },
      });
    
      console.log(`Created hsm key: ${key.name}`);
      return key;
    }
    
    return createKeyHsm();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Cloud KMS PHP SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-php).
    
    
    use Google\Cloud\Kms\V1\Client\KeyManagementServiceClient;
    use Google\Cloud\Kms\V1\CreateCryptoKeyRequest;
    use Google\Cloud\Kms\V1\CryptoKey;
    use Google\Cloud\Kms\V1\CryptoKey\CryptoKeyPurpose;
    use Google\Cloud\Kms\V1\CryptoKeyVersion\CryptoKeyVersionAlgorithm;
    use Google\Cloud\Kms\V1\CryptoKeyVersionTemplate;
    use Google\Cloud\Kms\V1\ProtectionLevel;
    use Google\Protobuf\Duration;
    
    function create_key_hsm(
        string $projectId = 'my-project',
        string $locationId = 'us-east1',
        string $keyRingId = 'my-key-ring',
        string $id = 'my-hsm-key'
    ): CryptoKey {
        // Create the Cloud KMS client.
        $client = new KeyManagementServiceClient();
    
        // Build the parent key ring name.
        $keyRingName = $client->keyRingName($projectId, $locationId, $keyRingId);
    
        // Build the key.
        $key = (new CryptoKey())
            ->setPurpose(CryptoKeyPurpose::ENCRYPT_DECRYPT)
            ->setVersionTemplate((new CryptoKeyVersionTemplate())
                ->setAlgorithm(CryptoKeyVersionAlgorithm::GOOGLE_SYMMETRIC_ENCRYPTION)
                ->setProtectionLevel(ProtectionLevel::HSM)
            )
    
            // Optional: customize how long key versions should be kept before destroying.
            ->setDestroyScheduledDuration((new Duration())
                ->setSeconds(24 * 60 * 60)
            );
    
        // Call the API.
        $createCryptoKeyRequest = (new CreateCryptoKeyRequest())
            ->setParent($keyRingName)
            ->setCryptoKeyId($id)
            ->setCryptoKey($key);
        $createdKey = $client->createCryptoKey($createCryptoKeyRequest);
        printf('Created hsm key: %s' . PHP_EOL, $createdKey->getName());
    
        return $createdKey;
    }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Cloud KMS Python SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-python).
    
    
    import datetime
    
    from google.cloud import kms
    from google.protobuf import duration_pb2  # type: ignore
    
    
    def create_key_hsm(
        project_id: str, location_id: str, key_ring_id: str, key_id: str
    ) -> kms.CryptoKey:
        """
        Creates a new key in Cloud KMS backed by Cloud HSM.
    
        Args:
            project_id (string): Google Cloud project ID (e.g. 'my-project').
            location_id (string): Cloud KMS location (e.g. 'us-east1').
            key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring').
            key_id (string): ID of the key to create (e.g. 'my-hsm-key').
    
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
        protection_level = kms.[ProtectionLevel](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.ProtectionLevel.html).HSM
        key = {
            "purpose": purpose,
            "version_template": {
                "algorithm": algorithm,
                "protection_level": protection_level,
            },
            # Optional: customize how long key versions should be kept before
            # destroying.
            "destroy_scheduled_duration": duration_pb2.Duration().FromTimedelta(
                datetime.timedelta(days=1)
            ),
        }
    
        # Call the API.
        created_key = client.[create_crypto_key](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_create_crypto_key)(
            request={"parent": key_ring_name, "crypto_key_id": key_id, "crypto_key": key}
        )
        print(f"Created hsm key: {created_key.name}")
        return created_key
    
    

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Cloud KMS Ruby SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-ruby).
    
    
    # TODO(developer): uncomment these values before running the sample.
    # project_id  = "my-project"
    # location_id = "us-east1"
    # key_ring_id = "my-key-ring"
    # id          = "my-hsm-key"
    
    # Require the library.
    require "google/cloud/kms"
    
    # Create the client.
    client = Google::Cloud::[Kms](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms.html).[key_management_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms/latest/Google-Cloud-Kms.html)
    
    # Build the parent key ring name.
    key_ring_name = client.[key_ring_path](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-KeyManagementService-Paths.html) project: project_id, location: location_id, key_ring: key_ring_id
    
    # Build the key.
    key = {
      purpose:          :ENCRYPT_DECRYPT,
      version_template: {
        algorithm:        :GOOGLE_SYMMETRIC_ENCRYPTION,
        protection_level: :HSM
      },
    
      # Optional: customize how long key versions should be kept before destroying.
      destroy_scheduled_duration: {
        seconds: 24 * 60 * 60
      }
    }
    
    # Call the API.
    created_key = client.create_crypto_key parent: key_ring_name, crypto_key_id: id, crypto_key: key
    puts "Created hsm key: #{created_key.name}"

### API

These examples use [curl](https://curl.haxx.se/) as an HTTP client to demonstrate using the API. For more information about access control, see [Accessing the Cloud KMS API](https://docs.cloud.google.com/kms/docs/accessing-the-api). 

To create a Multi-tenant Cloud HSM key, use the [`CryptoKey.create`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/create) method with the `HSM` protection level:
    
    
    curl "https://cloudkms.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys?crypto_key_id=KEY_NAME" \
        --request "POST" \
        --header "authorization: Bearer TOKEN" \
        --header "content-type: application/json" \
        --data '{"purpose": "ENCRYPT_DECRYPT", "versionTemplate": {
            "protectionLevel": "HSM", "algorithm": "ALGORITHM" }}'
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the key ring.
  * `LOCATION`: the Cloud KMS location of the key ring.
  * `KEY_RING`: the name of the key ring that contains the key.
  * `KEY_NAME`: the name of the key.
  * `ALGORITHM`: the algorithm that you want to use—for example, `GOOGLE_SYMMETRIC_ENCRYPTION`. To see all supported algorithms, see [Key purposes and algorithms](https://docs.cloud.google.com/kms/docs/algorithms).



To create a Single-tenant Cloud HSM key, use the [`CryptoKey.create`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/create) method with the `HSM_SINGLE_TENANT` protection level:
    
    
    curl "https://cloudkms.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys?crypto_key_id=KEY_NAME" \
        --request "POST" \
        --header "authorization: Bearer TOKEN" \
        --header "content-type: application/json" \
        --data '{"purpose": "ENCRYPT_DECRYPT", "versionTemplate": {
            "protectionLevel": "HSM_SINGLE_TENANT", "algorithm": "ALGORITHM",
            "cryptoKeyBackend": "projects/INSTANCE_PROJECT/locations/LOCATION/singleTenantHsmInstances/INSTANCE_NAME" }}'
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the key ring.
  * `LOCATION`: the Cloud KMS location of the key ring.
  * `KEY_RING`: the name of the key ring that contains the key.
  * `KEY_NAME`: the name of the key.
  * `ALGORITHM`: the algorithm that you want to use—for example, `GOOGLE_SYMMETRIC_ENCRYPTION`. To see all supported algorithms, see [Key purposes and algorithms](https://docs.cloud.google.com/kms/docs/algorithms).
  * `INSTANCE_PROJECT`: the identifier of the project where your Single-tenant Cloud HSM instance is located.
  * `INSTANCE_NAME`: the name of the Single-tenant Cloud HSM instance where you want to create the key. For more information about Single-tenant Cloud HSM instances, see [Create and manage a Single-tenant Cloud HSM instance](https://docs.cloud.google.com/kms/docs/create-manage-single-tenant-hsm). 



## Encrypt data

Now that you have a key, you can use that key to encrypt text or binary content.

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

## Decrypt ciphertext

To decrypt encrypted content, you must use the same key that was used to encrypt the content.

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

## Next steps

  * The encryption example in this topic used a symmetric key with the [protection level](https://docs.cloud.google.com/kms/docs/algorithms#protection_levels) of HSM. To encrypt using an asymmetric key with the protection level of HSM, follow the steps at [Encrypting and decrypting data with an asymmetric key](https://docs.cloud.google.com/kms/docs/encrypt-decrypt-rsa) with these changes: 

    * Create the key ring in one of the [supported regions for Cloud HSM](https://docs.cloud.google.com/kms/docs/locations).
    * Create the key with protection level HSM.
  * To use an asymmetric key with the [protection level](https://docs.cloud.google.com/kms/docs/algorithms#protection_levels) of HSM for elliptic curve signing or RSA signing, follow the steps at [Create and validate signatures](https://docs.cloud.google.com/kms/docs/create-validate-signatures) with these changes: 

    * Create the key ring in one of the [supported regions for Cloud HSM](https://docs.cloud.google.com/kms/docs/locations).
    * Create the key with protection level HSM.
  * Start [using the API](https://docs.cloud.google.com/kms/docs/accessing-the-api).

  * Take a look at the [Cloud KMS API Reference](https://docs.cloud.google.com/kms/docs/reference/rest).

  * Read [How-to guides](https://docs.cloud.google.com/kms/docs/how-tos) to get started with creating, rotating, and setting permissions on keys.

  * Read [Concepts](https://docs.cloud.google.com/kms/docs/concepts) to better understand object hierarchy, key states, and key rotation.

  * Learn about [Logging](https://docs.cloud.google.com/kms/docs/logging) in Cloud KMS. Note that logging is based on operations, and applies to keys with both HSM and software protection levels.

  * Learn more about how Cloud HSM protects your data in the [Cloud HSM architecture whitepaper](https://docs.cloud.google.com/docs/security/cloud-hsm-architecture).




## Known limitations

  * Message size is limited to 8 KiB (as opposed to 64 KiB for Cloud KMS software keys) for user-provided plaintext and ciphertext, including the [additional authenticated data](https://docs.cloud.google.com/kms/docs/additional-authenticated-data).

  * Cloud HSM is not available in all multi-regions. For a list of all locations that support Multi-tenant Cloud HSM, see [Cloud KMS locations](https://docs.cloud.google.com/kms/docs/locations), and select **Supports multi-tenant HSM** for the **HSM support** filter.

  * Single-tenant Cloud HSM is available in a subset of locations where Multi-tenant Cloud HSM is available. For a list of all locations that support Single-tenant Cloud HSM, see [Cloud KMS locations](https://docs.cloud.google.com/kms/docs/locations), and select **Supports single-tenant HSM** for the **HSM support** filter.

  * If you use Cloud HSM keys with customer-managed encryption key (CMEK) integrations in other Google Cloud services, the locations you use for the services must match the locations of your Cloud HSM keys exactly. This applies to regional, dual-regional, and multi-regional locations.

For more information about CMEK integrations, see the relevant section of [Encryption at rest](https://cloud.google.com/security/encryption/default-encryption/).

  * Key operations for asymmetric keys stored in Cloud HSM may incur a noticeably greater latency compared to using Cloud KMS software keys.




## Bare Metal Rack HSM

Google Cloud offers additional HSM options, such as single-tenancy. [Bare Metal Rack HSM](https://docs.cloud.google.com/kms/docs/bare-metal-rack-hsm) is available for customers to host their own HSMs in Google-provided space. Inquire with your account representative for additional information.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
