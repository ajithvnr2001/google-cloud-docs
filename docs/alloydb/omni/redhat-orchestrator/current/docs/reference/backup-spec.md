---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/reference/backup-spec/
title: Backup Custom Resource Definition \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: Current (18.3.0) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:28:27.284170+00:00
---

# Backup Custom Resource Definition  |  AlloyDB Omni using the RPM orchestrator: Current (18.3.0)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/reference/backup-spec/

This page documents AlloyDB Omni version **18.3.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: Current (18.3.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/overview)
  * [ Reference ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/reference/database-flags)



Send feedback 

#  Backup Custom Resource Definition Stay organized with collections  Save and categorize content based on your preferences. 

## Spec schema

Backup Spec defines the selected state of Backup.
    
    
    Backup:
      metadata:
        name: string
      spec:
        backupPlanRef: string
        dbclusterRef: string
        manual: boolean
    

FieldType  
Required or optional |  Description  
---|---  
`name`  
`string`  
 _Required_ |  Name of the Backup resource.   
`backupPlanRef`  
`string`  
 _Required_ |  Name of the BackupPlan from which this backup was created.   
`dbclusterRef`  
`string`  
 _Required_ |  The DBCluster name this backup belongs to.   
`manual`  
`boolean`  
 _Optional_ |  Indicates whether this backup is a scheduled or manual backup. Defaults to `false` (scheduled backup) if not specified.   
  
## Status schema

Backup Status defines the observed state of Backup.
    
    
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
`conditions`  
`list (object)`  
_Optional_ |  Represents the latest available observations of the entity's current state.   
`conditions[].lastTransitionTime`  
`string`  
 _Required_ |  The last time the condition transitioned from one status to another, which is when the underlying condition changed. If that is not known, then use the time when the API field changed.   
`conditions[].message`  
`string`  
 _Required_ |  A human readable message indicating details about the transition. This might be an empty string.   
`conditions[].observedGeneration`  
`integer`  
 _Optional_ |  Represents the `.metadata.generation` that the condition was set upon. For example, if `.metadata.generation` is `12`, but the `.status.conditions[x].observedGeneration` is `9`, the condition is out of date with respect to the current state of the instance.   
`conditions[].reason`  
`string`  
 _Required_ |  Contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field. The value should be a CamelCase string. This field cannot be empty.   
`conditions[].status`  
`string`  
 _Required_ |  Status of the condition, one of `True`, `False`, `Unknown`.   
`conditions[].type`  
`string`  
 _Required_ |  Type of condition in CamelCase or in `foo.example.com/CamelCase`. Many `.condition.type` values are consistent across resources like Available, but because arbitrary conditions can be useful (see `.node.status.conditions`), the ability to deconflict is important. The regular expression it matches is `(dns1123SubdomainFmt/)?(qualifiedNameFmt)`.   
`createTime`  
`string`  
 _Optional_ |  Creation time of the Backup.   
`criticalIncidents`  
`list (object)`  
_Required_ |  CriticalIncidents is a flat list of all active Critical Incidents.   
`criticalIncidents[].code`  
`string`  
 _Required_ |  The error code of this particular error. Error codes are formatted as `DBSE` followed by a number, like `DBSE1012`.   
`criticalIncidents[].createTime`  
`string`  
 _Required_ |  The timestamp when this Incident was created at the origin.   
`criticalIncidents[].message`  
`string`  
 _Optional_ |  Message describes the incident or error that occurred.   
`criticalIncidents[].messageTemplateParams`  
`object`  
 _Optional_ |  Contains key-value pairs necessary for generating a user-friendly data-driven version of Message in the user interface.   
`criticalIncidents[].resource`  
`object`  
 _Required_ |  Contains information about the Database Service component that reported the incident, as well as about the cluster manager resource.   
`criticalIncidents[].resource.component`  
`string`  
 _Required_ |  An internal identifier of the Database Service subsystem that reported the incident.   
