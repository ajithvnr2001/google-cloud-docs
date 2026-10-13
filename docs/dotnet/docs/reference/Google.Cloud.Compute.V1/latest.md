---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/
title: Google.Cloud.Compute.V1 \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:57:45.692608+00:00
---

# Google.Cloud.Compute.V1  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google.Cloud.Compute.V1 Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 

`Google.Cloud.Compute.V1` is a.NET client library for the [Compute Engine API](https://cloud.google.com/compute).

Note: This documentation is for version `4.0.0` of the library. Some samples may not work with other versions.

## Installation

Install the `Google.Cloud.Compute.V1` package from NuGet. Add it to your project in the normal way (for example by right-clicking on the project in Visual Studio and choosing "Manage NuGet Packages...").

## Authentication

When running on Google Cloud, no action needs to be taken to authenticate.

Otherwise, the simplest way of authenticating your API calls is to set up Application Default Credentials. The credentials will automatically be used to authenticate. See [Set up Application Default Credentials](https://cloud.google.com/docs/authentication/provide-credentials-adc) for more details.

## Getting started

All operations are performed through the following client classes:

  * [AcceleratorTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypesClient)
  * [AddressesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddressesClient)
  * [AdviceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AdviceClient)
  * [AutoscalersClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AutoscalersClient)
  * [BackendBucketsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendBucketsClient)
  * [BackendServicesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendServicesClient)
  * [CrossSiteNetworksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CrossSiteNetworksClient)
  * [DisksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.DisksClient)
  * [DiskTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.DiskTypesClient)
  * [ExternalVpnGatewaysClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ExternalVpnGatewaysClient)
  * [FirewallPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.FirewallPoliciesClient)
  * [FirewallsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.FirewallsClient)
  * [ForwardingRulesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ForwardingRulesClient)
  * [FutureReservationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.FutureReservationsClient)
  * [GlobalAddressesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalAddressesClient)
  * [GlobalForwardingRulesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalForwardingRulesClient)
  * [GlobalFrontendSettingsServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalFrontendSettingsServiceClient)
  * [GlobalNetworkEndpointGroupsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalNetworkEndpointGroupsClient)
  * [GlobalOperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalOperationsClient)
  * [GlobalOrganizationOperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalOrganizationOperationsClient)
  * [GlobalPublicDelegatedPrefixesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalPublicDelegatedPrefixesClient)
  * [GlobalVmExtensionPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalVmExtensionPoliciesClient)
  * [HealthChecksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.HealthChecksClient)
  * [HostsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.HostsClient)
  * [ImageFamilyViewsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ImageFamilyViewsClient)
  * [ImagesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ImagesClient)
  * [ImageViewsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ImageViewsClient)
  * [InstanceGroupManagerResizeRequestsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstanceGroupManagerResizeRequestsClient)
  * [InstanceGroupManagersClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstanceGroupManagersClient)
  * [InstanceGroupsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstanceGroupsClient)
  * [InstancesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstancesClient)
  * [InstanceSettingsServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstanceSettingsServiceClient)
  * [InstanceTemplatesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstanceTemplatesClient)
  * [InstantSnapshotGroupsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstantSnapshotGroupsClient)
  * [InstantSnapshotsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstantSnapshotsClient)
  * [InterconnectAttachmentGroupsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectAttachmentGroupsClient)
  * [InterconnectAttachmentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectAttachmentsClient)
  * [InterconnectGroupsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectGroupsClient)
  * [InterconnectLocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectLocationsClient)
  * [InterconnectRemoteLocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectRemoteLocationsClient)
  * [InterconnectsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectsClient)
  * [LicenseCodesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.LicenseCodesClient)
  * [LicensesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.LicensesClient)
  * [MachineImagesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.MachineImagesClient)
  * [MachineTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.MachineTypesClient)
  * [ManagedRulesetsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ManagedRulesetsClient)
  * [NetworkAttachmentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkAttachmentsClient)
  * [NetworkEdgeSecurityServicesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkEdgeSecurityServicesClient)
  * [NetworkEndpointGroupsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkEndpointGroupsClient)
  * [NetworkFirewallPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkFirewallPoliciesClient)
  * [NetworkProfilesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkProfilesClient)
  * [NetworksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworksClient)
  * [NodeGroupsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NodeGroupsClient)
  * [NodeTemplatesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NodeTemplatesClient)
  * [NodeTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NodeTypesClient)
  * [OrganizationSecurityPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.OrganizationSecurityPoliciesClient)
  * [PacketMirroringsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.PacketMirroringsClient)
  * [PreviewFeaturesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.PreviewFeaturesClient)
  * [ProjectsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ProjectsClient)
  * [ProjectViewsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ProjectViewsClient)
  * [PublicAdvertisedPrefixesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.PublicAdvertisedPrefixesClient)
  * [PublicDelegatedPrefixesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.PublicDelegatedPrefixesClient)
  * [RegionAutoscalersClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionAutoscalersClient)
  * [RegionBackendBucketsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionBackendBucketsClient)
  * [RegionBackendServicesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionBackendServicesClient)
  * [RegionCommitmentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionCommitmentsClient)
  * [RegionCompositeHealthChecksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionCompositeHealthChecksClient)
  * [RegionDisksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionDisksClient)
  * [RegionDiskTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionDiskTypesClient)
  * [RegionHealthAggregationPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionHealthAggregationPoliciesClient)
  * [RegionHealthChecksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionHealthChecksClient)
  * [RegionHealthCheckServicesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionHealthCheckServicesClient)
  * [RegionHealthSourcesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionHealthSourcesClient)
  * [RegionInstanceGroupManagerResizeRequestsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionInstanceGroupManagerResizeRequestsClient)
  * [RegionInstanceGroupManagersClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionInstanceGroupManagersClient)
  * [RegionInstanceGroupsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionInstanceGroupsClient)
  * [RegionInstancesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionInstancesClient)
  * [RegionInstanceTemplatesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionInstanceTemplatesClient)
  * [RegionInstantSnapshotGroupsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionInstantSnapshotGroupsClient)
  * [RegionInstantSnapshotsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionInstantSnapshotsClient)
  * [RegionNetworkEndpointGroupsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionNetworkEndpointGroupsClient)
  * [RegionNetworkFirewallPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionNetworkFirewallPoliciesClient)
  * [RegionNotificationEndpointsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionNotificationEndpointsClient)
  * [RegionOperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionOperationsClient)
  * [RegionsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionsClient)
  * [RegionSecurityPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSecurityPoliciesClient)
  * [RegionSnapshotsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSnapshotsClient)
  * [RegionSnapshotSettingsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSnapshotSettingsClient)
  * [RegionSslCertificatesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSslCertificatesClient)
  * [RegionSslPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSslPoliciesClient)
  * [RegionTargetHttpProxiesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionTargetHttpProxiesClient)
  * [RegionTargetHttpsProxiesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionTargetHttpsProxiesClient)
  * [RegionTargetTcpProxiesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionTargetTcpProxiesClient)
  * [RegionUrlMapsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionUrlMapsClient)
  * [RegionZonesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionZonesClient)
  * [ReliabilityRisksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReliabilityRisksClient)
  * [ReservationBlocksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReservationBlocksClient)
  * [ReservationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReservationsClient)
  * [ReservationSlotsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReservationSlotsClient)
  * [ReservationSubBlocksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReservationSubBlocksClient)
  * [ResourcePoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ResourcePoliciesClient)
  * [RolloutPlansClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RolloutPlansClient)
  * [RolloutsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RolloutsClient)
  * [RoutersClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RoutersClient)
  * [RoutesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RoutesClient)
  * [SecurityPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SecurityPoliciesClient)
  * [ServiceAttachmentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachmentsClient)
  * [SnapshotsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SnapshotsClient)
  * [SnapshotSettingsServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SnapshotSettingsServiceClient)
  * [SslCertificatesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SslCertificatesClient)
  * [SslPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SslPoliciesClient)
  * [StoragePoolsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.StoragePoolsClient)
  * [StoragePoolTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.StoragePoolTypesClient)
  * [SubnetworksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SubnetworksClient)
  * [TargetGrpcProxiesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TargetGrpcProxiesClient)
  * [TargetHttpProxiesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TargetHttpProxiesClient)
  * [TargetHttpsProxiesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TargetHttpsProxiesClient)
  * [TargetInstancesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TargetInstancesClient)
  * [TargetPoolsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TargetPoolsClient)
  * [TargetSslProxiesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TargetSslProxiesClient)
  * [TargetTcpProxiesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TargetTcpProxiesClient)
  * [TargetVpnGatewaysClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TargetVpnGatewaysClient)
  * [UrlMapsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.UrlMapsClient)
  * [VpnGatewaysClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.VpnGatewaysClient)
  * [VpnTunnelsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.VpnTunnelsClient)
  * [WireGroupsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.WireGroupsClient)
  * [ZoneOperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ZoneOperationsClient)
  * [ZonesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ZonesClient)
  * [ZoneVmExtensionPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ZoneVmExtensionPoliciesClient)



Create a client instance by calling the static `Create` or `CreateAsync` methods. Alternatively, use the builder class associated with each client class (e.g. AcceleratorTypesClientBuilder for AcceleratorTypesClient) as an easy way of specifying custom credentials, settings, or a custom endpoint. Clients are thread-safe, and we recommend using a single instance across your entire application unless you have a particular need to configure multiple client objects separately.

## Using wire values for enums

Many fields in the Compute API are effectively enums, representing one of a fixed set of values.

These are currently represented as string properties in the API surface, for compatibility reasons. C# enums containing the known values are generated, but not used directly within the API surface.

As an example, the `Address` resource has a `NetworkTier` property, of type `string`. The set of valid values is represented by the `Address.Types.NetworkTier` enum - but these are generated with C#-idiomatic names, _not_ the strings that need to be used for the `Address.NetworkTier` property.

Two approaches are provided to allow client code to refer to specific values without hard-coding string literals in an error-prone way. First, the [ComputeEnumConstants](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ComputeEnumConstants) class provides all known enum constants via nested classes. For example, the `NetworkTier` enum used by `Address` is represented in the `ComputeEnumConstants.Address.NetworkTier` class:
    
    
    Address addressResource = new Address
    {
        Name = addressName,
        Region = region,
        NetworkTier = ComputeEnumConstants.Address.NetworkTier.Premium
    };
    

This is simple for cases where client code needs to refer to a single value known at compile-time. In situations where more flexibility is required, the wire value corresponding to each enum value can be obtained using [ComputeEnumHelpers.Format](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ComputeEnumHelpers#Google_Cloud_Compute_V1_ComputeEnumHelpers_Format__1___0_):
    
    
    // This could be passed into a method as a parameter, for example.
    Address.Types.NetworkTier tier = Address.Types.NetworkTier.Premium;
    Address addressResource = new Address
    {
        Name = addressName,
        Region = region,
        NetworkTier = ComputeEnumHelpers.Format(tier)
    };
    

The reverse operation (parsing from a wire value to an enum value) can be achieved using [ComputeEnumHelpers.TryParse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ComputeEnumHelpers#Google_Cloud_Compute_V1_ComputeEnumHelpers_TryParse__1_System_String___0__) and [ComputeEnumHelpers.Parse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ComputeEnumHelpers#Google_Cloud_Compute_V1_ComputeEnumHelpers_Parse__1_System_String_):
    
    
    if (ComputeEnumHelpers.TryParse(addressResource.NetworkTier, out Address.Types.NetworkTier tier))
    {
        // The wire value was recognized, and tier contains the enum value.
        Console.WriteLine($"Network tier: {tier}");
    }
    

(Following .NET conventions, the `Parse` method returns the parsed enum value directly instead of using an `out` parameter, but throws an exception if the value is not recognized.)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
