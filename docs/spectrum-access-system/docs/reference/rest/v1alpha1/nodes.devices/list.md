---
url: https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/nodes.devices/list/
title: Method: nodes.devices.list \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:05:51.081868+00:00
---

# Method: nodes.devices.list  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/nodes.devices/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)



Send feedback 

#  Method: nodes.devices.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization Scopes



Lists `[devices](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device)` under a `[node](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.nodes#Node)` or `[customer](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers#Customer)`.

### HTTP request

`GET https://sasportal.googleapis.com/v1alpha1/{parent=nodes/*}/devices`

The URL uses [gRPC Transcoding](https://github.com/googleapis/googleapis/blob/master/google/api/http.proto) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The name of the parent resource.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` The maximum number of devices to return in the response. If empty or zero, all devices will be listed. Must be in the range [0, 1000].  
`pageToken` |  `string` A pagination token returned from a previous call to `[devices.list](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/nodes.devices/list#spectrum.sas.portal.v1alpha1.DeviceManager.ListDevices)` that indicates where this listing should continue from.  
`filter` |  `string` The filter expression. The filter should have one of the following formats: "sn=123454" or "displayName=MyDevice". sn corresponds to serial number of the device. The filter is case insensitive.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ListDevicesResponse](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/ListDevicesResponse)`.

### Authorization Scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/userinfo.email`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-09 UTC."],[],[]] 
