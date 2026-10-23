---
url: https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/connect-ha-vpn-vm/
title: Connect HA VPN to Compute Engine VMs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:47.766433+00:00
---

# Connect HA VPN to Compute Engine VMs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/connect-ha-vpn-vm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud VPN ](https://docs.cloud.google.com/network-connectivity/docs/vpn)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)



Send feedback 

#  Connect HA VPN to Compute Engine VMs Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to connect an HA VPN gateway to Compute Engine virtual machine (VM) instances with external IP addresses hosted in Google Cloud.

These instructions create the following HA VPN resources:

  * An HA VPN gateway
  * A peer VPN gateway
  * A pair of VPN tunnels from the peer VPN gateway to each VM instance to help ensure high availability



For more information about Cloud VPN, see the following resources:

  * For diagrams of this topology, see [HA VPN to Compute Engine VM instances in multiple zones](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/topologies#vm-multi-zone) and [HA VPN to a Compute Engine VM instance](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/topologies#vm-single-zone).

  * For best practices to consider before setting up Cloud VPN, see [Best practices](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/best-practices).

  * For more information about Cloud VPN, see the [Cloud VPN overview](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview).

  * For definitions of terms used on this page, see [Key terms](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/key-terms).




## Before you begin

  * Review information about how [dynamic routing](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/choosing-networks-routing#dynamic-routing) works in Google Cloud.

  * Ensure that your peer VPN gateway supports Border Gateway Protocol (BGP).

  * Ensure that you have one or two Compute Engine VMs with external IP addresses.




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

Before creating an HA VPN gateway and tunnel pair, create a Virtual Private Cloud (VPC) network and at least one subnet in the region where the HA VPN gateway resides:

  * To create a custom mode VPC network (recommended), see [Creating a custom mode VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#create-custom-network).
  * To create subnets, see [Working with subnets](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#subnet-rules).



To enable IPv6 for HA VPN gateways, you must enable the allocation of IPv6 internal addresses when you create the VPC. In addition, you must configure the subnets to use IPv6 internal addresses.

You must also configure IPv6 on the VMs in the subnet.

  * To create a custom mode VPC network with internal IPv6 addresses, see [Create a custom mode VPC network with at least one dual stack subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#create-network-dual).
  * To create a subnet with IPv6 enabled, see [Add a dual-stack subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#add-subnet-ipv6).
  * To enable IPv6 in an existing subnet, see [Convert an IPv4 subnet to a dual stack subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#subnet-enable-ipv6).
  * To create VMs with IPv6 enabled, see [Configuring IPv6 for instances and instance templates](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address).



The VPC subnet must be configured to use internal IPv6 addresses. When you use the gcloud CLI, you configure the subnet with the `--ipv6-access-type=INTERNAL` flag. Cloud Router does not dynamically advertise routes for subnets that are configured to use external IPv6 addresses (`--ipv6-access-type=EXTERNAL`).

For information about using internal IPv6 ranges in your VPC network and subnets, see [Internal IPv6 specifications](https://docs.cloud.google.com/vpc/docs/subnets#internal-ipv6).

The examples in this document also use [VPC global dynamic routing mode](https://docs.cloud.google.com/vpc/docs/vpc#routing_for_hybrid_networks), which behaves in the following way:

  * All instances of Cloud Router apply the `to on-premises` routes that they learn to all subnets of the VPC network.
  * Routes to all subnets in the VPC network are shared with on-premises routers.



## Create an HA VPN gateway and tunnels to Compute Engine VM instances

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

**Note:** After you create an HA VPN gateway, you cannot modify its stack type. If you need a different stack type for an existing HA VPN gateway, you must delete and recreate the gateway. 

To support IPv6 traffic, HA VPN gateways must use either the `IPv4 and IPv6 (dual-stack)` or `IPv6 (single-stack)` configuration. To temporarily disable IPv6 traffic without deleting your gateway, [ disable IPv6 route exchange in the IPv4 BGP session](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-mp-bgp#disable-ipv6-bgp) or [ disable the IPv6 session](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/disabling-removing-bgp#disable_a_bgp_session) that you established for the HA VPN tunnels. 

###  Console 

To create a VPN connection for the first time, use the VPN setup wizard. The **VPN setup wizard** includes all required configuration steps for creating an HA VPN gateway, a peer VPN gateway resource, tunnels, and BGP sessions.

**Create Cloud HA VPN gateway**

  1. In the Google Cloud console, go to the **VPN** page.

[Go to VPN](https://console.cloud.google.com/hybrid/vpn/list)

     1. If you are creating a gateway for the first time, click **Create VPN connection**.
     2. If you have existing Cloud VPN resources, click **VPN setup wizard**.
  2. Select **High-availability (HA) VPN**.

  3. Click **Continue**.

  4. Specify a **VPN gateway name**.

  5. In the **Network** list, select an existing network or the default network.

  6. In the **Region** list, select the same region where your Compute Engine VMs are located.

  7. Select a stack type for the VPN gateway, either **IPv4 (single-stack)** or **IPv4 and IPv6 (dual-stack)**.

  8. Click **Create and continue**.




The console page displays the gateway information. Two external IP addresses are automatically allocated for each of your gateway interfaces. For future configuration steps, make note of the details of your gateway configuration.

**Add VPN tunnels**

**Important:** You can create a pair of tunnels at once. To create a second pair, use the wizard after creating the first pair.

  1. In the **Peer VPN gateway** list, select **Compute Engine VMs with external IP addresses**.
  2. In the **Peer VPN gateway name** list, choose an existing peer gateway or click **Create a new peer VPN gateway**.

If you choose an existing peer gateway, the Google Cloud console selects the number of tunnels to configure based on the number of peer interfaces that you configured on the peer gateway.

To create a peer gateway, complete the following steps:

     1. Specify a name for the peer VPN gateway.
     2. In the **Peer VPN gateway interfaces** section, select one or two interfaces. You can connect a pair of tunnels to each Compute Engine VM instance. For examples of this topology, see [HA VPN topologies](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/topologies).
     3. In the field for each peer VPN interface, specify the external IP address used for that interface.

In the **Cloud Router** list, select or create a **Cloud Router** by specifying the following options.

     1. To create a new Cloud Router, specify the following:
     2. A **Name**
     3. An optional **Description**
     4. A **Google ASN** for the new router

You can use any private ASN (`64512` through `65534`, `4200000000` through `4294967294`) that you are not using elsewhere in your network. The Google ASN is used for all BGP sessions on the same Cloud Router, and you cannot change the ASN later.

     1. To create the router, click **Create**.

In the **VPN tunnels** section, expand each item to fill in the details of created VPN tunnels.

     1. In the **Associated peer VPN gateway interface** section, select the peer VPN gateway interface and IP address combination that you want to associate with this tunnel and with the HA VPN interface. This interface must match the interface on your actual peer router.
     2. Specify a **Name** for the tunnel.
     3. Specify an optional **Description**.
     4. Specify the **IKE version**. We recommend IKEv2, the default setting, if your peer router supports it. To allow IPv6 traffic, you must select IKEv2.
     5. Specify an **IKE pre-shared key** by using your pre-shared key (shared secret), which must correspond with the pre-shared key for the partner tunnel that you create on your peer gateway. If you haven't configured a pre-shared key on your peer VPN gateway and want to generate one, click **Generate and copy**. Make sure that you record the pre-shared key in a secure location because it cannot be retrieved after you create your VPN tunnels.
     6. Click **Done**.
     7. On the **Create a VPN** page, repeat the tunnel creation steps for any remaining tunnel dialogs.
  3. When you have configured all tunnels, click **Create and continue**.




**Configure BGP sessions**

  1. Click **Configure BGP Session** to set up the BGP session on the Cloud Router. For information about creating BGP sessions, see [Create BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn#bgp-sessions).
  2. Click **Save BGP configuration**.



The console page refreshes and displays the information about the HA VPN gateway, peer VPN gateway, and Cloud VPN tunnel information.

###  gcloud 

**Create an HA VPN gateway**

To create an HA VPN gateway, run the following command. When the gateway is created, two external IPv4 addresses are automatically allocated, one for each gateway interface.
    
    
    gcloud compute vpn-gateways create GW_NAME \
        --network=NETWORK \
        --region=REGION \
        [--stack-type=IP_STACK]
    

Replace the following:

  * `GW_NAME`: the name of the gateway
  * `NETWORK`: the name of your Google Cloud network
  * `REGION`: the [Google Cloud region](https://docs.cloud.google.com/compute/docs/regions-zones) where you create the gateway and tunnel
  * `IP_STACK`: Optional: the IP stack to use. Specify either `IPV4_ONLY` or `IPV4_IPV6`. If you don't specify this flag, the default stack type is `IPV4_ONLY`.



The gateway that you create looks similar to the following example output. An external IPv4 address is automatically assigned to each gateway interface:
    
    
    Created [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/vpnGateways/ha-vpn-gw-a].
    NAME          INTERFACE0     INTERFACE1     NETWORK     REGION
    ha-vpn-gw-a   203.0.113.16   203.0.113.23   network-a   us-central1
    

**Create a peer VPN gateway resource**

Depending on the high availability needs, you can create one or a pair of peer VPN gateway resources.

To create the first peer VPN gateway, run the following command:
    
    
     gcloud compute external-vpn-gateways create PEER_GW_NAME1 \
         --interfaces 0=PEER_GW_IP_0,1=PEER_GW_IP_1
    

To create the second peer VPN gateway, run the following command:
    
    
    gcloud compute external-vpn-gateways create PEER_GW_NAME2 \
        --interfaces 0=PEER_GW_IP_1,1=PEER_GW_IP_0
    

Replace the following:

  * `PEER_GW_NAME1`: a name representing the first peer VPN gateway
  * `PEER_GW_NAME2`: a name representing the second peer VPN gateway
  * `PEER_GW_IP_1`: the external IP address for the first Compute Engine virtual machine
  * `PEER_GW_IP_0`: the external IP address for the second Compute Engine virtual machine



The peer VPN gateway resource that you created looks like the following example, and `PEER_GW_IP_0` and `PEER_GW_IP_1` show the external IP addresses of the Compute Engine virtual machines:
    
    
    Created [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/externalVpnGateways/peer-gw].
    NAME          INTERFACE0     INTERFACE1
    peer-gw-1   203.0.113.16   203.0.113.23
    Peer-gw-2   203.0.113.23   203.0.113.16
    

**Create a Cloud Router**

To create a Cloud Router, run the following command:
    
    
    gcloud compute routers create ROUTER_NAME \
        --region=REGION \
        --network=NETWORK \
        --asn=GOOGLE_ASN
    

Replace the following:

  * `ROUTER_NAME`: the name of the Cloud Router in the same region as the Cloud VPN gateway
  * `REGION`: the [Google Cloud region](https://docs.cloud.google.com/compute/docs/regions-zones) where you create the gateway and tunnel
  * `NETWORK`: the name of your Google Cloud network
  * `GOOGLE_ASN`: any private ASN (`64512` through `65534`, `4200000000` through `4294967294`) that you are not already using in the peer network; the Google ASN is used for all BGP sessions on the same Cloud Router, and it cannot be changed later



The output is similar to the following:
    
    
    Created [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/routers/router-a].
    NAME       REGION        NETWORK
    router-a   us-central1   network-a
    

**Add VPN tunnels**

Create four VPN tunnels, two for each interface on the HA VPN gateway. When creating VPN tunnels, specify the peer side of the VPN tunnels as the external VPN gateway that you created earlier.

One VPN tunnel must connect to `interface 0` of the external VPN gateway, and the other VPN tunnel must connect to `interface 1` of the external VPN gateway.
    
    
    gcloud compute vpn-tunnels create TUNNEL_NAME_IF0 \
        --peer-external-gateway=PEER_GW_NAME1 \
        --peer-external-gateway-interface=PEER_EXT_GW_IF0 \
        --region=REGION \
        --ike-version=IKE_VERS \
        --shared-secret=SHARED_SECRET \
        --router=ROUTER_NAME \
        --vpn-gateway=GW_NAME \
        --interface=INT_NUM_0
    
    
    
    gcloud compute vpn-tunnels create TUNNEL_NAME_IF1 \
        --peer-external-gateway=PEER_GW_NAME1 \
        --peer-external-gateway-interface=PEER_EXT_GW_IF1 \
        --region=REGION \
        --ike-version=IKE_VERS \
        --shared-secret=SHARED_SECRET \
        --router=ROUTER_NAME \
        --vpn-gateway=GW_NAME \
        --interface=INT_NUM_1
    
    
    
    gcloud compute vpn-tunnels create TUNNEL_NAME_IF2 \
        --peer-external-gateway=PEER_GW_NAME2 \
        --peer-external-gateway-interface=PEER_EXT_GW_IF0 \
        --region=REGION \
        --ike-version=IKE_VERS \
        --shared-secret=SHARED_SECRET \
        --router=ROUTER_NAME \
        --vpn-gateway=GW_NAME \
        --interface=INT_NUM_0
    
    
    
    gcloud compute vpn-tunnels create TUNNEL_NAME_IF3 \
        --peer-external-gateway=PEER_GW_NAME2 \
        --peer-external-gateway-interface=PEER_EXT_GW_IF1 \
        --region=REGION \
        --ike-version=IKE_VERS \
        --shared-secret=SHARED_SECRET \
        --router=ROUTER_NAME \
        --vpn-gateway=GW_NAME \
        --interface=INT_NUM_1
    

Replace the following:

  * `TUNNEL_NAME_IF0`, `TUNNEL_NAME_IF1` `TUNNEL_NAME_IF2`, and `TUNNEL_NAME_IF3`: a name for the tunnel; naming the tunnels by including the gateway interface name can help identify the tunnels later
  * `PEER_GW_NAME`: a name of the external peer gateway created earlier
  * `PEER_EXT_GW_IF0` and `PEER_EXT_GW_IF1`: the interface number configured earlier on the external peer gateway
  * `IKE_VERS`: `1` for IKEv1 or `2` for IKEv2; if possible, use IKEv2 for the IKE version. If your peer gateway requires IKEv1, replace `--ike-version 2` with `--ike-version 1`. To allow IPv6 traffic, you must specify IKEv2.
  * `SHARED_SECRET`: your pre-shared key (shared secret), which must correspond with the pre-shared key for the partner tunnel that you create on your peer gateway; for recommendations, see [Generate a strong pre-shared key](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/generating-pre-shared-key)
  * `GW_NAME`: the name of the HA VPN gateway
  * `INT_NUM_0`: the number `0` for the first interface on the HA VPN gateway that you created earlier
  * `INT_NUM_1`: the number `1` for the second interface on the HA VPN gateway that you created earlier
  * Optional: the `--vpn-gateway-region` is the region of the HA VPN gateway to operate on. Its value should be the same as `--region`. If not specified, this option is automatically set. This option overrides the default compute or region property value for this command invocation.

The command output looks similar to the following example:
        
        Created [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/vpnTunnels/tunnel-a-to-on-prem-if-0].
        NAME                       REGION        GATEWAY       VPN_INTERFACE   PEER_GATEWAY  PEER_INTERFACE
        tunnel-a-to-on-prem-if-0   us-central1   ha-vpn-gw-a   0               peer-gw       0
        
        Created [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/vpnTunnels/tunnel-a-to-on-prem-if-1].
        NAME                       REGION        GATEWAY       VPN_INTERFACE   PEER_GATEWAY  PEER_INTERFACE
        tunnel-a-to-on-prem-if-1   us-central1   ha-vpn-gw-a   1               peer-gw       1
        
        Created [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/vpnTunnels/tunnel-a-to-on-prem-if-0].
        NAME                       REGION        GATEWAY       VPN_INTERFACE   PEER_GATEWAY  PEER_INTERFACE
        tunnel-a-to-on-prem-if-2   us-central1   ha-vpn-gw-b   0               peer-gw       0
        
        Created [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/vpnTunnels/tunnel-a-to-on-prem-if-1].
        NAME                       REGION        GATEWAY       VPN_INTERFACE   PEER_GATEWAY  PEER_INTERFACE
        tunnel-a-to-on-prem-if-3   us-central1   ha-vpn-gw-b   1               peer-gw       1
        




**Configure BGP sessions**

For information about creating BGP sessions, see [Create BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn#bgp-sessions).

###  API 

**Create Cloud HA VPN gateway**

To create an HA VPN gateway, make a `POST` request by using the [`vpnGateways.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/vpnGateways/insert):
    
    
       POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/vpnGateways
       {
         "name": "ha-vpn-gw-a",
         "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/network-a",
         "stackType": "IPV4_IPV6"
       }
    

The `stackType` field is optional. The only valid values are `IPV4_IPV6` or `IPV4_ONLY`. If you don't specify a `stackType`, the default is `IPV4_ONLY`.

**Create a peer VPN gateway resource**

To create an external VPN gateway resource, make a `POST` request by using the [`externalVpnGateways.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/externalVpnGateways/insert).
    
    
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
             {
               "id": 1,
               "ipAddress": "192.0.2.2"
             },
             {
               "id": 0,
               "ipAddress": "192.0.2.1"
             }
           ],
           "redundancyType": "FOUR_IPS_REDUNDANCY"
         }
     

To create a peer VPN gateway with two interfaces, or two external VPN gateways with one interface each, use the `TWO_IPS_REDUNDANCY` setting. To create a peer VPN gateway with four interfaces, specify four instances of the interface ID and `ipAddress` and use a `redundancyType` of `FOUR_IPS_REDUNDANCY`.

**Create a Cloud Router**

To create a Cloud Router, make a `POST` request by using the [`routers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/insert):
    
    
     POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers
     {
       "name": "router-a",
       "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/network-a"
     }
    

**Add VPN tunnels**

To create four VPN tunnels, two for each interface on the HA VPN gateway, make a `POST` request by using the [`vpnTunnels.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/vpnTunnels/insert). To get a 99.9% uptime SLA, you must create a tunnel on each interface of your HA VPN gateway.

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
         

If you plan to enable IPv6 in the BGP session associated with this tunnel, you must specify `2` for the `ikeVersion`.

  2. To create the other tunnels, repeat this command, but change the following parameters:

     * `name`
     * `peerExternalGatewayInterface`
     * `sharedSecret` or `sharedSecretHash`(if needed)
     * `vpnGatewayInterface`: change to the value of the other HA VPN gateway interface—in this example, change this value to `1`



**Configure BGP sessions**

For information about creating BGP sessions, see [Create BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn#bgp-sessions).

###  API 

To create the full configuration for an HA VPN gateway, use the API commands in the following sections. All field values used in these sections are example values.

To create an HA VPN gateway, make a `POST` request by using the [`vpnGateways.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/vpnGateways/insert):
    
    
       POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/vpnGateways
       {
         "name": "ha-vpn-gw-a",
         "network": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/network-a",
         "stackType": "IPV4_IPV6"
       }
    

The `stackType` field is optional. The only valid values are `IPV4_IPV6` or `IPV4_ONLY`. If you don't specify a `stackType`, the default is `IPV4_ONLY`.

## Verify the configuration

###  Console 

To verify the configuration, go to the **Summary and reminder** page:

  1. The **Summary** section of this page lists information for the HA VPN gateway and the peer VPN gateway profile. For each VPN tunnel, you can view the [**VPN tunnel status**](https://docs.cloud.google.com/network-connectivity/docs/vpn/support/troubleshooting#troubleshooting-reference), the **BGP session name** , the [**BGP session status**](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bgp-states), and the MED value (advertised route priority).
  2. The **Reminder** section of this page lists the steps that you must complete to have a fully operational VPN connection between Cloud VPN and your peer VPN.
  3. After reviewing the information on this page, click **OK**.



###  gcloud 

To verify the Cloud Router configuration, follow these steps:

  * List the BGP IP addresses chosen by Cloud Router. If you added a new interface to an existing Cloud Router, the BGP IP addresses for the new interface are listed with the highest index number. Use the BGP IP address `peerIpAddress` to configure your peer VPN gateway:
        
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

To verify the Cloud Router configuration, make a `GET` request by using the [`routers.getRouterStatus` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/getRouterStatus), and use an empty request body:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers
    

## What's next

  * To control which IP addresses are allowed for peer VPN gateways, see [Restrict IP addresses for peer VPN gateways](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/restrict-peer-ip-addresses).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
