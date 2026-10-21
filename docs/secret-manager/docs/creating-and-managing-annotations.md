---
url: https://docs.cloud.google.com/secret-manager/docs/creating-and-managing-annotations/
title: Create and manage annotations \u00a0|\u00a0 Secret Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:38:32.708607+00:00
---

# Create and manage annotations  |  Secret Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/docs/creating-and-managing-annotations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secret-manager/docs/overview)



Send feedback 

#  Create and manage annotations Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to add annotations to a secret and how to edit and view these annotations.

## Overview

You can use annotations to store custom metadata about a secret. For example, you might want to annotate a secret with the path it'll be mounted at. Annotations can be helpful in the following ways:

  * To categorize secrets based on their purpose, environment (development, staging, production), or sensitivity level. This makes it easier to search, filter, and organize secrets within Secret Manager.

  * To indicate the specific format or structure of the secret's value, helping the workload interpret it correctly.

  * To provide hints about how the secret should be used or any special considerations for its handling.




For example, if you have a secret containing a database password, you can add annotations such as the following:

  * `environment:production`

  * `purpose:database_access`

  * `owner:database_team`




These annotations make it easy to identify the secret's purpose, its environment, and who's responsible for it. Additionally, a workload accessing this secret can use the annotations to confirm that it's using the right password for the production environment.

Annotations are not the same as labels. Labels are used for sorting, filtering, and grouping resources, whereas annotations are used to store arbitrary, non-identifying metadata on a secret. There is a restriction of characters and character length when specifying metadata in a label. The metadata in an annotation can be small or large, structured or unstructured, and can include characters not permitted by labels.

## Required roles

  * Adding annotations on a secret and updating annotations requires the Secret Manager Admin role (`roles/secretmanager.admin`) on the secret, project, folder, or organization.

  * Viewing annotations requires the Secret Manager Viewer role (`roles/secretmanager.viewer`) on the secret, project, folder, or organization.




Identity and Access Management (IAM) roles can't be granted on a secret version. See [Access control with IAM](https://docs.cloud.google.com/secret-manager/docs/access-control) for more information.

## Add annotations to a secret

You can add annotations at the time of creating a new secret or updating an existing secret. The metadata in an annotation is stored as key-value pairs. To add annotations, use one of the following methods:

### Console

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. On the **Secret Manager** page, click **Create secret**.

  3. On the **Create secret** page, enter a name for the secret in the **Name** field.

  4. Enter a value for the secret (for example, `abcd1234`). You can also upload a text file containing the secret value using the **Upload file** option. This action automatically creates the secret version.

  5. Go to the **Annotations** section, and then click **Add annotation**.

  6. Enter the key and corresponding value.

  7. Click **Create secret**.




### gcloud

