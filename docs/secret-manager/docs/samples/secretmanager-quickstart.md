---
url: https://docs.cloud.google.com/secret-manager/docs/samples/secretmanager-quickstart/
title: Quickstart \u00a0|\u00a0 Secret Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:49:20.923477+00:00
---

# Quickstart  |  Secret Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/docs/samples/secretmanager-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Samples ](https://docs.cloud.google.com/secret-manager/docs/samples)



#  Quickstart Stay organized with collections  Save and categorize content based on your preferences. 

Quickstart for Secret Manager.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create and access a secret using Secret Manager](https://docs.cloud.google.com/secret-manager/docs/create-secret-quickstart)
  * [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries)



## Code sample

### C#

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using System.Text;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.SecretManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.html);
    using [Google.Protobuf](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.html);
    
    public class QuickstartSample
    {
        public void Quickstart(string projectId = "my-project", string secretId = "my-secret")
        {
            // Create the client.
            [SecretManagerServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html) client = [SecretManagerServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html#Google_Cloud_SecretManager_V1_SecretManagerServiceClient_Create)();
    
            // Build the parent project name.
            [ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html) projectName = new [ProjectName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)(projectId);
    
            // Build the secret to create.
            Secret secret = new Secret
            {
                Replication = new [Replication](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.Replication.html)
                {
                    Automatic = new Replication.Types.Automatic(),
                },
            };
    
            Secret createdSecret = client.[CreateSecret](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html#Google_Cloud_SecretManager_V1_SecretManagerServiceClient_CreateSecret_Google_Api_Gax_ResourceNames_LocationName_System_String_Google_Cloud_SecretManager_V1_Secret_Google_Api_Gax_Grpc_CallSettings_)(projectName, secretId, secret);
    
            // Build a payload.
            [SecretPayload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretPayload.html) payload = new [SecretPayload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretPayload.html)
            {
                Data = [ByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html).[CopyFrom](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html#Google_Protobuf_ByteString_CopyFrom_System_Byte___)("my super secret data", Encoding.UTF8),
            };
    
            // Add a secret version.
            [SecretVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretVersion.html) createdVersion = client.[AddSecretVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html#Google_Cloud_SecretManager_V1_SecretManagerServiceClient_AddSecretVersion_Google_Cloud_SecretManager_V1_AddSecretVersionRequest_Google_Api_Gax_Grpc_CallSettings_)(createdSecret.[SecretName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.Secret.html#Google_Cloud_SecretManager_V1_Secret_SecretName), payload);
    
            // Access the secret version.
            [AccessSecretVersionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.AccessSecretVersionResponse.html) result = client.[AccessSecretVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretManagerServiceClient.html#Google_Cloud_SecretManager_V1_SecretManagerServiceClient_AccessSecretVersion_Google_Cloud_SecretManager_V1_AccessSecretVersionRequest_Google_Api_Gax_Grpc_CallSettings_)(createdVersion.[SecretVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretVersion.html#Google_Cloud_SecretManager_V1_SecretVersion_SecretVersionName));
    
            // Print the results
            //
            // WARNING: Do not print secrets in production environments. This
            // snippet is for demonstration purposes only.
            string data = result.[Payload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.AccessSecretVersionResponse.html#Google_Cloud_SecretManager_V1_AccessSecretVersionResponse_Payload).[Data](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecretManager.V1/latest/Google.Cloud.SecretManager.V1.SecretPayload.html#Google_Cloud_SecretManager_V1_SecretPayload_Data).[ToStringUtf8](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html#Google_Protobuf_ByteString_ToStringUtf8)();
            Console.WriteLine($"Plaintext: {data}");
        }
    }

### Go

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Sample quickstart is a basic program that uses Secret Manager.
    package main
    
    import (
    	"context"
    	"fmt"
    	"log"
    
    	secretmanager "cloud.google.com/go/secretmanager/apiv1"
    	"cloud.google.com/go/secretmanager/apiv1/secretmanagerpb"
    )
    
    func main() {
    	// GCP project in which to store secrets in Secret Manager.
    	projectID := "your-project-id"
    
    	// Create the client.
    	ctx := context.Background()
    	client, err := secretmanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		log.Fatalf("failed to setup client: %v", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_Close)()
    
    	// Create the request to create the secret.
    	createSecretReq := &secretmanagerpb.CreateSecretRequest{
    		Parent:   fmt.Sprintf("projects/%s", projectID),
    		SecretId: "my-secret",
    		Secret: &secretmanagerpb.Secret{
    			Replication: &secretmanagerpb.Replication{
    				Replication: &secretmanagerpb.Replication_Automatic_{
    					Automatic: &secretmanagerpb.Replication_Automatic{},
    				},
    			},
    		},
    	}
    
    	secret, err := client.CreateSecret(ctx, createSecretReq)
    	if err != nil {
    		log.Fatalf("failed to create secret: %v", err)
    	}
    
    	// Declare the payload to store.
    	payload := []byte("my super secret data")
    
    	// Build the request.
    	addSecretVersionReq := &secretmanagerpb.AddSecretVersionRequest{
    		Parent: secret.Name,
    		Payload: &secretmanagerpb.SecretPayload{
    			Data: payload,
    		},
    	}
    
    	// Call the API.
    	version, err := client.AddSecretVersion(ctx, addSecretVersionReq)
    	if err != nil {
    		log.Fatalf("failed to add secret version: %v", err)
    	}
    
    	// Build the request.
    	accessRequest := &secretmanagerpb.AccessSecretVersionRequest{
    		Name: version.Name,
    	}
    
    	// Call the API.
    	result, err := client.AccessSecretVersion(ctx, accessRequest)
    	if err != nil {
    		log.Fatalf("failed to access secret version: %v", err)
    	}
    
    	// Print the secret payload.
    	//
    	// WARNING: Do not print the secret in a production environment - this
    	// snippet is showing how to access the secret material.
    	log.Printf("Plaintext: %s", result.Payload.Data)
    }
    

### Java

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.secretmanager.v1.[AccessSecretVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.AccessSecretVersionResponse.html);
    import com.google.cloud.secretmanager.v1.[ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.ProjectName.html);
    import com.google.cloud.secretmanager.v1.[Replication](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Replication.html);
    import com.google.cloud.secretmanager.v1.[Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html);
    import com.google.cloud.secretmanager.v1.[SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html);
    import com.google.cloud.secretmanager.v1.[SecretPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretPayload.html);
    import com.google.cloud.secretmanager.v1.[SecretVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretVersion.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    
    public class Quickstart {
    
      public void quickstart() throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String secretId = "your-secret-id";
        quickstart(projectId, secretId);
      }
    
      public void quickstart(String projectId, String secretId) throws Exception {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html) client = [SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html).create()) {
          // Build the parent name from the project.
          [ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.ProjectName.html) projectName = [ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.ProjectName.html).of(projectId);
    
          // Create the parent secret.
          [Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html) secret =
              [Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html).newBuilder()
                  .[setReplication](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.Builder.html#com_google_cloud_secretmanager_v1_Secret_Builder_setReplication_com_google_cloud_secretmanager_v1_Replication_)(
                      [Replication](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Replication.html).newBuilder()
                          .setAutomatic([Replication](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Replication.html).Automatic.newBuilder().build())
                          .build())
                  .build();
    
          [Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html) createdSecret = client.createSecret(projectName, secretId, secret);
    
          // Add a secret version.
          [SecretPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretPayload.html) payload =
              [SecretPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretPayload.html).newBuilder().[setData](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretPayload.Builder.html#com_google_cloud_secretmanager_v1_SecretPayload_Builder_setData_com_google_protobuf_ByteString_)([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFromUtf8](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFromUtf8_java_lang_String_)("hello world!")).build();
          [SecretVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretVersion.html) addedVersion = client.addSecretVersion(createdSecret.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html#com_google_cloud_secretmanager_v1_Secret_getName__)(), payload);
    
          // Access the secret version.
          [AccessSecretVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.AccessSecretVersionResponse.html) response = client.accessSecretVersion(addedVersion.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretVersion.html#com_google_cloud_secretmanager_v1_SecretVersion_getName__)());
    
          // Print the secret payload.
          //
          // WARNING: Do not print the secret in a production environment - this
          // snippet is showing how to access the secret material.
          String data = response.[getPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.AccessSecretVersionResponse.html#com_google_cloud_secretmanager_v1_AccessSecretVersionResponse_getPayload__)().getData().toStringUtf8();
          System.out.printf("Plaintext: %s\n", data);
        }
      }
    }

### Node.js

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Import the Secret Manager client and instantiate it:
    const {SecretManagerServiceClient} = require('[@google-cloud/secret-manager](https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/overview.html)');
    const client = new [SecretManagerServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/overview.html)();
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // parent = 'projects/my-project', // Project for which to manage secrets.
    // secretId = 'foo', // Secret ID.
    // payload = 'hello world!' // String source data.
    
    async function createAndAccessSecret() {
      // Create the secret with automation replication.
      const [secret] = await client.createSecret({
        parent: parent,
        secret: {
          name: secretId,
          replication: {
            automatic: {},
          },
        },
        secretId,
      });
    
      console.info(`Created secret ${secret.name}`);
    
      // Add a version with a payload onto the secret.
      const [version] = await client.addSecretVersion({
        parent: secret.name,
        payload: {
          data: Buffer.from(payload, 'utf8'),
        },
      });
    
      console.info(`Added secret version ${version.name}`);
    
      // Access the secret.
      const [accessResponse] = await client.accessSecretVersion({
        name: version.name,
      });
    
      const responsePayload = accessResponse.payload.data.toString('utf8');
      console.info(`Payload: ${responsePayload}`);
    }
    createAndAccessSecret();

### PHP

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Import the Secret Manager client library.
    use Google\Cloud\SecretManager\V1\AccessSecretVersionRequest;
    use Google\Cloud\SecretManager\V1\AddSecretVersionRequest;
    use Google\Cloud\SecretManager\V1\Client\SecretManagerServiceClient;
    use Google\Cloud\SecretManager\V1\CreateSecretRequest;
    use Google\Cloud\SecretManager\V1\Replication;
    use Google\Cloud\SecretManager\V1\Replication\Automatic;
    use Google\Cloud\SecretManager\V1\Secret;
    use Google\Cloud\SecretManager\V1\SecretPayload;
    
    /** Uncomment and populate these variables in your code */
    // $projectId = 'YOUR_GOOGLE_CLOUD_PROJECT' (e.g. 'my-project');
    // $secretId = 'YOUR_SECRET_ID' (e.g. 'my-secret');
    
    // Create the Secret Manager client.
    $client = new SecretManagerServiceClient();
    
    // Build the parent name from the project.
    $parent = $client->projectName($projectId);
    
    // Create the parent secret.
    $createSecretRequest = (new CreateSecretRequest())
        ->setParent($parent)
        ->setSecretId($secretId)
        ->setSecret(new Secret([
            'replication' => new Replication([
                'automatic' => new Automatic(),
            ]),
        ]));
    $secret = $client->createSecret($createSecretRequest);
    
    // Add the secret version.
    $addSecretVersionRequest = (new AddSecretVersionRequest())
        ->setParent($secret->getName())
        ->setPayload(new SecretPayload([
        'data' => 'hello world',
    ]));
    $version = $client->addSecretVersion($addSecretVersionRequest);
    
    // Access the secret version.
    $accessSecretVersionRequest = (new AccessSecretVersionRequest())
        ->setName($version->getName());
    $response = $client->accessSecretVersion($accessSecretVersionRequest);
    
    // Print the secret payload.
    //
    // WARNING: Do not print the secret in a production environment - this
    // snippet is showing how to access the secret material.
    $payload = $response->getPayload()->getData();
    printf('Plaintext: %s' . PHP_EOL, $payload);

### Python

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Import the Secret Manager client library.
    from google.cloud import secretmanager
    
    # GCP project in which to store secrets in Secret Manager.
    project_id = "YOUR_PROJECT_ID"
    
    # ID of the secret to create.
    secret_id = "YOUR_SECRET_ID"
    
    # Create the Secret Manager client.
    client = secretmanager.[SecretManagerServiceClient](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html)()
    
    # Build the parent name from the project.
    parent = f"projects/{project_id}"
    
    # Create the parent secret.
    secret = client.[create_secret](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html#google_cloud_secretmanager_v1_services_secret_manager_service_SecretManagerServiceClient_create_secret)(
        request={
            "parent": parent,
            "secret_id": secret_id,
            "secret": {"replication": {"automatic": {}}},
        }
    )
    
    # Add the secret version.
    version = client.[add_secret_version](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html#google_cloud_secretmanager_v1_services_secret_manager_service_SecretManagerServiceClient_add_secret_version)(
        request={"parent": secret.name, "payload": {"data": b"hello world!"}}
    )
    
    # Access the secret version.
    response = client.[access_secret_version](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html#google_cloud_secretmanager_v1_services_secret_manager_service_SecretManagerServiceClient_access_secret_version)(request={"name": version.name})
    
    # Print the secret payload.
    #
    # WARNING: Do not print the secret in a production environment - this
    # snippet is showing how to access the secret material.
    payload = response.payload.data.decode("UTF-8")
    print(f"Plaintext: {payload}")

### Ruby

To learn how to install and use the client library for Secret Manager, see [Secret Manager client libraries](https://docs.cloud.google.com/secret-manager/docs/reference/libraries). 

To authenticate to Secret Manager, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/secret_manager"
    
    ##
    # Secret manager quickstart
    #
    # @param project_id [String] Your Google Cloud project (e.g. "my-project")
    # @param secret_id [String] Your secret name (e.g. "my-secret")
    #
    def quickstart project_id:, secret_id:
      # Create the Secret Manager client.
      client = Google::Cloud::[SecretManager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager-v1beta2/latest/Google-Cloud-SecretManager.html).[secret_manager_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-secret_manager/latest/Google-Cloud-SecretManager.html)
    
      # Build the parent name from the project.
      parent = "projects/#{project_id}"
    
      # Create the parent secret.
      secret = client.create_secret(
        parent:    parent,
        secret_id: secret_id,
        secret:    {
          replication: {
            automatic: {}
          }
        }
      )
    
      # Add a secret version.
      version = client.add_secret_version(
        parent:  secret.name,
        payload: {
          data: "hello world!"
        }
      )
    
      # Access the secret version.
      response = client.access_secret_version name: version.name
    
      # Print the secret payload.
      #
      # WARNING: Do not print the secret in a production environment - this
      # snippet is showing how to access the secret material.
      payload = response.payload.data
      puts "Plaintext: #{payload}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=secretmanager). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
