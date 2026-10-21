---
url: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/create-parameter/
title: Create a parameter \u00a0|\u00a0 Parameter Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:09:39.923446+00:00
---

# Create a parameter  |  Parameter Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/create-parameter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Parameter Manager ](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/overview)



Send feedback 

#  Create a parameter Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a parameter. A parameter acts as a dynamic variable for your application, holding key configuration values like database connection strings, feature flags, or service endpoints.

Parameters can store various types of data, including:

  * Structured data like YAML or JSON for organized, machine-readable information.
  * Unstructured data such as plain text or binary content.



You can create both _global_ and _regional_ parameters in Parameter Manager.

The following table explains the key differences between the global and regional parameters.

Feature | Global parameters | Regional parameters  
---|---|---  
Storage | Stored centrally | Stored within a specific location  
Access | Standard API endpoint | Regional endpoint corresponding to the location of the parameter  
Use cases |  Parameters that apply to your application or service regardless of where the application or service is running:

  * Default language settings
  * API keys

|  Parameters that vary based on the location where your application is deployed:

  * Database connection strings for a regional database instance
  * Feature flags that are enabled or disabled for specific locations

  
  
## Before you begin

  1. [Prepare your environment for Parameter Manager](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/prepare-environment).

  2. If you haven't already, then set up authentication. [Authentication](https://docs.cloud.google.com/docs/authentication) is the process by which your identity is verified for access to Google Cloud services and APIs.

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




### Required roles

To get the permissions that you need to create a parameter, ask your administrator to grant you the [Parameter Manager Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.admin) (`roles/parametermanager.admin`) IAM role on the project, folder, or organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a parameter to store structured data

To create a parameter for storing structured data, use one of the following methods:

**Global parameters**

### Console

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. Click **Parameter Manager** to go to the **Parameter Manager** page, and then click **Create parameter**.

  3. In the **Create parameter** page, enter the parameter name.

  4. To specify the format in which the parameter stores data, select either **YAML** or **JSON** in the **Parameter format** section.

  5. To create a global parameter, select **Multi-region** in the **Location** section, and then select **global (Global)** from the **Region** list.

  6. Optional: To add a label to your parameter resource, click **Add label** , and then define the label key and value.

  7. Click **Create**.




### gcloud

Before using any of the command data below, make the following replacements: 

  * PARAMETER_ID: the name of the new parameter. Parameter names must be 63 characters or less and consist only of English letters (A-Z, a-z), numbers (0-9), dashes (-), and underscores (_). Names can't begin with a dash.
  * FORMAT: the data type or format of the parameter's value, such as `YAML` or `JSON`.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters create PARAMETER_ID --location=global --parameter-format=FORMAT

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters create PARAMETER_ID --location=global --parameter-format=FORMAT

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters create PARAMETER_ID --location=global --parameter-format=FORMAT

You should receive a response similar to the following:
    
    
    Created parameter [app_config].

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID.
  * PARAMETER_ID: the name of the new parameter. Parameter names must be 63 characters or less and consist only of English letters (A-Z, a-z), numbers (0-9), dashes (-), and underscores (_). Names can't begin with a dash.



HTTP method and URL: 
    
    
    POST https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/parameters?parameter_id=PARAMETER_ID

Request JSON body: 
    
    
    {"format": "YAML"}
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/parameters?parameter_id=PARAMETER_ID"

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
        -Uri "https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/parameters?parameter_id=PARAMETER_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/production-1/locations/global/parameters/app_config",
      "createTime": "2024-10-15T08:39:05.191747694Z",
      "updateTime": "2024-10-15T08:39:05.191747694Z",
      "format": "YAML",
      "policyMember": {
        "iamPolicyUidPrincipal": "principal://parametermanager.googleapis.com/projects/567445493557/uid/locations/global/parameters/c86ca5bc-f4c2-439d-b62c-d578b4b78b12"
      }
    }
    
    

### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Parameter Manager C# SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-csharp). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.ParameterManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.html);
    
    public class CreateStructuredParameterSample
    {
        /// <summary>
        /// This function creates a parameter of the specified format type using the Parameter Manager SDK for GCP.
        /// </summary>
        /// <param name="projectId">The ID of the project where the parameter is to be created.</param>
        /// <param name="parameterId">The ID to assign to the new parameter. This ID must be unique within the project.</param>
        /// <param name="format">The format type of the parameter (UNFORMATTED, YAML, JSON).</param>
        /// <returns>The created Parameter object.</returns>
        public Parameter CreateStructuredParameter(
            string projectId,
            string parameterId,
            [ParameterFormat](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterFormat.html) format)
        {
            // Create the client.
            [ParameterManagerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html) client = [ParameterManagerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html#Google_Cloud_ParameterManager_V1_ParameterManagerClient_Create)();
    
            // Build the parent resource name. 
            [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html) parent = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global");
    
            // Build the parameter with the specified format.
            Parameter parameter = new Parameter
            {
                Format = format
            };
    
            // Call the API to create the parameter.
            Parameter createdParameter = client.[CreateParameter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html#Google_Cloud_ParameterManager_V1_ParameterManagerClient_CreateParameter_Google_Api_Gax_ResourceNames_LocationName_Google_Cloud_ParameterManager_V1_Parameter_System_String_Google_Api_Gax_Grpc_CallSettings_)(parent, parameter, parameterId);
    
            // Print the created parameter name.
            Console.WriteLine($"Created parameter {createdParameter.[Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.Parameter.html#Google_Cloud_ParameterManager_V1_Parameter_Name)} with format {createdParameter.[Format](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.Parameter.html#Google_Cloud_ParameterManager_V1_Parameter_Format)}");
    
            // Return the created parameter.
            return createdParameter;
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
    
    // createStructuredParam creates a new parameter with the specified format in Parameter Manager.
    //
    // w: The io.Writer object used to write the output.
    // projectID: The ID of the project where the parameter is located.
    // parameterID: The ID of the parameter to be created.
    // format: The format type of the parameter (UNFORMATTED, YAML, JSON).
    //
    // The function returns an error if the parameter creation fails.
    func createStructuredParam(w io.Writer, projectID, parameterID string, format parametermanagerpb.ParameterFormat) error {
    	// Create a context and a Parameter Manager client.
    	ctx := context.Background()
    	client, err := parametermanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create Parameter Manager client: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_Close)()
    
    	// Construct the name of the create parameter.
    	parent := fmt.Sprintf("projects/%s/locations/global", projectID)
    
    	// Build the request to create a new parameter with the specified format.
    	req := &parametermanagerpb.CreateParameterRequest{
    		Parent:      parent,
    		ParameterId: parameterID,
    		Parameter: &parametermanagerpb.Parameter{
    			Format: format,
    		},
    	}
    
    	// Call the API to create the parameter.
    	parameter, err := client.CreateParameter(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to create parameter: %w", err)
    	}
    
    	fmt.Fprintf(w, "Created parameter %s with format %s\n", parameter.Name, parameter.Format.String())
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Parameter Manager Java SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-java). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    import com.google.cloud.parametermanager.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.LocationName.html);
    import com.google.cloud.parametermanager.v1.[Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html);
    import com.google.cloud.parametermanager.v1.[ParameterFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterFormat.html);
    import com.google.cloud.parametermanager.v1.[ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html);
    import java.io.IOException;
    
    /**
     * Example class to create a new parameter with a specific format using the Parameter Manager SDK
     * for GCP.
     */
    public class CreateStructuredParam {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String parameterId = "your-parameter-id";
        [ParameterFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterFormat.html) format = [ParameterFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterFormat.html).YAML;
    
        // Call the method to create a parameter with the specified format.
        createStructuredParameter(projectId, parameterId, format);
      }
    
      // This is an example snippet for creating a new parameter with a specific format.
      public static [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html) createStructuredParameter(
          String projectId, String parameterId, [ParameterFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterFormat.html) format) throws IOException {
        // Initialize the client that will be used to send requests.
        try ([ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html) client = [ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html).create()) {
          String locationId = "global";
    
          // Build the parent name from the project.
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.LocationName.html) location = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.LocationName.html).of(projectId, locationId);
    
          // Build the parameter to create with the provided format.
          [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html) parameter = [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html).newBuilder().setFormat(format).build();
    
          // Create the parameter.
          [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html) createdParameter =
              client.createParameter(location.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.LocationName.html#com_google_cloud_parametermanager_v1_LocationName_toString__)(), parameter, parameterId);
          System.out.printf(
              "Created parameter %s with format %s\n",
              createdParameter.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html#com_google_cloud_parametermanager_v1_Parameter_getName__)(), createdParameter.[getFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html#com_google_cloud_parametermanager_v1_Parameter_getFormat__)());
    
          return createdParameter;
        }
      }
    }

### Node.js

To run this code, first [set up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup) and [install the Parameter Manager Node.js SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-nodejs). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const {protos} = require('@google-cloud/parametermanager');
    // const projectId = 'YOUR_PROJECT_ID';
    // const parameterId = 'YOUR_PARAMETER_ID';
    // const formatType = protos.google.cloud.parametermanager.v1.ParameterFormat.JSON;
    
    // Imports the Parameter Manager library
    const {ParameterManagerClient} = require('[@google-cloud/parametermanager](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)');
    
    // Instantiates a client
    const client = new [ParameterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)();
    
    async function createStructuredParam() {
      const parent = client.[locationPath](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/parametermanager/v1.parametermanagerclient.html)(projectId, 'global');
      const request = {
        parent: parent,
        parameterId: parameterId,
        parameter: {
          format: formatType,
        },
      };
    
      const [parameter] = await client.createParameter(request);
      console.log(
        `Created parameter ${parameter.name} with format ${parameter.format}`
      );
      return parameter;
    }
    
    return await createStructuredParam();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Parameter Manager PHP SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-php). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    // Import necessary classes for creating a parameter.
    use Google\Cloud\ParameterManager\V1\Client\ParameterManagerClient;
    use Google\Cloud\ParameterManager\V1\CreateParameterRequest;
    use Google\Cloud\ParameterManager\V1\Parameter;
    use Google\Cloud\ParameterManager\V1\ParameterFormat;
    
    /**
     * Creates a parameter with the specified format.
     *
     * @param string $projectId The Google Cloud Project ID (e.g. 'my-project')
     * @param string $parameterId The Parameter ID (e.g. 'my-param')
     * @param string $format The format type of the parameter (UNFORMATTED, YAML, JSON)
     */
    function create_structured_param(string $projectId, string $parameterId, string $format): void
    {
        // Create a client for the Parameter Manager service.
        $client = new ParameterManagerClient();
    
        // Build the resource name of the parent object.
        $parent = $client->locationName($projectId, 'global');
    
        // Create a new Parameter object and set the format.
        $parameter = (new Parameter())
            ->setFormat(ParameterFormat::value($format));
    
        // Prepare the request with the parent, parameter ID, and the parameter object.
        $request = (new CreateParameterRequest())
            ->setParent($parent)
            ->setParameterId($parameterId)
            ->setParameter($parameter);
    
        // Call the API and handle any network failures with print statements.
        $newParameter = $client->createParameter($request);
        printf('Created parameter %s with format %s' . PHP_EOL, $newParameter->getName(), ParameterFormat::name($newParameter->getFormat()));
    }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Parameter Manager Python SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-python). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    def create_structured_param(
        project_id: str, parameter_id: str, format_type: [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[ParameterFormat](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.ParameterFormat.html)
    ) -> parametermanager_v1.Parameter:
        """
        Creates a parameter in the global location of the specified
        project with specified format using the Google Cloud Parameter Manager SDK.
    
        Args:
            project_id (str): The ID of the project where
            the parameter is to be created.
            parameter_id (str): The ID to assign to the new parameter.
            This ID must be unique within the project.
            format_type (parametermanager_v1.ParameterFormat): The format type of
            the parameter (UNFORMATTED, YAML, JSON).
    
        Returns:
            parametermanager_v1.Parameter: An object representing the
            newly created parameter.
    
        Example:
            create_structured_param(
                "my-project",
                "my-global-parameter",
                parametermanager_v1.ParameterFormat.JSON
            )
        """
        # Import the necessary library for Google Cloud Parameter Manager.
        from google.cloud import [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest)
    
        # Create the Parameter Manager client.
        client = [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[ParameterManagerClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html)()
    
        # Build the resource name of the parent project in the global location.
        parent = client.[common_location_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_common_location_path)(project_id, "global")
    
        # Define the parameter creation request with the specified format.
        request = [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[CreateParameterRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.CreateParameterRequest.html)(
            parent=parent,
            parameter_id=parameter_id,
            parameter=[parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[Parameter](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.Parameter.html)(format_=format_type),
        )
    
        # Create the parameter.
        response = client.[create_parameter](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_create_parameter)(request=request)
    
        # Print the newly created parameter name.
        print(f"Created parameter {response.name} with format {response.format_.name}")

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Parameter Manager Ruby SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-ruby). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    require "google/cloud/parameter_manager"
    
    ##
    # Create a parameter
    #
    # @param project_id [String] The Google Cloud project (e.g. "my-project")
    # @param parameter_id [String] The parameter name (e.g. "my-parameter")
    # @param format [Google::Cloud::ParameterManager::V1::ParameterFormat::]
    # The type of parameter format (UNFORMATTED, YAML, JSON)
    #
    def create_structured_param project_id:, parameter_id:, format:
      # Create a Parameter Manager client.
      client = Google::Cloud::[ParameterManager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager.html).[parameter_manager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager/latest/Google-Cloud-ParameterManager.html)
    
      # Build the resource name of the parent project.
      parent = client.[location_path](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager-V1-ParameterManager-Paths.html) project: project_id, location: "global"
    
      parameter = {
        format: format
      }
    
      # Create the parameter.
      param = client.create_parameter parent: parent, parameter_id: parameter_id, parameter: parameter
    
      # Print the new parameter name.
      puts "Created parameter #{param.name} with format #{param.format}"
    end

**Regional parameters**

### Console

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. Click **Parameter Manager** to go to the **Parameter Manager** page, and then click **Create parameter**.

  3. In the **Create parameter** page, enter the parameter name.

  4. To specify the format in which the parameter stores data, select either **YAML** or **JSON** in the **Parameter format** section.

  5. To create a regional parameter, select **Region** in the **Location** section, and then select the location from the **Region** list.

  6. Optional: To add a label to your parameter resource, click **Add label** , and then define the label key and value.

  7. Click **Create**.




### gcloud

Before using any of the command data below, make the following replacements: 

  * PARAMETER_ID: the name of the new parameter. Parameter names must be 63 characters or less and consist only of English letters (A-Z, a-z), numbers (0-9), dashes (-), and underscores (_). Names can't begin with a dash.
  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the parameter.
  * FORMAT: the data type or format of the parameter's value, such as `YAML` or `JSON`.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters create PARAMETER_ID --location=LOCATION --parameter-format=FORMAT

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters create PARAMETER_ID --location=LOCATION --parameter-format=FORMAT

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters create PARAMETER_ID --location=LOCATION --parameter-format=FORMAT

You should receive a response similar to the following:
    
    
    Created parameter [app_config].

### REST

Before using any of the request data, make the following replacements: 

  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the parameter.
  * PROJECT_ID: the Google Cloud project ID.
  * PARAMETER_ID: the name of the new parameter. Parameter names must be 63 characters or less and consist only of English letters (A-Z, a-z), numbers (0-9), dashes (-), and underscores (_). Names can't begin with a dash.



HTTP method and URL: 
    
    
    POST https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/parameters?parameter_id=PARAMETER_ID

Request JSON body: 
    
    
    {"format": "YAML"}
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/parameters?parameter_id=PARAMETER_ID"

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
        -Uri "https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/parameters?parameter_id=PARAMETER_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/production-1/locations/us-central1/parameters/app_config",
      "createTime": "2024-10-30T05:27:28.934719122Z",
      "updateTime": "2024-10-30T05:27:28.934719122Z",
      "format": "YAML",
      "policyMember": {
        "iamPolicyUidPrincipal": "principal://parametermanager.googleapis.com/projects/463050620945/uid/locations/us-central1/parameters/6ffe4045-0778-490a-a786-d77b124e2613"
      }
    }
    

### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Parameter Manager C# SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-csharp). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.ParameterManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.html);
    
    public class CreateStructuredRegionalParameterSample
    {
        /// <summary>
        /// This function creates a regional parameter of the specified format type using the Parameter Manager SDK for GCP.
        /// </summary>
        /// <param name="projectId">The ID of the project where the parameter is to be created.</param>
        /// <param name="locationId">The region where the parameter is to be created.</param>
        /// <param name="parameterId">The ID to assign to the new parameter. This ID must be unique within the project.</param>
        /// <param name="format">The format type of the parameter (UNFORMATTED, YAML, JSON).</param>
        /// <returns>The created Parameter object.</returns>
        public Parameter CreateStructuredRegionalParameter(
            string projectId,
            string locationId,
            string parameterId,
            [ParameterFormat](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterFormat.html) format)
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
    
            // Build the parameter with the specified format
            Parameter parameter = new Parameter
            {
                Format = format
            };
    
            // Call the API to create the parameter
            Parameter createdParameter = client.[CreateParameter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html#Google_Cloud_ParameterManager_V1_ParameterManagerClient_CreateParameter_Google_Api_Gax_ResourceNames_LocationName_Google_Cloud_ParameterManager_V1_Parameter_System_String_Google_Api_Gax_Grpc_CallSettings_)(parent, parameter, parameterId);
    
            // Print the created parameter name
            Console.WriteLine($"Created regional parameter {createdParameter.[Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.Parameter.html#Google_Cloud_ParameterManager_V1_Parameter_Name)} with format {createdParameter.[Format](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.Parameter.html#Google_Cloud_ParameterManager_V1_Parameter_Format)}");
    
            // Return the created parameter
            return createdParameter;
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
    
    // createStructuredRegionalParam creates a parameter regional of the format type given as a method argument using the Parameter Manager SDK for GCP.
    //
    // w: The io.Writer object used to write the output.
    // projectID: The ID of the project where the parameter is located.
    // locationID: The region where the parameter is to be created.
    // parameterID: The ID of the parameter to be created.
    // format: The format type of the parameter (UNFORMATTED, YAML, JSON).
    //
    // The function returns an error if the parameter creation fails.
    func createStructuredRegionalParam(w io.Writer, projectID, locationID, parameterID string, format parametermanagerpb.ParameterFormat) error {
    	// Create a context and a Parameter Manager client.
    	ctx := context.Background()
    
    	// Create a Parameter Manager client.
    	endpoint := fmt.Sprintf("parametermanager.%s.rep.googleapis.com:443", locationID)
    	client, err := parametermanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_NewClient)(ctx, option.WithEndpoint(endpoint))
    	if err != nil {
    		return fmt.Errorf("failed to create Parameter Manager client: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_Close)()
    
    	// Construct the name of the create parameter.
    	parent := fmt.Sprintf("projects/%s/locations/%s", projectID, locationID)
    
    	// Create a parameter with the given format.
    	req := &parametermanagerpb.CreateParameterRequest{
    		Parent:      parent,
    		ParameterId: parameterID,
    		Parameter: &parametermanagerpb.Parameter{
    			Format: format,
    		},
    	}
    	parameter, err := client.CreateParameter(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to create parameter: %w", err)
    	}
    
    	fmt.Fprintf(w, "Created regional parameter %s with format %s\n", parameter.Name, parameter.Format.String())
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Parameter Manager Java SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-java). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    import com.google.cloud.parametermanager.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.LocationName.html);
    import com.google.cloud.parametermanager.v1.[Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html);
    import com.google.cloud.parametermanager.v1.[ParameterFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterFormat.html);
    import com.google.cloud.parametermanager.v1.[ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html);
    import com.google.cloud.parametermanager.v1.[ParameterManagerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerSettings.html);
    import java.io.IOException;
    
    /**
     * Example class to create a new regional parameter with a specific format using the Parameter
     * Manager SDK for GCP.
     */
    public class CreateStructuredRegionalParam {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "your-location-id";
        String parameterId = "your-parameter-id";
        [ParameterFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterFormat.html) format = [ParameterFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterFormat.html).JSON;
    
        // Call the method to create a regional parameter with the specified format.
        createStructuredRegionalParam(projectId, locationId, parameterId, format);
      }
    
      // This is an example snippet that creates a regional parameter with a specific format.
      public static [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html) createStructuredRegionalParam(
          String projectId, String locationId, String parameterId, [ParameterFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterFormat.html) format)
          throws IOException {
    
        // Endpoint to call the regional parameter manager server
        String apiEndpoint = String.format("parametermanager.%s.rep.googleapis.com:443", locationId);
        [ParameterManagerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerSettings.html) parameterManagerSettings =
            [ParameterManagerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerSettings.html).newBuilder().setEndpoint(apiEndpoint).build();
    
        // Initialize the client that will be used to send requests. This client only needs to be
        // created once, and can be reused for multiple requests.
        try ([ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html) client = [ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html).create(parameterManagerSettings)) {
          // Build the parent name from the project.
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.LocationName.html) location = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.LocationName.html).of(projectId, locationId);
    
          // Build the regional parameter to create with the provided format.
          [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html) parameter = [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html).newBuilder().setFormat(format).build();
    
          // Create the regional parameter.
          [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html) createdParameter =
              client.createParameter(location.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.LocationName.html#com_google_cloud_parametermanager_v1_LocationName_toString__)(), parameter, parameterId);
          System.out.printf(
              "Created regional parameter %s with format %s\n",
              createdParameter.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html#com_google_cloud_parametermanager_v1_Parameter_getName__)(), createdParameter.[getFormat](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html#com_google_cloud_parametermanager_v1_Parameter_getFormat__)());
    
          return createdParameter;
        }
      }
    }

### Node.js

To run this code, first [set up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup) and [install the Parameter Manager Node.js SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-nodejs). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const {protos} = require('@google-cloud/parametermanager');
    // const projectId = 'YOUR_PROJECT_ID';
    // const locationId = 'YOUR_LOCATION_ID';
    // const parameterId = 'YOUR_PARAMETER_ID';
    // const formatType = protos.google.cloud.parametermanager.v1.ParameterFormat.JSON;
    
    // Imports the Parameter Manager library
    const {ParameterManagerClient} = require('[@google-cloud/parametermanager](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)');
    
    // Adding the endpoint to call the regional parameter manager server
    const options = {
      apiEndpoint: `parametermanager.${locationId}.rep.googleapis.com`,
    };
    
    // Instantiates a client with regional endpoint
    const client = new [ParameterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)(options);
    
    async function createStructuredRegionalParam() {
      const parent = client.[locationPath](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/parametermanager/v1.parametermanagerclient.html)(projectId, locationId);
      const request = {
        parent: parent,
        parameterId: parameterId,
        parameter: {
          format: formatType,
        },
      };
    
      const [parameter] = await client.createParameter(request);
      console.log(
        `Created regional parameter ${parameter.name} with format ${parameter.format}`
      );
      return parameter;
    }
    
    return await createStructuredRegionalParam();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Parameter Manager PHP SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-php). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    // Import necessary classes for creating a parameter.
    use Google\Cloud\ParameterManager\V1\Client\ParameterManagerClient;
    use Google\Cloud\ParameterManager\V1\CreateParameterRequest;
    use Google\Cloud\ParameterManager\V1\Parameter;
    use Google\Cloud\ParameterManager\V1\ParameterFormat;
    
    /**
     * Creates a regional parameter with the specified format.
     *
     * @param string $projectId The Google Cloud Project ID (e.g. 'my-project')
     * @param string $locationId The Parameter Location (e.g. 'us-central1')
     * @param string $parameterId The Parameter ID (e.g. 'my-param')
     * @param string $format The format type of the parameter (UNFORMATTED, YAML, JSON).
     */
    function create_structured_regional_param(string $projectId, string $locationId, string $parameterId, string $format): void
    {
        // Specify regional endpoint.
        $options = ['apiEndpoint' => "parametermanager.$locationId.rep.googleapis.com"];
    
        // Create a client for the Parameter Manager service.
        $client = new ParameterManagerClient($options);
    
        // Build the resource name of the parent object.
        $parent = $client->locationName($projectId, $locationId);
    
        // Create a new Parameter object and set the format.
        $parameter = (new Parameter())
            ->setFormat(ParameterFormat::value($format));
    
        // Prepare the request with the parent, parameter ID, and the parameter object.
        $request = (new CreateParameterRequest())
            ->setParent($parent)
            ->setParameterId($parameterId)
            ->setParameter($parameter);
    
        // Call the API and handle any network failures with print statements.
        $newParameter = $client->createParameter($request);
        printf('Created regional parameter %s with format %s' . PHP_EOL, $newParameter->getName(), ParameterFormat::name($newParameter->getFormat()));
    }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Parameter Manager Python SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-python). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    #!/usr/bin/env python
    
    # Copyright 2025 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    """
    command line application and sample code
    for creating a new formatted regional parameter.
    """
    
    from google.cloud import [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest)
    
    
    def create_structured_regional_param(
        project_id: str,
        location_id: str,
        parameter_id: str,
        format_type: [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[ParameterFormat](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.ParameterFormat.html),
    ) -> parametermanager_v1.Parameter:
        """
        Creates a parameter in the specified region of the specified
        project using the Google Cloud Parameter Manager SDK. The parameter is
        created with the specified format type.
    
        Args:
            project_id (str): The ID of the project where
            the parameter is to be created.
            location_id (str): The ID of the region where
            the parameter is to be created.
            parameter_id (str): The ID to assign to the new parameter.
            This ID must be unique within the project.
            format_type (parametermanager_v1.ParameterFormat): The format type of
            the parameter (UNFORMATTED, YAML, JSON).
    
        Returns:
            parametermanager_v1.Parameter: An object representing the
            newly created parameter.
    
        Example:
            create_structured_regional_param(
                "my-project",
                "my-regional-parameter",
                "us-central1",
                parametermanager_v1.ParameterFormat.JSON
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
    
        # Define the parameter creation request with the specified format.
        request = [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[CreateParameterRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.CreateParameterRequest.html)(
            parent=parent,
            parameter_id=parameter_id,
            parameter=[parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[Parameter](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.Parameter.html)(format_=format_type),
        )
    
        # Create the parameter.
        response = client.[create_parameter](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_create_parameter)(request=request)
    
        # Print the newly created parameter name.
        print(
            f"Created regional parameter: {response.name} "
            f"with format {response.format_.name}"
        )
    
        return response
    

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Parameter Manager Ruby SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-ruby). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    require "google/cloud/parameter_manager"
    
    ##
    # Create a regional parameter
    #
    # @param project_id [String] The Google Cloud project (e.g. "my-project")
    # @param location_id [String] The location name (e.g. "us-central1")
    # @param parameter_id [String] The parameter name (e.g. "my-parameter")
    # @param format [Google::Cloud::ParameterManager::V1::ParameterFormat::]
    # The type of parameter format (UNFORMATTED, YAML, JSON)
    #
    def create_structured_regional_param project_id:, location_id:, parameter_id:, format:
      # Endpoint for the regional parameter manager service.
      api_endpoint = "parametermanager.#{location_id}.rep.googleapis.com"
    
      # Create the Parameter Manager client.
      client = Google::Cloud::[ParameterManager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager.html).[parameter_manager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager/latest/Google-Cloud-ParameterManager.html) do |config|
        config.endpoint = api_endpoint
      end
    
      # Build the resource name of the parent project.
      parent = client.[location_path](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager-V1-ParameterManager-Paths.html) project: project_id, location: location_id
    
      parameter = {
        format: format
      }
    
      # Create the parameter.
      param = client.create_parameter parent: parent, parameter_id: parameter_id, parameter: parameter
    
      # Print the new parameter name.
      puts "Created regional parameter #{param.name} with format #{param.format}"
    end

## Create a parameter to store unstructured data

To create a parameter for storing unstructured data, use one of the following methods:

**Global parameters**

### Console

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. Click **Parameter Manager** to go to the **Parameter Manager** page, and then click **Create parameter**.

  3. In the **Create parameter** page, enter the parameter name.

  4. To create a parameter that stores unformatted data, select **Unformatted** in the **Parameter format** section.

  5. To create a global parameter, select **Multi-region** in the **Location** section, and then select **global (Global)** from the **Region** list.

  6. Optional: To add a label to your parameter resource, click **Add label** , and then define the label key and value.

  7. Click **Create**.




### gcloud

Before using any of the command data below, make the following replacements: 

  * PARAMETER_ID: the name of the new parameter. Parameter names must be 63 characters or less and consist only of English letters (A-Z, a-z), numbers (0-9), dashes (-), and underscores (_). Names can't begin with a dash.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters create PARAMETER_ID --location=global --parameter-format=UNFORMATTED

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters create PARAMETER_ID --location=global --parameter-format=UNFORMATTED

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters create PARAMETER_ID --location=global --parameter-format=UNFORMATTED

You should receive a response similar to the following:
    
    
    Created parameter [allowed_ip_ranges].

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID.
  * PARAMETER_ID: the name of the new parameter. Parameter names must be 63 characters or less and consist only of English letters (A-Z, a-z), numbers (0-9), dashes (-), and underscores (_). Names can't begin with a dash.



HTTP method and URL: 
    
    
    POST https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/parameters?parameter_id=PARAMETER_ID

Request JSON body: 
    
    
    {"format": "UNFORMATTED"}
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/parameters?parameter_id=PARAMETER_ID"

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
        -Uri "https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/parameters?parameter_id=PARAMETER_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/production-1/locations/global/parameters/allowed_ip_ranges",
      "createTime": "2024-10-15T08:31:53.250487112Z",
      "updateTime": "2024-10-15T08:31:53.250487112Z",
      "format": "UNFORMATTED",
      "policyMember": {
        "iamPolicyUidPrincipal": "principal://parametermanager.googleapis.com/projects/567445493557/uid/locations/global/parameters/c0100d79-7c8d-4da3-8eb6-fe2a35843d9b"
      }
    }
    
    

### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Parameter Manager C# SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-csharp). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.ParameterManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.html);
    
    public class CreateParameterSample
    {
        /// <summary>
        /// This function creates a parameter of the format type "unformatted" using the Parameter Manager SDK for GCP.
        /// </summary>
        /// <param name="projectId">The ID of the project where the parameter is to be created.</param>
        /// <param name="parameterId">The ID to assign to the new parameter. This ID must be unique within the project.</param>
        /// <returns>The created Parameter object.</returns>
        public Parameter CreateParameter(
            string projectId,
            string parameterId)
        {
            // Create the client.
            [ParameterManagerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html) client = [ParameterManagerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html#Google_Cloud_ParameterManager_V1_ParameterManagerClient_Create)();
    
            // Build the parent resource name. 
            [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html) parent = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global");
    
            // Build the parameter.
            Parameter parameter = new Parameter();
    
            // Call the API to create the parameter.
            Parameter createdParameter = client.[CreateParameter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html#Google_Cloud_ParameterManager_V1_ParameterManagerClient_CreateParameter_Google_Api_Gax_ResourceNames_LocationName_Google_Cloud_ParameterManager_V1_Parameter_System_String_Google_Api_Gax_Grpc_CallSettings_)(parent, parameter, parameterId);
    
            // Print the created parameter name.
            Console.WriteLine($"Created parameter: {createdParameter.[Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.Parameter.html#Google_Cloud_ParameterManager_V1_Parameter_Name)}");
    
            // Return the created parameter.
            return createdParameter;
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
    
    // createParam creates a new parameter with the format type "unformatted" in Parameter Manager.
    //
    // w: The io.Writer object used to write the output.
    // projectID: The ID of the project where the parameter is located.
    // parameterID: The ID of the parameter to be created.
    //
    // The function returns an error if the parameter creation fails.
    func createParam(w io.Writer, projectID, parameterID string) error {
    	// Create a context and a Parameter Manager client.
    	ctx := context.Background()
    	client, err := parametermanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("failed to create Parameter Manager client: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_Close)()
    
    	// Construct the name of the create parameter.
    	parent := fmt.Sprintf("projects/%s/locations/global", projectID)
    
    	// Build the request to create a new parameter
    	req := &parametermanagerpb.CreateParameterRequest{
    		Parent:      parent,
    		ParameterId: parameterID,
    		Parameter:   &parametermanagerpb.Parameter{},
    	}
    
    	// Call the API to create the parameter.
    	parameter, err := client.CreateParameter(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to create parameter: %w", err)
    	}
    
    	fmt.Fprintf(w, "Created parameter: %s\n", parameter.Name)
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Parameter Manager Java SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-java). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    import com.google.cloud.parametermanager.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.LocationName.html);
    import com.google.cloud.parametermanager.v1.[Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html);
    import com.google.cloud.parametermanager.v1.[ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html);
    import java.io.IOException;
    
    /** This class demonstrates how to create a parameter using the Parameter Manager SDK for GCP. */
    public class CreateParam {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String parameterId = "your-parameter-id";
    
        // Call the method to create parameter.
        createParam(projectId, parameterId);
      }
    
      // This is an example snippet for creating a new parameter.
      public static [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html) createParam(String projectId, String parameterId) throws IOException {
        // Initialize the client that will be used to send requests. This client only
        // needs to be created once, and can be reused for multiple requests.
        try ([ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html) client = [ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html).create()) {
          String locationId = "global";
    
          // Build the parent name from the project.
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.LocationName.html) location = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.LocationName.html).of(projectId, locationId);
    
          // Build the parameter to create.
          [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html) parameter = [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html).newBuilder().build();
    
          // Create the parameter.
          [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html) createdParameter =
              client.createParameter(location.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.LocationName.html#com_google_cloud_parametermanager_v1_LocationName_toString__)(), parameter, parameterId);
          System.out.printf("Created parameter: %s\n", createdParameter.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html#com_google_cloud_parametermanager_v1_Parameter_getName__)());
    
          return createdParameter;
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
    
    // Imports the Parameter Manager library
    const {ParameterManagerClient} = require('[@google-cloud/parametermanager](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)');
    
    // Instantiates a client
    const client = new [ParameterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)();
    
    async function createParam() {
      const parent = client.[locationPath](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/parametermanager/v1.parametermanagerclient.html)(projectId, 'global');
      const request = {
        parent: parent,
        parameterId: parameterId,
      };
    
      const [parameter] = await client.createParameter(request);
      console.log(`Created parameter: ${parameter.name}`);
      return parameter;
    }
    
    return await createParam();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Parameter Manager PHP SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-php). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    // Import necessary classes for creating a parameter.
    use Google\Cloud\ParameterManager\V1\Client\ParameterManagerClient;
    use Google\Cloud\ParameterManager\V1\CreateParameterRequest;
    use Google\Cloud\ParameterManager\V1\Parameter;
    
    /**
     * Creates a parameter of type "unformatted" using the Parameter Manager SDK for GCP.
     *
     * @param string $projectId The Google Cloud Project ID (e.g. 'my-project')
     * @param string $parameterId The Parameter ID (e.g. 'my-param')
     */
    function create_param(string $projectId, string $parameterId): void
    {
        // Create a client for the Parameter Manager service.
        $client = new ParameterManagerClient();
    
        // Build the resource name of the parent object.
        $parent = $client->locationName($projectId, 'global');
    
        // Create a new Parameter object.
        $parameter = new Parameter();
    
        // Prepare the request with the parent, parameter ID, and the parameter object.
        $request = (new CreateParameterRequest())
            ->setParent($parent)
            ->setParameterId($parameterId)
            ->setParameter($parameter);
    
        // Crete the parameter.
        $newParameter = $client->createParameter($request);
    
        // Print the new parameter name
        printf('Created parameter: %s' . PHP_EOL, $newParameter->getName());
    
    }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Parameter Manager Python SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-python). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    def create_param(project_id: str, parameter_id: str) -> parametermanager_v1.Parameter:
        """
        Creates a parameter with default format (Unformatted)
        in the global location of the specified
        project using the Google Cloud Parameter Manager SDK.
    
        Args:
            project_id (str): The ID of the project where
            the parameter is to be created.
            parameter_id (str): The ID to assign to the new parameter.
            This ID must be unique within the project.
    
        Returns:
            parametermanager_v1.Parameter: An object representing
            the newly created parameter.
    
        Example:
            create_param(
                "my-project",
                "my-global-parameter"
            )
        """
        # Import the necessary library for Google Cloud Parameter Manager.
        from google.cloud import parametermanager_v1
    
        # Create the Parameter Manager client.
        client = parametermanager_v1.ParameterManagerClient()
    
        # Build the resource name of the parent project in the global location.
        parent = client.common_location_path(project_id, "global")
    
        # Define the parameter creation request.
        request = parametermanager_v1.CreateParameterRequest(
            parent=parent,
            parameter_id=parameter_id,
        )
    
        # Create the parameter.
        response = client.create_parameter(request=request)
    
        # Print the newly created parameter name.
        print(f"Created parameter: {response.name}")

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Parameter Manager Ruby SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-ruby). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    require "google/cloud/parameter_manager"
    
    ##
    # Create a parameter
    #
    # @param project_id [String] The Google Cloud project (e.g. "my-project")
    # @param parameter_id [String] The parameter name (e.g. "my-parameter")
    #
    def create_param project_id:, parameter_id:
      # Create a Parameter Manager client.
      client = Google::Cloud::[ParameterManager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager.html).[parameter_manager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager/latest/Google-Cloud-ParameterManager.html)
    
      # Build the resource name of the parent project.
      parent = client.[location_path](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager-V1-ParameterManager-Paths.html) project: project_id, location: "global"
    
      # Create the parameter.
      param = client.create_parameter parent: parent, parameter_id: parameter_id
    
      # Print the new parameter name.
      puts "Created parameter #{param.name}"
    end

**Regional parameters**

### Console

  1. In the Google Cloud console, go to the **Secret Manager** page.

[Go to Secret Manager](https://console.cloud.google.com/security/secret-manager)

  2. Click **Parameter Manager** to go to the **Parameter Manager** page, and then click **Create parameter**.

  3. In the **Create parameter** page, enter the parameter name.

  4. To create a parameter that stores unformatted data, select **Unformatted** in the **Parameter format** section.

  5. To create a regional parameter, select **Region** in the **Location** section, and then select the location from the **Region** list.

  6. Optional: To add a label to your parameter resource, click **Add label** , and then define the label key and value.

  7. Click **Create**.




### gcloud

Before using any of the command data below, make the following replacements: 

  * PARAMETER_ID: the name of the new parameter. Parameter names must be 63 characters or less and consist only of English letters (A-Z, a-z), numbers (0-9), dashes (-), and underscores (_). Names can't begin with a dash.
  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the parameter.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters create PARAMETER_ID --location=LOCATION --parameter-format=UNFORMATTED

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters create PARAMETER_ID --location=LOCATION --parameter-format=UNFORMATTED

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters create PARAMETER_ID --location=LOCATION --parameter-format=UNFORMATTED

You should receive a response similar to the following:
    
    
    Created parameter [allowed_ip_ranges].

### REST

Before using any of the request data, make the following replacements: 

  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the parameter.
  * PROJECT_ID: the Google Cloud project ID.
  * PARAMETER_ID: the name of the new parameter. Parameter names must be 63 characters or less and consist only of English letters (A-Z, a-z), numbers (0-9), dashes (-), and underscores (_). Names can't begin with a dash.



HTTP method and URL: 
    
    
    POST https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/parameters?parameter_id=PARAMETER_ID

Request JSON body: 
    
    
    {"format": "UNFORMATTED"}
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/parameters?parameter_id=PARAMETER_ID"

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
        -Uri "https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/parameters?parameter_id=PARAMETER_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/production-1/locations/europe-west1/parameters/allowed_ip_ranges",
      "createTime": "2024-11-08T08:33:05.255559134Z",
      "updateTime": "2024-11-08T08:33:05.255559134Z",
      "format": "UNFORMATTED",
      "policyMember": {
        "iamPolicyUidPrincipal": "principal://parametermanager.googleapis.com/projects/609765466568/uid/locations/europe-west1/parameters/a7787f0d-b033-4f7e-aec0-e8ca4d0b1476"
      }
    }
    

### C#

To run this code, first [set up a C# development environment](https://docs.cloud.google.com/dotnet/docs/setup) and [install the Parameter Manager C# SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-csharp). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.ParameterManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.html);
    
    public class CreateRegionalParameterSample
    {
        /// <summary>
        /// This function creates a regional parameter using the Parameter Manager SDK for GCP.
        /// </summary>
        /// <param name="projectId">The ID of the project where the parameter is to be created.</param>
        /// <param name="locationId">The region where the parameter is to be created.</param>
        /// <param name="parameterId">The ID to assign to the new parameter. This ID must be unique within the project.</param>
        /// <returns>The created Parameter object.</returns>
        public Parameter CreateRegionalParameter(
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
    
            // Build the parent resource name for the regional locationId
            [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html) parent = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, locationId);
    
            // Build the parameter
            Parameter parameter = new Parameter();
    
            // Call the API to create the parameter
            Parameter createdParameter = client.[CreateParameter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.ParameterManagerClient.html#Google_Cloud_ParameterManager_V1_ParameterManagerClient_CreateParameter_Google_Api_Gax_ResourceNames_LocationName_Google_Cloud_ParameterManager_V1_Parameter_System_String_Google_Api_Gax_Grpc_CallSettings_)(parent, parameter, parameterId);
    
            // Print the created parameter name
            Console.WriteLine($"Created regional parameter: {createdParameter.[Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ParameterManager.V1/latest/Google.Cloud.ParameterManager.V1.Parameter.html#Google_Cloud_ParameterManager_V1_Parameter_Name)}");
    
            // Return the created parameter
            return createdParameter;
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
    
    // createRegionalParam creates a parameter regional of the format type "unformatted" using the Parameter Manager SDK for GCP.
    //
    // w: The io.Writer object used to write the output.
    // projectID: The ID of the project where the parameter is located.
    // locationID: The region where the parameter is to be created.
    // parameterID: The ID of the parameter to be created.
    //
    // The function returns an error if the parameter creation fails.
    func createRegionalParam(w io.Writer, projectID, locationID, parameterID string) error {
    	// Create a context and a Parameter Manager client.
    	ctx := context.Background()
    
    	// Create a Parameter Manager client.
    	endpoint := fmt.Sprintf("parametermanager.%s.rep.googleapis.com:443", locationID)
    	client, err := parametermanager.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_NewClient)(ctx, option.WithEndpoint(endpoint))
    	if err != nil {
    		return fmt.Errorf("failed to create Parameter Manager client: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1.html#cloud_google_com_go_parametermanager_apiv1_Client_Close)()
    
    	// Construct the name of the create parameter.
    	parent := fmt.Sprintf("projects/%s/locations/%s", projectID, locationID)
    
    	// Create a parameter with unformatted format.
    	req := &parametermanagerpb.CreateParameterRequest{
    		Parent:      parent,
    		ParameterId: parameterID,
    		Parameter: &parametermanagerpb.Parameter{
    			Format: parametermanagerpb.[ParameterFormat_UNFORMATTED](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/parametermanager/latest/apiv1/parametermanagerpb.html#cloud_google_com_go_parametermanager_apiv1_parametermanagerpb_ParameterFormat_PARAMETER_FORMAT_UNSPECIFIED_ParameterFormat_UNFORMATTED_ParameterFormat_YAML_ParameterFormat_JSON),
    		},
    	}
    	parameter, err := client.CreateParameter(ctx, req)
    	if err != nil {
    		return fmt.Errorf("failed to create parameter: %w", err)
    	}
    
    	fmt.Fprintf(w, "Created regional parameter: %s\n", parameter.Name)
    	return nil
    }
    

### Java

To run this code, first [set up a Java development environment](https://docs.cloud.google.com/java/docs/setup) and [install the Parameter Manager Java SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-java). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    import com.google.cloud.parametermanager.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.LocationName.html);
    import com.google.cloud.parametermanager.v1.[Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html);
    import com.google.cloud.parametermanager.v1.[ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html);
    import com.google.cloud.parametermanager.v1.[ParameterManagerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerSettings.html);
    import java.io.IOException;
    
    /**
     * This class demonstrates how to create a regional parameter using the Parameter Manager SDK for
     * GCP.
     */
    public class CreateRegionalParam {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String locationId = "your-location-id";
        String parameterId = "your-parameter-id";
    
        createRegionalParam(projectId, locationId, parameterId);
      }
    
      // This is an example snippet for creating a new regional parameter.
      public static [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html) createRegionalParam(
          String projectId, String locationId, String parameterId) throws IOException {
    
        // Endpoint to call the regional parameter manager server
        String apiEndpoint = String.format("parametermanager.%s.rep.googleapis.com:443", locationId);
        [ParameterManagerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerSettings.html) parameterManagerSettings =
            [ParameterManagerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerSettings.html).newBuilder().setEndpoint(apiEndpoint).build();
    
        // Initialize the client that will be used to send requests. This client only needs to be
        // created once, and can be reused for multiple requests.
        try ([ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html) client = [ParameterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.ParameterManagerClient.html).create(parameterManagerSettings)) {
          // Build the parent name from the project.
          [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.LocationName.html) location = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.LocationName.html).of(projectId, locationId);
    
          // Build the regional parameter to create.
          [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html) parameter = [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html).newBuilder().build();
    
          // Create the regional parameter.
          [Parameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html) createdParameter =
              client.createParameter(location.[toString](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.LocationName.html#com_google_cloud_parametermanager_v1_LocationName_toString__)(), parameter, parameterId);
          System.out.printf("Created regional parameter: %s\n", createdParameter.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-parametermanager/latest/com.google.cloud.parametermanager.v1.Parameter.html#com_google_cloud_parametermanager_v1_Parameter_getName__)());
    
          return createdParameter;
        }
      }
    }

### Node.js

To run this code, first [set up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup) and [install the Parameter Manager Node.js SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-nodejs). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const projectId = 'YOUR_PROJECT_ID';
    // const locationId = 'YOUR_LOCATION_ID';
    // const parameterId = 'YOUR_PARAMETER_ID';
    
    // Imports the Parameter Manager library
    const {ParameterManagerClient} = require('[@google-cloud/parametermanager](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)');
    
    // Adding the endpoint to call the regional parameter manager server
    const options = {
      apiEndpoint: `parametermanager.${locationId}.rep.googleapis.com`,
    };
    
    // Instantiates a client with regional endpoint
    const client = new [ParameterManagerClient](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/overview.html)(options);
    
    async function createRegionalParam() {
      const parent = client.[locationPath](https://docs.cloud.google.com/nodejs/docs/reference/parametermanager/latest/parametermanager/v1.parametermanagerclient.html)(projectId, locationId);
      const request = {
        parent: parent,
        parameterId: parameterId,
      };
    
      const [parameter] = await client.createParameter(request);
      console.log(`Created regional parameter: ${parameter.name}`);
      return parameter;
    }
    
    return await createRegionalParam();

### PHP

To run this code, first learn about [using PHP on Google Cloud](https://docs.cloud.google.com/php/docs) and [install the Parameter Manager PHP SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-php). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    // Import necessary classes for creating a parameter.
    use Google\Cloud\ParameterManager\V1\Client\ParameterManagerClient;
    use Google\Cloud\ParameterManager\V1\CreateParameterRequest;
    use Google\Cloud\ParameterManager\V1\Parameter;
    
    /**
     * Creates a regional parameter of type "unformatted" using the Parameter Manager SDK for GCP.
     *
     * @param string $projectId The Google Cloud Project ID (e.g. 'my-project')
     * @param string $locationId The Parameter Location (e.g. 'us-central1')
     * @param string $parameterId The Parameter ID (e.g. 'my-param')
     */
    function create_regional_param(string $projectId, string $locationId, string $parameterId): void
    {
        // Specify regional endpoint.
        $options = ['apiEndpoint' => "parametermanager.$locationId.rep.googleapis.com"];
    
        // Create a client for the Parameter Manager service.
        $client = new ParameterManagerClient($options);
    
        // Build the resource name of the parent object.
        $parent = $client->locationName($projectId, $locationId);
    
        // Create a new Parameter object.
        $parameter = new Parameter();
    
        // Prepare the request with the parent, parameter ID, and the parameter object.
        $request = (new CreateParameterRequest())
            ->setParent($parent)
            ->setParameterId($parameterId)
            ->setParameter($parameter);
    
        // Crete the parameter.
        $newParameter = $client->createParameter($request);
    
        // Print the new parameter name
        printf('Created regional parameter: %s' . PHP_EOL, $newParameter->getName());
    }

### Python

To run this code, first [set up a Python development environment](https://docs.cloud.google.com/python/docs/setup) and [install the Parameter Manager Python SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-python). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    def create_regional_param(
        project_id: str, location_id: str, parameter_id: str
    ) -> parametermanager_v1.Parameter:
        """
        Creates a regional parameter with default format (Unformatted)
        in the specified location and
        project using the Google Cloud Parameter Manager SDK.
    
        Args:
            project_id (str): The ID of the project where
            the parameter is to be created.
            location_id (str): The region where the parameter is to be created.
            parameter_id (str): The ID to assign to the new parameter.
            This ID must be unique within the project.
    
        Returns:
            parametermanager_v1.Parameter: An object representing
            the newly created parameter.
    
        Example:
            create_regional_param(
                "my-project",
                "us-central1",
                "my-regional-parameter"
            )
        """
    
        # Import the Parameter Manager client library.
        from google.cloud import [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest)
    
        api_endpoint = f"parametermanager.{location_id}.rep.googleapis.com"
        # Create the Parameter Manager client for the specified region.
        client = [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[ParameterManagerClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html)(
            client_options={"api_endpoint": api_endpoint}
        )
    
        # Build the resource name of the parent project for the specified region.
        parent = client.[common_location_path](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_common_location_path)(project_id, location_id)
    
        # Define the parameter creation request.
        request = [parametermanager_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest).[CreateParameterRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.CreateParameterRequest.html)(
            parent=parent,
            parameter_id=parameter_id,
        )
    
        # Create the parameter.
        response = client.[create_parameter](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.ParameterManagerClient.html#google_cloud_parametermanager_v1_services_parameter_manager_ParameterManagerClient_create_parameter)(request=request)
    
        # Print the newly created parameter name.
        print(f"Created regional parameter: {response.name}")

### Ruby

To run this code, first [set up a Ruby development environment](https://docs.cloud.google.com/ruby/docs/setup) and [install the Parameter Manager Ruby SDK](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference/libraries#client-libraries-install-ruby). On Compute Engine or GKE, you must [authenticate with the `cloud-platform` scope](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes). 
    
    
    require "google/cloud/parameter_manager"
    
    ##
    # Create a regional parameter
    #
    # @param project_id [String] The Google Cloud project (e.g. "my-project")
    # @param location_id [String] The location name (e.g. "us-central1")
    # @param parameter_id [String] The parameter name (e.g. "my-parameter")
    #
    def create_regional_param project_id:, location_id:, parameter_id:
      # Endpoint for the regional parameter manager service.
      api_endpoint = "parametermanager.#{location_id}.rep.googleapis.com"
    
      # Create the Parameter Manager client.
      client = Google::Cloud::[ParameterManager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager.html).[parameter_manager](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager/latest/Google-Cloud-ParameterManager.html) do |config|
        config.endpoint = api_endpoint
      end
    
      # Build the resource name of the parent project.
      parent = client.[location_path](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-parameter_manager-v1/latest/Google-Cloud-ParameterManager-V1-ParameterManager-Paths.html) project: project_id, location: location_id
    
      # Create the parameter.
      param = client.create_parameter parent: parent, parameter_id: parameter_id
    
      # Print the new parameter name.
      puts "Created regional parameter #{param.name}"
    end

**Note:** The parameter creation endpoint has a threshold of approximately 1 query per second (QPS). If you encounter a `RESOURCE_EXHAUSTED` error while creating a parameter, we recommend that you resubmit your request to resolve the issue.

### Built-in identities for parameters

Parameters are resource types with [built-in identities](https://docs.cloud.google.com/guides/product-specific/iam/iam-terms). This means that each parameter has a unique identifier that distinguishes it from all other resources in your Google Cloud project. This unique identifier is automatically generated when you create a parameter and stored in the `iamPolicyUidPrincipal` field of the parameter resource.

You can grant roles to the parameter by including the resource's principal identifier in your allow policies when you want the parameter to access Secret Manager resources. For more information, see [Built-in identities for resources](https://docs.cloud.google.com/iam/docs/built-in-resource-identities).

## What's next

  * [Add a parameter version](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/add-parameter-version)
  * [Reference secrets in parameters](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference-secrets-in-parameter)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
