---
url: https://docs.cloud.google.com/dns/docs/zones/forwarding-zones/
title: Create a forwarding zone \u00a0|\u00a0 Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:38:57.400823+00:00
---

# Create a forwarding zone  |  Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/zones/forwarding-zones/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Guides ](https://docs.cloud.google.com/dns/docs/set-up-dns-records-domain-name)



Send feedback 

#  Create a forwarding zone Stay organized with collections  Save and categorize content based on your preferences. 

You can use a forwarding zone in Cloud DNS to resolve queries for specific DNS names by sending them to another DNS server. This lets you integrate Cloud DNS with existing on-premises DNS infrastructure or other private DNS services for name resolution across hybrid environments. This page provides instructions about how to create a forwarding zone. For detailed background information, see [Forwarding zones](https://docs.cloud.google.com/dns/docs/zones/zones-overview#forwarding_zones).

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `dns.managedZones.create` to create a managed zone
  * `dns.managedZones.list` to list managed zones
  * `dns.managedZones.update` to update a managed zone
  * `dns.managedZones.patch` to update a managed zone



**Roles**

  * `roles/dns.admin`



Before you begin, verify that you understand the following:

  * The differences between standard and private routing as shown in [Forwarding targets and routing methods](https://docs.cloud.google.com/dns/docs/zones/zones-overview#fz-targets)
  * The [outbound DNS forwarding methods](https://docs.cloud.google.com/dns/docs/overview#dns-forwarding-methods)
  * The network requirements for forwarding targets
  * The [best practices for Cloud DNS forwarding zones](https://docs.cloud.google.com/dns/docs/best-practices#best_practices_for_dns_forwarding_zones_and_server_policies)

**Note:** If you use an FQDN as a forwarding target, the internal query used to resolve the forwarding IP address is charged at the normal rate. For more information, see [Cloud DNS pricing](https://cloud.google.com/dns/pricing).

To create a new managed private forwarding zone, complete the following steps.

###  Console 

  1. In the Google Cloud console, go to the **Create a DNS zone** page.

[Go to Create a DNS zone](https://console.cloud.google.com/net-services/dns/zones/new/create)

  2. For the **Zone type** , select **Private**.

  3. Enter a **Zone name** such as `my-new-zone`.

  4. Enter a **DNS name** suffix for the private zone. All records in the zone share this suffix. For example, `example.private`.

  5. Optional: Add a description.

  6. Under **Options** , select **Forward queries to another server**.

  7. Select the networks to which the private zone must be visible.

  8. To add the a forwarding target, click add**Add item**. You can add multiple IP addresses or a single fully qualified domain name (FQDN). The forwarding target must be either a list of IP addresses or an FQDN. You can't use both IP addresses and an FQDN in the same zone.

  9. To force private routing to the forwarding target, under **Private forwarding** , select the **Enable** checkbox.

  10. Click **Create**.




###  gcloud 

Run the [`dns managed-zones create`](https://docs.cloud.google.com/sdk/gcloud/reference/dns/managed-zones/create) command:
    
    
    gcloud dns managed-zones create NAME \
        --description=DESCRIPTION \
        --dns-name=DNS_SUFFIX \
        --networks=VPC_NETWORK_LIST \
        --forwarding-targets=FORWARDING_TARGETS_LIST \
        --private-forwarding-targets=PRIVATE_FORWARDING_TARGETS_LIST \
        --visibility=private
    

Replace the following:

  * `NAME`: a name for your zone
  * `DESCRIPTION`: a description for your zone
  * `DNS_SUFFIX`: the DNS suffix for your zone, such as `example.private`
  * `VPC_NETWORK_LIST`: a comma-delimited list of VPC networks that are authorized to query the zone
  * `FORWARDING_TARGETS_LIST`: a comma-delimited list of IP addresses or a single fully qualified domain name to which queries are sent. Domain names are resolved to their IP addresses. RFC 1918 IP addresses specified with this flag must be located in your VPC network or in an on-premises network connected to Google Cloud using Cloud VPN or Cloud Interconnect. Non-RFC 1918 IP addresses specified with this flag must be internet accessible.
  * `PRIVATE_FORWARDING_TARGETS_LIST`: a comma-delimited list of IP addresses or a single fully qualified domain name to which queries are sent. Domain names are resolved to their IP addresses. Any IP address specified with this flag must be located in your VPC network or in an on-premises network connected to Google Cloud using Cloud VPN or Cloud Interconnect.



###  Terraform 
    
    
    resource "google_dns_managed_zone" "private_zone" {
      name        = "private-zone"
      dns_name    = "private.example.com."
      description = "Example private DNS zone"
      labels = {
        foo = "bar"
      }
    
      visibility = "private"
    
      private_visibility_config {
        networks {
          network_url = google_compute_network.network_1.id
        }
        networks {
          network_url = google_compute_network.network_2.id
        }
      }
    
      forwarding_config {
        target_name_servers {
          ipv4_address = "172.16.1.10"
        }
        target_name_servers {
          ipv4_address = "172.16.1.20"
        }
      }
    }
    
    resource "google_compute_network" "network_1" {
      name                    = "network-1"
      auto_create_subnetworks = false
    }
    
    resource "google_compute_network" "network_2" {
      name                    = "network-2"
      auto_create_subnetworks = false
    }

###  API 

Send a `POST` request using the [`managedZones.create`](https://docs.cloud.google.com/dns/docs/reference/v1/managedZones/create) method:
    
    
    POST https://dns.googleapis.com/dns/v1/projects/PROJECT_ID/managedZones
    {
    
        "name": "NAME",
        "description": "DESCRIPTION",
        "dnsName": "DNS_NAME",
        "visibility": "private"
        "privateVisibilityConfig": {
            "kind": "dns#managedZonePrivateVisibilityConfig",
            "networks": [{
                    "kind": "dns#managedZonePrivateVisibilityConfigNetwork",
                    "networkUrl": VPC_NETWORK_1
                },
                {
                    "kind": "dns#managedZonePrivateVisibilityConfigNetwork",
                    "networkUrl": VPC_NETWORK_2
                },
                ....
            ]
        },
        "forwardingConfig": {
            "kind": "dns#managedZoneForwardingConfig",
            "targetNameServers": [{
                    "kind": "dns#managedZoneForwardingConfigNameServerTarget",
                    "ipv4Address": FORWARDING_TARGET_1
                },
                {
                    "kind": "dns#managedZoneForwardingConfigNameServerTarget",
                    "ipv4Address": FORWARDING_TARGET_2
                },
                ....
            ]
        },
    }
    
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the managed zone is created
  * `NAME`: a name for your zone
  * `DESCRIPTION`: a description for your zone
  * `DNS_NAME`: the DNS suffix for your zone, such as `example.private`
  * `VPC_NETWORK_1` and `VPC_NETWORK_2`: URLs for VPC networks in the same project that are able to query records in this zone. You can add multiple VPC networks as indicated. To determine the URL for a VPC network, describe the network with the following `gcloud` command, replacing `VPC_NETWORK_NAME` with the network's name: 
        
        gcloud compute networks describe VPC_NETWORK_NAME   
        
           --format="get(selfLink)"
        

  * `FORWARDING_TARGET_1` and `FORWARDING_TARGET_2`: IP addresses of forwarding target name servers or a single fully qualified domain name. You can add multiple IP addresses as indicated. RFC 1918 IP addresses specified here must be located in your VPC network or in an on-premises network connected to Google Cloud using Cloud VPN or Cloud Interconnect. Non-RFC 1918 IP addresses specified with this flag must be internet accessible.



**Note:** You cannot add records to a forwarding zone directly; the data comes from one or more configured target name servers.

## Forwarding target network requirements

When Cloud DNS sends requests to forwarding targets, it sends packets with the source ranges listed in the following table.

Forwarding target type | Source ranges  
---|---  
**Type 1 target** An [internal IP address](https://docs.cloud.google.com/vpc/docs/ip-addresses) of a Google Cloud VM or an [internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal) in _the same_ VPC network that is authorized to use the forwarding zone. **Type 2 target** An IP address of an on-premises system, connected to the VPC network authorized to use the forwarding zone, using Cloud VPN or Cloud Interconnect. For more information about what IP addresses are supported, see [Forwarding targets and routing methods](https://docs.cloud.google.com/dns/docs/zones/zones-overview#fz-targets). | `35.199.192.0/19` Cloud DNS uses the `35.199.192.0/19` source range for all customers. This range is _only_ accessible from a Google Cloud VPC network or from an on-premises network connected to a VPC network.  
**Type 3 target** An [external IP address](https://docs.cloud.google.com/vpc/docs/ip-addresses) of a DNS name server accessible to the internet _or_ the external IP address of a Google Cloud resource; for example, the external IP address of a VM in another VPC network. | [Google Public DNS source ranges](https://developers.google.com/speed/public-dns/faq#locations)  
**Type 4 target** A fully qualified domain name of a target name server that resolves to both IPv4 and IPv6 addresses through [ VPC network resolution order](https://docs.cloud.google.com/dns/docs/vpc-name-res-order#vpc_steps). The domain name can resolve to up to 50 IP addresses. The resolved IP addresses can be target Types 1-3. | Depending on the resolved IP addresses, the source ranges can be one of the following: 

  * 35.199.192.0/19
  * [Google Public DNS source ranges](https://developers.google.com/speed/public-dns/faq#locations)

  
  
### Type 1 and Type 2 targets

Cloud DNS requires the following to access a Type 1 or a Type 2 target. These requirements are the same whether the target is an RFC 1918 IP address and you're using standard routing or if you choose private routing:

  * **Firewall configuration for`35.199.192.0/19`**

For Type 1 targets, create an ingress allow [firewall rule](https://docs.cloud.google.com/vpc/docs/firewalls) for TCP and UDP port `53` traffic, applicable to your forwarding targets in each authorized VPC network. For Type 2 targets, configure an on-premises network firewall and similar equipment to permit TCP and UDP port `53`.

  * **Route to the forwarding target**

For Type 1 targets, Cloud DNS uses a [subnet route](https://docs.cloud.google.com/vpc/docs/routes#subnet-routes) to access the target in the VPC network authorized to use the forwarding zone. For Type 2 name targets, Cloud DNS uses either [custom dynamic or custom static routes](https://docs.cloud.google.com/vpc/docs/routes#types_of_routes), except for tagged static routes, to access the forwarding target.

  * **Return route to`35.199.192.0/19` through the same VPC network**

For Type 1 targets, Google Cloud uses a [special routing path](https://docs.cloud.google.com/vpc/docs/routes#cloud-dns) for the `35.199.192.0/19` destination. For Type 2 targets, your on-premises network must have a route for the `35.199.192.0/19` destination, whose next hop is in the same VPC network where the request originated, through a Cloud VPN tunnel or VLAN attachment for Cloud Interconnect. For information about how to meet this requirement, see return route strategies for Type 2 targets.

  * **Direct response from target**

Cloud DNS requires that the forwarding target that receives packets be the one that sends replies to `35.199.192.0/19`. If your forwarding target sends the request to a _different_ name server, and that _other_ name server responds to `35.199.192.0/19`, Cloud DNS ignores the response. For security reasons, Google Cloud expects the source address of each target name server's DNS reply to match the IP address of the forwarding target.




#### Return route strategies for Type 2 targets

Cloud DNS _cannot_ send responses from Type 2 forwarding targets over the internet or through a different VPC network. Responses _must_ return to the same VPC network, although they can use any Cloud VPN tunnel or VLAN attachment in that same network.

  * For Cloud VPN tunnels that use static routing, manually create a route in your on-premises network whose destination is `35.199.192.0/19` and whose next hop is the Cloud VPN tunnel. For Cloud VPN tunnels that use policy-based routing, [configure the Cloud VPN's local traffic selector](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/choosing-networks-routing#traffic-selectors) and the on-premises VPN gateway's remote traffic selector to include `35.199.192.0/19`.
  * For Cloud VPN tunnels that use dynamic routing or for Cloud Interconnect, [configure a custom route advertisement](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/advertising-custom-ip) for `35.199.192.0/19` on the BGP session of the Cloud Router that manages the tunnel or VLAN attachment.



### Type 3 targets

When Cloud DNS uses standard routing to access an external IP address, it expects the forwarding target to be either a system on the internet, publicly accessible, or an external IP address of a Google Cloud resource.

For example, a Type 3 target includes the external IP address of a VM in a different VPC network.

Private routing to Type 3 targets is not supported. 

### Type 4 targets

A Type 4 target first resolves the IP addresses of the target. The resolved forwarding target can then be resolved to up to 50 IP addresses, which includes both IPv4 and IPv6 addresses. Depending on the resolved forwarding target's network, the Type 4 target has the same network requirements as a Type 1, 2, or 3 target.

For additional requirements about using an FQDN as a forwarding target, see [Use forwarding zones](https://docs.cloud.google.com/dns/docs/zones/zones-overview#fz-using).

## What's next

  * To work with managed zones, see [Create, modify, and delete zones](https://docs.cloud.google.com/dns/docs/zones).
  * To find solutions for common issues that you might encounter when using Cloud DNS, see [Troubleshooting](https://docs.cloud.google.com/dns/docs/troubleshooting).
  * To get an overview of Cloud DNS, see [Cloud DNS overview](https://docs.cloud.google.com/dns/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
