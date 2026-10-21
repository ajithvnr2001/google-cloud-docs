---
url: https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.devices/list/
title: Method: projects.locations.devices.list \u00a0|\u00a0 Developer Device Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:26:01.867607+00:00
---

# Method: projects.locations.devices.list  |  Developer Device Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.devices/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Device Platform ](https://docs.cloud.google.com/developer-device-platform)
  * [ API Reference ](https://docs.cloud.google.com/developer-device-platform/apis)



Send feedback 

#  Method: projects.locations.devices.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Lists all devices.

### HTTP request

`GET https://devicerun.googleapis.com/v1alpha/{parent=projects/*/locations/*}/devices`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent of the collection of devices. Format: `projects/{project}/locations/global`. It takes the form `projects/{project}/locations/{location}`.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of devices to return. The server may return fewer items than this value.  
`pageToken` |  `string` Optional. A page token, received from a previous `devices.list` call. Provide this to receive the subsequent page.When paginating, all other parameters provided to `devices.list` must match the call that provided the page token.  
`filter` |  `string` Optional. An AIP-160 (<https://google.aip.dev/160>) filter expression restricting which devices are returned. An empty filter returns all devices.Filtering is supported over the `Device` fields, including nested fields via dot-path. Enum and string values must be double-quoted.Examples: * `platform = "ANDROID"` * `platform = "ANDROID" AND osVersion = "34"` * `hardwareType = "PHYSICAL" AND formFactor = "PHONE"` * `androidDetails.build_type = "userdebug"` * `availability.capacity = "HIGH"`  
  
### Request body

The request body must be empty.

### Response body

Response including listed devices.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "devices": [
        {
          object ([Device](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.devices#Device))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`devices[]` |  `object (`[Device](https://docs.cloud.google.com/developer-device-platform/reference/device-run/rest/v1alpha/projects.locations.devices#Device)`)` The list of devices.  
`nextPageToken` |  `string` Token to receive the next page of devices. This will be absent if the end of the response list has been reached.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://docs.cloud.google.com/iam/docs) permission on the `parent` resource:

  * `devicerun.devices.list`



For more information, see the [IAM documentation](https://docs.cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
