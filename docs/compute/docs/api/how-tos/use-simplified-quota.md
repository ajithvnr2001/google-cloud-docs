---
url: https://docs.cloud.google.com/compute/docs/api/how-tos/use-simplified-quota/
title: Use simplified API quota metrics in Cloud Monitoring \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:01:13.118044+00:00
---

# Use simplified API quota metrics in Cloud Monitoring  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/api/how-tos/use-simplified-quota/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Use simplified API quota metrics in Cloud Monitoring Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to use the simplified Compute Engine API quota metrics in your Cloud Monitoring dashboards, alerting policies, and queries. 

## Simplified API quota metrics

To improve the discoverability and manageability of Compute Engine API quota, Google Cloud has reduced the number of quota metrics by consolidating metrics into fewer quota groups. These simplified quota metrics also offer higher limits for each quota group.

### Legacy and simplified API quota metrics

The following table lists the legacy API quota metrics and their simplified equivalent metrics:

**Legacy API quota metrics** | **Simplified API quota metric**  
---|---  
`compute.googleapis.com/list_requests` | `compute.googleapis.com/global_reads`  
Read requests per minute  
`compute.googleapis.com/read_requests`  
`compute.googleapis.com/heavy_weight_read_requests`  
`compute.googleapis.com/default`  
Legacy quota metric for methods that list Compute Engine resources.  
`compute.googleapis.com/get_macsec_config_requests`  
`compute.googleapis.com/license_verification_requests`  
`compute.googleapis.com/default`  
Legacy quota metric for global methods that create, modify, or delete Compute Engine resources. | `compute.googleapis.com/global_writes`  
Mutation requests per minute  
`compute.googleapis.com/global_resource_write_requests`  
`compute.googleapis.com/heavy_weight_write_requests`  
`compute.googleapis.com/regional_v2_public_advertised_prefixes_delete_requests`  
`compute.googleapis.com/regional_v2_public_advertised_prefixes_create_requests`  
`compute.googleapis.com/address_move_requests`  
`compute.googleapis.com/project_set_common_instance_metadata_requests`  
`compute.googleapis.com/regional_v2_public_advertised_prefixes_announce_requests`  
`compute.googleapis.com/license_insert_requests`  
`compute.googleapis.com/heavy_weight_read_requests_per_region` | `compute.googleapis.com/reads_per_region`  
Read requests per minute per region  
`compute.googleapis.com/read_requests_per_region`  
`compute.googleapis.com/list_requests_per_region`  
`compute.googleapis.com/default_per_region`  
Legacy quota metric for regional and zonal methods that list Compute Engine resources.  
`compute.googleapis.com/license_verification_requests_per_region`  
`compute.googleapis.com/instance_list_referrers_requests_per_region`  
`compute.googleapis.com/operation_read_requests_per_region`  
`compute.googleapis.com/network_endpoint_list_requests_per_region`  
`compute.googleapis.com/regional_network_endpoint_list_requests_per_region`  
`compute.googleapis.com/get_serial_port_output_requests_per_region`  
`compute.googleapis.com/read_requests`  
`compute.googleapis.com/heavy_weight_write_requests_per_region` | `compute.googleapis.com/writes_per_region`  
Mutation requests per minute per region  
`compute.googleapis.com/default_per_region`  
Legacy quota metric for regional and zonal methods that create, modify, or delete Compute Engine resources.  
`compute.googleapis.com/global_resource_write_requests_per_region`  
`compute.googleapis.com/network_endpoint_write_requests_per_region`  
`compute.googleapis.com/regional_network_endpoint_write_requests_per_region`  
`compute.googleapis.com/regional_public_delegated_prefixes_create_requests_per_region`  
`compute.googleapis.com/address_move_requests_per_region`  
`compute.googleapis.com/simulate_maintenance_event_requests_per_region`  
`compute.googleapis.com/regional_public_delegated_prefixes_delete_requests_per_region`  
`compute.googleapis.com/regional_public_delegated_prefixes_announce_requests_per_region`  
  
`compute.googleapis.com/recommend_locations_requests_per_region` | `compute.googleapis.com/recommend_locations_per_region`  
RegionInstances RecommendLocations requests per minute per region  
`compute.googleapis.com/cache_invalidation_requests` | `compute.googleapis.com/global_cache_invalidation_requests`  
Cache invalidation requests per minute  
  
## Use the simplified metrics in Cloud Monitoring dashboards

To monitor Compute Engine API usage against the simplified API metrics, add filters for these metrics in your Cloud Monitoring dashboards, alerts, and queries.

### Create a dashboard that uses simplified API quota metrics

