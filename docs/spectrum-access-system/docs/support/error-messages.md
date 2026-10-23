---
url: https://docs.cloud.google.com/spectrum-access-system/docs/support/error-messages/
title: Error messages \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:40:17.077626+00:00
---

# Error messages  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/support/error-messages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Guides ](https://docs.cloud.google.com/spectrum-access-system/docs/overview)



Send feedback 

#  Error messages Stay organized with collections  Save and categorize content based on your preferences. 

The following table describes error messages that you might encounter when using the Google Spectrum Access System (SAS) Portal API.   
Error code | Message | Description  
---|---|---  
`400` | Invalid <parameter name>: <value> | The given device parameter was provided with an invalid value.  
`400` | CBSD must not set active configuration. | A device with an active configuration was passed to [`CreateDevice()`](https://docs.cloud.google.com/spectrum-access-system/reference/rest/customers.devices/create).  
`400` | CBSD out-of-date: <CBSD> | The device configuration changed on the server prior to being passed to [`SignDevice()`](https://docs.cloud.google.com/spectrum-access-system/reference/rest/customers.devices/signDevice).  
`400` | Secret expired: <secret> | The secret passed to [`ValidateInstaller()`](https://docs.cloud.google.com/spectrum-access-system/reference/rest/customers.devices/validate) has expired.  
`400` | No `value` in JWT payload. | The encoded JWT did not contain the `value` field.  
`400` | Signature verification error. | The CPI signature could not be verified.  
`401` | A missing request required an authentication credential. Expected OAuth 2 access token, login cookie, or other valid authentication credential. For details, see [Integrating Google Sign-In into your web app](https://developers.google.com/identity/sign-in/web/sign-in). | The credentials passed to the API call were missing.  
`403` | No permissions to call this method. | The caller is missing the role required to call the method.  
`403` | Installer not verified. | The caller has the `role_cpi` role but needs to be validated in order to make the API call.  
`404` | Requested entity was not found. | The resource specified in the API call does not exist.  
`409` | Entity already exists. | The resource specified in the API call already exists.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
