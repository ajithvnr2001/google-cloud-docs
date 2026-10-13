---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/kubernetes-crds-1.7.0/restore/
title: Restore v1.7.0 custom resource definition \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 16.9.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:44:31.136371+00:00
---

# Restore v1.7.0 custom resource definition  |  AlloyDB Omni for Kubernetes: 16.9.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/kubernetes-crds-1.7.0/restore/

This page documents AlloyDB Omni version **16.9.0** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/overview)
  * [ Reference ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/kubernetes-crds-1.1.1/backup)



Send feedback 

#  Restore v1.7.0 custom resource definition Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.9.0keyboard_arrow_down

  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/reference/kubernetes-crds-1.7.0/restore)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/reference/kubernetes-crds-1.7.0/restore)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/reference/kubernetes-crds-1.7.0/restore)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/reference/kubernetes-crds-1.7.0/restore)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/reference/kubernetes-crds-1.7.0/restore)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/reference/kubernetes-crds-1.7.0/restore)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/reference/kubernetes-crds-1.7.0/restore)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/kubernetes-crds-1.7.0/restore)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/reference/kubernetes-crds-1.7.0/restore)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/reference/kubernetes-crds-1.7.0/restore)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/reference/kubernetes-crds-1.7.0/restore)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/reference/kubernetes-crds-1.7.0/restore)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/reference/kubernetes-crds-1.7.0/restore)



## Spec schema

RestoreSpec defines the desired state of Restore.
    
    
    backup: string
    clonedDBClusterConfig:
      dbclusterName: string
    pointInTime: string
    sourceDBCluster: string
    

FieldType  
Required or optional |  Description  
---|---  
`backup`  
`string`  
 _Optional_ |  The Backup to restore from. You must specify either Backup or PointInTime. If you specify Backup, then you must leave the ClonedDBClusterConfig field unspecified. If you specify PointInTime, then you must provide a new DBCluster name in the ClonedDBClusterConfig field. Otherwise, the Restore request is rejected.   
`clonedDBClusterConfig`  
`object`  
 _Optional_ |  Settings for the cloned DBCluster. This lets you specify the name for the cloned DBCluster. Default to restore the source DBCluster if not specified.   
`clonedDBClusterConfig.dbclusterName`  
`string`  
 _Optional_ |  The name of cloned DBCluster.   
`pointInTime`  
`string`  
 _Optional_ |  Previous point in time to restore to. Default to restore the latest available time point if not specified.   
`sourceDBCluster`  
`string`  
 _Required_ |  The name of the source DBCluster to restore from.   
  
## Status schema

RestoreStatus defines the observed state of Restore.
    
    
    completeTime: string
    conditions:
    - lastTransitionTime: string
      message: string
      observedGeneration: integer
      reason: string
      status: string
      type: string
    createTime: string
    criticalIncidents:
    - code: string
      createTime: string
      message: string
      messageTemplateParams: object
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
    observedGeneration: integer
    phase: string
    reconciled: boolean
    

FieldType  
Required or optional |  Description  
---|---  
`completeTime`  
`string`  
 _Optional_ |  Completion time of the Restore.   
`conditions[]`  
`object`  
 _Optional_ |  Conditions represents the latest available observations of the entity's current state.   
`conditions[].lastTransitionTime`  
`string`  
 _Required_ |  lastTransitionTime is the last time the condition transitioned from one status to another, which occurs when the underlying condition changed. If the time when the underlying condition changed is unknown, use the time when the API field changed.   
`conditions[].message`  
`string`  
 _Required_ |  message is a human readable message indicating details about the transition. This can be an empty string.   
`conditions[].observedGeneration`  
`integer`  
 _Optional_ |  observedGeneration represents the `.metadata.generation` that the condition was set based upon. For example, if `.metadata.generation` is 12, but the `.status.conditions[x].observedGeneration` is 9, the condition is out of date with respect to the current state of the instance.   
`conditions[].reason`  
`string`  
 _Required_ |  reason contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types can define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value must be a CamelCase string. This field might not be empty.   
`conditions[].status`  
`string`  
 _Required_ |  status of the condition, one of True, False, Unknown.   
`conditions[].type`  
`string`  
 _Required_ |  type of condition in CamelCase or in `foo.example.com/CamelCase`. Many `.condition.type` values are consistent across resources like Available. Because arbitrary conditions can be useful, for example `.node.status.conditions`, the ability to deconflict is important. The regex it matches is `(dns1123SubdomainFmt/)?(qualifiedNameFmt)`.   
`createTime`  
`string`  
 _Optional_ |  Creation time of the Restore.   
`criticalIncidents[]`  
`object`  
 _Required_ |  CriticalIncidents is a flat list of all active Critical Incidents.   
`criticalIncidents[].code`  
`string`  
 _Required_ |  Code is the error code of this particular error. Error codes are `DBSE+numeric` strings, like `DBSE1012`.   
`criticalIncidents[].createTime`  
`string`  
 _Required_ |  CreateTime is the timestamp when this Incident was created at the origin.   
`criticalIncidents[].message`  
`string`  
 _Optional_ |  Message describes the incident or error that occurred.   
`criticalIncidents[].messageTemplateParams`  
`object`  
 _Optional_ |  MessageTemplateParams contains key-value pairs necessary for generating a user-friendly data-driven version of Message in the user interface.   
`criticalIncidents[].resource`  
`object`  
 _Required_ |  Resource contains information about the Database Service component that reported the incident, as well as information about the Kubernetes resource.   
`criticalIncidents[].resource.component`  
`string`  
 _Required_ |  Component is an internal identifier of the Database Service subsystem that reported the incident.   
`criticalIncidents[].resource.location`  
`object`  
 _Optional_ |  Location.   
`criticalIncidents[].resource.location.cluster`  
`string`  
 _Optional_ |  The name of the cluster of the affected Kubernetes resource.   
`criticalIncidents[].resource.location.group`  
`string`  
 _Optional_ |  The Group name of the Kubernetes resource.   
`criticalIncidents[].resource.location.kind`  
`string`  
 _Optional_ |  The Kind of the Kubernetes resource.   
`criticalIncidents[].resource.location.name`  
`string`  
 _Optional_ |  The name of the affected Kubernetes resource.   
`criticalIncidents[].resource.location.namespace`  
`string`  
 _Optional_ |  The namespace of the affected Kubernetes resource.   
`criticalIncidents[].resource.location.version`  
`string`  
 _Optional_ |  The Version of the Kubernetes resource.   
`criticalIncidents[].stackTrace[]`  
`object`  
 _Optional_ |  An unstructured list of messages from the stack trace.   
`criticalIncidents[].stackTrace.component`  
`string`  
 _Optional_ |  The name of a Database Service component that logged the message.   
`criticalIncidents[].stackTrace.message`  
`string`  
 _Optional_ |  Logged message.   
`criticalIncidents[].transientUntil`  
`string`  
 _Optional_ |  Indicates that the issue is considered transient until the specified time.   
`observedGeneration`  
`integer`  
 _Optional_ |  Internal: The generation observed by the controller.   
`phase`  
`string`  
 _Optional_ |  RestorePhase is the phase of a restore.   
`reconciled`  
`boolean`  
 _Optional_ |  Internal: Whether the resource was reconciled by the controller.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
