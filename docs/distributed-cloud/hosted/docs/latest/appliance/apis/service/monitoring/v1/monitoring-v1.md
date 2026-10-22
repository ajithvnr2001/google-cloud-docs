---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/monitoring/v1/monitoring-v1/
title: KRM API monitoring.gdc.goog/v1 \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:34.391461+00:00
---

# KRM API monitoring.gdc.goog/v1  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/monitoring/v1/monitoring-v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  KRM API monitoring.gdc.goog/v1 Stay organized with collections  Save and categorize content based on your preferences. 

## monitoring.gdc.goog/v1

Contains API Schema definitions for the Monitoring group.

### AlertRule

Defines the alert rules configuration.

_Appears in:_ \- MonitoringRuleSpec

Field | Description  
---|---  
`alert` _string_ | The alert name. Its value must be a valid label value.  
`expr` _string_ | The PromQL or LogQL expression to evaluate the alert rule.  
`for` _string_ | The duration in seconds over which the specified condition must be met to move the alert from the pending state to the open state.  
`labels` _object (keys:string, values:string)_ | The labels to add or overwrite. The required labels in this field are `severity: [error, critical, warning, info]`, `code: <short code for the error>`, and `resource: <component, service, or hardware related to the alert>`. Any additional labels are optional.  
`annotations` _object (keys:string, values:string)_ | The annotations to add.  
  
### ClusterStatus

ClusterStatus is a list of conditions affecting a specific cluster.

_Appears in:_ \- MonitoringTargetStatus

Field | Description  
---|---  
`cluster` _string_ |   
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ |   
  
### MonitoringRule

Defines the Schema for the Monitoring Rules API.

_Appears in:_ \- MonitoringRuleList

Field | Description  
---|---  
`apiVersion` _string_ | `monitoring.gdc.goog/v1`  
`kind` _string_ | `MonitoringRule`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _MonitoringRuleSpec_ |   
`status` _MonitoringRuleStatus_ |   
  
### MonitoringRuleList

Contains a list of monitoring rules.

Field | Description  
---|---  
`apiVersion` _string_ | `monitoring.gdc.goog/v1`  
`kind` _string_ | `MonitoringRuleList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _MonitoringRule array_ |   
  
### MonitoringRuleSpec

Defines the specification or expected state of the `MonitoringRule` object.

_Appears in:_ \- MonitoringRule

Field | Description  
---|---  
`interval` _string_ | The rule evaluation interval.  
`limit` _integer_ | The limit number of alerts. A value of `0` means no limit.  
`recordRules` _RecordRule array_ | The list of record rules.  
`alertRules` _AlertRule array_ | The list of alert rules.  
  
### MonitoringRuleStatus

Defines the observed state of the `MonitoringRule` object.

_Appears in:_ \- MonitoringRule

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Defines the observed state of the `MonitoringRule` object.  
`errorStatus` _ErrorStatus_ | ErrorStatus contains a list of current errors and the timestamp this field gets updated.  
  
### MonitoringTarget

Defines the Schema for the monitoring targets API.

_Appears in:_ \- MonitoringTargetList

Field | Description  
---|---  
`apiVersion` _string_ | `monitoring.gdc.goog/v1`  
`kind` _string_ | `MonitoringTarget`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _MonitoringTargetSpec_ |   
`status` _MonitoringTargetStatus_ |   
  
### MonitoringTargetList

Contains a list of monitoring targets.

Field | Description  
---|---  
`apiVersion` _string_ | `monitoring.gdc.goog/v1`  
`kind` _string_ | `MonitoringTargetList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _MonitoringTarget array_ |   
  
### MonitoringTargetMetricsRelabeling

Defines a filter for keeping or discarding metrics based on labels.

_Appears in:_ \- MonitoringTargetPodMetricsEndpoints

Field | Description  
---|---  
`sourceLabels` _string array_ | The selected values from existing labels. The content is concatenated using the `separator` and matched against the `regex` expression for the `replace`, `keep`, and `drop` actions.  
`separator` _string_ | The separator value placed between concatenated source label values.  
`regex` _string_ | The regular expression to match the extracted value.  
`action` _string_ | The action to perform when the `regex` expression matches the extracted value.  
`targetLabel` _string_ | The label to which to write the resulting value in a `replace` action. This field is mandatory for `replace` actions. Capture groups of regular expressions are available.  
`replacement` _string_ | The replacement value to use if the regular expression matches the extracted value in a `replace` action. Capture groups of regular expressions are available.  
  
### MonitoringTargetPodMetricsEndpoints

Configures the metric endpoints for scraped pods.

_Appears in:_ \- MonitoringTargetSpec

