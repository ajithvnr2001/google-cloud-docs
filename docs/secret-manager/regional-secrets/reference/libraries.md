---
url: https://docs.cloud.google.com/secret-manager/regional-secrets/reference/libraries/
title: Secret Manager client libraries \u00a0|\u00a0 Secret Manager Regional Service Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:52:48.818586+00:00
---

# Secret Manager client libraries  |  Secret Manager Regional Service Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/regional-secrets/reference/libraries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Regional service ](https://docs.cloud.google.com/secret-manager/regional-secrets)
  * [ Reference ](https://docs.cloud.google.com/secret-manager/regional-secrets/apis)



Send feedback 

#  Secret Manager client libraries Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to get started with the Cloud Client Libraries for the Secret Manager API. Client libraries make it easier to access Google Cloud APIs from a supported language. Although you can use Google Cloud APIs directly by making raw requests to the server, client libraries provide simplifications that significantly reduce the amount of code you need to write.

Read more about the Cloud Client Libraries and the older Google API Client Libraries in [Client libraries explained](https://docs.cloud.google.com/apis/docs/client-libraries-explained).

## Install the client library

### C++

See [Setting up a C++ development environment](https://docs.cloud.google.com/cpp/docs/setup) for details about this client library's requirements and install dependencies.

### C#

If you are using Visual Studio 2017 or higher, open nuget package manager window and type the following: 
    
    
    Install-Package Google.Apis

If you are using .NET Core command-line interface tools to install your dependencies, run the following command:
    
    
    dotnet add package Google.Apis

For more information, see [Setting Up a C# Development Environment](https://docs.cloud.google.com/dotnet/docs/setup).

### Go
    
    
    $ go get cloud.google.com/go/secretmanager/apiv1
    $ go get google.golang.org/genproto/googleapis/cloud/secretmanager/v1

For more information, see [Setting Up a Go Development Environment](https://docs.cloud.google.com/go/docs/setup).

### Java

If you are using [Maven](https://maven.apache.org/), add the following to your `pom.xml` file. For more information about BOMs, see [The Google Cloud Platform Libraries BOM](https://cloud.google.com/java/docs/bom).
    
    
    <dependencyManagement>
      <dependencies>
        <dependency>
          <groupId>com.google.cloud</groupId>
          <artifactId>libraries-bom</artifactId>
          <version>26.90.0</version>
          <type>pom</type>
          <scope>import</scope>
        </dependency>
      </dependencies>
    </dependencyManagement>
    
    <dependencies>
      <dependency>
        <groupId>com.google.cloud</groupId>
        <artifactId>google-cloud-secretmanager</artifactId>
      </dependency>
    </dependencies>

If you are using [Gradle](https://gradle.org/), add the following to your dependencies:
    
    
    implementation platform('com.google.cloud:libraries-bom:26.90.0')
    
    implementation 'com.google.cloud:google-cloud-secretmanager'

If you are using [sbt](https://www.scala-sbt.org/), add the following to your dependencies:
    
    
    libraryDependencies += "com.google.cloud" % "google-cloud-secretmanager" % "2.99.0"

If you're using Visual Studio Code or IntelliJ, you can add client libraries to your project using the following IDE plugins:

  * [Cloud Code for VS Code](https://docs.cloud.google.com/code/docs/vscode/client-libraries)
  * [Cloud Code for IntelliJ](https://docs.cloud.google.com/code/docs/intellij/client-libraries)



The plugins provide additional functionality, such as key management for service accounts. Refer to each plugin's documentation for details.

**Note:** Cloud Java client libraries do not currently support Android.

For more information, see [Setting Up a Java Development Environment](https://docs.cloud.google.com/java/docs/setup).

### Node.js
    
    
    $ npm install @google-cloud/secret-manager

For more information, see [Setting Up a Node.js Development Environment](https://docs.cloud.google.com/nodejs/docs/setup).

### PHP
    
    
    composer require google/apiclient

For more information, see [Using PHP on Google Cloud](https://docs.cloud.google.com/php/docs).

### Python
    
    
    $ pip install google-cloud-secret-manager

For more information, see [Setting Up a Python Development Environment](https://docs.cloud.google.com/python/docs/setup).

### Ruby
    
    
    gem install google-api-client

For more information, see [Setting Up a Ruby Development Environment](https://docs.cloud.google.com/ruby/docs/setup).

## Set up authentication

To authenticate calls to Google Cloud APIs, client libraries support [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials); the libraries look for credentials in a set of defined locations and use those credentials to authenticate requests to the API. With ADC, you can make credentials available to your application in a variety of environments, such as local development or production, without needing to modify your application code. 

For production environments, the way you set up ADC depends on the service and context. For more information, see [Set up Application Default Credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc).

For a local development environment, you can set up ADC with the credentials that are associated with your Google Account:

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
         
         gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  2. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

A sign-in screen appears. After you sign in, your credentials are stored in the [ local credential file used by ADC](https://docs.cloud.google.com/docs/authentication/application-default-credentials#personal). 




## Use the client library

The following example shows how to use the client library. 

### Go
    
    
    // Sample quickstart is a basic program that uses Secret Manager.
    package main
    
    import (
    	"context"
    	"fmt"
    	"log"
    
    	secretmanager "cloud.google.com/go/secretmanager/apiv1"
    	"cloud.google.com/go/secretmanager/apiv1/secretmanagerpb"
    	"google.golang.org/api/option"
    )
    
    func main() {
    	// GCP project in which to store secrets in Secret Manager.
    	projectID := "your-project-id"
    	// Location at which you want to store your secrets
    	locationID := "your-location-id"
    
    	// Create the client.
    	ctx := context.Background()
    	endpoint := fmt.Sprintf("secretmanager.%s.rep.googleapis.com:443", locationID)
    	client, err := secretmanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_NewClient)(ctx, option.WithEndpoint(endpoint))
    
    	if err != nil {
    		log.Fatalf("failed to setup client: %v", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/secretmanager/latest/apiv1.html#cloud_google_com_go_secretmanager_apiv1_Client_Close)()
    
    	parent := fmt.Sprintf("projects/%s/locations/%s", projectID, locationID)
    
    	// Create the request to create the secret.
    	createSecretReq := &secretmanagerpb.CreateSecretRequest{
    		Parent:   parent,
    		SecretId: "my-secret",
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
    
    
    import com.google.cloud.secretmanager.v1.[AccessSecretVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.AccessSecretVersionResponse.html);
    import com.google.cloud.secretmanager.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.LocationName.html);
    import com.google.cloud.secretmanager.v1.[Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html);
    import com.google.cloud.secretmanager.v1.[SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html);
    import com.google.cloud.secretmanager.v1.[SecretManagerServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceSettings.html);
    import com.google.cloud.secretmanager.v1.[SecretPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretPayload.html);
    import com.google.cloud.secretmanager.v1.[SecretVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretVersion.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    
    public class RegionalQuickstart {
    
      public void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
    
        // Your GCP project ID.
        String projectId = "your-project-id";
        // Location of the secret.
        String locationId = "your-location-id";
        // Resource ID of the secret.
        String secretId = "your-secret-id";
        regionalQuickstart(projectId, locationId, secretId);
      }
    
      // Demonstrates basic capabilities in the regional Secret Manager API.
      public [SecretPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretPayload.html) regionalQuickstart(
          String projectId, String locationId, String secretId) 
          throws Exception {
    
        // Endpoint to call the regional secret manager sever
        String apiEndpoint = String.format("secretmanager.%s.rep.googleapis.com:443", locationId);
        [SecretManagerServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceSettings.html) secretManagerServiceSettings =
            [SecretManagerServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceSettings.html).newBuilder().setEndpoint(apiEndpoint).build();
    
        // Initialize the client that will be used to send requests. This client only needs to be
        // created once, and can be reused for multiple requests.
        try ([SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html) client = 
            [SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html).create(secretManagerServiceSettings)) {
          // Build the parent name from the project.
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.LocationName.html) parent = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.LocationName.html).of(projectId, locationId);
    
          // Create the parent secret.
          [Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html) secret =
              [Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html).newBuilder()
                  .build();
    
          [Secret](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html) createdSecret = client.createSecret(parent, secretId, secret);
    
          // Add a secret version.
          [SecretPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretPayload.html) payload =
              [SecretPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretPayload.html).newBuilder().[setData](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretPayload.Builder.html#com_google_cloud_secretmanager_v1_SecretPayload_Builder_setData_com_google_protobuf_ByteString_)([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFromUtf8](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFromUtf8_java_lang_String_)("Secret data")).build();
          [SecretVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretVersion.html) addedVersion = client.addSecretVersion(createdSecret.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.Secret.html#com_google_cloud_secretmanager_v1_Secret_getName__)(), payload);
    
          // Access the secret version.
          [AccessSecretVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.AccessSecretVersionResponse.html) response = client.accessSecretVersion(addedVersion.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretVersion.html#com_google_cloud_secretmanager_v1_SecretVersion_getName__)());
    
          // Print the secret payload.
          //
          // WARNING: Do not print the secret in a production environment - this
          // snippet is showing how to access the secret material.
          String data = response.[getPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.AccessSecretVersionResponse.html#com_google_cloud_secretmanager_v1_AccessSecretVersionResponse_getPayload__)().getData().toStringUtf8();
          // System.out.printf("Plaintext: %s\n", data);
    
          return payload;
        }
      }
    }

### Node.js
    
    
    // Adding the endpoint to call the regional secret manager sever
    const options = {};
    options.apiEndpoint = `secretmanager.${locationId}.rep.googleapis.com`;
    
    // Import the Secret Manager client and instantiate it:
    const {SecretManagerServiceClient} = require('[@google-cloud/secret-manager](https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/overview.html)');
    const client = new [SecretManagerServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/overview.html)(options);
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // projectId = 'my-project', // Project for which to manage secrets.
    // locationID = 'my-location', // Region location to store secrets in
    // secretId = 'foo', // Secret ID.
    // payload = 'hello world!' // String source data.
    
    const parent = `projects/${projectId}/locations/${locationId}`;
    
    async function createAndAccessSecret() {
      // Create the secret.
      const [secret] = await client.createSecret({
        parent: parent,
        secret: {
          name: secretId,
        },
        secretId,
      });
    
      console.info(`Created regional secret ${secret.name}`);
    
      // Add a version with a payload onto the secret.
      const [version] = await client.addSecretVersion({
        parent: secret.name,
        payload: {
          data: Buffer.from(payload, 'utf8'),
        },
      });
    
      console.info(`Added regional secret version ${version.name}`);
    
      // Access the secret.
      const [accessResponse] = await client.accessSecretVersion({
        name: version.name,
      });
    
      const responsePayload = accessResponse.payload.data.toString('utf8');
      console.info(`Payload: ${responsePayload}`);
    }
    createAndAccessSecret();

### Python
    
    
    # Import the Secret Manager client library.
    from google.cloud import [secretmanager_v1](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest)
    
    # TODO (developer): uncomment variables and assign a value.
    
    # GCP project in which to store secrets in Secret Manager.
    # project_id = "YOUR_PROJECT_ID"
    
    # Location where the secret is to be stored
    # location_id = "YOUR_LOCATION_ID"
    
    # ID of the secret to create.
    # secret_id = "YOUR_SECRET_ID"
    
    # Endpoint to call the regional secret manager sever
    api_endpoint = f"secretmanager.{location_id}.rep.googleapis.com"
    
    # Create the Secret Manager client.
    client = [secretmanager_v1](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest).[SecretManagerServiceClient](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html)(
        client_options={"api_endpoint": api_endpoint},
    )
    
    # Build the parent name from the project.
    parent = f"projects/{project_id}/locations/{location_id}"
    
    # Create the parent secret.
    secret = client.[create_secret](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html#google_cloud_secretmanager_v1_services_secret_manager_service_SecretManagerServiceClient_create_secret)(
        request={
            "parent": parent,
            "secret_id": secret_id,
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

## Additional resources

### C++

The following list contains links to more resources related to the client library for C++:

  * [API reference](https://docs.cloud.google.com/cpp/docs/reference)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-cpp/issues)
  * [`google-secret-manager` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-secret-manager%5D%5Bc%2B%2B%5D)
  * [Source code](https://github.com/googleapis/google-cloud-cpp)



### C#

The following list contains links to more resources related to the client library for C#:

  * [API reference](https://developers.google.com/api-client-library/dotnet)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/google/google-api-dotnet-client/issues)
  * [`google-secret-manager` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-secret-manager%5D+%5Bc%23%5D)
  * [Source code](https://github.com/google/google-api-dotnet-client)



### Go

The following list contains links to more resources related to the client library for Go:

  * [API reference](https://github.com/googleapis/google-cloud-go/tree/main/secretmanager/apiv1)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-go/issues)
  * [`google-secret-manager` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-secret-manager%5D+%5Bgo%5D)
  * [Source code](https://github.com/googleapis/google-cloud-go)



### Java

The following list contains links to more resources related to the client library for Java:

  * [API reference](https://cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/overview)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-java/tree/main/java-secretmanager/issues)
  * [`google-secret-manager` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-secret-manager%5D+%5Bjava%5D)
  * [Source code](https://github.com/googleapis/google-cloud-java/tree/main/java-secretmanager)



### Node.js

The following list contains links to more resources related to the client library for Node.js:

  * [API reference](https://googleapis.dev/nodejs/secretmanager/latest/index.html)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-node/tree/main/packages/google-cloud-secretmanager/issues)
  * [`google-secret-manager` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-secret-manager%5D+%5Bnode.js%5D)
  * [Source code](https://github.com/googleapis/google-cloud-node/tree/main/packages/google-cloud-secretmanager)



### PHP

The following list contains links to more resources related to the client library for PHP:

  * [API reference](https://developers.google.com/api-client-library/php/)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/google/google-api-php-client/issues)
  * [`google-secret-manager` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-secret-manager%5D+%5Bphp%5D)
  * [Source code](https://github.com/google/google-api-php-client)



### Python

The following list contains links to more resources related to the client library for Python:

  * [API reference](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-secret-manager/issues)
  * [`google-secret-manager` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-secret-manager%5D+%5Bpython%5D)
  * [Source code](https://github.com/googleapis/google-cloud-python/tree/main/packages/google-cloud-secret-manager)



### Ruby

The following list contains links to more resources related to the client library for Ruby:

  * [API reference](https://developers.google.com/api-client-library/ruby/apis/)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/google/google-api-ruby-client/issues)
  * [`google-secret-manager` on Stack Overflow](https://stackoverflow.com/search?q=%5Bgoogle-secret-manager%5D+%5Bruby%5D)
  * [Source code](https://github.com/google/google-api-ruby-client)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
