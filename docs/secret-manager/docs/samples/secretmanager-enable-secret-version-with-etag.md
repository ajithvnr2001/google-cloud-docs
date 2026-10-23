---
url: https://docs.cloud.google.com/secret-manager/docs/samples/secretmanager-enable-secret-version-with-etag/
title: Enable a secret with ETags \u00a0|\u00a0 Secret Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:17:41.518478+00:00
---

# Enable a secret with ETags  |  Secret Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/docs/samples/secretmanager-enable-secret-version-with-etag/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Samples ](https://docs.cloud.google.com/secret-manager/docs/samples)



#  Enable a secret with ETags Stay organized with collections  Save and categorize content based on your preferences. 

Shows how to enable a given secret version that contains ETags.

## Code sample

### Go

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    
    	secretmanager "cloud.google.com/go/secretmanager/apiv1"
    	"cloud.google.com/go/secretmanager/apiv1/secretmanagerpb"
    )
    
    // enableSecretVersionWithEtag enables the given secret version, enabling it to be
    // accessed after previously being disabled. Other secrets versions are
    // unaffected.
    func enableSecretVersionWithEtag(name, etag string) error {
    	// name := "projects/my-project/secrets/my-secret/versions/5"
    	// etag := `"123"`
    
    	// Create the client.
    	ctx := context.Background()
    	client, err := secretmanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create secretmanager client: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_Close)()
    
    	// Build the request.
    	req := &secretmanagerpb.EnableSecretVersionRequest{
    		Name: name,
    		Etag: etag,
    	}
    
    	// Call the API.
    	if _, err := client.EnableSecretVersion(ctx, req); err != nil {
    		return fmt.Errorf("failed to enable secret version: %w", err)
    	}
    	return nil
    }
    

### Java

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.secretmanager.v1.[EnableSecretVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.EnableSecretVersionRequest.html);
    import com.google.cloud.secretmanager.v1.[SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html);
    import com.google.cloud.secretmanager.v1.[SecretVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretVersion.html);
    import com.google.cloud.secretmanager.v1.[SecretVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretVersionName.html);
    import java.io.IOException;
    
    public class EnableSecretVersionWithEtag {
    
      public static void enableSecretVersion() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String secretId = "your-secret-id";
        String versionId = "your-version-id";
        // Including the quotes is important.
        String etag = "\"1234\"";
        enableSecretVersion(projectId, secretId, versionId, etag);
      }
    
      // Enable an existing secret version.
      public static void enableSecretVersion(
          String projectId, String secretId, String versionId, String etag)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html) client = [SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html).create()) {
          // Build the name from the version.
          [SecretVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretVersionName.html) secretVersionName = [SecretVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretVersionName.html).of(projectId, secretId, versionId);
    
          // Build the request.
          [EnableSecretVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.EnableSecretVersionRequest.html) request =
              [EnableSecretVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.EnableSecretVersionRequest.html).newBuilder()
                  .setName(secretVersionName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretVersionName.html#com_google_cloud_secretmanager_v1_SecretVersionName_toString__)())
                  .setEtag(etag)
                  .build();
    
          // Enable the secret version.
          [SecretVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretVersion.html) version = client.enableSecretVersion(request);
          System.out.printf("Enabled secret version %s\n", version.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretVersion.html#com_google_cloud_secretmanager_v1_SecretVersion_getName__)());
        }
      }
    }

### Python

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def enable_secret_version_with_etag(
        project_id: str, secret_id: str, version_id: str, etag: str
    ) -> secretmanager.EnableSecretVersionRequest:
        """
        Enable the given secret version, enabling it to be accessed after
        previously being disabled. Other secrets versions are unaffected.
        """
    
        # Import the Secret Manager client library.
        from google.cloud import secretmanager
        from google.cloud.secretmanager_v1.types import service
    
        # Create the Secret Manager client.
        client = secretmanager.[SecretManagerServiceClient](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html)()
    
        # Build the resource name of the secret version
        name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"
    
        # Build the request
        request = service.[EnableSecretVersionRequest](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.types.EnableSecretVersionRequest.html)()
        request.name = name
        request.etag = etag
    
        # Disable the secret version.
        response = client.[enable_secret_version](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html#google_cloud_secretmanager_v1_services_secret_manager_service_SecretManagerServiceClient_enable_secret_version)(request=request)
    
        print(f"Enabled secret version: {response.name}")

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=secretmanager). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
