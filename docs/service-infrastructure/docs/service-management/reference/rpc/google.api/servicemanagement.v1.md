---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1
title: Package google.api.servicemanagement.v1 \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:32.021908+00:00
---

# Package google.api.servicemanagement.v1  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  Package google.api.servicemanagement.v1 Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[ServiceManager](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ServiceManager)` (interface)
  * `[ChangeReport](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ChangeReport)` (message)
  * `[ConfigFile](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ConfigFile)` (message)
  * `[ConfigFile.FileType](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ConfigFile.FileType)` (enum)
  * `[ConfigRef](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ConfigRef)` (message)
  * `[ConfigSource](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ConfigSource)` (message)
  * `[CreateServiceConfigRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.CreateServiceConfigRequest)` (message)
  * `[CreateServiceRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.CreateServiceRequest)` (message)
  * `[CreateServiceRolloutRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.CreateServiceRolloutRequest)` (message)
  * `[DeleteServiceRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.DeleteServiceRequest)` (message)
  * `[Diagnostic](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.Diagnostic)` (message)
  * `[Diagnostic.Kind](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.Diagnostic.Kind)` (enum)
  * `[DisableServiceRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.DisableServiceRequest)` (message)
  * `[DisableServiceResponse](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.DisableServiceResponse)` (message)
  * `[EnableServiceRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.EnableServiceRequest)` (message)
  * `[EnableServiceResponse](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.EnableServiceResponse)` (message)
  * `[GenerateConfigReportRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.GenerateConfigReportRequest)` (message)
  * `[GenerateConfigReportResponse](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.GenerateConfigReportResponse)` (message)
  * `[GetServiceConfigRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.GetServiceConfigRequest)` (message)
  * `[GetServiceConfigRequest.ConfigView](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.GetServiceConfigRequest.ConfigView)` (enum)
  * `[GetServiceRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.GetServiceRequest)` (message)
  * `[GetServiceRolloutRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.GetServiceRolloutRequest)` (message)
  * `[ListServiceConfigsRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ListServiceConfigsRequest)` (message)
  * `[ListServiceConfigsResponse](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ListServiceConfigsResponse)` (message)
  * `[ListServiceRolloutsRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ListServiceRolloutsRequest)` (message)
  * `[ListServiceRolloutsResponse](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ListServiceRolloutsResponse)` (message)
  * `[ListServicesRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ListServicesRequest)` (message)
  * `[ListServicesResponse](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ListServicesResponse)` (message)
  * `[ManagedService](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ManagedService)` (message)
  * `[OperationMetadata](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.OperationMetadata)` (message)
  * `[OperationMetadata.Status](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.OperationMetadata.Status)` (enum)
  * `[OperationMetadata.Step](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.OperationMetadata.Step)` (message)
  * `[Rollout](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.Rollout)` (message)
  * `[Rollout.DeleteServiceStrategy](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.Rollout.DeleteServiceStrategy)` (message)
  * `[Rollout.RolloutStatus](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.Rollout.RolloutStatus)` (enum)
  * `[Rollout.TrafficPercentStrategy](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.Rollout.TrafficPercentStrategy)` (message)
  * `[SubmitConfigSourceRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.SubmitConfigSourceRequest)` (message)
  * `[SubmitConfigSourceResponse](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.SubmitConfigSourceResponse)` (message)
  * `[UndeleteServiceRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.UndeleteServiceRequest)` (message)
  * `[UndeleteServiceResponse](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.UndeleteServiceResponse)` (message)



## ServiceManager

