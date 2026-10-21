---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/ha-vpn-interconnect-internal-ips/
title: Assign internal IP address ranges to HA VPN gateways \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:55:15.185455+00:00
---

# Assign internal IP address ranges to HA VPN gateways  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/ha-vpn-interconnect-internal-ips/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Assign internal IP address ranges to HA VPN gateways Stay organized with collections  Save and categorize content based on your preferences. 

When you deploy HA VPN over Cloud Interconnect, you have the option of using either regional internal IP addresses or regional external IP addresses for your HA VPN gateway interfaces. Unless you are required to use external IP addresses for your VPN tunnels (for example, to connect to another cloud provider), we recommend that you use regional internal IP addresses for HA VPN over Cloud Interconnect.

If you choose to use regional internal IP addresses (RFC 1918 only), you must reserve a private IPv4 address range for your VLAN attachment. The IP addresses from that range are used exclusively for your HA VPN gateway interfaces. HA VPN uses these IP addresses to communicate with one or more peer VPN gateways.

**Note:** You can't assign a regional internal IP address to an HA VPN gateway interface on an HA VPN gateway that is not deployed as part of an HA VPN over Cloud Interconnect deployment.

If you do not configure the VLAN attachments to use regional internal IP addresses, then Google Cloud selects two regional external IP addresses from its address pool and allocates an address to each interface.

Regardless of whether you choose regional internal or external IP addressing, HA VPN over Cloud Interconnect packets do not travel over the public internet at any point.

The IP address requirements for Cloud Router BGP interfaces remain the same as those used in HA VPN deployments without Cloud Interconnect. The BGP interfaces must be assigned link-local IPv4 addresses from the `169.254.0.0/16` address space.

## Prefix length and HA VPN gateway interfaces

When you reserve a regional internal IPv4 address range, you configure the prefix length. The prefix length determines the size of the reserved range. For HA VPN over Cloud Interconnect, this configuration establishes how many regional internal IP addresses are available for your HA VPN gateway interfaces.

The prefix length (`--prefix-length`) must be set between 26 and 29. You cannot modify the size of this range later.

When you specify the prefix length, choose the prefix length that matches your attachment's capacity. Reserve a large enough range for your VLAN attachment so that you can accommodate additional HA VPN gateways if you require them later.

For a VLAN attachment with the capacity of... | ...reserve at least this many IP addresses for your HA VPN gateway interfaces  | Use this prefix length  
---|---|---  
2 Gbps or fewer | 1 | /29  
5 Gbps | 2 | /29  
10 Gbps | 4 | /29  
20 Gbps | 7 | /28  
50 Gbps | 17 | /26  
100 Gbps | 34 | /26  
**Note:** This table assumes that you are deploying one HA VPN gateway for every peer VPN gateway. If you plan to deploy more peer VPN gateways and fewer HA VPN gateways, you might need fewer IP addresses. For more information, see [Gateway and tunnel mapping](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/configure-ha-vpn-interconnect#gateway_and_tunnel_mapping).

## Considerations

If you choose to reserve regional internal IP addresses for your HA VPN gateways, keep the following in mind:

  * Different reserved ranges in the same Virtual Private Cloud (VPC) network cannot overlap.
  * The reserved ranges cannot overlap with subnets used for virtual machine (VM) instances in the same virtual network.
  * If you reserve an internal IP address range by using `--purpose=IPSEC_INTERCONNECT`, then the prefix length for the range must be between 26 and 29.
  * If you are using Dedicated Interconnect, an error is thrown if you apply an address range with a prefix length that does not match the bandwidth of the VLAN attachments.
  * For each VLAN attachment, you can only specify one internal IP address range.
  * If you assign regional internal IP addresses to one VLAN attachment in your HA VPN over Cloud Interconnect deployment, then the other VLAN attachment in the deployment must match and also use internal IP addresses. The other VLAN attachment can't use regional external IP addresses.



## Reserve regional internal IP ranges

These IP address ranges are used for allocating IP addresses for the HA VPN gateways.

###  Console 

You have the option to create internal IP ranges when you create your encrypted VLAN attachments.

On the **Create VLAN attachments** page, select **Internal regional IP addresses**.

  * To create an encrypted VLAN attachment for Dedicated Interconnect, see [Create encrypted VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments#encrypted-attachments).

  * To create an encrypted VLAN attachment for Partner Interconnect, see [Create encrypted VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/creating-vlan-attachments#encrypted-attachments).




###  gcloud 

To reserve a regional internal IP address range, use the following command:
    
    
    gcloud compute addresses create ADDRESS_NAME \
        --region=REGION \
        --addresses=IP_ADDRESS \
        --prefix-length=PREFIX_LENGTH \
        --network=NETWORK_NAME \
        --purpose=IPSEC_INTERCONNECT
    

Replace the following:

  * `ADDRESS_NAME`: a name for the regional internal IP address range.
  * `REGION`: the region where you plan to create the VLAN attachment and HA VPN gateways.
  * `IP_ADDRESS`: the first IP address of the RFC 1918 internal IP address range that you are reserving.
  * `PREFIX_LENGTH`: the correct CIDR prefix length between `26` and `29` for the capacity of your attachment. Refer to Prefix lengths and HA VPN gateway interfaces.
  * `NETWORK_NAME`: the name of your VPC network.



For example, to reserve two regional internal IP address ranges with a prefix length of `29`, use the following commands:
    
    
    gcloud compute addresses create ip-range-1 \
        --region=REGION
        --addresses=192.168.1.0 \
        --prefix-length=29 \
        --network=NETWORK_NAME \
        --purpose=IPSEC_INTERCONNECT
    
    
    
    gcloud compute addresses create ip-range-2 \
        --region=REGION \
        --addresses=192.168.2.0 \
        --prefix-length=29 \
        --network=NETWORK_NAME \
        --purpose=IPSEC_INTERCONNECT
    

The output is similar to the following: 
    
    
    Created [https://www.googleapis.com/compute/v1/projects/[PROJECT_ID]/regions/us-central1/addresses/ip-range-1].
    NAME          REGION       NETWORK
    ip-range-1    us-central1  network-a
    
    
    
    Created https://www.googleapis.com/compute/v1/projects/[PROJECT_ID]/regions/us-central1/addresses/ip-range-2].
    NAME          REGION       NETWORK
    ip-range-2    us-central1  network-a
    

## What's next?

  * To choose a connection type for Cloud Interconnect, see [Choosing a Network Connectivity product](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product#cloud-interconnect).

  * To learn about best practices when planning for and configuring Cloud Interconnect, see [Best practices](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/best-practices).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
