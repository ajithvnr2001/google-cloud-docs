---
url: https://docs.cloud.google.com/logging/docs/alerting/sql-based-incidents/
title: Manage alerts for SQL-based alerting policies \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:09.277669+00:00
---

# Manage alerts for SQL-based alerting policies  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/alerting/sql-based-incidents/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Manage alerts for SQL-based alerting policies Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Cloud Monitoring _alerts_ let you track and investigate issues when SQL query results over grouped log entries meet the condition of a SQL-based alerting policy. For each alert, Monitoring sends a notification and creates an **Alert details** page to help you troubleshoot the failure and manage the alert lifecycle.

On the **Alert details** page, you can view SQL query result summaries and links to related alerts. Monitoring doesn't create an alert if the policy is snoozed or disabled, or if the number of alerting policies or alerts exceeds the [limits for alerting](https://docs.cloud.google.com/monitoring/quotas#alerting_uptime_limits).

This feature is supported only for Google Cloud projects. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project.

## Before you begin

To get the permissions that you need to view and manage alerts, ask your administrator to grant you the following IAM roles on your project: 

  * View alerts by using the Google Cloud CLI or the Cloud Monitoring API: [Monitoring Alert Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.alertViewer) (`roles/monitoring.alertViewer`) 
  * View alerts by using the Google Cloud console: 
    * [Monitoring Cloud Console Incident Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.cloudConsoleIncidentViewer) (`roles/monitoring.cloudConsoleIncidentViewer`)
    * [Stackdriver Accounts Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#stackdriver.accounts.viewer) (`roles/stackdriver.accounts.viewer`)
  * Manage alerts by using the Google Cloud console: 
    * [Monitoring Cloud Console Incident Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.cloudConsoleIncidentEditor) (`roles/monitoring.cloudConsoleIncidentEditor`)
    * [Stackdriver Accounts Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#stackdriver.accounts.viewer) (`roles/stackdriver.accounts.viewer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about Cloud Monitoring roles, see [Control access with Identity and Access Management](https://docs.cloud.google.com/monitoring/access-control).

## View alerts

To view alerts in your project, use the Google Cloud console, the gcloud CLI, or the Monitoring API.

###  Google Cloud console 

To list the alerts in your Google Cloud project, do the following:

  1. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or management project. 

The **Alerting** page displays information about your alerting policies, snoozes, and alerts:

     * The **Summary** pane lists the number of open alerts.
     * The **Alerts** table displays the most recent open alerts. To list the most recent alerts in the table, including those that are closed, click **Show closed alerts**.
  3. To view the details of a specific alert, select the alert in the list.

The **Alert details** page opens. For more information about the **Alert details** page, see the Investigate an alert section of this document.




### Find older alerts

The **Alerts** table on the **Alerting** page shows the most recent open alerts. To view older alerts, do one of the following:

  * To page through the entries in the **Alerts** table, click _arrow_back_ios_ **Newer** or _arrow_forward_ios_ **Older**.

  * To open a page that lets you list and filter your alerts, click **See all alerts**. The **Alerts** page opens. From that page, do the following:

    * Show all alerts, including closed alerts. To show all alerts, click **Show closed alerts**.
    * Filter alerts. For information about adding filters, see Filter alerts.
    * Acknowledge or close an alert, or snooze its alerting policy. To access these options, click _more_vert_ **More options** in the alert's row, and make a selection from the menu. For more information, see Manage alerts.



### Filter alerts

To restrict the alerts that the table shows, add filters. If you add multiple filters, the table displays only alerts that satisfy all the filters.

To filter the table of alerts, do the following:

  1. On the **Alerts** page, click _filter_list_ **Filter table** and then select a filter property. Filter properties include the following:

     * State of the alert
     * Name of the alerting policy
     * When the alert was opened or closed 
  2. Select a value from the secondary menu or enter a value in the filter bar. 

The **Alerts** table then lists the filter.




###  gcloud 

You can use the gcloud to get alerts and list alerts.

### Get alert

Before using any of the command data below, make the following replacements: 

  * ALERT_NAME: The resource name of the alert. For example, `projects/my-project/alerts/my-alert-id`.



Execute the [`gcloud alpha monitoring alerts describe`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/monitoring/alerts/describe) command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud alpha monitoring alerts describe ALERT_NAME

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud alpha monitoring alerts describe ALERT_NAME

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud alpha monitoring alerts describe ALERT_NAME

The command returns a response with alert details such as alert state, attached labels, and the source alerting policy. The response looks similar to the following: 
    
    
    {
      "name": "projects/my-project/alerts/my-alert-id",
      "state": "OPEN",
      "open_time": "2025-06-11T09:53:46Z",
      "resource": {
        "type": "sql_alert"
      },
      "policy": {
        "name": "projects/my-project/alertPolicies/POLICY_1",
        "displayName": "test-policy"
      },
      "summaryText": "The row count SQL Condition for \"test-policy\" is above the threshold of 1."
    }
    

### List alerts

You can list alerts in your project and filter the results using the gcloud CLI.

Before using any of the command data below, make the following replacements: 

  * PROJECT_ID: The identifier of the project.



Execute the [`gcloud alpha monitoring alerts list`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/monitoring/alerts/list) command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud alpha monitoring alerts list

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud alpha monitoring alerts list

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud alpha monitoring alerts list

The command returns a response with alert details such as alert state, attached labels, and the source alerting policy. The response looks similar to the following: 
    
    
    {
      "alerts": [
        {
          "name": "projects/my-project/alerts/my-alert-id",
          "state": "OPEN",
          "open_time": "2025-06-11T09:53:46Z",
          "resource": {
            "type": "sql_alert"
          },
          "policy": {
            "name": "projects/my-project/alertPolicies/POLICY_1",
            "displayName": "test-policy"
          },
          "summaryText": "The row count SQL Condition for \"test-policy\" is above the threshold of 1."
        }
      ]
    }
    

You can also use the following optional flags to filter, sort, or modify the output: 

  * `--filter`: Provide a filter expression to filter alerts by time or by label. For example, filter by time with `--filter='close_time>="2025-09-10T00:00:00Z"'`, or filter by label with `--filter='resource.labels.key="value"'`.

  * `--sort-by`: A comma-separated list of fields to sort the output by. For example, `--sort-by=open_time`.

  * `--uri`: The command outputs a list of resource URIs instead of the default output.

  * `--limit`: Set this flag to `2` or greater to limit the number of alerts returned. Don't use this flag in conjunction with the `--filter` flag.




###  Monitoring API 

You can use the Monitoring API to get alerts and list alerts.

### Get alert

To get details on a single alert with the Monitoring API, use the [`alerts.get`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alerts/get) method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: The identifier of the project.
  * ALERT_ID: The ID of the alert.



HTTP method and URL: 
    
    
    GET https://monitoring.googleapis.com/v3/projects/PROJECT_ID/alerts/ALERT_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         "https://monitoring.googleapis.com/v3/projects/PROJECT_ID/alerts/ALERT_ID"

#### PowerShell (Windows)

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://monitoring.googleapis.com/v3/projects/PROJECT_ID/alerts/ALERT_ID" | Select-Object -Expand Content

The command returns a response with alert details such as alert state, attached labels, and the source alerting policy. The response looks similar to the following: 
    
    
    {
      "name": "projects/my-project/alerts/my-alert-id",
      "state": "OPEN",
      "open_time": "2025-06-11T09:53:46Z",
      "resource": {
        "type": "sql_alert"
      },
      "policy": {
        "name": "projects/my-project/alertPolicies/POLICY_1",
        "displayName": "test-policy"
      },
      "summaryText": "The row count SQL Condition for \"test-policy\" is above the threshold of 1."
    }
    

### List alerts

To list alerts in your project and filter the results with the Monitoring API, use the [`alerts.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alerts/list) method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: The identifier of the project.



HTTP method and URL: 
    
    
    GET https://monitoring.googleapis.com/v3/projects/PROJECT_ID/alerts

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: PROJECT_ID" \  
         "https://monitoring.googleapis.com/v3/projects/PROJECT_ID/alerts"

#### PowerShell (Windows)

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "PROJECT_ID" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://monitoring.googleapis.com/v3/projects/PROJECT_ID/alerts" | Select-Object -Expand Content

The command returns a response with alert details such as alert state, attached labels, and the source alerting policy. The response looks similar to the following: 
    
    
    {
      "alerts": [
        {
          "name": "projects/my-project/alerts/my-alert-id",
          "state": "OPEN",
          "open_time": "2025-06-11T09:53:46Z",
          "resource": {
            "type": "sql_alert"
          },
          "policy": {
            "name": "projects/my-project/alertPolicies/POLICY_1",
            "displayName": "test-policy"
          },
          "summaryText": "The row count SQL Condition for \"test-policy\" is above the threshold of 1."
        }
      ]
    }
    

Curl users can add the `--data-urlencode` flag followed by a filter expression to filter alerts by time or label. See the following examples: 

List alerts that were opened in the last hour:
    
    
    --data-urlencode "filter=(open_time>=\"`date -u -d "1 hour ago" +"%Y-%m-%dT%H:%M:%SZ"`\")"
    

List & filter alerts that are open from the last day:
    
    
    --data-urlencode "filter=(open_time>=\"`date -u -d "1 DAY ago" +"%Y-%m-%dT%H:%M:%SZ"`\" AND state=open)"
    

List & filter alerts that were opened between two periods:
    
    
    --data-urlencode "filter=(open_time>=\"`date -u -d "2 DAY ago" +"%Y-%m-%dT%H:%M:%SZ"`\" AND open_time<=\"`date -u -d "1 DAY ago" +"%Y-%m-%dT%H:%M:%SZ"`\")"
    

List & filter alerts by user label. In this example, filter by a user label with the name `app` and the value `my-gke-app`:
    
    
    --data-urlencode "filter=(policy.user_labels.app=\"my-gke-app\")"
    

Powershell users can use the following example to add a time-based filter to their request url: 
    
    
    $baseUrl = "https://monitoring.googleapis.com/v3/projects/my-project/alerts"
    $filterValue = (Get-Date).AddHours(-1).ToString("yyyy-MM-ddTHH:mm:ssZ")
    $filter = 'open_time >= "' + $filterValue + '"'
    $encodedFilter = [System.Uri]::EscapeDataString($filter)
    $url = $baseUrl + "?filter=" + $encodedFilter
    

**Note:** Alerts aren't always created when a condition is met. For more information, see [Alert isn't created when condition is met](https://docs.cloud.google.com/monitoring/alerts/troubleshooting-alerts#no-incidents).

## Investigate an alert

The **Alert details** page contains information that may help you identify the cause of an alert.

**Caution:** If you're working with Google Cloud support to investigate the cause of an alert, then don't modify the associated alerting policy. Modifying an alerting policy causes Cloud Monitoring to discard the precomputed data that the system uses to determine when to create an alert. Discarding this data results in the loss of the historical record of the alert.

### Explore query results

The **Total slot time consumed per day** pane shows the amount of time that your reserved BigQuery slots spent running the SQL queries for the alerting policy over the last 24 hours.

The **SQL query results** pane shows a list of query result summaries from each time Observability Analytics ran the SQL query from the alerting policy's condition. By default, the list is filtered to show only queries that matched the condition of the alerting policy.

  * To view the query and the table of query results from a specific time that Observability Analytics ran the query, click a value from the **Query run time** column.
  * To toggle between showing only query results that matched the condition of the alerting policy and all queries that Observability Analytics ran from the alerting policy, click **Show only queries matching alert conditions**.



### View supplementary information

The **Documentation** section shows the documentation template for notifications that you provided when creating the alerting policy. This information might include a description of what the alerting policy monitors as well as tips for mitigation. For more information, see [Annotate notifications with user-defined documentation](https://docs.cloud.google.com/monitoring/alerts/doc-variables).

If you didn't configure documentation for your alerting policy, then the **Documentation** pane shows "No documentation is configured."

## Explore related alerts

To help you discover underlying issues across your application, you can explore alerts related to other alerting policy conditions.

The **Related alerts** section shows a list of other alerts that were created when the condition of the alerting policy was met. 

## Manage alerts

Alerts are in one of the following states:

  * _error_ Open: The condition of the SQL-based alerting policy was met, and the alert is still open. If the same condition is met again and there is already an alert open, then a new alert isn't opened. 

  * _warning_ Acknowledged: The alert is open and has manually been marked as acknowledged. Typically, this status indicates that the alert is being investigated.

  * _check_circle_ Closed: You have manually closed the alert, or it was automatically closed after the auto-close period expired. 




### Acknowledge alerts

We recommend that you mark an alert as acknowledged when you begin investigating the cause of the alert.

To mark an alert as acknowledged, do the following:

  1. In the **Alerts** table of the **Alerting** page, click **See all alerts**.
  2. On the **Alerts** page, find the alert that you want to acknowledge, and then do one of the following:

     * Click _more_vert_ **More options** and then select **Acknowledge**.
     * Open the details page for the alert and then click **Acknowledge alert**.



### Snooze an alerting policy

To prevent Monitoring from creating alerts and sending notifications during a specific time period, snooze the related alerting policy. When you snooze an alerting policy, alerts related to the alerting policy remain open but don't cause further notifications. The alerts close based on the alerting policy auto-close duration. 

To create a snooze for an alert that you are viewing, do the following:

  1. On the **Alert details** page, click **Snooze Policy**.

  2. Select the snooze duration. After you select the snooze duration, the snooze begins immediately.




You can also snooze an alerting policy from the **Alerts** page by finding the alert that you want to snooze, clicking _more_vert_ **More options** , and then selecting **Snooze**. You can snooze alerting policies during outages to prevent further notifications during the troubleshooting process.

### Close alerts

You can let Monitoring close an alert for you, or you can close the alert.

Monitoring automatically closes an alert when the auto-close duration for the alerting policy expires. By default, the auto-close duration is 7 days. The minimum auto-close duration is 30 minutes.

The auto-close duration specifies the time that must elapse, without a repeat of the cause of the alert, before the alert closes. For this reason, when an alert is open and its cause reoccurs, the alert can stay open longer than the auto-close duration.

To close an alert, do the following:

  1. In the **Alerts** table of the **Alerting** page, click **See all alerts**.
  2. On the **Alerts** page, find the alert that you want to close, and then do one of the following:

     * Click _more_vert_ **View more** and then select **Close alert**
     * Open the **Alert details** page for that alert and then click **Close alert**.



If you see the message `Unable to close alert`, try again in a few minutes. You can't close a new alert immediately because the conditions that caused the alert are still considered active by the alerting system.

## Data retention and limits

For information about limits and about the retention period of alerts, see [Limits for alerting](https://docs.cloud.google.com/monitoring/quotas#alerting_uptime_limits).

## What's next

  * To create and manage alerting policies with the Monitoring API or from the command line, see [Manage alerting policies by API](https://docs.cloud.google.com/monitoring/alerts/using-alerting-api).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
