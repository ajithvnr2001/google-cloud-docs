---
url: https://docs.cloud.google.com/secret-manager/docs/samples/secretmanager-list-secret-versions-with-filter/
title: List secret versions containing a filter \u00a0|\u00a0 Secret Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:18:18.278838+00:00
---

# List secret versions containing a filter  |  Secret Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/docs/samples/secretmanager-list-secret-versions-with-filter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Samples ](https://docs.cloud.google.com/secret-manager/docs/samples)



#  List secret versions containing a filter Stay organized with collections  Save and categorize content based on your preferences. 

Shows how to list all secret versions and metadata for a secret with a specified filter.

## Code sample

### Go

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	secretmanager "cloud.google.com/go/secretmanager/apiv1"
    	"cloud.google.com/go/secretmanager/apiv1/secretmanagerpb"
    	"google.golang.org/api/iterator"
    )
    
    // listSecretVersionsWithFilter lists all filter-matching secret versions in the given
    // secret and their metadata.
    func listSecretVersionsWithFilter(w io.Writer, parent string, filter string) error {
    	// parent := "projects/my-project/secrets/my-secret"
    	// Follow https://cloud.google.com/secret-manager/docs/filtering
    	// for filter syntax and examples.
    	// filter := "create_time>2021-01-01T00:00:00Z"
    
    	// Create the client.
    	ctx := context.Background()
    	client, err := secretmanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create secretmanager client: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_Close)()
    
    	// Build the request.
    	req := &secretmanagerpb.ListSecretVersionsRequest{
    		Parent: parent,
    		Filter: filter,
    	}
    
    	// Call the API.
    	it := client.ListSecretVersions(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    
    		if err != nil {
    			return fmt.Errorf("failed to list secret versions: %w", err)
    		}
    
    		fmt.Fprintf(w, "Found secret version %s with state %s\n",
    			resp.Name, resp.State)
    	}
    
    	return nil
    }
    

### Java

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.secretmanager.v1.[ListSecretVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.ListSecretVersionsRequest.html);
    import com.google.cloud.secretmanager.v1.[SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html);
    import com.google.cloud.secretmanager.v1.[SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html).[ListSecretVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.ListSecretVersionsPagedResponse.html);
    import com.google.cloud.secretmanager.v1.[SecretName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html);
    import java.io.IOException;
    
    public class ListSecretVersionsWithFilter {
    
      public static void listSecretVersions() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String secretId = "your-secret-id";
        // Follow https://cloud.google.com/secret-manager/docs/filtering
        // for filter syntax and examples.
        String filter = "create_time>2021-01-01T00:00:00Z";
        listSecretVersions(projectId, secretId, filter);
      }
    
      // List all secret versions for a secret.
      public static void listSecretVersions(String projectId, String secretId, String filter)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html) client = [SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html).create()) {
          // Build the parent name.
          [SecretName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html) secretName = [SecretName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html).of(projectId, secretId);
    
          // Get filtered versions.
          [ListSecretVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.ListSecretVersionsRequest.html) request =
              [ListSecretVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.ListSecretVersionsRequest.html).newBuilder()
                  .setParent(secretName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html#com_google_cloud_secretmanager_v1_SecretName_toString__)())
                  .setFilter(filter)
                  .build();
    
          [ListSecretVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.ListSecretVersionsPagedResponse.html) pagedResponse = client.listSecretVersions(request);
    
          // List all versions and their state.
          pagedResponse
              .iterateAll()
              .forEach(
                  version -> {
                    System.out.printf("Secret version %s, %s\n", version.getName(), version.getState());
                  });
        }
      }
    }

### Python

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def list_secret_versions_with_filter(
        project_id: str, secret_id: str, filter_str: str = "state:ENABLED"
    ) -> None:
        """
        List all secret versions in the given secret and their metadata.
    
        Args:
          project_id: Parent project id
          secret_id: Parent secret id
          filter_str: Secret version filter, constructing according to
                      https://cloud.google.com/secret-manager/docs/filtering
        """
    
        # Import the Secret Manager client library.
        from google.cloud import secretmanager
    
        # Create the Secret Manager client.
        client = secretmanager.[SecretManagerServiceClient](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html)()
    
        # Build the resource name of the parent secret.
        parent = client.[secret_path](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html#google_cloud_secretmanager_v1_services_secret_manager_service_SecretManagerServiceClient_secret_path)(project_id, secret_id)
    
        # List all secret versions.
        for version in client.[list_secret_versions](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html#google_cloud_secretmanager_v1_services_secret_manager_service_SecretManagerServiceClient_list_secret_versions)(
            request={"parent": parent, "filter": filter_str}
        ):
            print(f"Found secret version: {version.name}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=secretmanager). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
