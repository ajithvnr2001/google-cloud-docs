---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/
title: Service Management API \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:11:13.563622+00:00
---

# Service Management API  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  Service Management API Stay organized with collections  Save and categorize content based on your preferences. 

Google Service Management allows service producers to publish their services on Google Cloud Platform so that they can be discovered and used by service consumers.

## Service: servicemanagement.googleapis.com

The Service name `servicemanagement.googleapis.com` is needed to create RPC client stubs.

## `[google.api.servicemanagement.v1.ServiceManager](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ServiceManager)`

Methods  
---  
``[CreateService](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ServiceManager.CreateService)`` |  Creates a new managed service.  
``[CreateServiceConfig](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ServiceManager.CreateServiceConfig)`` |  Creates a new service configuration (version) for a managed service.  
``[CreateServiceRollout](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ServiceManager.CreateServiceRollout)`` |  Creates a new service configuration rollout.  
``[DeleteService](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ServiceManager.DeleteService)`` |  Deletes a managed service.  
``[DisableService](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ServiceManager.DisableService)`   
**(deprecated)**` |  Disables a `[service](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ManagedService)` for a project, so it can no longer be be used for the project.  
``[EnableService](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ServiceManager.EnableService)`   
**(deprecated)**` |  Enables a `[service](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ManagedService)` for a project, so it can be used for the project.  
``[GenerateConfigReport](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ServiceManager.GenerateConfigReport)`` |  Generates and returns a report (errors, warnings and changes from existing configurations) associated with GenerateConfigReportRequest.new_valueIf GenerateConfigReportRequest.old_value is specified, GenerateConfigReportRequest will contain a single ChangeReport based on the comparison between GenerateConfigReportRequest.new_value and GenerateConfigReportRequest.old_value.  
``[GetService](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ServiceManager.GetService)`` |  Gets a managed service.  
``[GetServiceConfig](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ServiceManager.GetServiceConfig)`` |  Gets a service configuration (version) for a managed service.  
``[GetServiceRollout](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ServiceManager.GetServiceRollout)`` |  Gets a service configuration `[rollout](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.Rollout)`.  
``[ListServiceConfigs](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ServiceManager.ListServiceConfigs)`` |  Lists the history of the service configuration for a managed service, from the newest to the oldest.  
``[ListServiceRollouts](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ServiceManager.ListServiceRollouts)`` |  Lists the history of the service configuration rollouts for a managed service, from the newest to the oldest.  
``[ListServices](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ServiceManager.ListServices)`` |  Lists managed services.  
``[SubmitConfigSource](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ServiceManager.SubmitConfigSource)`` |  Creates a new service configuration (version) for a managed service based on user-supplied configuration source files (for example: OpenAPI Specification).  
``[UndeleteService](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ServiceManager.UndeleteService)`` |  Revives a previously deleted managed service.  
  
## `[google.iam.v1.IAMPolicy](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.iam.v1#google.iam.v1.IAMPolicy)`

Methods  
---  
``[GetIamPolicy](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.iam.v1#google.iam.v1.IAMPolicy.GetIamPolicy)`` |  Gets the access control policy for a resource.  
``[SetIamPolicy](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.iam.v1#google.iam.v1.IAMPolicy.SetIamPolicy)`` |  Sets the access control policy on the specified resource.  
``[TestIamPermissions](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.iam.v1#google.iam.v1.IAMPolicy.TestIamPermissions)`` |  Returns permissions that a caller has on the specified resource.  
  
## `[google.longrunning.Operations](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.longrunning#google.longrunning.Operations)`

Methods  
---  
``[GetOperation](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.longrunning#google.longrunning.Operations.GetOperation)`` |  Gets the latest state of a long-running operation.  
``[ListOperations](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.longrunning#google.longrunning.Operations.ListOperations)`` |  Lists service operations that match the specified filter in the request.  
``[WaitOperation](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.longrunning#google.longrunning.Operations.WaitOperation)`` |  Waits until the specified long-running operation is done or reaches at most a specified timeout, returning the latest state.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
