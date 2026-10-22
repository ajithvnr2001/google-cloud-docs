---
url: https://docs.cloud.google.com/stackdriver/docs/observability/pricing-optimize-and-monitor/
title: Optimize and monitor Google Cloud Observability costs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:13.054007+00:00
---

# Optimize and monitor Google Cloud Observability costs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/observability/pricing-optimize-and-monitor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Resources ](https://docs.cloud.google.com/stackdriver/quotas)



Send feedback 

#  Optimize and monitor Google Cloud Observability costs Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how you can optimize and monitor your Google Cloud Observability costs. For pricing information, see [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing).

You might also be interested in the following documents:

  * [Estimate your bills](https://docs.cloud.google.com/stackdriver/estimating-bills).
  * [Pricing examples](https://cloud.google.com/stackdriver/observability-pricing-examples).
  * [Optimize costs with the Cost Explorer](https://docs.cloud.google.com/stackdriver/docs/costs/optimize-costs). The Cost Explorer provides current and historical visualizations of cost data and utilization metrics. As such, the data helps you identify optimization opportunities.



## Optimize

This section provides guidance about how to reduce or optimize costs associated with Cloud Logging, Cloud Trace, and Google Cloud Managed Service for Prometheus.

### Reduce your Cloud Logging costs

To reduce your Cloud Logging storage costs, configure exclusion filters on your log sinks to prevent low-value log entries from being streamed into your log buckets. You can configure a log sink to exclude all log entries that match an exclusion filter, or to exclude only a percentage of the matching log entries. Excluded log entries aren't streamed to your log buckets and they don't count against your storage allotment. To learn more, see [Log sink filters](https://docs.cloud.google.com/logging/docs/routing/overview#exclusions).

Cloud Logging storage costs apply only to log data that is stored in log buckets. You can configure your log sinks so that log data isn't stored in log buckets but is instead routed to one of the following destinations:

  * [Cloud Storage pricing](https://cloud.google.com/storage/pricing).
  * [BigQuery pricing](https://cloud.google.com/bigquery/pricing).
  * [Pub/Sub pricing](https://cloud.google.com/pubsub/pricing).



Cloud Logging doesn't charge to route log entries to the listed destinations. However, you might be charged when log entries are received by a destination.

For information about routing log data, see [Route logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/configure_export_v2).

### Optimize costs for Managed Service for Prometheus

Pricing for Managed Service for Prometheus is designed to be _controllable_. Because you are charged on a per-sample basis, you can use the following levers to control costs:

  * Sampling period: Changing the metric-scraping period from 15 seconds to 60 seconds can result in a 75% cost savings, without sacrificing cardinality. You can configure sampling periods on a per-job, per-target, or global basis.

  * Filtering: You can use filtering to reduce the number of samples sent to to the service's global datastore; for more information, see [Filtering exported metrics](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#filter-metrics). Use [metric-relabeling configs](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#metric_relabel_configs) in your Prometheus scrape configuration to drop metrics at ingestion time, based on label matchers.

  * Keep high-cardinality, low-value data local. You can run standard Prometheus alongside the managed service, using the same scape configs, and keep data locally that's not worth sending to the service's global datastore.




Pricing for Managed Service for Prometheus is designed to be _predictable_.

  * You are not penalized for having sparse histograms. Samples are counted only for the first non-zero value and then when the value for bucket _n_ is greater than the value in bucket _n-1_. For example, a histogram with values `10 10 13 14 14 14` counts as three samples, for the first, third and fourth buckets.

Depending on how many histograms you use, and what you use them for, the exclusion of unchanged buckets from pricing might typically result in 20% to 40% fewer samples being counted for billing purposes than the absolute number of histogram buckets would indicate.

  * By charging on a per-sample basis, you are not penalized for rapidly scaled and unscaled, preemptible, or ephemeral containers, like those created by HPA or GKE Autopilot.

If Managed Service for Prometheus charged on a per-metric basis, then you would pay for a full month's cardinality, all at once, each time a new container was spun up. With per-sample pricing, you pay only while the container is running.




**Queries, including alert queries**

All queries issued by the user, including queries issued when Prometheus recording rules are run, are charged through Cloud Monitoring API calls.

### Reduce your Trace usage

To control Trace span ingestion volume, you can manage your trace sampling rate to balance how many traces you need for performance analysis with your cost tolerance.

For high-traffic systems, most customers can sample at 1 in 1,000 transactions, or even 1 in 10,000 transactions, and still have enough information for performance analysis.

Sampling rate is configured with the [Cloud Trace client libraries](https://docs.cloud.google.com/trace/docs/client-libraries).

### Reduce your alerting bill

This section describes strategies you can use to reduce costs for alerting. For information about the pricing model, see [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing) and [Alerting pricing examples](https://cloud.google.com/stackdriver/observability-pricing-examples#alerting_policies).

#### See your estimated bill by using the in-UI pricing calculator

When you create or edit an alerting policy, Cloud Alerting displays the estimated cost of the policy. You can use this calculator to see how your estimated cost changes as you change the parameters of your alerting policy.

#### Use Metrics Explorer to verify the count of points returned

The number of points returned by the alerting policy query primarily depends on the cardinality of the output of your alerting policy query. To see the estimated cardinality of your alerting policy, do the following:

  * For a metric-threshold alerting condition, use Metrics Explorer to construct an identical query. Add a secondary transformation of **Count time series** by **None**.
  * For a PromQL alerting condition, copy the query into Metrics Explorer, then do the following: 
    * Break your query into separate clauses by splitting on every `>`, `<`, `>=`, `<=`, `==`, `!=`, `AND`, `OR`, and `UNLESS` operator.
    * Delete any clause that does not contain a metric, such as a numeric threshold value.
    * Wrap each clause in a `count()` function.
    * Sum the results.
  * For an MQL alerting condition, copy the query into Metrics Explorer. Remove the `| condition` line. Add a `| group_by [], .count` line to the end.

MQL is deprecated and cases requesting help with debugging billing issues might be declined by Cloud Customer Care.




#### Consolidate alerting policies to operate over more resources

Alerting charges a per-metric-reference cost, and each metric-threshold policy has one metric reference per condition. For this reason, when possible, use one alerting policy to monitor multiple resources instead of creating one alerting policy for each resource.

For example, assume that you have 100 VMs. Each VM generates a point each minute for the metric type `my_metric`. Here are two different ways you can monitor the points returned:

  * You create one alerting policy that has one condition and therefore has one metric reference. The condition monitors `my_metric` and aggregates data to the VM level. After aggregation, there is one point returned for each VM. Therefore, the condition generates 100 points returned per evaluation.

  * You create 100 alerting policies and each contains one condition and therefore has one metric reference. Each condition monitors the `my_metric` time series for one of the VMs, and it aggregates data to the VM level. Therefore, each condition returns one point per evaluation.




The second option, which creates 100 conditions (100 metric references), is more expensive than the first option, which only creates 1 condition (1 metric reference). Both options return 100 points per evaluation.

#### Aggregate to only the level that you need to alert on

A point is returned for each time series that is monitored by an alerting policy. Aggregating to higher levels of granularity results in higher costs than aggregating to lower levels of granularity. For example, aggregating to the Google Cloud project level is cheaper than aggregating to the cluster level, and aggregating to the cluster level is cheaper than aggregating to the cluster and namespace level.

For example, assume that you have 100 VMs. Each VM generates a point for the metric type `my_metric`. Each of your VMs belongs to one of five services. You decide to create one alerting policy that has one condition that monitors `my_metric`. Here are two different aggregation options:

  * You aggregate data to the service. After aggregation, each alerting policy execution returns one point for each service. Therefore, the condition returns 5 points per execution.

  * You aggregate data to the VM level. After aggregation, each alerting policy execution returns one point for each VM. Therefore, the condition returns 100 points per execution.




The second option, which returns 100 points per execution, is more expensive than the first option, which only returns five points per execution.

When you configure your alerting policies, choose aggregation levels that work best for your use case. For example, if you care about alerting on CPU utilization, then you might want to aggregate to the VM and CPU level. If you care about alerting on latency by service, then you might want to aggregate to the service level.

#### Don't alert on raw, unaggregated data

Monitoring uses a dimensional metrics system, where any metric has total [cardinality](https://docs.cloud.google.com/monitoring/api/v3/metric-model#cardinality) equal to the number of resources monitored multiplied by the number of label combinations on that metric. For example, if you have 100 VMs emitting a metric, and that metric has 10 labels with 10 values each, then your total cardinality is 100 * 10 * 10 = 10,000.

As a result of how cardinality scales, alerting on raw data can be extremely expensive. In the previous example, you have 10,000 points returned for each execution period. However, if you aggregate to the VM, then you have only 100 points returned per execution period, regardless of the label cardinality of the underlying data.

Alerting on raw data also puts you at risk for increased points returned when your metrics receive new labels. In the previous example, if a user adds a new label to your metric, then your total cardinality increases to 100 * 11 * 10 = 11,000 time series. In this case, your number of returned points increases by 1,000 each execution period even though your alerting policy is unchanged. If you instead aggregate to the VM, then, despite the increased underlying cardinality, you still have only 100 time series returned.

#### Filter out unnecessary responses

Configure your conditions to evaluate only data that's necessary for your alerting needs. If you wouldn't take action to fix something, then exclude it from your alerting policies. For example, you probably don't need to alert on an intern's development VM.

To reduce unnecessary alerts and costs, you can filter out time series that aren't important. You can use Google Cloud metadata labels to tag assets with categories and then filter out the unneeded metadata categories.

#### Use top-stream operators to reduce the number of points returned

If your condition uses a PromQL query, then you can use a top-streams operator to select a number of the points returned with the highest values:

  * PromQL: [`topk`](https://prometheus.io/docs/prometheus/latest/querying/operators/#aggregation-operators)



For example, a `topk(metric, 5)` clause in a PromQL query limits the number of points returned to five in each execution period.

Limiting to a top number of points might result in missing data and faulty alerts, such as:

  * If more than _N_ points violate your threshold, then you will miss data outside the top _N_ points.
  * If a violating point occurs outside the top _N_ points, then your alerts might auto-close despite the excluded points still violating the threshold.
  * Your condition queries might not show you important context such as baseline points that are functioning as intended.



To mitigate such risks, choose large values for _N_ and use the top-streams operator only in alerting policies that evaluate many time series, such as alerts for individual Kubernetes containers.

#### Increase the length of the execution period (PromQL only)

If your condition uses a PromQL query, then you can modify the length of your execution period by setting the [`evaluationInterval`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#PrometheusQueryLanguageCondition.FIELDS.evaluation_interval) field in the [condition](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#PrometheusQueryLanguageCondition).

Longer evaluation intervals result in fewer points returned per month; for example, a condition query with a 15-second interval runs twice as often as a query with a 30-second interval, and a query with a 1-minute interval runs half as often as a query with a 30-second interval.

**Note:** Other alerting policy conditions are fixed to a 30-second execution period.

#### Don't use "Unspecified Resource" (Log-based metrics only)

Alert conditions that use Log-based metrics allow you to set "Unspecified Resource" as your monitored resource type. When you do, your alert condition launches a separate query for every [monitored resource type](https://docs.cloud.google.com/monitoring/api/resources) in Cloud Monitoring. As each query bills a minimum of one point returned, not specifying the resource type causes a high points returned bill.

To lower your bill, choose a specific resource type instead of using "Unspecified Resource". This works because most Log-based metrics only appear in one resource type. If your Log-based metric appears in multiple resource types, you can make multiple alert policies or use multiple conditions in a single alert policy.

## Monitor

This section describes how to monitor your costs by creating [alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui). An alerting policy can monitor metric data and notify you when that data crosses a threshold.

### Monitor monthly log bytes ingested

To create an alerting policy that triggers when the number of log bytes written to your log buckets exceeds your user-defined limit for [Cloud Logging](https://docs.cloud.google.com/logging/docs), use the following settings.

#### Steps to create an [alerting policy](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui#create-policy).

To create an alerting policy, do the following:

  1. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. If you haven't created your notification channels and if you want to be notified, then click **Edit Notification Channels** and add your notification channels. Return to the **Alerting** page after you add your channels. 
  3. From the **Alerting** page, select **Create policy**.
  4. To select the resource, metric, and filters, expand the **Select a metric** menu and then use the values in the **New condition** table: 
     1. Optional: To limit the menu to relevant entries, enter the resource or metric name in the filter bar. 
     2. Select a **Resource type**. For example, select **VM instance**.
     3. Select a **Metric category**. For example, select **instance**.
     4. Select a **Metric**. For example, select **CPU Utilization**.
     5. Select **Apply**.
  5. Click **Next** and then configure the alerting policy trigger. To complete these fields, use the values in the **Configure alert trigger** table. 
  6. Click **Next**.
  7. Optional: To add notifications to your alerting policy, click **Notification channels**. In the dialog, select one or more notification channels from the menu, and then click **OK**.

To be notified when alerts are opened and closed, check **Notify on alert closure**. By default, notifications are sent only when alerts are opened.

  8. Optional: Update the **Alert autoclose duration**. This field determines when Monitoring closes alerts in the absence of metric data.
  9. Optional: Click **Documentation** , and then add any information that you want included in a notification message.
  10. Click **Alert name** and enter a name for the alerting policy.
  11. Click **Create Policy**.

**New condition**  
Field |   
Value  
---|---  
**Resource and Metric** | In the **Resources** menu, select **Global**.  
In the **Metric categories** menu, select **Logs-based metric**.  
In the **Metrics** menu, select **Monthly log bytes ingested**.   
**Filter** | None.  
**Across time series  
Time series aggregation** | `sum`  
  
**Rolling window** | `60 m`  
  
**Rolling window function** | `max`  
**Configure alert trigger**  
Field |   
Value  
---|---  
**Condition type** | `Threshold`  
**Alert trigger** | `Any time series violates`  
**Threshold position** | `Above threshold`  
**Threshold value** | You determine the acceptable value.  
**Retest window** | Minimum acceptable value is 30 minutes.  
  
### Monitor total metrics ingested

It can't create an alert based on the monthly metrics ingested. However, you can create an alert for your Cloud Monitoring costs. For information, see Configure a billing alert.

### Monitor monthly trace spans ingested

To create an alerting policy that triggers when your monthly [Cloud Trace](https://docs.cloud.google.com/trace/docs) spans ingested exceeds a user-defined limit, use the following settings.

#### Steps to create an [alerting policy](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui#create-policy).

To create an alerting policy, do the following:

  1. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. If you haven't created your notification channels and if you want to be notified, then click **Edit Notification Channels** and add your notification channels. Return to the **Alerting** page after you add your channels. 
  3. From the **Alerting** page, select **Create policy**.
  4. To select the resource, metric, and filters, expand the **Select a metric** menu and then use the values in the **New condition** table: 
     1. Optional: To limit the menu to relevant entries, enter the resource or metric name in the filter bar. 
     2. Select a **Resource type**. For example, select **VM instance**.
     3. Select a **Metric category**. For example, select **instance**.
     4. Select a **Metric**. For example, select **CPU Utilization**.
     5. Select **Apply**.
  5. Click **Next** and then configure the alerting policy trigger. To complete these fields, use the values in the **Configure alert trigger** table. 
  6. Click **Next**.
  7. Optional: To add notifications to your alerting policy, click **Notification channels**. In the dialog, select one or more notification channels from the menu, and then click **OK**.

To be notified when alerts are opened and closed, check **Notify on alert closure**. By default, notifications are sent only when alerts are opened.

  8. Optional: Update the **Alert autoclose duration**. This field determines when Monitoring closes alerts in the absence of metric data.
  9. Optional: Click **Documentation** , and then add any information that you want included in a notification message.
  10. Click **Alert name** and enter a name for the alerting policy.
  11. Click **Create Policy**.

**New condition**  
Field |   
Value  
---|---  
**Resource and Metric** | In the **Resources** menu, select **Global**.  
In the **Metric categories** menu, select **Billing**.  
In the **Metrics** menu, select **Monthly trace spans ingested**.   
**Filter** |   
**Across time series  
Time series aggregation** | `sum`  
  
**Rolling window** | `60 m`  
  
**Rolling window function** | `max`  
**Configure alert trigger**  
Field |   
Value  
---|---  
**Condition type** | `Threshold`  
**Alert trigger** | `Any time series violates`  
**Threshold position** | `Above threshold`  
**`Threshold value`** | You determine the acceptable value.  
**Retest window** | Minimum acceptable value is 30 minutes.  
  
### Configure a billing alert

To be notified if your billable or forecasted charges exceed a budget, create an alert by using the **Budgets and alerts** page of the Google Cloud console:

  1. In the Google Cloud console, go to the **Billing** page: 

[Go to **Billing**](https://console.cloud.google.com/billing)

You can also find this page by using the search bar.

If you have more than one Cloud Billing account, then do one of the following:

     * To manage Cloud Billing for the current project, select **Go to linked billing account**.
     * To locate a different Cloud Billing account, select **Manage billing accounts** and choose the account for which you'd like to set a budget.
  2. In the Billing navigation menu, select **Budgets & alerts**.
  3. Click add_box **Create budget**.
  4. Complete the budget dialog. In this dialog, you select Google Cloud projects and products, and then you create a budget for that combination. By default, you are notified when you reach 50%, 90%, and 100% of the budget. For complete documentation, see [Set budgets and budget alerts](https://docs.cloud.google.com/billing/docs/how-to/budgets). **Note:** In the billing dialog, use the following settings: 
     * To create an alert on Cloud Logging usage, select **Cloud Logging**
     * To create an alert on Cloud Monitoring usage, select **Stackdriver Monitoring**
     * To create an alert on Cloud Trace usage, select **Stackdriver Trace**



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
