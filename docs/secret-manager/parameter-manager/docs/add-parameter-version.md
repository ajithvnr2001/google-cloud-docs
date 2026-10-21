---
url: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/add-parameter-version/
title: Add a parameter version \u00a0|\u00a0 Parameter Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:09:40.440487+00:00
---

# Add a parameter version  |  Parameter Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/add-parameter-version/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Parameter Manager ](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/overview)



Send feedback 

#  Add a parameter version Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to add a parameter version. A parameter version stores the actual value of the parameter, whether it's a string, a number, or more complex data.

By creating parameter versions, you can do the following:

  * Track changes to your parameter values over time.
  * Rollback to previous values when required.
  * Maintain an audit trail to see who made changes to the parameters and when.



## Required roles

To get the permissions that you need to add a parameter version, ask your administrator to grant you the [Parameter Manager Parameter Version Adder ](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.parameterVersionAdder) (`roles/parametermanager.parameterVersionAdder`) IAM role on the parameter. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Add a parameter version

Parameter Manager lets you create multiple versions of a parameter. The version contains the actual data or value associated with the parameter. In the context of Parameter Manager, we'll call this data the _parameter payload_.

To add a new version, use one of the following methods:

**Global parameters**

### Console

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. Click **Parameter Manager** to go to the **Parameter Manager** page. You'll see the list of parameters for that project.

  3. Select the parameter for which you want to add the new version.

  4. Click the more_vert**Actions** menu associated with that parameter, and then click **Add new version**. The **Create parameter version** page appears.

  5. Enter the version name. Parameter version names must be 63 characters or less and consist only of alphanumeric characters (A-Z, a-z, 0-9), dashes (-), and underscores (_). Names cannot begin with a dash.

  6. In the **Payload** section, enter a value for the parameter. Alternatively, you can upload a file containing the parameter value, and then edit the values in the payload editor. The parameter value must be in the format specified for the parameter.

  7. Click **Create**.




### gcloud

Before using any of the command data below, make the following replacements: 

  * PARAMETER_VERSION_ID: the ID that you want to assign to the parameter version. Parameter version IDs must be 63 characters or less and consist only of alphanumeric characters (A-Z, a-z, 0-9), dashes (-), and underscores (_). IDs cannot begin with a dash.
  * PARAMETER_ID: the name of the parameter.
  * PARAMETER_PAYLOAD: the data, in plaintext, that you want to store within the parameter.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters versions create PARAMETER_VERSION_ID --parameter=PARAMETER_ID --location=global --payload-data="PARAMETER_PAYLOAD"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters versions create PARAMETER_VERSION_ID --parameter=PARAMETER_ID --location=global --payload-data="PARAMETER_PAYLOAD"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters versions create PARAMETER_VERSION_ID --parameter=PARAMETER_ID --location=global --payload-data="PARAMETER_PAYLOAD"

You should receive a response similar to the following:
    
    
    Created parameterVersion [set1].

### REST

Encode the raw parameter data to Base64 format.
    
    
    $ PARAMETER_PAYLOAD=$(echo "a: b" | base64 -w0)
    

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID.
  * PARAMETER_ID: the name of parameter.
  * PARAMETER_VERSION_ID: the ID that you want to assign to the parameter version. Parameter version IDs must be 63 characters or less and consist only of alphanumeric characters (A-Z, a-z, 0-9), dashes (-), and underscores (_). IDs cannot begin with a dash.
  * PARAMETER_PAYLOAD: the Base64 encoded string corresponding to the data that you want to store within the parameter.



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
      "name": "projects/production-1/locations/global/parameters/intrusion_detection_rules/versions/set1",
      "createTime": "2024-11-12T10:26:44.168165094Z",
      "updateTime": "2024-11-12T10:26:44.168165094Z",
      "payload": {
        "data": "QSBzdHJpbmcgYmxvYiBjYW4gYmUgc3RvcmVkIGluIHRoZSB1bmZvcm1hdHRlZCBwYXJhbWV0ZXIu"
      }
    }
    
    

### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Parameter Manager C# SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-csharp). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    using [Google.Cloud.ParameterManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.html);
    using [Google.Protobuf](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.html);
    using System.Text;
    
    public class CreateParameterVersionSample
    {
        /// <summary>
        /// This function creates a parameter version with an unformatted payload using the Parameter Manager SDK for GCP.
        /// </summary>
        /// <param name="projectId">The ID of the project where the parameter is located.</param>
        /// <param name="parameterId">The ID of the parameter for which the version is to be created.</param>
        /// <param name="versionId">The ID of the version to be created.</param>
        /// <returns>The created ParameterVersion object.</returns>
        public ParameterVersion CreateParameterVersion(
            string projectId,
            string parameterId,
            string versionId)
        {
            // Create the client.
            [ParameterManagerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html) client = [ParameterManagerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html#Google_Cloud_ParameterManager_V1_ParameterManagerClient_Create)();
    
            // Build the parent resource name.
            [ParameterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterName.html) parent = new [ParameterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterName.html)(projectId, "global", parameterId);
    
            // Convert the payload to bytes.
            string payload = "test123";
            [ByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html) data = [ByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html).[CopyFrom](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html#Google_Protobuf_ByteString_CopyFrom_System_Byte___)(payload, Encoding.UTF8);
    
            // Build the parameter version with the unformatted payload.
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
    
    // createParamVersion creates a new version of a parameter with an unformatted payload in Parameter Manager.
    //
    // w: The io.Writer object used to write the output.
    // projectID: The ID of the project where the parameter is located.
    // parameterID: The ID of the parameter for which the version is to be created.
    // versionID: The ID of the version to be created.
    // payload: The unformatted string payload to be stored in the new parameter version.
    //
    // The function returns an error if the parameter version creation fails.
    func createParamVersion(w io.Writer, projectID, parameterID, versionID, payload string) error {
    	// Create a context and a Parameter Manager client.
    	ctx := context.Background()
    	client, err := parametermanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create Parameter Manager client: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_Close)()
    
    	// Construct the name of the create parameter version.
    	parent := fmt.Sprintf("projects/%s/locations/global/parameters/%s", projectID, parameterID)
    
    	// Build the request to create a new parameter version with the unformatted payload.
    	req := &parametermanagerpb.CreateParameterVersionRequest{
    		Parent:             parent,
    		ParameterVersionId: versionID,
    		ParameterVersion: &parametermanagerpb.ParameterVersion{
    			Payload: &parametermanagerpb.ParameterVersionPayload{
    				Data: []byte(payload), // Set the unformatted payload data.
    			},
    		},
    	}
    
    	// Call the API to create the parameter version.
    	version, err := client.CreateParameterVersion(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to create parameter version: %w", err)
    	}
    
    	fmt.Fprintf(w, "Created parameter version: %s\n", version.Name)
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
     * This class demonstrates how to create a parameter version with an unformatted payload using the
     * Parameter Manager SDK for GCP.
     */
    public class CreateParamVersion {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String parameterId = "your-parameter-id";
        String versionId = "your-version-id";
        String payload = "test123";
    
        // Call the method to create a parameter version with unformatted payload.
        createParamVersion(projectId, parameterId, versionId, payload);
      }
    
      // This is an example snippet that creates a parameter version with an unformatted payload.
      public static [ParameterVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersion.html) createParamVersion(
          String projectId, String parameterId, String versionId, String payload) throws IOException {
        // Initialize the client that will be used to send requests. This client only
        // needs to be created once, and can be reused for multiple requests.
        try ([ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html) client = [ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html).create()) {
          String locationId = "global";
    
          // Build the parameter name.
          [ParameterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterName.html) parameterName = [ParameterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterName.html).of(projectId, locationId, parameterId);
    
          // Convert the payload string to ByteString.
          [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) byteStringPayload = [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFromUtf8](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFromUtf8_java_lang_String_)(payload);
    
          // Create the parameter version payload.
          [ParameterVersionPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersionPayload.html) parameterVersionPayload =
              [ParameterVersionPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersionPayload.html).newBuilder().setData(byteStringPayload).build();
    
          // Create the parameter version with the unformatted payload.
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
    // const payload = 'This is unstructured data';
    
    // Imports the Parameter Manager library
    const {ParameterManagerClient} = require('[@google-cloud/parametermanager](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)');
    
    // Instantiates a client
    const client = new [ParameterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)();
    
    async function createParamVersion() {
      // Construct the parent resource name
      const parent = client.[parameterPath](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/parametermanager/v1.parametermanagerclient.html)(projectId, 'global', parameterId);
    
      // Construct the parameter version
      const parameterVersion = {
        payload: {
          data: Buffer.from(payload, 'utf8'),
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
      console.log(`Created parameter version: ${paramVersion.name}`);
      return paramVersion;
    }
    
    return await createParamVersion();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Parameter Manager PHP SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-php). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    // Import necessary classes for creating a parameter version.
    use Google\Cloud\ParameterManager\V1\Client\ParameterManagerClient;
    use Google\Cloud\ParameterManager\V1\CreateParameterVersionRequest;
    use Google\Cloud\ParameterManager\V1\ParameterVersion;
    use Google\Cloud\ParameterManager\V1\ParameterVersionPayload;
    
    /**
     * Creates a parameter version with an unformatted payload.
     *
     * @param string $projectId The Google Cloud Project ID (e.g. 'my-project')
     * @param string $parameterId The Parameter ID (e.g. 'my-param')
     * @param string $versionId The Version ID (e.g. 'my-param-version')
     * @param string $payload The unformatted string payload (e.g. 'test123')
     */
    function create_param_version(string $projectId, string $parameterId, string $versionId, string $payload): void
    {
        // Create a client for the Parameter Manager service.
        $client = new ParameterManagerClient();
    
        // Build the resource name of the parent object.
        $parent = $client->parameterName($projectId, 'global', $parameterId);
    
        // Create a new ParameterVersionPayload object and set the unformatted data.
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
    
    
    def create_param_version(
        project_id: str, parameter_id: str, version_id: str, payload: str
    ) -> parametermanager_v1.ParameterVersion:
        """
        Creates a new version of an existing parameter in the global location
        of the specified project using the Google Cloud Parameter Manager SDK.
        The payload is specified as an unformatted string.
    
        Args:
            project_id (str): The ID of the project where the parameter is located.
            parameter_id (str): The ID of the parameter for which
            the version is to be created.
            version_id (str): The ID of the version to be created.
            payload (str): The unformatted string payload
            to be stored in the new parameter version.
    
        Returns:
            parametermanager_v1.ParameterVersion: An object representing the
            newly created parameter version.
    
        Example:
            create_param_version(
                "my-project",
                "my-global-parameter",
                "v1",
                "my-unformatted-payload"
            )
        """
        # Import the necessary library for Google Cloud Parameter Manager.
        from google.cloud import [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest)
    
        # Create the Parameter Manager client.
        client = [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[ParameterManagerClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html)()
    
        # Build the resource name of the parameter.
        parent = client.[parameter_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_parameter_path)(project_id, "global", parameter_id)
    
        # Define the parameter version creation request with an unformatted payload.
        request = [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[CreateParameterVersionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.CreateParameterVersionRequest.html)(
            parent=parent,
            parameter_version_id=version_id,
            parameter_version=[parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[ParameterVersion](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.ParameterVersion.html)(
                payload=[parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[ParameterVersionPayload](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.ParameterVersionPayload.html)(
                    data=payload.encode("utf-8")  # Encoding the payload to bytes.
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
    # @param payload [String] The parameter payload (e.g. "test123")
    #
    def create_param_version project_id:, parameter_id:, version_id:, payload:
      # Create a Parameter Manager client.
      client = Google::Cloud::[ParameterManager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager.html).[parameter_manager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager/latest/Google-Cloud-ParameterManager.html)
    
      # Build the resource name of the parent project.
      parent = client.[parameter_path](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager-V1-ParameterManager-Paths.html) project: project_id, location: "global", parameter: parameter_id
    
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

  2. Click **Parameter Manager** to go to the **Parameter Manager** page. You'll see the list of parameters for that project.

  3. Select the parameter for which you want to add the new version.

  4. Click the more_vert**Actions** menu associated with that parameter, and then click **Add new version**. The **Create parameter version** page appears.

  5. Enter the version name. Parameter version names must be 63 characters or less and consist only of alphanumeric characters (A-Z, a-z, 0-9), dashes (-), and underscores (_). Names cannot begin with a dash.

  6. In the **Payload** section, enter a value for the parameter. Alternatively, you can upload a file containing the parameter value, and then edit the values in the payload editor. The parameter value must be in the format specified for the parameter.

  7. Click **Create**.




### gcloud

Before using any of the command data below, make the following replacements: 

  * PARAMETER_VERSION_ID: the ID that you want to assign to the parameter version. Parameter version IDs must be 63 characters or less and consist only of alphanumeric characters (A-Z, a-z, 0-9), dashes (-), and underscores (_). IDs cannot begin with a dash.
  * PARAMETER_ID: the name of the parameter.
  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the parameter.
  * PARAMETER_PAYLOAD: the data, in plaintext, that you want to store within the parameter.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters versions create PARAMETER_VERSION_ID --parameter=PARAMETER_ID --location=LOCATION --payload-data="PARAMETER_PAYLOAD"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters versions create PARAMETER_VERSION_ID --parameter=PARAMETER_ID --location=LOCATION --payload-data="PARAMETER_PAYLOAD"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters versions create PARAMETER_VERSION_ID --parameter=PARAMETER_ID --location=LOCATION --payload-data="PARAMETER_PAYLOAD"

You should receive a response similar to the following:
    
    
    Created parameterVersion [set1].

### REST

Encode the raw parameter data to Base64 format.
    
    
    $ PARAMETER_PAYLOAD=$(echo "a: b" | base64 -w0)
    

Before using any of the request data, make the following replacements: 

  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the parameter.
  * PROJECT_ID: the Google Cloud project ID.
  * PARAMETER_ID: the name of the parameter.
  * PARAMETER_VERSION_ID: the ID that you want to assign to the parameter version. Parameter version IDs must be 63 characters or less and consist only of alphanumeric characters (A-Z, a-z, 0-9), dashes (-), and underscores (_). IDs cannot begin with a dash.
  * PARAMETER_PAYLOAD: the Base64 encoded string corresponding to the data that you want to store within the parameter.



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
      "name": "projects/production-1/locations/us-central1/parameters/intrusion_detection_rules/versions/set1",
      "createTime": "2024-10-30T05:27:51.206825427Z",
      "updateTime": "2024-10-30T05:27:51.206825427Z",
      "payload": {
        "data": "YTogYgo="
      }
    }
    
    

### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Parameter Manager C# SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-csharp). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    using [Google.Cloud.ParameterManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.html);
    using [Google.Protobuf](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.html);
    using System.Text;
    
    
    public class CreateRegionalParameterVersionSample
    {
        /// <summary>
        /// This function creates a regional parameter version with an unformatted payload using the Parameter Manager SDK for GCP.
        /// </summary>
        /// <param name="projectId">The ID of the project where the parameter is located.</param>
        /// <param name="locationId">The ID of the region where the parameter is located.</param>
        /// <param name="parameterId">The ID of the parameter for which the version is to be created.</param>
        /// <param name="versionId">The ID of the version to be created.</param>
        /// <returns>The created ParameterVersion object.</returns>
        public ParameterVersion CreateRegionalParameterVersion(
            string projectId,
            string locationId,
            string parameterId,
            string versionId)
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
    
            // Convert the payload to bytes
            string payload = "test123";
            [ByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html) data = [ByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html).[CopyFrom](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html#Google_Protobuf_ByteString_CopyFrom_System_Byte___)(payload, Encoding.UTF8);
    
            // Build the parameter version with the unformatted payload
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
            Console.WriteLine($"Created regional parameter version: {createdParameterVersion.[Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersion.html#Google_Cloud_ParameterManager_V1_ParameterVersion_Name)}");
    
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
    
    // createRegionalParamVersion creates a new version of a regional parameter with an unformatted payload in Parameter Manager.
    //
    // w: The io.Writer object used to write the output.
    // projectID: The ID of the project where the parameter is located.
    // locationID: The ID of the region where the parameter is located.
    // parameterID: The ID of the parameter for which the version is to be created.
    // versionID: The ID of the version to be created.
    // payload: The unformatted string payload to be stored in the new parameter version.
    //
    // The function returns an error if the parameter version creation fails.
    func createRegionalParamVersion(w io.Writer, projectID, locationID, parameterID, versionID, payload string) error {
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
    
    	// Create a parameter version.
    	req := &parametermanagerpb.CreateParameterVersionRequest{
    		Parent:             parent,
    		ParameterVersionId: versionID,
    		ParameterVersion: &parametermanagerpb.ParameterVersion{
    			Payload: &parametermanagerpb.ParameterVersionPayload{
    				Data: []byte(payload),
    			},
    		},
    	}
    	version, err := client.CreateParameterVersion(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to create parameter version: %w", err)
    	}
    	fmt.Fprintf(w, "Created regional parameter version: %s\n", version.Name)
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
     * This class demonstrates how to create a regional parameter version with an unformatted payload
     * using the Parameter Manager SDK for GCP.
     */
    public class CreateRegionalParamVersion {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "your-location-id";
        String parameterId = "your-parameter-id";
        String versionId = "your-version-id";
        String payload = "test123";
    
        // Call the method to create a regional parameter version with unformatted payload.
        createRegionalParamVersion(projectId, locationId, parameterId, versionId, payload);
      }
    
      // This is an example snippet that creates a regional parameter version with an unformatted
      // payload.
      public static [ParameterVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersion.html) createRegionalParamVersion(
          String projectId, String locationId, String parameterId, String versionId, String payload)
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
    
          // Convert the payload string to ByteString.
          [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) byteStringPayload = [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFromUtf8](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFromUtf8_java_lang_String_)(payload);
    
          // Create the parameter version payload.
          [ParameterVersionPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersionPayload.html) parameterVersionPayload =
              [ParameterVersionPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersionPayload.html).newBuilder().setData(byteStringPayload).build();
    
          // Create the parameter version with the unformatted payload.
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
    // const payload = 'This is unstructured data';
    
    // Imports the Parameter Manager library
    const {ParameterManagerClient} = require('[@google-cloud/parametermanager](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)');
    
    // Adding the endpoint to call the regional parameter manager server
    const options = {
      apiEndpoint: `parametermanager.${locationId}.rep.googleapis.com`,
    };
    
    // Instantiates a client with regional endpoint
    const client = new [ParameterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)(options);
    
    async function createRegionalParamVersion() {
      // Construct the parent resource name
      const parent = client.[parameterPath](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/parametermanager/v1.parametermanagerclient.html)(projectId, locationId, parameterId);
    
      // Construct the parameter version
      const parameterVersion = {
        payload: {
          data: Buffer.from(payload, 'utf8'),
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
      console.log(`Created regional parameter version: ${paramVersion.name}`);
      return paramVersion;
    }
    
    return await createRegionalParamVersion();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Parameter Manager PHP SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-php). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    // Import necessary classes for creating a parameter version.
    use Google\Cloud\ParameterManager\V1\Client\ParameterManagerClient;
    use Google\Cloud\ParameterManager\V1\CreateParameterVersionRequest;
    use Google\Cloud\ParameterManager\V1\ParameterVersion;
    use Google\Cloud\ParameterManager\V1\ParameterVersionPayload;
    
    /**
     * Creates a regional parameter version with an unformatted payload.
     *
     * @param string $projectId The Google Cloud Project ID (e.g. 'my-project')
     * @param string $locationId The Parameter Location (e.g. 'us-central1')
     * @param string $parameterId The Parameter ID (e.g. 'my-param')
     * @param string $versionId The Version ID (e.g. 'my-param-version')
     * @param string $payload The unformatted string payload (e.g. 'test123')
     */
    function create_regional_param_version(string $projectId, string $locationId, string $parameterId, string $versionId, string $payload): void
    {
        // Specify regional endpoint.
        $options = ['apiEndpoint' => "parametermanager.$locationId.rep.googleapis.com"];
    
        // Create a client for the Parameter Manager service.
        $client = new ParameterManagerClient($options);
    
        // Build the resource name of the parent object.
        $parent = $client->parameterName($projectId, $locationId, $parameterId);
    
        // Create a new ParameterVersionPayload object and set the unformatted data.
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
    
    
    def create_regional_param_version(
        project_id: str, location_id: str, parameter_id: str, version_id: str, payload: str
    ) -> parametermanager_v1.ParameterVersion:
        """
        Creates a new version of an existing parameter in the specified region
        of the specified project using the Google Cloud Parameter Manager SDK.
        The payload is specified as an unformatted string.
    
        Args:
            project_id (str): The ID of the project where the parameter is located.
            location_id (str): The ID of the region where the parameter is located.
            parameter_id (str): The ID of the parameter for which
            the version is to be created.
            version_id (str): The ID of the version to be created.
            payload (str): The unformatted string payload
            to be stored in the new parameter version.
    
        Returns:
            parametermanager_v1.ParameterVersion: An object representing the
            newly created parameter version.
    
        Example:
            create_regional_param_version(
                "my-project",
                "us-central1",
                "my-regional-parameter",
                "v1",
                "my-unformatted-payload"
            )
        """
        # Import the necessary library for Google Cloud Parameter Manager.
        from google.cloud import [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest)
    
        # Create the Parameter Manager client with the regional endpoint.
        api_endpoint = f"parametermanager.{location_id}.rep.googleapis.com"
        client = [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[ParameterManagerClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html)(
            client_options={"api_endpoint": api_endpoint}
        )
    
        # Build the resource name of the parameter.
        parent = client.[parameter_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_parameter_path)(project_id, location_id, parameter_id)
    
        # Define the parameter version creation request with an unformatted payload.
        request = [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[CreateParameterVersionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.CreateParameterVersionRequest.html)(
            parent=parent,
            parameter_version_id=version_id,
            parameter_version=[parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[ParameterVersion](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.ParameterVersion.html)(
                payload=[parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[ParameterVersionPayload](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.ParameterVersionPayload.html)(
                    data=payload.encode("utf-8")  # Encoding the payload to bytes.
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
    # @param payload [String] The parameter payload (e.g. "test123")
    #
    def create_regional_param_version project_id:, location_id:, parameter_id:, version_id:, payload:
      # Endpoint for the regional parameter manager service.
      api_endpoint = "parametermanager.#{location_id}.rep.googleapis.com"
    
      # Create the Parameter Manager client.
      client = Google::Cloud::[ParameterManager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager.html).[parameter_manager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager/latest/Google-Cloud-ParameterManager.html) do |config|
        config.endpoint = api_endpoint
      end
    
      # Build the resource name of the parent project.
      parent = client.[parameter_path](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager-V1-ParameterManager-Paths.html) project: project_id, location: location_id, parameter: parameter_id
    
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

If you're using the gcloud CLI or the REST API, you can pass a payload file containing the parameter data directly in the create version command. Following is an example of uploading a payload file using the REST API:

**Sample command**
    
    
      echo "{\"payload\": { \"data\": \"$(cat PAYLOAD_FILE.yaml | base64 -w0)\"}}" | \
      curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -d @- \
        "https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/parameters/PARAMETER_ID/versions?parameter_version_id=PARAMETER_VERSION_ID"
    

Replace the following:

  * PAYLOAD_FILE: the payload file containing the parameter data.
  * PROJECT_ID: the Google Cloud project ID.
  * PARAMETER_ID: the name of the parameter.
  * PARAMETER_VERSION_ID: the ID of the parameter version. Don't use _latest_ (uppercase or lowercase) when naming your parameter version resources, because it's a reserved keyword. Reserved keywords have special meanings within the API and can't be used for other purposes.



**Sample response**
    
    
      {
        "name": "projects/production-1/locations/global/parameters/db_connection_string_prod/versions/v1",
        "createTime": "2024-10-15T08:39:05.191747694Z",
        "updateTime": "2024-10-15T08:39:05.191747694Z"
      }
    

## What's next

  * [Reference secrets in parameters](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference-secrets-in-parameter)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
