---
url: https://docs.cloud.google.com/secret-manager/docs/samples/secretmanager-get-secret-version/
title: Get secret version \u00a0|\u00a0 Secret Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:40:22.416396+00:00
---

# Get secret version  |  Secret Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/docs/samples/secretmanager-get-secret-version/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Samples ](https://docs.cloud.google.com/secret-manager/docs/samples)



#  Get secret version Stay organized with collections  Save and categorize content based on your preferences. 

Gets a secret's version metadata.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [View secret version details](https://docs.cloud.google.com/secret-manager/docs/view-secret-version)



## Code sample

### C#

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.SecretManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.html);
    
    public class GetSecretVersionSample
    {
        public SecretVersion GetSecretVersion(
          string projectId = "my-project", string secretId = "my-secret", string secretVersionId = "123")
        {
            // Create the client.
            [SecretManagerServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html) client = [SecretManagerServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html#Google_Cloud_SecretManager_V1_SecretManagerServiceClient_Create)();
    
            // Build the resource name.
            [SecretVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretVersionName.html) secretVersionName = new [SecretVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretVersionName.html)(projectId, secretId, secretVersionId);
    
            // Call the API.
            [SecretVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretVersion.html) version = client.[GetSecretVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html#Google_Cloud_SecretManager_V1_SecretManagerServiceClient_GetSecretVersion_Google_Cloud_SecretManager_V1_GetSecretVersionRequest_Google_Api_Gax_Grpc_CallSettings_)(secretVersionName);
            return version;
        }
    }

### Go

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	secretmanager "cloud.google.com/go/secretmanager/apiv1"
    	"cloud.google.com/go/secretmanager/apiv1/secretmanagerpb"
    )
    
    // getSecretVersion gets information about the given secret version. It does not
    // include the payload data.
    func getSecretVersion(w io.Writer, name string) error {
    	// name := "projects/my-project/secrets/my-secret/versions/5"
    	// name := "projects/my-project/secrets/my-secret/versions/latest"
    
    	// Create the client.
    	ctx := context.Background()
    	client, err := secretmanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create secretmanager client: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_Close)()
    
    	// Build the request.
    	req := &secretmanagerpb.GetSecretVersionRequest{
    		Name: name,
    	}
    
    	// Call the API.
    	result, err := client.GetSecretVersion(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to get secret version: %w", err)
    	}
    
    	fmt.Fprintf(w, "Found secret version %s with state %s\n",
    		result.Name, result.State)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.secretmanager.v1.[SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html);
    import com.google.cloud.secretmanager.v1.[SecretVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretVersion.html);
    import com.google.cloud.secretmanager.v1.[SecretVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretVersionName.html);
    import java.io.IOException;
    
    public class GetSecretVersion {
    
      public static void getSecretVersion() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String secretId = "your-secret-id";
        String versionId = "your-version-id";
        getSecretVersion(projectId, secretId, versionId);
      }
    
      // Get an existing secret version.
      public static void getSecretVersion(String projectId, String secretId, String versionId)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html) client = [SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html).create()) {
          // Build the name from the version.
          [SecretVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretVersionName.html) secretVersionName = [SecretVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretVersionName.html).of(projectId, secretId, versionId);
    
          // Create the secret.
          [SecretVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretVersion.html) version = client.getSecretVersion(secretVersionName);
          System.out.printf("Secret version %s, state %s\n", version.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretVersion.html#com_google_cloud_secretmanager_v1_SecretVersion_getName__)(), version.[getState](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretVersion.html#com_google_cloud_secretmanager_v1_SecretVersion_getState__)());
        }
      }
    }

### Node.js

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const name = 'projects/my-project/secrets/my-secret/versions/5';
    // const name = 'projects/my-project/secrets/my-secret/versions/latest';
    
    // Imports the Secret Manager library
    const {SecretManagerServiceClient} = require('[@google-cloud/secret-manager](https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/overview.html)');
    
    // Instantiates a client
    const client = new [SecretManagerServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/overview.html)();
    
    async function getSecretVersion() {
      const [version] = await client.getSecretVersion({
        name: name,
      });
    
      console.info(`Found secret ${version.name} with state ${version.state}`);
    }
    
    getSecretVersion();

### PHP

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Import the Secret Manager client library.
    use Google\Cloud\SecretManager\V1\Client\SecretManagerServiceClient;
    use Google\Cloud\SecretManager\V1\SecretVersion\State;
    use Google\Cloud\SecretManager\V1\GetSecretVersionRequest;
    
    /**
     * @param string $projectId Your Google Cloud Project ID (e.g. 'my-project')
     * @param string $secretId  Your secret ID (e.g. 'my-secret')
     * @param string $versionId Your version ID (e.g. 'latest' or '5');
     */
    function get_secret_version(string $projectId, string $secretId, string $versionId): void
    {
        // Create the Secret Manager client.
        $client = new SecretManagerServiceClient();
    
        // Build the resource name of the secret version.
        $name = $client->secretVersionName($projectId, $secretId, $versionId);
    
        // Build the request.
        $request = GetSecretVersionRequest::build($name);
    
        // Access the secret version.
        $response = $client->getSecretVersion($request);
    
        // Get the state string from the enum.
        $state = State::name($response->getState());
    
        // Print a success message.
        printf('Got secret version %s with state %s', $response->getName(), $state);
    }

### Python

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def get_secret_version(
        project_id: str, secret_id: str, version_id: str
    ) -> secretmanager.GetSecretVersionRequest:
        """
        Get information about the given secret version. It does not include the
        payload data.
        """
    
        # Import the Secret Manager client library.
        from google.cloud import secretmanager
    
        # Create the Secret Manager client.
        client = secretmanager.SecretManagerServiceClient()
    
        # Build the resource name of the secret version.
        name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"
    
        # Get the secret version.
        response = client.get_secret_version(request={"name": name})
    
        # Print information about the secret version.
        state = response.state.name
        print(f"Got secret version {response.name} with state {state}")

### Ruby

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id = "YOUR-GOOGLE-CLOUD-PROJECT"  # (e.g. "my-project")
    # secret_id  = "YOUR-SECRET-ID"             # (e.g. "my-secret")
    # version_id = "YOUR-VERSION"               # (e.g. "5" or "latest")
    
    # Require the Secret Manager client library.
    require "google/cloud/secret_manager"
    
    # Create a Secret Manager client.
    client = Google::Cloud::[SecretManager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager.html).[secret_manager_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager/latest/Google-Cloud-SecretManager.html)
    
    # Build the resource name of the secret version.
    name = client.secret_version_path(
      project:        project_id,
      secret:         secret_id,
      secret_version: version_id
    )
    
    # Get the secret version.
    version = client.get_secret_version name: name
    
    # Get the state.
    state = version.state.to_s.downcase
    
    # Print a success message.
    puts "Got secret version #{version.name} with state #{state}"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=secretmanager). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
