---
url: https://docs.cloud.google.com/certificate-authority-service/docs/monitoring/
title: Monitor resources using Cloud Monitoring \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:27.226321+00:00
---

# Monitor resources using Cloud Monitoring  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Monitor resources using Cloud Monitoring

[Cloud Monitoring](https://docs.cloud.google.com/monitoring) can be used to monitor operations performed on resources in Certificate Authority Service.

## Before you begin

If you haven't already done so, set up a Google Cloud project that has the Certificate Authority Service API enabled. For information, see [Prepare your environment](https://docs.cloud.google.com/certificate-authority-service/docs/prepare-environment).

## View metrics in Cloud Monitoring

### Console

To view the metrics for a monitored resource by using the Metrics Explorer, do the following:

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or the app-enabled folder's management project.
  3. In the **Metric** element, expand the **Select a metric** menu, enter `Certificate Authority` in the filter bar, and then use the submenus to select a specific resource type and metric: 
     1. In the **Active resources** menu, select [**Certificate Authority**](https://docs.cloud.google.com/monitoring/api/resources#tag_privateca.googleapis.com/CertificateAuthority).
     2. To select a metric, use the **Active metric categories** and **Active metrics** menus. For a list of metrics, see [**privateca metrics**](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-privateca). 
     3. Click **Apply**.
  4. To add filters, which remove time series from the query results, use the [**Filter** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#filter-option).

  5. To combine time series, use the menus on the [**Aggregation** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#select_display). For example, to display the CPU utilization for your VMs, based on their zone, set the first menu to **Mean** and the second menu to **zone**.

All time series are displayed when the first menu of the **Aggregation** element is set to **Unaggregated**. The default settings for the **Aggregation** element are determined by the metric type you selected.

  6. For quota and other metrics that report one sample per day, do the following: 
     1. In the **Display** pane, set the **Widget type** to **Stacked bar chart**.
     2. Set the time period to at least one week.



## CA Service metrics

The list of metrics can be viewed in Cloud Monitoring [documentation](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-privateca).

The monitored resource documentation can be viewed in [Monitored resources](https://docs.cloud.google.com/monitoring/api/resources#tag_privateca.googleapis.com/CertificateAuthority).

## Set up quota alerts and monitoring

You can set up quota usage alerts and monitoring by using Cloud Monitoring.

For more information on how to set up alerts and create charts, see [Set up quota alerts and monitoring](https://docs.cloud.google.com/docs/quotas/set-up-quota-alerts).

## Enabling Recommended Alerts

Use the following instructions to enable recommended alerts.

### Console

  1. Go to the CA Service Overview page in the Google Cloud console.

[Certificate Authority Service](https://console.cloud.google.com/security/cas/overview)

  2. On the top right of the Overview page, click the **\+ 5 Recommended Alerts**.

  3. Enable or disable each alert, reading its description.

     * Some alerts support custom thresholds. For example, you can specify when you want to be alerted for an expiring CA certificate, or the error rate for a high rate of certificate creation failures.
     * All alerts support [notification channels](https://docs.cloud.google.com/monitoring/support/notification-options).
  4. Click **Submit** once you have enabled all selected alerts.




## Create an alerting policy

### Console

You can create alerting policies to monitor the values of metrics and to notify you when those metrics violate a condition. 

  1. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. If you haven't created your notification channels and if you want to be notified, then click **Edit Notification Channels** and add your notification channels. Return to the **Alerting** page after you add your channels. 
  3. From the **Alerting** page, select **Create policy**.
  4. To select the metric, expand the **Select a metric** menu and then do the following: 
     1. To limit the menu to relevant entries, enter `Certificate Authority` into the filter bar. If there are no results after you filter the menu, then disable the **Show only active resources & metrics** toggle. 
     2. For the **Resource type** , select [**Certificate Authority**](https://docs.cloud.google.com/monitoring/api/resources#tag_privateca.googleapis.com/CertificateAuthority).
     3. For the **Metric category** , select **Ca**.
     4. For the **Metric** , select a metric from the [**list of privateca metrics**](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-privateca).
     5. Select **Apply**.
  5. Click **Next**.
  6. The settings in the **Configure alert trigger** page determine when the alert is triggered. Select a condition type and, if necessary, specify a threshold. For more information, see [Create metric-threshold alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui). 
  7. Click **Next**.
  8. Optional: To add notifications to your alerting policy, click **Notification channels**. In the dialog, select one or more notification channels from the menu, and then click **OK**.
  9. Optional: Update the **Alert autoclose duration**. This field determines when Monitoring closes alerts in the absence of metric data.
  10. Optional: Click **Documentation** , and then add any information that you want included in a notification message.
  11. Click **Alert name** and enter a name for the alerting policy.
  12. Click **Create Policy**.

For more information, see [Alerting overview](https://docs.cloud.google.com/monitoring/alerts). 

## Create Pub/Sub notification channel

A notification channel that publishes events to Pub/Sub can be set up by following [these instructions](https://docs.cloud.google.com/monitoring/support/notification-options#pubsub).

## Sample alert policies

You can use the following sample alert policies for common CA Service monitoring use cases.

To learn more about alert policies, see the [documentation](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies).

### CA expiring in 30 days

This alert policy notifies you 30 days before a managed CA expires. This policy creates alert notifications for all managed CAs across all projects whose metrics are visible to the Google Cloud project selected in the Google Cloud console project picker. For information about metric visibility, see [Understanding metrics scope](https://docs.cloud.google.com/monitoring/settings#concept-scope).

### Console

You can create alerting policies to monitor the values of metrics and to notify you when those metrics violate a condition. 

  1. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. If you haven't created your notification channels and if you want to be notified, then click **Edit Notification Channels** and add your notification channels. Return to the **Alerting** page after you add your channels. 
  3. From the **Alerting** page, select **Create policy**.
  4. To select the metric, expand the **Select a metric** menu and then do the following: 
     1. To limit the menu to relevant entries, enter `Certificate Authority` into the filter bar. If there are no results after you filter the menu, then disable the **Show only active resources & metrics** toggle. 
     2. For the **Resource type** , select [**Certificate Authority**](https://docs.cloud.google.com/monitoring/api/resources#tag_privateca.googleapis.com/CertificateAuthority).
     3. For the **Metric category** , select **Ca**.
     4. For the **Metric** , select **ca/cert_expiration**.
     5. Select **Apply**.
  5. Click **Next**.
  6. The settings in the **Configure alert trigger** page determine when the alert is triggered. Complete this page with the settings in the following table.  
**Configure alert trigger** page  
Field |   
Value  
---|---  
**`Condition type`** | `Threshold`  
**`Alert trigger`** | `Any time series violates`  
**`Threshold position`** | `Below threshold`  
**`Threshold value`** | `2592000000 ms`  
**`Advanced Options: Retest window`** | `No retest`  
  7. Click **Next**.
  8. Optional: To add notifications to your alerting policy, click **Notification channels**. In the dialog, select one or more notification channels from the menu, and then click **OK**.
  9. Optional: Update the **Alert autoclose duration**. This field determines when Monitoring closes alerts in the absence of metric data.
  10. Optional: Click **Documentation** , and then add any information that you want included in a notification message.
  11. Click **Alert name** and enter a name for the alerting policy.
  12. Click **Create Policy**.

For more information, see [Alerting overview](https://docs.cloud.google.com/monitoring/alerts). 

### gcloud

Paste the following policy into a file named `ca-expiration-policy.yaml`:
    
    
    combiner: OR
    conditions:
    - conditionThreshold:
        aggregations:
        - alignmentPeriod: 60s
          perSeriesAligner: ALIGN_MEAN
        comparison: COMPARISON_LT
        duration: 0s
        filter: metric.type="privateca.googleapis.com/ca/cert_expiration" resource.type="privateca.googleapis.com/CertificateAuthority"
        thresholdValue: 2592000.0
        trigger:
          count: 1
      displayName: CA certificate expiration
    displayName: CA expiring in 30 days
    enabled: true
    

Create the alert policy with the following command:
    
    
    gcloud monitoring policies create --policy-from-file ca-expiration-policy.yaml
    

After creating the alert policy, follow [Managing notification channels](https://docs.cloud.google.com/monitoring/alerts/using-channels-api) to create or update existing notification channels, if required. To add a notification channel to an existing alert policy, follow [Updating notification channels in a policy](https://docs.cloud.google.com/monitoring/alerts/using-alerting-api#api-replace-channels).

### High rate of certificate creation failures

This alert policy notifies you when the ratio of certificate creation failures, due to either CA policy or validation failure, exceeds a threshold of `0.2`. This policy creates alert notifications for all managed CAs across all projects whose metrics are visible to the Google Cloud project selected in the Google Cloud console project picker. For information about metric visibility, see [Understanding metrics scope](https://docs.cloud.google.com/monitoring/settings#concept-scope).

**Note:** Editing the conditions of a [metric ratio policy](https://docs.cloud.google.com/monitoring/alerts/policies-in-json#json-ratio) is only supported through the gcloud CLI. Once the policy has been created, you can edit the policy's description and add notification channels through the Google Cloud console however.

### gcloud

Paste the following policy into a file named `cert-create-failure.yaml`:
    
    
    displayName: High rate of certificate creation failures
    enabled: true
    combiner: OR
    conditions:
    - conditionThreshold:
        filter: metric.type="privateca.googleapis.com/ca/cert/create_failure_count" resource.type="privateca.googleapis.com/CertificateAuthority"
        aggregations:
        - alignmentPeriod: 300s
          crossSeriesReducer: REDUCE_SUM
          groupByFields:
          - resource.label.resource_container
          - resource.label.location
          - resource.label.certificate_authority_id
          perSeriesAligner: ALIGN_DELTA
        denominatorFilter: metric.type="privateca.googleapis.com/ca/cert/create_request_count"
          resource.type="privateca.googleapis.com/CertificateAuthority"
        denominatorAggregations:
        - alignmentPeriod: 300s
          perSeriesAligner: ALIGN_DELTA
        comparison: COMPARISON_GT
        duration: 0s
        thresholdValue: 0.2
        trigger:
          count: 1
      displayName: 'Ratio: Certificate creation CA policy error count / Total certificate creation request count'
    

Create the alert policy with the following command:
    
    
    gcloud monitoring policies create --policy-from-file cert-create-failure.yaml
    

After creating the alert policy, follow [Managing notification channels](https://docs.cloud.google.com/monitoring/alerts/using-channels-api) to create or update existing notification channels, if required. To add a notification channel to an existing alert policy, follow [Updating notification channels in a policy](https://docs.cloud.google.com/monitoring/alerts/using-alerting-api#api-replace-channels).

#### What this policy does

This policy computes the ratio of failures to total requests. The policy triggers an alert notification if the ratio exceeds 20% (that is, the ratio is greater than 0.2) over the 5-minute alignment period.

The filter in the condition selects the number of certificate creation failures, which is the numerator in the ratio. The numerator aggregates by project, location, and CA resource ID, since this metric has additional labels. The denominator filter in the condition selects the number of certificate creation requests.

Once the threshold is reached, the policy triggers the alert notification immediately, since the permitted duration for the condition is 0 seconds. This policy uses a trigger count of 1, which is the number of time series that needs to violate the condition to trigger the alert notification.

## Monitoring gauge metrics

Gauge metrics measure a value at a specific instant in time. For example, `privateca.googleapis.com/ca/resource_state` or `privateca.googleapis.com/kms/key_issue` are gauge metrics. These metrics use a boolean value, while using labels to provide additional information. For example, `privateca.googleapis.com/ca/resource_state` uses a boolean for whether the CA state is enabled, but uses a label, `state`, for the actual resource state.

When monitoring gauge metrics that use boolean values, we recommend that you use the `COUNT` aggregator to build alert thresholds. The `SUM` aggregator only sums the boolean values, whereas the `COUNT` aggregator sums the number of time series. For example, if you want to determine the number of CAs that are in the `DISABLED` state, you should create a filter for `state=DISABLED`. Use the `COUNT` aggregator to determine the number of CAs that match this condition.

## Cloud Monitoring cost

There is no cost for monitoring CA Service.

## What's next

  * [Cloud Monitoring](https://docs.cloud.google.com/monitoring)
  * [CA Service metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-privateca)
  * [Managing notification channels](https://docs.cloud.google.com/monitoring/support/notification-options#pubsub)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
