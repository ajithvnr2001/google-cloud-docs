---
url: https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute-env/
title: Environment Variables \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:14:30.926810+00:00
---

# Environment Variables  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute-env/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Environment Variables Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1 

A number of environment variables can be used to configure the behavior of the library. There are also functions to configure this behavior in code. The environment variables are convenient when troubleshooting problems.

## Endpoint Overrides

  * `GOOGLE_CLOUD_CPP_ACCELERATOR_TYPES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeAcceleratorTypesConnection()`.
  * `GOOGLE_CLOUD_CPP_ADDRESSES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeAddressesConnection()`.
  * `GOOGLE_CLOUD_CPP_ADVICE_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeAdviceConnection()`.
  * `GOOGLE_CLOUD_CPP_AUTOSCALERS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeAutoscalersConnection()`.
  * `GOOGLE_CLOUD_CPP_BACKEND_BUCKETS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeBackendBucketsConnection()`.
  * `GOOGLE_CLOUD_CPP_BACKEND_SERVICES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeBackendServicesConnection()`.
  * `GOOGLE_CLOUD_CPP_CROSS_SITE_NETWORKS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeCrossSiteNetworksConnection()`.
  * `GOOGLE_CLOUD_CPP_DISKS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeDisksConnection()`.
  * `GOOGLE_CLOUD_CPP_DISK_TYPES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeDiskTypesConnection()`.
  * `GOOGLE_CLOUD_CPP_EXTERNAL_VPN_GATEWAYS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeExternalVpnGatewaysConnection()`.
  * `GOOGLE_CLOUD_CPP_FIREWALLS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeFirewallsConnection()`.
  * `GOOGLE_CLOUD_CPP_FIREWALL_POLICIES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeFirewallPoliciesConnection()`.
  * `GOOGLE_CLOUD_CPP_FORWARDING_RULES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeForwardingRulesConnection()`.
  * `GOOGLE_CLOUD_CPP_GLOBAL_ADDRESSES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeGlobalAddressesConnection()`.
  * `GOOGLE_CLOUD_CPP_GLOBAL_FORWARDING_RULES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeGlobalForwardingRulesConnection()`.
  * `GOOGLE_CLOUD_CPP_GLOBAL_FRONTEND_SETTINGS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeGlobalFrontendSettingsConnection()`.
  * `GOOGLE_CLOUD_CPP_GLOBAL_NETWORK_ENDPOINT_GROUPS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeGlobalNetworkEndpointGroupsConnection()`.
  * `GOOGLE_CLOUD_CPP_GLOBAL_OPERATIONS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeGlobalOperationsConnection()`.
  * `GOOGLE_CLOUD_CPP_GLOBAL_ORGANIZATION_OPERATIONS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeGlobalOrganizationOperationsConnection()`.
  * `GOOGLE_CLOUD_CPP_GLOBAL_PUBLIC_DELEGATED_PREFIXES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeGlobalPublicDelegatedPrefixesConnection()`.
  * `GOOGLE_CLOUD_CPP_GLOBAL_VM_EXTENSION_POLICIES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeGlobalVmExtensionPoliciesConnection()`.
  * `GOOGLE_CLOUD_CPP_HEALTH_CHECKS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeHealthChecksConnection()`.
  * `GOOGLE_CLOUD_CPP_HOSTS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeHostsConnection()`.
  * `GOOGLE_CLOUD_CPP_HTTPS_HEALTH_CHECKS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeHttpsHealthChecksConnection()`.
  * `GOOGLE_CLOUD_CPP_HTTP_HEALTH_CHECKS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeHttpHealthChecksConnection()`.
  * `GOOGLE_CLOUD_CPP_IMAGES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeImagesConnection()`.
  * `GOOGLE_CLOUD_CPP_IMAGE_FAMILY_VIEWS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeImageFamilyViewsConnection()`.
  * `GOOGLE_CLOUD_CPP_IMAGE_VIEWS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeImageViewsConnection()`.
  * `GOOGLE_CLOUD_CPP_INSTANCES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeInstancesConnection()`.
  * `GOOGLE_CLOUD_CPP_INSTANCE_GROUPS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeInstanceGroupsConnection()`.
  * `GOOGLE_CLOUD_CPP_INSTANCE_GROUP_MANAGERS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeInstanceGroupManagersConnection()`.
  * `GOOGLE_CLOUD_CPP_INSTANCE_GROUP_MANAGER_RESIZE_REQUESTS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeInstanceGroupManagerResizeRequestsConnection()`.
  * `GOOGLE_CLOUD_CPP_INSTANCE_SETTINGS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeInstanceSettingsConnection()`.
  * `GOOGLE_CLOUD_CPP_INSTANCE_TEMPLATES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeInstanceTemplatesConnection()`.
  * `GOOGLE_CLOUD_CPP_INSTANT_SNAPSHOTS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeInstantSnapshotsConnection()`.
  * `GOOGLE_CLOUD_CPP_INSTANT_SNAPSHOT_GROUPS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeInstantSnapshotGroupsConnection()`.
  * `GOOGLE_CLOUD_CPP_INTERCONNECTS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeInterconnectsConnection()`.
  * `GOOGLE_CLOUD_CPP_INTERCONNECT_ATTACHMENTS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeInterconnectAttachmentsConnection()`.
  * `GOOGLE_CLOUD_CPP_INTERCONNECT_ATTACHMENT_GROUPS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeInterconnectAttachmentGroupsConnection()`.
  * `GOOGLE_CLOUD_CPP_INTERCONNECT_GROUPS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeInterconnectGroupsConnection()`.
  * `GOOGLE_CLOUD_CPP_INTERCONNECT_LOCATIONS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeInterconnectLocationsConnection()`.
  * `GOOGLE_CLOUD_CPP_INTERCONNECT_REMOTE_LOCATIONS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeInterconnectRemoteLocationsConnection()`.
  * `GOOGLE_CLOUD_CPP_LICENSES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeLicensesConnection()`.
  * `GOOGLE_CLOUD_CPP_LICENSE_CODES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeLicenseCodesConnection()`.
  * `GOOGLE_CLOUD_CPP_MACHINE_IMAGES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeMachineImagesConnection()`.
  * `GOOGLE_CLOUD_CPP_MACHINE_TYPES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeMachineTypesConnection()`.
  * `GOOGLE_CLOUD_CPP_MANAGED_RULESETS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeManagedRulesetsConnection()`.
  * `GOOGLE_CLOUD_CPP_NETWORKS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeNetworksConnection()`.
  * `GOOGLE_CLOUD_CPP_NETWORK_ATTACHMENTS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeNetworkAttachmentsConnection()`.
  * `GOOGLE_CLOUD_CPP_NETWORK_EDGE_SECURITY_SERVICES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeNetworkEdgeSecurityServicesConnection()`.
  * `GOOGLE_CLOUD_CPP_NETWORK_ENDPOINT_GROUPS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeNetworkEndpointGroupsConnection()`.
  * `GOOGLE_CLOUD_CPP_NETWORK_FIREWALL_POLICIES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeNetworkFirewallPoliciesConnection()`.
  * `GOOGLE_CLOUD_CPP_NETWORK_PROFILES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeNetworkProfilesConnection()`.
  * `GOOGLE_CLOUD_CPP_NODE_GROUPS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeNodeGroupsConnection()`.
  * `GOOGLE_CLOUD_CPP_NODE_TEMPLATES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeNodeTemplatesConnection()`.
  * `GOOGLE_CLOUD_CPP_NODE_TYPES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeNodeTypesConnection()`.
  * `GOOGLE_CLOUD_CPP_ORGANIZATION_SECURITY_POLICIES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeOrganizationSecurityPoliciesConnection()`.
  * `GOOGLE_CLOUD_CPP_PACKET_MIRRORINGS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakePacketMirroringsConnection()`.
  * `GOOGLE_CLOUD_CPP_PREVIEW_FEATURES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakePreviewFeaturesConnection()`.
  * `GOOGLE_CLOUD_CPP_PROJECTS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeProjectsConnection()`.
  * `GOOGLE_CLOUD_CPP_PROJECT_VIEWS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeProjectViewsConnection()`.
  * `GOOGLE_CLOUD_CPP_PUBLIC_ADVERTISED_PREFIXES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakePublicAdvertisedPrefixesConnection()`.
  * `GOOGLE_CLOUD_CPP_PUBLIC_DELEGATED_PREFIXES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakePublicDelegatedPrefixesConnection()`.
  * `GOOGLE_CLOUD_CPP_REGIONS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeRegionsConnection()`.
  * `GOOGLE_CLOUD_CPP_REGION_AUTOSCALERS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeRegionAutoscalersConnection()`.
  * `GOOGLE_CLOUD_CPP_REGION_BACKEND_BUCKETS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeRegionBackendBucketsConnection()`.
  * `GOOGLE_CLOUD_CPP_REGION_BACKEND_SERVICES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeRegionBackendServicesConnection()`.
  * `GOOGLE_CLOUD_CPP_REGION_COMMITMENTS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeRegionCommitmentsConnection()`.
  * `GOOGLE_CLOUD_CPP_REGION_COMPOSITE_HEALTH_CHECKS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeRegionCompositeHealthChecksConnection()`.
  * `GOOGLE_CLOUD_CPP_REGION_DISKS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeRegionDisksConnection()`.
  * `GOOGLE_CLOUD_CPP_REGION_DISK_TYPES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeRegionDiskTypesConnection()`.
  * `GOOGLE_CLOUD_CPP_REGION_HEALTH_AGGREGATION_POLICIES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeRegionHealthAggregationPoliciesConnection()`.
  * `GOOGLE_CLOUD_CPP_REGION_HEALTH_CHECKS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeRegionHealthChecksConnection()`.
  * `GOOGLE_CLOUD_CPP_REGION_HEALTH_CHECK_SERVICES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeRegionHealthCheckServicesConnection()`.
  * `GOOGLE_CLOUD_CPP_REGION_HEALTH_SOURCES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeRegionHealthSourcesConnection()`.
  * `GOOGLE_CLOUD_CPP_REGION_INSTANCES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeRegionInstancesConnection()`.
  * `GOOGLE_CLOUD_CPP_REGION_INSTANCE_GROUPS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeRegionInstanceGroupsConnection()`.
  * `GOOGLE_CLOUD_CPP_REGION_INSTANCE_GROUP_MANAGERS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeRegionInstanceGroupManagersConnection()`.
  * `GOOGLE_CLOUD_CPP_REGION_INSTANCE_GROUP_MANAGER_RESIZE_REQUESTS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeRegionInstanceGroupManagerResizeRequestsConnection()`.
  * `GOOGLE_CLOUD_CPP_REGION_INSTANCE_TEMPLATES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeRegionInstanceTemplatesConnection()`.
  * `GOOGLE_CLOUD_CPP_REGION_INSTANT_SNAPSHOTS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeRegionInstantSnapshotsConnection()`.
  * `GOOGLE_CLOUD_CPP_REGION_INSTANT_SNAPSHOT_GROUPS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeRegionInstantSnapshotGroupsConnection()`.
  * `GOOGLE_CLOUD_CPP_REGION_NETWORK_ENDPOINT_GROUPS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeRegionNetworkEndpointGroupsConnection()`.
  * `GOOGLE_CLOUD_CPP_REGION_NETWORK_FIREWALL_POLICIES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeRegionNetworkFirewallPoliciesConnection()`.
  * `GOOGLE_CLOUD_CPP_REGION_NOTIFICATION_ENDPOINTS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeRegionNotificationEndpointsConnection()`.
  * `GOOGLE_CLOUD_CPP_REGION_OPERATIONS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeRegionOperationsConnection()`.
  * `GOOGLE_CLOUD_CPP_REGION_SECURITY_POLICIES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeRegionSecurityPoliciesConnection()`.
  * `GOOGLE_CLOUD_CPP_REGION_SNAPSHOTS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeRegionSnapshotsConnection()`.
  * `GOOGLE_CLOUD_CPP_REGION_SNAPSHOT_SETTINGS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeRegionSnapshotSettingsConnection()`.
  * `GOOGLE_CLOUD_CPP_REGION_SSL_CERTIFICATES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeRegionSslCertificatesConnection()`.
  * `GOOGLE_CLOUD_CPP_REGION_SSL_POLICIES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeRegionSslPoliciesConnection()`.
  * `GOOGLE_CLOUD_CPP_REGION_TARGET_HTTPS_PROXIES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeRegionTargetHttpsProxiesConnection()`.
  * `GOOGLE_CLOUD_CPP_REGION_TARGET_HTTP_PROXIES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeRegionTargetHttpProxiesConnection()`.
  * `GOOGLE_CLOUD_CPP_REGION_TARGET_TCP_PROXIES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeRegionTargetTcpProxiesConnection()`.
  * `GOOGLE_CLOUD_CPP_REGION_URL_MAPS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeRegionUrlMapsConnection()`.
  * `GOOGLE_CLOUD_CPP_REGION_ZONES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeRegionZonesConnection()`.
  * `GOOGLE_CLOUD_CPP_RELIABILITY_RISKS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeReliabilityRisksConnection()`.
  * `GOOGLE_CLOUD_CPP_RESERVATIONS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeReservationsConnection()`.
  * `GOOGLE_CLOUD_CPP_RESERVATION_BLOCKS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeReservationBlocksConnection()`.
  * `GOOGLE_CLOUD_CPP_RESERVATION_SLOTS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeReservationSlotsConnection()`.
  * `GOOGLE_CLOUD_CPP_RESERVATION_SUB_BLOCKS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeReservationSubBlocksConnection()`.
  * `GOOGLE_CLOUD_CPP_RESOURCE_POLICIES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeResourcePoliciesConnection()`.
  * `GOOGLE_CLOUD_CPP_ROLLOUTS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeRolloutsConnection()`.
  * `GOOGLE_CLOUD_CPP_ROLLOUT_PLANS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeRolloutPlansConnection()`.
  * `GOOGLE_CLOUD_CPP_ROUTERS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeRoutersConnection()`.
  * `GOOGLE_CLOUD_CPP_ROUTES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeRoutesConnection()`.
  * `GOOGLE_CLOUD_CPP_SECURITY_POLICIES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeSecurityPoliciesConnection()`.
  * `GOOGLE_CLOUD_CPP_SERVICE_ATTACHMENTS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeServiceAttachmentsConnection()`.
  * `GOOGLE_CLOUD_CPP_SNAPSHOTS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeSnapshotsConnection()`.
  * `GOOGLE_CLOUD_CPP_SNAPSHOT_SETTINGS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeSnapshotSettingsConnection()`.
  * `GOOGLE_CLOUD_CPP_SSL_CERTIFICATES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeSslCertificatesConnection()`.
  * `GOOGLE_CLOUD_CPP_SSL_POLICIES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeSslPoliciesConnection()`.
  * `GOOGLE_CLOUD_CPP_STORAGE_POOLS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeStoragePoolsConnection()`.
  * `GOOGLE_CLOUD_CPP_STORAGE_POOL_TYPES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeStoragePoolTypesConnection()`.
  * `GOOGLE_CLOUD_CPP_SUBNETWORKS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeSubnetworksConnection()`.
  * `GOOGLE_CLOUD_CPP_TARGET_GRPC_PROXIES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeTargetGrpcProxiesConnection()`.
  * `GOOGLE_CLOUD_CPP_TARGET_HTTPS_PROXIES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeTargetHttpsProxiesConnection()`.
  * `GOOGLE_CLOUD_CPP_TARGET_HTTP_PROXIES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeTargetHttpProxiesConnection()`.
  * `GOOGLE_CLOUD_CPP_TARGET_INSTANCES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeTargetInstancesConnection()`.
  * `GOOGLE_CLOUD_CPP_TARGET_POOLS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeTargetPoolsConnection()`.
  * `GOOGLE_CLOUD_CPP_TARGET_SSL_PROXIES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeTargetSslProxiesConnection()`.
  * `GOOGLE_CLOUD_CPP_TARGET_TCP_PROXIES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeTargetTcpProxiesConnection()`.
  * `GOOGLE_CLOUD_CPP_TARGET_VPN_GATEWAYS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeTargetVpnGatewaysConnection()`.
  * `GOOGLE_CLOUD_CPP_URL_MAPS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeUrlMapsConnection()`.
  * `GOOGLE_CLOUD_CPP_VPN_GATEWAYS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeVpnGatewaysConnection()`.
  * `GOOGLE_CLOUD_CPP_VPN_TUNNELS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeVpnTunnelsConnection()`.
  * `GOOGLE_CLOUD_CPP_WIRE_GROUPS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeWireGroupsConnection()`.
  * `GOOGLE_CLOUD_CPP_ZONES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeZonesConnection()`.
  * `GOOGLE_CLOUD_CPP_ZONE_OPERATIONS_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeZoneOperationsConnection()`.
  * `GOOGLE_CLOUD_CPP_ZONE_VM_EXTENSION_POLICIES_ENDPOINT=...` overrides the `EndpointOption` (which defaults to "compute.googleapis.com") used by `MakeZoneVmExtensionPoliciesConnection()`.



