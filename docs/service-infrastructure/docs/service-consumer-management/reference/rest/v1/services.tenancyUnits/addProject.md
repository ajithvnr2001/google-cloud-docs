---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/addProject/
title: Method: services.tenancyUnits.addProject \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:41.067517+00:00
---

# Method: services.tenancyUnits.addProject  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/addProject/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure/docs)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  Method: services.tenancyUnits.addProject Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization Scopes
  * Try it!



Add a new tenant project to the tenancy unit. There can be a maximum of 512 tenant projects in a tenancy unit. If there are previously failed `tenancyUnits.addProject` calls, you might need to call `tenancyUnits.removeProject` first to resolve them before you can make another call to `tenancyUnits.addProject` with the same tag. Operation<response: Empty>.

### HTTP request

`POST https://serviceconsumermanagement.googleapis.com/v1/{parent=services/*/*/*/tenancyUnits/*}:addProject`

The URL uses [gRPC Transcoding](https://github.com/googleapis/googleapis/blob/master/google/api/http.proto) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Name of the tenancy unit. Such as 'services/service.googleapis.com/projects/12345/tenancyUnits/abcd'. Authorization requires the following [Google IAM](https://cloud.google.com/iam) permission on the specified resource `parent`:

  * `serviceconsumermanagement.tenancyu.addResource`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "tag": string,
      "projectConfig": {
        object ([TenantProjectConfig](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/TenantProjectConfig))
      }
    }  
  
Fields  
---  
`tag` |  `string` Tag of the added project. Must be less than 128 characters. Required.  
`projectConfig` |  `object (`[TenantProjectConfig](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/TenantProjectConfig)`)` Configuration of the new tenant project to be added to tenancy unit resources.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/Shared.Types/Operation)`.

### Authorization Scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

## Try it!

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