Before using any of the command data below, make the following replacements: 

  * SECRET_ID: the ID of the secret
  * KEY: the annotation key
  * VALUE: the corresponding value of the annotation key



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets create SECRET_ID \
        --set-annotations= KEY1=VAL1,KEY2=VAL2

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets create SECRET_ID `
        --set-annotations= KEY1=VAL1,KEY2=VAL2

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets create SECRET_ID ^
        --set-annotations= KEY1=VAL1,KEY2=VAL2

The response contains the secret and the annotations. 

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID
  * SECRET_ID: the ID of the secret
  * KEY: the annotation key
  * VALUE: the corresponding value of the annotation key



HTTP method and URL: 
    
    
    PATCH https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets/SECRET_ID?updateMask=annotations

Request JSON body: 
    
    
    {'annotations': {'KEY1': 'VALUE1', 'KEY2': 'VALUE2' }}
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets/SECRET_ID?updateMask=annotations"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets/SECRET_ID?updateMask=annotations" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID",
      "createTime": "2024-09-02T07:14:00.281541Z",
      "etag": "\"16211dcd99c386\"",
      "annotations": {
        "key1": "value1",
        "key2": "value2"
      }
    }
    
    

### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Secret Manager C# SDK](https://docs.cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-csharp). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.SecretManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.html);
    using System.Collections.Generic;
    
    public class CreateSecretWithAnnotationsSample
    {
        public Secret CreateSecretWithAnnotations(
          string projectId = "my-project", string secretId = "my-secret", string annotationKey = "my-annotation-key", string annotationValue = "my-annotation-value")
        {
            // Create the client.
            [SecretManagerServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html) client = [SecretManagerServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html#Google_Cloud_SecretManager_V1_SecretManagerServiceClient_Create)();
    
            // Build the parent resource name.
            [ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html) projectName = new [ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)(projectId);
    
            // Build the secret.
            Secret secret = new Secret
            {
                Replication = new [Replication](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.Replication.html)
                {
                    Automatic = new Replication.Types.Automatic(),
                },
                Annotations =
                {
                  { annotationKey, annotationValue }
                },
            };
    
            // Call the API.
            Secret createdSecret = client.[CreateSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html#Google_Cloud_SecretManager_V1_SecretManagerServiceClient_CreateSecret_Google_Api_Gax_ResourceNames_LocationName_System_String_Google_Cloud_SecretManager_V1_Secret_Google_Api_Gax_Grpc_CallSettings_)(projectName, secretId, secret);
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
    )
    
    // createSecretWithAnnotations creates a new secret with the given name and annotations.
    func createSecretWithAnnotations(w io.Writer, parent, secretId string) error {
    	// parent := "projects/my-project"
    	// id := "my-secret"
    
    	annotationKey := "annotationkey"
    	annotationValue := "annotationvalue"
    
    	ctx := context.Background()
    	client, err := secretmanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create secretmanager client: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_Close)()
    
    	// Build the request.
    	req := &secretmanagerpb.CreateSecretRequest{
    		Parent:   parent,
    		SecretId: secretId,
    		Secret: &secretmanagerpb.Secret{
    			Replication: &secretmanagerpb.Replication{
    				Replication: &secretmanagerpb.Replication_Automatic_{
    					Automatic: &secretmanagerpb.Replication_Automatic{},
    				},
    			},
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

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Secret Manager Java SDK](https://docs.cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-java). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    import com.google.cloud.secretmanager.v1.[ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.ProjectName.html);
    import com.google.cloud.secretmanager.v1.[Replication](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Replication.html);
    import com.google.cloud.secretmanager.v1.[Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html);
    import com.google.cloud.secretmanager.v1.[SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html);
    import java.io.IOException;
    
    public class CreateSecretWithAnnotations {
    
      public static void createSecretWithAnnotations() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
    
        // This is the id of the GCP project
        String projectId = "your-project-id";
        // This is the id of the secret to act on
        String secretId = "your-secret-id";
        // This is the key of the annotation to be added
        String annotationKey = "your-annotation-key";
        // This is the value of the annotation to be added
        String annotationValue = "your-annotation-value";
        createSecretWithAnnotations(projectId, secretId, annotationKey, annotationValue);
      }
    
      // Create a secret with annotations.
      public static [Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html) createSecretWithAnnotations(
           String projectId,
           String secretId,
           String annotationKey,
           String annotationValue
      ) throws IOException {
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html) client = [SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html).create()) {
    
          // Build the name.
          [ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.ProjectName.html) projectName = [ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.ProjectName.html).of(projectId);
    
          // Build the secret to create with labels.
          [Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html) secret =
              [Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html).newBuilder()
                      .[setReplication](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.Builder.html#com_google_cloud_secretmanager_v1_Secret_Builder_setReplication_com_google_cloud_secretmanager_v1_Replication_)(
                      [Replication](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Replication.html).newBuilder()
                          .setAutomatic([Replication](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Replication.html).Automatic.newBuilder().build())
                          .build())
                      .[putAnnotations](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.Builder.html#com_google_cloud_secretmanager_v1_Secret_Builder_putAnnotations_java_lang_String_java_lang_String_)(annotationKey, annotationValue)
                  .build();
    
          // Create the secret.
          [Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html) createdSecret = client.createSecret(projectName, secretId, secret);
          System.out.printf("Created secret %s\n", createdSecret.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html#com_google_cloud_secretmanager_v1_Secret_getName__)());
          return createdSecret;
        }
      }
    }

### Node.js

To run this code, first [set up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup) and [install the Secret Manager Node.js SDK](https://docs.cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-nodejs). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const parent = 'projects/my-project';
    // const secretId = 'my-secret';
    // const annotationKey = 'exampleannotationkey';
    // const annotationValue = 'exampleannotationvalue';
    
    // Imports the Secret Manager library
    const {SecretManagerServiceClient} = require('[@google-cloud/secret-manager](https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/overview.html)');
    
    // Instantiates a client
    const client = new [SecretManagerServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/overview.html)();
    
    async function createSecretWithAnnotations() {
      const [secret] = await client.createSecret({
        parent: parent,
        secretId: secretId,
        secret: {
          replication: {
            automatic: {},
          },
          annotations: {
            [annotationKey]: annotationValue,
          },
        },
      });
    
      console.log(`Created secret ${secret.name}`);
    }
    
    createSecretWithAnnotations();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Secret Manager PHP SDK](https://docs.cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-php). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    // Import the Secret Manager client library.
    use Google\Cloud\SecretManager\V1\CreateSecretRequest;
    use Google\Cloud\SecretManager\V1\Replication;
    use Google\Cloud\SecretManager\V1\Replication\Automatic;
    use Google\Cloud\SecretManager\V1\Secret;
    use Google\Cloud\SecretManager\V1\Client\SecretManagerServiceClient;
    
    /**
     * @param string $projectId       Your Google Cloud Project ID (e.g. 'my-project')
     * @param string $secretId        Your secret ID (e.g. 'my-secret')
     * @param string $annotationKey   Your annotation key (e.g. 'annotation-key')
     * @param string $annotationValue Your annotation value (e.g. 'annotation-value')
     */
    function create_secret_with_annotations(string $projectId, string $secretId, string $annotationKey, string $annotationValue): void
    {
        // Create the Secret Manager client.
        $client = new SecretManagerServiceClient();
    
        // Build the resource name of the parent project.
        $parent = $client->projectName($projectId);
    
        $secret = new Secret([
            'replication' => new Replication([
                'automatic' => new Automatic(),
            ]),
        ]);
    
        // set the annoation.
        $annotation = [$annotationKey => $annotationValue];
        $secret->setAnnotations($annotation);
    
        // Build the request.
        $request = CreateSecretRequest::build($parent, $secretId, $secret);
    
        // Create the secret.
        $newSecret = $client->createSecret($request);
    
        // Print the new secret name.
        printf('Created secret %s with annotations', $newSecret->getName());
    }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Secret Manager Python SDK](https://docs.cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-python). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    import argparse
    import typing
    
    # Import the Secret Manager client library.
    from google.cloud import secretmanager
    
    
    def create_secret_with_annotations(
        project_id: str,
        secret_id: str,
        annotations: typing.Dict[str, str],
    ) -> secretmanager.Secret:
        """
        Create a new secret with the given name. A secret is a logical wrapper
        around a collection of secret versions. Secret versions hold the actual
        secret material.
        """
    
        # Create the Secret Manager client.
        client = secretmanager.[SecretManagerServiceClient](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html)()
    
        # Build the resource name of the parent project.
        parent = f"projects/{project_id}"
    
        # Create the secret.
        response = client.[create_secret](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html#google_cloud_secretmanager_v1_services_secret_manager_service_SecretManagerServiceClient_create_secret)(
            request={
                "parent": parent,
                "secret_id": secret_id,
                "secret": {
                    "replication": {"automatic": {}},
                    "annotations": annotations,
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
    # Create a secret with annotation.
    #
    # @param project_id [String] Your Google Cloud project (e.g. "my-project")
    # @param secret_id [String] Your secret name (e.g. "my-secret")
    # @param annotation_key [String] Your annotation key (e.g. "my-annotation-key")
    # @param annotation_value [String] Your annotation value (e.g. "my-annotation-value")
    #
    def create_secret_with_annotations project_id:, secret_id:, annotation_key:, annotation_value:
      # Create a Secret Manager client.
      client = Google::Cloud::[SecretManager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager.html).[secret_manager_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager/latest/Google-Cloud-SecretManager.html)
    
      # Build the resource name of the parent project.
      parent = client.project_path project: project_id
    
      # Create the secret.
      secret = client.create_secret(
        parent:    parent,
        secret_id: secret_id,
        secret:    {
          replication: {
            automatic: {}
          },
          annotations: {
            annotation_key => annotation_value
          }
        }
      )
    
      # Print the new secret name.
      puts "Created secret: #{secret.name}"
    end

To add annotations to an existing secret, see the [Edit annotations](https://docs.cloud.google.com/secret-manager/docs/creating-and-managing-annotations#editannotations) section of this document.

Annotation keys have the following requirements:

  * Keys must be unique to a secret. You can't repeat a key in the same secret.

  * Keys must be between 1 and 63 characters long.

  * Keys must have a UTF-8 encoding of maximum 128 bytes.

  * Keys must begin and end with an alphanumeric character.

  * Keys can have dashes, underscores, and dots in between the alphanumerics characters.

  * The total size of annotation keys and values must be less than 16KiB.




## Edit annotations

To edit annotations, use one of the following methods:

### Console

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. Locate the secret in the list and click the more_vert**Actions** menu associated with that secret. In the **Actions** menu, click **Edit**.

  3. On the **Edit secret** page, go to the **Annotations** section. Here you can change the value of an existing annotation, delete the annotation, or add a new annotation.

  4. After you have made your changes, click **Update secret**.




### gcloud

#### Edit existing annotations

Before using any of the command data below, make the following replacements: 

  * SECRET_ID: the ID of the secret
  * KEY: the annotation key
  * VALUE: the corresponding value of the annotation key



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets update SECRET_ID --update-annotations= KEY=VAL

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets update SECRET_ID --update-annotations= KEY=VAL

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets update SECRET_ID --update-annotations= KEY=VAL

The response edits the secret and the annotations. 

#### Remove a specific annotation

To remove annotations, use the following command:
    
    
    gcloud secrets update SECRET_ID --remove-annotations= KEY=VAL

#### Clear all annotations

To clear all annotations, use the following command:
    
    
    gcloud secrets update SECRET_ID --clear-annotations

### REST

To clear all annotations, use the following command:

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID
  * SECRET_ID: the ID of the secret



HTTP method and URL: 
    
    
    PATCH https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets/SECRET_ID?updateMask=annotations

Request JSON body: 
    
    
    {'annotations': {}}
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets/SECRET_ID?updateMask=annotations"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets/SECRET_ID?updateMask=annotations" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID",
      "createTime": "2024-09-02T07:14:00.281541Z",
      "etag": "\"16211dd90b37e7\""
    }
    
    

### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Secret Manager C# SDK](https://docs.cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-csharp). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.SecretManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.html);
    using [Google.Protobuf.Collections](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    
    public class EditSecretAnnotationsSample
    {
        public Secret EditSecretAnnotations(
          string projectId = "my-project", string secretId = "my-secret", string annotationKey = "my-annotation-key", string annotationValue = "my-annotation-value")
        {
            // Create the client.
            [SecretManagerServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html) client = [SecretManagerServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html#Google_Cloud_SecretManager_V1_SecretManagerServiceClient_Create)();
    
            // Build the secretName with the fields.
            [SecretName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretName.html) secretName = new [SecretName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretName.html)(projectId, secretId);
    
            // Get the exisitng secret.
            Secret secret = client.[GetSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html#Google_Cloud_SecretManager_V1_SecretManagerServiceClient_GetSecret_Google_Cloud_SecretManager_V1_GetSecretRequest_Google_Api_Gax_Grpc_CallSettings_)(secretName);
    
            // Edit the Secret annotations
            secret.[Annotations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.Secret.html#Google_Cloud_SecretManager_V1_Secret_Annotations)[annotationKey] = annotationValue;
    
            // Build the field mask.
            [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html) fieldMask = [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html).[FromString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html#Google_Protobuf_WellKnownTypes_FieldMask_FromString_System_String_)("annotations");
    
            // Call the API.
            Secret updatedSecret = client.[UpdateSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html#Google_Cloud_SecretManager_V1_SecretManagerServiceClient_UpdateSecret_Google_Cloud_SecretManager_V1_Secret_Google_Protobuf_WellKnownTypes_FieldMask_Google_Api_Gax_Grpc_CallSettings_)(secret, fieldMask);
            return updatedSecret;
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
    	"google.golang.org/genproto/protobuf/field_mask"
    )
    
    // editSecretAnnotation updates the annotations about an existing secret.
    // If the annotation key exists, it updates the annotation, otherwise it creates a new one.
    func editSecretAnnotation(w io.Writer, secretName string) error {
    	// name := "projects/my-project/secrets/my-secret"
    
    	annotationKey := "annotationkey"
    	annotationValue := "updatedannotationvalue"
    
    	ctx := context.Background()
    	client, err := secretmanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create secretmanager client: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_Close)()
    
    	// Build the request to get the secret.
    	req := &secretmanagerpb.GetSecretRequest{
    		Name: secretName,
    	}
    
    	result, err := client.GetSecret(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to get secret: %w", err)
    	}
    
    	annotations := result.Annotations
    
    	annotations[annotationKey] = annotationValue
    
    	// Build the request to update the secret.
    	update_req := &secretmanagerpb.UpdateSecretRequest{
    		Secret: &secretmanagerpb.Secret{
    			Name:        secretName,
    			Annotations: annotations,
    		},
    		UpdateMask: &field_mask.FieldMask{
    			Paths: []string{"annotations"},
    		},
    	}
    
    	update_result, err := client.UpdateSecret(ctx, update_req)
    	if err != nil {
    		return fmt.Errorf("failed to update secret: %w", err)
    	}
    	fmt.Fprintf(w, "Updated secret: %s\n", update_result.Name)
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Secret Manager Java SDK](https://docs.cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-java). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    import com.google.cloud.secretmanager.v1.[Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html);
    import com.google.cloud.secretmanager.v1.[SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html);
    import com.google.cloud.secretmanager.v1.[SecretName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import com.google.protobuf.util.[FieldMaskUtil](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.FieldMaskUtil.html);
    import java.io.IOException;
    import java.util.HashMap;
    import java.util.Map;
    
    public class EditSecretAnnotations {
    
      public static void editSecretAnnotations() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
    
        // This is the id of the GCP project
        String projectId = "your-project-id";
        // This is the id of the secret to act on
        String secretId = "your-secret-id";
        // This is the key of the annotation to be added/updated
        String annotationKey = "your-annotation-key";
        // This is the value of the annotation to be added/updated
        String annotationValue = "your-annotation-value";
        editSecretAnnotations(projectId, secretId, annotationKey, annotationValue);
      }
    
      // Update an existing secret, by creating a new annotation or updating an existing annotation.
      public static [Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html) editSecretAnnotations(
           String projectId,
           String secretId,
           String annotationKey,
           String annotationValue
      ) throws IOException {
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html) client = [SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html).create()) {
          // Build the name.
          [SecretName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html) secretName = [SecretName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html).of(projectId, secretId);
    
          // Get the existing secret
          [Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html) existingSecret = client.getSecret(secretName);
    
          Map<String, String> existingAnnotationsMap = 
                          new HashMap<String, String>(existingSecret.[getAnnotationsMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html#com_google_cloud_secretmanager_v1_Secret_getAnnotationsMap__)());
    
          // Add a new annotation key and value.
          existingAnnotationsMap.put(annotationKey, annotationValue);
    
          // Build the updated secret.
          [Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html) secret =
              [Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html).newBuilder()
                  .setName(secretName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html#com_google_cloud_secretmanager_v1_SecretName_toString__)())
                  .[putAllAnnotations](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.Builder.html#com_google_cloud_secretmanager_v1_Secret_Builder_putAllAnnotations_java_util_Map_java_lang_String_java_lang_String__)(existingAnnotationsMap)
                  .build();
    
          // Build the field mask.
          [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) fieldMask = [FieldMaskUtil](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.FieldMaskUtil.html).fromString("annotations");
    
          // Update the secret.
          [Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html) updatedSecret = client.updateSecret(secret, fieldMask);
          System.out.printf("Updated secret %s\n", updatedSecret.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html#com_google_cloud_secretmanager_v1_Secret_getName__)());
    
          return updatedSecret;
        }
      }
    }

### Node.js

To run this code, first [set up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup) and [install the Secret Manager Node.js SDK](https://docs.cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-nodejs). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const name = 'projects/my-project/secrets/my-secret';
    // const annotationKey = 'updatedannotationkey';
    // const annotationValue = 'updatedannotationvalue';
    
    // Imports the Secret Manager library
    const {SecretManagerServiceClient} = require('[@google-cloud/secret-manager](https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/overview.html)');
    
    // Instantiates a client
    const client = new [SecretManagerServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/overview.html)();
    
    async function getSecret() {
      const [secret] = await client.getSecret({
        name: name,
      });
    
      return secret;
    }
    
    async function editSecretAnnotations() {
      const oldSecret = await getSecret();
      oldSecret.annotations[annotationKey] = annotationValue;
      const [secret] = await client.updateSecret({
        secret: {
          name: name,
          annotations: oldSecret.annotations,
        },
        updateMask: {
          paths: ['annotations'],
        },
      });
    
      console.info(`Updated secret ${secret.name}`);
    }
    
    editSecretAnnotations();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Secret Manager PHP SDK](https://docs.cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-php). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    // Import the Secret Manager client library.
    use Google\Cloud\SecretManager\V1\Client\SecretManagerServiceClient;
    use Google\Cloud\SecretManager\V1\GetSecretRequest;
    use Google\Cloud\SecretManager\V1\UpdateSecretRequest;
    use Google\Protobuf\FieldMask;
    
    /**
     * @param string $projectId       Your Google Cloud Project ID (e.g. 'my-project')
     * @param string $secretId        Your secret ID (e.g. 'my-secret')
     * @param string $annotationKey   Your annotation key (e.g. 'annotation-key')
     * @param string $annotationValue Your annotation value (e.g. 'annotation-value')
     */
    function edit_secret_annotations(string $projectId, string $secretId, string $annotationKey, string $annotationValue): void
    {
        // Create the Secret Manager client.
        $client = new SecretManagerServiceClient();
    
        // Build the resource name of the parent project.
        $name = $client->secretName($projectId, $secretId);
    
        // Build the request.
        $request = GetSecretRequest::build($name);
    
        // get the secret.
        $getSecret = $client->getSecret($request);
    
        // get the annotations
        $annotations = $getSecret->getAnnotations();
    
        // update the annotation - need to create a new annotations map with the updated values
        $newAnnotations = [];
        foreach ($annotations as $key => $value) {
            $newAnnotations[$key] = $value;
        }
        $newAnnotations[$annotationKey] = $annotationValue;
        $getSecret->setAnnotations($newAnnotations);
    
        // set the field mask
        $fieldMask = new FieldMask();
        $fieldMask->setPaths(['annotations']);
    
        // build the secret
        $request = new UpdateSecretRequest();
        $request->setSecret($getSecret);
        $request->setUpdateMask($fieldMask);
    
        // update the secret
        $updateSecret = $client->updateSecret($request);
    
        // print the updated secret
        printf('Updated secret %s annotations' . PHP_EOL, $updateSecret->getName());
    }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Secret Manager Python SDK](https://docs.cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-python). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    import argparse
    from typing import Dict
    
    # Import the Secret Manager client library.
    from google.cloud import secretmanager
    
    
    def edit_secret_annotations(
        project_id: str, secret_id: str, new_annotations: Dict[str, str]
    ) -> secretmanager.UpdateSecretRequest:
        """
        Create or update a annotation on an existing secret.
        """
    
        # Create the Secret Manager client.
        client = secretmanager.[SecretManagerServiceClient](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html)()
    
        # Build the resource name of the secret.
        name = client.[secret_path](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html#google_cloud_secretmanager_v1_services_secret_manager_service_SecretManagerServiceClient_secret_path)(project_id, secret_id)
    
        # Get the secret.
        response = client.[get_secret](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html#google_cloud_secretmanager_v1_services_secret_manager_service_SecretManagerServiceClient_get_secret)(request={"name": name})
    
        annotations = response.annotations
    
        # Update the annotations
        for annotation_key in new_annotations:
            annotations[annotation_key] = new_annotations[annotation_key]
    
        # Update the secret.
        secret = {"name": name, "annotations": annotations}
        update_mask = {"paths": ["annotations"]}
        response = client.[update_secret](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html#google_cloud_secretmanager_v1_services_secret_manager_service_SecretManagerServiceClient_update_secret)(
            request={"secret": secret, "update_mask": update_mask}
        )
    
        # Print the new secret name.
        print(f"Updated secret: {response.name}")
    
        return response
    
    

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Secret Manager Ruby SDK](https://docs.cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-ruby). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    require "google/cloud/secret_manager"
    
    ##
    # Edits a secret annotations.
    #
    # @param project_id [String] Your Google Cloud project (e.g. "my-project")
    # @param secret_id [String] Your secret name (e.g. "my-secret")
    # @param annotation_key [String] Your annotation key (e.g. "my-annotation-key")
    # @param annotation_value [String] Your annotation value (e.g. "my-annotation-value")
    #
    def edit_secret_annotations project_id:, secret_id:, annotation_key:, annotation_value:
      # Create a Secret Manager client.
      client = Google::Cloud::[SecretManager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager.html).[secret_manager_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager/latest/Google-Cloud-SecretManager.html)
    
      # Build the resource name of the secret.
      name = client.secret_path project: project_id, secret: secret_id
    
      # Get the existing secret.
      existing_secret = client.get_secret name: name
    
      # Get the existing secret's annotations.
      existing_secret_annotations = existing_secret.annotations.to_h
    
      # Add a new annotation key and value.
      existing_secret_annotations[annotation_key] = annotation_value
    
      # Updates the secret.
      secret = client.update_secret(
        secret: {
          name: name,
          annotations: existing_secret_annotations
        },
        update_mask: {
          paths: ["annotations"]
        }
      )
    
      # Print the updated secret name and annotations.
      puts "Updated secret: #{secret.name}"
      puts "New updated annotations: #{secret.annotations}"
    end

## View annotations

To view annotations attached to a secret, use one of the following methods:

### Console

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. On the **Secret Manager** page, click on the secret whose annotations you want to view.

  3. The secret details page opens. Click the **Overview** tab. Here you can see the annotations attached to the secret. The keys are listed on the left column while the values are displayed on the right column.




### gcloud

Before using any of the command data below, make the following replacements: 

  * SECRET_ID: the ID of the secret



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets describe SECRET_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets describe SECRET_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets describe SECRET_ID

The response contains the secret and the annotations. 

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID
  * SECRET_ID: the ID of the secret



HTTP method and URL: 
    
    
    GET https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets/SECRET_ID

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
         "https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets/SECRET_ID"

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
        -Uri "https://secretmanager.googleapis.com/v1/projects/PROJECT_ID/secrets/SECRET_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID",
      "createTime": "2024-09-02T07:14:00.281541Z",
      "etag": "\"16211dcd99c386\"",
      "annotations": {
        "key1": "value1",
        "key2": "value2"
      }
    }
    
    

### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Secret Manager C# SDK](https://docs.cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-csharp). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.SecretManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.html);
    using [Google.Protobuf.Collections](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using System;
    
    public class ViewSecretAnnotationsSample
    {
        public Secret ViewSecretAnnotations(
          string projectId = "my-project", string secretId = "my-secret")
        {
            // Create the client.
            [SecretManagerServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html) client = [SecretManagerServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html#Google_Cloud_SecretManager_V1_SecretManagerServiceClient_Create)();
    
            // Build the resource name.
            [SecretName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretName.html) secretName = new [SecretName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretName.html)(projectId, secretId);
    
            // Fetch the secret.
            Secret secret = client.[GetSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html#Google_Cloud_SecretManager_V1_SecretManagerServiceClient_GetSecret_Google_Cloud_SecretManager_V1_GetSecretRequest_Google_Api_Gax_Grpc_CallSettings_)(secretName);
    
            // Get the secret's annotations.
            MapField<string, string> secretAnnotations = secret.[Annotations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.Secret.html#Google_Cloud_SecretManager_V1_Secret_Annotations);
    
            // Print the annotations.
            foreach (var annotation in secret.[Annotations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.Secret.html#Google_Cloud_SecretManager_V1_Secret_Annotations))
            {
                Console.WriteLine($"Annotation Key: {annotation.Key}, Annotation Value: {annotation.[Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Value.html)}");
            }
            return secret;
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
    )
    
    // viewSecretAnnotations gets annotations with the given secret.
    func viewSecretAnnotations(w io.Writer, secretName string) error {
    	// name := "projects/my-project/secrets/my-secret"
    
    	ctx := context.Background()
    	client, err := secretmanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create secretmanager client: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_Close)()
    
    	// Build the request.
    	req := &secretmanagerpb.GetSecretRequest{
    		Name: secretName,
    	}
    
    	result, err := client.GetSecret(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to get secret: %w", err)
    	}
    
    	annotations := result.Annotations
    	fmt.Fprintf(w, "Found secret %s\n", result.Name)
    
    	for key, value := range annotations {
    		fmt.Fprintf(w, "Annotations key %s : Annotations Value %s", key, value)
    	}
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Secret Manager Java SDK](https://docs.cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-java). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    import com.google.cloud.secretmanager.v1.[Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html);
    import com.google.cloud.secretmanager.v1.[SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html);
    import com.google.cloud.secretmanager.v1.[SecretName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html);
    import java.io.IOException;
    import java.util.Map;
    
    public class ViewSecretAnnotations {
    
      public static void viewSecretAnnotations() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
    
        // This is the id of the GCP project
        String projectId = "your-project-id";
        // This is the id of the secret whose annotations to view
        String secretId = "your-secret-id";
        viewSecretAnnotations(projectId, secretId);
      }
    
      // View the annotations of an existing secret.
      public static Map<String, String> viewSecretAnnotations(
          String projectId,
          String secretId
      ) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html) client = [SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html).create()) {
          // Build the name.
          [SecretName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html) secretName = [SecretName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html).of(projectId, secretId);
    
          // Create the secret.
          [Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html) secret = client.getSecret(secretName);
    
          Map<String, String> annotations = secret.[getAnnotationsMap](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html#com_google_cloud_secretmanager_v1_Secret_getAnnotationsMap__)();
    
          System.out.printf("Secret %s \n", secret.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html#com_google_cloud_secretmanager_v1_Secret_getName__)());
    
          for (Map.Entry<String, String> annotation : annotations.entrySet()) {
            System.out.printf("Annotation key : %s, Annotation Value : %s\n", 
                annotation.getKey(), annotation.getValue());
          }
    
          return secret.getAnnotationsMap();
        }
      }
    }

### Node.js

To run this code, first [set up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup) and [install the Secret Manager Node.js SDK](https://docs.cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-nodejs). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const parent = 'projects/my-project/secrets/my-secret';
    
    // Imports the Secret Manager library
    const {SecretManagerServiceClient} = require('[@google-cloud/secret-manager](https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/overview.html)');
    
    // Instantiates a client
    const client = new [SecretManagerServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/overview.html)();
    
    async function viewSecretAnnotations() {
      const [secret] = await client.getSecret({
        name: name,
      });
    
      for (const key in secret.annotations) {
        console.log(`${key} : ${secret.annotations[key]}`);
      }
    }
    
    viewSecretAnnotations();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Secret Manager PHP SDK](https://docs.cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-php). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    // Import the Secret Manager client library.
    use Google\Cloud\SecretManager\V1\Client\SecretManagerServiceClient;
    use Google\Cloud\SecretManager\V1\GetSecretRequest;
    
    /**
     * @param string $projectId Your Google Cloud Project ID (e.g. 'my-project')
     * @param string $secretId  Your secret ID (e.g. 'my-secret')
     */
    function view_secret_annotations(string $projectId, string $secretId): void
    {
        // Create the Secret Manager client.
        $client = new SecretManagerServiceClient();
    
        // Build the resource name of the parent project.
        $name = $client->secretName($projectId, $secretId);
    
        // Build the request.
        $request = GetSecretRequest::build($name);
    
        // get the secret.
        $getSecret = $client->getSecret($request);
    
        // get the annotations
        $annotations = $getSecret->getAnnotations();
    
        // print the secret name
        printf('Get secret %s with annotation:' . PHP_EOL, $getSecret->getName());
        // we can even loop over all the annotations
        foreach ($annotations as $key => $val) {
            printf("\t$key: $val" . PHP_EOL);
        }
    }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Secret Manager Python SDK](https://docs.cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-python). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    import argparse
    
    # Import the Secret Manager client library.
    from google.cloud import secretmanager
    
    
    def view_secret_annotations(project_id: str, secret_id: str) -> None:
        """
        List all secret annotations in the given secret.
        """
        # Create the Secret Manager client.
        client = secretmanager.[SecretManagerServiceClient](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html)()
    
        # Build the resource name of the parent secret.
        name = client.[secret_path](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html#google_cloud_secretmanager_v1_services_secret_manager_service_SecretManagerServiceClient_secret_path)(project_id, secret_id)
    
        response = client.[get_secret](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html#google_cloud_secretmanager_v1_services_secret_manager_service_SecretManagerServiceClient_get_secret)(request={"name": name})
    
        print(f"Got secret {response.name} with annotations :")
        for key in response.annotations:
            print(f"{key} : {response.annotations[key]}")
    
    

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Secret Manager Ruby SDK](https://docs.cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-ruby). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    require "google/cloud/secret_manager"
    
    ##
    # View annotations of a secret.
    #
    # @param project_id [String] Your Google Cloud project (e.g. "my-project")
    # @param secret_id [String] Your secret name (e.g. "my-secret")
    #
    def view_secret_annotations project_id:, secret_id:
      # Create a Secret Manager client.
      client = Google::Cloud::[SecretManager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager.html).[secret_manager_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager/latest/Google-Cloud-SecretManager.html)
    
      # Build the resource name of the secret.
      name = client.secret_path project: project_id, secret: secret_id
    
      # Get the existing secret.
      existing_secret = client.get_secret name: name
    
      # Get the existing secret's annotations.
      existing_secret_annotations = existing_secret.annotations.to_h
    
      # Print the secret name and the annotations.
      puts "Secret: #{existing_secret.name}"
      existing_secret_annotations.each do |key, value|
        puts "Annotation Key: #{key}, Annotation Value: #{value}"
      end
    end

## What's next

  * Learn how to [manage access to secrets](https://docs.cloud.google.com/secret-manager/docs/manage-access-to-secrets).
  * Learn how to [set up rotation schedules for secrets](https://docs.cloud.google.com/secret-manager/docs/secret-rotation).
  * Learn how to [set up notifications on a secret](https://docs.cloud.google.com/secret-manager/docs/event-notifications).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
