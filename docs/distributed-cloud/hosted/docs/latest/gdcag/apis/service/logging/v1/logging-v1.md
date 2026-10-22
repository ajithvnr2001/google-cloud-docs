---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/logging/v1/logging-v1/
title: KRM API logging.gdc.goog/v1 \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:56:58.774783+00:00
---

# KRM API logging.gdc.goog/v1  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/logging/v1/logging-v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



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
`labels` _object (keys:string, values:string)_ | The labels to add or overwrite. The required labels in this field are `severity: [error, critical, warning, info, high, moderate, low]`, `code: <short code for the error>`, and `resource: <component, service,`errorcode: ``_gdch_project: `  
`annotations` _object (keys:string, values:string)_ | The annotations to add.  
  
### ApiServerEntry

_Appears in:_ \- AuditlogInventorySpec

Field | Description  
---|---  
`resourceKind` _string_ |   
`auditRelevant` _boolean_ |   
`comment` _string_ |   
`resourceName` _string_ |   
`namespace` _string_ |   
`users` _string array_ |   
`filters` _Filter array_ |   
  
### AuditlogInventory

Defines the Schema for the AuditlogInventory API.

_Appears in:_ \- AuditlogInventoryList

Field | Description  
---|---  
`apiVersion` _string_ | `logging.gdc.goog/v1`  
`kind` _string_ | `AuditlogInventory`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _AuditlogInventorySpec_ |   
`status` _AuditlogInventoryStatus_ |   
  
### AuditlogInventoryList

Contains a list of AuditlogInventory.

Field | Description  
---|---  
`apiVersion` _string_ | `logging.gdc.goog/v1`  
`kind` _string_ | `AuditlogInventoryList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _AuditlogInventory array_ |   
  
### AuditlogInventorySpec

_Appears in:_ \- AuditlogInventory

Field | Description  
---|---  
`oc` _string_ |   
`apiServer` _ApiServerEntry array_ |   
`logFiles` _LogFile array_ |   
`syslogs` _Syslog array_ |   
  
### AuditlogInventoryStatus

_Appears in:_ \- AuditlogInventory

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ |   
  
### Condition

Condition defines a condition for a filter.

_Appears in:_ \- Filter

Field | Description  
---|---  
`path` _string_ |   
`match` _string_ |   
  
### ElasticOutput

Defines the Elastic output configuration.

_Appears in:_ \- SIEMDestinations

Field | Description  
---|---  
`host` _string_ | The host name of the target Elastic service.  
`http_credential` _HTTPCredential_ | The HTTP credential for the Elastic instance.  
`port` _integer_ | TCP port of the Elastic instance.  
`tls` _string_ |   
`netConnectTimeout` _integer_ |   
`index` _string_ | The index for the Elastic instance. If not specified, the log type (audit or operational) will be used.  
  
### Filter

Filter defines a rule for removing or replacing specific fields from audit logs. It can be used to filter sensitive information or any field irrelevant to the audit log.

_Appears in:_ \- ApiServerEntry

Field | Description  
---|---  
`name` _string_ |   
`action` _string_ |   
`targetPath` _string_ |   
`conditions` _Condition array_ |   
  
### HTTPCredential

Defines the HTTP credential for the Elastic SIEM.

_Appears in:_ \- ElasticOutput

Field | Description  
---|---  
`http_user` _string_ | HTTP user for the Elastic instance  
`http_passwd` _string_ | HTTP password for the Elastic instance  
  
### LogFile

LogFile represents a log file configuration.

_Appears in:_ \- AuditlogInventorySpec

Field | Description  
---|---  
`name` _string_ |   
`path` _string_ |   
  
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
  
### SIEMDestinations

SIEMDestinations defines the possible SIEM destination configurations. Users must specify outputs under `splunk` or `elastic` fields.

_Appears in:_ \- SIEMOrgForwarderSpec

Field | Description  
---|---  
`splunkOutputs` _SplunkOutput array_ | Splunk defines a list of Splunk destination configurations.  
`elasticOutputs` _ElasticOutput array_ | Elastic defines a list of Elastic destination configurations.  
  
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
`destinations` _SIEMDestinations_ | Destinations specifies the SIEM output configurations. Current available destinations are Splunk and Elastic  
`splunkOutputs` _SplunkOutput array_ | TODO (b/427090537): This field is to support the backward compatibility To be removed in 1.17  
  
### SIEMOrgForwarderStatus

Defines the observed state of the `SIEMOrgForwarder` resource.

_Appears in:_ \- SIEMOrgForwarder

Field | Description  
---|---  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | The observed state of the `SIEMOrgForwarder` resource.  
  
### SplunkOutput

Defines the Splunk output configuration.

_Appears in:_ \- SIEMDestinations \- SIEMOrgForwarderSpec

Field | Description  
---|---  
`host` _string_ | The host name of the target Splunk service.  
`token` _Token_ | The authentication token for the HTTP Event Collector interface.  
`tls` _string_ | The Transport Layer Security (TLS) protocol. For more information, see https://docs.fluentbit.io/manual/administration/transport-security.  
`netConnectTimeout` _integer_ | The maximum time in seconds to wait for a TCP connection to be established. This value includes the TLS handshake time.  
  
### Syslog

Syslog represents a syslog configuration.

_Appears in:_ \- AuditlogInventorySpec

Field | Description  
---|---  
`name` _string_ |   
`auditLoggingTargetName` _string_ |   
`auditLoggingTargetNamespace` _string_ |   
  
### Token

Defines the token configuration for the SIEM export.

_Appears in:_ \- SplunkOutput

Field | Description  
---|---  
`name` _string_ | The name of the token.  
`field` _string_ | The field of the token.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
