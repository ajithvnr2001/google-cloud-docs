---
url: https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal/
title: Signal \u00a0|\u00a0 Database Center Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:51:29.243559+00:00
---

# Signal  |  Database Center Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal/

The Database Center REST and RPC APIs are in [Preview](https://docs.cloud.google.com/products#product-launch-stages). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Database Center ](https://docs.cloud.google.com/database-center/docs/overview)
  * [ Documentation ](https://docs.cloud.google.com/database-center/docs)
  * [ Reference ](https://docs.cloud.google.com/database-center/docs/reference)



Send feedback 

#  Signal Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * AdditionalDetail
    * JSON representation
  * RetentionSettingsInfo
    * JSON representation
  * SubResource
    * JSON representation
  * BackupRunInfo
    * JSON representation
  * State
  * OperationErrorType
  * SCCInfo
    * JSON representation
  * RegulatoryStandard
    * JSON representation
  * RecommendationInfo
    * JSON representation
  * AutomatedBackupPolicyInfo
    * JSON representation
  * DeletionProtectionInfo
    * JSON representation
  * ResourceSuspensionInfo
    * JSON representation
  * SuspensionReason
  * InefficientQueryInfo
    * JSON representation
  * OutdatedMinorVersionInfo
    * JSON representation
  * MaintenanceRecommendationInfo
    * JSON representation
  * SignalSource



Represents a signal.

JSON representation  
---  
      
    
    {
      "signalType": enum ([SignalType](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/SignalType)),
      "signalStatus": enum ([SignalStatus](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/SignalStatus)),
      "additionalDetails": [
        {
          object ([AdditionalDetail](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal#AdditionalDetail))
        }
      ],
      "issueSeverity": enum ([IssueSeverity](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/IssueSeverity)),
      "issueCreateTime": string
    }  
  
Fields  
---  
`signalType` |  `enum (`[SignalType](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/SignalType)`)` Type of the signal.  
`signalStatus` |  `enum (`[SignalStatus](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/SignalStatus)`)` Status of the signal.  
`additionalDetails[]` |  `object (`[AdditionalDetail](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal#AdditionalDetail)`)` Additional information related to the signal. In the case of composite signals, this field encapsulates details associated with granular signals, having a signal status of "ISSUE"; signals with a status of "OK" are not included. For granular signals, it encompasses information relevant to the signal, regardless of the signal status.  
`issueSeverity` |  `enum (`[IssueSeverity](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/IssueSeverity)`)` Severity of the issue.  
`issueCreateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp when the issue was created (when signal status is ISSUE).Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## AdditionalDetail

Details related to signal.

JSON representation  
---  
      
    
    {
      "signalSource": enum ([SignalSource](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal#SignalSource)),
      "signalType": enum ([SignalType](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/SignalType)),
      "signalEventTime": string,
    
      // Union field detail can be only one of the following:
      "shortBackupRetentionInfo": {
        object ([RetentionSettingsInfo](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal#RetentionSettingsInfo))
      },
      "backupRunInfo": {
        object ([BackupRunInfo](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal#BackupRunInfo))
      },
      "sccInfo": {
        object ([SCCInfo](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal#SCCInfo))
      },
      "recommendationInfo": {
        object ([RecommendationInfo](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal#RecommendationInfo))
      },
      "automatedBackupPolicyInfo": {
        object ([AutomatedBackupPolicyInfo](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal#AutomatedBackupPolicyInfo))
      },
      "deletionProtectionInfo": {
        object ([DeletionProtectionInfo](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal#DeletionProtectionInfo))
      },
      "resourceSuspensionInfo": {
        object ([ResourceSuspensionInfo](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal#ResourceSuspensionInfo))
      },
      "inefficientQueryInfo": {
        object ([InefficientQueryInfo](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal#InefficientQueryInfo))
      },
      "outdatedMinorVersionInfo": {
        object ([OutdatedMinorVersionInfo](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal#OutdatedMinorVersionInfo))
      },
      "maintenanceRecommendationInfo": {
        object ([MaintenanceRecommendationInfo](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal#MaintenanceRecommendationInfo))
      }
      // End of list of possible types for union field detail.
    }  
  
Fields  
---  
`signalSource` |  `enum (`[SignalSource](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal#SignalSource)`)` Where the signal is coming from.  
`signalType` |  `enum (`[SignalType](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/SignalType)`)` Type of the signal.  
`signalEventTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Event time when signal was recorded by source service.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
Union field `detail`. Details related to signal. `detail` can be only one of the following:  
`shortBackupRetentionInfo` |  `object (`[RetentionSettingsInfo](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal#RetentionSettingsInfo)`)` Short backup retention information applies to signals with type SIGNAL_TYPE_SHORT_BACKUP_RETENTION.  
`backupRunInfo` |  `object (`[BackupRunInfo](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal#BackupRunInfo)`)` Backup run information applies to signals with types SIGNAL_TYPE_LAST_BACKUP_FAILED and SIGNAL_TYPE_LAST_BACKUP_OLD.  
`sccInfo` |  `object (`[SCCInfo](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal#SCCInfo)`)` SCC information applies to SCC signals.  
`recommendationInfo` |  `object (`[RecommendationInfo](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal#RecommendationInfo)`)` Recommendation information applies to recommendations.  
`automatedBackupPolicyInfo` |  `object (`[AutomatedBackupPolicyInfo](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal#AutomatedBackupPolicyInfo)`)` Automated backup policy information applies to signals with type SIGNAL_TYPE_NO_AUTOMATED_BACKUP_POLICY.  
`deletionProtectionInfo` |  `object (`[DeletionProtectionInfo](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal#DeletionProtectionInfo)`)` Deletion protection information applies to signals with type `[SIGNAL_TYPE_NO_DELETION_PROTECTION](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/SignalType#ENUM_VALUES.SIGNAL_TYPE_NO_DELETION_PROTECTION)`  
`resourceSuspensionInfo` |  `object (`[ResourceSuspensionInfo](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal#ResourceSuspensionInfo)`)` Resource suspension information applies to signals with type `[SIGNAL_TYPE_RESOURCE_SUSPENDED](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/SignalType#ENUM_VALUES.SIGNAL_TYPE_RESOURCE_SUSPENDED)`.  
`inefficientQueryInfo` |  `object (`[InefficientQueryInfo](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal#InefficientQueryInfo)`)` Inefficient query information applies to signals with type `[SIGNAL_TYPE_INEFFICIENT_QUERY](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/SignalType#ENUM_VALUES.SIGNAL_TYPE_INEFFICIENT_QUERY)`.  
`outdatedMinorVersionInfo` |  `object (`[OutdatedMinorVersionInfo](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal#OutdatedMinorVersionInfo)`)` Outdated minor version information applies to signals with type SIGNAL_TYPE_OUTDATED_MINOR_VERSION.  
`maintenanceRecommendationInfo` |  `object (`[MaintenanceRecommendationInfo](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal#MaintenanceRecommendationInfo)`)` Maintenance recommendation information applies to signals with type SIGNAL_TYPE_RECOMMENDED_MAINTENANCE_POLICIES.  
  
## RetentionSettingsInfo

Metadata about backup retention settings for a database resource.

JSON representation  
---  
      
    
    {
      "subResource": {
        object ([SubResource](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal#SubResource))
      },
    
      // Union field retention can be only one of the following:
      "quantityBasedRetention": integer,
      "durationBasedRetention": string,
      "timestampBasedRetentionTime": string
      // End of list of possible types for union field retention.
    }  
  
Fields  
---  
`subResource` |  `object (`[SubResource](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal#SubResource)`)` Optional. Sub resource details associated with the backup configuration.  
Union field `retention`. Depending on the value of retention_unit, this is used to determine if a backup needs to be deleted. If retention_unit is 'COUNT', we will retain this many backups. `retention` can be only one of the following:  
`quantityBasedRetention` |  `integer` Number of backups that will be retained.  
`durationBasedRetention` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Duration based retention period i.e. 172800 seconds (2 days)A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`timestampBasedRetentionTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp based retention period i.e. till 2024-05-01T00:00:00ZUses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## SubResource

Sub resource details For Spanner/Bigtable instance certain data protection settings are at sub resource level like database/table. This message is used to capture such sub resource details.

JSON representation  
---  
      
    
    {
      "resourceType": string,
      "fullResourceName": string,
      "product": {
        object ([Product](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Product))
      },
      "container": string
    }  
  
Fields  
---  
`resourceType` |  `string` Optional. Resource type associated with the sub resource where backup settings are configured. E.g. "spanner.googleapis.com/Database" for Spanner where backup retention is configured on database within an instance OPTIONAL  
`fullResourceName` |  `string` Optional. Resource name associated with the sub resource where backup settings are configured. E.g."//spanner.googleapis.com/projects/project1/instances/inst1/databases/db1" for Spanner where backup retention is configured on database within an instance OPTIONAL  
`product` |  `object (`[Product](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Product)`)` Optional. Product information associated with the sub resource where backup retention settings are configured. e.g.
    
    
    product: {
     type   : PRODUCT_TYPE_SPANNER
     engine : ENGINE_CLOUD_SPANNER_WITH_POSTGRES_DIALECT
    }
    

for Spanner where backup is configured on database within an instance OPTIONAL  
`container` |  `string` Specifies where the resource is created. For Google Cloud resources, it is the full name of the project.  
  
## BackupRunInfo

Metadata about latest backup run state for a database resource.

JSON representation  
---  
      
    
    {
      "startTime": string,
      "endTime": string,
      "state": enum ([State](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal#State)),
      "errorMessage": string,
      "operationErrorType": enum ([OperationErrorType](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal#OperationErrorType)),
      "subResource": {
        object ([SubResource](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal#SubResource))
      }
    }  
  
Fields  
---  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time the backup operation started.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time the backup operation completed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal#State)`)` Output only. The state of this run.  
`errorMessage` |  `string` Additional information about the error encountered.  
`operationErrorType` |  `enum (`[OperationErrorType](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal#OperationErrorType)`)` Optional. OperationErrorType to expose specific error when backup operation of database resource failed, that is state is FAILED.  
`subResource` |  `object (`[SubResource](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal#SubResource)`)` Optional. Sub resource details associated with the backup run.  
  
## State

The status of a backup run.

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified.  
`SUCCEEDED` | The backup succeeded.  
`FAILED` | The backup was unsuccessful.  
  
## OperationErrorType

OperationErrorType is used to expose specific error type which can happen in database resource while performing an operation. For example, an error can happen while database resource being backed up.

Enums  
---  
`OPERATION_ERROR_TYPE_UNSPECIFIED` | UNSPECIFIED means operation error type is not known or available.  
`KMS_KEY_ERROR` | Key destroyed, expired, not found, unreachable or permission denied.  
`DATABASE_ERROR` | Database is not accessible.  
`STOCKOUT_ERROR` | The zone or region does not have sufficient resources to handle the request at the moment.  
`CANCELLATION_ERROR` | User initiated cancellation.  
`SQLSERVER_ERROR` | SQL server specific error.  
`INTERNAL_ERROR` | Any other internal error.  
  
## SCCInfo

Info associated with SCC signals.

JSON representation  
---  
      
    
    {
      "signal": string,
      "category": string,
      "regulatoryStandards": [
        {
          object ([RegulatoryStandard](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal#RegulatoryStandard))
        }
      ],
      "externalUri": string
    }  
  
Fields  
---  
`signal` |  `string` Name of the signal.  
`category` |  `string` Name by which SCC calls this signal.  
`regulatoryStandards[]` |  `object (`[RegulatoryStandard](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal#RegulatoryStandard)`)` Compliances that are associated with the signal.  
`externalUri` |  `string` External URI which points to a SCC page associated with the signal.  
  
## RegulatoryStandard

Compliances associated with signals.

JSON representation  
---  
      
    
    {
      "standard": string,
      "version": string
    }  
  
Fields  
---  
`standard` |  `string` Name of industry compliance standards, such as such as CIS, PCI, and OWASP.  
`version` |  `string` Version of the standard or benchmark, for example, 1.1.  
  
## RecommendationInfo

Info associated with recommendation.

JSON representation  
---  
      
    
    {
      "recommender": string,
      "recommenderId": string,
      "recommenderSubtype": string
    }  
  
Fields  
---  
`recommender` |  `string` Name of recommendation. Examples: organizations/1234/locations/us-central1/recommenders/google.cloudsql.instance.PerformanceRecommender/recommendations/9876  
`recommenderId` |  `string` ID of recommender. Examples: "google.cloudsql.instance.PerformanceRecommender"  
`recommenderSubtype` |  `string` Contains an identifier for a subtype of recommendations produced for the same recommender. Subtype is a function of content and impact, meaning a new subtype might be added when significant changes to `content` or `primary_impact.category` are introduced. See the Recommenders section to see a list of subtypes for a given Recommender.Examples: For recommender = "google.cloudsql.instance.PerformanceRecommender", recommenderSubtype can be "MYSQL_HIGH_NUMBER_OF_OPEN_TABLES_BEST_PRACTICE"/"POSTGRES_HIGH_TRANSACTION_ID_UTILIZATION_BEST_PRACTICE"  
  
## AutomatedBackupPolicyInfo

Automated backup policy signal info

JSON representation  
---  
      
    
    {
      "subResource": {
        object ([SubResource](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal#SubResource))
      },
      "isEnabled": boolean
    }  
  
Fields  
---  
`subResource` |  `object (`[SubResource](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal#SubResource)`)` Optional. Sub resource details associated with the signal.  
`isEnabled` |  `boolean` Is automated policy enabled.  
  
## DeletionProtectionInfo

Deletion protection signal info for a database resource.

JSON representation  
---  
      
    
    {
      "subResource": {
        object ([SubResource](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal#SubResource))
      },
      "deletionProtectionEnabled": boolean
    }  
  
Fields  
---  
`subResource` |  `object (`[SubResource](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal#SubResource)`)` Optional. Sub resource details associated with the signal.  
`deletionProtectionEnabled` |  `boolean` Is deletion protection enabled.  
  
## ResourceSuspensionInfo

Resource suspension info for a database resource.

JSON representation  
---  
      
    
    {
      "resourceSuspended": boolean,
      "suspensionReason": enum ([SuspensionReason](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal#SuspensionReason))
    }  
  
Fields  
---  
`resourceSuspended` |  `boolean` Is resource suspended.  
`suspensionReason` |  `enum (`[SuspensionReason](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal#SuspensionReason)`)` Suspension reason for the resource.  
  
## SuspensionReason

The reason for suspension of the database resource.

Enums  
---  
`SUSPENSION_REASON_UNSPECIFIED` | Suspension reason is unspecified.  
`WIPEOUT_HIDE_EVENT` | Wipeout hide event.  
`WIPEOUT_PURGE_EVENT` | Wipeout purge event.  
`BILLING_DISABLED` | Billing disabled for project  
`ABUSER_DETECTED` | Abuse detected for resource  
`ENCRYPTION_KEY_INACCESSIBLE` | Encryption key inaccessible.  
`REPLICATED_CLUSTER_ENCRYPTION_KEY_INACCESSIBLE` | Replicated cluster encryption key inaccessible.  
  
## InefficientQueryInfo

Metadata about inefficient query signal info for a database resource.

JSON representation  
---  
      
    
    {
      "database": string,
      "table": string,
      "sqlIndexStatement": string,
      "storageCostBytes": string,
      "impactedQueriesCount": string
    }  
  
Fields  
---  
`database` |  `string` Name of the database where index is required. For example, "db1", which is the name of the database present in the instance.  
`table` |  `string` Name of the table where index is required  
`sqlIndexStatement` |  `string` SQL statement of the index. Based on the ddl type, this will be either CREATE INDEX or DROP INDEX.  
`storageCostBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Cost of additional disk usage in bytes  
`impactedQueriesCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Count of queries to be impacted if index is applied  
  
## OutdatedMinorVersionInfo

Info associated with outdated minor version.

JSON representation  
---  
      
    
    {
      "recommendedMinorVersion": string
    }  
  
Fields  
---  
`recommendedMinorVersion` |  `string` Recommended minor version of the underlying database engine. Example values: For MySQL, it could be "8.0.35", "5.7.25" etc. For PostgreSQL, it could be "14.4", "15.5" etc.  
  
## MaintenanceRecommendationInfo

Info associated with maintenance recommendation.

JSON representation  
---  
      
    
    {
      "resourceMaintenanceSchedules": [
        {
          object ([ResourceMaintenanceSchedule](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/ResourceMaintenanceSchedule))
        }
      ]
    }  
  
Fields  
---  
`resourceMaintenanceSchedules[]` |  `object (`[ResourceMaintenanceSchedule](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/ResourceMaintenanceSchedule)`)` Optional. List of recommended maintenance schedules for the database resource.  
  
## SignalSource

Represents the source system from where a signal comes from. More enum values are expected to be added as needed.

Enums  
---  
`SIGNAL_SOURCE_UNSPECIFIED` | Unspecified.  
`SIGNAL_SOURCE_RESOURCE_METADATA` | Signal comes from resource metadata.  
`SIGNAL_SOURCE_SECURITY_FINDINGS` | Signal comes from SCC findings.  
`SIGNAL_SOURCE_RECOMMENDER` | Signal comes from recommender hub.  
`SIGNAL_SOURCE_MODERN_OBSERVABILITY` | Signal comes from modern observability platform.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-22 UTC."],[],[]] 
