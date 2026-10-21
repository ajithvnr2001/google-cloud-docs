---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/extension/
title: Extensions API \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:29:35.040206+00:00
---

# Extensions API  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/extension/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)



Send feedback 

#  Extensions API Stay organized with collections  Save and categorize content based on your preferences. 

Extensions are tools for large language models (LLMs) to access external data, run computations, and perform other operations. They can process real-time data and perform real-world actions. 

Vertex AI provides the Extension API that can register, manage, and execute extensions. Vertex AI also provides a set of prebuilt extensions from the Extension API including the code interpreter extension and Agent Search extension.

**Limitations**

The Extension API is only available in the `us-central1` region.

## Example syntax

Syntax to create an extension resource.

### curl
    
    
    curl -X POST \
    
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    
    https://${LOCATION}-aiplatform.googleapis.com/v1beta1/projects/${PROJECT_ID}/locations/${LOCATION}/extensions:import \
    -d '{
      "displayName": "...",
      "description": "...",
      "manifest": {
        ...
        "apiSpec": {
          ...
        },
        "authConfig": {
          ...
        }
        ...
      }
    }'

### Python
    
    
    from vertexai.preview import extensions
    
    extensions.Extension.create(
      manifest: Union[JsonDict, ExtensionManifest],
      display_name: Optional[str] = None,
      description: Optional[str] = None,
      runtime_config: Optional[Union[JsonDict, RuntimeConfig]] = None
    )

## Parameter list

#### Request body

Parameters  
---  
`displayName` | Optional: `string`The display name of the extension that is displayed to users from the API and UI. This should be a UTF-8 string up to 128 characters.  
`description` | Optional: `string`The description of the extension that is displayed to users from the API and UI. This should be a UTF-8 string up to 1MB.  
`manifest` | `JsonDict|ExtensionManifest`The manifest of the extension.  
`runtimeConfig` | Optional: `JsonDict|RuntimeConfig`The runtime configuration that controls the runtime behavior of the extension. For the code interpreter extension, the format is the following:
    
    
      "runtimeConfig": {
        "codeInterpreterRuntimeConfig": {
            "fileInputGcsBucket": string,
            "fileOutputGcsBucket": string
        }
      }

For the Agent Search extension, the format is the following: 
    
    
      "runtimeConfig": {
        "vertexAiSearchRuntimeConfig": {
          "servingConfigName": string,
        }
      }  
  
#### `manifest`

The manifest of the extension.

Parameters  
---  
`name` | `string`The name of the extension that is used by the LLM for reasoning. This should be a UTF-8 string up to 128 characters.  
`description` | `string`The natural language description of the extension's usage. The description is shown to the LLM to help it perform reasoning.This should be a UTF-8 string up to 1MB.  
`apiSpec` | `ApiSpec`The API specification shown to the LLM for reasoning. You should provide a meaningful and informative description. `apiSpec` contains the reference to the Cloud Storage URI storing the OpenAPI yaml file. 
    
    
      "apiSpec": {
        "openApiGcsUri": string
      }  
  
`authConfig` | `JsonDict|AuthConfig`The type of auth supported by this extension. An extension import request must contain an authentication configuration.
    
    
    "authConfig": {
      "authType": "GOOGLE_SERVICE_ACCOUNT_AUTH",
      "googleServiceAccountConfig": {
        "serviceAccount": string
      },
    }  
  
#### `apiSpec`

The API specification shown to the LLM for reasoning.

Parameters  
---  
`openApiGcsUri` | `string`Cloud Storage URI of the OpenAPI YAML file describing the extension API, such as `gs://vertex-extension-public/code_interpreter.yaml`  
  
#### `authConfig`

The type of authentication supported by this extension.

Parameters  
---  
`authType` | `string`Authentication method. Supported values: `GOOGLE_SERVICE_ACCOUNT_AUTH`.  
  
#### `googleServiceAccountConfig`

The code interpreter extension and Vertex AI Search extension only support Google Service Account authentication, where Vertex AI uses the Vertex AI Extension Service Agent to access the APIs.

