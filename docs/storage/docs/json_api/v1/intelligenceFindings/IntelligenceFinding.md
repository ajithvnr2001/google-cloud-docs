---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceFindings/IntelligenceFinding/
title: IntelligenceFinding \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:52:22.649984+00:00
---

# IntelligenceFinding  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceFindings/IntelligenceFinding/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  IntelligenceFinding Stay organized with collections  Save and categorize content based on your preferences. 

The `IntelligenceFinding` resource represents a performance or usage optimization finding about a project or bucket. For a full list of findings, see [Findings reference catalog](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/findings-reference-catalog).

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "type": enum (FindingType),
      "category": enum (FindingCategory),
      "severity": enum (FindingSeverity),
      "createTime": string,
      "updateTime": string,
      "targetResource": string,
      "associatedResources": [
        string
      ],
      "observationPeriod": {
        object (TimeInterval)
      },
    
     // Union field intelligence_finding_details is one of the following:
      "coldlineAndArchivalStorageOperationsSpike": {
        object (ColdlineAndArchivalStorageOperationsSpike)
      },
      "throttledRequestsSpike": {
        object (ThrottledRequestSpike)
      },
      "crossRegionEgressSpike": {
        object (CrossRegionEgressSpike)
      },
      "storageGrowthAboveTrend": {
        object (StorageGrowthAboveTrend)
      }
      // End of list of possible types for union field intelligence_finding_details.
    }  
  
Fields  
---  
`name` |  `string`The resource name of `IntelligenceFinding`.   
Format: `projects/{project}/locations/{location}/intelligenceFindings/{intelligence_finding}`  
`description` |  `string` Output only. A short description of the finding.  
`type` |  `enum (`FindingType`)` Output only. The type of this finding.  
`category` |  `enum (`FindingCategory`)` Output only. The category of this finding.  
`severity` |  `enum (`FindingSeverity`)` Output only. The severity of the finding.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the finding was created.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the finding was last updated.  
`targetResource` |  `string` Output only. The fully qualified resource name of the resource that this `IntelligenceFinding` applies to. For example, `storage.googleapis.com/projects/_/buckets/b1`, `cloudresourcemanager.googleapis.com/projects/p1`  
`associatedResources[]` |  `string` Output only. Google Cloud resource names that are relevant to the `IntelligenceFinding`. This list also includes the `targetResource`. For example, `storage.googleapis.com/projects/_/buckets/b1`, `cloudresourcemanager.googleapis.com/projects/p1`  
`observationPeriod` |  `object (`TimeInterval`)` Output only. The time interval from which the underlying data generated this `IntelligenceFinding` was observed.  
Union field `intelligence_finding_details`. The specific details of the `IntelligenceFinding`. This field can be one of the following:  
`coldlineAndArchivalStorageOperationsSpike` |  `object (`ColdlineAndArchivalStorageOperationsSpike`)` A finding about a spike in Class A or Class B operations on Coldline or Archive Cloud Storage objects.  
`throttledRequestsSpike` |  `object (`ThrottledRequestSpike`)` A finding about a spike in throttled requests (429 errors) within a project.  
`crossRegionEgressSpike` |  `object (`CrossRegionEgressSpike`)` A finding about a spike in cross-region egress from Cloud Storage.  
`storageGrowthAboveTrend` |  `object (`StorageGrowthAboveTrend`)` A finding about storage growth above the expected trend.  
  
## FindingType

Lists the finding types.

Enums  
---  
`FINDING_TYPE_UNSPECIFIED` | The finding type is not specified.  
`FINDING_TYPE_COLDLINE_AND_ARCHIVAL_STORAGE_OPERATIONS_SPIKE` | Indicates a spike in Class A or Class B operations on Coldline or Archive Cloud Storage objects.  
`FINDING_TYPE_THROTTLED_REQUEST_SPIKE` | Indicates a spike in throttled requests (429 errors) within a project.  
`FINDING_TYPE_CROSS_REGION_EGRESS_SPIKE` | Indicates a spike in cross-region egress in Cloud Storage.  
`FINDING_TYPE_STORAGE_GROWTH_ABOVE_TREND` | Indicates that storage growth is above the expected trend.  
  
## FindingCategory

Lists the finding categories.

Enums  
---  
`FINDING_CATEGORY_UNSPECIFIED` | The category is not specified.  
`FINDING_CATEGORY_DATA_MANAGEMENT` | Data Management.  
`FINDING_CATEGORY_PERFORMANCE` | Performance.  
  
## FindingSeverity

Describes the severity of the `IntelligenceFinding`.

Enums  
---  
`FINDING_SEVERITY_UNSPECIFIED` | The severity is not specified.  
`FINDING_SEVERITY_CRITICAL` | Critical.  
  
## ColdlineAndArchivalStorageOperationsSpike