Field | Description  
---|---  
`port` _MonitoringTargetPodMetricsPort_ | The port from which metrics are scraped.  
`path` _MonitoringTargetPodMetricsPath_ | The path from which metrics are scraped.  
`scheme` _MonitoringTargetPodMetricsScheme_ | The scheme to use when scraping metrics.  
`params` _object (keys:string, values:string array)_ | The query parameters to use when scraping metrics from the `path`.  
`scrapeInterval` _string_ | The frequency for Prometheus to scrape the metric endpoints defined in the `podMetricsEndpoints` field.  
`scrapeTimeout` _string_ | The time for Prometheus to wait for the response from the metric endpoints defined in the `podMetricsEndpoints` field.  
`metricsRelabelings` _MonitoringTargetMetricsRelabeling array_ | The filter for either including (`allowlist`) or excluding (`denylist`) metrics based on labels.  
`ipAddresses` _string array_ | IPAddress is for configuring static IP addresses to scrape.  
`tlsConfig` _TLSConfig_ | Provide a custom TLS configuration. This is provided for workloads outside of kubernetes that need to be scraped.  
`authCredential` _string_ | Credentials to provide to the scrape endpoint.  
  
### MonitoringTargetPodMetricsPath

Determines the path to use for scraping metrics from pods.

_Appears in:_ \- MonitoringTargetPodMetricsEndpoints

Field | Description  
---|---  
`value` _string_ | The path to collect metrics from. If annotations are provided, they take priority over this field.  
`annotation` _string_ | The path to collect metrics from using annotations.  
  
### MonitoringTargetPodMetricsPort

Determines the port to use for scraping metrics from pods.

_Appears in:_ \- MonitoringTargetPodMetricsEndpoints

Field | Description  
---|---  
`value` _integer_ | The port to collect metrics from. If annotations are provided, they take priority over this field.  
`annotation` _string_ | The port to collect metrics from using annotations.  
  
### MonitoringTargetPodMetricsScheme

Determines the scheme to use for scraping metrics from pods.

_Appears in:_ \- MonitoringTargetPodMetricsEndpoints

Field | Description  
---|---  
`value` _string_ | The scheme to use when collecting metrics. If annotations are provided, they take priority over this field.  
`annotation` _string_ | The scheme to use when collecting metrics using annotations.  
  
### MonitoringTargetSelectors

Provides selectors that determine which pods to monitor.

_Appears in:_ \- MonitoringTargetSpec

Field | Description  
---|---  
`matchClusters` _string array_ | The clusters to consider for this job. The default configuration is to consider all the clusters applicable to the project. The relationship between different clusters is an `OR` relationship. For example, the value `["admin", "system"]` indicates to consider the admin cluster `OR` the system cluster.  
`matchLabels` _object (keys:string, values:string)_ | The pod labels to consider for this job. The default configuration is to consider no filter based on labels. The relationship between different pairs is an `AND` relationship, so all pairs are considered.  
`matchAnnotations` _object (keys:string, values:string)_ | The annotations to consider for this job. The default configuration is to consider no filter based on annotations. The relationship between different pairs is an `AND` relationship, so all pairs are considered.  
  
### MonitoringTargetSpec

Defines the specification or expected state of the `MonitoringTarget` object.

_Appears in:_ \- MonitoringTarget

Field | Description  
---|---  
`selector` _MonitoringTargetSelectors_ | The matching pattern that identifies pods for this job. To establish a relationship between different selectors, use `AND`.  
`podMetricsEndpoints` _MonitoringTargetPodMetricsEndpoints_ | The endpoint exposed for this job. The endpoint uses the style of Prometheus.  
  
### MonitoringTargetStatus

Defines the observed state of the `MonitoringTarget` object.

_Appears in:_ \- MonitoringTarget

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | A list of conditions observed in the monitoring stack.  
`clusterStatuses` _ClusterStatus array_ | ClusterStatuses is a list of each cluster and the conditions observed in the Monitoring stack for that cluster.  
  
### RecordRule

Defines the record rules configuration.

_Appears in:_ \- MonitoringRuleSpec

Field | Description  
---|---  
`record` _string_ | The time series in which to write the record rule. It must be a valid metric name.  
`expr` _string_ | The PromQL or LogQL expression to evaluate the record rule.  
`labels` _object (keys:string, values:string)_ | The labels to add or overwrite.  
  
### TLSConfig

_Appears in:_ \- MonitoringTargetPodMetricsEndpoints

Field | Description  
---|---  
`ca` _string_ | Text of the CA cert to use for the targets.  
`cert` _string_ | Text of the client cert file for the targets.  
`server_name` _string_ | Used to verify the hostname for the targets.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
