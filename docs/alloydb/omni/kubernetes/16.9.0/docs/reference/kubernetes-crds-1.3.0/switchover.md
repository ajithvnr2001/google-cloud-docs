---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/kubernetes-crds-1.3.0/switchover/
title: Switchover v1.3.0 custom resource definition \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 16.9.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:44:24.055680+00:00
---

# Switchover v1.3.0 custom resource definition  |  AlloyDB Omni for Kubernetes: 16.9.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/kubernetes-crds-1.3.0/switchover/

This page documents AlloyDB Omni version **16.9.0** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/overview)
  * [ Reference ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/kubernetes-crds-1.1.1/backup)



Send feedback 

#  Switchover v1.3.0 custom resource definition Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.9.0keyboard_arrow_down

  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/reference/kubernetes-crds-1.3.0/switchover)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/reference/kubernetes-crds-1.3.0/switchover)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/reference/kubernetes-crds-1.3.0/switchover)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/reference/kubernetes-crds-1.3.0/switchover)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/reference/kubernetes-crds-1.3.0/switchover)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/reference/kubernetes-crds-1.3.0/switchover)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/reference/kubernetes-crds-1.3.0/switchover)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/kubernetes-crds-1.3.0/switchover)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/reference/kubernetes-crds-1.3.0/switchover)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/reference/kubernetes-crds-1.3.0/switchover)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/reference/kubernetes-crds-1.3.0/switchover)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/reference/kubernetes-crds-1.3.0/switchover)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/reference/kubernetes-crds-1.3.0/switchover)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/reference/kubernetes-crds-1.3.0/switchover)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/reference/kubernetes-crds-1.3.0/switchover)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/reference/kubernetes-crds-1.3.0/switchover)



## Spec schema

SwitchoverSpec defines the selected state of Switchover.
    
    
    dbclusterRef: string
    newPrimary: string
    newPrimaryInstance: string
    primaryHost: string
    

FieldType  
Required or optional |  Description  
---|---  
`dbclusterRef`  
`string`  
 _Optional_ |  DBClusterRef is the DBCluster name to initiate a switchover. The `Switchover` object must be created in the same namespace as the DBCluster that it references. This field is required for Switchover.   
`newPrimary`  
`string`  
 _Optional_ |  NewPrimary is the standby instance to switch with the current primary.   
`newPrimaryInstance`  
`string`  
 _Optional_ |  NewPrimaryInstance is the standby instance to switch with the current primary. Deprecated: Please use NewPrimary field instead.   
`primaryHost`  
`string`  
 _Optional_ |  PrimaryHost is the IP always point to the primary instance.   
  
## Status schema

SwitchoverStatus defines the observed state of Switchover.
    
    
    conditions:
    - lastTransitionTime: string
      message: string
      observedGeneration: integer
      reason: string
      status: string
      type: string
    createTime: string
    critcalIncidents:
    - code: string
      createTime: string
      message: string
      messageTemplateParams:
      resource:
        component: string
        location:
          cluster: string
          group: string
          kind: string
          name: string
          namespace: string
          version: string
      stackTrace:
      - component: string
        message: string
      transientUntil: string
    endTime: string
    internal:
      newPrimary: string
      oldPrimary: string
      phase: string
    observedGeneration: integer
    reconciled: boolean
    startTime: string
    state: string
    