Parameters  
---  
`serviceAccount` | Optional: `string`The service account that the extension execution runs as. If the service account is specified, the `iam.serviceAccounts.getAccessToken` permission should be granted to the Vertex AI [Extension Service Agent](https://docs.cloud.google.com/vertex-ai/docs/general/access-control#service-agents) on the specified service account. If not specified, the Vertex AI Extension Service Agent is used to execute the extension.  
  
#### `runtimeConfig`

The `runtimeConfig` object contains additional configurations used when running the extension.

Code interpreter extension

Parameters  
---  
`fileInputGcsBucket` | Optional: `string`The Cloud Storage bucket for the file input to the extension. The Vertex Extension Custom Code Service Agent should be granted the `roles/storage.objectViewer` permission to this bucket. If not specified, the extension only accepts file contents from the request body and rejects Cloud Storage file inputs.  
`fileOutputGcsBucket` | Optional: `string`The Cloud Storage bucket for the file output from the extension. The Vertex Extension Custom Code Service Agent should be granted the `roles/storage.objectUser` permission to this bucket. If not specified, the file content is output in the response body.  
  
Agent Search extension

Parameters  
---  
`servingConfigName` | `string`Agent Search serving config name to specify which Agent Search resource the extension uses. Format:`projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/servingConfigs/{serving_config}`  
  
#### Execute extension

Parameters  
---  
`operation_id` | `string`The selected ID of the operation to be executed in this extension.  
`operation_params` | Optional: `JsonDict|Struct`Request parameters that are used for executing this operation. The JSON should be in the form of a map with parameter name as the key and the actual parameter value as the value. For example, to set a parameter called `query` to the string "What is Vertex AI?", you can use `{"query": "What is Vertex AI?"}`.  
  
## Examples

### Import a code interpreter extension

Create or register an extension resource.

This example shows how to import a code interpreter extension.

**Note:** Import a code interpreter is a preview feature and is only available through the `v1beta1` version of the API.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifiers).
  * LOCATION: The region to process the request.
  * DISPLAY_NAME: The display name of the extension that is displayed to users from the API and UI. This should be a UTF-8 string up to 128 characters. 
  * DESCRIPTION: The description of the extension that is displayed to users from the API and UI. This should be a UTF-8 string up to 1MB.
  * MANIFEST_NAME: The name of the extension that is used by the LLM for reasoning. This should be a UTF-8 string up to 128 characters 
  * MANIFEST_DESCRIPTION: The natural language description shown to the LLM. It should describe the usage of the extension, and is essential for the LLM to perform reasoning. This should be a UTF-8 string up to 1MB.
  * GCS_URI: Cloud Storage URI of the OpenAPI YAML file describing the extension API. 
  * AUTH_TYPE: Authentication method. Supported values: `GOOGLE_SERVICE_ACCOUNT_AUTH`.



HTTP method and URL: 
    
    
    POST https://LOCATION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/extensions:import