To create a dashboard that uses simplified metrics, do the following:

  1. In the Google Cloud console, go to **Monitoring** :

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  2. In the navigation pane, select **Dashboards**.

  3. Click **Create custom dashboard**.

  4. In the dashboard toolbar, click **Add widget** and select a widget type (for example, **Line chart**). The **Configure widget** page opens.

  5. In the **Select a metric** section, do the following:

     1. Select **Consumer Quota** for the resource.
     2. Select **Quota** for the metric category.
     3. Select **Rate quota usage** for the metric and then click **Apply**.
  6. In the **Add filter** section, use the `quota_metric` filter and select the corresponding simplified API quota metric. To find the simplified metric, see Legacy and simplified API quota metrics.

  7. Click **Apply** to add the widget to the dashboard.

  8. In the toolbar, click **Save** to save the dashboard.




### Modify a dashboard that uses a legacy quota metric

To update a dashboard that contains a legacy metric, do the following:

  1. In the Google Cloud console, go to **Monitoring** :

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  2. In the navigation pane, select **Dashboards**.

  3. Open the **dashboard** containing the chart that needs an update.

  4. Click **Edit**.

  5. Find the widget you want to update and edit it.

  6. In the **Select a metric** section, update the filter containing the legacy metric:

     1. In the **Filter** field, select `quota_metric`.
     2. In the **Value** field, update the current value to the corresponding simplified API quota metric. To find the replacement for your legacy metric, see Legacy and simplified API quota metrics. For example, change `compute.googleapis.com/read_requests` to `compute.googleapis.com/global_reads`.
  7. To apply your changes, click **Apply**.




## Use the simplified API quota metrics in Cloud Monitoring alerting policies

To monitor Compute Engine API usage against the simplified API metrics, add filters for these metrics in your Cloud Monitoring alerting policies.

### Create an alerting policy that uses simplified API quota metrics

To create an alerting policy that uses simplified metrics, do the following:

  1. In the Google Cloud console, go to **Monitoring** :

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  2. In the navigation pane, select **Alerting**.

  3. Click **Create policy**.

  4. In the **Select a metric** section, do the following:

     1. Select **Consumer Quota** for the resource.
     2. Select **Quota** for the metric category.
     3. Select **Rate quota usage** for the metric and then click **Apply**.
  5. In the **Add filter** section, use the `quota_metric` filter and select the corresponding simplified API quota metric. To find the simplified metric, see Legacy and simplified API quota metrics.

  6. Configure the condition, notification channels, and documentation as needed.

  7. Click **Save policy**.




You can also use the Google Cloud Terraform Provider to create alerting policies in your Google Cloud project. For more information, see [Create alerting policies with Terraform](https://docs.cloud.google.com/monitoring/alerts/terraform).

### Modify an alerting policy that uses a legacy quota metric

To update an existing alert policy that uses a legacy quota metric, do the following:

  1. In the Google Cloud console, go to **Monitoring** :

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  2. In the navigation pane, select **Alerting**. The Alerting page displays panes that list summary information, incidents, and alerting policies.

  3. To edit an existing policy, click the policy name under **Policies**.

  4. In the **Select a metric** section, update the filter containing the legacy metric:

     1. In the **Filter** field, select `quota_metric`.
     2. In the **Value** field, update the value to the corresponding simplified API quota metric. To find the replacement for your legacy metric, see Legacy and simplified API quota metrics. For example, change `compute.googleapis.com/read_requests` to `compute.googleapis.com/global_reads`.
  5. Click **Done** to save changes in the filter.

  6. Click **Save policy**.




### Use simplified quota metrics in Cloud Monitoring queries

To update a PromQL-based alerting policy or a chart in a dashboard, use the Query Editor and edit the query filter. For more information, see [Use the code editor for PromQL](https://docs.cloud.google.com/monitoring/promql/promql-in-monitoring).

To update your query, replace the legacy metric name in the `quota_metric` filter with the corresponding simplified metric name.

Example 1:

Query that uses a legacy metric:
    
    
    rate(serviceruntime_googleapis_com:quota_rate_net_usage{monitored_resource="consumer_quota", \
    quota_metric=~"**compute.googleapis.com/read_requests** "}[1m])

Modified query using simplified metric:
    
    
    rate(serviceruntime_googleapis_com:quota_rate_net_usage{monitored_resource="consumer_quota", \
    quota_metric=~"**compute.googleapis.com/global_reads** "}[1m])

Example 2:

Query that uses a legacy metric:
    
    
    rate(serviceruntime_googleapis_com:quota_rate_net_usage{monitored_resource="consumer_quota", \
    quota_metric=~"**compute.googleapis.com/heavy_weight_write_requests_per_region** "}[1m])

Modified query using simplified metric:
    
    
    rate(serviceruntime_googleapis_com:quota_rate_net_usage{monitored_resource="consumer_quota", \
    quota_metric=~"**compute.googleapis.com/writes_per_region** "}[1m])

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
