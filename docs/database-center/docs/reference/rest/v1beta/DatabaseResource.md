---
url: https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource/
title: DatabaseResource \u00a0|\u00a0 Database Center Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:51:28.625718+00:00
---

# DatabaseResource  |  Database Center Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource/

The Database Center REST and RPC APIs are in [Preview](https://docs.cloud.google.com/products#product-launch-stages). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Database Center ](https://docs.cloud.google.com/database-center/docs/overview)
  * [ Documentation ](https://docs.cloud.google.com/database-center/docs)
  * [ Reference ](https://docs.cloud.google.com/database-center/docs/reference)



Send feedback 

#  DatabaseResource Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Label
    * JSON representation
  * Tag
    * JSON representation
  * MachineConfig
    * JSON representation
  * SignalGroup
    * JSON representation
  * Metrics
    * JSON representation
  * MetricData
    * JSON representation
  * TypedValue
    * JSON representation
  * BackupDRConfig
    * JSON representation
  * MaintenanceInfo
    * JSON representation
  * ResourceMaintenanceDenySchedule
    * JSON representation



DatabaseResource represents every individually configured database unit representing compute and/or storage.

JSON representation  
---  
      
    
    {
      "childResources": [
        {
          object ([DatabaseResource](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource))
        }
      ],
      "fullResourceName": string,
      "container": string,
      "product": {
        object ([Product](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Product))
      },
      "location": string,
      "labels": [
        {
          object ([Label](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource#Label))
        }
      ],
      "tags": [
        {
          object ([Tag](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource#Tag))
        }
      ],
      "resourceType": string,
      "subResourceType": enum ([SubResourceType](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/SubResourceType)),
      "machineConfig": {
        object ([MachineConfig](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource#MachineConfig))
      },
      "signalGroups": [
        {
          object ([SignalGroup](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource#SignalGroup))
        }
      ],
      "metrics": {
        object ([Metrics](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource#Metrics))
      },
      "resourceCategory": enum ([ResourceCategory](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/ResourceCategory)),
      "resourceName": string,
      "backupdrConfig": {
        object ([BackupDRConfig](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource#BackupDRConfig))
      },
      "edition": enum ([Edition](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Edition)),
      "maintenanceInfo": {
        object ([MaintenanceInfo](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource#MaintenanceInfo))
      }
    }  
  
Fields  
---  
`childResources[]` |  `object (`[DatabaseResource](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource)`)` List of children associated with a database group.  
`fullResourceName` |  `string` The full resource name, based on CAIS resource name format <https://cloud.google.com/asset-inventory/docs/resource-name-format>Example:`//cloudsql.googleapis.com/projects/project-number/instances/mysql-1` `//cloudsql.googleapis.com/projects/project-number/instances/postgres-1` `//spanner.googleapis.com/projects/project-number/instances/spanner-instance-1` `//alloydb.googleapis.com/projects/project-number/locations/us-central1/clusters/c1` `//alloydb.googleapis.com/projects/project-number/locations/us-central1/clusters/c1/instances/i1`  
`container` |  `string` Specifies where the resource is created. For Google Cloud resources, it is the full name of the project.  
`product` |  `object (`[Product](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Product)`)` The product this resource represents.  
`location` |  `string` The location of the resources. It supports returning only regional locations in Google Cloud. These are of the form: "us-central1", "us-east1", etc. See <https://cloud.google.com/about/locations> for a list of such regions.  
`labels[]` |  `object (`[Label](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource#Label)`)` Labels applied on the resource. The requirements for labels assigned to Google Cloud resources may be found at <https://cloud.google.com/resource-manager/docs/labels-overview#requirements>  
`tags[]` |  `object (`[Tag](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource#Tag)`)` Tags applied on the resource. The requirements for tags assigned to Google Cloud resources may be found at <https://cloud.google.com/resource-manager/docs/tags/tags-overview>  
`resourceType` |  `string` The type of resource defined according to the pattern: {Service Name}/{Type}. Ex: sqladmin.googleapis.com/Instance alloydb.googleapis.com/Cluster alloydb.googleapis.com/Instance spanner.googleapis.com/Instance  
`subResourceType` |  `enum (`[SubResourceType](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/SubResourceType)`)` Subtype of the resource specified at creation time.  
`machineConfig` |  `object (`[MachineConfig](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource#MachineConfig)`)` Machine configuration like CPU, memory, etc for the resource.  
`signalGroups[]` |  `object (`[SignalGroup](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource#SignalGroup)`)` The list of signal groups and count of issues related to the resource. Only those signals which have been requested would be included.  
`metrics` |  `object (`[Metrics](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource#Metrics)`)` Observable metrics for the resource e.g. CPU utilization, memory utilization, etc.  
`resourceCategory` |  `enum (`[ResourceCategory](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/ResourceCategory)`)` The category of the resource.  
`resourceName` |  `string` The name of the resource(The last part of the full resource name). Example: For full resource name - `//cloudsql.googleapis.com/projects/project-number/instances/mysql-1`, resource name - `mysql-1` For full resource name - `//cloudsql.googleapis.com/projects/project-number/instances/postgres-1` , resource name - `postgres-1` Note: In some cases, there might be more than one resource with the same resource name.  
`backupdrConfig` |  `object (`[BackupDRConfig](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource#BackupDRConfig)`)` Optional. Backup and disaster recovery details for the resource.  
`edition` |  `enum (`[Edition](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Edition)`)` The edition of the resource.  
`maintenanceInfo` |  `object (`[MaintenanceInfo](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource#MaintenanceInfo)`)` Optional. The maintenance information of the resource.  
  
## Label

Label is a key value pair applied to a resource.

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string,
      "source": string
    }  
  
Fields  
---  
`key` |  `string` The key part of the label.  
`value` |  `string` The value part of the label.  
`source` |  `string` The source of the Label. Source is empty if the label is directly attached to the resource and not inherited.  
  
## Tag

Tag is a key value pair attached to a resource.

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string,
      "source": string,
      "inherited": boolean
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string` The value part of the tag.  
`source` |  `string` The source of the tag. According to <https://cloud.google.com/resource-manager/docs/tags/tags-overview#tags_and_labels>, tags can be created only at the project or organization level. Tags can be inherited from different project as well not just the current project where the database resource is present. Format: "projects/{PROJECT_ID}", "projects/{PROJECT_NUMBER}", "organizations/{ORGANIZATION_ID}"  
`inherited` |  `boolean` Indicates the inheritance status of a tag value attached to the given resource. If the tag value is inherited from one of the resource's ancestors, inherited will be true. If false, then the tag value is directly attached to the resource.  
  
## MachineConfig

MachineConfig describes the configuration of a machine specific to a Database Resource.

JSON representation  
---  
      
    
    {
      "memorySizeBytes": string,
      "shardCount": integer,
      "vcpuCount": number
    }  
  
Fields  
---  
`memorySizeBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Memory size in bytes.  
`shardCount` |  `integer` Optional. The number of Shards (if applicable).  
`vcpuCount` |  `number` Optional. The number of vCPUs (if applicable).  
  
## SignalGroup

A group of signals and their counts.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "issueCount": integer,
      "signals": [
        {
          object ([Signal](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal))
        }
      ]
    }  
  
Fields  
---  
`displayName` |  `string` Title of a signal group corresponding to the request.  
`issueCount` |  `integer` When applied to a DatabaseResource represents count of issues associated with the resource. A signal is an issue when its SignalStatus field is set to SIGNAL_STATUS_ISSUE.  
`signals[]` |  `object (`[Signal](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Signal)`)` List of signals present in the group and associated with the resource.Only applies to a DatabaseResource.  
  
## Metrics

Metrics represents the metrics for a database resource.

JSON representation  
---  
      
    
    {
      "p99CpuUtilization": {
        object ([MetricData](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource#MetricData))
      },
      "p95CpuUtilization": {
        object ([MetricData](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource#MetricData))
      },
      "currentStorageUsedBytes": {
        object ([MetricData](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource#MetricData))
      },
      "peakStorageUtilization": {
        object ([MetricData](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource#MetricData))
      },
      "peakMemoryUtilization": {
        object ([MetricData](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource#MetricData))
      },
      "peakNumberConnections": {
        object ([MetricData](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource#MetricData))
      },
      "nodeCount": {
        object ([MetricData](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource#MetricData))
      },
      "processingUnitCount": {
        object ([MetricData](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource#MetricData))
      },
      "currentMemoryUsedBytes": {
        object ([MetricData](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource#MetricData))
      }
    }  
  
Fields  
---  
`p99CpuUtilization` |  `object (`[MetricData](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource#MetricData)`)` P99 CPU utilization observed for the resource. The value is a fraction between 0.0 and 1.0 (may momentarily exceed 1.0 in some cases).  
`p95CpuUtilization` |  `object (`[MetricData](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource#MetricData)`)` P95 CPU utilization observed for the resource. The value is a fraction between 0.0 and 1.0 (may momentarily exceed 1.0 in some cases).  
`currentStorageUsedBytes` |  `object (`[MetricData](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource#MetricData)`)` Current storage used by the resource in bytes.  
`peakStorageUtilization` |  `object (`[MetricData](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource#MetricData)`)` Peak storage utilization observed for the resource. The value is a fraction between 0.0 and 1.0 (may momentarily exceed 1.0 in some cases).  
`peakMemoryUtilization` |  `object (`[MetricData](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource#MetricData)`)` Peak memory utilization observed for the resource. The value is a fraction between 0.0 and 1.0 (may momentarily exceed 1.0 in some cases).  
`peakNumberConnections` |  `object (`[MetricData](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource#MetricData)`)` Peak number of connections observed for the resource. The value is a positive integer.  
`nodeCount` |  `object (`[MetricData](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource#MetricData)`)` Number of nodes in instance for spanner or bigtable.  
`processingUnitCount` |  `object (`[MetricData](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource#MetricData)`)` Number of processing units in spanner.  
`currentMemoryUsedBytes` |  `object (`[MetricData](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource#MetricData)`)` Current memory used by the resource in bytes.  
  
## MetricData

MetricData represents the metric data for a database resource.

JSON representation  
---  
      
    
    {
      "value": {
        object ([TypedValue](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource#TypedValue))
      },
      "observationTime": string
    }  
  
Fields  
---  
`value` |  `object (`[TypedValue](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource#TypedValue)`)` The value associated with the metric.  
`observationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time the metric was observed in the metric source service.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## TypedValue

TypedValue represents the value of the metric based on data type.

JSON representation  
---  
      
    
    {
    
      // Union field value can be only one of the following:
      "doubleValue": number,
      "int64Value": string
      // End of list of possible types for union field value.
    }  
  
Fields  
---  
Union field `value`. The data type of metric value would be chosen based on the metric type. `value` can be only one of the following:  
`doubleValue` |  `number` The value of the metric as double.  
`int64Value` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The value of the metric as int.  
  
## BackupDRConfig

BackupDRConfig to capture the backup and disaster recovery details of database resource.

JSON representation  
---  
      
    
    {
      "backupdrManaged": boolean
    }  
  
Fields  
---  
`backupdrManaged` |  `boolean` Indicates if the resource is managed by BackupDR.  
  
## MaintenanceInfo

MaintenanceInfo to capture the maintenance details of database resource.

JSON representation  
---  
      
    
    {
      "maintenanceSchedule": {
        object ([ResourceMaintenanceSchedule](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/ResourceMaintenanceSchedule))
      },
      "denyMaintenanceSchedules": [
        {
          object ([ResourceMaintenanceDenySchedule](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource#ResourceMaintenanceDenySchedule))
        }
      ],
      "maintenanceVersion": string
    }  
  
Fields  
---  
`maintenanceSchedule` |  `object (`[ResourceMaintenanceSchedule](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/ResourceMaintenanceSchedule)`)` Optional. Maintenance window for the database resource.  
`denyMaintenanceSchedules[]` |  `object (`[ResourceMaintenanceDenySchedule](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/DatabaseResource#ResourceMaintenanceDenySchedule)`)` Optional. List of Deny maintenance period for the database resource.  
`maintenanceVersion` |  `string` Output only. Current Maintenance version of the database resource. Example: "MYSQL_8_0_41.R20250531.01_15"  
  
## ResourceMaintenanceDenySchedule

Deny maintenance period for the database resource. It specifies the time range during which the maintenance cannot start. This is configured by the customer.

JSON representation  
---  
      
    
    {
      "startDate": {
        object ([Date](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Date))
      },
      "endDate": {
        object ([Date](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Date))
      },
      "time": {
        object ([TimeOfDay](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/TimeOfDay))
      }
    }  
  
Fields  
---  
`startDate` |  `object (`[Date](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Date)`)` Optional. The start date of the deny maintenance period.  
`endDate` |  `object (`[Date](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/Date)`)` Optional. Deny period end date.  
`time` |  `object (`[TimeOfDay](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/TimeOfDay)`)` Optional. Time in UTC when the deny period starts on startDate and ends on endDate.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-22 UTC."],[],[]] 
