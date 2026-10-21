---
url: https://docs.cloud.google.com/monitoring/alerts/incidents-events/
title: Alerts for metric-based alerting policies \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:44:31.599061+00:00
---

# Alerts for metric-based alerting policies  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/alerts/incidents-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Alerts for metric-based alerting policies Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Monitoring _alerts_ let you track and investigate issues when time-series data meets the conditions of a metric-based alerting policy. For each alert, Monitoring sends a notification and creates an **Alert details** page to help you troubleshoot the failure and manage the alert lifecycle.

On the **Alert details** page, you can view the alert timeline, charts of monitored metric data, and links to related alerts and log entries. If a policy contains multiple conditions, then the policy specifies whether meeting a single condition opens an alert. Monitoring doesn't create an alert if the policy is snoozed or disabled, or if the number of alerting policies or alerts exceeds the [limits for alerting](https://docs.cloud.google.com/monitoring/quotas#alerting_uptime_limits).

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
     * Metric type
     * Resource type 
  2. Select a value from the secondary menu or enter a value in the filter bar. 

For example, if you select **Metric type** and enter `usage_time`, then you might see only the following options in the secondary menu:
         
         agent.googleapis.com/cpu/usage_time
         compute.googleapis.com/guest/container/cpu/usage_time
         container.googleapis.com/container/cpu/usage_time
         

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
      "name": "projects/my-project/alerts/my-alert-id1",
      "state": "OPEN",
      "open_time": "2025-06-11T09:53:46Z",
      "close_time": "2025-06-13T10:11:36Z",
      "resource": {
        "type": "gce_instance",
        "labels": {
          "zone": "us-west1",
          "instance_id": "123456789",
          "project_id": "my-project"
        }
      },
      "metric": {
        "labels": {
          "instance_name": "my-instance1"
        },
        "type": "compute.googleapis.com/instance/cpu/usage_time"
      },
      "policy": {
        "name": "projects/my-project/alertPolicies/POLICY_1",
        "displayName": "my-policy"
      },
      "summaryText": "[ALERT] VM Instance - CPU usage on my-project my-instance1"
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
          "name": "projects/my-project/alerts/my-alert-id1",
          "state": "OPEN",
          "open_time": "2025-06-11T09:53:46Z",
          "close_time": "2025-06-13T10:11:36Z",
          "resource": {
            "type": "gce_instance",
            "labels": {
              "zone": "us-west1",
              "instance_id": "123456789",
              "project_id": "my-project"
            }
          },
          "metric": {
            "labels": {
              "instance_name": "my-instance1"
            },
            "type": "compute.googleapis.com/instance/cpu/usage_time"
          },
          "policy": {
            "name": "projects/my-project/alertPolicies/POLICY_1",
            "displayName": "my-policy"
          },
          "summaryText": "[ALERT] VM Instance - CPU usage on my-project my-instance1"
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
      "name": "projects/my-project/alerts/my-alert-id1",
      "state": "OPEN",
      "open_time": "2025-06-11T09:53:46Z",
      "close_time": "2025-06-13T10:11:36Z",
      "resource": {
        "type": "gce_instance",
        "labels": {
          "zone": "us-west1",
          "instance_id": "123456789",
          "project_id": "my-project"
        }
      },
      "metric": {
        "labels": {
          "instance_name": "my-instance1"
        },
        "type": "compute.googleapis.com/instance/cpu/usage_time"
      },
      "policy": {
        "name": "projects/my-project/alertPolicies/POLICY_1",
        "displayName": "my-policy"
      },
      "summaryText": "[ALERT] VM Instance - CPU usage on my-project my-instance1"
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
          "name": "projects/my-project/alerts/my-alert-id1",
          "state": "OPEN",
          "open_time": "2025-06-11T09:53:46Z",
          "close_time": "2025-06-13T10:11:36Z",
          "resource": {
            "type": "gce_instance",
            "labels": {
              "zone": "us-west1",
              "instance_id": "123456789",
              "project_id": "my-project"
            }
          },
          "metric": {
            "labels": {
              "instance_name": "my-instance1"
            },
            "type": "compute.googleapis.com/instance/cpu/usage_time"
          },
          "policy": {
            "name": "projects/my-project/alertPolicies/POLICY_1",
            "displayName": "my-policy"
          },
          "summaryText": "[ALERT] VM Instance - CPU usage on my-project my-instance1"
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

### Explore metric data

To analyze the state of your metric before and after your alert occurred, use the **Alert Metrics** chart. This chart shows a timeline and the time series that caused the condition of your alerting policy to be met.

