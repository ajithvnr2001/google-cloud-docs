---
url: https://docs.cloud.google.com/secret-manager/regional-secrets/create-manage-tags-regional-secrets/
title: Create and manage tags for regional secrets \u00a0|\u00a0 Secret Manager Regional Service Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:30.346694+00:00
---

# Create and manage tags for regional secrets  |  Secret Manager Regional Service Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/regional-secrets/create-manage-tags-regional-secrets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Regional service ](https://docs.cloud.google.com/secret-manager/regional-secrets)
  * [ Guides ](https://docs.cloud.google.com/secret-manager/regional-secrets/regional-secrets-overview)



Send feedback 

#  Create and manage tags for regional secrets Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes how to create and manage tags on regional secrets. You can use tags to group related Secret Manager secrets and store metadata about those resources based on their tags.

## About tags

A tag is a key-value pair that can be attached to a resource within Google Cloud. You can use tags to conditionally allow or deny policies based on whether a resource has a specific tag. For example, you can conditionally grant Identity and Access Management (IAM) roles based on whether a resource has a specific tag. For more information, see [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview).

Tags are attached to resources by creating a tag binding resource that links the value to the Google Cloud resource.

## Required permissions

To get the permissions that you need to manage tags, ask your administrator to grant you the following IAM roles: 

  * [Tag Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`) on the resources the tags are attached to
  * View and manage tags at the organization level: [Organization Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.organizationViewer) (`roles/resourcemanager.organizationViewer`) on the organization 
  * Create, update, and delete tag definitions: [Tag Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagAdmin) (`roles/resourcemanager.tagAdmin`) on the resource you're creating, updating, or deleting tags for 
  * Attach and remove tags from resources: [Tag User ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`) on the tag value and the resources that you are attaching or removing the tag value to 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To attach tags to Secret Manager secrets, you need the [Secret Manager Admin](https://docs.cloud.google.com/secret-manager/docs/access-control#secretmanager.admin) role (`roles/secretmanager.admin`).

## Create tag keys and values

Before you can attach a tag, you need to create a tag and configure its value. For more information, see [Creating a tag](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing) and [Adding a tag value](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#adding_tag_values).

## Add tags during resource creation

You can add tags when you create regional secrets. Doing so lets you provide essential metadata for your resources and allows for better organization, cost tracking, and automated policy application.

### Console

  1. Go to the **Secret Manager** page in the Google Cloud console.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. On the **Secret Manager** page, click the **Regional secrets** tab.
  3. Select the option to create a new regional secret.
  4. Click label_important**Manage tags**.
  5. If your organization doesn't appear in the **Manage tags** panel, click **Select scope for tags** and select your organization or project.
  6. Click **Add tag**.
  7. Select the tag key and tag value from the list. You can filter the list using keywords.
  8. Click **Save**. The **Tags** section is updated with the tags information.
  9. Create your regional secret. The new regional secret is created with the provided tags.



### gcloud

Before using any of the command data below, make the following replacements: 

  * SECRET_ID: the unique identifier of the secret.
  * LOCATION: the location of the secret.
  * TAG_KEY: the permanent ID or namespaced name of the tag key that's attached-for example, `tagKeys/567890123456`.
  * TAG_VALUE: the permanent ID or namespaced name of the tag value that's attached—for example, `tagValues/567890123456`.



Specify multiple tags by separating the tags with a comma, for example, `TAGKEY1=TAGVALUE1,TAGKEY2=TAGVALUE2`.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets create SECRET_ID --location=LOCATION --tags=TAG_KEY=TAG_VALUE

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets create SECRET_ID --location=LOCATION --tags=TAG_KEY=TAG_VALUE

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets create SECRET_ID --location=LOCATION --tags=TAG_KEY=TAG_VALUE

### REST

Before using any of the request data, make the following replacements: 

  * LOCATION: the location of the secret
  * PROJECT_ID: the ID of the project
  * SECRET_ID: the unique identifier of the secret
  * TAGKEY_NAME: the permanent ID or namespaced name of the tag key that's attached—for example, `tagKeys/567890123456`.
  * TAGVALUE_NAME: the permanent ID or namespaced name of the tag value that is attached—for example, `tagValues/567890123456`.



HTTP method and URL: 
    
    
    POST https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets?secretId=SECRET_ID

Request JSON body: 
    
    
    {
      "tags": {
        "TAGKEY_NAME": "TAGVALUE_NAME"
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets?secretId=SECRET_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets?secretId=SECRET_ID" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Secret Manager C# SDK](https://docs.cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-csharp). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.SecretManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.html);
    using System.Collections.Generic;
    
    public class CreateRegionalSecretWithTagsSample
    {
        public Secret CreateRegionalSecretWithTags(
          string projectId = "my-project",
          string locationId = "my-location",
          string secretId = "my-secret",
          string tagKeyName = "tagKey/value",
          string tagValueName = "tagValue/value"
        )
        {
            // Create the Regional Secret Manager Client.
            [SecretManagerServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html) client = new [SecretManagerServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClientBuilder.html)
            {
                Endpoint = $"secretmanager.{locationId}.rep.googleapis.com"
            }.[Build](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClientBuilder.html#Google_Cloud_SecretManager_V1_SecretManagerServiceClientBuilder_Build)();
    
            // Build the parent resource name.
            [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html) location = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, locationId);
    
            // Build the secret.
            Secret secret = new Secret
            {
                Tags =
                {
                    { tagKeyName, tagValueName }
                },
            };
    
            // Call the API.
            Secret createdSecret = client.[CreateSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html#Google_Cloud_SecretManager_V1_SecretManagerServiceClient_CreateSecret_Google_Api_Gax_ResourceNames_LocationName_System_String_Google_Cloud_SecretManager_V1_Secret_Google_Api_Gax_Grpc_CallSettings_)(location, secretId, secret);
            return createdSecret;
        }
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
    
    // createSecretWithTags creates a new regional secret with the given name and tags.
    func createRegionalSecretWithTags(w io.Writer, projectId, locationId, secretId, tagKey, tagValue string) error {
    	parent := fmt.Sprintf("projects/%s/locations/%s", projectId, locationId)
    
    	// Create the client.
    	ctx := context.Background()
    	//Endpoint to send the request to regional server
    	endpoint := fmt.Sprintf("secretmanager.%s.rep.googleapis.com:443", locationId)
    	client, err := secretmanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_NewClient)(ctx, option.WithEndpoint(endpoint))
    	if err != nil {
    		return fmt.Errorf("failed to create secretmanager client: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_Close)()
    
    	// Build the request.
    	req := &secretmanagerpb.CreateSecretRequest{
    		Parent:   parent,
    		SecretId: secretId,
    		Secret: &secretmanagerpb.Secret{
    			Tags: map[string]string{
    				tagKey: tagValue,
    			},
    		},
    	}
    
    	// Call the API.
    	result, err := client.CreateSecret(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to create secret: %w", err)
    	}
    	fmt.Fprintf(w, "Created secret with tags: %s\n", result.Name)
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Secret Manager Java SDK](https://docs.cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-java). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    import com.google.cloud.secretmanager.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.LocationName.html);
    import com.google.cloud.secretmanager.v1.[Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html);
    import com.google.cloud.secretmanager.v1.[SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html);
    import com.google.cloud.secretmanager.v1.[SecretManagerServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceSettings.html);
    import java.io.IOException;
    
    public class CreateRegionalSecretWithTags {
    
      public static void createRegionalSecretWithTags() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
    
        // This is the id of the GCP project
        String projectId = "your-project-id";
        // Location of the secret.
        String locationId = "your-location-id";
        // This is the id of the secret to act on
        String secretId = "your-secret-id";
        // This is the key of the tag to be added
        String tagKey = "your-tag-key";
        // This is the value of the tag to be added
        String tagValue = "your-tag-value";
        createRegionalSecretWithTags(projectId, locationId, secretId, tagKey, tagValue);
      }
    
      // Create a secret with tags.
      public static [Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html) createRegionalSecretWithTags(
           String projectId,
           String locationId,
           String secretId,
           String tagKey,
           String tagValue)
          throws IOException {
    
        // Endpoint to call the regional secret manager sever
        String apiEndpoint = String.format("secretmanager.%s.rep.googleapis.com:443", locationId);
        [SecretManagerServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceSettings.html) secretManagerServiceSettings =
            [SecretManagerServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceSettings.html).newBuilder().setEndpoint(apiEndpoint).build();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html) client = 
            [SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html).create(secretManagerServiceSettings)) {
    
          // Build the parent name from the project.
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.LocationName.html) location = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.LocationName.html).of(projectId, locationId);
    
          // Build the secret to create with tags.
          [Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html) secret =
              [Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html).newBuilder()
                .[putTags](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.Builder.html#com_google_cloud_secretmanager_v1_Secret_Builder_putTags_java_lang_String_java_lang_String_)(tagKey, tagValue)
                .build();
    
          // Create the secret.
          [Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html) createdSecret = client.createSecret(location.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.LocationName.html#com_google_cloud_secretmanager_v1_LocationName_toString__)(), secretId, secret);
          System.out.printf("Created secret with Tags%s\n", createdSecret.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html#com_google_cloud_secretmanager_v1_Secret_getName__)());
          return createdSecret;
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
    // const tagKey = 'tagKeys/281475012216835';
    // const tagValue = 'tagValues/281476592621530';
    const parent = `projects/${projectId}/locations/${locationId}`;
    
    // Imports the library
    const {SecretManagerServiceClient} = require('[@google-cloud/secret-manager](https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/overview.html)');
    
    // Adding the endpoint to call the regional secret manager sever
    const options = {};
    options.apiEndpoint = `secretmanager.${locationId}.rep.googleapis.com`;
    
    // Instantiates a client
    const client = new [SecretManagerServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/overview.html)(options);
    
    async function createRegionalSecretWithTags() {
      const [secret] = await client.createSecret({
        parent: parent,
        secretId: secretId,
        secret: {
          tags: {
            [tagKey]: tagValue,
          },
        },
      });
    
      console.log(`Created secret ${secret.name}`);
    }
    
    createRegionalSecretWithTags();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Secret Manager PHP SDK](https://docs.cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-php). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    // Import the Secret Manager client library.
    use Google\Cloud\SecretManager\V1\CreateSecretRequest;
    use Google\Cloud\SecretManager\V1\Secret;
    use Google\Cloud\SecretManager\V1\Client\SecretManagerServiceClient;
    
    /**
     * @param string $projectId  Your Google Cloud Project ID (e.g. 'my-project')
     * @param string $locationId Your Google Cloud Location ID (e.g. 'us-central1')
     * @param string $secretId   Your secret ID (e.g. 'my-secret')
     * @param string $tagKey     Your tag key (e.g. 'tagKeys/281475012216835')
     * @param string $tagValue   Your tag value (e.g. 'tagValues/281476592621530')
     */
    function create_regional_secret_with_tags(string $projectId, string $locationId, string $secretId, string $tagKey, string $tagValue): void
    {
        // Specify regional endpoint.
        $options = ['apiEndpoint' => "secretmanager.$locationId.rep.googleapis.com"];
    
        // Create the Secret Manager client.
        $client = new SecretManagerServiceClient($options);
    
        // Build the resource name of the parent project.
        $parent = $client->locationName($projectId, $locationId);
    
        $secret = new Secret();
    
        // set the tags.
        $tags = [$tagKey => $tagValue];
        $secret ->setTags($tags);
    
        // Build the request.
        $request = CreateSecretRequest::build($parent, $secretId, $secret);
    
        // Create the secret.
        $newSecret = $client->createSecret($request);
    
        // Print the new secret name.
        printf('Created secret %s with tag', $newSecret->getName());
    }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Secret Manager Python SDK](https://docs.cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-python). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    import argparse
    
    # Import the Secret Manager client library.
    from google.cloud import [secretmanager_v1](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest)
    
    
    def create_regional_secret_with_tags(
        project_id: str,
        location_id: str,
        secret_id: str,
        tag_key: str,
        tag_value: str,
    ) -> secretmanager_v1.Secret:
        """
        Create a new regional secret with the given name and associated tags. A
        secret is a logical wrapper around a collection of secret versions. Secret
        versions hold the actual secret material.
        """
    
        # Endpoint to call the regional Secret Manager API.
        api_endpoint = f"secretmanager.{location_id}.rep.googleapis.com"
    
        # Create the Secret Manager client.
        client = [secretmanager_v1](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest).[SecretManagerServiceClient](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html)(
            client_options={"api_endpoint": api_endpoint},
        )
    
        # Build the resource name of the parent secret.
        parent = f"projects/{project_id}/locations/{location_id}"
    
        # Create the secret.
        response = client.[create_secret](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html#google_cloud_secretmanager_v1_services_secret_manager_service_SecretManagerServiceClient_create_secret)(
            request={
                "parent": parent,
                "secret_id": secret_id,
                "secret": {
                    "tags": {
                        tag_key: tag_value
                    }
                },
            }
        )
    
        # Print the new secret name.
        print(f"Created secret: {response.name}")
    
        return response
    
    

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Secret Manager Ruby SDK](https://docs.cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-ruby). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    require "google/cloud/secret_manager"
    
    ##
    # Create a regional secret with tags
    #
    # @param project_id [String] Your Google Cloud project (e.g. "my-project")
    # @param location_id [String] Your Google Cloud location (e.g. "us-west1")
    # @param secret_id [String] Your secret name (e.g. "my-secret")
    # @param tag_key [String] Your tag key (e.g. "my-tag-key")
    # @param tag_value [String] Your tag value (e.g "my-tag-value")
    #
    def create_regional_secret_with_tags project_id:, location_id:, secret_id:, tag_key:, tag_value:
      # Endpoint for the regional secret manager service.
      api_endpoint = "secretmanager.#{location_id}.rep.googleapis.com"
    
      # Create the Secret Manager client.
      client = Google::Cloud::[SecretManager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager.html).[secret_manager_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager/latest/Google-Cloud-SecretManager.html) do |config|
        config.endpoint = api_endpoint
      end
    
      # Build the resource name of the parent project.
      parent = client.location_path project: project_id, location: location_id
    
      # Create the secret.
      secret = client.create_secret(
        parent:    parent,
        secret_id: secret_id,
        secret: {
          tags: {
            tag_key.name => tag_value.name
          }
        }
      )
    
      # Print the new secret name.
      puts "Created regional secret with tags: #{secret.name}"
    end

## Add tags to existing resources

To add a tag to existing regional secrets, follow these steps:

### Console

  1. Go to the **Secret Manager** page in the Google Cloud console.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. Select the regional secret that you want to attach a tag to.
  3. Click label_important**Tags**.
  4. If your organization doesn't appear in the **Tags** panel, click **Select scope**. Select your organization and click **Open**.
  5. Click **Add tag**.
  6. Select the tag key and tag value from the list. You can filter the list using keywords.
  7. Click **Save**.
  8. In the **Confirm** dialog, click **Confirm** to attach the tag.

A notification confirms that your tags were updated.




### gcloud

To attach a tag to a regional secret, you must create a tag binding resource by using the `gcloud resource-manager tags bindings create` command:

Before using any of the command data below, make the following replacements: 

  * `TAGVALUE_NAME`: the permanent ID or namespaced name of the tag value that's attached—for example, `tagValues/567890123456`.
  * `RESOURCE_ID` is the full ID of the resource, including the API domain name to identify the type of resource (`//secretmanager.googleapis.com/`). For example, to attach a tag to `projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID`, the full ID is `//secretmanager.googleapis.com/projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID`.
  * `LOCATION`: the location of your resource. If you're attaching a tag to a global resource, such as a folder or project, omit this flag. If you're attaching a tag to a regional or zonal resource, you must specify the location—for example, `us-central1` (region) or `us-central1-a` (zone).



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud resource-manager tags bindings create \
        --tag-value=TAGVALUE_NAME \
        --parent=RESOURCE_ID \
        --location=LOCATION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud resource-manager tags bindings create `
        --tag-value=TAGVALUE_NAME `
        --parent=RESOURCE_ID `
        --location=LOCATION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud resource-manager tags bindings create ^
        --tag-value=TAGVALUE_NAME ^
        --parent=RESOURCE_ID ^
        --location=LOCATION

### Node.js

To run this code, first [set up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup) and [install the Secret Manager Node.js SDK](https://docs.cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-nodejs). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'my-project';
    // const locationId = 'my-location';
    // const secretId = 'my-secret';
    // const tagValue = 'tagValues/281476592621530';
    const parent = `projects/${projectId}/locations/${locationId}`;
    
    // Imports the library
    const {SecretManagerServiceClient} = require('[@google-cloud/secret-manager](https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/overview.html)');
    const {TagBindingsClient} = require('[@google-cloud/resource-manager](https://docs.cloud.google.com/nodejs/docs/reference/resource-manager/latest/overview.html)').v3;
    
    // Adding the endpoint to call the regional
    const options = {};
    const bindingOptions = {};
    options.apiEndpoint = `secretmanager.${locationId}.rep.googleapis.com`;
    bindingOptions.apiEndpoint = `${locationId}-cloudresourcemanager.googleapis.com`;
    
    // Instantiates a client
    const client = new [SecretManagerServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/overview.html)(options);
    const resourcemanagerClient = new [TagBindingsClient](https://docs.cloud.google.com/nodejs/docs/reference/resource-manager/latest/overview.html)(bindingOptions);
    
    async function bindTagsToRegionalSecret() {
      const [secret] = await client.createSecret({
        parent: parent,
        secretId: secretId,
      });
    
      console.log(`Created secret ${secret.name}`);
    
      const [operation] = await resourcemanagerClient.createTagBinding({
        tagBinding: {
          parent: `//secretmanager.googleapis.com/${secret.name}`,
          tagValue: tagValue,
        },
      });
      const [response] = await operation.promise();
      console.log('Created Tag Binding', response.name);
    }
    
    bindTagsToRegionalSecret();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Secret Manager PHP SDK](https://docs.cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-php). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    // Import the Secret Manager client library.
    use Google\Cloud\SecretManager\V1\CreateSecretRequest;
    use Google\Cloud\SecretManager\V1\Secret;
    use Google\Cloud\SecretManager\V1\Client\SecretManagerServiceClient;
    use Google\Cloud\ResourceManager\V3\Client\TagBindingsClient;
    use Google\Cloud\ResourceManager\V3\CreateTagBindingRequest;
    use Google\Cloud\ResourceManager\V3\TagBinding;
    
    /**
     * @param string $projectId  Your Google Cloud Project ID (e.g. 'my-project')
     * @param string $locationId Your Google Cloud Location ID (e.g. 'us-central1')
     * @param string $secretId   Your secret ID (e.g. 'my-secret')
     * @param string $tagValue   Your tag value (e.g. 'tagValues/281476592621530')
     */
    function bind_tags_to_regional_secret(string $projectId, string $locationId, string $secretId, string $tagValue): void
    {
        // Specify regional endpoint.
        $options = ['apiEndpoint' => "secretmanager.$locationId.rep.googleapis.com"];
    
        // Create the Secret Manager client.
        $client = new SecretManagerServiceClient($options);
    
        // Build the resource name of the parent project.
        $parent = $client->locationName($projectId, $locationId);
    
        $secret = new Secret();
    
        // Build the request.
        $request = CreateSecretRequest::build($parent, $secretId, $secret);
    
        // Create the secret.
        $newSecret = $client->createSecret($request);
    
        // Print the new secret name.
        printf('Created secret %s' . PHP_EOL, $newSecret->getName());
    
        // Specify regional endpoint.
        $tagBindOptions = ['apiEndpoint' => "$locationId-cloudresourcemanager.googleapis.com"];
        $tagBindingsClient = new TagBindingsClient($tagBindOptions);
        $tagBinding = (new TagBinding())
            ->setParent('//secretmanager.googleapis.com/' . $newSecret->getName())
            ->setTagValue($tagValue);
    
        // Build the request.
        $request = (new CreateTagBindingRequest())
            ->setTagBinding($tagBinding);
    
        // Create the tag binding.
        $operationResponse = $tagBindingsClient->createTagBinding($request);
        $operationResponse->pollUntilComplete();
    
        // Check if the operation succeeded.
        if ($operationResponse->operationSucceeded()) {
            printf('Tag binding created for secret %s with tag value %s' . PHP_EOL, $newSecret->getName(), $tagValue);
        } else {
            $error = $operationResponse->getError();
            printf('Error in creating tag binding: %s' . PHP_EOL, $error->getMessage());
        }
    }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Secret Manager Python SDK](https://docs.cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-python). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    import argparse
    
    # Import the Secret Manager and Resource Manager client library.
    from google.cloud import [resourcemanager_v3](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest)
    from google.cloud import secretmanager
    
    
    def bind_tags_to_regional_secret(
        project_id: str,
        location_id: str,
        secret_id: str,
        tag_value: str,
    ) -> resourcemanager_v3.TagBinding:
        """
        Create a new regional secret with the given name, and then bind an existing
        tag to it. A secret is a logical wrapper around a collection of secret
        versions. Secret versions hold the actual secret material.
        """
    
        # Endpoint to call the regional secret manager sever
        api_endpoint = f"secretmanager.{location_id}.rep.googleapis.com"
    
        # Create the Secret Manager client.
        client = secretmanager.[SecretManagerServiceClient](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html)(
            client_options={"api_endpoint": api_endpoint},
        )
    
        # Build the resource name of the parent project.
        parent = f"projects/{project_id}/locations/{location_id}"
    
        # Create the secret.
        secret_response = client.[create_secret](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html#google_cloud_secretmanager_v1_services_secret_manager_service_SecretManagerServiceClient_create_secret)(
            request={
                "parent": parent,
                "secret_id": secret_id,
            }
        )
    
        # Print the new secret name.
        print(f"Created secret: {secret_response.name}")
    
        # Endpoint to call the regional secret manager sever
        resource_manager_api_endpoint = f"{location_id}-cloudresourcemanager.googleapis.com"
    
        # Create the resource manager client
        resource_manager_client = [resourcemanager_v3](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest).[TagBindingsClient](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest/google.cloud.resourcemanager_v3.services.tag_bindings.TagBindingsClient.html)(
            client_options={"api_endpoint": resource_manager_api_endpoint},
        )
    
        # Create the tag binding
        request = [resourcemanager_v3](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest).[CreateTagBindingRequest](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest/google.cloud.resourcemanager_v3.types.CreateTagBindingRequest.html)(
            tag_binding=[resourcemanager_v3](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest).[TagBinding](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest/google.cloud.resourcemanager_v3.types.TagBinding.html)(
                parent=f"//secretmanager.googleapis.com/{secret_response.name}",
                tag_value=f"{tag_value}",
            ),
        )
    
        # Create the tag binding
        operation = resource_manager_client.[create_tag_binding](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest/google.cloud.resourcemanager_v3.services.tag_bindings.TagBindingsClient.html#google_cloud_resourcemanager_v3_services_tag_bindings_TagBindingsClient_create_tag_binding)(request=request)
    
        # Wait for the operation to complete
        response = operation.result()
    
        # Print the tag binding
        print(f"Created tag binding: {response.name}")
    
        return response
    
    

## List tags attached to resources

You can view a list of tag bindings directly attached to or inherited by the regional secret.

### Console

  1. Go to the **Secret Manager** page in the Google Cloud console.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. Tags are displayed in the **Tags** column of the secret.



### gcloud

To get a list of tag bindings attached to a resource, use the `gcloud resource-manager tags bindings list` command:

Before using any of the command data below, make the following replacements: 

  * `RESOURCE_ID` is the full ID of the resource, including the API domain name to identify the type of resource (`//secretmanager.googleapis.com/`). For example, to attach a tag to `projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID`, the full ID is `//secretmanager.googleapis.com/projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID`.
  * `LOCATION`: the location of your resource. If you're viewing a tag attached to a global resource, such as a folder or project, omit this flag. If you're viewing a tag attached to a regional or zonal resource, you must specify the location—for example, `us-central1` (region) or `us-central1-a` (zone).



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud resource-manager tags bindings list \
        --parent=RESOURCE_ID \
        --location=LOCATION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud resource-manager tags bindings list `
        --parent=RESOURCE_ID `
        --location=LOCATION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud resource-manager tags bindings list ^
        --parent=RESOURCE_ID ^
        --location=LOCATION

You should receive a response similar to the following:
    
    
      name: tagBindings/%2F%2Fcloudresourcemanager.googleapis.com%2Fprojects%2F7890123456/tagValues/567890123456
        tagValue: tagValues/567890123456
        resource: //secretmanager.googleapis.com/projects/project-abc/secrets/secret-xyz
    

## Detach tags from resources

You can detach tags that have been directly attached to a regional secret. Inherited tags can be overridden by attaching a tag with the same key and a different value, but they can't be detached.

### Console

  1. Go to the **Secret Manager** page in the Google Cloud console.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. Select the regional secret that you want to remove a tag from.
  3. Click label_important**Tags**.
  4. In the **Tags** panel, next to the tag you want to detach, click delete**Delete item**.
  5. Click **Save**.
  6. In the **Confirm** dialog, click **Confirm** to detach the tag.



A notification confirms that your tags were updated.

### gcloud

To delete a tag binding, use the `gcloud resource-manager tags bindings delete` command:

Before using any of the command data below, make the following replacements: 

  * `TAGVALUE_NAME`: the permanent ID or namespaced name of the tag value that's attached—for example, `tagValues/567890123456`.
  * `RESOURCE_ID` is the full ID of the resource, including the API domain name to identify the type of resource (`//secretmanager.googleapis.com/`). For example, to attach a tag to `projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID`, the full ID is `//secretmanager.googleapis.com/projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID`.
  * `LOCATION`: the location of your resource. If you're attaching a tag to a global resource, such as a folder or project, omit this flag. If you're attaching a tag to a regional or zonal resource, you must specify the location—for example, `us-central1` (region) or `us-central1-a` (zone).



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud resource-manager tags bindings delete \
        --tag-value=TAGVALUE_NAME \
        --parent=RESOURCE_ID \
        --location=LOCATION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud resource-manager tags bindings delete `
        --tag-value=TAGVALUE_NAME `
        --parent=RESOURCE_ID `
        --location=LOCATION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud resource-manager tags bindings delete ^
        --tag-value=TAGVALUE_NAME ^
        --parent=RESOURCE_ID ^
        --location=LOCATION

## Delete tag keys and values

When removing a tag key or value definition, ensure that the tag is detached from the regional secret. You must delete existing tag attachments, called tag bindings, before deleting the tag definition itself. For more information, see [Deleting tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#deleting).

## Identity and Access Management conditions and tags

You can use tags and IAM conditions to conditionally grant role bindings to users in your hierarchy. Changing or deleting the tag attached to a resource can remove user access to that resource if an IAM policy with conditional role bindings has been applied. For more information, see [Identity and Access Management conditions and tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#iam_conditions_and_tags).

## What's next

  * See the other [services that support tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-supported-services).
  * See [Tags and access control](https://docs.cloud.google.com/iam/docs/tags-access-control) to learn how to use tags with IAM.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
