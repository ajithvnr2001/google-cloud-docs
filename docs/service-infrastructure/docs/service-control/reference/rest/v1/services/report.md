---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/report/
title: Method: services.report \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:32.718224+00:00
---

# Method: services.report  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/report/

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
  * Authorization Scopes
  * ReportError
    * JSON representation



Reports operation results to Google Service Control, such as logs and metrics. It should be called after an operation is completed.

If feasible, the client should aggregate reporting data for up to 5 seconds to reduce API traffic. Limiting aggregation to 5 seconds is to reduce data loss during client crashes. Clients should carefully choose the aggregation time window to avoid data loss risk more than 0.01% for business and compliance reasons.

NOTE: the `ReportRequest` has the size limit (wire-format byte size) of 1MB.

This method requires the `servicemanagement.services.report` permission on the specified service. For more information, see [Google Cloud IAM](https://cloud.google.com/iam).

### HTTP request

`POST https://servicecontrol.googleapis.com/v1/services/{serviceName}:report`

The URL uses [gRPC Transcoding](https://github.com/googleapis/googleapis/blob/master/google/api/http.proto) syntax.

### Path parameters

Parameters  
---  
`serviceName` |  `string` The service name as specified in its service configuration. For example, `"pubsub.googleapis.com"`.See [google.api.Service](https://cloud.google.com/service-management/reference/rpc/google.api#google.api.Service) for the definition of a service name. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `serviceName`:

  * `servicemanagement.services.report`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "operations": [
        {
          object ([Operation](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/Operation))
        }
      ],
      "serviceConfigId": string
    }  
  
Fields  
---  
`operations[]` |  `object (`[Operation](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/Operation)`)` Operations to be reported.Typically the service should report one operation per request. Putting multiple operations into a single request is allowed, but should be used only when multiple operations are natually available at the time of the report.There is no limit on the number of operations in the same ReportRequest, however the ReportRequest size should be no larger than 1MB. See `[ReportResponse.report_errors](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/report#body.ReportResponse.FIELDS.report_errors)` for partial failure behavior.  
`serviceConfigId` |  `string` Specifies which version of service config should be used to process the request.If unspecified or no matching version can be found, the latest one will be used.  
  
### Response body

If successful, the response body contains data with the following structure:

Response message for the services.report method.

JSON representation  
---  
      
    
    {
      "reportErrors": [
        {
          object ([ReportError](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/report#ReportError))
        }
      ],
      "serviceConfigId": string,
      "serviceRolloutId": string
    }  
  
Fields  
---  
`reportErrors[]` |  `object (`[ReportError](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/report#ReportError)`)` Partial failures, one for each `Operation` in the request that failed processing. There are three possible combinations of the RPC status:

  1. The combination of a successful RPC status and an empty `reportErrors` list indicates a complete success where all `Operations` in the request are processed successfully.
  2. The combination of a successful RPC status and a non-empty `reportErrors` list indicates a partial success where some `Operations` in the request succeeded. Each `Operation` that failed processing has a corresponding item in this list.
  3. A failed RPC status indicates a general non-deterministic failure. When this happens, it's impossible to know which of the 'Operations' in the request succeeded or failed.

  
`serviceConfigId` |  `string` The actual config id used to process the request.  
`serviceRolloutId` |  `string` The current service rollout id used to process the request.  
  
### Authorization Scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/servicecontrol`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

## ReportError

Represents the processing error of one `[Operation](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/Operation)` in the request.

JSON representation  
---  
      
    
    {
      "operationId": string,
      "status": {
        object ([Status](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/Shared.Types/AuditLog#Status))
      }
    }  
  
Fields  
---  
`operationId` |  `string` The `[Operation.operation_id](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/Operation#FIELDS.operation_id)` value from the request.  
`status` |  `object (`[Status](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/Shared.Types/AuditLog#Status)`)` Details of the error when processing the `[Operation](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/Operation)`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
