---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/allocateQuota/
title: Method: services.allocateQuota \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:25:31.778521+00:00
---

# Method: services.allocateQuota  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/allocateQuota/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  Method: services.allocateQuota Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization Scopes
  * QuotaOperation
    * JSON representation
  * QuotaMode
  * QuotaError
    * JSON representation
  * Code



Attempts to allocate quota for the specified consumer. It should be called before the operation is executed.

This method requires the `servicemanagement.services.quota` permission on the specified service. For more information, see [Cloud IAM](https://cloud.google.com/iam).

**NOTE:** The client **must** fail-open on server errors `INTERNAL`, `UNKNOWN`, `DEADLINE_EXCEEDED`, and `UNAVAILABLE`. To ensure system reliability, the server may inject these errors to prohibit any hard dependency on the quota functionality.

### HTTP request

`POST https://servicecontrol.googleapis.com/v1/services/{serviceName}:allocateQuota`

The URL uses [gRPC Transcoding](https://github.com/googleapis/googleapis/blob/master/google/api/http.proto) syntax.

### Path parameters

Parameters  
---  
`serviceName` |  `string` Name of the service as specified in the service configuration. For example, `"pubsub.googleapis.com"`.See `google.api.Service` for the definition of a service name. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `serviceName`:

  * `servicemanagement.services.quota`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "allocateOperation": {
        object ([QuotaOperation](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/allocateQuota#QuotaOperation))
      },
      "serviceConfigId": string
    }  
  
Fields  
---  
`allocateOperation` |  `object (`[QuotaOperation](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/allocateQuota#QuotaOperation)`)` Operation that describes the quota allocation.  
`serviceConfigId` |  `string` Specifies which version of service configuration should be used to process the request. If unspecified or no matching version can be found, the latest one will be used.  
  
### Response body

If successful, the response body contains data with the following structure:

Response message for the services.allocateQuota method.

JSON representation  
---  
      
    
    {
      "operationId": string,
      "allocateErrors": [
        {
          object ([QuotaError](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/allocateQuota#QuotaError))
        }
      ],
      "quotaMetrics": [
        {
          object ([MetricValueSet](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/MetricValueSet))
        }
      ],
      "serviceConfigId": string
    }  
  
Fields  
---  
`operationId` |  `string` The same operationId value used in the AllocateQuotaRequest. Used for logging and diagnostics purposes.  
`allocateErrors[]` |  `object (`[QuotaError](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/allocateQuota#QuotaError)`)` Indicates the decision of the allocate.  
`quotaMetrics[]` |  `object (`[MetricValueSet](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/MetricValueSet)`)` Quota metrics to indicate the result of allocation. Depending on the request, one or more of the following metrics will be included:

  1. Per quota group or per quota metric incremental usage will be specified using the following delta metric : "serviceruntime.googleapis.com/api/consumer/quota_used_count"
  2. The quota limit reached condition will be specified using the following boolean metric : "serviceruntime.googleapis.com/quota/exceeded"

  
`serviceConfigId` |  `string` ID of the actual config used to process the request.  
  
### Authorization Scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/servicecontrol`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

## QuotaOperation

Represents information regarding a quota operation.

JSON representation  
---  
      
    
    {
      "operationId": string,
      "methodName": string,
      "consumerId": string,
      "labels": {
        string: string,
        ...
      },
      "quotaMetrics": [
        {
          object ([MetricValueSet](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/MetricValueSet))
        }
      ],
      "quotaMode": enum ([QuotaMode](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/allocateQuota#QuotaMode))
    }  
  
Fields  
---  
`operationId` |  `string` Identity of the operation. This is expected to be unique within the scope of the service that generated the operation, and guarantees idempotency in case of retries.In order to ensure best performance and latency in the Quota backends, operation_ids are optimally associated with time, so that related operations can be accessed fast in storage. For this reason, the recommended token for services that intend to operate at a high QPS is Unix time in nanos + UUID  
`methodName` |  `string` Fully qualified name of the API method for which this quota operation is requested. This name is used for matching quota rules or metric rules and billing status rules defined in service configuration.This field should not be set if any of the following is true: (1) the quota operation is performed on non-API resources. (2) quotaMetrics is set because the caller is doing quota override.Example of an RPC method name: google.example.library.v1.LibraryService.CreateShelf  
`consumerId` |  `string` Identity of the consumer for whom this quota operation is being performed.This can be in one of the following formats: project:, projectNumber:, apiKey:.  
`labels` |  `map (key: string, value: string)` Labels describing the operation.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`quotaMetrics[]` |  `object (`[MetricValueSet](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/MetricValueSet)`)` Represents information about this operation. Each MetricValueSet corresponds to a metric defined in the service configuration. The data type used in the MetricValueSet must agree with the data type specified in the metric definition.Within a single operation, it is not allowed to have more than one MetricValue instances that have the same metric names and identical label value combinations. If a request has such duplicated MetricValue instances, the entire request is rejected with an invalid argument error.This field is mutually exclusive with methodName.  
`quotaMode` |  `enum (`[QuotaMode](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/allocateQuota#QuotaMode)`)` Quota mode for this operation.  
  
## QuotaMode

Supported quota modes.

Enums  
---  
`UNSPECIFIED` | Guard against implicit default. Must not be used.  
`NORMAL` | For services.allocateQuota request, allocates quota for the amount specified in the service configuration or specified using the quota metrics. If the amount is higher than the available quota, allocation error will be returned and no quota will be allocated. If multiple quotas are part of the request, and one fails, none of the quotas are allocated or released.  
`BEST_EFFORT` | The operation allocates quota for the amount specified in the service configuration or specified using the quota metrics. If the amount is higher than the available quota, request does not fail but all available quota will be allocated. For rate quota, BEST_EFFORT will continue to deduct from other groups even if one does not have enough quota. For allocation, it will find the minimum available amount across all groups and deduct that amount from all the affected groups.  
`CHECK_ONLY` | For services.allocateQuota request, only checks if there is enough quota available and does not change the available quota. No lock is placed on the available quota either.  
`QUERY_ONLY` | Unimplemented. When used in AllocateQuotaRequest, this returns the effective quota limit(s) in the response, and no quota check will be performed. Not supported for other requests, and even for AllocateQuotaRequest, this is currently supported only for allowlisted services.  
`ADJUST_ONLY` | The operation allocates quota for the amount specified in the service configuration or specified using the quota metrics. If the requested amount is higher than the available quota, request does not fail and remaining quota would become negative (going over the limit). Not supported for Rate Quota.  
  
## QuotaError

Represents error information for `[QuotaOperation](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/allocateQuota#QuotaOperation)`.

JSON representation  
---  
      
    
    {
      "code": enum ([Code](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/allocateQuota#Code)),
      "subject": string,
      "description": string,
      "status": {
        object ([Status](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/Shared.Types/AuditLog#Status))
      }
    }  
  
Fields  
---  
`code` |  `enum (`[Code](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/allocateQuota#Code)`)` Error code.  
`subject` |  `string` Subject to whom this error applies. See the specific enum for more details on this field. For example, "clientip:" or "project:".  
`description` |  `string` Free-form text that provides details on the cause of the error.  
`status` |  `object (`[Status](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/Shared.Types/AuditLog#Status)`)` Contains additional information about the quota error. If available, `status.code` will be non zero.  
  
## Code

Error codes related to project config validations are deprecated since the quota controller methods do not perform these validations. Instead services have to call the services.check method, without quotaProperties field, to perform these validations before calling the quota controller methods. These methods check only for project deletion to be wipe out compliant.

Enums  
---  
`UNSPECIFIED` | This is never used.  
`RESOURCE_EXHAUSTED` | Quota allocation failed. Same as `[google.rpc.Code.RESOURCE_EXHAUSTED](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/Shared.Types/Code#ENUM_VALUES.RESOURCE_EXHAUSTED)`.  
`BILLING_NOT_ACTIVE` | Consumer cannot access the service because the service requires active billing.  
`PROJECT_DELETED` | Consumer's project has been marked as deleted (soft deletion).  
`API_KEY_INVALID` | Specified API key is invalid.  
`API_KEY_EXPIRED` | Specified API Key has expired.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
