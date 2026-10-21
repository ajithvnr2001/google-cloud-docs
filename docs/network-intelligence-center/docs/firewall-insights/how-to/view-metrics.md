---
url: https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/view-metrics/
title: View Firewall Insights metrics \u00a0|\u00a0 Network Intelligence Center - Firewall Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:56:13.059395+00:00
---

# View Firewall Insights metrics  |  Network Intelligence Center - Firewall Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/view-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Firewall Insights ](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/using-firewall-insights)



Send feedback 

#  View Firewall Insights metrics Stay organized with collections  Save and categorize content based on your preferences. 

Firewall Insights metrics let you analyze how your firewall rules are used. You can view the metrics by using Cloud Monitoring and the Google Cloud console.

The following metrics help you track your firewall usage:

  * _Firewall hit count metrics_ show you the number of times that a firewall rule was used to allow or deny traffic.
  * _Firewall last used metrics_ show you the last time that a particular firewall rule was used to allow or deny traffic.



Note the following aspects about Firewall Insights metrics:

  * The metrics are derived from Firewall Rules Logging.
  * The metrics are available only for rules that have Firewall Rules Logging enabled and are accurate only for the time during which Firewall Rules Logging is enabled.
  * Firewall metrics are generated only for traffic that fits the specifications for Firewall Rules Logging. For example, data is logged and metrics are generated only for TCP and UDP traffic. For a complete list of criteria, see [Specifications](https://docs.cloud.google.com/vpc/docs/firewall-rules-logging#specifications) in the _Firewall Rules Logging overview_.



You can construct arbitrary queries over Firewall Insights metrics by using the [`projects.timeSeries.list` request method](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list) in the Cloud Monitoring version 3 API documentation.

Firewall Insights gathers metrics data for the last time that a firewall rule was applied to allow or deny traffic (timestamp) and for the number of hits on a firewall rule for the retention period.

  * `firewallinsights.googleapis.com/subnet/firewall_hit_count`
  * `firewallinsights.googleapis.com/subnet/firewall_last_used_timestamp`
  * `firewallinsights.googleapis.com/vm/firewall_hit_count`
  * `firewallinsights.googleapis.com/vm/firewall_last_used_timestamp`



The metric for tracking firewall hit counts is defined per virtual machine (VM) instance and per Virtual Private Cloud (VPC) subnet.

Per-instance (VM) metrics provide hit count and last used timestamp information for the network interface of a VM. Per-subnet metrics provide hit count information for individual firewall rules.

Use the following resources to access Firewall Insights metrics data:

  * View metrics for Firewall Insights on the [Google Cloud metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#gcp-firewallinsights) page.
  * For an overview of metrics, time series, and resources, see the [metric model](https://docs.cloud.google.com/monitoring/api/v3/metrics) in the Cloud Monitoring version 3 API documentation.
  * For information about how to read these metrics, see [Reading metric data](https://docs.cloud.google.com/monitoring/custom-metrics/reading-metrics).



## Required roles and permissions

To get the permission that you need to manage and export insights, ask your administrator to grant you the following IAM roles on your project: 

  * [Firewall Recommender Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/recommender#recommender.firewallAdmin) (`roles/recommender.firewallAdmin`)
  * [Firewall Recommender Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/recommender#recommender.firewallViewer) (`roles/recommender.firewallViewer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `recommender.computeFirewallInsights.list` permission, which is required to manage and export insights. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View firewall hit count metrics

The `firewall_hit_count` metric tracks the number of times that a firewall rule is used to allow or deny traffic.

For each firewall rule, Cloud Monitoring stores data for the `firewall_hit_count` metric only if the rule had hits because of TCP or UDP traffic. That is, Cloud Monitoring does not store data about rules _that had no hits_.

You can view the data derived from this metric on the **[Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)** page in the Google Cloud console. The hit count metric is from the last six weeks, collected only while Firewall Rules Logging is enabled. The data on the **Firewall policies** page might not be identical to the `firewall_hit_count` metric data that is stored in Cloud Monitoring.

This behavior differs from the [`allow rules with no hits` insight](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/concepts/insights-categories-states#no-hits). When this insight identifies firewall rules with no hits, it omits firewall rules that are configured to allow traffic other than TCP or UDP, even if those rules also allow TCP or UDP traffic.

## View firewall last used metrics

By using the Metrics Explorer in Cloud Monitoring, you can see the last time a particular firewall rule was used to allow or deny traffic by viewing the `firewall_last_used_timestamp` metric. This metric helps you identify which firewall rules haven't been used recently.

On the **[Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)** page in the Google Cloud console, you can see when you last used a firewall rule in the past six weeks or for whatever duration Firewall Rules Logging has been enabled, whichever is less. If the last hit occurred _before_ the past six weeks or _before_ Firewall Rules Logging was enabled, the `last hit` time is shown as `—`.

## Reporting frequency and retention

The `firewall rule hit count` metric is exported to Monitoring every minute. Monitoring data retention is two years.

## Filtering and aggregation

For each firewall rule, by aggregating the hit counts for VM instances, you can observe the overall hit counts that accumulate for all the traffic flowing in your VPC network.

For example, see [Detect sudden increases in the hit count for `deny` firewall rules](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/review-optimize#detect-increase-hit-count).

## Use Monitoring dashboards and alerts

You can use Monitoring dashboards and their associated charts to visualize the data for the Firewall Insights metrics described in the preceding sections.

To monitor these metrics in Monitoring, you can [create custom dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards#custom_dashboards). You can also [add alerts](https://docs.cloud.google.com/monitoring/alerts/using-alerting-api) based on these metrics.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
