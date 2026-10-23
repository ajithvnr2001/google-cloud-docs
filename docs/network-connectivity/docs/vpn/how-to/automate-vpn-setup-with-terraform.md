---
url: https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/automate-vpn-setup-with-terraform/
title: Terraform examples for HA VPN gateways \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:48.525335+00:00
---

# Terraform examples for HA VPN gateways  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/automate-vpn-setup-with-terraform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud VPN ](https://docs.cloud.google.com/network-connectivity/docs/vpn)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)



Send feedback 

#  Terraform examples for HA VPN gateways Stay organized with collections  Save and categorize content based on your preferences. 

You can use the following examples to deploy HA VPN gateways.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

## Between VPCs

You can use [Terraform resources](https://github.com/terraform-google-modules/terraform-docs-samples) to bring up a sample HA VPN gateway between Google Cloud networks. For information about this setup, see the [primary setup guide](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn2).
    
    
    resource "google_compute_ha_vpn_gateway" "ha_gateway1" {
      region  = "us-central1"
      name    = "ha-vpn-1"
      network = google_compute_network.network1.id
    }
    
    resource "google_compute_ha_vpn_gateway" "ha_gateway2" {
      region  = "us-central1"
      name    = "ha-vpn-2"
      network = google_compute_network.network2.id
    }
    
    resource "google_compute_network" "network1" {
      name                    = "network1"
      routing_mode            = "GLOBAL"
      auto_create_subnetworks = false
    }
    
    resource "google_compute_network" "network2" {
      name                    = "network2"
      routing_mode            = "GLOBAL"
      auto_create_subnetworks = false
    }
    
    resource "google_compute_subnetwork" "network1_subnet1" {
      name          = "ha-vpn-subnet-1"
      ip_cidr_range = "10.0.1.0/24"
      region        = "us-central1"
      network       = google_compute_network.network1.id
    }
    
    resource "google_compute_subnetwork" "network1_subnet2" {
      name          = "ha-vpn-subnet-2"
      ip_cidr_range = "10.0.2.0/24"
      region        = "us-west1"
      network       = google_compute_network.network1.id
    }
    
    resource "google_compute_subnetwork" "network2_subnet1" {
      name          = "ha-vpn-subnet-3"
      ip_cidr_range = "192.168.1.0/24"
      region        = "us-central1"
      network       = google_compute_network.network2.id
    }
    
    resource "google_compute_subnetwork" "network2_subnet2" {
      name          = "ha-vpn-subnet-4"
      ip_cidr_range = "192.168.2.0/24"
      region        = "us-east1"
      network       = google_compute_network.network2.id
    }
    
    resource "google_compute_router" "router1" {
      name    = "ha-vpn-router1"
      region  = "us-central1"
      network = google_compute_network.network1.name
      bgp {
        asn = 64514
      }
    }
    
    resource "google_compute_router" "router2" {
      name    = "ha-vpn-router2"
      region  = "us-central1"
      network = google_compute_network.network2.name
      bgp {
        asn = 64515
      }
    }
    
    resource "google_compute_vpn_tunnel" "tunnel1" {
      name                  = "ha-vpn-tunnel1"
      region                = "us-central1"
      vpn_gateway           = google_compute_ha_vpn_gateway.ha_gateway1.id
      peer_gcp_gateway      = google_compute_ha_vpn_gateway.ha_gateway2.id
      shared_secret         = "a secret message"
      router                = google_compute_router.router1.id
      vpn_gateway_interface = 0
    }
    
    resource "google_compute_vpn_tunnel" "tunnel2" {
      name                  = "ha-vpn-tunnel2"
      region                = "us-central1"
      vpn_gateway           = google_compute_ha_vpn_gateway.ha_gateway1.id
      peer_gcp_gateway      = google_compute_ha_vpn_gateway.ha_gateway2.id
      shared_secret         = "a secret message"
      router                = google_compute_router.router1.id
      vpn_gateway_interface = 1
    }
    
    resource "google_compute_vpn_tunnel" "tunnel3" {
      name                  = "ha-vpn-tunnel3"
      region                = "us-central1"
      vpn_gateway           = google_compute_ha_vpn_gateway.ha_gateway2.id
      peer_gcp_gateway      = google_compute_ha_vpn_gateway.ha_gateway1.id
      shared_secret         = "a secret message"
      router                = google_compute_router.router2.id
      vpn_gateway_interface = 0
    }
    
    resource "google_compute_vpn_tunnel" "tunnel4" {
      name                  = "ha-vpn-tunnel4"
      region                = "us-central1"
      vpn_gateway           = google_compute_ha_vpn_gateway.ha_gateway2.id
      peer_gcp_gateway      = google_compute_ha_vpn_gateway.ha_gateway1.id
      shared_secret         = "a secret message"
      router                = google_compute_router.router2.id
      vpn_gateway_interface = 1
    }
    
    resource "google_compute_router_interface" "router1_interface1" {
      name       = "router1-interface1"
      router     = google_compute_router.router1.name
      region     = "us-central1"
      ip_range   = "169.254.0.1/30"
      vpn_tunnel = google_compute_vpn_tunnel.tunnel1.name
    }
    
    resource "google_compute_router_peer" "router1_peer1" {
      name                      = "router1-peer1"
      router                    = google_compute_router.router1.name
      region                    = "us-central1"
      peer_ip_address           = "169.254.0.2"
      peer_asn                  = 64515
      advertised_route_priority = 100
      interface                 = google_compute_router_interface.router1_interface1.name
    }
    
    resource "google_compute_router_interface" "router1_interface2" {
      name       = "router1-interface2"
      router     = google_compute_router.router1.name
      region     = "us-central1"
      ip_range   = "169.254.1.2/30"
      vpn_tunnel = google_compute_vpn_tunnel.tunnel2.name
    }
    
    resource "google_compute_router_peer" "router1_peer2" {
      name                      = "router1-peer2"
      router                    = google_compute_router.router1.name
      region                    = "us-central1"
      peer_ip_address           = "169.254.1.1"
      peer_asn                  = 64515
      advertised_route_priority = 100
      interface                 = google_compute_router_interface.router1_interface2.name
    }
    
    resource "google_compute_router_interface" "router2_interface1" {
      name       = "router2-interface1"
      router     = google_compute_router.router2.name
      region     = "us-central1"
      ip_range   = "169.254.0.2/30"
      vpn_tunnel = google_compute_vpn_tunnel.tunnel3.name
    }
    
    resource "google_compute_router_peer" "router2_peer1" {
      name                      = "router2-peer1"
      router                    = google_compute_router.router2.name
      region                    = "us-central1"
      peer_ip_address           = "169.254.0.1"
      peer_asn                  = 64514
      advertised_route_priority = 100
      interface                 = google_compute_router_interface.router2_interface1.name
    }
    
    resource "google_compute_router_interface" "router2_interface2" {
      name       = "router2-interface2"
      router     = google_compute_router.router2.name
      region     = "us-central1"
      ip_range   = "169.254.1.1/30"
      vpn_tunnel = google_compute_vpn_tunnel.tunnel4.name
    }
    
    resource "google_compute_router_peer" "router2_peer2" {
      name                      = "router2-peer2"
      router                    = google_compute_router.router2.name
      region                    = "us-central1"
      peer_ip_address           = "169.254.1.2"
      peer_asn                  = 64514
      advertised_route_priority = 100
      interface                 = google_compute_router_interface.router2_interface2.name
    }

## To an external peer network

You can use [Terraform resources](https://github.com/terraform-google-modules/terraform-docs-samples) to bring up a sample HA VPN gateway to an external peer. For information about this setup, see the [primary setup guide](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn).

For HA VPN over Cloud Interconnect examples, see [ Terraform examples for HA VPN over Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/ha-vpn-interconnect-terraform).
    
    
    resource "google_compute_ha_vpn_gateway" "ha_gateway" {
      region  = "us-central1"
      name    = "ha-vpn"
      network = google_compute_network.network.id
    }
    
    resource "google_compute_external_vpn_gateway" "external_gateway" {
      name            = "external-gateway"
      redundancy_type = "SINGLE_IP_INTERNALLY_REDUNDANT"
      description     = "An externally managed VPN gateway"
      interface {
        id         = 0
        ip_address = "8.8.8.8"
      }
    }
    
    resource "google_compute_network" "network" {
      name                    = "network-1"
      routing_mode            = "GLOBAL"
      auto_create_subnetworks = false
    }
    
    resource "google_compute_subnetwork" "network_subnet1" {
      name          = "ha-vpn-subnet-1"
      ip_cidr_range = "10.0.1.0/24"
      region        = "us-central1"
      network       = google_compute_network.network.id
    }
    
    resource "google_compute_subnetwork" "network_subnet2" {
      name          = "ha-vpn-subnet-2"
      ip_cidr_range = "10.0.2.0/24"
      region        = "us-west1"
      network       = google_compute_network.network.id
    }
    
    resource "google_compute_router" "router1" {
      name    = "ha-vpn-router1"
      network = google_compute_network.network.name
      bgp {
        asn = 64514
      }
    }
    
    resource "google_compute_vpn_tunnel" "tunnel1" {
      name                            = "ha-vpn-tunnel1"
      region                          = "us-central1"
      vpn_gateway                     = google_compute_ha_vpn_gateway.ha_gateway.id
      peer_external_gateway           = google_compute_external_vpn_gateway.external_gateway.id
      peer_external_gateway_interface = 0
      shared_secret                   = "a secret message"
      router                          = google_compute_router.router1.id
      vpn_gateway_interface           = 0
    }
    
    resource "google_compute_vpn_tunnel" "tunnel2" {
      name                            = "ha-vpn-tunnel2"
      region                          = "us-central1"
      vpn_gateway                     = google_compute_ha_vpn_gateway.ha_gateway.id
      peer_external_gateway           = google_compute_external_vpn_gateway.external_gateway.id
      peer_external_gateway_interface = 0
      shared_secret                   = "a secret message"
      router                          = " ${google_compute_router.router1.id}"
      vpn_gateway_interface           = 1
    }
    
    resource "google_compute_router_interface" "router1_interface1" {
      name       = "router1-interface1"
      router     = google_compute_router.router1.name
      region     = "us-central1"
      ip_range   = "169.254.0.1/30"
      vpn_tunnel = google_compute_vpn_tunnel.tunnel1.name
    }
    
    resource "google_compute_router_peer" "router1_peer1" {
      name                      = "router1-peer1"
      router                    = google_compute_router.router1.name
      region                    = "us-central1"
      peer_ip_address           = "169.254.0.2"
      peer_asn                  = 64515
      advertised_route_priority = 100
      interface                 = google_compute_router_interface.router1_interface1.name
    }
    
    resource "google_compute_router_interface" "router1_interface2" {
      name       = "router1-interface2"
      router     = google_compute_router.router1.name
      region     = "us-central1"
      ip_range   = "169.254.1.1/30"
      vpn_tunnel = google_compute_vpn_tunnel.tunnel2.name
    }
    
    resource "google_compute_router_peer" "router1_peer2" {
      name                      = "router1-peer2"
      router                    = google_compute_router.router1.name
      region                    = "us-central1"
      peer_ip_address           = "169.254.1.2"
      peer_asn                  = 64515
      advertised_route_priority = 100
      interface                 = google_compute_router_interface.router1_interface2.name
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
