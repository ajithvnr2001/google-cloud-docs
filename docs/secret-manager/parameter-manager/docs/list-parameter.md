---
url: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/list-parameter/
title: List parameters and view parameter details \u00a0|\u00a0 Parameter Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:57:40.164290+00:00
---

# List parameters and view parameter details  |  Parameter Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/list-parameter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Parameter Manager ](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/overview)



Send feedback 

#  List parameters and view parameter details Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to retrieve a list of all parameters within a project and view metadata associated with each parameter.

A parameter acts as a container for its versions. While the parameter stores metadata like name and format, the individual parameter versions hold the actual data payload.

## Required roles

To get the permissions that you need to list parameters, ask your administrator to grant you the [Parameter Manager Parameter Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.parameterViewer) (`roles/parametermanager.parameterViewer`) IAM role on the project, folder, or organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## List all parameters

To list all parameters in a project, folder, or organization, use one of the following methods:

**Global parameters**

### Console

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. Click **Parameter Manager** to go to the **Parameter Manager** page. You'll see a list of all the parameters in that project.




### gcloud

Before using any of the command data below, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters list --location=global --project=PROJECT_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters list --location=global --project=PROJECT_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters list --location=global --project=PROJECT_ID

You should receive a response similar to the following:
    
    
    projects/production-1/locations/global/parameters/allowed_ip_ranges                         UNFORMATTED  {'iamPolicyUidPrincipal': 'principal://parametermanager.googleapis.com/projects/567445493557/uid/locations/global/parameters/d81462f3-f333-49d6-8a37-18ba24ad21b3'}  2024-10-23T09:58:00.195567192Z  2024-10-23T09:58:00.521576004Z
    projects/production-1/locations/global/parameters/app_config                                FORMATTED  {'iamPolicyUidPrincipal': 'principal://parametermanager.googleapis.com/projects/567445493557/uid/locations/global/parameters/4d3737fa-ab28-47f3-8ca7-4ea4d3de6305'}  2024-10-25T13:54:53.162338414Z  2024-10-25T13:54:53.444576707Z
    

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID



HTTP method and URL: 
    
    
    GET https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/parameters

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
         "https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/parameters"

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
        -Uri "https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/parameters" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "parameters": [
        {
          "name": "projects/production-1/locations/global/parameters/app_config",
          "createTime": "2024-10-15T08:39:05.191747694Z",
          "updateTime": "2024-10-15T08:39:05.530311092Z",
          "format": "YAML",
          "policyMember": {
            "iamPolicyUidPrincipal": "principal://parametermanager.googleapis.com/projects/567445493557/uid/locations/global/parameters/c86ca5bc-f4c2-439d-b62c-d578b4b78b12"
          }
        },
        {
          "name": "projects/production-1/locations/global/parameters/allowed_ip_ranges",
          "createTime": "2024-10-15T08:31:53.250487112Z",
          "updateTime": "2024-10-15T08:31:53.576010644Z",
          "format": "UNFORMATTED",
          "policyMember": {
            "iamPolicyUidPrincipal": "principal://parametermanager.googleapis.com/projects/567445493557/uid/locations/global/parameters/c0100d79-7c8d-4da3-8eb6-fe2a35843d9b"
          }
        }
      ]
    }
    
    

### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Parameter Manager C# SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-csharp). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    using [Google.Api.Gax](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html);
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.ParameterManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.html);
    
    public class ListParametersSample
    {
        /// <summary>
        /// This function lists parameter using the Parameter Manager SDK for GCP.
        /// </summary>
        /// <param name="projectId">The ID of the project where the parameter is located.</param>
        /// <returns>A list of Parameter objects.</returns>
        public IEnumerable<Parameter> ListParameters(string projectId)
        {
            // Create the client.
            [ParameterManagerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html) client = [ParameterManagerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html#Google_Cloud_ParameterManager_V1_ParameterManagerClient_Create)();
    
            // Build the parent resource name.
            [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html) parent = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global");
    
            // Call the API to list the parameters.
            PagedEnumerable<ListParametersResponse, Parameter> response = client.[ListParameters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html#Google_Cloud_ParameterManager_V1_ParameterManagerClient_ListParameters_Google_Api_Gax_ResourceNames_LocationName_System_String_System_Nullable_System_Int32__Google_Api_Gax_Grpc_CallSettings_)(parent);
    
            // Print each parameter name.
            foreach (Parameter parameter in response)
            {
                Console.WriteLine($"Found parameter {parameter.Name} with format {parameter.Format}");
            }
    
            // Return the list of parameters.
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
    
    // listParam lists parameters using the Parameter Manager SDK for GCP.
    //
    // w: The io.Writer object used to write the output.
    // projectID: The ID of the project where the parameters are located.
    //
    // The function returns an error if the parameter listing fails.
    func listParams(w io.Writer, projectID string) error {
    	// Create a context and a Parameter Manager client.
    	ctx := context.Background()
    	client, err := parametermanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create Parameter Manager client: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_Close)()
    
    	// Construct the name of the list parameter.
    	parent := fmt.Sprintf("projects/%s/locations/global", projectID)
    	// Build the request to list parameters.
    	req := &parametermanagerpb.ListParametersRequest{
    		Parent: parent,
    	}
    
    	// Call the API to list parameters.
    	parameters := client.ListParameters(ctx, req)
    	for {
    		parameter, err := parameters.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("failed to list parameters: %w", err)
    		}
    
    		fmt.Fprintf(w, "Found parameter %s with format %s \n", parameter.Name, parameter.Format.String())
    	}
    
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Parameter Manager Java SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-java). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    import com.google.cloud.parametermanager.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.LocationName.html);
    import com.google.cloud.parametermanager.v1.[ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html);
    import com.google.cloud.parametermanager.v1.[ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html).[ListParametersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.ListParametersPagedResponse.html);
    import java.io.IOException;
    
    /** Class to demonstrate listing parameter using the parameter manager SDK for GCP. */
    public class ListParams {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
    
        // Call the method to list parameters.
        listParams(projectId);
      }
    
      // This is an example snippet for listing all parameters in given project.
      public static [ListParametersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.ListParametersPagedResponse.html) listParams(String projectId) throws IOException {
        // Initialize the client that will be used to send requests. This client only
        // needs to be created once, and can be reused for multiple requests.
        try ([ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html) client = [ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html).create()) {
          String locationId = "global";
    
          // Build the parent name from the project.
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.LocationName.html) location = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.LocationName.html).of(projectId, locationId);
    
          // Get all parameters.
          [ListParametersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.ListParametersPagedResponse.html) response = client.listParameters(location.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.LocationName.html#com_google_cloud_parametermanager_v1_LocationName_toString__)());
    
          // List all parameters.
          response
              .iterateAll()
              .forEach(parameter ->
                      System.out.printf("Found parameter %s with format %s\n",
                              parameter.getName(), parameter.getFormat()));
    
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
    
    // Imports the Parameter Manager library
    const {ParameterManagerClient} = require('[@google-cloud/parametermanager](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)');
    
    // Instantiates a client
    const client = new [ParameterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)();
    
    async function listParams() {
      // Construct the parent string for listing parameters globally
      const parent = client.[locationPath](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/parametermanager/v1.parametermanagerclient.html)(projectId, 'global');
    
      const request = {
        parent: parent,
      };
    
      // Use listParametersAsync to handle pagination automatically
      const parameters = await client.[listParametersAsync](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/parametermanager/v1.parametermanagerclient.html)(request);
    
      for await (const parameter of parameters) {
        console.log(
          `Found parameter ${parameter.name} with format ${parameter.format}`
        );
      }
      return parameters;
    }
    
    return await listParams();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Parameter Manager PHP SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-php). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    // Import necessary classes for list a parameters.
    use Google\Cloud\ParameterManager\V1\Client\ParameterManagerClient;
    use Google\Cloud\ParameterManager\V1\ListParametersRequest;
    use Google\Cloud\ParameterManager\V1\ParameterFormat;
    
    /**
     * Lists a parameters using the Parameter Manager SDK for GCP.
     *
     * @param string $projectId The Google Cloud Project ID (e.g. 'my-project')
     */
    function list_params(string $projectId): void
    {
        // Create a client for the Parameter Manager service.
        $client = new ParameterManagerClient();
    
        // Build the resource name of the parameter.
        $parent = $client->locationName($projectId, 'global');
    
        // Prepare the request to list the parameters.
        $request = (new ListParametersRequest())
            ->setParent($parent);
    
        // Retrieve the parameter using the client.
        foreach ($client->listParameters($request) as $parameter) {
            printf('Found parameter %s with format %s' . PHP_EOL, $parameter->getName(), ParameterFormat::name($parameter->getFormat()));
        }
    }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Parameter Manager Python SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-python). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    def list_params(project_id: str) -> None:
        """
        Lists all parameters in the global location for the specified
        project using the Google Cloud Parameter Manager SDK.
    
        Args:
            project_id (str): The ID of the project
            where the parameters are located.
    
        Returns:
            None
    
        Example:
            list_params(
                "my-project"
            )
        """
        # Import the necessary library for Google Cloud Parameter Manager.
        from google.cloud import [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest)
    
        # Create the Parameter Manager client.
        client = [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[ParameterManagerClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html)()
    
        # Build the resource name of the parent project in the global location.
        parent = client.[common_location_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_common_location_path)(project_id, "global")
    
        # List all parameters in the specified parent project.
        for parameter in client.[list_parameters](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_list_parameters)(parent=parent):
            print(f"Found parameter {parameter.name} with format {parameter.format_.name}")
    

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Parameter Manager Ruby SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-ruby). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    require "google/cloud/parameter_manager"
    
    ##
    # List a parameters
    #
    # @param project_id [String] The Google Cloud project (e.g. "my-project")
    #
    def list_params project_id:
      # Create a Parameter Manager client.
      client = Google::Cloud::[ParameterManager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager.html).[parameter_manager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager/latest/Google-Cloud-ParameterManager.html)
    
      # Build the resource name of the parent project.
      parent = client.[location_path](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager-V1-ParameterManager-Paths.html) project: project_id, location: "global"
    
      # List the parameters.
      param_list = client.list_parameters parent: parent
    
      # Print out all parameters.
      param_list.each do |param|
        puts "Found parameter #{param.name} with format #{param.format}"
      end
    end

**Regional parameters**

### Console

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. Click **Parameter Manager** to go to the **Parameter Manager** page. You'll see a list of all the parameters in that project.




### gcloud

Before using any of the command data below, make the following replacements: 

  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the parameter
  * PROJECT_ID: the Google Cloud project ID



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters list --location=LOCATION --project=PROJECT_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters list --location=LOCATION --project=PROJECT_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters list --location=LOCATION --project=PROJECT_ID

