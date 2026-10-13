---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarSettings/legacyGetVisualSummaryRecords/
title: Method: legacySoarSettings.legacyGetVisualSummaryRecords \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:57:21.433683+00:00
---

# Method: legacySoarSettings.legacyGetVisualSummaryRecords  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarSettings/legacyGetVisualSummaryRecords/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: legacySoarSettings.legacyGetVisualSummaryRecords Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * LegacyVisualSummaryFieldMetadataRecord
    * JSON representation
  * LegacyVisualSummarySectionType



**Full name** : projects.locations.instances.legacySoarSettings.legacyGetVisualSummaryRecords

Returns all configured visual summary field metadata records. This defines the set of information displayed in entity and event summaries across the platform.

### HTTP request

`GET https://{endpoint}/v1alpha/{instance}/legacySoarSettings:legacyGetVisualSummaryRecords`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`instance` |  `string` Required. The instance to get the visual summary records for. Format: projects/{project}/locations/{location}/instances/{instance}  
  
### Request body

The request body must be empty.

### Response body

Response message for LegacySoarSettingService.LegacyGetVisualSummaryRecords.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "payload": [
        {
          object ([LegacyVisualSummaryFieldMetadataRecord](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarSettings/legacyGetVisualSummaryRecords#LegacyVisualSummaryFieldMetadataRecord))
        }
      ]
    }  
  
Fields  
---  
`payload[]` |  `object (`[LegacyVisualSummaryFieldMetadataRecord](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarSettings/legacyGetVisualSummaryRecords#LegacyVisualSummaryFieldMetadataRecord)`)` Optional. The visual summary records.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `instance` resource:

  * `chronicle.legacySoarSettings.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## LegacyVisualSummaryFieldMetadataRecord

Response message for LegacySoarSettingService.LegacyGetVisualSummaryRecords.

JSON representation  
---  
      
    
    {
      "fieldName": string,
      "sectionType": enum ([LegacyVisualSummarySectionType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarSettings/legacyGetVisualSummaryRecords#LegacyVisualSummarySectionType)),
      "id": integer,
      "creationTimeUnixTimeInMs": string,
      "modificationTimeUnixTimeInMs": string,
      "maxValue": integer,
      "isDescending": boolean,
      "isTypeBool": boolean
    }  
  
Fields  
---  
`fieldName` |  `string` Output only. The field name.  
`sectionType` |  `enum (`[LegacyVisualSummarySectionType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.legacySoarSettings/legacyGetVisualSummaryRecords#LegacyVisualSummarySectionType)`)` Output only. The section type.  
`id` |  `integer` Optional. The visual summary records.  
`creationTimeUnixTimeInMs` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. The creation time.  
`modificationTimeUnixTimeInMs` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. The modification time.  
`maxValue` |  `integer` Output only. The max value.  
`isDescending` |  `boolean` Output only. Whether is descending.  
`isTypeBool` |  `boolean` Output only. Whether is type bool.  
  
## LegacyVisualSummarySectionType

Visual summary section type.

Enums  
---  
`ENTITIES` | Entities.  
`RELATIONS` | Events.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
