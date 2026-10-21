---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceFindings/FindingSummary/
title: FindingSummary \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:52:22.251466+00:00
---

# FindingSummary  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceFindings/FindingSummary/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  FindingSummary Stay organized with collections  Save and categorize content based on your preferences. 

A summary of findings for an organization, a folder, or a project.

JSON representation  
---  
      
    
    {
      "type": enum ([FindingType](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceFindings/IntelligenceFinding#FindingType)),
      "category": enum ([FindingCategory](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceFindings/IntelligenceFinding#FindingCategory)),
      "targetResource": string,
      "createTime": string,
      "updateTime": string,
      "severity": enum ([FindingSeverity](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceFindings/IntelligenceFinding#FindingSeverity)),
      "summaryDetails": [
        {
          object (SummaryDetails)
        }
      ]
    }  
  
Fields  
---  
`type` |  `enum (`[FindingType](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceFindings/IntelligenceFinding#FindingType)`)` Output only. The type of the finding.  
`category` |  `enum (`[FindingCategory](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceFindings/IntelligenceFinding#FindingCategory)`)` Output only. The category of finding.  
`targetResource` |  `string` Output only. The fully qualified Cloud resource name for which this summary was generated.  
Example: `//cloudresourcemanager.googleapis.com/projects/p1`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The creation time of the earliest finding that this summary is based on.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time of the most recent update among all the findings that this summary is based on.  
`severity` |  `enum (`[FindingSeverity](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceFindings/IntelligenceFinding#FindingSeverity)`)` Output only. Severity of the finding.  
`summaryDetails[]` |  `object (`SummaryDetails`)` Output only. The `SummaryDetails` resources.  
  
## SummaryDetails

Details about the `FindingSummary` resource.

JSON representation  
---  
      
    
    {
      // Union field magnitude can be only one of the following:
      "count": string,
      "percentage": number
      // End of list of possible types for union field magnitude.
    
      "resourceType": enum (ResourceType),
      "description": string
    }  
  
Fields  
---  
Union field `magnitude`. The value of the summary, which can be one of the following:  
`count` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The count of impacted resources.  
`percentage` |  `number` The percentage of impacted resources.  
`resourceType` |  `enum (`ResourceType`)` Output only. The type of Cloud resource this summary detail applies to.  
`description` |  `string` Output only. A short description about the `FindingSummary`.  
  
## ResourceType

The resource types.

Enums  
---  
`RESOURCE_TYPE_UNSPECIFIED` | Resource type is unspecified.  
`PROJECT` | Resource type is project.  
`BUCKET` | Resource type is bucket.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-09 UTC."],[],[]] 
