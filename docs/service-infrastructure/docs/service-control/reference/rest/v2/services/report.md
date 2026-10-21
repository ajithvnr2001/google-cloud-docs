---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v2/services/report/
title: Method: services.report \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:33.304688+00:00
---

# Method: services.report  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v2/services/report/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  Method: services.report Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes



This method provides telemetry reporting for services that are integrated with [Service Infrastructure](https://cloud.google.com/service-infrastructure). It reports a list of operations that have occurred on a service. It must be called after the operations have been executed. For more information, see [Telemetry Reporting](https://cloud.google.com/service-infrastructure/docs/telemetry-reporting).

NOTE: The telemetry reporting has a hard limit of 1000 operations and 1MB per services.report call. It is recommended to have no more than 100 operations per call.

This method requires the `servicemanagement.services.report` permission on the specified service. For more information, see [Service Control API Access Control](https://cloud.google.com/service-infrastructure/docs/service-control/access-control).

### HTTP request

`POST https://servicecontrol.googleapis.com/v2/services/{serviceName}:report`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`serviceName` |  `string` The service name as specified in its service configuration. For example, `"pubsub.googleapis.com"`.See [google.api.Service](https://cloud.google.com/service-management/reference/rpc/google.api#google.api.Service) for the definition of a service name.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "serviceConfigId": string,
      "operations": [
        {
          object ([AttributeContext](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v2/AttributeContext))
        }
      ]
    }  
  
Fields  
---  
`serviceConfigId` |  `string` Specifies the version of the service configuration that should be used to process the request. Must not be empty. Set this field to 'latest' to specify using the latest configuration.  
`operations[]` |  `object (`[AttributeContext](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v2/AttributeContext)`)` Describes the list of operations to be reported. Each operation is represented as an AttributeContext, and contains all attributes around an API access.  
  
### Response body

Response message for the services.report method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "extensions": {
        "@type": string,
        field1: ...,
        ...
      }
    }  
  
Fields  
---  
`extensions` |  `object` The extension field to store serialized OTel responses. e.g. ExportLogsServiceResponse, ExportMetricsServiceResponse.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/servicecontrol`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
