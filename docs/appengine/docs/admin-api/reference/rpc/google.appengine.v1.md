---
url: https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1
title: Package google.appengine.v1 \u00a0|\u00a0 App Engine Admin API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:04:06.044250+00:00
---

# Package google.appengine.v1  |  App Engine Admin API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1

  * [ Home ](https://docs.cloud.google.com/)
  * [ App Engine ](https://docs.cloud.google.com/appengine)
  * [ Admin API ](https://docs.cloud.google.com/appengine/docs/admin-api)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/admin-api/apis)



Send feedback 

#  Package google.appengine.v1 Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[Applications](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Applications)` (interface)
  * `[AuthorizedCertificates](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.AuthorizedCertificates)` (interface)
  * `[AuthorizedDomains](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.AuthorizedDomains)` (interface)
  * `[DomainMappings](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.DomainMappings)` (interface)
  * `[Firewall](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Firewall)` (interface)
  * `[Instances](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Instances)` (interface)
  * `[Services](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Services)` (interface)
  * `[Versions](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Versions)` (interface)
  * `[ApiConfigHandler](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ApiConfigHandler)` (message)
  * `[ApiEndpointHandler](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ApiEndpointHandler)` (message)
  * `[Application](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Application)` (message)
  * `[Application.DatabaseType](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Application.DatabaseType)` (enum)
  * `[Application.FeatureSettings](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Application.FeatureSettings)` (message)
  * `[Application.IdentityAwareProxy](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Application.IdentityAwareProxy)` (message)
  * `[Application.ServingStatus](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Application.ServingStatus)` (enum)
  * `[AuthFailAction](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.AuthFailAction)` (enum)
  * `[AuthorizedCertificate](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.AuthorizedCertificate)` (message)
  * `[AuthorizedCertificateView](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.AuthorizedCertificateView)` (enum)
  * `[AuthorizedDomain](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.AuthorizedDomain)` (message)
  * `[AutomaticScaling](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.AutomaticScaling)` (message)
  * `[BasicScaling](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.BasicScaling)` (message)
  * `[BatchUpdateIngressRulesRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.BatchUpdateIngressRulesRequest)` (message)
  * `[BatchUpdateIngressRulesResponse](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.BatchUpdateIngressRulesResponse)` (message)
  * `[CertificateRawData](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.CertificateRawData)` (message)
  * `[CloudBuildOptions](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.CloudBuildOptions)` (message)
  * `[ContainerInfo](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ContainerInfo)` (message)
  * `[CpuUtilization](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.CpuUtilization)` (message)
  * `[CreateApplicationRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.CreateApplicationRequest)` (message)
  * `[CreateAuthorizedCertificateRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.CreateAuthorizedCertificateRequest)` (message)
  * `[CreateDomainMappingRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.CreateDomainMappingRequest)` (message)
  * `[CreateIngressRuleRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.CreateIngressRuleRequest)` (message)
  * `[CreateVersionMetadataV1](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.CreateVersionMetadataV1)` (message)
  * `[CreateVersionRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.CreateVersionRequest)` (message)
  * `[DebugInstanceRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.DebugInstanceRequest)` (message)
  * `[DeleteAuthorizedCertificateRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.DeleteAuthorizedCertificateRequest)` (message)
  * `[DeleteDomainMappingRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.DeleteDomainMappingRequest)` (message)
  * `[DeleteIngressRuleRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.DeleteIngressRuleRequest)` (message)
  * `[DeleteInstanceRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.DeleteInstanceRequest)` (message)
  * `[DeleteServiceRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.DeleteServiceRequest)` (message)
  * `[DeleteVersionRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.DeleteVersionRequest)` (message)
  * `[Deployment](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Deployment)` (message)
  * `[DiskUtilization](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.DiskUtilization)` (message)
  * `[DomainMapping](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.DomainMapping)` (message)
  * `[DomainOverrideStrategy](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.DomainOverrideStrategy)` (enum)
  * `[EndpointsApiService](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.EndpointsApiService)` (message)
  * `[EndpointsApiService.RolloutStrategy](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.EndpointsApiService.RolloutStrategy)` (enum)
  * `[Entrypoint](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Entrypoint)` (message)
  * `[ErrorHandler](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ErrorHandler)` (message)
  * `[ErrorHandler.ErrorCode](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ErrorHandler.ErrorCode)` (enum)
  * `[FileInfo](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.FileInfo)` (message)
  * `[FirewallRule](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.FirewallRule)` (message)
  * `[FirewallRule.Action](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.FirewallRule.Action)` (enum)
  * `[FlexibleRuntimeSettings](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.FlexibleRuntimeSettings)` (message)
  * `[GetApplicationRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.GetApplicationRequest)` (message)
  * `[GetAuthorizedCertificateRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.GetAuthorizedCertificateRequest)` (message)
  * `[GetDomainMappingRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.GetDomainMappingRequest)` (message)
  * `[GetIngressRuleRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.GetIngressRuleRequest)` (message)
  * `[GetInstanceRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.GetInstanceRequest)` (message)
  * `[GetServiceRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.GetServiceRequest)` (message)
  * `[GetVersionRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.GetVersionRequest)` (message)
  * `[HealthCheck](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.HealthCheck)` (message)
  * `[InboundServiceType](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.InboundServiceType)` (enum)
  * `[Instance](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Instance)` (message)
  * `[Instance.Availability](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Instance.Availability)` (enum)
  * `[Instance.Liveness](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Instance.Liveness)` (message)
  * `[Instance.Liveness.LivenessState](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Instance.Liveness.LivenessState)` (enum)
  * `[Library](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Library)` (message)
  * `[ListAuthorizedCertificatesRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ListAuthorizedCertificatesRequest)` (message)
  * `[ListAuthorizedCertificatesResponse](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ListAuthorizedCertificatesResponse)` (message)
  * `[ListAuthorizedDomainsRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ListAuthorizedDomainsRequest)` (message)
  * `[ListAuthorizedDomainsResponse](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ListAuthorizedDomainsResponse)` (message)
  * `[ListDomainMappingsRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ListDomainMappingsRequest)` (message)
  * `[ListDomainMappingsResponse](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ListDomainMappingsResponse)` (message)
  * `[ListIngressRulesRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ListIngressRulesRequest)` (message)
  * `[ListIngressRulesResponse](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ListIngressRulesResponse)` (message)
  * `[ListInstancesRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ListInstancesRequest)` (message)
  * `[ListInstancesResponse](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ListInstancesResponse)` (message)
  * `[ListServicesRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ListServicesRequest)` (message)
  * `[ListServicesResponse](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ListServicesResponse)` (message)
  * `[ListVersionsRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ListVersionsRequest)` (message)
  * `[ListVersionsResponse](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ListVersionsResponse)` (message)
  * `[LivenessCheck](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.LivenessCheck)` (message)
  * `[LocationMetadata](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.LocationMetadata)` (message)
  * `[LoginRequirement](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.LoginRequirement)` (enum)
  * `[ManagedCertificate](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ManagedCertificate)` (message)
  * `[ManagementStatus](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ManagementStatus)` (enum)
  * `[ManualScaling](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ManualScaling)` (message)
  * `[Network](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Network)` (message)
  * `[NetworkSettings](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.NetworkSettings)` (message)
  * `[NetworkSettings.IngressTrafficAllowed](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.NetworkSettings.IngressTrafficAllowed)` (enum)
  * `[NetworkUtilization](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.NetworkUtilization)` (message)
  * `[OperationMetadataV1](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.OperationMetadataV1)` (message)
  * `[ReadinessCheck](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ReadinessCheck)` (message)
  * `[RepairApplicationRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.RepairApplicationRequest)` (message)
  * `[RequestUtilization](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.RequestUtilization)` (message)
  * `[ResourceRecord](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ResourceRecord)` (message)
  * `[ResourceRecord.RecordType](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ResourceRecord.RecordType)` (enum)
  * `[Resources](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Resources)` (message)
  * `[ScriptHandler](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ScriptHandler)` (message)
  * `[SecurityLevel](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.SecurityLevel)` (enum)
  * `[Service](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Service)` (message)
  * `[ServingStatus](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ServingStatus)` (enum)
  * `[SslSettings](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.SslSettings)` (message)
  * `[SslSettings.SslManagementType](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.SslSettings.SslManagementType)` (enum)
  * `[StandardSchedulerSettings](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.StandardSchedulerSettings)` (message)
  * `[StaticFilesHandler](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.StaticFilesHandler)` (message)
  * `[TrafficSplit](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.TrafficSplit)` (message)
  * `[TrafficSplit.ShardBy](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.TrafficSplit.ShardBy)` (enum)
  * `[UpdateApplicationRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.UpdateApplicationRequest)` (message)
  * `[UpdateAuthorizedCertificateRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.UpdateAuthorizedCertificateRequest)` (message)
  * `[UpdateDomainMappingRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.UpdateDomainMappingRequest)` (message)
  * `[UpdateIngressRuleRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.UpdateIngressRuleRequest)` (message)
  * `[UpdateServiceRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.UpdateServiceRequest)` (message)
  * `[UpdateVersionRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.UpdateVersionRequest)` (message)
  * `[UrlDispatchRule](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.UrlDispatchRule)` (message)
  * `[UrlMap](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.UrlMap)` (message)
  * `[UrlMap.RedirectHttpResponseCode](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.UrlMap.RedirectHttpResponseCode)` (enum)
  * `[Version](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Version)` (message)
  * `[VersionView](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.VersionView)` (enum)
  * `[Volume](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Volume)` (message)
  * `[VpcAccessConnector](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.VpcAccessConnector)` (message)
  * `[VpcAccessConnector.EgressSetting](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.VpcAccessConnector.EgressSetting)` (enum)
  * `[ZipInfo](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ZipInfo)` (message)



## Applications

Manages App Engine applications.

CreateApplication  
---  
` rpc CreateApplication(`[CreateApplicationRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.CreateApplicationRequest)`) returns (`[Operation](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Creates an App Engine application for a Google Cloud Platform project. Required fields:

  * `id` \- The ID of the target Cloud Platform project.
  * _location_ \- The [region](https://cloud.google.com/appengine/docs/locations) where you want the App Engine application located.

For more information about App Engine applications, see [Managing Projects, Applications, and Billing](https://cloud.google.com/appengine/docs/standard/python/console/).

Authorization Scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
GetApplication  
---  
` rpc GetApplication(`[GetApplicationRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.GetApplicationRequest)`) returns (`[Application](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Application)`) ` Gets information about an application.

Authorization Scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/appengine.admin`
  * ` https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/cloud-platform.read-only`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
RepairApplication  
---  
` rpc RepairApplication(`[RepairApplicationRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.RepairApplicationRequest)`) returns (`[Operation](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Recreates the required App Engine features for the specified App Engine application, for example a Cloud Storage bucket or App Engine service account. Use this method if you receive an error message about a missing feature, for example, _Error retrieving the App Engine service account_. If you have deleted your App Engine service account, this will not be able to recreate it. Instead, you should attempt to use the IAM undelete API if possible at [https://cloud.google.com/iam/reference/rest/v1/projects.serviceAccounts/undelete?apix_params=%7B"name"%3A"projects%2F-%2FserviceAccounts%2Funique_id"%2C"resource"%3A%7B%7D%7D](https://cloud.google.com/iam/reference/rest/v1/projects.serviceAccounts/undelete?apix_params=%7B) . If the deletion was recent, the numeric ID can be found in the Cloud Console Activity Log.

Authorization Scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
UpdateApplication  
---  
` rpc UpdateApplication(`[UpdateApplicationRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.UpdateApplicationRequest)`) returns (`[Operation](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Updates the specified Application resource. You can update the following fields:

  * `auth_domain` \- Google authentication domain for controlling user access to the application.
  * `default_cookie_expiration` \- Cookie expiration policy for the application.
  * `iap` \- Identity-Aware Proxy properties for the application.



Authorization Scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
  
## AuthorizedCertificates

Manages SSL certificates a user is authorized to administer. A user can administer any SSL certificates applicable to their authorized domains.

CreateAuthorizedCertificate  
---  
` rpc CreateAuthorizedCertificate(`[CreateAuthorizedCertificateRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.CreateAuthorizedCertificateRequest)`) returns (`[AuthorizedCertificate](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.AuthorizedCertificate)`) ` Uploads the specified SSL certificate.

Authorization Scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
DeleteAuthorizedCertificate  
---  
` rpc DeleteAuthorizedCertificate(`[DeleteAuthorizedCertificateRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.DeleteAuthorizedCertificateRequest)`) returns (`[Empty](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Empty)`) ` Deletes the specified SSL certificate.

Authorization Scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
GetAuthorizedCertificate  
---  
` rpc GetAuthorizedCertificate(`[GetAuthorizedCertificateRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.GetAuthorizedCertificateRequest)`) returns (`[AuthorizedCertificate](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.AuthorizedCertificate)`) ` Gets the specified SSL certificate.

Authorization Scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/appengine.admin`
  * ` https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/cloud-platform.read-only`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
ListAuthorizedCertificates  
---  
` rpc ListAuthorizedCertificates(`[ListAuthorizedCertificatesRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ListAuthorizedCertificatesRequest)`) returns (`[ListAuthorizedCertificatesResponse](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ListAuthorizedCertificatesResponse)`) ` Lists all SSL certificates the user is authorized to administer.

Authorization Scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/appengine.admin`
  * ` https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/cloud-platform.read-only`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
UpdateAuthorizedCertificate  
---  
` rpc UpdateAuthorizedCertificate(`[UpdateAuthorizedCertificateRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.UpdateAuthorizedCertificateRequest)`) returns (`[AuthorizedCertificate](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.AuthorizedCertificate)`) ` Updates the specified SSL certificate. To renew a certificate and maintain its existing domain mappings, update `certificate_data` with a new certificate. The new certificate must be applicable to the same domains as the original certificate. The certificate `display_name` may also be updated.

Authorization Scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
  
## AuthorizedDomains

Manages domains a user is authorized to administer. To authorize use of a domain, verify ownership via [Search Console](https://search.google.com/search-console/welcome).

ListAuthorizedDomains  
---  
` rpc ListAuthorizedDomains(`[ListAuthorizedDomainsRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ListAuthorizedDomainsRequest)`) returns (`[ListAuthorizedDomainsResponse](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ListAuthorizedDomainsResponse)`) ` Lists all domains the user is authorized to administer.

Authorization Scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/appengine.admin`
  * ` https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/cloud-platform.read-only`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
  
## DomainMappings

Manages domains serving an application.

CreateDomainMapping  
---  
` rpc CreateDomainMapping(`[CreateDomainMappingRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.CreateDomainMappingRequest)`) returns (`[Operation](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Maps a domain to an application. A user must be authorized to administer a domain in order to map it to an application. For a list of available authorized domains, see [`AuthorizedDomains.ListAuthorizedDomains`](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1).

Authorization Scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
DeleteDomainMapping  
---  
` rpc DeleteDomainMapping(`[DeleteDomainMappingRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.DeleteDomainMappingRequest)`) returns (`[Operation](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Deletes the specified domain mapping. A user must be authorized to administer the associated domain in order to delete a `DomainMapping` resource.

Authorization Scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
GetDomainMapping  
---  
` rpc GetDomainMapping(`[GetDomainMappingRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.GetDomainMappingRequest)`) returns (`[DomainMapping](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.DomainMapping)`) ` Gets the specified domain mapping.

Authorization Scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/appengine.admin`
  * ` https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/cloud-platform.read-only`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
ListDomainMappings  
---  
` rpc ListDomainMappings(`[ListDomainMappingsRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ListDomainMappingsRequest)`) returns (`[ListDomainMappingsResponse](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ListDomainMappingsResponse)`) ` Lists the domain mappings on an application.

Authorization Scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/appengine.admin`
  * ` https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/cloud-platform.read-only`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
UpdateDomainMapping  
---  
` rpc UpdateDomainMapping(`[UpdateDomainMappingRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.UpdateDomainMappingRequest)`) returns (`[Operation](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Updates the specified domain mapping. To map an SSL certificate to a domain mapping, update `certificate_id` to point to an `AuthorizedCertificate` resource. A user must be authorized to administer the associated domain in order to update a `DomainMapping` resource.

Authorization Scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
  
## Firewall

Firewall resources are used to define a collection of access control rules for an Application. Each rule is defined with a position which specifies the rule's order in the sequence of rules, an IP range to be matched against requests, and an action to take upon matching requests.

Every request is evaluated against the Firewall rules in priority order. Processesing stops at the first rule which matches the request's IP address. A final rule always specifies an action that applies to all remaining IP addresses. The default final rule for a newly-created application will be set to "allow" if not otherwise specified by the user.

BatchUpdateIngressRules  
---  
` rpc BatchUpdateIngressRules(`[BatchUpdateIngressRulesRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.BatchUpdateIngressRulesRequest)`) returns (`[BatchUpdateIngressRulesResponse](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.BatchUpdateIngressRulesResponse)`) ` Replaces the entire firewall ruleset in one bulk operation. This overrides and replaces the rules of an existing firewall with the new rules.If the final rule does not match traffic with the '*' wildcard IP range, then an "allow all" rule is explicitly added to the end of the list.

Authorization Scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
CreateIngressRule  
---  
` rpc CreateIngressRule(`[CreateIngressRuleRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.CreateIngressRuleRequest)`) returns (`[FirewallRule](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.FirewallRule)`) ` Creates a firewall rule for the application.

Authorization Scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
DeleteIngressRule  
---  
` rpc DeleteIngressRule(`[DeleteIngressRuleRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.DeleteIngressRuleRequest)`) returns (`[Empty](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Empty)`) ` Deletes the specified firewall rule.

Authorization Scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
GetIngressRule  
---  
` rpc GetIngressRule(`[GetIngressRuleRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.GetIngressRuleRequest)`) returns (`[FirewallRule](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.FirewallRule)`) ` Gets the specified firewall rule.

Authorization Scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/appengine.admin`
  * ` https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/cloud-platform.read-only`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
ListIngressRules  
---  
` rpc ListIngressRules(`[ListIngressRulesRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ListIngressRulesRequest)`) returns (`[ListIngressRulesResponse](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ListIngressRulesResponse)`) ` Lists the firewall rules of an application.

Authorization Scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/appengine.admin`
  * ` https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/cloud-platform.read-only`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
UpdateIngressRule  
---  
` rpc UpdateIngressRule(`[UpdateIngressRuleRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.UpdateIngressRuleRequest)`) returns (`[FirewallRule](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.FirewallRule)`) ` Updates the specified firewall rule.

Authorization Scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
  
## Instances

Manages instances of a version.

DebugInstance  
---  
` rpc DebugInstance(`[DebugInstanceRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.DebugInstanceRequest)`) returns (`[Operation](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Enables debugging on a VM instance. This allows you to use the SSH command to connect to the virtual machine where the instance lives. While in "debug mode", the instance continues to serve live traffic. You should delete the instance when you are done debugging and then allow the system to take over and determine if another instance should be started.Only applicable for instances in App Engine flexible environment.

Authorization Scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
DeleteInstance  
---  
` rpc DeleteInstance(`[DeleteInstanceRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.DeleteInstanceRequest)`) returns (`[Operation](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Stops a running instance.The instance might be automatically recreated based on the scaling settings of the version. For more information, see "How Instances are Managed" ([standard environment](https://cloud.google.com/appengine/docs/standard/python/how-instances-are-managed) | [flexible environment](https://cloud.google.com/appengine/docs/flexible/python/how-instances-are-managed)).To ensure that instances are not re-created and avoid getting billed, you can stop all instances within the target version by changing the serving status of the version to `STOPPED` with the [`apps.services.versions.patch`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions/patch) method.

Authorization Scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
GetInstance  
---  
` rpc GetInstance(`[GetInstanceRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.GetInstanceRequest)`) returns (`[Instance](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Instance)`) ` Gets instance information.

Authorization Scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/appengine.admin`
  * ` https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/cloud-platform.read-only`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
ListInstances  
---  
` rpc ListInstances(`[ListInstancesRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ListInstancesRequest)`) returns (`[ListInstancesResponse](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ListInstancesResponse)`) ` Lists the instances of a version.Tip: To aggregate details about instances over time, see the [Stackdriver Monitoring API](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list).

Authorization Scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/appengine.admin`
  * ` https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/cloud-platform.read-only`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
  
## Services

Manages services of an application.

DeleteService  
---  
` rpc DeleteService(`[DeleteServiceRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.DeleteServiceRequest)`) returns (`[Operation](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Deletes the specified service and all enclosed versions.

Authorization Scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
GetService  
---  
` rpc GetService(`[GetServiceRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.GetServiceRequest)`) returns (`[Service](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Service)`) ` Gets the current configuration of the specified service.

Authorization Scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/appengine.admin`
  * ` https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/cloud-platform.read-only`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
ListServices  
---  
` rpc ListServices(`[ListServicesRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ListServicesRequest)`) returns (`[ListServicesResponse](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ListServicesResponse)`) ` Lists all the services in the application.

Authorization Scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/appengine.admin`
  * ` https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/cloud-platform.read-only`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
UpdateService  
---  
` rpc UpdateService(`[UpdateServiceRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.UpdateServiceRequest)`) returns (`[Operation](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Updates the configuration of the specified service.

Authorization Scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
  
## Versions

Manages versions of a service.

CreateVersion  
---  
` rpc CreateVersion(`[CreateVersionRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.CreateVersionRequest)`) returns (`[Operation](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Deploys code and resource files to a new version.

Authorization Scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
DeleteVersion  
---  
` rpc DeleteVersion(`[DeleteVersionRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.DeleteVersionRequest)`) returns (`[Operation](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Deletes an existing Version resource.

Authorization Scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
GetVersion  
---  
` rpc GetVersion(`[GetVersionRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.GetVersionRequest)`) returns (`[Version](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Version)`) ` Gets the specified Version resource. By default, only a `BASIC_VIEW` will be returned. Specify the `FULL_VIEW` parameter to get the full resource.

Authorization Scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/appengine.admin`
  * ` https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/cloud-platform.read-only`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
ListVersions  
---  
` rpc ListVersions(`[ListVersionsRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ListVersionsRequest)`) returns (`[ListVersionsResponse](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ListVersionsResponse)`) ` Lists the versions of a service.

Authorization Scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/appengine.admin`
  * ` https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/cloud-platform.read-only`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
UpdateVersion  
---  
` rpc UpdateVersion(`[UpdateVersionRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.UpdateVersionRequest)`) returns (`[Operation](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Updates the specified Version resource. You can specify the following fields depending on the App Engine environment and type of scaling that the version resource uses:**Standard environment**

  * [`instance_class`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.instance_class)

_automatic scaling_ in the standard environment:

  * [`automatic_scaling.min_idle_instances`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling)
  * [`automatic_scaling.max_idle_instances`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling)
  * [`automaticScaling.standard_scheduler_settings.max_instances`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#StandardSchedulerSettings)
  * [`automaticScaling.standard_scheduler_settings.min_instances`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#StandardSchedulerSettings)
  * [`automaticScaling.standard_scheduler_settings.target_cpu_utilization`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#StandardSchedulerSettings)
  * [`automaticScaling.standard_scheduler_settings.target_throughput_utilization`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#StandardSchedulerSettings)

_basic scaling_ or _manual scaling_ in the standard environment:

  * [`serving_status`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.serving_status)
  * [`manual_scaling.instances`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#manualscaling)

**Flexible environment**

  * [`serving_status`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.serving_status)

_automatic scaling_ in the flexible environment:

  * [`automatic_scaling.min_total_instances`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling)
  * [`automatic_scaling.max_total_instances`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling)
  * [`automatic_scaling.cool_down_period_sec`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling)
  * [`automatic_scaling.cpu_utilization.target_utilization`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#Version.FIELDS.automatic_scaling)

_manual scaling_ in the flexible environment:

  * [`manual_scaling.instances`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#manualscaling)



Authorization Scopes
     Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).  
  
## ApiConfigHandler

[Google Cloud Endpoints](https://cloud.google.com/endpoints) configuration for API handlers.

Fields  
---  
`auth_fail_action` |  ``[AuthFailAction](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.AuthFailAction)`` Action to take when users access resources that require authentication. Defaults to `redirect`.  
`login` |  ``[LoginRequirement](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.LoginRequirement)`` Level of login required to access this resource. Defaults to `optional`.  
`script` |  `string` Path to the script from the application root directory.  
`security_level` |  ``[SecurityLevel](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.SecurityLevel)`` Security (HTTPS) enforcement for this URL.  
`url` |  `string` URL to serve the endpoint at.  
  
## ApiEndpointHandler

Uses Google Cloud Endpoints to handle requests.

Fields  
---  
`script_path` |  `string` Path to the script from the application root directory.  
  
## Application

An Application resource contains the top-level configuration of an App Engine application.

Fields  
---  
`name` |  `string` Output only. Full path to the Application resource in the API. Example: `apps/myapp`.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`id` |  `string` Identifier of the Application resource. This identifier is equivalent to the project ID of the Google Cloud Platform project where you want to deploy your application. Example: `myapp`.  
`dispatch_rules[]` |  ``[UrlDispatchRule](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.UrlDispatchRule)`` HTTP path dispatch rules for requests to the application that do not explicitly target a service or version. Rules are order-dependent. Up to 20 dispatch rules can be supported.  
`auth_domain` |  `string` Google Apps authentication domain that controls which users can access this application.Defaults to open access for any Google Account.  
`location_id` |  `string` Location from which this application runs. Application instances run out of the data centers in the specified location, which is also where all of the application's end user content is stored.Defaults to `us-central`.View the list of [supported locations](https://cloud.google.com/appengine/docs/locations).  
`code_bucket` |  `string` Output only. Google Cloud Storage bucket that can be used for storing files associated with this application. This bucket is associated with the application and can be used by the gcloud deployment commands.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`default_cookie_expiration` |  ``[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)`` Cookie expiration policy for this application.  
`serving_status` |  ``[ServingStatus](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Application.ServingStatus)`` Serving status of this application.  
`default_hostname` |  `string` Output only. Hostname used to reach this application, as resolved by App Engine.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`default_bucket` |  `string` Output only. Google Cloud Storage bucket that can be used by this application to store content.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`service_account` |  `string` The service account associated with the application. This is the app-level default identity. If no identity provided during create version, Admin API will fallback to this one.  
`iap` |  ``[IdentityAwareProxy](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Application.IdentityAwareProxy)``  
`gcr_domain` |  `string` Output only. The Google Container Registry domain used for storing managed build docker images for this application.  
`database_type` |  ``[DatabaseType](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Application.DatabaseType)`` The type of the Cloud Firestore or Cloud Datastore database associated with this application.  
`feature_settings` |  ``[FeatureSettings](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Application.FeatureSettings)`` The feature specific settings to be used in the application.  
  
## DatabaseType

Enums  
---  
`DATABASE_TYPE_UNSPECIFIED` | Database type is unspecified.  
`CLOUD_DATASTORE` | Cloud Datastore  
`CLOUD_FIRESTORE` | Cloud Firestore Native  
`CLOUD_DATASTORE_COMPATIBILITY` | Cloud Firestore in Datastore Mode  
  
## FeatureSettings

The feature specific settings to be used in the application. These define behaviors that are user configurable.

Fields  
---  
`split_health_checks` |  `bool` Boolean value indicating if split health checks should be used instead of the legacy health checks. At an app.yaml level, this means defaulting to 'readiness_check' and 'liveness_check' values instead of 'health_check' ones. Once the legacy 'health_check' behavior is deprecated, and this value is always true, this setting can be removed.  
`use_container_optimized_os` |  `bool` If true, use [Container-Optimized OS](https://cloud.google.com/container-optimized-os/) base image for VMs, rather than a base Debian image.  
  
## IdentityAwareProxy

Identity-Aware Proxy

Fields  
---  
`enabled` |  `bool` Whether the serving infrastructure will authenticate and authorize all incoming requests.If true, the `oauth2_client_id` and `oauth2_client_secret` fields must be non-empty.  
`oauth2_client_id` |  `string` OAuth2 client ID to use for the authentication flow.  
`oauth2_client_secret` |  `string` OAuth2 client secret to use for the authentication flow.For security reasons, this value cannot be retrieved via the API. Instead, the SHA-256 hash of the value is returned in the `oauth2_client_secret_sha256` field.@InputOnly  
`oauth2_client_secret_sha256` |  `string` Output only. Hex-encoded SHA-256 hash of the client secret.Note: This field is used in responses only. Any value specified here in a request is ignored.  
  
## ServingStatus

Enums  
---  
`UNSPECIFIED` | Serving status is unspecified.  
`SERVING` | Application is serving.  
`USER_DISABLED` | Application has been disabled by the user.  
`SYSTEM_DISABLED` | Application has been disabled by the system.  
  
## AuthFailAction

Actions to take when the user is not logged in.

Enums  
---  
`AUTH_FAIL_ACTION_UNSPECIFIED` | Not specified. `AUTH_FAIL_ACTION_REDIRECT` is assumed.  
`AUTH_FAIL_ACTION_REDIRECT` | Redirects user to "accounts.google.com". The user is redirected back to the application URL after signing in or creating an account.  
`AUTH_FAIL_ACTION_UNAUTHORIZED` | Rejects request with a `401` HTTP status code and an error message.  
  
## AuthorizedCertificate

An SSL certificate that a user has been authorized to administer. A user is authorized to administer any certificate that applies to one of their authorized domains.

Fields  
---  
`name` |  `string` Full path to the `AuthorizedCertificate` resource in the API. Example: `apps/myapp/authorizedCertificates/12345`.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`id` |  `string` Relative name of the certificate. This is a unique value autogenerated on `AuthorizedCertificate` resource creation. Example: `12345`.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`display_name` |  `string` The user-specified display name of the certificate. This is not guaranteed to be unique. Example: `My Certificate`.  
`domain_names[]` |  `string` Topmost applicable domains of this certificate. This certificate applies to these domains and their subdomains. Example: `example.com`.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`expire_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` The time when this certificate expires. To update the renewal time on this certificate, upload an SSL certificate with a different expiration time using [`AuthorizedCertificates.UpdateAuthorizedCertificate`](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1).Note: This field is used in responses only. Any value specified here in a request is ignored.  
`certificate_raw_data` |  ``[CertificateRawData](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.CertificateRawData)`` The SSL certificate serving the `AuthorizedCertificate` resource. This must be obtained independently from a certificate authority.  
`managed_certificate` |  ``[ManagedCertificate](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ManagedCertificate)`` Only applicable if this certificate is managed by App Engine. Managed certificates are tied to the lifecycle of a `DomainMapping` and cannot be updated or deleted via the `AuthorizedCertificates` API. If this certificate is manually administered by the user, this field will be empty.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`visible_domain_mappings[]` |  `string` The full paths to user visible Domain Mapping resources that have this certificate mapped. Example: `apps/myapp/domainMappings/example.com`.This may not represent the full list of mapped domain mappings if the user does not have `VIEWER` permissions on all of the applications that have this certificate mapped. See `domain_mappings_count` for a complete count.Only returned by `GET` or `LIST` requests when specifically requested by the `view=FULL_CERTIFICATE` option.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`domain_mappings_count` |  `int32` Aggregate count of the domain mappings with this certificate mapped. This count includes domain mappings on applications for which the user does not have `VIEWER` permissions.Only returned by `GET` or `LIST` requests when specifically requested by the `view=FULL_CERTIFICATE` option.Note: This field is used in responses only. Any value specified here in a request is ignored.  
  
## AuthorizedCertificateView

Fields that should be returned when an AuthorizedCertificate resource is retrieved.

Enums  
---  
`BASIC_CERTIFICATE` | Basic certificate information, including applicable domains and expiration date.  
`FULL_CERTIFICATE` | The information from `BASIC_CERTIFICATE`, plus detailed information on the domain mappings that have this certificate mapped.  
  
## AuthorizedDomain

A domain that a user has been authorized to administer. To authorize use of a domain, verify ownership via [Search Console](https://search.google.com/search-console/welcome).

Fields  
---  
`name` |  `string` Full path to the `AuthorizedDomain` resource in the API. Example: `apps/myapp/authorizedDomains/example.com`.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`id` |  `string` Fully qualified domain name of the domain authorized for use. Example: `example.com`.  
  
## AutomaticScaling

Automatic scaling is based on request rate, response latencies, and other application metrics.

Fields  
---  
`cool_down_period` |  ``[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)`` The time period that the [Autoscaler](https://cloud.google.com/compute/docs/autoscaler/) should wait before it starts collecting information from a new instance. This prevents the autoscaler from collecting information when the instance is initializing, during which the collected usage would not be reliable. Only applicable in the App Engine flexible environment.  
`cpu_utilization` |  ``[CpuUtilization](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.CpuUtilization)`` Target scaling by CPU usage.  
`max_concurrent_requests` |  `int32` Number of concurrent requests an automatic scaling instance can accept before the scheduler spawns a new instance.Defaults to a runtime-specific value.  
`max_idle_instances` |  `int32` Maximum number of idle instances that should be maintained for this version.  
`max_total_instances` |  `int32` Maximum number of instances that should be started to handle requests for this version.  
`max_pending_latency` |  ``[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)`` Maximum amount of time that a request should wait in the pending queue before starting a new instance to handle it.  
`min_idle_instances` |  `int32` Minimum number of idle instances that should be maintained for this version. Only applicable for the default version of a service.  
`min_total_instances` |  `int32` Minimum number of running instances that should be maintained for this version.  
`min_pending_latency` |  ``[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)`` Minimum amount of time a request should wait in the pending queue before starting a new instance to handle it.  
`request_utilization` |  ``[RequestUtilization](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.RequestUtilization)`` Target scaling by request utilization.  
`disk_utilization` |  ``[DiskUtilization](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.DiskUtilization)`` Target scaling by disk usage.  
`network_utilization` |  ``[NetworkUtilization](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.NetworkUtilization)`` Target scaling by network usage.  
`standard_scheduler_settings` |  ``[StandardSchedulerSettings](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.StandardSchedulerSettings)`` Scheduler settings for standard environment.  
  
## BasicScaling

A service with basic scaling will create an instance when the application receives a request. The instance will be turned down when the app becomes idle. Basic scaling is ideal for work that is intermittent or driven by user activity.

Fields  
---  
`idle_timeout` |  ``[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)`` Duration of time after the last request that an instance must wait before the instance is shut down.  
`max_instances` |  `int32` Maximum number of instances to create for this version.  
  
## BatchUpdateIngressRulesRequest

Request message for `Firewall.BatchUpdateIngressRules`.

Fields  
---  
`name` |  `string` Name of the Firewall collection to set. Example: `apps/myapp/firewall/ingressRules`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `appengine.applications.update`

  
`ingress_rules[]` |  ``[FirewallRule](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.FirewallRule)`` A list of FirewallRules to replace the existing set.  
  
## BatchUpdateIngressRulesResponse

Response message for `Firewall.UpdateAllIngressRules`.

Fields  
---  
`ingress_rules[]` |  ``[FirewallRule](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.FirewallRule)`` The full list of ingress FirewallRules for this application.  
  
## CertificateRawData

An SSL certificate obtained from a certificate authority.

Fields  
---  
`public_certificate` |  `string` PEM encoded x.509 public key certificate. This field is set once on certificate creation. Must include the header and footer. Example:
    
    
    -----BEGIN CERTIFICATE-----
    
    -----END CERTIFICATE-----
      
  
`private_key` |  `string` Unencrypted PEM encoded RSA private key. This field is set once on certificate creation and then encrypted. The key size must be 2048 bits or fewer. Must include the header and footer. Example:
    
    
    -----BEGIN RSA PRIVATE KEY-----
    
    -----END RSA PRIVATE KEY-----
    

@InputOnly  
  
## CloudBuildOptions

Options for the build operations performed as a part of the version deployment. Only applicable for App Engine flexible environment when creating a version using source code directly.

Fields  
---  
`app_yaml_path` |  `string` Path to the yaml file used in deployment, used to determine runtime configuration details.Required for flexible environment builds.See <https://cloud.google.com/appengine/docs/standard/python/config/appref> for more details.  
`cloud_build_timeout` |  ``[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)`` The Cloud Build timeout used as part of any dependent builds performed by version creation. Defaults to 10 minutes.  
  
## ContainerInfo

Docker image that is used to create a container and start a VM instance for the version that you deploy. Only applicable for instances running in the App Engine flexible environment.

Fields  
---  
`image` |  `string` URI to the hosted container image in Google Container Registry. The URI must be fully qualified and include a tag or digest. Examples: "gcr.io/my-project/image:tag" or "gcr.io/my-project/image@digest"  
  
## CpuUtilization

Target scaling by CPU usage.

Fields  
---  
`aggregation_window_length` |  ``[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)`` Period of time over which CPU utilization is calculated.  
`target_utilization` |  `double` Target CPU utilization ratio to maintain when scaling. Must be between 0 and 1.  
  
## CreateApplicationRequest

Request message for `Applications.CreateApplication`.

Fields  
---  
`application` |  ``[Application](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Application)`` Application configuration. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `application`:

  * `appengine.applications.create`

  
  
## CreateAuthorizedCertificateRequest

Request message for `AuthorizedCertificates.CreateAuthorizedCertificate`.

Fields  
---  
`parent` |  `string` Name of the parent `Application` resource. Example: `apps/myapp`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `appengine.applications.update`

  
`certificate` |  ``[AuthorizedCertificate](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.AuthorizedCertificate)`` SSL certificate data.  
  
## CreateDomainMappingRequest

Request message for `DomainMappings.CreateDomainMapping`.

Fields  
---  
`parent` |  `string` Name of the parent Application resource. Example: `apps/myapp`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `appengine.applications.update`

  
`domain_mapping` |  ``[DomainMapping](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.DomainMapping)`` Domain mapping configuration.  
`override_strategy` |  ``[DomainOverrideStrategy](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.DomainOverrideStrategy)`` Whether the domain creation should override any existing mappings for this domain. By default, overrides are rejected.  
  
## CreateIngressRuleRequest

Request message for `Firewall.CreateIngressRule`.

Fields  
---  
`parent` |  `string` Name of the parent Firewall collection in which to create a new rule. Example: `apps/myapp/firewall/ingressRules`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `appengine.applications.update`

  
`rule` |  ``[FirewallRule](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.FirewallRule)`` A FirewallRule containing the new resource.The user may optionally provide a position at which the new rule will be placed. The positions define a sequential list starting at 1. If a rule already exists at the given position, rules greater than the provided position will be moved forward by one.If no position is provided, the server will place the rule as the second to last rule in the sequence before the required default allow-all or deny-all rule.  
  
## CreateVersionMetadataV1

Metadata for the given `[google.longrunning.Operation](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.longrunning#google.longrunning.Operation)` during a `[google.appengine.v1.CreateVersionRequest](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.CreateVersionRequest)`.

Fields  
---  
`cloud_build_id` |  `string` The Cloud Build ID if one was created as part of the version create.Note: This field is used in responses only. Any value specified here in a request is ignored.  
  
## CreateVersionRequest

Request message for `Versions.CreateVersion`.

Fields  
---  
`parent` |  `string` Name of the parent resource to create this version under. Example: `apps/myapp/services/default`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `appengine.versions.create`

  
`version` |  ``[Version](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Version)`` Application deployment configuration.  
  
## DebugInstanceRequest

Request message for `Instances.DebugInstance`.

Fields  
---  
`name` |  `string` Name of the resource requested. Example: `apps/myapp/services/default/versions/v1/instances/instance-1`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `appengine.instances.enableDebug`

  
`ssh_key` |  `string` Public SSH key to add to the instance. Examples:

  * `[USERNAME]:ssh-rsa [KEY_VALUE] [USERNAME]`
  * `[USERNAME]:ssh-rsa [KEY_VALUE] google-ssh {"userName":"[USERNAME]","expireOn":"[EXPIRE_TIME]"}`

For more information, see [Adding and Removing SSH Keys](https://cloud.google.com/compute/docs/instances/adding-removing-ssh-keys). Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `sshKey`:

  * `appengine.instances.enableDebug`

  
  
## DeleteAuthorizedCertificateRequest

Request message for `AuthorizedCertificates.DeleteAuthorizedCertificate`.

Fields  
---  
`name` |  `string` Name of the resource to delete. Example: `apps/myapp/authorizedCertificates/12345`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `appengine.applications.update`

  
  
## DeleteDomainMappingRequest

Request message for `DomainMappings.DeleteDomainMapping`.

Fields  
---  
`name` |  `string` Name of the resource to delete. Example: `apps/myapp/domainMappings/example.com`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `appengine.applications.update`

  
  
## DeleteIngressRuleRequest

Request message for `Firewall.DeleteIngressRule`.

Fields  
---  
`name` |  `string` Name of the Firewall resource to delete. Example: `apps/myapp/firewall/ingressRules/100`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `appengine.applications.update`

  
  
## DeleteInstanceRequest

Request message for `Instances.DeleteInstance`.

Fields  
---  
`name` |  `string` Name of the resource requested. Example: `apps/myapp/services/default/versions/v1/instances/instance-1`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `appengine.instances.delete`

  
  
## DeleteServiceRequest

Request message for `Services.DeleteService`.

Fields  
---  
`name` |  `string` Name of the resource requested. Example: `apps/myapp/services/default`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `appengine.services.delete`

  
  
## DeleteVersionRequest

Request message for `Versions.DeleteVersion`.

Fields  
---  
`name` |  `string` Name of the resource requested. Example: `apps/myapp/services/default/versions/v1`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `appengine.versions.delete`

  
  
## Deployment

Code and application artifacts used to deploy a version to App Engine.

Fields  
---  
`files` |  `map<string, `[FileInfo](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.FileInfo)`>` Manifest of the files stored in Google Cloud Storage that are included as part of this version. All files must be readable using the credentials supplied with this call.  
`container` |  ``[ContainerInfo](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ContainerInfo)`` The Docker image for the container that runs the version. Only applicable for instances running in the App Engine flexible environment.  
`zip` |  ``[ZipInfo](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ZipInfo)`` The zip file for this deployment, if this is a zip deployment.  
`cloud_build_options` |  ``[CloudBuildOptions](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.CloudBuildOptions)`` Options for any Google Cloud Build builds created as a part of this deployment.These options will only be used if a new build is created, such as when deploying to the App Engine flexible environment using files or zip.  
  
## DiskUtilization

Target scaling by disk usage. Only applicable in the App Engine flexible environment.

Fields  
---  
`target_write_bytes_per_second` |  `int32` Target bytes written per second.  
`target_write_ops_per_second` |  `int32` Target ops written per second.  
`target_read_bytes_per_second` |  `int32` Target bytes read per second.  
`target_read_ops_per_second` |  `int32` Target ops read per seconds.  
  
## DomainMapping

A domain serving an App Engine application.

Fields  
---  
`name` |  `string` Full path to the `DomainMapping` resource in the API. Example: `apps/myapp/domainMapping/example.com`.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`id` |  `string` Relative name of the domain serving the application. Example: `example.com`.  
`ssl_settings` |  ``[SslSettings](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.SslSettings)`` SSL configuration for this domain. If unconfigured, this domain will not serve with SSL.  
`resource_records[]` |  ``[ResourceRecord](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ResourceRecord)`` The resource records required to configure this domain mapping. These records must be added to the domain's DNS configuration in order to serve the application via this domain mapping.Note: This field is used in responses only. Any value specified here in a request is ignored.  
  
## DomainOverrideStrategy

Override strategy for mutating an existing mapping.

Enums  
---  
`UNSPECIFIED_DOMAIN_OVERRIDE_STRATEGY` | Strategy unspecified. Defaults to `STRICT`.  
`STRICT` | Overrides not allowed. If a mapping already exists for the specified domain, the request will return an ALREADY_EXISTS (409).  
`OVERRIDE` | Overrides allowed. If a mapping already exists for the specified domain, the request will overwrite it. Note that this might stop another Google product from serving. For example, if the domain is mapped to another App Engine application, that app will no longer serve from that domain.  
  
## EndpointsApiService

[Google Cloud Endpoints](https://cloud.google.com/endpoints) configuration. The Endpoints API Service provides tooling for serving Open API and gRPC endpoints via an NGINX proxy. Only valid for App Engine Flexible environment deployments.

The fields here refer to the name and configuration ID of a "service" resource in the [Service Management API](https://cloud.google.com/service-management/overview).

Fields  
---  
`name` |  `string` Endpoints service name which is the name of the "service" resource in the Service Management API. For example "myapi.endpoints.myproject.cloud.goog"  
`config_id` |  `string` Endpoints service configuration ID as specified by the Service Management API. For example "2016-09-19r1".By default, the rollout strategy for Endpoints is `RolloutStrategy.FIXED`. This means that Endpoints starts up with a particular configuration ID. When a new configuration is rolled out, Endpoints must be given the new configuration ID. The `config_id` field is used to give the configuration ID and is required in this case.Endpoints also has a rollout strategy called `RolloutStrategy.MANAGED`. When using this, Endpoints fetches the latest configuration and does not need the configuration ID. In this case, `config_id` must be omitted.  
`rollout_strategy` |  ``[RolloutStrategy](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.EndpointsApiService.RolloutStrategy)`` Endpoints rollout strategy. If `FIXED`, `config_id` must be specified. If `MANAGED`, `config_id` must be omitted.  
`disable_trace_sampling` |  `bool` Enable or disable trace sampling. By default, this is set to false for enabled.  
  
## RolloutStrategy

Available rollout strategies.

Enums  
---  
`UNSPECIFIED_ROLLOUT_STRATEGY` | Not specified. Defaults to `FIXED`.  
`FIXED` | Endpoints service configuration ID will be fixed to the configuration ID specified by `config_id`.  
`MANAGED` | Endpoints service configuration ID will be updated with each rollout.  
  
## Entrypoint

The entrypoint for the application.

Fields  
---  
`shell` |  `string` The format should be a shell command that can be fed to `bash -c`.  
  
## ErrorHandler

Custom static error page to be served when an error occurs.

Fields  
---  
`error_code` |  ``[ErrorCode](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ErrorHandler.ErrorCode)`` Error condition this handler applies to.  
`static_file` |  `string` Static file content to be served for this error.  
`mime_type` |  `string` MIME type of file. Defaults to `text/html`.  
  
## ErrorCode

Error codes.

Enums  
---  
`ERROR_CODE_UNSPECIFIED` | Not specified. ERROR_CODE_DEFAULT is assumed.  
`ERROR_CODE_DEFAULT` | All other error types.  
`ERROR_CODE_OVER_QUOTA` | Application has exceeded a resource quota.  
`ERROR_CODE_DOS_API_DENIAL` | Client blocked by the application's Denial of Service protection configuration.  
`ERROR_CODE_TIMEOUT` | Deadline reached before the application responds.  
  
## FileInfo

Single source file that is part of the version to be deployed. Each source file that is deployed must be specified separately.

Fields  
---  
`source_url` |  `string` URL source to use to fetch this file. Must be a URL to a resource in Google Cloud Storage in the form 'http(s)://storage.googleapis.com/<bucket>/<object>'.  
`sha1_sum` |  `string` The SHA1 hash of the file, in hex.  
`mime_type` |  `string` The MIME type of the file.Defaults to the value from Google Cloud Storage.  
  
## FirewallRule

A single firewall rule that is evaluated against incoming traffic and provides an action to take on matched requests.

Fields  
---  
`priority` |  `int32` A positive integer between [1, Int32.MaxValue-1] that defines the order of rule evaluation. Rules with the lowest priority are evaluated first.A default rule at priority Int32.MaxValue matches all IPv4 and IPv6 traffic when no previous rule matches. Only the action of this rule can be modified by the user.  
`action` |  ``[Action](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.FirewallRule.Action)`` The action to take on matched requests.  
`source_range` |  `string` IP address or range, defined using CIDR notation, of requests that this rule applies to. You can use the wildcard character "*" to match all IPs equivalent to "0/0" and "::/0" together. Examples: `192.168.1.1` or `192.168.0.0/16` or `2001:db8::/32` or `2001:0db8:0000:0042:0000:8a2e:0370:7334`.Truncation will be silently performed on addresses which are not properly truncated. For example, `1.2.3.4/24` is accepted as the same address as `1.2.3.0/24`. Similarly, for IPv6, `2001:db8::1/32` is accepted as the same address as `2001:db8::/32`.  
`description` |  `string` An optional string description of this rule. This field has a maximum length of 400 characters.  
  
## Action

Available actions to take on matching requests.

Enums  
---  
`UNSPECIFIED_ACTION` |   
`ALLOW` | Matching requests are allowed.  
`DENY` | Matching requests are denied.  
  
## FlexibleRuntimeSettings

Runtime settings for the App Engine flexible environment.

Fields  
---  
`operating_system` |  `string` The operating system of the application runtime.  
`runtime_version` |  `string` The runtime version of an App Engine flexible application.  
  
## GetApplicationRequest

Request message for `Applications.GetApplication`.

Fields  
---  
`name` |  `string` Name of the Application resource to get. Example: `apps/myapp`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `appengine.applications.get`

  
  
## GetAuthorizedCertificateRequest

Request message for `AuthorizedCertificates.GetAuthorizedCertificate`.

Fields  
---  
`name` |  `string` Name of the resource requested. Example: `apps/myapp/authorizedCertificates/12345`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `appengine.applications.get`

  
`view` |  ``[AuthorizedCertificateView](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.AuthorizedCertificateView)`` Controls the set of fields returned in the `GET` response.  
  
## GetDomainMappingRequest

Request message for `DomainMappings.GetDomainMapping`.

Fields  
---  
`name` |  `string` Name of the resource requested. Example: `apps/myapp/domainMappings/example.com`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `appengine.applications.get`

  
  
## GetIngressRuleRequest

Request message for `Firewall.GetIngressRule`.

Fields  
---  
`name` |  `string` Name of the Firewall resource to retrieve. Example: `apps/myapp/firewall/ingressRules/100`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `appengine.applications.get`

  
  
## GetInstanceRequest

Request message for `Instances.GetInstance`.

Fields  
---  
`name` |  `string` Name of the resource requested. Example: `apps/myapp/services/default/versions/v1/instances/instance-1`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `appengine.instances.get`

  
  
## GetServiceRequest

Request message for `Services.GetService`.

Fields  
---  
`name` |  `string` Name of the resource requested. Example: `apps/myapp/services/default`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `appengine.services.get`

  
  
## GetVersionRequest

Request message for `Versions.GetVersion`.

Fields  
---  
`name` |  `string` Name of the resource requested. Example: `apps/myapp/services/default/versions/v1`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `appengine.versions.get`

  
`view` |  ``[VersionView](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.VersionView)`` Controls the set of fields returned in the `Get` response.  
  
## HealthCheck

Health checking configuration for VM instances. Unhealthy instances are killed and replaced with new instances. Only applicable for instances in App Engine flexible environment.

Fields  
---  
`disable_health_check` |  `bool` Whether to explicitly disable health checks for this instance.  
`host` |  `string` Host header to send when performing an HTTP health check. Example: "myapp.appspot.com"  
`healthy_threshold` |  `uint32` Number of consecutive successful health checks required before receiving traffic.  
`unhealthy_threshold` |  `uint32` Number of consecutive failed health checks required before removing traffic.  
`restart_threshold` |  `uint32` Number of consecutive failed health checks required before an instance is restarted.  
`check_interval` |  ``[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)`` Interval between health checks.  
`timeout` |  ``[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)`` Time before the health check is considered failed.  
  
## InboundServiceType

Available inbound services.

Enums  
---  
`INBOUND_SERVICE_UNSPECIFIED` | Not specified.  
`INBOUND_SERVICE_MAIL` | Allows an application to receive mail.  
`INBOUND_SERVICE_MAIL_BOUNCE` | Allows an application to receive email-bound notifications.  
`INBOUND_SERVICE_XMPP_ERROR` | Allows an application to receive error stanzas.  
`INBOUND_SERVICE_XMPP_MESSAGE` | Allows an application to receive instant messages.  
`INBOUND_SERVICE_XMPP_SUBSCRIBE` | Allows an application to receive user subscription POSTs.  
`INBOUND_SERVICE_XMPP_PRESENCE` | Allows an application to receive a user's chat presence.  
`INBOUND_SERVICE_CHANNEL_PRESENCE` | Registers an application for notifications when a client connects or disconnects from a channel.  
`INBOUND_SERVICE_WARMUP` | Enables warmup requests.  
  
## Instance

An Instance resource is the computing unit that App Engine uses to automatically scale an application.

Fields  
---  
`name` |  `string` Output only. Full path to the Instance resource in the API. Example: `apps/myapp/services/default/versions/v1/instances/instance-1`.  
`id` |  `string` Output only. Relative name of the instance within the version. Example: `instance-1`.  
`app_engine_release` |  `string` Output only. App Engine release this instance is running on.  
`availability` |  ``[Availability](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Instance.Availability)`` Output only. Availability of the instance.  
`vm_name` |  `string` Output only. Name of the virtual machine where this instance lives. Only applicable for instances in App Engine flexible environment.  
`vm_zone_name` |  `string` Output only. Zone where the virtual machine is located. Only applicable for instances in App Engine flexible environment.  
`vm_id` |  `string` Output only. Virtual machine ID of this instance. Only applicable for instances in App Engine flexible environment.  
`start_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` Output only. Time that this instance was started.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`requests` |  `int32` Output only. Number of requests since this instance was started.  
`errors` |  `int32` Output only. Number of errors since this instance was started.  
`qps` |  `float` Output only. Average queries per second (QPS) over the last minute.  
`average_latency` |  `int32` Output only. Average latency (ms) over the last minute.  
`memory_usage` |  `int64` Output only. Total memory in use (bytes).  
`vm_status` |  `string` Output only. Status of the virtual machine where this instance lives. Only applicable for instances in App Engine flexible environment.  
`vm_debug_enabled` |  `bool` Output only. Whether this instance is in debug mode. Only applicable for instances in App Engine flexible environment.  
`vm_ip` |  `string` Output only. The IP address of this instance. Only applicable for instances in App Engine flexible environment.  
`vm_liveness` |  ``[LivenessState](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Instance.Liveness.LivenessState)`` Output only. The liveness health check of this instance. Only applicable for instances in App Engine flexible environment.  
  
## Availability

Availability of the instance.

Enums  
---  
`UNSPECIFIED` |   
`RESIDENT` |   
`DYNAMIC` |   
  
## Liveness

Wrapper for LivenessState enum.

## LivenessState

Liveness health check status for Flex instances.

Enums  
---  
`LIVENESS_STATE_UNSPECIFIED` | There is no liveness health check for the instance. Only applicable for instances in App Engine standard environment.  
`UNKNOWN` | The health checking system is aware of the instance but its health is not known at the moment.  
`HEALTHY` | The instance is reachable i.e. a connection to the application health checking endpoint can be established, and conforms to the requirements defined by the health check.  
`UNHEALTHY` | The instance is reachable, but does not conform to the requirements defined by the health check.  
`DRAINING` | The instance is being drained. The existing connections to the instance have time to complete, but the new ones are being refused.  
`TIMEOUT` | The instance is unreachable i.e. a connection to the application health checking endpoint cannot be established, or the server does not respond within the specified timeout.  
  
## Library

Third-party Python runtime library that is required by the application.

Fields  
---  
`name` |  `string` Name of the library. Example: "django".  
`version` |  `string` Version of the library to select, or "latest".  
  
## ListAuthorizedCertificatesRequest

Request message for `AuthorizedCertificates.ListAuthorizedCertificates`.

Fields  
---  
`parent` |  `string` Name of the parent `Application` resource. Example: `apps/myapp`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `appengine.applications.get`

  
`view` |  ``[AuthorizedCertificateView](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.AuthorizedCertificateView)`` Controls the set of fields returned in the `LIST` response.  
`page_size` |  `int32` Maximum results to return per page.  
`page_token` |  `string` Continuation token for fetching the next page of results.  
  
## ListAuthorizedCertificatesResponse

Response message for `AuthorizedCertificates.ListAuthorizedCertificates`.

Fields  
---  
`certificates[]` |  ``[AuthorizedCertificate](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.AuthorizedCertificate)`` The SSL certificates the user is authorized to administer.  
`next_page_token` |  `string` Continuation token for fetching the next page of results.  
  
## ListAuthorizedDomainsRequest

Request message for `AuthorizedDomains.ListAuthorizedDomains`.

Fields  
---  
`parent` |  `string` Name of the parent Application resource. Example: `apps/myapp`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `appengine.applications.get`

  
`page_size` |  `int32` Maximum results to return per page.  
`page_token` |  `string` Continuation token for fetching the next page of results.  
  
## ListAuthorizedDomainsResponse

Response message for `AuthorizedDomains.ListAuthorizedDomains`.

Fields  
---  
`domains[]` |  ``[AuthorizedDomain](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.AuthorizedDomain)`` The authorized domains belonging to the user.  
`next_page_token` |  `string` Continuation token for fetching the next page of results.  
  
## ListDomainMappingsRequest

Request message for `DomainMappings.ListDomainMappings`.

Fields  
---  
`parent` |  `string` Name of the parent Application resource. Example: `apps/myapp`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `appengine.applications.get`

  
`page_size` |  `int32` Maximum results to return per page.  
`page_token` |  `string` Continuation token for fetching the next page of results.  
  
## ListDomainMappingsResponse

Response message for `DomainMappings.ListDomainMappings`.

Fields  
---  
`domain_mappings[]` |  ``[DomainMapping](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.DomainMapping)`` The domain mappings for the application.  
`next_page_token` |  `string` Continuation token for fetching the next page of results.  
  
## ListIngressRulesRequest

Request message for `Firewall.ListIngressRules`.

Fields  
---  
`parent` |  `string` Name of the Firewall collection to retrieve. Example: `apps/myapp/firewall/ingressRules`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `appengine.applications.get`

  
`page_size` |  `int32` Maximum results to return per page.  
`page_token` |  `string` Continuation token for fetching the next page of results.  
`matching_address` |  `string` A valid IP Address. If set, only rules matching this address will be returned. The first returned rule will be the rule that fires on requests from this IP.  
  
## ListIngressRulesResponse

Response message for `Firewall.ListIngressRules`.

Fields  
---  
`ingress_rules[]` |  ``[FirewallRule](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.FirewallRule)`` The ingress FirewallRules for this application.  
`next_page_token` |  `string` Continuation token for fetching the next page of results.  
  
## ListInstancesRequest

Request message for `Instances.ListInstances`.

Fields  
---  
`parent` |  `string` Name of the parent Version resource. Example: `apps/myapp/services/default/versions/v1`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `appengine.instances.list`

  
`page_size` |  `int32` Maximum results to return per page.  
`page_token` |  `string` Continuation token for fetching the next page of results.  
  
## ListInstancesResponse

Response message for `Instances.ListInstances`.

Fields  
---  
`instances[]` |  ``[Instance](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Instance)`` The instances belonging to the requested version.  
`next_page_token` |  `string` Continuation token for fetching the next page of results.  
  
## ListServicesRequest

Request message for `Services.ListServices`.

Fields  
---  
`parent` |  `string` Name of the parent Application resource. Example: `apps/myapp`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `appengine.services.list`

  
`page_size` |  `int32` Maximum results to return per page.  
`page_token` |  `string` Continuation token for fetching the next page of results.  
  
## ListServicesResponse

Response message for `Services.ListServices`.

Fields  
---  
`services[]` |  ``[Service](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Service)`` The services belonging to the requested application.  
`next_page_token` |  `string` Continuation token for fetching the next page of results.  
  
## ListVersionsRequest

Request message for `Versions.ListVersions`.

Fields  
---  
`parent` |  `string` Name of the parent Service resource. Example: `apps/myapp/services/default`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `appengine.versions.list`

  
`view` |  ``[VersionView](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.VersionView)`` Controls the set of fields returned in the `List` response.  
`page_size` |  `int32` Maximum results to return per page.  
`page_token` |  `string` Continuation token for fetching the next page of results.  
  
## ListVersionsResponse

Response message for `Versions.ListVersions`.

Fields  
---  
`versions[]` |  ``[Version](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Version)`` The versions belonging to the requested service.  
`next_page_token` |  `string` Continuation token for fetching the next page of results.  
  
## LivenessCheck

Health checking configuration for VM instances. Unhealthy instances are killed and replaced with new instances.

Fields  
---  
`path` |  `string` The request path.  
`host` |  `string` Host header to send when performing a HTTP Liveness check. Example: "myapp.appspot.com"  
`failure_threshold` |  `uint32` Number of consecutive failed checks required before considering the VM unhealthy.  
`success_threshold` |  `uint32` Number of consecutive successful checks required before considering the VM healthy.  
`check_interval` |  ``[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)`` Interval between health checks.  
`timeout` |  ``[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)`` Time before the check is considered failed.  
`initial_delay` |  ``[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)`` The initial delay before starting to execute the checks.  
  
## LocationMetadata

Metadata for the given `[google.cloud.location.Location](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.cloud.location#google.cloud.location.Location)`.

Fields  
---  
`standard_environment_available` |  `bool` App Engine standard environment is available in the given location.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`flexible_environment_available` |  `bool` App Engine flexible environment is available in the given location.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`search_api_available` |  `bool` Output only. [Search API](https://cloud.google.com/appengine/docs/standard/python/search) is available in the given location.  
  
## LoginRequirement

Methods to restrict access to a URL based on login status.

Enums  
---  
`LOGIN_UNSPECIFIED` | Not specified. `LOGIN_OPTIONAL` is assumed.  
`LOGIN_OPTIONAL` | Does not require that the user is signed in.  
`LOGIN_ADMIN` | If the user is not signed in, the `auth_fail_action` is taken. In addition, if the user is not an administrator for the application, they are given an error message regardless of `auth_fail_action`. If the user is an administrator, the handler proceeds.  
`LOGIN_REQUIRED` | If the user has signed in, the handler proceeds normally. Otherwise, the auth_fail_action is taken.  
  
## ManagedCertificate

A certificate managed by App Engine.

Fields  
---  
`last_renewal_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` Time at which the certificate was last renewed. The renewal process is fully managed. Certificate renewal will automatically occur before the certificate expires. Renewal errors can be tracked via `ManagementStatus`.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`status` |  ``[ManagementStatus](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ManagementStatus)`` Status of certificate management. Refers to the most recent certificate acquisition or renewal attempt.Note: This field is used in responses only. Any value specified here in a request is ignored.  
  
## ManagementStatus

State of certificate management. Refers to the most recent certificate acquisition or renewal attempt.

Enums  
---  
`MANAGEMENT_STATUS_UNSPECIFIED` |   
`OK` | Certificate was successfully obtained and inserted into the serving system.  
`PENDING` | Certificate is under active attempts to acquire or renew.  
`FAILED_RETRYING_NOT_VISIBLE` | Most recent renewal failed due to an invalid DNS setup and will be retried. Renewal attempts will continue to fail until the certificate domain's DNS configuration is fixed. The last successfully provisioned certificate may still be serving.  
`FAILED_PERMANENT` | All renewal attempts have been exhausted, likely due to an invalid DNS setup.  
`FAILED_RETRYING_CAA_FORBIDDEN` | Most recent renewal failed due to an explicit CAA record that does not include one of the in-use CAs (Google CA and Let's Encrypt). Renewals will continue to fail until the CAA is reconfigured. The last successfully provisioned certificate may still be serving.  
`FAILED_RETRYING_CAA_CHECKING` | Most recent renewal failed due to a CAA retrieval failure. This means that the domain's DNS provider does not properly handle CAA records, failing requests for CAA records when no CAA records are defined. Renewals will continue to fail until the DNS provider is changed or a CAA record is added for the given domain. The last successfully provisioned certificate may still be serving.  
  
## ManualScaling

A service with manual scaling runs continuously, allowing you to perform complex initialization and rely on the state of its memory over time.

Fields  
---  
`instances` |  `int32` Number of instances to assign to the service at the start. This number can later be altered by using the [Modules API](https://cloud.google.com/appengine/docs/python/modules/functions) `set_num_instances()` function.  
  
## Network

Extra network settings. Only applicable in the App Engine flexible environment.

Fields  
---  
`forwarded_ports[]` |  `string` List of ports, or port pairs, to forward from the virtual machine to the application container. Only applicable in the App Engine flexible environment.  
`instance_tag` |  `string` Tag to apply to the instance during creation. Only applicable in the App Engine flexible environment.  
`name` |  `string` Google Compute Engine network where the virtual machines are created. Specify the short name, not the resource path.Defaults to `default`.  
`subnetwork_name` |  `string` Google Cloud Platform sub-network where the virtual machines are created. Specify the short name, not the resource path.If a subnetwork name is specified, a network name will also be required unless it is for the default network.

  * If the network that the instance is being created in is a Legacy network, then the IP address is allocated from the IPv4Range.
  * If the network that the instance is being created in is an auto Subnet Mode Network, then only network name should be specified (not the subnetwork_name) and the IP address is created from the IPCidrRange of the subnetwork that exists in that zone for that network.
  * If the network that the instance is being created in is a custom Subnet Mode Network, then the subnetwork_name must be specified and the IP address is created from the IPCidrRange of the subnetwork.

If specified, the subnetwork must exist in the same region as the App Engine flexible environment application.  
`session_affinity` |  `bool` Enable session affinity. Only applicable in the App Engine flexible environment.  
  
## NetworkSettings

A NetworkSettings resource is a container for ingress settings for a version or service.

Fields  
---  
`ingress_traffic_allowed` |  ``[IngressTrafficAllowed](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.NetworkSettings.IngressTrafficAllowed)`` The ingress settings for version or service.  
  
## IngressTrafficAllowed

If unspecified, INGRESS_TRAFFIC_ALLOWED_ALL will be used.

Enums  
---  
`INGRESS_TRAFFIC_ALLOWED_UNSPECIFIED` | Unspecified  
`INGRESS_TRAFFIC_ALLOWED_ALL` | Allow HTTP traffic from public and private sources.  
`INGRESS_TRAFFIC_ALLOWED_INTERNAL_ONLY` | Allow HTTP traffic from only private VPC sources.  
`INGRESS_TRAFFIC_ALLOWED_INTERNAL_AND_LB` | Allow HTTP traffic from private VPC sources and through load balancers.  
  
## NetworkUtilization

Target scaling by network usage. Only applicable in the App Engine flexible environment.

Fields  
---  
`target_sent_bytes_per_second` |  `int32` Target bytes sent per second.  
`target_sent_packets_per_second` |  `int32` Target packets sent per second.  
`target_received_bytes_per_second` |  `int32` Target bytes received per second.  
`target_received_packets_per_second` |  `int32` Target packets received per second.  
  
## OperationMetadataV1

Metadata for the given `[google.longrunning.Operation](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.longrunning#google.longrunning.Operation)`.

Fields  
---  
`method` |  `string` API method that initiated this operation. Example: `google.appengine.v1.Versions.CreateVersion`.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`insert_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` Time that this operation was created.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`end_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` Time that this operation completed.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`user` |  `string` User who requested this operation.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`target` |  `string` Name of the resource that this operation is acting on. Example: `apps/myapp/services/default`.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`ephemeral_message` |  `string` Ephemeral message that may change every time the operation is polled.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`warning[]` |  `string` Durable messages that persist on every operation poll.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`create_version_metadata` |  ``[CreateVersionMetadataV1](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.CreateVersionMetadataV1)``  
  
## ReadinessCheck

Readiness checking configuration for VM instances. Unhealthy instances are removed from traffic rotation.

Fields  
---  
`path` |  `string` The request path.  
`host` |  `string` Host header to send when performing a HTTP Readiness check. Example: "myapp.appspot.com"  
`failure_threshold` |  `uint32` Number of consecutive failed checks required before removing traffic.  
`success_threshold` |  `uint32` Number of consecutive successful checks required before receiving traffic.  
`check_interval` |  ``[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)`` Interval between health checks.  
`timeout` |  ``[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)`` Time before the check is considered failed.  
`app_start_timeout` |  ``[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)`` A maximum time limit on application initialization, measured from moment the application successfully replies to a healthcheck until it is ready to serve traffic.  
  
## RepairApplicationRequest

Request message for 'Applications.RepairApplication'.

Fields  
---  
`name` |  `string` Name of the application to repair. Example: `apps/myapp` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `appengine.applications.update`

  
  
## RequestUtilization

Target scaling by request utilization. Only applicable in the App Engine flexible environment.

Fields  
---  
`target_request_count_per_second` |  `int32` Target requests per second.  
`target_concurrent_requests` |  `int32` Target number of concurrent requests.  
  
## ResourceRecord

A DNS resource record.

Fields  
---  
`name` |  `string` Relative name of the object affected by this record. Only applicable for `CNAME` records. Example: 'www'.  
`rrdata` |  `string` Data for this record. Values vary by record type, as defined in RFC 1035 (section 5) and RFC 1034 (section 3.6.1).  
`type` |  ``[RecordType](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ResourceRecord.RecordType)`` Resource record type. Example: `AAAA`.  
  
## RecordType

A resource record type.

Enums  
---  
`RECORD_TYPE_UNSPECIFIED` | An unknown resource record.  
`A` | An A resource record. Data is an IPv4 address.  
`AAAA` | An AAAA resource record. Data is an IPv6 address.  
`CNAME` | A CNAME resource record. Data is a domain name to be aliased.  
  
## Resources

Machine resources for a version.

Fields  
---  
`cpu` |  `double` Number of CPU cores needed.  
`disk_gb` |  `double` Disk size (GB) needed.  
`memory_gb` |  `double` Memory (GB) needed.  
`volumes[]` |  ``[Volume](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Volume)`` User specified volumes.  
`kms_key_reference` |  `string` The name of the encryption key that is stored in Google Cloud KMS. Only should be used by Cloud Composer to encrypt the vm disk  
  
## ScriptHandler

Executes a script to handle the request that matches the URL pattern.

Fields  
---  
`script_path` |  `string` Path to the script from the application root directory.  
  
## SecurityLevel

Methods to enforce security (HTTPS) on a URL.

Enums  
---  
`SECURE_UNSPECIFIED` | Not specified.  
`SECURE_DEFAULT` | Both HTTP and HTTPS requests with URLs that match the handler succeed without redirects. The application can examine the request to determine which protocol was used, and respond accordingly.  
`SECURE_NEVER` | Requests for a URL that match this handler that use HTTPS are automatically redirected to the HTTP equivalent URL.  
`SECURE_OPTIONAL` | Both HTTP and HTTPS requests with URLs that match the handler succeed without redirects. The application can examine the request to determine which protocol was used and respond accordingly.  
`SECURE_ALWAYS` | Requests for a URL that match this handler that do not use HTTPS are automatically redirected to the HTTPS URL with the same path. Query parameters are reserved for the redirect.  
  
## Service

A Service resource is a logical component of an application that can share state and communicate in a secure fashion with other services. For example, an application that handles customer requests might include separate services to handle tasks such as backend data analysis or API requests from mobile devices. Each service has a collection of versions that define a specific set of code used to implement the functionality of that service.

Fields  
---  
`name` |  `string` Full path to the Service resource in the API. Example: `apps/myapp/services/default`.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`id` |  `string` Relative name of the service within the application. Example: `default`.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`split` |  ``[TrafficSplit](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.TrafficSplit)`` Mapping that defines fractional HTTP traffic diversion to different versions within the service.  
`labels` |  `map<string, string>` A set of labels to apply to this service. Labels are key/value pairs that describe the service and all resources that belong to it (e.g., versions). The labels can be used to search and group resources, and are propagated to the usage and billing reports, enabling fine-grain analysis of costs. An example of using labels is to tag resources belonging to different environments (e.g., "env=prod", "env=qa").Label keys and values can be no longer than 63 characters and can only contain lowercase letters, numeric characters, underscores, dashes, and international characters. Label keys must start with a lowercase letter or an international character. Each service can have at most 32 labels.  
`network_settings` |  ``[NetworkSettings](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.NetworkSettings)`` Ingress settings for this service. Will apply to all versions.  
  
## ServingStatus

Run states of a version.

Enums  
---  
`SERVING_STATUS_UNSPECIFIED` | Not specified.  
`SERVING` | Currently serving. Instances are created according to the scaling settings of the version.  
`STOPPED` | Disabled. No instances will be created and the scaling settings are ignored until the state of the version changes to `SERVING`.  
  
## SslSettings

SSL configuration for a `DomainMapping` resource.

Fields  
---  
`certificate_id` |  `string` ID of the `AuthorizedCertificate` resource configuring SSL for the application. Clearing this field will remove SSL support.By default, a managed certificate is automatically created for every domain mapping. To omit SSL support or to configure SSL manually, specify `SslManagementType.MANUAL` on a `CREATE` or `UPDATE` request. You must be authorized to administer the `AuthorizedCertificate` resource to manually map it to a `DomainMapping` resource. Example: `12345`.  
`ssl_management_type` |  ``[SslManagementType](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.SslSettings.SslManagementType)`` SSL management type for this domain. If `AUTOMATIC`, a managed certificate is automatically provisioned. If `MANUAL`, `certificate_id` must be manually specified in order to configure SSL for this domain.  
`pending_managed_certificate_id` |  `string` ID of the managed `AuthorizedCertificate` resource currently being provisioned, if applicable. Until the new managed certificate has been successfully provisioned, the previous SSL state will be preserved. Once the provisioning process completes, the `certificate_id` field will reflect the new managed certificate and this field will be left empty. To remove SSL support while there is still a pending managed certificate, clear the `certificate_id` field with an `UpdateDomainMappingRequest`.Note: This field is used in responses only. Any value specified here in a request is ignored.  
  
## SslManagementType

The SSL management type for this domain.

Enums  
---  
`SSL_MANAGEMENT_TYPE_UNSPECIFIED` | Defaults to `AUTOMATIC`.  
`AUTOMATIC` | SSL support for this domain is configured automatically. The mapped SSL certificate will be automatically renewed.  
`MANUAL` | SSL support for this domain is configured manually by the user. Either the domain has no SSL support or a user-obtained SSL certificate has been explictly mapped to this domain.  
  
## StandardSchedulerSettings

Scheduler settings for standard environment.

Fields  
---  
`target_cpu_utilization` |  `double` Target CPU utilization ratio to maintain when scaling.  
`target_throughput_utilization` |  `double` Target throughput utilization ratio to maintain when scaling  
`min_instances` |  `int32` Minimum number of instances to run for this version. Set to zero to disable `min_instances` configuration.  
`max_instances` |  `int32` Maximum number of instances to run for this version. Set to 2147483647 to disable `max_instances` configuration.  
  
## StaticFilesHandler

Files served directly to the user for a given URL, such as images, CSS stylesheets, or JavaScript source files. Static file handlers describe which files in the application directory are static files, and which URLs serve them.

Fields  
---  
`path` |  `string` Path to the static files matched by the URL pattern, from the application root directory. The path can refer to text matched in groupings in the URL pattern.  
`upload_path_regex` |  `string` Regular expression that matches the file paths for all files that should be referenced by this handler.  
`http_headers` |  `map<string, string>` HTTP headers to use for all responses from these URLs.  
`mime_type` |  `string` MIME type used to serve all files served by this handler.Defaults to file-specific MIME types, which are derived from each file's filename extension.  
`expiration` |  ``[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)`` Time a static file served by this handler should be cached by web proxies and browsers.  
`require_matching_file` |  `bool` Whether this handler should match the request if the file referenced by the handler does not exist.  
`application_readable` |  `bool` Whether files should also be uploaded as code data. By default, files declared in static file handlers are uploaded as static data and are only served to end users; they cannot be read by the application. If enabled, uploads are charged against both your code and static data storage resource quotas.  
  
## TrafficSplit

Traffic routing configuration for versions within a single service. Traffic splits define how traffic directed to the service is assigned to versions.

Fields  
---  
`shard_by` |  ``[ShardBy](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.TrafficSplit.ShardBy)`` Mechanism used to determine which version a request is sent to. The traffic selection algorithm will be stable for either type until allocations are changed.  
`allocations` |  `map<string, double>` Mapping from version IDs within the service to fractional (0.000, 1] allocations of traffic for that version. Each version can be specified only once, but some versions in the service may not have any traffic allocation. Services that have traffic allocated cannot be deleted until either the service is deleted or their traffic allocation is removed. Allocations must sum to 1. Up to two decimal place precision is supported for IP-based splits and up to three decimal places is supported for cookie-based splits.  
  
## ShardBy

Available sharding mechanisms.

Enums  
---  
`UNSPECIFIED` | Diversion method unspecified.  
`COOKIE` | Diversion based on a specially named cookie, "GOOGAPPUID." The cookie must be set by the application itself or no diversion will occur.  
`IP` | Diversion based on applying the modulus operation to a fingerprint of the IP address.  
`RANDOM` | Diversion based on weighted random assignment. An incoming request is randomly routed to a version in the traffic split, with probability proportional to the version's traffic share.  
  
## UpdateApplicationRequest

Request message for `Applications.UpdateApplication`.

Fields  
---  
`name` |  `string` Name of the Application resource to update. Example: `apps/myapp`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `appengine.applications.update`

  
`application` |  ``[Application](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Application)`` An Application containing the updated resource.  
`update_mask` |  ``[FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask)`` Required. Standard field mask for the set of fields to be updated.  
  
## UpdateAuthorizedCertificateRequest

Request message for `AuthorizedCertificates.UpdateAuthorizedCertificate`.

Fields  
---  
`name` |  `string` Name of the resource to update. Example: `apps/myapp/authorizedCertificates/12345`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `appengine.applications.update`

  
`certificate` |  ``[AuthorizedCertificate](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.AuthorizedCertificate)`` An `AuthorizedCertificate` containing the updated resource. Only fields set in the field mask will be updated.  
`update_mask` |  ``[FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask)`` Standard field mask for the set of fields to be updated. Updates are only supported on the `certificate_raw_data` and `display_name` fields.  
  
## UpdateDomainMappingRequest

Request message for `DomainMappings.UpdateDomainMapping`.

Fields  
---  
`name` |  `string` Name of the resource to update. Example: `apps/myapp/domainMappings/example.com`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `appengine.applications.update`

  
`domain_mapping` |  ``[DomainMapping](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.DomainMapping)`` A domain mapping containing the updated resource. Only fields set in the field mask will be updated.  
`update_mask` |  ``[FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask)`` Required. Standard field mask for the set of fields to be updated.  
  
## UpdateIngressRuleRequest

Request message for `Firewall.UpdateIngressRule`.

Fields  
---  
`name` |  `string` Name of the Firewall resource to update. Example: `apps/myapp/firewall/ingressRules/100`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `appengine.applications.update`

  
`rule` |  ``[FirewallRule](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.FirewallRule)`` A FirewallRule containing the updated resource  
`update_mask` |  ``[FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask)`` Standard field mask for the set of fields to be updated.  
  
## UpdateServiceRequest

Request message for `Services.UpdateService`.

Fields  
---  
`name` |  `string` Name of the resource to update. Example: `apps/myapp/services/default`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `appengine.services.update`

  
`service` |  ``[Service](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Service)`` A Service resource containing the updated service. Only fields set in the field mask will be updated.  
`update_mask` |  ``[FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask)`` Required. Standard field mask for the set of fields to be updated.  
`migrate_traffic` |  `bool` Set to `true` to gradually shift traffic to one or more versions that you specify. By default, traffic is shifted immediately. For gradual traffic migration, the target versions must be located within instances that are configured for both [warmup requests](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#InboundServiceType) and [automatic scaling](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#AutomaticScaling). You must specify the [`shardBy`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services#ShardBy) field in the Service resource. Gradual traffic migration is not supported in the App Engine flexible environment. For examples, see [Migrating and Splitting Traffic](https://cloud.google.com/appengine/docs/admin-api/migrating-splitting-traffic).  
  
## UpdateVersionRequest

Request message for `Versions.UpdateVersion`.

Fields  
---  
`name` |  `string` Name of the resource to update. Example: `apps/myapp/services/default/versions/1`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `appengine.versions.update`

  
`version` |  ``[Version](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Version)`` A Version containing the updated resource. Only fields set in the field mask will be updated.  
`update_mask` |  ``[FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask)`` Standard field mask for the set of fields to be updated.  
  
## UrlDispatchRule

Rules to match an HTTP request and dispatch that request to a service.

Fields  
---  
`domain` |  `string` Domain name to match against. The wildcard "`*`" is supported if specified before a period: "`*.`".Defaults to matching all domains: "`*`".  
`path` |  `string` Pathname within the host. Must start with a "`/`". A single "`*`" can be included at the end of the path.The sum of the lengths of the domain and path may not exceed 100 characters.  
`service` |  `string` Resource ID of a service in this application that should serve the matched request. The service must already exist. Example: `default`.  
  
## UrlMap

URL pattern and description of how the URL should be handled. App Engine can handle URLs by executing application code or by serving static files uploaded with the version, such as images, CSS, or JavaScript.

Fields  
---  
`url_regex` |  `string` URL prefix. Uses regular expression syntax, which means regexp special characters must be escaped, but should not contain groupings. All URLs that begin with this prefix are handled by this handler, using the portion of the URL after the prefix as part of the file path.  
`security_level` |  ``[SecurityLevel](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.SecurityLevel)`` Security (HTTPS) enforcement for this URL.  
`login` |  ``[LoginRequirement](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.LoginRequirement)`` Level of login required to access this resource. Not supported for Node.js in the App Engine standard environment.  
`auth_fail_action` |  ``[AuthFailAction](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.AuthFailAction)`` Action to take when users access resources that require authentication. Defaults to `redirect`.  
`redirect_http_response_code` |  ``[RedirectHttpResponseCode](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.UrlMap.RedirectHttpResponseCode)`` `30x` code to use when performing redirects for the `secure` field. Defaults to `302`.  
Union field `handler_type`. Type of handler for this URL pattern. `handler_type` can be only one of the following:  
`static_files` |  ``[StaticFilesHandler](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.StaticFilesHandler)`` Returns the contents of a file, such as an image, as the response.  
`script` |  ``[ScriptHandler](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ScriptHandler)`` Executes a script to handle the requests that match this URL pattern. Only the `auto` value is supported for Node.js in the App Engine standard environment, for example `"script": "auto"`.  
`api_endpoint` |  ``[ApiEndpointHandler](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ApiEndpointHandler)`` Uses API Endpoints to handle requests.  
  
## RedirectHttpResponseCode

Redirect codes.

Enums  
---  
`REDIRECT_HTTP_RESPONSE_CODE_UNSPECIFIED` | Not specified. `302` is assumed.  
`REDIRECT_HTTP_RESPONSE_CODE_301` | `301 Moved Permanently` code.  
`REDIRECT_HTTP_RESPONSE_CODE_302` | `302 Moved Temporarily` code.  
`REDIRECT_HTTP_RESPONSE_CODE_303` | `303 See Other` code.  
`REDIRECT_HTTP_RESPONSE_CODE_307` | `307 Temporary Redirect` code.  
  
## Version

A Version resource is a specific set of source code and configuration files that are deployed into a service.

Fields  
---  
`name` |  `string` Full path to the Version resource in the API. Example: `apps/myapp/services/default/versions/v1`.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`id` |  `string` Relative name of the version within the service. Example: `v1`. Version names can contain only lowercase letters, numbers, or hyphens. Reserved names: "default", "latest", and any name with the prefix "ah-".  
`inbound_services[]` |  ``[InboundServiceType](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.InboundServiceType)`` Before an application can receive email or XMPP messages, the application must be configured to enable the service.  
`instance_class` |  `string` Instance class that is used to run this version. Valid values are:

  * AutomaticScaling: `F1`, `F2`, `F4`, `F4_1G`
  * ManualScaling or BasicScaling: `B1`, `B2`, `B4`, `B8`, `B4_1G`

Defaults to `F1` for AutomaticScaling and `B1` for ManualScaling or BasicScaling.  
`network` |  ``[Network](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Network)`` Extra network settings. Only applicable in the App Engine flexible environment.  
`zones[]` |  `string` The Google Compute Engine zones that are supported by this version in the App Engine flexible environment. Deprecated.  
`resources` |  ``[Resources](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Resources)`` Machine resources for this version. Only applicable in the App Engine flexible environment.  
`runtime` |  `string` Desired runtime. Example: `python27`.  
`runtime_channel` |  `string` The channel of the runtime to use. Only available for some runtimes. Defaults to the `default` channel.  
`threadsafe` |  `bool` Whether multiple requests can be dispatched to this version at once.  
`vm` |  `bool` Whether to deploy this version in a container on a virtual machine.  
`flexible_runtime_settings` |  ``[FlexibleRuntimeSettings](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.FlexibleRuntimeSettings)`` Settings for App Engine flexible runtimes.  
`app_engine_apis` |  `bool` Allows App Engine second generation runtimes to access the legacy bundled services.  
`beta_settings` |  `map<string, string>` Metadata settings that are supplied to this version to enable beta runtime features.  
`env` |  `string` App Engine execution environment for this version.Defaults to `standard`.  
`serving_status` |  ``[ServingStatus](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ServingStatus)`` Current serving status of this version. Only the versions with a `SERVING` status create instances and can be billed.`SERVING_STATUS_UNSPECIFIED` is an invalid value. Defaults to `SERVING`.  
`created_by` |  `string` Email address of the user who created this version.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`create_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` Time that this version was created.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`disk_usage_bytes` |  `int64` Total size in bytes of all the files that are included in this version and currently hosted on the App Engine disk.Note: This field is used in responses only. Any value specified here in a request is ignored.  
`runtime_api_version` |  `string` The version of the API in the given runtime environment. Please see the app.yaml reference for valid values at <https://cloud.google.com/appengine/docs/standard/>/config/appref  
`runtime_main_executable_path` |  `string` The path or name of the app's main executable.  
`service_account` |  `string` The identity that the deployed version will run as. Admin API will use the App Engine Appspot service account as default if this field is neither provided in app.yaml file nor through CLI flag.  
`handlers[]` |  ``[UrlMap](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.UrlMap)`` An ordered list of URL-matching patterns that should be applied to incoming requests. The first matching URL handles the request and other request handlers are not attempted.Only returned in `GET` requests if `view=FULL` is set.  
`error_handlers[]` |  ``[ErrorHandler](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ErrorHandler)`` Custom static error pages. Limited to 10KB per page.Only returned in `GET` requests if `view=FULL` is set.  
`libraries[]` |  ``[Library](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Library)`` Configuration for third-party Python runtime libraries that are required by the application.Only returned in `GET` requests if `view=FULL` is set.  
`api_config` |  ``[ApiConfigHandler](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ApiConfigHandler)`` Serving configuration for [Google Cloud Endpoints](https://cloud.google.com/endpoints).Only returned in `GET` requests if `view=FULL` is set.  
`env_variables` |  `map<string, string>` Environment variables available to the application.Only returned in `GET` requests if `view=FULL` is set.  
`build_env_variables` |  `map<string, string>` Environment variables available to the build environment.Only returned in `GET` requests if `view=FULL` is set.  
`default_expiration` |  ``[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)`` Duration that static files should be cached by web proxies and browsers. Only applicable if the corresponding [StaticFilesHandler](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions#StaticFilesHandler) does not specify its own expiration time.Only returned in `GET` requests if `view=FULL` is set.  
`health_check` |  ``[HealthCheck](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.HealthCheck)`` Configures health checking for instances. Unhealthy instances are stopped and replaced with new instances. Only applicable in the App Engine flexible environment.Only returned in `GET` requests if `view=FULL` is set.  
`readiness_check` |  ``[ReadinessCheck](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ReadinessCheck)`` Configures readiness health checking for instances. Unhealthy instances are not put into the backend traffic rotation.Only returned in `GET` requests if `view=FULL` is set.  
`liveness_check` |  ``[LivenessCheck](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.LivenessCheck)`` Configures liveness health checking for instances. Unhealthy instances are stopped and replaced with new instancesOnly returned in `GET` requests if `view=FULL` is set.  
`nobuild_files_regex` |  `string` Files that match this pattern will not be built into this version. Only applicable for Go runtimes.Only returned in `GET` requests if `view=FULL` is set.  
`deployment` |  ``[Deployment](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Deployment)`` Code and application artifacts that make up this version.Only returned in `GET` requests if `view=FULL` is set.  
`version_url` |  `string` Serving URL for this version. Example: "https://myversion-dot-myservice-dot-myapp.appspot.com"Note: This field is used in responses only. Any value specified here in a request is ignored.  
`endpoints_api_service` |  ``[EndpointsApiService](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.EndpointsApiService)`` Cloud Endpoints configuration.If endpoints_api_service is set, the Cloud Endpoints Extensible Service Proxy will be provided to serve the API implemented by the app.  
`entrypoint` |  ``[Entrypoint](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Entrypoint)`` The entrypoint for the application.  
`vpc_access_connector` |  ``[VpcAccessConnector](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.VpcAccessConnector)`` Enables VPC connectivity for standard apps.  
Union field `scaling`. Controls how instances are created, scaled, and reaped.Defaults to `AutomaticScaling`. `scaling` can be only one of the following:  
`automatic_scaling` |  ``[AutomaticScaling](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.AutomaticScaling)`` Automatic scaling is based on request rate, response latencies, and other application metrics. Instances are dynamically created and destroyed as needed in order to handle traffic.  
`basic_scaling` |  ``[BasicScaling](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.BasicScaling)`` A service with basic scaling will create an instance when the application receives a request. The instance will be turned down when the app becomes idle. Basic scaling is ideal for work that is intermittent or driven by user activity.  
`manual_scaling` |  ``[ManualScaling](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.ManualScaling)`` A service with manual scaling runs continuously, allowing you to perform complex initialization and rely on the state of its memory over time. Manually scaled versions are sometimes referred to as "backends".  
  
## VersionView

Fields that should be returned when `[Version](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.Version)` resources are retrieved.

Enums  
---  
`BASIC` | Basic version information including scaling and inbound services, but not detailed deployment information.  
`FULL` | The information from `BASIC`, plus detailed information about the deployment. This format is required when creating resources, but is not returned in `Get` or `List` by default.  
  
## Volume

Volumes mounted within the app container. Only applicable in the App Engine flexible environment.

Fields  
---  
`name` |  `string` Unique name for the volume.  
`volume_type` |  `string` Underlying volume type, e.g. 'tmpfs'.  
`size_gb` |  `double` Volume size in gigabytes.  
  
## VpcAccessConnector

VPC access connector specification.

Fields  
---  
`name` |  `string` Full Serverless VPC Access Connector name e.g. /projects/my-project/locations/us-central1/connectors/c1.  
`egress_setting` |  ``[EgressSetting](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rpc/google.appengine.v1#google.appengine.v1.VpcAccessConnector.EgressSetting)`` The egress setting for the connector, controlling what traffic is diverted through it.  
  
## EgressSetting

Available egress settings.

This controls what traffic is diverted through the VPC Access Connector resource. By default PRIVATE_IP_RANGES will be used.

Enums  
---  
`EGRESS_SETTING_UNSPECIFIED` |   
`ALL_TRAFFIC` | Force the use of VPC Access for all egress traffic from the function.  
`PRIVATE_IP_RANGES` | Use the VPC Access Connector for private IP space from RFC1918.  
  
## ZipInfo

The zip file information for a zip deployment.

Fields  
---  
`source_url` |  `string` URL of the zip file to deploy from. Must be a URL to a resource in Google Cloud Storage in the form 'http(s)://storage.googleapis.com/<bucket>/<object>'.  
`files_count` |  `int32` An estimate of the number of files in a zip for a zip deployment. If set, must be greater than or equal to the actual number of files. Used for optimizing performance; if not provided, deployment may be slow.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
