---
url: https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-drive-list-task/
title: Drive - List task \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:22.857296+00:00
---

# Drive - List task  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/gcp-tasks/configure-drive-list-task/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Drive - List task

**Preview — BigQuery Connector**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The **Drive - List** task lets you search and retrieve files and folders that are stored on a Google Drive account. 

[Google Drive](https://developers.google.com/drive) is a cloud file storage service that provides you personal storage space to store and access collaborative shared files and folders in the cloud. 

## Before you begin

Ensure that you perform the following tasks in your Google Cloud project before configuring the **Drive - List** task:

  1. Enable the Google Drive API (`drive.googleapis.com`). 

[ Enable the Google Drive API ](https://console.cloud.google.com/apis/enableflow?apiid=drive.googleapis.com)

  2. Create an [authentication profile](https://docs.cloud.google.com/application-integration/docs/configuring-auth-profile#createAuthProfile). Application Integration uses an authentication profile to connect to an authentication endpoint for the **Drive - List** task. 

For information about granting additional roles or permissions to a service account, see [Granting, changing, and revoking access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).




## Configure the Drive - List task

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
  5. Click and place the **Drive - List** element in the integration editor.
  6. Click the **Drive - List** element on the designer to view the **Drive - List** task configuration pane.
  7. Go to **Authentication** , and select an existing authentication profile that you want to use. 

Optional. If you have not created an authentication profile prior to configuring the task, Click **\+ New authentication profile** and follow the steps as mentioned in [Create a new authentication profile](https://docs.cloud.google.com/application-integration/docs/configuring-auth-profile#createAuthProfile).

  8. Go to **Task Input** , and configure the desired inputs fields using the following Task input parameters table. 

Changes to the inputs fields are saved automatically.




## Task input parameters

The following table describes the input parameters of the **Drive - List** task: 

Property  | Data type  | Description   
---|---|---  
`Corpora` | String | Optional parameter to search for files within a [corpora](https://developers.google.com/drive/api/guides/about-files#org).   
`DriveId` | String |  The ID of your Google shared drive.   
`IncludeItemsFromAllDrives` | Boolean |  Set the value to `true` if you want to include both your personal drive and shared drive items in the search results. Default value: `false`.  
`IncludeLabels` | String |  A comma-separated list of label IDs that is included in the `labelInfo` part of the response. For more information about label IDs, see [Labels overview](https://developers.google.com/drive/api/guides/about-labels).   
`IncludePermissionsForView` | String |  Specify `published`. For more information, see [Share files, folders & drives](https://developers.google.com/drive/api/guides/manage-sharing).   
`OrderBy` | String |  The order in which the files are sorted. Each key sorts ascending by default. For more information, see the [`files.list` method](https://developers.google.com/drive/api/reference/rest/v3/files/list). The following are the salid values: 

  * `createdTime`
  * `folder`
  * `modifiedByMeTime`
  * `modifiedTime`
  * `name`
  * `name_natural`
  * `quotaBytesUsed`
  * `recency`
  * `sharedWithMeTime`
  * `starred`
  * `viewedByMeTime`

**Note:** When you sort the files by `recency` descending, if the last thing you did was view a file, then that file appears at the top of the `files.list` result.  
`PageSize` | Integer |  The maximum number of files to return per page. Acceptable values are `1` to `1000`. Default value: `100`.  
`PageToken` | String |  The token for continuing a previous **Drive - List** task. Set this value to the value of `nextPageToken` from the previous response.   
`Q` | String |  A query for filtering the file results. For more information, see [Search for files](https://developers.google.com/drive/api/v3/search-files).   
`Spaces` | String |  A comma-separated list of spaces to query within the corpora. Acceptable values are `drive` and `appDataFolder`.   
`SupportsAllDrives` | Boolean |  Set the value to `true` if the requesting application supports both My Drives and shared drives. Default value: `false`.  
  
## Task output

The **Drive - List** task returns the response output containing the list of files. Following is a sample output:
    
    
      {
        "nextPageToken": string,
        "kind": string,
        "incompleteSearch": boolean,
        "files": [
          {
            object ([File](https://developers.google.com/drive/api/reference/rest/v3/files#File))
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
