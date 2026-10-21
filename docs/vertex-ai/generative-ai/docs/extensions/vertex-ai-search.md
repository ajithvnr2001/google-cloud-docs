---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/extensions/vertex-ai-search/
title: Agent Search extension \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:43:06.590251+00:00
---

# Agent Search extension  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/extensions/vertex-ai-search/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)



Send feedback 

#  Agent Search extension Stay organized with collections  Save and categorize content based on your preferences. 

Vertex AI Extensions has been deprecated as of May 26, 2026. After November 26, 2026, Vertex AI Extensions will be shut down and no longer function. For equivalent functionality, see the [Extensions migration guide](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/extensions/migrate). 

**Preview**

Vertex AI Extensions is a Preview offering, subject to the "Pre-GA Offerings Terms" of the [Google Cloud Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA products and features may have limited support, and changes to pre-GA products and features may not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). Further, by using Vertex AI Extensions, you agree to the Generative AI Preview [terms and conditions](https://cloud.google.com/trustedtester/aitos) ("Preview Terms"). 

This document shows you how to register and use the Google-provided Agent Search [extension](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/extensions/overview) from the Google Cloud console and the Vertex AI API. This extension lets you access and search website corpuses and unstructured data to provide relevant responses to natural language questions, such as:

  * "How did the competitive threats for the company change from Q1 of last year to Q1 of this year?"
  * "What parts of the company are growing the fastest? How fast?"



The Agent Search extension uses [Agent Search](https://docs.cloud.google.com/generative-ai-app-builder/docs/introduction#es-and-personalize) to retrieve meaningful results from your data store. The Agent Search extension is defined in an [OpenAPI Specification](https://github.com/OAI/OpenAPI-Specification/blob/main/README.md) `vertex_ai_search.yaml` file.

To use the Agent Search extension, you must [Create a data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/prepare-data) in the global region with a specified search scope. For best search results, enable advanced indexing for website data and the Enterprise edition for unstructured data. See [About advanced features](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-advanced-features) for more information.

Expand Me Collapse Me
    
    
    openapi: "3.0.0"
    info:
      title: Vertex AI Search
      version: v1alpha
      description: >
        Performs search on user ingested data including website and unstructured data type.
    
        This extension is used when user wants to search or retrieve meaningful results from their ingested data in the Vertex AI Search service.
    
        Supported AuthTypes:
        - GOOGLE_SERVICE_ACCOUNT_AUTH: (only supports using Vertex AI Extension Service Agent).
    paths:
      /search:
        get:
          operationId: search
          description: Retrieves the results from user's query by searching in the data store.
          parameters:
          - name: query
            in: query
            schema:
              type: string
            description: User natural language instructions for search.
            required: true
          responses:
            default:
              description: Search execution result.
              content:
                application/json:
                  schema:
                    $ref: "#/components/schemas/SearchResult"
    
    components:
      schemas:
        SearchResult:
          description: Top results from search response.
          type: object
          properties:
            results:
              type: array
              items:
                type: object
                properties:
                  title:
                    type: string
                    description: Retrieved document title.
                  display_link:
                    type: string
                    description: Retrieved document link to display.
                  link:
                    type: string
                    description: Retrieved document link.
                  extractive_segments:
                    type: array
                    description: Extractive segments from the retrieved file.
                    items:
                      type: string
                  extractive_answers:
                    type: array
                    description: Extractive answers from the retrieved file. These are generated from the extractive segments.
                    items:
                      type: string
    
        

To learn about Google extensions with end-to-end tutorials, see the following Jupyter notebooks:

  * **Business analyst workflow with Vertex AI Extensions** : Use the [Code Interpreter extension](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/extensions/code-interpreter) and the Agent Search extension to complete a housing investment opportunities research report for business stakeholders.  
[Colab](https://art-analytics.appspot.com/r.html?uaid=G-FHXEFWTT4E&utm_source=aRT-ba_extbygoog_notebook-cloud_docs-colab&utm_medium=aRT-clicks&utm_campaign=ba_extbygoog_notebook-cloud_docs-colab&destination=ba_extbygoog_notebook-cloud_docs-colab&url=https%3A%2F%2Fcolab.research.google.com%2Fgithub%2FGoogleCloudPlatform%2Fapplied-ai-engineering-samples%2Fblob%2Fmain%2Fgenai-on-vertex-ai%2Fvertex_ai_extensions%2Fnotebooks%2Fbusiness_analyst_workflow_vertexai_extensions.ipynb) | [GitHub](https://art-analytics.appspot.com/r.html?uaid=G-FHXEFWTT4E&utm_source=aRT-ba_extbygoog_notebook-cloud_docs-github&utm_medium=aRT-clicks&utm_campaign=ba_extbygoog_notebook-cloud_docs-github&destination=ba_extbygoog_notebook-cloud_docs-github&url=https%3A%2F%2Fgithub.com%2FGoogleCloudPlatform%2Fapplied-ai-engineering-samples%2Fblob%2Fmain%2Fgenai-on-vertex-ai%2Fvertex_ai_extensions%2Fnotebooks%2Fbusiness_analyst_workflow_vertexai_extensions.ipynb) | [Vertex AI Workbench](https://art-analytics.appspot.com/r.html?uaid=G-FHXEFWTT4E&utm_source=aRT-ba_extbygoog_notebook-cloud_docs-vai_workbench&utm_medium=aRT-clicks&utm_campaign=ba_extbygoog_notebook-cloud_docs-vai_workbench&destination=ba_extbygoog_notebook-cloud_docs-vai_workbench&url=https%3A%2F%2Fconsole.cloud.google.com%2Fvertex-ai%2Fworkbench%2Fdeploy-notebook%3Fdownload_url%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fapplied-ai-engineering-samples%2Fmain%2Fgenai-on-vertex-ai%2Fvertex_ai_extensions%2Fnotebooks%2Fbusiness_analyst_workflow_vertexai_extensions.ipynb)
  * **Game review analysis workflow with Vertex AI Extensions** : Use the [Code Interpreter extension](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/extensions/code-interpreter) to analyze game reviews from [Steam](https://store.steampowered.com/). Use the Agent Search extension to summarize game reviews from websites. Use the Code Interpreter extension to build a report with all of the generated assets.  
[Colab](https://art-analytics.appspot.com/r.html?uaid=G-FHXEFWTT4E&utm_source=aRT-gamerev_extbygoog_notebook-cloud_docs-colab&utm_medium=aRT-clicks&utm_campaign=gamerev_extbygoog_notebook-cloud_docs-colab&destination=gamerev_extbygoog_notebook-cloud_docs-colab&url=https%3A%2F%2Fcolab.research.google.com%2Fgithub%2FGoogleCloudPlatform%2Fapplied-ai-engineering-samples%2Fblob%2Fmain%2Fgenai-on-vertex-ai%2Fvertex_ai_extensions%2Fnotebooks%2Fgame_review_analysis_vertexai_extensions.ipynb) | [GitHub](https://art-analytics.appspot.com/r.html?uaid=G-FHXEFWTT4E&utm_source=aRT-gamerev_extbygoog_notebook-cloud_docs-github&utm_medium=aRT-clicks&utm_campaign=gamerev_extbygoog_notebook-cloud_docs-github&destination=gamerev_extbygoog_notebook-cloud_docs-github&url=https%3A%2F%2Fgithub.com%2FGoogleCloudPlatform%2Fapplied-ai-engineering-samples%2Fblob%2Fmain%2Fgenai-on-vertex-ai%2Fvertex_ai_extensions%2Fnotebooks%2Fgame_review_analysis_vertexai_extensions.ipynb) | [Vertex AI Workbench](https://art-analytics.appspot.com/r.html?uaid=G-FHXEFWTT4E&utm_source=aRT-gamerev_extbygoog_notebook-cloud_docs-vai_workbench&utm_medium=aRT-clicks&utm_campaign=gamerev_extbygoog_notebook-cloud_docs-vai_workbench&destination=gamerev_extbygoog_notebook-cloud_docs-vai_workbench&url=https%3A%2F%2Fconsole.cloud.google.com%2Fvertex-ai%2Fworkbench%2Fdeploy-notebook%3Fdownload_url%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fapplied-ai-engineering-samples%2Fblob%2Fmain%2Fgenai-on-vertex-ai%2Fvertex_ai_extensions%2Fnotebooks%2Fgame_review_analysis_vertexai_extensions.ipynb)



## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Vertex AI API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com&redirect=https%3A//console.cloud.google.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Vertex AI API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com&redirect=https%3A//console.cloud.google.com)




## Register and run the Agent Search extension

The following sections show you how to register the Agent Search extension using the Google Cloud console and the Vertex AI API. After registering the extension, you can run it using the Vertex AI API.

### Console

**Register the extension**

Perform the following steps to register the Agent Search extension using the Google Cloud console.

  1. In the Google Cloud console, go to the Vertex AI **Extensions** page.

[Go to Vertex AI Extensions](https://console.cloud.google.com/vertex-ai/extensions)

  2. Click **Create Extension**.

  3. In the **Create a new extension** dialog, fill in the following fields:

     * **Extension name:** Enter a name for your extension, such as "vertex_search_extension".
     * **Description:** (Optional) Enter an extension description, such as "A Vertex AI search extension".
     * **Extension type:** Select `Vertex AI search`.
  4. In the **OpenAPI Spec file** section that now appears, confirm that the following fields are set correctly:

     * **API name:** `vertex_ai_search`.
     * **API description:** `Performs search on user ingested data including website and unstructured data type...`
     * **Source:** `Cloud Storage`.
     * **OpenAPI Spec:** `vertex-extension-public/vertex_ai_search.yaml`.
     * **Authentication:** `Google service account`.
  5. In the **Runtime configurations** section, provide a serving configuration name. The serving configuration name is specified in the [vertexAiSearchRuntimeConfig](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1beta1/projects.locations.extensions#vertexaisearchruntimeconfig). It is formatted and completed as follows: `projects/PROJECT_ID/locations/global/collections/COLLECTION_NAME/engines/ENGINE/servingConfigs/SERVING_CONFIG`

     * Set COLLECTION_NAME to `default_collection`.
     * Set ENGINE to the application ID you received when you created your search application. To learn more, see [Create a search app for website data](https://docs.cloud.google.com/generative-ai-app-builder/docs/try-enterprise-search#create_a_search_app_for_website_data).
     * Set SERVING_CONFIG to `default_search`.
  6. Click **Create Extension**.




### REST

**Register the extension**

Submit an Vertex AI API [`extensions.import`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1beta1/projects.locations.extensions/import) request to register the Agent Search extension.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: The ID of your Google Cloud project.
  * REGION: A [Compute Engine region](https://docs.cloud.google.com/compute/docs/regions-zones#available).
  * DISPLAY_NAME: The [name](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1beta1/projects.locations.extensions#Extension.FIELDS.display_name) extension that is displayed to users, such as "my_search_extension".
  * DESCRIPTION: (Optional) The extension [description](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1beta1/projects.locations.extensions#Extension.FIELDS.description) that is displayed to users, such as "A search extension".
  * SERVICE_ACCOUNT: (Optional) The Vertex AI Search extension uses [GOOGLE_SERVICE_ACCOUNT_AUTH](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1beta1/projects.locations.extensions#AuthConfig.FIELDS.google_service_account_config) as shown in the sample request body. If you do not specify a service account, the extension uses the default [Vertex AI Extension Service Agent](https://docs.cloud.google.com/vertex-ai/docs/general/access-control#service-agents) service account. If you specify a different service account, grant the [`iam.serviceAccounts.getAccessToken`](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccounts.getAccessToken) permission to the Vertex AI Extension Service Agent service account on the specified service account.
  * SERVING_CONFIG_NAME: The serving configuration name is specified in the [vertexAiSearchRuntimeConfig](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1beta1/projects.locations.extensions#vertexaisearchruntimeconfig). It is formatted and completed as follows: ` projects/PROJECT_ID/locations/global/collections/COLLECTION_NAME/engines/ENGINE/servingConfigs/SERVING_CONFIG`. 
    * PROJECT_ID: The ID of your Google Cloud project.
    * Set COLLECTION_NAME to `default_collection`.
    * ENGINE: The application ID you received when you created your search application. To learn more, see [Create a search app for website data](https://docs.cloud.google.com/generative-ai-app-builder/docs/try-enterprise-search#create_a_search_app_for_website_data).
    * Set SERVING_CONFIG to `default_search`.



HTTP method and URL: 
    
    
    POST https://REGION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/REGION/extensions:import

Request JSON body: 
    
    
    {
      "displayName":"DISPLAY_NAME",
      "description":"DESCRIPTION",
      "manifest":{
        "name":"vertex_ai_search_tool",
        "description":"A Vertex AI Search tool",
        "apiSpec":{
          "openApiGcsUri":"gs://vertex-extension-public/vertex_ai_search.yaml"
        },
        "authConfig":{
          "authType":"GOOGLE_SERVICE_ACCOUNT_AUTH",
          "googleServiceAccountConfig":{
            "serviceAccount":"SERVICE_ACCOUNT"
          }
        }
      }
      "runtimeConfig": {
         "vertexAiSearchRuntimeConfig": {
            "servingConfigName": "SERVING_CONFIG_NAME",
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
         "https://REGION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/REGION/extensions:import"

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
        -Uri "https://REGION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/REGION/extensions:import" | Select-Object -Expand Content

**Run the extension**

You can submit an `execute` operation to the Vertex AI API to obtain meaningful results from your data store.

### Document search

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: The ID of your Google Cloud project.
  * REGION: A [Compute Engine region](https://docs.cloud.google.com/compute/docs/regions-zones#available).
  * EXTENSION_ID: The ID of your Vertex AI Search extension listed in the **Extension details** in the Google Cloud console.



HTTP method and URL: 
    
    
    POST https://REGION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/REGION/extensions/EXTENSION_ID:execute

Request JSON body: 
    
    
    {
      "operation_id":"search",
      "operation_params":{
        "query":"Housing affordability since 2010",
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
         "https://REGION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/REGION/extensions/EXTENSION_ID:execute"

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
        -Uri "https://REGION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/REGION/extensions/EXTENSION_ID:execute" | Select-Object -Expand Content

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
