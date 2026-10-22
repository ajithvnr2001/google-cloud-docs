---
url: https://docs.cloud.google.com/monitoring/alerts/cost-control/
title: Manage alerting costs \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:01.201877+00:00
---

# Manage alerting costs  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/alerts/cost-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Manage alerting costs Stay organized with collections  Save and categorize content based on your preferences. 

You can manage the costs of your Cloud Monitoring alerting policies by consolidating policies and limiting the number of time-series points that your queries return. To reduce the points returned, you can aggregate and filter monitored time series and adjust PromQL evaluation intervals. You can also see your estimated bill update as you change policy parameters.

For information about the pricing model, see [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing) and [Alerting pricing examples](https://cloud.google.com/stackdriver/observability-pricing-examples#alerting_policies).

## See your estimated bill by using the in-UI pricing calculator

When you create or edit an alerting policy, Cloud Alerting displays the estimated cost of the policy. You can use this calculator to see how your estimated cost changes as you change the parameters of your alerting policy.

## Use Metrics Explorer to verify the count of points returned

The number of points returned by the alerting policy query primarily depends on the cardinality of the output of your alerting policy query. To see the estimated cardinality of your alerting policy, do the following:

  * For a metric-threshold alerting condition, use Metrics Explorer to construct an identical query. Add a secondary transformation of **Count time series** by **None**.
  * For a PromQL alerting condition, copy the query into Metrics Explorer, then do the following: 
    * Break your query into separate clauses by splitting on every `>`, `<`, `>=`, `<=`, `==`, `!=`, `AND`, `OR`, and `UNLESS` operator.
    * Delete any clause that does not contain a metric, such as a numeric threshold value.
    * Wrap each clause in a `count()` function.
    * Sum the results.
  * For an MQL alerting condition, copy the query into Metrics Explorer. Remove the `| condition` line. Add a `| group_by [], .count` line to the end.

MQL is deprecated and cases requesting help with debugging billing issues might be declined by Cloud Customer Care.




## Consolidate alerting policies to operate over more resources

Alerting charges a per-metric-reference cost, and each metric-threshold policy has one metric reference per condition. For this reason, when possible, use one alerting policy to monitor multiple resources instead of creating one alerting policy for each resource.

For example, assume that you have 100 VMs. Each VM generates a point each minute for the metric type `my_metric`. Here are two different ways you can monitor the points returned:

  * You create one alerting policy that has one condition and therefore has one metric reference. The condition monitors `my_metric` and aggregates data to the VM level. After aggregation, there is one point returned for each VM. Therefore, the condition generates 100 points returned per evaluation.

  * You create 100 alerting policies and each contains one condition and therefore has one metric reference. Each condition monitors the `my_metric` time series for one of the VMs, and it aggregates data to the VM level. Therefore, each condition returns one point per evaluation.




The second option, which creates 100 conditions (100 metric references), is more expensive than the first option, which only creates 1 condition (1 metric reference). Both options return 100 points per evaluation.

## Aggregate to only the level that you need to alert on

A point is returned for each time series that is monitored by an alerting policy. Aggregating to higher levels of granularity results in higher costs than aggregating to lower levels of granularity. For example, aggregating to the Google Cloud project level is cheaper than aggregating to the cluster level, and aggregating to the cluster level is cheaper than aggregating to the cluster and namespace level.

For example, assume that you have 100 VMs. Each VM generates a point for the metric type `my_metric`. Each of your VMs belongs to one of five services. You decide to create one alerting policy that has one condition that monitors `my_metric`. Here are two different aggregation options:

  * You aggregate data to the service. After aggregation, each alerting policy execution returns one point for each service. Therefore, the condition returns 5 points per execution.

  * You aggregate data to the VM level. After aggregation, each alerting policy execution returns one point for each VM. Therefore, the condition returns 100 points per execution.




The second option, which returns 100 points per execution, is more expensive than the first option, which only returns five points per execution.

When you configure your alerting policies, choose aggregation levels that work best for your use case. For example, if you care about alerting on CPU utilization, then you might want to aggregate to the VM and CPU level. If you care about alerting on latency by service, then you might want to aggregate to the service level.

## Don't alert on raw, unaggregated data

Monitoring uses a dimensional metrics system, where any metric has total [cardinality](https://docs.cloud.google.com/monitoring/api/v3/metric-model#cardinality) equal to the number of resources monitored multiplied by the number of label combinations on that metric. For example, if you have 100 VMs emitting a metric, and that metric has 10 labels with 10 values each, then your total cardinality is 100 * 10 * 10 = 10,000.

As a result of how cardinality scales, alerting on raw data can be extremely expensive. In the previous example, you have 10,000 points returned for each execution period. However, if you aggregate to the VM, then you have only 100 points returned per execution period, regardless of the label cardinality of the underlying data.

Alerting on raw data also puts you at risk for increased points returned when your metrics receive new labels. In the previous example, if a user adds a new label to your metric, then your total cardinality increases to 100 * 11 * 10 = 11,000 time series. In this case, your number of returned points increases by 1,000 each execution period even though your alerting policy is unchanged. If you instead aggregate to the VM, then, despite the increased underlying cardinality, you still have only 100 time series returned.

## Filter out unnecessary responses

Configure your conditions to evaluate only data that's necessary for your alerting needs. If you wouldn't take action to fix something, then exclude it from your alerting policies. For example, you probably don't need to alert on an intern's development VM.

To reduce unnecessary alerts and costs, you can filter out time series that aren't important. You can use Google Cloud metadata labels to tag assets with categories and then filter out the unneeded metadata categories.

## Use top-stream operators to reduce the number of points returned

If your condition uses a PromQL query, then you can use a top-streams operator to select a number of the points returned with the highest values:

  * PromQL: [`topk`](https://prometheus.io/docs/prometheus/latest/querying/operators/#aggregation-operators)



For example, a `topk(metric, 5)` clause in a PromQL query limits the number of points returned to five in each execution period.

Limiting to a top number of points might result in missing data and faulty alerts, such as:

  * If more than _N_ points violate your threshold, then you will miss data outside the top _N_ points.
  * If a violating point occurs outside the top _N_ points, then your alerts might auto-close despite the excluded points still violating the threshold.
  * Your condition queries might not show you important context such as baseline points that are functioning as intended.



To mitigate such risks, choose large values for _N_ and use the top-streams operator only in alerting policies that evaluate many time series, such as alerts for individual Kubernetes containers.

## Increase the length of the execution period (PromQL only)

If your condition uses a PromQL query, then you can modify the length of your execution period by setting the [`evaluationInterval`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#PrometheusQueryLanguageCondition.FIELDS.evaluation_interval) field in the [condition](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies#PrometheusQueryLanguageCondition).

Longer evaluation intervals result in fewer points returned per month; for example, a condition query with a 15-second interval runs twice as often as a query with a 30-second interval, and a query with a 1-minute interval runs half as often as a query with a 30-second interval.

**Note:** Other alerting policy conditions are fixed to a 30-second execution period.

## Don't use "Unspecified Resource" (Log-based metrics only)

Alert conditions that use Log-based metrics allow you to set "Unspecified Resource" as your monitored resource type. When you do, your alert condition launches a separate query for every [monitored resource type](https://docs.cloud.google.com/monitoring/api/resources) in Cloud Monitoring. As each query bills a minimum of one point returned, not specifying the resource type causes a high points returned bill.

To lower your bill, choose a specific resource type instead of using "Unspecified Resource". This works because most Log-based metrics only appear in one resource type. If your Log-based metric appears in multiple resource types, you can make multiple alert policies or use multiple conditions in a single alert policy.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
