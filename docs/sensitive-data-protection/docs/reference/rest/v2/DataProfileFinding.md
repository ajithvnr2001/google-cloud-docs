---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileFinding/
title: DataProfileFinding \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:44.988816+00:00
---

# DataProfileFinding  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileFinding/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  DataProfileFinding Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * DataProfileFindingLocation
    * JSON representation
  * DataProfileFindingRecordLocation
    * JSON representation



Details about a piece of potentially sensitive information that was detected when the data resource was profiled.

JSON representation  
---  
      
    
    {
      "quote": string,
      "infotype": {
        object ([InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType))
      },
      "quoteInfo": {
        object ([QuoteInfo](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#QuoteInfo))
      },
      "dataProfileResourceName": string,
      "findingId": string,
      "timestamp": string,
      "location": {
        object ([DataProfileFindingLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileFinding#DataProfileFindingLocation))
      },
      "resourceVisibility": enum ([ResourceVisibility](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ResourceVisibility)),
      "fullResourceName": string,
      "dataSourceType": {
        object ([DataSourceType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataSourceType))
      }
    }  
  
Fields  
---  
`quote` |  `string` The content that was found. Even if the content is not textual, it may be converted to a textual representation here. If the finding exceeds 4096 bytes in length, the quote may be omitted.  
`infotype` |  `object (`[InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType)`)` The [type of content](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference) that might have been found.  
`quoteInfo` |  `object (`[QuoteInfo](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectResult#QuoteInfo)`)` Contains data parsed from quotes. Currently supported infoTypes: DATE, DATE_OF_BIRTH, and TIME.  
`dataProfileResourceName` |  `string` Resource name of the data profile associated with the finding.  
`findingId` |  `string` A unique identifier for the finding.  
`timestamp` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp when the finding was detected.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`location` |  `object (`[DataProfileFindingLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileFinding#DataProfileFindingLocation)`)` Where the content was found.  
`resourceVisibility` |  `enum (`[ResourceVisibility](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ResourceVisibility)`)` How broadly a resource has been shared.  
`fullResourceName` |  `string` The [full resource name](https://cloud.google.com/apis/design/resource_names#fullResourceName) of the resource profiled for this finding.  
`dataSourceType` |  `object (`[DataSourceType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataSourceType)`)` The type of the resource that was profiled.  
  
## DataProfileFindingLocation

Location of a data profile finding within a resource.

JSON representation  
---  
      
    
    {
      "containerName": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "dataProfileFindingRecordLocation": {
        object ([DataProfileFindingRecordLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileFinding#DataProfileFindingRecordLocation))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`containerName` |  `string` Name of the container where the finding is located. The top-level name is the source file name or table name. Names of some common storage containers are formatted as follows:

  * BigQuery tables: `{projectId}:{datasetId}.{tableId}`
  * Cloud Storage files: `gs://{bucket}/{path}`

  
Additional location details that may be provided for some types of profiles. At this time, only findings for table data profiles include such details. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`dataProfileFindingRecordLocation` |  `object (`[DataProfileFindingRecordLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileFinding#DataProfileFindingRecordLocation)`)` Location of a finding within a resource that produces a table data profile.  
End of mutually exclusive fields.  
  
## DataProfileFindingRecordLocation

Location of a finding within a resource that produces a table data profile.

JSON representation  
---  
      
    
    {
      "field": {
        object ([FieldId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/FieldId))
      }
    }  
  
Fields  
---  
`field` |  `object (`[FieldId](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/FieldId)`)` Field ID of the column containing the finding.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-05 UTC."],[],[]] 
