---
url: https://docs.cloud.google.com/secret-manager/docs/samples/secretmanager-delete-regional-secret-with-etag/
title: Delete regional secret with Etag \u00a0|\u00a0 Secret Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:58:28.375235+00:00
---

# Delete regional secret with Etag  |  Secret Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/docs/samples/secretmanager-delete-regional-secret-with-etag/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Samples ](https://docs.cloud.google.com/secret-manager/docs/samples)



#  Delete regional secret with Etag Stay organized with collections  Save and categorize content based on your preferences. 

Deletes a regional secret with Etag

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Use entity tags for optimistic concurrency control](https://docs.cloud.google.com/secret-manager/regional-secrets/etags-regional-secrets)



## Code sample

### C#

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.SecretManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.html);
    
    public class DeleteRegionalSecretWithEtagSample
    {
        public void DeleteRegionalSecretWithEtag(
          string projectId = "my-project",
          string locationId = "my-location",
          string secretId = "my-secret",
          string etag = "\"1234\""
        )
        {
            // Create the Regional Secret Manager Client.
            [SecretManagerServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html) client = new [SecretManagerServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClientBuilder.html)
            {
                Endpoint = $"secretmanager.{locationId}.rep.googleapis.com"
            }.[Build](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClientBuilder.html#Google_Cloud_SecretManager_V1_SecretManagerServiceClientBuilder_Build)();
    
            [DeleteSecretRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.DeleteSecretRequest.html) request = new [DeleteSecretRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.DeleteSecretRequest.html)
            {
                SecretName = [SecretName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretName.html).[FromProjectLocationSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretName.html#Google_Cloud_SecretManager_V1_SecretName_FromProjectLocationSecret_System_String_System_String_System_String_)(projectId, locationId, secretId),
                Etag = etag
            };
    
            // Delete the secret.
            client.[DeleteSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html#Google_Cloud_SecretManager_V1_SecretManagerServiceClient_DeleteSecret_Google_Cloud_SecretManager_V1_DeleteSecretRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
        }
    }

### Go

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    
    	secretmanager "cloud.google.com/go/secretmanager/apiv1"
    	"cloud.google.com/go/secretmanager/apiv1/secretmanagerpb"
    	"google.golang.org/api/option"
    )
    
    // deleteSecretWithEtag deletes the secret with the given name and all of its versions.
    func DeleteRegionalSecretWithEtag(projectId, locationId, secretId, etag string) error {
    	// name := "projects/my-project/locations/my-location/secrets/my-secret"
    	// etag := `"123"`
    
    	// Create the client.
    	ctx := context.Background()
    	//Endpoint to send the request to regional server
    	endpoint := fmt.Sprintf("secretmanager.%s.rep.googleapis.com:443", locationId)
    	client, err := secretmanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_NewClient)(ctx, option.WithEndpoint(endpoint))
    
    	if err != nil {
    		return fmt.Errorf("failed to create secretmanager client: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_Close)()
    
    	//Endpoint to send the request to regional server
    	name := fmt.Sprintf("projects/%s/locations/%s/secrets/%s", projectId, locationId, secretId)
    
    	// Build the request.
    	req := &secretmanagerpb.DeleteSecretRequest{
    		Name: name,
    		Etag: etag,
    	}
    
    	// Call the API.
    	if err := client.DeleteSecret(ctx, req); err != nil {
    		return fmt.Errorf("failed to delete regional secret: %w", err)
    	}
    	return nil
    }
    

### Java

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.secretmanager.v1.[DeleteSecretRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.DeleteSecretRequest.html);
    import com.google.cloud.secretmanager.v1.[SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html);
    import com.google.cloud.secretmanager.v1.[SecretManagerServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceSettings.html);
    import com.google.cloud.secretmanager.v1.[SecretName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html);
    import java.io.IOException;
    
    public class DeleteRegionalSecretWithEtag {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
    
        // Your GCP project ID.
        String projectId = "your-project-id";
        // Location of the secret.
        String locationId = "your-location-id";
        // Resource ID of the secret to delete.
        String secretId = "your-secret-id";
        // Etag associated with the secret. Quotes should be included as part of the string.
        String etag = "\"1234\"";
        deleteRegionalSecretWithEtag(projectId, locationId, secretId, etag);
      }
    
      // Delete an existing secret with the given name and etag.
      public static void deleteRegionalSecretWithEtag(
          String projectId, String locationId, String secretId, String etag)
          throws IOException {
    
        // Endpoint to call the regional secret manager sever
        String apiEndpoint = String.format("secretmanager.%s.rep.googleapis.com:443", locationId);
        [SecretManagerServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceSettings.html) secretManagerServiceSettings =
            [SecretManagerServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceSettings.html).newBuilder().setEndpoint(apiEndpoint).build();
    
        // Initialize the client that will be used to send requests. This client only needs to be
        // created once, and can be reused for multiple requests.
        try ([SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html) client = 
            [SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html).create(secretManagerServiceSettings)) {
          // Build the secret name.
          [SecretName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html) secretName = [SecretName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html).[ofProjectLocationSecretName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html#com_google_cloud_secretmanager_v1_SecretName_ofProjectLocationSecretName_java_lang_String_java_lang_String_java_lang_String_)(
              projectId, locationId, secretId);
    
          // Construct the request.
          [DeleteSecretRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.DeleteSecretRequest.html) request =
              [DeleteSecretRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.DeleteSecretRequest.html).newBuilder()
                  .setName(secretName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html#com_google_cloud_secretmanager_v1_SecretName_toString__)())
                  .setEtag(etag)
                  .build();
    
          // Delete the secret.
          client.deleteSecret(request);
          System.out.printf("Deleted regional secret %s\n", secretId);
        }
      }
    }

### Ruby

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id  = "YOUR-GOOGLE-CLOUD-PROJECT"  # (e.g. "my-project")
    # location_id = "YOUR-GOOGLE-CLOUD-LOCATION" # (e.g. "us-west1")
    # secret_id   = "YOUR-SECRET-ID"             # (e.g. "my-secret")
    # etag        = "YOUR-ETAG-ASSOCIATED-WITH-SECRET"  # (e.g. "\"1234\"")
    
    # Require the Secret Manager client library.
    require "google/cloud/secret_manager"
    
    # Endpoint for the regional secret manager service.
    api_endpoint = "secretmanager.#{location_id}.rep.googleapis.com"
    
    # Create the Secret Manager client.
    client = Google::Cloud::[SecretManager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager/latest/Google-Cloud-SecretManager.html).[secret_manager_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager/latest/Google-Cloud-SecretManager.html) do |config|
      config.endpoint = api_endpoint
    end
    
    # Build the resource name of the secret.
    name = client.secret_path project: project_id, location: location_id, secret: secret_id
    
    # Delete the secret.
    client.delete_secret name: name, etag: etag
    
    # Print a success message.
    puts "Deleted regional secret #{name}"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=secretmanager). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
