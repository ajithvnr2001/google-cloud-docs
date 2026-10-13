---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentPolicyActionLog/
title: ContentPolicyActionLog \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:43.208749+00:00
---

# ContentPolicyActionLog  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentPolicyActionLog/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  ContentPolicyActionLog Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * InfoTypeMatch
    * JSON representation
  * ScannedContent
    * JSON representation



Message used when saving content policy logs to external storage (such as BigQuery or Cloud Storage).

JSON representation  
---  
      
    
    {
      "contentPolicy": string,
      "logTime": string,
      "dataSourceType": {
        object ([DataSourceType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataSourceType))
      },
      "containerId": string,
      "documentId": string,
      "matchingInfoTypes": [
        {
          object ([InfoTypeMatch](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentPolicyActionLog#InfoTypeMatch))
        }
      ],
      "correlationId": string,
      "scannedContent": {
        object ([ScannedContent](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentPolicyActionLog#ScannedContent))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "returnedVerdict": enum ([ContentPolicyVerdict](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies#ContentPolicyVerdict))
      // End of mutually exclusive fields.
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "policyRule": {
        object ([PolicyRule](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies#PolicyRule))
      },
      "fallbackAction": enum ([FallbackActionType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/FallbackActionType))
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`contentPolicy` |  `string` The resource name of the content policy that produced this log.  
`logTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The timestamp of when the action was taken.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`dataSourceType` |  `object (`[DataSourceType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataSourceType)`)` The client-supplied source of the data that is being processed. This allows for aggregating logs by source, for example, "geminienterprise/slack".  
`containerId` |  `string` The client-supplied identifier for a container from which content was scanned, also to aid in aggregation, for example, a specific folder or chat room.  
`documentId` |  `string` The client-supplied identifier for the document that was scanned. This allows tracking down the exact source that produced this log, for example, a message id.  
`matchingInfoTypes[]` |  `object (`[InfoTypeMatch](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentPolicyActionLog#InfoTypeMatch)`)` Unordered set of matching infoTypes found in the content.  
`correlationId` |  `string` Optional. A correlation ID to associate this log with other logs or systems.  
`scannedContent` |  `object (`[ScannedContent](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ContentPolicyActionLog#ScannedContent)`)` Optional. Details about the scanned content.  
The resulting action from evaluating the content policy. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`returnedVerdict` |  `enum (`[ContentPolicyVerdict](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies#ContentPolicyVerdict)`)` The verdict that was returned.  
End of mutually exclusive fields.  
Trigger for the action. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`policyRule` |  `object (`[PolicyRule](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies#PolicyRule)`)` A user-defined rule in the content policy was matched.  
`fallbackAction` |  `enum (`[FallbackActionType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/FallbackActionType)`)` A fallback action was taken.  
End of mutually exclusive fields.  
  
## InfoTypeMatch

Information about a matching infoType found in the content.

JSON representation  
---  
      
    
    {
      "infoTypeName": string
    }  
  
Fields  
---  
`infoTypeName` |  `string`  
  
## ScannedContent

Details about the scanned content.

JSON representation  
---  
      
    
    {
      "bytesType": enum ([BytesType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ByteContentItem#BytesType)),
      "fileSizeBytes": string
    }  
  
Fields  
---  
`bytesType` |  `enum (`[BytesType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ByteContentItem#BytesType)`)` Optional. The type of the content that was scanned.  
`fileSizeBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. The size of the content in bytes that was scanned.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
