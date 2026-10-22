---
url: https://docs.cloud.google.com/iam/docs/review-iam-policy-history/
title: Review IAM allow policy history \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:38.772854+00:00
---

# Review IAM allow policy history  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/review-iam-policy-history/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Review IAM allow policy history Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to review the history of changes to your IAM allow policies.

You can review changes to your resource's allow policies by searching your audit logs for entries containing the `SetIamPolicy` method.

You can also review allow policy changes with Cloud Asset Inventory. 

## View allow policy changes with `SetIamPolicy`

You can view allow policy changes by reviewing your audit logs for entries that contain the `SetIamPolicy` method. You can review your audit logs using the Google Cloud console or the gcloud CLI.

### Console

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. In the query editor, enter one of the following queries. These queries search your audit logs for entries that have `SetIamPolicy` in the `methodName` field of the `protoPayload`:

     * To get the logs of all allow policy changes made on a resource, use the following query:
           
           logName="RESOURCE_TYPE/RESOURCE_ID/logs/cloudaudit.googleapis.com%2Factivity"
           protoPayload.methodName:SetIamPolicy
           

     * To get the logs of allow policy changes that involve a specific user or service account, use the following query:
           
           logName="RESOURCE_TYPE/RESOURCE_ID/logs/cloudaudit.googleapis.com%2Factivity"
           protoPayload.methodName:SetIamPolicy
           protoPayload.serviceData.policyDelta.bindingDeltas.member:"EMAIL_ADDRESS"
           

Replace the following:

       * `RESOURCE_TYPE`: The resource type that you're listing audit logs for. Valid values are `projects`, `folders`, or `organizations`.
       * `RESOURCE_ID`: Your Google Cloud project, folder, or organization ID. Project IDs are alphanumeric, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.
       * `EMAIL_ADDRESS`: The email address of the user or service account—for example, `example-service-account@example-project.iam.gserviceaccount.com`.
  3. To run the query, click **Run query**.

  4. Use the **Timeline** selector to specify the appropriate time range for the query. Alternatively, you can add a timestamp expression directly to the query editor. For more information, see [View logs by time range](https://docs.cloud.google.com/logging/docs/view/building-queries#queries-with-time-restriction).




### gcloud

The `[gcloud logging read](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read)` command reads log entries. 

Before using any of the command data below, make the following replacements: 

  * `RESOURCE_TYPE`: The resource type that you are listing audit logs for. Use the value `projects`, `folders`, or `organizations`. 
  * `RESOURCE_ID`: Your Google Cloud project, organization, or folder ID. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`. 
  * `TIME_PERIOD`: The time period that you are listing audit logs for. The entries returned are not older than this value. If left unspecified, the default value is `1d`. For information about time formats, see [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes). 
  * `RESOURCE_TYPE_SINGULAR`: The resource type that you are listing audit logs for. Use the value `project`, `folder`, or `organization`. 



Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud logging read \
        'logName:RESOURCE_TYPE/RESOURCE_ID/logs/cloudaudit.googleapis.com%2Factivity
        AND protoPayload.methodName=SetIamPolicy' \
        --freshness=TIME_PERIOD \
        --RESOURCE_TYPE_SINGULAR=RESOURCE_ID

#### Windows (PowerShell)
    
    
    gcloud logging read `
        'logName:RESOURCE_TYPE/RESOURCE_ID/logs/cloudaudit.googleapis.com%2Factivity
        AND protoPayload.methodName=SetIamPolicy' `
        --freshness=TIME_PERIOD `
        --RESOURCE_TYPE_SINGULAR=RESOURCE_ID

#### Windows (cmd.exe)

**Note:** If this command uses `'` for quoting content, replace these single quotes with double quotes. If quoting is nested, use `\"` to escape the inner quotes. 
    
    
    gcloud logging read ^
        'logName:RESOURCE_TYPE/RESOURCE_ID/logs/cloudaudit.googleapis.com%2Factivity
        AND protoPayload.methodName=SetIamPolicy' ^
        --freshness=TIME_PERIOD ^
        --RESOURCE_TYPE_SINGULAR=RESOURCE_ID

## View allow policy changes with Cloud Asset Inventory

You can also view allow policy changes using [Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory/docs/overview) in the Google Cloud console or the gcloud CLI.

### Console

  1. In the Google Cloud console, go to the **Asset Inventory** page.

[Go to Asset Inventory](https://console.cloud.google.com/iam-admin/asset-inventory/policies)

  2. Click the **IAM Policy** tab.

  3. Run the following query in the **Filter** field:
         
         Resource : RESOURCE_ID

Replace `RESOURCE_ID` with your Google Cloud project, folder, or organization ID. Project IDs are alphanumeric, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.

  4. To view the change history of the resource's allow policy, click the resource's name, then select the **Change History** tab.

  5. To compare any changes to the allow policy for the resource, select two different timestamped records from the **Select a record to compare** menu.




### gcloud

The `[gcloud asset get-history](https://docs.cloud.google.com/sdk/gcloud/reference/asset/get-history)` command gets the updated history of allow policies on an asset that overlaps a time window. 

Before using any of the command data below, make the following replacements: 

  * `RESOURCE_TYPE`: The resource type that you are listing audit logs for. Use the value `project`, `folder`, or `organization`. 
  * `RESOURCE_ID`: Your Google Cloud project, organization, or folder ID. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`. 
  * `ASSET_NAME`: A comma-separated list of [formatted resource names](https://docs.cloud.google.com/asset-inventory/docs/resource-name-format) for the resources whose allow policy histories you want to view. For example, `//cloudresourcemanager.googleapis.com/projects/my-project`. These resources can be any of the resource types that [accept allow policies](https://docs.cloud.google.com/iam/docs/resource-types-with-policies). 
  * `START_TIME`: The beginning of the time range. The maximum time range is 7 days. The value must be the current time or a time no more than 35 days in the past. For information about time formats, see [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes). 
  * `END_TIME`: Optional. The finishing point of the time range. The maximum time range is 7 days. The value must be the current time or a time no more than 35 days in the past. When not provided, the end time is assumed to be the current time. For information about time formats, see [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes). 



Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud asset get-history \
        --RESOURCE_TYPE=RESOURCE_ID \
        --asset-names=ASSET_NAME_1,ASSET_NAME_2,... \
        --content-type=iam-policy \
        --start-time=START_TIME \
        --end-time=END_TIME

#### Windows (PowerShell)
    
    
    gcloud asset get-history `
        --RESOURCE_TYPE=RESOURCE_ID `
        --asset-names=ASSET_NAME_1,ASSET_NAME_2,... `
        --content-type=iam-policy `
        --start-time=START_TIME `
        --end-time=END_TIME

#### Windows (cmd.exe)
    
    
    gcloud asset get-history ^
        --RESOURCE_TYPE=RESOURCE_ID ^
        --asset-names=ASSET_NAME_1,ASSET_NAME_2,... ^
        --content-type=iam-policy ^
        --start-time=START_TIME ^
        --end-time=END_TIME

The response contains the updated history of allow policies.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
