---
url: https://docs.cloud.google.com/application-integration/docs/upload-download-integrations/
title: Upload and download integrations \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:39:05.099826+00:00
---

# Upload and download integrations  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/upload-download-integrations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Upload and download integrations

You can download your integrations as a JSON file and save it in your local system. As a result, your entire integration is available in a file, which you can directly upload in another integration project without any modifications. [Uploading an integration](https://docs.cloud.google.com/application-integration/docs/create-integrations#upload-an-integration) creates a new version of the integration in the project where the file is uploaded. 

Having an entire integration in a file format provides you with the following advantages: 

  * You can copy your integration from one project to another without much effort.
  * You can programmatically update the integration file for repetitive changes, such as renaming of tasks or dynamically modifying variable names.

**Note:** Details of authentication profiles configured for an integration is not available in the downloaded file. After uploading the integration file, you must re-configure the authentication profiles in the uploaded integration.

## Download an integration

To download an integration, select one of the following optionss:

### Console

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. Click **Integrations** from the left navigation menu to open the **Integrations** page. 
  3. Select an existing integration. This opens the integration in the _integration editor_. 
  4. Click the **Versions** dropdown and select the version you want to download.
  5. In the designer toolbar, click  more_vert  (Actions menu) and select **Download**. 

The INTEGRATION_NAME.json file is automatically saved in your web browser's default download folder.


**Note:** The downloaded JSON file will have the structure of [`DownloadIntegrationVersionResponse`](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/DownloadIntegrationVersionResponse) type. If you modify the JSON file, ensure that the modified file adheres to the `DownloadIntegrationVersionResponse` structure.

### API

To download an integration, issue a `GET` request to the following API: GET https://integrations.googleapis.com/v1/projects/*/locations/*/integrations/*/versions/*:download 
    
    
    https://integrations.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/integrations/INTEGRATION_NAME/versions/INTEGRATION_VERSION:download
    

The following example shows you how to download a specific version of an integration:
    
    
    curl -v -s \
    -H "Content-Type: application/json" -H "Authorization: Bearer $TOKEN" \
    -H "X-GFE-SSL: yes" \
    -X GET "https://integrations.googleapis.com/v1/projects/demo-project/locations/us-east1/integrations/test-integration/versions/0e90d453-5fcf-4aae-b164-2e8344d1ac11:download"
    

**Note:** In the previous example, the integration version number is `0e90d453-5fcf-4aae-b164-2e8344d1ac11`. To get the integration version, open the required version of the integration in the UI and copy the auto-generated unique ID string after `../integrations/integration/INTEGRATION_NAME/` from the URL.

For more information, see [`projects.locations.integrations.versions.download`](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations.versions/download).

## Upload an integration

Uploading an integration creates a new version of the integration in the project where the file is uploaded. For example, if you have an integration by name `IP-Test` at version 5, and you upload an integration file in `IP-Test`, a new version 6 is created for the integration. 

If you don't have an existing integration in which you can upload a file, you must first create a new integration and then upload. In this case, the new integration you create will be at version 1 and the uploaded integration will be at version 2.

If you have an existing integration that you want to upload, then select one of the following options:

### Console

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. Click **Integrations** from the left navigation menu to open the **Integrations** page. 
  3. Select an existing integration or create a new integration by clicking **Create integration**.

If you are creating a new integration: 

     1. Enter a name and description in the **Create Integration** dialog.
     2. Select a region for the integration. **Note:** The **Regions** dropdown only lists the regions provisioned in your Google Cloud project. To provision a new region, Click **Enable Region**. See [Enable new region](https://docs.cloud.google.com/application-integration/docs/enable-new-region) for more information. 
     3. Click **Create**.

This opens the integration in the _integration editor_.

  4. In the designer toolbar, click  more_vert  (Actions menu) and select **Upload**.
  5. In the file browser dialog, select the file that you want to upload, and then click **Open**. 

A new version of the integration is created using the uploaded file.




### API

To upload an integration, issue a `POST` request to the following API: 
    
    
      https://integrations.googleapis.com/v1/projects/$YOUR_GOOGLE_PROJECT_ID/locations/$PROJECT_LOCATION/integrations $INTEGRATION_NAME/versions/$INTEGRATION_VERSION}:upload
      

The following example shows you how to upload an integration:
    
    
      curl -v -s -H "Content-Type: application/json"  -H "Authorization: Bearer $TOKEN"  \
      -X POST -d '{"content": 
        "{\"name\":\"projects/450954726404/locations/us-east1/integrations/test-workflow/versions/0e90d453-5fcf-4aae-b164-2e8344d1ac11\",
        \"origin\":\"UI\",
        \"snapshotNumber\":\"3\",
        \"updateTime\":\"2022-01-06T04:26:58.137Z\",
        \"lockHolder\":\"abc@test.com\",
        \"createTime\":\"2022-01-06T04:26:42.734Z\",
        \"lastModifierEmail\":\"abc@test.com\",
        \"state\":\"DRAFT\",
        \"triggerConfigs\":[{\"label\":\"API Trigger\",\"startTasks\":[{\"taskId\":\"1\"}],
        \"properties\":{\"Trigger name\":\"rj-test-workflow_API_1\"},\"triggerType\":\"API\",\"triggerNumber\":\"1\",\"triggerId\":\"api_trigger/rj-test-workflow_API_1\"}],\"taskConfigs\":[{\"task\":\"EmailTask\",\"taskId\":\"1\",\"taskExecutionStrategy\":\"WHEN_ALL_SUCCEED\",\"displayName\":\"Send Email\"}]}"}' 
        \https://integrations.googleapis.com/v1/projects/demo-project/locations/us-east1/integrations/test-integration/versions:upload
      

For more information, see [`projects.locations.integrations.versions.upload`](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/projects.locations.integrations.versions/upload).

## What's next

  * Learn how to [manage integrations](https://docs.cloud.google.com/application-integration/docs/view-integration-details).
  * Learn how to [test and publish integrations](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations).
  * Learn about [all tasks and triggers](https://docs.cloud.google.com/application-integration/docs/all-triggers-tasks).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
