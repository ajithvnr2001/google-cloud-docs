---
url: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/render-parameter-version/
title: Access a parameter version \u00a0|\u00a0 Parameter Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:08:27.334327+00:00
---

# Access a parameter version  |  Parameter Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/render-parameter-version/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Parameter Manager ](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/overview)



Send feedback 

#  Access a parameter version Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to access a parameter version. When you access a parameter version, you retrieve the specific data payload stored within it.

Parameter versions can contain [references to secrets](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference-secrets-in-parameter) created in Secret Manager. The references don't expose secret values. Instead, your application retrieves the parameter to obtain a reference. The application then uses the reference to dynamically fetch the secret value from Secret Manager at runtime. This process ensures that the secret is only accessed and exposed in memory when needed, reducing the risk of a compromise.

To access a parameter version using the Google Cloud CLI or Parameter Manager API, specify either a version ID or use `latest` to access the most recent version.

## Required roles

To get the permissions that you need to render secret within a parameter version , ask your administrator to grant you the [Parameter Manager Parameter Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.parameterAccessor) (`roles/parametermanager.parameterAccessor`) IAM role on the parameter, project, folder, or organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Render the secret referenced within a parameter version

To render the secret referenced within a parameter version, use one of the following methods:

**Global parameters**

### Console

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. Click **Parameter Manager** to go to the **Parameter Manager** page. You'll see the list of parameters for that project.

  3. Click the parameter name to access its versions. The parameter details page opens with the **Versions** tab in focus where you can see all the versions belonging to the selected parameter.

  4. Select the parameter version with the secret reference.

  5. Click the more_vert**Actions** menu associated with that version, and then click **Render**.