FieldType  
Required or optional |  Description  
---|---  
`conditions`  
`list (object)`  
_Optional_ |  Conditions represents the latest available observations of the entity's current state.   
`conditions[]`  
`object`  
 _Optional_ |  Condition contains details for one aspect of the current state of this API Resource. --- This struct is intended for direct use as an array at the field path .status.conditions. For example, \n type FooStatus struct{ // Represents the observations of a foo's current state. // Known .status.conditions.type are: \"Available\", \"Progressing\", and \"Degraded\" // +patchMergeKey=type // +patchStrategy=merge // +listType=map // +listMapKey=type Conditions []metav1.Condition `json:\"conditions,omitempty\" patchStrategy:\"merge\" patchMergeKey:\"type\" protobuf:\"bytes,1,rep,name=conditions\"` \n // other fields }   
`conditions[].lastTransactionTime`  
`string`  
 _Required_ |  lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable.   
`conditions[].message`  
`string`  
 _Required_ |  message is a human readable message indicating details about the transition. This may be an empty string.   
`conditions[].observedGeneration`  
`integer`  
 _Optional_ |  observedGeneration represents the .metadata.generation that the condition was set based upon. For example, if .metadata.generation is 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance.   
`conditions[].reason`  
`string`  
 _Required_ |  reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty.   
`conditions[].status`  
`string`  
 _Required_ |  Valid values: `"True"`, `"False"`, `Unknown` status of the condition, one of True, False, Unknown.   
`conditions[].type`  
`string`  
 _Required_ |  type of condition in CamelCase or in foo.example.com/CamelCase. \--- Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. The regular expression it matches is (dns1123SubdomainFmt/)?(qualifiedNameFmt)   
`createTime`  
`string`  
 _Optional_ |  CreateTime is the time that the internal switchover workflow mechanism was created.   
`criticalIncidents`  
`list (object)`  
_Optional_ |  CriticalIncidents is a flat list of all active Critical Incidents.   
`criticalIncidents[]`  
`object`  
 _Optional_ |  CriticalIncident contains all information about an ongoing critical incident.   
`criticalIncidents[].code`  
`string`  
 _Required_ |  Code is the error code of this particular error. Error codes are DBSE+numeric strings, like "DBSE1012".   
`criticalIncidents[].createTime`  
`string`  
 _Required_ |  CreateTime is the timestamp when this Incident was created at the origin.   
`criticalIncidents[].message`  
`string`  
 _Optional_ |  Message describes the incident/error that occurred.   
`criticalIncidents[].messageTemplateParams`  
`object`  
 _Optional_ |  MessageTemplateParams contains key-value pairs necessary for generating a user-friendly data-driven version of Message in the UI.   
`criticalIncidents[].resource`  
`object`  
 _Required_ |  Resource contains information about the Database Service component that reported the incident as well as about the Kubernetes resource.   
`criticalIncidents[].resource.component`  
`string`  
 _Required_ |  Component is an internal identifier of the Database Service subsystem that reported the incident.   
`criticalIncidents[].resource.location`  
`object`  
 _Optional_ |  Location   
`criticalIncidents[].resource.location.cluster`  
`string`  
 _Optional_ |  Cluster is the name of the cluster of the affected Kubernetes resource.   
`criticalIncidents[].resource.location.group`  
`string`  
 _Optional_ |  Group is the Group name of the Kubernetes resource.   
`criticalIncidents[].resource.location.kind`  
`string`  
 _Optional_ |  Kind is the Kind of the Kubernetes resource.   
`criticalIncidents[].resource.location.name`  
`string`  
 _Optional_ |  Name is the name of the affected Kubernetes resource.   
`criticalIncidents[].resource.location.namespace`  
`string`  
 _Optional_ |  Namespace is the namespace of the affected Kubernetes resource.   
`criticalIncidents[].resource.location.version`  
`TYPE`  
 _Optional_ |  Group is the Version of the Kubernetes resource.   
`criticalIncidents[].stackTrace`  
`list (object)`  
_Optional_ |  StackTrace contains an unstructured list of messages from the stack trace.   
`criticalIncidents[].stackTrace[]`  
`object`  
 _Optional_ |  CriticalIncidentStackTraceMessage contains stack trace information available for the incident.   
`criticalIncidents[].stackTrace[].component`  
`string`  
 _Optional_ |  Component is the name of a Database Service component that logged the message.   
`criticalIncidents[].stackTrace[].message`  
`string`  
 _Optional_ |  Logged message.   
`criticalIncidents[].stackTrace[].message`  
`string`  
 _Optional_ |  TransientUntil if present indicates that the issue should be considered transient until the specified time.   
`endTime`  
`string`  
 _Optional_ |  EndTime is the time switchover reached its final state.   
`internal`  
`object`  
 _Optional_ |  Internal is used by the system controllers. Don't depend on the information in this section.   
`internal.newPrimary`  
`string`  
 _Required_ |  NewPrimary is the instance that we are attempting to switchover to.   
`internal.oldPrimary`  
`string`  
 _Required_ |  OldPrimary is the instance that was the primary at the start of the switchover.   
`internal.phase`  
`string`  
 _Optional_ |  Valid values: `UpdateDbcluster`, `StopPrimary`, `PromoteStandby`, `ValidateNewPrimary`, `UpdateOldPrimaryResources`, `UpdateNewPrimaryResources`, `UpdateOldPrimaryConfigs`, `Complete`, `SyncOldPrimary`, `StartOldPrimary`, `PreSuccess`, `RepointStandbys`, `RollbackPrimary`, `RollbackStandbys` Phase is used to keep track of the current state of the switchover   
`observedGeneration`  
`integer`  
 _Optional_ |  Internal: The generation observed by the controller.   
`reconciled`  
`boolean`  
 _Optional_ |  Internal: Whether the resource was reconciled by the controller.   
`startTime`  
`string`  
 _Optional_ |  StartTime is the time that the switchover operation started.   
`state`  
`string`  
 _Optional_ |  Valid values: `InProgress`, `Success`, `Failed_RollbackInProgress`, `Failed_RollbackSuccess`, `Failed_RollbackFailed` State is the current state of the switchover operation. The values are `InProgress`, `Success`, `Failed_RollbackInProgress`, `Failed_RollbackSuccess`, `Failed_RollbackFailed` `InProgress` means the switchover is still in progress. `Success` means that the switchover has completed. `Failed_RollbackInProgress` means that the operator was unable to promote the new primary instance, and is attempting to restart the old primary instance. `Failed_RollbackSuccess` means that the operator was unable to promote the new primary instance, and successfully restarted the old primary instance. `Failed_RollbackFailed` means that the operator was unable to promote the new primary instance, and were not able to restart the old primary instance. The DBCluster might need to be manually repaired.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
