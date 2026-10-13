---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/reference/kubernetes-crds-1.2.0/backup/
title: Backup v1.2.0 custom resource definition \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: Current (18.3.0) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:00:27.516021+00:00
---

# Backup v1.2.0 custom resource definition  |  AlloyDB Omni using the container orchestrator: Current (18.3.0)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/reference/kubernetes-crds-1.2.0/backup/

This page documents AlloyDB Omni version **18.3.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: Current (18.3.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/overview)
  * [ Reference ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/reference/database-flags)



Send feedback 

#  Backup v1.2.0 custom resource definition Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.3.0keyboard_arrow_down

  * [ Current (18.3.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/reference/kubernetes-crds-1.2.0/backup)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/reference/kubernetes-crds-1.2.0/backup)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/reference/kubernetes-crds-1.2.0/backup)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/reference/kubernetes-crds-1.2.0/backup)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/reference/kubernetes-crds-1.2.0/backup)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/reference/kubernetes-crds-1.2.0/backup)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/reference/kubernetes-crds-1.2.0/backup)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/reference/kubernetes-crds-1.2.0/backup)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/kubernetes-crds-1.2.0/backup)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/reference/kubernetes-crds-1.2.0/backup)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/reference/kubernetes-crds-1.2.0/backup)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/reference/kubernetes-crds-1.2.0/backup)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/reference/kubernetes-crds-1.2.0/backup)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/reference/kubernetes-crds-1.2.0/backup)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/reference/kubernetes-crds-1.2.0/backup)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/reference/kubernetes-crds-1.2.0/backup)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/reference/kubernetes-crds-1.2.0/backup)



## Spec schema

BackupSpec defines the desired state of Backup.
    
    
    backupPlanRef: string
    dbclusterRef: string
    manual:
      physicalbackupSpec:
        backuptype: string
      type: boolean
    physicalbackupSpec: string
    

FieldType  
Required or optional |  Description  
---|---  
`backupPlanRef`  
`string`  
 _Required_ |  Name of the BackupPlan from which this backup was created.   
`dbclusterRef`  
`string`  
 _Required_ |  The DBCluster name this backup belongs to.   
`manual`  
`boolean`  
 _Optional_ |  Indicates whether this backup is a scheduled or manual backup. Defaults to false (scheduled backup) if not specified.   
`manual.physicalbackupSpec`  
`object`  
 _Optional_ |  Contains spec for physical backups, allowing to specify backup type as an enum in {"full","diff","incr"}. Default to full if not specified.   
`manual.physicalbackupSpec.backuptype`  
`string`  
 _Optional_ |  The type of backup to be created. It's an enum in {"full","diff","incr"}. Default to full if not specified.   
  
## Status schema

BackupStatus defines the observed state of Backup.
    
    
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
    physicalbackupStatus:
      backupID: string
      priorBackup: string
    reconciled: boolean
    retainexpireTime: string
    

FieldType  
Required or optional |  Description  
---|---  
`completeTime`  
`string`  
 _Optional_ |  Completion time of the Backup.   
`conditions[]`  
`object`  
 _Optional_ |  Represents the latest available observations of the entity's current state.   
`conditions[].lastTransitionTime`  
`string`  
 _Required_ |  The last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable.   
`conditions[].message`  
`string`  
 _Required_ |  a human readable message indicating details about the transition. This may be an empty string.   
`conditions[].observedGeneration`  
`integer`  
 _Optional_ |  Represents the .metadata.generation that the condition was set based upon. For example, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance.   
`conditions[].reason`  
`string`  
 _Required_ |  Contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty.   
`conditions[].status`  
`string`  
 _Required_ |  Status of the condition, one of True, False, Unknown.   
`conditions[].type`  
`string`  
 _Required_ |  Type of condition in CamelCase or in foo.example.com/CamelCase. Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. The regex it matches is (dns1123SubdomainFmt/)?(qualifiedNameFmt).   
`createTime`  
`string`  
 _Optional_ |  Creation time of the Backup.   
`criticalIncidents[]`  
`object`  
 _Required_ |  CriticalIncidents is a flat list of all active Critical Incidents.   
`criticalIncidents[].code`  
`string`  
 _Required_ |  The error code of this particular error. Error codes are DBSE+numeric strings, like "DBSE1012".   
`criticalIncidents[].createTime`  
`string`  
 _Required_ |  The timestamp when this Incident was created at the origin.   
`criticalIncidents[].message`  
`string`  
 _Optional_ |  Message describes the incident/error that occurred.   
`criticalIncidents[].messageTemplateParams`  
`object`  
 _Optional_ |  Contains key-value pairs necessary for generating a user-friendly data-driven version of Message in the user interface.   
`criticalIncidents[].resource`  
`object`  
 _Required_ |  Contains information about the Database Service component that reported the incident as well as about the K8s resource.   
`criticalIncidents[].resource.component`  
`string`  
 _Required_ |  An internal identifier of the Database Service subsystem that reported the incident.   
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
`criticalIncidents[].stackTrace`  
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
 _Optional_ |  If present indicates that the issue should be considered transient until the specified time.   
`observedGeneration`  
`integer`  
 _Optional_ |  Internal: The generation observed by the controller.   
`phase`  
`string`  
 _Optional_ |  BackupPhase is the phase of a backup.   
`phase.physicalBackupStatus`  
`object`  
 _Optional_ |  PhysicalBackupStatus contains status info that are specific for physical backups.   
`phase.physicalBackupStatus.backupID`  
`string`  
 _Optional_ |  The unique id of the physical backup tracked by pgbackrest.   
`phase.physicalBackupStatus.priorBackup`  
`string`  
 _Optional_ |  PriorBackup is the prior backup this backup depends on.   
`reconciled`  
`boolean`  
 _Optional_ |  Internal: Whether the resource was reconciled by the controller.   
`retainExpireTime`  
`string`  
 _Optional_ |  RetainExpireTime defines the time when the Backup is deleted. It's an output only field calculated from create_time + retain_days, and is updated accordingly when the retain_days field of a Backup is updated.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
