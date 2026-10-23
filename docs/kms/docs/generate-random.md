---
url: https://docs.cloud.google.com/kms/docs/generate-random/
title: Generating random bytes \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:41.797115+00:00
---

# Generating random bytes  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/generate-random/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Generating random bytes Stay organized with collections  Save and categorize content based on your preferences. 

This topic shows you how to retrieve random bytes from the random number generator in Cloud HSM.

## Before you begin

  * Grant the `cloudkms.locations.generateRandomBytes` permission in the cloud location(s) where your service will be generating random bytes. You can learn about permissions in Cloud Key Management Service at [Permissions and roles](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles).



## Generating random bytes

### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Cloud KMS C# SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-csharp).
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.html);
    
    public class GenerateRandomBytesSample
    {
        public byte[] GenerateRandomBytes(
          string projectId = "my-project", string locationId = "us-east1", int numBytes = 256)
        {
            // Create the client.
            [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_Create)();
    
            // Build the location name.
            [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html) locationName = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, locationId);
    
            // Call the API.
            [GenerateRandomBytesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.GenerateRandomBytesResponse.html) result = client.[GenerateRandomBytes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyManagementServiceClient.html#Google_Cloud_Kms_V1_KeyManagementServiceClient_GenerateRandomBytes_Google_Cloud_Kms_V1_GenerateRandomBytesRequest_Google_Api_Gax_Grpc_CallSettings_)(locationName.[ToString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html#Google_Api_Gax_ResourceNames_LocationName_ToString)(), numBytes, [ProtectionLevel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ProtectionLevel.html).[Hsm](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ProtectionLevel.html#Google_Cloud_Kms_V1_ProtectionLevel_Hsm));
    
            // The data comes back as raw bytes, which may include non-printable
            // characters. To print the result, you could encode it as base64.
            // string encodedData = result.Data.ToBase64();
    
            return result.[Data](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.GenerateRandomBytesResponse.html#Google_Cloud_Kms_V1_GenerateRandomBytesResponse_Data).ToByteArray();
        }
    }

### Go

To run this code, first [set up a Go development environment](https://docs.cloud.google.com/go/docs/setup) and [install the Cloud KMS Go SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-go).
    
    
    import (
    	"context"
    	"encoding/base64"
    	"fmt"
    	"io"
    
    	kms "cloud.google.com/go/kms/apiv1"
    	"cloud.google.com/go/kms/apiv1/kmspb"
    )
    
    // generateRandomBytes generates random bytes with entropy sourced from the
    // given location.
    func generateRandomBytes(w io.Writer, location string, numBytes int32) error {
    	// name := "projects/my-project/locations/us-east1"
    	// numBytes := 256
    
    	// Create the client.
    	ctx := context.Background()
    	client, err := kms.[NewKeyManagementClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1.html#cloud_google_com_go_kms_apiv1_KeyManagementClient_NewKeyManagementClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create kms client: %w", err)
    	}
    	defer client.Close()
    
    	// Build the request.
    	req := &kmspb.GenerateRandomBytesRequest{
    		Location:        location,
    		LengthBytes:     numBytes,
    		ProtectionLevel: kmspb.[ProtectionLevel_HSM](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/kms/latest/apiv1/kmspb.html#cloud_google_com_go_kms_apiv1_kmspb_ProtectionLevel_PROTECTION_LEVEL_UNSPECIFIED_ProtectionLevel_SOFTWARE_ProtectionLevel_HSM_ProtectionLevel_EXTERNAL_ProtectionLevel_EXTERNAL_VPC_ProtectionLevel_HSM_SINGLE_TENANT),
    	}
    
    	// Generate random bytes.
    	result, err := client.GenerateRandomBytes(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to generate random bytes: %w", err)
    	}
    
    	// The data comes back as raw bytes, which may include non-printable
    	// characters. This base64-encodes the result so it can be printed below.
    	encodedData := base64.StdEncoding.EncodeToString(result.Data)
    
    	fmt.Fprintf(w, "Random bytes: %s", encodedData)
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Cloud KMS Java SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-java).
    
    
    import com.google.cloud.kms.v1.[GenerateRandomBytesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.GenerateRandomBytesResponse.html);
    import com.google.cloud.kms.v1.[KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html);
    import com.google.cloud.kms.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.LocationName.html);
    import com.google.cloud.kms.v1.[ProtectionLevel](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ProtectionLevel.html);
    import java.io.IOException;
    import java.util.Base64;
    
    public class GenerateRandomBytes {
    
      public void generateRandomBytes() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "us-east1";
        int numBytes = 256;
        generateRandomBytes(projectId, locationId, numBytes);
      }
    
      // Create a new key for use with MacSign.
      public void generateRandomBytes(String projectId, String locationId, int numBytes)
          throws IOException {
        // Initialize client that will be used to send requests. This client only
        // needs to be created once, and can be reused for multiple requests. After
        // completing all of your requests, call the "close" method on the client to
        // safely clean up any remaining background resources.
        try ([KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html) client = [KeyManagementServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.KeyManagementServiceClient.html).create()) {
          // Build the parent name for the location.
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.LocationName.html) locationName = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.LocationName.html).of(projectId, locationId);
    
          // Generate the bytes.
          [GenerateRandomBytesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.GenerateRandomBytesResponse.html) response =
              client.generateRandomBytes(locationName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.LocationName.html#com_google_cloud_kms_v1_LocationName_toString__)(), numBytes, [ProtectionLevel](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ProtectionLevel.html).HSM);
    
          // The data comes back as raw bytes, which may include non-printable
          // characters. This base64-encodes the result so it can be printed below.
          String encodedData = Base64.getEncoder().encodeToString(response.[getData](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.GenerateRandomBytesResponse.html#com_google_cloud_kms_v1_GenerateRandomBytesResponse_getData__)().toByteArray());
    
          System.out.printf("Random bytes: %s", encodedData);
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
    // const numBytes = 256;
    
    // Imports the Cloud KMS library
    const {KeyManagementServiceClient} = require('[@google-cloud/kms](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)');
    
    // Instantiates a client
    const client = new [KeyManagementServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/kms/latest/overview.html)();
    
    // Build the location name
    const locationName = client.locationPath(projectId, locationId);
    
    async function generateRandomBytes() {
      const [randomBytesResponse] = await client.generateRandomBytes({
        location: locationName,
        lengthBytes: numBytes,
        protectionLevel: 'HSM',
      });
    
      console.log(`Random bytes: ${randomBytesResponse.data.toString('base64')}`);
      return randomBytesResponse;
    }
    
    return generateRandomBytes();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Cloud KMS PHP SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-php).
    
    
    use Google\Cloud\Kms\V1\Client\KeyManagementServiceClient;
    use Google\Cloud\Kms\V1\GenerateRandomBytesRequest;
    use Google\Cloud\Kms\V1\ProtectionLevel;
    
    /**
     * Generate a random byte string using Cloud KMS.
     *
     * @param string $projectId The Google Cloud project ID.
     * @param string $locationId The location ID (e.g. us-east1).
     * @param int $numBytes The number of bytes to generate.
     */
    function generate_random_bytes(
        string $projectId,
        string $locationId = 'us-east1',
        int $numBytes = 256
    ) {
        // Create the Cloud KMS client.
        $client = new KeyManagementServiceClient();
    
        // Build the parent name.
        $locationName = $client->locationName($projectId, $locationId);
    
        // Call the API.
        $generateRandomBytesRequest = (new GenerateRandomBytesRequest())
            ->setLocation($locationName)
            ->setLengthBytes($numBytes)
            ->setProtectionLevel(ProtectionLevel::HSM);
        $randomBytesResponse = $client->generateRandomBytes($generateRandomBytesRequest);
    
        // The data comes back as raw bytes, which may include non-printable
        // characters. This base64-encodes the result so it can be printed below.
        $encodedData = base64_encode($randomBytesResponse->getData());
        printf('Random bytes: %s' . PHP_EOL, $encodedData);
    
        return $randomBytesResponse;
    }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Cloud KMS Python SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-python).
    
    
    # Import base64 for encoding the bytes for printing.
    import base64
    
    # Import the client library.
    from google.cloud import kms
    
    
    def generate_random_bytes(project_id: str, location_id: str, num_bytes: int) -> bytes:
        """
        Generate random bytes with entropy sourced from the given location.
    
        Args:
            project_id (string): Google Cloud project ID (e.g. 'my-project').
            location_id (string): Cloud KMS location (e.g. 'us-east1').
            num_bytes (integer): number of bytes of random data.
    
        Returns:
            bytes: Encrypted ciphertext.
    
        """
    
        # Create the client.
        client = kms.[KeyManagementServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html)()
    
        # Build the location name.
        location_name = client.[common_location_path](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_common_location_path)(project_id, location_id)
    
        # Call the API.
        protection_level = kms.[ProtectionLevel](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.ProtectionLevel.html).HSM
        random_bytes_response = client.[generate_random_bytes](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.KeyManagementServiceClient.html#google_cloud_kms_v1_services_key_management_service_KeyManagementServiceClient_generate_random_bytes)(
            request={
                "location": location_name,
                "length_bytes": num_bytes,
                "protection_level": protection_level,
            }
        )
    
        print(f"Random bytes: {base64.b64encode(random_bytes_response.data)}")
        return random_bytes_response
    
    

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Cloud KMS Ruby SDK](https://docs.cloud.google.com/kms/docs/reference/libraries#client-libraries-install-ruby).
    
    
    # TODO(developer): uncomment these values before running the sample.
    # project_id  = "my-project"
    # location_id = "us-east1"
    # num_bytes = 256
    
    # Require the library.
    require "google/cloud/kms"
    
    # Create the client.
    client = Google::Cloud::[Kms](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms.html).[key_management_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms/latest/Google-Cloud-Kms.html)
    
    # Build the parent location name.
    location_name = client.location_path project:    project_id,
                                         location:   location_id
    
    # Call the API.
    response = client.generate_random_bytes location: location_name, length_bytes: num_bytes, protection_level: :HSM
    
    # The data comes back as raw bytes, which may include non-printable
    # characters. This base64-encodes the result so it can be printed below.
    encoded_data = Base64.strict_encode64 response.data
    
    puts "Random bytes: #{encoded_data}"

## Known limitations

  * The `GenerateRandomBytes` API call can produce at most 1024 bytes of randomness per call. To generate more bytes of randomness, you can make multiple API calls.

  * The `GenerateRandomBytes` API call is not supported for the **Software** or **External** [protection levels](https://docs.cloud.google.com/kms/docs/algorithms#protection_levels).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
