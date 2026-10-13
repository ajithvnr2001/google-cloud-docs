---
url: https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers.clientStates/list/
title: Method: devices.deviceUsers.clientStates.list \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:36.870885+00:00
---

# Method: devices.deviceUsers.clientStates.list  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers.clientStates/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  Method: devices.deviceUsers.clientStates.list Stay organized with collections  Save and categorize content based on your preferences. 

Lists the client states for the given search query.

### HTTP request

`GET https://cloudidentity.googleapis.com/v1/{parent=devices/*/deviceUsers/*}/clientStates`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. To list all ClientStates, set this to "devices/-/deviceUsers/-". To list all ClientStates owned by a DeviceUser, set this to the resource name of the DeviceUser. Format: devices/{device}/deviceUsers/{deviceUser}  
  
### Query parameters

Parameters  
---  
`customer` |  `string` Optional. [Resource name](https://cloud.google.com/apis/design/resource_names) of the customer. If you're using this API for your own organization, use `customers/my_customer` If you're using this API to manage another organization, use `customers/{customer}`, where customer is the customer to whom the device belongs.  
`filter` |  `string` Optional. Additional restrictions when fetching list of client states.  
`pageToken` |  `string` Optional. A page token, received from a previous `clientStates.list` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `clientStates.list` must match the call that provided the page token.  
`orderBy` |  `string` Optional. Order specification for client states in the response.  
  
### Request body

The request body must be empty.

### Response body

Response message that is returned in clientStates.list.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "clientStates": [
        {
          object ([ClientState](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers.clientStates#ClientState))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`clientStates[]` |  `object (`[ClientState](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers.clientStates#ClientState)`)` Client states meeting the list restrictions.  
`nextPageToken` |  `string` Token to retrieve the next page of results. Empty if there are no more results.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-identity.devices.readonly`
  * `https://www.googleapis.com/auth/cloud-identity.devices`
  * `https://www.googleapis.com/auth/cloud-identity`



For more information, see the [Authorization guide](https://developers.google.com/workspace/guides/configure-oauth-consent).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-16 UTC."],[],[]] 
