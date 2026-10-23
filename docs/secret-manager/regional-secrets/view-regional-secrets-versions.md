---
url: https://docs.cloud.google.com/secret-manager/regional-secrets/view-regional-secrets-versions/
title: List regional secret versions and view version details \u00a0|\u00a0 Secret Manager Regional Service Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:52:10.236314+00:00
---

# List regional secret versions and view version details  |  Secret Manager Regional Service Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/regional-secrets/view-regional-secrets-versions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Regional service ](https://docs.cloud.google.com/secret-manager/regional-secrets)
  * [ Guides ](https://docs.cloud.google.com/secret-manager/regional-secrets/regional-secrets-overview)



Send feedback 

#  List regional secret versions and view version details Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to retrieve a list of all the different versions of a secret that have been created over time and view the metadata of a specific secret version.

## Required roles

To get the permissions that you need to list secret versions and view version details, ask your administrator to grant you the [Secret Manager Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.viewer) (`roles/secretmanager.viewer`) IAM role on the secret, project, folder, or organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## List a secret's versions

Listing a secret's versions is useful in the following ways:

  * You can see see how a secret has changed over time, who made the changes, and when. This is required for auditing and compliance.

  * You can roll back to a previous, known-good version if a secret is accidentally updated or compromised.

  * You can identify versions that are no longer in use and can be safely deleted.

  * You can troubleshoot issues. For example, if an application is experiencing problems, you can examine previous versions of a secret to see if a change to the secret is the cause.




To list all the versions of a secret, use one of the following methods:

### Console

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. On the **Secret Manager** page, click the **Regional secrets** tab.

  3. Click a secret to access its versions.

The versions belonging to the secret are displayed in the **Versions** table.




### gcloud

Before using any of the command data below, make the following replacements: 

  * SECRET_ID: the ID of the secret
  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the secret



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets versions list SECRET_ID --location=LOCATION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets versions list SECRET_ID --location=LOCATION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets versions list SECRET_ID --location=LOCATION

The response contains the secret. 

### REST

Before using any of the request data, make the following replacements: 

  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the secret
  * PROJECT_ID: the Google Cloud project ID
  * SECRET_ID: the ID of the secret



HTTP method and URL: 
    
    
    GET https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID/versions

Request JSON body: 
    
    
    {}
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID/versions"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID/versions" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "versions": [
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID/versions/VERSION_ID",
          "createTime": "2024-09-04T06:41:57.859674Z",
          "state": "ENABLED",
          "etag": "\"1621457b3c1459\""
        }
      ],
      "totalSize": 1
    }
    

### Go

