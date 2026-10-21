---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans
title: REST Resource: projects.locations.backupPlans \u00a0|\u00a0 Backup for GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:41:33.142800+00:00
---

# REST Resource: projects.locations.backupPlans  |  Backup for GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ APIs & Reference ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest)



Send feedback 

#  REST Resource: projects.locations.backupPlans Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: BackupPlan
    * JSON representation
  * RetentionPolicy
    * JSON representation
  * Schedule
    * JSON representation
  * RpoConfig
    * JSON representation
  * ExclusionWindow
    * JSON representation
  * TimeOfDay
    * JSON representation
  * Date
    * JSON representation
  * DayOfWeekList
    * JSON representation
  * DayOfWeek
  * BackupConfig
    * JSON representation
  * State
  * Methods



## Resource: BackupPlan

Defines the configuration and scheduling for a "line" of Backups.

JSON representation  
---  
      
    
    {
      "name": string,
      "uid": string,
      "createTime": string,
      "updateTime": string,
      "description": string,
      "cluster": string,
      "retentionPolicy": {
        object ([RetentionPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans#RetentionPolicy))
      },
      "labels": {
        string: string,
        ...
      },
      "backupSchedule": {
        object ([Schedule](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans#Schedule))
      },
      "etag": string,
      "deactivated": boolean,
      "backupConfig": {
        object ([BackupConfig](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans#BackupConfig))
      },
      "protectedPodCount": integer,
      "protectedNamespaceCount": integer,
      "state": enum ([State](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans#State)),
      "stateReason": string,
      "rpoRiskLevel": integer,
      "rpoRiskReason": string,
      "backupChannel": string,
      "lastSuccessfulBackupTime": string
    }  
  
Fields  
---  
`name` |  `string` Output only. Identifier. The full name of the BackupPlan resource. Format: `projects/*/locations/*/backupPlans/*`  
`uid` |  `string` Output only. Server generated global unique identifier of [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) format.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when this BackupPlan resource was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when this BackupPlan resource was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`description` |  `string` Optional. User specified descriptive string for this BackupPlan.  
`cluster` |  `string` Required. Immutable. The source cluster from which Backups will be created via this BackupPlan. Valid formats:

  * `projects/*/locations/*/clusters/*`
  * `projects/*/zones/*/clusters/*`

  
`retentionPolicy` |  `object (`[RetentionPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans#RetentionPolicy)`)` Optional. RetentionPolicy governs lifecycle of Backups created under this plan.  
`labels` |  `map (key: string, value: string)` Optional. A set of custom labels supplied by user.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`backupSchedule` |  `object (`[Schedule](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans#Schedule)`)` Optional. Defines a schedule for automatic Backup creation via this BackupPlan.  
`etag` |  `string` Output only. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a backup plan from overwriting each other. It is strongly suggested that systems make use of the 'etag' in the read-modify-write cycle to perform BackupPlan updates in order to avoid race conditions: An `etag` is returned in the response to `backupPlans.get`, and systems are expected to put that etag in the request to `backupPlans.patch` or `backupPlans.delete` to ensure that their change will be applied to the same version of the resource.  
`deactivated` |  `boolean` Optional. This flag indicates whether this BackupPlan has been deactivated. Setting this field to True locks the BackupPlan such that no further updates will be allowed (except deletes), including the deactivated field itself. It also prevents any new Backups from being created via this BackupPlan (including scheduled Backups).Default: False  
`backupConfig` |  `object (`[BackupConfig](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans#BackupConfig)`)` Optional. Defines the configuration of Backups created via this BackupPlan.  
`protectedPodCount` |  `integer` Output only. The number of Kubernetes Pods backed up in the last successful Backup created via this BackupPlan.  
`protectedNamespaceCount` |  `integer` Output only. The number of user managed namespaces backed up in the last successful Backup created via this BackupPlan.  
`state` |  `enum (`[State](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans#State)`)` Output only. State of the BackupPlan. This State field reflects the various stages a BackupPlan can be in during the Create operation. It will be set to "DEACTIVATED" if the BackupPlan is deactivated on an Update  
`stateReason` |  `string` Output only. Human-readable description of why BackupPlan is in the current `state`. This field is only meant for human readability and should not be used programmatically as this field is not guaranteed to be consistent.  
`rpoRiskLevel` |  `integer` Output only. A number that represents the current risk level of this BackupPlan from RPO perspective with 1 being no risk and 5 being highest risk.  
`rpoRiskReason` |  `string` Output only. Human-readable description of why the BackupPlan is in the current rpoRiskLevel and action items if any.  
`backupChannel` |  `string` Output only. The fully qualified name of the BackupChannel to be used to create a backup. This field is set only if the cluster being backed up is in a different project. `projects/*/locations/*/backupChannels/*`  
`lastSuccessfulBackupTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Completion time of the last successful Backup. This is sourced from a successful Backup's completeTime field. This field is added to maintain consistency with BackupPlanBinding to display last successful backup time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## RetentionPolicy

RetentionPolicy defines a Backup retention policy for a BackupPlan.

JSON representation  
---  
      
    
    {
      "backupDeleteLockDays": integer,
      "backupRetainDays": integer,
      "locked": boolean
    }  
  
Fields  
---  
`backupDeleteLockDays` |  `integer` Optional. Minimum age for Backups created via this BackupPlan (in days). This field MUST be an integer value between 0-90 (inclusive). A Backup created under this BackupPlan will NOT be deletable until it reaches Backup's (createTime + backupDeleteLockDays). Updating this field of a BackupPlan does NOT affect existing Backups under it. Backups created AFTER a successful update will inherit the new value.Default: 0 (no delete blocking)  
`backupRetainDays` |  `integer` Optional. The default maximum age of a Backup created via this BackupPlan. This field MUST be an integer value >= 0 and <= 365. If specified, a Backup created under this BackupPlan will be automatically deleted after its age reaches (createTime + backupRetainDays). If not specified, Backups created under this BackupPlan will NOT be subject to automatic deletion. Updating this field does NOT affect existing Backups under it. Backups created AFTER a successful update will automatically pick up the new value. NOTE: backupRetainDays must be >= `[backupDeleteLockDays](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans#RetentionPolicy.FIELDS.backup_delete_lock_days)`. If `[cronSchedule](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans#Schedule.FIELDS.cron_schedule)` is defined, then this must be <= 360 * the creation interval. If `[rpoConfig](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans#Schedule.FIELDS.rpo_config)` is defined, then this must be <= 360 * [targetRpoMinutes][Schedule.rpo_config.target_rpo_minutes] / (1440minutes/day).Default: 0 (no automatic deletion)  
`locked` |  `boolean` Optional. This flag denotes whether the retention policy of this BackupPlan is locked. If set to True, no further update is allowed on this policy, including the `locked` field itself.Default: False  
  
## Schedule

Defines scheduling parameters for automatically creating Backups via this BackupPlan.

JSON representation  
---  
      
    
    {
      "cronSchedule": string,
      "paused": boolean,
      "rpoConfig": {
        object ([RpoConfig](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans#RpoConfig))
      },
      "nextScheduledBackupTime": string
    }  
  
Fields  
---  
`cronSchedule` |  `string` Optional. A standard [cron](https://wikipedia.com/wiki/cron) string that defines a repeating schedule for creating Backups via this BackupPlan. This is mutually exclusive with the `[rpoConfig](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans#Schedule.FIELDS.rpo_config)` field since at most one schedule can be defined for a BackupPlan. If this is defined, then `[backupRetainDays](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans#RetentionPolicy.FIELDS.backup_retain_days)` must also be defined.Default (empty): no automatic backup creation will occur.  
`paused` |  `boolean` Optional. This flag denotes whether automatic Backup creation is paused for this BackupPlan.Default: False  
`rpoConfig` |  `object (`[RpoConfig](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans#RpoConfig)`)` Optional. Defines the RPO schedule configuration for this BackupPlan. This is mutually exclusive with the `[cronSchedule](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans#Schedule.FIELDS.cron_schedule)` field since at most one schedule can be defined for a BackupPLan. If this is defined, then `[backupRetainDays](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans#RetentionPolicy.FIELDS.backup_retain_days)` must also be defined.Default (empty): no automatic backup creation will occur.  
`nextScheduledBackupTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Start time of next scheduled backup under this BackupPlan by either cronSchedule or rpo config.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## RpoConfig

Defines RPO scheduling configuration for automatically creating Backups via this BackupPlan.

JSON representation  
---  
      
    
    {
      "targetRpoMinutes": integer,
      "exclusionWindows": [
        {
          object ([ExclusionWindow](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans#ExclusionWindow))
        }
      ]
    }  
  
Fields  
---  
`targetRpoMinutes` |  `integer` Required. Defines the target RPO for the BackupPlan in minutes, which means the target maximum data loss in time that is acceptable for this BackupPlan. This must be at least 60, i.e., 1 hour, and at most 86400, i.e., 60 days.  
`exclusionWindows[]` |  `object (`[ExclusionWindow](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans#ExclusionWindow)`)` Optional. User specified time windows during which backup can NOT happen for this BackupPlan - backups should start and finish outside of any given exclusion window. Note: backup jobs will be scheduled to start and finish outside the duration of the window as much as possible, but running jobs will not get canceled when it runs into the window. All the time and date values in exclusionWindows entry in the API are in UTC. We only allow <=1 recurrence (daily or weekly) exclusion window for a BackupPlan while no restriction on number of single occurrence windows.  
  
## ExclusionWindow

Defines a time window during which no backup should happen. All time and date are in UTC.

JSON representation  
---  
      
    
    {
      "duration": string,
      "startTime": {
        object ([TimeOfDay](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans#TimeOfDay))
      },
    
      // Union field recurrence can be only one of the following:
      "singleOccurrenceDate": {
        object ([Date](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans#Date))
      },
      "daily": boolean,
      "daysOfWeek": {
        object ([DayOfWeekList](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans#DayOfWeekList))
      }
      // End of list of possible types for union field recurrence.
    }  
  
Fields  
---  
`duration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Required. Specifies duration of the window. Duration must be >= 5 minutes and < (target RPO - 20 minutes). Additional restrictions based on the recurrence type to allow some time for backup to happen: - singleOccurrenceDate: no restriction, but UI may warn about this when duration >= target RPO - daily window: duration < 24 hours - weekly window: - days of week includes all seven days of a week: duration < 24 hours - all other weekly window: duration < 168 hours (i.e., 24 * 7 hours)A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`startTime` |  `object (`[TimeOfDay](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans#TimeOfDay)`)` Optional. Specifies the start time of the window using time of the day in UTC.  
Union field `recurrence`. Required. Specifies the day(s) on which the exclusion window takes effect. Exactly one of the fields MUST be specified. `recurrence` can be only one of the following:  
`singleOccurrenceDate` |  `object (`[Date](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans#Date)`)` No recurrence. The exclusion window occurs only once and on this date in UTC.  
`daily` |  `boolean` The exclusion window occurs every day if set to "True". Specifying this field to "False" is an error.  
`daysOfWeek` |  `object (`[DayOfWeekList](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans#DayOfWeekList)`)` The exclusion window occurs on these days of each week in UTC.  
  
## TimeOfDay

Represents a time of day. The date and time zone are either not significant or are specified elsewhere. An API may choose to allow leap seconds. Related types are `[google.type.Date](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans#Date)` and `google.protobuf.Timestamp`.

JSON representation  
---  
      
    
    {
      "hours": integer,
      "minutes": integer,
      "seconds": integer,
      "nanos": integer
    }  
  
Fields  
---  
`hours` |  `integer` Hours of a day in 24 hour format. Must be greater than or equal to 0 and typically must be less than or equal to 23. An API may choose to allow the value "24:00:00" for scenarios like business closing time.  
`minutes` |  `integer` Minutes of an hour. Must be greater than or equal to 0 and less than or equal to 59.  
`seconds` |  `integer` Seconds of a minute. Must be greater than or equal to 0 and typically must be less than or equal to 59. An API may allow the value 60 if it allows leap-seconds.  
`nanos` |  `integer` Fractions of seconds, in nanoseconds. Must be greater than or equal to 0 and less than or equal to 999,999,999.  
  
## Date

Represents a whole or partial calendar date, such as a birthday. The time of day and time zone are either specified elsewhere or are insignificant. The date is relative to the Gregorian Calendar. This can represent one of the following:

  * A full date, with non-zero year, month, and day values.
  * A month and day, with a zero year (for example, an anniversary).
  * A year on its own, with a zero month and a zero day.
  * A year and month, with a zero day (for example, a credit card expiration date).



Related types:

  * `[google.type.TimeOfDay](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans#TimeOfDay)`
  * `google.type.DateTime`
  * `[google.protobuf.Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)`

JSON representation  
---  
      
    
    {
      "year": integer,
      "month": integer,
      "day": integer
    }  
  
Fields  
---  
`year` |  `integer` Year of the date. Must be from 1 to 9999, or 0 to specify a date without a year.  
`month` |  `integer` Month of a year. Must be from 1 to 12, or 0 to specify a year without a month and day.  
`day` |  `integer` Day of a month. Must be from 1 to 31 and valid for the year and month, or 0 to specify a year by itself or a year and month where the day isn't significant.  
  
## DayOfWeekList

Holds repeated DaysOfWeek values as a container.

JSON representation  
---  
      
    
    {
      "daysOfWeek": [
        enum ([DayOfWeek](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans#DayOfWeek))
      ]
    }  
  
Fields  
---  
`daysOfWeek[]` |  `enum (`[DayOfWeek](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans#DayOfWeek)`)` Optional. A list of days of week.  
  
## DayOfWeek

Represents a day of the week.

Enums  
---  
`DAY_OF_WEEK_UNSPECIFIED` | The day of the week is unspecified.  
`MONDAY` | Monday  
`TUESDAY` | Tuesday  
`WEDNESDAY` | Wednesday  
`THURSDAY` | Thursday  
`FRIDAY` | Friday  
`SATURDAY` | Saturday  
`SUNDAY` | Sunday  
  
## BackupConfig

BackupConfig defines the configuration of Backups created via this BackupPlan.

JSON representation  
---  
      
    
    {
      "includeVolumeData": boolean,
      "includeSecrets": boolean,
      "encryptionKey": {
        object ([EncryptionKey](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/EncryptionKey))
      },
      "permissiveMode": boolean,
    
      // Union field backup_scope can be only one of the following:
      "allNamespaces": boolean,
      "selectedNamespaces": {
        object ([Namespaces](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/Namespaces))
      },
      "selectedApplications": {
        object ([NamespacedNames](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/NamespacedNames))
      },
      "selectedNamespaceLabels": {
        object ([ResourceLabels](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/ResourceLabels))
      }
      // End of list of possible types for union field backup_scope.
    }  
  
Fields  
---  
`includeVolumeData` |  `boolean` Optional. This flag specifies whether volume data should be backed up when PVCs are included in the scope of a Backup.Default: False  
`includeSecrets` |  `boolean` Optional. This flag specifies whether Kubernetes Secret resources should be included when they fall into the scope of Backups.Default: False  
`encryptionKey` |  `object (`[EncryptionKey](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/EncryptionKey)`)` Optional. This defines a customer managed encryption key that will be used to encrypt the "config" portion (the Kubernetes resources) of Backups created via this plan.Default (empty): Config backup artifacts will not be encrypted.  
`permissiveMode` |  `boolean` Optional. If false, Backups will fail when Backup for GKE detects Kubernetes configuration that is non-standard or requires additional setup to restore.Default: False  
Union field `backup_scope`. This defines the "scope" of the Backup - which namespaced resources in the cluster will be included in a Backup. Exactly one of the fields of backup_scope MUST be specified. `backup_scope` can be only one of the following:  
`allNamespaces` |  `boolean` If True, include all namespaced resources  
`selectedNamespaces` |  `object (`[Namespaces](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/Namespaces)`)` If set, include just the resources in the listed namespaces.  
`selectedApplications` |  `object (`[NamespacedNames](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/NamespacedNames)`)` If set, include just the resources referenced by the listed ProtectedApplications.  
`selectedNamespaceLabels` |  `object (`[ResourceLabels](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/ResourceLabels)`)` If set, the list of labels whose constituent namespaces were included in the Backup.  
  
## State

State

Enums  
---  
`STATE_UNSPECIFIED` | Default first value for Enums.  
`CLUSTER_PENDING` | Waiting for cluster state to be RUNNING.  
`PROVISIONING` | The BackupPlan is in the process of being created.  
`READY` | The BackupPlan has successfully been created and is ready for Backups.  
`FAILED` | BackupPlan creation has failed.  
`DEACTIVATED` | The BackupPlan has been deactivated.  
`DELETING` | The BackupPlan is in the process of being deleted.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans/create)`

|  Creates a new BackupPlan in a given location.  
  
### `[delete](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans/delete)`

|  Deletes an existing BackupPlan.  
  
### `[get](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans/get)`

|  Retrieve the details of a single BackupPlan.  
  
### `[getIamPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[getTags](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans/getTags)`

|  Returns tags directly bound to a GCP resource.  
  
### `[list](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans/list)`

|  Lists BackupPlans in a given location.  
  
### `[patch](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans/patch)`

|  Update a BackupPlan.  
  
### `[setIamPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[setTags](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans/setTags)`

|  Updates tags directly bound to a GCP resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-15 UTC."],[],[]] 
