---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/observability/v1/observability-v1/
title: KRM API observability.gdc.goog/v1 \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:34.824269+00:00
---

# KRM API observability.gdc.goog/v1  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/observability/v1/observability-v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  KRM API observability.gdc.goog/v1 Stay organized with collections  Save and categorize content based on your preferences. 

## observability.gdc.goog/v1

Contains API Schema definitions for the Observability group.

### AdditionalLogSink

Configures the additional sinks to route logs. For more information, see <https://cloud.google.com/anthos/private-mode/docs/1.9/how-to/export-logs>.

_Appears in:_ \- ObservabilityAuditLogging \- ObservabilityLogging \- ObservabilitySecurityLogging

Field | Description  
---|---  
`clusterSelector` _ClusterSelector_ |   
`fluentbitConfigMaps` _string array_ |   
`volumes` _[Volume](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#volume-v1-core) array_ |   
`volumeMounts` _[VolumeMount](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#volumemount-v1-core) array_ |   
  
### ClusterSelector

Selects target clusters.

_Appears in:_ \- AdditionalLogSink

Field | Description  
---|---  
`exclude` _string array_ |   
  
### Dashboard

Defines the Schema for the Dashboards API.

_Appears in:_ \- DashboardList

Field | Description  
---|---  
`apiVersion` _string_ | `observability.gdc.goog/v1`  
`kind` _string_ | `Dashboard`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _DashboardSpec_ |   
`status` _DashboardStatus_ |   
  
### DashboardConfigMap

Provides information about the `ConfigMap` object that contains the JSON model of a Grafana dashboard.

_Appears in:_ \- DashboardSpec

Field | Description  
---|---  
`name` _string_ | The name of the `ConfigMap` object containing the JSON model of the dashboard.  
`namespace` _string_ | The namespace of the `ConfigMap` object containing the JSON model of the dashboard.  
`key` _string_ | The key of the `ConfigMap` object containing the JSON model of the dashboard.  
  
### DashboardInfo

Contains a list of information about the connection of a dashboard created in Grafana. 

_Appears in:_ \- DashboardStatus

Field | Description  
---|---  
`uid` _string_ | The unique ID of the dashboard.  
`url` _string_ | The path to the dashboard.  
  
### DashboardList

Contains a list of dashboards in Grafana. 

Field | Description  
---|---  
`apiVersion` _string_ | `observability.gdc.goog/v1`  
`kind` _string_ | `DashboardList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _Dashboard array_ |   
  
### DashboardSpec

Defines the specification or expected state of the `Dashboard` object.

_Appears in:_ \- Dashboard

Field | Description  
---|---  
`configMapRef` _DashboardConfigMap_ | The `ConfigMap` object that contains the JSON model of the Grafana dashboard to include.  
`foldername` _string_ | The name of the folder where the system must store the dashboards.  
  
### DashboardStatus

Defines the observed state of the `Dashboard` object.

_Appears in:_ \- Dashboard

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | A list of conditions observed in the dashboard.  
`dashboards` _object (keys:string, values:DashboardInfo)_ | A mapping of all the dashboards created by the custom resource using the unique ID (`uid`) of the dashboard as the key.  
  
### Grafana

Defines the expected state of the Grafana instance provisioned.

_Appears in:_ \- ObservabilityMonitoring

Field | Description  
---|---  
`storageSize` _string_ | The storage size for the dashboards within an organization. https://kubernetes.io/docs/reference/kubernetes-api/common-definitions/quantity/  
  
### ObservabilityAlerting

Defines the rules to create alerts based on metrics data.

_Appears in:_ \- ObservabilityPipelineSpec

Field | Description  
---|---  
`localStorageSize` _string_ | The storage size for alerting data within an organization.  
`alertmanagerConfig` _string_ | The name of the `ConfigMap` object that contains the Alertmanager configuration file. https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names  
`volumes` _[Volume](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#volume-v1-core) array_ |   
`volumeMounts` _[VolumeMount](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#volumemount-v1-core) array_ |   
  
### ObservabilityAuditLogging

Defines the expected state of the audit logging stack of the Observability pipeline.

_Appears in:_ \- ObservabilityPipelineSpec

Field | Description  
---|---  
`retentionTime` _string_ | The retention time for audit logs in hours. https://cortexmetrics.io/docs/configuration/configuration-file/#generic-placeholders  
`localStorageSize` _string_ | The storage size for audit logging data within an organization. https://kubernetes.io/docs/reference/kubernetes-api/common-definitions/quantity/  
`additionalSink` _AdditionalLogSink_ | The configuration of an optional additional sink for all audit logs.  
`dynamicAdditionalSinks` _string array_ | The additional sinks for audit logs apart from any predefined sink. The difference with the `additionalSink` field is that `dynamicAdditionalSinks` determines most of the sink variables, such as the sink's hostname, on the user's behalf. The supported outputs include `ioSplunkExternalSink`.  
  
### ObservabilityLogging

Defines the expected state of the logging stack of the Observability pipeline.

_Appears in:_ \- ObservabilityPipelineSpec

Field | Description  
---|---  
`retentionTime` _string_ | The retention time for operational logs in hours. https://cortexmetrics.io/docs/configuration/configuration-file/#generic-placeholders  
`localStorageSize` _string_ | The storage size for logging data within an organization. https://kubernetes.io/docs/reference/kubernetes-api/common-definitions/quantity/  
`sink` _string_ | The sink for all logs. For example, using the project namespace of an Application Operator as a value means that the logs become visible to the Application Operator of the project.  
`additionalSink` _AdditionalLogSink_ | The configuration of an optional additional sink for all operational logs.  
`dynamicAdditionalSinks` _string array_ | The additional sinks for operational logs apart from any predefined sink. The difference with the `additionalSink` field is that `dynamicAdditionalSinks` determines most of the sink variables, such as the sink's hostname, on the user's behalf. The supported outputs include `ioSplunkExternalSink`.  
  
### ObservabilityMonitoring

Defines the configuration for the monitoring dashboards.

_Appears in:_ \- ObservabilityPipelineSpec

Field | Description  
---|---  
`retentionTime` _string_ | Retention time for metrics in hours. https://cortexmetrics.io/docs/configuration/configuration-file/#generic-placeholders  
`localStorageSize` _string_ | The storage size for metrics data within an organization. https://kubernetes.io/docs/reference/kubernetes-api/common-definitions/quantity/  
`grafana` _Grafana_ | The configuration information for the Grafana instance to create.  
`sink` _string_ | The sink for all metrics. For example, using the project namespace of an Application Operator as a value means that the metrics become visible to the Application Operator of the project. Route by time series using the `timeseries` label.  
  
### ObservabilityPipeline

Defines the Schema for the Observability Pipeline API.

_Appears in:_ \- ObservabilityPipelineList

Field | Description  
---|---  
`apiVersion` _string_ | `observability.gdc.goog/v1`  
`kind` _string_ | `ObservabilityPipeline`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ObservabilityPipelineSpec_ |   
`status` _ObservabilityPipelineStatus_ |   
  
### ObservabilityPipelineList

Contains a list of `ObservabilityPipeline` objects.

Field | Description  
---|---  
`apiVersion` _string_ | `observability.gdc.goog/v1`  
`kind` _string_ | `ObservabilityPipelineList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ObservabilityPipeline array_ |   
  
### ObservabilityPipelineSpec

Defines the specification or expected state of the `ObservabilityPipeline` object.

_Appears in:_ \- ObservabilityPipeline

Field | Description  
---|---  
`enabled` _boolean_ | Specifies if the Observability pipeline stack is enabled.  
`monitoring` _ObservabilityMonitoring_ | The monitoring pipeline configuration.  
`alerting` _ObservabilityAlerting_ | The Alertmanager pipeline configuration.  
`logging` _ObservabilityLogging_ | The logging pipeline configuration.  
`auditLogging` _ObservabilityAuditLogging_ | The audit logging pipeline configuration.  
`securityLogging` _ObservabilitySecurityLogging_ | The security pipeline configuration.  
  
### ObservabilityPipelineStatus

Defines the observed state of the `ObservabilityPipeline` object.

_Appears in:_ \- ObservabilityPipeline

Field | Description  
---|---  
`version` _string_ | The installed version of the Observability pipeline stack.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | A list of conditions observed in the Observability pipeline stack.  
  
### ObservabilitySecurityLogging

Defines the expected state of the security logging stack of the Observability pipeline.

_Appears in:_ \- ObservabilityPipelineSpec

Field | Description  
---|---  
`retentionTime` _string_ | The retention time for security logs in hours. https://cortexmetrics.io/docs/configuration/configuration-file/#generic-placeholders  
`localStorageSize` _string_ | The storage size for security logging data within an organization. https://kubernetes.io/docs/reference/kubernetes-api/common-definitions/quantity/  
`additionalSink` _AdditionalLogSink_ | The configuration of an optional additional sink for all security logs.  
`dynamicAdditionalSinks` _string array_ | The additional sinks for security logs apart from any predefined sink. The difference with the `additionalSink` field is that `dynamicAdditionalSinks` determines most of the sink variables, such as the sink's hostname, on the user's behalf. The supported outputs include `ioSplunkExternalSink`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