###### See Also

[`google::cloud::EndpointOption`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1EndpointOption.html)

## Logging

`GOOGLE_CLOUD_CPP_ENABLE_TRACING=rpc`: turns on tracing for most gRPC calls. The library injects an additional Stub decorator that prints each gRPC request and response. Unless you have configured your own logging backend, you should also set `GOOGLE_CLOUD_CPP_ENABLE_CLOG` to produce any output on the program's console.

###### See Also

[`google::cloud::LoggingComponentsOption`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1LoggingComponentsOption.html)`GOOGLE_CLOUD_CPP_TRACING_OPTIONS=...`: modifies the behavior of gRPC tracing, including whether messages will be output on multiple lines, or whether string/bytes fields will be truncated.

###### See Also

google:☁️:TracingOptionsOption`GOOGLE_CLOUD_CPP_ENABLE_CLOG=yes`: turns on logging in the library, basically the library always "logs" but the logging infrastructure has no backend to actually print anything until the application sets a backend or they set this environment variable.

###### See Also

[`google::cloud::LogBackend`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1LogBackend.html)

###### See Also

[`google::cloud::LogSink`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1LogSink.html)

## Setting the Default Project

`GOOGLE_CLOUD_PROJECT=...`: is used in examples and integration tests to configure the GCP project. This has no effect in the library. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