Describes a spike in Class A or Class B operations on Coldline or Archive Cloud Storage objects. This finding corresponds to the `COLD_AND_ARCHIVAL_STORAGE_OPERATIONS_SPIKE` finding type.

JSON representation  
---  
      
    
    {
      "percentageIncrease": number,
      "totalOperationsCount": string,
      "topBuckets": [
        {
          object (BucketContribution)
        }
      ]
    }  
  
Fields  
---  
`percentageIncrease` |  `number` Output only. The percentage increase in operations across the project compared to the historical baseline.  
`totalOperationsCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The total count of operations across the project.  
`topBuckets[]` |  `object (`BucketContribution`)` Output only. A list of the top buckets driving the increase in operations.  
  
## BucketContribution

Describes the operation spike details for a bucket.

JSON representation  
---  
      
    
    {
      "bucket": string,
      "percentageIncrease": number,
      "totalOperationsCount": string,
    
      // Union field details can be only one of the following:
      "contribution": {
        object (Contribution)
      },
      "error": {
        object ([Status](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/Status))
      }
      // End of list of possible types for union field details.
    }  
  
Fields  
---  
`bucket` |  `string` Output only. The name of the bucket.  
`percentageIncrease` |  `number` Output only. The percentage increase in operations for the bucket.  
`totalOperationsCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The total count of operations for the bucket.  
Union field `details`. The details of the bucket's contribution towards the `IntelligenceFinding`. This field can be one of the following:  
`contribution` |  `object (`Contribution`)` The details about the contribution of the bucket.  
`error` |  `object (`[Status](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/Status)`)` The error when accessing details about the bucket's contribution.  
  
## Contribution

Describes the bucket's contribution to the `IntelligenceFinding`.

JSON representation  
---  
      
    
    {
      "topPrefixes": [
        {
          object (PrefixContribution)
        }
      ]
    }  
  
Fields  
---  
`topPrefixes[]` |  `object (`PrefixContribution`)` Output only. The top object prefixes driving the increase in operations.  
  
## PrefixContribution

Describes the operation spike details for an object prefix.

JSON representation  
---  
      
    
    {
      "prefix": string,
      "percentageIncrease": number,
      "totalOperationsCount": string
    }  
  
Fields  
---  
`prefix` |  `string` Output only. The object prefix. For example, `a/b/c` or `a/b/d`.  
`percentageIncrease` |  `number` Output only. The percentage increase in operations for the object prefix.  
`totalOperationsCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The total count of operations for the object prefix.  
  
## ThrottledRequestSpike

Represents a spike in throttled requests (429 errors) within a project. This finding corresponds to the `THROTTLED_REQUEST_SPIKE` finding type.

JSON representation  
---  
      
    
    {
      "throttledRequests": string,
      "percentageIncrease": number,
      "topBuckets": [
        {
          object (BucketContribution)
        }
      ]
    }  
  
Fields  
---  
`throttledRequests` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The count of throttled requests across the project.  
`percentageIncrease` |  `number` Output only. The percentage increase in throttled requests across the project.  
`topBuckets[]` |  `object (`BucketContribution`)` Output only. A list of top buckets driving the increase in throttled requests.  
  
## BucketContribution

Represents the throttled request details for a bucket.

JSON representation  
---  
      
    
    {
      "bucket": string,
      "throttledRequests": string,
      "percentageIncrease": number,
    
      // Union field details can be only one of the following:
      "contribution": {
        object (Contribution)
      },
      "error": {
        object ([Status](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/Status))
      }
      // End of list of possible types for union field details.
    }  
  
Fields  
---  
`bucket` |  `string` Output only. The name of the bucket.  
`throttledRequests` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The count of throttled requests for the bucket.  
`percentageIncrease` |  `number` Output only. The percentage increase in throttled requests for the bucket.  
Union field `details`. The details of the bucket's contribution towards the `IntelligenceFinding`. This field can be one of the following:  
`contribution` |  `object (`Contribution`)` The details about the contribution of the bucket.  
`error` |  `object (`[Status](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/Status)`)` The error related to accessing the details about the contribution of the bucket.  
  
## Contribution

Represents the bucket's contribution to the `IntelligenceFinding`.

JSON representation  
---  
      
    
    {
      "topPrefixes": [
        {
          object (PrefixContribution)
        }
      ]
    }  
  
Fields  
---  
`topPrefixes[]` |  `object (`PrefixContribution`)` Output only. A list of top object prefixes driving the increase in throttled requests.  
  
## PrefixContribution

Represents throttled request details for an object prefix.

JSON representation  
---  
      
    
    {
      "prefix": string,
      "throttledRequests": string,
      "percentageIncrease": number
    }  
  
Fields  
---  
`prefix` |  `string` Output only. The object prefix. For example, `a/b/c` or `a/b/d`.  
`throttledRequests` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The count of throttled requests for the object prefix.  
`percentageIncrease` |  `number` Output only. The percentage increase in throttled requests for the object prefix.  
  
## CrossRegionEgressSpike

Represents a spike in cross-region egress from Cloud Storage. This finding corresponds to the `CROSS_REGION_EGRESS_SPIKE` finding type.

JSON representation  
---  
      
    
    {
      "totalEgressBytes": string,
      "percentageIncrease": number,
      "topBuckets": [
        {
          object (BucketContribution)
        }
      ]
    }  
  
Fields  
---  
`totalEgressBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The total cross-region egress volume in bytes across the project.  
`percentageIncrease` |  `number` Output only. The percentage increase in cross-region egress across the project.  
`topBuckets[]` |  `object (`BucketContribution`)` Output only. A list of top buckets driving the increase in cross-region egress.  
  
