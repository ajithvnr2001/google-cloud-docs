---
url: https://docs.cloud.google.com/monitoring/promql/
title: PromQL for Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:22.907923+00:00
---

# PromQL for Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/promql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  PromQL for Cloud Monitoring Stay organized with collections  Save and categorize content based on your preferences. 

You can use [Prometheus Query Language (PromQL)](https://prometheus.io/docs/prometheus/latest/querying/basics/) in Cloud Monitoring as an alternative to the Metrics Explorer menu-driven interface for creating charts and dashboards. 

PromQL lets you query and chart Cloud Monitoring data from the following sources:

  * Google Cloud services, such as Google Kubernetes Engine or Compute Engine, that write metrics described in the lists of [Cloud Monitoring system metrics](https://docs.cloud.google.com/monitoring/api/metrics).
  * User-defined metrics, such as [log-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics) and Cloud Monitoring [user-defined metrics](https://docs.cloud.google.com/monitoring/custom-metrics).
  * Google Cloud Managed Service for Prometheus, the fully managed multi-cloud solution for [Prometheus](https://prometheus.io) from Google Cloud. For information about the managed service, including support for PromQL, see [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus).



Third-party tools such as Grafana can also chart metric data ingested into Cloud Monitoring. Available metrics include metrics from Managed Service for Prometheus and Cloud Monitoring metrics documented in the [lists of metrics](https://docs.cloud.google.com/monitoring/api/metrics). For information about setting up Grafana and other tools based on the Prometheus API, see the Managed Service for Prometheus documentation about [Grafana](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query#ui-grafana). Additionally, you can [import your Grafana dashboards into Cloud Monitoring](https://docs.cloud.google.com/monitoring/dashboards/import-grafana-dashboards).

## Querying Cloud Monitoring metrics by using PromQL

Cloud Monitoring metrics can be queried by using the [UTF-8 spec for PromQL](https://prometheus.io/docs/guides/utf8/#querying). UTF-8 metric names must be quoted and moved inside the braces. Label names must also be quoted if they contain legacy-incompatible characters. For the Cloud Monitoring metric `kubernetes.io/container/cpu/limit_utilization`, the following queries are equivalent:

  * `{"kubernetes.io/container/cpu/limit_utilization", pod_name="foo"}`
  * `{__name__="kubernetes.io/container/cpu/limit_utilization", pod_name="foo"}`
  * `{"__name__"="kubernetes.io/container/cpu/limit_utilization", "pod_name"="foo"}`



Cloud Monitoring [distribution-valued metrics](https://docs.cloud.google.com/monitoring/api/v3/kinds-and-types) can be queried like Prometheus histograms, with the `_count`, `_sum`, or `_bucket` suffix appended to the metric name.

You can use [metadata labels](https://docs.cloud.google.com/monitoring/api/v3/metric-model#meta-labels) in PromQL just like any other label, but like metric names, metadata labels also need to be made PromQL-compatible. The syntax for referring to a metadata system label `version` is `metadata_system_version`, and the syntax for the metadata user label `version` is `metadata_user_version`. Well-formed PromQL queries using metadata labels might look like the following:

  * `{"compute.googleapis.com/instance/cpu/utilization", monitored_resource="gce_instance", metadata_user_env="prod"}`
  * `sum("compute.googleapis.com/instance/cpu/utilization") by (metadata_system_region)`
  * `sum("compute.googleapis.com/instance/cpu/utilization") by (metadata_user_env)`
  * `{"compute.googleapis.com/instance/uptime_total", "metadata_user_i-love.special/chars"="yes"}`
  * `sum("compute.googleapis.com/instance/uptime_total") by ("metadata_user_i-love.special/chars")`



If your metadata label key contains special characters other than the `_` character, then you have to wrap your label key in double quotes (`"`) according to [PromQL UTF-8 specification](https://prometheus.io/docs/guides/utf8/#querying). You still need to prefix your metadata label with the string `metadata_user_`.

Charts and dashboards made before UTF-8 compatibility query Cloud Monitoring metrics by converting their names into legacy PromQL-compatible equivalents. For more information about legacy PromQL conversion rules, see Mapping Cloud Monitoring metrics to legacy PromQL.

## Accessing PromQL in Cloud Monitoring

You can use PromQL from the **Code** tab on the following pages in the Google Cloud console:

  * Metrics Explorer
  * **Add Chart** when creating custom dashboards



For information about accessing and using the editor, see [Using the PromQL editor](https://docs.cloud.google.com/monitoring/promql/promql-in-monitoring). 

## PromQL rules and alerts

You can use PromQL to create alerting policies for any metric in Cloud Monitoring. Alerting policies can also filter and group time series by metric and resource labels. For more information, see [PromQL-based alerting policies](https://docs.cloud.google.com/monitoring/promql/promql-in-alerting).

**Note:** Don't use metadata labels in alerting policies.

You can also use PromQL to create recording and alerting rules on any metric in Cloud Monitoring by using Prometheus-style in-cluster alerting in Cloud Monitoring. For more information, see [Managed rule evaluation and alerting](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/rules-managed) or [Self-deployed rule evaluation and alerting](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/rules-unmanaged). 

## Learning PromQL

To learn the basics of using PromQL, we recommend consulting open source documentation. The following resources can help you get started:

  * [Querying Prometheus](https://prometheus.io/docs/prometheus/latest/querying/basics/)
  * [Query examples](https://prometheus.io/docs/prometheus/latest/querying/examples/)
  * [PromQL cheat sheet](https://promlabs.com/promql-cheat-sheet/)



## Specifying a monitored resource type

When a Cloud Monitoring metric is associated with only a single [Cloud Monitoring monitored resource type](https://docs.cloud.google.com/monitoring/api/resources), PromQL querying will work without manually specifying a resource type. However, some metrics within Cloud Monitoring, including some system metrics and many of those generated by [log-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics), map to more than one resource type. If you are using one of these metrics, especially log-based metrics, then you have to explicitly specify the resource type. 

You can see which monitored resource types map to a metric by doing one of the following:

  * For Google-curated metrics, you can consult the lists of metrics available, including [Google Cloud metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp) and [Kubernetes metrics](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes). Each entry in the documentation lists the associated monitored resource types in the first column of each entry below the type. If no monitored resource types are listed, then the metric can be associated with any type.
  * In [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer), you can do the following:

    1. Enter your metric name in the **Select a metric** field and then navigate through the menus to select the metric. The resource menu lists valid resource types for that metric, for example, "VM Instance".
    2. In the toolbar of the query-builder pane, select the button whose name is **< > PromQL**.

The displayed PromQL query shows the resource type as the value of the `monitored_resource` field. In particular, this method is useful for metrics that can be associated with many monitored resource types, for example log-based metrics, custom metrics, or any user-defined metric.




If a metric is associated with more than one resource type, then you must specify the resource type in your PromQL query. There is a special label, `monitored_resource`, that you can use to select the resource type.

[Monitored resource types](https://docs.cloud.google.com/monitoring/api/resources) are in most cases a short string, like `gce_instance`, but occasionally they appear as full URIs, like `monitoring.googleapis.com/MetricIngestionAttribution`. Well-formed PromQL queries might look like the following:

  * `logging_googleapis_com:byte_count{monitored_resource="k8s_container"}`
  * `custom_googleapis_com:opencensus_opencensus_io_http_server_request_count_by_method{monitored_resource="global"}`
  * `loadbalancing_googleapis_com:l3_external_egress_bytes_count{monitored_resource="loadbalancing.googleapis.com/ExternalNetworkLoadBalancerRule"}`



The value of `""` for the `monitored_resource` label is special and refers to the default [`prometheus_target`](https://docs.cloud.google.com/monitoring/api/resources#tag_prometheus_target) resource type that is used for Cloud Monitoring metrics.

If you don't use the `monitored_resource` label when it is needed, then you receive the following error:

`metric is configured to be used with more than one monitored resource type; series selector must specify a label matcher on monitored resource name`

## Resolving label conflicts

In Cloud Monitoring, labels can belong to either the metric or the resource. If a metric label has the same key name as a resource label, you can refer to the metric label specifically by adding the prefix `metric_` to the label key name in your query.

For example, suppose you have a resource label and a metric label both named `pod_name` in the metric `example.googleapis.com/user/widget_count`.

  * To filter on the value of the resource label, use  
`example_googleapis_com:user_widget_count{pod_name="RESOURCE_LABEL_VALUE"}`

  * To filter on the value of the metric label, use  
`example_googleapis_com:user_widget_count{metric_pod_name="METRIC_LABEL_VALUE"}`




## Mapping Cloud Monitoring metric names to legacy PromQL

Cloud Monitoring metric names include two components, a domain (such as `compute.googleapis.com/`) and a path (such as `instance/disk/max_read_ops_count`). Because legacy PromQL only supports the special characters `:` and `_`, you must apply the following rules to make Monitoring metric names compatible with legacy PromQL:

  * Replace the first `/` with `:`.
  * Replace all other special characters (including `.` and other `/` characters) with `_`.



The following table lists some metric names and their legacy PromQL equivalents:

Cloud Monitoring metric name | Legacy PromQL metric name  
---|---  
`kubernetes.io/container/cpu/limit_cores` | `kubernetes_io:container_cpu_limit_cores`  
`compute.googleapis.com/instance/cpu/utilization` | `compute_googleapis_com:instance_cpu_utilization`  
`logging.googleapis.com/log_entry_count` | `logging_googleapis_com:log_entry_count`  
`custom.googleapis.com/opencensus/opencensus.io/  
http/server/request_count_by_method` | `custom_googleapis_com:opencensus_opencensus_io_  
http_server_request_count_by_method`  
`agent.googleapis.com/disk/io_time` | `agent_googleapis_com:disk_io_time`  
  
Cloud Monitoring [distribution-valued metrics](https://docs.cloud.google.com/monitoring/api/v3/kinds-and-types) can be queried like Prometheus histograms, with the `_count`, `_sum`, or `_bucket` suffix appended to the metric name:

Cloud Monitoring metric name | Legacy PromQL metric names  
---|---  
`networking.googleapis.com/vm_flow/rtt` | `networking_googleapis_com:vm_flow_rtt_sum`  
`networking_googleapis_com:vm_flow_rtt_count`  
`networking_googleapis_com:vm_flow_rtt_bucket`  
  
## PromQL compatibility

PromQL for Cloud Monitoring might function slightly differently from upstream PromQL.

[PromQL](https://prometheus.io/docs/prometheus/latest/querying/basics/) queries in Cloud Monitoring are partially evaluated at the [Monarch](https://research.google/pubs/monarch-googles-planet-scale-in-memory-time-series-database/) backend by using an internal query language, and there are some known differences in query results. Other than the differences listed in this section, the PromQL in Cloud Monitoring is at parity with the PromQL available in Prometheus version **2.44**. 

PromQL functions added after Prometheus version **2.44** might not be supported.

### UTF-8 support

PromQL for Cloud Monitoring supports [UTF-8 querying](https://prometheus.io/docs/guides/utf8/#querying).

If your Prometheus metric name only consists of alphanumeric characters plus the `_` or `:` characters, and if your label keys only consist of alphanumeric characters plus the `_` character, then you can query using traditional PromQL syntax. For example, a valid query might look like `job:my_metric:sum{label_key="label_value"}`.

However, if your Prometheus metric name uses any special characters except for the `_` or `:` characters, or if your label keys use any special character except for the `_` character, then you have to construct your query according to the [UTF-8 spec for PromQL](https://prometheus.io/docs/guides/utf8/#querying). 

UTF-8 metric names must be quoted and moved into the braces. Label names must also be quoted if they contain legacy-incompatible characters. The following example valid queries are all equivalent:

  * `{"my.domain.com/metric/name_bucket", "label.key"="label.value"}`
  * `{__name__="my.domain.com/metric/name_bucket", "label.key"="label.value"}`
  * `{"__name__"="my.domain.com/metric/name_bucket", "label.key"="label.value"}`



### Matching on metric names

Only exact matching on metric names is supported. You must include an exact match on the metric name in your query.

We recommend the following workarounds for common scenarios that use a regular expression matcher on the `__name__` label:

  * Prometheus adapter configurations often use the `=~` operator to match on multiple metric names. To fix this usage, expand the config to use a separate policy for each metric and name each metric explicitly. This also prevents you from accidentally autoscaling on unexpected metrics.
  * Regular expressions are often used to graph multiple non-dimensional metrics on the same chart. For example, if you have a metric like `cpu_servicename_usage`, you might use a wildcard to graph all your services together. Using non-dimensional metrics like this is an explicitly bad practice in Cloud Monitoring, and this practice leads to extremely poor query performance. To fix this usage, move all dimensionality into metric labels instead of embedding dimensions in the metric name.
  * Querying over multiple metrics is often used to see what metrics are available to query. We recommend you instead use the `/labels/__name__/values` call to discover metrics. You can also discover metrics using the Cloud Monitoring UI.
  * Matching multiple metrics is useful for seeing how many samples were scraped, ingested, and charged on a per-metric basis. Cloud Monitoring provides this information to you on the [Metrics Management](https://docs.cloud.google.com/monitoring/docs/metrics-management) page. You can also access this information as metric data by using the [Samples Ingested metric or the Samples Written by Attribution ID metric](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/cost-controls#identify-cost-sources). 



### Staleness

[Staleness](https://prometheus.io/docs/prometheus/latest/querying/basics/#staleness) is not supported in the Monarch backend.

### Calculation of `irate`

When the lookback window for the [`irate`](https://prometheus.io/docs/prometheus/latest/querying/functions/#irate) function is less than the step size, we increase the window to the step size. Monarch requires this change to ensure that none of the input data is completely ignored in the output. This difference applies to `rate` calculations as well.

### Calculation of `rate` and `increase`

When the lookback window for the [`rate`](https://prometheus.io/docs/prometheus/latest/querying/functions/#rate) function is less than the step size, we increase the window to the step size. Monarch requires this change to ensure that none of the input data is completely ignored in the output. This difference applies to `irate` calculations as well.

There are differences in the interpolation and extrapolation calculations. Monarch uses a different interpolation algorithm than Prometheus, and this difference can lead to slightly different results. For example, Monarch counter samples are stored with a time range rather than the single timestamp that Prometheus uses. Therefore, counter samples in Monarch can be included in a rate calculation even though the Prometheus timestamp would exclude them. This generally results in more accurate rate results, especially when querying over the beginning or end of the underlying time series.

### Calculation of `histogram_quantile`

A PromQL [`histogram_quantile`](https://prometheus.io/docs/prometheus/latest/querying/functions/#histogram_quantile) calculation on a histogram with no samples produces a NaN value. The internal query language's calculation produces no value; the point at the timestamp is dropped instead.

The rate-calculation differences can also affect the input to `histogram_quantile` queries.

### Type-specific functions on differently typed metrics

Although upstream Prometheus is weakly typed, Monarch is strongly typed. This means that running functions specific to a single type on a differently typed metric (for example, running `rate()` on a GAUGE metric or `histogram_quantile()` on a COUNTER or untyped metric) doesn't work in Cloud Monitoring, even though these functions work in upstream Prometheus.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
