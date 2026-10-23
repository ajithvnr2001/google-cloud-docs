---
url: https://docs.cloud.google.com/secret-manager/docs/samples/secretmanager-create-regional-secret-with-annotations/
title: Create a regional secret with annotations \u00a0|\u00a0 Secret Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:41:09.314134+00:00
---

# Create a regional secret with annotations  |  Secret Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/docs/samples/secretmanager-create-regional-secret-with-annotations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Samples ](https://docs.cloud.google.com/secret-manager/docs/samples)



#  Create a regional secret with annotations Stay organized with collections  Save and categorize content based on your preferences. 

Create a regional secret with annotations

## Code sample

### C#

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.SecretManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.html);
    using System.Collections.Generic;
    
    public class CreateRegionalSecretWithAnnotationsSample
    {
        public Secret CreateRegionalSecretWithAnnotations(
          string projectId = "my-project",
          string locationId = "my-location",
          string secretId = "my-secret",
          string annotationKey = "my-annotation-key",
          string annotationValue = "my-annotation-value"
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
                Annotations =
              {
                  { annotationKey, annotationValue }
              },
            };
    
            // Call the API.
            Secret createdSecret = client.[CreateSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html#Google_Cloud_SecretManager_V1_SecretManagerServiceClient_CreateSecret_Google_Api_Gax_ResourceNames_LocationName_System_String_Google_Cloud_SecretManager_V1_Secret_Google_Api_Gax_Grpc_CallSettings_)(location, secretId, secret);
            return createdSecret;
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
    	"google.golang.org/api/option"
    )
    
    // createRegionalSecretWithAnnotations creates a new secret with the given name and annotations.
    func createRegionalSecretWithAnnotations(w io.Writer, projectId, locationId, secretId string) error {
    	// parent := "projects/my-project"
    	// id := "my-secret"
    
    	annotationKey := "annotationkey"
    	annotationValue := "annotationvalue"
    
    	ctx := context.Background()
    
    	//Endpoint to send the request to regional server
    	endpoint := fmt.Sprintf("secretmanager.%s.rep.googleapis.com:443", locationId)
    	client, err := secretmanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_NewClient)(ctx, option.WithEndpoint(endpoint))
    	if err != nil {
    		return fmt.Errorf("failed to create secretmanager client: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_Close)()
    
    	parent := fmt.Sprintf("projects/%s/locations/%s", projectId, locationId)
    
    	// Build the request.
    	req := &secretmanagerpb.CreateSecretRequest{
    		Parent:   parent,
    		SecretId: secretId,
    		Secret: &secretmanagerpb.Secret{
    			Annotations: map[string]string{
    				annotationKey: annotationValue,
    			},
    		},
    	}
    
    	result, err := client.CreateSecret(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to create secret: %w", err)
    	}
    	fmt.Fprintf(w, "Created secret with annotations: %s\n", result.Name)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.secretmanager.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.LocationName.html);
    import com.google.cloud.secretmanager.v1.[Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html);
    import com.google.cloud.secretmanager.v1.[SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html);
    import com.google.cloud.secretmanager.v1.[SecretManagerServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceSettings.html);
    import java.io.IOException;
    
    public class CreateRegionalSecretWithAnnotations {
    
      public static void createRegionalSecretWithAnnotations() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
    
        // This is the id of the GCP project
        String projectId = "your-project-id";
        // Location of the secret.
        String locationId = "your-location-id";
        // This is the id of the secret to act on
        String secretId = "your-secret-id";
        // This is the key of the annotation to be added
        String annotationKey = "your-annotation-key";
        // This is the value of the annotation to be added
        String annotationValue = "your-annotation-value";
        createRegionalSecretWithAnnotations(
            projectId, locationId, secretId, annotationKey, annotationValue
        );
      }
    
      // Create a secret with annotations.
      public static [Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html) createRegionalSecretWithAnnotations(
            String projectId,
            String locationId,
            String secretId,
            String annotationKey,
            String annotationValue
      ) throws IOException {
    
        // Endpoint to call the regional secret manager sever
        String apiEndpoint = String.format("secretmanager.%s.rep.googleapis.com:443", locationId);
        [SecretManagerServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceSettings.html) secretManagerServiceSettings =
            [SecretManagerServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceSettings.html).newBuilder().setEndpoint(apiEndpoint).build();
    
        // Initialize the client that will be used to send requests. This client only needs to be
        // created once, and can be reused for multiple requests.
        try ([SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html) client = 
            [SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html).create(secretManagerServiceSettings)) {
    
          // Build the parent name from the project.
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.LocationName.html) location = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.LocationName.html).of(projectId, locationId);
    
          // Build the secret to create with labels.
          [Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html) secret =
              [Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html).newBuilder()
                    .[putAnnotations](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.Builder.html#com_google_cloud_secretmanager_v1_Secret_Builder_putAnnotations_java_lang_String_java_lang_String_)(annotationKey, annotationValue)
                    .build();
    
          // Create the secret.
          [Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html) createdSecret = client.createSecret(location.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.LocationName.html#com_google_cloud_secretmanager_v1_LocationName_toString__)(), secretId, secret);
          System.out.printf("Created secret %s\n", createdSecret.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html#com_google_cloud_secretmanager_v1_Secret_getName__)());
          return createdSecret;
        }
      }
    }

### Node.js

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'my-project'
    // const locationId = 'locationId';
    // const secretId = 'my-secret';
    // const annotationKey = 'exampleannotationkey';
    // const annotationValue = 'exampleannotationvalue';
    
    const parent = `projects/${projectId}/locations/${locationId}`;
    
    // Imports the Secret Manager library
    const {SecretManagerServiceClient} = require('[@google-cloud/secret-manager](https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/overview.html)');
    
    // Adding the endpoint to call the regional secret manager sever
    const options = {};
    options.apiEndpoint = `secretmanager.${locationId}.rep.googleapis.com`;
    // Instantiates a client
    const client = new [SecretManagerServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/overview.html)(options);
    
    async function createRegionalSecretWithAnnotations() {
      const [secret] = await client.createSecret({
        parent: parent,
        secretId: secretId,
        secret: {
          annotations: {
            [annotationKey]: annotationValue,
          },
        },
      });
    
      console.log(`Created secret ${secret.name}`);
    }
    
    createRegionalSecretWithAnnotations();

### PHP

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Import the Secret Manager client library.
    use Google\Cloud\SecretManager\V1\CreateSecretRequest;
    use Google\Cloud\SecretManager\V1\Secret;
    use Google\Cloud\SecretManager\V1\Client\SecretManagerServiceClient;
    
    /**
     * @param string $projectId       Your Google Cloud Project ID (e.g. 'my-project')
     * @param string $locationId      Your Google Cloud Location ID (e.g. 'us-central1')
     * @param string $secretId        Your secret ID (e.g. 'my-secret')
     * @param string $annotationKey   Your annotation key (e.g. 'annotation-key')
     * @param string $annotationValue Your annotation value (e.g. 'annotation-value')
     */
    function create_regional_secret_with_annotations(string $projectId, string $locationId, string $secretId, string $annotationKey, string $annotationValue): void
    {
        // Specify regional endpoint.
        $options = ['apiEndpoint' => "secretmanager.$locationId.rep.googleapis.com"];
    
        // Create the Secret Manager client.
        $client = new SecretManagerServiceClient($options);
    
        // Build the resource name of the parent project.
        $parent = $client->locationName($projectId, $locationId);
    
        $secret = new Secret();
    
        // set the annotations.
        $annotations = [$annotationKey => $annotationValue];
        $secret->setAnnotations($annotations);
    
        // Build the request.
        $request = CreateSecretRequest::build($parent, $secretId, $secret);
    
        // Create the secret.
        $newSecret = $client->createSecret($request);
    
        // Print the new secret name.
        printf('Created secret %s with annotations', $newSecret->getName());
    }

### Python

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    import typing
    
    # Import the Secret Manager client library.
    from google.cloud import [secretmanager_v1](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest)
    
    
    def create_regional_secret_with_annotations(
        project_id: str,
        location_id: str,
        secret_id: str,
        annotations: typing.Dict[str, str],
    ) -> secretmanager_v1.Secret:
        """
        Create a new secret with the given name. A secret is a logical wrapper
        around a collection of secret versions. Secret versions hold the actual
        secret material.
        """
    
        # Endpoint to call the regional secret manager sever
        api_endpoint = f"secretmanager.{location_id}.rep.googleapis.com"
    
        # Create the Secret Manager client.
        client = [secretmanager_v1](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest).[SecretManagerServiceClient](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html)(
            client_options={"api_endpoint": api_endpoint},
        )
    
        # Build the resource name of the parent project.
        parent = f"projects/{project_id}/locations/{location_id}"
    
        # Create the secret.
        response = client.[create_secret](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html#google_cloud_secretmanager_v1_services_secret_manager_service_SecretManagerServiceClient_create_secret)(
            request={
                "parent": parent,
                "secret_id": secret_id,
                "secret": {"annotations": annotations},
            }
        )
    
        # Print the new secret name.
        print(f"Created secret: {response.name}")
    
        return response
    
    

### Ruby

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # project_id       = "YOUR-GOOGLE-CLOUD-PROJECT"  # (e.g. "my-project")
    # location_id      = "YOUR-GOOGLE-CLOUD-LOCATION" # (e.g. "us-west1")
    # secret_id        = "YOUR-SECRET-ID"             # (e.g. "my-secret")
    # annotation_key   = "YOUR-ANNOTATION-KEY"        # (e.g. "my-annotation-key")
    # annotation_value = "YOUR-ANNOTATION-VALUE"      # (e.g. "my-annotation-value")
    
    # Require the Secret Manager client library.
    require "google/cloud/secret_manager"
    
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
        annotations: {
          annotation_key => annotation_value
        }
      }
    )
    
    # Print the new secret name.
    puts "Created regional secret with annotations: #{secret.name}"

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=secretmanager). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
