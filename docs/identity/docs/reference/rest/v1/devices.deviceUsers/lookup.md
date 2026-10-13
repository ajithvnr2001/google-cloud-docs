---
url: https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers/lookup/
title: Method: devices.deviceUsers.lookup \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:35.962581+00:00
---

# Method: devices.deviceUsers.lookup  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers/lookup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  Method: devices.deviceUsers.lookup Stay organized with collections  Save and categorize content based on your preferences. 

Looks up resource names of the DeviceUsers associated with the caller's credentials, as well as the properties provided in the request.

This method must be called with end-user credentials with the scope: <https://www.googleapis.com/auth/cloud-identity.devices.lookup>

If multiple properties are provided, only DeviceUsers having all of these properties are considered as matches - i.e. the query behaves like an AND.

Different platforms require different amounts of information from the caller to ensure that the DeviceUser is uniquely identified.

  * iOS: If either the `partner` or `iosDeviceId` field is provided, then both fields are required.
  * Android: Specifying the `androidId` field is required.
  * Desktop: Specifying the `rawResourceId` field is required.



### HTTP request

`GET https://cloudidentity.googleapis.com/v1/{parent=devices/*/deviceUsers}:lookup`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Must be set to "devices/-/deviceUsers" to search across all DeviceUser belonging to the user.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` The maximum number of DeviceUsers to return. If unspecified, at most 20 DeviceUsers will be returned. The maximum value is 20; values above 20 will be coerced to 20.  
`pageToken` |  `string` A page token, received from a previous `LookupDeviceUsers` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `LookupDeviceUsers` must match the call that provided the page token.  
`androidId` |  `string` Android Id returned by [Settings.Secure#ANDROID_ID](https://developer.android.com/reference/android/provider/Settings.Secure.html#ANDROID_ID).  
`rawResourceId` |  `string` Raw Resource Id used by Google Endpoint Verification.If the user is enrolled into Google Endpoint Verification, this id will be saved as the 'device_resource_id' field in the following platform dependent files.Mac: ~/.secureConnect/context_aware_config.json Windows: C:\Users\%USERPROFILE%.secureConnect\context_aware_config.json Linux: ~/.secureConnect/context_aware_config.json  
`userId` |  `string` The user whose DeviceUser's resource name will be fetched. Must be set to 'me' to fetch the DeviceUser's resource name for the calling user.  
`partner` |  `string` Optional. The partner ID of the calling iOS app. This string must match the value of the partner key within the app configuration dictionary provided to Google Workspace apps.  
`iosDeviceId` |  `string` Optional. The partner-specified device identifier assigned to the iOS device that initiated the Lookup API call. This string must match the value of the iosDeviceId key in the app config dictionary provided to Google Workspace apps.  
  
### Request body

The request body must be empty.

### Response body

Response containing resource names of the DeviceUsers associated with the caller's credentials.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "names": [
        string
      ],
      "customer": string,
      "nextPageToken": string
    }  
  
Fields  
---  
`names[]` |  `string` [Resource names](https://cloud.google.com/apis/design/resource_names) of the DeviceUsers in the format: `devices/{device}/deviceUsers/{user_resource}`, where device is the unique ID assigned to a Device and user_resource is the unique user ID  
`customer` |  `string` The customer resource name that may be passed back to other Devices API methods such as List, Get, etc.  
`nextPageToken` |  `string` Token to retrieve the next page of results. Empty if there are no more results.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-identity.devices.lookup`



For more information, see the [Authorization guide](https://developers.google.com/workspace/guides/configure-oauth-consent).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-14 UTC."],[],[]] 
