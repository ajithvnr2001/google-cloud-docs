---
url: https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/installer/validate/
title: Method: installer.validate \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:43:54.582518+00:00
---

# Method: installer.validate  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/installer/validate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Reference ](https://docs.cloud.google.com/spectrum-access-system/docs/apis)



Send feedback 

#  Method: installer.validate Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Request body
    * JSON representation
  * Response body
  * Authorization Scopes



Validates the identity of a Certified Professional Installer (CPI).

### HTTP request

`POST https://sasportal.googleapis.com/v1alpha1/installer:validate`

The URL uses [gRPC Transcoding](https://github.com/googleapis/googleapis/blob/master/google/api/http.proto) syntax.

### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "installerId": string,
      "secret": string,
      "encodedSecret": string
    }  
  
Fields  
---  
`installerId` |  `string` Required. Unique installer id (cpiId) from the Certified Professional Installers database.   
`secret` |  `string` Required. Secret returned by the `[installer.generateSecret method](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/installer/generateSecret#spectrum.sas.portal.v1alpha1.DeviceManager.GenerateSecret)`.   
`encodedSecret` |  `string` Required. JSON Web Token signed using a CPI private key. Payload must include a "secret" claim whose value is the secret.   
  
### Response body

If successful, the response body will be empty.

### Authorization Scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/userinfo.email`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-09 UTC."],[],[]] 
