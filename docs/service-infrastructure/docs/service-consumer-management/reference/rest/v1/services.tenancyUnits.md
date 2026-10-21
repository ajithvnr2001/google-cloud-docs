---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits
title: REST Resource: services.tenancyUnits \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:41.425032+00:00
---

# REST Resource: services.tenancyUnits  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure/docs)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  REST Resource: services.tenancyUnits Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: TenancyUnit
    * JSON representation
  * TenantResource
    * JSON representation
  * Status
  * Methods



## Resource: TenancyUnit

Representation of a tenancy unit.

JSON representation  
---  
      
    
    {
      "name": string,
      "service": string,
      "consumer": string,
      "createTime": string,
      "tenantResources": [
        {
          object ([TenantResource](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits#TenantResource))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Globally unique identifier of this tenancy unit "services/{service}/{collection id}/{resource id}/tenancyUnits/{unit}"  
`service` |  `string` Output only. Google Cloud API name of the managed service owning this tenancy unit. For example 'serviceconsumermanagement.googleapis.com'.  
`consumer` |  `string` Cloud resource name of the consumer of this service. For example 'projects/123456'.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`createTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` The time this tenancy unit was created.A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: `"2014-10-02T15:01:23.045123456Z"`.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`tenantResources[]` |  `object (`[TenantResource](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits#TenantResource)`)` Resources constituting the tenancy unit. There can be at most 512 tenant resources in a tenancy unit.  
  
## TenantResource

Resource constituting the TenancyUnit.

JSON representation  
---  
      
    
    {
      "tag": string,
      "resource": string,
      "status": enum ([Status](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits#Status))
    }  
  
Fields  
---  
`tag` |  `string` Unique per single tenancy unit.  
`resource` |  `string` Identifier of the tenant resource. For cloud projects, it is in the form 'projects/{number}'. For example 'projects/123456'.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`status` |  `enum (`[Status](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits#Status)`)` Status of tenant resource.  
  
## Status

The status of tenant resources.

Enums  
---  
`STATUS_UNSPECIFIED` | Unspecified status is the default unset value.  
`PENDING_CREATE` | Creation of the tenant resource is ongoing.  
`ACTIVE` | Active resource.  
`PENDING_DELETE` | Deletion of the resource is ongoing.  
`FAILED` | Tenant resource creation or deletion has failed.  
`DELETED` | Tenant resource has been deleted.  
  
## Methods  
  
---  
  
### `[addProject](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/addProject)`

|  Add a new tenant project to the tenancy unit.  
  
### `[applyProjectConfig](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/applyProjectConfig)`

|  Apply a configuration to an existing tenant project.  
  
### `[attachProject](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/attachProject)`

|  Attach an existing project to the tenancy unit as a new tenant resource.  
  
### `[create](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/create)`

|  Creates a tenancy unit with no tenant resources.  
  
### `[delete](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/delete)`

|  Delete a tenancy unit.  
  
### `[deleteProject](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/deleteProject)`

|  Deletes the specified project resource identified by a tenant resource tag.  
  
### `[list](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/list)`

|  Find the tenancy unit for a managed service and service consumer.  
  
### `[removeProject](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/removeProject)`

|  Removes the specified project resource identified by a tenant resource tag.  
  
### `[undeleteProject](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/services.tenancyUnits/undeleteProject)`

|  Attempts to undelete a previously deleted tenant project.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