An error occurs if the parameter cannot access the referenced secret. For more information, see [Grant the Secret Manager Secret Accessor role to the parameter](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference-secrets-in-parameter#grant_the_secret_manager_secret_accessor_role_to_the_parameter).

To allow the parameter to access the secret, click the **Grant permissions** button.

**Note:** The Grant permissions button triggers multiple API calls. Each of the calls counts against your project's API quota. 
     * The system triggers `[secrets.getIamPolicy](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets/getIamPolicy)` API call for every referenced secret to verify existing permissions. If the call fails for any secret, the grant operation fails entirely, and the system encounters an error.
     * If all the checks succeed, the system triggers `[secrets.setIamPolicy](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets/setIamPolicy)` API call for every referenced secret to add the required role. If the call fails for any secret, the system grants permissions to the remaining secrets.

A new page is displayed with the payload and the rendered value of the parameter version.




### gcloud

Before using any of the command data below, make the following replacements: 

  * PARAMETER_VERSION_ID: the ID of the parameter version
  * PARAMETER_ID: the name of the parameter



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters versions render PARAMETER_VERSION_ID --parameter=PARAMETER_ID --location=global

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters versions render PARAMETER_VERSION_ID --parameter=PARAMETER_ID --location=global

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters versions render PARAMETER_VERSION_ID --parameter=PARAMETER_ID --location=global

This method returns the parameter version metadata as well as the following two values: 

  * Payload: the raw, unprocessed parameter payload. This payload can have many key-value pairs, some of which might contain secrets. The `data` field within it holds a Base64-encoded string. If you decode this string, you'll find that the raw payload contains references (`REF(...)`) to locations where the secrets are stored. Note that each parameter version can contain up to 15 secret references.
  * Rendered Payload: the key-value pairs with actual secret values as a Base64-encoded string. Decode this string to fetch the parameter payload with rendered secret values.

Note: You can also use the render parameter version method to get version details for parameters that don't have secret references. In this scenario, the `payload` and `renderedPayload` fields contain the same value. 
    
    
    parameterVersion: projects/production-1/locations/global/parameters/db_password_secret_ref/versions/v4
    payload:
      data: ZGJfcGFzc3dvcmQ6IF9fUkVGX18oLy9zZWNyZXRtYW5hZ2VyLmdvb2dsZWFwaXMuY29tL3Byb2plY3RzL3BtLWNlcC1wcm9kL3NlY3JldHMvZHVyYWJsZS1zZWNyZXQvdmVyc2lvbnMvMSk=
    renderedPayload: ZGJfcGFzc3dvcmQ6IHRlc3Qtc2VjcmV0Cg==
    

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID
  * PARAMETER_ID: the name of the parameter
  * PARAMETER_VERSION_ID: the ID of the parameter version



HTTP method and URL: 
    
    
    GET https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/parameters/PARAMETER_ID/versions/PARAMETER_VERSION_ID:render

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
         "https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/parameters/PARAMETER_ID/versions/PARAMETER_VERSION_ID:render"

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
        -Uri "https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/parameters/PARAMETER_ID/versions/PARAMETER_VERSION_ID:render" | Select-Object -Expand Content

This method returns the parameter version metadata as well as the following two values: 

  * Payload: the raw, unprocessed parameter payload. This payload can have many key-value pairs, some of which might contain secrets. The `data` field within it holds a Base64-encoded string. If you decode this string, you'll find that the raw payload contains references (`REF(...)`) to locations where the secrets are stored. Note that each parameter version can contain up to 15 secret references.
  * Rendered Payload: the key-value pairs with actual secret values as a Base64-encoded string. Decode this string to fetch the parameter payload with rendered secret values.

Note: You can also use the render parameter version method to get version details for parameters that don't have secret references. In this scenario, the `payload` and `renderedPayload` fields contain the same value. 
    
    
    {
      "name": "projects/production-1/locations/global/parameters/db_password_secret_ref/versions/v2",
        "createTime": "2024-10-15T08:39:05.191747694Z",
        "updateTime": "2024-10-15T08:39:05.530311092Z",
        "payload": {
          "data": "ZGJfcGFzc3dvcmQ6IF9fUkVGX18oLy9zZWNyZXRtYW5hZ2VyLmdvb2dsZWFwaXMuY29tL3Byb2plY3RzL3BtLWNlcC1wcm9kL3NlY3JldHMvZHVyYWJsZS1zZWNyZXQvdmVyc2lvbnMvMSkK"
        },
        "renderedPayload": "ZGJfcGFzc3dvcmQ6IHRlc3Qtc2VjcmV0Cgo="
    }
    
    

### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Parameter Manager C# SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-csharp). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    using [Google.Cloud.ParameterManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.html);
    using System.Text;
    
    public class RenderParameterVersionSample
    {
        /// <summary>
        /// This function renders a parameter version using the Parameter Manager SDK for GCP.
        /// </summary>
        /// <param name="projectId">The ID of the project where the parameter is located.</param>
        /// <param name="parameterId">The ID of the parameter for which the version is to be rendered.</param>
        /// <param name="versionId">The ID of the version or alias (e.g. "latest") to be rendered.</param>
        /// <returns>The rendered parameter version data as a string.</returns>
        public string RenderParameterVersion(
            string projectId,
            string parameterId,
            string versionId)
        {
            // Create the client.
            [ParameterManagerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html) client = [ParameterManagerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html#Google_Cloud_ParameterManager_V1_ParameterManagerClient_Create)();
    
            // Build the resource name for the parameter version.
            [ParameterVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName.html) parameterVersionName = new [ParameterVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName.html)(projectId, "global", parameterId, versionId);
    
            // Call the API to render the parameter version.
            [RenderParameterVersionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.RenderParameterVersionResponse.html) renderParameterVersionResponse = client.[RenderParameterVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html#Google_Cloud_ParameterManager_V1_ParameterManagerClient_RenderParameterVersion_Google_Cloud_ParameterManager_V1_ParameterVersionName_Google_Api_Gax_Grpc_CallSettings_)(parameterVersionName);
    
            // Decode the base64 encoded data.
            string decodedData = Encoding.UTF8.GetString(renderParameterVersionResponse.[RenderedPayload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.RenderParameterVersionResponse.html#Google_Cloud_ParameterManager_V1_RenderParameterVersionResponse_RenderedPayload).ToByteArray());
    
            // Print the rendered parameter version data.
            Console.WriteLine($"Rendered parameter version payload: {decodedData}");
    
            // Return the rendered parameter version data.
            return decodedData;
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
    
    // renderParamVersion renders a parameter version using the Parameter Manager SDK for GCP.
    // The version can be a version ID as a string (e.g. "parameter1") or an alias (e.g. "latest")
    //
    // w: The io.Writer object used to write the output.
    // projectID: The ID of the project where the parameter is located.
    // parameterID: The ID of the parameter for which the version details is to be rendered.
    // versionID: The ID of the version to be rendered.
    //
    // The function returns an error if the parameter version rendering fails.
    func renderParamVersion(w io.Writer, projectID, parameterID, versionID string) error {
    	// Create a context and a Parameter Manager client.
    	ctx := context.Background()
    	client, err := parametermanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create Parameter Manager client: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_Close)()
    
    	// Construct the name of the parameter version to get render data.
    	name := fmt.Sprintf("projects/%s/locations/global/parameters/%s/versions/%s", projectID, parameterID, versionID)
    
    	// Build the request to render a parameter version.
    	req := &parametermanagerpb.RenderParameterVersionRequest{
    		Name: name,
    	}
    
    	// Call the API to render a parameter version.
    	rendered, err := client.RenderParameterVersion(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to render parameter version: %w", err)
    	}
    
    	fmt.Fprintf(w, "Rendered parameter version: %s\n", rendered.ParameterVersion)
    
    	// If the parameter contains secret references, they will be resolved
    	// and the actual secret values will be included in the rendered output.
    	// Be cautious with logging or displaying this information.
    	fmt.Fprintf(w, "Rendered payload: %s\n", rendered.RenderedPayload)
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Parameter Manager Java SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-java). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    import com.google.cloud.parametermanager.v1.[ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html);
    import com.google.cloud.parametermanager.v1.[ParameterVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersionName.html);
    import com.google.cloud.parametermanager.v1.[RenderParameterVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.RenderParameterVersionResponse.html);
    import java.io.IOException;
    
    /**
     * This class demonstrates how to render a parameter version using the Parameter Manager SDK for
     * GCP.
     * The version can be a version ID as a string (e.g. "parameter1") or an alias (e.g. "latest")
     */
    public class RenderParamVersion {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String parameterId = "your-parameter-id";
        String versionId = "your-version-id";
    
        // Call the method to render a parameter version.
        renderParamVersion(projectId, parameterId, versionId);
      }
    
      // This is an example snippet to render a parameter version.
      public static [RenderParameterVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.RenderParameterVersionResponse.html) renderParamVersion(
          String projectId, String parameterId, String versionId) throws IOException {
        // Initialize the client that will be used to send requests. This client only
        // needs to be created once, and can be reused for multiple requests.
        try ([ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html) client = [ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html).create()) {
          String locationId = "global";
    
          // Build the parameter version name.
          [ParameterVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersionName.html) parameterVersionName =
              [ParameterVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersionName.html).of(projectId, locationId, parameterId, versionId);
    
          // Render the parameter version.
          [RenderParameterVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.RenderParameterVersionResponse.html) response =
              client.renderParameterVersion(parameterVersionName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersionName.html#com_google_cloud_parametermanager_v1_ParameterVersionName_toString__)());
          System.out.printf(
              "Rendered parameter version payload: %s\n",
              response.[getRenderedPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.RenderParameterVersionResponse.html#com_google_cloud_parametermanager_v1_RenderParameterVersionResponse_getRenderedPayload__)().toStringUtf8());
    
          return response;
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
    // const parameterVersionId = 'latest';
    
    // Imports the Parameter Manager library
    const {ParameterManagerClient} = require('[@google-cloud/parametermanager](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)');
    
    // Instantiates a client
    const client = new [ParameterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)();
    
    async function renderParamVersion() {
      // Construct the parameter version name
      const name = client.[parameterVersionPath](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/parametermanager/v1.parametermanagerclient.html)(
        projectId,
        'global',
        parameterId,
        parameterVersionId
      );
    
      // Construct the request
      const request = {
        name: name,
      };
    
      // Render the parameter version
      const [parameterVersion] = await client.renderParameterVersion(request);
      console.log(
        `Rendered parameter version: ${parameterVersion.parameterVersion}`
      );
    
      // If the parameter contains secret references, they will be resolved
      // and the actual secret values will be included in the rendered output.
      // Be cautious with logging or displaying this information.
      console.log(
        'Rendered payload: ',
        parameterVersion.renderedPayload.toString('utf-8')
      );
      return parameterVersion;
    }
    
    return await renderParamVersion();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Parameter Manager PHP SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-php). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    // Import necessary classes for render a parameter version.
    use Google\Cloud\ParameterManager\V1\Client\ParameterManagerClient;
    use Google\Cloud\ParameterManager\V1\RenderParameterVersionRequest;
    
    /**
     * Renders a parameter version using the Parameter Manager SDK for GCP.
     *
     * @param string $projectId The Google Cloud Project ID (e.g. 'my-project')
     * @param string $parameterId The Parameter ID (e.g. 'my-param')
     * @param string $versionId The Version ID (e.g. 'my-param-version')
     */
    function render_param_version(string $projectId, string $parameterId, string $versionId): void
    {
        // Create a client for the Parameter Manager service.
        $client = new ParameterManagerClient();
    
        // Build the resource name of the parameter version.
        $parameterVersionName = $client->parameterVersionName($projectId, 'global', $parameterId, $versionId);
    
        // Prepare the request to render the parameter version.
        $request = (new RenderParameterVersionRequest())->setName($parameterVersionName);
    
        // Retrieve the render parameter version using the client.
        $parameterVersion = $client->renderParameterVersion($request);
    
        // Print the retrieved parameter version details.
        printf('Rendered parameter version payload: %s' . PHP_EOL, $parameterVersion->getRenderedPayload());
    }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Parameter Manager Python SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-python). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    def render_param_version(
        project_id: str, parameter_id: str, version_id: str
    ) -> parametermanager_v1.RenderParameterVersionResponse:
        """
        Retrieves and renders the details of a specific version of an
        existing parameter in the global location of the specified project
        using the Google Cloud Parameter Manager SDK.
    
        Args:
            project_id (str): The ID of the project where the parameter is located.
            parameter_id (str): The ID of the parameter for
            which version details are to be rendered.
            version_id (str): The ID of the version or alias (e.g. "latest") to be rendered.
    
        Returns:
            parametermanager_v1.RenderParameterVersionResponse: An object
            representing the rendered parameter version.
    
        Example:
            render_param_version(
                "my-project",
                "my-global-parameter",
                "v1"
            )
        """
        # Import the necessary library for Google Cloud Parameter Manager.
        from google.cloud import parametermanager_v1
    
        # Create the Parameter Manager client.
        client = parametermanager_v1.ParameterManagerClient()
    
        # Build the resource name of the parameter version.
        name = client.parameter_version_path(project_id, "global", parameter_id, version_id)
    
        # Define the request to render the parameter version.
        request = parametermanager_v1.RenderParameterVersionRequest(name=name)
    
        # Get the rendered parameter version details.
        response = client.render_parameter_version(request=request)
    
        # Print the rendered parameter version payload.
        print(
            f"Rendered parameter version payload: "
            f"{response.rendered_payload.decode('utf-8')}"
        )

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Parameter Manager Ruby SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-ruby). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    require "google/cloud/parameter_manager"
    
    ##
    # Render a parameter version
    #
    # @param project_id [String] The Google Cloud project (e.g. "my-project")
    # @param parameter_id [String] The parameter name (e.g. "my-parameter")
    # @param version_id [String] The version name (e.g. "my-version")
    #
    def render_param_version project_id:, parameter_id:, version_id:
      # Create a Parameter Manager client.
      client = Google::Cloud::[ParameterManager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager.html).[parameter_manager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager/latest/Google-Cloud-ParameterManager.html)
    
      # Build the resource name of the parent project.
      name = client.[parameter_version_path](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager-V1-ParameterManager-Paths.html) project: project_id, location: "global", parameter: parameter_id,
                                           parameter_version: version_id
    
      # Retrieve the parameter version.
      param_version = client.render_parameter_version name: name
    
      # Print the retrieved render parameter version name.
      puts "Rendered parameter version payload: #{param_version.rendered_payload}"
    end

**Regional parameters**

### Console

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. Click **Parameter Manager** to go to the **Parameter Manager** page. You'll see the list of parameters for that project.

  3. Click the parameter name to access its versions. The parameter details page opens with the **Versions** tab in focus where you can see all the versions belonging to the selected parameter.

  4. Select the parameter version with the secret reference.

  5. Click the more_vert**Actions** menu associated with that version, and then click **Render**.

An error occurs if the parameter cannot access the referenced secret. For more information, see [Grant the Secret Manager Secret Accessor role to the parameter](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference-secrets-in-parameter#grant_the_secret_manager_secret_accessor_role_to_the_parameter).

To allow the parameter to access the secret, click the **Grant permissions** button.

**Note:** The Grant permissions button triggers multiple API calls. Each of the calls counts against your project's API quota. 
     * The system triggers `[secrets.getIamPolicy](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets/getIamPolicy)` API call for every referenced secret to verify existing permissions. If the call fails for any secret, the grant operation fails entirely, and the system encounters an error.
     * If all the checks succeed, the system triggers `[secrets.setIamPolicy](https://docs.cloud.google.com/secret-manager/docs/reference/rest/v1/projects.secrets/setIamPolicy)` API call for every referenced secret to add the required role. If the call fails for any secret, the system grants permissions to the remaining secrets.

A new page is displayed with the payload and the rendered value of the parameter version.




### gcloud

Before using any of the command data below, make the following replacements: 

  * PARAMETER_VERSION_ID: the ID of the parameter version
  * PARAMETER_ID: the name of the parameter
  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the parameter



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters versions render PARAMETER_VERSION_ID --parameter=PARAMETER_ID --location=LOCATION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters versions render PARAMETER_VERSION_ID --parameter=PARAMETER_ID --location=LOCATION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters versions render PARAMETER_VERSION_ID --parameter=PARAMETER_ID --location=LOCATION

This method returns the parameter version metadata as well as the following two values: 

  * Payload: the raw, unprocessed parameter payload. This payload can have many key-value pairs, some of which might contain secrets. The `data` field within it holds a Base64-encoded string. If you decode this string, you'll find that the raw payload contains references (`REF(...)`) to locations where the secrets are stored. Note that each parameter version can contain up to 15 secret references.
  * Rendered Payload: the key-value pairs with actual secret values as a Base64-encoded string. Decode this string to fetch the parameter payload with rendered secret values.

Note: You can also use the render parameter version method to get version details for parameters that don't have secret references. In this scenario, the `payload` and `renderedPayload` fields contain the same value. 
    
    
    parameterVersion: projects/production-1/locations/us-central1/parameters/db_password_secret_ref/versions/v4
    payload:
      data: ZGJfcGFzc3dvcmQ6IF9fUkVGX18oLy9zZWNyZXRtYW5hZ2VyLmdvb2dsZWFwaXMuY29tL3Byb2plY3RzL3BtLWNlcC1wcm9kL2xvY2F0aW9ucy91cy1jZW50cmFsMS9zZWNyZXRzL2R1cmFibGUtc2VjcmV0L3ZlcnNpb25zLzEpCg==
    renderedPayload: ZGJfcGFzc3dvcmQ6IHRlc3Qtc2VjcmV0Cgo=
    

### REST

Before using any of the request data, make the following replacements: 

  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the parameter
  * PROJECT_ID: the Google Cloud project ID
  * PARAMETER_ID: the name of the parameter
  * PARAMETER_VERSION_ID: the ID of the parameter version



HTTP method and URL: 
    
    
    GET https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID/versions/PARAMETER_VERSION_ID:render

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
         "https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID/versions/PARAMETER_VERSION_ID:render"

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
        -Uri "https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID/versions/PARAMETER_VERSION_ID:render" | Select-Object -Expand Content

This method returns the parameter version metadata as well as the following two values: 

  * Payload: the raw, unprocessed parameter payload. This payload can have many key-value pairs, some of which might contain secrets. The `data` field within it holds a Base64-encoded string. If you decode this string, you'll find that the raw payload contains references (`REF(...)`) to locations where the secrets are stored. Note that each parameter version can contain up to 15 secret references.
  * Rendered Payload: the key-value pairs with actual secret values as a Base64-encoded string. Decode this string to fetch the parameter payload with rendered secret values.

Note: You can also use the render parameter version method to get version details for parameters that don't have secret references. In this scenario, the `payload` and `renderedPayload` fields contain the same value. 
    
    
    {
      "parameterVersion": "projects/production-1/locations/us-central1/parameters/db_password_secret_ref/versions/v3",
      "payload": {
        "data": "ZGJfcGFzc3dvcmQ6IF9fUkVGX18oLy9zZWNyZXRtYW5hZ2VyLmdvb2dsZWFwaXMuY29tL3Byb2plY3RzL3BtLWNlcC1wcm9kL2xvY2F0aW9ucy91cy1jZW50cmFsMS9zZWNyZXRzL2R1cmFibGUtc2VjcmV0L3ZlcnNpb25zLzEpCg=="
      },
      "renderedPayload": "ZGJfcGFzc3dvcmQ6IHRlc3Qtc2VjcmV0Cgo="
    }
    
    

### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Parameter Manager C# SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-csharp). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    using [Google.Cloud.ParameterManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.html);
    using System.Text;
    
    public class RenderRegionalParameterVersionSample
    {
        /// <summary>
        /// This function renders a regional parameter version using the Parameter Manager SDK for GCP.
        /// </summary>
        /// <param name="projectId">The ID of the project where the parameter is located.</param>
        /// <param name="locationId">The ID of the region where the parameter is located.</param>
        /// <param name="parameterId">The ID of the parameter for which the version is to be rendered.</param>
        /// <param name="versionId">The ID of the version or alias (e.g. "latest") to be rendered.</param>
        /// <returns>The rendered parameter version data as a string.</returns>
        public string RenderRegionalParameterVersion(
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
    
            // Build the resource name for the parameter version in the specified regional locationId
            [ParameterVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName.html) parameterVersionName = new [ParameterVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName.html)(projectId, locationId, parameterId, versionId);
    
            // Call the API to render the parameter version
            [RenderParameterVersionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.RenderParameterVersionResponse.html) renderParameterVersionResponse = client.[RenderParameterVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html#Google_Cloud_ParameterManager_V1_ParameterManagerClient_RenderParameterVersion_Google_Cloud_ParameterManager_V1_ParameterVersionName_Google_Api_Gax_Grpc_CallSettings_)(parameterVersionName);
    
            // Decode the base64 encoded data
            string decodedData = Encoding.UTF8.GetString(renderParameterVersionResponse.[RenderedPayload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.RenderParameterVersionResponse.html#Google_Cloud_ParameterManager_V1_RenderParameterVersionResponse_RenderedPayload).ToByteArray());
    
            // Print the rendered parameter version data
            Console.WriteLine($"Rendered regional parameter version payload: {decodedData}");
    
            // Return the rendered parameter version data
            return decodedData;
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
    
    // renderRegionalParamVersion renders a regional parameter version using the Parameter Manager SDK for GCP.
    // The version can be a version ID as a string (e.g. "parameter1") or an alias (e.g. "latest")
    //
    // w: The io.Writer object used to write the output.
    // projectID: The ID of the project where the parameter is located.
    // locationID: The ID of the region where the parameter is located.
    // parameterID: The ID of the parameter for which the version is to be rendered.
    // versionID: The ID of the version to be rendered.
    //
    // The function returns an error if the parameter version render retrieval fails.
    func renderRegionalParamVersion(w io.Writer, projectID, locationID, parameterID, versionID string) error {
    	// Create a new context.
    	ctx := context.Background()
    
    	// Create a Parameter Manager client.
    	endpoint := fmt.Sprintf("parametermanager.%s.rep.googleapis.com:443", locationID)
    	client, err := parametermanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_NewClient)(ctx, option.WithEndpoint(endpoint))
    	if err != nil {
    		return fmt.Errorf("failed to create Parameter Manager client: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_Close)()
    
    	// Construct the name of the parameter version to render.
    	name := fmt.Sprintf("projects/%s/locations/%s/parameters/%s/versions/%s", projectID, locationID, parameterID, versionID)
    
    	// Build the request to render the parameter version.
    	req := &parametermanagerpb.RenderParameterVersionRequest{
    		Name: name,
    	}
    
    	// Call the API to render the parameter version.
    	rendered, err := client.RenderParameterVersion(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to render parameter version: %w", err)
    	}
    
    	fmt.Fprintf(w, "Rendered regional parameter version: %s\n", rendered.ParameterVersion)
    
    	// If the parameter contains secret references, they will be resolved
    	// and the actual secret values will be included in the rendered output.
    	// Be cautious with logging or displaying this information.
    	fmt.Fprintf(w, "Rendered payload: %s\n", rendered.RenderedPayload)
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Parameter Manager Java SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-java). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    import com.google.cloud.parametermanager.v1.[ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html);
    import com.google.cloud.parametermanager.v1.[ParameterManagerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerSettings.html);
    import com.google.cloud.parametermanager.v1.[ParameterVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersionName.html);
    import com.google.cloud.parametermanager.v1.[RenderParameterVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.RenderParameterVersionResponse.html);
    import java.io.IOException;
    
    /**
     * This class demonstrates how to render a regional parameter version using the Parameter Manager
     * SDK for GCP.
     */
    public class RenderRegionalParamVersion {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "your-location-id";
        String parameterId = "your-parameter-id";
        String versionId = "your-version-id";
    
        // Call the method to render a regional parameter version.
        renderRegionalParamVersion(projectId, locationId, parameterId, versionId);
      }
    
      // This is an example snippet to render a regional parameter version.
      public static [RenderParameterVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.RenderParameterVersionResponse.html) renderRegionalParamVersion(
          String projectId, String locationId, String parameterId, String versionId)
          throws IOException {
        // Endpoint to call the regional parameter manager server
        String apiEndpoint = String.format("parametermanager.%s.rep.googleapis.com:443", locationId);
        [ParameterManagerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerSettings.html) parameterManagerSettings =
            [ParameterManagerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerSettings.html).newBuilder().setEndpoint(apiEndpoint).build();
    
        // Initialize the client that will be used to send requests. This client only
        // needs to be created once, and can be reused for multiple requests.
        try ([ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html) client = [ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html).create(parameterManagerSettings)) {
          // Build the parameter version name.
          [ParameterVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersionName.html) parameterVersionName =
              [ParameterVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersionName.html).of(projectId, locationId, parameterId, versionId);
    
          // Render the parameter version.
          [RenderParameterVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.RenderParameterVersionResponse.html) response =
              client.renderParameterVersion(parameterVersionName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersionName.html#com_google_cloud_parametermanager_v1_ParameterVersionName_toString__)());
          System.out.printf(
              "Rendered regional parameter version payload: %s\n",
              response.[getRenderedPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.RenderParameterVersionResponse.html#com_google_cloud_parametermanager_v1_RenderParameterVersionResponse_getRenderedPayload__)().toStringUtf8());
    
          return response;
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
    // const parameterVersionId = 'latest';
    
    // Imports the Parameter Manager library
    const {ParameterManagerClient} = require('[@google-cloud/parametermanager](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)');
    
    // Adding the endpoint to call the regional parameter manager server
    const options = {
      apiEndpoint: `parametermanager.${locationId}.rep.googleapis.com`,
    };
    
    // Instantiates a client with regional endpoint
    const client = new [ParameterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)(options);
    
    async function renderRegionalParamVersion() {
      // Construct the parameter version name
      const name = client.[parameterVersionPath](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/parametermanager/v1.parametermanagerclient.html)(
        projectId,
        locationId,
        parameterId,
        parameterVersionId
      );
    
      // Construct the request
      const request = {
        name: name,
      };
    
      // Render the parameter version
      const [paramVersions] = await client.renderParameterVersion(request);
    
      console.log(
        `Rendered regional parameter version: ${paramVersions.parameterVersion}`
      );
    
      // If the parameter contains secret references, they will be resolved
      // and the actual secret values will be included in the rendered output.
      // Be cautious with logging or displaying this information.
      console.log(
        'Rendered payload: ',
        paramVersions.renderedPayload.toString('utf-8')
      );
      return paramVersions;
    }
    
    return await renderRegionalParamVersion();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Parameter Manager PHP SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-php). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    // Import necessary classes for render a parameter version.
    use Google\Cloud\ParameterManager\V1\Client\ParameterManagerClient;
    use Google\Cloud\ParameterManager\V1\RenderParameterVersionRequest;
    
    /**
     * Renders a regional parameter version using the Parameter Manager SDK for GCP.
     *
     * @param string $projectId The Google Cloud Project ID (e.g. 'my-project')
     * @param string $locationId The Parameter Location (e.g. 'us-central1')
     * @param string $parameterId The Parameter ID (e.g. 'my-param')
     * @param string $versionId The Version ID (e.g. 'my-param-version')
     */
    function render_regional_param_version(string $projectId, string $locationId, string $parameterId, string $versionId): void
    {
        // Specify regional endpoint.
        $options = ['apiEndpoint' => "parametermanager.$locationId.rep.googleapis.com"];
    
        // Create a client for the Parameter Manager service.
        $client = new ParameterManagerClient($options);
    
        // Build the resource name of the parameter version.
        $parameterVersionName = $client->parameterVersionName($projectId, $locationId, $parameterId, $versionId);
    
        // Prepare the request to render the parameter version.
        $request = (new RenderParameterVersionRequest())->setName($parameterVersionName);
    
        // Retrieve the render parameter version using the client.
        $parameterVersion = $client->renderParameterVersion($request);
    
        // Print the retrieved parameter version details.
        printf('Rendered regional parameter version payload: %s' . PHP_EOL, $parameterVersion->getRenderedPayload());
    }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Parameter Manager Python SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-python). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    def render_regional_param_version(
        project_id: str, location_id: str, parameter_id: str, version_id: str
    ) -> parametermanager_v1.RenderParameterVersionResponse:
        """
        Retrieves and renders the details of a specific version of an
        existing parameter in the specified region of the specified project
        using the Google Cloud Parameter Manager SDK.
    
        Args:
            project_id (str): The ID of the project where the parameter is located.
            location_id (str): The ID of the region where the parameter is located.
            parameter_id (str): The ID of the parameter for
            which version details are to be rendered.
            version_id (str): The ID of the version or alias (e.g. "latest") to
            be rendered.
    
        Returns:
            parametermanager_v1.RenderParameterVersionResponse: An object
            representing the rendered parameter version.
    
        Example:
            render_regional_param_version(
                "my-project",
                "us-central1",
                "my-regional-parameter",
                "v1"
            )
        """
        # Import the necessary library for Google Cloud Parameter Manager.
        from google.cloud import [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest)
    
        # Create the Parameter Manager client with the regional endpoint.
        api_endpoint = f"parametermanager.{location_id}.rep.googleapis.com"
        client = [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[ParameterManagerClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html)(
            client_options={"api_endpoint": api_endpoint}
        )
    
        # Build the resource name of the parameter version.
        name = client.[parameter_version_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_parameter_version_path)(
            project_id, location_id, parameter_id, version_id
        )
    
        # Define the request to render the parameter version.
        request = [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[RenderParameterVersionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.RenderParameterVersionRequest.html)(name=name)
    
        # Get the rendered parameter version details.
        response = client.[render_parameter_version](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_render_parameter_version)(request=request)
    
        # Print the response payload.
        print(
            f"Rendered regional parameter version payload: "
            f"{response.rendered_payload.decode('utf-8')}"
        )

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Parameter Manager Ruby SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-ruby). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    require "google/cloud/parameter_manager"
    
    ##
    # Render a regional parameter version
    #
    # @param project_id [String] The Google Cloud project (e.g. "my-project")
    # @param location_id [String] The location name (e.g. "us-central1")
    # @param parameter_id [String] The parameter name (e.g. "my-parameter")
    # @param version_id [String] The version name (e.g. "my-version")
    #
    def render_regional_param_version project_id:, location_id:, parameter_id:, version_id:
      # Endpoint for the regional parameter manager service.
      api_endpoint = "parametermanager.#{location_id}.rep.googleapis.com"
    
      # Create the Parameter Manager client.
      client = Google::Cloud::[ParameterManager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager.html).[parameter_manager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager/latest/Google-Cloud-ParameterManager.html) do |config|
        config.endpoint = api_endpoint
      end
    
      # Build the resource name of the parent project.
      name = client.[parameter_version_path](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager-V1-ParameterManager-Paths.html) project: project_id, location: location_id, parameter: parameter_id,
                                           parameter_version: version_id
    
      # Retrieve the parameter version.
      param_version = client.render_parameter_version name: name
    
      # Print the retrieved render parameter version name.
      puts "Rendered regional parameter version payload: #{param_version.rendered_payload}"
    end

### Resource consistency

In Parameter Manager, all operations are eventually consistent, including adding and accessing parameter versions.

Eventually consistent operations usually take effect within minutes, but can sometimes take a few hours.

IAM permission updates are also eventually consistent, so granting or revoking access to parameters might not take effect immediately.For more information, see [Access change propagation](https://docs.cloud.google.com/iam/docs/access-change-propagation).

## What's next

  * [Disable a parameter version](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/disable-parameter-versions)
  * [Enable a disabled parameter version](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/enable-disabled-versions)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