You can adjust the range of the timeline to look for trends and patterns in your metric data relative to the alert:

  * To toggle between showing only the time series that caused the condition to be met and showing all the time series that the condition evaluates, click _toggle_off_ **Show all timeseries**.

  * To change the time range displayed by the chart, you can use the time-range selector in the toolbar, or highlight time ranges on the chart with your pointer.




You can also analyze your metric data in greater detail by viewing it in the [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer). To do so, go to the **Alert Metrics** chart and then click _query_stats_ **Explore Data**. By default, the Metrics Explorer aggregates and filters metric data so that the metric chart aligns with the time series shown on the **Alert Metrics** timeline.

### Explore log entries

The **Logs** pane on the **Alert details** page shows log entries that match the resource type and labels of the monitored resource for your metric. You can analyze these log entries to find additional information that might help you troubleshoot your alert.

  * To view the log entries in the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface), click **View in Logs Explorer** , and then select a scoping project. The **Logs Explorer** provides additional tools to analyze log entry data, such as a timeline of when related log entries were created.
  * To view and edit the query used to filter the log entries in the [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer), click _query_stats_ **Explore Data**.

**Note:** The `resource.type` appears as `timeseries_query` for MQL-based alerts and as `prometheus_target` for PromQL-based alerts when the resource type can't be inferred. The **Logs** pane might not display any logs for either of these resource types. To resolve this, click **View in Logs Explorer** or _query_stats_ **Explore Data** and remove the `resource.type` clause from the query.

### View application information

For alerting policies associated with an [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) application, go to the **Associated with application** section. One entry in this section lists the application ID and links to a dashboard displaying information about the application. The second entry lists either a workload or service, and links to a dashboard.

### View supplementary information

