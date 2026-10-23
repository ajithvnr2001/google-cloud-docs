---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/ha-vpn-interconnect-terraform/
title: Terraform examples for HA VPN over Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:21.800243+00:00
---

# Terraform examples for HA VPN over Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/ha-vpn-interconnect-terraform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Terraform examples for HA VPN over Cloud Interconnect Stay organized with collections  Save and categorize content based on your preferences. 

You can use the following Terraform examples to deploy HA VPN over Cloud Interconnect.

The examples require that you already have two Dedicated Interconnect connections provisioned in two edge availability domains (zones).

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

## Examples

###  5-Gbps example

The following Terraform example deploys an HA VPN over Cloud Interconnect deployment with two 5-Gbps VLAN attachments.
    
    
    provider "google" {
      # Specify the project where you want
      # to deploy HA VPN over Cloud Interconnect resources.
      # Your Dedicated Interconnect connections can be
      # located in a different project.
      #
      # project = "your-project"
    
      # Create all resources in the same region, which
      # you can specify at the provider level.
      # Important: This region must support the creation
      # of new VLAN attachments on Dataplane v2.
      region = "us-east4"
    }
    
    # VPC Network
    resource "google_compute_network" "network_havpn_ic" {
      name                    = "network-havpn-ic"
      auto_create_subnetworks = false
      routing_mode            = "GLOBAL"
    }
    
    # Subnet
    resource "google_compute_subnetwork" "subnet_havpn_ic" {
      name          = "subnet-havpn-ic"
      ip_cidr_range = "192.168.1.0/24"
      network       = google_compute_network.network_havpn_ic.self_link
    }
    
    # Begin Cloud Interconnect tier
    # Create Interconnect Cloud Router, specific to HA VPN over Cloud Interconnect
    
    resource "google_compute_router" "ic_router" {
      name                          = "ic-router"
      network                       = google_compute_network.network_havpn_ic.self_link
      encrypted_interconnect_router = true
      bgp {
        asn = 65000
      }
    }
    
    # Optional: Reserve regional internal IP ranges to allocate to the HA VPN gateway
    # interfaces. Reserve an internal range for each VLAN attachment.
    
    resource "google_compute_address" "address_vpn_ia_1" {
      name          = "address-vpn-ia-1"
      address_type  = "INTERNAL"
      purpose       = "IPSEC_INTERCONNECT"
      address       = "192.168.20.0"
      prefix_length = 29 # Allows you to reserve up to 8 IP addresses
      network       = google_compute_network.network_havpn_ic.self_link
    }
    
    resource "google_compute_address" "address_vpn_ia_2" {
      name          = "address-vpn-ia-2"
      address_type  = "INTERNAL"
      purpose       = "IPSEC_INTERCONNECT"
      address       = "192.168.21.0"
      prefix_length = 29 # Allows you to reserve up to 8 IP addresses
      network       = google_compute_network.network_havpn_ic.self_link
    }
    
    # Create encrypted VLAN attachments
    
    data "google_project" "project" {
    }
    resource "google_compute_interconnect_attachment" "ia_1" {
      name    = "ia-1"
      project = data.google_project.project.project_id
      router  = google_compute_router.ic_router.self_link
      # If you use the same project for your Dedicated Interconnect connection and attachments, you can keep the variable in the following URL.
      # If not, replace the URL and variable.
      interconnect = "https://www.googleapis.com/compute/v1/projects/${data.google_project.project.project_id}/global/interconnects/interconnect-zone1"
      description  = ""
      bandwidth    = "BPS_5G"
      type         = "DEDICATED"
      encryption   = "IPSEC"
      ipsec_internal_addresses = [
        google_compute_address.address_vpn_ia_1.self_link,
      ]
      vlan_tag8021q = 2001
    }
    
    resource "google_compute_interconnect_attachment" "ia_2" {
      name    = "ia-2"
      project = data.google_project.project.project_id
      router  = google_compute_router.ic_router.self_link
      # If you use the same project for your Dedicated Interconnect connection and attachments, you can keep the variable in the following URL.
      # If not, replace the URL and variable.
      interconnect = "https://www.googleapis.com/compute/v1/projects/${data.google_project.project.project_id}/global/interconnects/interconnect-zone2"
      description  = ""
      bandwidth    = "BPS_5G"
      type         = "DEDICATED"
      encryption   = "IPSEC"
      ipsec_internal_addresses = [
        google_compute_address.address_vpn_ia_2.self_link,
      ]
      vlan_tag8021q = 2002
    }
    
    # Create VLAN attachment interfaces for Cloud Router
    
    resource "google_compute_router_interface" "ic_if_1" {
      name                    = "ic-if-1"
      router                  = google_compute_router.ic_router.name
      ip_range                = google_compute_interconnect_attachment.ia_1.cloud_router_ip_address
      interconnect_attachment = google_compute_interconnect_attachment.ia_1.self_link
    }
    
    resource "google_compute_router_interface" "ic_if_2" {
      name                    = "ic-if-2"
      router                  = google_compute_router.ic_router.name
      ip_range                = google_compute_interconnect_attachment.ia_2.cloud_router_ip_address
      interconnect_attachment = google_compute_interconnect_attachment.ia_2.self_link
    }
    
    # Create BGP peers for Interconnect Cloud Router
    
    resource "google_compute_router_peer" "ic_peer_1" {
      name            = "ic-peer-1"
      router          = google_compute_router.ic_router.name
      peer_ip_address = trimsuffix(google_compute_interconnect_attachment.ia_1.customer_router_ip_address, "/29")
      interface       = google_compute_router_interface.ic_if_1.name
      peer_asn        = 65098
    }
    
    resource "google_compute_router_peer" "ic_peer_2" {
      name            = "ic-peer-2"
      router          = google_compute_router.ic_router.name
      peer_ip_address = trimsuffix(google_compute_interconnect_attachment.ia_2.customer_router_ip_address, "/29")
      interface       = google_compute_router_interface.ic_if_2.name
      peer_asn        = 65099
    }
    
    # Begin VPN Layer
    # Create HA VPN Gateways and associate with Cloud Interconnect VLAN attachments
    
    resource "google_compute_ha_vpn_gateway" "vpngw_1" {
      name    = "vpngw-1"
      network = google_compute_network.network_havpn_ic.id
      vpn_interfaces {
        id                      = 0
        interconnect_attachment = google_compute_interconnect_attachment.ia_1.self_link
      }
      vpn_interfaces {
        id                      = 1
        interconnect_attachment = google_compute_interconnect_attachment.ia_2.self_link
      }
    }
    
    resource "google_compute_ha_vpn_gateway" "vpngw_2" {
      name    = "vpngw-2"
      network = google_compute_network.network_havpn_ic.id
      vpn_interfaces {
        id                      = 0
        interconnect_attachment = google_compute_interconnect_attachment.ia_1.self_link
      }
      vpn_interfaces {
        id                      = 1
        interconnect_attachment = google_compute_interconnect_attachment.ia_2.self_link
      }
    }
    
    # Create external peer VPN gateway resources
    
    resource "google_compute_external_vpn_gateway" "external_vpngw_1" {
      name            = "external-vpngw-1"
      redundancy_type = "TWO_IPS_REDUNDANCY"
      interface {
        id         = 0
        ip_address = "192.25.67.3"
      }
      interface {
        id         = 1
        ip_address = "192.25.67.4"
      }
    }
    
    resource "google_compute_external_vpn_gateway" "external_vpngw_2" {
      name            = "external-vpngw-2"
      redundancy_type = "TWO_IPS_REDUNDANCY"
      interface {
        id         = 0
        ip_address = "192.25.68.5"
      }
      interface {
        id         = 1
        ip_address = "192.25.68.6"
      }
    }
    
    # Create HA VPN Cloud Router
    
    resource "google_compute_router" "vpn_router" {
      name    = "vpn-router"
      network = google_compute_network.network_havpn_ic.self_link
      bgp {
        asn = 65010
      }
    }
    
    # Create HA VPN tunnels
    
    resource "google_compute_vpn_tunnel" "tunnel_1" {
      name                            = "tunnel-1"
      vpn_gateway                     = google_compute_ha_vpn_gateway.vpngw_1.id
      peer_external_gateway           = google_compute_external_vpn_gateway.external_vpngw_1.id
      shared_secret                   = "shhhhh"
      router                          = google_compute_router.vpn_router.id
      vpn_gateway_interface           = 0
      peer_external_gateway_interface = 0
    }
    
    resource "google_compute_vpn_tunnel" "tunnel_2" {
      name                            = "tunnel-2"
      vpn_gateway                     = google_compute_ha_vpn_gateway.vpngw_1.id
      peer_external_gateway           = google_compute_external_vpn_gateway.external_vpngw_1.id
      shared_secret                   = "shhhhh"
      router                          = google_compute_router.vpn_router.id
      vpn_gateway_interface           = 1
      peer_external_gateway_interface = 1
    }
    
    resource "google_compute_vpn_tunnel" "tunnel_3" {
      name                            = "tunnel-3"
      vpn_gateway                     = google_compute_ha_vpn_gateway.vpngw_2.id
      peer_external_gateway           = google_compute_external_vpn_gateway.external_vpngw_2.id
      shared_secret                   = "shhhhh"
      router                          = google_compute_router.vpn_router.id
      vpn_gateway_interface           = 0
      peer_external_gateway_interface = 0
    }
    
    resource "google_compute_vpn_tunnel" "tunnel_4" {
      name                            = "tunnel-4"
      vpn_gateway                     = google_compute_ha_vpn_gateway.vpngw_2.id
      peer_external_gateway           = google_compute_external_vpn_gateway.external_vpngw_2.id
      shared_secret                   = "shhhhh"
      router                          = google_compute_router.vpn_router.id
      vpn_gateway_interface           = 1
      peer_external_gateway_interface = 1
    }
    
    # Create VPN tunnel interfaces for Cloud Router
    
    resource "google_compute_router_interface" "vpn_1_if_0" {
      name       = "vpn-1-if-0"
      router     = google_compute_router.vpn_router.name
      ip_range   = "169.254.1.1/30"
      vpn_tunnel = google_compute_vpn_tunnel.tunnel_1.self_link
    }
    
    resource "google_compute_router_interface" "vpn_1_if_1" {
      name       = "vpn-1-if-1"
      router     = google_compute_router.vpn_router.name
      ip_range   = "169.254.2.1/30"
      vpn_tunnel = google_compute_vpn_tunnel.tunnel_2.self_link
    }
    
    resource "google_compute_router_interface" "vpn_2_if_0" {
      name       = "vpn-2-if-0"
      router     = google_compute_router.vpn_router.name
      ip_range   = "169.254.3.1/30"
      vpn_tunnel = google_compute_vpn_tunnel.tunnel_3.self_link
    }
    
    resource "google_compute_router_interface" "vpn_2_if_1" {
      name       = "vpn-2-if-1"
      router     = google_compute_router.vpn_router.name
      ip_range   = "169.254.4.1/30"
      vpn_tunnel = google_compute_vpn_tunnel.tunnel_4.self_link
    }
    
    # Create BGP Peers for Cloud Router
    
    resource "google_compute_router_peer" "vpn_peer_1" {
      name            = "vpn-peer-1"
      router          = google_compute_router.vpn_router.name
      peer_ip_address = "169.254.1.2"
      interface       = google_compute_router_interface.vpn_1_if_0.name
      peer_asn        = 65011
    }
    
    resource "google_compute_router_peer" "vpn_peer_2" {
      name            = "vpn-peer-2"
      router          = google_compute_router.vpn_router.name
      peer_ip_address = "169.254.2.2"
      interface       = google_compute_router_interface.vpn_1_if_1.name
      peer_asn        = 65011
    }
    
    resource "google_compute_router_peer" "vpn_peer_3" {
      name            = "vpn-peer-3"
      router          = google_compute_router.vpn_router.name
      peer_ip_address = "169.254.3.2"
      interface       = google_compute_router_interface.vpn_2_if_0.name
      peer_asn        = 65034
    }
    
    resource "google_compute_router_peer" "vpn_peer_4" {
      name            = "vpn-peer-4"
      router          = google_compute_router.vpn_router.name
      peer_ip_address = "169.254.4.2"
      interface       = google_compute_router_interface.vpn_2_if_1.name
      peer_asn        = 65034
    }
    

