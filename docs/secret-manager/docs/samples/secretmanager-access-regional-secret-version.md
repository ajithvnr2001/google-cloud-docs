---
url: https://docs.cloud.google.com/secret-manager/docs/samples/secretmanager-access-regional-secret-version/
title: Access regional secret version \u00a0|\u00a0 Secret Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:41:09.566297+00:00
---

# Access regional secret version  |  Secret Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/docs/samples/secretmanager-access-regional-secret-version/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Samples ](https://docs.cloud.google.com/secret-manager/docs/samples)



#  Access regional secret version Stay organized with collections  Save and categorize content based on your preferences. 

Gets the version of a regional secret

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Access a regional secret version](https://docs.cloud.google.com/secret-manager/regional-secrets/access-secret-version-rs)



## Code sample

### C#

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.SecretManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.html);
    using System;
    
    public class AccessRegionalSecretVersionSample
    {
        public String AccessRegionalSecretVersion(
          string projectId = "my-project",
          string locationId = "my-location",
          string secretId = "my-secret",
          string secretVersionId = "123")
        {
            // Create the Regional Secret Manager Client.
            [SecretManagerServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html) client = new [SecretManagerServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClientBuilder.html)
            {
                Endpoint = $"secretmanager.{locationId}.rep.googleapis.com"
            }.[Build](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClientBuilder.html#Google_Cloud_SecretManager_V1_SecretManagerServiceClientBuilder_Build)();
    
            // Build the resource name.
            [SecretVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretVersionName.html) secretVersionName = [SecretVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretVersionName.html).[FromProjectLocationSecretSecretVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretVersionName.html#Google_Cloud_SecretManager_V1_SecretVersionName_FromProjectLocationSecretSecretVersion_System_String_System_String_System_String_System_String_)(
              projectId, locationId, secretId, secretVersionId);
    
            // Call the API.
            [AccessSecretVersionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.AccessSecretVersionResponse.html) result = client.[AccessSecretVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html#Google_Cloud_SecretManager_V1_SecretManagerServiceClient_AccessSecretVersion_Google_Cloud_SecretManager_V1_AccessSecretVersionRequest_Google_Api_Gax_Grpc_CallSettings_)(secretVersionName);
    
            // Convert the payload to a string. Payloads are bytes by default.
            String payload = result.[Payload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.AccessSecretVersionResponse.html#Google_Cloud_SecretManager_V1_AccessSecretVersionResponse_Payload).[Data](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretPayload.html#Google_Cloud_SecretManager_V1_SecretPayload_Data).ToStringUtf8();
            return payload;
        }
    }

### Go

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"hash/crc32"
    	"io"
    
    	secretmanager "cloud.google.com/go/secretmanager/apiv1"
    	"cloud.google.com/go/secretmanager/apiv1/secretmanagerpb"
    	"google.golang.org/api/option"
    )
    
    // accessSecretVersion accesses the payload for the given secret version if one
    // exists. The version can be a version number as a string (e.g. "5") or an
    // alias (e.g. "latest").
    func AccessRegionalSecretVersion(w io.Writer, projectId, locationId, secretId, versionId string) error {
    	// name := "projects/my-project/locations/my-location/secrets/my-secret/versions/5"
    	// name := "projects/my-project/locations/my-location/secrets/my-secret/versions/latest"
    
    	// Create the client.
    	ctx := context.Background()
    
    	// Endpoint to call the regional secret manager sever
    	endpoint := fmt.Sprintf("secretmanager.%s.rep.googleapis.com:443", locationId)
    	client, err := secretmanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_NewClient)(ctx, option.WithEndpoint(endpoint))
    	if err != nil {
    		return fmt.Errorf("failed to create secretmanager client: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_Close)()
    
    	name := fmt.Sprintf("projects/%s/locations/%s/secrets/%s/versions/%s", projectId, locationId, secretId, versionId)
    
    	// Build the request.
    	req := &secretmanagerpb.AccessSecretVersionRequest{
    		Name: name,
    	}
    
    	// Call the API.
    	result, err := client.AccessSecretVersion(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to access regional secret version: %w", err)
    	}
    
    	// Verify the data checksum.
    	crc32c := crc32.MakeTable(crc32.Castagnoli)
    	checksum := int64(crc32.Checksum(result.Payload.Data, crc32c))
    	if checksum != *result.Payload.DataCrc32C {
    		return fmt.Errorf("Data corruption detected.")
    	}
    
    	// WARNING: Do not print the secret in a production environment - this snippet
    	// is showing how to access the secret material.
    	fmt.Fprintf(w, "Plaintext: %s\n", string(result.Payload.Data))
    	return nil
    }
    

### Java

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.secretmanager.v1.[AccessSecretVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.AccessSecretVersionResponse.html);
    import com.google.cloud.secretmanager.v1.[SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html);
    import com.google.cloud.secretmanager.v1.[SecretManagerServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceSettings.html);
    import com.google.cloud.secretmanager.v1.[SecretPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretPayload.html);
    import com.google.cloud.secretmanager.v1.[SecretVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretVersionName.html);
    import java.util.zip.CRC32C;
    import java.util.zip.Checksum;
    
    public class AccessRegionalSecretVersion {
    
      public static void main(String[] args)throws Exception {
        // TODO(developer): Replace these variables before running the sample.
    
        // Your GCP project ID.
        String projectId = "your-project-id";
        // Location of the secret.
        String locationId = "your-location-id";
        // Resource ID of the secret.
        String secretId = "your-secret-id";
        // Version of the Secret ID you want to access.
        String versionId = "your-version-id";
        accessRegionalSecretVersion(projectId, locationId, secretId, versionId);
      }
    
      // Access the payload for the given secret version if one exists. The version
      // can be a version number as a string (e.g. "5") or an alias (e.g. "latest").
      public static [SecretPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretPayload.html) accessRegionalSecretVersion(
          String projectId, String locationId, String secretId, String versionId)
          throws Exception {
    
        // Endpoint to call the regional secret manager sever
        String apiEndpoint = String.format("secretmanager.%s.rep.googleapis.com:443", locationId);
        [SecretManagerServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceSettings.html) secretManagerServiceSettings =
            [SecretManagerServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceSettings.html).newBuilder().setEndpoint(apiEndpoint).build();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html) client = 
            [SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html).create(secretManagerServiceSettings)) {
          [SecretVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretVersionName.html) secretVersionName = 
              [SecretVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretVersionName.html).[ofProjectLocationSecretSecretVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretVersionName.html#com_google_cloud_secretmanager_v1_SecretVersionName_ofProjectLocationSecretSecretVersionName_java_lang_String_java_lang_String_java_lang_String_java_lang_String_)(
                  projectId, locationId, secretId, versionId);
          // Access the secret version.
          [AccessSecretVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.AccessSecretVersionResponse.html) response = client.accessSecretVersion(secretVersionName);
    
          // Verify checksum. The used library is available in Java 9+.
          // For Java 8, use:
          // https://github.com/google/guava/blob/e62d6a0456420d295089a9c319b7593a3eae4a83/guava/src/com/google/common/hash/Hashing.java#L395
          byte[] data = response.[getPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.AccessSecretVersionResponse.html#com_google_cloud_secretmanager_v1_AccessSecretVersionResponse_getPayload__)().getData().toByteArray();
          Checksum checksum = new CRC32C();
          checksum.update(data, 0, data.length);
          if (response.[getPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.AccessSecretVersionResponse.html#com_google_cloud_secretmanager_v1_AccessSecretVersionResponse_getPayload__)().getDataCrc32C() != checksum.getValue()) {
            System.out.printf("Data corruption detected.");
            throw new Exception("Data corruption detected.");
          }
    
          // Print the secret payload.
          //
          // WARNING: Do not print the secret in a production environment - this
          // snippet is showing how to access the secret material.
          // String payload = response.getPayload().getData().toStringUtf8();
          // System.out.printf("Plaintext: %s\n", payload);
    
          return response.[getPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.AccessSecretVersionResponse.html#com_google_cloud_secretmanager_v1_AccessSecretVersionResponse_getPayload__)();
        }
      }
    }

### Node.js

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'my-project';
    // const locationId = 'location-id';
    // const secretId = 'my-secret'
    // const version = 'secret-version';
    
    const name = `projects/${projectId}/locations/${locationId}/secrets/${secretId}/versions/${version}`;
    
    // Imports the Secret Manager library
    const {SecretManagerServiceClient} = require('[@google-cloud/secret-manager](https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/overview.html)');
    
    // Adding the endpoint to call the regional secret manager sever
    const options = {};
    options.apiEndpoint = `secretmanager.${locationId}.rep.googleapis.com`;
    
    // Instantiates a client
    const client = new [SecretManagerServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/overview.html)(options);
    
    async function accessRegionalSecretVersion() {
      const [version] = await client.accessSecretVersion({
        name: name,
      });
    
      // Extract the payload as a string.
      const payload = version.payload.data.toString();
    
      // WARNING: Do not print the secret in a production environment - this
      // snippet is showing how to access the secret material.
      console.info(`Payload: ${payload}`);
    }
    
    accessRegionalSecretVersion();

### PHP

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Import the Secret Manager client library.
    use Google\Cloud\SecretManager\V1\Client\SecretManagerServiceClient;
    use Google\Cloud\SecretManager\V1\AccessSecretVersionRequest;
    
    /**
     * @param string $projectId Your Google Cloud Project ID (e.g. 'my-project')
     * @param string $locationId Your secret Location (e.g. "us-central1")
     * @param string $secretId  Your secret ID (e.g. 'my-secret')
     * @param string $versionId Your version ID (e.g. 'latest' or '5');
     */
    function access_regional_secret_version(
        string $projectId,
        string $locationId,
        string $secretId,
        string $versionId
    ): void {
        // Specify regional endpoint.
        $options = ['apiEndpoint' => "secretmanager.$locationId.rep.googleapis.com"];
    
        // Create the Secret Manager client.
        $client = new SecretManagerServiceClient($options);
    
        // Build the resource name of the secret version.
        $name = $client->projectLocationSecretSecretVersionName($projectId, $locationId, $secretId, $versionId);
    
        // Build the request.
        $request = AccessSecretVersionRequest::build($name);
    
        // Access the secret version.
        $response = $client->accessSecretVersion($request);
    
        // Print the secret payload.
        //
        // WARNING: Do not print the secret in a production environment - this
        // snippet is showing how to access the secret material.
        $payload = $response->getPayload()->getData();
        printf('Plaintext: %s', $payload);
    }

### Python

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import [secretmanager_v1](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest)
    import google_crc32c
    
    
    def access_regional_secret_version(
        project_id: str,
        location_id: str,
        secret_id: str,
        version_id: str,
    ) -> secretmanager_v1.AccessSecretVersionResponse:
        """
        Access the payload for the given secret version if one exists. The version
        can be a version number as a string (e.g. "5") or an alias (e.g. "latest").
        """
    
        # Endpoint to call the regional secret manager sever.
        api_endpoint = f"secretmanager.{location_id}.rep.googleapis.com"
    
        # Create the Secret Manager client.
        client = [secretmanager_v1](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest).[SecretManagerServiceClient](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html)(
            client_options={"api_endpoint": api_endpoint},
        )
    
        # Build the resource name of the secret version.
        name = f"projects/{project_id}/locations/{location_id}/secrets/{secret_id}/versions/{version_id}"
    
        # Access the secret version.
        response = client.[access_secret_version](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html#google_cloud_secretmanager_v1_services_secret_manager_service_SecretManagerServiceClient_access_secret_version)(request={"name": name})
    
        # Verify payload checksum.
        crc32c = google_crc32c.Checksum()
        crc32c.update(response.payload.data)
        if response.payload.data_crc32c != int(crc32c.hexdigest(), 16):
            print("Data corruption detected.")
            return response
    
        # Print the secret payload.
        #
        # WARNING: Do not print the secret in a production environment - this
        # snippet is showing how to access the secret material.
        payload = response.payload.data.decode("UTF-8")
        print(f"Plaintext: {payload}")
    
        return response
    
    

### Ruby

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id  = "YOUR-GOOGLE-CLOUD-PROJECT"  # (e.g. "my-project")
    # location_id = "YOUR-GOOGLE-CLOUD-LOCATION" # (e.g. "us-west1")
    # secret_id   = "YOUR-SECRET-ID"             # (e.g. "my-secret")
    # version_id  = "YOUR-VERSION"               # (e.g. "5" or "latest")
    
    # Require the Secret Manager client library.
    require "google/cloud/secret_manager"
    
    # Endpoint for the regional secret manager service.
    api_endpoint = "secretmanager.#{location_id}.rep.googleapis.com"
    
    # Create the Secret Manager client.
    client = Google::Cloud::[SecretManager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager.html).[secret_manager_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager/latest/Google-Cloud-SecretManager.html) do |config|
      config.endpoint = api_endpoint
    end
    
    # Build the resource name of the secret version.
    name = client.secret_version_path(
      project:        project_id,
      location:       location_id,
      secret:         secret_id,
      secret_version: version_id
    )
    
    # Access the secret version.
    version = client.access_secret_version name: name
    
    # Print the secret payload.
    #
    # WARNING: Do not print the secret in a production environment - this
    # snippet is showing how to access the secret material.
    payload = version.payload.data
    puts "Plaintext: #{payload}"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=secretmanager). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
