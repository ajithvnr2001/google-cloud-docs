---
url: https://docs.cloud.google.com/compute/docs/terraform/
title: Provision Compute Engine resources with Terraform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:20.741923+00:00
---

# Provision Compute Engine resources with Terraform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/terraform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Provision Compute Engine resources with Terraform Stay organized with collections  Save and categorize content based on your preferences. 

HashiCorp Terraform is an infrastructure-as-code (IaC) tool that lets you provision and manage cloud infrastructure. Terraform provides plugins called _providers_ that let you interact with cloud providers and other APIs. You can use the _Terraform provider for Google Cloud_ to provision and manage Google Cloud resources, including Compute Engine.

This page introduces you to using Terraform with Compute Engine, including an introduction to how Terraform works and some resources to help you get started using Terraform with Google Cloud. You'll also find links to Terraform reference docs for Compute Engine, code examples, and guides for using Terraform to provision Compute Engine resources.

For instructions on how to get started with Terraform for Google Cloud, see [Install and configure Terraform](https://docs.cloud.google.com/docs/terraform/install-configure-terraform) or the [Terraform for Google Cloud quickstart](https://docs.cloud.google.com/docs/terraform/create-vm-instance).

## How Terraform works

Terraform has a declarative and configuration-oriented syntax, which you can use to describe the infrastructure that you want to provision in your Google Cloud project. After you author this configuration in one or more Terraform configuration files, you can use the Terraform CLI to apply this configuration to your Compute Engine resources.

The following steps explain how Terraform works:

  1. You describe the infrastructure you want to provision in a _Terraform configuration file_. You don't need to write code describing how to provision the infrastructure. Terraform provisions the infrastructure for you.
  2. You run the `terraform plan` command, which evaluates your configuration and generates an execution plan. You can review the plan and make changes as needed.
  3. You run the `terraform apply` command, which performs the following actions:

     1. It provisions your infrastructure based on your execution plan by invoking the corresponding Compute Engine APIs in the background.
     2. It creates a _Terraform state file_ , which is a JSON file that maps the resources in your configuration file to the resources in the real-world infrastructure. Terraform uses this file to keep a record of the most recent state of your infrastructure, and to determine when to create, update, and destroy resources.
     3. When you run `terraform apply`, Terraform uses the mapping in the state file to compare the existing infrastructure to the code, and make updates as necessary:

        * If a resource object is defined in the configuration file, but doesn't exist in the state file, Terraform creates it.
        * If a resource object exists in the state file, but has a different configuration from your configuration file, Terraform updates the resource to match your configuration file.
        * If a resource object in the state file matches your configuration file, Terraform leaves the resource unchanged.



## Terraform resources for Compute Engine

_Resources_ are the fundamental elements in the Terraform language. Each resource block describes one or more infrastructure objects, such as virtual networks or compute instances.

The following table lists the Terraform resources available for Compute Engine:

Terraform resources | Terraform data sources  
---|---  
  
  * [google_compute_address](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_address)
  * [google_compute_attached_disk](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_attached_disk)
  * [google_compute_autoscaler](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_autoscaler)
  * [google_compute_backend_bucket](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_backend_bucket)
  * [google_compute_backend_bucket_iam](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_backend_bucket_iam)
  * [google_compute_backend_bucket_signed_url_key](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_backend_bucket_signed_url_key)
  * [google_compute_backend_service](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_backend_service)
  * [google_compute_backend_service_iam](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_backend_service_iam)
  * [google_compute_backend_service_signed_url_key](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_backend_service_signed_url_key)
  * [google_compute_disk](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_disk)
  * [google_compute_disk_async_replication](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_disk_async_replication)
  * [google_compute_disk_iam](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_disk_iam)
  * [google_compute_disk_resource_policy_attachment](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_disk_resource_policy_attachment)
  * [google_compute_external_vpn_gateway](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_external_vpn_gateway)
  * [google_compute_firewall](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_firewall)
  * [google_compute_firewall_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_firewall_policy)
  * [google_compute_firewall_policy_association](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_firewall_policy_association)
  * [google_compute_firewall_policy_rule](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_firewall_policy_rule)
  * [google_compute_firewall_policy_with_rules](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_firewall_policy_with_rules)
  * [google_compute_forwarding_rule](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_forwarding_rule)
  * [google_compute_global_address](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_global_address)
  * [google_compute_global_forwarding_rule](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_global_forwarding_rule)
  * [google_compute_global_network_endpoint](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_global_network_endpoint)
  * [google_compute_global_network_endpoint_group](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_global_network_endpoint_group)
  * [google_compute_ha_vpn_gateway](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_ha_vpn_gateway)
  * [google_compute_health_check](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_health_check)
  * [google_compute_http_health_check](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_http_health_check)
  * [google_compute_https_health_check](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_https_health_check)
  * [google_compute_image](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_image)
  * [google_compute_image_iam](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_image_iam)
  * [google_compute_instance](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance)
  * [google_compute_instance_from_machine_image](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance_from_machine_image)
  * [google_compute_instance_from_template](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance_from_template)
  * [google_compute_instance_group](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance_group)
  * [google_compute_instance_group_manager](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance_group_manager)
  * [google_compute_instance_group_membership](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance_group_membership)
  * [google_compute_instance_group_named_port](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance_group_named_port)
  * [google_compute_instance_iam](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance_iam)
  * [google_compute_instance_settings](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance_settings)
  * [google_compute_instance_template](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance_template)
  * [google_compute_instance_template_iam](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance_template_iam)
  * [google_compute_instant_snapshot](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instant_snapshot)
  * [google_compute_instant_snapshot_iam](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instant_snapshot_iam)
  * [google_compute_interconnect](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_interconnect)
  * [google_compute_interconnect_attachment](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_interconnect_attachment)
  * [google_compute_machine_image](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_machine_image)
  * [google_compute_machine_image_iam](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_machine_image_iam)
  * [google_compute_managed_ssl_certificate](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_managed_ssl_certificate)
  * [google_compute_network](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_network)
  * [google_compute_network_attachment](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_network_attachment)
  * [google_compute_network_edge_security_service](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_network_edge_security_service)
  * [google_compute_network_endpoint](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_network_endpoint)
  * [google_compute_network_endpoint_group](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_network_endpoint_group)
  * [google_compute_network_endpoints](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_network_endpoints)
  * [google_compute_network_firewall_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_network_firewall_policy)
  * [google_compute_network_firewall_policy_association](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_network_firewall_policy_association)
  * [google_compute_network_firewall_policy_packet_mirroring_rule](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_network_firewall_policy_packet_mirroring_rule)
  * [google_compute_network_firewall_policy_rule](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_network_firewall_policy_rule)
  * [google_compute_network_firewall_policy_with_rules](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_network_firewall_policy_with_rules)
  * [google_compute_network_peering](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_network_peering)
  * [google_compute_network_peering_routes_config](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_network_peering_routes_config)
  * [google_compute_node_group](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_node_group)
  * [google_compute_node_template](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_node_template)
  * [google_compute_organization_security_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_organization_security_policy)
  * [google_compute_organization_security_policy_association](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_organization_security_policy_association)
  * [google_compute_organization_security_policy_rule](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_organization_security_policy_rule)
  * [google_compute_packet_mirroring](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_packet_mirroring)
  * [google_compute_per_instance_config](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_per_instance_config)
  * [google_compute_project_cloud_armor_tier](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_project_cloud_armor_tier)
  * [google_compute_project_default_network_tier](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_project_default_network_tier)
  * [google_compute_project_metadata](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_project_metadata)
  * [google_compute_project_metadata_item](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_project_metadata_item)
  * [google_compute_public_advertised_prefix](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_public_advertised_prefix)
  * [google_compute_public_delegated_prefix](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_public_delegated_prefix)
  * [google_compute_region_autoscaler](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_autoscaler)
  * [google_compute_region_backend_service](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_backend_service)
  * [google_compute_region_backend_service_iam](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_backend_service_iam)
  * [google_compute_region_commitment](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_commitment)
  * [google_compute_region_disk](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_disk)
  * [google_compute_region_disk_iam](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_disk_iam)
  * [google_compute_region_disk_resource_policy_attachment](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_disk_resource_policy_attachment)
  * [google_compute_region_health_check](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_health_check)
  * [google_compute_region_instance_group_manager](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_instance_group_manager)
  * [google_compute_region_instance_template](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_instance_template)
  * [google_compute_region_network_endpoint](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_network_endpoint)
  * [google_compute_region_network_endpoint_group](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_network_endpoint_group)
  * [google_compute_region_network_firewall_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_network_firewall_policy)
  * [google_compute_region_network_firewall_policy_association](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_network_firewall_policy_association)
  * [google_compute_region_network_firewall_policy_rule](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_network_firewall_policy_rule)
  * [google_compute_region_network_firewall_policy_with_rules](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_network_firewall_policy_with_rules)
  * [google_compute_region_per_instance_config](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_per_instance_config)
  * [google_compute_region_resize_request](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_resize_request)
  * [google_compute_region_security_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_security_policy)
  * [google_compute_region_security_policy_rule](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_security_policy_rule)
  * [google_compute_region_ssl_certificate](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_ssl_certificate)
  * [google_compute_region_ssl_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_ssl_policy)
  * [google_compute_region_target_http_proxy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_target_http_proxy)
  * [google_compute_region_target_https_proxy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_target_https_proxy)
  * [google_compute_region_target_tcp_proxy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_target_tcp_proxy)
  * [google_compute_region_url_map](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_url_map)
  * [google_compute_reservation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_reservation)
  * [google_compute_resize_request](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_resize_request)
  * [google_compute_resource_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_resource_policy)
  * [google_compute_resource_policy_attachment](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_resource_policy_attachment)
  * [google_compute_route](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_route)
  * [google_compute_router](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_router)
  * [google_compute_router_interface](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_router_interface)
  * [google_compute_router_nat](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_router_nat)
  * [google_compute_router_nat_address](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_router_nat_address)
  * [google_compute_router_peer](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_router_peer)
  * [google_compute_router_route_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_router_route_policy)
  * [google_compute_security_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_security_policy)
  * [google_compute_security_policy_rule](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_security_policy_rule)
  * [google_compute_service_attachment](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_service_attachment)
  * [google_compute_shared_vpc_host_project](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_shared_vpc_host_project)
  * [google_compute_shared_vpc_service_project](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_shared_vpc_service_project)
  * [google_compute_snapshot](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_snapshot)
  * [google_compute_snapshot_iam](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_snapshot_iam)
  * [google_compute_ssl_certificate](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_ssl_certificate)
  * [google_compute_ssl_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_ssl_policy)
  * [google_compute_storage_pool](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_storage_pool)
  * [google_compute_storage_pool_iam](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_storage_pool_iam)
  * [google_compute_subnetwork](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_subnetwork)
  * [google_compute_subnetwork_iam](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_subnetwork_iam)
  * [google_compute_target_grpc_proxy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_target_grpc_proxy)
  * [google_compute_target_http_proxy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_target_http_proxy)
  * [google_compute_target_https_proxy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_target_https_proxy)
  * [google_compute_target_instance](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_target_instance)
  * [google_compute_target_pool](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_target_pool)
  * [google_compute_target_ssl_proxy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_target_ssl_proxy)
  * [google_compute_target_tcp_proxy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_target_tcp_proxy)
  * [google_compute_url_map](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_url_map)
  * [google_compute_vpn_gateway](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_vpn_gateway)
  * [google_compute_vpn_tunnel](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_vpn_tunnel)
  * [google_project_usage_export_bucket](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/project_usage_export_bucket)

| 

  * [google_compute_address](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_address)
  * [google_compute_addresses](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_addresses)
  * [google_compute_backend_bucket](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_backend_bucket)
  * [google_compute_backend_bucket_iam_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_backend_bucket_iam_policy)
  * [google_compute_backend_service](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_backend_service)
  * [google_compute_backend_service_iam_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_backend_service_iam_policy)
  * [google_compute_default_service_account](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_default_service_account)
  * [google_compute_disk](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_disk)
  * [google_compute_disk_iam_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_disk_iam_policy)
  * [google_compute_forwarding_rule](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_forwarding_rule)
  * [google_compute_forwarding_rules](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_forwarding_rules)
  * [google_compute_global_address](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_global_address)
  * [google_compute_global_forwarding_rule](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_global_forwarding_rule)
  * [google_compute_ha_vpn_gateway](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_ha_vpn_gateway)
  * [google_compute_health_check](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_health_check)
  * [google_compute_image](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_image)
  * [google_compute_image_iam_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_image_iam_policy)
  * [google_compute_images](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_images)
  * [google_compute_instance](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_instance)
  * [google_compute_instance_group](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_instance_group)
  * [google_compute_instance_group_manager](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_instance_group_manager)
  * [google_compute_instance_guest_attributes](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_instance_guest_attributes)
  * [google_compute_instance_iam_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_instance_iam_policy)
  * [google_compute_instance_serial_port](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_instance_serial_port)
  * [google_compute_instance_template](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_instance_template)
  * [google_compute_instance_template_iam_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_instance_template_iam_policy)
  * [google_compute_instant_snapshot_iam_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_instant_snapshot_iam_policy)
  * [google_compute_lb_ip_ranges](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_lb_ip_ranges)
  * [google_compute_machine_image_iam_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_machine_image_iam_policy)
  * [google_compute_machine_types](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_machine_types)
  * [google_compute_network](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_network)
  * [google_compute_network_endpoint_group](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_network_endpoint_group)
  * [google_compute_network_peering](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_network_peering)
  * [google_compute_networks](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_networks)
  * [google_compute_node_types](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_node_types)
  * [google_compute_region_backend_service](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_region_backend_service)
  * [google_compute_region_backend_service_iam_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_region_backend_service_iam_policy)
  * [google_compute_region_disk](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_region_disk)
  * [google_compute_region_disk_iam_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_region_disk_iam_policy)
  * [google_compute_region_instance_group](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_region_instance_group)
  * [google_compute_region_instance_template](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_region_instance_template)
  * [google_compute_region_network_endpoint_group](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_region_network_endpoint_group)
  * [google_compute_region_ssl_certificate](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_region_ssl_certificate)
  * [google_compute_regions](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_regions)
  * [google_compute_reservation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_reservation)
  * [google_compute_resource_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_resource_policy)
  * [google_compute_router](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_router)
  * [google_compute_router_nat](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_router_nat)
  * [google_compute_router_status](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_router_status)
  * [google_compute_security_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_security_policy)
  * [google_compute_snapshot](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_snapshot)
  * [google_compute_snapshot_iam_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_snapshot_iam_policy)
  * [google_compute_ssl_certificate](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_ssl_certificate)
  * [google_compute_ssl_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_ssl_policy)
  * [google_compute_storage_pool_iam_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_storage_pool_iam_policy)
  * [google_compute_storage_pool_type](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_storage_pool_type)
  * [google_compute_subnetwork](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_subnetwork)
  * [google_compute_subnetwork_iam_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_subnetwork_iam_policy)
  * [google_compute_subnetworks](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_subnetworks)
  * [google_compute_vpn_gateway](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_vpn_gateway)
  * [google_compute_zones](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_zones)

  
  
## Terraform-based guides for Compute Engine

The following table lists Terraform-based how-to guides and tutorials for Compute Engine:

**Guide** | **Details**  
---|---  
[Create and start a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance) | Explains how to create a virtual machine (VM) instance.  
[Create a VM with Local SSD disks](https://docs.cloud.google.com/compute/docs/disks/add-local-ssd) | Explains how you can create a VM with Local SSD disk storage.  
[Create disk snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots) | Explains how to create standard snapshots to periodically back up data from disks.  
[Duplicate a disk with clones](https://docs.cloud.google.com/compute/docs/disks/clone-duplicate-disks) | Explains how to create zonal disk clones of an existing disk.  
[Create and manage regional disks](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk) | Explains how to create and manage regional disks.  
[Create and use Spot VMs](https://docs.cloud.google.com/compute/docs/instances/create-use-spot) | Explains how to create and manage Spot VMs. Spot VMs are VM instances that are excess Compute Engine capacity. Spot VMs are available at much lower prices compared to the on-demand price for standard VMs  
[Add SSH keys to VMs](https://docs.cloud.google.com/compute/docs/connect/add-ssh-keys) | Describes how to add SSH keys to VM instances that use OS Login and VMs that use metadata-based SSH keys.   
[Running shutdown scripts](https://docs.cloud.google.com/compute/docs/shutdownscript) | Explains how to create and run shutdown scripts that execute commands right before a VM instance is stopped or restarted.  
[Create a reservation for a single project](https://docs.cloud.google.com/compute/docs/instances/reservations-single-project) | Explains how to create a single-project reservation, which can be consumed only by VM instances in the same project.  
[ Create instance templates](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates) | Describes how to create and manage instance templates.   
[Scaling based on schedules](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-schedules) | Describes how you can create scaling schedules for an existing MIG. Schedule-based autoscaling lets you improve the availability of your workloads by scheduling capacity ahead of anticipated load.  
[Add Persistent Disk storage to your VM](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk) | Explains how to create a blank, non-boot zonal Persistent Disk volume and attach it to your VM.  
[Set up OS Login](https://docs.cloud.google.com/compute/docs/oslogin/set-up-oslogin) | Describes how to set up OS Login.  
[Attach a non-boot disk to a VM](https://docs.cloud.google.com/compute/docs/disks/attach-disks) | Explains how to attach a non-boot zonal disk to your VM.  
[ Create a VM that uses a user-managed service account](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances) | Explains how to create a VM instance that is configured to use a user-managed service account. A service account is a special kind of account typically used by an application or compute workload to make authorized API calls.  
[Increase the size of a persistent disk](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk) | Explains how to increase the size of a persistent disk.  
[ Enable virtual displays on a VM](https://docs.cloud.google.com/compute/docs/instances/enable-instance-virtual-display) | Describes how to enable virtual displays on a VM instance.  
[Create a MIG in a single zone](https://docs.cloud.google.com/compute/docs/instance-groups/create-zonal-mig) | Describes how to create a managed instance group (MIG) in a single zone. Putting all your MIG's VMs in a single zone helps to minimize latency, which is useful for certain workloads—for example, batch workloads.  
[Create a VM instance with a custom hostname](https://docs.cloud.google.com/compute/docs/instances/custom-hostname-vm) | Explains how to create a VM instance with a custom hostname.  
[ Set up an application-based health check and autohealing](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs) | Describes how to set up an application-based health check to autoheal VMs in a MIG.  
[Add and remove VMs from a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig) | Describes how to add and remove VMs from a MIG.  
[ Create a MIG with autoscaling enabled](https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-basic-autoscaling) | Describes how to create an autoscaled MIG that automatically adds and removes VMs based on average CPU utilization across the group.  
[ Create a MIG with stateful disks](https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-basic-stateful-disks) | Describes how to create a MIG that uses preemptible VM instances. Preemptible VMs are useful if your workload can tolerate disruptions and you want to take advantage of the cost-savings associated with preemptible VMs.  
[ Creating SQL Server VM instances](https://docs.cloud.google.com/compute/docs/instances/sql-server/creating-sql-server-instances) | Explains how to create Microsoft SQL Server VM instances. SQL Server is a database system that runs on Windows Server and some Linux distributions. You can use SQL Server on Compute Engine as part of the backend for your applications, as a flexible development and test environment, or in addition to your on-premises systems for backup and disaster recovery.  
[ Create an OS policy assignment](https://docs.cloud.google.com/compute/docs/os-configuration-management/create-os-policy-assignment) | Explains how to create an OS policy assignment. You can use OS policies to maintain consistent software configurations across Linux and Windows VM instances.  
[ Configuring stateful metadata in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-metadata-in-migs) | Describes how to configure stateful metadata in MIGs. Instance metadata is useful for setting properties for and communicating with your applications through the metadata server.   
[ Configuring stateful persistent disks in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-disks-in-migs) | Explains how to configure stateful persistent disks in MIGs. Configuring persistent disks to be stateful lets you benefit from VM instance autohealing and automated updates while preserving the state of the disks.  
[ Configuring stateful IP addresses in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-ip-addresses-in-migs) | Describes how to configure stateful IP addresses in MIGs. By configuring stateful IP addresses in a MIG, you ensure that IP addresses are preserved when VM instances in the group are autohealed, updated, and recreated.  
[ Set a target distribution shape for VMs in a regional MIG](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-set-target-distribution-shape) | Explains how to set a target distribution shape for VMs.  
[Create a MIG with VMs in multiple zones in a region](https://docs.cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups) | Describes how to create a MIG that has its VMs spread across multiple zones in a region. Spreading your application load across multiple zones protects your workload against zonal failures.  
[Disable and re-enable proactive VM redistribution in a regional MIG](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-enable-disable-proactive-redistribution) | Describes how to disable and re-enable proactive VM redistribution in a regional MIG. In a regional MIG, to maintain an even number of VM instances across the selected zones in the region, use proactive instance redistribution. This configuration option maximizes the availability of your application in the event of a zone-level failure.  
  
## Terraform modules and blueprints for Compute Engine

Modules and blueprints help you automate provisioning and managing of Google Cloud resources at scale. A _module_ is a reusable set of Terraform configuration files that creates a logical abstraction of Terraform resources. A _blueprint_ is a package of deployable and reusable modules, and a policy that implements and documents a specific solution.

The following table lists modules and blueprints related to Compute Engine:

Module or blueprint | Details  
---|---  
[`terraform-google-vm`](https://github.com/terraform-google-modules/terraform-google-vm) | Collection of opinionated submodules that you can use as building blocks to provision VMs in Google Cloud.  
[`terraform-google-startup-scripts`](https://github.com/terraform-google-modules/terraform-google-startup-scripts) | Provides a library of useful startup scripts to embed in VMs.  
[`terraform-google-container-vm`](https://github.com/terraform-google-modules/terraform-google-container-vm) | Deploys containers on Compute Engine instances  
  
## What's next

  * [Terraform code samples for Compute Engine](https://docs.cloud.google.com/docs/samples?language=terraform&product=computeengine)
  * [Terraform on Google Cloud documentation](https://docs.cloud.google.com/docs/terraform)
  * [Google Cloud provider documentation in HashiCorp](https://registry.terraform.io/providers/hashicorp/google/latest/docs)
  * [Infrastructure as code for Google Cloud](https://docs.cloud.google.com/docs/terraform/iac-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
