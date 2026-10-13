---
url: https://docs.cloud.google.com/cpp/docs/reference/compute/latest/
title: Compute Engine API C++ Client Library \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:14:25.274777+00:00
---

# Compute Engine API C++ Client Library  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/compute/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Compute Engine API C++ Client Library Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1 

An idiomatic C++ client library for the [Compute Engine API](https://cloud.google.com/compute), a service to create and manage cloud computing resources.

While this library is **GA** , please note that the Google Cloud C++ client libraries do **not** follow [Semantic Versioning](https://semver.org/).

### Quickstart

The following shows the code that you'll run in the `google/cloud/compute/quickstart/` directory, which should give you a taste of the Cloud Compute Engine API C++ client library.
    
    
    #include "google/cloud/compute/disks/v1/disks_client.h"
    #include <iostream>
    
    int main(int argc, char* argv[]) try {
      if (argc != 3) {
        std::cerr << "Usage: " << argv[0] << " project-id zone-id\n";
        return 1;
      }
    
      namespace disks = ::google::cloud::compute_disks_v1;
      auto client = disks::DisksClient(disks::MakeDisksConnectionRest());
    
      for (auto disk : client.ListDisks(argv[1], argv[2])) {
        if (!disk) throw std::move(disk).status();
        std::cout << disk->DebugString() << "\n";
      }
    
      return 0;
    } catch (google::cloud::Status const& status) {
      std::cerr << "google::cloud::Status thrown: " << status << "\n";
      return 1;
    }
    

### Main classes

This library offers multiple `*Client` classes, which are listed below. Each one of these classes exposes all the RPCs for a service as member functions of the class. This library groups multiple services because they are part of the same product or are often used together. A typical example may be the administrative and data plane operations for a single product.

The library also has other classes that provide helpers, configuration parameters, and infrastructure to mock the `*Client` classes when testing your application.

  * [`compute_accelerator_types_v1::AcceleratorTypesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__accelerator__types__v1_1_1AcceleratorTypesClient)
  * [`compute_addresses_v1::AddressesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__addresses__v1_1_1AddressesClient)
  * [`compute_advice_v1::AdviceClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__advice__v1_1_1AdviceClient)
  * [`compute_autoscalers_v1::AutoscalersClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__autoscalers__v1_1_1AutoscalersClient)
  * [`compute_backend_buckets_v1::BackendBucketsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__backend__buckets__v1_1_1BackendBucketsClient)
  * [`compute_backend_services_v1::BackendServicesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__backend__services__v1_1_1BackendServicesClient)
  * [`compute_cross_site_networks_v1::CrossSiteNetworksClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__cross__site__networks__v1_1_1CrossSiteNetworksClient)
  * [`compute_disk_types_v1::DiskTypesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__disk__types__v1_1_1DiskTypesClient)
  * [`compute_disks_v1::DisksClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__disks__v1_1_1DisksClient)
  * [`compute_external_vpn_gateways_v1::ExternalVpnGatewaysClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__external__vpn__gateways__v1_1_1ExternalVpnGatewaysClient)
  * [`compute_firewall_policies_v1::FirewallPoliciesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__firewall__policies__v1_1_1FirewallPoliciesClient)
  * [`compute_firewalls_v1::FirewallsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__firewalls__v1_1_1FirewallsClient)
  * [`compute_forwarding_rules_v1::ForwardingRulesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__forwarding__rules__v1_1_1ForwardingRulesClient)
  * [`compute_global_addresses_v1::GlobalAddressesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__global__addresses__v1_1_1GlobalAddressesClient)
  * [`compute_global_forwarding_rules_v1::GlobalForwardingRulesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__global__forwarding__rules__v1_1_1GlobalForwardingRulesClient)
  * [`compute_global_frontend_settings_v1::GlobalFrontendSettingsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__global__frontend__settings__v1_1_1GlobalFrontendSettingsClient)
  * [`compute_global_network_endpoint_groups_v1::GlobalNetworkEndpointGroupsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__global__network__endpoint__groups__v1_1_1GlobalNetworkEndpointGroupsClient)
  * [`compute_global_operations_v1::GlobalOperationsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__global__operations__v1_1_1GlobalOperationsClient)
  * [`compute_global_organization_operations_v1::GlobalOrganizationOperationsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__global__organization__operations__v1_1_1GlobalOrganizationOperationsClient)
  * [`compute_global_public_delegated_prefixes_v1::GlobalPublicDelegatedPrefixesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__global__public__delegated__prefixes__v1_1_1GlobalPublicDelegatedPrefixesClient)
  * [`compute_global_vm_extension_policies_v1::GlobalVmExtensionPoliciesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__global__vm__extension__policies__v1_1_1GlobalVmExtensionPoliciesClient)
  * [`compute_health_checks_v1::HealthChecksClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__health__checks__v1_1_1HealthChecksClient)
  * [`compute_hosts_v1::HostsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__hosts__v1_1_1HostsClient)
  * [`compute_http_health_checks_v1::HttpHealthChecksClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__http__health__checks__v1_1_1HttpHealthChecksClient)
  * [`compute_https_health_checks_v1::HttpsHealthChecksClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__https__health__checks__v1_1_1HttpsHealthChecksClient)
  * [`compute_image_family_views_v1::ImageFamilyViewsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__image__family__views__v1_1_1ImageFamilyViewsClient)
  * [`compute_image_views_v1::ImageViewsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__image__views__v1_1_1ImageViewsClient)
  * [`compute_images_v1::ImagesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__images__v1_1_1ImagesClient)
  * [`compute_instance_group_manager_resize_requests_v1::InstanceGroupManagerResizeRequestsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__instance__group__manager__resize__requests__v1_1_1InstanceGroupManagerResizeRequestsClient)
  * [`compute_instance_group_managers_v1::InstanceGroupManagersClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__instance__group__managers__v1_1_1InstanceGroupManagersClient)
  * [`compute_instance_groups_v1::InstanceGroupsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__instance__groups__v1_1_1InstanceGroupsClient)
  * [`compute_instance_settings_v1::InstanceSettingsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__instance__settings__v1_1_1InstanceSettingsClient)
  * [`compute_instance_templates_v1::InstanceTemplatesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__instance__templates__v1_1_1InstanceTemplatesClient)
  * [`compute_instances_v1::InstancesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__instances__v1_1_1InstancesClient)
  * [`compute_instant_snapshot_groups_v1::InstantSnapshotGroupsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__instant__snapshot__groups__v1_1_1InstantSnapshotGroupsClient)
  * [`compute_instant_snapshots_v1::InstantSnapshotsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__instant__snapshots__v1_1_1InstantSnapshotsClient)
  * [`compute_interconnect_attachment_groups_v1::InterconnectAttachmentGroupsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__interconnect__attachment__groups__v1_1_1InterconnectAttachmentGroupsClient)
  * [`compute_interconnect_attachments_v1::InterconnectAttachmentsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__interconnect__attachments__v1_1_1InterconnectAttachmentsClient)
  * [`compute_interconnect_groups_v1::InterconnectGroupsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__interconnect__groups__v1_1_1InterconnectGroupsClient)
  * [`compute_interconnect_locations_v1::InterconnectLocationsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__interconnect__locations__v1_1_1InterconnectLocationsClient)
  * [`compute_interconnect_remote_locations_v1::InterconnectRemoteLocationsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__interconnect__remote__locations__v1_1_1InterconnectRemoteLocationsClient)
  * [`compute_interconnects_v1::InterconnectsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__interconnects__v1_1_1InterconnectsClient)
  * [`compute_license_codes_v1::LicenseCodesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__license__codes__v1_1_1LicenseCodesClient)
  * [`compute_licenses_v1::LicensesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__licenses__v1_1_1LicensesClient)
  * [`compute_machine_images_v1::MachineImagesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__machine__images__v1_1_1MachineImagesClient)
  * [`compute_machine_types_v1::MachineTypesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__machine__types__v1_1_1MachineTypesClient)
  * [`compute_managed_rulesets_v1::ManagedRulesetsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__managed__rulesets__v1_1_1ManagedRulesetsClient)
  * [`compute_network_attachments_v1::NetworkAttachmentsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__network__attachments__v1_1_1NetworkAttachmentsClient)
  * [`compute_network_edge_security_services_v1::NetworkEdgeSecurityServicesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__network__edge__security__services__v1_1_1NetworkEdgeSecurityServicesClient)
  * [`compute_network_endpoint_groups_v1::NetworkEndpointGroupsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__network__endpoint__groups__v1_1_1NetworkEndpointGroupsClient)
  * [`compute_network_firewall_policies_v1::NetworkFirewallPoliciesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__network__firewall__policies__v1_1_1NetworkFirewallPoliciesClient)
  * [`compute_network_profiles_v1::NetworkProfilesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__network__profiles__v1_1_1NetworkProfilesClient)
  * [`compute_networks_v1::NetworksClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__networks__v1_1_1NetworksClient)
  * [`compute_node_groups_v1::NodeGroupsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__node__groups__v1_1_1NodeGroupsClient)
  * [`compute_node_templates_v1::NodeTemplatesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__node__templates__v1_1_1NodeTemplatesClient)
  * [`compute_node_types_v1::NodeTypesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__node__types__v1_1_1NodeTypesClient)
  * [`compute_organization_security_policies_v1::OrganizationSecurityPoliciesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__organization__security__policies__v1_1_1OrganizationSecurityPoliciesClient)
  * [`compute_packet_mirrorings_v1::PacketMirroringsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__packet__mirrorings__v1_1_1PacketMirroringsClient)
  * [`compute_preview_features_v1::PreviewFeaturesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__preview__features__v1_1_1PreviewFeaturesClient)
  * [`compute_project_views_v1::ProjectViewsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__project__views__v1_1_1ProjectViewsClient)
  * [`compute_projects_v1::ProjectsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__projects__v1_1_1ProjectsClient)
  * [`compute_public_advertised_prefixes_v1::PublicAdvertisedPrefixesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__public__advertised__prefixes__v1_1_1PublicAdvertisedPrefixesClient)
  * [`compute_public_delegated_prefixes_v1::PublicDelegatedPrefixesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__public__delegated__prefixes__v1_1_1PublicDelegatedPrefixesClient)
  * [`compute_region_autoscalers_v1::RegionAutoscalersClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__autoscalers__v1_1_1RegionAutoscalersClient)
  * [`compute_region_backend_buckets_v1::RegionBackendBucketsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__backend__buckets__v1_1_1RegionBackendBucketsClient)
  * [`compute_region_backend_services_v1::RegionBackendServicesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__backend__services__v1_1_1RegionBackendServicesClient)
  * [`compute_region_commitments_v1::RegionCommitmentsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__commitments__v1_1_1RegionCommitmentsClient)
  * [`compute_region_composite_health_checks_v1::RegionCompositeHealthChecksClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__composite__health__checks__v1_1_1RegionCompositeHealthChecksClient)
  * [`compute_region_disk_types_v1::RegionDiskTypesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__disk__types__v1_1_1RegionDiskTypesClient)
  * [`compute_region_disks_v1::RegionDisksClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__disks__v1_1_1RegionDisksClient)
  * [`compute_region_health_aggregation_policies_v1::RegionHealthAggregationPoliciesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__health__aggregation__policies__v1_1_1RegionHealthAggregationPoliciesClient)
  * [`compute_region_health_check_services_v1::RegionHealthCheckServicesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__health__check__services__v1_1_1RegionHealthCheckServicesClient)
  * [`compute_region_health_checks_v1::RegionHealthChecksClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__health__checks__v1_1_1RegionHealthChecksClient)
  * [`compute_region_health_sources_v1::RegionHealthSourcesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__health__sources__v1_1_1RegionHealthSourcesClient)
  * [`compute_region_instance_group_manager_resize_requests_v1::RegionInstanceGroupManagerResizeRequestsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__instance__group__manager__resize__requests__v1_1_1Regio144dfd969c716fd0d06fb46a6f025906)
  * [`compute_region_instance_group_managers_v1::RegionInstanceGroupManagersClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__instance__group__managers__v1_1_1RegionInstanceGroupManagersClient)
  * [`compute_region_instance_groups_v1::RegionInstanceGroupsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__instance__groups__v1_1_1RegionInstanceGroupsClient)
  * [`compute_region_instance_templates_v1::RegionInstanceTemplatesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__instance__templates__v1_1_1RegionInstanceTemplatesClient)
  * [`compute_region_instances_v1::RegionInstancesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__instances__v1_1_1RegionInstancesClient)
  * [`compute_region_instant_snapshot_groups_v1::RegionInstantSnapshotGroupsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__instant__snapshot__groups__v1_1_1RegionInstantSnapshotGroupsClient)
  * [`compute_region_instant_snapshots_v1::RegionInstantSnapshotsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__instant__snapshots__v1_1_1RegionInstantSnapshotsClient)
  * [`compute_region_network_endpoint_groups_v1::RegionNetworkEndpointGroupsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__network__endpoint__groups__v1_1_1RegionNetworkEndpointGroupsClient)
  * [`compute_region_network_firewall_policies_v1::RegionNetworkFirewallPoliciesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__network__firewall__policies__v1_1_1RegionNetworkFirewallPoliciesClient)
  * [`compute_region_notification_endpoints_v1::RegionNotificationEndpointsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__notification__endpoints__v1_1_1RegionNotificationEndpointsClient)
  * [`compute_region_operations_v1::RegionOperationsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__operations__v1_1_1RegionOperationsClient)
  * [`compute_region_security_policies_v1::RegionSecurityPoliciesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__security__policies__v1_1_1RegionSecurityPoliciesClient)
  * [`compute_region_snapshot_settings_v1::RegionSnapshotSettingsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__snapshot__settings__v1_1_1RegionSnapshotSettingsClient)
  * [`compute_region_snapshots_v1::RegionSnapshotsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__snapshots__v1_1_1RegionSnapshotsClient)
  * [`compute_region_ssl_certificates_v1::RegionSslCertificatesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__ssl__certificates__v1_1_1RegionSslCertificatesClient)
  * [`compute_region_ssl_policies_v1::RegionSslPoliciesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__ssl__policies__v1_1_1RegionSslPoliciesClient)
  * [`compute_region_target_http_proxies_v1::RegionTargetHttpProxiesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__target__http__proxies__v1_1_1RegionTargetHttpProxiesClient)
  * [`compute_region_target_https_proxies_v1::RegionTargetHttpsProxiesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__target__https__proxies__v1_1_1RegionTargetHttpsProxiesClient)
  * [`compute_region_target_tcp_proxies_v1::RegionTargetTcpProxiesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__target__tcp__proxies__v1_1_1RegionTargetTcpProxiesClient)
  * [`compute_region_url_maps_v1::RegionUrlMapsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__url__maps__v1_1_1RegionUrlMapsClient)
  * [`compute_region_zones_v1::RegionZonesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__zones__v1_1_1RegionZonesClient)
  * [`compute_regions_v1::RegionsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__regions__v1_1_1RegionsClient)
  * [`compute_reliability_risks_v1::ReliabilityRisksClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__reliability__risks__v1_1_1ReliabilityRisksClient)
  * [`compute_reservation_blocks_v1::ReservationBlocksClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__reservation__blocks__v1_1_1ReservationBlocksClient)
  * [`compute_reservation_slots_v1::ReservationSlotsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__reservation__slots__v1_1_1ReservationSlotsClient)
  * [`compute_reservation_sub_blocks_v1::ReservationSubBlocksClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__reservation__sub__blocks__v1_1_1ReservationSubBlocksClient)
  * [`compute_reservations_v1::ReservationsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__reservations__v1_1_1ReservationsClient)
  * [`compute_resource_policies_v1::ResourcePoliciesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__resource__policies__v1_1_1ResourcePoliciesClient)
  * [`compute_rollout_plans_v1::RolloutPlansClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__rollout__plans__v1_1_1RolloutPlansClient)
  * [`compute_rollouts_v1::RolloutsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__rollouts__v1_1_1RolloutsClient)
  * [`compute_routers_v1::RoutersClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__routers__v1_1_1RoutersClient)
  * [`compute_routes_v1::RoutesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__routes__v1_1_1RoutesClient)
  * [`compute_security_policies_v1::SecurityPoliciesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__security__policies__v1_1_1SecurityPoliciesClient)
  * [`compute_service_attachments_v1::ServiceAttachmentsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__service__attachments__v1_1_1ServiceAttachmentsClient)
  * [`compute_snapshot_settings_v1::SnapshotSettingsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__snapshot__settings__v1_1_1SnapshotSettingsClient)
  * [`compute_snapshots_v1::SnapshotsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__snapshots__v1_1_1SnapshotsClient)
  * [`compute_ssl_certificates_v1::SslCertificatesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__ssl__certificates__v1_1_1SslCertificatesClient)
  * [`compute_ssl_policies_v1::SslPoliciesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__ssl__policies__v1_1_1SslPoliciesClient)
  * [`compute_storage_pool_types_v1::StoragePoolTypesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__storage__pool__types__v1_1_1StoragePoolTypesClient)
  * [`compute_storage_pools_v1::StoragePoolsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__storage__pools__v1_1_1StoragePoolsClient)
  * [`compute_subnetworks_v1::SubnetworksClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__subnetworks__v1_1_1SubnetworksClient)
  * [`compute_target_grpc_proxies_v1::TargetGrpcProxiesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__target__grpc__proxies__v1_1_1TargetGrpcProxiesClient)
  * [`compute_target_http_proxies_v1::TargetHttpProxiesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__target__http__proxies__v1_1_1TargetHttpProxiesClient)
  * [`compute_target_https_proxies_v1::TargetHttpsProxiesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__target__https__proxies__v1_1_1TargetHttpsProxiesClient)
  * [`compute_target_instances_v1::TargetInstancesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__target__instances__v1_1_1TargetInstancesClient)
  * [`compute_target_pools_v1::TargetPoolsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__target__pools__v1_1_1TargetPoolsClient)
  * [`compute_target_ssl_proxies_v1::TargetSslProxiesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__target__ssl__proxies__v1_1_1TargetSslProxiesClient)
  * [`compute_target_tcp_proxies_v1::TargetTcpProxiesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__target__tcp__proxies__v1_1_1TargetTcpProxiesClient)
  * [`compute_target_vpn_gateways_v1::TargetVpnGatewaysClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__target__vpn__gateways__v1_1_1TargetVpnGatewaysClient)
  * [`compute_url_maps_v1::UrlMapsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__url__maps__v1_1_1UrlMapsClient)
  * [`compute_vpn_gateways_v1::VpnGatewaysClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__vpn__gateways__v1_1_1VpnGatewaysClient)
  * [`compute_vpn_tunnels_v1::VpnTunnelsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__vpn__tunnels__v1_1_1VpnTunnelsClient)
  * [`compute_wire_groups_v1::WireGroupsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__wire__groups__v1_1_1WireGroupsClient)
  * [`compute_zone_operations_v1::ZoneOperationsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__zone__operations__v1_1_1ZoneOperationsClient)
  * [`compute_zone_vm_extension_policies_v1::ZoneVmExtensionPoliciesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__zone__vm__extension__policies__v1_1_1ZoneVmExtensionPoliciesClient)
  * [`compute_zones_v1::ZonesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__zones__v1_1_1ZonesClient)



### More Information

  * [Error Handling](https://docs.cloud.google.com/cpp/docs/reference/common/latest/common-error-handling.html) \- describes how the library reports errors.
  * [How to Override the Default Endpoint](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute-override-endpoint) \- describes how to override the default endpoint.
  * [How to Override the Authentication Credentials](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute-override-authentication) \- describes how to change the authentication credentials used by the library.
  * [Override Retry, Backoff, and Idempotency Policies](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute-override-retry) \- describes how to change the default retry policies.
  * [Environment Variables](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute-env) \- describes environment variables that can configure the behavior of the library.
  * [How to Override the Default Universe Domain](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute-override-universe-domain) \- describes how to override the default universe domain. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
