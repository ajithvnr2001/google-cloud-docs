---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/objects/viewFullContext/
title: Objects: viewFullContext \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:41:30.481304+00:00
---

# Objects: viewFullContext  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/objects/viewFullContext/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Objects: viewFullContext Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Retrieves a single object context, including its extended data, by key.

## Required permissions

The authenticated user must have the `storage.objects.viewFullContext` IAM permission to use this method.

## Request

### HTTP request
    
    
    GET https://storage.googleapis.com/storage/v1/b/bucket/o/object/viewFullContext

In addition to [standard query parameters](https://docs.cloud.google.com/storage/docs/json_api/v1/parameters#query), the following query parameters apply to this method.

### Parameters

Parameter name | Value | Description  
---|---|---  
**Path parameters**  
`bucket` | `string` |  Name of the bucket in which the object resides.   
`object` | `string` |  Name of the object. For information about how to URL encode object names to be path safe, see [Encoding URI path parts](https://docs.cloud.google.com/storage/docs/request-endpoints#encoding).   
**Query parameters**  
`contextKey` | `string` |  **Required.** The key of the object context to retrieve. For example, `google:annotation:face-detector-v1`.   
`generation` | `long` |  If present, selects a specific revision of this object (as opposed to the latest version, the default).   
  
### Request body

Do not supply a request body with this method.

## Response

If successful, this method returns a response body with the following structure:
    
    
    {
      "kind": "storage#objectFullContext",
      "type": "CUSTOM",
      "key": string,
      "value": string,
      "createTime": datetime,
      "updateTime": datetime,
      "extendedData": {
        "@type": "type.googleapis.com/google.protobuf.Struct",
        "value": object
      }
    }

Property name | Value | Description | Notes  
---|---|---|---  
`kind` | `string` | The kind of item this is. For an object full context, this is always `storage#objectFullContext`. |   
`type` | `string` | The context type. Always `CUSTOM`. |   
`key` | `string` | The unique identifier for the context. |   
`value` | `string` | The value associated with this context. |   
`createTime` | `datetime` | The time when this context key was first added to the object. Specified in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format. |   
`updateTime` | `datetime` | The time when this context key was last updated. Specified in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format. |   
`extendedData` | `nested object` | The structured JSON payload containing extended context metadata ([Preview](https://docs.cloud.google.com/products#product-launch-stages)). |   
`extendedData.@type` | `string` | The type URL of the extended metadata (`type.googleapis.com/google.protobuf.Struct`). |   
`extendedData.value` | `object` | The JSON payload containing the structured extended data. |   
  
For information about status and error codes returned by this API, see the [reference page](https://docs.cloud.google.com/storage/docs/json_api/v1/status-codes).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