To run this code, first [set up a Go development environment](https://docs.cloud.google.com/go/docs/setup) and [install the Secret Manager Go SDK](https://docs.cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-go). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	secretmanager "cloud.google.com/go/secretmanager/apiv1"
    	"cloud.google.com/go/secretmanager/apiv1/secretmanagerpb"
    	"google.golang.org/api/iterator"
    	"google.golang.org/api/option"
    )
    
    // listSecretVersions lists all secret versions in the given secret and their
    // metadata.
    func ListRegionalSecretVersions(w io.Writer, projectId, locationId, secretId string) error {
    	// parent := "projects/my-project/locations/my-location/secrets/my-secret"
    
    	// Create the client.
    	ctx := context.Background()
    	//Endpoint to send the request to regional server
    	endpoint := fmt.Sprintf("secretmanager.%s.rep.googleapis.com:443", locationId)
    	client, err := secretmanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_NewClient)(ctx, option.WithEndpoint(endpoint))
    
    	if err != nil {
    		return fmt.Errorf("failed to create regional secretmanager client: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_Close)()
    
    	parent := fmt.Sprintf("projects/%s/locations/%s/secrets/%s", projectId, locationId, secretId)
    	// Build the request.
    	req := &secretmanagerpb.ListSecretVersionsRequest{
    		Parent: parent,
    	}
    
    	// Call the API.
    	it := client.ListSecretVersions(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    
    		if err != nil {
    			return fmt.Errorf("failed to list regional secret versions: %w", err)
    		}
    
    		fmt.Fprintf(w, "Found regional secret version %s with state %s\n",
    			resp.Name, resp.State)
    	}
    
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Secret Manager Java SDK](https://docs.cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-java). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    import com.google.cloud.secretmanager.v1.[SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html);
    import com.google.cloud.secretmanager.v1.[SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html).[ListSecretVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.ListSecretVersionsPagedResponse.html);
    import com.google.cloud.secretmanager.v1.[SecretManagerServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceSettings.html);
    import com.google.cloud.secretmanager.v1.[SecretName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html);
    import java.io.IOException;
    
    public class ListRegionalSecretVersions {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
    
        // Your GCP project ID.
        String projectId = "your-project-id";
        // Location of the secret.
        String locationId = "your-location-id";
        // Resource ID of the secret.
        String secretId = "your-secret-id";
        listRegionalSecretVersions(projectId, locationId, secretId);
      }
    
      // List all secret versions for a secret.
      public static [ListSecretVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.ListSecretVersionsPagedResponse.html) listRegionalSecretVersions(
          String projectId, String locationId, String secretId)
          throws IOException {
    
        // Endpoint to call the regional secret manager sever
        String apiEndpoint = String.format("secretmanager.%s.rep.googleapis.com:443", locationId);
        [SecretManagerServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceSettings.html) secretManagerServiceSettings =
            [SecretManagerServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceSettings.html).newBuilder().setEndpoint(apiEndpoint).build();
    
        // Initialize the client that will be used to send requests. This client only needs to be
        // created once, and can be reused for multiple requests.
        try ([SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html) client = 
            [SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html).create(secretManagerServiceSettings)) {
          // Build the parent name.
          [SecretName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html) secretName = 
              [SecretName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html).[ofProjectLocationSecretName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html#com_google_cloud_secretmanager_v1_SecretName_ofProjectLocationSecretName_java_lang_String_java_lang_String_java_lang_String_)(projectId, locationId, secretId);
    
          // Get all versions.
          [ListSecretVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.ListSecretVersionsPagedResponse.html) pagedResponse = client.listSecretVersions(secretName);
    
          // List all versions and their state.
          pagedResponse
              .iterateAll()
              .forEach(
                  version -> {
                    System.out.printf("Regional secret version %s, %s\n", 
                        version.getName(), version.getState());
                  });
    
          return pagedResponse;
        }
      }
    }

### Node.js

To run this code, first [set up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup) and [install the Secret Manager Node.js SDK](https://docs.cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-nodejs). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'my-project';
    // const locationId = 'my-location';
    // const secretId = 'my-secret';
    
    const parent = `projects/${projectId}/locations/${locationId}/secrets/${secretId}`;
    
    // Imports the Secret Manager library
    const {SecretManagerServiceClient} = require('[@google-cloud/secret-manager](https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/overview.html)');
    
    // Adding the endpoint to call the regional secret manager sever
    const options = {};
    options.apiEndpoint = `secretmanager.${locationId}.rep.googleapis.com`;
    
    // Instantiates a client
    const client = new [SecretManagerServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/overview.html)(options);
    
    async function listRegionalSecretVersions() {
      const [versions] = await client.listSecretVersions({
        parent: parent,
      });
    
      versions.forEach(version => {
        console.log(`${version.name}: ${version.state}`);
      });
    }
    
    listRegionalSecretVersions();

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Secret Manager Python SDK](https://docs.cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-python). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    # Import the Secret Manager client library.
    from google.cloud import [secretmanager_v1](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest)
    
    
    def list_regional_secret_versions(
        project_id: str, location_id: str, secret_id: str
    ) -> None:
        """
        Lists all secret versions in the given secret and their metadata.
        """
    
        # Endpoint to call the regional secret manager sever.
        api_endpoint = f"secretmanager.{location_id}.rep.googleapis.com"
    
        # Create the Secret Manager client.
        client = [secretmanager_v1](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest).[SecretManagerServiceClient](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html)(
            client_options={"api_endpoint": api_endpoint},
        )
    
        # Build the resource name of the parent secret.
        parent = f"projects/{project_id}/locations/{location_id}/secrets/{secret_id}"
    
        # List all secret versions.
        for version in client.[list_secret_versions](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html#google_cloud_secretmanager_v1_services_secret_manager_service_SecretManagerServiceClient_list_secret_versions)(request={"parent": parent}):
            print(f"Found secret version: {version.name}")
    
    

## Get details about a secret version

This process lets you view the metadata of a secret version such as the version ID, creation date and time, encryption details, and status. Viewing the metadata of a secret version means accessing information about the secret version, but not the actual secret value itself. To view the secret value, see [Access a regional secret version](https://docs.cloud.google.com/secret-manager/regional-secrets/access-secret-version-rs).

To view a secret version's metadata, use one of the following methods:

### Console

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. On the **Secret Manager** page, click the **Regional secrets** tab.

  3. Click a secret to access its versions.

The versions belonging to the secret are displayed in the **Versions** table. For each version, the version ID and its metadata is also displayed in the table.




### gcloud

Before using any of the command data below, make the following replacements: 

  * VERSION_ID: the ID of the secret version
  * SECRET_ID: the ID of the secret
  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the secret



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets versions describe VERSION_ID --secret=SECRET_ID --location=LOCATION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets versions describe VERSION_ID --secret=SECRET_ID --location=LOCATION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets versions describe VERSION_ID --secret=SECRET_ID --location=LOCATION

The response contains the secret. 

### REST

Before using any of the request data, make the following replacements: 

  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the secret
  * PROJECT_ID: the Google Cloud project ID
  * SECRET_ID: the ID of the secret
  * VERSION_ID: the ID of the secret version



HTTP method and URL: 
    
    
    GET https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID/versions/VERSION_ID

Request JSON body: 
    
    
    {}
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID/versions/VERSION_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID/versions/VERSION_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID/versions/VERSION_ID",
      "createTime": "2024-09-04T06:41:57.859674Z",
      "state": "ENABLED",
      "etag": "\"1621457b3c1459\""
    }
    

### Go

To run this code, first [set up a Go development environment](https://docs.cloud.google.com/go/docs/setup) and [install the Secret Manager Go SDK](https://docs.cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-go). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	secretmanager "cloud.google.com/go/secretmanager/apiv1"
    	"cloud.google.com/go/secretmanager/apiv1/secretmanagerpb"
    	"google.golang.org/api/option"
    )
    
    // getSecretVersion gets information about the given secret version. It does not
    // include the payload data.
    func GetRegionalSecretVersion(w io.Writer, projectId, locationId, secretId, versionId string) error {
    	// name := "projects/my-project/locations/my-location/secrets/my-secret/versions/5"
    	// name := "projects/my-project/locations/my-location/secrets/my-secret/versions/latest"
    
    	// Create the client.
    	ctx := context.Background()
    	//Endpoint to send the request to regional server
    	endpoint := fmt.Sprintf("secretmanager.%s.rep.googleapis.com:443", locationId)
    	client, err := secretmanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_NewClient)(ctx, option.WithEndpoint(endpoint))
    
    	if err != nil {
    		return fmt.Errorf("failed to create regional secretmanager client: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_Close)()
    
    	name := fmt.Sprintf("projects/%s/locations/%s/secrets/%s/versions/%s", projectId, locationId, secretId, versionId)
    	// Build the request.
    	req := &secretmanagerpb.GetSecretVersionRequest{
    		Name: name,
    	}
    
    	// Call the API.
    	result, err := client.GetSecretVersion(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to get regional secret version: %w", err)
    	}
    
    	fmt.Fprintf(w, "Found regional secret version %s with state %s\n",
    		result.Name, result.State)
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Secret Manager Java SDK](https://docs.cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-java). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    import com.google.cloud.secretmanager.v1.[SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html);
    import com.google.cloud.secretmanager.v1.[SecretManagerServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceSettings.html);
    import com.google.cloud.secretmanager.v1.[SecretVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretVersion.html);
    import com.google.cloud.secretmanager.v1.[SecretVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretVersionName.html);
    import java.io.IOException;
    
    public class GetRegionalSecretVersion {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
    
        // Your GCP project ID.
        String projectId = "your-project-id";
        // Location of the secret.
        String locationId = "your-location-id";
        // Resource ID of the secret.
        String secretId = "your-secret-id";
        // Version of the Secret ID you want to retrieve.
        String versionId = "your-version-id";
        getRegionalSecretVersion(projectId, locationId, secretId, versionId);
      }
    
      // Get an existing secret version.
      public static [SecretVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretVersion.html) getRegionalSecretVersion(
          String projectId, String locationId, String secretId, String versionId)
          throws IOException {
    
        // Endpoint to call the regional secret manager sever
        String apiEndpoint = String.format("secretmanager.%s.rep.googleapis.com:443", locationId);
        [SecretManagerServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceSettings.html) secretManagerServiceSettings =
            [SecretManagerServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceSettings.html).newBuilder().setEndpoint(apiEndpoint).build();
    
        // Initialize the client that will be used to send requests. This client only needs to be
        // created once, and can be reused for multiple requests.
        try ([SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html) client = 
            [SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html).create(secretManagerServiceSettings)) {
          // Build the name from the version.
          [SecretVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretVersionName.html) secretVersionName = 
              [SecretVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretVersionName.html).[ofProjectLocationSecretSecretVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretVersionName.html#com_google_cloud_secretmanager_v1_SecretVersionName_ofProjectLocationSecretSecretVersionName_java_lang_String_java_lang_String_java_lang_String_java_lang_String_)(
              projectId, locationId, secretId, versionId);
    
          // Create the secret.
          [SecretVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretVersion.html) version = client.getSecretVersion(secretVersionName);
          System.out.printf("Regional secret version %s, state %s\n", 
              version.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretVersion.html#com_google_cloud_secretmanager_v1_SecretVersion_getName__)(), version.[getState](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretVersion.html#com_google_cloud_secretmanager_v1_SecretVersion_getState__)());
    
          return version;
        }
      }
    }

### Node.js

To run this code, first [set up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup) and [install the Secret Manager Node.js SDK](https://docs.cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-nodejs). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    
    // const projectId = 'my-project';
    // const locationId = 'my-location';
    // const secretId = 'my-secret';
    // const versionId = 'my-version';
    
    const name = `projects/${projectId}/locations/${locationId}/secrets/${secretId}/versions/${version}`;
    
    // Imports the Secret Manager library
    const {SecretManagerServiceClient} = require('[@google-cloud/secret-manager](https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/overview.html)');
    
    // Adding the endpoint to call the regional secret manager sever
    const options = {};
    options.apiEndpoint = `secretmanager.${locationId}.rep.googleapis.com`;
    
    // Instantiates a client
    const client = new [SecretManagerServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/overview.html)(options);
    
    async function getRegionalSecretVersion() {
      const [version] = await client.getSecretVersion({
        name: name,
      });
    
      console.info(`Found secret ${version.name} with state ${version.state}`);
    }
    
    getRegionalSecretVersion();

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Secret Manager Python SDK](https://docs.cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-python). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    # Import the Secret Manager client library.
    from google.cloud import [secretmanager_v1](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest)
    
    
    def get_regional_secret_version(
        project_id: str,
        location_id: str,
        secret_id: str,
        version_id: str,
    ) -> secretmanager_v1.GetSecretVersionRequest:
        """
        Gets information about the given secret version. It does not include the
        payload data.
        """
    
        # Endpoint to call the regional secret manager sever.
        api_endpoint = f"secretmanager.{location_id}.rep.googleapis.com"
    
        # Create the Secret Manager client.
        client = [secretmanager_v1](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest).[SecretManagerServiceClient](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html)(
            client_options={"api_endpoint": api_endpoint},
        )
    
        # Build the resource name of the secret version.
        name = f"projects/{project_id}/locations/{location_id}/secrets/{secret_id}/versions/{version_id}"
    
        # Get the secret version.
        response = client.[get_secret_version](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html#google_cloud_secretmanager_v1_services_secret_manager_service_SecretManagerServiceClient_get_secret_version)(request={"name": name})
    
        # Print information about the secret version.
        state = response.state.name
        print(f"Got secret version {response.name} with state {state}")
    
        return response
    
    

## What's next

  * [Assign an alias to a secret version](https://docs.cloud.google.com/secret-manager/regional-secrets/assign-alias-to-secret-version-rs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
