---
url: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference-secrets-in-parameter/
title: Reference secrets in parameters \u00a0|\u00a0 Parameter Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:40:36.610618+00:00
---

# Reference secrets in parameters  |  Parameter Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference-secrets-in-parameter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Parameter Manager ](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/overview)



Send feedback 

#  Reference secrets in parameters Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to reference secrets in parameters. To learn more about secrets, see [Secret Manager overview](https://docs.cloud.google.com/secret-manager/docs/overview).

You can store sensitive information such as your passwords and API keys in Secret Manager and then reference those secrets from within parameters used in your applications or infrastructure. The maximum number of secret references a parameter version can contain is 15.

For example, you have a database connection string that includes a password. Do the following:

  * Store the password as a secret in Secret Manager.
  * Create a parameter in Parameter Manager for the connection string.
  * Store a reference to the secret in your parameter version.



When your application or infrastructure needs the secret, it retrieves the parameter value, which contains the reference to the secret. Then, it uses that reference to fetch the actual secret value from Secret Manager. This way, the actual password is not exposed in your configuration files.

By storing secrets separately from configuration files and application code, you can reduce the risk of accidental exposure or unauthorized access. You can securely store, audit, and rotate your secrets in Secret Manager while keeping all your configuration data organized in Parameter Manager.

To reference secrets within parameters, you must do the following:

  * [Create a parameter version with the secret reference](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference-secrets-in-parameter#create-parameter-secret-reference)
  * [Grant the Secret Manager Secret Accessor role to the parameter](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference-secrets-in-parameter#grant_the_secret_manager_secret_accessor_role_to_the_parameter)

**Note:** Secret references can only be added to _parameters_ that hold structured data, such as YAML or JSON. However, the content of the referenced secrets must not be YAML or JSON.

## Required roles

To get the permissions that you need to create a parameter version with a secret reference, ask your administrator to grant you the [Parameter Manager Parameter Version Adder ](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.parameterversions.create) (`roles/parametermanager.parameterversions.create`) IAM role on the project, folder, or organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a parameter version with the secret reference

If you are using the REST API to manage parameter versions, complete these steps before creating a new version:

  * Encode the parameter payload data containing the secret reference using Base64 and then pass the encoded string in the create version command. For example, you want to create a new version of an existing parameter with a secret reference using the following YAML data:
        
        project:
          display_name: PM Bank
          locale: en-US
          port: 8080
          db_password: __REF__("//secretmanager.googleapis.com/projects/production-1/secrets/db_password/versions/1")
          mask_sensitive_fields: false
        

The field `db_password` uses a special reference (`__REF__()`) to pull the actual password value from Secret Manager and the corresponding URL specifies the location of your database password within Secret Manager.

Here's the Base64 string for the sample YAML data given in this section:

`cHJvamVjdDoNCiAgZGlzcGxheV9uYW1lOiBQTSBCYW5rDQogIGxvY2FsZTogZW4tVVMNCiAgcG9ydDogODA4MA0KICBkYl9wYXNzd29yZDogX19SRUZfXygiLy9zZWNyZXRtYW5hZ2VyLmdvb2dsZWFwaXMuY29tL3Byb2plY3RzL2FjbS1zYW1wbGUvc2VjcmV0cy9kYl9wYXNzd29yZC92ZXJzaW9ucy8xIikNCiAgbWFza19zZW5zaXRpdmVfZmllbGRzOiBmYWxzZQ==`


**Note:** The parameter payload is encoded by default when you use it with the gcloud CLI command.

To create a new version with the secret reference, use one of the following methods:

**Global parameters**

### Console

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. Click **Parameter Manager** to go to the **Parameter Manager** page.

  3. Click the parameter name that you want to add the new version. The parameter details are displayed.

  4. Click the **Versions** tab and then click **New version**. The **Create parameter version** page opens.

  5. Enter the version name. Parameter version names can be up to 63 characters long, can contain letters (both upper and lowercase), numbers, hyphens (-), and underscores (_), but cannot start with a hyphen.

  6. In the **Payload** section, enter the parameter value containing the secret reference using one of the following methods:

     * **Option 1: upload a file**
       1. Click **Browse**.

       2. Select a file containing the parameter value with the secret reference.

     * **Option 2: enter the payload manually**
       1. Enter the parameter value containing the secret reference in the payload text area.

Ensure that the secret uses the special reference (`__REF__()`) format.

     * **Option 3: dynamically insert a secret**
       1. Enter the parameter value in the payload text area.

       2. Navigate to the field that contains the secret reference, press **Ctrl** \+ **Space** , and then press **Enter**. The **Secret picker** side panel appears.

       3. Select the **Secret** and the **Secret version**. Optionally, enable the **Select regional secret** toggle to select a regional secret.

Alternatively, you can either [enter the secret manually](https://docs.cloud.google.com/secret-manager/docs/view-secret-details) by specifying the resource ID or [create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets).

       4. Click **Insert**.

  7. Click **Create**.




### gcloud

Before using any of the command data below, make the following replacements: 

  * PARAMETER_VERSION_ID: the ID that you want to assign to the parameter version. Parameter version IDs must be 63 characters or less and consist only of alphanumeric characters (A-Z, a-z, 0-9), dashes (-), and underscores (_). IDs cannot begin with a dash.
  * PARAMETER_ID: the name of the parameter.
  * PARAMETER_PAYLOAD: the data, in plaintext, containing the secret references that you want to store within the parameter version.
  * PROJECT_ID: the Google Cloud project ID.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters versions create PARAMETER_VERSION_ID --parameter=PARAMETER_ID --location=global --payload-data="PARAMETER_PAYLOAD" --project=PROJECT_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters versions create PARAMETER_VERSION_ID --parameter=PARAMETER_ID --location=global --payload-data="PARAMETER_PAYLOAD" --project=PROJECT_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters versions create PARAMETER_VERSION_ID --parameter=PARAMETER_ID --location=global --payload-data="PARAMETER_PAYLOAD" --project=PROJECT_ID

You should receive a response similar to the following:
    
    
    Created parameterVersion [refv1].

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID.
  * PARAMETER_ID: the name of the parameter.
  * PARAMETER_VERSION_ID: the ID that you want to assign to the parameter version. Parameter version IDs must be 63 characters or less and consist only of alphanumeric characters (A-Z, a-z, 0-9), dashes (-), and underscores (_). IDs cannot begin with a dash.
  * PARAMETER_PAYLOAD: the data, as a Base64 encoded string, containing the secret references that you want to store within the parameter version.



HTTP method and URL: 
    
    
    POST https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/parameters/PARAMETER_ID/versions?parameter_version_id=PARAMETER_VERSION_ID

Request JSON body: 
    
    
    {"payload": {"data": "PARAMETER_PAYLOAD"}}
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/parameters/PARAMETER_ID/versions?parameter_version_id=PARAMETER_VERSION_ID"

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
        -Uri "https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/parameters/PARAMETER_ID/versions?parameter_version_id=PARAMETER_VERSION_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/production-1/locations/global/parameters/db_password_secret_ref/versions/refv1",
      "createTime": "2024-10-15T08:39:05.191747694Z",
      "updateTime": "2024-10-15T08:39:05.191747694Z"
    }
    
    

### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Parameter Manager C# SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-csharp). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    using [Google.Cloud.ParameterManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.html);
    using [Google.Protobuf](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.html);
    using System.Text;
    
    public class CreateParameterVersionWithSecretSample
    {
        /// <summary>
        /// This function creates a parameter version with a JSON payload that includes a secret reference using the Parameter Manager SDK for GCP.
        /// </summary>
        /// <param name="projectId">The ID of the project where the parameter is located.</param>
        /// <param name="parameterId">The ID of the parameter for which the version is to be created.</param>
        /// <param name="versionId">The ID of the version to be created.</param>
        /// <param name="secretId">The ID of the secret to be referenced.</param>
        /// <returns>The created ParameterVersion object.</returns>
        public ParameterVersion CreateParameterVersionWithSecret(
            string projectId,
            string parameterId,
            string versionId,
            string secretId)
        {
            // Create the client.
            [ParameterManagerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html) client = [ParameterManagerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html#Google_Cloud_ParameterManager_V1_ParameterManagerClient_Create)();
    
            // Build the parent resource name.
            [ParameterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterName.html) parent = new [ParameterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterName.html)(projectId, "global", parameterId);
    
            // Convert the JSON payload to bytes.
            string payload = $"{{\"username\": \"test-user\", \"password\": \"__REF__(//secretmanager.googleapis.com/{secretId}\"}}";
            [ByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html) data = [ByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html).[CopyFrom](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html#Google_Protobuf_ByteString_CopyFrom_System_Byte___)(payload, Encoding.UTF8);
    
            // Build the parameter version with the JSON payload that includes a secret reference.
            [ParameterVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersion.html) parameterVersion = new [ParameterVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersion.html)
            {
                Payload = new [ParameterVersionPayload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionPayload.html)
                {
                    Data = data
                }
            };
    
            // Call the API to create the parameter version.
            [ParameterVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersion.html) createdParameterVersion = client.[CreateParameterVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html#Google_Cloud_ParameterManager_V1_ParameterManagerClient_CreateParameterVersion_Google_Cloud_ParameterManager_V1_CreateParameterVersionRequest_Google_Api_Gax_Grpc_CallSettings_)(parent, parameterVersion, versionId);
    
            // Print the created parameter version name.
            Console.WriteLine($"Created parameter version: {createdParameterVersion.[Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersion.html#Google_Cloud_ParameterManager_V1_ParameterVersion_Name)}");
    
            // Return the created parameter version.
            return createdParameterVersion;
        }
    }

### Go

To run this code, first [set up a Go development environment](https://docs.cloud.google.com/go/docs/setup) and [install the Parameter Manager Go SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-go). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	parametermanager "cloud.google.com/go/parametermanager/apiv1"
    	parametermanagerpb "cloud.google.com/go/parametermanager/apiv1/parametermanagerpb"
    )
    
    // createParamVersionWithSecret creates a new version of a parameter with a JSON payload that has a secret reference in it using the Parameter Manager SDK for GCP.
    //
    // w: The io.Writer object used to write the output.
    // projectID: The ID of the project where the parameter is located.
    // parameterID: The ID of the parameter for which the version is to be created.
    // versionID: The ID of the version to be created.
    // secretID: The ID of the secret to be referenced.
    //
    // The function returns an error if the parameter version creation fails.
    func createParamVersionWithSecret(w io.Writer, projectID, parameterID, versionID, secretID string) error {
    	// Create a context and a Parameter Manager client.
    	ctx := context.Background()
    	client, err := parametermanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create Parameter Manager client: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_Close)()
    
    	// Construct the name of the create parameter version.
    	parent := fmt.Sprintf("projects/%s/locations/global/parameters/%s", projectID, parameterID)
    
    	payload := []byte(fmt.Sprintf(`{"username": "test-user","password": "__REF__(//secretmanager.googleapis.com/%s)"}`, secretID))
    
    	// Build the request to create a new parameter version with the JSON payload that has a secret reference.
    	req := &parametermanagerpb.CreateParameterVersionRequest{
    		Parent:             parent,
    		ParameterVersionId: versionID,
    		ParameterVersion: &parametermanagerpb.ParameterVersion{
    			Payload: &parametermanagerpb.ParameterVersionPayload{
    				Data: payload,
    			},
    		},
    	}
    
    	// Call the API to create the parameter version.
    	version, err := client.CreateParameterVersion(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to create parameter version: %w", err)
    	}
    
    	fmt.Fprintf(w, "Created parameter version with secret reference: %s\n", version.Name)
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Parameter Manager Java SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-java). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    import com.google.cloud.parametermanager.v1.[ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html);
    import com.google.cloud.parametermanager.v1.[ParameterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterName.html);
    import com.google.cloud.parametermanager.v1.[ParameterVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersion.html);
    import com.google.cloud.parametermanager.v1.[ParameterVersionPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersionPayload.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    
    /**
     * This class demonstrates how to create a parameter version with a JSON payload that includes a
     * secret reference using the Parameter Manager SDK for GCP.
     */
    public class CreateParamVersionWithSecret {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String parameterId = "your-parameter-id";
        String versionId = "your-version-id";
        String secretId = "projects/your-project-id/secrets/your-secret-id/versions/latest";
    
        // Call the method to create parameter version with JSON payload that includes a secret
        // reference.
        createParamVersionWithSecret(projectId, parameterId, versionId, secretId);
      }
    
      // This is an example snippet that creates a parameter version with a JSON payload that includes a
      // secret reference.
      public static [ParameterVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersion.html) createParamVersionWithSecret(
          String projectId, String parameterId, String versionId, String secretId) throws IOException {
        // Initialize the client that will be used to send requests. This client only
        // needs to be created once, and can be reused for multiple requests.
        try ([ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html) client = [ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html).create()) {
          String locationId = "global";
    
          // Build the parameter name.
          [ParameterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterName.html) parameterName = [ParameterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterName.html).of(projectId, locationId, parameterId);
    
          // Convert the JSON payload string to ByteString.
          String payload =
              String.format(
                  "{\"username\": \"test-user\", "
                      + "\"password\": \"__REF__(//secretmanager.googleapis.com/%s)\"}",
                  secretId);
          [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) byteStringPayload = [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFromUtf8](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFromUtf8_java_lang_String_)(payload);
    
          // Create the parameter version payload with the secret reference.
          [ParameterVersionPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersionPayload.html) parameterVersionPayload =
              [ParameterVersionPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersionPayload.html).newBuilder().setData(byteStringPayload).build();
    
          // Create the parameter version with the JSON payload.
          [ParameterVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersion.html) parameterVersion =
              [ParameterVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersion.html).newBuilder().setPayload(parameterVersionPayload).build();
    
          // Create the parameter version in the Parameter Manager.
          [ParameterVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersion.html) createdParameterVersion =
              client.createParameterVersion(parameterName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterName.html#com_google_cloud_parametermanager_v1_ParameterName_toString__)(), parameterVersion, versionId);
          System.out.printf("Created parameter version: %s\n", createdParameterVersion.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersion.html#com_google_cloud_parametermanager_v1_ParameterVersion_getName__)());
    
          return createdParameterVersion;
        }
      }
    }

### Node.js

To run this code, first [set up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup) and [install the Parameter Manager Node.js SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-nodejs). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const parameterId = 'YOUR_PARAMETER_ID';
    // const parameterVersionId = 'YOUR_PARAMETER_VERSION_ID';
    // const secretId = 'YOUR_SECRET_ID'; // For example projects/my-project/secrets/application-secret/version/latest
    
    // Imports the Parameter Manager library
    const {ParameterManagerClient} = require('[@google-cloud/parametermanager](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)');
    
    // Instantiates a client
    const client = new [ParameterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)();
    
    async function createParamVersionWithSecret() {
      // Construct the parent resource name
      const parent = client.[parameterPath](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/parametermanager/v1.parametermanagerclient.html)(projectId, 'global', parameterId);
    
      // Construct the JSON data with secret references
      const jsonData = {
        db_user: 'test_user',
        db_password: `__REF__(//secretmanager.googleapis.com/${secretId})`,
      };
    
      // Construct the parameter version
      const parameterVersion = {
        payload: {
          data: Buffer.from([JSON](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/parametermanager/protos.google.cloud.parametermanager.v1.parameterformat.html).stringify(jsonData), 'utf8'),
        },
      };
    
      // Construct the request
      const request = {
        parent: parent,
        parameterVersionId: parameterVersionId,
        parameterVersion: parameterVersion,
      };
    
      // Create the parameter version
      const [paramVersion] = await client.createParameterVersion(request);
      console.log(
        `Created parameter version with secret references: ${paramVersion.name}`
      );
      return paramVersion;
    }
    
    return await createParamVersionWithSecret();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Parameter Manager PHP SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-php). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    // Import necessary classes for creating a parameter version.
    use Google\Cloud\ParameterManager\V1\Client\ParameterManagerClient;
    use Google\Cloud\ParameterManager\V1\CreateParameterVersionRequest;
    use Google\Cloud\ParameterManager\V1\ParameterVersion;
    use Google\Cloud\ParameterManager\V1\ParameterVersionPayload;
    
    /**
     * Creates a parameter version with an secret reference.
     *
     * @param string $projectId The Google Cloud Project ID (e.g. 'my-project')
     * @param string $parameterId The Parameter ID (e.g. 'my-param')
     * @param string $versionId The Version ID (e.g. 'my-param-version')
     * @param string $secretId The ID of the secret to be referenced (e.g. 'projects/my-project/secrets/my-secret/versions/latest')
     */
    function create_param_version_with_secret(string $projectId, string $parameterId, string $versionId, string $secretId): void
    {
        // Create a client for the Parameter Manager service.
        $client = new ParameterManagerClient();
    
        // Build the resource name of the parent object.
        $parent = $client->parameterName($projectId, 'global', $parameterId);
    
        // Build payload.
        $payload = json_encode([
            'username' => 'test-user',
            'password' => sprintf('__REF__(//secretmanager.googleapis.com/%s)', $secretId)
        ], JSON_UNESCAPED_SLASHES);
    
        // Create a new ParameterVersionPayload object and set the payload with secret reference.
        $parameterVersionPayload = new ParameterVersionPayload();
        $parameterVersionPayload->setData($payload);
    
        // Create a new ParameterVersion object and set the payload.
        $parameterVersion = new ParameterVersion();
        $parameterVersion->setPayload($parameterVersionPayload);
    
        // Prepare the request with the parent and parameter version object.
        $request = (new CreateParameterVersionRequest())
            ->setParent($parent)
            ->setParameterVersionId($versionId)
            ->setParameterVersion($parameterVersion);
    
        // Call the API to create the parameter version.
        $newParameterVersion = $client->createParameterVersion($request);
        printf('Created parameter version: %s' . PHP_EOL, $newParameterVersion->getName());
    }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Parameter Manager Python SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-python). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    def create_param_version_with_secret(
        project_id: str, parameter_id: str, version_id: str, secret_id: str
    ) -> parametermanager_v1.ParameterVersion:
        """
        Creates a new version of an existing parameter in the global location
        of the specified project using the Google Cloud Parameter Manager SDK.
        The payload is specified as a JSON string and
        includes a reference to a secret.
    
        Args:
            project_id (str): The ID of the project where the parameter is located.
            parameter_id (str): The ID of the parameter for
            which the version is to be created.
            version_id (str): The ID of the version to be created.
            secret_id (str): The ID of the secret to be referenced.
    
        Returns:
            parametermanager_v1.ParameterVersion: An object representing the
            newly created parameter version.
    
        Example:
            create_param_version_with_secret(
                "my-project",
                "my-global-parameter",
                "v1",
                "projects/my-project/secrets/application-secret/versions/latest"
            )
        """
        # Import the necessary library for Google Cloud Parameter Manager.
        from google.cloud import [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest)
        import json
    
        # Create the Parameter Manager client.
        client = [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[ParameterManagerClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html)()
    
        # Build the resource name of the parameter.
        parent = client.[parameter_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_parameter_path)(project_id, "global", parameter_id)
    
        # Create the JSON payload with a secret reference.
        payload_dict = {
            "username": "test-user",
            "password": f"__REF__('//secretmanager.googleapis.com/{secret_id}')",
        }
        payload_json = json.dumps(payload_dict)
    
        # Define the parameter version creation request with the JSON payload.
        request = [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[CreateParameterVersionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.CreateParameterVersionRequest.html)(
            parent=parent,
            parameter_version_id=version_id,
            parameter_version=[parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[ParameterVersion](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.ParameterVersion.html)(
                payload=[parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[ParameterVersionPayload](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.ParameterVersionPayload.html)(
                    data=payload_json.encode("utf-8")
                )
            ),
        )
    
        # Create the parameter version.
        response = client.[create_parameter_version](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_create_parameter_version)(request=request)
    
        # Print the newly created parameter version name.
        print(f"Created parameter version: {response.name}")

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Parameter Manager Ruby SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-ruby). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    require "google/cloud/parameter_manager"
    
    ##
    # Create a parameter version
    #
    # @param project_id [String] The Google Cloud project (e.g. "my-project")
    # @param parameter_id [String] The parameter name (e.g. "my-parameter")
    # @param version_id [String] The version name (e.g. "my-version")
    # @param secret_id [String] The secret name
    # (e.g. "projects/my-project/secrets/my-secret/versions/latest")
    #
    def create_param_version_with_secret project_id:, parameter_id:, version_id:, secret_id:
      # Create a Parameter Manager client.
      client = Google::Cloud::[ParameterManager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager/latest/Google-Cloud-ParameterManager.html).[parameter_manager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager/latest/Google-Cloud-ParameterManager.html)
    
      # Build the resource name of the parent project.
      parent = client.[parameter_path](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager-V1-ParameterManager-Paths.html) project: project_id, location: "global", parameter: parameter_id
    
      payload = "{\"username\": \"test-user\", \"password\": \"__REF__(//secretmanager.googleapis.com/#{secret_id})\"}"
      parameter_version = {
        payload: {
          data: payload
        }
      }
    
      # Create the parameter version.
      param_version = client.create_parameter_version parent: parent, parameter_version_id: version_id,
                                                      parameter_version: parameter_version
    
      # Print the new parameter version name.
      puts "Created parameter version #{param_version.name}"
    end

**Regional parameters**

### Console

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. Click **Parameter Manager** to go to the **Parameter Manager** page.

  3. Click the parameter name that you want to add the new version. The parameter details are displayed.

  4. Click the **Versions** tab and then click **New version**. The **Create parameter version** page opens.

  5. Enter the version name. Parameter version names can be up to 63 characters long, can contain letters (both upper and lowercase), numbers, hyphens (-), and underscores (_), but cannot start with a hyphen.

  6. In the **Payload** section, enter the parameter value containing the secret reference using one of the following methods:

     * **Option 1: upload a file**
       1. Click **Browse**.

       2. Select a file containing the parameter value with the secret reference.

     * **Option 2: enter the payload manually**
       1. Enter the parameter value containing the secret reference in the payload text area.

Ensure that the secret uses the special reference (`__REF__()`) format.

     * **Option 3: dynamically insert a secret**
       1. Enter the parameter value in the payload text area.

       2. Navigate to the field that contains the secret reference, press **Ctrl** \+ **Space** , and then press **Enter**. The **Secret picker** side panel appears.

       3. Select the **Secret** and the **Secret version**. Optionally, enable the **Select regional secret** toggle to select a regional secret.

Alternatively, you can either [enter the secret manually](https://docs.cloud.google.com/secret-manager/docs/view-secret-details) by specifying the resource ID or [create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets).

       4. Click **Insert**.

  7. Click **Create**.




### gcloud

Before using any of the command data below, make the following replacements: 

  * PARAMETER_VERSION_ID: the ID that you want to assign to the parameter version. Parameter version IDs must be 63 characters or less and consist only of alphanumeric characters (A-Z, a-z, 0-9), dashes (-), and underscores (_). IDs cannot begin with a dash.
  * PARAMETER_ID: the name of the parameter.
  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the parameter.
  * PARAMETER_PAYLOAD: the data, in plaintext, containing the secret references that you want to store within the parameter version.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters versions create PARAMETER_VERSION_ID --parameter=PARAMETER_ID --location=LOCATION --payload-data="PARAMETER_PAYLOAD" --project=PROJECT_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters versions create PARAMETER_VERSION_ID --parameter=PARAMETER_ID --location=LOCATION --payload-data="PARAMETER_PAYLOAD" --project=PROJECT_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters versions create PARAMETER_VERSION_ID --parameter=PARAMETER_ID --location=LOCATION --payload-data="PARAMETER_PAYLOAD" --project=PROJECT_ID

You should receive a response similar to the following:
    
    
    Created parameterVersion [refv2].

### REST

Before using any of the request data, make the following replacements: 

  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the parameter.
  * PROJECT_ID: the Google Cloud project ID.
  * PARAMETER_ID: the name of the parameter.
  * PARAMETER_VERSION_ID: the ID that you want to assign to the parameter version. Parameter version IDs must be 63 characters or less and consist only of alphanumeric characters (A-Z, a-z, 0-9), dashes (-), and underscores (_). IDs cannot begin with a dash.
  * PARAMETER_PAYLOAD: the data, as a Base64 encoded string, containing the secret references that you want to store within the parameter version.



HTTP method and URL: 
    
    
    POST https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID/versions?parameter_version_id=PARAMETER_VERSION_ID

Request JSON body: 
    
    
    {"payload": {"data": "PARAMETER_PAYLOAD"}}
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID/versions?parameter_version_id=PARAMETER_VERSION_ID"

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
        -Uri "https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID/versions?parameter_version_id=PARAMETER_VERSION_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/production-1/locations/us-central1/parameters/db_password_secret_ref/versions/refv2",
      "createTime": "2024-10-15T08:39:05.191747694Z",
      "updateTime": "2024-10-15T08:39:05.191747694Z"
    }
    
    

### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Parameter Manager C# SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-csharp). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    using [Google.Cloud.ParameterManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.html);
    using [Google.Protobuf](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.html);
    using System.Text;
    
    
    public class CreateRegionalParameterVersionWithSecretSample
    {
        /// <summary>
        /// This function creates a regional parameter version with a JSON payload that includes a secret reference using the Parameter Manager SDK for GCP.
        /// </summary>
        /// <param name="projectId">The ID of the project where the parameter is located.</param>
        /// <param name="locationId">The ID of the region where the parameter is located.</param>
        /// <param name="parameterId">The ID of the parameter for which the version is to be created.</param>
        /// <param name="versionId">The ID of the version to be created.</param>
        /// <param name="secretId">The ID of the secret to be referenced.</param>
        /// <returns>The created ParameterVersion object.</returns>
        public ParameterVersion CreateRegionalParameterVersionWithSecret(
            string projectId,
            string locationId,
            string parameterId,
            string versionId,
            string secretId)
        {
            // Define the regional endpoint
            string regionalEndpoint = $"parametermanager.{locationId}.rep.googleapis.com";
    
            // Create the client with the regional endpoint
            [ParameterManagerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html) client = new [ParameterManagerClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClientBuilder.html)
            {
                Endpoint = regionalEndpoint
            }.[Build](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClientBuilder.html#Google_Cloud_ParameterManager_V1_ParameterManagerClientBuilder_Build)();
    
            // Build the parent resource name using ParameterName
            [ParameterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterName.html) parent = new [ParameterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterName.html)(projectId, locationId, parameterId);
    
            // Convert the JSON payload to bytes
            string payload = $"{{\"username\": \"test-user\", \"password\": \"__REF__(//secretmanager.googleapis.com/{secretId}\"}}";
            [ByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html) data = [ByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html).[CopyFrom](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html#Google_Protobuf_ByteString_CopyFrom_System_Byte___)(payload, Encoding.UTF8);
    
            // Build the parameter version with the JSON payload that includes a secret reference
            [ParameterVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersion.html) parameterVersion = new [ParameterVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersion.html)
            {
                Payload = new [ParameterVersionPayload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionPayload.html)
                {
                    Data = data
                }
            };
    
            // Call the API to create the parameter version
            [ParameterVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersion.html) createdParameterVersion = client.[CreateParameterVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html#Google_Cloud_ParameterManager_V1_ParameterManagerClient_CreateParameterVersion_Google_Cloud_ParameterManager_V1_CreateParameterVersionRequest_Google_Api_Gax_Grpc_CallSettings_)(parent, parameterVersion, versionId);
    
            // Print the created parameter version name
            Console.WriteLine($"created regional parameter version: {createdParameterVersion.[Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersion.html#Google_Cloud_ParameterManager_V1_ParameterVersion_Name)}");
    
            // Return the created parameter version
            return createdParameterVersion;
        }
    }

### Go

To run this code, first [set up a Go development environment](https://docs.cloud.google.com/go/docs/setup) and [install the Parameter Manager Go SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-go). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	parametermanager "cloud.google.com/go/parametermanager/apiv1"
    	parametermanagerpb "cloud.google.com/go/parametermanager/apiv1/parametermanagerpb"
    	"google.golang.org/api/option"
    )
    
    // createRegionalParamVersionWithSecret creates a new version of a regional parameter with a JSON payload that has a secret reference in it using the Parameter Manager SDK for GCP.
    //
    // w: The io.Writer object used to write the output.
    // projectID: The ID of the project where the parameter is located.
    // locationID: The ID of the region where the parameter is located.
    // parameterID: The ID of the parameter for which the version is to be created.
    // versionID: The ID of the version to be created.
    // secretID: The ID of the secret to be referenced.
    //
    // The function returns an error if the parameter version creation fails.
    func createRegionalParamVersionWithSecret(w io.Writer, projectID, locationID, parameterID, versionID, secretID string) error {
    	// Create a context.
    	ctx := context.Background()
    
    	// Create a Parameter Manager client.
    	endpoint := fmt.Sprintf("parametermanager.%s.rep.googleapis.com:443", locationID)
    	client, err := parametermanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_NewClient)(ctx, option.WithEndpoint(endpoint))
    	if err != nil {
    		return fmt.Errorf("failed to create parametermanager client: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_Close)()
    
    	// Construct the name of the create parameter version.
    	parent := fmt.Sprintf("projects/%s/locations/%s/parameters/%s", projectID, locationID, parameterID)
    
    	payload := []byte(fmt.Sprintf(`{"db_host": "localhost","db_password": "__REF__(//secretmanager.googleapis.com/%s)"}`, secretID))
    
    	// Create a parameter version.
    	req := &parametermanagerpb.CreateParameterVersionRequest{
    		Parent:             parent,
    		ParameterVersionId: versionID,
    		ParameterVersion: &parametermanagerpb.ParameterVersion{
    			Payload: &parametermanagerpb.ParameterVersionPayload{
    				Data: payload,
    			},
    		},
    	}
    	version, err := client.CreateParameterVersion(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to create parameter version: %w", err)
    	}
    	fmt.Fprintf(w, "Created regional parameter version with secret reference: %s\n", version.Name)
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Parameter Manager Java SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-java). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    import com.google.cloud.parametermanager.v1.[ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html);
    import com.google.cloud.parametermanager.v1.[ParameterManagerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerSettings.html);
    import com.google.cloud.parametermanager.v1.[ParameterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterName.html);
    import com.google.cloud.parametermanager.v1.[ParameterVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersion.html);
    import com.google.cloud.parametermanager.v1.[ParameterVersionPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersionPayload.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    
    /**
     * This class demonstrates how to create a regional parameter version with a JSON payload that
     * includes a secret reference using the Parameter Manager SDK for GCP.
     */
    public class CreateRegionalParamVersionWithSecret {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "your-location-id";
        String parameterId = "your-parameter-id";
        String versionId = "your-version-id";
        String secretId =
            "projects/your-project-id/locations/your-location-id"
                + "/secrets/your-secret-id/versions/latest";
    
        // Call the method to create a regional parameter version with JSON payload that includes a
        // secret reference.
        createRegionalParamVersionWithSecret(projectId, locationId, parameterId, versionId, secretId);
      }
    
      // This is an example snippet that creates a regional parameter version with a JSON payload that
      // includes a secret reference.
      public static [ParameterVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersion.html) createRegionalParamVersionWithSecret(
          String projectId, String locationId, String parameterId, String versionId, String secretId)
          throws IOException {
        // Endpoint to call the regional parameter manager server
        String apiEndpoint = String.format("parametermanager.%s.rep.googleapis.com:443", locationId);
        [ParameterManagerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerSettings.html) parameterManagerSettings =
            [ParameterManagerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerSettings.html).newBuilder().setEndpoint(apiEndpoint).build();
    
        // Initialize the client that will be used to send requests. This client only
        // needs to be created once, and can be reused for multiple requests.
        try ([ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html) client = [ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html).create(parameterManagerSettings)) {
          // Build the parameter name.
          [ParameterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterName.html) parameterName = [ParameterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterName.html).of(projectId, locationId, parameterId);
    
          // Convert the JSON payload string to ByteString.
          String payload =
              String.format(
                  "{\"username\": \"test-user\","
                      + "\"password\": \"__REF__(//secretmanager.googleapis.com/%s)\"}",
                  secretId);
          [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) byteStringPayload = [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFromUtf8](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFromUtf8_java_lang_String_)(payload);
    
          // Create the parameter version payload with the secret reference.
          [ParameterVersionPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersionPayload.html) parameterVersionPayload =
              [ParameterVersionPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersionPayload.html).newBuilder().setData(byteStringPayload).build();
    
          // Create the parameter version with the JSON payload.
          [ParameterVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersion.html) parameterVersion =
              [ParameterVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersion.html).newBuilder().setPayload(parameterVersionPayload).build();
    
          // Create the parameter version in the Parameter Manager.
          [ParameterVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersion.html) createdParameterVersion =
              client.createParameterVersion(parameterName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterName.html#com_google_cloud_parametermanager_v1_ParameterName_toString__)(), parameterVersion, versionId);
          System.out.printf(
              "Created regional parameter version: %s\n", createdParameterVersion.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersion.html#com_google_cloud_parametermanager_v1_ParameterVersion_getName__)());
    
          return createdParameterVersion;
        }
      }
    }

### Node.js

To run this code, first [set up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup) and [install the Parameter Manager Node.js SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-nodejs). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const locationId = 'us-central1';
    // const parameterId = 'YOUR_PARAMETER_ID';
    // const parameterVersionId = 'YOUR_PARAMETER_VERSION_ID';
    // const secretId = 'YOUR_SECRET_ID'; // For example projects/my-project/secrets/application-secret/version/latest
    
    // Imports the Parameter Manager library
    const {ParameterManagerClient} = require('[@google-cloud/parametermanager](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)');
    
    // Adding the endpoint to call the regional parameter manager server
    const options = {
      apiEndpoint: `parametermanager.${locationId}.rep.googleapis.com`,
    };
    
    // Instantiates a client with regional endpoint
    const client = new [ParameterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)(options);
    
    async function createRegionalParamVersionWithSecret() {
      // Construct the parent resource name
      const parent = client.[parameterPath](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/parametermanager/v1.parametermanagerclient.html)(projectId, locationId, parameterId);
    
      // Construct the payload JSON data with secret references
      const payloadData = {
        db_user: 'test_user',
        db_password: `__REF__("//secretmanager.googleapis.com/${secretId}")`,
      };
    
      // Construct the parameter version
      const parameterVersion = {
        payload: {
          data: Buffer.from([JSON](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/parametermanager/protos.google.cloud.parametermanager.v1.parameterformat.html).stringify(payloadData), 'utf8'),
        },
      };
    
      // Construct the request
      const request = {
        parent: parent,
        parameterVersionId: parameterVersionId,
        parameterVersion: parameterVersion,
      };
    
      // Create the regional parameter version
      const [paramVersion] = await client.createParameterVersion(request);
      console.log(
        `Created regional parameter version with secret: ${paramVersion.name}`
      );
      return paramVersion;
    }
    
    return await createRegionalParamVersionWithSecret();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Parameter Manager PHP SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-php). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    // Import necessary classes for creating a parameter version.
    use Google\Cloud\ParameterManager\V1\Client\ParameterManagerClient;
    use Google\Cloud\ParameterManager\V1\CreateParameterVersionRequest;
    use Google\Cloud\ParameterManager\V1\ParameterVersion;
    use Google\Cloud\ParameterManager\V1\ParameterVersionPayload;
    
    /**
     * Creates a regional parameter version with an secret reference.
     *
     * @param string $projectId The Google Cloud Project ID (e.g. 'my-project')
     * @param string $locationId The Parameter Location (e.g. 'us-central1')
     * @param string $parameterId The Parameter ID (e.g. 'my-param')
     * @param string $versionId The Version ID (e.g. 'my-param-version')
     * @param string $secretId The ID of the secret to be referenced (e.g. 'projects/my-project/locations/us-central1/secrets/my-secret/versions/latest')
     */
    function create_regional_param_version_with_secret(string $projectId, string $locationId, string $parameterId, string $versionId, string $secretId): void
    {
        // Specify regional endpoint.
        $options = ['apiEndpoint' => "parametermanager.$locationId.rep.googleapis.com"];
    
        // Create a client for the Parameter Manager service.
        $client = new ParameterManagerClient($options);
    
        // Build the resource name of the parent object.
        $parent = $client->parameterName($projectId, $locationId, $parameterId);
    
        // Build payload.
        $payload = json_encode([
            'username' => 'test-user',
            'password' => sprintf('__REF__(//secretmanager.googleapis.com/%s)', $secretId)
        ], JSON_UNESCAPED_SLASHES);
    
        // Create a new ParameterVersionPayload object and set the payload with secret reference.
        $parameterVersionPayload = new ParameterVersionPayload();
        $parameterVersionPayload->setData($payload);
    
        // Create a new ParameterVersion object and set the payload.
        $parameterVersion = new ParameterVersion();
        $parameterVersion->setPayload($parameterVersionPayload);
    
        // Prepare the request with the parent and parameter version object.
        $request = (new CreateParameterVersionRequest())
            ->setParent($parent)
            ->setParameterVersionId($versionId)
            ->setParameterVersion($parameterVersion);
    
        // Call the API to create the parameter version.
        $newParameterVersion = $client->createParameterVersion($request);
        printf('Created regional parameter version: %s' . PHP_EOL, $newParameterVersion->getName());
    }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Parameter Manager Python SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-python). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    def create_regional_param_version_with_secret(
        project_id: str,
        location_id: str,
        parameter_id: str,
        version_id: str,
        secret_id: str,
    ) -> parametermanager_v1.ParameterVersion:
        """
        Creates a new version of an existing parameter in the specified region
        of the specified project using the Google Cloud Parameter Manager SDK.
        The payload is specified as a JSON string and
        includes a reference to a secret.
    
        Args:
            project_id (str): The ID of the project where the parameter is located.
            location_id (str): The ID of the region where the parameter is located.
            parameter_id (str): The ID of the parameter for
            which the version is to be created.
            version_id (str): The ID of the version to be created.
            secret_id (str): The ID of the secret to be referenced.
    
        Returns:
            parametermanager_v1.ParameterVersion: An object representing the
            newly created parameter version.
    
        Example:
            create_regional_param_version_with_secret(
                "my-project",
                "us-central1",
                "my-regional-parameter",
                "v1",
                "projects/my-project/locations/us-central1/secrets/application-secret/versions/latest"
            )
        """
        # Import the necessary library for Google Cloud Parameter Manager.
        from google.cloud import [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest)
        import json
    
        # Create the Parameter Manager client with the regional endpoint.
        api_endpoint = f"parametermanager.{location_id}.rep.googleapis.com"
        client = [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[ParameterManagerClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html)(
            client_options={"api_endpoint": api_endpoint}
        )
    
        # Build the resource name of the parameter.
        parent = client.[parameter_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_parameter_path)(project_id, location_id, parameter_id)
    
        # Create the JSON payload with a secret reference.
        payload_dict = {
            "username": "test-user",
            "password": f"__REF__('//secretmanager.googleapis.com/{secret_id}')",
        }
        payload_json = json.dumps(payload_dict)
    
        # Define the parameter version creation request with the JSON payload.
        request = [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[CreateParameterVersionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.CreateParameterVersionRequest.html)(
            parent=parent,
            parameter_version_id=version_id,
            parameter_version=[parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[ParameterVersion](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.ParameterVersion.html)(
                payload=[parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[ParameterVersionPayload](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.ParameterVersionPayload.html)(
                    data=payload_json.encode("utf-8")
                )
            ),
        )
    
        # Create the parameter version.
        response = client.[create_parameter_version](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_create_parameter_version)(request=request)
    
        # Print the newly created parameter version name.
        print(f"Created regional parameter version: {response.name}")

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Parameter Manager Ruby SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-ruby). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    require "google/cloud/parameter_manager"
    
    ##
    # Create a regional parameter version
    #
    # @param project_id [String] The Google Cloud project (e.g. "my-project")
    # @param location_id [String] The location name (e.g. "us-central1")
    # @param parameter_id [String] The parameter name (e.g. "my-parameter")
    # @param version_id [String] The version name (e.g. "my-version")
    # @param secret_id [String] The secret name
    # (e.g. "projects/my-project/locations/us-central1/secrets/my-secret/versions/latest")
    #
    def create_regional_param_version_with_secret project_id:, location_id:, parameter_id:, version_id:, secret_id:
      # Endpoint for the regional parameter manager service.
      api_endpoint = "parametermanager.#{location_id}.rep.googleapis.com"
    
      # Create the Parameter Manager client.
      client = Google::Cloud::[ParameterManager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager/latest/Google-Cloud-ParameterManager.html).[parameter_manager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager/latest/Google-Cloud-ParameterManager.html) do |config|
        config.endpoint = api_endpoint
      end
    
      # Build the resource name of the parent project.
      parent = client.[parameter_path](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager-V1-ParameterManager-Paths.html) project: project_id, location: location_id, parameter: parameter_id
    
      payload = "{\"username\": \"test-user\", \"password\": \"__REF__(//secretmanager.googleapis.com/#{secret_id})\"}"
      parameter_version = {
        payload: {
          data: payload
        }
      }
    
      # Create the parameter version.
      param_version = client.create_parameter_version parent: parent, parameter_version_id: version_id,
                                                      parameter_version: parameter_version
    
      # Print the new parameter version name.
      puts "Created regional parameter version #{param_version.name}"
    end

## Grant the Secret Manager Secret Accessor role to the parameter

To let a parameter access a secret stored in Secret Manager, grant the Secret Manager Secret Accessor role (`roles/secretmanager.secretAccessor`) to the parameter. This gives the parameter permission to read the secret's value. Parameters are resources with [built-in identities](https://docs.cloud.google.com/iam/docs/built-in-resource-identities), which means that you must [grant the IAM role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) using the [resource's principal identifier](https://docs.cloud.google.com/iam/docs/resources-with-built-in-identities). Refer to the following example to grant the role using the Google Cloud CLI:

### gcloud

Before using any of the command data below, make the following replacements: 

  * PROJECT_ID: the ID of the project containing the secret
  * SECRET_ID: the ID of the secret or fully qualified identifier for the secret
  * PROJECT_NUMBER: the project number of the Google Cloud project where the parameter is stored
  * PARAMETER_UID: the system-generated unique ID of the parameter



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets add-iam-policy-binding projects/PROJECT_ID/secrets/SECRET_ID --member="principal://parametermanager.googleapis.com/projects/PROJECT_NUMBER/uid/locations/global/parameters/PARAMETER_UID" --role="roles/secretmanager.secretAccessor"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets add-iam-policy-binding projects/PROJECT_ID/secrets/SECRET_ID --member="principal://parametermanager.googleapis.com/projects/PROJECT_NUMBER/uid/locations/global/parameters/PARAMETER_UID" --role="roles/secretmanager.secretAccessor"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud secrets add-iam-policy-binding projects/PROJECT_ID/secrets/SECRET_ID --member="principal://parametermanager.googleapis.com/projects/PROJECT_NUMBER/uid/locations/global/parameters/PARAMETER_UID" --role="roles/secretmanager.secretAccessor"

You should receive a response similar to the following:
    
    
    Updated IAM policy for secret [db_password].
    bindings:
    - members:
      - principal://parametermanager.googleapis.com/projects/609765466568/uid/locations/global/parameters/3fe3492e-a0da-4447-8d6b-68b4594b7243
      role: roles/secretmanager.secretAccessor
    etag: BwYkj3X1kGo=
    version: 1
    

For information on rendering secret references when retrieving parameter payloads, see [Render secrets referenced within a parameter version](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/render-parameter-version).

## What's next

  * [List and view parameter details](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/list-parameter)
  * [Edit a parameter](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/edit-parameter)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
