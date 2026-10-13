---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/kubernetes-crds-1.2.0/backupplan/
title: BackupPlan v1.2.0 custom resource definition \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 16.9.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:44:20.242350+00:00
---

# BackupPlan v1.2.0 custom resource definition  |  AlloyDB Omni for Kubernetes: 16.9.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/kubernetes-crds-1.2.0/backupplan/

This page documents AlloyDB Omni version **16.9.0** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/overview)
  * [ Reference ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/kubernetes-crds-1.1.1/backup)



Send feedback 

#  BackupPlan v1.2.0 custom resource definition Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.9.0keyboard_arrow_down

  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/reference/kubernetes-crds-1.2.0/backupplan)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/reference/kubernetes-crds-1.2.0/backupplan)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/reference/kubernetes-crds-1.2.0/backupplan)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/reference/kubernetes-crds-1.2.0/backupplan)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/reference/kubernetes-crds-1.2.0/backupplan)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/reference/kubernetes-crds-1.2.0/backupplan)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/reference/kubernetes-crds-1.2.0/backupplan)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/kubernetes-crds-1.2.0/backupplan)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/reference/kubernetes-crds-1.2.0/backupplan)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/reference/kubernetes-crds-1.2.0/backupplan)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/reference/kubernetes-crds-1.2.0/backupplan)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/reference/kubernetes-crds-1.2.0/backupplan)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/reference/kubernetes-crds-1.2.0/backupplan)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/reference/kubernetes-crds-1.2.0/backupplan)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/reference/kubernetes-crds-1.2.0/backupplan)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/reference/kubernetes-crds-1.2.0/backupplan)



## Spec schema

BackupPlanSpec defines the desired state of BackupPlan.
    
    
    backupLocation:
      gcsOptions:
        bucket: string
        key: string
        secretRef:
          name: string
          namespace: string
      type: string
    backupRetainDays: integer
    backupSchedules:
      differential: string
      full: string
      incremental: string
    dbclusterRef: string
    paused: boolean
    

FieldType  
Required or optional |  Description  
---|---  
`backupLocation`  
`object`  
 _Optional_ |  BackupLocation specifies the remote object storage location to store backups. For example, specs to a Cloud Storage buckets. This field is optional. By default, backups are stored in the backup disk.   
`backupLocation.gcsOptions`  
`object`  
 _Optional_ |  gcsOptions is a reference to Cloud Storage dependent options.   
`backupLocation.gcsOptions.bucket`  
`string`  
 _Required_ |  Bucket is a required field, (ex: dbs-dump-bucket) A user is to ensure proper write access to the storage bucket from within the Operator.   
`backupLocation.gcsOptions.key`  
`string`  
 _Required_ |  Object key for the dump files. (ex: ods-dump/scottschema.dmp).   
`backupLocation.gcsOptions.secretRef`  
`object`  
 _Optional_ |  SecretRef is a reference to the secret that stores GCS access information.   
`backupLocation.gcsOptions.secretRef.name`  
`string`  
 _Optional_ |  name is unique within a namespace to reference a secret resource.   
`backupLocation.gcsOptions.secretRef.namespace`  
`string`  
 _Optional_ |  namespace defines the space within which the secret name must be unique.   
