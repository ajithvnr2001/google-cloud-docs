---
url: https://docs.cloud.google.com/policy-intelligence/docs/configure-role-recommendations/
title: Configure role recommendation generation \u00a0|\u00a0 Policy Intelligence \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:46:49.351283+00:00
---

# Configure role recommendation generation  |  Policy Intelligence  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/policy-intelligence/docs/configure-role-recommendations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Policy Intelligence ](https://docs.cloud.google.com/policy-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/policy-intelligence/docs/overview)



Send feedback 

#  Configure role recommendation generation Stay organized with collections  Save and categorize content based on your preferences. 

By changing your IAM recommender configuration, you can customize how your role recommendations are generated. This page explains how to edit your configuration to change how quickly recommendations are generated for your project.

Though the IAM recommender generates role recommendations for a variety of resources, you can only edit how role recommendations are generated for projects.

## Before you begin

  * Enable the Recommender API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=recommender.googleapis.com&redirect=https%3A//console.cloud.google.com)

  * Understand [how the IAM recommender generates role recommendations](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview#how-recommender-works).
  * Install the [Google Cloud CLI](https://cloud.google.com/sdk/).



### Required roles

To get the permissions that you need to configure IAM role recommendations, ask your administrator to grant you the following IAM roles on the project whose IAM recommender you want to configure: 

  * View configuration details: IAM Recommender Viewer (roles/recommender.iamViewer) 
  * Modify your configuration: IAM Recommender Admin (roles/recommender.iamAdmin) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to configure IAM role recommendations. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to configure IAM role recommendations:

  * View configuration details: `recommender.iamPolicyRecommenderConfig.get`
  * Modify your configuration: `recommender.iamPolicyRecommenderConfig.update`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View your current configuration

View your current configuration to see how many days of permission usage data the IAM recommender waits before generating role recommendations.

You can view the configuration using the gcloud CLI or the REST API.

### gcloud

To get a project's IAM recommender configuration, use the `[gcloud beta recommender recommender-config describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/recommender/recommender-config/describe)` command. 

Before using any of the command data below, make the following replacements: 

  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.



Execute the [gcloud beta recommender recommender-config describe](https://docs.cloud.google.com/sdk/gcloud/reference/beta/recommender/recommender-config/describe) command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud beta recommender recommender-config describe \
    google.iam.policy.Recommender \
    --project="PROJECT_ID" \
    --location="global"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud beta recommender recommender-config describe `
    google.iam.policy.Recommender `
    --project="PROJECT_ID" `
    --location="global"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud beta recommender recommender-config describe ^
    google.iam.policy.Recommender ^
    --project="PROJECT_ID" ^
    --location="global"

The response contains the project's IAM recommender configuration. For example, it might look like the following: 
    
    
    etag: '"d3e779ee3f34f276"'
    name: projects/123456789012/locations/global/recommenders/google.iam.policy.Recommender/config
    recommenderGenerationConfig:
      params:
        minimum_observation_period: P90D
    revisionId: DEFAULT
    updateTime: '2022-10-02T22:57:33Z'
    

### REST

To get a project's IAM recommender configuration, use the Recommender API's `[projects.locations.recommenders.getConfig](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.recommenders/getConfig)` method. 

Before using any of the request data, make the following replacements: 

  * `PROJECT_NUMBER`: The numeric ID of your Google Cloud project.
  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.



HTTP method and URL: 
    
    
    GET https://recommender.googleapis.com/v1beta1/projects/PROJECT_NUMBER/locations/global/recommenders/google.iam.policy.Recommender/config

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         "https://recommender.googleapis.com/v1beta1/projects/PROJECT_NUMBER/locations/global/recommenders/google.iam.policy.Recommender/config"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://recommender.googleapis.com/v1beta1/projects/PROJECT_NUMBER/locations/global/recommenders/google.iam.policy.Recommender/config" | Select-Object -Expand Content

The response contains the project's IAM recommender configuration. For example, it might look like the following: 
    
    
    {
      "name": "projects/123456789012/locations/global/recommenders/google.iam.policy.Recommender/config",
      "recommenderGenerationConfig": {
        "params": {
          "minimum_observation_period": "P90D"
        }
      },
      "etag": "\"d3e779ee3f34f276\"",
      "updateTime": "2022-10-02T22:57:33Z",
      "revisionId": "DEFAULT"
    }
    

## Understand configuration details

The contents of a configuration depend on which recommender the configuration is for. IAM recommender configurations have the following components, not necessarily in this order:

  * `name`: The identifier for the configuration, in the form `projects/PROJECT_NUMBER/locations/global/recommenders/google.iam.policy.Recommender/config`.
  * `recommenderGenerationConfig`: The parameters that the IAM recommender uses when generating recommendations. This field contains the following parameters:

    * `minimum_observation_period`: The number of days of permission usage data that the IAM recommender needs to start generating role recommendations. If you get a project's IAM recommender configuration, and this field hasn't been set, its value is `0`.
  * `etag`: An identifier for the current state of a configuration, used to prevent concurrent updates. Each time the configuration changes, a new ETag value is assigned.

  * `updateTime`: The timestamp of the most recent time that the configuration was updated, in UTC format ([RFC 3339](https://tools.ietf.org/html/rfc3339)).

  * `revisionId`: Output only. An identifier for the current revision of the configuration. This value is updated every time the configuration is edited.




## Edit your configuration

Edit your configuration to change how quickly recommendations are generated for your project.

**Important:** If you set the minimum observation period to fewer than 90 days, you'll get recommendations sooner, but the accuracy of the recommendations might be affected.

### gcloud

To edit a project's IAM recommender configuration, use the `[gcloud beta recommender recommender-config update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/recommender/recommender-config/update)` command. 

Before using any of the command data below, make the following replacements: 

  * `OBSERVATION_PERIOD`: The minimum observation period that you want to set. Use one of the following values: `P30D` (30 days), `P60D` (60 days), or `P90D` (90 days). 
  * `ETAG`: The configuration's current etag, which you can find by getting the current configuration and copying the value of the response's `etag` field. 
  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.

Save the following content in a file called `request.json`: 
    
    {
      "params": {
        "minimum_observation_period": "OBSERVATION_PERIOD"
      }
    }

Execute the [gcloud beta recommender recommender-config update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/recommender/recommender-config/update) command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud beta recommender recommender-config update \
    google.iam.policy.Recommender \
    --etag="ETAG" \
    --project="PROJECT_ID" \
    --location="global" \
    --config-file="request.json"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud beta recommender recommender-config update `
    google.iam.policy.Recommender `
    --etag="ETAG" `
    --project="PROJECT_ID" `
    --location="global" `
    --config-file="request.json"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud beta recommender recommender-config update ^
    google.iam.policy.Recommender ^
    --etag="ETAG" ^
    --project="PROJECT_ID" ^
    --location="global" ^
    --config-file="request.json"

The response contains the updated configuration. For example, it might look like the following: 
    
    etag: '"2549af0942332910"'
    name: projects/123456789012/locations/global/recommenders/google.iam.policy.Recommender/config
    recommenderGenerationConfig:
      params:
        minimum_observation_period: P60D
    revisionId: 288c60eb
    updateTime: '2022-10-05T21:42:21.069170Z'
    




### REST

To edit a project's IAM recommender configuration, use the Recommender API's `[projects.locations.recommenders.updateConfig](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.recommenders/updateConfig)` method. 

Before using any of the request data, make the following replacements: 

  * `PROJECT_NUMBER`: The numeric ID of your Google Cloud project.
  * `OBSERVATION_PERIOD`: The minimum observation period that you want to set. Use one of the following values: `P30D` (30 days), `P60D` (60 days), or `P90D` (90 days). 
  * `ETAG`: The configuration's current etag, which you can find by getting the current configuration and copying the value of the response's `etag` field. Use backslashes to escape quotes, for example, `"\"df7308cca9719dcc\""`. 
  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.

HTTP method and URL: 
    
    PATCH https://recommender.googleapis.com/v1beta1/projects/PROJECT_NUMBER/locations/global/recommenders/google.iam.policy.Recommender/config

Request JSON body: 
    
    {
      "name": "projects/PROJECT_NUMBER/locations/global/recommenders/google.iam.policy.Recommender/config",
      "recommenderGenerationConfig": {
        "params": {
          "minimum_observation_period": "OBSERVATION_PERIOD"
        }
      },
      "etag": "ETAG"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://recommender.googleapis.com/v1beta1/projects/PROJECT_NUMBER/locations/global/recommenders/google.iam.policy.Recommender/config"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://recommender.googleapis.com/v1beta1/projects/PROJECT_NUMBER/locations/global/recommenders/google.iam.policy.Recommender/config" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.recommenders/updateConfig). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

The response contains the updated configuration. For example, it might look like the following: 
    
    {
      "name": "projects/123456789012/locations/global/recommenders/google.iam.policy.Recommender/config",
      "recommenderGenerationConfig": {
        "params": {
          "minimum_observation_period": "P60D"
        }
      },
      "etag": "\"2549af0942332910\"",
      "updateTime": "2022-10-05T21:26:52.127512Z",
      "revisionId": "b5fc0053"
    }
    




## What's next

  * [Review and apply role recommendations for projects, folders, and organizations](https://docs.cloud.google.com/policy-intelligence/docs/review-apply-role-recommendations).
  * [Review and apply your role recommendations for Cloud Storage buckets](https://docs.cloud.google.com/policy-intelligence/docs/review-apply-role-recommendations-buckets)
  * Learn more about [Recommender](https://docs.cloud.google.com/recommender/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