The **Labels** section shows the labels and values for the monitored resource and metric of the time series that caused the alert, as well as user labels defined in the alerting policy. This information might help you identify the specific monitored resource that caused the alert. For more information, see [Annotate alerts with labels](https://docs.cloud.google.com/monitoring/alerts/labels).

The **Documentation** section shows the documentation template for notifications that you provided when creating the alerting policy. This information might include a description of what the alerting policy monitors as well as tips for mitigation. For more information, see [Annotate notifications with user-defined documentation](https://docs.cloud.google.com/monitoring/alerts/doc-variables).

If you didn't configure documentation for your alerting policy, then the **Documentation** pane shows "No documentation is configured."

## Explore related alerts

To help you discover underlying issues across your application, you can explore alerts related to other alerting policy conditions.

The **Related alerts** section shows a list of alerts that match one of the following: 

  * The alert was created when a condition of the same alerting policy was met.
  * The alert shares a label with the alert shown on the **Alert details** page. 



## Manage alerts

Alerts are in one of the following states:

  * _error_ Open: The alerting policy's set of conditions are being met or there isn't data to indicate that the condition is no longer met. If an alerting policy contains multiple conditions, then alerts are opened depending on how those conditions are combined. For more information, see [Policies with multiple conditions](https://docs.cloud.google.com/monitoring/alerts/concepts-indepth#condition-combiners). 

  * _warning_ Acknowledged: The alert is open and has manually been marked as acknowledged. Typically, this status indicates that the alert is being investigated.

  * _check_circle_ Closed: The system observed that the condition stopped being met, you closed the alert, or 7 days passed without an observation that the condition continued to be met. 


When you configure an alerting policy, ensure that the steady state provides a signal when everything is OK. This is necessary to ensure that the error-free state can be identified and, if an alert is open, for that alert to be closed. If there is no signal to indicate that an error condition has stopped, after an alert is opened, it stays open for 7 days after the alerting policy fires. 

For example, if you create an alerting policy that notifies you when the count of errors is more than 0, ensure that it produces a count of 0 errors when there aren't any errors. If the alerting policy returns null or empty in the error-free state, then there is no signal to indicate when the errors have stopped. If necessary, PromQL lets you specify a default value that is used when no measured value is available. 

### Acknowledge alerts

We recommend that you mark an alert as acknowledged when you begin investigating the cause of the alert.

To mark an alert as acknowledged, do the following:

  1. In the **Alerts** table of the **Alerting** page, click **See all alerts**.
  2. On the **Alerts** page, find the alert that you want to acknowledge, and then do one of the following:

     * Click _more_vert_ **More options** and then select **Acknowledge**.
     * Open the details page for the alert and then click **Acknowledge alert**.



If your alerting policy is configured to [send repeated notifications](https://docs.cloud.google.com/monitoring/alerts/policies-in-api#send-repeated-notifications), then acknowledging an alert doesn't stop the notifications. To stop them, do one of the following:

  * Create a snooze for the alerting policy.
  * Disable the alerting policy.



### Snooze an alerting policy

To prevent Monitoring from creating alerts and sending notifications during a specific time period, snooze the related alerting policy. When you snooze an alerting policy, Monitoring also closes all alerts related to the alerting policy. 

To create a snooze for an alert that you are viewing, do the following:

  1. On the **Alert details** page, click **Snooze Policy**.

  2. Select the snooze duration. After you select the snooze duration, the snooze begins immediately.




You can also snooze an alerting policy from the **Alerts** page by finding the alert that you want to snooze, clicking _more_vert_ **More options** , and then selecting **Snooze**. You can snooze alerting policies during outages to prevent further notifications during the troubleshooting process.

### Close alerts

You can let Monitoring close an alert for you, or you can close an alert after observations stop arriving. If you close an alert and then data arrives that indicates the condition is met, then a new alert is created. When you close an alert, that action doesn't close any other alerts that are open for the same condition. If you snooze an alerting policy, then open alerts are closed when the snooze starts.

Monitoring automatically closes an alert when any of the following occur:

  * Metric-threshold conditions:

    * An observation arrives that indicates that the threshold isn't violated.
    * No observations arrive, the condition is configured to close alerts when observations stop arriving, and the state of the underlying resource is either unknown or isn't disabled.

**Note:** The alert isn't closed when data stops arriving if the state of a resource is known to be disabled. However, you can close the alert manually. Monitoring can determine the state of a resource when the resource contains the `metadata.system_labels.state` label and when the alerting policy isn't written with the Monitoring Query Language. For more information, see [Alert isn't closed when data stops arriving](https://docs.cloud.google.com/monitoring/alerts/troubleshooting-alerts#incident-not-closed).
    * No observations arrive for the auto-close duration of the alerting policy and the condition isn't configured to automatically close alerts when observations stop arriving. To configure the auto-close duration, you can use the Google Cloud console or the Monitoring API. By default, the auto-close duration is seven days. The minimum auto-close duration is 30 minutes.

  * Metric-absence conditions:

    * An observation occurs.
    * No observations arrive for 24 hours after the auto-close duration of the alerting policy expires. To configure the auto-close duration, you can use the Google Cloud console or the Monitoring API. By default, the auto-close duration is seven days.
  * Forecast conditions:

    * A forecast is produced and it predicts that the time series won't violate the threshold within the forecast window.
    * No observations arrive for 10 minutes, the condition is configured to close alerts when observations stop arriving, and the state of the underlying resource is either unknown or isn't disabled.

**Note:** The alert isn't closed when data stops arriving if the state of a resource is known to be disabled. However, you can close the alert manually. Monitoring can determine the state of a resource when the resource contains the `metadata.system_labels.state` label and when the alerting policy isn't written with the Monitoring Query Language. For more information, see [Alert isn't closed when data stops arriving](https://docs.cloud.google.com/monitoring/alerts/troubleshooting-alerts#incident-not-closed).
    * No observations arrive for the auto-close duration of the alerting policy and the condition isn't configured to automatically close alerts when observations stop arriving.




For example, an alerting policy generated an alert because the HTTP response latency was greater than 2 seconds for 10 consecutive minutes. If the next measurement of the HTTP response latency is less than or equal to two seconds, then the alert is closed. Similarly, if no data at all is received for seven days, then the alert is closed.

To close an alert, do the following:

  1. In the **Alerts** table of the **Alerting** page, click **See all alerts**.
  2. On the **Alerts** page, find the alert that you want to close, and then do one of the following:

     * Click _more_vert_ **View more** and then select **Close alert**
     * Open the **Alert details** page for that alert and then click **Close alert**.



If you see the message `Unable to close alert with active conditions`, then the alert can't be closed because data has been received within the most recent alerting period.

If you see the message `Unable to close alert. Please try again in a few minutes.`, then the alert couldn't be closed due to an internal error.

## Data retention and limits

For information about limits and about the retention period of alerts, see [Limits for alerting](https://docs.cloud.google.com/monitoring/quotas#alerting_uptime_limits).

## What's next

  * To create and manage alerting policies with the Monitoring API or from the command line, see [Manage alerting policies by API](https://docs.cloud.google.com/monitoring/alerts/using-alerting-api).


  * For a detailed conceptual treatment of alerting policies, see [Behavior of metric-based alerting policies](https://docs.cloud.google.com/monitoring/alerts/concepts-indepth).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
