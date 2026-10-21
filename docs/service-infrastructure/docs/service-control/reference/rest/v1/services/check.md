---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/check/
title: Method: services.check \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:32.507120+00:00
---

# Method: services.check  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/check/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  Method: services.check Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization Scopes
  * CheckError
    * JSON representation
  * Code
  * CheckInfo
    * JSON representation
  * ConsumerInfo
    * JSON representation
  * ConsumerType



Checks whether an operation on a service should be allowed to proceed based on the configuration of the service and related policies. It must be called before the operation is executed.

If feasible, the client should cache the check results and reuse them for 60 seconds. In case of any server errors, the client should rely on the cached results for much longer time to avoid outage. WARNING: There is general 60s delay for the configuration and policy propagation, therefore callers MUST NOT depend on the `services.check` method having the latest policy information.

NOTE: the `CheckRequest` has the size limit of 1MB.

This method requires the `servicemanagement.services.check` permission on the specified service. For more information, see [Cloud IAM](https://cloud.google.com/iam).

### HTTP request

`POST https://servicecontrol.googleapis.com/v1/services/{serviceName}:check`

The URL uses [gRPC Transcoding](https://github.com/googleapis/googleapis/blob/master/google/api/http.proto) syntax.

### Path parameters

Parameters  
---  
`serviceName` |  `string` The service name as specified in its service configuration. For example, `"pubsub.googleapis.com"`.See [google.api.Service](https://cloud.google.com/service-management/reference/rpc/google.api#google.api.Service) for the definition of a service name. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `serviceName`:

  * `servicemanagement.services.check`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "operation": {
        object ([Operation](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/Operation))
      },
      "serviceConfigId": string
    }  
  
Fields  
---  
`operation` |  `object (`[Operation](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/Operation)`)` The operation to be checked.  
`serviceConfigId` |  `string` Specifies which version of service configuration should be used to process the request.If unspecified or no matching version can be found, the latest one will be used.  
  
### Response body

If successful, the response body contains data with the following structure:

Response message for the services.check method.

JSON representation  
---  
      
    
    {
      "operationId": string,
      "checkErrors": [
        {
          object ([CheckError](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/check#CheckError))
        }
      ],
      "serviceConfigId": string,
      "serviceRolloutId": string,
      "checkInfo": {
        object ([CheckInfo](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/check#CheckInfo))
      }
    }  
  
Fields  
---  
`operationId` |  `string` The same operationId value used in the `CheckRequest`. Used for logging and diagnostics purposes.  
`checkErrors[]` |  `object (`[CheckError](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/check#CheckError)`)` Indicate the decision of the check.If no check errors are present, the service should process the operation. Otherwise the service should use the list of errors to determine the appropriate action.  
`serviceConfigId` |  `string` The actual config id used to process the request.  
`serviceRolloutId` |  `string` The current service rollout id used to process the request.  
`checkInfo` |  `object (`[CheckInfo](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/check#CheckInfo)`)` Feedback data returned from the server during processing a services.check request.  
  
### Authorization Scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/servicecontrol`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

## CheckError

Defines the errors to be returned in `[google.api.servicecontrol.v1.CheckResponse.check_errors](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/check#body.CheckResponse.FIELDS.check_errors)`.

JSON representation  
---  
      
    
    {
      "code": enum ([Code](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/check#Code)),
      "subject": string,
      "detail": string,
      "status": {
        object ([Status](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/Shared.Types/AuditLog#Status))
      }
    }  
  
Fields  
---  
`code` |  `enum (`[Code](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/check#Code)`)` The error code.  
`subject` |  `string` Subject to whom this error applies. See the specific code enum for more details on this field. For example:

  * "project:"
  * "folder:"
  * "organization:"

  
`detail` |  `string` Free-form text providing details on the error cause of the error.  
`status` |  `object (`[Status](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/Shared.Types/AuditLog#Status)`)` Contains public information about the check error. If available, `status.code` will be non zero and client can propagate it out as public error.  
  
## Code

Error codes for services.check responses.

Enums  
---  
`ERROR_CODE_UNSPECIFIED` | This is never used in `CheckResponse`.  
`NOT_FOUND` | The consumer's project id, network container, or resource container was not found. Same as `[google.rpc.Code.NOT_FOUND](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/Shared.Types/Code#ENUM_VALUES.NOT_FOUND)`.  
`PERMISSION_DENIED` | The consumer doesn't have access to the specified resource. Same as `[google.rpc.Code.PERMISSION_DENIED](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/Shared.Types/Code#ENUM_VALUES.PERMISSION_DENIED)`.  
`RESOURCE_EXHAUSTED` | Quota check failed. Same as `[google.rpc.Code.RESOURCE_EXHAUSTED](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/Shared.Types/Code#ENUM_VALUES.RESOURCE_EXHAUSTED)`.  
`SERVICE_NOT_ACTIVATED` | The consumer hasn't activated the service.  
`BILLING_DISABLED` | The consumer cannot access the service because billing is disabled.  
`PROJECT_DELETED` | The consumer's project has been marked as deleted (soft deletion).  
`PROJECT_INVALID` | The consumer's project number or id does not represent a valid project.  
`CONSUMER_INVALID` | The input consumer info does not represent a valid consumer folder or organization.  
`IP_ADDRESS_BLOCKED` | The IP address of the consumer is invalid for the specific consumer project.  
`REFERER_BLOCKED` | The referer address of the consumer request is invalid for the specific consumer project.  
`CLIENT_APP_BLOCKED` | The client application of the consumer request is invalid for the specific consumer project.  
`API_TARGET_BLOCKED` | The API targeted by this request is invalid for the specified consumer project.  
`API_KEY_INVALID` | The consumer's API key is invalid.  
`API_KEY_EXPIRED` | The consumer's API Key has expired.  
`API_KEY_NOT_FOUND` | The consumer's API Key was not found in config record.  
`INVALID_CREDENTIAL` | The credential in the request can not be verified.  
`NAMESPACE_LOOKUP_UNAVAILABLE` | The backend server for looking up project id/number is unavailable.  
`SERVICE_STATUS_UNAVAILABLE` | The backend server for checking service status is unavailable.  
`BILLING_STATUS_UNAVAILABLE` | The backend server for checking billing status is unavailable.  
`CLOUD_RESOURCE_MANAGER_BACKEND_UNAVAILABLE` | Cloud Resource Manager backend server is unavailable.  
  
## CheckInfo

Contains additional information about the check operation.

JSON representation  
---  
      
    
    {
      "unusedArguments": [
        string
      ],
      "consumerInfo": {
        object ([ConsumerInfo](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/check#ConsumerInfo))
      }
    }  
  
Fields  
---  
`unusedArguments[]` |  `string` A list of fields and label keys that are ignored by the server. The client doesn't need to send them for following requests to improve performance and allow better aggregation.  
`consumerInfo` |  `object (`[ConsumerInfo](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/check#ConsumerInfo)`)` Consumer info of this check.  
  
## ConsumerInfo

`ConsumerInfo` provides information about the consumer.

JSON representation  
---  
      
    
    {
      "projectNumber": string,
      "type": enum ([ConsumerType](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/check#ConsumerType)),
      "consumerNumber": string
    }  
  
Fields  
---  
`projectNumber` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The Google cloud project number, e.g. 1234567890. A value of 0 indicates no project number is found.NOTE: This field is deprecated after Chemist support flexible consumer id. New code should not depend on this field anymore.  
`type` |  `enum (`[ConsumerType](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/check#ConsumerType)`)` The type of the consumer which should have been defined in [Google Resource Manager](https://cloud.google.com/resource-manager/).  
`consumerNumber` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The consumer identity number, can be Google cloud project number, folder number or organization number e.g. 1234567890. A value of 0 indicates no consumer number is found.  
  
## ConsumerType

The type of the consumer as defined in [Google Resource Manager](https://cloud.google.com/resource-manager/).

Enums  
---  
`CONSUMER_TYPE_UNSPECIFIED` | This is never used.  
`PROJECT` | The consumer is a Google Cloud Project.  
`FOLDER` | The consumer is a Google Cloud Folder.  
`ORGANIZATION` | The consumer is a Google Cloud Organization.  
`SERVICE_SPECIFIC` | Service-specific resource container which is defined by the service producer to offer their users the ability to manage service control functionalities at a finer level of granularity than the PROJECT.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
