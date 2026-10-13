---
url: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/monitoring/monitoringmetricdescriptor/
title: MonitoringMetricDescriptor \u00a0|\u00a0 Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:06:46.225189+00:00
---

# MonitoringMetricDescriptor  |  Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/monitoring/monitoringmetricdescriptor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ API and reference ](https://docs.cloud.google.com/config-connector/docs/reference/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# MonitoringMetricDescriptor

**Property** | **Value**  
---|---  
Google Cloud Service Name | Cloud Monitoring  
Google Cloud Service Documentation | [/monitoring/docs/](https://docs.cloud.google.com/monitoring/docs)  
Google Cloud REST Resource Name | v3.projects.metricDescriptors  
Google Cloud REST Resource Documentation | [/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors)  
Config Connector Resource Short Names | gcpmonitoringmetricdescriptor  
gcpmonitoringmetricdescriptors  
monitoringmetricdescriptor  
Config Connector Service Name | monitoring.googleapis.com  
Config Connector Resource Fully Qualified Name | monitoringmetricdescriptors.monitoring.cnrm.cloud.google.com  
Can Be Referenced by IAMPolicy/IAMPolicyMember | No  
Config Connector Default Average Reconcile Interval In Seconds | 600  
  
## Custom Resource Definition Properties

### Spec

#### Schema
    
    
    description: string
    displayName: string
    labels:
    - description: string
      key: string
      valueType: string
    launchStage: string
    metadata:
      ingestDelay: string
      launchStage: string
      samplePeriod: string
    metricKind: string
    projectRef:
      external: string
      name: string
      namespace: string
    type: string
    unit: string
    valueType: string
    

Fields  
---  
`description` _Optional_ |  `string` Immutable. A detailed description of the metric, which can be used in documentation.  
`displayName` _Optional_ |  `string` Immutable. A concise name for the metric, which can be displayed in user interfaces. Use sentence case without an ending period, for example "Request count". This field is optional but it is recommended to be set for any metrics associated with user-visible concepts, such as Quota.  
`labels` _Optional_ |  `list (object)` Immutable. The set of labels that can be used to describe a specific instance of this metric type. For example, the `appengine.googleapis.com/http/server/response_latencies` metric type has a label for the HTTP response code, `response_code`, so you can look at latencies for successful responses or just for responses that failed.  
`labels[]` _Optional_ |  `object`  
`labels[].description` _Optional_ |  `string` Immutable. A human-readable description for the label.  
`labels[].key` _Optional_ |  `string` Immutable. The key for this label. The key must meet the following criteria: * Does not exceed 100 characters. * Matches the following regular expression: `a-zA-Z*` * The first character must be an upper- or lower-case letter. * The remaining characters must be letters, digits, or underscores.  
`labels[].valueType` _Optional_ |  `string` Immutable. The type of data that can be assigned to the label. Possible values: STRING, BOOL, INT64  
`launchStage` _Optional_ |  `string` Immutable. Optional. The launch stage of the metric definition. Possible values: LAUNCH_STAGE_UNSPECIFIED, UNIMPLEMENTED, PRELAUNCH, EARLY_ACCESS, ALPHA, BETA, GA, DEPRECATED  
`metadata` _Optional_ |  `object` Immutable. Optional. Metadata which can be used to guide usage of the metric.  
`metadata.ingestDelay` _Optional_ |  `string` Immutable. The delay of data points caused by ingestion. Data points older than this age are guaranteed to be ingested and available to be read, excluding data loss due to errors.  
`metadata.launchStage` _Optional_ |  `string` Immutable. Deprecated. Must use the MetricDescriptor.launch_stage instead. Possible values: LAUNCH_STAGE_UNSPECIFIED, UNIMPLEMENTED, PRELAUNCH, EARLY_ACCESS, ALPHA, BETA, GA, DEPRECATED  
`metadata.samplePeriod` _Optional_ |  `string` Immutable. The sampling period of metric data points. For metrics which are written periodically, consecutive data points are stored at this time interval, excluding data loss due to errors. Metrics with a higher granularity have a smaller sampling period.  
`metricKind` _Required_ |  `string` Immutable. Whether the metric records instantaneous values, changes to a value, etc. Some combinations of `metric_kind` and `value_type` might not be supported. Possible values: METRIC_KIND_UNSPECIFIED, GAUGE, DELTA, CUMULATIVE  
`projectRef` _Required_ |  `object` Immutable. The Project that this resource belongs to.  
`projectRef.external` _Optional_ |  `string` The `projectID` field of a project, when not managed by Config Connector.  
`projectRef.name` _Optional_ |  `string` The `name` field of a `Project` resource.  
`projectRef.namespace` _Optional_ |  `string` The `namespace` field of a `Project` resource.  
`type` _Required_ |  `string` Immutable. The metric type, including its DNS name prefix. The type is not URL-encoded. All user-defined metric types have the DNS name `custom.googleapis.com` or `external.googleapis.com`. Metric types should use a natural hierarchical grouping. For example: "custom.googleapis.com/invoice/paid/amount" "external.googleapis.com/prometheus/up" "appengine.googleapis.com/http/server/response_latencies"  
`unit` _Optional_ |  `string` Immutable. The units in which the metric value is reported. It is only applicable if the `value_type` is `INT64`, `DOUBLE`, or `DISTRIBUTION`. The `unit` defines the representation of the stored metric values. Different systems might scale the values to be more easily displayed (so a value of `0.02kBy` _might_ be displayed as `20By`, and a value of `3523kBy` _might_ be displayed as `3.5MBy`). However, if the `unit` is `kBy`, then the value of the metric is always in thousands of bytes, no matter how it might be displayed. If you want a custom metric to record the exact number of CPU-seconds used by a job, you can create an `INT64 CUMULATIVE` metric whose `unit` is `s{CPU}` (or equivalently `1s{CPU}` or just `s`). If the job uses 12,005 CPU-seconds, then the value is written as `12005`. Alternatively, if you want a custom metric to record data in a more granular way, you can create a `DOUBLE CUMULATIVE` metric whose `unit` is `ks{CPU}`, and then write the value `12.005` (which is `12005/1000`), or use `Kis{CPU}` and write `11.723` (which is `12005/1024`). The supported units are a subset of [The Unified Code for Units of Measure](https://unitsofmeasure.org/ucum.html) standard: **Basic units (UNIT)** * `bit` bit * `By` byte * `s` second * `min` minute * `h` hour * `d` day * `1` dimensionless **Prefixes (PREFIX)** * `k` kilo (10^3) * `M` mega (10^6) * `G` giga (10^9) * `T` tera (10^12) * `P` peta (10^15) * `E` exa (10^18) * `Z` zetta (10^21) * `Y` yotta (10^24) * `m` milli (10^-3) * `u` micro (10^-6) * `n` nano (10^-9) * `p` pico (10^-12) * `f` femto (10^-15) * `a` atto (10^-18) * `z` zepto (10^-21) * `y` yocto (10^-24) * `Ki` kibi (2^10) * `Mi` mebi (2^20) * `Gi` gibi (2^30) * `Ti` tebi (2^40) * `Pi` pebi (2^50) **Grammar** The grammar also includes these connectors: * `/` division or ratio (as an infix operator). For examples, `kBy/{email}` or `MiBy/10ms` (although you should almost never have `/s` in a metric `unit`; rates should always be computed at query time... [truncated]  
`valueType` _Required_ |  `string` Immutable. Whether the measurement is an integer, a floating-point number, etc. Some combinations of `metric_kind` and `value_type` might not be supported. Possible values: STRING, BOOL, INT64  
  
### Status

#### Schema
    
    
    conditions:
    - lastTransitionTime: string
      message: string
      reason: string
      status: string
      type: string
    monitoredResourceTypes:
    - string
    observedGeneration: integer
    selfLink: string
    

Fields  
---  
`conditions` |  `list (object)` Conditions represent the latest available observations of the MonitoringMetricDescriptor's current state.  
`conditions[]` |  `object`  
`conditions[].lastTransitionTime` |  `string` Last time the condition transitioned from one status to another.  
`conditions[].message` |  `string` Human-readable message indicating details about last transition.  
`conditions[].reason` |  `string` Unique, one-word, CamelCase reason for the condition's last transition.  
`conditions[].status` |  `string` Status is the status of the condition. Can be True, False, Unknown.  
`conditions[].type` |  `string` Type is the type of the condition.  
`monitoredResourceTypes` |  `list (string)` Read-only. If present, then a time series, which is identified partially by a metric type and a MonitoredResourceDescriptor, that is associated with this metric type can only be associated with one of the monitored resource types listed here.  
`monitoredResourceTypes[]` |  `string`  
`observedGeneration` |  `integer` ObservedGeneration is the generation of the resource that was most recently observed by the Config Connector controller. If this is equal to metadata.generation, then that means that the current reported status reflects the most recent desired state of the resource.  
`selfLink` |  `string` The resource name of the metric descriptor.  
  
## Sample YAML(s)

### Typical Use Case
    
    
    # Copyright 2021 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    apiVersion: monitoring.cnrm.cloud.google.com/v1beta1
    kind: MonitoringMetricDescriptor
    metadata:
      name: monitoringmetricdescriptor-sample
    spec:
      projectRef:
         # Replace ${PROJECT_ID?} with your project ID
         external: "projects/${PROJECT_ID?}"
      labels:
      - key: system_stable
        valueType: BOOL
        description: True if the estimation system is stable.
      - key: condition_summary
        valueType: STRING
        description: A description of the condition the market system is in.
      launchStage: BETA
      metadata:
        ingestDelay: 1000s
        samplePeriod: 100s
      metricKind: GAUGE
      type: custom.googleapis.com/market/measurements/volume
      unit: "{USD}/h"
      valueType: DISTRIBUTION
      description: Tracks a combination of estimates of trade volume for a given resource, in $USD per hour.
      displayName: Trading Volume Estimate
    

**Note:** If you have any trouble with instantiating the resource, refer to [Troubleshoot Config Connector](https://docs.cloud.google.com/config-connector/docs/troubleshooting).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
