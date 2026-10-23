---
url: https://docs.cloud.google.com/secret-manager/regional-secrets/add-secret-version-rs/
title: Add a regional secret version \u00a0|\u00a0 Secret Manager Regional Service Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:52:48.534838+00:00
---

# Add a regional secret version  |  Secret Manager Regional Service Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/regional-secrets/add-secret-version-rs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Regional service ](https://docs.cloud.google.com/secret-manager/regional-secrets)
  * [ Guides ](https://docs.cloud.google.com/secret-manager/regional-secrets/regional-secrets-overview)



Send feedback 

#  Add a regional secret version Stay organized with collections  Save and categorize content based on your preferences. 

Secret data is immutable and most operations take place on secret versions. A secret version contains the actual secret data, along with [state](https://docs.cloud.google.com/secret-manager/regional-secrets/add-secret-version-rs#secret-version-states) and metadata about the secret. This page describes how to add a secret version.

For more information about versioning, see this [video](https://youtu.be/4iddawLDurw?si=Ph22Et2rgiZJLiMr) on versioning.

## Required roles

To get the permissions that you need to add a secret version, ask your administrator to grant you the following IAM roles on a secret: 

  * [Secret Manager Secret Version Adder ](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.secretVersionAdder) (`roles/secretmanager.secretVersionAdder`)
  * [Secret Manager Secret Version Manager ](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.secretVersionManager) (`roles/secretmanager.secretVersionManager`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

IAM roles can't be granted on a secret version.

## Add a secret version

To add a secret version, use one of the following methods:

### Console

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. On the **Secret Manager** page, click the **Regional secrets** tab, and then locate the secret for which you want to add the new version.

  3. Click the more_vert**Actions** menu associated with that secret, and then click **Add new version**. The **Add new version** dialog appears.

  4. In the **Secret value** field, enter a value for the secret such as `abcd1234`. Alternatively, you can upload a file containing the secret value.

  5. Click **Add new version**.




### gcloud

Ensure that you have [configured Secret Manager to use a regional endpoint](https://docs.cloud.google.com/secret-manager/regional-secrets/config-sm-rs#identify_endpoints) to manage regional secrets. 

#### Add a secret version from the contents of a file on disk

Before using any of the command data below, make the following replacements: 

  * SECRET_ID: the ID of the secret
  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the secret
  * FILE_PATH: the full path (including file name) to the file containing the version details



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets versions add SECRET_ID --location=LOCATION --data-file="FILE_PATH"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets versions add SECRET_ID --location=LOCATION --data-file="FILE_PATH"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets versions add SECRET_ID --location=LOCATION --data-file="FILE_PATH"

The response contains the newly created secret version. 

#### Add a secret version directly on the command line

You can also add a secret version directly on the command line, but this is discouraged because _it appears as plaintext_ in the list of processes and may be captured by other system users. Note that the command with the plaintext will also be in your shell history.
    
    
      echo -n "SECRET_DATA" | \
          gcloud secrets versions add SECRET_ID --location=LOCATION --data-file=-

Replace the following: 

  * SECRET_DATA: the data that you want to store in the secret version
  * SECRET_ID: the ID of the secret or fully qualified identifier for the secret
  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the secret



#### Optional: Add a version from a file's contents when first creating a secret

Before using any of the command data below, make the following replacements: 

  * SECRET_ID: the ID of the secret
  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the secret
  * FILE_PATH: the full path (including file name) to the file containing the version details



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets create SECRET_ID --location=LOCATION --data-file="FILE_PATH"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets create SECRET_ID --location=LOCATION --data-file="FILE_PATH"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets create SECRET_ID --location=LOCATION --data-file="FILE_PATH"

The response contains the newly created secret version. 

### REST

Base64-encode the secret data and save it as a shell variable.
    
    
    $ SECRET_DATA=$(echo "seCr3t" | base64)
    

Before using any of the request data, make the following replacements: 

  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the secret
  * PROJECT_ID: the Google Cloud project ID
  * SECRET_ID: the ID of the secret



HTTP method and URL: 
    
    
    POST https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID:addVersion

Request JSON body: 
    
    
    {"payload": {"data": "${SECRET_DATA}"}}
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID:addVersion"

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
        -Uri "https://secretmanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID:addVersion" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/secrets/SECRET_ID/versions/1",
      "createTime": "2024-03-25T08:24:13.153705Z",
      "state": "ENABLED",
      "etag": "\"161477e6071da9\""
    }
    
    

### Go

To run this code, first [set up a Go development environment](https://docs.cloud.google.com/go/docs/setup) and [install the Secret Manager Go SDK](https://docs.cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-go). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    import (
    	"context"
    	"fmt"
    	"hash/crc32"
    	"io"
    
    	secretmanager "cloud.google.com/go/secretmanager/apiv1"
    	"cloud.google.com/go/secretmanager/apiv1/secretmanagerpb"
    	"google.golang.org/api/option"
    )
    
    // addSecretVersion adds a new secret version to the given secret with the
    // provided payload.
    func AddRegionalSecretVersion(w io.Writer, projectId, locationId, secretId string) error {
    	// parent := "projects/my-project/locations/my-location/secrets/my-secret"
    
    	// Declare the payload to store.
    	payload := []byte("my super secret data")
    	// Compute checksum, use Castagnoli polynomial. Providing a checksum
    	// is optional.
    	crc32c := crc32.MakeTable(crc32.Castagnoli)
    	checksum := int64(crc32.Checksum(payload, crc32c))
    
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
    	req := &secretmanagerpb.AddSecretVersionRequest{
    		Parent: parent,
    		Payload: &secretmanagerpb.SecretPayload{
    			Data:       payload,
    			DataCrc32C: &checksum,
    		},
    	}
    
    	// Call the API.
    	result, err := client.AddSecretVersion(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to add regional secret version: %w", err)
    	}
    	fmt.Fprintf(w, "Added regional secret version: %s\n", result.Name)
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Secret Manager Java SDK](https://docs.cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-java). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    import com.google.cloud.secretmanager.v1.[SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html);
    import com.google.cloud.secretmanager.v1.[SecretManagerServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceSettings.html);
    import com.google.cloud.secretmanager.v1.[SecretName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html);
    import com.google.cloud.secretmanager.v1.[SecretPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretPayload.html);
    import com.google.cloud.secretmanager.v1.[SecretVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretVersion.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    import java.util.zip.CRC32C;
    import java.util.zip.Checksum;
    
    public class AddRegionalSecretVersion {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
    
        // Your GCP project ID.
        String projectId = "your-project-id";
        // Location of the secret.
        String locationId = "your-location-id";
        // Resource ID of the secret.
        String secretId = "your-secret-id";
        addRegionalSecretVersion(projectId, locationId, secretId);
      }
    
      // Add a new version to the existing regional secret.
      public static [SecretVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretVersion.html) addRegionalSecretVersion(
          String projectId, String locationId, String secretId) 
          throws IOException {
    
        // Endpoint to call the regional secret manager sever
        String apiEndpoint = String.format("secretmanager.%s.rep.googleapis.com:443", locationId);
        [SecretManagerServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceSettings.html) secretManagerServiceSettings =
            [SecretManagerServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceSettings.html).newBuilder().setEndpoint(apiEndpoint).build();
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html) client = 
            [SecretManagerServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretManagerServiceClient.html).create(secretManagerServiceSettings)) {
          [SecretName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html) secretName = 
              [SecretName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html).[ofProjectLocationSecretName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretName.html#com_google_cloud_secretmanager_v1_SecretName_ofProjectLocationSecretName_java_lang_String_java_lang_String_java_lang_String_)(projectId, locationId, secretId);
          byte[] data = "my super secret data".getBytes();
          // Calculate data checksum. The library is available in Java 9+.
          // For Java 8, use:
          // https://cloud.google.com/appengine/docs/standard/java/javadoc/com/google/appengine/api/files/Crc32c
          Checksum checksum = new CRC32C();
          checksum.update(data, 0, data.length);
    
          // Create the secret payload.
          [SecretPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretPayload.html) payload =
              [SecretPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretPayload.html).newBuilder()
                  .[setData](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretPayload.Builder.html#com_google_cloud_secretmanager_v1_SecretPayload_Builder_setData_com_google_protobuf_ByteString_)([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(data))
                  // Providing data checksum is optional.
                  .[setDataCrc32C](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretPayload.Builder.html#com_google_cloud_secretmanager_v1_SecretPayload_Builder_setDataCrc32C_long_)(checksum.getValue())
                  .build();
    
          // Add the secret version.
          [SecretVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretVersion.html) version = client.addSecretVersion(secretName, payload);
          System.out.printf("Added regional secret version %s\n", version.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-secretmanager/latest/com.google.cloud.secretmanager.v1.SecretVersion.html#com_google_cloud_secretmanager_v1_SecretVersion_getName__)());
    
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
    // const locationId = 'location';
    // const secretId = 'my-secret';
    
    const parent = `projects/${projectId}/locations/${locationId}/secrets/${secretId}`;
    // Imports the Secret Manager library
    const {SecretManagerServiceClient} = require('[@google-cloud/secret-manager](https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/overview.html)');
    
    // Adding the endpoint to call the regional secret manager sever
    const options = {};
    options.apiEndpoint = `secretmanager.${locationId}.rep.googleapis.com`;
    
    // Instantiates a client
    const client = new [SecretManagerServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/secret-manager/latest/overview.html)(options);
    
    // Payload is the plaintext data to store in the secret
    const payload = Buffer.from('my super secret data', 'utf8');
    
    async function addRegionalSecretVersion() {
      const [version] = await client.addSecretVersion({
        parent: parent,
        payload: {
          data: payload,
        },
      });
    
      console.log(`Added regional secret version ${version.name}`);
    }
    
    addRegionalSecretVersion();

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Secret Manager Python SDK](https://docs.cloud.google.com/secret-manager/docs/reference/libraries#client-libraries-install-python). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    from google.cloud import [secretmanager_v1](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest)
    import google_crc32c
    
    
    def add_regional_secret_version(
        project_id: str,
        location_id: str,
        secret_id: str,
        payload: str,
    ) -> secretmanager_v1.SecretVersion:
        """
        Adds a new secret version to the given secret with the provided payload.
        """
    
        # Endpoint to call the regional secret manager sever.
        api_endpoint = f"secretmanager.{location_id}.rep.googleapis.com"
    
        # Create the Secret Manager client.
        client = [secretmanager_v1](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest).[SecretManagerServiceClient](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html)(
            client_options={"api_endpoint": api_endpoint},
        )
    
        # Build the resource name of the parent secret.
        parent = f"projects/{project_id}/locations/{location_id}/secrets/{secret_id}"
    
        # Convert the string payload into a bytes. This step can be omitted if you
        # pass in bytes instead of a str for the payload argument.
        payload_bytes = payload.encode("UTF-8")
    
        # Calculate payload checksum. Passing a checksum in add-version request
        # is optional.
        crc32c = google_crc32c.Checksum()
        crc32c.update(payload_bytes)
    
        # Add the secret version.
        response = client.[add_secret_version](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1.services.secret_manager_service.SecretManagerServiceClient.html#google_cloud_secretmanager_v1_services_secret_manager_service_SecretManagerServiceClient_add_secret_version)(
            request={
                "parent": parent,
                "payload": {
                    "data": payload_bytes,
                    "data_crc32c": int(crc32c.hexdigest(), 16),
                },
            }
        )
    
        # Print the new secret version name.
        print(f"Added secret version: {response.name}")
        return response
    
    

## Secret version states

A secret version can be in one of the following states at any given time:

  * **Enabled** \- In this state, the secret version can be accessed and described. This is the default state for a new secret version.

  * **Disabled** \- In this state, the secret version cannot be accessed, but the secret's contents still exist. The secret version can be re-enabled to restore access.

  * **Destroyed** \- In this state, the secret version's contents are discarded. The secret version cannot be changed to another state.




You are billed for both enabled and disabled secret versions. You are not billed for secret versions that are in the destroyed state.

## What's next

  * [Access a regional secret version](https://docs.cloud.google.com/secret-manager/regional-secrets/access-secret-version-rs)
  * [Assign an alias to a regional secret version](https://docs.cloud.google.com/secret-manager/regional-secrets/assign-alias-to-secret-version-rs)
  * [List regional secret versions and view version details](https://docs.cloud.google.com/secret-manager/regional-secrets/view-regional-secrets-versions)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
