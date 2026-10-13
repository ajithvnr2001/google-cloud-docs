---
url: https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices/cancelWipe/
title: Method: devices.cancelWipe \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:46.776494+00:00
---

# Method: devices.cancelWipe  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices/cancelWipe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  Method: devices.cancelWipe Stay organized with collections  Save and categorize content based on your preferences. 

Cancels an unfinished device wipe. This operation can be used to cancel device wipe in the gap between the wipe operation returning success and the device being wiped.

### HTTP request

`POST https://cloudidentity.googleapis.com/v1beta1/{name=devices/*}:cancelWipe`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. [Resource name](https://cloud.google.com/apis/design/resource_names) of the Device in format: `devices/{deviceId}`, where deviceId is the unique ID assigned to the Device.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "customer": string
    }  
  
Fields  
---  
`customer` |  `string` Optional. [Resource name](https://cloud.google.com/apis/design/resource_names) of the customer. If you're using this API for your own organization, use `customers/my_customer` If you're using this API to manage another organization, use `customers/{customerId}`, where customerId is the customer to whom the device belongs.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/identity/docs/reference/rest/Shared.Types/Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-identity.devices`
  * `https://www.googleapis.com/auth/cloud-identity`



For more information, see the [Authorization guide](https://developers.google.com/workspace/guides/configure-oauth-consent).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-16 UTC."],[],[]] 