## BucketContribution

Represents the cross-region egress spike details for a bucket.

JSON representation  
---  
      
    
    {
      "bucket": string,
      "totalEgressBytes": string,
      "percentageIncrease": number,
    
      // Union field details can be only one of the following:
      "contribution": {
        object (Contribution)
      },
      "error": {
        object ([Status](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/Status))
      }
      // End of list of possible types for union field details.
    }  
  
Fields  
---  
`bucket` |  `string` Output only. The name of the bucket.  
`totalEgressBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The total cross-region egress volume in bytes for the bucket.  
`percentageIncrease` |  `number` Output only. The percentage increase in cross-region egress for the bucket.  
Union field `details`. The details of the bucket's contribution towards the `IntelligenceFinding`. This field can be one of the following:  
`contribution` |  `object (`Contribution`)` The details about the contribution of the bucket.  
`error` |  `object (`[Status](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/Status)`)` The error related to accessing the details about the contribution of the bucket.  
  
## Contribution

Represents the bucket's contribution to the `IntelligenceFinding`.

JSON representation  
---  
      
    
    {
      "topPrefixes": [
        {
          object (PrefixContribution)
        }
      ]
    }  
  
Fields  
---  
`topPrefixes[]` |  `object (`PrefixContribution`)` Output only. A list of top object prefixes driving the increase in cross-region egress.  
  
## PrefixContribution

Represents cross-region egress spike details for an object prefix.

JSON representation  
---  
      
    
    {
      "prefix": string,
      "totalEgressBytes": string,
      "percentageIncrease": number
    }  
  
Fields  
---  
`prefix` |  `string` Output only. The object prefix. For example, `a/b/c` or `a/b/d`.  
`totalEgressBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The total cross-region egress volume in bytes from the object prefix.  
`percentageIncrease` |  `number` Output only. The percentage increase in cross-region egress for the object prefix.  
  
## StorageGrowthAboveTrend

Represents a finding about storage growth above the expected trend. This finding corresponds to the `STORAGE_GROWTH_ABOVE_TREND` finding type.

JSON representation  
---  
      
    
    {
      "totalStorageGrowthBytes": string,
      "percentageIncrease": number,
      "topBuckets": [
        {
          object (BucketContribution)
        }
      ]
    }  
  
Fields  
---  
`totalStorageGrowthBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The total storage growth in bytes.  
`percentageIncrease` |  `number` Output only. The percentage increase in storage growth.  
`topBuckets[]` |  `object (`BucketContribution`)` Output only. A list of top buckets driving the increase in storage growth.  
  
## BucketContribution

Represents the storage growth details for a bucket.

JSON representation  
---  
      
    
    {
      "bucket": string,
      "totalStorageGrowthBytes": string,
      "percentageIncrease": number,
    
      // Union field details can be only one of the following:
      "error": {
        object ([Status](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/Status))
      }
      // End of list of possible types for union field details.
    }  
  
Fields  
---  
`bucket` |  `string` Output only. The name of the bucket.  
`totalStorageGrowthBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The total storage growth in bytes for the bucket.  
`percentageIncrease` |  `number` Output only. The percentage increase in storage growth for the bucket.  
Union field `details`. The details of the bucket's contribution towards the `IntelligenceFinding`. This field can be one of the following:  
`error` |  `object (`[Status](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/Status)`)` The error related to accessing the details about the contribution of the bucket.  
  
## TimeInterval

Represents a time interval with an inclusive `Timestamp` start time and an exclusive `Timestamp` end time.

The start time must precede or equal the end time. If the start time equals the end time, the interval is empty and matches no time. If both `startTime` and `endTime` are unspecified, the interval matches any time.

JSON representation  
---  
      
    
    {
      "startTime": string,
      "endTime": string
    }  
  
Fields  
---  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Inclusive start time of the interval. If specified, a matching timestamp must be at or after the start time.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Exclusive end time of the interval. If specified, a matching timestamp must be before the end time.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-14 UTC."],[],[]] 