`backupLocation.type`  
`string`  
 _Required_ |  Valid values: GCS, S3. Type of Repository (`S3` for Amazon S3, `GCS` for Google's Cloud Storage), which tells the agent which storage system/API to use.   
`backupRetainDays`  
`integer`  
 _Optional_ |  Default: 14; minimum: 1, maximum: 90. Number of days after which the service will delete a Backup. If specified, a Backup created under this BackupPlan will be automatically deleted after its age reaches create_time + backup_retain_days. The valid values are from 1 to 90 days. Default to 14 retain days if not specified.   
`backupSchedules`  
`object`  
 _Optional_ |  Defines the schedules for different types of backups. Full, Differential and Incremental backup types are supported: https://pgbackrest.org/user-guide.html#concept/backup This field is optional. By default, take one full backup every day at midnight.   
`backupSchedules.differential`  
`string`  
 _Optional_ |  Defines the Cron schedule for a differential pgBackRest backup. Follows the standard Cron schedule syntax: https://k8s.io/docs/concepts/workloads/controllers/cron-jobs/#cron-schedule-syntax   
`backupSchedules.full`  
`string`  
 _Optional_ |  Defines the Cron schedule for a full pgBackRest backup. Follows the standard Cron schedule syntax: https://k8s.io/docs/concepts/workloads/controllers/cron-jobs/#cron-schedule-syntax   
`backupSchedules.incremental`  
`string`  
 _Optional_ |  Defines the Cron schedule for a full pgBackRest backup. Follows the standard Cron schedule syntax: https://k8s.io/docs/concepts/workloads/controllers/cron-jobs/#cron-schedule-syntax   
`dbclusterRef`  
`string`  
 _Optional_ |  The DBCluster name this backupplan configures. This field is required and immutable.   
`paused`  
`boolean`  
 _Optional_ |  Default: false. A flag to indicate if the backup creation under this BackupPlan is paused. If set to true, the service will pause the scheduling of new Backups under this BackupPlan. Default to False.   
  
## Status schema

BackupPlanStatus defines the observed state of BackupPlan.
    
    
    conditions:
    - lastTransactionTime: string
      message: string
      observedGeneration: integer
      reason: string
      status: string
      type: string
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
    lastBackupTime: string
    nextBackupTime: string
    observedGeneration: integer
    phase: string
    reconciled: boolean
    recoveryWindow:
      begin: string
      end: string
    

FieldType  
Required or optional |  Description  
---|---  
`conditions`  
`list (object)`  
_OPTIONALITY_ |  Conditions represents the latest available observations of the Entity's current state.   
`conditions[]`  
`object`  
 _OPTIONALITY_ |  Condition contains details for one aspect of the current   
`conditions[].lastTransactionTime`  
`string`  
 _Required_ |  The last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable.   
`conditions[].message`  
`string`  
 _Required_ |  A human readable message indicating details about the transition. This may be an empty string.   
`conditions[].observedGeneration`  
`integer`  
 _Optional_ |  Represents the .metadata.generation that the condition was set based upon. For example, if .metadata.generation is 12 but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance.   
`conditions[].reason`  
`string`  
 _Required_ |  maximum length: 1024, minimum length: 1 Contains a programmatic identifier indicating the reason for the condition's last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty.   
`conditions[].status`  
`string`  
 _Required_ |  Status of the condition, one of True, False, Unknown.   
`conditions[].type`  
`string`  
 _Required_ |  Maximum length: 316 Type of condition in CamelCase or in foo.example.com/CamelCase.   
`criticalIncidents`  
`object`  
 _Required_ |  A flat list of all active Critical Incidents. CriticalIncident contains all information about an ongoing critical incident.   
`criticalIncidents[].code`  
`string`  
 _Required_ |  The error code of this particular error. Error codes are DBSE+numeric strings, like "DBSE1012".   
`criticalIncidents[].createTime`  
`string`  
 _Required_ |  The timestamp when this Incident was created at the origin.   
`criticalIncidents[].message`  
`string`  
 _Optional_ |  The incident/error that occurred.   
`criticalIncidents[].messageTemplateParams`  
`object`  
 _Optional_ |  Contains key-value pairs necessary for generating a user-friendly data-driven version of Message in the user interface.   
`criticalIncidents[].resource`  
`object`  
 _Required_ |  Contains information about the Database Service component that reported the incident as well as about the Kubernetes resource.   
`criticalIncidents[].resource.component`  
`string`  
 _Required_ |  An internal identifier of the Database Service subsystem that reported the incident.   
`criticalIncidents[].resource.location`  
`object`  
 _Optional_ |  Location   
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
 _Optional_ |  TransientUntil if present indicates that the issue should be considered transient until the specified time.   
`lastBackupTime`  
`string`  
 _Optional_ |  The timestamp for the most recently executed backup.   
`nextBackupTime`  
`string`  
 _Optional_ |  The timestamp for the next scheduled backup.   
`observedGeneration`  
`integer`  
 _Optional_ |  Internal: The generation observed by the controller.   
`phase`  
`string`  
 _Optional_ |  The phase of a BackupPlan.   
`reconciled`  
`boolean`  
 _Optional_ |  Internal: Whether the resource was reconciled by the controller.   
`recoveryWindow`  
`object`  
 _Optional_ |  The currently available recovery window.   
`recoveryWindow.begin`  
`string`  
 _Optional_ |  Begin time.   
`recoveryWindow.end`  
`string`  
 _Optional_ |  End time.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
