---
url: https://docs.cloud.google.com/vision-ai/docs/manage-app/
title: Manage applications \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:27:08.343896+00:00
---

# Manage applications  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/manage-app/

Vertex AI Vision is deprecated as of June 15, 2026 and reaches End of Life on September 30, 2026. To migrate, see the [Cloud Vision API](https://docs.cloud.google.com/vision/docs), [Agent Platform serverless training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview), or [Agent Platform models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/vision-ai/docs/cloud-environment)



Send feedback 

#  Manage applications Stay organized with collections  Save and categorize content based on your preferences. 

After you [build](https://docs.cloud.google.com/vision-ai/docs/build-app) and [deploy](https://docs.cloud.google.com/vision-ai/docs/deploy-app) apps, you can manage these apps using the Google Cloud console or command line.

## Manage an application

## Update an app

#### Undeployed apps

Make any modifications to the app (such as adding or removing component nodes) ; Gemini Enterprise Agent Platform Vision will automatically store the changes.

#### Deployed apps

Changes to deployed apps are automatically stored to the Gemini Enterprise Agent Platform Vision server and the deployed application is not affected. To discard modifications, click the **Discard changes** button. To save changes, select **Update the application**. To apply these local changes to the application, undeploy the current application, then redeploy it.

## List apps

### REST

To list all apps in a project, send a GET request by using the [projects.locations.applications.list](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.applications/list) method.

Before using any of the request data, make the following replacements: 

  * PROJECT: Your Google Cloud [project ID or project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 



HTTP method and URL: 
    
    
    GET https://visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/applications

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/applications"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/applications" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "applications": [
        {
          "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/applications/test-application-1",
          "createTime": "2022-03-01T20:04:12.558371402Z",
          "updateTime": "2022-03-01T20:07:21.589713094Z",
          "displayName": "Test Application 1",
          "runtimeInfo": {
            "deployTime": "2022-03-01T20:07:21.460654Z"
          }
          "state": "DEPLOYED"
        },
        {
          "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/applications/test-application-2",
          "createTime": "2022-03-01T20:04:12.558371402Z",
          "updateTime": "2022-03-01T20:07:21.589713094Z",
          "displayName": "Test Application 2",
          "runtimeInfo": {
            "deployTime": "2022-03-01T20:07:21.460654Z"
          }
          "state": "DEPLOYED"
        },
      ]
    }
    

## What's next

  * Learn how to read app input data from an ingestion stream or analyzed model output data in [Read stream data](https://docs.cloud.google.com/vision-ai/docs/read-stream).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