Request JSON body: 
    
    
    {
      "displayName": "DISPLAY_NAME",
      "description": "DESCRIPTION",
      "manifest": {
        "name": "NAME",
        "description": "MANIFEST_DESCRIPTION",
        "apiSpec": {
          "openApiGcsUri": "GCS_URI",
        },
        "authConfig": {
          "authType": "AUTH_TYPE",
          "googleServiceAccountConfig": {}
        }
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://LOCATION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/extensions:import"

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
        -Uri "https://LOCATION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/extensions:import" | Select-Object -Expand Content

### Python

To learn how to install or update the Vertex AI SDK for Python, see [Install the Vertex AI SDK for Python](https://docs.cloud.google.com/vertex-ai/docs/start/use-vertex-ai-python-sdk). For more information, see the [ Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 
    
    
    import vertexai
    from vertexai.preview import extensions
    
    # TODO(developer): Update and un-comment below line
    # PROJECT_ID = "your-project-id"
    vertexai.init(project=PROJECT_ID, location="us-central1")
    
    extension = extensions.Extension.create(
        display_name="Code Interpreter",
        description="This extension generates and executes code in the specified language",
        manifest={
            "name": "code_interpreter_tool",
            "description": "Google Code Interpreter Extension",
            "api_spec": {
                "open_api_gcs_uri": "gs://vertex-extension-public/code_interpreter.yaml"
            },
            "auth_config": {
                "google_service_account_config": {},
                "auth_type": "GOOGLE_SERVICE_ACCOUNT_AUTH",
            },
        },
    )
    print(extension.resource_name)
    # Example response:
    # projects/123456789012/locations/us-central1/extensions/12345678901234567
    

### Import with a runtime configuration

Create or register an extension resource.

This example shows to import a Agent Search extension by specifying `RuntimeConfig`.

**Note:** Import with a runtime configuration is a preview feature and is only available through the `v1beta1` version of the API.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: .
  * LOCATION: The region to process the request.
  * DISPLAY_NAME: The display name of the extension that is displayed to users from the API and UI. This should be a UTF-8 string up to 128 characters. 
  * DESCRIPTION: The description of the extension that is displayed to users from the API and UI. This should be a UTF-8 string up to 1MB.
  * MANIFEST_NAME: The name of the extension that is used by the LLM for reasoning. This should be a UTF-8 string up to 128 characters 
  * MANIFEST_DESCRIPTION: The natural language description shown to the LLM. It should describe the usage of the extension, and is essential for the LLM to perform reasoning. This should be a UTF-8 string up to 1MB.
  * GCS_URI: Cloud Storage URI of the OpenAPI YAML file describing the extension API. 
  * AUTH_TYPE: Authentication method. Supported values: `GOOGLE_SERVICE_ACCOUNT_AUTH`.
  * SERVING_CONFIG_NAME: Vertex AI Search serving config name to specify which Vertex AI Search resource the extension uses. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/servingConfigs/{serving_config}`



HTTP method and URL: 
    
    
    POST https://LOCATION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/extensions:import

Request JSON body: 
    
    
    {
      "displayName": "DISPLAY_NAME",
      "description": "DESCRIPTION",
      "manifest": {
        "name": "NAME",
        "description": "MANIFEST_DESCRIPTION",
        "apiSpec": {
          "openApiGcsUri": "GCS_URI",
        },
        "authConfig": {
          "authType": "AUTH_TYPE",
          "googleServiceAccountConfig": {}
        },
        runtime_config={
          "vertex_ai_search_runtime_config": {
              "serving_config_name": SERVING_CONFIG_NAME,
          }
        }
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://LOCATION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/extensions:import"

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
        -Uri "https://LOCATION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/extensions:import" | Select-Object -Expand Content

### Python
    
    
    import [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest)
    from vertexai.preview import extensions
    
    [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest).init(project=PROJECT_ID, location=LOCATION)
    
    extension_vertex_ai_search = extensions.Extension.create(
        display_name = "vertex_ai_search",
        description = "This extension search from provided datastore",
        manifest = {
            "name": "vertex_ai_search",
            "description": "Google Vertex AI Search Extension",
            "api_spec": {
                "open_api_gcs_uri": "gs://vertex-extension-public/vertex_ai_search.yaml"
            },
            "auth_config": {
                "google_service_account_config": {},
                "auth_type": "GOOGLE_SERVICE_ACCOUNT_AUTH",
            },
        },
        runtime_config={
            "vertex_ai_search_runtime_config": {
                "serving_config_name": SERVING_CONFIG_NAME,
            }
        }
    )

## Execute an extension

To execute an extension, directly call the extension and provide the execution parameters in the request.

This example executes the code interpreter extension `generate_and_execute` to get the answer for the query `find the max value in the list: [1,2,3,4,-5]`.

**Note:** Execute an extension is a preview feature and is only available through the `v1beta1` version of the API.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: .
  * LOCATION: The region to process the request.
  * EXTENSION_ID: The ID of the extension.
  * OPERATION_ID: The selected ID of the operation to be executed in this extension.
  * QUERY: The Request parameters to execute the operation in a Key-Value format, `{"query": "What is Vertex AI?"}.`



HTTP method and URL: 
    
    
    POST https://LOCATION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/extensions/EXTENSION_ID:execute

Request JSON body: 
    
    
    {
      "operation_id": "OPERATION_ID",
      "operation_params": {
        "query": "QUERY",
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://LOCATION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/extensions/EXTENSION_ID:execute"

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
        -Uri "https://LOCATION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/extensions/EXTENSION_ID:execute" | Select-Object -Expand Content

### Python

To learn how to install or update the Vertex AI SDK for Python, see [Install the Vertex AI SDK for Python](https://docs.cloud.google.com/vertex-ai/docs/start/use-vertex-ai-python-sdk). For more information, see the [ Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 
    
    
    import vertexai
    from vertexai.preview import extensions
    
    # TODO(developer): Update and un-comment below lines
    # PROJECT_ID = "your-project-id"
    # extension_id = "your-extension-id"
    vertexai.init(project=PROJECT_ID, location="us-central1")
    
    extension = extensions.Extension(extension_id)
    
    response = extension.execute(
        operation_id="generate_and_execute",
        operation_params={"query": "find the max value in the list: [1,2,3,4,-5]"},
    )
    print(response)
    # Example response:
    # {
    #     "generated_code": "```python\n# Find the maximum value in the list\ndata = [1, 2,..", ..
    #     "execution_result": "The maximum value in the list is: 4\n",
    #     "execution_error": "",
    #     "output_files": [],
    # }
    

## List Extensions

List extensions in a project.

**Note:** List extensions is a preview feature and is only available through the `v1beta1` version of the API.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: .
  * LOCATION: The region to process the request.
  * EXTENSION_ID: The ID of the extension.



HTTP method and URL: 
    
    
    GET https://LOCATION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/extensions

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://LOCATION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/extensions"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://LOCATION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/extensions" | Select-Object -Expand Content

### Python

To learn how to install or update the Vertex AI SDK for Python, see [Install the Vertex AI SDK for Python](https://docs.cloud.google.com/vertex-ai/docs/start/use-vertex-ai-python-sdk). For more information, see the [ Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 
    
    
    import vertexai
    from vertexai.preview import extensions
    
    # TODO (developer):Update project_id
    # PROJECT_ID = "your-project-id"
    vertexai.init(project=PROJECT_ID, location="us-central1")
    
    extensions_list = extensions.Extension.list()
    print(extensions_list)
    # Example response:
    # [<vertexai.extensions._extensions.Extension object at 0x76e8ced37af0>
    # resource name: projects/[PROJECT_ID]/locations/us-central1/extensions/1234567890123456]
    

## Get an extension

Get details of an extension.

**Note:** Get details is a preview feature and is only available through the `v1beta1` version of the API.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: .
  * LOCATION: The region to process the request.
  * EXTENSION_ID: The ID of the extension.



HTTP method and URL: 
    
    
    GET https://LOCATION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/extensions/EXTENSION_ID

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://LOCATION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/extensions/EXTENSION_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://LOCATION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/extensions/EXTENSION_ID" | Select-Object -Expand Content

### Python

To learn how to install or update the Vertex AI SDK for Python, see [Install the Vertex AI SDK for Python](https://docs.cloud.google.com/vertex-ai/docs/start/use-vertex-ai-python-sdk). For more information, see the [ Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 
    
    
    import vertexai
    from vertexai.preview import extensions
    
    # TODO(developer): Update and un-comment below lines
    # PROJECT_ID = "your-project-id"
    # extension_id = "your-extension-id"
    vertexai.init(project=PROJECT_ID, location="us-central1")
    
    extension = extensions.Extension(extension_id)
    print(extension.resource_name)
    # Example response:
    # projects/[PROJECT_ID]/locations/us-central1/extensions/12345678901234567
    

## Update an extension

Update an extension.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: .
  * LOCATION: The region to process the request.
  * EXTENSION_ID: The ID of the extension.
  * UPDATE_MASK: The parameter to updated. Accepted values, `displayName`, `description`, or `toolUseExamples`.



HTTP method and URL: 
    
    
    PATCH https://LOCATION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/extensions/EXTENSION_ID?update_mask="UPDATE_MASK"

Request JSON body: 
    
    
    {
      "description": "UPDATE_MASK",
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://LOCATION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/extensions/EXTENSION_ID?update_mask="UPDATE_MASK""

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
        -Uri "https://LOCATION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/extensions/EXTENSION_ID?update_mask="UPDATE_MASK"" | Select-Object -Expand Content

## Delete Extension

Delete an extension.

This example deletes the extension associated with the extension ID.

**Note:** Delete extension is a preview feature and is only available through the `v1beta1` version of the API.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: .
  * LOCATION: The region to process the request.
  * EXTENSION_ID: The ID of the extension.



HTTP method and URL: 
    
    
    DELETE https://LOCATION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/extensions/EXTENSION_ID

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://LOCATION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/extensions/EXTENSION_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://LOCATION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/extensions/EXTENSION_ID" | Select-Object -Expand Content

### Python

To learn how to install or update the Vertex AI SDK for Python, see [Install the Vertex AI SDK for Python](https://docs.cloud.google.com/vertex-ai/docs/start/use-vertex-ai-python-sdk). For more information, see the [ Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 
    
    
    import vertexai
    from vertexai.preview import extensions
    
    # TODO(developer): Update and un-comment below lines
    # PROJECT_ID = "your-project-id"
    # extension_id = "extension_id"
    vertexai.init(project=PROJECT_ID, location="us-central1")
    
    extension = extensions.Extension(extension_id)
    extension.delete()
    # Example response:
    # ...
    # Extension resource projects/[PROJECT_ID]/locations/us-central1/extensions/[extension_id] deleted.
    

## What's next

  * [Connect models to APIs by using extensions](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/extensions/overview)
  * [Extensions by Google](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/extensions/google-extensions)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
