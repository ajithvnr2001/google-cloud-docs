---
url: https://docs.cloud.google.com/vision-ai/docs/deploy-app/
title: Deploy and undeploy an application \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:54.476786+00:00
---

# Deploy and undeploy an application  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/deploy-app/

Vertex AI Vision is deprecated as of June 15, 2026 and reaches End of Life on September 30, 2026. To migrate, see the [Cloud Vision API](https://docs.cloud.google.com/vision/docs), [Agent Platform serverless training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview), or [Agent Platform models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/vision-ai/docs/cloud-environment)



Send feedback 

#  Deploy and undeploy an application Stay organized with collections  Save and categorize content based on your preferences. 

After you [create an app](https://docs.cloud.google.com/vision-ai/docs/build-app) you must deploy the app to be able to stream and analyze data.

## Deploy an application

After you have built an end-to-end application with all the necessary components, you must deploy the app to start using it.

### Console

  1. Open the **Applications** tab of the Gemini Enterprise Agent Platform Vision dashboard.

[Go to the Applications tab](https://console.cloud.google.com/ai/vision-ai/applications)

  2. Select **View app** next to the name of your application from the list.

  3. From the application graph builder page click the **Deploy** button.

  4. In the **Deploy application** menu that opens, select any options and click **Deploy**.

**Note:** For more information about the **Enable output streaming** option, see check_box_outline_blank [Enable live stream output](https://docs.cloud.google.com/vision-ai/docs/enable-stream-output). For more information about the **Enable monitoring for this application** option, see check_box_outline_blank [Enable and use app monitoring](https://docs.cloud.google.com/vision-ai/docs/monitor-app).

After deployment completes there will be green check marks next to the nodes.




### REST & CMD LINE

To deploy your application for use, send a POST request using the [projects.locations.applications.deploy](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.applications/deploy) method.

Before using any of the request data, make the following replacements: 

  * PROJECT: Your Google Cloud [project ID or project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * APPLICATION_ID: The ID of your target application.



HTTP method and URL: 
    
    
    POST https://visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/applications/APPLICATION_ID:deploy

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/applications/APPLICATION_ID:deploy"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/applications/APPLICATION_ID:deploy" | Select-Object -Expand Content

If successful, the request starts a long-running operation and returns a JSON object with the operation ID. 
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.visionai.v1.OperationMetadata",
        "createTime": "YYYY-MM-DDTHH:MM:SS.454506987Z",
        "target": "projects/PROJECT_ID/locations/LOCATION_ID/applications/APPLICATION_ID",
        "verb": "update",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      **"done": false**
    }
    

**Get operation status**

Use the operation ID in the response to get the status of the deploy request.

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * OPERATION_ID: The operation ID that is returned when you start a long-running operation. For example: 
    * projects/123456/locations/us-central1/[...]/operations/**OPERATION_ID**



HTTP method and URL: 
    
    
    GET https://visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/operations/OPERATION_ID

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/operations/OPERATION_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/operations/OPERATION_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.visionai.v1.OperationMetadata",
        "createTime": "2023-01-12T17:53:14.454506987Z",
        "endTime": "2023-01-12T17:53:22.979720545Z",
        "target": "projects/PROJECT_ID/locations/LOCATION_ID/applications/APPLICATION_NAME",
        "verb": "update",
        "statusMessage": "Instance Deployment Pending....",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      **"done": true,**
      "response": {
        "@type": "type.googleapis.com/google.cloud.visionai.v1.Application",
        "name": "projects/PROJECT_ID/locations/LOCATION_ID/applications/APPLICATION_NAME",
        "createTime": "2023-01-06T21:16:26.465867295Z",
        "updateTime": "2023-01-12T17:53:14.458441937Z",
        "displayName": "APPLICATION_NAME",
        "applicationConfigs": {
          "nodes": [
            {
              "name": "builtin-input-stream",
              "displayName": "Streams",
              "nodeConfig": {
                "videoStreamInputConfig": {}
              },
              "processor": "builtin:stream-input",
              "outputAllOutputChannelsToStream": false
            },
            {
              "name": "builtin-general-object-detector",
              "displayName": "Object detector",
              "nodeConfig": {
                "generalObjectDetectionConfig": {}
              },
              "processor": "builtin:general-object-detector",
              "parents": [
                {
                  "parentNode": "builtin-input-stream"
                }
              ],
              "outputAllOutputChannelsToStream": false
            },
            {
              "name": "builtin-media-warehouse",
              "displayName": "Vision AI Warehouse",
              "nodeConfig": {
                "mediaWarehouseConfig": {
                  "corpus": "projects/PROJECT_ID/locations/LOCATION_ID/corpora/CORPUS_ID"
                }
              },
              "processor": "builtin:media-warehouse",
              "parents": [
                {
                  "parentNode": "builtin-input-stream"
                },
                {
                  "parentNode": "builtin-general-object-detector"
                }
              ],
              "outputAllOutputChannelsToStream": false
            }
          ]
        },
        "runtimeInfo": {
          "deployTime": "2023-01-12T17:53:22.887918Z",
          "globalOutputResources": [
            {
              "outputResource": "projects/PROJECT_ID/locations/LOCATION_ID/corpora/CORPUS_ID/dataSchemas/stream-resource-name",
              "key": "stream-resource-name"
            },
            {
              "outputResource": "projects/PROJECT_ID/locations/LOCATION_ID/corpora/CORPUS_ID/dataSchemas/stream-display-name",
              "key": "stream-display-name"
            },
            {
              "outputResource": "projects/PROJECT_ID/locations/LOCATION_ID/corpora/CORPUS_ID/dataSchemas/stream-resource-id",
              "key": "stream-resource-id"
            },
            {
              "outputResource": "projects/PROJECT_ID/locations/LOCATION_ID/corpora/CORPUS_ID/dataSchemas/general-object-detection",
              "producerNode": "builtin-general-object-detector",
              "key": "general_object_detection_data_schema_id"
            }
          ]
        },
        **"state": "DEPLOYED",**
        "deploymentEnvironment": "DEPLOYMENT_ENVIRONMENT_CLOUD"
      }
    }
    

## Undeploy an application

To stop using an app, you must undeploy the application.

### Console

  1. Open the **Applications** tab of the Gemini Enterprise Agent Platform Vision dashboard.

[Go to the Applications tab](https://console.cloud.google.com/ai/vision-ai/applications)

  2. Select **View app** next to the name of your application from the list.

  3. From the application graph builder page click the **Deactivate** button.




### REST & CMD LINE

To undeploy your application, send a POST request using the [projects.locations.applications.undeploy](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1/projects.locations.applications/undeploy) method.

Before using any of the request data, make the following replacements: 

  * PROJECT: Your Google Cloud [project ID or project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * APPLICATION_ID: The ID of your target application.



HTTP method and URL: 
    
    
    POST https://visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/applications/APPLICATION_ID:undeploy

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/applications/APPLICATION_ID:undeploy"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/applications/APPLICATION_ID:undeploy" | Select-Object -Expand Content

If successful, the request starts a long-running operation and returns a JSON object with the operation ID. 
    
    
    {
      "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.visionai.v1.OperationMetadata",
        "createTime": "2023-01-12T18:14:48.260296926Z",
        "target": "projects/PROJECT_NUMBER/locations/LOCATION_ID/applications/APPLICATION_NAME",
        "verb": "update",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      **"done": false**
    }
    

**Get operation status**

Use the operation ID in the response to get the status of the undeploy request.

Before using any of the request data, make the following replacements: 

  * REGIONALIZED_ENDPOINT: Endpoint might include a prefix matching the `LOCATION_ID` such as `europe-west4-`. See more about [ regionalized endpoints](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * PROJECT_NUMBER: Your Google Cloud [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). 
  * LOCATION_ID: The [region](https://cloud.google.com/about/locations) where you are using Agent Platform Vision. For example: `us-central1`, `europe-west4`. See [available regions](https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions). 
  * OPERATION_ID: The operation ID that is returned when you start a long-running operation. For example: 
    * projects/123456/locations/us-central1/[...]/operations/**OPERATION_ID**



HTTP method and URL: 
    
    
    GET https://visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/operations/OPERATION_ID

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/operations/OPERATION_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://visionai.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID/operations/OPERATION_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.visionai.v1.OperationMetadata",
        "createTime": "2023-01-12T18:14:48.260296926Z",
        "endTime": "2023-01-12T18:14:58.059563424Z",
        "target": "projects/PROJECT_ID/locations/LOCATION_ID/applications/APPLICATION_NAME",
        "verb": "update",
        "statusMessage": "Instance Undeployment Pending....",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      **"done": true,**
      "response": {
        "@type": "type.googleapis.com/google.cloud.visionai.v1.Application",
        "name": "projects/PROJECT_ID/locations/LOCATION_ID/applications/APPLICATION_NAME",
        "createTime": "2023-01-06T21:16:26.465867295Z",
        "updateTime": "2023-01-12T18:14:48.264089325Z",
        "displayName": "APPLICATION_NAME",
        "applicationConfigs": {
          "nodes": [
            {
              "name": "builtin-input-stream",
              "displayName": "Streams",
              "nodeConfig": {
                "videoStreamInputConfig": {}
              },
              "processor": "builtin:stream-input",
              "outputAllOutputChannelsToStream": false
            },
            {
              "name": "builtin-general-object-detector",
              "displayName": "Object detector",
              "nodeConfig": {
                "generalObjectDetectionConfig": {}
              },
              "processor": "builtin:general-object-detector",
              "parents": [
                {
                  "parentNode": "builtin-input-stream"
                }
              ],
              "outputAllOutputChannelsToStream": false
            },
            {
              "name": "builtin-media-warehouse",
              "displayName": "Vision AI Warehouse",
              "nodeConfig": {
                "mediaWarehouseConfig": {
                  "corpus": "projects/PROJECT_ID/locations/LOCATION_ID/corpora/CORPUS_ID"
                }
              },
              "processor": "builtin:media-warehouse",
              "parents": [
                {
                  "parentNode": "builtin-input-stream"
                },
                {
                  "parentNode": "builtin-general-object-detector"
                }
              ],
              "outputAllOutputChannelsToStream": false
            }
          ]
        },
        "state": "CREATED",
        "deploymentEnvironment": "DEPLOYMENT_ENVIRONMENT_CLOUD"
      }
    }
    

## What's next

  * Read instructions about how to begin data ingestion from an app's input stream in [Create and manage streams](https://docs.cloud.google.com/vision-ai/docs/create-manage-streams#ingest-videos).
  * Learn how to list apps and view a deployed app's instances in [Managing applications](https://docs.cloud.google.com/vision-ai/docs/manage-app).
  * Learn how to read app input data from an ingestion stream or analyzed model output data in [Read stream data](https://docs.cloud.google.com/vision-ai/docs/read-stream).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
