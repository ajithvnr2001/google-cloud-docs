---
url: https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn/
title: Create an HA VPN gateway to a peer VPN gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:18:50.917880+00:00
---

# Create an HA VPN gateway to a peer VPN gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud VPN ](https://docs.cloud.google.com/network-connectivity/docs/vpn)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)



Send feedback 

#  Create an HA VPN gateway to a peer VPN gateway Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a high-availability VPN gateway that connects to a peer VPN gateway.

HA VPN gateways use the HA VPN API and provide a 99.99% SLA. This configuration uses a tunnel pair, with one tunnel on each HA VPN gateway interface. To receive a 99.99% SLA, you must configure VPN tunnels on _both_ HA VPN gateway interfaces.

There are two gateway components to configure for HA VPN:

  * An HA VPN gateway in Google Cloud.
  * Your peer VPN gateway or gateways.

One or more physical VPN gateway devices or software applications in the peer network to which the HA VPN gateway connects. The peer gateway can be either an on-premises VPN gateway or one hosted by another cloud provider.

Create an _external VPN gateway resource_ in Google Cloud for each peer gateway device or service. All peer gateway scenarios are represented in Google Cloud by a single external peer VPN resource.


**Caution:** When creating an HA VPN gateway for use with a peer gateway, correctly match the IPv4 or IPv6 addresses for the peer interfaces with the IPv4 or IPv6 addresses for the HA VPN gateway interfaces.   
  
For an example, see the Google Cloud CLI command output in the Verify the configuration section of this page. If these IPv4 or IPv6 addresses are mismatched, the tunnels aren't established. For instructions about how to verify your tunnel configuration, see [Check VPN status](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/checking-vpn-status).