`criticalIncidents[].resource.location`  
`object`  
 _Optional_ |  Location.   
`criticalIncidents[].resource.location.cluster`  
`string`  
 _Optional_ |  The name of the cluster of the affected cluster manager resource.   
`criticalIncidents[].resource.location.group`  
`string`  
 _Optional_ |  The Group name of the cluster manager resource.   
`criticalIncidents[].resource.location.kind`  
`string`  
 _Optional_ |  The Kind of the cluster manager resource.   
`criticalIncidents[].resource.location.name`  
`string`  
 _Optional_ |  The name of the affected cluster manager resource.   
`criticalIncidents[].resource.location.namespace`  
`string`  
 _Optional_ |  The namespace of the affected cluster manager resource.   
`criticalIncidents[].resource.location.version`  
`string`  
 _Optional_ |  The Version of the cluster manager resource.   
`criticalIncidents[].stackTrace`  
`list (object)`  
_Optional_ |  An unstructured list of messages from the stack trace.   
`criticalIncidents[].stackTrace.component`  
`string`  
 _Optional_ |  The name of a Database Service component that logged the message.   
`criticalIncidents[].stackTrace.message`  
`string`  
 _Optional_ |  Logged message.   
`criticalIncidents[].transientUntil`  
`string`  
 _Optional_ |  If present, this indicates that the issue is considered transient until the specified time.   
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
 _Optional_ |  The unique ID of the physical backup tracked by pgbackrest.   
`status.physicalBackupStatus.backupType`  
`string`  
 _Optional_ |  BackupType indicates the type of the backup performed. It can be "full", "diff" (differential), or "incr" (incremental).   
`phase.physicalBackupStatus.priorBackup`  
`string`  
 _Optional_ |  PriorBackup is the prior backup that this backup depends on.   
`reconciled`  
`boolean`  
 _Optional_ |  Whether the resource was reconciled by the controller.   
`retainExpireTime`  
`string`  
 _Optional_ |  RetainExpireTime defines the time when the Backup is deleted. It's an output only field calculated from `create_time` \+ `retain_days`, and is updated accordingly when the `retain_days` field of a Backup is updated.   
`physicalbackupStatus.startTime`  
`string`  
 _Optional_ |  The start time of the physical backup.   
`physicalbackupStatus.endTime`  
`string`  
 _Optional_ |  The end time of the physical backup.   
`physicalbackupStatus.wal`  
`object`  
 _Optional_ |  Contains the WAL (Write-Ahead Logging) segments.   
`physicalbackupStatus.wal.start`  
`string`  
 _Optional_ |  The starting WAL segment.   
`physicalbackupStatus.wal.end`  
`string`  
 _Optional_ |  The ending WAL segment.   
`physicalbackupStatus.lsn`  
`object`  
 _Optional_ |  Contains the LSN (Log Sequence Number) range.   
`physicalbackupStatus.lsn.start`  
`string`  
 _Optional_ |  The starting LSN.   
`physicalbackupStatus.lsn.stop`  
`string`  
 _Optional_ |  The ending LSN.   
`physicalbackupStatus.size`  
`object`  
 _Optional_ |  Contains various size metrics.   
`physicalbackupStatus.size.databaseSize`  
`string`  
 _Optional_ |  The total size of the database.   
`physicalbackupStatus.size.databaseBackupSize`  
`string`  
 _Optional_ |  The size of the database backup.   
`physicalbackupStatus.size.backupSetSize`  
`string`  
 _Optional_ |  The size of the backup set.   
`physicalbackupStatus.size.backupSize`  
`string`  
 _Optional_ |  The size of the backup.   
`physicalbackupStatus.compressed`  
`boolean`  
 _Optional_ |  Indicates if compression is used.   
`physicalbackupStatus.encrypted`  
`boolean`  
 _Optional_ |  Indicates if encryption is used.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
