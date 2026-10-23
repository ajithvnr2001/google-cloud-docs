---
url: https://docs.cloud.google.com/kms/docs/samples/kms-create-key-ring/
title: Create a key ring \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:38.371180+00:00
---

# Create a key ring  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/samples/kms-create-key-ring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Samples ](https://docs.cloud.google.com/kms/docs/samples)



#  Create a key ring Stay organized with collections  Save and categorize content based on your preferences. 

Create a key ring.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Cloud HSM](https://docs.cloud.google.com/kms/docs/hsm)
  * [Create a key ring](https://docs.cloud.google.com/kms/docs/create-key-ring)



## Code sample

### C#

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

To learn how to install and use the client library for Cloud KMS, see [Cloud KMS client libraries](https://docs.cloud.google.com/kms/docs/reference/libraries). 

To authenticate to Cloud KMS, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudkeymanagementservice). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
