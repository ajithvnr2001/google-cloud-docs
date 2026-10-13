---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.feeds/scheduleTransfer/
title: Method: feeds.scheduleTransfer \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:58:12.844797+00:00
---

# Method: feeds.scheduleTransfer  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.feeds/scheduleTransfer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Method: feeds.scheduleTransfer Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * State
  * ScheduleFeedTransferErrorDetails
    * JSON representation



**Full name** : projects.locations.instances.feeds.scheduleTransfer

Schedules a feed transfer for the feed. It passes the data fetched from the last feed transfer to the chronicle ingestion pipeline.

### HTTP request

`POST https://{endpoint}/v1alpha/{name}:scheduleTransfer`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/chronicle/docs/reference/rest#rest_endpoints).

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the feed for which we need to schedule the transfer. Format: projects/{project}/locations/{location}/instances/{instance}/feeds/{feed}  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "logType": string,
      "transferState": enum ([State](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.feeds/scheduleTransfer#State)),
      "errorDetails": {
        object ([ScheduleFeedTransferErrorDetails](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.feeds/scheduleTransfer#ScheduleFeedTransferErrorDetails))
      }
    }  
  
Fields  
---  
`logType` |  `string` Required. The logType  
`transferState` |  `enum (`[State](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.feeds/scheduleTransfer#State)`)` Required. The state of this transfer  
`errorDetails` |  `object (`[ScheduleFeedTransferErrorDetails](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.feeds/scheduleTransfer#ScheduleFeedTransferErrorDetails)`)` Optional. The details why transfer is not successful  
  
### Response body

feeds.scheduleTransfer response message.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "transferId": string,
      "nextStartTime": string
    }  
  
Fields  
---  
`transferId` |  `string` Required. The unique identifier of the next feed transfer.  
`nextStartTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Required. The customer identifier.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/chronicle`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## State

Possible transfer state

Enums  
---  
`STATE_UNSPECIFIED` | Default value. This value is unused.  
`SUCCEEDED` | Transfer is successful.  
`FAILED` | Transfer failed.  
`PARTIAL` | Transfer was partial.  
  
## ScheduleFeedTransferErrorDetails

ScheduleFeedTransferErrorDetails contains the error details for the transfer failure.

JSON representation  
---  
      
    
    {
      "errorCode": string,
      "errorMessage": string
    }  
  
Fields  
---  
`errorCode` |  `string` Optional. errorCode contains the error code for the transfer. The field is populated for the transfer with failed status  
`errorMessage` |  `string` Optional. errorCause contains the information regarding the failure cause.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