###  10-Gbps example

The following Terraform example deploys an HA VPN over Cloud Interconnect deployment with two 10-Gbps VLAN attachments.
    
    
    provider "google" {
      # Specify the project where you want
      # to deploy HA VPN over Cloud Interconnect resources.
      # Your Dedicated Interconnect connections can be
      # located in a different project.
      #
      # project = "your-project"
    
      # Create all resources in the same region, which
      # you can specify at the provider level.
      # Important: This region must support the creation
      # of new VLAN attachments on Dataplane v2.
      region = "us-east4"
    }
    
    # VPC Network
    resource "google_compute_network" "network_havpn_ic" {
      name                    = "network-havpn-ic"
      auto_create_subnetworks = false
      routing_mode            = "GLOBAL"
    }
    
    # Subnet
    resource "google_compute_subnetwork" "subnet_havpn_ic" {
      name          = "subnet-havpn-ic"
      ip_cidr_range = "192.168.1.0/24"
      network       = google_compute_network.network_havpn_ic.self_link
    }
    
    # Begin Cloud Interconnect tier
    # Create Interconnect Cloud Router, specific to HA VPN over Cloud Interconnect
    
    resource "google_compute_router" "ic_router" {
      name                          = "ic-router"
      network                       = google_compute_network.network_havpn_ic.self_link
      encrypted_interconnect_router = true
      bgp {
        asn = 65000
      }
    }
    
    # Optional: Reserve regional internal IP ranges to allocate to the HA VPN gateway
    # interfaces. Reserve an internal range for each VLAN attachment.
    
    resource "google_compute_address" "address_vpn_ia_1" {
      name          = "address-vpn-ia-1"
      address_type  = "INTERNAL"
      purpose       = "IPSEC_INTERCONNECT"
      address       = "192.168.20.0"
      prefix_length = 29 # Allows you to reserve up to 8 IP addresses
      network       = google_compute_network.network_havpn_ic.self_link
    }
    
    resource "google_compute_address" "address_vpn_ia_2" {
      name          = "address-vpn-ia-2"
      address_type  = "INTERNAL"
      purpose       = "IPSEC_INTERCONNECT"
      address       = "192.168.21.0"
      prefix_length = 29 # Allows you to reserve up to 8 IP addresses
      network       = google_compute_network.network_havpn_ic.self_link
    }
    
    # Create encrypted VLAN attachments
    
    data "google_project" "project" {
    }
    resource "google_compute_interconnect_attachment" "ia_1" {
      name    = "ia-1"
      project = data.google_project.project.project_id
      router  = google_compute_router.ic_router.self_link
      # If you use the same project for your Dedicated Interconnect connection and attachments, you can keep the variable in the following URL.
      # If not, replace the URL and variable.
      interconnect = "https://www.googleapis.com/compute/v1/projects/${data.google_project.project.project_id}/global/interconnects/interconnect-zone1"
      description  = ""
      bandwidth    = "BPS_10G"
      type         = "DEDICATED"
      encryption   = "IPSEC"
      ipsec_internal_addresses = [
        google_compute_address.address_vpn_ia_1.self_link,
      ]
      vlan_tag8021q = 2001
    }
    
    resource "google_compute_interconnect_attachment" "ia_2" {
      name         = "ia-2"
      project      = data.google_project.project.project_id
      router       = google_compute_router.ic_router.self_link
      interconnect = "https://www.googleapis.com/compute/v1/projects/${data.google_project.project.project_id}/global/interconnects/interconnect-zone2"
      description  = ""
      bandwidth    = "BPS_10G"
      type         = "DEDICATED"
      encryption   = "IPSEC"
      ipsec_internal_addresses = [
        google_compute_address.address_vpn_ia_2.self_link,
      ]
      vlan_tag8021q = 2002
    }
    
    # Create VLAN attachment interfaces for Cloud Router
    
    resource "google_compute_router_interface" "ic_if_1" {
      name                    = "ic-if-1"
      router                  = google_compute_router.ic_router.name
      ip_range                = google_compute_interconnect_attachment.ia_1.cloud_router_ip_address
      interconnect_attachment = google_compute_interconnect_attachment.ia_1.self_link
    }
    
    resource "google_compute_router_interface" "ic_if_2" {
      name                    = "ic-if-2"
      router                  = google_compute_router.ic_router.name
      ip_range                = google_compute_interconnect_attachment.ia_2.cloud_router_ip_address
      interconnect_attachment = google_compute_interconnect_attachment.ia_2.self_link
    }
    
    # Create BGP peers for Interconnect Cloud Router
    
    resource "google_compute_router_peer" "ic_peer_1" {
      name            = "ic-peer-1"
      router          = google_compute_router.ic_router.name
      peer_ip_address = trimsuffix(google_compute_interconnect_attachment.ia_1.customer_router_ip_address, "/29")
      interface       = google_compute_router_interface.ic_if_1.name
      peer_asn        = 65098
    }
    
    resource "google_compute_router_peer" "ic_peer_2" {
      name            = "ic-peer-2"
      router          = google_compute_router.ic_router.name
      peer_ip_address = trimsuffix(google_compute_interconnect_attachment.ia_2.customer_router_ip_address, "/29")
      interface       = google_compute_router_interface.ic_if_2.name
      peer_asn        = 65099
    }
    
    # Begin VPN Layer
    # Create HA VPN Gateways and associate with the Cloud Interconnect VLAN attachments
    
    resource "google_compute_ha_vpn_gateway" "vpngw_1" {
      name    = "vpngw-1"
      network = google_compute_network.network_havpn_ic.id
      vpn_interfaces {
        id                      = 0
        interconnect_attachment = google_compute_interconnect_attachment.ia_1.self_link
      }
      vpn_interfaces {
        id                      = 1
        interconnect_attachment = google_compute_interconnect_attachment.ia_2.self_link
      }
    }
    
    resource "google_compute_ha_vpn_gateway" "vpngw_2" {
      name    = "vpngw-2"
      network = google_compute_network.network_havpn_ic.id
      vpn_interfaces {
        id                      = 0
        interconnect_attachment = google_compute_interconnect_attachment.ia_1.self_link
      }
      vpn_interfaces {
        id                      = 1
        interconnect_attachment = google_compute_interconnect_attachment.ia_2.self_link
      }
    }
    
    resource "google_compute_ha_vpn_gateway" "vpngw_3" {
      name    = "vpngw-3"
      network = google_compute_network.network_havpn_ic.id
      vpn_interfaces {
        id                      = 0
        interconnect_attachment = google_compute_interconnect_attachment.ia_1.self_link
      }
      vpn_interfaces {
        id                      = 1
        interconnect_attachment = google_compute_interconnect_attachment.ia_2.self_link
      }
    }
    
    resource "google_compute_ha_vpn_gateway" "vpngw_4" {
      name    = "vpngw-4"
      network = google_compute_network.network_havpn_ic.id
      vpn_interfaces {
        id                      = 0
        interconnect_attachment = google_compute_interconnect_attachment.ia_1.self_link
      }
      vpn_interfaces {
        id                      = 1
        interconnect_attachment = google_compute_interconnect_attachment.ia_2.self_link
      }
    }
    
    # Create external peer VPN gateway resources
    
    resource "google_compute_external_vpn_gateway" "external_vpngw_1" {
      name            = "external-vpngw-1"
      redundancy_type = "TWO_IPS_REDUNDANCY"
      interface {
        id         = 0
        ip_address = "192.25.67.3"
      }
      interface {
        id         = 1
        ip_address = "192.25.67.4"
      }
    }
    
    resource "google_compute_external_vpn_gateway" "external_vpngw_2" {
      name            = "external-vpngw-2"
      redundancy_type = "TWO_IPS_REDUNDANCY"
      interface {
        id         = 0
        ip_address = "192.25.68.5"
      }
      interface {
        id         = 1
        ip_address = "192.25.68.6"
      }
    }
    
    # Create HA VPN Cloud Router
    
    resource "google_compute_router" "vpn_router" {
      name    = "vpn-router"
      network = google_compute_network.network_havpn_ic.self_link
      bgp {
        asn = 65010
      }
    }
    
    # Create HA VPN tunnels
    
    resource "google_compute_vpn_tunnel" "tunnel_1" {
      name                            = "tunnel-1"
      vpn_gateway                     = google_compute_ha_vpn_gateway.vpngw_1.id
      peer_external_gateway           = google_compute_external_vpn_gateway.external_vpngw_1.id
      shared_secret                   = "shhhhh"
      router                          = google_compute_router.vpn_router.id
      vpn_gateway_interface           = 0
      peer_external_gateway_interface = 0
    }
    
    resource "google_compute_vpn_tunnel" "tunnel_2" {
      name                            = "tunnel-2"
      vpn_gateway                     = google_compute_ha_vpn_gateway.vpngw_1.id
      peer_external_gateway           = google_compute_external_vpn_gateway.external_vpngw_1.id
      shared_secret                   = "shhhhh"
      router                          = google_compute_router.vpn_router.id
      vpn_gateway_interface           = 1
      peer_external_gateway_interface = 1
    }
    
    resource "google_compute_vpn_tunnel" "tunnel_3" {
      name                            = "tunnel-3"
      vpn_gateway                     = google_compute_ha_vpn_gateway.vpngw_2.id
      peer_external_gateway           = google_compute_external_vpn_gateway.external_vpngw_2.id
      shared_secret                   = "shhhhh"
      router                          = google_compute_router.vpn_router.id
      vpn_gateway_interface           = 0
      peer_external_gateway_interface = 0
    }
    
    resource "google_compute_vpn_tunnel" "tunnel_4" {
      name                            = "tunnel-4"
      vpn_gateway                     = google_compute_ha_vpn_gateway.vpngw_2.id
      peer_external_gateway           = google_compute_external_vpn_gateway.external_vpngw_2.id
      shared_secret                   = "shhhhh"
      router                          = google_compute_router.vpn_router.id
      vpn_gateway_interface           = 1
      peer_external_gateway_interface = 1
    }
    
    resource "google_compute_vpn_tunnel" "tunnel_5" {
      name                            = "tunnel-5"
      vpn_gateway                     = google_compute_ha_vpn_gateway.vpngw_3.id
      peer_external_gateway           = google_compute_external_vpn_gateway.external_vpngw_1.id
      shared_secret                   = "shhhhh"
      router                          = google_compute_router.vpn_router.id
      vpn_gateway_interface           = 0
      peer_external_gateway_interface = 0
    }
    
    resource "google_compute_vpn_tunnel" "tunnel_6" {
      name                            = "tunnel-6"
      vpn_gateway                     = google_compute_ha_vpn_gateway.vpngw_3.id
      peer_external_gateway           = google_compute_external_vpn_gateway.external_vpngw_1.id
      shared_secret                   = "shhhhh"
      router                          = google_compute_router.vpn_router.id
      vpn_gateway_interface           = 1
      peer_external_gateway_interface = 1
    }
    
    resource "google_compute_vpn_tunnel" "tunnel_7" {
      name                            = "tunnel-7"
      vpn_gateway                     = google_compute_ha_vpn_gateway.vpngw_4.id
      peer_external_gateway           = google_compute_external_vpn_gateway.external_vpngw_2.id
      shared_secret                   = "shhhhh"
      router                          = google_compute_router.vpn_router.id
      vpn_gateway_interface           = 0
      peer_external_gateway_interface = 0
    }
    
    resource "google_compute_vpn_tunnel" "tunnel_8" {
      name                            = "tunnel-8"
      vpn_gateway                     = google_compute_ha_vpn_gateway.vpngw_4.id
      peer_external_gateway           = google_compute_external_vpn_gateway.external_vpngw_2.id
      shared_secret                   = "shhhhh"
      router                          = google_compute_router.vpn_router.id
      vpn_gateway_interface           = 1
      peer_external_gateway_interface = 1
    }
    
    # Create VPN tunnel interfaces for Cloud Router
    
    resource "google_compute_router_interface" "vpn_1_if_0" {
      name       = "vpn-1-if-0"
      router     = google_compute_router.vpn_router.name
      ip_range   = "169.254.1.1/30"
      vpn_tunnel = google_compute_vpn_tunnel.tunnel_1.self_link
    }
    
    resource "google_compute_router_interface" "vpn_1_if_1" {
      name       = "vpn-1-if-1"
      router     = google_compute_router.vpn_router.name
      ip_range   = "169.254.2.1/30"
      vpn_tunnel = google_compute_vpn_tunnel.tunnel_2.self_link
    }
    
    resource "google_compute_router_interface" "vpn_2_if_0" {
      name       = "vpn-2-if-0"
      router     = google_compute_router.vpn_router.name
      ip_range   = "169.254.3.1/30"
      vpn_tunnel = google_compute_vpn_tunnel.tunnel_3.self_link
    }
    
    resource "google_compute_router_interface" "vpn_2_if_1" {
      name       = "vpn-2-if-1"
      router     = google_compute_router.vpn_router.name
      ip_range   = "169.254.4.1/30"
      vpn_tunnel = google_compute_vpn_tunnel.tunnel_4.self_link
    }
    
    resource "google_compute_router_interface" "vpn_3_if_0" {
      name       = "vpn-3-if-0"
      router     = google_compute_router.vpn_router.name
      ip_range   = "169.254.5.1/30"
      vpn_tunnel = google_compute_vpn_tunnel.tunnel_5.self_link
    }
    
    resource "google_compute_router_interface" "vpn_3_if_1" {
      name       = "vpn-3-if-1"
      router     = google_compute_router.vpn_router.name
      ip_range   = "169.254.6.1/30"
      vpn_tunnel = google_compute_vpn_tunnel.tunnel_6.self_link
    }
    
    resource "google_compute_router_interface" "vpn_4_if_0" {
      name       = "vpn-4-if-0"
      router     = google_compute_router.vpn_router.name
      ip_range   = "169.254.7.1/30"
      vpn_tunnel = google_compute_vpn_tunnel.tunnel_7.self_link
    }
    
    resource "google_compute_router_interface" "vpn_4_if_1" {
      name       = "vpn-4-if-1"
      router     = google_compute_router.vpn_router.name
      ip_range   = "169.254.8.1/30"
      vpn_tunnel = google_compute_vpn_tunnel.tunnel_8.self_link
    }
    
    # Create BGP Peers for Cloud Router
    
    resource "google_compute_router_peer" "vpn_peer_1" {
      name            = "vpn-peer-1"
      router          = google_compute_router.vpn_router.name
      peer_ip_address = "169.254.1.2"
      interface       = google_compute_router_interface.vpn_1_if_0.name
      peer_asn        = 65011
    }
    
    resource "google_compute_router_peer" "vpn_peer_2" {
      name            = "vpn-peer-2"
      router          = google_compute_router.vpn_router.name
      peer_ip_address = "169.254.2.2"
      interface       = google_compute_router_interface.vpn_1_if_1.name
      peer_asn        = 65011
    }
    
    resource "google_compute_router_peer" "vpn_peer_3" {
      name            = "vpn-peer-3"
      router          = google_compute_router.vpn_router.name
      peer_ip_address = "169.254.3.2"
      interface       = google_compute_router_interface.vpn_2_if_0.name
      peer_asn        = 65011
    }
    
    resource "google_compute_router_peer" "vpn_peer_4" {
      name            = "vpn-peer-4"
      router          = google_compute_router.vpn_router.name
      peer_ip_address = "169.254.4.2"
      interface       = google_compute_router_interface.vpn_2_if_1.name
      peer_asn        = 65011
    }
    
    resource "google_compute_router_peer" "vpn_peer_5" {
      name            = "vpn-peer-5"
      router          = google_compute_router.vpn_router.name
      peer_ip_address = "169.254.5.2"
      interface       = google_compute_router_interface.vpn_3_if_0.name
      peer_asn        = 65034
    }
    
    resource "google_compute_router_peer" "vpn_peer_6" {
      name            = "vpn-peer-6"
      router          = google_compute_router.vpn_router.name
      peer_ip_address = "169.254.6.2"
      interface       = google_compute_router_interface.vpn_3_if_1.name
      peer_asn        = 65034
    }
    
    resource "google_compute_router_peer" "vpn_peer_7" {
      name            = "vpn-peer-7"
      router          = google_compute_router.vpn_router.name
      peer_ip_address = "169.254.7.2"
      interface       = google_compute_router_interface.vpn_4_if_0.name
      peer_asn        = 65034
    }
    
    resource "google_compute_router_peer" "vpn_peer_8" {
      name            = "vpn-peer-8"
      router          = google_compute_router.vpn_router.name
      peer_ip_address = "169.254.8.2"
      interface       = google_compute_router_interface.vpn_4_if_1.name
      peer_asn        = 65034
    }
    

## What's next?

  * To add HA VPN gateways to your HA VPN over Cloud Interconnect deployment, see [Add an HA VPN gateway to HA VPN over Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product#cloud-interconnect).

  * To learn about best practices when planning for and configuring Cloud Interconnect, see [Best practices](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/best-practices).

  * To troubleshoot your HA VPN over Cloud Interconnect deployment, see [Troubleshooting - HA VPN over Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting#ha-vpn-interconnect).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
