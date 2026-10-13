---
url: https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute-override-retry/
title: Override Retry, Backoff, and Idempotency Policies \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:14:49.730631+00:00
---

# Override Retry, Backoff, and Idempotency Policies  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute-override-retry/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Override Retry, Backoff, and Idempotency Policies Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1 

When it is safe to do so, the library automatically retries requests that fail due to a transient error. The library then uses [exponential backoff](https://en.wikipedia.org/wiki/Exponential_backoff) to backoff before trying again. Which operations are considered safe to retry, which errors are treated as transient failures, the details of the exponential backoff algorithm, and for how long the library retries are all configurable via policies.

This document provides examples showing how to override the default policies.

The policies can be set when the `*Connection` object is created. The library provides default policies for any policy that is not set. The application can also override some (or all) policies when the `*Client` object is created. This can be useful if multiple `*Client` objects share the same `*Connection` object, but you want different retry behavior in some of the clients. Finally, the application can override some retry policies when calling a specific member function.

The library uses three different options to control the retry loop. The options have per-client names.

## Configuring the transient errors and retry duration

The `*RetryPolicyOption` controls:

  * Which errors are to be treated as transient errors.
  * How long the library will keep retrying transient errors.



You can provide your own class for this option. The library also provides two built-in policies:

  * `*LimitedErrorCountRetryPolicy`: stops retrying after a specified number of transient errors.
  * `*LimitedTimeRetryPolicy`: stops retrying after a specified time.



Note that a library may have more than one version of these classes. Their name match the `*Client` and `*Connection` object they are intended to be used with. Some `*Client` objects treat different error codes as transient errors. In most cases, only [kUnavailable](https://docs.cloud.google.com/cpp/docs/reference/common/latest/namespacegoogle_1_1cloud_1a90e17f75452470f0f3ee1a06ffe58847.html) is treated as a transient error.

## Controlling the backoff algorithm

The `*BackoffPolicyOption` controls how long the client library will wait before retrying a request that failed with a transient error. You can provide your own class for this option.

The only built-in backoff policy is [`ExponentialBackoffPolicy`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/namespacegoogle_1_1cloud.html). This class implements a truncated exponential backoff algorithm, with jitter. In summary, it doubles the current backoff time after each failure. The actual backoff time for an RPC is chosen at random, but never exceeds the current backoff. The current backoff is doubled after each failure, but never exceeds (or is "truncated") if it reaches a prescribed maximum.

## Controlling which operations are retryable

The `*IdempotencyPolicyOption` controls which requests are retryable, as some requests are never safe to retry.

Only one built-in idempotency policy is provided by the library. The name matches the name of the client it is intended for. For example, `FooBarClient` will use `FooBarIdempotencyPolicy`. This policy is very conservative.

## Example

For example, this will override the retry policies for `compute_accelerator_types_v1::AcceleratorTypesClient`:
    
    
      auto options =
          google::cloud::Options{}
              .set<google::cloud::compute_accelerator_types_v1::
                       AcceleratorTypesConnectionIdempotencyPolicyOption>(
                  CustomIdempotencyPolicy().clone())
              .set<google::cloud::compute_accelerator_types_v1::
                       AcceleratorTypesRetryPolicyOption>(
                  google::cloud::compute_accelerator_types_v1::
                      AcceleratorTypesLimitedErrorCountRetryPolicy(3)
                          .clone())
              .set<google::cloud::compute_accelerator_types_v1::
                       AcceleratorTypesBackoffPolicyOption>(
                  google::cloud::ExponentialBackoffPolicy(
                      /*initial_delay=*/std::chrono::milliseconds(200),
                      /*maximum_delay=*/std::chrono::seconds(45),
                      /*scaling=*/2.0)
                      .clone());
      auto connection = google::cloud::compute_accelerator_types_v1::
          MakeAcceleratorTypesConnectionRest(options);
    
      // c1 and c2 share the same retry policies
      auto c1 = google::cloud::compute_accelerator_types_v1::AcceleratorTypesClient(
          connection);
      auto c2 = google::cloud::compute_accelerator_types_v1::AcceleratorTypesClient(
          connection);
    
      // You can override any of the policies in a new client. This new client
      // will share the policies from c1 (or c2) *except* for the retry policy.
      auto c3 = google::cloud::compute_accelerator_types_v1::AcceleratorTypesClient(
          connection, google::cloud::Options{}
                          .set<google::cloud::compute_accelerator_types_v1::
                                   AcceleratorTypesRetryPolicyOption>(
                              google::cloud::compute_accelerator_types_v1::
                                  AcceleratorTypesLimitedTimeRetryPolicy(
                                      std::chrono::minutes(5))
                                      .clone()));
    
      // You can also override the policies in a single call:
      // c3.SomeRpc(..., google::cloud::Options{}
      //     .set<google::cloud::compute_accelerator_types_v1::AcceleratorTypesRetryPolicyOption>(
      //       google::cloud::compute_accelerator_types_v1::AcceleratorTypesLimitedErrorCountRetryPolicy(10).clone()));
    

This assumes you have created a custom idempotency policy. Such as:
    
    
    class CustomIdempotencyPolicy
        : public google::cloud::compute_accelerator_types_v1::
              AcceleratorTypesConnectionIdempotencyPolicy {
     public:
      ~CustomIdempotencyPolicy() override = default;
      std::unique_ptr<google::cloud::compute_accelerator_types_v1::
                          AcceleratorTypesConnectionIdempotencyPolicy>
      clone() const override {
        return std::make_unique<CustomIdempotencyPolicy>(*this);
      }
      // Override inherited functions to define as needed.
    };
    

Follow these links to find examples for other `*Client` classes:

  * [`compute_accelerator_types_v1::AcceleratorTypesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_accelerator_types_v1_1_1AcceleratorTypesClient-retry-snippet)
  * [`compute_addresses_v1::AddressesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_addresses_v1_1_1AddressesClient-retry-snippet)
  * [`compute_advice_v1::AdviceClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_advice_v1_1_1AdviceClient-retry-snippet)
  * [`compute_autoscalers_v1::AutoscalersClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_autoscalers_v1_1_1AutoscalersClient-retry-snippet)
  * [`compute_backend_buckets_v1::BackendBucketsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_backend_buckets_v1_1_1BackendBucketsClient-retry-snippet)
  * [`compute_backend_services_v1::BackendServicesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_backend_services_v1_1_1BackendServicesClient-retry-snippet)
  * [`compute_cross_site_networks_v1::CrossSiteNetworksClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_cross_site_networks_v1_1_1CrossSiteNetworksClient-retry-snippet)
  * [`compute_disk_types_v1::DiskTypesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_disk_types_v1_1_1DiskTypesClient-retry-snippet)
  * [`compute_disks_v1::DisksClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_disks_v1_1_1DisksClient-retry-snippet)
  * [`compute_external_vpn_gateways_v1::ExternalVpnGatewaysClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_external_vpn_gateways_v1_1_1ExternalVpnGatewaysClient-retry-snippet)
  * [`compute_firewall_policies_v1::FirewallPoliciesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_firewall_policies_v1_1_1FirewallPoliciesClient-retry-snippet)
  * [`compute_firewalls_v1::FirewallsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_firewalls_v1_1_1FirewallsClient-retry-snippet)
  * [`compute_forwarding_rules_v1::ForwardingRulesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_forwarding_rules_v1_1_1ForwardingRulesClient-retry-snippet)
  * [`compute_global_addresses_v1::GlobalAddressesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_global_addresses_v1_1_1GlobalAddressesClient-retry-snippet)
  * [`compute_global_forwarding_rules_v1::GlobalForwardingRulesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_global_forwarding_rules_v1_1_1GlobalForwardingRulesClient-retry-snippet)
  * [`compute_global_frontend_settings_v1::GlobalFrontendSettingsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_global_frontend_settings_v1_1_1GlobalFrontendSettingsClient-retry-snippet)
  * [`compute_global_network_endpoint_groups_v1::GlobalNetworkEndpointGroupsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_global_network_endpoint_groups_v1_1_1GlobalNetworkEndpointGroupsClient-retry-snippet)
  * [`compute_global_operations_v1::GlobalOperationsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_global_operations_v1_1_1GlobalOperationsClient-retry-snippet)
  * [`compute_global_organization_operations_v1::GlobalOrganizationOperationsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_global_organization_operations_v1_1_1GlobalOrganizationOperationsClient-retry-snippet)
  * [`compute_global_public_delegated_prefixes_v1::GlobalPublicDelegatedPrefixesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_global_public_delegated_prefixes_v1_1_1GlobalPublicDelegatedPrefixesClient-retry-snippet)
  * [`compute_global_vm_extension_policies_v1::GlobalVmExtensionPoliciesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_global_vm_extension_policies_v1_1_1GlobalVmExtensionPoliciesClient-retry-snippet)
  * [`compute_health_checks_v1::HealthChecksClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_health_checks_v1_1_1HealthChecksClient-retry-snippet)
  * [`compute_hosts_v1::HostsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_hosts_v1_1_1HostsClient-retry-snippet)
  * [`compute_http_health_checks_v1::HttpHealthChecksClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_http_health_checks_v1_1_1HttpHealthChecksClient-retry-snippet)
  * [`compute_https_health_checks_v1::HttpsHealthChecksClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_https_health_checks_v1_1_1HttpsHealthChecksClient-retry-snippet)
  * [`compute_image_family_views_v1::ImageFamilyViewsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_image_family_views_v1_1_1ImageFamilyViewsClient-retry-snippet)
  * [`compute_image_views_v1::ImageViewsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_image_views_v1_1_1ImageViewsClient-retry-snippet)
  * [`compute_images_v1::ImagesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_images_v1_1_1ImagesClient-retry-snippet)
  * [`compute_instance_group_manager_resize_requests_v1::InstanceGroupManagerResizeRequestsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_instance_group_manager_resize_requests_v1_1_1InstanceGroupManagerResizeRequestsClient-retry-snippet)
  * [`compute_instance_group_managers_v1::InstanceGroupManagersClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_instance_group_managers_v1_1_1InstanceGroupManagersClient-retry-snippet)
  * [`compute_instance_groups_v1::InstanceGroupsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_instance_groups_v1_1_1InstanceGroupsClient-retry-snippet)
  * [`compute_instance_settings_v1::InstanceSettingsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_instance_settings_v1_1_1InstanceSettingsClient-retry-snippet)
  * [`compute_instance_templates_v1::InstanceTemplatesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_instance_templates_v1_1_1InstanceTemplatesClient-retry-snippet)
  * [`compute_instances_v1::InstancesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_instances_v1_1_1InstancesClient-retry-snippet)
  * [`compute_instant_snapshot_groups_v1::InstantSnapshotGroupsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_instant_snapshot_groups_v1_1_1InstantSnapshotGroupsClient-retry-snippet)
  * [`compute_instant_snapshots_v1::InstantSnapshotsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_instant_snapshots_v1_1_1InstantSnapshotsClient-retry-snippet)
  * [`compute_interconnect_attachment_groups_v1::InterconnectAttachmentGroupsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_interconnect_attachment_groups_v1_1_1InterconnectAttachmentGroupsClient-retry-snippet)
  * [`compute_interconnect_attachments_v1::InterconnectAttachmentsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_interconnect_attachments_v1_1_1InterconnectAttachmentsClient-retry-snippet)
  * [`compute_interconnect_groups_v1::InterconnectGroupsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_interconnect_groups_v1_1_1InterconnectGroupsClient-retry-snippet)
  * [`compute_interconnect_locations_v1::InterconnectLocationsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_interconnect_locations_v1_1_1InterconnectLocationsClient-retry-snippet)
  * [`compute_interconnect_remote_locations_v1::InterconnectRemoteLocationsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_interconnect_remote_locations_v1_1_1InterconnectRemoteLocationsClient-retry-snippet)
  * [`compute_interconnects_v1::InterconnectsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_interconnects_v1_1_1InterconnectsClient-retry-snippet)
  * [`compute_license_codes_v1::LicenseCodesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_license_codes_v1_1_1LicenseCodesClient-retry-snippet)
  * [`compute_licenses_v1::LicensesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_licenses_v1_1_1LicensesClient-retry-snippet)
  * [`compute_machine_images_v1::MachineImagesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_machine_images_v1_1_1MachineImagesClient-retry-snippet)
  * [`compute_machine_types_v1::MachineTypesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_machine_types_v1_1_1MachineTypesClient-retry-snippet)
  * [`compute_managed_rulesets_v1::ManagedRulesetsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_managed_rulesets_v1_1_1ManagedRulesetsClient-retry-snippet)
  * [`compute_network_attachments_v1::NetworkAttachmentsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_network_attachments_v1_1_1NetworkAttachmentsClient-retry-snippet)
  * [`compute_network_edge_security_services_v1::NetworkEdgeSecurityServicesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_network_edge_security_services_v1_1_1NetworkEdgeSecurityServicesClient-retry-snippet)
  * [`compute_network_endpoint_groups_v1::NetworkEndpointGroupsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_network_endpoint_groups_v1_1_1NetworkEndpointGroupsClient-retry-snippet)
  * [`compute_network_firewall_policies_v1::NetworkFirewallPoliciesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_network_firewall_policies_v1_1_1NetworkFirewallPoliciesClient-retry-snippet)
  * [`compute_network_profiles_v1::NetworkProfilesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_network_profiles_v1_1_1NetworkProfilesClient-retry-snippet)
  * [`compute_networks_v1::NetworksClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_networks_v1_1_1NetworksClient-retry-snippet)
  * [`compute_node_groups_v1::NodeGroupsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_node_groups_v1_1_1NodeGroupsClient-retry-snippet)
  * [`compute_node_templates_v1::NodeTemplatesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_node_templates_v1_1_1NodeTemplatesClient-retry-snippet)
  * [`compute_node_types_v1::NodeTypesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_node_types_v1_1_1NodeTypesClient-retry-snippet)
  * [`compute_organization_security_policies_v1::OrganizationSecurityPoliciesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_organization_security_policies_v1_1_1OrganizationSecurityPoliciesClient-retry-snippet)
  * [`compute_packet_mirrorings_v1::PacketMirroringsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_packet_mirrorings_v1_1_1PacketMirroringsClient-retry-snippet)
  * [`compute_preview_features_v1::PreviewFeaturesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_preview_features_v1_1_1PreviewFeaturesClient-retry-snippet)
  * [`compute_project_views_v1::ProjectViewsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_project_views_v1_1_1ProjectViewsClient-retry-snippet)
  * [`compute_projects_v1::ProjectsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_projects_v1_1_1ProjectsClient-retry-snippet)
  * [`compute_public_advertised_prefixes_v1::PublicAdvertisedPrefixesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_public_advertised_prefixes_v1_1_1PublicAdvertisedPrefixesClient-retry-snippet)
  * [`compute_public_delegated_prefixes_v1::PublicDelegatedPrefixesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_public_delegated_prefixes_v1_1_1PublicDelegatedPrefixesClient-retry-snippet)
  * [`compute_region_autoscalers_v1::RegionAutoscalersClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_autoscalers_v1_1_1RegionAutoscalersClient-retry-snippet)
  * [`compute_region_backend_buckets_v1::RegionBackendBucketsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_backend_buckets_v1_1_1RegionBackendBucketsClient-retry-snippet)
  * [`compute_region_backend_services_v1::RegionBackendServicesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_backend_services_v1_1_1RegionBackendServicesClient-retry-snippet)
  * [`compute_region_commitments_v1::RegionCommitmentsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_commitments_v1_1_1RegionCommitmentsClient-retry-snippet)
  * [`compute_region_composite_health_checks_v1::RegionCompositeHealthChecksClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_composite_health_checks_v1_1_1RegionCompositeHealthChecksClient-retry-snippet)
  * [`compute_region_disk_types_v1::RegionDiskTypesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_disk_types_v1_1_1RegionDiskTypesClient-retry-snippet)
  * [`compute_region_disks_v1::RegionDisksClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_disks_v1_1_1RegionDisksClient-retry-snippet)
  * [`compute_region_health_aggregation_policies_v1::RegionHealthAggregationPoliciesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_health_aggregation_policies_v1_1_1RegionHealthAggregationPoliciesClient-retry-snippet)
  * [`compute_region_health_check_services_v1::RegionHealthCheckServicesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_health_check_services_v1_1_1RegionHealthCheckServicesClient-retry-snippet)
  * [`compute_region_health_checks_v1::RegionHealthChecksClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_health_checks_v1_1_1RegionHealthChecksClient-retry-snippet)
  * [`compute_region_health_sources_v1::RegionHealthSourcesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_health_sources_v1_1_1RegionHealthSourcesClient-retry-snippet)
  * [`compute_region_instance_group_manager_resize_requests_v1::RegionInstanceGroupManagerResizeRequestsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_instance_group_manager_resize_requests_v1_1_1RegionInstanceGroupManagerResizeRequestsClient-retry-snippet)
  * [`compute_region_instance_group_managers_v1::RegionInstanceGroupManagersClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_instance_group_managers_v1_1_1RegionInstanceGroupManagersClient-retry-snippet)
  * [`compute_region_instance_groups_v1::RegionInstanceGroupsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_instance_groups_v1_1_1RegionInstanceGroupsClient-retry-snippet)
  * [`compute_region_instance_templates_v1::RegionInstanceTemplatesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_instance_templates_v1_1_1RegionInstanceTemplatesClient-retry-snippet)
  * [`compute_region_instances_v1::RegionInstancesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_instances_v1_1_1RegionInstancesClient-retry-snippet)
  * [`compute_region_instant_snapshot_groups_v1::RegionInstantSnapshotGroupsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_instant_snapshot_groups_v1_1_1RegionInstantSnapshotGroupsClient-retry-snippet)
  * [`compute_region_instant_snapshots_v1::RegionInstantSnapshotsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_instant_snapshots_v1_1_1RegionInstantSnapshotsClient-retry-snippet)
  * [`compute_region_network_endpoint_groups_v1::RegionNetworkEndpointGroupsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_network_endpoint_groups_v1_1_1RegionNetworkEndpointGroupsClient-retry-snippet)
  * [`compute_region_network_firewall_policies_v1::RegionNetworkFirewallPoliciesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_network_firewall_policies_v1_1_1RegionNetworkFirewallPoliciesClient-retry-snippet)
  * [`compute_region_notification_endpoints_v1::RegionNotificationEndpointsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_notification_endpoints_v1_1_1RegionNotificationEndpointsClient-retry-snippet)
  * [`compute_region_operations_v1::RegionOperationsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_operations_v1_1_1RegionOperationsClient-retry-snippet)
  * [`compute_region_security_policies_v1::RegionSecurityPoliciesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_security_policies_v1_1_1RegionSecurityPoliciesClient-retry-snippet)
  * [`compute_region_snapshot_settings_v1::RegionSnapshotSettingsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_snapshot_settings_v1_1_1RegionSnapshotSettingsClient-retry-snippet)
  * [`compute_region_snapshots_v1::RegionSnapshotsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_snapshots_v1_1_1RegionSnapshotsClient-retry-snippet)
  * [`compute_region_ssl_certificates_v1::RegionSslCertificatesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_ssl_certificates_v1_1_1RegionSslCertificatesClient-retry-snippet)
  * [`compute_region_ssl_policies_v1::RegionSslPoliciesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_ssl_policies_v1_1_1RegionSslPoliciesClient-retry-snippet)
  * [`compute_region_target_http_proxies_v1::RegionTargetHttpProxiesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_target_http_proxies_v1_1_1RegionTargetHttpProxiesClient-retry-snippet)
  * [`compute_region_target_https_proxies_v1::RegionTargetHttpsProxiesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_target_https_proxies_v1_1_1RegionTargetHttpsProxiesClient-retry-snippet)
  * [`compute_region_target_tcp_proxies_v1::RegionTargetTcpProxiesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_target_tcp_proxies_v1_1_1RegionTargetTcpProxiesClient-retry-snippet)
  * [`compute_region_url_maps_v1::RegionUrlMapsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_url_maps_v1_1_1RegionUrlMapsClient-retry-snippet)
  * [`compute_region_zones_v1::RegionZonesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_region_zones_v1_1_1RegionZonesClient-retry-snippet)
  * [`compute_regions_v1::RegionsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_regions_v1_1_1RegionsClient-retry-snippet)
  * [`compute_reliability_risks_v1::ReliabilityRisksClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_reliability_risks_v1_1_1ReliabilityRisksClient-retry-snippet)
  * [`compute_reservation_blocks_v1::ReservationBlocksClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_reservation_blocks_v1_1_1ReservationBlocksClient-retry-snippet)
  * [`compute_reservation_slots_v1::ReservationSlotsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_reservation_slots_v1_1_1ReservationSlotsClient-retry-snippet)
  * [`compute_reservation_sub_blocks_v1::ReservationSubBlocksClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_reservation_sub_blocks_v1_1_1ReservationSubBlocksClient-retry-snippet)
  * [`compute_reservations_v1::ReservationsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_reservations_v1_1_1ReservationsClient-retry-snippet)
  * [`compute_resource_policies_v1::ResourcePoliciesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_resource_policies_v1_1_1ResourcePoliciesClient-retry-snippet)
  * [`compute_rollout_plans_v1::RolloutPlansClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_rollout_plans_v1_1_1RolloutPlansClient-retry-snippet)
  * [`compute_rollouts_v1::RolloutsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_rollouts_v1_1_1RolloutsClient-retry-snippet)
  * [`compute_routers_v1::RoutersClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_routers_v1_1_1RoutersClient-retry-snippet)
  * [`compute_routes_v1::RoutesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_routes_v1_1_1RoutesClient-retry-snippet)
  * [`compute_security_policies_v1::SecurityPoliciesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_security_policies_v1_1_1SecurityPoliciesClient-retry-snippet)
  * [`compute_service_attachments_v1::ServiceAttachmentsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_service_attachments_v1_1_1ServiceAttachmentsClient-retry-snippet)
  * [`compute_snapshot_settings_v1::SnapshotSettingsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_snapshot_settings_v1_1_1SnapshotSettingsClient-retry-snippet)
  * [`compute_snapshots_v1::SnapshotsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_snapshots_v1_1_1SnapshotsClient-retry-snippet)
  * [`compute_ssl_certificates_v1::SslCertificatesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_ssl_certificates_v1_1_1SslCertificatesClient-retry-snippet)
  * [`compute_ssl_policies_v1::SslPoliciesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_ssl_policies_v1_1_1SslPoliciesClient-retry-snippet)
  * [`compute_storage_pool_types_v1::StoragePoolTypesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_storage_pool_types_v1_1_1StoragePoolTypesClient-retry-snippet)
  * [`compute_storage_pools_v1::StoragePoolsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_storage_pools_v1_1_1StoragePoolsClient-retry-snippet)
  * [`compute_subnetworks_v1::SubnetworksClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_subnetworks_v1_1_1SubnetworksClient-retry-snippet)
  * [`compute_target_grpc_proxies_v1::TargetGrpcProxiesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_target_grpc_proxies_v1_1_1TargetGrpcProxiesClient-retry-snippet)
  * [`compute_target_http_proxies_v1::TargetHttpProxiesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_target_http_proxies_v1_1_1TargetHttpProxiesClient-retry-snippet)
  * [`compute_target_https_proxies_v1::TargetHttpsProxiesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_target_https_proxies_v1_1_1TargetHttpsProxiesClient-retry-snippet)
  * [`compute_target_instances_v1::TargetInstancesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_target_instances_v1_1_1TargetInstancesClient-retry-snippet)
  * [`compute_target_pools_v1::TargetPoolsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_target_pools_v1_1_1TargetPoolsClient-retry-snippet)
  * [`compute_target_ssl_proxies_v1::TargetSslProxiesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_target_ssl_proxies_v1_1_1TargetSslProxiesClient-retry-snippet)
  * [`compute_target_tcp_proxies_v1::TargetTcpProxiesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_target_tcp_proxies_v1_1_1TargetTcpProxiesClient-retry-snippet)
  * [`compute_target_vpn_gateways_v1::TargetVpnGatewaysClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_target_vpn_gateways_v1_1_1TargetVpnGatewaysClient-retry-snippet)
  * [`compute_url_maps_v1::UrlMapsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_url_maps_v1_1_1UrlMapsClient-retry-snippet)
  * [`compute_vpn_gateways_v1::VpnGatewaysClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_vpn_gateways_v1_1_1VpnGatewaysClient-retry-snippet)
  * [`compute_vpn_tunnels_v1::VpnTunnelsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_vpn_tunnels_v1_1_1VpnTunnelsClient-retry-snippet)
  * [`compute_wire_groups_v1::WireGroupsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_wire_groups_v1_1_1WireGroupsClient-retry-snippet)
  * [`compute_zone_operations_v1::ZoneOperationsClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_zone_operations_v1_1_1ZoneOperationsClient-retry-snippet)
  * [`compute_zone_vm_extension_policies_v1::ZoneVmExtensionPoliciesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_zone_vm_extension_policies_v1_1_1ZoneVmExtensionPoliciesClient-retry-snippet)
  * [`compute_zones_v1::ZonesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/compute_zones_v1_1_1ZonesClient-retry-snippet)



## More Information

###### See Also

[`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html)

###### See Also

[`google::cloud::BackoffPolicy`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/namespacegoogle_1_1cloud.html)

###### See Also

[`google::cloud::ExponentialBackoffPolicy`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/namespacegoogle_1_1cloud.html)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
