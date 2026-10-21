---
url: https://docs.cloud.google.com/colab/docs/manage-runtimes/
title: Manage Colab Enterprise runtimes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:30:21.611195+00:00
---

# Manage Colab Enterprise runtimes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/colab/docs/manage-runtimes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Colab Enterprise ](https://docs.cloud.google.com/colab/docs)
  * [ Guides ](https://docs.cloud.google.com/colab/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage runtimes

This page describes how to manage a Colab Enterprise runtime, including the following tasks:

  * Start a runtime.
  * Stop a runtime.
  * Disconnect from a runtime.
  * Reconnect to a runtime.
  * Change the runtime that you are connected to.
  * Delete a runtime.



## Required roles

To get the permissions that you need to manage a Colab Enterprise runtime, ask your administrator to grant you the Colab Enterprise User ([`roles/aiplatform.colabEnterpriseUser`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/access-control#aiplatform.colabEnterpriseUser)) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

One or more of the required roles includes the `dataform.repositories.list` permission. Users who are granted the `dataform.repositories.list` permission or the [Code Creator (`roles/dataform.codeCreator`)](https://docs.cloud.google.com/dataform/docs/access-control#dataform.codeCreator) role in a project can list the names of code assets in that project by using the Dataform API or the Dataform command-line interface (CLI). Non-administrators using BigQuery Studio can only see code assets that they created or that were shared with them. 

## Start a runtime

To start a runtime, you can use the Google Cloud console, the gcloud CLI, or the REST API.

### Console

To start a runtime:

  1. In the Google Cloud console, go to the Colab Enterprise **Runtimes** page. 

[Go to Runtimes](https://console.cloud.google.com/agent-platform/colab/runtimes)

  2. In the **Region** menu, select the region that contains your runtime. 

  3. Select the runtime that you want to start.

  4. Click **Start**.




### gcloud

Before using any of the command data below, make the following replacements: 

  * `RUNTIME_ID`: the ID of your runtime.
  * `PROJECT_ID`: your project ID.
  * `REGION`: the region where your runtime is located.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud colab runtimes start RUNTIME_ID \
        --project=PROJECT_ID \
        --region=REGION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud colab runtimes start RUNTIME_ID `
        --project=PROJECT_ID `
        --region=REGION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud colab runtimes start RUNTIME_ID ^
        --project=PROJECT_ID ^
        --region=REGION

For more information about the command for starting a runtime from the command line, see the [gcloud CLI documentation](https://docs.cloud.google.com/sdk/gcloud/reference/colab/runtimes/start). 

### REST

Before using any of the request data, make the following replacements: 

  * `REGION`: the region where your runtime is located.
  * `PROJECT_ID`: your project ID.
  * `RUNTIME_ID`: the ID of your runtime.



HTTP method and URL: 
    
    
    POST https://REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/notebookRuntimes/RUNTIME_ID:start

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/notebookRuntimes/RUNTIME_ID:start"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/notebookRuntimes/RUNTIME_ID:start" | Select-Object -Expand Content

If successful, the response body contains an instance of [Operation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ListOperationsResponse#Operation). 

For more information, see the [`notebookRuntimes.start` REST API documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.notebookRuntimes/start). 

## Stop a runtime

To stop a runtime, you can use the gcloud CLI or the REST API.

### gcloud

Before using any of the command data below, make the following replacements: 

  * `RUNTIME_ID`: the ID of your runtime.
  * `PROJECT_ID`: your project ID.
  * `REGION`: the region where your runtime is located.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud colab runtimes stop RUNTIME_ID \
        --project=PROJECT_ID \
        --region=REGION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud colab runtimes stop RUNTIME_ID `
        --project=PROJECT_ID `
        --region=REGION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud colab runtimes stop RUNTIME_ID ^
        --project=PROJECT_ID ^
        --region=REGION

For more information about the command for stopping a runtime from the command line, see the [gcloud CLI documentation](https://docs.cloud.google.com/sdk/gcloud/reference/colab/runtimes/stop). 

### REST

Before using any of the request data, make the following replacements: 

  * `REGION`: the region where your runtime is located.
  * `PROJECT_ID`: your project ID.
  * `RUNTIME_ID`: the ID of your runtime.



HTTP method and URL: 
    
    
    POST https://REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/notebookRuntimes/RUNTIME_ID:start

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/notebookRuntimes/RUNTIME_ID:start"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/notebookRuntimes/RUNTIME_ID:start" | Select-Object -Expand Content

If successful, the response body contains an instance of [Operation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ListOperationsResponse#Operation). 

For more information, see the [`notebookRuntimes.stop` REST API documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.notebookRuntimes/stop). 

## Disconnect from a runtime

To disconnect from a runtime:

  1. In the Google Cloud console, go to the Colab Enterprise **My notebooks** page. 

[Go to My notebooks](https://console.cloud.google.com/agent-platform/colab/notebooks)

  2. In the **Region** menu, select the region that contains your notebook.

  3. Open the notebook that you want to disconnect from the runtime.

  4. In the header toolbar, click **Runtime** > **Manage sessions**. If you don't see the header toolbar, click arrow_drop_down **Toggle header visibility**. 

  5. In the **Active sessions** pane, click the ![](https://docs.cloud.google.com/static/colab/images/icon-end-session.png) **End session** button. 

  6. Click **Terminate**.




## Reconnect to a runtime

To reconnect to a runtime:

  1. In the Google Cloud console, go to the Colab Enterprise **My notebooks** page. 

[Go to My notebooks](https://console.cloud.google.com/agent-platform/colab/notebooks)

  2. In the **Region** menu, select the region that contains your notebook.

  3. Open a notebook that was recently disconnected from a runtime.

  4. In the top right corner of the notebook, click **Reconnect**. 

If the runtime that the notebook was previously connected to is still running, Colab Enterprise connects to it. If that runtime isn't running anymore, it connects to the default runtime. 




## Change the runtime

To change the runtime that you are connected to:

  1. In the Google Cloud console, go to the Colab Enterprise **My notebooks** page. 

[Go to My notebooks](https://console.cloud.google.com/agent-platform/colab/notebooks)

  2. In the **Region** menu, select the region that contains your notebook.

  3. Open a notebook that is connected to a runtime.

  4. In the top right corner of the notebook, click arrow_drop_down **Additional connection options** > **Change runtime type**. 

  5. Complete the dialog to [connect to a runtime](https://docs.cloud.google.com/colab/docs/connect-to-runtime). 




## Delete a runtime

To delete a runtime, you can use the Google Cloud console, the gcloud CLI, or the REST API.

### Console

To delete a runtime:

  1. In the Google Cloud console, go to the Colab Enterprise **Runtimes** page. 

[Go to Runtimes](https://console.cloud.google.com/agent-platform/colab/runtimes)

  2. In the **Region** menu, select the region that contains your runtime. 

  3. Select the runtime that you want to delete.

  4. Click delete **Delete**.

  5. Click **Confirm**.




### gcloud

Before using any of the command data below, make the following replacements: 

  * `RUNTIME_ID`: the ID of your runtime.
  * `PROJECT_ID`: your project ID.
  * `REGION`: the region where your runtime is located.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud colab runtimes delete RUNTIME_ID \
        --project=PROJECT_ID \
        --region=REGION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud colab runtimes delete RUNTIME_ID `
        --project=PROJECT_ID `
        --region=REGION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud colab runtimes delete RUNTIME_ID ^
        --project=PROJECT_ID ^
        --region=REGION

For more information about the command for deleting a runtime from the command line, see the [gcloud CLI documentation](https://docs.cloud.google.com/sdk/gcloud/reference/colab/runtimes/delete). 

### REST

Before using any of the request data, make the following replacements: 

  * `REGION`: the region where your runtime is located.
  * `PROJECT_ID`: your project ID.
  * `RUNTIME_ID`: the ID of your runtime.



HTTP method and URL: 
    
    
    DELETE https://REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/notebookRuntimes/RUNTIME_ID

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/notebookRuntimes/RUNTIME_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/notebookRuntimes/RUNTIME_ID" | Select-Object -Expand Content

If successful, the response body contains an instance of [Operation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ListOperationsResponse#Operation). 

For more information, see the [`notebookRuntimes.delete` REST API documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.notebookRuntimes/delete). 

## What's next

  * Learn more about [runtimes and runtime templates](https://docs.cloud.google.com/colab/docs/runtimes).
  * [Create a runtime template](https://docs.cloud.google.com/colab/docs/create-runtime-template).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
