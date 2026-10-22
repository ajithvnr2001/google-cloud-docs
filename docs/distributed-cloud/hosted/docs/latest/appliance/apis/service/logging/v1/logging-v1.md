---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/logging/v1/logging-v1/
title: KRM API logging.gdc.goog/v1 \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:34.936531+00:00
---

# KRM API logging.gdc.goog/v1  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/logging/v1/logging-v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  KRM API logging.gdc.goog/v1 Stay organized with collections  Save and categorize content based on your preferences. 

## logging.gdc.goog/v1

Contains API Schema definitions for the Logging group.

### AlertRule

Defines the alert rules configuration.

_Appears in:_ \- LoggingRuleSpec

Field | Description  
---|---  
`alert` _string_ | The alert name. Its value must be a valid label value.  
`expr` _string_ | The PromQL or LogQL expression to evaluate the alert rule.  
`for` _string_ | The duration in seconds over which the specified condition must be met to move the alert from the pending state to the open state.  
`labels` _object (keys:string, values:string)_ | The labels to add or overwrite. The required labels in this field are `severity: [error, critical, warning, info]`, `code: <short code for the error>`, and `resource: <component, service, or hardware related to the alert>`. Any additional labels are optional.  
`annotations` _object (keys:string, values:string)_ | The annotations to add.  
  
### LoggingRule

Defines the Schema for the Logging Rules API.

_Appears in:_ \- LoggingRuleList

Field | Description  
---|---  
`apiVersion` _string_ | `logging.gdc.goog/v1`  
`kind` _string_ | `LoggingRule`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _LoggingRuleSpec_ |   
`status` _LoggingRuleStatus_ |   
  
### LoggingRuleList

Contains a list of logging rules.

Field | Description  
---|---  
`apiVersion` _string_ | `logging.gdc.goog/v1`  
`kind` _string_ | `LoggingRuleList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _LoggingRule array_ |   
  
### LoggingRuleSpec

Defines the specification or expected state of the `LoggingRule` object.

_Appears in:_ \- LoggingRule

Field | Description  
---|---  
`source` _Source_ | The log source on which to base alerts. Accepted values are `operational` and `audit`.  
`interval` _string_ | The rule evaluation interval.  
`limit` _integer_ | The limit number of alerts. A value of `0` means no limit.  
`recordRules` _RecordRule array_ | The list of record rules.  
`alertRules` _AlertRule array_ | The list of alert rules.  
  
### LoggingRuleStatus

Defines the observed state of the `LoggingRule` object.

_Appears in:_ \- LoggingRule

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | A list of conditions observed in the logging alerting stack.  
`lokiInstance` _string_ | The name of the Loki host instance where the `LoggingRule` object is currently installed.  
  
### LoggingTarget

Defines the Schema for the operational logging targets API.

_Appears in:_ \- LoggingTargetList

Field | Description  
---|---  
`apiVersion` _string_ | `logging.gdc.goog/v1`  
`kind` _string_ | `LoggingTarget`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _LoggingTargetSpec_ |   
`status` _LoggingTargetStatus_ |   
  
### LoggingTargetList

Contains a list of logging targets.

Field | Description  
---|---  
`apiVersion` _string_ | `logging.gdc.goog/v1`  
`kind` _string_ | `LoggingTargetList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _LoggingTarget array_ |   
  
### LoggingTargetSelectors

Provides selectors that determine which pods or containers to collect logs from.

_Appears in:_ \- LoggingTargetSpec

Field | Description  
---|---  
`matchClusters` _string array_ | The clusters to collect logs from. The default configuration is to collect logs from all clusters. The relationship between different clusters is an `OR` relationship. For example, the value `["admin", "system"]` indicates to consider the admin cluster `OR` the system cluster.  
`matchPodNames` _string array_ | The pod name prefixes to collect logs from. The Observability platform scrapes all pods with names that start with the specified prefixes. The values must contain `[a-z0-9-]` characters only. The relationship between different list elements is an `OR` relationship.  
`matchContainerNames` _string array_ | The container name prefixes to collect logs from. The Observability platform scrapes all containers with names that start with the specified prefixes. The values must contain `[a-z0-9-]` characters only. The relationship between different list elements is an `OR` relationship.  
  
