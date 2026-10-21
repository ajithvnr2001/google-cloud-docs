---
url: https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn2/
title: Create HA VPN gateways to connect VPC networks \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:42:49.271334+00:00
---

# Create HA VPN gateways to connect VPC networks  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud VPN ](https://docs.cloud.google.com/network-connectivity/docs/vpn)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)



Send feedback 

#  Create HA VPN gateways to connect VPC networks Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to connect two Virtual Private Cloud (VPC) networks in Google Cloud by using two HA VPN gateways. You can connect two VPC networks together as long as the primary and secondary subnet IPv4 or IPv6 address ranges in each network don't overlap.

For more information about Cloud VPN, see the following resources:

  * For diagrams of this topology, see [HA VPN between Google Cloud networks](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/topologies#2-gcp-gateways).

  * To automate this setup, see the [Terraform example for an HA VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/automate-vpn-setup-with-terraform#between-vpcs).

  * For best practices to consider before setting up Cloud VPN, see [Best practices](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/best-practices).

  * For more information about Cloud VPN, see the [Cloud VPN overview](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview).

  * For definitions of terms used on this page, see [Key terms](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/key-terms).




## Requirements

To receive a 99.99% SLA, make sure that you meet the following requirements when creating this configuration:

  * Place one HA VPN gateway in each [VPC network](https://docs.cloud.google.com/vpc/docs/vpc).
  * Place both HA VPN gateways in the same [Google Cloud region](https://docs.cloud.google.com/docs/geography-and-regions).
  * Configure a tunnel on each interface of each gateway.
  * Match the gateway interfaces as follows: 
    * The tunnel on `interface 0` of the first gateway must connect to `interface 0` on the second gateway.
    * The tunnel on `interface 1` of the first gateway must connect to `interface 1` on the second gateway.



Although it is possible to connect two VPC networks together by using a single tunnel between HA VPN gateways or by using Classic VPN gateways, this type of configuration is not considered to have high availability and does not meet the HA SLA of 99.99% availability.

**Caution:** If one or both of the VPN gateways are Classic VPN gateways, your configuration does not meet the 99.99% SLA.

## Cloud Router recommendations

When configuring a new HA VPN gateway, you can create a new Cloud Router, or you can use an existing Cloud Router with existing Cloud VPN tunnels or VLAN attachments. However, the Cloud Router that you use must not already manage a BGP session for a VLAN attachment associated with a Partner Interconnect connection because of the attachment's [specific ASN requirements](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/creating-vlan-attachments#encrypted-attachments).

### Manage permissions

HA VPN gateways might not always belong to you or your Google Cloud organization. When you create an HA VPN gateway or connect to a gateway owned by someone else, consider these requirements:

  * If you own the project where you create an HA VPN gateway, configure the recommended permissions on it.
  * If you want to connect to an HA VPN gateway that resides in a Google Cloud organization or project that you don't own, request the `compute.vpnGateways.use` permission from the owner.



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
             




### Create custom VPC networks and subnets

The procedures in this document use two different VPC networks. Each VPC network has at least two subnets, which are located in different regions.

Before you create your HA VPN gateways and your HA VPN tunnels, create two VPC networks.

Each VPC network must have at least one subnet in the region where you create the HA VPN gateway.

  * To create a custom mode VPC network (recommended), see [Create a custom mode VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#create-custom-network).
  * To create a subnet, see [Working with subnets](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#subnet-rules).



To enable IPv6 traffic in your HA VPN tunnels, you must enable the allocation of IPv6 internal addresses when you create the VPC networks. In addition, configure the subnets to use IPv6 internal addresses.

You must also configure IPv6 on the VMs in the subnet.

  * To create a custom mode VPC network that has at least one dual-stack subnet or one IPv6-only subnet with internal IPv6 addresses, see [Create and manage VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks).
  * To create a dual-stack subnet with IPv6 enabled, see [Add a dual-stack subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#add-subnet-ipv6).
  * To create an IPv6-only subnet, see [Add an IPv6-only subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#add-subnet-ipv6-only).
  * To enable IPv6 in an existing IPv4-only subnet, see [Change an IPv4-only subnet to dual-stack](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#subnet-enable-ipv6).
  * To create VMs with IPv6 enabled, see [Configuring IPv6 for instances and instance templates](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address).



The VPC subnets must be configured to use internal IPv6 addresses. When you use the gcloud CLI, you configure the subnets with the `--ipv6-access-type=INTERNAL` flag. Cloud Router does not dynamically advertise routes for subnets that are configured to use external IPv6 addresses (`--ipv6-access-type=EXTERNAL`).

For information about using internal IPv6 address ranges in your VPC networks and subnets, see [Internal IPv6 specifications](https://docs.cloud.google.com/vpc/docs/subnets#internal-ipv6).

The examples in this document also use [VPC global dynamic routing mode](https://docs.cloud.google.com/vpc/docs/vpc#routing_for_hybrid_networks), which behaves in the following way:

  * All instances of Cloud Router apply the `to on-premises` routes that they learn to all subnets of the VPC network.
  * Routes to all subnets in the VPC network are shared with on-premises routers.



## Create two fully configured HA VPN gateways that connect to each other

**Note:** It can help to have two Google Cloud console or terminal sessions open when configuring two HA VPN gateways that connect to each other.

Follow the instructions in this section to create an HA VPN gateway, a peer VPN gateway resource, tunnels, and BGP sessions.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `compute.vpnGateways.get`
  * `compute.vpnGateways.list`
  * `compute.externalVpnGateways.get`
  * `compute.externalVpnGateways.list`
  * `compute.vpnGateways.create`
  * `compute.vpnGateways.delete`
  * `compute.vpnGateways.get`
  * `compute.vpnGateways.list`
  * `compute.vpnGateways.use`
  * `compute.vpnGateways.setLabels`
  * `compute.externalVpnGateways.create`
  * `compute.externalVpnGateways.delete`
  * `compute.externalVpnGateways.get`
  * `compute.externalVpnGateways.list`
  * `compute.externalVpnGateways.use`
  * `compute.externalVpnGateways.setLabels`



**Roles**

  * `roles/compute.networkAdmin`



### Create the HA VPN gateways

**Note:** After you create an HA VPN gateway, you cannot modify its stack type. If you need a different stack type for an existing HA VPN gateway, you must delete and recreate the gateway. 

To support IPv6 traffic, HA VPN gateways must use either the `IPv4 and IPv6 (dual-stack)` or `IPv6 (single-stack)` configuration. To temporarily disable IPv6 traffic without deleting your gateway, [ disable IPv6 route exchange in the IPv4 BGP session](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-mp-bgp#disable-ipv6-bgp) or [ disable the IPv6 session](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/disabling-removing-bgp#disable_a_bgp_session) that you established for the HA VPN tunnels. 

###  Console 

The **VPN setup wizard** includes all required configuration steps for creating an HA VPN gateway, a peer VPN gateway resource, tunnels, and BGP sessions.

To create the first HA VPN gateway, follow these steps:

  1. In the Google Cloud console, go to the **VPN** page.

[Go to VPN](https://console.cloud.google.com/hybrid/vpn/list)

  2. If you are creating a gateway for the first time, click **Create VPN connection**.

  3. Select the **VPN setup wizard**.

  4. If you have an existing HA VPN gateway, select the option button for that gateway.

  5. Click **Continue**.

  6. Specify a **VPN gateway name**.

  7. Under **VPC network** , select an existing network or the default network.

  8. Select a **Region**.

  9. Select a stack type for the gateway, either **IPv4 (single stack)** or **IPv4 and IPv6 (dual stack)**.

  10. Click **Create and continue**.

  11. The console page refreshes and displays your gateway information. Two external IPv4 addresses are automatically allocated for each of your gateway interfaces. For future configuration steps, make note of the details of your gateway configuration.




To create the second HA VPN gateway, repeat the preceding steps in a new browser tab. Make sure you specify the same HA VPN tunnel stack type as the first HA VPN gateway.

###  gcloud 

Depending on the workloads you plan to support with your tunnels, you can choose the stack type as follows while creating the gateways:

  * To support only IPv4 workloads, create an HA VPN gateway with the `IPV4_ONLY` stack type.
  * To support both IPv4 and IPv6 workloads, create an HA VPN gateway with the `IPV4_IPV6` stack type.
  * To support only IPv6 workloads, create an HA VPN gateway with the `IPV6_ONLY` stack type.



To create two HA VPN gateways, complete the following command sequence:

  * Create an HA VPN gateway in each network in `REGION`.

When each gateway is created, two external IPv4 addresses are automatically allocated, one for each gateway interface. Take note of these IP addresses to use later on in the configuration steps.

In the following commands, replace the following:

    * `GW_NAME_1` and `GW_NAME_2`: the name of each gateway
    * `NETWORK`: the name of your Google Cloud network
    * `REGION`: the [Google Cloud region](https://docs.cloud.google.com/compute/docs/regions-zones) where you need to create the gateway and tunnel
    * `IP_STACK`: Optional: the IP stack to use. Specify `IPV4_ONLY`, `IPV4_IPV6`, or `IPV6_ONLY`. If you don't specify this flag, the stack type defaults to `IPV4_IPV6`.

**Create the first gateway**

For a gateway with IPv4 interfaces:
    
    gcloud compute vpn-gateways create GW_NAME_1 \
       --network=NETWORK_1 \
       --region=REGION \
       --stack-type=IP_STACK
    

The gateway that you create is similar to the following example output. An external IPv4 address has been automatically assigned to each gateway interface:
    
    Created [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/vpnGateways/ha-vpn-gw-a].
    NAME          INTERFACE0     INTERFACE1     NETWORK     REGION
    ha-vpn-gw-a   203.0.113.16   203.0.113.23   network-a   us-central1
    

**Create the second gateway**
    
    gcloud compute vpn-gateways create GW_NAME_2 \
       --network=NETWORK_2 \
       --region=REGION \
       --stack-type=IP_STACK
    

If you specified a stack type for the first gateway, use the same stack type for the second gateway.

The gateway that you create is similar to the following example output:
    
    Created [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-east1/vpnGateways/ha-vpn-gw-b].
    NAME          INTERFACE0     INTERFACE1     NETWORK     REGION
    ha-vpn-gw-b   203.0.114.18   203.0.114.25   network-b   us-east1
    

For a gateway with IPv6 interfaces:
    
    gcloud compute vpn-gateways create GW_NAME_1 \
       --network=NETWORK_1 \
       --region=REGION \
       --gateway-ip-version=IPV6 \
       --stack-type=IP_STACK
    

An external IPv6 address is automatically assigned to each gateway interface.




###  API 

To create BGP sessions, follow these steps:

To create the full configuration for an HA VPN gateway, use the API commands in the following sections. All field values used in these sections are example values.

For a gateway with IPv4 interfaces:

  1. Create the first HA VPN gateway by making a `POST` request to the [`vpnGateways.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/vpnGateways/insert) method.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/vpnGateways
         {
          "name": "ha-vpn-gw-a",
          "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/network-a",
          "stackType": "IPV4_IPV6"
         }
         

The `stackType` field is optional. The only valid values are `IPV4_IPV6` or `IPV4_ONLY`. If you don't specify a `stackType`, the default is `IPV4_ONLY`.

  2. Repeat the command to create the second HA VPN gateway, and specify the appropriate `project`, `name`, `network`, and `region`.

If you specified `stackType` for the first gateway, use the same stack type for the second gateway, either `IPV4_ONLY` or `IPV4_IPV6`.




For a gateway with IPv6 interfaces:

  1. Create the first HA VPN gateway by making a `POST` request to the [`vpnGateways.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/vpnGateways/insert).
         
         POST https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/regions/REGION/vpnGateways
         {
          "name": "ha-vpn-gw-a",
          "network": "https://www.googleapis.com/compute/beta/projects/PROJECT_ID/global/networks/network-a",
          "gatewayIpVersion": "IPV6",
          "stackType": "IPV6_ONLY"
         }
         

When you allocate external IPv6 addresses to the HA VPN gateway, you must specify `IPV6` as the `gatewayIpVersion` value. The `stackType` field is optional.

     * If you don't specify `stackType`, the default value is `IPV4_IPV6`.

     * The only valid `stackType` values for a gateway with a `gatewayIpVersion` of `IPV6` are `IPV4_IPV6` or `IPV6_ONLY`.

  2. Repeat the command to create the second HA VPN gateway, and specify the appropriate `project`, `name`, `network`, and `region`.

When you allocate external IPv6 addresses to the HA VPN gateway, you must specify `IPV6` as the `gatewayIpVersion` value. The `stackType` field is optional.

If you specified `stackType` for the first gateway, use the same stack type for the second gateway, either `IPV6_ONLY` or `IPV4_IPV6`.




### Specify the peer VPN gateway resource

In this setup, the peer VPN gateway resource is the second HA VPN, which is the endpoint of the new VPN tunnel connections.

If you are connecting two VPC networks, the second VPC network can exist in the same Google Cloud project or in a separate Google Cloud project.

###  Console 

To specify the peer HA VPN gateway resource, follow these steps:

  1. On the **Create a VPN** page, in the **Peer VPN gateway** section, select **Google Cloud VPN gateway**.
  2. For **Project** , select the Google Cloud project that contains the second HA VPN gateway you created in [Create the HA VPN gateways](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn2#create-ha-gateways).
  3. For **VPN gateway name** , select the name of the second HA VPN.
  4. Continue to create VPN tunnels.



###  gcloud 

You created the peer VPN gateway resource when you created the second HA VPN gateway in Create the HA VPN gateways.

You specify this HA VPN gateway as the peer VPN gateway resource when you create the HA VPN tunnels.

###  API 

You created the peer VPN gateway resource when you created the second HA VPN gateway in Create the HA VPN gateways.

You specify this HA VPN gateway as the peer VPN gateway resource when you create the HA VPN tunnels.

### Create Cloud Routers

###  Console 

Under **Cloud Router** , if you haven't already, create a Cloud Router specifying the following options. You can use an existing Cloud Router if the router does not already manage a BGP session for a VLAN attachment associated with a Partner Interconnect connection.

  1. To create a new Cloud Router, specify the following:

     * A **Name**
     * An optional **Description**
     * A **Google ASN** for the new router

You can use any private ASN (`64512` through `65534`, `4200000000` through `4294967294`) that you are not using elsewhere in your network. The Google ASN is used for all BGP sessions on the same Cloud Router, and you cannot change the ASN later.

  2. To create the new router, click **Create**.




###  gcloud 

The following instructions assume that you haven't already created Cloud Routers to use for managing BGP sessions for your HA VPN tunnels. You can use an existing Cloud Router in each VPC network unless those routers already manage a BGP session for a VLAN attachment associated with a Partner Interconnect connection.

To create two Cloud Routers, complete the following command sequence:

  * Create a Cloud Router in each network in `REGION`.

In the following commands, replace the following:

    * `PEER_ASN_1` and `PEER_ASN_2`: any private ASN (`64512` through `65534`, `4200000000` through `4294967294`) that you are not already using. This example uses ASN `65001` for both interfaces of `ROUTER_NAME_1` and ASN `65002` for both interfaces of `ROUTER_NAME_2`.
    * Replace all other options with the values that you used previously.

**Create the first router**
    
    gcloud compute routers create ROUTER_NAME_1 \
       --region=REGION \
       --network=NETWORK_1 \
       --asn=PEER_ASN_1
    

The router that you create is similar to the following example output:
    
    Created [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/routers/router-a].
    NAME       REGION        NETWORK
    router-a   us-central1   network-a
    

**Create the second router**
    
    gcloud compute routers create ROUTER_NAME_2 \
       --region=REGION \
       --network=NETWORK_2 \
       --asn=PEER_ASN_2
    

The router that you create is similar to the following example output:
    
    Created [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/routers/router-b].
    NAME       REGION        NETWORK
    router-b   us-central1   network-b
    




###  API 

If you already created a Cloud Router in each of the VPC networks where each of your HA VPN gateways reside, you can use those Cloud Routers instead of creating new ones. However, if a Cloud Router manages a BGP session for a VLAN attachment associated with a Partner Interconnect connection, then create a new Cloud Router.

To create a Cloud Router, make a `POST` request to the [`routers.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/insert) method.
    
    
     POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers
       {
         "name": "router-a",
         "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/network-a"
       }
    

### Create VPN tunnels

**Important:** To create a VPN configuration that meets the requirements for 99.99% availability, configure tunnels as described throughout this section. The VPN tunnels that you create are not available until the corresponding partner tunnels have been created on the other HA VPN gateway.

###  Console 

To create VPN tunnels, follow these steps:

  1. Under **High availability** , select either a pair of tunnels or one tunnel to the other HA VPN gateway:

     * If you select **Create a pair of VPN tunnels** (recommended), configure the two tunnel dialogs that appear at the bottom of the **Create VPN** page.

     * If you select **Create a single VPN tunnel** , you configure your single tunnel on the rest of the **Create VPN** page. However, to get a 99.99% SLA to the other HA VPN gateway, you must create a second tunnel. You can add a second tunnel later as described at the end of this procedure.

**Caution:** If you configure only a single tunnel, you don't receive a 99.99% SLA for this configuration.
  2. Complete the following steps either on the same page or in each tunnel's dialog at the bottom of the page.

  3. If you are configuring one tunnel, under **Associated Cloud VPN gateway interface** , select the HA VPN interface and IP address combination for this gateway to associate it with the gateway interface on the other HA VPN gateway. For two-tunnel configurations, this option and the **Associated peer VPN gateway interface** option are both unavailable because the correct interface combinations are configured for you.

     1. Specify a **Name** for the tunnel.
     2. Specify an optional **Description**.
     3. Specify the **IKE version**. We recommend IKEv2, the default setting. To allow IPv6 traffic, you must select IKEv2.
     4. Specify an **IKE pre-shared key** by using your pre-shared key (shared secret), which must correspond with the pre-shared key for the partner tunnel that you create on your peer gateway. If you haven't configured a pre-shared key on your peer VPN gateway and want to generate one, click **Generate and copy**. Make sure that you record the pre-shared key in a secure location because it cannot be retrieved after you create your VPN tunnels.
     5. Click **Done**.
     6. On the **Create VPN** page, repeat the tunnel creation steps for any remaining tunnel dialogs.
  4. When you have configured all tunnels, click **Create and continue**.




###  gcloud 

To create two VPN tunnels on each HA VPN gateway, complete the following command sequence.

  * The tunnel that you create from `interface 0` of `GW_NAME_1` must connect to the external IP address associated with `interface 0` of `GW_NAME_2` in `NETWORK_2`.
  * The tunnel from `interface 1` of `GW_NAME_1` must connect to the external IP address associated with `interface 1` of `GW_NAME_2`.
  * When you create VPN tunnels on `GW_NAME_1` in `NETWORK_1`, specify the information for `GW_NAME_2` in `NETWORK_2`. Google automatically connects the tunnel from `interface 0` of `GW_NAME_1` to `interface 0` of `GW_NAME_2`, and `interface 1` of `GW_NAME_1` to `interface 1` of `GW_NAME_2`.
  * You also have the option to configure cipher algorithms when creating Cloud VPN tunnels. For more information, see [Create Cloud VPN tunnels](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn#create_vpn_tunnels).

**Create two tunnels on` GW_NAME_1`**

    * Create two VPN tunnels, one on each interface, of `GW_NAME_1` in `NETWORK_1`.

In the following commands, replace the following:

      * `TUNNEL_NAME_GW1_IF0` and `TUNNEL_NAME_GW1_IF1`: a name for each tunnel originating from `GW_NAME_1`; naming the tunnels by including the gateway interface name can help identify the tunnels later
      * `GW_NAME_2`: the value of `--peer-gcp-gateway`
      * `REGION`: the region where `GW_NAME_1` is located
      * Optional: The `--vpn-gateway-region` is the region of the HA VPN gateway to operate on. Its value should be the same as `--region`. If not specified, this option is automatically set. This option overrides the default region property value for this command invocation.
      * `IKE_VERS`: `2` for IKEv2; because both tunnels connect to another HA VPN gateway, Google recommends using IKEv2. To allow IPv6 traffic, you must use IKEv2.
      * `SHARED_SECRET`: your pre-shared key (shared secret), which must be the same pre-shared key that you use for the corresponding tunnel created from `GW_NAME_2` on `interface 0` and `interface 1`; for recommendations, see [Generate a strong pre-shared key](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/generating-pre-shared-key)
      * `INT_NUM_0`: the number `0` for the first interface on `GW_NAME_1`
      * `INT_NUM_1`: the number `1` for the second interface on `GW_NAME_1`
      * If the `peer-gcp-gateway` is in a different project from the VPN tunnel and local VPN gateway, to specify the project, use the `--peer-gcp-gateway` option as a full URI or as a relative name. The following sample option is a relative name: 
            
            --peer-gcp-gateway projects/other-project/regions/us-central1/vpnGateways/ha-vpn-gw-b
            

**Create the first tunnel on` GW_NAME_1` `INT_NUM_0`**
    
    gcloud compute vpn-tunnels create TUNNEL_NAME_GW1_IF0 \
        --peer-gcp-gateway=GW_NAME_2 \
        --region=REGION \
        --ike-version=IKE_VERS \
        --shared-secret=SHARED_SECRET \
        --router=ROUTER_NAME_1 \
        --vpn-gateway=GW_NAME_1 \
        --interface=INT_NUM_0
    

**Create the second tunnel on` GW_NAME_1` `INT_NUM_1`**
    
    gcloud compute vpn-tunnels create TUNNEL_NAME_GW1_IF1 \
        --peer-gcp-gateway=GW_NAME_2 \
        --region=REGION \
        --ike-version=IKE_VERS \
        --shared-secret=SHARED_SECRET \
        --router=ROUTER_NAME_1 \
        --vpn-gateway=GW_NAME_1 \
        --interface=INT_NUM_1
    

The command output looks similar to the following example:
    
    Created [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/vpnTunnels/tunnel-a-to-b-if-0].
    NAME                 REGION        VPN_GATEWAY   VPN_INTERFACE  PEER_ADDRESS
    tunnel-a-to-b-if-0   us-central1   ha-vpn-gw-a   0          ha-vpn-gw-b
    
    Created [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/vpnTunnels/tunnel-a-to-b-if-1].
    NAME                 REGION        VPN_GATEWAY   VPN_INTERFACE  PEER_ADDRESS
    tunnel-a-to-b-if-1   us-central1   ha-vpn-gw-a   1          ha-vpn-gw-b
    

**Create two tunnels on` GW_NAME_2`**

    * Create two VPN tunnels, one on each interface, of `GW_NAME_2` in `NETWORK_2`.

      * The tunnel that you create from `interface 0` of `GW_NAME_2` must connect to the external IP address associated with `interface 0` of `GW_NAME_1` in `NETWORK_1`.
      * The tunnel from `interface 1` of `GW_NAME_2` must connect to the external IP address associated with `interface 1` of `GW_NAME_1`.

In the following commands, replace the following:

      * `REGION`: the region where `GW_NAME_2` is located
      * Optional: The `--vpn-gateway-region` is the region of the VPN gateway to operate on. Its value should be the same as `--region`. If not specified, this option is automatically set. This option overrides the default region property value for this command invocation.
      * `TUNNEL_NAME_GW2_IF0` and `TUNNEL_NAME_GW2_IF1`: a name for each tunnel originating from `GW_NAME_2`; naming the tunnels by including the gateway interface name can help identify the tunnels later
      * `GW_NAME_1`: the value of `--peer-gcp-gateway`
      * `IKE_VERS`: `2` for IKEv2; because these tunnels connect to the two tunnels created in the previous step, they must use the same IKE version (Google recommends using IKEv2). To allow IPv6 traffic, you must use IKEv2.
      * `SHARED_SECRET`: your pre-shared key (shared secret), which must correspond with the pre-shared key for the partner tunnel that you created on each interface of `GW_NAME_1`; for recommendations, see [Generate a strong pre-shared key](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/generating-pre-shared-key)
      * `GW_NAME_2`: the name of the second gateway that you configured in the gateway configuration step
      * `INT_NUM_0`: the number `0` for the first interface on `GW_NAME_2`
      * `INT_NUM_1`: the number `1` for the second interface on `GW_NAME_2`
      * If the `peer-gcp-gateway` is in a different project than the VPN tunnel and local VPN gateway, to specify the project, use the `--peer-gcp-gateway` option as a full URI or as a relative name. The following sample option is a relative name: 
            
            --peer-gcp-gateway projects/other-project/regions/us-central1/vpnGateways/ha-vpn-gw-b
            

      * The `--peer-gcp-gateway-region`, which is the region of the peer-side HA VPN gateway to which the VPN tunnel is connected, must be in the same region as the VPN tunnel. If not specified, the region is automatically set.

**Create the first tunnel on` GW_NAME_2` `INT_NUM_0`**
    
    gcloud compute vpn-tunnels create TUNNEL_NAME_GW2_IF0 \
        --peer-gcp-gateway=GW_NAME_1 \
        --region=REGION \
        --ike-version=IKE_VERS \
        --shared-secret=SHARED_SECRET \
        --router=ROUTER_NAME_2 \
        --vpn-gateway=GW_NAME_2 \
        --interface=INT_NUM_0
    

**Create the second tunnel on` GW_NAME_2` `INT_NUM_1`**
    
    gcloud compute vpn-tunnels create TUNNEL_NAME_GW2_IF1 \
        --peer-gcp-gateway=GW_NAME_1 \
        --region=REGION \
        --ike-version=IKE_VERS \
        --shared-secret=SHARED_SECRET \
        --router=ROUTER_NAME_2 \
        --vpn-gateway=GW_NAME_2 \
        --interface=INT_NUM_1
    

The command output looks similar to the following example:
    
    Created [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/vpnTunnels/tunnel-b-to-a-if-0].
    NAME                 REGION       VPN_GATEWAY   VPN_INTERFACE  PEER_ADDRESS
    tunnel-b-to-a-if-0   us-central1  ha-vpn-gw-b   0          ha-vpn-gw-a
    
    Created [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/vpnTunnels/tunnel-b-to-a-if-1].
    NAME                 REGION       VPN_GATEWAY   VPN_INTERFACE  PEER_ADDRESS
    tunnel-b-to-a-if-1   us-central1  ha-vpn-gw-b   1          ha-vpn-gw-a
    

After this step, wait a few minutes, and then [check the status](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/checking-vpn-status) of each VPN tunnel.

A VPN tunnel's state changes to `Established` only when the corresponding partner tunnel is also available and properly configured. A valid IKE and Child Security Association (SA) must also be negotiated between them.

For example, `tunnel-a-to-b-if-0` on `ha-vpn-gw-a` can only be established if `tunnel-b-to-a-if-0` on `ha-vpn-gw-b` is configured and available.




###  API 

To create two VPN tunnels, one for each interface on an HA VPN gateway, make a `POST` request to the [`vpnTunnels.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/vpnTunnels/insert) method.

**Important:** To get a 99.99% uptime SLA, you must create a tunnel on each interface of your HA VPN gateway.

  1. To create the first tunnel, run the following command:
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/vpnTunnels
         {
          "name": "ha-vpn-gw-a-tunnel-0",
          "ikeVersion": 2,
          "peerGcpGateway": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/vpnGateways/ha-vpn-gw-b",
          "router": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/router-a",
          "sharedSecret": "SECRET_1",
          "vpnGateway": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/vpnGateways/ha-vpn-gw-a",
          "vpnGatewayInterface": 0
         }
         

If you plan to enable IPv6 in the BGP session associated with this tunnel, you must specify `2` for the `ikeVersion`.

  2. To create the second tunnel, repeat the preceding command, but change the following parameters:

     * `name`: for example, `ha-vpn-gw-a-tunnel-1`
     * `sharedSecret` or `sharedSecretHash` (if needed)
     * `vpnGatewayInterface`: change to the value of the other HA VPN gateway interface—in this example, change this value to `1`



Next, create two tunnels for your second HA VPN gateway that connect to your first HA VPN gateway.

  1. To create the first tunnel on the second HA VPN gateway, run the following command:
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/vpnTunnels
         {
          "name": "ha-vpn-gw-b-tunnel-0",
          "ikeVersion": 2,
          "peerGcpGateway": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/vpnGateways/ha-vpn-gw-a",
          "router": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/router-b",
          "sharedSecret": SECRET_1,
          "vpnGateway": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/vpnGateways/ha-vpn-gw-b",
          "vpnGatewayInterface": 0
         }
         

Use the same `sharedSecret` that you specified for the first tunnel on the first gateway (`ha-vpn-gw-a-tunnel-0`).

If you plan to enable IPv6 in the BGP session associated with this tunnel, you must specify `2` for the `ikeVersion`.

  2. To create the second tunnel on the second HA VPN gateway, repeat the preceding command, but change the following parameters:



  * `name`: for example `ha-vpn-gw-b-tunnel-1`
  * `sharedSecret` or `sharedSecretHash`: specify the `sharedSecret` or `sharedSecretHash` that you used when creating the second tunnel on the first gateway
  * `vpnGatewayInterface`: change to the value of the other HA VPN gateway interface—in this example, change this value to `1`



### Create BGP sessions

For each HA VPN tunnel, you can create an IPv4 BGP session, an IPv6 BGP session, or both.

To view specific instructions, select the type of BGP session that is appropriate for your HA VPN gateway and VPC network traffic needs.

BGP session type | HA VPN gateway | VPC network | MP-BGP allowed?  
---|---|---|---  
IPv4 BGP sessions | IPv4 only or dual stack | IPv4 only or dual stack | yes  
IPv6 BGP sessions | dual stack | dual stack | yes  
Both IPv4 and IPv6 BGP sessions | dual stack | dual stack | no  
  
To use multiprotocol BGP (MP-BGP) in the BGP sessions of your HA VPN tunnels, you must use dual-stack HA VPN gateways.

You must also use a dual-stack HA VPN gateway to set up both IPv4 and IPv6 BGP sessions in the same HA VPN tunnel. However, you can't enable dual-stack route exchange (MP-BGP) in the individual IPv4 and IPv6 BGP sessions.

### IPv4 BGP sessions

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

In this section, you configure Cloud Router interfaces and BGP peers; the following table provides an overview of these interfaces and peers. It shows the relationship between the IPv4 address range and the peer IPv4 addresses that you specify for each interface.

For example, the first interface of `router-1` has an IPv4 address of `169.254.0.1`, which means `router-1` is the first host in IPv4 subnet `169.254.0.0/30`. The other Cloud Router, `router-2`, is the BGP peer of `router-1`. The first interface of `router-2` is assigned `169.254.0.2`, which is the second host in the IPv4 subnet `169.254.0.0/30`. Therefore, the peer IPv4 BGP address of `router-1` is `169.254.0.2` and the peer IPv4 BGP address of `router-2` is `169.254.0.1`.

This table also shows an example IPv6 next hop address configuration.

**Important:** The BGP IPv4 address range for each BGP session must be unique among all Cloud Routers in all regions of a VPC network.

Router | Interface name | IPv4 address range | Peer IPv4 address | Peer ASN | IPv6 next hop  
address | Peer IPv6 next hop  
address  
---|---|---|---|---|---|---  
router-1 | if-tunnel-a-to-b-if-0 | 169.254.0.1/30 | 169.254.0.2 | 65002 | 2600:2d00:0:2::1 | 2600:2d00:0:2::2  
router-2 | if-tunnel-b-to-a-if-0 | 169.254.0.2/30 | 169.254.0.1 | 65001 | 2600:2d00:0:2::2 | 2600:2d00:0:2::1  
router-1 | if-tunnel-a-to-b-if-1 | 169.254.1.1/30 | 169.254.1.2 | 65002 | 2600:2d00:0:2:1::1 | 2600:2d00:0:2:1::2  
router-2 | if-tunnel-b-to-a-if-1 | 169.254.1.2/30 | 169.254.1.1 | 65001 | 2600:2d00:0:2:1::2 | 2600:2d00:0:2:1::1  
  
To create Cloud Router interfaces and BGP peers, complete the following command sequence.

  1. **Create an interface and BGP peer on` ROUTER_NAME_1` for the tunnel `TUNNEL_NAME_GW1_IF0`**.

This interface connects `TUNNEL_NAME_GW1_IF0` on `interface 0` of `GW_1` to `interface 0` of `GW_2`.

In the following commands, replace the following:

     * `ROUTER_1_INTERFACE_NAME_0`: a name for the Cloud Router interface; using a name related to `TUNNEL_NAME_GW1_IF0` is helpful
     * `IP_VERSION`: specify `IPV4` or leave unspecified. If unspecified, the default is `IPV4`.
     * `IP_ADDRESS_1`: a BGP IPv4 address from the `169.254.0.0/16` IPv4 address range that's not already in use; this example uses `169.254.0.1`. If you omit this flag and don't manually assign a BGP IPv4 address, Google Cloud automatically assigns an address for you.
     * `MASK_LENGTH`: specify `30` because the Cloud Router must use a unique `/30` CIDR from the same `169.254.0.0/16` IPv4 address range.
     * `PEER_NAME_GW1_IF0`: a name describing the BGP peer; using a name related to `TUNNEL_NAME_GW1_IF0` is helpful
     * `PEER_IP_ADDRESS_1`: a BGP IPv4 address from the `169.254.0.0/16` that's not already in use; this example uses `169.254.0.2`. If you did not specifically assign a BGP IPv4 address, `IP_ADDRESS_1` previously, omit this option as well and Google Cloud automatically assigns a matching BGP peer IPv4 address for you. If you manually specified `IP_ADDRESS_1`, you must also manually configure this option.
     * `PEER_ASN_2`: the ASN number used for all interfaces on the other Cloud Router `ROUTER_NAME_2`; this example uses ASN number `65002`
     * Optional: If you are creating IPv4 BGP sessions with MP-BGP, specify `--enable-ipv6` when you run the `add-bgp-peer` command to enable IPv6 route exchange. You also have the option to configure IPv6 next hop addresses automatically or manually. To configure next hop addresses manually, replace both of the following:

       * `IPV6_NEXTHOP_ADDRESS_1`: the next hop address for IPv6 routes that are advertised by Cloud Router.
       * `PEER_IPV6_NEXTHOP_ADDRESS_1`: the next hop address for IPv6 routes learned by the Cloud Router from the BGP peer.

The next-hop address must be in the `2600:2d00:0:2::/63` IPv6 address range.

If you don't specify the IPv6 next hop addresses, then Google Cloud automatically assigns unused addresses from the `2600:2d00:0:2::/63` IPv6 address range.

     * `AUTHENTICATION_KEY`: the secret key to use for MD5 authentication on `PEER_NAME_GW1_IF0`; for more information about this optional feature, see [Use MD5 authentication](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication).

**Create a Cloud Router interface for` TUNNEL_NAME_GW1_IF0`**

To create an interface with an IPv4 address on Cloud Router, run the following command:
    
    gcloud compute routers add-interface ROUTER_NAME_1 \
        --interface-name=ROUTER_1_INTERFACE_NAME_0 \
        --ip-address=IP_ADDRESS_1 \
        --mask-length=MASK_LENGTH \
        --vpn-tunnel=TUNNEL_NAME_GW1_IF0 \
        --region=REGION
    

**Create a BGP peer for` TUNNEL_NAME_GW1_IF0`**

The following example command creates an IPv6-enabled BGP peer with manually specified IPv4 BGP addresses and IPv6 next hop addresses:
    
    gcloud compute routers add-bgp-peer ROUTER_NAME_1 \
        --peer-name=PEER_NAME_GW1_IF0 \
        --interface=ROUTER_1_INTERFACE_NAME_0 \
        --peer-ip-address=PEER_IP_ADDRESS_1 \
        --peer-asn=PEER_ASN_2 \
        --region=REGION \
        --enable-ipv6 \
        --ipv6-nexthop-address=IPV6_NEXTHOP_ADDRESS_1 \
        --peer-ipv6-nexthop-address=PEER_IPV6_NEXTHOP_ADDRESS_1
    

The following command creates an IPv4 BGP peer without IPv6 enabled:
    
    gcloud compute routers add-bgp-peer ROUTER_NAME_1 \
        --peer-name=PEER_NAME_GW1_IF0 \
        --interface=ROUTER_1_INTERFACE_NAME_0 \
        --peer-ip-address=PEER_IP_ADDRESS_1 \
        --peer-asn=PEER_ASN_2 \
        --region=REGION
    

Optional: To use MD5 authentication, use the `--md5-authentication-key` flag to provide your secret key:
    
    gcloud compute routers add-bgp-peer ROUTER_NAME_1 \
        --peer-name=PEER_NAME_GW1_IF0 \
        --interface=ROUTER_1_INTERFACE_NAME_0 \
        --peer-ip-address=PEER_IP_ADDRESS_1 \
        --peer-asn=PEER_ASN_2 \
        --region=REGION \
        --md5-authentication-key=AUTHENTICATION_KEY
    

The command output looks similar to the following example:
    
    Updated [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/routers/router-a].
    

  2. **Create an interface and a BGP peer on` ROUTER_NAME_1` for the tunnel `TUNNEL_NAME_GW1_IF1`**.

This interface is used to connect `TUNNEL_NAME_GW1_IF1` on `interface 1` of `GW_1` to `interface 1` of `GW_2`.

In the following commands, replace the following:

     * `ROUTER_1_INTERFACE_NAME_1`: a Cloud Router interface name; using a name related to `TUNNEL_NAME_GW1_IF1` is helpful
     * `IP_VERSION`: specify `IPV4` or leave unspecified
     * `IP_ADDRESS_2`: optional: a BGP IPv4 address from the `169.254.0.0/16` that's not already in use; this example uses `169.254.1.1`. If you omit this flag and don't manually assign a BGP IPv4 address, Google Cloud automatically assigns an address for you
     * `MASK_LENGTH`: specify `30` because the Cloud Router must use a unique `/30` CIDR from the same `169.254.0.0/16` IPv4 address range.
     * `PEER_NAME_GW1_IF1`: a name describing the BGP peer; using a name related to `TUNNEL_NAME_GW1_IF1` is helpful
     * `PEER_IP_ADDRESS_2`: a BGP IPv4 address from the `169.254.0.0/16` IPv4 address range that's not already in use; this example uses `169.254.1.2`. If you did not specifically assign a BGP IPv4 address, `IP_ADDRESS_2`, omit this option and Google Cloud automatically assigns a matching BGP peer IPv4 address for you. If you manually specified `IP_ADDRESS_2`, you must also manually configure this option.
     * `PEER_ASN_2`: the ASN number used for all interfaces on the other Cloud Router `ROUTER_NAME_2`; this example uses ASN number `65002`
     * Optional: If you are configuring an IPv4 BGP session with MP-BGP, specify `--enable-ipv6` in the `add-bgp-peer` command to enable IPv6 route exchange. You also have the option to configure IPv6 next hop addresses manually. To configure next hop addresses, replace both of the following:

       * `IPV6_NEXTHOP_ADDRESS_2`: the next hop address for IPv6 routes that are advertised by Cloud Router; the address must be in the `2600:2d00:0:2::/63` IPv6 address range
       * `PEER_IPV6_NEXTHOP_ADDRESS_2`: the next hop address for IPv6 routes learned by the Cloud Router from the BGP peer; the address must be in the `2600:2d00:0:2::/63` IPv6 address range

If you don't specify the IPv6 next hop addresses, Google Cloud automatically assigns unused addresses from the `2600:2d00:0:2::/63` IPv6 address range.

     * `AUTHENTICATION_KEY_2`: the secret key to use for MD5 authentication on `PEER_NAME_GW1_IF1`; for more information about this optional feature, see [Use MD5 authentication](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication)

**Create a Cloud Router interface for` TUNNEL_NAME_GW1_IF1`**

To create an interface with an IPv4 address, run the following command:
    
    gcloud compute routers add-interface ROUTER_NAME_1 \
      --interface-name=ROUTER_1_INTERFACE_NAME_1 \
      --ip-address=IP_ADDRESS_2 \
      --mask-length=MASK_LENGTH \
      --vpn-tunnel=TUNNEL_NAME_GW1_IF1 \
      --region=REGION
    

**Create a BGP peer for` TUNNEL_NAME_GW1_IF1`**

The following example command creates an IPv6-enabled BGP peer with manually specified IPv4 BGP addresses and IPv6 next hop addresses:
    
    gcloud compute routers add-bgp-peer ROUTER_NAME_1  \
      --peer-name=PEER_NAME_GW1_IF1 \
      --interface=ROUTER_1_INTERFACE_NAME_1 \
      --peer-ip-address=PEER_IP_ADDRESS_2 \
      --peer-asn=PEER_ASN_2 \
      --region=REGION \
      --enable-ipv6 \
      --ipv6-nexthop-address=IPV6_NEXTHOP_ADDRESS_1 \
      --peer-ipv6-nexthop-address=PEER_IPV6_NEXTHOP_ADDRESS_1
    

The following command creates an IPv4 BGP peer that does not have IPv6 route exchange enabled:
    
    gcloud compute routers add-bgp-peer ROUTER_NAME_1 \
        --peer-name=PEER_NAME_GW1_IF1 \
        --interface=ROUTER_1_INTERFACE_NAME_1 \
        --peer-ip-address=PEER_IP_ADDRESS_2 \
        --peer-asn=PEER_ASN_2 \
        --region=REGION
    

Optional: To use MD5 authentication, use the `--md5-authentication-key` flag to provide your secret key:
    
    gcloud compute routers add-bgp-peer ROUTER_NAME_1 \
      --peer-name=PEER_NAME_GW1_IF1 \
      --interface=ROUTER_1_INTERFACE_NAME_1 \
      --peer-ip-address=PEER_IP_ADDRESS_2 \
      --peer-asn=PEER_ASN_2 \
      --region=REGION \
      --md5-authentication-key=AUTHENTICATION_KEY_2
    

The command output looks similar to the following example:
    
    Updated [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/routers/router-a].
    

  3. **Verify the settings for` ROUTER_NAME_1`**:
         
         gcloud compute routers describe ROUTER_NAME_1 \
             --region=REGION
         

The command output looks similar to the following example:
         
         bgp:
           advertisemode: DEFAULT
           asn: 65001
           keepaliveInterval: 20
         bgpPeers:
         — bfd:
               minReceiveInterval: 1000
               minTransmitInterval: 1000
               mode: DISABLED
               multiplier: 5
               sessionInitializationMode: DISABLED
           enable: 'TRUE'
           enableIpv6: true
           interfaceName: if-tunnel-a-to-b-if-0
           ipAddress: 169.254.0.1
           ipv6NexthopAddress: 2600:2d00:0:2:0:0:0:1
           name: bgp-peer-tunnel-a-to-b-if-0
           peerAsn: 65002
           peerIpAddress: 169.254.0.2
           peerIpv6NexthopAddress: 2600:2d00:0:2:0:0:0:2
         — bfd:
               minReceiveInterval: 1000
               minTransmitInterval: 1000
               mode: DISABLED
               multiplier: 5
               sessionInitializationMode: DISABLED
           enable: 'TRUE'
           enableIpv6: true
           interfaceName: if-tunnel-a-to-b-if-1
           ipAddress: 169.254.1.1
           ipv6NexthopAddress: 2600:2d00:0:2:0:0:1:1
           name: bgp-peer-tunnel-a-to-b-if-1
           peerAsn: 65002
           peerIpAddress: 169.254.1.2
           peerIpv6NexthopAddress: 2600:2d00:0:2:0:0:1:2
         creationTimestamp: '2021-10-19T14:31:52.639-07:00'
         id: '4047683710114914215'
         interfaces:
         — ipRange: 169.254.0.1/30
           linkedVpnTunnel: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/vpnTunnels/tunnel-a-to-b-if-0
           name: if-tunnel-a-to-b-if-0
         — ipRange: 169.254.1.1/30
           linkedVpnTunnel: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/vpnTunnels/tunnel-a-to-b-if-1
           name: if-tunnel-a-to-b-if-1
         kind: compute#router
         name: router-a
         network: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/network-a
         region: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1
         selfLink: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/routers/router-a
         

  4. **Create an interface and a BGP peer on` ROUTER_NAME_2` for the tunnel `TUNNEL_NAME_GW2_IF0`**.

This interface connects `TUNNEL_NAME_GW2_IF0` on `interface 0` of `GW_2` to `interface 0` of `GW_1`.

In the following commands, replace the following:

     * `ROUTER_2_INTERFACE_NAME_0`: a Cloud Router interface name; using a name related to `TUNNEL_NAME_GW2_IF0` is helpful
     * `IP_VERSION`: specify `IPV4` or leave unspecified. If unspecified, the default is `IPV4`.
     * `IP_ADDRESS_3`: if you manually configured `PEER_IP_ADDRESS_1` for `TUNNEL_NAME_GW1_IF0`, then specify that value for `IP_ADDRESS_3`. If Google Cloud automatically assigned this peer IPv4 address, then you must find out which address has been allocated by Google Cloud. Run the `gcloud compute routers describe ROUTER_NAME_1` command. In the output for the BGP peer `PEER_NAME_GW1_IF0`, use the value that appears in the `peerIpAddress` field. This example uses `169.254.0.2`.
     * `MASK_LENGTH`: specify `30` because the Cloud Router must use a unique `/30` CIDR from the same `169.254.0.0/16` IPv4 address range.
     * `PEER_NAME_GW2_IF0`: a name describing the BGP peer; using a name related to `TUNNEL_NAME_GW2_IF0` is helpful
     * `PEER_IP_ADDRESS_3`: the BGP IPv4 address used previously when you configured the first gateway and interface. Run the `gcloud compute routers describe ROUTER_NAME_1` command, and use the value that appears in the `ipAddress` field for the BGP peer `PEER_NAME_GW1_IF0` that you created for `TUNNEL_NAME_GW1_IF0`. This example uses `169.254.0.1`.
     * `PEER_ASN_1`: the ASN number used for all interfaces on `ROUTER_NAME_1` and that was set previously; this example uses ASN number `65001`
     * Optional: If you are creating VPN tunnels with IPv4 BGP sessions and MP-BGP, specify `--enable-ipv6` in the `add-bgp-peer` command to enable IPv6 traffic. You must configure the IPv6 next hop addresses to match the interface and BGP peer configured for the first gateway. To configure next hop addresses, replace both of the following:

       * `IPV6_NEXTHOP_ADDRESS_3`: the next hop address for IPv6 routes that you specified previously in `PEER_IPV6_NEXTHOP_ADDRESS_1`. If you automatically assigned IPv6 next hop addresses when you created the interface and BGP peer for `TUNNEL_NAME_GW1_IF0` on `ROUTER_NAME_1`, then you must find out what IPv6 next hop address has been allocated by Google Cloud. Run `gcloud compute routers describe ROUTER_NAME_1` and check the output for the BPG peer `PEER_NAME_GW1_IF0` that you set up for `TUNNEL_NAME_GW1_IF0`. Use the value that appears in the `peerIpv6NextHopAddress` field. This example uses `2600:2d00:0:2:0:0:0:2`.
       * `PEER_IPV6_NEXTHOP_ADDRESS_3`: the next hop address for IPv6 routes learned by the Cloud Router from the BGP peer. Use the value that you specified previously in `IPV6_NEXTHOP_ADDRESS_1`. If you automatically assigned IPv6 next hop addresses, run the `gcloud compute routers describe ROUTER_NAME_1` command and check the output for the BPG peer you set up for `TUNNEL_NAME_GW1_IF0`. Use the value that appears in the `Ipv6NextHopAddress` field. This example uses `2600:2d00:0:2:0:0:0:1`.
     * `AUTHENTICATION_KEY`: the secret key to use for MD5 authentication on `PEER_NAME_GW2_IF0`

**Create a Cloud Router interface for` TUNNEL_NAME_GW2_IF0`**

To create an interface with an IPv4 address, run the following command:
    
    gcloud compute routers add-interface ROUTER_NAME_2 \
        --interface-name=ROUTER_2_INTERFACE_NAME_0 \
        --ip-address=IP_ADDRESS_3 \
        --mask-length=MASK_LENGTH \
        --vpn-tunnel=TUNNEL_NAME_GW2_IF0 \
        --region=REGION
    

**Create a BGP peer for` TUNNEL_NAME_GW2_IF0`**

The following example command creates a BGP peer with IPv6 route exchange enabled:
    
    gcloud compute routers add-bgp-peer ROUTER_NAME_2 \
        --peer-name=PEER_NAME_GW2_IF0 \
        --interface=ROUTER_2_INTERFACE_NAME_0 \
        --peer-ip-address=PEER_IP_ADDRESS_3 \
        --peer-asn=PEER_ASN_1 \
        --region=REGION \
        --enable-ipv6 \
        --ipv6-nexthop-address=IPV6_NEXTHOP_ADDRESS \
        --peer-ipv6-nexthop-address=PEER_IPV6_NEXTHOP_ADDRESS
    

The following command creates an IPv4 BGP peer without IPv6 route exchange enabled:
    
    gcloud compute routers add-bgp-peer ROUTER_NAME_2 \
        --peer-name=PEER_NAME_GW2_IF0 \
        --interface=ROUTER_2_INTERFACE_NAME_0 \
        --peer-ip-address=PEER_IP_ADDRESS_3 \
        --peer-asn=PEER_ASN_1 \
        --region=REGION
    

Alternatively, if you configured `ROUTER_NAME_1` to use MD5 authentication for `PEER_NAME_GW1_IF0`, configure `ROUTER_NAME_2` to use MD5 authentication, as follows:
    
    gcloud compute routers add-bgp-peer ROUTER_NAME_2  \
      --peer-name=PEER_NAME_GW2_IF0 \
      --interface=ROUTER_2_INTERFACE_NAME_0 \
      --peer-ip-address=PEER_IP_ADDRESS_3 \
      --peer-asn=PEER_ASN_1 \
      --region=REGION \
      --md5-authentication-key=AUTHENTICATION_KEY
    

The command output looks similar to the following example:
    
    Updated [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/routers/router-b].
    

  5. **Create an interface with an IPv4 address and a BGP peer on` ROUTER_NAME_2` for the tunnel `TUNNEL_NAME_GW2_IF1`**.

This interface connects `TUNNEL_NAME_GW2_IF1` on `interface 1` of `GW_2` to `interface 1` of `GW_1`.

In the following commands, replace the following:

     * `ROUTER_2_INTERFACE_NAME_1`: a Cloud Router interface name; using a name related to `TUNNEL_NAME_GW2_IF1` is helpful
     * `IP_VERSION`: specify `IPV4` or leave unspecified. If unspecified, the default is `IPV4`.
     * `IP_ADDRESS_4`: if you manually assigned a BGP IPv4 address for`PEER_IP_ADDRESS_2` for `TUNNEL_NAME_GW1_IF1`, then specify that value for `IP_ADDRESS_4`. If Google Cloud automatically assigned the IPv4 address, then you must find out which address has been allocated by Google Cloud. Run the `gcloud compute routers describe ROUTER_NAME_1` command. In the output for the BGP peer `PEER_NAME_GW1_IF1`, use the value that appears in the `peerIpAddress` field. This example uses `169.254.1.2`.
     * `MASK_LENGTH`: for an interface with an IPv4 address, specify `30` because the Cloud Router must use a unique `/30` CIDR from the same `169.254.0.0/16` IPv4 address range. For an interface with an IPv6 address, specify a mask length of `126` or lower.
     * `PEER_NAME_GW2_IF1`: a name describing the BGP peer; using a name related to `TUNNEL_NAME_GW2_IF1` is helpful
     * `PEER_IP_ADDRESS_4`: the IP address you specified as `IP_ADDRESS_2` when you configured the first gateway and interface. Run the `gcloud compute routers describe ROUTER_NAME_1` command, and use the value that appears in the `ipAddress` field for the BGP peer you created for `TUNNEL_NAME_GW1_IF1`. This example uses `169.254.1.1`.
     * `PEER_ASN_1`: the ASN number used for all interfaces on `ROUTER_NAME_1` and that was set previously; this example uses ASN number `65001`
     * Optional: If you are configuring an IPv4 BGP session with MP-BGP, specify `--enable-ipv6` in the `add-bgp-peer` command to enable IPv6 route exchange. You also have the option to configure IPv6 next hop addresses manually. To configure next hop addresses, replace both of the following:

       * `IPV6_NEXTHOP_ADDRESS_4`: the next hop address for IPv6 routes that you specified previously in `PEER_IPV6_NEXTHOP_ADDRESS_2`. If you automatically assigned IPv6 next hop addresses when you created the interface and BGP peer for `TUNNEL_NAME_GW1_IF1` on `ROUTER_NAME_1`, then you must find out what IPv6 next hop address has been allocated by Google Cloud. Run the `gcloud compute routers describe ROUTER_NAME_1` command and check the output for the BPG peer `PEER_NAME_GW1_IF1` that you set up for `TUNNEL_NAME_GW1_IF1`. Use the value that appears in the `peerIpv6NextHopAddress` field.
       * `PEER_IPV6_NEXTHOP_ADDRESS_3`: the next hop address for IPv6 routes learned by the Cloud Router from the BGP peer. Use the value that you specified previously in `IPV6_NEXTHOP_ADDRESS_2`. If you automatically assigned IPv6 next hop addresses, run the `gcloud compute routers describe ROUTER_NAME_1` command and check the output for the BPG peer `PEER_NAME_GW1_IF1` that you set up for `TUNNEL_NAME_GW1_IF1`. Use the value that appears in the `Ipv6NextHopAddress` field. This example uses `2600:2d00:0:2:0:0:1:1`.
     * `AUTHENTICATION_KEY_2`: the secret key to use for MD5 authentication on `PEER_NAME_GW2_IF1`

**Create a Cloud Router interface for` TUNNEL_NAME_GW2_IF1`**
    
    gcloud compute routers add-interface ROUTER_NAME_2 \
      --interface-name=ROUTER_2_INTERFACE_NAME_1 \
      --ip-address=IP_ADDRESS_4 \
      --mask-length=MASK_LENGTH \
      --vpn-tunnel=TUNNEL_NAME_GW2_IF1 \
      --region=REGION
    

The command output looks similar to the following example:
    
    Updated [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/routers/router-b].
    

**Create a BGP peer for` TUNNEL_NAME_GW2_IF1`**

The following example command creates a BGP peer with IPv6 route exchange enabled:
    
    gcloud compute routers add-bgp-peer ROUTER_NAME_2  \
      --peer-name=PEER_NAME_GW2_IF1 \
      --interface=ROUTER_2_INTERFACE_NAME_1 \
      --peer-ip-address=PEER_IP_ADDRESS_4 \
      --peer-asn=PEER_ASN_1 \
      --region=REGION \
      --enable-ipv6 \
      --ipv6-nexthop-address=IPV6_NEXTHOP_ADDRESS \
      --peer-ipv6-nexthop-address=PEER_IPV6_NEXTHOP_ADDRESS
    

The following command creates a BGP peer without IPv6 route exchange enabled:
    
    gcloud compute routers add-bgp-peer ROUTER_NAME_2 \
        --peer-name=PEER_NAME_GW2_IF1 \
        --interface=ROUTER_2_INTERFACE_NAME_1 \
        --peer-ip-address=PEER_IP_ADDRESS_4 \
        --peer-asn=PEER_ASN_1 \
        --region=REGION
    

Alternatively, if you configured `ROUTER_NAME_1` to use MD5 authentication for `PEER_NAME_GW1_IF1`, configure `ROUTER_NAME_2` to use MD5 authentication, as follows:
    
    gcloud compute routers add-bgp-peer ROUTER_NAME_2  \
      --peer-name=PEER_NAME_GW2_IF1 \
      --interface=ROUTER_2_INTERFACE_NAME_1 \
      --peer-ip-address=PEER_IP_ADDRESS_4 \
      --peer-asn=PEER_ASN_1 \
      --region=REGION \
      --md5-authentication-key=AUTHENTICATION_KEY_2
    

The command output looks similar to the following example:
    
    Updated [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/routers/router-b].
    

  6. **Verify the settings for` ROUTER_NAME_2`**:
         
         gcloud compute routers describe ROUTER_NAME_2  \
           --region=REGION
         

The command output looks similar to the following example:
         
         bgp:
           advertiseMode: DEFAULT
           asn: 65002
         bgpPeers:
         — bfd:
               minReceiveInterval: 1000
               minTransmitInterval: 1000
               mode: DISABLED
               multiplier: 5
               sessionInitializationMode: DISABLED
           enable: 'TRUE'
           enableIpv6: true
           interfaceName: if-tunnel-b-to-a-if-0
           ipAddress: 169.254.0.2
           ipv6NexthopAddress: 2600:2d00:0:2:0:0:0:2
           name: bgp-peer-tunnel-b-to-a-if-0
           peerAsn: 65001
           peerIpAddress: 169.254.0.1
           peerIpv6NexthopAddress: 2600:2d00:0:2:0:0:0:1
         — bfd:
               minReceiveInterval: 1000
               minTransmitInterval: 1000
               mode: DISABLED
               multiplier: 5
               sessionInitializationMode: DISABLED
           enable: 'TRUE'
           enableIpv6: true
           interfaceName: if-tunnel-b-to-a-if-1
           ipAddress: 169.254.1.2
           ipv6NexthopAddress: 2600:2d00:0:2:0:0:1:2
           name: bgp-peer-tunnel-b-to-a-if-1
           peerAsn: 65001
           peerIpAddress: 169.254.1.1
           peerIpv6NexthopAddress: 2600:2d00:0:2:0:0:1:1
         creationTimestamp: '2021-10-19T14:31:52.639-07:00'
         id: '4047683710114914215'
         interfaces:
         — ipRange: 169.254.0.1/30
           linkedVpnTunnel: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/vpnTunnels/tunnel-b-to-a-if-0
           name: if-tunnel-b-to-a-if-0
           — ipRange: 169.254.1.1/30
           linkedVpnTunnel: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/vpnTunnels/tunnel-b-to-a-if-1
           name: if-tunnel-b-to-a-if-1
         kind: compute#router
         name: router-b
         network: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/network-b
         region: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1
         selfLink: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/routers/router-b
         




###  API 

  1. To create a Cloud Router interface, make one of the following requests:

     * `PATCH`: Use the [`routers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/patch)
     * `UPDATE`: Use the [`routers.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/update)

The `PATCH` request updates only the parameters that you include, whereas the `UPDATE` request updates all the parameters of a Cloud Router.

You must create a Cloud Router interface for each VPN tunnel on the HA VPN gateway.

**Note:** For information about setting advertised routes, see Setting the base advertised route priority.

The BGP IPv4 address ranges that you specify must be unique among all Cloud Routers in all regions of a VPC network.
    
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

To create a full BGP session configuration for an HA VPN gateway, use the following API command:
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
    {
    "bgpPeers": [
      {
        "name": "bgp-peer-tunnel-a-to-on-prem-if-0",
        "interfaceName": "if-tunnel-a-to-on-prem-if-0",
        "ipAddress": "169.254.0.1",
        "peerIpAddress": "169.254.0.2",
        "peerAsn": 65002,
    
        "advertiseMode": "DEFAULT"
      }
    ]
    }
    

To create the full BGP session configuration for an HA VPN gateway with IPv6 enabled, use the following API command:
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
    {
    "bgpPeers": [
      {
        "name": "bgp-peer-tunnel-a-to-on-prem-if-0",
        "interfaceName": "if-tunnel-a-to-on-prem-if-0",
        "ipAddress": "169.254.0.1",
        "peerIpAddress": "169.254.0.2",
        "peerAsn": 65002,
    
        "advertiseMode": "DEFAULT"
        "enableIpv6": true
        "ipv6NexthopAddress: "2600:2d00:0:2:0:0:0:1"
        "peerIpv6NexthopAddress: "2600:2d00:0:2:0:0:0:2"
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
      "ipAddress": "169.254.0.1",
      "name": "bgp-peer-tunnel-a-to-on-prem-if-0",
      "peerAsn": 65002,
      "peerIpAddress": "169.254.0.2",
      "advertiseMode": "DEFAULT",
      "md5AuthenticationKeyName": "bgppeer-1-key"
      }
    ],
    }
    




### IPv6 BGP sessions

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

In this section, you configure IPv6 Cloud Router interfaces and BGP peers; the following table provides an overview of these interfaces and peers. It shows the relationship between the IPv6 BGP ranges and peer IP addresses that you specify for each interface.

For example, the first interface of `router-1` has an IPv6 address of `fdff:1::1`, which means `router-1` is the first host in IPv6 subnet `fdff:1::/126`. The other Cloud Router, `router-2`, is the BGP peer of `router-1`. The first interface of `router-2` is assigned `fdff:1::2`, which is the second host in the IPv6 subnet `fdff:1::/126`. Therefore, the BGP peer IPv6 address of `router-1` is `fdff:1::2` and the address of `router-2` is `fdff:1::2`.

**Important:** The BGP IPv6 address range for each BGP session must be unique among all Cloud Routers in all regions of a VPC network.

Router | Interface name | IPv6 address range | Peer IPv6 address | Peer ASN | IPv4 next-hop  
address | Peer IPv4 next-hop  
address  
---|---|---|---|---|---|---  
router-1 | if-tunnel-a-to-b-if-0 | fdff:1::/64 | fdff:1::2 | 65002 | 169.254.12.1 | 169.254.12.2  
router-2 | if-tunnel-b-to-a-if-0 | fdff:1::/64 | fdff:1::1 | 65001 | 169.254.12.2 | 169.254.12.1  
router-1 | if-tunnel-a-to-b-if-1 | fdff:1::/64 | fdff:1::2 | 65002 | 169.254.13.1 | 169.254.13.2  
router-2 | if-tunnel-b-to-a-if-1 | fdff:1::/64 | fdff:1::1 | 65001 | 169.254.13.2 | 169.254.13.1  
  
To create Cloud Router interfaces and BGP peers, complete the following command sequence.

  1. **Create an interface and BGP peer on` ROUTER_NAME_1` for the tunnel `TUNNEL_NAME_GW1_IF0`**.

This interface connects `TUNNEL_NAME_GW1_IF0` on `interface 0` of `GW_1` to `interface 0` of `GW_2`.

In the following commands, replace the following:

     * `ROUTER_1_INTERFACE_NAME_0`: a name for the Cloud Router interface; using a name related to `TUNNEL_NAME_GW1_IF0` is helpful
     * `IP_VERSION`: `IPV6`; this parameter is only required if you want Google Cloud to assign the IPv6 address automatically for this interface. If you are manually assigning an IPv6 address to this interface, you can omit this flag.
     * `IP_ADDRESS_1`: a BGP IPv6 address from the `fdff:1::/64` IPv6 address range that's not already in use; this example uses `fdff:1::1`. If you omit this flag and don't manually assign an IPv6 address, Google Cloud automatically assigns an address for you.
     * `MASK_LENGTH`: specify a mask length of `126`.
     * `PEER_NAME_GW1_IF0`: a name describing the BGP peer; using a name related to `TUNNEL_NAME_GW1_IF0` is helpful
     * `PEER_IP_ADDRESS_1`: a BGP IPv6 address from the `fdff:1::/64` IPv6 address range that's not already in use; this example uses `fdff:1::2`. If you did not previously assign a specific BGP IPv6 address, `IP_ADDRESS_1`, omit this option as well and Google Cloud automatically assigns a matching BGP peer IPv6 address for you. If you manually specified `IP_ADDRESS_1`, you must also manually configure this option.
     * `PEER_ASN_2`: the ASN number used for all interfaces on the other Cloud Router `ROUTER_NAME_2`; this example uses ASN number `65002`
     * Optional: To enable IPv4 route exchange in IPv6 BGP sessions with MP-BGP, specify `--enable-ipv4` when you run the `gcloud compute routers add-bgp-peer` command. You also have the option to configure IPv4 next hop addresses automatically or manually.

To configure IPv4 next hop addresses manually, replace both of the following:

       * `IPV4_NEXTHOP_ADDRESS_1`: the next hop address for IPv4 routes that are advertised by Cloud Router; the address must be in the link-local IPv4 address range `169.254.0.0/16`. for IPv4 routes learned by the Cloud Router from the BGP peer; the address must be in the link-local address range `169.254.0.0/16`.

If you don't specify IPv4 next hop addresses, then Google Cloud automatically assigns unused addresses from the `169.254.0.0/16` IPv4 address range for you.

     * `AUTHENTICATION_KEY`: the secret key to use for MD5 authentication on `PEER_NAME_GW1_IF0`; for more information about this optional feature, see [Use MD5 authentication](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication).

**Optional: Assign a BGP identifier range**

When you add the first interface to a Cloud Router with an IPv6 address, a BGP identifier range is automatically assigned to the Cloud Router. If you prefer to define your own BGP identifier range for a Cloud Router, you can create your own range. You can also modify this range later.

For more information, see [Configure the BGP identifier range for a Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configure-bgp-identifier).

###  Automatic 

**Create an interface for` TUNNEL_NAME_GW1_IF0`**

To create an interface with an automatically assigned IPv6 address, run the following command.
    
    gcloud compute routers add-interface ROUTER_NAME_1 \
      --interface-name=ROUTER_1_INTERFACE_NAME_0 \
      --vpn-tunnel=TUNNEL_NAME_GW1_IF0 \
      --region=REGION \
      --ip-version=IPV6
    

**Create a BGP peer for` TUNNEL_NAME_GW1_IF0`**

To create an IPv6 BGP peer with IPv4 route exchange enabled and automatically assigned IPv4 next-hop addresses, run the following command.
    
    gcloud compute routers add-bgp-peer ROUTER_NAME_1 \
      --peer-name=PEER_NAME_GW1_IF0 \
      --interface=ROUTER_1_INTERFACE_NAME_0 \
      --peer-asn=PEER_ASN_2 \
      --region=REGION \
      --enable-ipv4 \
    

The following command creates a BGP peer without IPv4 enabled and an automatically assigned IPv6 address:
    
    gcloud compute routers add-bgp-peer ROUTER_NAME_1 \
    --peer-name=PEER_NAME_GW1_IF0 \
    --interface=ROUTER_1_INTERFACE_NAME_0 \
    --peer-asn=PEER_ASN_2 \
    --region=REGION
    

Optional: To use MD5 authentication, use the `--md5-authentication-key` flag to provide your secret key:
    
    gcloud compute routers add-bgp-peer ROUTER_NAME_1   
    
        --peer-name=PEER_NAME_GW1_IF0   
    
        --interface=ROUTER_1_INTERFACE_NAME_0   
    
        --peer-asn=PEER_ASN_2   
    
        --region=REGION   
    
        --md5-authentication-key=AUTHENTICATION_KEY
      

The command output looks similar to the following example:
    
    Updated [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/routers/router-a].
      

###  Manual 

**Create an interface for` TUNNEL_NAME_GW1_IF0`**

To create an interface with a manually specified IPv6 address, run the following command.
    
    gcloud compute routers add-interface ROUTER_NAME_1 \
      --interface-name=ROUTER_1_INTERFACE_NAME_0 \
      --ip-address=IP_ADDRESS_1 \
      --mask-length=MASK_LENGTH \
      --vpn-tunnel=TUNNEL_NAME_GW1_IF0 \
      --region=REGION \
    

**Create a BGP peer for` TUNNEL_NAME_GW1_IF0`**

To create a BGP peer with IPv4 route exchange enabled and manually specified IPv4 next-hop addresses, run the following command.
    
    gcloud compute routers add-bgp-peer ROUTER_NAME_1 \
      --peer-name=PEER_NAME_GW1_IF0 \
      --interface=ROUTER_1_INTERFACE_NAME_0 \
      --peer-ip-address=PEER_IP_ADDRESS_1 \
      --peer-asn=PEER_ASN_2 \
      --region=REGION \
      --enable-ipv4 \
      --ipv4-nexthop-address=IPV4_NEXTHOP_ADDRESS_1 \
      --peer-ipv4-nexthop-address=PEER_IPV4_NEXTHOP_ADDRESS_1
    

The following command creates a BGP peer without IPv4 route exchange enabled:
    
    gcloud compute routers add-bgp-peer ROUTER_NAME_1 \
    --peer-name=PEER_NAME_GW1_IF0 \
    --interface=ROUTER_1_INTERFACE_NAME_0 \
    --peer-ip-address=PEER_IP_ADDRESS_1 \
    --peer-asn=PEER_ASN_2 \
    --region=REGION
    

Optional: To use MD5 authentication, use the `--md5-authentication-key` flag to provide your secret key:
    
    gcloud compute routers add-bgp-peer ROUTER_NAME_1 \
      --peer-name=PEER_NAME_GW1_IF0 \
      --interface=ROUTER_1_INTERFACE_NAME_0 \
      --peer-ip-address=PEER_IP_ADDRESS_1 \
      --peer-asn=PEER_ASN_2 \
      --region=REGION \
      --md5-authentication-key=AUTHENTICATION_KEY
    

The command output looks similar to the following example:
    
    Updated [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/routers/router-a].
    

  2. **Create an interface and BGP peer on` ROUTER_NAME_1` for the tunnel `TUNNEL_NAME_GW1_IF1`**.

This interface connects `TUNNEL_NAME_GW1_IF1` on `interface 1` of `GW_1` to `interface 1` of `GW_2`.

In the following commands, replace the following:

     * `ROUTER_1_INTERFACE_NAME_1`: a Cloud Router interface name; using a name related to `TUNNEL_NAME_GW1_IF1` is helpful
     * `IP_VERSION`: `IPV6`
     * `IP_ADDRESS_2`: a BGP IPv6 address from the `fdff:1::/64` IPv6 address range that's not already in use; this example uses `fdff:1::1:1`. If you omit this flag and don't manually assign a BGP IPv6 address, Google Cloud automatically assigns an address for you.
     * `MASK_LENGTH`: specify a mask length of `64`
     * `PEER_NAME_GW1_IF1`: a name describing the BGP peer; using a name related to `TUNNEL_NAME_GW1_IF1` is helpful
     * `PEER_IP_ADDRESS_2`: a BGP IPv6 address from the `fdff:1::/64` IPv6 address range that's not already in use; this example uses `fdff:1::1:2`. If you did not specifically assign an IPv6 address, `IP_ADDRESS_2`, omit this option, and Google Cloud automatically assigns a matching BGP peer IPv6 address for you. If you manually specified `IP_ADDRESS_2`, you must also manually configure this option.
     * `PEER_ASN_2`: the ASN number used for all interfaces on the other Cloud Router `ROUTER_NAME_2`; this example uses ASN number `65002`
     * Optional: To enable IPv4 route exchange in IPv6 BGP sessions with MP-BGP, specify `--enable-ipv4` when you run the `gcloud compute routers add-bgp-peer` command. You also have the option to configure IPv4 next hop addresses automatically or manually.

To configure IPv4 next hop addresses manually, replace both of the following:

       * `IPV4_NEXTHOP_ADDRESS_2`: the next hop address for IPv4 routes that are advertised by Cloud Router; the address must be in the link-local IPv4 address range `169.254.0.0/16`.
       * `PEER_IPV4_NEXTHOP_ADDRESS_2`: the next hop address for IPv4 routes learned by the Cloud Router from the BGP peer; the address must be in the link-local IPv4 address range `169.254.0.0/16`.
     * `AUTHENTICATION_KEY_2`: the secret key to use for MD5 authentication on `PEER_NAME_GW1_IF1`; for more information about this optional feature, see [Use MD5 authentication](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication)

###  Automatic 

**Create a Cloud Router interface for` TUNNEL_NAME_GW1_IF1`**

To create an interface with an automatically assigned IPv6 address, run the following command.
    
    gcloud compute routers add-interface ROUTER_NAME_1 \
      --interface-name=ROUTER_1_INTERFACE_NAME_1 \
      --vpn-tunnel=TUNNEL_NAME_GW1_IF1 \
      --region=REGION \
      --ip-version=IPV6
    

**Create a BGP peer for` TUNNEL_NAME_GW1_IF1`**

To create an IPv6 BGP peer with IPv4 route exchange enabled and automatically assigned IPv4 next-hop addresses, run the following command.
    
    gcloud compute routers add-bgp-peer ROUTER_NAME_1 \
      --peer-name=PEER_NAME_GW1_IF1 \
      --interface=ROUTER_1_INTERFACE_NAME_1 \
      --peer-asn=PEER_ASN_2 \
      --region=REGION \
      --enable-ipv4 \
    

The following command creates a BGP peer without IPv4 enabled:
    
    gcloud compute routers add-bgp-peer ROUTER_NAME_1 \
      --peer-name=PEER_NAME_GW1_IF1 \
      --interface=ROUTER_1_INTERFACE_NAME_1 \
      --peer-asn=PEER_ASN_2 \
      --region=REGION
    

Optional: To use MD5 authentication, use the `--md5-authentication-key` flag to provide your secret key:
    
    gcloud compute routers add-bgp-peer ROUTER_NAME_1 \
      --peer-name=PEER_NAME_GW1_IF1 \
      --interface=ROUTER_1_INTERFACE_NAME_1 \
      --peer-asn=PEER_ASN_2 \
      --region=REGION \
      --md5-authentication-key=AUTHENTICATION_KEY_2
    

The command output looks similar to the following example:
    
    Updated [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/routers/router-a].
    

###  Manual 

**Create a Cloud Router interface for` TUNNEL_NAME_GW1_IF1`**

To create an interface with a manually specified IPv6 address, run the following command:
    
    gcloud compute routers add-interface ROUTER_NAME_1 \
      --interface-name=ROUTER_1_INTERFACE_NAME_1 \
      --ip-address=IP_ADDRESS_2 \
      --mask-length=MASK_LENGTH \
      --vpn-tunnel=TUNNEL_NAME_GW1_IF1 \
      --region=REGION \
    

**Create a BGP peer for` TUNNEL_NAME_GW1_IF1`**

To create an IPv6 BGP peer with IPv4 route exchange enabled, run the following command:
    
    gcloud compute routers add-bgp-peer ROUTER_NAME_1 \
    --peer-name=PEER_NAME_GW1_IF1 \
    --interface=ROUTER_1_INTERFACE_NAME_1 \
    --peer-ip-address=PEER_IP_ADDRESS_2 \
    --peer-asn=PEER_ASN_2 \
    --region=REGION \
    --enable-ipv4 \
    --ipv4-nexthop-address=IPV4_NEXTHOP_ADDRESS_2 \
    --peer-ipv4-nexthop-address=PEER_IPV4_NEXTHOP_ADDRESS_2
    

The following command creates a BGP peer without IPv4 enabled:
    
    gcloud compute routers add-bgp-peer ROUTER_NAME_1 \
    --peer-name=PEER_NAME_GW1_IF1 \
    --interface=ROUTER_1_INTERFACE_NAME_1 \
    --peer-ip-address=PEER_IP_ADDRESS_2 \
    --peer-asn=PEER_ASN_2 \
    --region=REGION
    

Optional: To use MD5 authentication, use the `--md5-authentication-key` flag to provide your secret key:
    
    gcloud compute routers add-bgp-peer ROUTER_NAME_1 \
      --peer-name=PEER_NAME_GW1_IF1 \
      --interface=ROUTER_1_INTERFACE_NAME_1 \
      --peer-ip-address=PEER_IP_ADDRESS_2 \
      --peer-asn=PEER_ASN_2 \
      --region=REGION \
      --md5-authentication-key=AUTHENTICATION_KEY_2
    

The command output looks similar to the following example:
    
    Updated [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/routers/router-a].
    

  3. **Verify the settings for` ROUTER_NAME_1`**:
         
         gcloud compute routers describe ROUTER_NAME_1 \
             --region=REGION
         

The command output looks similar to the following example: 
         
         bgp:
           advertisemode: DEFAULT
           asn: 65001
           keepaliveInterval: 20
         bgpPeers:
         — bfd:
               minReceiveInterval: 1000
               minTransmitInterval: 1000
               mode: DISABLED
               multiplier: 5
               sessionInitializationMode: DISABLED
           enable: 'TRUE'
           enableIpv4: true
           interfaceName: if-tunnel-a-to-b-if-0
           ipAddress: fdff:1::1
           ipv4NexthopAddress: 169.254.12.2
           name: bgp-peer-tunnel-a-to-b-if-0
           peerAsn: 65002
           peerIpAddress: fdff:1::2
           peerIpv4NexthopAddress: 169.254.12.1
         — bfd:
               minReceiveInterval: 1000
               minTransmitInterval: 1000
               mode: DISABLED
               multiplier: 5
               sessionInitializationMode: DISABLED
           enable: 'TRUE'
           enableIpv4: true
           interfaceName: if-tunnel-a-to-b-if-1
           ipAddress: fdff:1:1:2::1
           ipv4NexthopAddress: 169.254.13.2
           name: bgp-peer-tunnel-a-to-b-if-1
           peerAsn: 65002
           peerIpAddress: fdff:1::2
           peerIpv4NexthopAddress: 169.254.13.1
         creationTimestamp: '2021-10-19T14:31:52.639-07:00'
         id: '4047683710114914215'
         interfaces:
         — ipRange:  fdff:1::1/126
           linkedVpnTunnel: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/vpnTunnels/tunnel-a-to-b-if-0
           name: if-tunnel-a-to-b-if-0
         — ipRange:  fdff:1::1/126
           linkedVpnTunnel: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/vpnTunnels/tunnel-a-to-b-if-1
           name: if-tunnel-a-to-b-if-1
         kind: compute#router
         name: router-a
         network: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/network-a
         region: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1
         selfLink: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/routers/router-a
         

  4. **Create an interface and BGP peer on` ROUTER_NAME_2` for the tunnel `TUNNEL_NAME_GW2_IF0`**.

This interface connects `TUNNEL_NAME_GW2_IF0` on `interface 0` of `GW_2` to `interface 0` of `GW_1`.

In the following commands, replace the following:

     * `ROUTER_2_INTERFACE_NAME_0`: a Cloud Router interface name; using a name related to `TUNNEL_NAME_GW2_IF0` is helpful
     * `IP_VERSION`: `IPV6`; this parameter is only required if you want Google Cloud to assign the IPv6 address automatically for this interface. If you are manually assigning an IPv6 address to this interface, you can omit this flag.
     * `IP_ADDRESS_3`: if you manually assigned a BGP IPv6 address for `PEER_IP_ADDRESS_1` for `TUNNEL_NAME_GW1_IF0`, then specify that value for `IP_ADDRESS_3`. If Google Cloud automatically assigned this peer IPv6 address, then you must find out which address has been allocated by Google Cloud. Run the `gcloud compute routers describe ROUTER_NAME_1` command. In the output for the BGP peer `PEER_NAME_GW1_IF0`, use the value that appears in the `peerIpAddress` field. This example uses`fdff:1::2`.
     * `MASK_LENGTH`: specify a mask length of `126` or smaller.
     * `PEER_NAME_GW2_IF0`: a name describing the BGP peer; using a name related to `TUNNEL_NAME_GW2_IF0` is helpful
     * `PEER_IP_ADDRESS_3`: the BGP IPv6 address used previously when you configured the first gateway and interface. Run the `gcloud compute routers describe ROUTER_NAME_1` command, and use the value that appears in the `ipAddress` field for the BGP peer you created for `fdff:1::1`.
     * `PEER_ASN_1`: the ASN number used for all interfaces on `ROUTER_NAME_1` and that was set previously; this example uses ASN number `65001`
     * Optional: If you are creating IPv6 BGP sessions and MP-BGP, specify `--enable-ipv4` when you run the `gcloud compute routers add-bgp-peer` command to enable IPv4 traffic. You must configure the IPv4 next hop addresses to match the interface and IPv4-enabled BGP peer configured for the first gateway.

To configure next hop addresses, replace both of the following:

       * `IPV4_NEXTHOP_ADDRESS_3`: the next hop address for IPv4 routes specified previously in `PEER_IPV4_NEXTHOP_ADDRESS_1`; if you automatically assigned IPv4 next hop addresses when you created the interface and BGP peer for `TUNNEL_NAME_GW1_IF0` on `ROUTER_NAME_1`, then you must find out what address has been allocated by Google Cloud. Run the `gcloud compute routers describe ROUTER_NAME_1` command, and check the output for the BPG peer you set up for `TUNNEL_NAME_GW1_IF0`. Use the value that appears in the `peerIpv4NextHopAddress` field. This example uses `169.254.13.1`.
       * `PEER_IPV4_NEXTHOP_ADDRESS_2`: the next hop address for IPv4 routes learned by the Cloud Router from the BGP peer; the address must be in the IPv4 link-local range `169.254.0.0/16`. This example uses `169.254.13.2`.
     * `AUTHENTICATION_KEY`: the secret key to use for MD5 authentication on `PEER_NAME_GW2_IF0`

**Optional: Assign a BGP identifier range**

When you add the first interface to a Cloud Router with an IPv6 address, a BGP identifier range is automatically assigned to the Cloud Router. If you prefer to define your own BGP identifier range for a Cloud Router, you can create your own range. You can also modify this range later.

For more information, see [Configure the BGP identifier range for a Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configure-bgp-identifier).

**Create a Cloud Router interface for` TUNNEL_NAME_GW2_IF0`**

To create an interface with an IPv6 address, run the following command:
    
    gcloud compute routers add-interface ROUTER_NAME_1 \
        --interface-name=ROUTER_2_INTERFACE_NAME_0 \
        --ip-address=IP_ADDRESS_3 \
        --mask-length=MASK_LENGTH \
        --vpn-tunnel=TUNNEL_NAME_GW2_IF0 \
        --region=REGION \
        --ip-version=IPV6
    

**Create a BGP peer for` TUNNEL_NAME_GW2_IF0`**

The following example command creates an IPv4-enabled BGP peer:
    
    gcloud compute routers add-bgp-peer ROUTER_NAME_2 \
        --peer-name=PEER_NAME_GW2_IF0 \
        --interface=ROUTER_2_INTERFACE_NAME_0 \
        --peer-ip-address=PEER_IP_ADDRESS_3 \
        --peer-asn=PEER_ASN_1 \
        --region=REGION \
        --enable-ipv4 \
        --ipv4-nexthop-address=IPV4_NEXTHOP_ADDRESS \
        --peer-ipv4-nexthop-address=PEER_IPV4_NEXTHOP_ADDRESS
    

The following command creates a BGP peer without IPv4 enabled:
    
    gcloud compute routers add-bgp-peer ROUTER_NAME_2 \
        --peer-name=PEER_NAME_GW2_IF0 \
        --interface=ROUTER_2_INTERFACE_NAME_0 \
        --peer-ip-address=PEER_IP_ADDRESS_3 \
        --peer-asn=PEER_ASN_1 \
        --region=REGION
    

Alternatively, if you configured `ROUTER_NAME_1` to use MD5 authentication for `PEER_NAME_GW1_IF0`, configure `ROUTER_NAME_2` to use MD5 authentication, as follows:
    
    gcloud compute routers add-bgp-peer ROUTER_NAME_2  \
      --peer-name=PEER_NAME_GW2_IF0 \
      --interface=ROUTER_2_INTERFACE_NAME_0 \
      --peer-ip-address=PEER_IP_ADDRESS_3 \
      --peer-asn=PEER_ASN_1 \
      --region=REGION \
      --md5-authentication-key=AUTHENTICATION_KEY
    

The command output looks similar to the following example:
    
    Updated [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/routers/router-b].
    

  5. **Create an interface and BGP peer on` ROUTER_NAME_2` for the tunnel `TUNNEL_NAME_GW2_IF1`**.

This interface connects `TUNNEL_NAME_GW2_IF1` on `interface 1` of `GW_2` to `interface 1` of `GW_1`.

In the following commands, replace the following:

     * `ROUTER_2_INTERFACE_NAME_1`: a Cloud Router interface name; using a name related to `TUNNEL_NAME_GW2_IF1` is helpful
     * `IP_ADDRESS_4`: if you manually assigned a BGP IPv6 address for `PEER_IP_ADDRESS_2` for `TUNNEL_NAME_GW1_IF1`, then specify that value for `IP_ADDRESS_4`. If Google Cloud automatically assigned the peer BGP IPv6 address when you created the interface and BGP peer for `TUNNEL_NAME_GW1_IF1` on `ROUTER_NAME_1`, then you must find out which address has been allocated by Google Cloud. Run the `gcloud compute routers describe ROUTER_NAME_1` command. In the output for the BGP peer, use the value that appears in the `peerIpAddress` field. This example uses `fdff:1::1:2`.
     * `MASK_LENGTH`: specify a mask length of `126`.
     * `PEER_NAME_GW2_IF1`: a name describing the BGP peer; using a name related to `TUNNEL_NAME_GW2_IF1` is helpful
     * `PEER_IP_ADDRESS_4`: if you manually assigned a BGP IP address for `IP_ADDRESS_2` for `TUNNEL_NAME_GW1_IF1`, then specify that value for `PEER_IP_ADDRESS_4`. If Google Cloud automatically assigned the BGP IPv6 address for you, then you must find out which address has been allocated by Google Cloud. Run `gcloud compute routers describe ROUTER_NAME_1`, and use the value that appears in the `ipAddress` field for the BGP peer you created. This example uses `fdff:1::1:1`.
     * `PEER_ASN_1`: the ASN number used for all interfaces on `ROUTER_NAME_1` and that was set previously; this example uses ASN number `65001`
     * Optional: If you are creating IPv6 BGP sessions and MP-BGP, specify `--enable-ipv4` when you run the `gcloud compute routers add-bgp-peer` command to enable IPv4 traffic. You must configure the IPv4 next hop addresses to match the interface and IPv4-enabled BGP peer configured for the first gateway.

To configure next hop addresses, replace both of the following:

       * `IPV4_NEXTHOP_ADDRESS_4`: the next hop address for IPv4 routes specified previously in `PEER_IPV4_NEXTHOP_ADDRESS_3`; if you automatically assigned IPv4 next hop addresses when you created the interface and BGP peer for `TUNNEL_NAME_GW1_IF0` on `ROUTER_NAME_1`, then you must find out what address has been allocated by Google Cloud. Run the `gcloud compute routers describe ROUTER_NAME_1` command and check the output for the BPG peer you set up for `TUNNEL_NAME_GW1_IF0`. Use the value that appears in the `peerIpv4NextHopAddress` field. This example uses `169.254.13.1`.
       * `PEER_IPV4_NEXTHOP_ADDRESS_4`: the next hop address for IPv4 routes learned by the Cloud Router from the BGP peer; the address must be in the link-local IPv4 address range `169.254.0.0/16`. This example uses `169.254.13.2`.
     * `AUTHENTICATION_KEY_2`: the secret key to use for MD5 authentication on `PEER_NAME_GW2_IF1`

**Create a Cloud Router interface for` TUNNEL_NAME_GW2_IF1`**
    
    gcloud compute routers add-interface ROUTER_NAME_2 \
      --interface-name=ROUTER_2_INTERFACE_NAME_1 \
      --ip-address=IP_ADDRESS_4 \
      --mask-length=MASK_LENGTH \
      --vpn-tunnel=TUNNEL_NAME_GW2_IF1 \
      --region=REGION \
    

The command output is similar to the following example:
    
    Updated [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/routers/router-b].
    

**Create a BGP peer for` TUNNEL_NAME_GW2_IF1`**

The following example command creates an IPv6 BGP peer with IPv4 route exchange enabled:
    
    gcloud compute routers add-bgp-peer ROUTER_NAME_2  \
      --peer-name=PEER_NAME_GW2_IF1 \
      --interface=ROUTER_2_INTERFACE_NAME_1 \
      --peer-ip-address=PEER_IP_ADDRESS_4 \
      --peer-asn=PEER_ASN_1 \
      --region=REGION \
      --enable-ipv4 \
      --ipv4-nexthop-address=IPV4_NEXTHOP_ADDRESS \
      --peer-ipv4-nexthop-address=PEER_IPV4_NEXTHOP_ADDRESS
    

The following command creates an IPv6 BGP peer without IPv4 route exchange enabled:
    
    gcloud compute routers add-bgp-peer ROUTER_NAME_2 \
        --peer-name=PEER_NAME_GW2_IF1 \
        --interface=ROUTER_2_INTERFACE_NAME_1 \
        --peer-ip-address=PEER_IP_ADDRESS_4 \
        --peer-asn=PEER_ASN_1 \
        --region=REGION
    

Alternatively, if you configured `ROUTER_NAME_1` to use MD5 authentication for `PEER_NAME_GW1_IF1`, configure `ROUTER_NAME_2` to use MD5 authentication, as follows:
    
    gcloud compute routers add-bgp-peer ROUTER_NAME_2  \
      --peer-name=PEER_NAME_GW2_IF1 \
      --interface=ROUTER_2_INTERFACE_NAME_1 \
      --peer-ip-address=PEER_IP_ADDRESS_4 \
      --peer-asn=PEER_ASN_1 \
      --region=REGION \
      --md5-authentication-key=AUTHENTICATION_KEY_2
    

The command output is similar to the following example:
    
    Updated [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/routers/router-b].
    

  6. **Verify the settings for` ROUTER_NAME_2`**:
         
         gcloud compute routers describe ROUTER_NAME_2  \
           --region=REGION
         

The command output is similar to the following example:
         
         bgp:
           advertiseMode: DEFAULT
           asn: 65002
         bgpPeers:
         — bfd:
               minReceiveInterval: 1000
               minTransmitInterval: 1000
               mode: DISABLED
               multiplier: 5
               sessionInitializationMode: DISABLED
           enable: 'TRUE'
           enableIpv4: true
           interfaceName: if-tunnel-b-to-a-if-0
           ipAddress: fdff:1::2
           ipv4NexthopAddress: 169.254.12.2
           name: bgp-peer-tunnel-b-to-a-if-0
           peerAsn: 65001
           peerIpAddress: fdff:1::1
           peerIpv4NexthopAddress: 169.254.12.1
         — bfd:
               minReceiveInterval: 1000
               minTransmitInterval: 1000
               mode: DISABLED
               multiplier: 5
               sessionInitializationMode: DISABLED
           enable: 'TRUE'
           enableIpv4: true
           interfaceName: if-tunnel-b-to-a-if-1
           ipAddress: fdff:1::1
           ipv4NexthopAddress: 169.254.13.2
           name: bgp-peer-tunnel-b-to-a-if-1
           peerAsn: 65001
           peerIpAddress: fdff:1::2
           peerIpv4NexthopAddress: 169.254.13.2
         creationTimestamp: '2021-10-19T14:31:52.639-07:00'
         id: '4047683710114914215'
         interfaces:
         — ipRange: fdff:1::2/126
           linkedVpnTunnel: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/vpnTunnels/tunnel-b-to-a-if-0
           name: if-tunnel-b-to-a-if-0
           — ipRange: fdff:1::1:2/126
           linkedVpnTunnel: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/vpnTunnels/tunnel-b-to-a-if-1
           name: if-tunnel-b-to-a-if-1
         kind: compute#router
         name: router-b
         network: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/network-b
         region: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1
         selfLink: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/routers/router-b
         




###  API 

  1. To create a Cloud Router interface with an IPv6 address, make either a `PATCH` or `UPDATE` request to the [`routers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/routers/patch) or the [`routers.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/routers/update). `PATCH` updates only the parameters that you include. `UPDATE` updates all parameters for Cloud Router. Create an interface for each VPN tunnel on the HA VPN gateway.

The following example creates an interface with a manually configured IPv6 BGP address.
         
         PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
         {
         "interfaces": [
           {
             "name": "if-tunnel-a-to-b-if-0",
             "linkedVpnTunnel": "ha-vpn-gw-a-tunnel-0",
             "ipRange": "fdff:1::1/126"
             }
           ]
         }
         

Each BGP IPv6 address range for each BGP session must be unique among all Cloud Routers in all regions of a VPC network.

As another example, the following command creates an interface with an automatically assigned IPv6 address.
         
         PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
         {
         "interfaces": [
           {
             "name": "if-tunnel-a-to-b-if-0",
             "linkedVpnTunnel": "ha-vpn-gw-a-tunnel-0",
             "ipVersion": "IPV6"
             }
           ]
         }
         

Repeat this step for each VPN tunnel on the HA VPN gateway.

  2. Add a BGP peer to Cloud Router for each interface.

To create a BGP peer, make either a `PATCH` or `UPDATE` request by using the [`routers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/routers/patch) or the [`routers.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/routers/update). Repeat this command for the other interfaces, changing the field values as needed.
         
         PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
         {
         "bgpPeers": [
           {
             "name": "bgp-peer-tunnel-a-to-b-if-0",
             "interfaceName": "if-tunnel-a-to-b-if-0",
             "ipAddress": "fdff:1::2",
             "peerIpAddress": "fdff:1::1",
             "peerAsn": 65002,
             "advertiseMode": "DEFAULT"
           }
         ]
         }
         

To create an IPv6 BGP session with MP-BGP and IPv4 next-hop addresses configured, use the following API command:
         
         PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
         {
         "bgpPeers": [
           {
             "name": "bgp-peer-tunnel-a-to-b-if-0",
             "interfaceName": "if-tunnel-a-to-b-if-0",
             "ipAddress": "fdff:1::2",
             "peerIpAddress": "fdff:1::1",
             "peerAsn": 65002,
             "advertiseMode": "DEFAULT",
             "enableIpv4": true,
             "ipv4NexthopAddress: "169.254.12.2",
             "peerIpv4NexthopAddress: "169.254.12.1"
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
           "interfaceName": "if-tunnel-a-to-b-if-0",
           "ipAddress": "fdff:1::2",
           "name": "bgp-peer-tunnel-a-to-b-if-0",
           "peerAsn": 65002,
           "peerIpAddress": "fdff:1::1",
           "advertiseMode": "DEFAULT",
           "md5AuthenticationKeyName": "bgppeer-1-key"
           }
         ],
         }
         




###  Both IPv4 and IPv6 BGP sessions 

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

In this section, you configure two interfaces and BGP peers for each HA VPN tunnel. The following table provides an overview of these interfaces and peers. It shows the relationship between the IP address ranges and peer IP addresses that you specify for each interface.

For example, the first interface of `router-1` is assigned an IPv4 address of `169.254.0.1`. The second interface of `router-1` is assigned an IPv6 address of `fdff:1::1`. The other Cloud Router, `router-2`, is the BGP peer of `router-1`. The first interface of `router-2` is assigned `169.254.0.2`, which is the second host in the IPv4 subnet `169.254.0.0/30`. The second interface of `router-2` is assigned `fdff:1::2`, which is the second host in the IPv6 subnet `fdff:1::/126`. Therefore, the peer IPv4 BGP address of `router-1` is `169.254.0.2` and its peer BGP peer IPv6 address is `fdff:1::2`. The peer IPv4 BGP address of `router-2` is `169.254.0.1` and its peer BGP peer IPv6 address is `fdff:1::1`.

**Important:** The BGP IPv4 and IPv6 address ranges for each BGP session must be unique among all Cloud Routers in all regions of a VPC network.

Router | Interface name | BGP IP address | Peer IP address | Peer ASN  
---|---|---|---|---  
router-1 | if-tunnel-a-to-b-if-0_ipv4 | 169.254.0.1/30 | 169.254.0.2 | 65002  
router-1 | if-tunnel-a-to-b-if-0_ipv6 | fdff:1::1/126 | fdff:1::2 | 65002  
router-1 | if-tunnel-a-to-b-if-1_ipv4 | 169.254.1.1/30 | 169.254.1.2 | 65002  
router-1 | if-tunnel-a-to-b-if-1_ipv6 | fdff:1::1:1/126 | fdff:1::1:2 | 65002  
router-2 | if-tunnel-b-to-a-if-0_ipv4 | 169.254.0.2/30 | 169.254.0.1 | 65001  
router-2 | if-tunnel-b-to-a-if-0_ipv6 | fdff:1::2/126 | fdff:1::1 | 65001  
router-2 | if-tunnel-b-to-a-if-1_ipv4 | 169.254.1.2/30 | 169.254.1.1 | 65001  
router-2 | if-tunnel-b-to-a-if-1_ipv6 | fdff:1::1:2/126 | fdff:1::1:1 | 65001  
  
To create Cloud Router interfaces and BGP peers, complete the following command sequence.

  1. **Create both interfaces and BGP peers on` ROUTER_NAME_1` for the tunnel `TUNNEL_NAME_GW1_IF0`**.

The two interfaces connect `TUNNEL_NAME_GW1_IF0` on `interface 0` of `GW_1` to `interface 0` of `GW_2`.

In the commands, replace the following:

     * `ROUTER_1_INTERFACE_NAME_0_ipv4` and `ROUTER_1_INTERFACE_NAME_0_ipv6`: names for the Cloud Router interfaces; using names related to `TUNNEL_NAME_GW1_IF0` is helpful
     * `IP_VERSION`: IPv6 version of the interface, either `IPV6` or `IPV4`. This parameter is only required if you want Google Cloud to assign the IPv6 address automatically for an interface. If you are manually assigning an IPv6 address to this interface, you can omit this flag.
     * `IPV4_ADDRESS_1` and `IPV6_ADDRESS_1`: a BGP IP address from the `169.254.0.0/16` or `fdff:1::/64` address range that's not already in use; this example uses `169.254.0.1` and `fdff:1::1`. If you omit this flag and don't manually assign a BGP IP address, Google Cloud automatically assigns an address for you.
     * `MASK_LENGTH`: when you specify a BGP IPv6 address for an interface, specify `30` because the Cloud Router must use a unique `/30` CIDR from the same `169.254.0.0/16` IPv4 address range. When specifying an IPv6 address for an interface, specify a mask length of `126`.
     * `PEER_NAME_GW1_IF0_ipv4` and `PEER_NAME_GW1_IF0_ipv6`: names describing the IPv4 and IPv6 BGP peers; using names related to `TUNNEL_NAME_GW1_IF0` is helpful
     * `PEER_IPV4_ADDRESS_1` and `PEER_IPV6_ADDRESS_1`: a BGP address from the `169.254.0.0/16` or `fdff:1::/64` IPv6 address range that's not already in use; this example uses `169.254.0.2` and `fdff:1::2`. If you did not previously assign specific BGP addresses for `IPV4_ADDRESS_1` and `IPV6_ADDRESS_1`, omit these options as well and Google Cloud automatically assigns a matching BGP peer IP addresses for you. If you manually specified `IPV4_ADDRESS_1` and `IPV6_ADDRESS_1`, you must also manually configure these options.
     * `PEER_ASN_2`: the ASN number used for all interfaces on `ROUTER_NAME_2`; this example uses ASN number `65002`

**Optional: Assign a BGP identifier range**

When you add the first interface with an IPv6 address to a Cloud Router, a BGP identifier range is automatically assigned to the Cloud Router. If you prefer to define your own BGP identifier range for a Cloud Router, you can create your own range. You can also modify this range later.

For more information, see [Configure the BGP identifier range for a Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configure-bgp-identifier).

###  Automatic 

**Create Cloud Router interfaces for` TUNNEL_NAME_GW1_IF0`**

To create an interface with an automatically configured BGP IPv4 address, run the following command:
    
    gcloud compute routers add-interface ROUTER_NAME_1 \
      --interface-name=ROUTER_1_INTERFACE_NAME_0_ipv4 \
      --vpn-tunnel=TUNNEL_NAME_GW1_IF0 \
      --region=REGION \
      --ip-version=IPV4
    

To create an interface with an automatically configured BGP IPv6 address, run the following command:
    
    gcloud compute routers add-interface ROUTER_NAME_1 \
      --interface-name=ROUTER_1_INTERFACE_NAME_0_ipv6 \
      --vpn-tunnel=TUNNEL_NAME_GW1_IF0 \
      --region=REGION \
      --ip-version=IPV6
    

**Create BGP peers for` TUNNEL_NAME_GW1_IF0`**

The following example command creates the IPv4 BGP peer:
    
    gcloud compute routers add-bgp-peer ROUTER_NAME_1 \
      --peer-name=PEER_NAME_GW1_IF0_ipv4 \
      --interface=ROUTER_1_INTERFACE_NAME_0_ipv4 \
      --peer-asn=PEER_ASN_2 \
      --region=REGION \
    

The following example command creates the IPv6 BGP peer:
    
    gcloud compute routers add-bgp-peer ROUTER_NAME_1 \
      --peer-name=PEER_NAME_GW1_IF0_ipv6 \
      --interface=ROUTER_1_INTERFACE_NAME_0_ipv6 \
      --peer-asn=PEER_ASN_2 \
      --region=REGION
    

By creating two interfaces and BGP peers, you run two parallel IPv4 and IPv6 BGP sessions in the same tunnel.

You can't use MP-BGP in this configuration.

###  Manual 

**Create Cloud Router interfaces for` TUNNEL_NAME_GW1_IF0`**

To create an interface with a manually configured BGP IPv4 address, run the following command:
    
    gcloud compute routers add-interface ROUTER_NAME_1 \
      --interface-name=ROUTER_1_INTERFACE_NAME_0_ipv4 \
      --ip-address=IPV4_ADDRESS_1 \
      --mask-length=30 \
      --vpn-tunnel=TUNNEL_NAME_GW1_IF0 \
      --region=REGION
    

To create an interface with a manually configured BGP IPv6 address, run the following command:
    
    gcloud compute routers add-interface ROUTER_NAME_1 \
      --interface-name=ROUTER_1_INTERFACE_NAME_0_ipv6 \
      --ip-address=IPV6_ADDRESS_1 \
      --mask-length=MASK_LENGTH \
      --vpn-tunnel=TUNNEL_NAME_GW1_IF0 \
      --region=REGION \
    

**Create BGP peers for` TUNNEL_NAME_GW1_IF0`**

The following example command creates the IPv4 BGP peer:
    
    gcloud compute routers add-bgp-peer ROUTER_NAME_1 \
      --peer-name=PEER_NAME_GW1_IF0_ipv4 \
      --interface=ROUTER_1_INTERFACE_NAME_0_ipv4 \
      --peer-ip-address=PEER_IPV4_ADDRESS_1 \
      --peer-asn=PEER_ASN_2 \
      --region=REGION \
    

The following command creates the IPv6 BGP peer:
    
    gcloud compute routers add-bgp-peer ROUTER_NAME_1 \
      --peer-name=PEER_NAME_GW1_IF0_ipv6 \
      --interface=ROUTER_1_INTERFACE_NAME_0_ipv6 \
      --peer-ip-address=PEER_IPV6_ADDRESS_1 \
      --peer-asn=PEER_ASN_2 \
      --region=REGION
    

By creating two interfaces and BGP peers, you run two parallel IPv4 and IPv6 BGP sessions in the same tunnel.

You can't use MP-BGP in this configuration.

  2. **Create both interfaces and BGP peers on` ROUTER_NAME_1` for the tunnel `TUNNEL_NAME_GW1_IF1`**.

The two interfaces connect `TUNNEL_NAME_GW1_IF1` on `interface 1` of `GW_1` to `interface 1` of `GW_2`.

In the following commands, replace the following:

     * `ROUTER_1_INTERFACE_NAME_1_ipv4` and `ROUTER_1_INTERFACE_NAME_1_ipv6`: names for the Cloud Router interfaces; using names related to `TUNNEL_NAME_GW1_IF1` is helpful
     * `IP_VERSION`: the version of the interface, either `IPV6` or `IPV4`. If unspecified, the default is `IPV4`. This parameter is only required if you want Google Cloud to assign an IPv6 address automatically to an interface. If you are manually assigning an IPv4 or IPv6 address to this interface, you can omit this flag.
     * `IPV4_ADDRESS_2` or `IPV6_ADDRESS_2`: a BGP IPv4 or IPv6 address from the `169.254.0.0/16` or `fdff:1::/64` IPv6 address range that's not already in use; this example uses `169.254.1.1` and or `fdff:1::1:1`. If you omit this flag and don't manually assign a BGP IPv4 or IPv6 address, Google Cloud automatically assigns an address for you.
     * `MASK_LENGTH`: when you specify an IPv4 address for an interface, specify `30` because the Cloud Router must use a unique `/30` CIDR from the same `169.254.0.0/16` IPv4 address range. When you specify an IPv6 address for an interface, specify a mask length of `64`.
     * `PEER_NAME_GW1_IF1_ipv4` and `PEER_NAME_GW1_IF0_ipv6`: names describing the IPv4 and IPv6 BGP peers; using names related to `TUNNEL_NAME_GW1_IF1` is helpful
     * `PEER_IPV4_ADDRESS_2` or `PEER_IPV6_ADDRESS_2`: a BGP IPv4 or IPv6 address from the `169.254.0.0/16` or `fdff:1::/64` IPv6 address range that's not already in use; this example uses `169.254.1.2` and `fdff:1::1:2`. If you did not specifically assign an IPv4 or IPv6 address, `IPV4_ADDRESS_2` or `IPV6_ADDRESS_2`, omit this option and Google Cloud automatically assigns a matching BGP peer IPv4 or IPv6 address for you. If you manually specified `IPV4_ADDRESS_2` or `IPV6_ADDRESS_2`, you must also manually configure this option.
     * `PEER_ASN_2`: the ASN number used for all interfaces on the other Cloud Router `ROUTER_NAME_2`; this example uses ASN number `65002`
     * `AUTHENTICATION_KEY_2`: the secret key to use for MD5 authentication on `PEER_NAME_GW1_IF1`; for more information about this optional feature, see [Use MD5 authentication](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication)

###  Automatic 

**Create Cloud Router interfaces for` TUNNEL_NAME_GW1_IF1`**

To create an interface with an automatically configured IPv4 address, run the following command:
    
    gcloud compute routers add-interface ROUTER_NAME_1 \
      --interface-name=ROUTER_1_INTERFACE_NAME_1_ipv4 \
      --vpn-tunnel=TUNNEL_NAME_GW1_IF1 \
      --region=REGION \
      --ip-version=IPV4
    

To create an interface with an automatically configured IPv6 address, run the following command:
    
    gcloud compute routers add-interface ROUTER_NAME_1 \
      --interface-name=ROUTER_1_INTERFACE_NAME_1_ipv6 \
      --vpn-tunnel=TUNNEL_NAME_GW1_IF1 \
      --region=REGION \
      --ip-version=IPV6
    

**Create BGP peers for` TUNNEL_NAME_GW1_IF1`**

The following example command creates an IPv4 BGP peer:
    
    gcloud compute routers add-bgp-peer ROUTER_NAME_1 \
      --peer-name=PEER_NAME_GW1_IF1_ipv4 \
      --interface=ROUTER_1_INTERFACE_NAME_1_ipv4 \
      --peer-ip-address=PEER_IPV4_ADDRESS_2 \
      --peer-asn=PEER_ASN_2 \
      --region=REGION
    

The following example command creates an IPv6 BGP peer:
    
    gcloud compute routers add-bgp-peer ROUTER_NAME_1 \
      --peer-name=PEER_NAME_GW1_IF1_ipv6 \
      --interface=ROUTER_1_INTERFACE_NAME_1_ipv6 \
      --peer-ip-address=PEER_IPV6_ADDRESS_2 \
      --peer-asn=PEER_ASN_2 \
      --region=REGION
    

By creating two interfaces and BGP peers, you run two parallel IPv4 and IPv6 BGP sessions in the same tunnel.

You can't use MP-BGP in this configuration.

###  Manual 

**Create Cloud Router interfaces for` TUNNEL_NAME_GW1_IF1`**

To create an interface with a manually configured IPv4 address, run the following command:
    
    gcloud compute routers add-interface ROUTER_NAME_1 \
      --interface-name=ROUTER_1_INTERFACE_NAME_1_ipv4 \
      --ip-address=IPV4_ADDRESS_2 \
      --mask-length=30 \
      --vpn-tunnel=TUNNEL_NAME_GW1_IF1 \
      --region=REGION
    

To create an interface with a manually configured IPv6 address, run the following command:
    
    gcloud compute routers add-interface ROUTER_NAME_1 \
      --interface-name=ROUTER_1_INTERFACE_NAME_1_ipv6 \
      --ip-address=IPV6_ADDRESS_2 \
      --mask-length=MASK_LENGTH \
      --vpn-tunnel=TUNNEL_NAME_GW1_IF1 \
      --region=REGION
    

**Create BGP peers for` TUNNEL_NAME_GW1_IF1`**

The following example command creates an IPv4 BGP peer:
    
    gcloud compute routers add-bgp-peer ROUTER_NAME_1 \
      --peer-name=PEER_NAME_GW1_IF1_ipv4 \
      --interface=ROUTER_1_INTERFACE_NAME_1_ipv4 \
      --peer-ip-address=PEER_IPV4_ADDRESS_2 \
      --peer-asn=PEER_ASN_2 \
      --region=REGION
    

The following example command creates an IPv6 BGP peer:
    
    gcloud compute routers add-bgp-peer ROUTER_NAME_1 \
        --peer-name=PEER_NAME_GW1_IF1_ipv6 \
        --interface=ROUTER_1_INTERFACE_NAME_1_ipv6 \
        --peer-ip-address=PEER_IPV6_ADDRESS_2 \
        --peer-asn=PEER_ASN_2 \
        --region=REGION
    

By creating two interfaces and BGP peers, you run two parallel IPv4 and IPv6 BGP sessions in the same tunnel.

You can't use MP-BGP in this configuration.

  3. **Verify the settings for` ROUTER_NAME_1`**:
         
         gcloud compute routers describe ROUTER_NAME_1 \
             --region=REGION
         

The command output is similar to the following example:
         
         bgp:
           advertisemode: DEFAULT
           asn: 65001
           keepaliveInterval: 20
         bgpPeers:
         — bfd:
               minReceiveInterval: 1000
               minTransmitInterval: 1000
               mode: DISABLED
               multiplier: 5
               sessionInitializationMode: DISABLED
           enable: 'TRUE'
           interfaceName: if-tunnel-a-to-b-if-0_ipv4
           ipAddress: 169.254.0.1
           name: bgp-peer-tunnel-a-to-b-if-0_ipv4
           peerAsn: 65002
           peerIpAddress: 169.254.0.2
         — bfd:
               minReceiveInterval: 1000
               minTransmitInterval: 1000
               mode: DISABLED
               multiplier: 5
               sessionInitializationMode: DISABLED
           enable: 'TRUE'
           interfaceName: if-tunnel-a-to-b-if-1_ipv4
           ipAddress: 169.254.1.1
           name: bgp-peer-tunnel-a-to-b-if-1_ipv4
           peerAsn: 65002
           peerIpAddress: 169.254.1.2
         — bfd:
               minReceiveInterval: 1000
               minTransmitInterval: 1000
               mode: DISABLED
               multiplier: 5
               sessionInitializationMode: DISABLED
           enable: 'TRUE'
           interfaceName: if-tunnel-a-to-b-if-0_ipv6
           ipAddress: fdff:1::1
           name: bgp-peer-tunnel-a-to-b-if-0_ipv6
           peerAsn: 65002
           peerIpAddress: fdff:1::2
         — bfd:
               minReceiveInterval: 1000
               minTransmitInterval: 1000
               mode: DISABLED
               multiplier: 5
               sessionInitializationMode: DISABLED
           enable: 'TRUE'
           interfaceName: if-tunnel-a-to-b-if-1_ipv6
           ipAddress: fdff:1::1
           name: bgp-peer-tunnel-a-to-b-if-1_ipv6
           peerAsn: 65002
           peerIpAddress: fdff:1::2
         creationTimestamp: '2021-10-19T14:31:52.639-07:00'
         id: '4047683710114914215'
         interfaces:
         — ipRange: 169.254.0.1/30
           linkedVpnTunnel: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/vpnTunnels/tunnel-a-to-b-if-0
           name: if-tunnel-a-to-b-if-0
         — ipRange: 169.254.1.1/30
           linkedVpnTunnel: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/vpnTunnels/tunnel-a-to-b-if-0
           name: if-tunnel-a-to-b-if-0
         — ipRange: fdff:1::1/126
           linkedVpnTunnel: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/vpnTunnels/tunnel-a-to-b-if-1
           name: if-tunnel-a-to-b-if-1
         — ipRange: fdff:1::1:1/126
           linkedVpnTunnel: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/vpnTunnels/tunnel-a-to-b-if-1
           name: if-tunnel-a-to-b-if-1
         kind: compute#router
         name: router-a
         network: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/network-a
         region: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1
         selfLink: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/routers/router-a
         

  4. **Create both interfaces and BGP peers on` ROUTER_NAME_2` for the tunnel `TUNNEL_NAME_GW2_IF0`**.

The two interfaces connect `TUNNEL_NAME_GW2_IF0` on `interface 0` of `GW_2` to `interface 0` of `GW_1`.

You must configure the interface and BGP peering addresses on this Cloud Router manually because the corresponding addresses have already been configured on the other Cloud Router,`ROUTER_NAME_1`.

In the commands, replace the following:

     * `ROUTER_2_INTERFACE_NAME_0_ipv4` and `ROUTER_2_INTERFACE_NAME_0<_ipv6`: Cloud Router interface names; using names related to `TUNNEL_NAME_GW2_IF0` is helpful
     * `IPV4_ADDRESS_3` and `IPV6_ADDRESS_3`: the BGP IPv4 and IPv6 addresses used previously for this gateway and interface. If you automatically assigned the peer IPv4 and IPv6 addresses when you created the interfaces and BGP peers for `TUNNEL_NAME_GW1_IF0` on `ROUTER_NAME_1`, then you must specify the allocated addresses as `IPV4_ADDRESS_3` and `IPV6_ADDRESS_3`. To find out which addresses have been allocated by Google Cloud, run the `gcloud compute routers describe ROUTER_NAME_1` command. In the output for the BGP peers, use the values that appear in the `peerIpAddress` field. This example uses `169.254.0.2` and `fdff:1::2`.
     * `MASK_LENGTH`: for an interface with an IPv4 address, specify `30` because the Cloud Router must use a unique `/30` CIDR from the same `169.254.0.0/16` IPv4 address range. For an interface with an IPv6 address, specify a mask length of `64`.
     * `PEER_NAME_GW2_IF0_ipv4` and `PEER_NAME_GW2_IF0_ipv6`: a name describing the BGP peer; using a name related to `TUNNEL_NAME_GW2_IF0` is helpful
     * `PEER_IPV4_ADDRESS_3` and `PEER_IPV6_ADDRESS_3`: the BGP IPv4 or IPv6 addresses used previously when you configured the first gateway and interface. Run `gcloud compute routers describe ROUTER_NAME_1`, and use the values that appear in the `ipAddress` field for the BGP peers you created for `TUNNEL_NAME_GW1_IF0`. This example uses `169.254.0.1` and `fdff:1::1`.
     * `PEER_ASN_1`: the ASN number used for all interfaces on `ROUTER_NAME_1` and that was set previously; this example uses ASN number `65001`

**Create Cloud Router interfaces for` TUNNEL_NAME_GW2_IF0`**

To create an interface and manually configure its IPv4 address, run the following command:
    
    gcloud compute routers add-interface ROUTER_NAME_2 \
        --interface-name=ROUTER_2_INTERFACE_NAME_0 \
        --ip-address=IPV4_ADDRESS_3 \
        --mask-length=MASK_LENGTH \
        --vpn-tunnel=TUNNEL_NAME_GW2_IF0 \
        --region=REGION
    

To create an interface and manually configure its IPv6 address, run the following command:
    
    gcloud compute routers add-interface ROUTER_NAME_1 \
        --interface-name=ROUTER_2_INTERFACE_NAME_0 \
        --ip-address=IPV6_ADDRESS_3 \
        --mask-length=MASK_LENGTH \
        --vpn-tunnel=TUNNEL_NAME_GW2_IF0 \
        --region=REGION \
    

**Create BGP peers for` TUNNEL_NAME_GW2_IF0`**

The following example command creates the IPv4 BGP peer:
    
    gcloud compute routers add-bgp-peer ROUTER_NAME_2 \
        --peer-name=PEER_NAME_GW2_IF0_ipv4 \
        --interface=ROUTER_2_INTERFACE_NAME_0_ipv4 \
        --peer-ip-address=PEER_IPV4_ADDRESS_3 \
        --peer-asn=PEER_ASN_1 \
        --region=REGION
    

The following example command creates the IPv6 BGP peer:
    
    gcloud compute routers add-bgp-peer ROUTER_NAME_2 \
      --peer-name=PEER_NAME_GW2_IF0_ipv6 \
      --interface=ROUTER_2_INTERFACE_NAME_0_ipv6 \
      --peer-ip-address=PEER_IPV6_ADDRESS_3 \
      --peer-asn=PEER_ASN_1 \
      --region=REGION
    

By creating two interfaces and BGP peers, you run two parallel IPv4 and IPv6 BGP sessions in the same tunnel.

You can't use MP-BGP in this configuration.

  5. **Create both interfaces and BGP peers on` ROUTER_NAME_2` for the tunnel `TUNNEL_NAME_GW2_IF1`**.

The two interfaces connect `TUNNEL_NAME_GW2_IF0` on `interface 0` of `GW_2` to `interface 0` of `GW_1`.

You must configure the interface and BGP peering addresses on this Cloud Router manually because the corresponding addresses have already been configured on the other Cloud Router,`ROUTER_NAME_1`.

The two interfaces connect `TUNNEL_NAME_GW2_IF1` on `interface 1` of `GW_2` to `interface 1` of `GW_1`.

In the following commands, replace the following:

     * `ROUTER_2_INTERFACE_NAME_1_ipv4` and `ROUTER_2_INTERFACE_NAME_1_ipv6`: names for the Cloud Router interfaces; using names related to `TUNNEL_NAME_GW2_IF1` is helpful
     * `IPV4_ADDRESS_4` and `IPV6_ADDRESS_4`: the BGP IPv4 and IPv6 addresses used previously for this gateway and interface. If you automatically assigned the peer BGP IP address when you created the interface and BGP peer for `TUNNEL_NAME_GW1_IF1` on `ROUTER_NAME_1`, then you must manually specify these allocated addresses as `IPV4_ADDRESS_4` and `IPV6_ADDRESS_4`. To find out which addresses have been allocated by Google Cloud, run the `gcloud compute routers describe ROUTER_NAME_1` command. In the output for the BGP peer, use the values that appear in the `peerIpAddress` field. This example uses `169.254.1.2` and `fdff:1::1:2`.
     * `MASK_LENGTH`: for an interface with an IPv4 address, specify `30` because the Cloud Router must use a unique `/30` CIDR from the same `169.254.0.0/16` IPv4 address range. For an interface with an IPv6 address, specify a mask length of `64`.
     * `PEER_NAME_GW2_IF1_ipv4` and `PEER_NAME_GW2_IF1_ipv6`: a name describing the BGP peer; using a name related to `TUNNEL_NAME_GW2_IF1` is helpful
     * `PEER_IPV4_ADDRESS_4` and `PEER_IPV6_ADDRESS_4`: the IP address you specified as `IPV4_ADDRESS_2` and `IPV6_ADDRESS_2` and when you configured the first gateway and interface. Run `gcloud compute routers describe ROUTER_NAME_1`, and use the values that appear in the `ipAddress` field for the BGP peer you created for `TUNNEL_NAME_GW2_IF1`. This example uses `169.254.1.1` and `fdff:1::1:1`.
     * `PEER_ASN_1`: the ASN number used for all interfaces on `ROUTER_NAME_1` and that was set previously; this example uses ASN number `65001`

**Create Cloud Router interfaces for` TUNNEL_NAME_GW2_IF1`**

To create an interface and manually configure its IPv4 address, run the following command:
    
    gcloud compute routers add-interface ROUTER_NAME_2 \
      --interface-name=ROUTER_2_INTERFACE_NAME_1 \
      --ip-address=IPV4_ADDRESS_4 \
      --mask-length=MASK_LENGTH \
      --vpn-tunnel=TUNNEL_NAME_GW2_IF1 \
      --region=REGION
    

To create an interface and manually configure its IPv6 address, run the following command:
    
    gcloud compute routers add-interface ROUTER_NAME_2 \
        --interface-name=ROUTER_2_INTERFACE_NAME_1 \
        --ip-address=IPV6_ADDRESS_4 \
        --mask-length=MASK_LENGTH \
        --vpn-tunnel=TUNNEL_NAME_GW2_IF1 \
        --region=REGION
    

**Create BGP peers for` TUNNEL_NAME_GW2_IF1`**

The following example command creates the IPv4 BGP peer:
    
    gcloud compute routers add-bgp-peer ROUTER_NAME_2  \
      --peer-name=PEER_NAME_GW2_IF1_ipv4 \
      --interface=ROUTER_2_INTERFACE_NAME_1_ipv4 \
      --peer-ip-address=PEER_IPV4_ADDRESS_4 \
      --peer-asn=PEER_ASN_1 \
      --region=REGION
    

The following example command creates the IPv6 BGP peer:
    
    gcloud compute routers add-bgp-peer ROUTER_NAME_2 \
      --peer-name=PEER_NAME_GW2_IF1_ipv6 \
      --interface=ROUTER_2_INTERFACE_NAME_1_ipv6 \
      --peer-ip-address=PEER_IPV6_ADDRESS_4 \
      --peer-asn=PEER_ASN_1 \
      --region=REGION
    

  6. **Verify the settings for` ROUTER_NAME_2`**:
         
         gcloud compute routers describe ROUTER_NAME_2  \
           --region=REGION
         

The command output looks similar to the following example:
         
         bgp:
           advertisemode: DEFAULT
           asn: 65002
           keepaliveInterval: 20
         bgpPeers:
         — bfd:
               minReceiveInterval: 1000
               minTransmitInterval: 1000
               mode: DISABLED
               multiplier: 5
               sessionInitializationMode: DISABLED
           enable: 'TRUE'
           interfaceName: if-tunnel-b-to-a-if-0_ipv4
           ipAddress: 169.254.0.2
           name: bgp-peer-tunnel-b-to-a-if-0_ipv4
           peerAsn: 65002
           peerIpAddress: 169.254.0.1
         — bfd:
               minReceiveInterval: 1000
               minTransmitInterval: 1000
               mode: DISABLED
               multiplier: 5
               sessionInitializationMode: DISABLED
           enable: 'TRUE'
           interfaceName: if-tunnel-b-to-a-if-1_ipv4
           ipAddress: 169.254.1.2
           name: bgp-peer-tunnel-b-to-a-if-1_ipv4
           peerAsn: 65001
           peerIpAddress: 169.254.1.1
         — bfd:
               minReceiveInterval: 1000
               minTransmitInterval: 1000
               mode: DISABLED
               multiplier: 5
               sessionInitializationMode: DISABLED
           enable: 'TRUE'
           interfaceName: if-tunnel-b-to-a-if-0_ipv6
           ipAddress: fdff:1::2
           name: bgp-peer-tunnel-b-to-a-if-0_ipv6
           peerAsn: 65001
           peerIpAddress: fdff:1::1
         — bfd:
               minReceiveInterval: 1000
               minTransmitInterval: 1000
               mode: DISABLED
               multiplier: 5
               sessionInitializationMode: DISABLED
           enable: 'TRUE'
           interfaceName: if-tunnel-b-to-a-if-1_ipv6
           ipAddress: fdff:1::2
           name: bgp-peer-tunnel-b-to-a-if-1_ipv6
           peerAsn: 65001
           peerIpAddress: fdff:1::1
         creationTimestamp: '2021-10-19T14:31:52.639-07:00'
         id: '4047683710114914215'
         interfaces:
         — ipRange: 169.254.0.2/30
           linkedVpnTunnel: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/vpnTunnels/tunnel-b-to-a-if-0
           name: if-tunnel-b-to-a-if-0
         — ipRange: 169.254.1.2/30
           linkedVpnTunnel: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/vpnTunnels/tunnel-b-to-a-if-0
           name: if-tunnel-b-to-a-if-0
         — ipRange: fdff:1::2/126
           linkedVpnTunnel: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/vpnTunnels/tunnel-b-to-a-if-1
           name: if-tunnel-b-to-a-if-1
         — ipRange: fdff:1::1:2/126
           linkedVpnTunnel: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/vpnTunnels/tunnel-b-to-a-if-1
           name: if-tunnel-b-to-a-if-1
         kind: compute#router
         name: router-b
         network: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/network-b
         region: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1
         selfLink: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/routers/router-b
         




###  API 

  1. To create multiple Cloud Router interfaces, make either a `PATCH` or `UPDATE` request by using the [`routers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/routers/patch) or the [`routers.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/routers/update). `PATCH` updates only the parameters that you include. `UPDATE` updates all parameters for Cloud Router.

The BGP address ranges that you specify must be unique among all Cloud Routers in all regions of a VPC network.

Repeat this step and command for each VPN tunnel defined on each HA VPN gateway. For an HA VPN gateway to HA VPN deployment, this means four HA VPN tunnel configurations.
         
         PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
         {
         "interfaces": [
           {
             "name": "if-tunnel-a-to-b-if-0_ipv4",
             "linkedVpnTunnel": "ha-vpn-gw-a-tunnel-0",
             "ipRange": "169.254.0.1/30"
             },
             {
             "name": "if-tunnel-a-to-b-if-0_ipv6",
             "linkedVpnTunnel": "ha-vpn-gw-a-tunnel-0",
             "ipRange": "fdff:1::1/126"
             }
           ]
         }
         

The following example adds an interface with an IPv4 address and an interface with an IPv6 address to the same `linkedVpnTunnel`. The command automatically assigns IPv4 and IPv6 addresses to the interfaces:
         
         PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
         {
         "interfaces": [
           {
             "name": "if-tunnel-a-to-b-if-0_ipv4",
             "linkedVpnTunnel": "ha-vpn-gw-a-tunnel-0",
             "ipVersion": "IPV4"
             },
             {
             "name": "if-tunnel-a-to-b-if-0_ipv6",
             "linkedVpnTunnel": "ha-vpn-gw-a-tunnel-0",
             "ipVersion": "IPV6"
             }
         ]
         }
         

  2. To add BGP peers to the Cloud Router for each VPN tunnel, make either a `PATCH` or `UPDATE` request by using the [`routers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/routers/patch) or the [`routers.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/routers/update). Repeat this command for each VPN tunnel, changing all options as needed.

For example:
         
         PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
         {
         "bgpPeers": [
         {
           "interfaceName": "if-tunnel-a-to-b-if-0_ipv4",
           "ipAddress": "169.254.0.1",
           "name": "bgp-peer-tunnel-a-to-b-if-0_ipv4",
           "peerAsn": 65002,
           "peerIpAddress": "169.254.0.2",
           "advertiseMode": "DEFAULT"
           },
           {
           "interfaceName": "if-tunnel-a-to-b-if-0_ipv6",
           "ipAddress": fdff:1::1",
           "name": "bgp-peer-tunnel-a-to-b-if-0_ipv6",
           "peerAsn": 65002,
           "peerIpAddress": "fdff:1::2",
           "advertiseMode": "DEFAULT"
           }
         ]
         }
         




### Verify the configuration

###  Console 

To verify the configuration, follow these steps.

  1. In the Google Cloud console, go to the **Cloud VPN** tunnels page.

[Go to Cloud VPN tunnels](https://console.cloud.google.com/hybrid/vpn/list?&tab=tunnels)

  2. View the VPN tunnel status and the BGP session status.

If your configuration is correct, the VPN tunnel status is `Established` and the BGP session status is `BGP established`.

For more information about the **VPN tunnel status** and the **BGP session states** , see [Interpret tunnel status messages](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/checking-vpn-status#tunnel-status-messages) and [BGP session states](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bgp-states).




###  gcloud 

  * To verify the HA VPN tunnel configuration, see [Check HA VPN tunnels](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/checking-vpn-status#checking-ha-tunnels).
  * To verify the Cloud Router configuration, see [View router details](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details).



###  API 

To verify the Cloud Router configuration, make a `GET` request by using the [`routers.getRouterStatus`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/getRouterStatus) method, and use an empty request body:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers
    

To learn about how to troubleshoot your Cloud VPN connection, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/vpn/support/troubleshooting).

### Create an additional tunnel on a single-tunnel gateway

###  Console 

To receive a 99.99% uptime SLA, configure a tunnel on each HA VPN interface on each side of an HA VPN-to-HA VPN gateway configuration.

If you configured one tunnel on an HA VPN gateway to another HA VPN gateway but want to receive a 99.99% uptime SLA, you must configure a second tunnel.

To configure a second tunnel, follow the steps at [Add a tunnel from an HA VPN gateway to another HA VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/adding-a-tunnel#add-tunnel-from-ha-vpn-to-ha-vpn).

## Set the base advertised route priority (optional)

The BGP sessions that you create let each Cloud Router advertise routes to peer networks. The advertisements use _unmodified base priorities_.

Use the configuration documented in Create two fully configured HA VPN gateways that connect to each other for _active-active routing configurations_ where the advertised route priorities of the two tunnels on both sides match. Omitting the advertised route priority (`--advertised-route-priority`) results in the same advertised route priorities to both BGP peers.

For _active-passive routing configurations_ , you can control the advertised route priority of the `to Google Cloud` routes that Cloud Router shares with your peer VPN gateway by setting the advertised route priority (`--advertised-route-priority`) when adding or updating a BGP peer. To create an active-passive configuration, set a higher advertised route priority for one BGP session and its corresponding VPN tunnel than for the other BGP session and VPN tunnel.

For more information about the base advertised route priority, see [Advertised priority](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#advertised-priority).

You can also refine the routes that are advertised by using [Advertised routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes):

  * Add the `--advertisement-mode=CUSTOM` flag (`gcloud`) or the `advertiseMode: custom` flag (API).
  * Specify IP address ranges with the `--set-advertisement-ranges` flag (`gcloud`) or the `advertisedIpRanges` flag (API).



## Complete the configuration

Before you can use a new Cloud VPN gateway and its associated VPN tunnels, complete the following steps:

  1. [Configure firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls) in Google Cloud for your VPC networks.
  2. [Check the status of your VPN tunnels](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/checking-vpn-status). This step includes checking the high-availability configuration of your HA VPN gateway.



## What's next

  * To control which IP addresses are allowed for peer VPN gateways, see [Restrict IP addresses for peer VPN gateways](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/restrict-peer-ip-addresses).
  * To use high-availability and high-throughput scenarios or multiple subnet scenarios, see [Advanced configurations](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/advanced).
  * To help you solve common issues that you might encounter when using Cloud VPN, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/vpn/support/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
