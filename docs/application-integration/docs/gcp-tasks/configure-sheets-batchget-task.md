---
url: https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-sheets-batchget-task/
title: Sheets - Batch Get task \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:27:09.942176+00:00
---

# Sheets - Batch Get task  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-sheets-batchget-task/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Sheets - Batch Get task

**Preview — BigQuery Connector**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The **Sheets - Batch Get** task lets you read and retrieve multiple, discontinuous ranges of values from a Google spreadsheet. 

**Spreadsheet:** The primary object in Google Sheets that can contain multiple sheets. Each [sheet](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/sheets) has structured information contained in [cells](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/cells). 

You can find the ID of your spreadsheet from its web URL. For example, `https://docs.google.com/spreadsheets/d/SPREADSHEET_ID/edit#gid=0`

[Google Sheets](https://developers.google.com/sheets) is one of the many cloud-based productivity solutions in [Google Workspace](https://docs.cloud.google.com/workspace). It allows you to create and edit online spreadsheets with real-time collaboration functionality. 

## Before you begin

Ensure that you perform the following tasks in your Google Cloud project before configuring the **Sheets - Batch Get** task:

  1. Enable the Google Sheets API (`sheets.googleapis.com`). 

[ Enable the Google Sheets API ](https://console.cloud.google.com/apis/enableflow?apiid=sheets.googleapis.com)

  2. Create an [authentication profile](https://docs.cloud.google.com/application-integration/docs/configuring-auth-profile#createAuthProfile). Application Integration uses an authentication profile to connect to an authentication endpoint for the **Sheets - Batch Get** task. 

For information about granting additional roles or permissions to a service account, see [Granting, changing, and revoking access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

  3. Understand and learn about the [common terminologies](https://developers.google.com/sheets/api/guides/concepts) used in Google Sheet.



## Configure the Sheets - Batch Get task

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Integrations**. 

The **Integrations** page appears listing all the integrations available in the Google Cloud project. 

  3. Select an existing integration or click **Create integration** to create a new one. 

If you are creating a new integration: 

     1. Enter a name and description in the **Create Integration** pane.
     2. Select a region for the integration. **Note:** The **Regions** dropdown only lists the regions provisioned in your Google Cloud project. To provision a new region, click **Enable Region**. See [Enable new region](https://docs.cloud.google.com/application-integration/docs/enable-new-region) for more information. 
     3. Select a service account for the integration. You can change or update the service account details of an integration any time from the info **Integration summary** pane in the integration toolbar. **Note:** The option to select a service account is displayed only if you have enabled integration governance for the selected region. 
     4. Click **Create**. The newly created integration opens in the _integration editor_. 

  4. In the _integration editor_ navigation bar, click **Tasks** to view the list of available tasks and connectors. 
  5. Click and place the **Sheets - Batch Get** element in the integration editor.
  6. Click the **Sheets - Batch Get** element on the designer to view the **Sheets - Batch Get** task configuration pane.
  7. Go to **Authentication** , and select an existing authentication profile that you want to use. 

Optional. If you have not created an authentication profile prior to configuring the task, Click **\+ New authentication profile** and follow the steps as mentioned in [Create a new authentication profile](https://docs.cloud.google.com/application-integration/docs/configuring-auth-profile#createAuthProfile).

  8. Go to **Task Input** , and configure the displayed inputs fields using the following Task input parameters table. 

Changes to the inputs fields are saved automatically.




## Task input parameters

The following table describes the input parameters of the **Sheets - Batch Get** task: 

Property  | Data type  | Description   
---|---|---  
SpreadsheetId | String  | The ID of your spreadsheet. You can find the ID of your spreadsheet from its web URL. For example, `https://docs.google.com/spreadsheets/d/SPREADSHEET_ID/edit#gid=0`  
MajorDimension | enum [(Dimension)](https://developers.google.com/sheets/api/reference/rest/v4/Dimension) | The primary category or dimension that should be applied. For example, `ROWS` or `COLUMNS`.  **Default value:** `DIMENSION_UNSPECIFIED`  
Ranges | String  | The [A1 notation or R1C1 notation](https://developers.google.com/sheets/api/guides/concepts#cell) of the range to retrieve values from.   
DateTimeRenderOption | enum [(DateTimeRenderOption)](https://developers.google.com/sheets/api/reference/rest/v4/DateTimeRenderOption) | Indicates how values related to date, time, and duration is represented in the output. **Note:** **dateTimeRenderOption** is not considered if the value specified for **valueRenderOption** is `FORMATTED_VALUE`.  **Default value:** `SERIAL_NUMBER`  
ValueRenderOption | enum [(ValueRenderOption)](https://developers.google.com/sheets/api/reference/rest/v4/ValueRenderOption) | Indicates how the retrieved values are represented in the output.  **Default value:** `FORMATTED_VALUE`  
  
## Task output

The **Sheets - Batch Get** task returns the response output containing an object with the spreadsheet ID and an array of [ValueRange](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values#resource:-valuerange) objects corresponding to each requested range, listed in the requested order. Following is a sample output:
    
    
    {
            "spreadsheetId": SPREADSHEET_ID,
            "[valueRanges](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values#resource-valuerange)": [
              {
                "range": "Sheet1!B1:B1000",
                "[majorDimension](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values#dimension)": "COLUMNS",
                "values": [
                  ["Cost",20.5,15,100,135.5]
                ]
              },
              {
                "range": "Sheet1!D1:D1000",
                "[majorDimension](https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets.values#dimension)": "COLUMNS",
                "values": [
                  ["Ship Date",42430,42444,42449,42449]
                ]
              }
            ]
          }

## Error handling strategy

An error handling strategy for a task specifies the action to take if the task fails due to a [temporary error](https://docs.cloud.google.com/application-integration/docs/error-handling). For information about how to use an error handling strategy, and to know about the different types of error handling strategies, see [Error handling strategies](https://docs.cloud.google.com/application-integration/docs/error-handling-strategy). 

## Quotas and limits

For information about quotas and limits, see [Quotas and limits](https://docs.cloud.google.com/application-integration/docs/quotas).

## What's next

  * Add [edges and edge conditions](https://docs.cloud.google.com/application-integration/docs/edge-overview).
  * [Test and publish](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations) your integration.
  * Configure a [trigger](https://docs.cloud.google.com/application-integration/docs/how-to-guides#configure-triggers).
  * Add a [Data Mapping task](https://docs.cloud.google.com/application-integration/docs/data-mapping-task).
  * See [all tasks for Google Cloud services](https://docs.cloud.google.com/application-integration/docs/how-to#configure-tasks-for-google-cloud-services).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