For more information about Cloud VPN, see the following resources:

  * For diagrams of this topology, see [Connect Google Cloud to your peer VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/topologies#peer-vpn-gateways).

  * For best practices to consider before setting up Cloud VPN, see [Best practices for Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/best-practices).

  * For more information about Cloud VPN, see the [Cloud VPN overview](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview).

  * For definitions of terms used on this page, see [Key terms](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/key-terms).




If you want to deploy HA VPN over Cloud Interconnect, see the [HA VPN over Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/ha-vpn-interconnect).

## Redundancy types

The HA VPN API contains an option for `REDUNDANCY_TYPE`, which represents the number of interfaces that you configure for the external VPN gateway resource.

When you configure an external VPN gateway resource, gcloud CLI commands automatically infer the following values of `REDUNDANCY_TYPE` from the number of interfaces that you provide in the interface ID:

  * One external VPN interface is `SINGLE_IP_INTERNALLY_REDUNDANT`.
  * Two external VPN interfaces are `TWO_IPS_REDUNDANCY`.
  * Four external VPN interfaces are `FOUR_IPS_REDUNDANCY`.



When configuring external VPN gateways, use the following interface identification numbers for the stated number of external VPN interfaces:

  * For one external VPN interface, use a value of `0`.
  * For two external VPN interfaces, use values `0` and `1`.
  * For four external VPN interfaces, use values `0`,`1`,`2`, and `3`.



## Create Cloud Routers

When configuring a new HA VPN gateway, you can create a new Cloud Router, or you can use an existing Cloud Router with existing Cloud VPN tunnels or VLAN attachments. However, the Cloud Router that you use must not already manage a BGP session for a VLAN attachment associated with a Partner Interconnect connection because of the attachment's [specific ASN requirements](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/creating-vlan-attachments#encrypted-attachments).

## Before you begin

Review information about how [dynamic routing](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/choosing-networks-routing#dynamic-routing) works in Google Cloud.

Make sure that your peer VPN gateway supports Border Gateway Protocol (BGP).

Set up the following items in Google Cloud to make it easier to configure Cloud VPN:

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  5. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  6. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  7. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init



  1. If you are using the Google Cloud CLI, set your project ID with the following command. The `gcloud` instructions on this page assume that you have set your project ID before issuing commands.
         
         gcloud config set project PROJECT_ID
           



  1. You can also view a project ID that has already been set by running the following command:
         
         gcloud config list --format='text(core.project)'
           


**Note:** Instructions in this guide are written from the point of view of your VPC network and Cloud VPN gateway.

### Create a custom VPC network and subnet

**Note:** The examples in this document use one VPC network with one subnet in one [Google Cloud region](https://docs.cloud.google.com/docs/geography-and-regions). However, your requirements might be different.

Before creating an HA VPN gateway and tunnel pair, create a Virtual Private Cloud (VPC) network and at least one subnet in the region where the HA VPN gateway is located:

  * To create a custom mode VPC network (recommended), see [Create a custom mode VPC network with IPv4-only subnets](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#create-custom-network).
  * To create subnets, see [Work with subnets](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#subnet-rules).



To enable IPv6 for HA VPN gateways, you must enable the allocation of IPv6 internal addresses when you create the VPC. In addition, you must configure the subnets to use IPv6 internal addresses.

You must also configure IPv6 on the VMs in the subnet.

  * To create a custom mode VPC network that has at least one dual-stack subnet or one IPv6-only subnet with internal IPv6 addresses, see [Create and manage VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks).
  * To create a dual-stack subnet with IPv6 enabled, see [Add a dual-stack subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#add-subnet-ipv6).
  * To create an IPv6-only subnet, see [Add an IPv6-only subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#add-subnet-ipv6-only).
  * To enable IPv6 in an existing IPv4-only subnet, see [Convert an IPv4 subnet to a dual-stack subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#subnet-enable-ipv6).
  * To create VMs with IPv6 enabled, see [Configuring IPv6 for instances and instance templates](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address).



The VPC subnet must be configured to use internal IPv6 addresses. When you use the gcloud CLI, you configure the subnet with the `--ipv6-access-type=INTERNAL` flag. Cloud Router does not dynamically advertise routes for subnets that are configured to use external IPv6 addresses (`--ipv6-access-type=EXTERNAL`).

For information about using internal IPv6 address ranges in your VPC network and subnets, see [Internal IPv6 specifications](https://docs.cloud.google.com/vpc/docs/subnets#internal-ipv6).

The examples in this document also use [VPC global dynamic routing mode](https://docs.cloud.google.com/vpc/docs/vpc#routing_for_hybrid_networks), which behaves in the following way:

  * All instances of Cloud Router apply the `to on-premises` routes that they learn to all subnets of the VPC network.
  * Routes to all subnets in the VPC network are shared with on-premises routers.



## Create an HA VPN gateway and tunnel pair to a peer VPN

Follow the instructions in this section to create an HA VPN gateway, a peer VPN gateway resource, a pair of tunnels, and BGP sessions.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `compute.vpnGateways.get`
  * `compute.vpnGateways.list`
  * `compute.vpnGateways.create`
  * `compute.vpnGateways.delete`
  * `compute.vpnGateways.use`
  * `compute.vpnGateways.setLabels`
  * `compute.externalVpnGateways.get`
  * `compute.externalVpnGateways.list`
  * `compute.externalVpnGateways.create`
  * `compute.externalVpnGateways.delete`
  * `compute.externalVpnGateways.use`
  * `compute.externalVpnGateways.setLabels`



**Roles**

  * `roles/compute.networkAdmin`



### Create an HA VPN gateway

###  Console 

The **VPN setup wizard** includes all required configuration steps for creating an HA VPN gateway, a peer VPN gateway resource, tunnels, and BGP sessions.

To create an HA VPN gateway, follow these steps:

  1. In the Google Cloud console, go to the **VPN** page.

[Go to VPN](https://console.cloud.google.com/hybrid/vpn/list)

  2. If you are creating a gateway for the first time, click **Create VPN connection**.

  3. Select the **VPN setup wizard**.

  4. For **VPN gateway name** , enter a name for the HA VPN gateway.

  5. For **VPC network** , select an existing network or the default network.

  6. For **Region** , select a region for your HA VPN gateway.

  7. For **VPN gateway IP version** , select a HA VPN gateway IP version.

The IP version of the HA VPN gateway and the peer VPN gateway must be the same.

  8. For **VPN gateway IP stack type** , select a stack type for the VPN gateway.

**Note:** After you create an HA VPN gateway, you cannot modify its stack type. If you need a different stack type for an existing HA VPN gateway, you must delete and recreate the gateway. 

To support IPv6 traffic, HA VPN gateways must use either the `IPv4 and IPv6 (dual-stack)` or `IPv6 (single-stack)` configuration. To temporarily disable IPv6 traffic without deleting your gateway, [ disable IPv6 route exchange in the IPv4 BGP session](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-mp-bgp#disable-ipv6-bgp) or [ disable the IPv6 session](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/disabling-removing-bgp#disable_a_bgp_session) that you established for the HA VPN tunnels. 

  9. Click **Create and continue**.

The console page refreshes and displays your gateway information. Two external IP addresses are automatically allocated for each of your gateway interfaces. For future configuration steps, make note of the details of your gateway configuration.




###  gcloud 

To create an HA VPN gateway, run the following commands. When the gateway is created, two external IP addresses are automatically allocated, one for each gateway interface.

  * To support only IPv4 workloads, you can create an HA VPN gateway with the `IPV4_ONLY` stack type.
  * To support both IPv4 and IPv6 workloads, you can create an HA VPN gateway with the `IPV4_IPV6` stack type.
  * To support only IPv6 workloads, you can create an HA VPN gateway with the `IPV6_ONLY` stack type.



To create an HA VPN gateway with IPv4 interfaces, run the following command. When the gateway is created, two external IPv4 addresses are automatically allocated, one for each gateway interface.
    
    
    gcloud compute vpn-gateways create GW_NAME \
        --network=NETWORK \
        --region=REGION \
       [--stack-type=IP_STACK]
    

Replace the following:

  * `GW_NAME`: the name of the gateway
  * `NETWORK`: the name of your Google Cloud network
  * `REGION`: the [Google Cloud region](https://docs.cloud.google.com/compute/docs/regions-zones) where you create the gateway and tunnel
  * `IP_STACK`: the IP stack to use. Specify either `IPV4_ONLY` or `IPV4_IPV6`. If you don't specify this flag, the stack type is `IPV4_ONLY` for the HA VPN gateway. The `--stack-type` flag is optional.



You can also specify `--gateway-ip-version=IPV4`. However, this flag isn't required. If you don't specify this flag, the HA VPN gateway defaults to using external IPv4 addresses.

To create an HA VPN gateway with IPv6 interfaces, run the following command. When the gateway is created, two external IPv6 addresses are automatically allocated, one for each gateway interface.
    
    
    gcloud compute vpn-gateways create GW_NAME \
        --network=NETWORK \
        --region=REGION \
        --gateway-ip-version=IPV6 \
        --stack-type=IP_STACK
    

Replace the following:

  * `GW_NAME`: the name of the gateway
  * `NETWORK`: the name of your Google Cloud network
  * `REGION`: the [Google Cloud region](https://docs.cloud.google.com/compute/docs/regions-zones) where you create the gateway and tunnel
  * `IP_STACK`: the IP stack to use. Specify either `IPV4_IPV6` or `IPV6_ONLY`. If you don't specify this flag, the stack type is `IPV4_IPV6` for the HA VPN gateway. The `--stack-type` flag is optional.



The gateway that you create looks similar to the following example output. If you specify `--gateway-ip-version=IPV6`, IPv6 interfaces are assigned.
    
    
    Created [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/vpnGateways/ha-vpn-gw-a].
    NAME          INTERFACE0                 INTERFACE1                NETWORK     REGION
    ha-vpn-gw-a   2600:1900:4f00:2:a:49b::   2600:1900:4f10:2:a:6a8::  network-a   us-central1
    

###  API 

To create the full configuration for an HA VPN gateway, use the API commands in the following sections. All field values used in these sections are example values.

To create an HA VPN gateway, make a `POST` request by using the [`vpnGateways.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/vpnGateways/insert):
    
    
       POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/vpnGateways
       {
         "name": "ha-vpn-gw-a",
         "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/network-a",
         "stackType": "IPV4_IPV6",
         "gatewayIpVersion": "IPV4"
       }
    
    
    
       POST https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/regions/REGION/vpnGateways
       {
         "name": "ha-vpn-gw-a",
         "network": "https://www.googleapis.com/compute/beta/projects/PROJECT_ID/global/networks/network-a",
         "gatewayIpVersion": "IPV6",
         "stackType": "IPV6_ONLY"
       }
    

  * When you create an HA VPN gateway with IPv4 interfaces, the `gatewayIpVersion` and `stackType` fields are optional.

    * If you don't specify `stackType`, the default value is `IPV4_ONLY`.

    * If you don't specify `gatewayIpVersion`, the default value is `IPV4`.

    * The only valid `stackType` values for a gateway with a `gatewayIpVersion` of `IPV4` are `IPV4_IPV6` or `IPV4_ONLY`.

  * When you create an HA VPN gateway with IPv6 interfaces, specify `IPV6` as the `gatewayIpVersion` value. The `stackType` field is optional.

    * If you don't specify `stackType`, the default value is `IPV4_IPV6`.

    * The only valid `stackType` values for a gateway with a `gatewayIpVersion` of `IPV6` are `IPV4_IPV6` or `IPV6_ONLY`.




### Create a peer VPN gateway resource

###  Console 

The peer VPN gateway resource represents your non-Google Cloud gateway in Google Cloud.

**Note:** If you specify a peer VPN gateway resource with one interface, the Google Cloud console creates only one tunnel on one interface of the HA VPN gateway. For your configuration to meet the 99.99% SLA, follow the instructions at the end of this procedure for creating an additional tunnel.

To create a peer VPN gateway resource, follow these steps:

  1. On the **Create a VPN** page, under **Peer VPN gateway** , select **On-prem or Non-Google Cloud**.
  2. Under **Peer VPN gateway name** , choose an existing peer gateway or click **Create a new peer VPN gateway**.

If you choose an existing gateway, the Google Cloud console selects the number of tunnels to configure based on the number of peer interfaces that you configured on the existing peer gateway.

To create a new peer gateway, complete the following steps:

     1. Specify a **Name** for the peer VPN gateway.
     2. Under **Peer VPN gateway interfaces** , select `one`, `two`, or `four` interfaces, depending on the type of interfaces your peer gateway has. For examples of each type, see the [Topologies page](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/topologies).
     3. In the field for each peer VPN interface, specify the external IP address used for that interface. For more information, see [Configure the peer VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/configuring-peer-gateway).
     4. Click **Create**.



###  gcloud 

Create an external VPN gateway resource that provides information to Google Cloud about your peer VPN gateway or gateways. Depending on the high availability recommendations for your peer VPN gateway, you can create external VPN gateway resources for the following different types of on-premises VPN gateways:

  * Two separate peer VPN gateway devices where the two devices are redundant with each other, and each device has its own external IP address.
  * A single peer VPN gateway that uses two separate interfaces, each with its own external IP address. For this kind of peer gateway, you can create a single external VPN gateway with two interfaces.
  * A single peer VPN gateway with a single external IP address.



**Option 1: Create an external VPN gateway resource for two separate peer VPN gateway devices**

  * For this type of peer gateway, each interface of the external VPN gateway has one external IP address, and each address is from one of the peer VPN gateway devices:
        
        gcloud compute external-vpn-gateways create PEER_GW_NAME \
           --interfaces 0=PEER_GW_IP_0,1=PEER_GW_IP_1
        

Replace the following:

    * `PEER_GW_NAME`: a name representing the peer gateway
    * `PEER_GW_IP_0`: the external IP address for a peer gateway
    * `PEER_GW_IP_1`: the external IP address for another peer gateway

The external VPN gateway resource that you created looks like the following example where `PEER_GW_IP_0` and `PEER_GW_IP_1` show the actual external IP addresses of the peer gateway interfaces:
    
    Created [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/externalVpnGateways/peer-gw].
    NAME      INTERFACE0    INTERFACE1
    peer-gw   PEER_GW_IP_0  PEER_GW_IP_1
    




**Option 2: Create an external VPN gateway resource for a single peer VPN gateway with two separate interfaces**

  * For this type of peer gateway, create a single external VPN gateway with two interfaces:
        
        gcloud compute external-vpn-gateways create PEER_GW_NAME \
           --interfaces 0=PEER_GW_IP_0,1=PEER_GW_IP_1
        

Replace the following:

    * `PEER_GW_NAME`: a name representing the peer gateway
    * `PEER_GW_IP_0`: the external IP address for one interface from the peer gateway
    * `PEER_GW_IP_1`: the external IP address for another interface from the peer gateway

The external VPN gateway resource that you created looks like the following example where `PEER_GW_IP_0` and `PEER_GW_IP_1` show the actual external IP addresses of the peer gateway interfaces:
    
    Created [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/externalVpnGateways/peer-gw].
    NAME     INTERFACE0    INTERFACE1
    peer-gw  PEER_GW_IP_0  PEER_GW_IP_1
    




**Option 3: Create an external VPN gateway resource for a single peer VPN gateway with a single external IP address**

  * For this type of peer gateway, create an external VPN gateway with one interface:
        
        gcloud compute external-vpn-gateways create PEER_GW_NAME \
           --interfaces 0=PEER_GW_IP_0
        

Replace the following:

    * `PEER_GW_NAME`: a name representing the peer gateway
    * `PEER_GW_IP_0`: the external IP address for the interface from the peer gateway

The external VPN gateway resource that you created looks like the following example where `PEER_GW_IP_0` shows the actual external IP addresses of the peer gateway interface:
    
    Created [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/externalVpnGateways/peer-gw].
    NAME       INTERFACE0
    peer-gw    PEER_GW_IP_0
    




###  API 

To create an external VPN gateway resource, make a `POST` request by using the [`externalVpnGateways.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/externalVpnGateways/insert) method.

  * For an external (peer) VPN gateway that has one interface, use the following example, but specify only one interface ID and one `ipAddress`, with a `redundancyType` of `SINGLE_IP_INTERNALLY_REDUNDANT`.
  * For an external VPN gateway with two interfaces, or two external VPN gateways with one interface each, use the `TWO_IPS_REDUNDANCY` example.
  * For one or more external VPN gateways with four external VPN interfaces, for example, Amazon Web Services (AWS), use the following example, but specify four instances of the interface ID and `ipAddress` and use a `redundancyType` of `FOUR_IPS_REDUNDANCY`.
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/externalVpnGateways
         {
           "name": "my-peer-gateway",
           "interfaces": [
             {
               "id": 0,
               "ipAddress": "192.0.2.1"
             },
             {
               "id": 1,
               "ipAddress": "192.0.2.2"
             }
           ],
           "redundancyType": "TWO_IPS_REDUNDANCY"
         }
        




### Create a Cloud Router

###  Console 

Under **Cloud Router** , if you haven't already, create a Cloud Router specifying the following options. You can use an existing Cloud Router as long as the Cloud Router is not being used for Cloud NAT.

  1. To create a new Cloud Router, specify the following:

     * A **Name**
     * An optional **Description**
     * A **Google ASN** for the new router

You can use any private ASN (`64512` through `65534`, `4200000000` through `4294967294`) that you are not using elsewhere in your network. The Google ASN is used for all BGP sessions on the same Cloud Router, and you cannot change the ASN later.

  2. To create the new router, click **Create**.




###  gcloud 

You can use an existing Cloud Router as long as the Cloud Router is not being used for Cloud NAT. Otherwise, create another Cloud Router.

To create a Cloud Router, run the following command:
    
    
    gcloud compute routers create ROUTER_NAME \
        --region=REGION \
        --network=NETWORK \
        --asn=GOOGLE_ASN
    

Replace the following:

  * `ROUTER_NAME`: the name of the Cloud Router in the same region as the Cloud VPN gateway
  * `REGION`: the [Google Cloud region](https://docs.cloud.google.com/compute/docs/regions-zones) where you create the gateway and tunnel
  * `NETWORK`: the name of your VPC network
  * `GOOGLE_ASN`: any private ASN (`64512` through `65534`, `4200000000` through `4294967294`) that you are not already using in the peer network; the Google ASN is used for all BGP sessions on the same Cloud Router, and it cannot be changed later



The router that you create looks similar to the following example output:
    
    
    Created [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/routers/router-a].
    NAME       REGION        NETWORK
    router-a   us-central1   network-a
    

###  API 

You can use an existing Cloud Router as long as the Cloud Router is not being used for Cloud NAT. Otherwise, create another Cloud Router.

To create a Cloud Router, make a `POST` request by using the [`routers.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/insert) method:
    
    
     POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers
     {
       "name": "router-a",
       "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/network-a"
     }
    

### Create VPN tunnels

###  Console 

If you configured your peer VPN gateway resource with one interface, on the **Create VPN** page, configure your single tunnel in the single VPN tunnel dialog. For a 99.99% SLA, you must create a second tunnel.

If you configured your peer VPN gateway resource with two or four interfaces, configure the associated dialogs that appear at the bottom of the **Create VPN** page.

There are two ways of creating a VPN tunnel, without cipher configuration and with cipher configuration. If you don't want to configure ciphers, the system uses a set of default values. Or, you can manually configure the ciphers.

**Note:** You can only configure ciphers for tunnels that use IKEv2.

To create VPN tunnels, follow these steps:

  1. If applicable, under **Associated Cloud VPN gateway interface** , select the HA VPN interface and IP address combination that you want to associate with your peer VPN gateway interface for this tunnel.
  2. Under **Associated peer VPN gateway interface** , select the peer VPN gateway interface and IP address combination that you want to associate with this tunnel and with the HA VPN interface. This interface must match the interface on your actual peer router. 
     1. Specify a **Name** for the tunnel.
     2. Specify an optional **Description**.
     3. Specify the **IKE version**. We recommend IKEv2, the default setting, if your peer router supports it. To allow IPv6 traffic and to configure ciphers, you must select IKEv2.
     4. Specify an **IKE pre-shared key** by using your pre-shared key (shared secret), which must correspond with the pre-shared key for the partner tunnel that you create on your peer gateway. If you haven't configured a pre-shared key on your peer VPN gateway and want to generate one, click **Generate and copy**. Make sure that you record the pre-shared key in a secure location because it cannot be retrieved after you create your VPN tunnels.
     5. Optional: Select cipher configuration. Select **Default** for automatic, recommended security settings, or **Custom** to manually configure the ciphers. For steps about how to configure ciphers, see Configure ciphers. Skip this step if you don't want to manually configure the ciphers.
     6. Select [routing options](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/choosing-networks-routing), route-based or policy-based.
     7. Click **Done**.
     8. On the **Create VPN** page, repeat the tunnel creation steps for any remaining tunnel dialogs.
  3. When you have configured all tunnels, click **Create and continue**.



**Configure ciphers**

You can configure ciphers when creating Cloud VPN tunnels. If you don't configure ciphers, the system uses the [default values](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/supported-ike-ciphers#tables).

To configure ciphers, do the following:

  1. Go to the **VPN cipher selection** section.
  2. Select **Custom**.
  3. Configure the ciphers for **IKE Phase 1**.

     1. In the **Encryption** row, click editEdit.
     2. In the **New Cipher** section, select the encryption cipher.
     3. Click **Done**.
     4. To add more ciphers, click **Add Cipher** and select the encryption cipher, and click **Done**.
**Note:** You can change the priority order of ciphers using the arrows.
  4. Click **Save**.

  5. Similarly, configure the following:

     * **Integrity** : in the **Integrity** row, click editEdit, select ciphers, and then click **Save**.
     * **PRF** : in the **PRF** row, click editEdit, select ciphers, and then click **Save**.
     * **Diffie-Hellman (DH)** : in the **Diffie-Hellman (DH)** row, click editEdit, select ciphers, and then click **Save**.
  6. Configure the following for **IKE Phase 2** :

     * **Encryption** : in the **Encryption** row, click editEdit, select ciphers, and then click **Save**.
     * **Integrity** : in the **Integrity** row, click editEdit, select ciphers, and then click **Save**.
     * **PFS** : in the **PFS** row, click editEdit, select ciphers, and then click **Save**.

**Note:** When selecting multiple ciphers, ensure that you order Authenticated Encryption with Associated Data (AEAD) ciphers before non-AEAD ciphers.

###  gcloud 

Create two VPN tunnels, one for each interface on the HA VPN gateway. When creating VPN tunnels, specify the peer side of the VPN tunnels as the external VPN gateway that you created earlier. Depending on the redundancy type of the external VPN gateway, configure the tunnels by using one of the following two options.

There are two ways of creating a VPN tunnel, without cipher configuration and with cipher configuration. If you don't want to configure ciphers, the system uses a set of default values. Alternatively, you can manually configure the ciphers to create a more secure and customized tunnel. To configure ciphers, see Configure ciphers.

**Note:** You can only configure ciphers for tunnels that use IKEv2.

**Option 1: If the external VPN gateway is two separate peer VPN gateway devices or a single device with two IP addresses**

  * In this case, one VPN tunnel needs to connect to `interface 0` of the external VPN gateway, and the other VPN tunnel needs to connect to `interface 1` of the external VPN gateway.

**Note:** The VPN tunnels that you create aren't available until the corresponding partner tunnels have been created on your peer VPN gateway or gateways.
        
        gcloud compute vpn-tunnels create TUNNEL_NAME_IF0 \
             --peer-external-gateway=PEER_GW_NAME \
             --peer-external-gateway-interface=PEER_EXT_GW_IF0 \
             --region=REGION \
             --ike-version=IKE_VERS \
             --shared-secret=SHARED_SECRET \
             --router=ROUTER_NAME \
             --vpn-gateway=GW_NAME \
             [--vpn-gateway-region=VPN_GATEWAY_REGION] \
             --interface=INT_NUM_0
        
        
        gcloud compute vpn-tunnels create TUNNEL_NAME_IF1 \
             --peer-external-gateway=PEER_GW_NAME \
             --peer-external-gateway-interface=PEER_EXT_GW_IF1 \
             --region=REGION \
             --ike-version=IKE_VERS \
             --shared-secret=SHARED_SECRET \
             --router=ROUTER_NAME \
             --vpn-gateway=GW_NAME \
             [--vpn-gateway-region=VPN_GATEWAY_REGION] \
             --interface=INT_NUM_1
        

Replace the following:

    * `TUNNEL_NAME_IF0` and `TUNNEL_NAME_IF1`: a name for the tunnel; naming the tunnels by including the gateway interface name can help identify the tunnels later
    * `PEER_GW_NAME`: a name of the external peer gateway created earlier
    * `PEER_EXT_GW_IF0` and `PEER_EXT_GW_IF1`: the interface number configured earlier on the external peer gateway
    * `IKE_VERS`: `1` for IKEv1 or `2` for IKEv2; if possible, use IKEv2 for the IKE version. If your peer gateway requires IKEv1, replace `--ike-version 2` with `--ike-version 1`. To allow IPv6 traffic, you must specify IKEv2.
    * `SHARED_SECRET`: your pre-shared key (shared secret), which must correspond with the pre-shared key for the partner tunnel that you create on your peer gateway; for recommendations, see [Generate a strong pre-shared key](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/generating-pre-shared-key)
    * `GW_NAME`: the name of the HA VPN gateway
    * `INT_NUM_0`: the number `0` for the first interface on the HA VPN gateway that you created earlier
    * `INT_NUM_1`: the number `1` for the second interface on the HA VPN gateway that you created earlier
    * `VPN_GATEWAY_REGION`: the region of the HA VPN gateway to operate on. Its value should be the same as `--region`. If not specified, this option is automatically set. This option overrides the default region property value for this command invocation. The `--vpn-gateway-region` flag is optional.

The output is similar to the following:
    
    Created [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/vpnTunnels/tunnel-a-to-on-prem-if-0].
    NAME                       REGION        GATEWAY       VPN_INTERFACE   PEER_GATEWAY  PEER_INTERFACE
    tunnel-a-to-on-prem-if-0   us-central1   ha-vpn-gw-a   0               peer-gw       0
    
    Created [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/vpnTunnels/tunnel-a-to-on-prem-if-1].
    NAME                       REGION        GATEWAY       VPN_INTERFACE   PEER_GATEWAY  PEER_INTERFACE
    tunnel-a-to-on-prem-if-1   us-central1   ha-vpn-gw-a   1               peer-gw       1
    




**Option 2: If the external VPN gateway is a single peer VPN gateway with a single external IP address**

  * In this case, both VPN tunnels need to connect to `interface 0` of the external VPN gateway.

**Note:** The VPN tunnels that you create are not available until the corresponding partner tunnels have been created on your peer VPN gateway or gateways.
        
        gcloud compute vpn-tunnels create TUNNEL_NAME_IF0 \
             --peer-external-gateway=PEER_GW_NAME \
             --peer-external-gateway-interface=PEER_EXT_GW_IF0 \
             --region=REGION \
             --ike-version=IKE_VERS \
             --shared-secret=SHARED_SECRET \
             --router=ROUTER_NAME \
             --vpn-gateway=GW_NAME \
             [--vpn-gateway-region=VPN_GATEWAY_REGION] \
             --interface=INT_NUM_0
        
        
        gcloud compute vpn-tunnels create TUNNEL_NAME_IF1 \
             --peer-external-gateway=PEER_GW_NAME \
             --peer-external-gateway-interface=PEER_EXT_GW_IF0 \
             --region=REGION \
             --ike-version=IKE_VERS \
             --shared-secret=SHARED_SECRET \
             --router=ROUTER_NAME \
             --vpn-gateway=GW_NAME \
             [--vpn-gateway-region=VPN_GATEWAY_REGION] \
             --interface=INT_NUM_1
        

Replace the following:

    * `TUNNEL_NAME_IF0` and `TUNNEL_NAME_IF1`: a name for the tunnel; naming the tunnels by including the gateway interface name can help identify the tunnels later
    * `PEER_GW_NAME`: the name of the external peer gateway created earlier
    * `PEER_EXT_GW_IF0`: the interface number configured earlier on the external peer gateway
    * `IKE_VERS`: `1` for IKEv1 or `2` for IKEv2. If possible, use IKEv2 for the IKE version. If your peer gateway requires IKEv1, replace `--ike-version 2` with `--ike-version 1`. To allow IPv6 traffic, you must specify IKEv2.
    * `SHARED_SECRET`: your pre-shared key (shared secret), which must correspond with the pre-shared key for the partner tunnel that you create on your peer gateway; for recommendations, see [Generate a strong pre-shared key](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/generating-pre-shared-key)
    * `INT_NUM_0`: the number `0` for the first interface on the HA VPN gateway that you created earlier
    * `INT_NUM_1`: the number `1` for the second interface on the HA VPN gateway that you created earlier
    * `VPN_GATEWAY_REGION`: the region of the HA VPN gateway to operate on. Its value should be the same as `--region`. If not specified, this option is automatically set. This option overrides the default region property value for this command invocation. The `--vpn-gateway-region` flag is optional.

The output is similar to the following:
    
    Created [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/vpnTunnels/tunnel-a-to-on-prem-if-0].
    NAME                       REGION       GATEWAY        VPN_INTERFACE   PEER_GATEWAY   PEER_INTERFACE
    tunnel-a-to-on-prem-if-0   us-central1  ha-vpn-gw-a    0               peer-gw        0
    
    Created [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/vpnTunnels/tunnel-a-to-on-prem-if-1].
    NAME                       REGION       GATEWAY        VPN_INTERFACE   PEER_GATEWAY   PEER_INTERFACE
    tunnel-a-to-on-prem-if-1   us-central1  ha-vpn-gw-a    1               peer-gw        0
    




**Configure ciphers**

For both the previous options, you can also configure cipher algorithms when creating Cloud VPN tunnels. For example, to configure cipher algorithms for the Cloud VPN tunnel that connects to `interface 0` of the external Cloud VPN gateway, run the following command:
    
    
     gcloud compute vpn-tunnels create TUNNEL_NAME_IF0 \
         --peer-external-gateway=PEER_GW_NAME \
         --peer-external-gateway-interface=PEER_EXT_GW_IF0 \
         --region=REGION \
         --ike-version=IKE_VERS \
         --shared-secret=SHARED_SECRET \
         --router=ROUTER_NAME \
         --vpn-gateway=GW_NAME \
         [--vpn-gateway-region=VPN_GATEWAY_REGION] \
         --interface=INT_NUM_0 \
         --phase1-encryption=PH1_ENCRYPT_ALGRTHS \
         --phase1-integrity=PH1_INTEGRITY_ALGRTHS \
         --phase1-prf=PH1_PRF_ALGRTHS \
         --phase1-dh=PH1_DH_GROUP \
         --phase2-encryption=PH2_ENCRYPT_ALGRTHS \
         --phase2-integrity= PH2_INTEGRITY_ALGRTHS \
         --phase2-pfs =PH2_PFS_ALGRTHS
    

Replace the following:

  * `PH1_ENCRYPT_ALGRTHS`: a comma-separated list of encryption algorithms that are supported for phase 1 IKE security association (SA) negotiations. You can list the algorithms in your order of preference.
  * `PH1_INTEGRITY_ALGRTHS`: a comma-separated list of integrity algorithms that are supported for phase 1 IKE SA negotiations. You can list the algorithms in your order of preference.
  * `PH1_PRF_ALGRTHS`: a comma-separated list of Pseudo-Random Function (PRF) algorithms that are supported for phase 1 IKE SA negotiations. You can list the algorithms in your order of preference.
  * `PH1_DH_GROUP`: a comma-separated list of Diffie-Hellman (DH) algorithms that are supported for phase 1 IKE SA negotiations. You can list the algorithms in your order of preference.
  * `PH2_ENCRYPT_ALGRTHS`: a comma-separated list of encryption algorithms that are supported for phase 2 IKE SA negotiations. You can list the algorithms in your order of preference.
  * `PH2_INTEGRITY_ALGRTHS`: a comma-separated list of integrity algorithms that are supported for phase 2 IKE SA negotiations. You can list the algorithms in your order of preference.
  * `PH2_PFS_ALGRTHS`: a comma-separated list of PFS algorithms that are supported for phase 2 IKE SA negotiations. You can list the algorithms in your order of preference. To learn more about the cipher algorithms supported by Cloud VPN, see [Supported IKE ciphers](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/supported-ike-ciphers).



###  API 

To create two VPN tunnels, one for each interface on the HA VPN gateway, make a `POST` request by using the [`vpnTunnels.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/vpnTunnels/insert) method. To get a 99.99% uptime SLA, you must create a tunnel on each interface of your HA VPN gateway.

There are two ways of creating a VPN tunnel, without cipher configuration and with cipher configuration. If you don't want to configure ciphers, the system uses a set of default values. Alternatively, you can manually configure the ciphers to create a more secure and customized tunnel.

**Note:** You can only configure ciphers for tunnels that use IKEv2.

**Create the tunnels without configuring ciphers.**

  1. To create the first tunnel, run the following command:
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/vpnTunnels
            {
              "name": "ha-vpn-gw-a-tunnel-0",
              "ikeVersion": 2,
              "peerExternalGateway": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/externalVpnGateways/my-peer-gateway",
              "peerExternalGatewayInterface": 0,
              "router": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/router-a",
              "sharedSecret": "SHARED_SECRET",
              "vpnGateway": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/vpnGateways/ha-vpn-gw-a",
              "vpnGatewayInterface": 0
            }
         

If you plan to enable IPv6 in the BGP session associated with this tunnel, or configure ciphers, you must specify `2` for the `ikeVersion`. IKEv2 is a prerequisite for both the features.

  2. To create the second tunnel, repeat this command, but change the following parameters:

     * `name`
     * `peerExternalGatewayInterface`
     * `sharedSecret` or `sharedSecretHash`(if needed)
     * `vpnGatewayInterface`: change to the value of the other HA VPN gateway interface—in this example, change this value to `1`



**Create the tunnels with cipher configuration.**

For example, to configure ciphers for the VPN tunnel 0, run the following command: 
    
    
         POST https://www.googleapis.com/compute/{version}/projects/PROJECT_ID/regions/REGION/vpntunnels/ha-vpn-gw-a-tunnel-0
         {
          "name": "ha-vpn-gw-a-tunnel-0",
             "ikeVersion": 2,
             "peerExternalGateway": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/externalVpnGateways/my-peer-gateway",
             "peerExternalGatewayInterface": 0,
             "router": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/router-a",
             "sharedSecret": "SHARED_SECRET",
             "vpnGateway": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/vpnGateways/ha-vpn-gw-a",
             "vpnGatewayInterface": 0
             "ciphers": {
               "phase1": {
                    "encryption": "3DES-CBC,AES-GCM-16-192,AES-GCM-16-256",
                    "integrity": "AES-XCBC-96,HMAC-SHA2-256-128",
                    "prf": "PRF-AES128-XCBC,PRF-AES128-CMAC,PRF-HMAC-SHA1",
                    "dh": "Group-14,Group-15,Group-16"
                         },
               "phase2": {
                    "encryption": "AES-CBC-128,AES-GCM-16-192,AES-GCM-16-256",
                    "integrity": "HMAC-SHA2-256-128,HMAC-SHA2-512-256",
                    "pfs": "Group-14,Group-15,Group-16"
                         }
                       }
          } 

**For phase 1, specify the following values:**

  * **encryption** : a comma-separated list of encryption algorithms that are supported for phase 1 IKE security association (SA) negotiations. You can list the algorithms in your order of preference.
  * **integrity** : a comma-separated list of integrity algorithms that are supported for phase 1 IKE SA negotiations. You can list the algorithms in your order of preference.
  * **prf** : a comma-separated list of Pseudo-Random Function (PRF) algorithms that are supported for phase 1 IKE SA negotiations. You can list the algorithms in your order of preference.
  * **dh** : a comma-separated list of Diffie-Hellman (DH) algorithms that are supported for phase 1 IKE SA negotiations. You can list the algorithms in your order of preference.



**For phase 2, specify the following values:**

  * **encryption** : a comma-separated list of encryption algorithms that are supported for phase 2 IKE SA negotiations. You can list the algorithms in your order of preference.
  * **integrity** : a comma-separated list of integrity algorithms that are supported for phase 2 IKE SA negotiations. You can list the algorithms in your order of preference.
  * **pfs** : a comma-separated list of PFS algorithms that are supported for phase 2 IKE SA negotiations. You can list the algorithms in your order of preference. To learn more about the cipher algorithms supported by Cloud VPN, see see [Supported IKE ciphers](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/supported-ike-ciphers).



### Create BGP sessions

For each HA VPN tunnel, you can create an IPv4 BGP session, an IPv6 BGP session, or both.

The following table lists the BGP session type for the HA VPN stack and VPC network traffic. To view specific instructions, select any BGP session type.

BGP session type | HA VPN gateway | VPC network type | Multiprotocol BGP (MP-BGP) allowed?  
---|---|---|---  
IPv4 BGP sessions | IPv4 only or dual stack | IPv4 only or dual stack | yes  
IPv6 BGP sessions | dual stack | dual stack | yes  
Both IPv4 and IPv6 BGP sessions | dual stack | dual stack | no  
  
To set up both an IPv4 and an IPv6 BGP session in the same tunnel or to enable MP-BGP in the BGP session of an HA VPN tunnel, use a dual-stack HA VPN gateway. However, if you set up an IPv4 BGP session and an IPv6 BGP session in the same HA VPN tunnel, you can't enable MP-BGP in either session.

#### IPv4 BGP sessions

###  Console 

To create BGP sessions, follow these steps:

  1. Click **Configure BGP session**.
  2. On the **Create BGP session** page, complete the following steps: 
     1. For **BGP session type** , select **IPv4 BGP session**.
     2. For **Name** , enter a name for the BGP session.
     3. For **Peer ASN** , enter the peer ASN configured for the peer VPN gateway.
     4. Optional: For **Advertised route priority (MED)** , enter the priority of routes advertised to this BGP peer.
     5. Optional: To enable IPv6 route exchange, click the **Enable IPv6 traffic** toggle.
  3. For **Allocate BGP IPv4 address** , select **Automatically** or **Manually**. If you select **Manually** , do the following:

     1. For **Cloud Router BGP IPv4 address** , enter the Cloud Router BGP IPv4 address.
     2. For **BGP peer IPv4 address** , enter the IPv4 address of the BGP peer. The IPv4 address must meet the following requirements:

        * Each IPv4 address must belong to the same `/30` subnet that fits within the `169.254.0.0/16` address range.
        * Each IPv4 address is the first or second host of the `/30` subnet. The first and the last IP addresses of the subnet are reserved for network and broadcast addresses.
        * Each IPv4 address range for a BGP session must be unique among all Cloud Routers in all regions of a VPC network.

If you select **Automatically** , Google Cloud automatically selects the IPv4 addresses for your BGP session.

     3. Optional: If you enabled IPv6 route exchange in the previous step, for **Allocate BGP IPv6 next hop** , select **Automatically** or **Manually**. If you select **Manually** , do the following:

        1. For **Cloud Router BGP IPv6 next hop** , enter an IPv6 address in the `2600:2d00:0:2::/63` address range. This IP address is the next hop address for IPv6 routes that are advertised by the Cloud Router.
        2. For **Peer BGP IPv6 next hop** , enter an IPv6 address in the `2600:2d00:0:2::/63` address range. This IP address is the next hop address for IPv6 routes learned by the Cloud Router from the BGP peer.
        3. Optional: Expand the **Advanced options** section.
        4. To enable **BGP peer** , select **Enabled**. If enabled, the peer connection is established with routing information. For more information, see [Establish BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-bgp).
        5. To enable **MD5 authentication** , select **Enabled**. If enabled, MD5 authentication is used to authenticate BGP sessions For more information, see [Use MD5 authentication](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication). You can alternatively choose to enable MD5 authentication later.
        6. To add outbound routes to the BGP session, for **Priority of all custom learned routes** , enter a learned route priority. For more information, see [Learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes).
  4. Click **Save and continue**.

  5. Repeat the previous steps for the rest of the tunnels configured on the gateway. For each tunnel, use a different Cloud Router BGP IP address and BGP Peer IP address.

  6. Click **Save BGP configuration**. 




###  gcloud 

To create BGP sessions, follow these steps:

In the commands, replace the following:

  * `ROUTER_INTERFACE_NAME_0` and `ROUTER_INTERFACE_NAME_1`: a name for the Cloud Router interface; it can be helpful to use names related to the tunnel names configured previously
  * `TUNNEL_NAME_0` and `TUNNEL_NAME_1`: the tunnel associated with the HA VPN gateway interface that you configured
  * `IP_VERSION`: specify `IPV4` or leave unspecified. If unspecified, the default is `IPV4`.
  * `IP_PREFIXES` and `CUSTOM_ROUTE_PRIORITY`: values that let you manually specify learned routes for a BGP session; for more information about this feature, see [Learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes).
  * `AUTHENTICATION_KEY`: the secret key to use for MD5 authentication; for more information about this optional feature, see [Use MD5 authentication](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication).



**Assign IPv4 addresses for a BGP session**

Choose the automatic or manual configuration method of configuring addresses for BGP. These commands don't enable IPv6 for BGP.

If you want to enable IPv6, run the commands listed in **Assign IPv6 next-hop addresses**.

###  Automatic 

To let Google Cloud automatically choose the link-local BGP IPv4 addresses, complete the following steps.

**For the first VPN tunnel**

  1. Add an interface to the Cloud Router:
         
         gcloud compute routers add-interface ROUTER_NAME \
            --interface-name=ROUTER_INTERFACE_NAME_0 \
            --vpn-tunnel=TUNNEL_NAME_0 \
            --region=REGION
         

By default, if you don't specify an IP version, the command assigns an IPv4 address to the interface.

The command output looks similar to the following example:
         
         Updated [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/routers/router-a].
         

  2. Add the BGP peer configuration to the interface for the **first tunnel** ; replace `PEER_NAME_0` with a name for the peer VPN interface, and replace `PEER_ASN` with the ASN of the BGP peer:
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
            --peer-name=PEER_NAME_0 \
            --peer-asn=PEER_ASN \
            --interface=ROUTER_INTERFACE_NAME_0 \
            --region=REGION
         

If you want to specify learned routes for the peer, add the `--set-custom-learned-route-ranges` flag. You can also optionally use the `--custom-learned-route-priority` flag to set a priority value of between `0` and `65535` (inclusive) for the routes. Each BGP session can have one priority value that applies to all the learned routes that you configured for the session. For more information about this feature, see [Learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes).

For example, to add learned routes and set a priority for the routes, run the following command:
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
            --peer-name=PEER_NAME_0 \
            --peer-asn=PEER_ASN \
            --interface=ROUTER_INTERFACE_NAME_0 \
            --region=REGION \
            --set-custom-learned-route-ranges=IP_PREFIXES \
            --custom-learned-route-priority=CUSTOM_ROUTE_PRIORITY
         

If you want to use MD5 authentication, add the `--md5-authentication-key` flag. Use this field to provide your secret key:
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
            --peer-name=PEER_NAME_0 \
            --peer-asn=PEER_ASN \
            --interface=ROUTER_INTERFACE_NAME_0 \
            --region=REGION \
            --md5-authentication-key=AUTHENTICATION_KEY
         

The command output looks similar to the following example:
         
         Creating peer [bgp-peer-tunnel-a-to-on-prem-if-0] in router [router-a]...done.
         




**For the second VPN tunnel**

  1. Add an interface to the Cloud Router:
         
         gcloud compute routers add-interface ROUTER_NAME \
          --interface-name=ROUTER_INTERFACE_NAME_1 \
          --vpn-tunnel=TUNNEL_NAME_1 \
          --region=REGION
         

  2. Add a BGP peer configuration to the interface for the **second tunnel** ; replace `PEER_NAME_1` with a name for the peer VPN interface, and replace `PEER_ASN` with the ASN configured for the peer VPN gateway:
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
          --peer-name=PEER_NAME_1 \
          --peer-asn=PEER_ASN \
          --interface=ROUTER_INTERFACE_NAME_1 \
          --region=REGION
         

If you configured learned routes on the first tunnel, you might want to configure the same routes on the second tunnel. For example, you can configure the second tunnel to function as a backup for the routes; in this case, give the routes a less preferential priority (a higher number). If you want to use both tunnels together as part of an equal-cost multipath (ECMP) route, give the routes the same priority that they had on the first tunnel. In either case, use a command like the following:
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
            --peer-name=PEER_NAME_1 \
            --peer-asn=PEER_ASN \
            --interface=ROUTER_INTERFACE_NAME_1 \
            --region=REGION \
            --set-custom-learned-route-ranges=IP_PREFIXES \
            --custom-learned-route-priority=CUSTOM_ROUTE_PRIORITY
         

If you want to use MD5 authentication, use the `--md5-authentication-key` flag to provide your secret key:
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
          --peer-name=PEER_NAME_1 \
          --peer-asn=PEER_ASN \
          --interface=ROUTER_INTERFACE_NAME_1 \
          --region=REGION \
          --md5-authentication-key=AUTHENTICATION_KEY
         




###  Manual 

To manually allocate the IPv4 BGP addresses associated with the Cloud Router interface and BGP peer, complete the following steps.

For each VPN tunnel, decide on a pair of link-local IPv4 addresses in a `/30` block from the `169.254.0.0/16` address range (a total of four `/30` subnets, one per HA VPN gateway). The IPv4 subnets that you specify must be unique among all Cloud Routers in all regions of a VPC network.

For each tunnel, assign one of these BGP IPv4 addresses to the Cloud Router, and the other BGP IPv4 address to your peer VPN gateway. Configure your peer VPN device to use the peer BGP IPv4 address.

In the following commands, replace the following:

  * `GOOGLE_BGP_IP_0`: the BGP IPv4 address of the Cloud Router's interface for the tunnel on Cloud VPN gateway `interface 0`; `PEER_BGP_IP_0` represents the BGP IPv4 address of its peer
  * `GOOGLE_BGP_IP_1`: the BGP IPv4 address of the Cloud Router's interface for the tunnel on Cloud VPN gateway `interface 1`; `PEER_BGP_IP_1` represents the BGP IPv4 address of its peer
  * `MASK_LENGTH`: `30`; Cloud Router must use a unique `/30` subnet from the `169.254.0.0/16` IPv4 address range



**For the first VPN tunnel**

  1. Add an interface to the Cloud Router; replace `ROUTER_INTERFACE_NAME_0` with a name for the interface:
         
         gcloud compute routers add-interface ROUTER_NAME \
           --interface-name=ROUTER_INTERFACE_NAME_0 \
           --vpn-tunnel=TUNNEL_NAME_0 \
           --ip-address=GOOGLE_BGP_IP_0 \
           --mask-length 30 \
           --region=REGION
         

The command output looks similar to the following example:
         
         Updated [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/routers/router-a].
         

  2. Add a BGP peer configuration to the interface; replace `PEER_NAME_0` with a name for the peer, and replace `PEER_ASN` with the ASN configured for the peer VPN gateway:
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
          --peer-name=PEER_NAME_0 \
          --peer-asn=PEER_ASN \
          --interface=ROUTER_INTERFACE_NAME_0 \
          --peer-ip-address=PEER_BGP_IP_0 \
          --region=REGION
         

If you want to specify learned routes for the peer, add the `--set-custom-learned-route-ranges` flag. You can also optionally use the `--custom-learned-route-priority` flag to set a priority value of between `0` and `65535` (inclusive) for the routes. Each BGP session can have one priority value that applies to all the learned routes that you configured for the session. For more information about this feature, see [Learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes).

For example, to add learned routes and set a priority for the routes, run the following command:
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
            --peer-name=PEER_NAME_0 \
            --peer-asn=PEER_ASN \
            --interface=ROUTER_INTERFACE_NAME_0 \
            --region=REGION \
            --set-custom-learned-route-ranges=IP_PREFIXES \
            --custom-learned-route-priority=CUSTOM_ROUTE_PRIORITY
         

If you want to use MD5 authentication, use the `--md5-authentication-key` flag to provide your secret key:
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
           --peer-name=PEER_NAME_0 \
           --peer-asn=PEER_ASN \
           --interface=ROUTER_INTERFACE_NAME_0 \
           --peer-ip-address=PEER_BGP_IP_0 \
           --region=REGION \
           --md5-authentication-key=AUTHENTICATION_KEY
         

The command output looks similar to the following example:
         
         Creating peer [bgp-peer-tunnel-a-to-on-prem-if-0] in router [router-a]...done.
         




**For the second VPN tunnel**

  1. Add an interface to the Cloud Router; replace `ROUTER_INTERFACE_NAME_1` with a name for the interface:
         
         gcloud compute routers add-interface ROUTER_NAME \
          --interface-name=ROUTER_INTERFACE_NAME_1 \
          --vpn-tunnel=TUNNEL_NAME_1 \
          --ip-address=GOOGLE_BGP_IP_1 \
          --mask-length 30 \
          --region=REGION
         

  2. Add a BGP peer configuration to the interface; replace `PEER_NAME_1` with a name for the peer, and replace `PEER_ASN` with the ASN configured for the peer VPN gateway:
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
          --peer-name=PEER_NAME_1 \
          --peer-asn=PEER_ASN \
          --interface=ROUTER_INTERFACE_NAME_1 \
          --peer-ip-address=PEER_BGP_IP_1 \
          --region=REGION
         

If you configured learned routes on the first tunnel, you might want to specify the same routes on the second tunnel. For example, you can configure the second tunnel to function as a backup for the routes; in this case, give the routes a less preferential priority (a higher number). If you want to use both tunnels together as part of an equal-cost multipath (ECMP) route, give the routes the same priority that they had on the first tunnel. In either case, use a command like the following:
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
            --peer-name=PEER_NAME_1 \
            --peer-asn=PEER_ASN \
            --interface=ROUTER_INTERFACE_NAME_1 \
            --region=REGION \
            --set-custom-learned-route-ranges=IP_PREFIXES \
            --custom-learned-route-priority=PRIORITY
         

Optional: To enable MD5 authentication, use the `--md5-authentication-key` flag to provide your secret key:
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
           --peer-name=PEER_NAME_1 \
           --peer-asn=PEER_ASN \
           --interface=ROUTER_INTERFACE_NAME_0 \
           --peer-ip-address=PEER_BGP_IP_0 \
           --region=REGION \
           --md5-authentication-key=AUTHENTICATION_KEY
         




**Assign IPv6 next-hop addresses**

Use the commands in this section only if you want VPN tunnels that use MP-BGP and exchange both IPv4 and IPv6 traffic. If you don't want to route IPv6 traffic over this tunnel, or if you plan to add a single IPv6 BGP session to this tunnel later, then you can use the commands listed in **Assign IPv4 BGP addresses**.

###  Automatic 

If you create an IPv4 BGP session that uses MP-BGP, Google Cloud can assign IPv6 next-hop addresses automatically for you. Google Cloud assigns unused addresses from the `2600:2d00:0:2::/63` IPv6 address range.

This configuration has no relation to whether you choose automatic or manual configuration for the Cloud Router and BGP peer IPv4 addresses. The following commands use automatic configuration. However, you can also assign BGP IPv4 and BGP peer IPv4 addresses by using the `--ip-address` and `--peer-ip-address` flags that are described in **Assign IPv4 BGP addresses**.

**For the first VPN tunnel**

  1. Add an interface to the Cloud Router:
         
         gcloud compute routers add-interface ROUTER_NAME \
            --interface-name=ROUTER_INTERFACE_NAME_0 \
            --vpn-tunnel=TUNNEL_NAME_0 \
            --region=REGION
         

The command output looks similar to the following example:
         
         Updated [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/routers/router-a].
         

  2. Add a BGP peer configuration to the interface for the **first tunnel** ; replace `PEER_NAME_0` with a name for the peer VPN interface, and replace `PEER_ASN` with the ASN configured for the peer VPN gateway:
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
            --peer-name=PEER_NAME_0 \
            --peer-asn=PEER_ASN \
            --interface=ROUTER_INTERFACE_NAME_0 \
            --region=REGION \
            --enable-ipv6
         

By specifying the `--enable-ipv6` flag, you enable IPv6 route exchange in this IPv4 BGP session, which is required to assign IPv6 next hop addresses. You can disable IPv6 route exchange later. For more information, see [Configure multiprotocol BGP for IPv4 or IPv6 sessions](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-mp-bgp).

The command output looks similar to the following example:
         
         Creating peer [bgp-peer-tunnel-a-to-on-prem-if-0] in router [router-a]...done.
         




**For the second VPN tunnel**

  1. Add a second interface to the Cloud Router:
         
         gcloud compute routers add-interface ROUTER_NAME \
          --interface-name=ROUTER_INTERFACE_NAME_1 \
          --vpn-tunnel=TUNNEL_NAME_1 \
          --region=REGION
         

  2. Add a BGP peer configuration to the interface for the **second tunnel** ; replace `PEER_NAME_1` with a name for the peer VPN interface, and replace `PEER_ASN` with the ASN configured for the peer VPN gateway:
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
          --peer-name=PEER_NAME_1 \
          --peer-asn=PEER_ASN \
          --interface=ROUTER_INTERFACE_NAME_1 \
          --region=REGION \
          --enable-ipv6
         




###  Manual 

When you create an IPv4 BGP session that uses MP-BGP, you can manually configure IPv6 next-hop addresses for both Cloud Router and the BGP peer.

This configuration has no relation to whether you choose automatic or manual configuration of the Cloud Router and BGP peer IPv4 addresses. For examples on how to configure those addresses manually, see **Assign IPv4 BGP addresses**.

For each VPN tunnel, decide on a pair of IPv6 next hop addresses. The IPv6 next hop addresses that you specify must be unique among all Cloud Routers in all regions of a VPC network, and selected from the internal IPv6 address ranges that have been pre-allocated by Google: `2600:2d00:0:2::/63`.

To manually allocate the BGP IPv6 next-hop addresses, complete the following steps.

**For the first VPN tunnel**

  1. Add an interface to the Cloud Router:
         
         gcloud compute routers add-interface ROUTER_NAME \
            --interface-name=ROUTER_INTERFACE_NAME_0 \
            --vpn-tunnel=TUNNEL_NAME_0 \
            --region=REGION
         

The command output looks similar to the following example:
         
         Updated [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/routers/router-a].
         

  2. Add a BGP peer configuration to the interface for the **first tunnel**.
         
         gcloud compute routers add-bgp-peerROUTER_NAME \
           --peer-name=PEER_NAME_0 \
           --peer-asn=PEER_ASN \
           --interface=ROUTER_INTERFACE_NAME_0 \
           --region=REGION \
           --enable-ipv6 \
           --ipv6-nexthop-address=IPV6_NEXTHOP_ADDRESS \
           --peer-ipv6-nexthop-address=PEER_IPV6_NEXTHOP_ADDRESS
         

In the commands, replace the following:

     * `PEER_NAME_0` with a name for the peer VPN interface
     * `PEER_ASN` with the ASN configured for the peer VPN gateway
     * `IPV6_NEXTHOP_ADDRESS`: the next hop address for IPv6 routes that are advertised by Cloud Router; the address must be in the `2600:2d00:0:2::/63` IPv6 address range
     * `PEER_IPV6_NEXTHOP_ADDRESS`: the next hop address for IPv6 routes that are learned by Cloud Router from the BGP peer; the address must be in the `2600:2d00:0:2::/63` IPv6 address range

The command output looks similar to the following example:
    
    Creating peer [bgp-peer-tunnel-a-to-on-prem-if-0] in router [router-a]...done.
    

**For the second VPN tunnel**

  3. Add a second interface to the Cloud Router.
         
         gcloud compute routers add-interface ROUTER_NAME \
          --interface-name=ROUTER_INTERFACE_NAME_1 \
          --vpn-tunnel=TUNNEL_NAME_1 \
          --region=REGION
         

  4. Add a BGP peer configuration to the second interface for the **second tunnel**.
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
           --peer-name=PEER_NAME_1 \
           --peer-asn=PEER_ASN \
           --interface=ROUTER_INTERFACE_NAME_1 \
           --region=REGION \
           --enable-ipv6 \
           --ipv6-nexthop-address=IPV6_NEXTHOP_ADDRESS \
           --peer-ipv6-nexthop-address=PEER_IPV6_NEXTHOP_ADDRESS
         

In the commands, replace the following:

     * `PEER_NAME_1` with a name for the peer VPN interface
     * `PEER_ASN` with the ASN configured for the peer VPN gateway
     * `IPV6_NEXTHOP_ADDRESS`: the next hop address for IPv6 routes that are advertised by Cloud Router
     * `PEER_IPV6_NEXTHOP_ADDRESS`: the next hop address for IPv6 routes learned by the Cloud Router from the BGP peer



###  API 

To create BGP sessions, follow these steps:

  1. To create a Cloud Router interface, make one of the following requests:

     * `PATCH`: Use the [`routers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/patch)
     * `UPDATE`: Use the [`routers.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/update)

The `PATCH` request updates only the parameters that you include, whereas the `UPDATE` request updates all the parameters of a Cloud Router.

Each BGP address range for each IPv4 BGP session must be unique among all Cloud Routers in all regions of a VPC network.

Repeat this step and command for each VPN tunnel on the second HA VPN gateway.
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
    {
      "interfaces": [
        {
          "name": "if-tunnel-a-to-on-prem-if-0",
          "linkedVpnTunnel": "ha-vpn-gw-a-tunnel-0",
          "ipRange": "169.254.0.1/30"
          }
        ]
    }
    

  2. To add a BGP peer configuration to the interface, make one of the following requests:

     * `PATCH`: Use the [`routers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/patch)
     * `UPDATE`: Use the [`routers.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/update)

Repeat this command for the other VPN tunnel, changing all options except `name`and `peerAsn`.

For example:
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
    {
      "bgpPeers": [
      {
        "interfaceName": "if-tunnel-a-to-on-prem-if-0",
        "ipAddress": "169.254.0.1",
        "name": "bgp-peer-tunnel-a-to-on-prem-if-0",
        "peerAsn": 65002,
        "peerIpAddress": "169.254.0.2",
        "advertiseMode": "DEFAULT"
        }
      ]
    }
    

The following example includes a command to add a BGP peer with IPv6 route exchange enabled and manually configured IPv6 next-hop addresses. If you omit `ipv6NexthopAddress` and `peerIpv6NexthopAddress`, then the IPv6 next-hop addresses are automatically assigned.
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
    {
      "bgpPeers": [
      {
        "interfaceName": "if-tunnel-a-to-on-prem-if-0",
        "ipAddress": "169.254.0.1",
        "name": "bgp-peer-tunnel-a-to-on-prem-if-0",
        "peerAsn": 65002,
        "peerIpAddress": "169.254.0.2",
        "advertiseMode": "DEFAULT",
        "enableIpv6": true,
        "ipv6NexthopAddress: "2600:2d00:0:2::1"
        "peerIpv6NexthopAddress: "2600:2d00:0:2::2"
        }
      ]
    }
    

If you want to specify learned routes for the peer, define the IP prefixes for the routes. You can also optionally set a priority value of between `0` and `65535` (inclusive) for the routes. Each BGP session can have one priority value that applies to all the custom learned routes that you configured for the session. For more information about this feature, see [Learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes).
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
    {
      "bgpPeers": [
      {
        "interfaceName": "if-tunnel-a-to-on-prem-if-0",
        "ipAddress": "169.254.0.1",
        "name": "bgp-peer-tunnel-a-to-on-prem-if-0",
        "peerAsn": 65002,
        "peerIpAddress": "169.254.0.2",
        "advertiseMode": "DEFAULT",
        "enableIpv6": true,
        "ipv6NexthopAddress": "2600:2d00:0:2::1",
        "peerIpv6NexthopAddress": "2600:2d00:0:2::2",
        "customLearnedRoutePriority": 200,
        "customLearnedIpRanges": [
            {
              "range": "1.2.3.4"
            },
            {
              "range": "6.7.0.0/16"
            },
            {
              "range": "2001:db8:abcd:12::/64"
            }
          ]
          }
        ]
      }
    

To configure the session for MD5 authentication, include an authentication key in your request by adding both the key and the name of the key. Then, when creating the BGP peering session, reference this key by its name.
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
    {
      "md5AuthenticationKeys": [
        {
        "name": "bgppeer-1-key",
        "key": "secret_key_value"
        }
        ],
    }
    {
      "bgpPeers": [
      {
        "interfaceName": "if-tunnel-a-to-on-prem-if-0",
        "ipAddress": "169.254.0.1",
        "name": "bgp-peer-tunnel-a-to-on-prem-if-0",
        "peerAsn": 65002,
        "peerIpAddress": "169.254.0.2",
        "advertiseMode": "DEFAULT",
        "md5AuthenticationKeyName": "bgppeer-1-key"
        }
      ]
    }
    




#### IPv6 BGP sessions

###  Console 

To create BGP sessions, follow these steps:

  1. Click **Configure BGP session**.
  2. On the **Create BGP session** page, complete the following steps:

     1. For **BGP session type** , select **IPv6 BGP session**.
     2. For **Name** , enter a name for the BGP session.
     3. For **Peer ASN** , enter the peer ASN configured for the peer VPN gateway.
     4. Optional: For **Advertised route priority (MED)** , enter the priority of routes advertised to this BGP peer.
     5. Optional: To enable IPv4 route exchange, click the **Enable IPv4 traffic** toggle.
     6. For **Allocate BGP IPv6 address** , select **Automatically** or **Manually**. If you select **Manually** , do the following:

        1. For **Cloud Router BGP IPv6 address** , enter the Cloud Router BGP IPv6 address.
        2. For **BGP peer IPv6 address** , enter the IPv6 address of the BGP peer. The IPv6 address must meet the following requirements: 
           * Each address must be unique local addresses (ULA) from the `fdff:1::/64` address range with a mask length of `/64`. For example, `fdff:1::1`.
           * Each address must be unique among all Cloud Routers in all regions of a VPC network.

If you select **Automatically** , Google Cloud automatically selects the IPv6 addresses for your BGP session.

     7. Optional: If you enabled IPv4 route exchange in the previous step, for **Allocate BGP IPv4 next hop** , select **Automatically** or **Manually**. If you select **Manually** , do the following:

        1. In the **Cloud Router BGP IPv4 next hop** field, enter an IPv4 address in the `169.254.0.0/16` address range. This IP address is the next hop address for IPv4 routes that are advertised by the Cloud Router.
        2. In the **Peer BGP IPv4 next hop** field, enter an IP address in the `169.254.0.0/16` address range. This IP address is the next hop address for IPv4 routes learned by the Cloud Router from the BGP peer.
        3. Optional: Expand the **Advanced options** section.
        4. To enable **BGP peer** , select **Enabled**. If enabled, the peer connection is established with routing information. For more information, see [Establish BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-bgp).
        5. To add **MD5 authentication** , select **Enabled**. If enabled, you can use MD5 authentication to authenticate BGP sessions between Cloud Router and its peers. For more information, see [Use MD5 authentication](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication). You can alternatively choose to enable MD5 authentication later.
        6. To add outbound routes to the BGP session, for **Priority of all custom learned routes** , enter a learned route priority. For more information, see [Learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes).
  3. Click **Save and continue**.

  4. Repeat the previous steps for the rest of the tunnels configured on the gateway. For each tunnel, use a different Cloud Router BGP IP address and BGP peer IP address.

  5. Click **Save BGP configuration**. 




###  gcloud 

To create BGP sessions, follow these steps:

In the commands, replace the following:

  * `ROUTER_INTERFACE_NAME_0` and `ROUTER_INTERFACE_NAME_1`: a name for the Cloud Router interface; it can be helpful to use names related to the tunnel names configured previously
  * `TUNNEL_NAME_0` and `TUNNEL_NAME_1`: the tunnel associated with the HA VPN gateway interface that you configured
  * `IP_VERSION`: `IPV6`. This parameter is only required if you want Google Cloud to assign the IPv6 address automatically for this interface. If you are manually assigning an IPv6 address to this interface, you can omit this flag.

  * `IP_PREFIXES` and `CUSTOM_ROUTE_PRIORITY`: values that let you manually specify learned routes for a BGP session; for more information about this feature, see [Learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes).

  * `AUTHENTICATION_KEY`: the secret key to use for MD5 authentication; for more information about this optional feature, see [Use MD5 authentication](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication).




**Optional: Assign a BGP identifier range**

When you add the first interface to a Cloud Router, a BGP identifier range is automatically assigned to the Cloud Router. If you prefer to define your own BGP identifier range for a Cloud Router, you can create your own range. You can also modify this range later. For more information, see [Configure the BGP identifier range for a Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configure-bgp-identifier).

**Assign IPv6 BGP addresses**

The following procedures create IPv6 BGP sessions with automatically or manually configured BGP IPv6 and BGP peer IPv6 addresses.

If you want to use IPv6 BGP with MP-BGP, run the commands listed in **Assign IPv4 next-hop addresses**.

###  Automatic 

To let Google Cloud automatically choose the IPv6 addresses for the BGP session, complete the following steps.

**For the first VPN tunnel**

  1. Add an interface to the Cloud Router:
         
         gcloud compute routers add-interface ROUTER_NAME \
            --interface-name=ROUTER_INTERFACE_NAME_0 \
            --vpn-tunnel=TUNNEL_NAME_0 \
            --region=REGION \
            --ip-version=IPV6
         

The command output looks similar to the following example:
         
         Updated [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/routers/router-a].
         

  2. Add a BGP peer configuration to the interface for the **first tunnel** ; replace `PEER_NAME_0` with a name for the peer VPN interface, and replace `PEER_ASN` with the ASN configured for the peer VPN gateway:
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
            --peer-name=PEER_NAME_0 \
            --peer-asn=PEER_ASN \
            --interface=ROUTER_INTERFACE_NAME_0 \
            --region=REGION
         

If you want to specify learned routes for the peer, add the `--set-custom-learned-route-ranges` flag. You can also optionally use the `--custom-learned-route-priority` flag to set a priority value of between `0` and `65535` (inclusive) for the routes. Each BGP session can have one priority value that applies to all the learned routes that you configured for the session. For more information about this feature, see [Learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes).

For example, to add learned routes and set a priority for the routes, run the following command:
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
            --peer-name=PEER_NAME_0 \
            --peer-asn=PEER_ASN \
            --interface=ROUTER_INTERFACE_NAME_0 \
            --region=REGION \
            --set-custom-learned-route-ranges=IP_PREFIXES \
            --custom-learned-route-priority=CUSTOM_ROUTE_PRIORITY
         

Optional: If you want to enable MD5 authentication, use the `--md5-authentication-key` flag to provide your secret key:
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
            --peer-name=PEER_NAME_0 \
            --peer-asn=PEER_ASN \
            --interface=ROUTER_INTERFACE_NAME_0 \
            --region=REGION \
            --md5-authentication-key=AUTHENTICATION_KEY
         

The command output looks similar to the following example:
         
         Creating peer [bgp-peer-tunnel-a-to-on-prem-if-0] in router [router-a]...done.
         




**For the second VPN tunnel**

  1. Add a second interface to the Cloud Router:
         
         gcloud compute routers add-interface ROUTER_NAME \
           --interface-name=ROUTER_INTERFACE_NAME_1 \
           --vpn-tunnel=TUNNEL_NAME_1 \
           --region=REGION \
           --ip-version=IPV6
         

  2. Add a BGP peer configuration to the interface for the **second tunnel** ; replace `PEER_NAME_1` with a name for the peer VPN interface, and replace `PEER_ASN` with the ASN configured for the peer VPN gateway:
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
          --peer-name=PEER_NAME_1 \
          --peer-asn=PEER_ASN \
          --interface=ROUTER_INTERFACE_NAME_1 \
          --region=REGION
         

If you configured learned routes on the first tunnel, you might want to configure the same routes on the second tunnel. For example, you can configure the second tunnel to function as a backup for the routes; in this case, give the routes a less preferential priority (a higher number). If you want to use both tunnels together as part of an equal-cost multipath (ECMP) route, give the routes the same priority that they had on the first tunnel. In either case, use a command like the following:
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
          --peer-name=PEER_NAME_1 \
          --peer-asn=PEER_ASN \
          --interface=ROUTER_INTERFACE_NAME_1 \
          --region=REGION \
          --set-custom-learned-route-ranges=IP_PREFIXES \
          --custom-learned-route-priority=CUSTOM_ROUTE_PRIORITY
         

Optional: If you want to enable MD5 authentication, use the `--md5-authentication-key` flag to provide your secret key:
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
          --peer-name=PEER_NAME_1 \
          --peer-asn=PEER_ASN \
          --interface=ROUTER_INTERFACE_NAME_1 \
          --region=REGION \
          --md5-authentication-key=AUTHENTICATION_KEY
         




###  Manual 

To manually allocate IPv6 addresses to the BGP session associated with the Cloud Router interface and BGP peer, complete the following steps.

For each VPN tunnel, decide on a pair of appropriate IPv6 addresses for the BGP session based on the type of BGP session you are configuring.

Each IPv6 address must be unique local addresses (ULA) from the `fdff:1::/64` IPv6 address range with a mask length of `/126` or lower. For example, `fdff:1::1`.

Each IPv6 address must be unique among all Cloud Routers in all regions of a VPC network.

For each tunnel, assign one of these IPv6 addresses to the Cloud Router, and the other IPv6 address to your peer VPN gateway. Configure your peer VPN device to use the peer IPv6 address of the BGP session.

In the following commands, replace the following:

  * `GOOGLE_BGP_IPV6_0`: the IPv6 address of the Cloud Router's interface for the tunnel on Cloud VPN gateway `interface 0`; `PEER_BGP_IPV6_0` represents the IPv6 address of its BGP peer and must match the IP version of `GOOGLE_BGP_IPV6_0`
  * `GOOGLE_BGP_IPV6_1`: the IPv6 address of the Cloud Router's interface for the tunnel on Cloud VPN gateway `interface 1`; `PEER_BGP_IPV6_1` represents the IPv6 address of its BGP peer and must match the IP version of `GOOGLE_BGP_IPV6_1`



**For the first VPN tunnel**

  1. Add an interface to the Cloud Router; replace `ROUTER_INTERFACE_NAME_0` with a name for the interface:
         
         gcloud compute routers add-interface ROUTER_NAME \
          --interface-name=ROUTER_INTERFACE_NAME_0 \
          --vpn-tunnel=TUNNEL_NAME_0 \
          --ip-address=GOOGLE_BGP_IPV6_0 \
          --mask-length=MASK_LENGTH  \
          --region=REGION \
         

Replace `MASK_LENGTH` with a value of `126` or lower.

The command output looks similar to the following example:
         
         Updated [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/routers/router-a].
         

  2. Add a BGP peer configuration to the interface; replace PEER_NAME_0`with a name for the peer, and replace`PEER_ASN` with the ASN configured for the peer VPN gateway:
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
          --peer-name=PEER_NAME_0 \
          --peer-asn=PEER_ASN \
          --interface=ROUTER_INTERFACE_NAME_0 \
          --peer-ip-address=PEER_BGP_IPV6_0 \
          --region=REGION
         

If you want to specify learned routes for the peer, add the `--set-custom-learned-route-ranges` flag. You can also optionally use the `--custom-learned-route-priority` flag to set a priority value of between `0` and `65535` (inclusive) for the routes. Each BGP session can have one priority value that applies to all the learned routes that you configured for the session. For more information about this feature, see [Learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes).

For example, to add learned routes and set a priority for the routes, run the following command:
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
          --peer-name=PEER_NAME_0 \
          --peer-asn=PEER_ASN \
          --interface=ROUTER_INTERFACE_NAME_0 \
          --region=REGION \
          --set-custom-learned-route-ranges=IPV6_PREFIXES \
          --custom-learned-route-priority=CUSTOM_ROUTE_PRIORITY
         

Optional: If you want to enable MD5 authentication, use the `--md5-authentication-key` flag to provide your secret key:
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
          --peer-name=PEER_NAME_0 \
          --peer-asn=PEER_ASN \
          --interface=ROUTER_INTERFACE_NAME_0 \
          --peer-ip-address=PEER_BGP_IPV6_0 \
          --region=REGION \
          --md5-authentication-key=AUTHENTICATION_KEY
         

The command output looks similar to the following example:
         
         Creating peer [bgp-peer-tunnel-a-to-on-prem-if-0] in router [router-a]...done.
         




**For the second VPN tunnel**

  1. Add a second interface to the Cloud Router; replace `ROUTER_INTERFACE_NAME_1` with a name for the interface:
         
         gcloud compute routers add-interface ROUTER_NAME \
          --interface-name=ROUTER_INTERFACE_NAME_1 \
          --vpn-tunnel=TUNNEL_NAME_1 \
          --ip-address=GOOGLE_BGP_IPV6_1 \
          --mask-length=MASK_LENGTH \
          --region=REGION \
         

Replace `MASK_LENGTH` with a value of `64` or lower.

  2. Add a BGP peer configuration to the interface; replace `PEER_NAME_1` with a name for the peer, and replace `PEER_ASN` with the ASN configured for the peer VPN gateway:
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
          --peer-name=PEER_NAME_1 \
          --peer-asn=PEER_ASN \
          --interface=ROUTER_INTERFACE_NAME_1 \
          --peer-ip-address=PEER_BGP_IPV6_1 \
          --region=REGION
         

If you configured learned routes on the first tunnel, you might want to specify the same routes on the second tunnel. For example, you can configure the second tunnel to function as a backup for the routes; in this case, give the routes a less preferential priority (a higher number). If you want to use both tunnels together as part of an equal-cost multipath (ECMP) route, give the routes the same priority that they had on the first tunnel. In either case, use a command like the following:
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
          --peer-name=PEER_NAME_1 \
          --peer-asn=PEER_ASN \
          --interface=ROUTER_INTERFACE_NAME_1 \
          --region=REGION \
          --set-custom-learned-route-ranges=IPV6_PREFIXES \
          --custom-learned-route-priority=PRIORITY
         

Optional: If you want to enable MD5 authentication, use the `--md5-authentication-key` flag to provide your secret key:
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
          --peer-name=PEER_NAME_1 \
          --peer-asn=PEER_ASN \
          --interface=ROUTER_INTERFACE_NAME_1 \
          --peer-ip-address=PEER_BGP_IPV6_1 \
          --region=REGION \
          --md5-authentication-key=AUTHENTICATION_KEY
         




**Assign IPv4 next-hop addresses**

Use the commands in this section only if you want VPN tunnels that use MP-BGP. With MP-BGP, you can exchange IPv4 routes over IPv6 BGP sessions.

If you don't plan to use MP-BGP in the BGP session for the tunnel, then use the commands listed in **Assign IPv6 BGP addresses**.

You can choose to automatically or manually configure BGP peer next hop IPv4 or IPv6 addresses.

###  Automatic 

If you create an IPv6 BGP session that uses MP-BGP, Google Cloud can assign IPv4 next-hop addresses automatically for you. Google Cloud assigns unused addresses from the `169.254.0.0/16` address range.

This configuration has no relation to whether you choose automatic or manual configuration for the Cloud Router and BGP peer IPv6 addresses. The following commands use automatic configuration. However, you can also assign the IPv6 addresses to the Cloud Router interfaces and BGP peers by using the `--ip-address` and `--peer-ip-address` flags that are described in **Assign IPv6 BGP IP addresses**.

**For the first VPN tunnel**

  1. Add an interface to the Cloud Router:
         
         gcloud compute routers add-interface ROUTER_NAME \
           --interface-name=ROUTER_INTERFACE_NAME_0 \
           --vpn-tunnel=TUNNEL_NAME_0 \
           --region=REGION \
           --ip-version=IPV6
         

The command output looks similar to the following example:
         
         Updated [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/routers/router-a].
         

  2. Add a BGP peer configuration to the interface for the **first tunnel** ; replace `PEER_NAME_0` with a name for the peer VPN interface, and replace `PEER_ASN` with the ASN configured for the peer VPN gateway:
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
            --peer-name=PEER_NAME_0 \
            --peer-asn=PEER_ASN \
            --interface=ROUTER_INTERFACE_NAME_0 \
            --region=REGION \
            --enable-ipv4
         

The command output looks similar to the following example:
         
         Creating peer [bgp-peer-tunnel-a-to-on-prem-if-0] in router [router-a]...done.
         




**For the second VPN tunnel**

  1. Add a second interface to the Cloud Router:
         
         gcloud compute routers add-interface ROUTER_NAME \
           --interface-name=ROUTER_INTERFACE_NAME_1 \
           --vpn-tunnel=TUNNEL_NAME_1 \
           --region=REGION \
           --ip-version=IPV6
         

  2. Add a BGP peer configuration to the second interface for the **second tunnel** ; replace `PEER_NAME_1` with a name for the peer VPN interface, and replace `PEER_ASN` with the ASN configured for the peer VPN gateway:
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
            --peer-name=PEER_NAME_1 \
            --peer-asn=PEER_ASN \
            --interface=ROUTER_INTERFACE_NAME_1 \
            --region=REGION \
            --enable-ipv4
         




###  Manual 

When you create IPv6 BGP sessions that use MP-BGP, you can manually configure IPv4 next-hop addresses for both Cloud Router and the BGP peer.

This configuration has no relation to whether you choose automatic or manual configuration of the Cloud Router and IPv6 addresses for BGP sessions. For examples on how to configure those addresses manually, see **Assign IPv6 BGP addresses**.

For each VPN tunnel, select a pair of IPv4 next-hop addresses from the link-local IPv4 address range `169.254.0.0/16`. These IPv4 addresses must be unique across all Cloud Routers in your VPC network.

To manually allocate the BGP IPv4 next hop addresses, complete the following steps.

**For the first VPN tunnel**

  1. Add an interface to the Cloud Router.
         
         gcloud compute routers add-interface ROUTER_NAME \
           --interface-name=ROUTER_INTERFACE_NAME_0 \
           --vpn-tunnel=TUNNEL_NAME_0 \
           --region=REGION \
           --ip-version=IPV6
         

The command output looks similar to the following example:
         
         Updated [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/routers/router-a].
         

  2. Add a BGP peer configuration to the interface for the **first tunnel**.
         
         gcloud compute routers add-bgp-peerROUTER_NAME \
           --peer-name=PEER_NAME_0 \
           --peer-asn=PEER_ASN \
           --interface=ROUTER_INTERFACE_NAME_0 \
           --region=REGION \
           --enable-ipv4 \
           --ipv4-nexthop-address=IPV4_NEXTHOP_ADDRESS \
           --peer-ipv4-nexthop-address=PEER_IPV4_NEXTHOP_ADDRESS
         

In the commands, replace the following:

     * `PEER_NAME_0` with a name for the peer VPN interface
     * `PEER_ASN` with the ASN configured for the peer VPN gateway
     * `IPV4_NEXTHOP_ADDRESS`: the next hop address for IPv4 routes that are advertised by Cloud Router; the address must be in the `169.254.0.0/16` IPv4 address range
     * `PEER_IPV4_NEXTHOP_ADDRESS`: the next hop address for IPv4 routes that are learned by Cloud Router from the BGP peer; the address must be in the `169.254.0.0/16` IPv4 address range

The command output looks similar to the following example:
    
    Creating peer [bgp-peer-tunnel-a-to-on-prem-if-0] in router [router-a]...done.
    

**For the second VPN tunnel**

  3. Add a second interface to the Cloud Router.
         
         gcloud compute routers add-interface ROUTER_NAME \
           --interface-name=ROUTER_INTERFACE_NAME_1 \
           --vpn-tunnel=TUNNEL_NAME_1 \
           --region=REGION \
           --ip-version=IPV6
         

  4. Add a BGP peer configuration to the interface for the **second tunnel**.
         
         gcloud compute routers add-bgp-peerROUTER_NAME \
           --peer-name=PEER_NAME_1 \
           --peer-asn=PEER_ASN \
           --interface=ROUTER_INTERFACE_NAME_1 \
           --region=REGION \
           --enable-ipv4 \
           --ipv4-nexthop-address=IPV4_NEXTHOP_ADDRESS \
           --peer-ipv4-nexthop-address=PEER_IPV4_NEXTHOP_ADDRESS
         

In the following commands, replace the following:

     * `PEER_NAME_1` with a name for the peer VPN interface
     * `PEER_ASN` with the ASN configured for the peer VPN gateway
     * `IPV4_NEXTHOP_ADDRESS`: the next hop address for IPv4 routes that are advertised by Cloud Router; the address must be in the `169.254.0.0/16` IPv4 address range
     * `PEER_IPV4_NEXTHOP_ADDRESS`: the next hop address for IPv4 routes that are learned by Cloud Router from the BGP peer; the address must be in the `169.254.0.0/16` IPv4 address range



###  API 

To create BGP sessions, follow these steps:

  1. To create a Cloud Router interface and assign it an IPv6 address, make either a `PATCH` or `UPDATE` request by using the [`routers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/patch) or the [`routers.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/update). `PATCH` updates only the parameters that you include. `UPDATE` updates all parameters for Cloud Router.

The following example creates an interface with a manually configured IPv6 address.
         
         PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
         {
           "interfaces": [
             {
               "name": "if-tunnel-a-to-on-prem-if-0",
               "linkedVpnTunnel": "ha-vpn-gw-a-tunnel-0",
               "ipRange": "fdff:1::/112"
               }
             ]
         }
         

Each BGP address range for each IPv6 BGP session must be unique among all Cloud Routers in all regions of a VPC network.

As another example, the following command creates an interface with an automatically assigned IPv6 address.
         
         PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
         {
           "interfaces": [
             {
               "name": "if-tunnel-a-to-on-prem-if-0",
               "linkedVpnTunnel": "ha-vpn-gw-a-tunnel-0",
               "ipVersion": "IPV6"
               }
             ]
         }
         

Repeat this step for each VPN tunnel on the HA VPN gateway.

  2. Add a BGP peer configuration to a Cloud Router for a VPN tunnel, make either a `PATCH` or `UPDATE` request by using the [`routers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/patch) or the [`routers.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/update). Repeat this command for the other VPN tunnel, changing all options except `name`and `peerAsn`.

For example:
         
         PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
         {
           "bgpPeers": [
           {
             "interfaceName": "if-tunnel-a-to-on-prem-if-0",
             "ipAddress": "fdff:1::1",
             "name": "bgp-peer-tunnel-a-to-on-prem-if-0",
             "peerAsn": 65002,
             "peerIpAddress": "fdff:1::2",
             "advertiseMode": "DEFAULT"
             }
           ]
         }
         

The following example includes a command to add a BGP peer for the IPv6 BGP interface with IPv4 route exchange enabled and IPv4 next-hop addresses manually configured. If you omit `ipv4NexthopAddress` and `peerIpv4NexthopAddress`, then IPv4 next-hop addresses are automatically assigned.
         
         PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers//ROUTER_NAME
         {
           "bgpPeers": [
           {
             "interfaceName": "if-tunnel-a-to-on-prem-if-0",
             "ipAddress": "fdff:1::1",
             "name": "bgp-peer-tunnel-a-to-on-prem-if-0",
             "peerAsn": 65002,
             "peerIpAddress": "fdff:1::2",
             "advertiseMode": "DEFAULT",
             "enableIpv4": true,
             "ipv4NexthopAddress: "169.254.0.1",
             "peerIpv4NexthopAddress: "169.254.0.2"
             }
           ]
         }
         

If you want to specify learned routes for the peer, define the IP prefixes for the routes. You can also optionally set a priority value of between `0` and `65535` (inclusive) for the routes. Each BGP session can have one priority value that applies to all the custom learned routes that you configured for the session. For more information, see [Learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes).
         
         PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
         {
           "bgpPeers": [
           {
             "interfaceName": "if-tunnel-a-to-on-prem-if-0",
             "ipAddress": "fdff:1::1",
             "name": "bgp-peer-tunnel-a-to-on-prem-if-0",
             "peerAsn": 65002,
             "peerIpAddress": "fdff:1::2",
             "advertiseMode": "DEFAULT",
             "enableIpv4": true,
             "ipv4NexthopAddress: "169.254.0.1",
             "peerIpv4NexthopAddress: "169.254.0.2"
             "customLearnedRoutePriority": 200,
             "customLearnedIpRanges": [
                 {
                   "range": "1.2.3.4"
                 },
                 {
                   "range": "6.7.0.0/16"
                 },
                 {
                   "range": "2001:db8:abcd:12::/64"
                 }
               ]
               }
             ]
         }
         

If you want to configure the session to use MD5 authentication, your request must include an authentication key, which means that it must provide both the key and a name for the key. It must also reference the key by name when creating the BGP peering session. For example:
         
         PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
         {
           "md5AuthenticationKeys": [
             {
             "name": "bgppeer-1-key",
             "key": "secret_key_value"
             }
             ],
         }
         {
           "bgpPeers": [
           {
             "interfaceName": "if-tunnel-a-to-on-prem-if-0",
             "ipAddress": "fdff:1::1",
             "name": "bgp-peer-tunnel-a-to-on-prem-if-0",
             "peerAsn": 65002,
             "peerIpAddress": "fdff:1::2",
             "advertiseMode": "DEFAULT",
             "md5AuthenticationKeyName": "bgppeer-1-key"
             }
           ]
         }
         




#### Both IPv4 BGP and IPv6 BGP sessions

Use the following steps to create both an IPv4 BGP session and an IPv6 BGP session that run in parallel in the same HA VPN tunnel.

To create this configuration, add two BGP interfaces and two BGP peers to your Cloud Router, linking them to the same VPN tunnel. You can't use MP-BGP on either of the BGP sessions.

###  Console 

To create both IPv4 and IPv6 BGP sessions, follow these steps:

  1. Click **Configure BGP session**.
  2. On the **Create BGP session** page, complete the following steps:

     1. For **BGP session type** , select **Both**.

**IPv4 BGP session**

     1. For **Name** , enter a name for the BGP session.
     2. For **Peer ASN** , enter the peer ASN configured for the peer VPN gateway.
     3. For **Allocate BGP IPv4 address** , select **Automatically** or **Manually**. If you select **Manually** , do the following:
     4. For **Cloud Router BGP IPv4 address** , enter the Cloud Router BGP IPv4 address.
     5. For **BGP peer IPv4 address** , enter the IPv4 address of the BGP peer. The IPv4 address must meet the following requirements:

        * Each IPv4 address must belong to the same `/30` subnet that fits within the `169.254.0.0/16` address range.
        * Each IPv4 address is the first or second host of the `/30` subnet. The first and the last IP addresses of the subnet are reserved for network and broadcast addresses.
        * Each IPv4 address range for a BGP session must be unique among all Cloud Routers in all regions of a VPC network.

If you select **Automatically** , Google Cloud automatically selects the IPv4 addresses for your BGP session.

If you select automatic IPv6 address allotment, Google Cloud automatically selects the IPv6 addresses for your BGP session.

     6. Optional: Expand the **Advanced options** section.

     7. To enable **BGP peer** , select **Enabled**. If enabled, the peer connection is established with routing information. For more information, see [Establish BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-bgp).

     8. To add **MD5 authentication** , select **Enabled**. If enabled, you can use MD5 authentication to authenticate BGP sessions between Cloud Router and its peers. For more information, see [Use MD5 authentication](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication). You can alternatively choose to enable MD5 authentication later.

     9. To add outbound routes to the BGP session, for **Priority of all custom learned routes** , enter a learned route priority. For more information, see [Learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes).

     10. Click **Save and continue**.

**IPv6 BGP session**

     1. For **Name** , enter a name for the BGP session.
     2. For **Peer ASN** , enter the peer ASN configured for the peer VPN gateway.
     3. Optional: For **Advertised route priority (MED)** , enter the priority of routes advertised to this BGP peer.
     4. For **Allocate BGP IPv6 address** , select **Automatically** or **Manually**. If you select **Manually** , do the following:
     5. For **Cloud Router BGP IPv6 address** , enter the Cloud Router BGP IPv6 address.
     6. For **BGP peer IPv6 address** , enter the IPv6 address of the BGP peer. The IPv4 address must meet the following requirements:

        * Each address must be unique local addresses (ULA) from the `fdff:1::/64` address range with a mask length of `/64`. For example, `fdff:1::1`.
        * Each address must be unique among all Cloud Routers in all regions of a VPC network.

If you select **Automatically** , Google Cloud automatically selects the IPv6 addresses for your BGP session.

     7. Optional: Expand the **Advanced options** section.

     8. To enable **BGP peer** , select **Enabled**. If enabled, the peer connection is established with routing information. For more information, see [Establish BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-bgp).

     9. To enable **MD5 authentication** , select **Enabled**. If enabled, MD5 authentication is used to authenticate BGP sessions between Cloud Router and its peers. For more information, see [Use MD5 authentication](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication). You can alternatively choose to enable MD5 authentication later.

     10. To add outbound routes to the BGP session, for **Priority of all custom learned routes** , enter a learned route priority. For more information, see [Learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes).

     11. Click **Save and continue**.

  3. Repeat the previous steps for the rest of the tunnels configured on the gateway. For each tunnel, use a different Cloud Router BGP IP address and BGP peer IP address.

  4. Click **Save BGP configuration**. 




###  gcloud 

To create BGP sessions, follow these steps:

In the commands, replace the following:

  * `ROUTER_INTERFACE_NAME_0_ipv4`and `ROUTER_INTERFACE_NAME_0_ipv6`: names for the first pair of Cloud Router BGP interfaces that share the same tunnel; it can be helpful to use names related to the tunnel names configured previously
  * `ROUTER_INTERFACE_NAME_1_ipv4`, `ROUTER_INTERFACE_NAME_1_ipv6`: names for the second set of Cloud Router BGP interfaces
  * `TUNNEL_NAME_0` and `TUNNEL_NAME_1`: the tunnel associated with the HA VPN gateway interface that you configured
  * `IP_PREFIXES` and `CUSTOM_ROUTE_PRIORITY`: values that let you manually specify learned routes for a BGP session; for more information about this feature, see [Learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes).
  * `AUTHENTICATION_KEY`: the secret key to use for MD5 authentication; for more information about this optional feature, see [Use MD5 authentication](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication).

In addition, you can choose to automatically or manually configure the IPv4 and IPv6 addresses for your Cloud Router interfaces and BGP peers.

**Optional: Assign a BGP identifier range**

When you add the first interface with an IPv6 address to a Cloud Router, a BGP identifier range is automatically assigned to the Cloud Router. If you prefer to define your own BGP identifier range for a Cloud Router, you can create your own range. You can also modify this range later. For more information, see [Configure the BGP identifier range for a Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configure-bgp-identifier).




###  Automatic 

To let Google Cloud automatically choose the BGP addresses, complete the following steps.

**For the first VPN tunnel**

  1. Add an interface with an IPv4 address to the Cloud Router.
         
         gcloud compute routers add-interface ROUTER_NAME \
            --interface-name=ROUTER_INTERFACE_NAME_0_ipv4 \
            --vpn-tunnel=TUNNEL_NAME_0 \
            --region=REGION
            --ip-version=IPV4
         

The command output looks similar to the following example:
         
         Updated [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/routers/router-a].
         

  2. Add a second interface with an IPv6 address to the same tunnel. Run the following command:
         
         gcloud compute routers add-interface ROUTER_NAME \
            --interface-name=ROUTER_INTERFACE_NAME_0_ipv6 \
            --vpn-tunnel=TUNNEL_NAME_0 \
            --region=REGION \
            --ip-version=IPV6
         

The command output looks similar to the following example:
         
         Updated [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/routers/router-a].
         

  3. Add a BGP peer configuration to the first interface with the IPv4 address for the **first tunnel** ; replace `PEER_NAME_0_ipv4` with a name for the peer VPN interface, and replace `PEER_ASN` with the ASN configured for the peer VPN gateway:
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
            --peer-name=PEER_NAME_0_ipv4 \
            --peer-asn=PEER_ASN \
            --interface=ROUTER_INTERFACE_NAME_0_ipv4 \
            --region=REGION
         

  4. Add a BGP peer configuration to the second interface with the IPv6 address for the **first tunnel** ; replace `PEER_NAME_0_ipv6` with a name for the peer VPN interface, and replace `PEER_ASN` with the ASN configured for the peer VPN gateway:
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
            --peer-name=PEER_NAME_0_ipv6 \
            --peer-asn=PEER_ASN \
            --interface=ROUTER_INTERFACE_NAME_0_ipv6 \
            --region=REGION
         

In most cases the `PEER_ASN` is the same, but it can be different depending on your on-premises network topology.




**For the second VPN tunnel**

  1. Add an interface with an IPv4 address to the Cloud Router:
         
         gcloud compute routers add-interface ROUTER_NAME \
          --interface-name=ROUTER_INTERFACE_NAME_1_ipv4 \
          --vpn-tunnel=TUNNEL_NAME_1 \
          --region=REGION
          --ip-version=IPV4
         

  2. Add an interface with an IPv6 address to the same tunnel. Run the following command:
         
         gcloud compute routers add-interface ROUTER_NAME \
          --interface-name=ROUTER_INTERFACE_NAME_1_ipv6 \
          --vpn-tunnel=TUNNEL_NAME_1 \
          --region=REGION \
          --ip-version=IPV6
         

  3. Add a BGP peer configuration to the first interface with the IPv4 address for the **second tunnel** ; replace `PEER_NAME_1_ipv4` with a name for the peer VPN interface, and replace `PEER_ASN` with the ASN configured for the peer VPN gateway:
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
          --peer-name=PEER_NAME_1_ipv4 \
          --peer-asn=PEER_ASN \
          --interface=ROUTER_INTERFACE_NAME_1_ipv4 \
          --region=REGION
         

  4. Add a BGP peer configuration to the second interface with the IPv6 address for the **second tunnel** ; replace `PEER_NAME_1_ipv6` with a name for the peer VPN interface, and replace `PEER_ASN` with the ASN configured for the peer VPN gateway:
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
            --peer-name=PEER_NAME_1_ipv6 \
            --peer-asn=PEER_ASN \
            --interface=ROUTER_INTERFACE_NAME_1_ipv6 \
            --region=REGION
         

In most cases the `PEER_ASN` is the same, but it can be different depending on your on-premises network topology.




###  Manual 

To manually allocate the IPv4 and IPv6 addresses associated with the Cloud Router interfaces and BGP peers, complete the following steps.

For each VPN tunnel, decide on a pair of appropriate BGP addresses based on the type of BGP session you are configuring. You must select four IP addresses in total for each type of session.

  * For your IPv4 BGP sessions, the four IPv4 addresses must be link-local IPv4 addresses in a `/30` block from the `169.254.0.0/16` range. For example, `169.254.0.1/30`.
  * For your IPv6 BGP sessions, the four IPv6 addresses must be unique local addresses (ULA) from the `fdff:1::/64` range with a length of `/126` or less. For example, `fdff:1:1:1::/112`.



The BGP addresses that you specify must be unique among all Cloud Routers in all regions of a VPC network.

For each tunnel, assign the BGP IPv6 addresses to the Cloud Router. Configure your peer VPN device to use the BGP peer IPv6 addresses.

In the following commands, replace the following:

  * `GOOGLE_BGP_IPV4_0`: the IPv4 address of the Cloud Router's interface for the tunnel on Cloud VPN gateway `interface 0`; `PEER_BGP_IPV4_0` represents the IPv4 address of its BGP peer, matches with `GOOGLE_BGP_IPV4_0`
  * `GOOGLE_BGP_IPV6_0`: the IPv6 address of the Cloud Router's interface for the tunnel on Cloud VPN gateway `interface 0`; `PEER_BGP_IPV6_0` represents the IPv6 address of its BGP peer, matches with `GOOGLE_BGP_IPV6_0`
  * `GOOGLE_BGP_IPV4_1`: the IPv4 address of the Cloud Router's interface for the tunnel on Cloud VPN gateway `interface 1`; `PEER_BGP_IPV4_1` represents the IPv4 address of its BGP peer, matches with `GOOGLE_BGP_IPV4_1`
  * `GOOGLE_BGP_IPV6_1`: the IPv6 address of the Cloud Router's interface for the tunnel on Cloud VPN gateway `interface 1`; `PEER_BGP_IPV6_1` represents the IPv6 address of its BGP peer, matches with `GOOGLE_BGP_IPV6_1`



**For the first VPN tunnel**

  1. Add an interface with an IPv4 address to the Cloud Router; replace `ROUTER_INTERFACE_NAME_0_ipv4` with a name for the interface:
         
         gcloud compute routers add-interface ROUTER_NAME \
           --interface-name=ROUTER_INTERFACE_NAME_0_ipv4 \
           --vpn-tunnel=TUNNEL_NAME_0 \
           --ip-address=GOOGLE_BGP_IPV4_0 \
           --mask-length 30 \
           --region=REGION
         

The command output looks similar to the following example:
         
         Updated [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/routers/router-a].
         

  2. Add an interface with an IPv6 address to the same tunnel; replace `ROUTER_INTERFACE_NAME_0_ipv6` with a name for the interface:
         
         gcloud compute routers add-interface ROUTER_NAME \
           --interface-name=ROUTER_INTERFACE_NAME_0_ipv6 \
           --vpn-tunnel=TUNNEL_NAME_0 \
           --ip-address=GOOGLE_BGP_IPV6_0 \
           --mask-length=MASK_LENGTH  \
           --region=REGION \
         

Replace `MASK_LENGTH` with a value of `64` or lower.

  3. Add a BGP peer configuration to the first interface for the **first tunnel** ; replace `PEER_NAME_0_ipv4` with a name for the peer VPN interface, and replace `PEER_ASN` with the ASN configured for the peer VPN gateway:
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
          --peer-name=PEER_NAME_0_ipv4 \
          --peer-asn=PEER_ASN \
          --interface=ROUTER_INTERFACE_NAME_0_ipv4 \
          --peer-ip-address=PEER_BGP_IPV4_0 \
          --region=REGION
         

  4. Add a BGP peer configuration to the second interface for the **first tunnel** ; replace `PEER_NAME_0_ipv6` with a name for the peer VPN interface, and replace `PEER_ASN` with the ASN configured for the peer VPN gateway:
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
            --peer-name=PEER_NAME_0_ipv6 \
            --peer-asn=PEER_ASN \
            --interface=ROUTER_INTERFACE_NAME_0_ipv6 \
            --peer-ip-address=PEER_BGP_IPV6_0 \
            --region=REGION
         

In most cases the PEER_ASN is the same, but it can be different depending on your on-premises network topology.




**For the second VPN tunnel**

  1. Add an interface with an IPv4 address to the Cloud Router; replace `ROUTER_INTERFACE_NAME_1_ipv4` with a name for the interface:
         
         gcloud compute routers add-interface ROUTER_NAME \
          --interface-name=ROUTER_INTERFACE_NAME_1_ipv4 \
          --vpn-tunnel=TUNNEL_NAME_1 \
          --ip-address=GOOGLE_BGP_IPV4_1 \
          --mask-length MASK_LENGTH \
          --region=REGION
         

  2. Add an interface with an IPv6 address to the same tunnel; replace `ROUTER_INTERFACE_NAME_1_ipv6` with a name for the interface:
         
         gcloud compute routers add-interface ROUTER_NAME \
          --interface-name=ROUTER_INTERFACE_NAME_1_ipv6 \
          --vpn-tunnel=TUNNEL_NAME_1 \
          --ip-address=GOOGLE_BGP_IPV6_1 \
          --mask-length=MASK_LENGTH \
          --region=REGION \
         

Replace `MASK_LENGTH` with a value of `64` or lower.

  3. Add a BGP peer configuration to the first interface for the **second tunnel** ; replace `PEER_NAME_1_ipv4` with a name for the peer, and replace `PEER_ASN` with the ASN configured for the peer VPN gateway:
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
          --peer-name=PEER_NAME_1_ipv4 \
          --peer-asn=PEER_ASN \
          --interface=ROUTER_INTERFACE_NAME_1_ipv4 \
          --peer-ip-address=PEER_BGP_IPV4_1 \
          --region=REGION
         

  4. Add a BGP peer configuration to the second interface for the **second tunnel** ; replace `PEER_NAME_1_ipv6` with a name for the peer VPN interface, and replace `PEER_ASN` with the ASN configured for the peer VPN gateway:
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
            --peer-name=PEER_NAME_1_ipv6 \
            --peer-asn=PEER_ASN \
            --interface=ROUTER_INTERFACE_NAME_1_ipv6 \
            --peer-ip-address=PEER_BGP_IPV6_1 \
            --region=REGION
         

In most cases the PEER_ASN is the same, but it can be different depending on your on-premises network topology.




###  API 

To create BGP sessions, follow these steps:

  1. To create two Cloud Router interfaces, make either a `PATCH` or `UPDATE` request by using the [`routers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/patch) or the [`routers.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/update). `PATCH` updates only the parameters that you include. `UPDATE` updates all parameters for Cloud Router.

Create two Cloud Router interfaces for the first VPN tunnel on the HA VPN gateway. You create interface with an IPv4 address and an interface with an IPv6 address. You can configure both interfaces and their BGP peers in the same `PATCH` or `UPDATE` request. The interfaces are associated with the same `linkedVpnTunnel`tunnel, and the BGP peers are then associated with the interfaces.

The BGP address ranges for each interface must be unique among all Cloud Routers in all regions of a VPC network.

Repeat this step and command for each VPN tunnel on the HA VPN gateway.

The following example adds one interface with an IPv4 address and one interface with an IPv6 address to the same `linkedVpnTunnel`. The example command manually specifies the IPv4 and IPv6 BGP addresses:
         
         PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
         {
           "interfaces": [
             {
               "name": "if-tunnel-a-to-on-prem-if-0_ipv4",
               "linkedVpnTunnel": "ha-vpn-gw-a-tunnel-0",
               "ipRange": "169.254.0.1/30"
               },
               {
               "name": "if-tunnel-a-to-on-prem-if-0_ipv6",
               "linkedVpnTunnel": "ha-vpn-gw-a-tunnel-0",
               "ipRange": "fdff:1::/126"
               }
         
             ]
         }
         

The following example adds an IPv4 BGP interface and an IPv6 BGP interface to the same `linkedVpnTunnel` with automatically assigned IPv4 and IPv6 BGP addresses:
         
         PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
         {
           "interfaces": [
             {
               "name": "if-tunnel-a-to-on-prem-if-0_ipv4",
               "linkedVpnTunnel": "ha-vpn-gw-a-tunnel-0",
               "ipVersion": "IPV4"
               },
               {
               "name": "if-tunnel-a-to-on-prem-if-0_ipv6",
               "linkedVpnTunnel": "ha-vpn-gw-a-tunnel-0",
               "ipVersion": "IPV6"
               }
         
             ]
         }
         

     1. To add the BGP peers to the Cloud Router for each VPN tunnel, make either a `PATCH` or `UPDATE` request by using the [`routers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/patch) or the [`routers.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/update). Repeat this command for the other VPN tunnels, changing all options as needed.

For example:
            
            PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
            {
            "bgpPeers": [
            {
              "interfaceName": "if-tunnel-a-to-on-prem-if-0_ipv4",
              "ipAddress": "169.254.0.1",
              "name": "bgp-peer-tunnel-a-to-on-prem-if-0_ipv4",
              "peerAsn": 65002,
              "peerIpAddress": "169.254.0.2",
              "advertiseMode": "DEFAULT"
              },
              {
              "interfaceName": "if-tunnel-a-to-on-prem-if-0_ipv6",
              "ipAddress": fdff:1::1",
              "name": "bgp-peer-tunnel-a-to-on-prem-if-0_ipv6",
              "peerAsn": 65002,
              "peerIpAddress": "fdff:1::2",
              "advertiseMode": "DEFAULT"
              }
            ]
            }
            




### Verify the configuration

###  Console 

To verify the configuration, go to the **Summary and reminder** page:

  1. The **Summary** section of this page lists information for the HA VPN gateway and the peer VPN gateway profile. For each VPN tunnel, you can view the [**VPN tunnel status**](https://docs.cloud.google.com/network-connectivity/docs/vpn/support/troubleshooting#troubleshooting-reference), the **BGP session name** , the [**BGP session status**](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bgp-states), and the MED value (advertised route priority).
  2. The **Reminder** section of this page lists the steps that you must complete to have a fully operational VPN connection between Cloud VPN and your peer VPN.
  3. If you want to download a configuration template for your peer VPN device, click **Download configuration**. For instructions on how to select your template and to view a list of supported vendors, see [Download a peer VPN configuration template](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/download-config). You can also download the configuration template later by going to the **Peer VPN gateways** page.
  4. After reviewing the information on this page, click **OK**.



###  gcloud 

To verify the Cloud Router configuration, follow these steps:

  * List the BGP session IP addresses chosen by Cloud Router. If you added a new interface to an existing Cloud Router, the BGP IPv4 or IPv6 addresses for the new interface might be listed with the highest index number. Use the BGP IPv4 or BGP IPv6 address `peerIpAddress` to configure your peer VPN gateway:
        
        gcloud compute routers get-status ROUTER_NAME \
             --region=REGION \
             --format='flattened(result.bgpPeerStatus[].name,
             result.bgpPeerStatus[].ipAddress, result.bgpPeerStatus[].peerIpAddress)'
        

The expected output for a Cloud Router managing two Cloud VPN tunnels (index `0` and index `1`) looks like the following example where the following is true:

    * `GOOGLE_BGP_IP_0` represents the BGP IP address of the Cloud Router's interface for the tunnel on Cloud VPN gateway `interface 0`; `PEER_BGP_IP_0` represents the BGP IP address of its peer.
    * `GOOGLE_BGP_IP_1` represents the BGP IP address of the Cloud Router's interface for the tunnel on Cloud VPN gateway `interface 1`; `PEER_BGP_IP_1` represents the BGP IP address of its peer.
    
    result.bgpPeerStatus[0].ipAddress:      169.254.0.1 GOOGLE_BGP_IP_0
      result.bgpPeerStatus[0].name:           bgp-peer-tunnel-a-to-on-prem-if-0
      result.bgpPeerStatus[0].peerIpAddress:  169.254.0.2 PEER_BGP_IP_0
      result.bgpPeerStatus[1].ipAddress:      169.254.1.1 GOOGLE_BGP_IP_1
      result.bgpPeerStatus[1].name:           bgp-peer-tunnel-a-to-on-prem-if-1
      result.bgpPeerStatus[1].peerIpAddress:  169.254.1.2 PEER_BGP_IP_1
    

  * You can also use the following command to get a full listing of the Cloud Router configuration:
        
        gcloud compute routers describe ROUTER_NAME \
             --region=REGION
        

The full listing looks like the following example:
        
        bgp:
          advertiseMode: DEFAULT
          asn: 65001
        bgpPeers:
        - interfaceName: if-tunnel-a-to-on-prem-if-0
          ipAddress: 169.254.0.1
          name: bgp-peer-tunnel-a-to-on-prem-if-0
          peerAsn: 65002
          peerIpAddress: 169.254.0.2
        - interfaceName: if-tunnel-a-to-on-prem-if-1
          ipAddress: 169.254.1.1
          name: bgp-peer-tunnel-a-to-on-prem-if-1
          peerAsn: 65004
          peerIpAddress: 169.254.1.2
        creationTimestamp: '2018-10-18T11:58:41.704-07:00'
        id: '4726715617198303502'
        interfaces:
        - ipRange: 169.254.0.1/30
          linkedVpnTunnel: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/vpnTunnels/tunnel-a-to-on-prem-if-0
          name: if-tunnel-a-to-on-prem-if-0
        - ipRange: 169.254.1.1/30
          linkedVpnTunnel: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/vpnTunnels/tunnel-a-to-on-prem-if-1
          name: if-tunnel-a-to-on-prem-if-1
          kind: compute#router
          name: router-a
          network: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/network-a
          region: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1
          selfLink: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/routers/router-a
        




###  API 

To verify the Cloud Router configuration, make a `GET` request by using the [`routers.getRouterStatus` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/getRouterStatus) , and use an empty request body:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers
    

### Create an additional tunnel on a single-tunnel gateway

###  Console 

To receive a 99.99% uptime SLA, configure a tunnel on each HA VPN interface of an HA VPN gateway.

Configure a second tunnel in the following circumstances:

  * If you configured an HA VPN gateway to a peer VPN gateway that has a single peer VPN interface.
  * If you previously set up a single tunnel on an HA VPN gateway to a peer VPN gateway that contains any number of interfaces, but now want a 99.99% uptime SLA for your HA VPN gateway.



To configure a second tunnel, follow the steps at [Add a tunnel from an HA VPN gateway to a peer VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/adding-a-tunnel#add-tunnel-from-ha-vpn-to-peer).

## Set the base advertised route priority (optional)

The BGP sessions that you create let each Cloud Router advertise routes to peer networks. The advertisements use _unmodified base priorities_.

Use the configuration documented in Creating an HA VPN gateway and tunnel pair to a peer VPN for _active-active routing configurations_ where the advertised route priorities of the two VPN tunnels from the Google Cloud side and the peer side match. To configure the same advertised route priorities from Google Cloud to both BGP peers, omit the advertised route priority on the Google Cloud side.

To create an _active-passive configuration_ , configure unequal advertised route priorities for the two HA VPN tunnels. One advertised route priority must be higher than the other. For example:

  * BGP session1/tunnel1, route priority = `10`
  * BGP session2/tunnel2, route priority = `20`



For more information about the base advertised route priority, see [Advertised prefixes and priorities](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#advertised-priority).

You can also specify which routes are advertised by using [custom advertisements](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#am-custom):

  * Add the `--advertisement-mode=CUSTOM` flag (`gcloud`) or the `advertiseMode: custom` flag (API).
  * Specify IP address ranges with the `--set-advertisement-ranges` flag (`gcloud`) or the `advertisedIpRanges` flag (API).



## Complete the configuration

Before you can use a new Cloud VPN gateway and its associated VPN tunnels, complete the following steps:

  1. Set up the peer VPN gateway and configure the corresponding tunnel or tunnels there. For instructions, see the following: 
     * For specific configuration guidance for certain peer VPN devices, see [Use third-party VPNs](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/interop-guides).
     * For supported peer topologies, see [Cloud VPN topologies](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/topologies).
     * For general configuration parameters, see [Configure the peer VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/configuring-peer-gateway).
  2. [Configure firewall rules](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/configuring-firewall-rules) in Google Cloud and your peer network as required.
  3. [Check the status of your VPN tunnels](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/checking-vpn-status). This step includes checking the high-availability configuration of your HA VPN gateway.



## What's next

  * To control which IP addresses are allowed for peer VPN gateways, see [Restrict IP addresses for peer VPN gateways](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/restrict-peer-ip-addresses).
  * To use high-availability and high-throughput scenarios or multiple subnet scenarios, see [Advanced configurations](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/advanced).
  * To help you solve common issues that you might encounter when using Cloud VPN, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/vpn/support/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
