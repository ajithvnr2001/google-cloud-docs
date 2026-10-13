---
url: https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.devices/updateSigned/
title: Method: customers.devices.updateSigned \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:51:29.839277+00:00
---

# Method: customers.devices.updateSigned  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.devices/updateSigned/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)



Send feedback 

#  Method: customers.devices.updateSigned Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization Scopes



Updates a signed `[device](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device)`.

### HTTP request

`PATCH https://sasportal.googleapis.com/v1alpha1/{name=customers/*/devices/*}:updateSigned`

The URL uses [gRPC Transcoding](https://github.com/googleapis/googleapis/blob/master/google/api/http.proto) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the device to update.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "encodedDevice": string,
      "installerId": string
    }  
  
Fields  
---  
`encodedDevice` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. The JSON Web Token signed using a CPI private key. Payload must be the JSON encoding of the `[device](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device)`. The `[userId](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device.DeviceConfig.FIELDS.user_id)` field must be set.A base64-encoded string.  
`installerId` |  `string` Required. Unique installer ID (CPI ID) from the Certified Professional Installers database.  
  
### Response body

If successful, the response body contains an instance of `[Device](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/v1alpha1/customers.deployments.devices#Device)`.

### Authorization Scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/userinfo.email`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-09 UTC."],[],[]] 
