---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v2
title: Package google.api.servicecontrol.v2 \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:34.546682+00:00
---

# Package google.api.servicecontrol.v2  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v2

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  Package google.api.servicecontrol.v2 Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[ServiceController](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v2#google.api.servicecontrol.v2.ServiceController)` (interface)
  * `[CheckRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v2#google.api.servicecontrol.v2.CheckRequest)` (message)
  * `[CheckResponse](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v2#google.api.servicecontrol.v2.CheckResponse)` (message)
  * `[ReportRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v2#google.api.servicecontrol.v2.ReportRequest)` (message)
  * `[ReportResponse](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v2#google.api.servicecontrol.v2.ReportResponse)` (message)
  * `[ResourceInfo](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v2#google.api.servicecontrol.v2.ResourceInfo)` (message)



## ServiceController

[Service Control API v2](https://cloud.google.com/service-infrastructure/docs/service-control/access-control)

This API provides admission control and telemetry reporting for services that are integrated with [Service Infrastructure](https://cloud.google.com/service-infrastructure).

Check  
---  
` rpc Check(`[CheckRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v2#google.api.servicecontrol.v2.CheckRequest)`) returns (`[CheckResponse](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v2#google.api.servicecontrol.v2.CheckResponse)`) ` This method provides admission control for services that are integrated with [Service Infrastructure](https://cloud.google.com/service-infrastructure). It checks whether an operation should be allowed based on the service configuration and relevant policies. It must be called before the operation is executed. For more information, see [Admission Control](https://cloud.google.com/service-infrastructure/docs/admission-control).NOTE: The admission control has an expected policy propagation delay of 60s. The caller **must** not depend on the most recent policy changes.NOTE: The admission control has a hard limit of 1 referenced resources per call. If an operation refers to more than 1 resources, the caller must call the Check method multiple times.This method requires the `servicemanagement.services.check` permission on the specified service. For more information, see [Service Control API Access Control](https://cloud.google.com/service-infrastructure/docs/service-control/access-control).

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/servicecontrol`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
Report  
---  
` rpc Report(`[ReportRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v2#google.api.servicecontrol.v2.ReportRequest)`) returns (`[ReportResponse](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v2#google.api.servicecontrol.v2.ReportResponse)`) ` This method provides telemetry reporting for services that are integrated with [Service Infrastructure](https://cloud.google.com/service-infrastructure). It reports a list of operations that have occurred on a service. It must be called after the operations have been executed. For more information, see [Telemetry Reporting](https://cloud.google.com/service-infrastructure/docs/telemetry-reporting).NOTE: The telemetry reporting has a hard limit of 1000 operations and 1MB per Report call. It is recommended to have no more than 100 operations per call.This method requires the `servicemanagement.services.report` permission on the specified service. For more information, see [Service Control API Access Control](https://cloud.google.com/service-infrastructure/docs/service-control/access-control).

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/servicecontrol`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
  
## CheckRequest

Request message for the Check method.

Fields  
---  
`service_name` |  `string` The service name as specified in its service configuration. For example, `"pubsub.googleapis.com"`.See [google.api.Service](https://cloud.google.com/service-management/reference/rpc/google.api#google.api.Service) for the definition of a service name.  
`service_config_id` |  `string` Specifies the version of the service configuration that should be used to process the request. Must not be empty. Set this field to 'latest' to specify using the latest configuration.  
`attributes` |  `[AttributeContext](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.rpc/context#google.rpc.context.AttributeContext)` Describes attributes about the operation being executed by the service.  
`resources[]` |  `[ResourceInfo](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api/servicecontrol.v2#google.api.servicecontrol.v2.ResourceInfo)` Describes the resources and the policies applied to each resource.  
`flags` |  `string` Optional. Contains a comma-separated list of flags.  
  
## CheckResponse

Response message for the Check method.

Fields  
---  
`status` |  `[Status](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.rpc#google.rpc.Status)` Operation is allowed when this field is not set. Any non-'OK' status indicates a denial; `[google.rpc.Status.details](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.rpc#google.rpc.Status.FIELDS.repeated.google.protobuf.Any.google.rpc.Status.details)` would contain additional details about the denial.  
`headers` |  `map<string, string>` Returns a set of request contexts generated from the `CheckRequest`.  
`dynamic_metadata` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Optional response metadata that will be emitted as dynamic metadata to be consumed by the caller of ServiceController. For compatibility with the ext_authz interface.  
  
## ReportRequest

Request message for the Report method.

Fields  
---  
`service_name` |  `string` The service name as specified in its service configuration. For example, `"pubsub.googleapis.com"`.See [google.api.Service](https://cloud.google.com/service-management/reference/rpc/google.api#google.api.Service) for the definition of a service name.  
`service_config_id` |  `string` Specifies the version of the service configuration that should be used to process the request. Must not be empty. Set this field to 'latest' to specify using the latest configuration.  
`operations[]` |  `[AttributeContext](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.rpc/context#google.rpc.context.AttributeContext)` Describes the list of operations to be reported. Each operation is represented as an AttributeContext, and contains all attributes around an API access.  
  
## ReportResponse

Response message for the Report method.

Fields  
---  
`extensions` |  `[Any](https://protobuf.dev/reference/protobuf/google.protobuf/#any)` The extension field to store serialized OTel responses. e.g. ExportLogsServiceResponse, ExportMetricsServiceResponse.  
  
## ResourceInfo

Describes a resource referenced in the request.

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
