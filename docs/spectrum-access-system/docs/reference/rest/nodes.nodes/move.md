---
url: https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/nodes.nodes/move/
title: Method: nodes.nodes.move \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:30:02.164618+00:00
---

# Method: nodes.nodes.move  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/nodes.nodes/move/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Reference ](https://docs.cloud.google.com/spectrum-access-system/docs/apis)



Send feedback 

#  Method: nodes.nodes.move Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization Scopes



Moves a `[node](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/customers.nodes#Node)` under another `[node](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/customers.nodes#Node)` or `[customer](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/customers#Customer)`.

### HTTP request

`POST https://sasportal.googleapis.com/v1alpha1/{name=nodes/*/nodes/*}:move`

The URL uses [gRPC Transcoding](https://github.com/googleapis/googleapis/blob/master/google/api/http.proto) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the `[node](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/customers.nodes#Node)` to move.   
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "destination": string
    }  
  
Fields  
---  
`destination` |  `string` Required. The name of the new parent resource `[node](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/customers.nodes#Node)` or `[Customer](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/customers#Customer)` to reparent the node under.   
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/spectrum-access-system/docs/reference/rest/Operation)`.

### Authorization Scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/userinfo.email`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-09 UTC."],[],[]] 
