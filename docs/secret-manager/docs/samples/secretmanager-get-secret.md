---
url: https://docs.cloud.google.com/secret-manager/docs/samples/secretmanager-get-secret/
title: Get secret \u00a0|\u00a0 Secret Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:21:35.554581+00:00
---

# Get secret  |  Secret Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/docs/samples/secretmanager-get-secret/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Samples ](https://docs.cloud.google.com/secret-manager/docs/samples)



#  Get secret Stay organized with collections  Save and categorize content based on your preferences. 

Gets a secret.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [List secrets and view secret details](https://docs.cloud.google.com/secret-manager/docs/view-secret-details)



## Code sample

### C#

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.SecretManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.html);
    
    public class GetSecretSample
    {
        public Secret GetSecret(string projectId = "my-project", string secretId = "my-secret")
        {
            // Create the client.
            [SecretManagerServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html) client = [SecretManagerServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html#Google_Cloud_SecretManager_V1_SecretManagerServiceClient_Create)();
    
            // Build the resource name.
            [SecretName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretName.html) secretName = new [SecretName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretName.html)(projectId, secretId);
    
            // Call the API.
            Secret secret = client.[GetSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html#Google_Cloud_SecretManager_V1_SecretManagerServiceClient_GetSecret_Google_Cloud_SecretManager_V1_GetSecretRequest_Google_Api_Gax_Grpc_CallSettings_)(secretName);
            return secret;
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
    
    // getSecret gets information about the given secret. This only returns metadata
    // about the secret container, not any secret material.
    func getSecret(w io.Writer, name string) error {
    	// name := "projects/my-project/secrets/my-secret"
    
    	// Create the client.
    	ctx := context.Background()
    	client, err := secretmanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create secretmanager client: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_Close)()
    
    	// Build the request.
    	req := &secretmanagerpb.GetSecretRequest{
    		Name: name,
    	}
    
    	// Call the API.
    	result, err := client.GetSecret(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to get secret: %w", err)
    	}
    
    	replication := result.Replication.Replication
    	fmt.Fprintf(w, "Found secret %s with replication policy %s\n", result.Name, replication)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.secretmanager.v1.[Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html);
    import com.google.cloud.secretmanager.v1.[SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html);
    import com.google.cloud.secretmanager.v1.[SecretName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html);
    import java.io.IOException;
    
    public class GetSecret {
    
      public static void getSecret() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String secretId = "your-secret-id";
        getSecret(projectId, secretId);
      }
    
      // Get an existing secret.
      public static void getSecret(String projectId, String secretId) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html) client = [SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html).create()) {
          // Build the name.
          [SecretName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html) secretName = [SecretName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html).of(projectId, secretId);
    
          // Create the secret.
          [Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html) secret = client.getSecret(secretName);
    
          // Get the replication policy.
          String replication = "";
          if (secret.[getReplication](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html#com_google_cloud_secretmanager_v1_Secret_getReplication__)().getAutomatic() != null) {
            replication = "AUTOMATIC";
          } else if (secret.[getReplication](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html#com_google_cloud_secretmanager_v1_Secret_getReplication__)().getUserManaged() != null) {
            replication = "MANAGED";
          } else {
            throw new IllegalStateException("Unknown replication type");
          }
    
          System.out.printf("Secret %s, replication %s\n", secret.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html#com_google_cloud_secretmanager_v1_Secret_getName__)(), replication);
        }
      }
    }

### Node.js

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Get metadata about a secret.
     *
     * @param {string} projectId The ID of the Google Cloud project.
     * @param {string} secretId The ID of the secret to retrieve.
     */
    async function getSecret(projectId, secretId) {
      const client = new SecretManagerServiceClient();
      const name = `projects/${projectId}/secrets/${secretId}`;
      try {
        const [secret] = await client.getSecret({
          name: name,
        });
    
        if (secret.replication && secret.replication.replication) {
          const policy = secret.replication.replication;
          console.info(
            `Found secret ${secret.name} with replication policy ${policy}`
          );
        } else {
          console.info(`Found secret ${secret.name} with no replication policy.`);
        }
        return secret;
      } catch (err) {
        console.error(`Failed to retrieve secret ${name}:`, err);
      } finally {
        await client.close();
      }
    }

### PHP

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Import the Secret Manager client library.
    use Google\Cloud\SecretManager\V1\Client\SecretManagerServiceClient;
    use Google\Cloud\SecretManager\V1\GetSecretRequest;
    
    /**
     * @param string $projectId Your Google Cloud Project ID (e.g. 'my-project')
     * @param string $secretId  Your secret ID (e.g. 'my-secret')
     */
    function get_secret(string $projectId, string $secretId): void
    {
        // Create the Secret Manager client.
        $client = new SecretManagerServiceClient();
    
        // Build the resource name of the secret.
        $name = $client->secretName($projectId, $secretId);
    
        // Build the request.
        $request = GetSecretRequest::build($name);
    
        // Get the secret.
        $secret = $client->getSecret($request);
    
        // Get the replication policy.
        $replication = strtoupper($secret->getReplication()->getReplication());
    
        // Print data about the secret.
        printf('Got secret %s with replication policy %s', $secret->getName(), $replication);
    }

### Python

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def get_secret(project_id: str, secret_id: str) -> secretmanager.GetSecretRequest:
        """
        Get information about the given secret. This only returns metadata about
        the secret container, not any secret material.
        """
    
        # Import the Secret Manager client library.
        from google.cloud import secretmanager
    
        # Create the Secret Manager client.
        client = secretmanager.SecretManagerServiceClient()
    
        # Build the resource name of the secret.
        name = client.secret_path(project_id, secret_id)
    
        # Get the secret.
        response = client.get_secret(request={"name": name})
    
        # Get the replication policy.
        if "automatic" in response.replication:
            replication = "AUTOMATIC"
        elif "user_managed" in response.replication:
            replication = "MANAGED"
        else:
            raise Exception(f"Unknown replication {response.replication}")
    
        # Print data about the secret.
        print(f"Got secret {response.name} with replication policy {replication}")

### Ruby

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id = "YOUR-GOOGLE-CLOUD-PROJECT"  # (e.g. "my-project")
    # secret_id  = "YOUR-SECRET-ID"             # (e.g. "my-secret")
    
    # Require the Secret Manager client library.
    require "google/cloud/secret_manager"
    
    # Create a Secret Manager client.
    client = Google::Cloud::[SecretManager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager.html).[secret_manager_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager/latest/Google-Cloud-SecretManager.html)
    
    # Build the resource name of the secret.
    name = client.secret_path project: project_id, secret: secret_id
    
    # Get the secret.
    secret = client.get_secret name: name
    
    # Get the replication policy.
    if !secret.replication.automatic.nil?
      replication = "automatic"
    elsif !secret.replication.user_managed.nil?
      replication = "user managed"
    else
      raise "Unknown replication #{secret.replication}"
    end
    
    # Print a success message.
    puts "Got secret #{secret.name} with replication policy #{replication}"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=secretmanager). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
