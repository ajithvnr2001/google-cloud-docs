---
url: https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets
title: REST Resource: projects.locations.assets \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:49:03.521091+00:00
---

# REST Resource: projects.locations.assets  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Reference ](https://docs.cloud.google.com/migration-center/docs/api)



Send feedback 

#  REST Resource: projects.locations.assets Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Asset
    * JSON representation
  * InsightList
    * JSON representation
  * Insight
    * JSON representation
  * MigrationInsight
    * JSON representation
  * FitDescriptor
    * JSON representation
  * FitLevel
  * ComputeEngineMigrationTarget
    * JSON representation
  * ComputeEngineShapeDescriptor
    * JSON representation
  * ComputeStorageDescriptor
    * JSON representation
  * GenericInsight
    * JSON representation
  * AssetPerformanceData
    * JSON representation
  * DailyResourceUsageAggregation
    * JSON representation
  * CPU
    * JSON representation
  * Stats
    * JSON representation
  * Memory
    * JSON representation
  * Network
    * JSON representation
  * Disk
    * JSON representation
  * Methods



## Resource: Asset

An asset represents a resource in your environment. Asset types include virtual machines and databases.

JSON representation  
---  
      
    
    {
      "name": string,
      "title": string,
      "createTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      },
      "attributes": {
        string: string,
        ...
      },
      "insightList": {
        object ([InsightList](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#InsightList))
      },
      "performanceData": {
        object ([AssetPerformanceData](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#AssetPerformanceData))
      },
      "sources": [
        string
      ],
      "assignedGroups": [
        string
      ],
    
      // Union field AssetDetails can be only one of the following:
      "machineDetails": {
        object ([MachineDetails](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/MachineDetails))
      },
      "databaseDeploymentDetails": {
        object ([DatabaseDeploymentDetails](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/DatabaseDeploymentDetails))
      },
      "databaseDetails": {
        object ([DatabaseDetails](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/DatabaseDetails))
      }
      // End of list of possible types for union field AssetDetails.
    }  
  
Fields  
---  
`name` |  `string` Output only. The full name of the asset.  
`title` |  `string` Output only. Server generated human readable name of the asset.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the asset was created.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the asset was last updated.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`labels` |  `map (key: string, value: string)` Labels as key value pairs.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`attributes` |  `map (key: string, value: string)` Generic asset attributes.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`insightList` |  `object (`[InsightList](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#InsightList)`)` Output only. The list of insights associated with the asset.  
`performanceData` |  `object (`[AssetPerformanceData](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#AssetPerformanceData)`)` Output only. Performance data for the asset.  
`sources[]` |  `string` Output only. The list of sources contributing to the asset.  
`assignedGroups[]` |  `string` Output only. The list of groups that the asset is assigned to.  
Union field `AssetDetails`. The internal information of an asset. Only one field can be specified with different attributes based on the type of the asset. `AssetDetails` can be only one of the following:  
`machineDetails` |  `object (`[MachineDetails](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/MachineDetails)`)` Output only. Asset information specific for virtual and physical machines.  
`databaseDeploymentDetails` |  `object (`[DatabaseDeploymentDetails](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/DatabaseDeploymentDetails)`)` Output only. Asset information specific for database deployments.  
`databaseDetails` |  `object (`[DatabaseDetails](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/DatabaseDetails)`)` Output only. Asset information specific for logical databases.  
  
## InsightList

Message containing insights list.

JSON representation  
---  
      
    
    {
      "insights": [
        {
          object ([Insight](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#Insight))
        }
      ],
      "updateTime": string
    }  
  
Fields  
---  
`insights[]` |  `object (`[Insight](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#Insight)`)` Output only. Insights of the list.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Update timestamp.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
  
## Insight

An insight about an asset.

JSON representation  
---  
      
    
    {
    
      // Union field insight can be only one of the following:
      "migrationInsight": {
        object ([MigrationInsight](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#MigrationInsight))
      },
      "genericInsight": {
        object ([GenericInsight](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#GenericInsight))
      }
      // End of list of possible types for union field insight.
    }  
  
Fields  
---  
Union field `insight`.`insight` can be only one of the following:  
`migrationInsight` |  `object (`[MigrationInsight](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#MigrationInsight)`)` Output only. An insight about potential migrations for an asset.  
`genericInsight` |  `object (`[GenericInsight](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#GenericInsight)`)` Output only. A generic insight about an asset.  
  
## MigrationInsight

An insight about potential migrations for an asset.

JSON representation  
---  
      
    
    {
      "fit": {
        object ([FitDescriptor](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#FitDescriptor))
      },
    
      // Union field migration_target can be only one of the following:
      "computeEngineTarget": {
        object ([ComputeEngineMigrationTarget](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#ComputeEngineMigrationTarget))
      }
      // End of list of possible types for union field migration_target.
    }  
  
Fields  
---  
`fit` |  `object (`[FitDescriptor](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#FitDescriptor)`)` Output only. Description of how well the asset this insight is associated with fits the proposed migration.  
Union field `migration_target`. A target for the migration. `migration_target` can be only one of the following:  
`computeEngineTarget` |  `object (`[ComputeEngineMigrationTarget](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#ComputeEngineMigrationTarget)`)` Output only. A Google Compute Engine target.  
  
## FitDescriptor

Describes the fit level of an asset for migration to a specific target.

JSON representation  
---  
      
    
    {
      "fitLevel": enum ([FitLevel](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#FitLevel))
    }  
  
Fields  
---  
`fitLevel` |  `enum (`[FitLevel](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#FitLevel)`)` Output only. Fit level.  
  
## FitLevel

Fit level.

Enums  
---  
`FIT_LEVEL_UNSPECIFIED` | Not enough information.  
`FIT` | Fit.  
`NO_FIT` | No Fit.  
`REQUIRES_EFFORT` | Fit with effort.  
  
## ComputeEngineMigrationTarget

Compute engine migration target.

JSON representation  
---  
      
    
    {
      "shape": {
        object ([ComputeEngineShapeDescriptor](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#ComputeEngineShapeDescriptor))
      }
    }  
  
Fields  
---  
`shape` |  `object (`[ComputeEngineShapeDescriptor](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#ComputeEngineShapeDescriptor)`)` Description of the suggested shape for the migration target.  
  
## ComputeEngineShapeDescriptor

Compute Engine target shape descriptor.

JSON representation  
---  
      
    
    {
      "memoryMb": integer,
      "physicalCoreCount": integer,
      "logicalCoreCount": integer,
      "series": string,
      "machineType": string,
      "storage": [
        {
          object ([ComputeStorageDescriptor](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#ComputeStorageDescriptor))
        }
      ]
    }  
  
Fields  
---  
`memoryMb` |  `integer` Memory in mebibytes.  
`physicalCoreCount` |  `integer` Number of physical cores.  
`logicalCoreCount` |  `integer` Output only. Number of logical cores.  
`series` |  `string` Output only. Compute Engine machine series.  
`machineType` |  `string` Output only. Compute Engine machine type.  
`storage[]` |  `object (`[ComputeStorageDescriptor](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#ComputeStorageDescriptor)`)` Output only. Compute Engine storage. Never empty.  
  
## ComputeStorageDescriptor

Compute Engine storage option descriptor.

JSON representation  
---  
      
    
    {
      "type": enum ([PersistentDiskType](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/PersistentDiskType)),
      "sizeGb": integer
    }  
  
Fields  
---  
`type` |  `enum (`[PersistentDiskType](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/PersistentDiskType)`)` Output only. Disk type backing the storage.  
`sizeGb` |  `integer` Output only. Disk size in GiB.  
  
## GenericInsight

A generic insight about an asset.

JSON representation  
---  
      
    
    {
      "messageId": string,
      "defaultMessage": string,
      "additionalInformation": [
        string
      ]
    }  
  
Fields  
---  
`messageId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Represents a globally unique message id for this insight, can be used for localization purposes, in case message_code is not yet known by the client use defaultMessage instead.  
`defaultMessage` |  `string` Output only. In case message_code is not yet known by the client defaultMessage will be the message to be used instead.  
`additionalInformation[]` |  `string` Output only. Additional information about the insight, each entry can be a logical entry and must make sense if it is displayed with line breaks between each entry. Text can contain md style links.  
  
## AssetPerformanceData

Performance data for an asset.

JSON representation  
---  
      
    
    {
      "dailyResourceUsageAggregations": [
        {
          object ([DailyResourceUsageAggregation](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#DailyResourceUsageAggregation))
        }
      ]
    }  
  
Fields  
---  
`dailyResourceUsageAggregations[]` |  `object (`[DailyResourceUsageAggregation](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#DailyResourceUsageAggregation)`)` Daily resource usage aggregations. Contains all of the data available for an asset, up to the last 420 days. Aggregations are sorted from oldest to most recent.  
  
## DailyResourceUsageAggregation

Usage data aggregation for a single day.

JSON representation  
---  
      
    
    {
      "date": {
        object ([Date](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/Date))
      },
      "cpu": {
        object ([CPU](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#CPU))
      },
      "memory": {
        object ([Memory](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#Memory))
      },
      "network": {
        object ([Network](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#Network))
      },
      "disk": {
        object ([Disk](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#Disk))
      }
    }  
  
Fields  
---  
`date` |  `object (`[Date](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/Date)`)` Aggregation date. Day boundaries are at midnight UTC.  
`cpu` |  `object (`[CPU](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#CPU)`)` CPU usage.  
`memory` |  `object (`[Memory](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#Memory)`)` Memory usage.  
`network` |  `object (`[Network](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#Network)`)` Network usage.  
`disk` |  `object (`[Disk](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#Disk)`)` Disk usage.  
  
## CPU

Statistical aggregation of CPU usage.

JSON representation  
---  
      
    
    {
      "utilizationPercentage": {
        object ([Stats](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#Stats))
      }
    }  
  
Fields  
---  
`utilizationPercentage` |  `object (`[Stats](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#Stats)`)` CPU utilization percentage.  
  
## Stats

Statistical aggregation of samples for a single resource usage.

JSON representation  
---  
      
    
    {
      "average": number,
      "median": number,
      "ninteyFifthPercentile": number,
      "peak": number
    }  
  
Fields  
---  
`average` |  `number` Average usage value.  
`median` |  `number` Median usage value.  
`ninteyFifthPercentile` |  `number` 95th percentile usage value.  
`peak` |  `number` Peak usage value.  
  
## Memory

Statistical aggregation of memory usage.

JSON representation  
---  
      
    
    {
      "utilizationPercentage": {
        object ([Stats](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#Stats))
      }
    }  
  
Fields  
---  
`utilizationPercentage` |  `object (`[Stats](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#Stats)`)` Memory utilization percentage.  
  
## Network

Statistical aggregation of network usage.

JSON representation  
---  
      
    
    {
      "ingressBps": {
        object ([Stats](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#Stats))
      },
      "egressBps": {
        object ([Stats](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#Stats))
      }
    }  
  
Fields  
---  
`ingressBps` |  `object (`[Stats](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#Stats)`)` Network ingress in B/s.  
`egressBps` |  `object (`[Stats](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#Stats)`)` Network egress in B/s.  
  
## Disk

Statistical aggregation of disk usage.

JSON representation  
---  
      
    
    {
      "iops": {
        object ([Stats](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#Stats))
      },
      "readIops": {
        object ([Stats](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#Stats))
      },
      "writeIops": {
        object ([Stats](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#Stats))
      }
    }  
  
Fields  
---  
`iops` |  `object (`[Stats](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#Stats)`)` Optional. Disk I/O operations per second.  
`readIops` |  `object (`[Stats](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#Stats)`)` Optional. Disk read I/O operations per second.  
`writeIops` |  `object (`[Stats](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets#Stats)`)` Optional. Disk write I/O operations per second.  
  
## Methods  
  
---  
  
### `[aggregateValues](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets/aggregateValues)`

|  Aggregates the requested fields based on provided function.  
  
### `[batchDelete](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets/batchDelete)`

|  Deletes list of Assets.  
  
### `[batchUpdate](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets/batchUpdate)`

|  Updates the parameters of a list of assets.  
  
### `[delete](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets/delete)`

|  Deletes an asset.  
  
### `[get](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets/get)`

|  Gets the details of an asset.  
  
### `[list](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets/list)`

|  Lists all the assets in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets/patch)`

|  Updates the parameters of an asset.  
  
### `[reportAssetFrames](https://docs.cloud.google.com/migration-center/docs/reference/rest/v1/projects.locations.assets/reportAssetFrames)`

|  Reports a set of frames.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-17 UTC."],[],[]] 
