---
url: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/disable-parameter-versions/
title: Disable a parameter version \u00a0|\u00a0 Parameter Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:57:41.440934+00:00
---

# Disable a parameter version  |  Parameter Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/disable-parameter-versions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Parameter Manager ](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/overview)



Send feedback 

#  Disable a parameter version Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to disable versions within a parameter.

Disabling parameter versions is helpful in the following scenarios:

  * If a specific version of a parameter represents a deprecated or outdated configuration, disabling it prevents accidental use.
  * If a version contains sensitive information that should no longer be accessible, disabling it mitigates security risks.
  * If you suspect that a specific version of a parameter is causing problems, disabling the version can help isolate the issue.
  * If you're testing new configurations or experimenting with different settings, you might disable versions temporarily.



## Required roles

To get the permissions that you need to disable a parameter version, ask your administrator to grant you the [Parameter Manager Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.admin) (`roles/parametermanager.admin`) IAM role on the parameter, project, folder, or organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Disable a parameter version

To disable a parameter version, use one of the following methods:

**Global parameters**

### Console

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. Click **Parameter Manager** to go to the **Parameter Manager** page. You'll see the list of parameters for that project.

  3. Click the parameter name to access its versions. The parameter details page opens with the **Versions** tab in focus where you can see all the versions belonging to the selected parameter.

  4. Select the parameter version that you want to disable.

  5. Click the more_vert**Actions** menu associated with that version, and then click **Disable**.

  6. In the confirmation dialog that appears, click **Disable**.




### gcloud

Before using any of the command data below, make the following replacements: 

  * PARAMETER_VERSION_ID: the ID of the parameter version
  * PARAMETER_ID: the name of the parameter



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters versions update PARAMETER_VERSION_ID --parameter=PARAMETER_ID --location=global --disabled

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters versions update PARAMETER_VERSION_ID --parameter=PARAMETER_ID --location=global --disabled

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters versions update PARAMETER_VERSION_ID --parameter=PARAMETER_ID --location=global --disabled

You should receive a response similar to the following:
    
    
    Updated parameterVersion [range1].
    createTime: '2024-11-14T10:07:12.883361876Z'
    disabled: true
    name: projects/production-1/locations/global/parameters/allowed_ip_ranges/versions/range1
    updateTime: '2024-11-14T10:21:00.238113299Z'
    

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID
  * PARAMETER_ID: the name of the parameter
  * PARAMETER_VERSION_ID: the ID of the parameter version



HTTP method and URL: 
    
    
    PATCH https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/parameters/PARAMETER_ID/versions/PARAMETER_VERSION_ID

Request JSON body: 
    
    
    {"disabled": true}
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/parameters/PARAMETER_ID/versions/PARAMETER_VERSION_ID"

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
        -Uri "https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/parameters/PARAMETER_ID/versions/PARAMETER_VERSION_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/production-1/locations/global/parameters/allowed_ip_ranges/versions/range1",
      "createTime": "2024-10-15T08:39:05.191747694Z",
      "updateTime": "2024-10-15T08:39:05.530311092Z",
      "disabled": true
    }
    
    

### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Parameter Manager C# SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-csharp). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    using [Google.Cloud.ParameterManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    
    public class DisableParameterVersionSample
    {
        /// <summary>
        /// This function disables a parameter version using the Parameter Manager SDK for GCP.
        /// </summary>
        /// <param name="projectId">The ID of the project where the parameter is located.</param>
        /// <param name="parameterId">The ID of the parameter for which the version is to be disabled.</param>
        /// <param name="versionId">The ID of the version to be disabled.</param>
        /// <returns>The updated ParameterVersion object.</returns>
        public ParameterVersion DisableParameterVersion(
            string projectId,
            string parameterId,
            string versionId)
        {
            // Create the client.
            [ParameterManagerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html) client = [ParameterManagerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html#Google_Cloud_ParameterManager_V1_ParameterManagerClient_Create)();
    
            // Build the resource name for the parameter version.
            [ParameterVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName.html) parameterVersionName = new [ParameterVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName.html)(projectId, "global", parameterId, versionId);
    
            [UpdateParameterVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.UpdateParameterVersionRequest.html) request = new [UpdateParameterVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.UpdateParameterVersionRequest.html)
            {
                ParameterVersion = new [ParameterVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersion.html)
                {
                    Name = parameterVersionName.[ToString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName.html#Google_Cloud_ParameterManager_V1_ParameterVersionName_ToString)(),
                    Disabled = true
                },
                UpdateMask = new [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)
                {
                    Paths = { "disabled" }
                }
            };
    
            // Call the API to update (disable) the parameter version.
            [ParameterVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersion.html) updatedParameterVersion = client.[UpdateParameterVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html#Google_Cloud_ParameterManager_V1_ParameterManagerClient_UpdateParameterVersion_Google_Cloud_ParameterManager_V1_ParameterVersion_Google_Protobuf_WellKnownTypes_FieldMask_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Print the updated parameter version name.
            Console.WriteLine($"Disabled parameter version {versionId} for parameter {parameterId}");
    
            // Return the updated parameter version.
            return updatedParameterVersion;
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
    	"google.golang.org/genproto/protobuf/field_mask"
    )
    
    // disableParamVersion disables a parameter version.
    //
    // w: The io.Writer object used to write the output.
    // projectID: The ID of the project where the parameter is located.
    // parameterID: The ID of the parameter for which the version is to be disabled.
    // versionID: The ID of the version to be disabled.
    //
    // The function returns an error if the parameter version update fails.
    func disableParamVersion(w io.Writer, projectID, parameterID, versionID string) error {
    	// Create the client.
    	ctx := context.Background()
    	client, err := parametermanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create parametermanager client: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_Close)()
    
    	// Construct the name of the parameter version to disable.
    	name := fmt.Sprintf("projects/%s/locations/global/parameters/%s/versions/%s", projectID, parameterID, versionID)
    
    	// Build the request to disable the parameter version by updating the parameter version.
    	req := &parametermanagerpb.UpdateParameterVersionRequest{
    		UpdateMask: &field_mask.FieldMask{
    			Paths: []string{"disabled"},
    		},
    		ParameterVersion: &parametermanagerpb.ParameterVersion{
    			Name:     name,
    			Disabled: true,
    		},
    	}
    
    	// Call the API to disable the parameter version.
    	if _, err := client.UpdateParameterVersion(ctx, req); err != nil {
    		return fmt.Errorf("failed to disable parameter version: %w", err)
    	}
    
    	fmt.Fprintf(w, "Disabled parameter version %s for parameter %s\n", name, parameterID)
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Parameter Manager Java SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-java). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    import com.google.cloud.parametermanager.v1.[ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html);
    import com.google.cloud.parametermanager.v1.[ParameterVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersion.html);
    import com.google.cloud.parametermanager.v1.[ParameterVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersionName.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import com.google.protobuf.util.[FieldMaskUtil](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.FieldMaskUtil.html);
    import java.io.IOException;
    
    /**
     * This class demonstrates how to disable a parameter version using the Parameter Manager SDK for
     * GCP.
     */
    public class DisableParamVersion {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String parameterId = "your-parameter-id";
        String versionId = "your-version-id";
    
        // Call the method to disable a parameter version.
        disableParamVersion(projectId, parameterId, versionId);
      }
    
      // This is an example snippet for disabling a parameter version.
      public static [ParameterVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersion.html) disableParamVersion(
          String projectId, String parameterId, String versionId) throws IOException {
        // Initialize the client that will be used to send requests. This client only
        // needs to be created once, and can be reused for multiple requests.
        try ([ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html) client = [ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html).create()) {
          String locationId = "global";
    
          // Build the parameter version name.
          [ParameterVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersionName.html) parameterVersionName =
              [ParameterVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersionName.html).of(projectId, locationId, parameterId, versionId);
    
          // Set the parameter version to disable.
          [ParameterVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersion.html) parameterVersion =
              [ParameterVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersion.html).newBuilder()
                  .setName(parameterVersionName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersionName.html#com_google_cloud_parametermanager_v1_ParameterVersionName_toString__)())
                  .setDisabled(true)
                  .build();
    
          // Build the field mask for the disabled field.
          [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) fieldMask = [FieldMaskUtil](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.FieldMaskUtil.html).fromString("disabled");
    
          // Update the parameter version to disable it.
          [ParameterVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersion.html) disabledParameterVersion =
              client.updateParameterVersion(parameterVersion, fieldMask);
          System.out.printf(
              "Disabled parameter version %s for parameter %s\n",
              disabledParameterVersion.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersion.html#com_google_cloud_parametermanager_v1_ParameterVersion_getName__)(), parameterId);
    
          return disabledParameterVersion;
        }
      }
    }

### Node.js

To run this code, first [set up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup) and [install the Parameter Manager Node.js SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-nodejs). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'my-project';
    // const parameterId = 'my-parameter';
    // const versionId = 'v1';
    
    // Imports the Parameter Manager library
    const {ParameterManagerClient} = require('[@google-cloud/parametermanager](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)');
    
    // Instantiates a client
    const client = new [ParameterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)();
    
    async function disableParamVersion() {
      // Construct the full resource name
      const name = client.[parameterVersionPath](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/parametermanager/v1.parametermanagerclient.html)(
        projectId,
        'global',
        parameterId,
        versionId
      );
    
      // Construct the request
      const request = {
        parameterVersion: {
          name: name,
          disabled: true,
        },
        updateMask: {
          paths: ['disabled'],
        },
      };
    
      // Make the API call to update the parameter version
      const [parameterVersion] = await client.updateParameterVersion(request);
    
      console.log(
        `Disabled parameter version ${parameterVersion.name} for parameter ${parameterId}`
      );
      return parameterVersion;
    }
    
    return await disableParamVersion();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Parameter Manager PHP SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-php). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    // Import necessary classes for disable a parameter version.
    use Google\Cloud\ParameterManager\V1\Client\ParameterManagerClient;
    use Google\Cloud\ParameterManager\V1\ParameterVersion;
    use Google\Cloud\ParameterManager\V1\UpdateParameterVersionRequest;
    use Google\Protobuf\FieldMask;
    
    /**
     * Disables a parameter version using the Parameter Manager SDK for GCP.
     *
     * @param string $projectId The Google Cloud Project ID (e.g. 'my-project')
     * @param string $parameterId The Parameter ID (e.g. 'my-param')
     * @param string $versionId The Version ID (e.g. 'my-param-version')
     */
    function disable_param_version(string $projectId, string $parameterId, string $versionId): void
    {
        // Create a client for the Parameter Manager service.
        $client = new ParameterManagerClient();
    
        // Build the resource name of the parameter version.
        $parameterVersionName = $client->parameterVersionName($projectId, 'global', $parameterId, $versionId);
    
        // Update the parameter version.
        $parameterVersion = (new ParameterVersion())
            ->setName($parameterVersionName)
            ->setDisabled(true);
    
        $updateMask = (new FieldMask())
            ->setPaths(['disabled']);
    
        // Prepare the request to disable the parameter version.
        $request = (new UpdateParameterVersionRequest())
            ->setUpdateMask($updateMask)
            ->setParameterVersion($parameterVersion);
    
        // Disable the parameter version using the client.
        $client->updateParameterVersion($request);
    
        // Print the parameter version details.
        printf('Disabled parameter version %s for parameter %s' . PHP_EOL, $versionId, $parameterId);
    }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Parameter Manager Python SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-python). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    def disable_param_version(
        project_id: str, parameter_id: str, version_id: str
    ) -> parametermanager_v1.ParameterVersion:
        """
        Disables a specific version of a specified global parameter
        in the specified project using the Google Cloud Parameter Manager SDK.
    
        Args:
            project_id (str): The ID of the project where the parameter is located.
            parameter_id (str): The ID of the parameter for
            which version is to be disabled.
            version_id (str): The ID of the version to be disabled.
    
        Returns:
            parametermanager_v1.ParameterVersion: An object representing the
            disabled parameter version.
    
        Example:
            disable_param_version(
                "my-project",
                "my-global-parameter",
                "v1"
            )
        """
        # Import the necessary library for Google Cloud Parameter Manager.
        from google.cloud import [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest)
        from google.protobuf import field_mask_pb2
    
        # Create the Parameter Manager client.
        client = [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[ParameterManagerClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html)()
    
        # Build the resource name of the parameter version.
        name = client.[parameter_version_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_parameter_version_path)(project_id, "global", parameter_id, version_id)
    
        # Get the current parameter version details.
        parameter_version = client.[get_parameter_version](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_get_parameter_version)(name=name)
    
        # Set the disabled field to True to disable the version.
        parameter_version.disabled = True
    
        # Define the update mask for the disabled field.
        update_mask = field_mask_pb2.FieldMask(paths=["disabled"])
    
        # Define the request to update the parameter version.
        request = [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[UpdateParameterVersionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.UpdateParameterVersionRequest.html)(
            parameter_version=parameter_version, update_mask=update_mask
        )
    
        # Call the API to update (disable) the parameter version.
        response = client.[update_parameter_version](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_update_parameter_version)(request=request)
    
        # Print the parameter version ID that it was disabled.
        print(f"Disabled parameter version {version_id} for parameter {parameter_id}")

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Parameter Manager Ruby SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-ruby). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    require "google/cloud/parameter_manager"
    
    ##
    # Disable a parameter version
    #
    # @param project_id [String] The Google Cloud project (e.g. "my-project")
    # @param parameter_id [String] The parameter name (e.g. "my-parameter")
    # @param version_id [String] The version name (e.g. "my-version")
    #
    def disable_param_version project_id:, parameter_id:, version_id:
      # Create a Parameter Manager client.
      client = Google::Cloud::[ParameterManager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager.html).[parameter_manager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager/latest/Google-Cloud-ParameterManager.html)
    
      # Build the resource name of the parent project.
      name = client.[parameter_version_path](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager-V1-ParameterManager-Paths.html) project: project_id, location: "global", parameter: parameter_id,
                                           parameter_version: version_id
    
      parameter_version = {
        name: name,
        disabled: true
      }
    
      update_mask = {
        paths: ["disabled"]
      }
    
      # Disabled the parameter version
      param_version = client.update_parameter_version parameter_version: parameter_version, update_mask: update_mask
    
      # Print the parameter version name.
      puts "Disabled parameter version #{version_id} for parameter #{parameter_id}"
    end

**Regional parameters**

### Console

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. Click **Parameter Manager** to go to the **Parameter Manager** page. You'll see the list of parameters for that project.

  3. Click the parameter name to access its versions. The parameter details page opens with the **Versions** tab in focus where you can see all the versions belonging to the selected parameter.

  4. Select the parameter version that you want to disable.

  5. Click the more_vert**Actions** menu associated with that version, and then click **Disable**.

  6. In the confirmation dialog that appears, click **Disable**.




### gcloud

Before using any of the command data below, make the following replacements: 

  * PARAMETER_VERSION_ID: the ID of the parameter version
  * PARAMETER_ID: the name of the parameter
  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the parameter



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters versions update PARAMETER_VERSION_ID --parameter=PARAMETER_ID --location=LOCATION --disabled

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters versions update PARAMETER_VERSION_ID --parameter=PARAMETER_ID --location=LOCATION --disabled

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters versions update PARAMETER_VERSION_ID --parameter=PARAMETER_ID --location=LOCATION --disabled

You should receive a response similar to the following:
    
    
    Updated parameterVersion [v1].
    createTime: '2024-11-14T10:07:12.883361876Z'
    disabled: true
    name: projects/production-1/locations/us-central1/parameters/p1/versions/v1
    updateTime: '2024-11-14T10:21:00.238113299Z'
    

### REST

Before using any of the request data, make the following replacements: 

  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the parameter
  * PROJECT_ID: the Google Cloud project ID
  * PARAMETER_ID: the name of the parameter
  * PARAMETER_VERSION_ID: the ID of the parameter version



HTTP method and URL: 
    
    
    PATCH https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID/versions/PARAMETER_VERSION_ID

Request JSON body: 
    
    
    {"disabled": true}
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID/versions/PARAMETER_VERSION_ID"

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
        -Uri "https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID/versions/PARAMETER_VERSION_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/production-1/locations/us-central1/parameters/p1/versions/v1",
      "createTime": "2024-11-22T05:24:41.338299211Z",
      "updateTime": "2024-11-22T05:35:12.630776330Z",
      "disabled": true
    }
    
    

### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Parameter Manager C# SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-csharp). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    using [Google.Cloud.ParameterManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    
    public class DisableRegionalParameterVersionSample
    {
        /// <summary>
        /// This function disables a regional parameter version using the Parameter Manager SDK for GCP.
        /// </summary>
        /// <param name="projectId">The ID of the project where the parameter is located.</param>
        /// <param name="locationId">The ID of the region where the parameter is located.</param>
        /// <param name="parameterId">The ID of the parameter for which the version is to be disabled.</param>
        /// <param name="versionId">The ID of the version to be disabled.</param>
        public ParameterVersion DisableRegionalParameterVersion(
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
    
            [UpdateParameterVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.UpdateParameterVersionRequest.html) request = new [UpdateParameterVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.UpdateParameterVersionRequest.html)
            {
                ParameterVersion = new [ParameterVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersion.html)
                {
                    Name = parameterVersionName.[ToString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName.html#Google_Cloud_ParameterManager_V1_ParameterVersionName_ToString)(),
                    Disabled = true
                },
                UpdateMask = new [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)
                {
                    Paths = { "disabled" }
                }
            };
    
            // Call the API to update (disable) the parameter version.
            [ParameterVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersion.html) updatedParameterVersion = client.[UpdateParameterVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html#Google_Cloud_ParameterManager_V1_ParameterManagerClient_UpdateParameterVersion_Google_Cloud_ParameterManager_V1_ParameterVersion_Google_Protobuf_WellKnownTypes_FieldMask_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            Console.WriteLine($"Disabled regional parameter version {versionId} for parameter {parameterId}");
    
            return updatedParameterVersion;
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
    	"google.golang.org/genproto/protobuf/field_mask"
    )
    
    // disableRegionalParamVersion disables a regional parameter version using the Parameter Manager SDK for GCP.
    //
    // w: The io.Writer object used to write the output.
    // projectID: The ID of the project where the parameter is located.
    // locationID: The ID of the region where the parameter is located.
    // parameterID: The ID of the parameter for which the version is to be disabled.
    // versionID: The ID of the version to be disabled.
    //
    // The function returns an error if the parameter version update fails.
    func disableRegionalParamVersion(w io.Writer, projectID, locationID, parameterID, versionID string) error {
    	// Create a new context.
    	ctx := context.Background()
    
    	// Create a Parameter Manager client.
    	endpoint := fmt.Sprintf("parametermanager.%s.rep.googleapis.com:443", locationID)
    	client, err := parametermanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_NewClient)(ctx, option.WithEndpoint(endpoint))
    	if err != nil {
    		return fmt.Errorf("failed to create Parameter Manager client: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_Close)()
    
    	// Construct the name of the parameter version to disable.
    	name := fmt.Sprintf("projects/%s/locations/%s/parameters/%s/versions/%s", projectID, locationID, parameterID, versionID)
    
    	// Build the request to disable the parameter version by updating the parameter version.
    	req := &parametermanagerpb.UpdateParameterVersionRequest{
    		UpdateMask: &field_mask.FieldMask{
    			Paths: []string{"disabled"},
    		},
    		ParameterVersion: &parametermanagerpb.ParameterVersion{
    			Name:     name,
    			Disabled: true,
    		},
    	}
    
    	// Call the API to disable the parameter version.
    	if _, err := client.UpdateParameterVersion(ctx, req); err != nil {
    		return fmt.Errorf("failed to disable parameter version: %w", err)
    	}
    
    	fmt.Fprintf(w, "Disabled regional parameter version %s for parameter %s\n", name, parameterID)
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Parameter Manager Java SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-java). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    import com.google.cloud.parametermanager.v1.[ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html);
    import com.google.cloud.parametermanager.v1.[ParameterManagerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerSettings.html);
    import com.google.cloud.parametermanager.v1.[ParameterVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersion.html);
    import com.google.cloud.parametermanager.v1.[ParameterVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersionName.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import com.google.protobuf.util.[FieldMaskUtil](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.FieldMaskUtil.html);
    import java.io.IOException;
    
    /**
     * This class demonstrates how to disable a regional parameter version using the Parameter Manager
     * SDK for GCP.
     */
    public class DisableRegionalParamVersion {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "your-location-id";
        String parameterId = "your-parameter-id";
        String versionId = "your-version-id";
    
        // Call the method to disable a regional parameter version.
        disableRegionalParamVersion(projectId, locationId, parameterId, versionId);
      }
    
      // This is an example snippet that disables a regional parameter version.
      public static [ParameterVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersion.html) disableRegionalParamVersion(
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
    
          // Set the parameter version to disable.
          [ParameterVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersion.html) parameterVersion =
              [ParameterVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersion.html).newBuilder()
                  .setName(parameterVersionName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersionName.html#com_google_cloud_parametermanager_v1_ParameterVersionName_toString__)())
                  .setDisabled(true)
                  .build();
    
          // Build the field mask for the disabled field.
          [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) fieldMask = [FieldMaskUtil](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.util.FieldMaskUtil.html).fromString("disabled");
    
          // Update the parameter version to disable it.
          [ParameterVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersion.html) disabledParameterVersion =
              client.updateParameterVersion(parameterVersion, fieldMask);
          System.out.printf(
              "Disabled regional parameter version %s for regional parameter %s\n",
              disabledParameterVersion.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersion.html#com_google_cloud_parametermanager_v1_ParameterVersion_getName__)(), parameterId);
    
          return disabledParameterVersion;
        }
      }
    }

### Node.js

To run this code, first [set up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup) and [install the Parameter Manager Node.js SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-nodejs). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'my-project';
    // const locationId = 'us-central1';
    // const parameterId = 'my-parameter';
    // const versionId = 'v1';
    
    // Imports the Parameter Manager library
    const {ParameterManagerClient} = require('[@google-cloud/parametermanager](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)');
    
    // Adding the endpoint to call the regional parameter manager server
    const options = {
      apiEndpoint: `parametermanager.${locationId}.rep.googleapis.com`,
    };
    
    // Instantiates a client with regional endpoint
    const client = new [ParameterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)(options);
    
    async function disableRegionalParamVersion() {
      // Construct the full resource name
      const name = client.[parameterVersionPath](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/parametermanager/v1.parametermanagerclient.html)(
        projectId,
        locationId,
        parameterId,
        versionId
      );
    
      // Construct the request
      const request = {
        parameterVersion: {
          name: name,
          disabled: true,
        },
        updateMask: {
          paths: ['disabled'],
        },
      };
    
      // Make the API call to update the parameter version
      const [paramVersion] = await client.updateParameterVersion(request);
    
      console.log(
        `Disabled regional parameter version ${paramVersion.name} for parameter ${parameterId}`
      );
      return paramVersion;
    }
    
    return await disableRegionalParamVersion();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Parameter Manager PHP SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-php). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    // Import necessary classes for disable a parameter version.
    use Google\Cloud\ParameterManager\V1\Client\ParameterManagerClient;
    use Google\Cloud\ParameterManager\V1\ParameterVersion;
    use Google\Cloud\ParameterManager\V1\UpdateParameterVersionRequest;
    use Google\Protobuf\FieldMask;
    
    /**
     * Disables a regional parameter version using the Parameter Manager SDK for GCP.
     *
     * @param string $projectId The Google Cloud Project ID (e.g. 'my-project')
     * @param string $locationId The Parameter Location (e.g. 'us-central1')
     * @param string $parameterId The Parameter ID (e.g. 'my-param')
     * @param string $versionId The Version ID (e.g. 'my-param-version')
     */
    function disable_regional_param_version(string $projectId, string $locationId, string $parameterId, string $versionId): void
    {
        // Specify regional endpoint.
        $options = ['apiEndpoint' => "parametermanager.$locationId.rep.googleapis.com"];
    
        // Create a client for the Parameter Manager service.
        $client = new ParameterManagerClient($options);
    
        // Build the resource name of the parameter version.
        $parameterVersionName = $client->parameterVersionName($projectId, $locationId, $parameterId, $versionId);
    
        // Update the parameter version.
        $parameterVersion = (new ParameterVersion())
            ->setName($parameterVersionName)
            ->setDisabled(true);
    
        $updateMask = (new FieldMask())
            ->setPaths(['disabled']);
    
        // Prepare the request to disable the parameter version.
        $request = (new UpdateParameterVersionRequest())
            ->setUpdateMask($updateMask)
            ->setParameterVersion($parameterVersion);
    
        // Disable the parameter version using the client.
        $client->updateParameterVersion($request);
    
        // Print the parameter version details.
        printf('Disabled regional parameter version %s for parameter %s' . PHP_EOL, $versionId, $parameterId);
    }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Parameter Manager Python SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-python). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    def disable_regional_param_version(
        project_id: str, location_id: str, parameter_id: str, version_id: str
    ) -> parametermanager_v1.ParameterVersion:
        """
        Disables a regional parameter version in the given project.
    
        Args:
            project_id (str): The ID of the GCP project
            where the parameter is located.
            location_id (str): The region where the parameter is stored.
            parameter_id (str): The ID of the parameter
            for which version is to be disabled.
            version_id (str): The version ID of the parameter to be disabled.
    
        Returns:
            parametermanager_v1.ParameterVersion: An object representing
            the disabled parameter version.
    
        Example:
            disable_regional_param_version(
                "my-project",
                "us-central1",
                "my-regional-parameter",
                "v1"
            )
        """
    
        # Import the Parameter Manager client library.
        from google.cloud import [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest)
        from google.protobuf import field_mask_pb2
    
        # Endpoint to call the regional parameter manager server.
        api_endpoint = f"parametermanager.{location_id}.rep.googleapis.com"
    
        # Create the Parameter Manager client for the specified region.
        client = [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[ParameterManagerClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html)(
            client_options={"api_endpoint": api_endpoint}
        )
    
        # Build the resource name of the parameter version for the specified region.
        name = client.[parameter_version_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_parameter_version_path)(
            project_id, location_id, parameter_id, version_id
        )
    
        # Get the current parameter version to update its state.
        parameter_version = client.[get_parameter_version](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_get_parameter_version)(request={"name": name})
    
        # Disable the parameter version.
        parameter_version.disabled = True
    
        # Create a field mask to specify which fields to update.
        update_mask = field_mask_pb2.FieldMask(paths=["disabled"])
    
        # Define the parameter version update request.
        request = [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[UpdateParameterVersionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.UpdateParameterVersionRequest.html)(
            parameter_version=parameter_version,
            update_mask=update_mask,
        )
    
        # Update the parameter version.
        response = client.[update_parameter_version](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_update_parameter_version)(request=request)
    
        # Print the parameter version ID that it was disabled.
        print(
            f"Disabled regional parameter version {version_id} "
            f"for regional parameter {parameter_id}"
        )

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Parameter Manager Ruby SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-ruby). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    require "google/cloud/parameter_manager"
    
    ##
    # Disable a regional parameter version
    #
    # @param project_id [String] The Google Cloud project (e.g. "my-project")
    # @param location_id [String] The location name (e.g. "us-central1")
    # @param parameter_id [String] The parameter name (e.g. "my-parameter")
    # @param version_id [String] The version name (e.g. "my-version")
    #
    def disable_regional_param_version project_id:, location_id:, parameter_id:, version_id:
      # Endpoint for the regional parameter manager service.
      api_endpoint = "parametermanager.#{location_id}.rep.googleapis.com"
    
      # Create the Parameter Manager client.
      client = Google::Cloud::[ParameterManager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager.html).[parameter_manager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager/latest/Google-Cloud-ParameterManager.html) do |config|
        config.endpoint = api_endpoint
      end
    
      # Build the resource name of the parent project.
      name = client.[parameter_version_path](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager-V1-ParameterManager-Paths.html) project: project_id, location: location_id, parameter: parameter_id,
                                           parameter_version: version_id
    
      parameter_version = {
        name: name,
        disabled: true
      }
    
      update_mask = {
        paths: ["disabled"]
      }
    
      # Disabled the parameter version
      param_version = client.update_parameter_version parameter_version: parameter_version, update_mask: update_mask
    
      # Print the parameter version name.
      puts "Disabled regional parameter version #{version_id} for parameter #{parameter_id}"
    end

## What's next

  * [Enable a disabled parameter version](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/enable-disabled-versions)
  * [Delete a parameter version](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/delete-parameter-version)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