[Google Service Management API](https://cloud.google.com/service-infrastructure/docs/overview)

CreateService  
---  
` rpc CreateService(`[CreateServiceRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.CreateServiceRequest)`) returns (`[Operation](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Creates a new managed service.A managed service is immutable, and is subject to mandatory 30-day data retention. You cannot move a service or recreate it within 30 days after deletion.One producer project can own no more than 500 services. For security and reliability purposes, a production service should be hosted in a dedicated producer project.Operation<response: ManagedService>

Authorization Scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/service.management`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
CreateServiceConfig  
---  
` rpc CreateServiceConfig(`[CreateServiceConfigRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.CreateServiceConfigRequest)`) returns (`[Service](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api#google.api.Service)`) ` Creates a new service configuration (version) for a managed service. This method only stores the service configuration. To roll out the service configuration to backend systems please call `[CreateServiceRollout](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ServiceManager.CreateServiceRollout)`.Only the 100 most recent service configurations and ones referenced by existing rollouts are kept for each service. The rest will be deleted eventually.

Authorization Scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/service.management`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
CreateServiceRollout  
---  
` rpc CreateServiceRollout(`[CreateServiceRolloutRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.CreateServiceRolloutRequest)`) returns (`[Operation](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Creates a new service configuration rollout. Based on rollout, the Google Service Management will roll out the service configurations to different backend services. For example, the logging configuration will be pushed to Google Cloud Logging.Please note that any previous pending and running Rollouts and associated Operations will be automatically cancelled so that the latest Rollout will not be blocked by previous Rollouts.Only the 100 most recent (in any state) and the last 10 successful (if not already part of the set of 100 most recent) rollouts are kept for each service. The rest will be deleted eventually.Operation<response: Rollout>

Authorization Scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/service.management`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
DeleteService  
---  
` rpc DeleteService(`[DeleteServiceRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.DeleteServiceRequest)`) returns (`[Operation](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Deletes a managed service. This method will change the service to the `Soft-Delete` state for 30 days. Within this period, service producers may call `[UndeleteService](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ServiceManager.UndeleteService)` to restore the service. After 30 days, the service will be permanently deleted.Operation<response: google.protobuf.Empty>

Authorization Scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/service.management`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
DisableService  
---  
Enable and Disable methods in Service Management are deprecated in favor of the [Service Usage methods](https://cloud.google.com/service-usage/docs/reference/rest/v1/services/disable).` rpc DisableService(`[DisableServiceRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.DisableServiceRequest)`) returns (`[Operation](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Disables a `[service](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ManagedService)` for a project, so it can no longer be be used for the project. It prevents accidental usage that may cause unexpected billing charges or security leaks.Operation<response: DisableServiceResponse>

Authorization Scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/service.management`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
EnableService  
---  
Enable and Disable methods in Service Management are deprecated in favor of the [Service Usage methods](https://cloud.google.com/service-usage/docs/reference/rest/v1/services/enable).` rpc EnableService(`[EnableServiceRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.EnableServiceRequest)`) returns (`[Operation](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Enables a `[service](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ManagedService)` for a project, so it can be used for the project. See [Cloud Auth Guide](https://cloud.google.com/docs/authentication) for more information.Operation<response: EnableServiceResponse>

Authorization Scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/service.management`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
GenerateConfigReport  
---  
` rpc GenerateConfigReport(`[GenerateConfigReportRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.GenerateConfigReportRequest)`) returns (`[GenerateConfigReportResponse](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.GenerateConfigReportResponse)`) ` Generates and returns a report (errors, warnings and changes from existing configurations) associated with GenerateConfigReportRequest.new_valueIf GenerateConfigReportRequest.old_value is specified, GenerateConfigReportRequest will contain a single ChangeReport based on the comparison between GenerateConfigReportRequest.new_value and GenerateConfigReportRequest.old_value. If GenerateConfigReportRequest.old_value is not specified, this method will compare GenerateConfigReportRequest.new_value with the last pushed service configuration.

Authorization Scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/service.management`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
GetService  
---  
` rpc GetService(`[GetServiceRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.GetServiceRequest)`) returns (`[ManagedService](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ManagedService)`) ` Gets a managed service. Authentication is required unless the service is public.

Authorization Scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/service.management.readonly`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/service.management`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
GetServiceConfig  
---  
` rpc GetServiceConfig(`[GetServiceConfigRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.GetServiceConfigRequest)`) returns (`[Service](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api#google.api.Service)`) ` Gets a service configuration (version) for a managed service.

Authorization Scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/service.management.readonly`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/service.management`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
GetServiceRollout  
---  
` rpc GetServiceRollout(`[GetServiceRolloutRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.GetServiceRolloutRequest)`) returns (`[Rollout](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.Rollout)`) ` Gets a service configuration `[rollout](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.Rollout)`.

Authorization Scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/service.management.readonly`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/service.management`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
ListServiceConfigs  
---  
` rpc ListServiceConfigs(`[ListServiceConfigsRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ListServiceConfigsRequest)`) returns (`[ListServiceConfigsResponse](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ListServiceConfigsResponse)`) ` Lists the history of the service configuration for a managed service, from the newest to the oldest.

Authorization Scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/service.management.readonly`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/service.management`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
ListServiceRollouts  
---  
` rpc ListServiceRollouts(`[ListServiceRolloutsRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ListServiceRolloutsRequest)`) returns (`[ListServiceRolloutsResponse](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ListServiceRolloutsResponse)`) ` Lists the history of the service configuration rollouts for a managed service, from the newest to the oldest.

Authorization Scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/service.management.readonly`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/service.management`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
ListServices  
---  
` rpc ListServices(`[ListServicesRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ListServicesRequest)`) returns (`[ListServicesResponse](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ListServicesResponse)`) ` Lists managed services.Returns all public services. For authenticated users, also returns all services the calling user has "servicemanagement.services.get" permission for.

Authorization Scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/service.management.readonly`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/service.management`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
SubmitConfigSource  
---  
` rpc SubmitConfigSource(`[SubmitConfigSourceRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.SubmitConfigSourceRequest)`) returns (`[Operation](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Creates a new service configuration (version) for a managed service based on user-supplied configuration source files (for example: OpenAPI Specification). This method stores the source configurations as well as the generated service configuration. To rollout the service configuration to other services, please call `[CreateServiceRollout](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ServiceManager.CreateServiceRollout)`.Only the 100 most recent configuration sources and ones referenced by existing service configurtions are kept for each service. The rest will be deleted eventually.Operation<response: SubmitConfigSourceResponse>

Authorization Scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/service.management`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
UndeleteService  
---  
` rpc UndeleteService(`[UndeleteServiceRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.UndeleteServiceRequest)`) returns (`[Operation](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Revives a previously deleted managed service. The method restores the service using the configuration at the time the service was deleted. The target service must exist and must have been deleted within the last 30 days.Operation<response: UndeleteServiceResponse>

Authorization Scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/service.management`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
  
## ChangeReport

Change report associated with a particular service configuration.

It contains a list of ConfigChanges based on the comparison between two service configurations.

Fields  
---  
`config_changes[]` |  ``[ConfigChange](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api#google.api.ConfigChange)`` List of changes between two service configurations. The changes will be alphabetically sorted based on the identifier of each change. A ConfigChange identifier is a dot separated path to the configuration. Example: visibility.rules[selector='LibraryService.CreateBook'].restriction  
  
## ConfigFile

Generic specification of a source configuration file

Fields  
---  
`file_path` |  `string` The file name of the configuration file (full or relative path).  
`file_contents` |  `bytes` The bytes that constitute the file.  
`file_type` |  ``[FileType](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ConfigFile.FileType)`` The type of configuration file this represents.  
  
## FileType

Enums  
---  
`FILE_TYPE_UNSPECIFIED` | Unknown file type.  
`SERVICE_CONFIG_YAML` | YAML-specification of service.  
`OPEN_API_JSON` | OpenAPI specification, serialized in JSON.  
`OPEN_API_YAML` | OpenAPI specification, serialized in YAML.  
`FILE_DESCRIPTOR_SET_PROTO` | FileDescriptorSet, generated by protoc.To generate, use protoc with imports and source info included. For an example test.proto file, the following command would put the value in a new file named out.pb.$protoc --include_imports --include_source_info test.proto -o out.pb  
`PROTO_FILE` | Uncompiled Proto file. Used for storage and display purposes only, currently server-side compilation is not supported. Should match the inputs to 'protoc' command used to generated FILE_DESCRIPTOR_SET_PROTO. A file of this type can only be included if at least one file of type FILE_DESCRIPTOR_SET_PROTO is included.  
  
## ConfigRef

Represents a service configuration with its name and id.

Fields  
---  
`name` |  `string` Resource name of a service config. It must have the following format: "services/{service name}/configs/{config id}".  
  
## ConfigSource

Represents a source file which is used to generate the service configuration defined by `google.api.Service`.

Fields  
---  
`id` |  `string` A unique ID for a specific instance of this message, typically assigned by the client for tracking purpose. If empty, the server may choose to generate one instead.  
`files[]` |  ``[ConfigFile](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ConfigFile)`` Set of source configuration files that are used to generate a service configuration (`google.api.Service`).  
  
## CreateServiceConfigRequest

Request message for CreateServiceConfig method.

Fields  
---  
`service_name` |  `string` Required. The name of the service. See the [overview](https://cloud.google.com/service-management/overview) for naming requirements. For example: `example.googleapis.com`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `serviceName`:

  * `servicemanagement.services.update`

  
`service_config` |  ``[Service](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api#google.api.Service)`` Required. The service configuration resource.  
  
## CreateServiceRequest

Request message for CreateService method.

Fields  
---  
`service` |  ``[ManagedService](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ManagedService)`` Required. Initial values for the service resource.  
  
## CreateServiceRolloutRequest

Request message for 'CreateServiceRollout'

Fields  
---  
`service_name` |  `string` Required. The name of the service. See the [overview](https://cloud.google.com/service-management/overview) for naming requirements. For example: `example.googleapis.com`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `serviceName`:

  * `servicemanagement.services.update`

  
`rollout` |  ``[Rollout](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.Rollout)`` Required. The rollout resource. The `service_name` field is output only.  
  
## DeleteServiceRequest

Request message for DeleteService method.

Fields  
---  
`service_name` |  `string` Required. The name of the service. See the [overview](https://cloud.google.com/service-management/overview) for naming requirements. For example: `example.googleapis.com`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `serviceName`:

  * `servicemanagement.services.delete`

  
  
## Diagnostic

Represents a diagnostic message (error or warning)

Fields  
---  
`location` |  `string` File name and line number of the error or warning.  
`kind` |  ``[Kind](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.Diagnostic.Kind)`` The kind of diagnostic information provided.  
`message` |  `string` Message describing the error or warning.  
  
## Kind

The kind of diagnostic information possible.

Enums  
---  
`WARNING` | Warnings and errors  
`ERROR` | Only errors  
  
## DisableServiceRequest

Request message for DisableService method.

Fields  
---  
`service_name` |  `string` Required. Name of the service to disable. Specifying an unknown service name will cause the request to fail. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `serviceName`:

  * `servicemanagement.services.bind`

  
`consumer_id` |  `string` Required. The identity of consumer resource which service disablement will be applied to.The Google Service Management implementation accepts the following forms: - "project:"Note: this is made compatible with google.api.servicecontrol.v1.Operation.consumer_id. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `consumerId`:

  * `servicemanagement.services.bind`

  
  
## DisableServiceResponse

Operation payload for DisableService method.

## EnableServiceRequest

Request message for EnableService method.

Fields  
---  
`service_name` |  `string` Required. Name of the service to enable. Specifying an unknown service name will cause the request to fail. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `serviceName`:

  * `servicemanagement.services.bind`

  
`consumer_id` |  `string` Required. The identity of consumer resource which service enablement will be applied to.The Google Service Management implementation accepts the following forms: - "project:"Note: this is made compatible with google.api.servicecontrol.v1.Operation.consumer_id. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `consumerId`:

  * `servicemanagement.services.bind`

  
  
## EnableServiceResponse

Operation payload for EnableService method.

## GenerateConfigReportRequest

Request message for GenerateConfigReport method.

Fields  
---  
`new_config` |  ``[Any](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Any)`` Required. Service configuration for which we want to generate the report. For this version of API, the supported types are `[google.api.servicemanagement.v1.ConfigRef](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ConfigRef)`, `[google.api.servicemanagement.v1.ConfigSource](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ConfigSource)`, and `[google.api.Service](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api#google.api.Service)`  
`old_config` |  ``[Any](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Any)`` Optional. Service configuration against which the comparison will be done. For this version of API, the supported types are `[google.api.servicemanagement.v1.ConfigRef](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ConfigRef)`, `[google.api.servicemanagement.v1.ConfigSource](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ConfigSource)`, and `[google.api.Service](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api#google.api.Service)`  
  
## GenerateConfigReportResponse

Response message for GenerateConfigReport method.

Fields  
---  
`service_name` |  `string` Name of the service this report belongs to.  
`id` |  `string` ID of the service configuration this report belongs to.  
`change_reports[]` |  ``[ChangeReport](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ChangeReport)`` list of ChangeReport, each corresponding to comparison between two service configurations.  
`diagnostics[]` |  ``[Diagnostic](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.Diagnostic)`` Errors / Linter warnings associated with the service definition this report belongs to.  
  
## GetServiceConfigRequest

Request message for GetServiceConfig method.

Fields  
---  
`service_name` |  `string` Required. The name of the service. See the [overview](https://cloud.google.com/service-management/overview) for naming requirements. For example: `example.googleapis.com`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `serviceName`:

  * `servicemanagement.services.get`

  
`config_id` |  `string` Required. The id of the service configuration resource.This field must be specified for the server to return all fields, including `SourceInfo`.  
`view` |  ``[ConfigView](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.GetServiceConfigRequest.ConfigView)`` Specifies which parts of the Service Config should be returned in the response.  
  
## ConfigView

Enums  
---  
`BASIC` | Server response includes all fields except SourceInfo.  
`FULL` | Server response includes all fields including SourceInfo. SourceFiles are of type 'google.api.servicemanagement.v1.ConfigFile' and are only available for configs created using the SubmitConfigSource method.  
  
## GetServiceRequest

Request message for `GetService` method.

Fields  
---  
`service_name` |  `string` Required. The name of the service. See the `ServiceManager` overview for naming requirements. For example: `example.googleapis.com`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `serviceName`:

  * `servicemanagement.services.get`

  
  
## GetServiceRolloutRequest

Request message for GetServiceRollout method.

Fields  
---  
`service_name` |  `string` Required. The name of the service. See the [overview](https://cloud.google.com/service-management/overview) for naming requirements. For example: `example.googleapis.com`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `serviceName`:

  * `servicemanagement.services.get`

  
`rollout_id` |  `string` Required. The id of the rollout resource.  
  
## ListServiceConfigsRequest

Request message for ListServiceConfigs method.

Fields  
---  
`service_name` |  `string` Required. The name of the service. See the [overview](https://cloud.google.com/service-management/overview) for naming requirements. For example: `example.googleapis.com`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `serviceName`:

  * `servicemanagement.services.get`

  
`page_token` |  `string` The token of the page to retrieve.  
`page_size` |  `int32` The max number of items to include in the response list. Page size is 50 if not specified. Maximum value is 100.  
  
## ListServiceConfigsResponse

Response message for ListServiceConfigs method.

Fields  
---  
`service_configs[]` |  ``[Service](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api#google.api.Service)`` The list of service configuration resources.  
`next_page_token` |  `string` The token of the next page of results.  
  
## ListServiceRolloutsRequest

Request message for 'ListServiceRollouts'

Fields  
---  
`service_name` |  `string` Required. The name of the service. See the [overview](https://cloud.google.com/service-management/overview) for naming requirements. For example: `example.googleapis.com`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `serviceName`:

  * `servicemanagement.services.get`

  
`page_token` |  `string` The token of the page to retrieve.  
`page_size` |  `int32` The max number of items to include in the response list. Page size is 50 if not specified. Maximum value is 100.  
`filter` |  `string` Required. Use `filter` to return subset of rollouts. The following filters are supported:\-- By `[status](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.Rollout.RolloutStatus)`. For example, `filter='status=SUCCESS'`\-- By [strategy] [google.api.servicemanagement.v1.Rollout.strategy]. For example, `filter='strategy=TrafficPercentStrategy'`  
  
## ListServiceRolloutsResponse

Response message for ListServiceRollouts method.

Fields  
---  
`rollouts[]` |  ``[Rollout](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.Rollout)`` The list of rollout resources.  
`next_page_token` |  `string` The token of the next page of results.  
  
## ListServicesRequest

Request message for `ListServices` method.

Fields  
---  
`producer_project_id` |  `string` Include services produced by the specified project.  
`page_size` |  `int32` The max number of items to include in the response list. Page size is 50 if not specified. Maximum value is 500.  
`page_token` |  `string` Token identifying which result to start with; returned by a previous list call.  
`consumer_id  
**(deprecated)**` |  `string` Listing services by consumer_id is deprecated. To list the services in use by a consumer, please call Service Usage ListServices method with the filter state:ENABLED.Include services consumed by the specified consumer.The Google Service Management implementation accepts the following forms: - project:  
  
## ListServicesResponse

Response message for `ListServices` method.

Fields  
---  
`services[]` |  ``[ManagedService](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ManagedService)`` The returned services will only have the name field set.  
`next_page_token` |  `string` Token that can be passed to `ListServices` to resume a paginated query.  
  
## ManagedService

The full representation of a Service that is managed by Google Service Management.

Fields  
---  
`service_name` |  `string` The name of the service. See the [overview](https://cloud.google.com/service-infrastructure/docs/overview) for naming requirements.  
`producer_project_id` |  `string` ID of the project that produces and owns this service.  
  
## OperationMetadata

The metadata associated with a long running operation resource.

Fields  
---  
`resource_names[]` |  `string` The full name of the resources that this operation is directly associated with.  
`steps[]` |  ``[Step](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.OperationMetadata.Step)`` Detailed status information for each step. The order is undetermined.  
`progress_percentage` |  `int32` Percentage of completion of this operation, ranging from 0 to 100.  
`start_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` The start time of the operation.  
  
## Status

Code describes the status of the operation (or one of its steps).

Enums  
---  
`STATUS_UNSPECIFIED` | Unspecifed code.  
`DONE` | The operation or step has completed without errors.  
`NOT_STARTED` | The operation or step has not started yet.  
`IN_PROGRESS` | The operation or step is in progress.  
`FAILED` | The operation or step has completed with errors. If the operation is rollbackable, the rollback completed with errors too.  
`CANCELLED` | The operation or step has completed with cancellation.  
  
## Step

Represents the status of one operation step.

Fields  
---  
`description` |  `string` The short description of the step.  
`status` |  ``[Status](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.OperationMetadata.Status)`` The status code.  
  
## Rollout

A rollout resource that defines how service configuration versions are pushed to control plane systems. Typically, you create a new version of the service config, and then create a Rollout to push the service config.

Fields  
---  
`rollout_id` |  `string` Optional. Unique identifier of this Rollout. Must be no longer than 63 characters and only lower case letters, digits, '.', '_' and '-' are allowed.If not specified by client, the server will generate one. The generated id will have the form of , where "date" is the create date in ISO 8601 format. "revision number" is a monotonically increasing positive number that is reset every day for each service. An example of the generated rollout_id is '2016-02-16r1'  
`create_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` Creation time of the rollout. Readonly.  
`created_by` |  `string` The user who created the Rollout. Readonly.  
`status` |  ``[RolloutStatus](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.Rollout.RolloutStatus)`` The status of this rollout. Readonly. In case of a failed rollout, the system will automatically rollback to the current Rollout version. Readonly.  
`service_name` |  `string` The name of the service associated with this Rollout.  
Union field `strategy`. Strategy that defines which versions of service configurations should be pushed and how they should be used at runtime. `strategy` can be only one of the following:  
`traffic_percent_strategy` |  ``[TrafficPercentStrategy](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.Rollout.TrafficPercentStrategy)`` Google Service Control selects service configurations based on traffic percentage.  
`delete_service_strategy` |  ``[DeleteServiceStrategy](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.Rollout.DeleteServiceStrategy)`` The strategy associated with a rollout to delete a `ManagedService`. Readonly.  
  
## DeleteServiceStrategy

Strategy used to delete a service. This strategy is a placeholder only used by the system generated rollout to delete a service.

## RolloutStatus

Status of a Rollout.

Enums  
---  
`ROLLOUT_STATUS_UNSPECIFIED` | No status specified.  
`IN_PROGRESS` | The Rollout is in progress.  
`SUCCESS` | The Rollout has completed successfully.  
`CANCELLED` | The Rollout has been cancelled. This can happen if you have overlapping Rollout pushes, and the previous ones will be cancelled.  
`FAILED` | The Rollout has failed and the rollback attempt has failed too.  
`PENDING` | The Rollout has not started yet and is pending for execution.  
`FAILED_ROLLED_BACK` | The Rollout has failed and rolled back to the previous successful Rollout.  
  
## TrafficPercentStrategy

Strategy that specifies how clients of Google Service Controller want to send traffic to use different config versions. This is generally used by API proxy to split traffic based on your configured percentage for each config version.

One example of how to gradually rollout a new service configuration using this strategy: Day 1
    
    
    Rollout {
      id: "example.googleapis.com/rollout_20160206"
      traffic_percent_strategy {
        percentages: {
          "example.googleapis.com/20160201": 70.00
          "example.googleapis.com/20160206": 30.00
        }
      }
    }
    

Day 2
    
    
    Rollout {
      id: "example.googleapis.com/rollout_20160207"
      traffic_percent_strategy: {
        percentages: {
          "example.googleapis.com/20160206": 100.00
        }
      }
    }
    

Fields  
---  
`percentages` |  `map<string, double>` Maps service configuration IDs to their corresponding traffic percentage. Key is the service configuration ID, Value is the traffic percentage which must be greater than 0.0 and the sum must equal to 100.0.  
  
## SubmitConfigSourceRequest

Request message for SubmitConfigSource method.

Fields  
---  
`service_name` |  `string` Required. The name of the service. See the [overview](https://cloud.google.com/service-management/overview) for naming requirements. For example: `example.googleapis.com`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `serviceName`:

  * `servicemanagement.services.update`

  
`config_source` |  ``[ConfigSource](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ConfigSource)`` Required. The source configuration for the service.  
`validate_only` |  `bool` Optional. If set, this will result in the generation of a `google.api.Service` configuration based on the `ConfigSource` provided, but the generated config and the sources will NOT be persisted.  
  
## SubmitConfigSourceResponse

Response message for SubmitConfigSource method.

Fields  
---  
`service_config` |  ``[Service](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api#google.api.Service)`` The generated service configuration.  
  
## UndeleteServiceRequest

Request message for UndeleteService method.

Fields  
---  
`service_name` |  `string` Required. The name of the service. See the [overview](https://cloud.google.com/service-management/overview) for naming requirements. For example: `example.googleapis.com`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `serviceName`:

  * `servicemanagement.services.delete`

  
  
## UndeleteServiceResponse

Response message for UndeleteService method.

Fields  
---  
`service` |  ``[ManagedService](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rpc/google.api/servicemanagement.v1#google.api.servicemanagement.v1.ManagedService)`` Revived service resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