You should receive a response similar to the following:
    
    
    projects/production-1/locations/us-central1/parameters/allowed_ip_ranges                        UNFORMATTED  {'iamPolicyUidPrincipal': 'principal://parametermanager.googleapis.com/projects/567445493557/uid/locations/us-central1/parameters/d81462f3-f333-49d6-8a37-18ba24ad21b3'}  2024-10-23T09:58:00.195567192Z  2024-10-23T09:58:00.521576004Z
    projects/production-1/locations/us-central1/parameters/app_config                                FORMATTED  {'iamPolicyUidPrincipal': 'principal://parametermanager.googleapis.com/projects/567445493557/uid/locations/us-central1/parameters/4d3737fa-ab28-47f3-8ca7-4ea4d3de6305'}  2024-10-25T13:54:53.162338414Z  2024-10-25T13:54:53.444576707Z
    

### REST

Before using any of the request data, make the following replacements: 

  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the parameters
  * PROJECT_ID: the Google Cloud project ID



HTTP method and URL: 
    
    
    GET https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/parameters

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
         "https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/parameters"

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
        -Uri "https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/parameters" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "parameters": [
        {
          "name": "projects/production-1/locations/us-central1/parameters/app_config",
          "createTime": "2024-10-30T05:27:28.934719122Z",
          "updateTime": "2024-10-30T05:27:29.010260475Z",
          "format": "YAML",
          "policyMember": {
            "iamPolicyUidPrincipal": "principal://parametermanager.googleapis.com/projects/463050620945/uid/locations/us-central1/parameters/6ffe4045-0778-490a-a786-d77b124e2613"
          }
        },
        {
          "name": "projects/production-1/locations/us-central1/parameters/allowed_ip_ranges",
          "createTime": "2024-10-29T06:18:23.070009070Z",
          "updateTime": "2024-10-29T06:18:23.123580038Z",
          "format": "UNFORMATTED",
          "policyMember": {
            "iamPolicyUidPrincipal": "principal://parametermanager.googleapis.com/projects/463050620945/uid/locations/us-central1/parameters/a7d81e39-3f53-4794-b3c6-484800a18c32"
          }
        }
      ]
    }
    
    

### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Parameter Manager C# SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-csharp). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    using [Google.Api.Gax](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html);
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.ParameterManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.html);
    
    public class ListRegionalParametersSample
    {
        /// <summary>
        /// This function lists all regional parameters using the Parameter Manager SDK for GCP.
        /// </summary>
        /// <param name="projectId">The ID of the project where the parameter is located.</param>
        /// <param name="locationId">The ID of the region where the parameter is located.</param>
        /// <returns>A list of Parameter objects.</returns>
        public IEnumerable<Parameter> ListRegionalParameters(
            string projectId,
            string locationId)
        {
            // Define the regional endpoint
            string regionalEndpoint = $"parametermanager.{locationId}.rep.googleapis.com";
    
            // Create the client with the regional endpoint
            [ParameterManagerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html) client = new [ParameterManagerClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClientBuilder.html)
            {
                Endpoint = regionalEndpoint
            }.[Build](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClientBuilder.html#Google_Cloud_ParameterManager_V1_ParameterManagerClientBuilder_Build)();
    
            // Build the parent resource name for the regional locationId
            [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html) parent = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, locationId);
    
            // Call the API to list the parameters
            PagedEnumerable<ListParametersResponse, Parameter> response = client.[ListParameters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html#Google_Cloud_ParameterManager_V1_ParameterManagerClient_ListParameters_Google_Api_Gax_ResourceNames_LocationName_System_String_System_Nullable_System_Int32__Google_Api_Gax_Grpc_CallSettings_)(parent);
    
            // Print each parameter name
            foreach (Parameter parameter in response)
            {
                Console.WriteLine($"Found regional parameter {parameter.Name} with format {parameter.Format}");
            }
    
            // Return the list of parameters
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
    
    // listRegionalParam lists all parameters regional using the Parameter Manager SDK for GCP.
    //
    // projectID: The ID of the project where the parameter is located.
    // locationID: The ID of the region where the parameter is located.
    // parameterID: The ID of the parameter to be listed.
    //
    // The function returns an error if the parameter listing fails
    func listRegionalParam(w io.Writer, projectID, locationID string) error {
    	// Create a new context.
    	ctx := context.Background()
    
    	// Create a Parameter Manager client.
    	endpoint := fmt.Sprintf("parametermanager.%s.rep.googleapis.com:443", locationID)
    	client, err := parametermanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_NewClient)(ctx, option.WithEndpoint(endpoint))
    	if err != nil {
    		return fmt.Errorf("failed to create Parameter Manager client: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_Close)()
    
    	// Construct the name of the parent resource to list parameters.
    	parent := fmt.Sprintf("projects/%s/locations/%s", projectID, locationID)
    
    	// Build the request to list all parameters.
    	req := &parametermanagerpb.ListParametersRequest{
    		Parent: parent,
    	}
    
    	// Call the API to list all parameters.
    	parameters := client.ListParameters(ctx, req)
    	for {
    		parameter, err := parameters.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("failed to list parameters: %w", err)
    		}
    
    		fmt.Fprintf(w, "Found regional parameter %s with format %s\n", parameter.Name, parameter.Format.String())
    	}
    
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Parameter Manager Java SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-java). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    import com.google.cloud.parametermanager.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.LocationName.html);
    import com.google.cloud.parametermanager.v1.[ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html);
    import com.google.cloud.parametermanager.v1.[ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html).[ListParametersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.ListParametersPagedResponse.html);
    import com.google.cloud.parametermanager.v1.[ParameterManagerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerSettings.html);
    import java.io.IOException;
    
    /**
     * Class to demonstrate listing parameters for a specified region using the Parameter Manager SDK
     * for GCP.
     */
    public class ListRegionalParams {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "your-location-id";
    
        // Call the method to list parameters regionally.
        listRegionalParams(projectId, locationId);
      }
    
      // This is an example snippet that list all parameters in a given region.
      public static [ListParametersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.ListParametersPagedResponse.html) listRegionalParams(String projectId, String locationId)
          throws IOException {
        // Endpoint to call the regional parameter manager server
        String apiEndpoint = String.format("parametermanager.%s.rep.googleapis.com:443", locationId);
        [ParameterManagerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerSettings.html) parameterManagerSettings =
            [ParameterManagerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerSettings.html).newBuilder().setEndpoint(apiEndpoint).build();
    
        // Initialize the client that will be used to send requests. This client only
        // needs to be created once, and can be reused for multiple requests.
        try ([ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html) client = [ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html).create(parameterManagerSettings)) {
          // Build the parent name from the project.
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.LocationName.html) location = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.LocationName.html).of(projectId, locationId);
    
          // Get all parameters.
          [ListParametersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.ListParametersPagedResponse.html) response = client.listParameters(location.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.LocationName.html#com_google_cloud_parametermanager_v1_LocationName_toString__)());
    
          // List all parameters.
          response
              .iterateAll()
              .forEach(parameter ->
                      System.out.printf("Found regional parameter %s with format %s\n",
                              parameter.getName(), parameter.getFormat()));
    
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
    
    // Imports the Parameter Manager library
    const {ParameterManagerClient} = require('[@google-cloud/parametermanager](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)');
    
    // Adding the endpoint to call the regional parameter manager server
    const options = {
      apiEndpoint: `parametermanager.${locationId}.rep.googleapis.com`,
    };
    
    // Instantiates a client with regional endpoint
    const client = new [ParameterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)(options);
    
    async function listRegionalParams() {
      // Construct the parent string for listing parameters in a specific region
      const parent = client.[locationPath](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/parametermanager/v1.parametermanagerclient.html)(projectId, locationId);
    
      const request = {
        parent: parent,
      };
    
      // Use listParametersAsync to handle pagination automatically
      const parameters = await client.[listParametersAsync](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/parametermanager/v1.parametermanagerclient.html)(request);
    
      for await (const parameter of parameters) {
        console.log(
          `Found regional parameter ${parameter.name} with format ${parameter.format}`
        );
      }
      return parameters;
    }
    
    return await listRegionalParams();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Parameter Manager PHP SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-php). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    // Import necessary classes for list a parameters.
    use Google\Cloud\ParameterManager\V1\Client\ParameterManagerClient;
    use Google\Cloud\ParameterManager\V1\ListParametersRequest;
    use Google\Cloud\ParameterManager\V1\ParameterFormat;
    
    /**
     * Lists a regional parameters using the Parameter Manager SDK for GCP.
     *
     * @param string $projectId The Google Cloud Project ID (e.g. 'my-project')
     * @param string $locationId The Parameter Location (e.g. 'us-central1')
     */
    function list_regional_params(string $projectId, string $locationId): void
    {
        // Specify regional endpoint.
        $options = ['apiEndpoint' => "parametermanager.$locationId.rep.googleapis.com"];
    
        // Create a client for the Parameter Manager service.
        $client = new ParameterManagerClient($options);
    
        // Build the resource name of the parameter.
        $parent = $client->locationName($projectId, $locationId);
    
        // Prepare the request to list the parameters.
        $request = (new ListParametersRequest())
            ->setParent($parent);
    
        // Retrieve the parameter using the client.
        foreach ($client->listParameters($request) as $parameter) {
            printf('Found regional parameter %s with format %s' . PHP_EOL, $parameter->getName(), ParameterFormat::name($parameter->getFormat()));
        }
    }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Parameter Manager Python SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-python). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    def list_regional_params(project_id: str, location_id: str) -> None:
        """
        Lists all parameters in the specified region for the specified
        project using the Google Cloud Parameter Manager SDK.
    
        Args:
            project_id (str): The ID of the project where
            the parameters are located.
            location_id (str): The ID of the region where
            the parameters are located.
    
        Returns:
            None
    
        Example:
            list_regional_params(
                "my-project",
                "us-central1"
            )
        """
        # Import the necessary library for Google Cloud Parameter Manager.
        from google.cloud import [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest)
    
        # Create the Parameter Manager client with the regional endpoint.
        api_endpoint = f"parametermanager.{location_id}.rep.googleapis.com"
        client = [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[ParameterManagerClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html)(
            client_options={"api_endpoint": api_endpoint}
        )
    
        # Build the resource name of the parent project in the specified region.
        parent = client.[common_location_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_common_location_path)(project_id, location_id)
    
        # List all parameters in the specified parent project and region.
        for parameter in client.[list_parameters](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_list_parameters)(parent=parent):
            print(f"Found regional parameter {parameter.name} with format {parameter.format_.name}")
    

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Parameter Manager Ruby SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-ruby). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    require "google/cloud/parameter_manager"
    
    ##
    # List a regional parameters
    #
    # @param project_id [String] The Google Cloud project (e.g. "my-project")
    # @param location_id [String] The location name (e.g. "us-central1")
    #
    def list_regional_params project_id:, location_id:
      # Endpoint for the regional parameter manager service.
      api_endpoint = "parametermanager.#{location_id}.rep.googleapis.com"
    
      # Create the Parameter Manager client.
      client = Google::Cloud::[ParameterManager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager.html).[parameter_manager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager/latest/Google-Cloud-ParameterManager.html) do |config|
        config.endpoint = api_endpoint
      end
    
      # Build the resource name of the parent project.
      parent = client.[location_path](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager-V1-ParameterManager-Paths.html) project: project_id, location: location_id
    
      # List the parameters.
      param_list = client.list_parameters parent: parent
    
      # Print out all parameters.
      param_list.each do |param|
        puts "Found regional parameter #{param.name} with format #{param.format}"
      end
    end

## View parameter details

To view the details of a specific parameter, use one of the following methods:

**Global parameters**

### Console

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. Click **Parameter Manager** to go to the **Parameter Manager** page. You'll see the list of parameters for that project.

  3. Click the name of the parameter to view its details.

  4. On the parameter details page, click the **Overview** tab. This tab displays the general details and metadata associated with the parameter.




### gcloud

Before using any of the command data below, make the following replacements: 

  * PARAMETER_ID: the name of the parameter



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters describe PARAMETER_ID --location=global

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters describe PARAMETER_ID --location=global

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters describe PARAMETER_ID --location=global

You should receive a response similar to the following:
    
    
    createTime: '2024-11-14T06:07:35.529019883Z'
    format: UNFORMATTED
    name: projects/production-1/locations/global/parameters/app_config
    policyMember:
      iamPolicyUidPrincipal: principal://parametermanager.googleapis.com/projects/567445493557/uid/locations/global/parameters/307fa2aa-c769-496f-9362-f908d14bac71
    updateTime: '2024-11-14T06:07:35.992040677Z'
    

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID
  * PARAMETER_ID: the name of the parameter



HTTP method and URL: 
    
    
    GET https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/parameters/PARAMETER_ID

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
         "https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/parameters/PARAMETER_ID"

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
        -Uri "https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/parameters/PARAMETER_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/production-1/locations/global/parameters/app_config",
      "createTime": "2024-10-15T08:39:05.191747694Z",
      "updateTime": "2024-10-15T08:39:05.530311092Z",
      "format": "YAML",
      "policyMember": {
        "iamPolicyUidPrincipal": "principal://parametermanager.googleapis.com/projects/567445493557/uid/locations/global/parameters/c86ca5bc-f4c2-439d-b62c-d578b4b78b12"
      }
    }
    
    

### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Parameter Manager C# SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-csharp). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    using [Google.Cloud.ParameterManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.html);
    
    public class GetParameterSample
    {
        /// <summary>
        /// This function retrieves a parameter using the Parameter Manager SDK for GCP.
        /// </summary>
        /// <param name="projectId">The ID of the project where the parameter is located.</param>
        /// <param name="parameterId">The ID of the parameter to be retrieved.</param>
        /// <returns>The retrieved Parameter object.</returns>
        public Parameter GetParameter(
            string projectId,
            string parameterId)
        {
            // Create the client.
            [ParameterManagerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html) client = [ParameterManagerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html#Google_Cloud_ParameterManager_V1_ParameterManagerClient_Create)();
    
            // Build the resource name for the parameter.
            [ParameterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterName.html) parameterName = new [ParameterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterName.html)(projectId, "global", parameterId);
    
            // Call the API to get the parameter.
            Parameter parameter = client.[GetParameter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html#Google_Cloud_ParameterManager_V1_ParameterManagerClient_GetParameter_Google_Cloud_ParameterManager_V1_GetParameterRequest_Google_Api_Gax_Grpc_CallSettings_)(parameterName);
    
            // Print the retrieved parameter name.
            Console.WriteLine($"Found the parameter {parameter.[Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.Parameter.html#Google_Cloud_ParameterManager_V1_Parameter_Name)} with format {parameter.[Format](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.Parameter.html#Google_Cloud_ParameterManager_V1_Parameter_Format)}");
    
            // Return the retrieved parameter.
            return parameter;
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
    
    // getParam get parameter using the Parameter Manager SDK for GCP.
    //
    // w: The io.Writer object used to write the output.
    // projectID: The ID of the project where the parameter is located.
    // parameterID: The ID of the parameter to retrieved.
    //
    // The function returns an error if the parameter retrieval fails.
    func getParam(w io.Writer, projectID, parameterID string) error {
    	// Create a context and a Parameter Manager client.
    	ctx := context.Background()
    	client, err := parametermanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create Parameter Manager client: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_Close)()
    
    	// Construct the name of the parameter to get parameter.
    	name := fmt.Sprintf("projects/%s/locations/global/parameters/%s", projectID, parameterID)
    
    	// Build the request to get parameter.
    	req := &parametermanagerpb.GetParameterRequest{
    		Name: name,
    	}
    
    	// Call the API to get parameter.
    	param, err := client.GetParameter(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to get parameter: %w", err)
    	}
    
    	// Find more details for the Parameter object here:
    	// https://cloud.google.com/secret-manager/parameter-manager/docs/reference/rest/v1/projects.locations.parameters#Parameter
    	fmt.Fprintf(w, "Found parameter %s with format %s\n", param.Name, param.Format.String())
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Parameter Manager Java SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-java). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    import com.google.cloud.parametermanager.v1.[Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html);
    import com.google.cloud.parametermanager.v1.[ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html);
    import com.google.cloud.parametermanager.v1.[ParameterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterName.html);
    import java.io.IOException;
    
    /** This class demonstrates how to get a parameter using the Parameter Manager SDK for GCP. */
    public class GetParam {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String parameterId = "your-parameter-id";
    
        // Call the method to get a parameter.
        getParam(projectId, parameterId);
      }
    
      // This is an example snippet for getting a parameter.
      public static [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html) getParam(String projectId, String parameterId) throws IOException {
        // Initialize the client that will be used to send requests. This client only
        // needs to be created once, and can be reused for multiple requests.
        try ([ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html) client = [ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html).create()) {
          String locationId = "global";
    
          // Build the parameter name.
          [ParameterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterName.html) parameterName = [ParameterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterName.html).of(projectId, locationId, parameterId);
    
          // Get the parameter.
          [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html) parameter = client.getParameter(parameterName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterName.html#com_google_cloud_parametermanager_v1_ParameterName_toString__)());
          // Find more details for the Parameter object here:
          // https://cloud.google.com/secret-manager/parameter-manager/docs/reference/rest/v1/projects.locations.parameters#Parameter
          System.out.printf(
              "Found the parameter %s with format: %s\n", parameter.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html#com_google_cloud_parametermanager_v1_Parameter_getName__)(), parameter.[getFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html#com_google_cloud_parametermanager_v1_Parameter_getFormat__)());
    
          return parameter;
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
    
    async function getParam() {
      // Construct the fully qualified parameter name
      const name = client.[parameterPath](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/parametermanager/v1.parametermanagerclient.html)(projectId, 'global', parameterId);
    
      // Get the parameter
      const [parameter] = await client.getParameter({
        name: name,
      });
    
      // Find more details for the Parameter object here:
      // https://cloud.google.com/secret-manager/parameter-manager/docs/reference/rest/v1/projects.locations.parameters#Parameter
      console.log(
        `Found parameter ${parameter.name} with format ${parameter.format}`
      );
      return parameter;
    }
    
    return await getParam();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Parameter Manager PHP SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-php). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    // Import necessary classes for retrieve a parameter version.
    use Google\Cloud\ParameterManager\V1\Client\ParameterManagerClient;
    use Google\Cloud\ParameterManager\V1\GetParameterRequest;
    use Google\Cloud\ParameterManager\V1\ParameterFormat;
    
    /**
     * Retrieves a parameter using the Parameter Manager SDK for GCP.
     *
     * @param string $projectId The Google Cloud Project ID (e.g. 'my-project')
     * @param string $parameterId The Parameter ID (e.g. 'my-param')
     */
    function get_param(string $projectId, string $parameterId): void
    {
        // Create a client for the Parameter Manager service.
        $client = new ParameterManagerClient();
    
        // Build the resource name of the parameter.
        $parameterName = $client->parameterName($projectId, 'global', $parameterId);
    
        // Prepare the request to get the parameter.
        $request = (new GetParameterRequest())
            ->setName($parameterName);
    
        // Retrieve the parameter using the client.
        $parameter = $client->getParameter($request);
    
        // Print the retrieved parameter details.
        printf('Found parameter %s with format %s' . PHP_EOL, $parameter->getName(), ParameterFormat::name($parameter->getFormat()));
    }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Parameter Manager Python SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-python). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    def get_param(project_id: str, parameter_id: str) -> parametermanager_v1.Parameter:
        """
        Retrieves a parameter from the global location of the specified
        project using the Google Cloud Parameter Manager SDK.
    
        Args:
            project_id (str): The ID of the project where the parameter is located.
            parameter_id (str): The ID of the parameter to retrieve.
    
        Returns:
            parametermanager_v1.Parameter: An object representing the parameter.
    
        Example:
            get_param(
                "my-project",
                "my-global-parameter"
            )
        """
        # Import the necessary library for Google Cloud Parameter Manager.
        from google.cloud import parametermanager_v1
    
        # Create the Parameter Manager client.
        client = parametermanager_v1.ParameterManagerClient()
    
        # Build the resource name of the parameter.
        name = client.parameter_path(project_id, "global", parameter_id)
    
        # Retrieve the parameter.
        parameter = client.get_parameter(name=name)
    
        # Show parameter details.
        # Find more details for the Parameter object here:
        # https://cloud.google.com/secret-manager/parameter-manager/docs/reference/rest/v1/projects.locations.parameters#Parameter
        print(f"Found the parameter {parameter.name} with format {parameter.format_.name}")

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Parameter Manager Ruby SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-ruby). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    require "google/cloud/parameter_manager"
    
    ##
    # Retrieve a parameter
    #
    # @param project_id [String] The Google Cloud project (e.g. "my-project")
    # @param parameter_id [String] The parameter name (e.g. "my-parameter")
    #
    def get_param project_id:, parameter_id:
      # Create a Parameter Manager client.
      client = Google::Cloud::[ParameterManager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager.html).[parameter_manager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager/latest/Google-Cloud-ParameterManager.html)
    
      # Build the resource name of the parent project.
      name = client.[parameter_path](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager-V1-ParameterManager-Paths.html) project: project_id, location: "global", parameter: parameter_id
    
      # Retrieve the parameter.
      param = client.get_parameter name: name
    
      # Print the retrieved parameter name.
      puts "Found parameter #{param.name} with format #{param.format}"
    end

**Regional parameters**

### Console

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. Click **Parameter Manager** to go to the **Parameter Manager** page. You'll see the list of parameters for that project.

  3. Click the name of the parameter to view its details.

  4. On the parameter details page, click the **Overview** tab. This tab displays the general details and metadata associated with the parameter.




### gcloud

Before using any of the command data below, make the following replacements: 

  * PARAMETER_ID: the name of the parameter
  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the parameter



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters describe PARAMETER_ID --location=LOCATION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters describe PARAMETER_ID --location=LOCATION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters describe PARAMETER_ID --location=LOCATION

You should receive a response similar to the following:
    
    
    createTime: '2024-11-14T06:07:35.529019883Z'
    format: UNFORMATTED
    name: projects/production-1/locations/us-central1/parameters/app_config
    policyMember:
      iamPolicyUidPrincipal: principal://parametermanager.googleapis.com/projects/567445493557/uid/locations/us-central1/parameters/307fa2aa-c769-496f-9362-f908d14bac71
    updateTime: '2024-11-14T06:07:35.992040677Z'
    

### REST

Before using any of the request data, make the following replacements: 

  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the parameter
  * PROJECT_ID: the Google Cloud project ID
  * PARAMETER_ID: the name of the parameter



HTTP method and URL: 
    
    
    GET https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID

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
         "https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID"

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
        -Uri "https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/production-1/locations/us-central1/parameters/app_config",
      "createTime": "2024-10-15T08:39:05.191747694Z",
      "updateTime": "2024-10-15T08:39:05.530311092Z",
      "format": "YAML",
      "policyMember": {
        "iamPolicyUidPrincipal": "principal://parametermanager.googleapis.com/projects/567445493557/uid/locations/global/parameters/c86ca5bc-f4c2-439d-b62c-d578b4b78b12"
      }
    }
    
    

### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Parameter Manager C# SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-csharp). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    using [Google.Cloud.ParameterManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.html);
    
    public class GetRegionalParameterSample
    {
        /// <summary>
        /// This function retrieves a regional parameter using the Parameter Manager SDK for GCP.
        /// </summary>
        /// <param name="projectId">The ID of the project where the parameter is located.</param>
        /// <param name="locationId">The ID of the region where the parameter is located.</param>
        /// <param name="parameterId">The ID of the parameter to be retrieved.</param>
        /// <returns>The retrieved Parameter object.</returns>
        public Parameter GetRegionalParameter(
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
    
            // Build the resource name for the parameter in the specified regional locationId
            [ParameterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterName.html) parameterName = new [ParameterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterName.html)(projectId, locationId, parameterId);
    
            // Call the API to get the parameter
            Parameter parameter = client.[GetParameter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html#Google_Cloud_ParameterManager_V1_ParameterManagerClient_GetParameter_Google_Cloud_ParameterManager_V1_GetParameterRequest_Google_Api_Gax_Grpc_CallSettings_)(parameterName);
    
            // Print the retrieved parameter name
            Console.WriteLine($"Found the regional parameter {parameter.[Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.Parameter.html#Google_Cloud_ParameterManager_V1_Parameter_Name)} with format {parameter.[Format](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.Parameter.html#Google_Cloud_ParameterManager_V1_Parameter_Format)}");
    
            // Return the retrieved parameter
            return parameter;
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
    
    // getRegionalParam gets a parameter regional using the Parameter Manager SDK for GCP.
    //
    // w: The io.Writer object used to write the output.
    // projectID: The ID of the project where the parameter is located.
    // locationID: The ID of the region where the parameter is located.
    // parameterID: The ID of the parameter to be retrieved.
    //
    // The function returns an error if the parameter retrieval fails.
    func getRegionalParam(w io.Writer, projectID, locationID, parameterID string) error {
    	// Create a new context.
    	ctx := context.Background()
    
    	// Create a Parameter Manager client.
    	endpoint := fmt.Sprintf("parametermanager.%s.rep.googleapis.com:443", locationID)
    	client, err := parametermanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_NewClient)(ctx, option.WithEndpoint(endpoint))
    	if err != nil {
    		return fmt.Errorf("failed to create Parameter Manager client: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_Close)()
    
    	// Construct the name of the parameter to retrieve.
    	name := fmt.Sprintf("projects/%s/locations/%s/parameters/%s", projectID, locationID, parameterID)
    
    	// Build the request to get the parameter.
    	req := &parametermanagerpb.GetParameterRequest{
    		Name: name,
    	}
    
    	// Call the API to get the parameter.
    	param, err := client.GetParameter(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to get parameter: %w", err)
    	}
    
    	// Find more details for the Parameter object here:
    	// https://cloud.google.com/secret-manager/parameter-manager/docs/reference/rest/v1/projects.locations.parameters#Parameter
    	fmt.Fprintf(w, "Found regional parameter %s with format %s\n", param.Name, param.Format.String())
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Parameter Manager Java SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-java). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    import com.google.cloud.parametermanager.v1.[Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html);
    import com.google.cloud.parametermanager.v1.[ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html);
    import com.google.cloud.parametermanager.v1.[ParameterManagerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerSettings.html);
    import com.google.cloud.parametermanager.v1.[ParameterName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterName.html);
    import java.io.IOException;
    
    /**
     * This class demonstrates how to get a regional parameter using the Parameter Manager SDK for GCP.
     */
    public class GetRegionalParam {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "your-location-id";
        String parameterId = "your-parameter-id";
    
        // Call the method to get a regional parameter.
        getRegionalParam(projectId, locationId, parameterId);
      }
    
      // This is an example snippet that gets a regional parameter.
      public static [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html) getRegionalParam(String projectId, String locationId, String parameterId)
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
    
          // Get the parameter.
          [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html) parameter = client.getParameter(parameterName.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterName.html#com_google_cloud_parametermanager_v1_ParameterName_toString__)());
          // Find more details for the Parameter object here:
          // https://cloud.google.com/secret-manager/parameter-manager/docs/reference/rest/v1/projects.locations.parameters#Parameter
          System.out.printf(
              "Found the regional parameter %s with format %s\n",
              parameter.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html#com_google_cloud_parametermanager_v1_Parameter_getName__)(), parameter.[getFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html#com_google_cloud_parametermanager_v1_Parameter_getFormat__)());
    
          return parameter;
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
    
    async function getRegionalParam() {
      // Construct the fully qualified parameter name
      const name = client.[parameterPath](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/parametermanager/v1.parametermanagerclient.html)(projectId, locationId, parameterId);
    
      // Get the parameter
      const [parameter] = await client.getParameter({
        name: name,
      });
    
      // Find more details for the Parameter object here:
      // https://cloud.google.com/secret-manager/parameter-manager/docs/reference/rest/v1/projects.locations.parameters#Parameter
      console.log(
        `Found regional parameter ${parameter.name} with format ${parameter.format}`
      );
      return parameter;
    }
    
    return await getRegionalParam();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Parameter Manager PHP SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-php). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    // Import necessary classes for retrieve a parameter version.
    use Google\Cloud\ParameterManager\V1\Client\ParameterManagerClient;
    use Google\Cloud\ParameterManager\V1\GetParameterRequest;
    use Google\Cloud\ParameterManager\V1\ParameterFormat;
    
    /**
     * Retrieves a regional parameter using the Parameter Manager SDK for GCP.
     *
     * @param string $projectId The Google Cloud Project ID (e.g. 'my-project')
     * @param string $locationId The Parameter Location (e.g. 'us-central1')
     * @param string $parameterId The Parameter ID (e.g. 'my-param')
     */
    function get_regional_param(string $projectId, string $locationId, string $parameterId): void
    {
        // Specify regional endpoint.
        $options = ['apiEndpoint' => "parametermanager.$locationId.rep.googleapis.com"];
    
        // Create a client for the Parameter Manager service.
        $client = new ParameterManagerClient($options);
    
        // Build the resource name of the parameter.
        $parameterName = $client->parameterName($projectId, $locationId, $parameterId);
    
        // Prepare the request to get the parameter.
        $request = (new GetParameterRequest())
            ->setName($parameterName);
    
        // Retrieve the parameter using the client.
        $parameter = $client->getParameter($request);
    
        // Print the retrieved parameter details.
        printf('Found regional parameter %s with format %s' . PHP_EOL, $parameter->getName(), ParameterFormat::name($parameter->getFormat()));
    }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Parameter Manager Python SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-python). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    def get_regional_param(
        project_id: str, location_id: str, parameter_id: str
    ) -> parametermanager_v1.Parameter:
        """
        Retrieves a parameter from the specified region of the specified
        project using the Google Cloud Parameter Manager SDK.
    
        Args:
            project_id (str): The ID of the project where the parameter is located.
            location_id (str): The ID of the region where the parameter is located.
            parameter_id (str): The ID of the parameter to retrieve.
    
        Returns:
            parametermanager_v1.Parameter: An object representing the parameter.
    
        Example:
            get_regional_param(
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
        name = client.[parameter_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_parameter_path)(project_id, location_id, parameter_id)
    
        # Retrieve the parameter.
        parameter = client.[get_parameter](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_get_parameter)(name=name)
    
        # Show parameter details.
        # Find more details for the Parameter object here:
        # https://cloud.google.com/secret-manager/parameter-manager/docs/reference/rest/v1/projects.locations.parameters#Parameter
        print(f"Found the regional parameter {parameter.name} with format {parameter.format_.name}")

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Parameter Manager Ruby SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-ruby). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    require "google/cloud/parameter_manager"
    
    ##
    # Retrieve a regional parameter
    #
    # @param project_id [String] The Google Cloud project (e.g. "my-project")
    # @param location_id [String] The location name (e.g. "us-central1")
    # @param parameter_id [String] The parameter name (e.g. "my-parameter")
    #
    def get_regional_param project_id:, location_id:, parameter_id:
      # Endpoint for the regional parameter manager service.
      api_endpoint = "parametermanager.#{location_id}.rep.googleapis.com"
    
      # Create the Parameter Manager client.
      client = Google::Cloud::[ParameterManager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager.html).[parameter_manager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager/latest/Google-Cloud-ParameterManager.html) do |config|
        config.endpoint = api_endpoint
      end
    
      # Build the resource name of the parent project.
      name = client.[parameter_path](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager-V1-ParameterManager-Paths.html) project: project_id, location: location_id, parameter: parameter_id
    
      # Retrieve the parameter.
      param = client.get_parameter name: name
    
      # Print the retrieved parameter name.
      puts "Found regional parameter #{param.name} with format #{param.format}"
    end

The response is the parameter object, which contains the metadata of the parameter.

## What's next

  * [Edit a parameter](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/edit-parameter)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
