---
url: https://docs.cloud.google.com/colab/docs/post-startup-script/
title: Use a post-startup script in Colab Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:50.065298+00:00
---

# Use a post-startup script in Colab Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/colab/docs/post-startup-script/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Colab Enterprise ](https://docs.cloud.google.com/colab/docs)
  * [ Guides ](https://docs.cloud.google.com/colab/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use a post-startup script

This guide describes how to use a post-startup script with Colab Enterprise. This guide also describes how to set environment variables for use with your post-startup script.

## Overview

You can use a post-startup script to perform tasks after the startup process of your Colab Enterprise runtime. For example, you can use a post-startup script to install specific packages or make specific changes to your runtime's VM.

To use a post-startup script in Colab Enterprise, you specify the post-startup script when you create a runtime template. Then, when you create a runtime based on that runtime template, the post-startup script runs at the end of the startup process.

### Post-startup script location

Your post-startup script URI can be any of the following:

  * **A Cloud Storage URI** : For example, `gs://BUCKET_NAME/SCRIPT_FILE_NAME`. If your post-startup script is stored in Cloud Storage, you must use a runtime with end-user credentials enabled. This is because Colab Enterprise uses your user credentials to access the Cloud Storage bucket.
  * **An HTTPS URL** : For example, `https://example.com/FOLDER_NAME/SCRIPT_FILE_NAME`. Using an HTTPS URL isn't supported when creating your runtime template by using the Google Cloud console.



### Post-startup script behavior

You can specify the behavior of your post-startup script. See the following table:

Behavior | Description  
---|---  
Run once (`RUN_ONCE`) |  Default. Colab Enterprise runs the post-startup script only once, during runtime creation.   
Run every start (`RUN_EVERY_START`) |  After every start, Colab Enterprise runs the post-startup script. For example, if idle shutdown stops the runtime, Colab Enterprise runs the post-startup script again when the runtime is restarted.   
Download and run every start (`DOWNLOAD_AND_RUN_EVERY_START`) |  After every start, Colab Enterprise re-downloads the post-startup script from its source, and then runs the script.   
  
### Environment variables

You can specify environment variables in your runtime template, and refer to those variables in your post-startup script.

For example, you can [set the quota project using an environment variable](https://docs.cloud.google.com/docs/quotas/set-quota-project#set-project-variable). You might set your quota project to a specific project ID by using `GOOGLE_CLOUD_QUOTA_PROJECT`, a common variable used in Google Cloud client libraries.

To use a post-startup script with environment variables, see Create a runtime template with a post-startup script and environment variables.

### Track changes to and recover post-startup scripts

To track changes to your post-startup script and enable recovery of a specific version of the post-startup script, store your post-startup script in a Cloud Storage bucket with Object Versioning enabled. Object Versioning preserves deleted objects as versioned, noncurrent objects that remain accessible in your bucket until explicitly removed.

To specify a version of your post-startup script, add `#GENERATION_NUMBER` to your post-startup script's URI when you create your runtime template, for example, `gs://BUCKET_NAME/FOLDER_NAME/FILE_NAME.py#GENERATION_NUMBER`. For more information about Object Versioning and generation numbers, see [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning).

When you use the Google Cloud console to create your runtime template, specifying a generation number for your post-startup script isn't supported.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Agent Platform, Dataform, and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com,dataform.googleapis.com,compute.googleapis.com&redirect=https%3A//console.cloud.google.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Agent Platform, Dataform, and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com,dataform.googleapis.com,compute.googleapis.com&redirect=https%3A//console.cloud.google.com)




### Required roles

To get the permissions that you need to create a runtime template in Colab Enterprise, ask your administrator to grant you the Colab Enterprise Admin ([`roles/aiplatform.colabEnterpriseAdmin`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/access-control#aiplatform.colabEnterpriseAdmin)) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

One or more of the required roles includes the `dataform.repositories.list` permission. Users who are granted the `dataform.repositories.list` permission or the [Code Creator (`roles/dataform.codeCreator`)](https://docs.cloud.google.com/dataform/docs/access-control#dataform.codeCreator) role in a project can list the names of code assets in that project by using the Dataform API or the Dataform command-line interface (CLI). Non-administrators using BigQuery Studio can only see code assets that they created or that were shared with them. 

## Create a runtime template that uses a post-startup script

To create a runtime template that uses a post-startup script, you can use the Google Cloud console, the Google Cloud CLI, or the REST API.

### Console

To create a runtime template that uses a post-startup script, do the following: 

  1. In the Google Cloud console, go to the Colab Enterprise **Runtime templates** page. 

[Go to Runtime templates](https://console.cloud.google.com/agent-platform/colab/runtime-templates)

  2. Click add_box **New template**. 

The **Create new runtime template** dialog appears.

  3. In the **Runtime basics** section, enter a **Display name**. 

  4. In the **Region** menu, select the region where you want your runtime template. 

  5. In the **Environment** section, in the **Post-startup script** field, click **Browse** , and then navigate to a post-startup script located in Cloud Storage. For more information, see Post-startup script location. 

  6. Under the post-startup script URL, select your post-startup script's behavior. The default behavior is **Run once**. For more information, see Post-startup script behavior. 

  7. In the **Networking and security** section, make sure that **Enable end-user credentials** is selected. 

  8. Complete the rest of the dialog, and then click **Create**. 

Your runtime template appears in the list on the **Runtime templates** tab. 




### gcloud

Before using any of the command data below, make the following replacements: 

  * `DISPLAY_NAME`: the display name of your runtime template.
  * `PROJECT_ID`: your project ID.
  * `REGION`: the region where you want your runtime template.
  * `POST_STARTUP_SCRIPT_URI`: the URI for your post-startup script. For more information, see [Post-startup script location](https://docs.cloud.google.com/colab/docs/post-startup-script#location). 
  * `POST_STARTUP_SCRIPT_BEHAVIOR`: the behavior of the post-startup script. See [Post-startup script behavior](https://docs.cloud.google.com/colab/docs/post-startup-script#behavior). 



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud colab runtime-templates create --display-name="DISPLAY_NAME" \
        --project=PROJECT_ID \
        --region=REGION \
        --machine-type=e2-standard-4 \
        --post-startup-script-url=POST_STARTUP_SCRIPT_URI \
        --post-startup-script-behavior=POST_STARTUP_SCRIPT_BEHAVIOR

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud colab runtime-templates create --display-name="DISPLAY_NAME" `
        --project=PROJECT_ID `
        --region=REGION `
        --machine-type=e2-standard-4 `
        --post-startup-script-url=POST_STARTUP_SCRIPT_URI `
        --post-startup-script-behavior=POST_STARTUP_SCRIPT_BEHAVIOR

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud colab runtime-templates create --display-name="DISPLAY_NAME" ^
        --project=PROJECT_ID ^
        --region=REGION ^
        --machine-type=e2-standard-4 ^
        --post-startup-script-url=POST_STARTUP_SCRIPT_URI ^
        --post-startup-script-behavior=POST_STARTUP_SCRIPT_BEHAVIOR

For more information about the command for creating a runtime template from the command line, see the [gcloud CLI documentation](https://docs.cloud.google.com/sdk/gcloud/reference/colab/runtime-templates/create). 

### REST

Before using any of the request data, make the following replacements: 

  * `REGION`: the region where you want your runtime template.
  * `PROJECT_ID`: your project ID.
  * `DISPLAY_NAME`: the display name of your runtime template.
  * `POST_STARTUP_SCRIPT_URI`: the URI for your post-startup script. For more information, see [Post-startup script location](https://docs.cloud.google.com/colab/docs/post-startup-script#location). 
  * `POST_STARTUP_SCRIPT_BEHAVIOR`: the behavior of the post-startup script. See [Post-startup script behavior](https://docs.cloud.google.com/colab/docs/post-startup-script#behavior). 



HTTP method and URL: 
    
    
    POST https://REGION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/REGION/notebookRuntimeTemplates

Request JSON body: 
    
    
    {
      "displayName": "DISPLAY_NAME",
      "machineSpec": {
        "machineType": "e2-standard-4"
      },
      softwareConfig: {
        postStartupScriptConfig: {
          postStartupScriptUrl: "POST_STARTUP_SCRIPT_URI",
          postStartupScriptBehavior: "POST_STARTUP_SCRIPT_BEHAVIOR"
        },
      },
      "networkSpec": {
        "enableInternetAccess": true
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
         "https://REGION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/REGION/notebookRuntimeTemplates"

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
        -Uri "https://REGION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/REGION/notebookRuntimeTemplates" | Select-Object -Expand Content

If successful, the response body contains an instance of [Operation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ListOperationsResponse#Operation). 

For more information, see the [`notebookRuntimeTemplates.create` REST API documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.notebookRuntimeTemplates/create). 

### Create the runtime

After you create a runtime template that uses your post-startup script, create a runtime based on that runtime template. The runtime starts, and the post-startup script runs according to the specified behavior. See [Create a runtime](https://docs.cloud.google.com/colab/docs/create-runtime).

**Note:** To create a runtime based on a runtime template that includes a post-startup script, you must be the owner and creator of that runtime template.

## Create a runtime template with a post-startup script and environment variables

To create a runtime template that uses a post-startup script and environment variables, you can use the Google Cloud console, the Google Cloud CLI, or the REST API.

### Console

To create a runtime template that uses a post-startup script and environment variables, do the following: 

  1. In the Google Cloud console, go to the Colab Enterprise **Runtime templates** page. 

[Go to Runtime templates](https://console.cloud.google.com/agent-platform/colab/runtime-templates)

  2. Click add_box **New template**. 

The **Create new runtime template** dialog appears.

  3. In the **Runtime basics** section, enter a **Display name**. 

  4. In the **Region** menu, select the region where you want your runtime template. 

  5. In the **Environment** section, in the **Post-startup script** field, click **Browse** , and then navigate to a post-startup script located in Cloud Storage. For more information, see Post-startup script location. 

  6. Under the post-startup script URL, select your post-startup script's behavior. The default behavior is **Run once**. For more information, see [Post-startup script behavior](https://docs.cloud.google.com/colab/docs/post-startup-script#behavior). 

  7. To add an environment variable, click add **Add env variable** , and then enter a **Key** and **Value** pair. To add more environment variables, repeat this step. 

  8. In the **Networking and security** section, make sure that **Enable end-user credentials** is selected. 

  9. Complete the rest of the dialog, and then click **Create**. 

Your runtime template appears in the list on the **Runtime templates** tab. 




### gcloud

Before using any of the command data below, make the following replacements: 

  * `DISPLAY_NAME`: the display name of your runtime template.
  * `PROJECT_ID`: your project ID.
  * `REGION`: the region where you want your runtime template.
  * `POST_STARTUP_SCRIPT_URI`: the URI for your post-startup script. For more information, see [Post-startup script location](https://docs.cloud.google.com/colab/docs/post-startup-script#location). 
  * `POST_STARTUP_SCRIPT_BEHAVIOR`: the behavior of the post-startup script. See [Post-startup script behavior](https://docs.cloud.google.com/colab/docs/post-startup-script#behavior). 
  * `ENV_VARIABLE_NAME`: the name of an environment variable to set for your runtime. 
  * `ENV_VARIABLE_VALUE`: the value of the environment variable to set for your runtime. 



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud colab runtime-templates create --display-name="DISPLAY_NAME" \
        --project=PROJECT_ID \
        --region=REGION \
        --machine-type=e2-standard-4 \
        --post-startup-script-url=POST_STARTUP_SCRIPT_URI \
        --post-startup-script-behavior=POST_STARTUP_SCRIPT_BEHAVIOR \
        --set-env-vars=ENV_VARIABLE_NAME=ENV_VARIABLE_VALUE

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud colab runtime-templates create --display-name="DISPLAY_NAME" `
        --project=PROJECT_ID `
        --region=REGION `
        --machine-type=e2-standard-4 `
        --post-startup-script-url=POST_STARTUP_SCRIPT_URI `
        --post-startup-script-behavior=POST_STARTUP_SCRIPT_BEHAVIOR `
        --set-env-vars=ENV_VARIABLE_NAME=ENV_VARIABLE_VALUE

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud colab runtime-templates create --display-name="DISPLAY_NAME" ^
        --project=PROJECT_ID ^
        --region=REGION ^
        --machine-type=e2-standard-4 ^
        --post-startup-script-url=POST_STARTUP_SCRIPT_URI ^
        --post-startup-script-behavior=POST_STARTUP_SCRIPT_BEHAVIOR ^
        --set-env-vars=ENV_VARIABLE_NAME=ENV_VARIABLE_VALUE

For more information about the command for creating a runtime template from the command line, see the [gcloud CLI documentation](https://docs.cloud.google.com/sdk/gcloud/reference/colab/runtime-templates/create). 

### REST

Before using any of the request data, make the following replacements: 

  * `REGION`: the region where you want your runtime template.
  * `PROJECT_ID`: your project ID.
  * `DISPLAY_NAME`: the display name of your runtime template.
  * `POST_STARTUP_SCRIPT_URI`: the URI for your post-startup script. For more information, see [Post-startup script location](https://docs.cloud.google.com/colab/docs/post-startup-script#location). 
  * `POST_STARTUP_SCRIPT_BEHAVIOR`: the behavior of the post-startup script. See [Post-startup script behavior](https://docs.cloud.google.com/colab/docs/post-startup-script#behavior). 
  * `ENV_VARIABLE_NAME`: the name of an environment variable to set for your runtime. 
  * `ENV_VARIABLE_VALUE`: the value of the environment variable to set for your runtime. 



HTTP method and URL: 
    
    
    POST https://REGION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/REGION/notebookRuntimeTemplates

Request JSON body: 
    
    
    {
      "displayName": "DISPLAY_NAME",
      "machineSpec": {
        "machineType": "e2-standard-4"
      },
      softwareConfig: {
        postStartupScriptConfig: {
          postStartupScriptUrl: "POST_STARTUP_SCRIPT_URI",
          postStartupScriptBehavior: "POST_STARTUP_SCRIPT_BEHAVIOR"
        },
        "env": [
          {
            "name": "ENV_VARIABLE_NAME",
            "value": "ENV_VARIABLE_VALUE"
          }
        ]
      },
      "networkSpec": {
        "enableInternetAccess": true
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
         "https://REGION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/REGION/notebookRuntimeTemplates"

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
        -Uri "https://REGION-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/REGION/notebookRuntimeTemplates" | Select-Object -Expand Content

If successful, the response body contains an instance of [Operation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ListOperationsResponse#Operation). 

For more information, see the [`notebookRuntimeTemplates.create` REST API documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.notebookRuntimeTemplates/create). 

### Create the runtime

After you create a runtime template that uses your post-startup script, create a runtime based on that runtime template. The runtime starts, and the post-startup script runs according to the specified behavior. See [Create a runtime](https://docs.cloud.google.com/colab/docs/create-runtime).

**Note:** To create a runtime based on a runtime template that includes a post-startup script, you must be the owner and creator of that runtime template.

## Best practices

Consider the following best practices when using post-startup scripts with Colab Enterprise:

  * **Control access to runtime templates** : To prevent unwanted changes to your post-startup script configuration, use IAM roles and permissions to control who can create and update runtime templates.
  * **Control access to the script** : To prevent unwanted changes to your post-startup script file, use IAM roles and permissions to control access to the Cloud Storage bucket where the script is stored.
  * **Use object versioning** : To track changes to your post-startup script and make sure that your runtime template uses a specific version of the script, store your post-startup script in a Cloud Storage bucket with [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning) enabled. Then include the generation number in the script path when you create the runtime template. For example: `gs://BUCKET_NAME/OBJECT_NAME1#GENERATION_NUMBER1`. For more information, see Track changes to and recover post-startup scripts.
  * **Prevent data exfiltration** : If your organization requires it, you can use [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) to help prevent data exfiltration.



## Limitations

Consider the following limitations when using post-startup scripts with Colab Enterprise:

  * To create a runtime based on a runtime template that includes a post-startup script and EUC enabled, you must be the owner of that runtime. For example, an administrator can't use the REST API to create a runtime that uses a post-startup script for another user.
  * Passing environment variables through the post-startup script isn't supported. You must specify environment variables in the software configuration as described in this guide.
  * To use a post-startup script located in Cloud Storage, you must use a runtime with end-user credentials enabled and your user credentials must have access to the Cloud Storage bucket.
  * If you use the Google Cloud console to create your runtime template, your post-startup script must be located in Cloud Storage. Post-startup scripts in other locations aren't supported when creating your runtime template by using the Google Cloud console.
  * Specifying a generation number for your post-startup script isn't supported when you use the Google Cloud console to create your runtime template.



## What's next

  * [Create a runtime and connect to it](https://docs.cloud.google.com/colab/docs/connect-to-runtime#connect-create).
  * To manage your runtime, see [Manage runtimes](https://docs.cloud.google.com/colab/docs/manage-runtimes).
  * Learn more about [runtimes and runtime templates](https://docs.cloud.google.com/colab/docs/runtimes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
