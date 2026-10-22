---
url: https://docs.cloud.google.com/apigee/docs/api-security/security-alerts/
title: Security alerts \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:31:52.328655+00:00
---

# Security alerts  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-security/security-alerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Security alerts Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

**Preview — Advanced API Security Alerts**

This feature is covered by the [Pre-GA Offerings Terms](https://cloud.google.com/terms/service-terms#1) of the Google Cloud Terms of Service. Pre-GA features may have limited support, and changes to pre-GA features may not be compatible with other pre-GA versions. For more information, see the [ launch stage descriptions](https://cloud.google.com/products#product-launch-stages).

Support for the Preview launch of Advanced API Security Alerts is available through the [ Apigee - Google Cloud Community](https://www.googlecloudcommunity.com/gc/Apigee/bd-p/cloud-apigee) forum. 

Advanced API Security Alerts lets you create alerts for events related to API security, such as changes to your security scores or incidents of detected API abuse. You create alerts using [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview). You can configure an alert to send you a notification by text, email, or other channels, when the alert is triggered.

See [Create metric-threshold alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui) for more information on creating alerts and [Incidents for metric-based alertings policies](https://docs.cloud.google.com/monitoring/alerts/incidents-events) for information on managing generated alerts.

**Note:** You can configure security alerts for Risk Assessment v1 and Risk Assessment v2 security scores. This page discusses security alerts and monitoring metrics for both. See Metrics for security alerts. 

## Required roles

To set up alerts and notification channels in Cloud Monitoring, you need to be assigned the following roles:

  * `roles/monitoring.alertPolicyEditor`
  * `roles/monitoring.notificationChannelEditor`



## Limitations

For alerting, the following limitations apply:

  * The maximum number of alerting policies is 500 for all Apigee subscription levels.
  * Metrics data is stored for 6 weeks.
  * Maximum time period that a metric-threshold condition evaluates is 23 hours 30 minutes.
  * There can be up to a 4-minute delay from the time an event that triggers an alert occurs until the time the alert is created and a notification is sent.



See [Limits for alerting](https://cloud.google.com/monitoring/quotas#alerting_uptime_limits) for a complete list of limits for alerting.

The following sections present examples that show how to create alerts.

## Example: Create an alert for a decrease in proxy security score (Risk Assessment v1)

This example creates an alert when a [proxy security score](https://docs.cloud.google.com/apigee/docs/api-security/security-scores#proxy-assessment) falls below a specified threshold. To create the alert, do the following steps: 

  1. In the Google Cloud console, go to the **Monitoring >Alerting > Policies > Create alerting policy** page.

[Go to Create alerting policy](https://console.cloud.google.com/monitoring/alerting/policies/create)

  2. Click **Select a Metric**.
  3. Deselect **Show only active resources & metrics**. 

**Note:** If there is no recent API traffic data in your organization, the metric in the next step won't be displayed unless this option is unselected.

  4. Select a metric as follows: 
     1. Select **Apigee API Security Profile Environment Association**.
     2. In the pane that opens to the right, select **Security**.
     3. In the next pane to the right, select **Security score of Apigee API proxy**. 
     4. Click **Apply**.
**Note:** Alternatively, you can choose one of the following metrics: 
     * **Security score of Apigee sources** : See [Source assessment](https://docs.cloud.google.com/apigee/docs/api-security/security-scores#source-assessment). 
     * **Security score of Apigee target servers** : See [Target assessment](https://docs.cloud.google.com/apigee/docs/api-security/security-scores#target-assessment). 
     * **Security score of Apigee environment** : The total security score in the environment.

See Metrics for security alerts.

  5. (Optional) To restrict the data for the alert, say to a specified environment, you can create a filter as follows: 
     1. Under **Add filters > New filter**, click in the **Filter** field and select a resource label to filter on, such as **env**.
     2. In the **Comparator** field, select a comparator, such as **=**.
     3. In the **Value** field, select a value for the resource label, such as an environment name.

With this filter, an alert will only be triggered by data that passes the filter condition. See Filters for a list of available filters.

  6. Under **Transform data** , in the **Rolling window function** field, select **sum**.
  7. Click **Next**.
  8. In the **Configure alert trigger** pane, set the following: 
     * Under **Condition Types** , select **Threshold**.
     * Under **Alert trigger** , select **Any time series violates**.
     * Under **Threshold position** , select **Below threshold**.
     * In the **Threshold value** field, enter a threshold that triggers the alert, such as **600**.
  9. Click **Next**.
  10. In the **Configure notifications** field, click in the **Notification Channels** field and select channels, such as text message or email, for the notification. If you have not configured any channels, click **Manage Notification Channels** and add a channel or channels. 
  11. Click **OK**.
  12. In the **Documentation** field, enter any text that you want delivered with the notification, such as a description of what triggered the alert. For example, you could enter "A security score has fallen below 600."
  13. Under **Name the alert policy** , enter a name for the alert policy.
  14. Click **Next** and review the details of the alert policy.
  15. If everything looks good, click **Create Policy** to create the alert policy.



## Example: Create an alert for increase in detected abuse traffic for a detection rule

This example shows how to create an alert when the number of requests with detected abuse traffic exceeds a specified threshold for any single [detection rule](https://docs.cloud.google.com/apigee/docs/api-security/detection-rules). To create the alert, do the following steps:

  1. In the Google Cloud console, go to the **Monitoring >Alerting > Policies > Create alerting policy** page.

[Go to Create alerting policy](https://console.cloud.google.com/monitoring/alerting/policies/create)

![Create alerting policy page](https://docs.cloud.google.com/static/apigee/docs/api-monitoring/images/create-alerting-policy-new-condition.png)

  2. Click **Select a Metric**.
  3. Deselect **Show only active resources & metrics**. 

**Note:** If there is no recent API traffic data in your organization, the metric in the next step won't be displayed unless this option is unselected.

  4. Select a metric as follows: 
     1. Select **Apigee API Security Detection Rule**.
     2. In the pane that opens to the right, select **Security**.
     3. In the next pane to the right, select **Apigee API Security detected request count by rule**. 
     4. Click **Apply**.
**Note:** Alternatively, you could select the metric **Apigee Environment > Security > Apigee API Security detected request count**. In this case, an alert would be triggered when the total detected request count exceeded the specified threshold (as opposed to the count for a single rule). 

See Metrics for security alerts.

  5. (Optional) To restrict the data for the alert, say to a specified environment, you can create a filter as follows: 
     1. Under **Add filters > New filter**, click in the **Filter** field and select a resource label to filter on, such as **env**.
     2. In the **Comparator** field, select a comparator, such as **=**.
     3. In the **Value** field, select a value for the resource label, such as an environment name.

With this filter, an alert will only be triggered by data that passes the filter condition, such as data in an environment. See Filters for a list of available filters.

  6. Under **Transform data** , in the **Rolling window function** field, select **sum**.
  7. Click **Next**.
  8. In the **Configure alert trigger** pane, set the following: 
     * Under **Condition Types** , select **Threshold**.
     * Under **Alert trigger** , select **Any time series violates**.
     * Under **Threshold position** , select **Above threshold**.
     * In the **Threshold value** field, enter a threshold that triggers the alert, such as **100**.
  9. Click **Next**.
  10. In the **Configure notifications** field, click in the **Notification Channels** field and select channels, such as text message or email, for the notification. If you have not configured any channels, click **Manage Notification Channels** and add a channel or channels. 
  11. Click **OK**.
  12. In the **Documentation** field, enter any text that you want delivered with the notification, such as a description of what triggered the alert. For example, you could enter "Detected abuse traffic exceeded 100 for $(resource.label.env)." This uses the label $(resource.label.env), which displays the environment whose data triggered the alert. 
  13. Under **Name the alert policy** , enter a name for the alert policy.
  14. Click **Next** and review the details of the alert policy.
  15. If everything looks good, click **Create Policy** to create the alert policy.



## Example: Create a risk assessment monitoring condition monitoring alert (Risk Assessment v2) 

This example creates a new Cloud Monitoring alerting policy for a [Risk Assessment monitoring condition](https://docs.cloud.google.com/apigee/docs/api-security/security-scores#monitoring-conditions) that alerts if the security score on any of its monitored proxies falls below a certain threshold. 

  1. [Create a monitoring condition](https://docs.cloud.google.com/apigee/docs/api-security/security-scores#manage-monitoring-conditions).
  2. Follow the instructions in [Create a monitoring alert](https://docs.cloud.google.com/apigee/docs/api-security/security-scores#create-monitoring-alerts) to create a new monitoring alert. Apigee prepopulates some fields for you when the page loads.
  3. If desired, you can change settings to customize the alerting policy. Follow the guidance in [Create alerting policy](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui#create-policy). You must provide a name for the alerting policy.
  4. Click **Create policy** to save the new alerting policy.



## Metrics for security alerts

The table below describes the available metrics for creating security alerts:

Resource | Metric | Description | Supported filters  
---|---|---|---  
Apigee Environment | Apigee API Security request count:  
`apigee.googleapis.com/security/request_count` | Number of API requests processed by Advanced API Security, since the last sample. | location, org, env, proxy  
Apigee Environment | Apigee API Security detected request count:  
`apigee.googleapis.com/security/detected_request_count` | Number of API requests detected by Advanced API Security abuse detection, since the last sample. | location, org, env, proxy  
Apigee API Security Detection Rule | Apigee API Security detected request count by rule:  
`apigee.googleapis.com/security/detected_request_count_by_rule` | Number of API requests detected by Advanced API Security abuse detection and grouped by detection rule since the last sample. | location, org, env, proxy, detection_rule  
Apigee API Security Incident | Apigee API Security incident request count:  
`apigee.googleapis.com/security/incident_request_count` | Number of API requests detected to be part of an API Security incident. This value is measured once every hour. | location, org, env, proxy  
Apigee API Security Incident | Apigee API Security incident request count by detection rule:  
`apigee.googleapis.com/security/incident_request_count_by_rule` | Number of API requests detected to be part of an API Security incident grouped by detection rule. This value is measured once every hour. | location, org, env, incident_id, detection_rule  
Apigee API Security Profile Environment Association | Security score of Apigee API sources:  
`apigee.googleapis.com/security/source_score` | Applies to Risk Assessment v1. Current security score of Apigee API proxy based on Advanced API Security source assessment. This value is measured at least once every 3 hours.  | location, org, env, profile  
Apigee API Security Profile Environment Association | Security score of Apigee API proxy:  
`apigee.googleapis.com/security/proxy_score` | Applies to Risk Assessment v1. Current security score of Apigee API proxy based on Advanced API Security proxy assessment. This value is measured at least once every 3 hours.  | location, org, env, profile, proxy  
Apigee API Security Profile Environment Association | Security score of Apigee API target:  
`apigee.googleapis.com/security/target_score` | Applies to Risk Assessment v1. Current security score of Apigee API proxy based on Advanced API Security target assessment. This value is measured at least once every 3 hours.  | location, org, env, profile, target_server  
Apigee API Security Profile Environment Association | Security score of Apigee environment:  
`apigee.googleapis.com/security/environment_score` | Applies to Risk Assessment v1. Current total security score of Apigee environment based on Advanced API Security assessments of sources, proxies, and targets. This value is measured at least once every 3 hours.  | location, org, env, profile  
Apigee API Security Assessment Result | Security score:  
`apigee.googleapis.com/security/score` | Applies to Risk Assessment v2. Current security score of a deployed resource based on a security profile.  | location, org, scope, resource, security_profile  
  
### Filters

Filter Label | Description  
---|---  
location | Location of the resource: global always.  
org | Apigee organization name  
env | Apigee environment name  
profile | Apigee API Security profile name  
proxy | Apigee API proxy name  
target_server | Apigee target server name  
detection_rule | Apigee API security detection rule name  
scope | For Risk Assessment v2, identifier of the scope associated with the assessed resource.  
resource | For Risk Assessment v2, identifier of the assessed resource.  
security_profile | For Risk Assessment v2, identifier of the security profile used to assess the resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
