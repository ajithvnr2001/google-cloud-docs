---
url: https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute-override-endpoint/
title: How to Override the Default Endpoint \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:14:47.340205+00:00
---

# How to Override the Default Endpoint  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute-override-endpoint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  How to Override the Default Endpoint Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1 

In some cases, you may need to override the default endpoint used by the client library. Use the [EndpointOption](https://docs.cloud.google.com/cpp/docs/reference/common/latest/structgoogle_1_1cloud_1_1EndpointOption.html) when initializing the client library to change this default.

For example, this will override the default endpoint for `compute_accelerator_types_v1::AcceleratorTypesClient`:
    
    
      // This configuration is common with Private Google Access:
      //     https://cloud.google.com/vpc/docs/private-google-access
      auto options = google::cloud::Options{}.set<google::cloud::EndpointOption>(
          "private.googleapis.com");
      auto vpc_client =
          google::cloud::compute_accelerator_types_v1::AcceleratorTypesClient(
              google::cloud::compute_accelerator_types_v1::
                  MakeAcceleratorTypesConnectionRest(options));
    

Follow these links to find examples for other `*Client` classes:

  * [`compute_accelerator_types_v1::AcceleratorTypesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_accelerator_types_v1_1_1AcceleratorTypesClient-endpoint-snippet)
  * [`compute_addresses_v1::AddressesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_addresses_v1_1_1AddressesClient-endpoint-snippet)
  * [`compute_advice_v1::AdviceClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_advice_v1_1_1AdviceClient-endpoint-snippet)
  * [`compute_autoscalers_v1::AutoscalersClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_autoscalers_v1_1_1AutoscalersClient-endpoint-snippet)
  * [`compute_backend_buckets_v1::BackendBucketsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_backend_buckets_v1_1_1BackendBucketsClient-endpoint-snippet)
  * [`compute_backend_services_v1::BackendServicesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_backend_services_v1_1_1BackendServicesClient-endpoint-snippet)
  * [`compute_cross_site_networks_v1::CrossSiteNetworksClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_cross_site_networks_v1_1_1CrossSiteNetworksClient-endpoint-snippet)
  * [`compute_disk_types_v1::DiskTypesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_disk_types_v1_1_1DiskTypesClient-endpoint-snippet)
  * [`compute_disks_v1::DisksClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_disks_v1_1_1DisksClient-endpoint-snippet)
  * [`compute_external_vpn_gateways_v1::ExternalVpnGatewaysClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_external_vpn_gateways_v1_1_1ExternalVpnGatewaysClient-endpoint-snippet)
  * [`compute_firewall_policies_v1::FirewallPoliciesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_firewall_policies_v1_1_1FirewallPoliciesClient-endpoint-snippet)
  * [`compute_firewalls_v1::FirewallsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_firewalls_v1_1_1FirewallsClient-endpoint-snippet)
  * [`compute_forwarding_rules_v1::ForwardingRulesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_forwarding_rules_v1_1_1ForwardingRulesClient-endpoint-snippet)
  * [`compute_global_addresses_v1::GlobalAddressesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_global_addresses_v1_1_1GlobalAddressesClient-endpoint-snippet)
  * [`compute_global_forwarding_rules_v1::GlobalForwardingRulesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_global_forwarding_rules_v1_1_1GlobalForwardingRulesClient-endpoint-snippet)
  * [`compute_global_frontend_settings_v1::GlobalFrontendSettingsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_global_frontend_settings_v1_1_1GlobalFrontendSettingsClient-endpoint-snippet)
  * [`compute_global_network_endpoint_groups_v1::GlobalNetworkEndpointGroupsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_global_network_endpoint_groups_v1_1_1GlobalNetworkEndpointGroupsClient-endpoint-snippet)
  * [`compute_global_operations_v1::GlobalOperationsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_global_operations_v1_1_1GlobalOperationsClient-endpoint-snippet)
  * [`compute_global_organization_operations_v1::GlobalOrganizationOperationsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_global_organization_operations_v1_1_1GlobalOrganizationOperationsClient-endpoint-snippet)
  * [`compute_global_public_delegated_prefixes_v1::GlobalPublicDelegatedPrefixesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_global_public_delegated_prefixes_v1_1_1GlobalPublicDelegatedPrefixesClient-endpoint-snippet)
  * [`compute_global_vm_extension_policies_v1::GlobalVmExtensionPoliciesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_global_vm_extension_policies_v1_1_1GlobalVmExtensionPoliciesClient-endpoint-snippet)
  * [`compute_health_checks_v1::HealthChecksClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_health_checks_v1_1_1HealthChecksClient-endpoint-snippet)
  * [`compute_hosts_v1::HostsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_hosts_v1_1_1HostsClient-endpoint-snippet)
  * [`compute_http_health_checks_v1::HttpHealthChecksClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_http_health_checks_v1_1_1HttpHealthChecksClient-endpoint-snippet)
  * [`compute_https_health_checks_v1::HttpsHealthChecksClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_https_health_checks_v1_1_1HttpsHealthChecksClient-endpoint-snippet)
  * [`compute_image_family_views_v1::ImageFamilyViewsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_image_family_views_v1_1_1ImageFamilyViewsClient-endpoint-snippet)
  * [`compute_image_views_v1::ImageViewsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_image_views_v1_1_1ImageViewsClient-endpoint-snippet)
  * [`compute_images_v1::ImagesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_images_v1_1_1ImagesClient-endpoint-snippet)
  * [`compute_instance_group_manager_resize_requests_v1::InstanceGroupManagerResizeRequestsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_instance_group_manager_resize_requests_v1_1_1InstanceGroupManagerResizeRequestsClient-endpoint-snippet)
  * [`compute_instance_group_managers_v1::InstanceGroupManagersClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_instance_group_managers_v1_1_1InstanceGroupManagersClient-endpoint-snippet)
  * [`compute_instance_groups_v1::InstanceGroupsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_instance_groups_v1_1_1InstanceGroupsClient-endpoint-snippet)
  * [`compute_instance_settings_v1::InstanceSettingsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_instance_settings_v1_1_1InstanceSettingsClient-endpoint-snippet)
  * [`compute_instance_templates_v1::InstanceTemplatesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_instance_templates_v1_1_1InstanceTemplatesClient-endpoint-snippet)
  * [`compute_instances_v1::InstancesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_instances_v1_1_1InstancesClient-endpoint-snippet)
  * [`compute_instant_snapshot_groups_v1::InstantSnapshotGroupsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_instant_snapshot_groups_v1_1_1InstantSnapshotGroupsClient-endpoint-snippet)
  * [`compute_instant_snapshots_v1::InstantSnapshotsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_instant_snapshots_v1_1_1InstantSnapshotsClient-endpoint-snippet)
  * [`compute_interconnect_attachment_groups_v1::InterconnectAttachmentGroupsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_interconnect_attachment_groups_v1_1_1InterconnectAttachmentGroupsClient-endpoint-snippet)
  * [`compute_interconnect_attachments_v1::InterconnectAttachmentsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_interconnect_attachments_v1_1_1InterconnectAttachmentsClient-endpoint-snippet)
  * [`compute_interconnect_groups_v1::InterconnectGroupsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_interconnect_groups_v1_1_1InterconnectGroupsClient-endpoint-snippet)
  * [`compute_interconnect_locations_v1::InterconnectLocationsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_interconnect_locations_v1_1_1InterconnectLocationsClient-endpoint-snippet)
  * [`compute_interconnect_remote_locations_v1::InterconnectRemoteLocationsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_interconnect_remote_locations_v1_1_1InterconnectRemoteLocationsClient-endpoint-snippet)
  * [`compute_interconnects_v1::InterconnectsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_interconnects_v1_1_1InterconnectsClient-endpoint-snippet)
  * [`compute_license_codes_v1::LicenseCodesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_license_codes_v1_1_1LicenseCodesClient-endpoint-snippet)
  * [`compute_licenses_v1::LicensesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_licenses_v1_1_1LicensesClient-endpoint-snippet)
  * [`compute_machine_images_v1::MachineImagesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_machine_images_v1_1_1MachineImagesClient-endpoint-snippet)
  * [`compute_machine_types_v1::MachineTypesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_machine_types_v1_1_1MachineTypesClient-endpoint-snippet)
  * [`compute_managed_rulesets_v1::ManagedRulesetsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_managed_rulesets_v1_1_1ManagedRulesetsClient-endpoint-snippet)
  * [`compute_network_attachments_v1::NetworkAttachmentsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_network_attachments_v1_1_1NetworkAttachmentsClient-endpoint-snippet)
  * [`compute_network_edge_security_services_v1::NetworkEdgeSecurityServicesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_network_edge_security_services_v1_1_1NetworkEdgeSecurityServicesClient-endpoint-snippet)
  * [`compute_network_endpoint_groups_v1::NetworkEndpointGroupsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_network_endpoint_groups_v1_1_1NetworkEndpointGroupsClient-endpoint-snippet)
  * [`compute_network_firewall_policies_v1::NetworkFirewallPoliciesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_network_firewall_policies_v1_1_1NetworkFirewallPoliciesClient-endpoint-snippet)
  * [`compute_network_profiles_v1::NetworkProfilesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_network_profiles_v1_1_1NetworkProfilesClient-endpoint-snippet)
  * [`compute_networks_v1::NetworksClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_networks_v1_1_1NetworksClient-endpoint-snippet)
  * [`compute_node_groups_v1::NodeGroupsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_node_groups_v1_1_1NodeGroupsClient-endpoint-snippet)
  * [`compute_node_templates_v1::NodeTemplatesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_node_templates_v1_1_1NodeTemplatesClient-endpoint-snippet)
  * [`compute_node_types_v1::NodeTypesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_node_types_v1_1_1NodeTypesClient-endpoint-snippet)
  * [`compute_organization_security_policies_v1::OrganizationSecurityPoliciesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_organization_security_policies_v1_1_1OrganizationSecurityPoliciesClient-endpoint-snippet)
  * [`compute_packet_mirrorings_v1::PacketMirroringsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_packet_mirrorings_v1_1_1PacketMirroringsClient-endpoint-snippet)
  * [`compute_preview_features_v1::PreviewFeaturesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_preview_features_v1_1_1PreviewFeaturesClient-endpoint-snippet)
  * [`compute_project_views_v1::ProjectViewsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_project_views_v1_1_1ProjectViewsClient-endpoint-snippet)
  * [`compute_projects_v1::ProjectsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_projects_v1_1_1ProjectsClient-endpoint-snippet)
  * [`compute_public_advertised_prefixes_v1::PublicAdvertisedPrefixesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_public_advertised_prefixes_v1_1_1PublicAdvertisedPrefixesClient-endpoint-snippet)
  * [`compute_public_delegated_prefixes_v1::PublicDelegatedPrefixesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_public_delegated_prefixes_v1_1_1PublicDelegatedPrefixesClient-endpoint-snippet)
  * [`compute_region_autoscalers_v1::RegionAutoscalersClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_autoscalers_v1_1_1RegionAutoscalersClient-endpoint-snippet)
  * [`compute_region_backend_buckets_v1::RegionBackendBucketsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_backend_buckets_v1_1_1RegionBackendBucketsClient-endpoint-snippet)
  * [`compute_region_backend_services_v1::RegionBackendServicesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_backend_services_v1_1_1RegionBackendServicesClient-endpoint-snippet)
  * [`compute_region_commitments_v1::RegionCommitmentsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_commitments_v1_1_1RegionCommitmentsClient-endpoint-snippet)
  * [`compute_region_composite_health_checks_v1::RegionCompositeHealthChecksClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_composite_health_checks_v1_1_1RegionCompositeHealthChecksClient-endpoint-snippet)
  * [`compute_region_disk_types_v1::RegionDiskTypesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_disk_types_v1_1_1RegionDiskTypesClient-endpoint-snippet)
  * [`compute_region_disks_v1::RegionDisksClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_disks_v1_1_1RegionDisksClient-endpoint-snippet)
  * [`compute_region_health_aggregation_policies_v1::RegionHealthAggregationPoliciesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_health_aggregation_policies_v1_1_1RegionHealthAggregationPoliciesClient-endpoint-snippet)
  * [`compute_region_health_check_services_v1::RegionHealthCheckServicesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_health_check_services_v1_1_1RegionHealthCheckServicesClient-endpoint-snippet)
  * [`compute_region_health_checks_v1::RegionHealthChecksClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_health_checks_v1_1_1RegionHealthChecksClient-endpoint-snippet)
  * [`compute_region_health_sources_v1::RegionHealthSourcesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_health_sources_v1_1_1RegionHealthSourcesClient-endpoint-snippet)
  * [`compute_region_instance_group_manager_resize_requests_v1::RegionInstanceGroupManagerResizeRequestsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_instance_group_manager_resize_requests_v1_1_1RegionInstanceGroupManagerResizeRequestsClient-endpoint-snippet)
  * [`compute_region_instance_group_managers_v1::RegionInstanceGroupManagersClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_instance_group_managers_v1_1_1RegionInstanceGroupManagersClient-endpoint-snippet)
  * [`compute_region_instance_groups_v1::RegionInstanceGroupsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_instance_groups_v1_1_1RegionInstanceGroupsClient-endpoint-snippet)
  * [`compute_region_instance_templates_v1::RegionInstanceTemplatesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_instance_templates_v1_1_1RegionInstanceTemplatesClient-endpoint-snippet)
  * [`compute_region_instances_v1::RegionInstancesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_instances_v1_1_1RegionInstancesClient-endpoint-snippet)
  * [`compute_region_instant_snapshot_groups_v1::RegionInstantSnapshotGroupsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_instant_snapshot_groups_v1_1_1RegionInstantSnapshotGroupsClient-endpoint-snippet)
  * [`compute_region_instant_snapshots_v1::RegionInstantSnapshotsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_instant_snapshots_v1_1_1RegionInstantSnapshotsClient-endpoint-snippet)
  * [`compute_region_network_endpoint_groups_v1::RegionNetworkEndpointGroupsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_network_endpoint_groups_v1_1_1RegionNetworkEndpointGroupsClient-endpoint-snippet)
  * [`compute_region_network_firewall_policies_v1::RegionNetworkFirewallPoliciesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_network_firewall_policies_v1_1_1RegionNetworkFirewallPoliciesClient-endpoint-snippet)
  * [`compute_region_notification_endpoints_v1::RegionNotificationEndpointsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_notification_endpoints_v1_1_1RegionNotificationEndpointsClient-endpoint-snippet)
  * [`compute_region_operations_v1::RegionOperationsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_operations_v1_1_1RegionOperationsClient-endpoint-snippet)
  * [`compute_region_security_policies_v1::RegionSecurityPoliciesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_security_policies_v1_1_1RegionSecurityPoliciesClient-endpoint-snippet)
  * [`compute_region_snapshot_settings_v1::RegionSnapshotSettingsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_snapshot_settings_v1_1_1RegionSnapshotSettingsClient-endpoint-snippet)
  * [`compute_region_snapshots_v1::RegionSnapshotsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_snapshots_v1_1_1RegionSnapshotsClient-endpoint-snippet)
  * [`compute_region_ssl_certificates_v1::RegionSslCertificatesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_ssl_certificates_v1_1_1RegionSslCertificatesClient-endpoint-snippet)
  * [`compute_region_ssl_policies_v1::RegionSslPoliciesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_ssl_policies_v1_1_1RegionSslPoliciesClient-endpoint-snippet)
  * [`compute_region_target_http_proxies_v1::RegionTargetHttpProxiesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_target_http_proxies_v1_1_1RegionTargetHttpProxiesClient-endpoint-snippet)
  * [`compute_region_target_https_proxies_v1::RegionTargetHttpsProxiesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_target_https_proxies_v1_1_1RegionTargetHttpsProxiesClient-endpoint-snippet)
  * [`compute_region_target_tcp_proxies_v1::RegionTargetTcpProxiesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_target_tcp_proxies_v1_1_1RegionTargetTcpProxiesClient-endpoint-snippet)
  * [`compute_region_url_maps_v1::RegionUrlMapsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_url_maps_v1_1_1RegionUrlMapsClient-endpoint-snippet)
  * [`compute_region_zones_v1::RegionZonesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_zones_v1_1_1RegionZonesClient-endpoint-snippet)
  * [`compute_regions_v1::RegionsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_regions_v1_1_1RegionsClient-endpoint-snippet)
  * [`compute_reliability_risks_v1::ReliabilityRisksClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_reliability_risks_v1_1_1ReliabilityRisksClient-endpoint-snippet)
  * [`compute_reservation_blocks_v1::ReservationBlocksClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_reservation_blocks_v1_1_1ReservationBlocksClient-endpoint-snippet)
  * [`compute_reservation_slots_v1::ReservationSlotsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_reservation_slots_v1_1_1ReservationSlotsClient-endpoint-snippet)
  * [`compute_reservation_sub_blocks_v1::ReservationSubBlocksClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_reservation_sub_blocks_v1_1_1ReservationSubBlocksClient-endpoint-snippet)
  * [`compute_reservations_v1::ReservationsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_reservations_v1_1_1ReservationsClient-endpoint-snippet)
  * [`compute_resource_policies_v1::ResourcePoliciesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_resource_policies_v1_1_1ResourcePoliciesClient-endpoint-snippet)
  * [`compute_rollout_plans_v1::RolloutPlansClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_rollout_plans_v1_1_1RolloutPlansClient-endpoint-snippet)
  * [`compute_rollouts_v1::RolloutsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_rollouts_v1_1_1RolloutsClient-endpoint-snippet)
  * [`compute_routers_v1::RoutersClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_routers_v1_1_1RoutersClient-endpoint-snippet)
  * [`compute_routes_v1::RoutesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_routes_v1_1_1RoutesClient-endpoint-snippet)
  * [`compute_security_policies_v1::SecurityPoliciesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_security_policies_v1_1_1SecurityPoliciesClient-endpoint-snippet)
  * [`compute_service_attachments_v1::ServiceAttachmentsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_service_attachments_v1_1_1ServiceAttachmentsClient-endpoint-snippet)
  * [`compute_snapshot_settings_v1::SnapshotSettingsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_snapshot_settings_v1_1_1SnapshotSettingsClient-endpoint-snippet)
  * [`compute_snapshots_v1::SnapshotsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_snapshots_v1_1_1SnapshotsClient-endpoint-snippet)
  * [`compute_ssl_certificates_v1::SslCertificatesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_ssl_certificates_v1_1_1SslCertificatesClient-endpoint-snippet)
  * [`compute_ssl_policies_v1::SslPoliciesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_ssl_policies_v1_1_1SslPoliciesClient-endpoint-snippet)
  * [`compute_storage_pool_types_v1::StoragePoolTypesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_storage_pool_types_v1_1_1StoragePoolTypesClient-endpoint-snippet)
  * [`compute_storage_pools_v1::StoragePoolsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_storage_pools_v1_1_1StoragePoolsClient-endpoint-snippet)
  * [`compute_subnetworks_v1::SubnetworksClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_subnetworks_v1_1_1SubnetworksClient-endpoint-snippet)
  * [`compute_target_grpc_proxies_v1::TargetGrpcProxiesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_target_grpc_proxies_v1_1_1TargetGrpcProxiesClient-endpoint-snippet)
  * [`compute_target_http_proxies_v1::TargetHttpProxiesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_target_http_proxies_v1_1_1TargetHttpProxiesClient-endpoint-snippet)
  * [`compute_target_https_proxies_v1::TargetHttpsProxiesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_target_https_proxies_v1_1_1TargetHttpsProxiesClient-endpoint-snippet)
  * [`compute_target_instances_v1::TargetInstancesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_target_instances_v1_1_1TargetInstancesClient-endpoint-snippet)
  * [`compute_target_pools_v1::TargetPoolsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_target_pools_v1_1_1TargetPoolsClient-endpoint-snippet)
  * [`compute_target_ssl_proxies_v1::TargetSslProxiesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_target_ssl_proxies_v1_1_1TargetSslProxiesClient-endpoint-snippet)
  * [`compute_target_tcp_proxies_v1::TargetTcpProxiesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_target_tcp_proxies_v1_1_1TargetTcpProxiesClient-endpoint-snippet)
  * [`compute_target_vpn_gateways_v1::TargetVpnGatewaysClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_target_vpn_gateways_v1_1_1TargetVpnGatewaysClient-endpoint-snippet)
  * [`compute_url_maps_v1::UrlMapsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_url_maps_v1_1_1UrlMapsClient-endpoint-snippet)
  * [`compute_vpn_gateways_v1::VpnGatewaysClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_vpn_gateways_v1_1_1VpnGatewaysClient-endpoint-snippet)
  * [`compute_vpn_tunnels_v1::VpnTunnelsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_vpn_tunnels_v1_1_1VpnTunnelsClient-endpoint-snippet)
  * [`compute_wire_groups_v1::WireGroupsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_wire_groups_v1_1_1WireGroupsClient-endpoint-snippet)
  * [`compute_zone_operations_v1::ZoneOperationsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_zone_operations_v1_1_1ZoneOperationsClient-endpoint-snippet)
  * [`compute_zone_vm_extension_policies_v1::ZoneVmExtensionPoliciesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_zone_vm_extension_policies_v1_1_1ZoneVmExtensionPoliciesClient-endpoint-snippet)
  * [`compute_zones_v1::ZonesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_zones_v1_1_1ZonesClient-endpoint-snippet)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
