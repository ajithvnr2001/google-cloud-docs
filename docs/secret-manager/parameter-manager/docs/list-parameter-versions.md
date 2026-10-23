---
url: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/list-parameter-versions/
title: View parameter version details \u00a0|\u00a0 Parameter Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:57:41.095263+00:00
---

# View parameter version details  |  Parameter Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/list-parameter-versions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Parameter Manager ](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/overview)



Send feedback 

#  View parameter version details Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This operation is intended for retrieving parameter metadata and isn't designed for high-volume access. For scalable, high-volume access to parameter values in your application, see [Access a parameter version](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/render-parameter-version).

This page describes how you can retrieve a list of all the versions of a parameter created over time and view the metadata of a specific version.

A parameter version represents the specific setting or configuration value that the parameter holds at a given point in time. While a parameter acts as a metadata container, the version contains the actual data payload. By looking at the list of versions, you can see how a parameter has changed over time and who made the change. This helps with auditing and troubleshooting. For example, if you're experiencing issues with your current configuration, examining disabled versions can help you understand what settings were previously used and potentially identify if a recent change caused the problem.

The parameter version details include its name, value, state, and creation and update timestamps.

## Required roles

To get the permissions that you need to list parameter versions, ask your administrator to grant you the [Parameter Manager Parameter Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.parameterViewer) (`roles/parametermanager.parameterViewer`) IAM role on the parameter, project, folder, or organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## List all parameter versions

To list all the parameter versions associated with a parameter, use one of the following methods:

**Global parameters**

### Console

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. Click **Parameter Manager** to go to the **Parameter Manager** page. You'll see the list of parameters for that project.

  3. Click the parameter name to view its versions.

The parameter details page opens with the **Versions** tab in focus where you can see all the versions of the selected parameter.




### gcloud

Before using any of the command data below, make the following replacements: 

  * PARAMETER_ID: the name of the parameter



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters versions list --parameter=PARAMETER_ID --location=global

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters versions list --parameter=PARAMETER_ID --location=global

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters versions list --parameter=PARAMETER_ID --location=global

You should receive a response similar to the following:
    
    
    NAME                                                                                DISABLED  CREATE_TIME                     UPDATE_TIME
    projects/production-1/locations/global/parameters/app_config/versions/configv3            2024-11-14T10:07:12.883361876Z  2024-11-14T10:07:13.331806596Z
    

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID
  * PARAMETER_ID: the name of the parameter



HTTP method and URL: 
    
    
    GET https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/parameters/PARAMETER_ID/versions

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
         "https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/parameters/PARAMETER_ID/versions"

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
        -Uri "https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/parameters/PARAMETER_ID/versions" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "parameterVersions": [
        {
          "name": "projects/production-1/locations/global/parameters/app_config/versions/configv3",
          "createTime": "2024-11-12T10:22:17.704800878Z",
          "updateTime": "2024-11-12T11:08:24.173199506Z",
          "disabled": true
        },
        {
          "name": "projects/production-1/locations/global/parameters/app_config/versions/configv2",
          "createTime": "2024-11-12T10:26:44.168165094Z",
          "updateTime": "2024-11-12T10:26:44.483145675Z"
        }
      ]
    }
    
    

### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Parameter Manager C# SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-csharp). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    using [Google.Api.Gax](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html);
    using [Google.Cloud.ParameterManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.html);
    
    public class ListParameterVersionsSample
    {
        /// <summary>
        /// This function lists parameter version using the Parameter Manager SDK for GCP.
        /// </summary>
        /// <param name="projectId">The ID of the project where the parameter is located.</param>
        /// <param name="parameterId">The ID of the parameter for which the version is to be listed.</param>
        /// <returns>A list of ParameterVersion objects.</returns>
        public IEnumerable<ParameterVersion> ListParameterVersions(
            string projectId,
            string parameterId)
        {
            // Create the client.
            [ParameterManagerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html) client = [ParameterManagerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html#Google_Cloud_ParameterManager_V1_ParameterManagerClient_Create)();
    
            // Build the parent resource name for the parameter.
            [ParameterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterName.html) parent = new [ParameterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterName.html)(projectId, "global", parameterId);
    
            // Call the API to list the parameter versions.
            PagedEnumerable<ListParameterVersionsResponse, ParameterVersion> response = client.[ListParameterVersions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html#Google_Cloud_ParameterManager_V1_ParameterManagerClient_ListParameterVersions_Google_Cloud_ParameterManager_V1_ListParameterVersionsRequest_Google_Api_Gax_Grpc_CallSettings_)(parent);
    
            // Print each parameter version name.
            foreach ([ParameterVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersion.html) parameterVersion in response)
            {
                Console.WriteLine($"Found parameter version: {parameterVersion.Name}");
            }
    
            // Return the list of parameter versions.
            return response;
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
    	"google.golang.org/api/iterator"
    )
    
    // listParamVersions lists parameter versions using the Parameter Manager SDK for GCP.
    //
    // w: The io.Writer object used to write the output.
    // projectID: The ID of the project where the parameter is located.
    // parameterID: The ID of the parameter for which the versions are to be listed.
    //
    // The function returns an error if the parameter version listing fails.
    func listParamVersions(w io.Writer, projectID, parameterID string) error {
    	// Create a context and a Parameter Manager client.
    	ctx := context.Background()
    	client, err := parametermanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create Parameter Manager client: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_Close)()
    
    	// Construct the name of the list parameter.
    	parent := fmt.Sprintf("projects/%s/locations/global/parameters/%s", projectID, parameterID)
    
    	// Build the request to list parameter versions.
    	req := &parametermanagerpb.ListParameterVersionsRequest{
    		Parent: parent,
    	}
    
    	// Call the API to list parameter versions.
    	parameterVersions := client.ListParameterVersions(ctx, req)
    	for {
    		version, err := parameterVersions.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("failed to list parameter versions: %w", err)
    		}
    
    		fmt.Fprintf(w, "Found parameter version %s with disabled state in %v\n", version.Name, version.Disabled)
    	}
    
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Parameter Manager Java SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-java). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    import com.google.cloud.parametermanager.v1.[ListParameterVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ListParameterVersionsRequest.html);
    import com.google.cloud.parametermanager.v1.[ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html);
    import com.google.cloud.parametermanager.v1.[ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html).[ListParameterVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.ListParameterVersionsPagedResponse.html);
    import com.google.cloud.parametermanager.v1.[ParameterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterName.html);
    import java.io.IOException;
    
    /** Class to list parameter versions using the Parameter Manager SDK for GCP. */
    public class ListParamVersions {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String parameterId = "your-parameter-id";
    
        // Call the method to list parameter versions.
        listParamVersions(projectId, parameterId);
      }
    
      // This is an example snippet that list all parameter versions
      public static [ListParameterVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.ListParameterVersionsPagedResponse.html) listParamVersions(
          String projectId, String parameterId) throws IOException {
        // Initialize the client that will be used to send requests. This client only needs to be
        // created once,
        // and can be reused for multiple requests.
        try ([ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html) client = [ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html).create()) {
          String locationId = "global";
    
          // Build the parameter name from the project and parameter ID.
          [ParameterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterName.html) parameterName = [ParameterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterName.html).of(projectId, locationId, parameterId);
    
          // Build the request to list parameter versions.
          [ListParameterVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ListParameterVersionsRequest.html) request =
              [ListParameterVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ListParameterVersionsRequest.html).newBuilder().setParent(parameterName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterName.html#com_google_cloud_parametermanager_v1_ParameterName_toString__)()).build();
    
          // Send the request and get the response.
          [ListParameterVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.ListParameterVersionsPagedResponse.html) response = client.listParameterVersions(request);
    
          // Iterate through all versions and print their details.
          response
              .iterateAll()
              .forEach(
                  version ->
                      System.out.printf(
                          "Found parameter version %s with state %s\n",
                          version.getName(), (version.getDisabled() ? "disabled" : "enabled")));
    
          return response;
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
    
    // Imports the Parameter Manager library
    const {ParameterManagerClient} = require('[@google-cloud/parametermanager](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)');
    
    // Instantiates a client
    const client = new [ParameterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)();
    
    async function listParamVersions() {
      // Construct the parent string for listing parameter versions globally
      const parent = client.[parameterPath](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/parametermanager/v1.parametermanagerclient.html)(projectId, 'global', parameterId);
    
      const request = {
        parent: parent,
      };
    
      // Use listParameterVersionsAsync to handle pagination automatically
      const parameterVersions = await client.[listParameterVersionsAsync](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/parametermanager/v1.parametermanagerclient.html)(request);
    
      for await (const version of parameterVersions) {
        console.log(
          `Found parameter version ${version.name} with state ${version.disabled ? 'disabled' : 'enabled'}`
        );
      }
      return parameterVersions;
    }
    
    return await listParamVersions();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Parameter Manager PHP SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-php). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    // Import necessary classes for list a parameter versions.
    use Google\Cloud\ParameterManager\V1\Client\ParameterManagerClient;
    use Google\Cloud\ParameterManager\V1\ListParameterVersionsRequest;
    
    /**
     * Lists a parameter versions using the Parameter Manager SDK for GCP.
     *
     * @param string $projectId The Google Cloud Project ID (e.g. 'my-project')
     * @param string $parameterId The Parameter ID (e.g. 'my-param')
     */
    function list_param_versions(string $projectId, string $parameterId): void
    {
        // Create a client for the Parameter Manager service.
        $client = new ParameterManagerClient();
    
        // Build the resource name of the parameter.
        $parent = $client->parameterName($projectId, 'global', $parameterId);
    
        // Prepare the request to list the parameter versions.
        $request = (new ListParameterVersionsRequest())
            ->setParent($parent);
    
        // Retrieve the parameter version using the client.
        foreach ($client->listParameterVersions($request) as $parameterVersion) {
            printf('Found parameter version: %s' . PHP_EOL, $parameterVersion->getName());
        }
    }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Parameter Manager Python SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-python). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    def list_param_versions(project_id: str, parameter_id: str) -> None:
        """
        Lists all versions of an existing parameter in the global location
        of the specified project using the Google Cloud Parameter Manager SDK.
    
        Args:
            project_id (str): The ID of the project where the parameter is located.
            parameter_id (str): The ID of the parameter for
            which versions are to be listed.
    
        Returns:
            None
    
        Example:
            list_param_versions(
                "my-project",
                "my-global-parameter"
            )
        """
        # Import the necessary library for Google Cloud Parameter Manager.
        from google.cloud import [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest)
    
        # Create the Parameter Manager client.
        client = [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[ParameterManagerClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html)()
    
        # Build the resource name of the parameter.
        parent = client.[parameter_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_parameter_path)(project_id, "global", parameter_id)
    
        # Define the request to list parameter versions.
        request = [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[ListParameterVersionsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.ListParameterVersionsRequest.html)(parent=parent)
    
        # List the parameter versions.
        page_result = client.[list_parameter_versions](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_list_parameter_versions)(request=request)
    
        # Print the versions of the parameter.
        for response in page_result:
            print(f"Found parameter version: {response.name}")
    

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Parameter Manager Ruby SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-ruby). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    require "google/cloud/parameter_manager"
    
    ##
    # List a parameter versions
    #
    # @param project_id [String] The Google Cloud project (e.g. "my-project")
    # @param parameter_id [String] The parameter ID (e.g. "my-parameter")
    #
    def list_param_versions project_id:, parameter_id:
      # Create a Parameter Manager client.
      client = Google::Cloud::[ParameterManager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager.html).[parameter_manager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager/latest/Google-Cloud-ParameterManager.html)
    
      # Build the resource name of the parent project.
      parent = client.[parameter_path](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager-V1-ParameterManager-Paths.html) project: project_id, location: "global", parameter: parameter_id
    
      # List the parameter versions.
      param_version_list = client.list_parameter_versions parent: parent
    
      # Print out all parameter versions.
      param_version_list.each do |param_version|
        puts "Found parameter version #{param_version.name} with state #{param_version.disabled ? 'disabled' : 'enabled'}"
      end
    end

**Regional parameters**

### Console

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. Click **Parameter Manager** to go to the **Parameter Manager** page. You'll see the list of parameters for that project.

  3. Click the parameter name to view its versions.

The parameter details page opens with the **Versions** tab in focus where you can see all the versions of the selected parameter.




### gcloud

Before using any of the command data below, make the following replacements: 

  * PARAMETER_ID: the name of the parameter
  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the parameter



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters versions list --parameter=PARAMETER_ID --location=LOCATION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters versions list --parameter=PARAMETER_ID --location=LOCATION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters versions list --parameter=PARAMETER_ID --location=LOCATION

You should receive a response similar to the following:
    
    
    NAME                                                                                DISABLED  CREATE_TIME                     UPDATE_TIME
    projects/production-1/locations/us-central1/parameters/app_config/versions/configv3            2024-11-14T10:07:12.883361876Z  2024-11-14T10:07:13.331806596Z
    

### REST

Before using any of the request data, make the following replacements: 

  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the parameter
  * PROJECT_ID: the Google Cloud project ID
  * PARAMETER_ID: the name of the parameter



HTTP method and URL: 
    
    
    GET https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID/versions

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
         "https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID/versions"

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
        -Uri "https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID/versions" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "parameterVersions": [
        {
          "name": "projects/production-1/locations/us-central1/parameters/app_config/versions/configv3",
          "createTime": "2024-10-30T05:27:51.206825427Z",
          "updateTime": "2024-10-30T05:27:51.442194863Z"
        }
      ]
    }
    
    

### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Parameter Manager C# SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-csharp). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    using [Google.Api.Gax](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html);
    using [Google.Cloud.ParameterManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.html);
    
    public class ListRegionalParameterVersionsSample
    {
        /// <summary>
        /// This function lists all versions of a regional parameter using the Parameter Manager SDK for GCP.
        /// </summary>
        /// <param name="projectId">The ID of the project where the parameter is located.</param>
        /// <param name="locationId">The ID of the region where the parameter is located.</param>
        /// <param name="parameterId"> The ID of the parameter for which the version is to be listed.</param>
        /// <returns>A list of ParameterVersion objects.</returns>
        public IEnumerable<ParameterVersion> ListRegionalParameterVersions(
            string projectId,
            string locationId,
            string parameterId)
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
    
            // Call the API to list the parameter versions
            PagedEnumerable<ListParameterVersionsResponse, ParameterVersion> response = client.[ListParameterVersions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html#Google_Cloud_ParameterManager_V1_ParameterManagerClient_ListParameterVersions_Google_Cloud_ParameterManager_V1_ListParameterVersionsRequest_Google_Api_Gax_Grpc_CallSettings_)(parent);
    
            // Print each parameter version name
            foreach ([ParameterVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersion.html) version in response)
            {
                Console.WriteLine($"Found regional parameter version: {version.Name}");
            }
    
            // Return the list of parameter versions
            return response;
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
    	"google.golang.org/api/iterator"
    	"google.golang.org/api/option"
    )
    
    // listRegionalParamVersion lists all parameter versions regional using the Parameter Manager SDK for GCP.
    //
    // w: The io.Writer object used to write the output.
    // projectID: The ID of the project where the parameter is located.
    // locationID: The ID of the region where the parameter is located.
    // parameterID: The ID of the parameter for which the version is to be listed.
    //
    // The function returns an error if the parameter version listing fails
    func listRegionalParamVersion(w io.Writer, projectID, locationID, parameterID string) error {
    	// Create a new context.
    	ctx := context.Background()
    
    	// Create a Parameter Manager client.
    	endpoint := fmt.Sprintf("parametermanager.%s.rep.googleapis.com:443", locationID)
    	client, err := parametermanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_NewClient)(ctx, option.WithEndpoint(endpoint))
    	if err != nil {
    		return fmt.Errorf("failed to create Parameter Manager client: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_Close)()
    
    	// Construct the name of the parameter to list versions.
    	parent := fmt.Sprintf("projects/%s/locations/%s/parameters/%s", projectID, locationID, parameterID)
    
    	// Build the request to list all parameter versions.
    	req := &parametermanagerpb.ListParameterVersionsRequest{
    		Parent: parent,
    	}
    
    	// Call the API to list all parameter versions.
    	parameterVersions := client.ListParameterVersions(ctx, req)
    	for {
    		version, err := parameterVersions.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("failed to list parameter versions: %w", err)
    		}
    
    		fmt.Fprintf(w, "Found regional parameter version %s with disabled state in %v\n", version.Name, version.Disabled)
    	}
    
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Parameter Manager Java SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-java). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    import com.google.cloud.parametermanager.v1.[ListParameterVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ListParameterVersionsRequest.html);
    import com.google.cloud.parametermanager.v1.[ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html);
    import com.google.cloud.parametermanager.v1.[ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html).[ListParameterVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.ListParameterVersionsPagedResponse.html);
    import com.google.cloud.parametermanager.v1.[ParameterManagerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerSettings.html);
    import com.google.cloud.parametermanager.v1.[ParameterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterName.html);
    import java.io.IOException;
    
    /**
     * Class to list parameter versions for a specified region using the Parameter Manager SDK
     * for GCP.
     */
    public class ListRegionalParamVersions {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "your-location-id";
        String parameterId = "your-parameter-id";
    
        // Call the method to list parameter versions regionally.
        listRegionalParamVersions(projectId, locationId, parameterId);
      }
    
      // This is an example snippet that list all parameter versions regionally
      public static [ListParameterVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.ListParameterVersionsPagedResponse.html) listRegionalParamVersions(
          String projectId, String locationId, String parameterId) throws IOException {
        // Endpoint to call the regional parameter manager server
        String apiEndpoint = String.format("parametermanager.%s.rep.googleapis.com:443", locationId);
        [ParameterManagerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerSettings.html) parameterManagerSettings =
            [ParameterManagerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerSettings.html).newBuilder().setEndpoint(apiEndpoint).build();
    
        // Initialize the client that will be used to send requests. This client only needs to be
        // created once,
        // and can be reused for multiple requests.
        try ([ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html) client = [ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html).create(parameterManagerSettings)) {
          // Build the parameter name from the project and parameter ID.
          [ParameterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterName.html) parameterName = [ParameterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterName.html).of(projectId, locationId, parameterId);
    
          // Build the request to list parameter versions.
          [ListParameterVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ListParameterVersionsRequest.html) request =
              [ListParameterVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ListParameterVersionsRequest.html).newBuilder().setParent(parameterName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterName.html#com_google_cloud_parametermanager_v1_ParameterName_toString__)()).build();
    
          // Send the request and get the response.
          [ListParameterVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.ListParameterVersionsPagedResponse.html) response = client.listParameterVersions(request);
    
          // Iterate through all versions and print their details.
          response
              .iterateAll()
              .forEach(
                  version ->
                      System.out.printf(
                          "Found regional parameter version %s with state %s\n",
                          version.getName(), (version.getDisabled() ? "disabled" : "enabled")));
    
          return response;
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
    
    // Imports the Parameter Manager library
    const {ParameterManagerClient} = require('[@google-cloud/parametermanager](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)');
    
    // Adding the endpoint to call the regional parameter manager server
    const options = {
      apiEndpoint: `parametermanager.${locationId}.rep.googleapis.com`,
    };
    
    // Instantiates a client with regional endpoint
    const client = new [ParameterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)(options);
    
    async function listRegionalParamVersions() {
      // Construct the parent string for listing parameter versions in a specific region
      const parent = client.[parameterPath](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/parametermanager/v1.parametermanagerclient.html)(projectId, locationId, parameterId);
    
      const request = {
        parent: parent,
      };
    
      // Use listParameterVersionsAsync to handle pagination automatically
      const paramVersions = await client.[listParameterVersionsAsync](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/parametermanager/v1.parametermanagerclient.html)(request);
    
      for await (const version of paramVersions) {
        console.log(
          `Found regional parameter version ${version.name} with state ${version.disabled ? 'disabled' : 'enabled'} `
        );
      }
      return paramVersions;
    }
    
    return await listRegionalParamVersions();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Parameter Manager PHP SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-php). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    // Import necessary classes for list a parameter versions.
    use Google\Cloud\ParameterManager\V1\Client\ParameterManagerClient;
    use Google\Cloud\ParameterManager\V1\ListParameterVersionsRequest;
    
    /**
     * Lists a regional parameter versions using the Parameter Manager SDK for GCP.
     *
     * @param string $projectId The Google Cloud Project ID (e.g. 'my-project')
     * @param string $locationId The Parameter Location (e.g. 'us-central1')
     * @param string $parameterId The Parameter ID (e.g. 'my-param')
     */
    function list_regional_param_versions(string $projectId, string $locationId, string $parameterId): void
    {
        // Specify regional endpoint.
        $options = ['apiEndpoint' => "parametermanager.$locationId.rep.googleapis.com"];
    
        // Create a client for the Parameter Manager service.
        $client = new ParameterManagerClient($options);
    
        // Build the resource name of the parameter.
        $parent = $client->parameterName($projectId, $locationId, $parameterId);
    
        // Prepare the request to list the parameter versions.
        $request = (new ListParameterVersionsRequest())
            ->setParent($parent);
    
        // Retrieve the parameter version using the client.
        foreach ($client->listParameterVersions($request) as $parameterVersion) {
            printf('Found regional parameter version: %s' . PHP_EOL, $parameterVersion->getName());
        }
    }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Parameter Manager Python SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-python). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    def list_regional_param_versions(
        project_id: str, location_id: str, parameter_id: str
    ) -> None:
        """
        List all versions of a regional parameter in Google Cloud Parameter Manager.
    
        This function lists all versions of an existing
        parameter in the specified region of the specified project
        using the Google Cloud Parameter Manager SDK.
    
        Args:
            project_id (str): The ID of the project where the parameter is located.
            location_id (str): The ID of the region where the parameter is located.
            parameter_id (str): The ID of the parameter for
            which versions are to be listed.
    
        Returns:
            None
    
        Example:
            list_regional_param_versions(
                "my-project",
                "us-central1",
                "my-regional-parameter"
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
    
        # Define the request to list parameter versions.
        request = [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[ListParameterVersionsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.ListParameterVersionsRequest.html)(parent=parent)
    
        # List the parameter versions.
        page_result = client.[list_parameter_versions](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_list_parameter_versions)(request=request)
    
        # Print the versions of the parameter.
        for response in page_result:
            print(f"Found regional parameter version: {response.name}")

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Parameter Manager Ruby SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-ruby). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    require "google/cloud/parameter_manager"
    
    ##
    # List a regional parameter versions
    #
    # @param project_id [String] The Google Cloud project (e.g. "my-project")
    # @param location_id [String] The location name (e.g. "us-central1")
    # @param parameter_id [String] The parameter ID (e.g. "my-parameter")
    #
    def list_regional_param_versions project_id:, location_id:, parameter_id:
      # Endpoint for the regional parameter manager service.
      api_endpoint = "parametermanager.#{location_id}.rep.googleapis.com"
    
      # Create the Parameter Manager client.
      client = Google::Cloud::[ParameterManager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager.html).[parameter_manager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager/latest/Google-Cloud-ParameterManager.html) do |config|
        config.endpoint = api_endpoint
      end
    
      # Build the resource name of the parent project.
      parent = client.[parameter_path](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager-V1-ParameterManager-Paths.html) project: project_id, location: location_id, parameter: parameter_id
    
      # List the parameter versions.
      param_version_list = client.list_parameter_versions parent: parent
    
      # Print out all parameter versions.
      param_version_list.each do |param_version|
        state = param_version.disabled ? "disabled" : "enabled"
        puts "Found regional parameter version #{param_version.name} with state #{state}"
      end
    end

## View parameter version details

To view the details of a parameter version, use one of the following methods:

**Global parameters**

### Console

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. Click **Parameter Manager** to go to the **Parameter Manager** page. You'll see the list of parameters for that project.

  3. Click the parameter name to access its versions.

The parameter details page opens with the **Versions** tab in focus where you can see all the versions of the selected parameter. For each version, the version ID and its metadata is also displayed in the table.

  4. Certain parameter versions contain secret values. To inspect the raw parameter payload before secret substitution, select the version and then click **View payload** from the more_vert**Actions** menu.

Viewing the payload lets you verify the parameter's structure and content before secret substitution. This helps you check the parameter configuration and understand its structure.




### gcloud

Before using any of the command data below, make the following replacements: 

  * PARAMETER_VERSION_ID: the ID of the parameter version
  * PARAMETER_ID: the name of the parameter



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters versions describe PARAMETER_VERSION_ID --parameter=PARAMETER_ID --location=global

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters versions describe PARAMETER_VERSION_ID --parameter=PARAMETER_ID --location=global

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters versions describe PARAMETER_VERSION_ID --parameter=PARAMETER_ID --location=global

You should receive a response similar to the following:
    
    
    createTime: '2024-11-14T10:07:12.883361876Z'
    name: projects/production-1/locations/global/parameters/app_config/versions/configv3
    payload:
      data: YWJj
    updateTime: '2024-11-14T10:07:13.331806596Z'
    

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID
  * PARAMETER_ID: the name of the parameter
  * PARAMETER_VERSION_ID: the ID of the parameter version



HTTP method and URL: 
    
    
    GET https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/parameters/PARAMETER_ID/versions/PARAMETER_VERSION_ID

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
         "https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/parameters/PARAMETER_ID/versions/PARAMETER_VERSION_ID"

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
        -Uri "https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/parameters/PARAMETER_ID/versions/PARAMETER_VERSION_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/production-1/locations/global/parameters/app_config/versions/configv1",
      "createTime": "2024-10-16T03:08:42.914611506Z",
      "updateTime": "2024-10-16T03:08:44.530493212Z",
      "payload": {
        "data": "cHJvamVjdDoNCiAgZGlzcGxheV9uYW1lOiBQTSBCYW5rDQogIGxvY2FsZTogZW4tVVMNCiAgcG9ydDogODA4MA0KICBkYl9wYXNzd29yZDogX19SRUZfXygiLy9zZWNyZXRtYW5hZ2VyLmdvb2dsZWFwaXMuY29tL3Byb2plY3RzL2FjbS1zYW1wbGUvc2VjcmV0cy9kYl9wYXNzd29yZC92ZXJzaW9ucy8xIikNCiAgbWFza19zZW5zaXRpdmVfZmllbGRzOiBmYWxzZQ=="
      }
    }
    
    

### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Parameter Manager C# SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-csharp). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    using [Google.Cloud.ParameterManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.html);
    using System.Text;
    
    public class GetParameterVersionSample
    {
        /// <summary>
        /// This function retrieves a parameter version using the Parameter Manager SDK for GCP.
        /// </summary>
        /// <param name="projectId">The ID of the project where the parameter is located.</param>
        /// <param name="parameterId">The ID of the parameter for which the version is to be retrieved.</param>
        /// <param name="versionId">The ID of the version to be retrieved.</param>
        /// <returns>The retrieved ParameterVersion object.</returns>
        public ParameterVersion GetParameterVersion(
            string projectId,
            string parameterId,
            string versionId)
        {
            // Create the client.
            [ParameterManagerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html) client = [ParameterManagerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html#Google_Cloud_ParameterManager_V1_ParameterManagerClient_Create)();
    
            // Build the resource name for the parameter version.
            [ParameterVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName.html) parameterVersionName = new [ParameterVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersionName.html)(projectId, "global", parameterId, versionId);
    
            // Call the API to get the parameter version.
            [ParameterVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersion.html) parameterVersion = client.[GetParameterVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html#Google_Cloud_ParameterManager_V1_ParameterManagerClient_GetParameterVersion_Google_Cloud_ParameterManager_V1_GetParameterVersionRequest_Google_Api_Gax_Grpc_CallSettings_)(parameterVersionName);
    
            // Print the retrieved parameter version name.
            Console.WriteLine($"Found regional parameter version {parameterVersion.[Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersion.html#Google_Cloud_ParameterManager_V1_ParameterVersion_Name)} with state {(parameterVersion.[Disabled](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersion.html#Google_Cloud_ParameterManager_V1_ParameterVersion_Disabled) ? "disabled" : "enabled")}");
    
            if (!parameterVersion.[Disabled](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersion.html#Google_Cloud_ParameterManager_V1_ParameterVersion_Disabled))
            {
                Console.WriteLine($"Payload: {Encoding.UTF8.GetString(parameterVersion.[Payload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersion.html#Google_Cloud_ParameterManager_V1_ParameterVersion_Payload).Data.ToByteArray())}");
            }
    
            // Return the retrieved parameter version.
            return parameterVersion;
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
    
    // getParamVersion get parameter version using the Parameter Manager SDK for GCP.
    //
    // w: The io.Writer object used to write the output.
    // projectID: The ID of the project where the parameter is located.
    // parameterID: The ID of the parameter for which the version details are to be retrieved.
    // versionID: The ID of the version to be retrieved.
    //
    // The function returns an error if the parameter version retrieval fails.
    func getParamVersion(w io.Writer, projectID, parameterID, versionID string) error {
    	// Create a context and a Parameter Manager client.
    	ctx := context.Background()
    	client, err := parametermanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create Parameter Manager client: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_Close)()
    
    	// Construct the name of the parameter to get the parameter version.
    	name := fmt.Sprintf("projects/%s/locations/global/parameters/%s/versions/%s", projectID, parameterID, versionID)
    
    	// Build the request to get parameter version.
    	req := &parametermanagerpb.GetParameterVersionRequest{
    		Name: name,
    	}
    
    	// Call the API to get parameter version.
    	version, err := client.GetParameterVersion(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to get parameter version: %w", err)
    	}
    
    	// Find more details for the Parameter Version object here:
    	// https://cloud.google.com/secret-manager/parameter-manager/docs/reference/rest/v1/projects.locations.parameters.versions#ParameterVersion
    	fmt.Fprintf(w, "Found parameter version %s with disabled state in %v\n", version.Name, version.Disabled)
    	if !version.Disabled {
    		fmt.Fprintf(w, "Payload: %s\n", version.Payload.Data)
    	}
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Parameter Manager Java SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-java). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    import com.google.cloud.parametermanager.v1.[ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html);
    import com.google.cloud.parametermanager.v1.[ParameterVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersion.html);
    import com.google.cloud.parametermanager.v1.[ParameterVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersionName.html);
    import java.io.IOException;
    
    /**
     * This class demonstrates how to get a parameter version using the Parameter Manager SDK for GCP.
     */
    public class GetParamVersion {
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String parameterId = "your-parameter-id";
        String versionId = "your-version-id";
    
        // Call the method to get a parameter version.
        getParamVersion(projectId, parameterId, versionId);
      }
    
      // This is an example snippet for getting a parameter version.
      public static [ParameterVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersion.html) getParamVersion(
          String projectId, String parameterId, String versionId) throws IOException {
        // Initialize the client that will be used to send requests. This client only
        // needs to be created once, and can be reused for multiple requests.
        try ([ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html) client = [ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html).create()) {
          String locationId = "global";
    
          // Build the parameter version name.
          [ParameterVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersionName.html) parameterVersionName =
              [ParameterVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersionName.html).of(projectId, locationId, parameterId, versionId);
    
          // Get the parameter version.
          [ParameterVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersion.html) parameterVersion =
              client.getParameterVersion(parameterVersionName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersionName.html#com_google_cloud_parametermanager_v1_ParameterVersionName_toString__)());
          // Find more details for the Parameter Version object here:
          // https://cloud.google.com/secret-manager/parameter-manager/docs/reference/rest/v1/projects.locations.parameters.versions#ParameterVersion
          System.out.printf(
              "Found parameter version %s with state %s\n",
              parameterVersion.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersion.html#com_google_cloud_parametermanager_v1_ParameterVersion_getName__)(), (parameterVersion.[getDisabled](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersion.html#com_google_cloud_parametermanager_v1_ParameterVersion_getDisabled__)() ? "disabled" : "enabled"));
          if (!parameterVersion.[getDisabled](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersion.html#com_google_cloud_parametermanager_v1_ParameterVersion_getDisabled__)()) {
            System.out.printf("Payload: %s\n", parameterVersion.[getPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersion.html#com_google_cloud_parametermanager_v1_ParameterVersion_getPayload__)().getData().toStringUtf8());
          }
          return parameterVersion;
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
    
    async function getParamVersion() {
      // Construct the fully qualified parameter version name
      const name = client.[parameterVersionPath](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/parametermanager/v1.parametermanagerclient.html)(
        projectId,
        'global',
        parameterId,
        versionId
      );
    
      // Get the parameter version
      const [parameterVersion] = await client.getParameterVersion({
        name: name,
      });
      // Find more details for the Parameter Version object here:
      // https://cloud.google.com/secret-manager/parameter-manager/docs/reference/rest/v1/projects.locations.parameters.versions#ParameterVersion
      console.log(
        `Found parameter version ${parameterVersion.name} with state ${parameterVersion.disabled ? 'disabled' : 'enabled'}`
      );
      if (!parameterVersion.disabled) {
        console.log(
          `Payload: ${parameterVersion.payload.data.toString('utf-8')}`
        );
      }
      return parameterVersion;
    }
    
    return await getParamVersion();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Parameter Manager PHP SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-php). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    // Import necessary classes for retrieve a parameter.
    use Google\Cloud\ParameterManager\V1\Client\ParameterManagerClient;
    use Google\Cloud\ParameterManager\V1\GetParameterVersionRequest;
    
    /**
     * Retrieves a parameter version using the Parameter Manager SDK for GCP.
     *
     * @param string $projectId The Google Cloud Project ID (e.g. 'my-project')
     * @param string $parameterId The Parameter ID (e.g. 'my-param')
     * @param string $versionId The Version ID (e.g. 'my-param-version')
     */
    function get_param_version(string $projectId, string $parameterId, string $versionId): void
    {
        // Create a client for the Parameter Manager service.
        $client = new ParameterManagerClient();
    
        // Build the resource name of the parameter version.
        $parameterVersionName = $client->parameterVersionName($projectId, 'global', $parameterId, $versionId);
    
        // Prepare the request to get the parameter version.
        $request = (new GetParameterVersionRequest())
            ->setName($parameterVersionName);
    
        // Retrieve the parameter version using the client.
        $parameterVersion = $client->getParameterVersion($request);
    
        // Print the retrieved parameter version details.
        printf('Found parameter version %s with state %s' . PHP_EOL, $parameterVersion->getName(), $parameterVersion->getDisabled() ? 'disabled' : 'enabled');
        if (!($parameterVersion->getDisabled())) {
            printf('Payload: %s' . PHP_EOL, $parameterVersion->getPayload()->getData());
        }
    }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Parameter Manager Python SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-python). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    # The GetParameterVersion operation retrieves parameter metadata and doesn't
    # support high-volume access. To access parameter values at scale,
    # see Access a parameter version (https://docs.cloud.google.com/secret-manager/parameter-manager/docs/render-parameter-version).
    
    
    def get_param_version(
        project_id: str, parameter_id: str, version_id: str
    ) -> parametermanager_v1.ParameterVersion:
        """
        Retrieves the details of a specific version of an
        existing parameter in the specified
        project using the Google Cloud Parameter Manager SDK.
    
        Args:
            project_id (str): The ID of the project where the parameter is located.
            parameter_id (str): The ID of the parameter for
            which the version details are to be retrieved.
            version_id (str): The ID of the version to be retrieved.
    
        Returns:
            parametermanager_v1.ParameterVersion: An object
            representing the parameter version.
    
        Example:
            get_param_version(
                "my-project",
                "my-global-parameter",
                "v1"
            )
        """
        # Import the necessary library for Google Cloud Parameter Manager.
        from google.cloud import [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest)
    
        # Create the Parameter Manager client.
        client = [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[ParameterManagerClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html)()
    
        # Build the resource name of the parameter version.
        name = client.[parameter_version_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_parameter_version_path)(project_id, "global", parameter_id, version_id)
    
        # Define the request to get the parameter version details.
        request = [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[GetParameterVersionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.GetParameterVersionRequest.html)(name=name)
    
        # Get the parameter version details.
        response = client.[get_parameter_version](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_get_parameter_version)(request=request)
    
        # Show parameter version details.
        # Find more details for the Parameter Version object here:
        # https://cloud.google.com/secret-manager/parameter-manager/docs/reference/rest/v1/projects.locations.parameters.versions#ParameterVersion
        print(f"Found parameter version {response.name} with state {'disabled' if response.disabled else 'enabled'}")
        if not response.disabled:
            print(f"Payload: {response.payload.data.decode('utf-8')}")

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Parameter Manager Ruby SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-ruby). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    require "google/cloud/parameter_manager"
    
    ##
    # Retrieve a parameter version
    #
    # @param project_id [String] The Google Cloud project (e.g. "my-project")
    # @param parameter_id [String] The parameter name (e.g. "my-parameter")
    # @param version_id [String] The version name (e.g. "my-version")
    #
    def get_param_version project_id:, parameter_id:, version_id:
      # Create a Parameter Manager client.
      client = Google::Cloud::[ParameterManager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager.html).[parameter_manager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager/latest/Google-Cloud-ParameterManager.html)
    
      # Build the resource name of the parent project.
      name = client.[parameter_version_path](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager-V1-ParameterManager-Paths.html) project: project_id, location: "global", parameter: parameter_id,
                                           parameter_version: version_id
    
      # Retrieve the parameter version.
      param_version = client.get_parameter_version name: name
    
      # Print the retrieved parameter version name.
      puts "Found parameter version #{param_version.name} with state #{param_version.disabled ? 'disabled' : 'enabled'}"
    
      # Use a guard clause to return early if the parameter version is disabled.
      return if param_version.disabled
    
      puts "Payload: #{param_version.payload.data}"
    end

**Regional parameters**

### Console

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. Click **Parameter Manager** to go to the **Parameter Manager** page. You'll see the list of parameters for that project.

  3. Click the parameter name to access its versions.

The parameter details page opens with the **Versions** tab in focus where you can see all the versions of the selected parameter. For each version, the version ID and its metadata is also displayed in the table.

  4. Certain parameter versions contain secret values. To inspect the raw parameter payload before secret substitution, select the version and then click **View payload** from the more_vert**Actions** menu.

Viewing the payload lets you verify the parameter's structure and content before secret substitution. This helps you check the parameter configuration and understand its structure.




### gcloud

Before using any of the command data below, make the following replacements: 

  * PARAMETER_VERSION_ID: the ID of the parameter version
  * PARAMETER_ID: the name of the parameter
  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the parameter



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters versions describe PARAMETER_VERSION_ID --parameter=PARAMETER_ID --location=LOCATION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters versions describe PARAMETER_VERSION_ID --parameter=PARAMETER_ID --location=LOCATION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters versions describe PARAMETER_VERSION_ID --parameter=PARAMETER_ID --location=LOCATION

You should receive a response similar to the following:
    
    
    createTime: '2024-11-14T10:07:12.883361876Z'
    name: projects/production-1/locations/us-central1/parameters/app_config/versions/configv3
    payload:
      data: YWJj
    updateTime: '2024-11-14T10:07:13.331806596Z'
    

### REST

Before using any of the request data, make the following replacements: 

  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the parameter
  * PROJECT_ID: the Google Cloud project ID
  * PARAMETER_ID: the name of the parameter
  * PARAMETER_VERSION_ID: the ID of the parameter version



HTTP method and URL: 
    
    
    GET https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID/versions/PARAMETER_VERSION_ID?view=FULL

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
         "https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID/versions/PARAMETER_VERSION_ID?view=FULL"

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
        -Uri "https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID/versions/PARAMETER_VERSION_ID?view=FULL" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/production-1/locations/us-central1/parameters/app_config/versions/configv2",
      "createTime": "2024-10-30T05:27:51.206825427Z",
      "updateTime": "2024-10-30T05:27:51.442194863Z",
      "payload": {
        "data": "YTogYgo="
      }
    }
    
    

### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Parameter Manager C# SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-csharp). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    using [Google.Cloud.ParameterManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.html);
    using System.Text;
    
    public class GetRegionalParameterVersionSample
    {
        /// <summary>
        /// This function retrieves a regional parameter version using the Parameter Manager SDK for GCP.
        /// </summary>
        /// <param name="projectId">The ID of the project where the parameter is located.</param>
        /// <param name="locationId">The ID of the region where the parameter is located.</param>
        /// <param name="parameterId">The ID of the parameter for which the version is to be retrieved.</param>
        /// <param name="versionId">The ID of the version to be retrieved.</param>
        /// <returns>The retrieved ParameterVersion object.</returns>
        public ParameterVersion GetRegionalParameterVersion(
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
    
            // Call the API to get the parameter version
            [ParameterVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersion.html) parameterVersion = client.[GetParameterVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html#Google_Cloud_ParameterManager_V1_ParameterManagerClient_GetParameterVersion_Google_Cloud_ParameterManager_V1_GetParameterVersionRequest_Google_Api_Gax_Grpc_CallSettings_)(parameterVersionName);
    
    
    
            // Print the retrieved parameter version name
            Console.WriteLine($"Found regional parameter version {parameterVersion.[Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersion.html#Google_Cloud_ParameterManager_V1_ParameterVersion_Name)} with state {(parameterVersion.[Disabled](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersion.html#Google_Cloud_ParameterManager_V1_ParameterVersion_Disabled) ? "disabled" : "enabled")}");
    
            if (!parameterVersion.[Disabled](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersion.html#Google_Cloud_ParameterManager_V1_ParameterVersion_Disabled))
            {
                Console.WriteLine($"Payload: {Encoding.UTF8.GetString(parameterVersion.[Payload](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterVersion.html#Google_Cloud_ParameterManager_V1_ParameterVersion_Payload).Data.ToByteArray())}");
            }
    
            // Return the retrieved parameter version
            return parameterVersion;
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
    
    // getRegionalParamVersion gets a parameter version regional using the Parameter Manager SDK for GCP.
    //
    // w: The io.Writer object used to write the output.
    // projectID: The ID of the project where the parameter is located.
    // locationID: The ID of the region where the parameter is located.
    // parameterID: The ID of the parameter for which the version is to be retrieved.
    // versionID: The ID of the version to be retrieved.
    //
    // The function returns an error if the parameter version retrieval fails.
    func getRegionalParamVersion(w io.Writer, projectID, locationID, parameterID, versionID string) error {
    	// Create a new context.
    	ctx := context.Background()
    
    	// Create a Parameter Manager client.
    	endpoint := fmt.Sprintf("parametermanager.%s.rep.googleapis.com:443", locationID)
    	client, err := parametermanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_NewClient)(ctx, option.WithEndpoint(endpoint))
    	if err != nil {
    		return fmt.Errorf("failed to create Parameter Manager client: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_Close)()
    
    	// Construct the name of the parameter version to retrieve.
    	name := fmt.Sprintf("projects/%s/locations/%s/parameters/%s/versions/%s", projectID, locationID, parameterID, versionID)
    
    	// Build the request to get the parameter version.
    	req := &parametermanagerpb.GetParameterVersionRequest{
    		Name: name,
    	}
    
    	// Call the API to get the parameter version.
    	version, err := client.GetParameterVersion(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to get parameter version: %w", err)
    	}
    
    	// Find more details for the Parameter Version object here:
    	// https://cloud.google.com/secret-manager/parameter-manager/docs/reference/rest/v1/projects.locations.parameters.versions#ParameterVersion
    	fmt.Fprintf(w, "Found regional parameter version %s with disabled state in %v\n", version.Name, version.Disabled)
    	if !version.Disabled {
    		fmt.Fprintf(w, "Payload: %s\n", version.Payload.Data)
    	}
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Parameter Manager Java SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-java). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    import com.google.cloud.parametermanager.v1.[ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html);
    import com.google.cloud.parametermanager.v1.[ParameterManagerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerSettings.html);
    import com.google.cloud.parametermanager.v1.[ParameterVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersion.html);
    import com.google.cloud.parametermanager.v1.[ParameterVersionName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersionName.html);
    import java.io.IOException;
    
    /**
     * This class demonstrates how to get a regional parameter version using the Parameter Manager SDK
     * for GCP.
     */
    public class GetRegionalParamVersion {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "your-location-id";
        String parameterId = "your-parameter-id";
        String versionId = "your-version-id";
    
        // Call the method to get a regional parameter version.
        getRegionalParamVersion(projectId, locationId, parameterId, versionId);
      }
    
      // This is an example snippet that gets a regional parameter version.
      public static [ParameterVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersion.html) getRegionalParamVersion(
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
    
          // Get the parameter version.
          [ParameterVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersion.html) parameterVersion =
              client.getParameterVersion(parameterVersionName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersionName.html#com_google_cloud_parametermanager_v1_ParameterVersionName_toString__)());
          // Find more details for the Parameter Version object here:
          // https://cloud.google.com/secret-manager/parameter-manager/docs/reference/rest/v1/projects.locations.parameters.versions#ParameterVersion
          System.out.printf(
              "Found regional parameter version %s with state %s\n",
              parameterVersion.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersion.html#com_google_cloud_parametermanager_v1_ParameterVersion_getName__)(), (parameterVersion.[getDisabled](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersion.html#com_google_cloud_parametermanager_v1_ParameterVersion_getDisabled__)() ? "disabled" : "enabled"));
          if (!parameterVersion.[getDisabled](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersion.html#com_google_cloud_parametermanager_v1_ParameterVersion_getDisabled__)()) {
            System.out.printf("Payload: %s", parameterVersion.[getPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterVersion.html#com_google_cloud_parametermanager_v1_ParameterVersion_getPayload__)().getData().toStringUtf8());
          }
          return parameterVersion;
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
    
    async function getRegionalParamVersion() {
      // Construct the fully qualified parameter version name
      const name = client.[parameterVersionPath](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/parametermanager/v1.parametermanagerclient.html)(
        projectId,
        locationId,
        parameterId,
        versionId
      );
    
      // Get the parameter version
      const [parameterVersion] = await client.getParameterVersion({
        name: name,
      });
    
      // Find more details for the Parameter Version object here:
      // https://cloud.google.com/secret-manager/parameter-manager/docs/reference/rest/v1/projects.locations.parameters.versions#ParameterVersion
      console.log(
        `Found regional parameter version ${parameterVersion.name} with state ${parameterVersion.disabled ? 'disabled' : 'enabled'}`
      );
      if (!parameterVersion.disabled) {
        console.log(
          `Payload: ${parameterVersion.payload.data.toString('utf-8')}`
        );
      }
      return parameterVersion;
    }
    
    return await getRegionalParamVersion();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Parameter Manager PHP SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-php). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    // Import necessary classes for retrieve a parameter.
    use Google\Cloud\ParameterManager\V1\Client\ParameterManagerClient;
    use Google\Cloud\ParameterManager\V1\GetParameterVersionRequest;
    
    /**
     * Retrieves a regional parameter version using the Parameter Manager SDK for GCP.
     *
     * @param string $projectId The Google Cloud Project ID (e.g. 'my-project')
     * @param string $locationId The Parameter Location (e.g. 'us-central1')
     * @param string $parameterId The Parameter ID (e.g. 'my-param')
     * @param string $versionId The Version ID (e.g. 'my-param-version')
     */
    function get_regional_param_version(string $projectId, string $locationId, string $parameterId, string $versionId): void
    {
        // Specify regional endpoint.
        $options = ['apiEndpoint' => "parametermanager.$locationId.rep.googleapis.com"];
    
        // Create a client for the Parameter Manager service.
        $client = new ParameterManagerClient($options);
    
        // Build the resource name of the parameter version.
        $parameterVersionName = $client->parameterVersionName($projectId, $locationId, $parameterId, $versionId);
    
        // Prepare the request to get the parameter version.
        $request = (new GetParameterVersionRequest())
            ->setName($parameterVersionName);
    
        // Retrieve the parameter version using the client.
        $parameterVersion = $client->getParameterVersion($request);
    
        printf('Found regional parameter version %s with state %s' . PHP_EOL, $parameterVersion->getName(), $parameterVersion->getDisabled() ? 'disabled' : 'enabled');
        if (!($parameterVersion->getDisabled())) {
            printf('Payload: %s' . PHP_EOL, $parameterVersion->getPayload()->getData());
        }
    }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Parameter Manager Python SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-python). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    def get_regional_param_version(
        project_id: str, location_id: str, parameter_id: str, version_id: str
    ) -> parametermanager_v1.ParameterVersion:
        """
        Retrieves the details of a specific version of an
        existing parameter in the specified region of the specified
        project using the Google Cloud Parameter Manager SDK.
    
        Args:
            project_id (str): The ID of the project where the parameter is located.
            location_id (str): The ID of the region where the parameter is located.
            parameter_id (str): The ID of the parameter for
            which version details are to be retrieved.
            version_id (str): The ID of the version to be retrieved.
    
        Returns:
            parametermanager_v1.ParameterVersion: An object
            representing the parameter version.
    
        Example:
            get_regional_param_version(
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
    
        # Define the request to get the parameter version details.
        request = [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[GetParameterVersionRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.GetParameterVersionRequest.html)(name=name)
    
        # Get the parameter version details.
        response = client.[get_parameter_version](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_get_parameter_version)(request=request)
    
        # Show parameter version details.
        # Find more details for the Parameter Version object here:
        # https://cloud.google.com/secret-manager/parameter-manager/docs/reference/rest/v1/projects.locations.parameters.versions#ParameterVersion
        print(f"Found regional parameter version {response.name} with state {'disabled' if response.disabled else 'enabled'}")
        if not response.disabled:
            print(f"Payload: {response.payload.data.decode('utf-8')}")

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Parameter Manager Ruby SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-ruby). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    require "google/cloud/parameter_manager"
    
    ##
    # Retrieve a regional parameter version
    #
    # @param project_id [String] The Google Cloud project (e.g. "my-project")
    # @param location_id [String] The location name (e.g. "us-central1")
    # @param parameter_id [String] The parameter name (e.g. "my-parameter")
    # @param version_id [String] The version name (e.g. "my-version")
    #
    def get_regional_param_version project_id:, location_id:, parameter_id:, version_id:
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
      param_version = client.get_parameter_version name: name
    
      # Print the retrieved parameter version name.
      state = param_version.disabled ? "disabled" : "enabled"
      puts "Found regional parameter version #{param_version.name} with state #{state}"
    
      # Use a guard clause to return early if the parameter version is disabled.
      return if param_version.disabled
    
      puts "Payload: #{param_version.payload.data}"
    end

**Additional information about the REST command**

Use `view=FULL` in your request to the Parameter Manager API when you want the service to return the metadata of the parameter version and the actual value that is stored in the version. To view just the version metadata such as the `name`, `createTime`, and `updateTime`, you can use `view=BASIC` in your request. See the following example:

### REST

Before using any of the request data, make the following replacements: 

  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the parameter
  * PROJECT_ID: the Google Cloud project ID
  * PARAMETER_ID: the name of the parameter
  * PARAMETER_VERSION_ID: the ID of the parameter version



HTTP method and URL: 
    
    
    GET https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID/versions/PARAMETER_VERSION_ID?view=BASIC

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
         "https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID/versions/PARAMETER_VERSION_ID?view=BASIC"

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
        -Uri "https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID/versions/PARAMETER_VERSION_ID?view=BASIC" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/production-1/locations/us-central1/parameters/app_config/versions/configv2",
      "createTime": "2024-10-30T05:38:58.682341106Z",
      "updateTime": "2024-10-30T05:38:58.919983684Z"
    }
    
    

## What's next

  * [Disable a parameter version](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/disable-parameter-versions)
  * [Enable a disabled parameter version](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/enable-disabled-versions)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
