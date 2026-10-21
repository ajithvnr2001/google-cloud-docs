---
url: https://docs.cloud.google.com/iam/docs/service-account-monitoring/
title: Monitor usage patterns for service accounts and keys \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:47:37.231172+00:00
---

# Monitor usage patterns for service accounts and keys  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/service-account-monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Monitor usage patterns for service accounts and keys Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to use Cloud Monitoring to view usage metrics for your service accounts and service account keys. These metrics let you view and track usage patterns, which can help you identify anomalies, either automatically or manually.

**Note:** To quickly identify the dates of only the most recent service account and key usages, see [View recent usage for service accounts and keys](https://docs.cloud.google.com/iam/docs/service-account-recent-usage).

Service accounts and service account keys appear in these metrics if they are used to call any Google API, including APIs that are not part of Google Cloud. The metrics include both successful and failed API calls. For example, if an API call fails because the caller is not authorized to call that API, or because the request referred to a resource that does not exist, the service account or key that was used for that API call appears in the metrics.

Service account keys also appear in these metrics if a system lists the keys while attempting to authenticate a request, even if the system doesn't use the key to authenticate the request. This behavior is most common when using [signed URLs for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/signed-urls) or when authenticating to third-party applications. As a result it is possible to see usage metrics for keys that have not been used for authentication.

The following don't appear in either service account or service account key metrics:

  * Cloud Storage HMAC authentication keys
  * Requests authenticated by [API keys bound to service accounts](https://docs.cloud.google.com/docs/authentication/api-keys#api-keys-bound-sa)



Monitoring retains service account metrics for 6 weeks. If you need to access data for a longer time period, you can periodically export the results to BigQuery. For more information, see [Monitoring metric export](https://docs.cloud.google.com/solutions/stackdriver-monitoring-metric-export) in the Solutions documentation.

After you use a service account or service account key, usage metrics are usually available within a few minutes.

## Before you begin

  * Enable the IAM and Cloud Monitoring APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=iam.googleapis.com,monitoring.googleapis.com&redirect=https%3A//console.cloud.google.com)




### Required roles

To get the permissions that you need to view recent usage for service accounts and keys, ask your administrator to grant you the [Monitoring Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer) (`roles/monitoring.viewer`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View usage metrics for all service accounts or keys

To view the usage metrics for your service accounts or service account keys, follow these steps:

### Console

To view the metrics for a monitored resource by using the Metrics Explorer, do the following:

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or the app-enabled folder's management project.
  3. In the **Metric** element, expand the **Select a metric** menu, enter `IAM Service Account` in the filter bar, and then use the submenus to select a specific resource type and metric: 
     1. In the **Active resources** menu, select **IAM Service Account**.
     2. In the **Active metric categories** menu, select **Service_account**.
     3. In the **Active metrics** menu, select a service account metric. The following metrics are available within your selected time interval: 
        * For service account usage metrics, select **Service account authentication events**.
        * For service account key usage metrics, select **Service account key authentication events**.
     4. Click **Apply**.
  4. To add filters, which remove time series from the query results, use the [**Filter** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#filter-option).

  5. To combine time series, use the menus on the [**Aggregation** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#select_display). For example, to display the CPU utilization for your VMs, based on their zone, set the first menu to **Mean** and the second menu to **zone**.

All time series are displayed when the first menu of the **Aggregation** element is set to **Unaggregated**. The default settings for the **Aggregation** element are determined by the metric type you selected.

  6. For quota and other metrics that report one sample per day, do the following: 
     1. In the **Display** pane, set the **Widget type** to **Stacked bar chart**.
     2. Set the time period to at least one week.

**Note:** Service account metrics include disabled service accounts. Service account key metrics _do not_ include disabled service account keys, but they might include expired or deleted service account keys.

### REST

The Cloud Monitoring API API's `[timeSeries.list](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list)` method allows you to access usage metrics programmatically. 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.
  * `METRIC_TYPE`: The type of metric you want to check. Use one of the following values: 
    * For service account usage metrics, use `iam.googleapis.com%2Fservice_account%2Fauthn_events_count`. 
    * For service account key usage metrics, use `iam.googleapis.com%2Fservice_account%2Fkey%2Fauthn_events_count`. 
  * `END_TIME`: The end of the time interval that you want to check, in percent-encoded [RFC 3339](https://tools.ietf.org/html/rfc3339) format. For example, `2020-06-12T00%3A00%3A00.00Z`.
  * `START_TIME`: The start of the time interval that you want to check, in percent-encoded [RFC 3339](https://tools.ietf.org/html/rfc3339) format. For example, `2020-04-12T00%3A00%3A00.00Z`.

**Note:** If you are sending the request using the API Explorer, do not use percent-encoded values. 




HTTP method and URL: 
    
    
    GET https://monitoring.googleapis.com/v3/projects/PROJECT_ID/timeSeries?filter=metric.type%3D%22METRIC_TYPE%22&interval.endTime=END_TIME&interval.startTime=START_TIME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://monitoring.googleapis.com/v3/projects/PROJECT_ID/timeSeries?filter=metric.type%3D%22METRIC_TYPE%22&interval.endTime=END_TIME&interval.startTime=START_TIME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://monitoring.googleapis.com/v3/projects/PROJECT_ID/timeSeries?filter=metric.type%3D%22METRIC_TYPE%22&interval.endTime=END_TIME&interval.startTime=START_TIME" | Select-Object -Expand Content

#### APIs Explorer (browser)

Open the [method reference page](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

For more information about programmatically reading usage metrics, see [Reading metric data](https://docs.cloud.google.com/monitoring/custom-metrics/reading-metrics) in the Monitoring documentation. 

**Note:** Service account metrics include disabled service accounts. Service account key metrics _do not_ include disabled service account keys, but they might include expired or deleted service account keys.

## View usage metrics for a single service account

To view usage metrics for a single service account, follow these steps:

### Console

  1. In the Google Cloud console, go to the **Service Accounts** page.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Select the project that contains your service account.

  3. Click the email address of your service account.

  4. Click the **Metrics** tab. The **Authentication traffic** chart shows the usage metrics for the service account.

  5. Optional: To view the chart on the **Metrics explorer** page, which offers additional filtering and viewing options, click more_vert > **View in Metrics Explorer**.




### REST

The Cloud Monitoring API's `[timeSeries.list](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list)` method , when used with specific filters, allows you to get usage metrics for a single service account. You can then use those metrics to determine when the account was last used. 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.
  * `SERVICE_ACCOUNT_ID`: The unique numeric ID of your service account. To find your service account's unique numeric ID, follow these steps: 
    1. In the Google Cloud console, go to the **Service Accounts** page.

[Go to the Service Accounts page](https://console.cloud.google.com/iam-admin/serviceaccounts)
    2. Click the email address of your service account. Your service account's unique numeric ID is the value in the **Unique ID** field.
  * `END_TIME`: The end of the time interval that you want to check, in percent-encoded [RFC 3339](https://tools.ietf.org/html/rfc3339) format. For example, `2020-06-12T00%3A00%3A00.00Z`.
  * `START_TIME`: The start of the time interval that you want to check, in percent-encoded [RFC 3339](https://tools.ietf.org/html/rfc3339) format. For example, `2020-04-12T00%3A00%3A00.00Z`.

**Note:** If you are sending the request using the API Explorer, do not use percent-encoded values. 




HTTP method and URL: 
    
    
    GET https://monitoring.googleapis.com/v3/projects/PROJECT_ID/timeSeries?filter=metric.type%3D%22iam.googleapis.com%2Fservice_account%2Fauthn_events_count%22%20AND%20resource.labels.unique_id%3D%22SERVICE_ACCOUNT_ID%22&interval.endTime=END_TIME&interval.startTime=START_TIME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://monitoring.googleapis.com/v3/projects/PROJECT_ID/timeSeries?filter=metric.type%3D%22iam.googleapis.com%2Fservice_account%2Fauthn_events_count%22%20AND%20resource.labels.unique_id%3D%22SERVICE_ACCOUNT_ID%22&interval.endTime=END_TIME&interval.startTime=START_TIME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://monitoring.googleapis.com/v3/projects/PROJECT_ID/timeSeries?filter=metric.type%3D%22iam.googleapis.com%2Fservice_account%2Fauthn_events_count%22%20AND%20resource.labels.unique_id%3D%22SERVICE_ACCOUNT_ID%22&interval.endTime=END_TIME&interval.startTime=START_TIME" | Select-Object -Expand Content

#### APIs Explorer (browser)

Open the [method reference page](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

The response contains a [`timeSeries` object](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TimeSeries) with all of the recent authentication events for the specified service account. 

## View usage metrics for a single service account key

To view usage metrics for a single service account key, follow these steps:

### Console

  1. In the Google Cloud console, go to the **Service Accounts** page.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Select the project that contains the service account associated with your key.

  3. Click the email address of the service account associated with your key.

  4. Click the **Metrics** tab. The **Authentication traffic per key** chart shows usage metrics for all keys associated with the service account.

  5. In the chart legend, click the ID of the service account key that you want to view usage metrics for. The chart updates to show metrics for only that service account key.

  6. Optional: To view the chart on the **Metrics explorer** page, which offers additional filtering and viewing options, click more_vert > **View in Metrics Explorer**.




### REST

**First, get the service account key's ID.**

  1. List the service account keys:

The `[projects.serviceAccounts.keys.list](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys/list)` method lists all of the service account keys for a service account. 

Before using any of the request data, make the following replacements: 

     * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.
     * `SA_NAME`: The name of the service account whose keys you want to list.
     * `KEY_TYPES`: Optional. A comma-separated list of key types that you want to include in the response. The key type indicates whether a key is user-managed (`USER_MANAGED`) or system-managed (`SYSTEM_MANAGED`). If left blank, all keys are returned. 

HTTP method and URL: 
    
    GET https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SA_NAME@PROJECT_ID.iam.gserviceaccount.com/keys?keyTypes=KEY_TYPES

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SA_NAME@PROJECT_ID.iam.gserviceaccount.com/keys?keyTypes=KEY_TYPES"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SA_NAME@PROJECT_ID.iam.gserviceaccount.com/keys?keyTypes=KEY_TYPES" | Select-Object -Expand Content

#### APIs Explorer (browser)

Open the [method reference page](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys/list). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a JSON response similar to the following:
    
    {
      "keys": [
        {
          "name": "projects/my-project/serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com/keys/90c48f61c65cd56224a12ab18e6ee9ca9c3aee7c",
          "validAfterTime": "2020-03-04T17:39:47Z",
          "validBeforeTime": "9999-12-31T23:59:59Z",
          "keyAlgorithm": "KEY_ALG_RSA_2048",
          "keyOrigin": "GOOGLE_PROVIDED",
          "keyType": "USER_MANAGED"
        },
        {
          "name": "projects/my-project/serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com/keys/e5e3800831ac1adc8a5849da7d827b4724b1fce8",
          "validAfterTime": "2020-03-31T23:50:09Z",
          "validBeforeTime": "9999-12-31T23:59:59Z",
          "keyAlgorithm": "KEY_ALG_RSA_2048",
          "keyOrigin": "GOOGLE_PROVIDED",
          "keyType": "USER_MANAGED"
        },
        {
          "name": "projects/my-project/serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com/keys/b97699f042b8eee6a846f4f96259fbcd13e2682e",
          "validAfterTime": "2020-05-17T18:58:13Z",
          "validBeforeTime": "9999-12-31T23:59:59Z",
          "keyAlgorithm": "KEY_ALG_RSA_2048",
          "keyOrigin": "GOOGLE_PROVIDED",
          "keyType": "USER_MANAGED",
          "disabled": true
          "disable_reason": "SERVICE_ACCOUNT_KEY_DISABLE_REASON_EXPOSED"
          "extended_status": "SERVICE_ACCOUNT_KEY_EXTENDED_STATUS_KEY_EXPOSED"
          "extended_status_message": "exposed at: https://www.github.com/SomePublicRepo"
        }
      ]
    }
    

  2. Use the metadata in the response to identify the key you want to track. Then, copy the key's unique ID from the end of the `name` field.

The `name` field has the following format:
         
         "name": "projects/PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT_EMAIL/keys/KEY_ID"

The key's unique ID is everything after `keys/`.

For example, the unique ID in the following key name is `0f561cc41650ff521899de2fd653bd3de08e2da4`:
         
         "name": "projects/my-project/serviceAccounts/my-account@my-project.iam.gserviceaccount.com/keys/0f561cc41650ff521899de2fd653bd3de08e2da4"




**Then, use the ID to view usage metrics for the service account key.**

The Cloud Monitoring API's `[timeSeries.list](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list)` method , when used with specific filters, allows you to get usage metrics for a single service account key. You can then use those metrics to determine when the key was last used. 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.
  * `KEY_ID`: The unique ID of your service account key.
  * `END_TIME`: The end of the time interval that you want to check, in percent-encoded [RFC 3339](https://tools.ietf.org/html/rfc3339) format. For example, `2020-06-12T00%3A00%3A00.00Z`.
  * `START_TIME`: The start of the time interval that you want to check, in percent-encoded [RFC 3339](https://tools.ietf.org/html/rfc3339) format. For example, `2020-04-12T00%3A00%3A00.00Z`.

**Note:** If you are sending the request using the API Explorer, do not use percent-encoded values. 




HTTP method and URL: 
    
    
    GET https://monitoring.googleapis.com/v3/projects/PROJECT_ID/timeSeries?filter=metric.type%3D%22iam.googleapis.com%2Fservice_account%2Fkey%2Fauthn_events_count%22%20AND%20metric.labels.key_id%3D%22KEY_ID%22&interval.endTime=END_TIME&interval.startTime=START_TIME

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://monitoring.googleapis.com/v3/projects/PROJECT_ID/timeSeries?filter=metric.type%3D%22iam.googleapis.com%2Fservice_account%2Fkey%2Fauthn_events_count%22%20AND%20metric.labels.key_id%3D%22KEY_ID%22&interval.endTime=END_TIME&interval.startTime=START_TIME"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://monitoring.googleapis.com/v3/projects/PROJECT_ID/timeSeries?filter=metric.type%3D%22iam.googleapis.com%2Fservice_account%2Fkey%2Fauthn_events_count%22%20AND%20metric.labels.key_id%3D%22KEY_ID%22&interval.endTime=END_TIME&interval.startTime=START_TIME" | Select-Object -Expand Content

#### APIs Explorer (browser)

Open the [method reference page](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

The response contains a [`timeSeries` object](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TimeSeries) with all of the recent authentication events for the specified service account key. 

## Export metrics

You can use Monitoring to export your metrics to BigQuery. Exporting metrics is useful for performing long-term analysis because Monitoring only retains metrics for a limited time.

For instructions, see [Monitoring metric export](https://docs.cloud.google.com/solutions/stackdriver-monitoring-metric-export) in the Solutions documentation.

## What's next

  * Discover how to [export metric data](https://docs.cloud.google.com/solutions/stackdriver-monitoring-metric-export) to BigQuery.


  * Use Activity Analyzer to [view only the most recent authentication events](https://docs.cloud.google.com/iam/docs/service-account-recent-usage) for your service accounts and keys.


  * Use [service account insights](https://docs.cloud.google.com/iam/docs/manage-service-account-insights) to identify service accounts that have not been used in the past 90 days.


  * Learn how to [disable service accounts](https://docs.cloud.google.com/iam/docs/service-accounts-disable-enable#disabling) or [delete service accounts](https://docs.cloud.google.com/iam/docs/service-accounts-delete-undelete#deleting).
  * Learn how to [delete service account keys](https://docs.cloud.google.com/iam/docs/keys-create-delete#deleting).
  * Explore the features offered by [Monitoring](https://docs.cloud.google.com/monitoring/docs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
