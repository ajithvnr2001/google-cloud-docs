---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v2/services/check/
title: Method: services.check \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:33.093086+00:00
---

# Method: services.check  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v2/services/check/

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
  * Authorization scopes
  * ResourceInfo
    * JSON representation



This method provides admission control for services that are integrated with [Service Infrastructure](https://cloud.google.com/service-infrastructure). It checks whether an operation should be allowed based on the service configuration and relevant policies. It must be called before the operation is executed. For more information, see [Admission Control](https://cloud.google.com/service-infrastructure/docs/admission-control).

NOTE: The admission control has an expected policy propagation delay of 60s. The caller **must** not depend on the most recent policy changes.

NOTE: The admission control has a hard limit of 1 referenced resources per call. If an operation refers to more than 1 resources, the caller must call the services.check method multiple times.

This method requires the `servicemanagement.services.check` permission on the specified service. For more information, see [Service Control API Access Control](https://cloud.google.com/service-infrastructure/docs/service-control/access-control).

### HTTP request

`POST https://servicecontrol.googleapis.com/v2/services/{serviceName}:check`

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
      "attributes": {
        object ([AttributeContext](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v2/AttributeContext))
      },
      "resources": [
        {
          object ([ResourceInfo](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v2/services/check#ResourceInfo))
        }
      ],
      "flags": string
    }  
  
Fields  
---  
`serviceConfigId` |  `string` Specifies the version of the service configuration that should be used to process the request. Must not be empty. Set this field to 'latest' to specify using the latest configuration.  
`attributes` |  `object (`[AttributeContext](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v2/AttributeContext)`)` Describes attributes about the operation being executed by the service.  
`resources[]` |  `object (`[ResourceInfo](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v2/services/check#ResourceInfo)`)` Describes the resources and the policies applied to each resource.  
`flags` |  `string` Optional. Contains a comma-separated list of flags.  
  
### Response body

Response message for the services.check method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "status": {
        object ([Status](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/Shared.Types/AuditLog#Status))
      },
      "headers": {
        string: string,
        ...
      },
      "dynamicMetadata": {
        object
      }
    }  
  
Fields  
---  
`status` |  `object (`[Status](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/Shared.Types/AuditLog#Status)`)` Operation is allowed when this field is not set. Any non-'OK' status indicates a denial; `[google.rpc.Status.details](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/Shared.Types/AuditLog#Status.FIELDS.details)` would contain additional details about the denial.  
`headers` |  `map (key: string, value: string)` Returns a set of request contexts generated from the `CheckRequest`.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`dynamicMetadata` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional response metadata that will be emitted as dynamic metadata to be consumed by the caller of ServiceController. For compatibility with the ext_authz interface.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/servicecontrol`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## ResourceInfo

Describes a resource referenced in the request.

JSON representation  
---  
      
    
    {
      "name": string,
      "type": string,
      "permission": string,
      "container": string,
      "location": string
    }  
  
Fields  
---  
`name` |  `string` The name of the resource referenced in the request.  
`type` |  `string` The resource type in the format of "{service}/{kind}".  
`permission` |  `string` The resource permission needed for this request. The format must be "{service}/{plural}.{verb}".  
`container` |  `string` Optional. The identifier of the container of this resource. For Google Cloud APIs, the resource container must be one of the following formats: - `projects/<project-id or project-number>` \- `folders/<folder-number>` \- `organizations/<organization-number>` Required for the policy enforcement on the container level (e.g. VPCSC, Location Policy check, Org Policy check).  
`location` |  `string` Optional. The location of the resource, it must be a valid zone, region or multiregion, for example: "europe-west4", "northamerica-northeast1-a". Required for location policy check.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
