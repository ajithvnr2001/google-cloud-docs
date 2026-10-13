---
url: https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices/list/
title: Method: devices.list \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:35.509195+00:00
---

# Method: devices.list  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  Method: devices.list Stay organized with collections  Save and categorize content based on your preferences. 

Lists/Searches devices.

### HTTP request

`GET https://cloudidentity.googleapis.com/v1/devices`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Query parameters

Parameters  
---  
`customer` |  `string` Optional. [Resource name](https://cloud.google.com/apis/design/resource_names) of the customer in the format: `customers/{customer}`, where customer is the customer to whom the device belongs. If you're using this API for your own organization, use `customers/my_customer`. If you're using this API to manage another organization, use `customers/{customer}`, where customer is the customer to whom the device belongs.  
`filter` |  `string` Optional. Additional restrictions when fetching list of devices. For a list of search fields, refer to [Mobile device search fields](https://developers.google.com/admin-sdk/directory/v1/search-operators). Multiple search fields are separated by the space character.  
`pageSize` |  `integer` Optional. The maximum number of Devices to return. If unspecified, at most 20 Devices will be returned. The maximum value is 100; values above 100 will be coerced to 100.  
`pageToken` |  `string` Optional. A page token, received from a previous `devices.list` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `devices.list` must match the call that provided the page token.  
`orderBy` |  `string` Optional. Order specification for devices in the response. Only one of the following field names may be used to specify the order: `createTime`, `lastSyncTime`, `model`, `osVersion`, `deviceType` and `serialNumber`. `desc` may be specified optionally at the end to specify results to be sorted in descending order. Default order is ascending.  
`view` |  `enum (`[View](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices/list#View)`)` Optional. The view to use for the List request.  
  
### Request body

The request body must be empty.

### Response body

Response message that is returned from the devices.list method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "devices": [
        {
          object ([Device](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices#Device))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`devices[]` |  `object (`[Device](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices#Device)`)` Devices meeting the list restrictions.  
`nextPageToken` |  `string` Token to retrieve the next page of results. Empty if there are no more results.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-identity.devices.readonly`
  * `https://www.googleapis.com/auth/cloud-identity.devices`
  * `https://www.googleapis.com/auth/cloud-identity`



For more information, see the [Authorization guide](https://developers.google.com/workspace/guides/configure-oauth-consent).

## View

The view determines which devices and device info are present in the response.

Enums  
---  
`VIEW_UNSPECIFIED` | Default value. The value is unused.  
`COMPANY_INVENTORY` | This view contains all devices imported by the company admin. Each device in the response contains all information specified by the company admin when importing the device (i.e. asset tags). This includes devices that may be unassigned or assigned to users.  
`USER_ASSIGNED_DEVICES` | This view contains all devices with at least one user registered on the device. Each device in the response contains all device information, except for asset tags.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-16 UTC."],[],[]] 