### LoggingTargetSpec

Defines the specification or expected state of the `LoggingTarget` object.

_Appears in:_ \- LoggingTarget

Field | Description  
---|---  
`selector` _LoggingTargetSelectors_ | The matching pattern that identifies pods or containers to collect logs from. The relationship between different selectors is an `AND` relationship, so all selectors are considered.  
`logAccessLevel` _LogAccessLevel_ | The access level for log entries. The default value is `AO` for Application Operator.  
`parser` _OperationalLogParser_ | The predefined parser for log entries.  
`serviceName` _string_ | A service name to apply as a label. For user workloads, you can consider this field for a workload name.  
`additionalFields` _object (keys:string, values:string)_ | The additional static fields to apply to log entries. This field is a mapping of key-value pairs, where the field name is the key and the field value is the value.  
  
### LoggingTargetStatus

Defines the observed state of the `LoggingTarget` object.

_Appears in:_ \- LoggingTarget

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | A list of conditions observed in the logging stack.  
  
### RecordRule

Defines the record rules configuration.

_Appears in:_ \- LoggingRuleSpec

Field | Description  
---|---  
`record` _string_ | The time series in which to write the record rule. It must be a valid metric name.  
`expr` _string_ | The PromQL or LogQL expression to evaluate the record rule.  
`labels` _object (keys:string, values:string)_ | The labels to add or overwrite.  
  
### SIEMOrgForwarder

Defines the Schema for the `SIEMOrgForwarder` API. This API defines the type of logs, which can be audit or operational, and the external SIEM destination to send the logs.

_Appears in:_ \- SIEMOrgForwarderList

Field | Description  
---|---  
`apiVersion` _string_ | `logging.gdc.goog/v1`  
`kind` _string_ | `SIEMOrgForwarder`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _SIEMOrgForwarderSpec_ |   
`status` _SIEMOrgForwarderStatus_ |   
  
### SIEMOrgForwarderList

Contains a list of `SIEMOrgForwarder` objects.

Field | Description  
---|---  
`apiVersion` _string_ | `logging.gdc.goog/v1`  
`kind` _string_ | `SIEMOrgForwarderList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _SIEMOrgForwarder array_ |   
  
### SIEMOrgForwarderSpec

Defines the specification or expected state of the `SIEMOrgForwarder` resource.

_Appears in:_ \- SIEMOrgForwarder

Field | Description  
---|---  
`source` _LogType_ | The type of logs to export to a SIEM destination. Accepted values are `operational` and `audit`.  
`splunkOutputs` _SplunkOutput array_ | The list of Splunk outputs.  
  
### SIEMOrgForwarderStatus

Defines the observed state of the `SIEMOrgForwarder` resource.

_Appears in:_ \- SIEMOrgForwarder

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The observed state of the `SIEMOrgForwarder` resource.  
  
### SplunkOutput

Defines the Splunk output configuration.

_Appears in:_ \- SIEMOrgForwarderSpec

Field | Description  
---|---  
`host` _string_ | The host name of the target Splunk service.  
`token` _Token_ | The authentication token for the HTTP Event Collector interface.  
`tls` _string_ | The Transport Layer Security (TLS) protocol. For more information, see https://docs.fluentbit.io/manual/administration/transport-security.  
`netConnectTimeout` _integer_ | The maximum time in seconds to wait for a TCP connection to be established. This value includes the TLS handshake time.  
  
### Token

Defines the token configuration for the SIEM export.

_Appears in:_ \- SplunkOutput

Field | Description  
---|---  
`name` _string_ | The name of the token.  
`field` _string_ | The field of the token.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
