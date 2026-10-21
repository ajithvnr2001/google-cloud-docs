---
url: https://docs.cloud.google.com/network-connectivity/docs/vpn/tutorials/create-ha-vpn-connections-google-cloud-azure/
title: Create HA VPN connections between Google Cloud and Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:42:49.555274+00:00
---

# Create HA VPN connections between Google Cloud and Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/vpn/tutorials/create-ha-vpn-connections-google-cloud-azure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud VPN ](https://docs.cloud.google.com/network-connectivity/docs/vpn)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)



Send feedback 

#  Create HA VPN connections between Google Cloud and Azure Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial demonstrates how to create highly available (HA) virtual private network (VPN) connections between Google Cloud and Microsoft Azure. You can use these HA VPN services for direct communication between Virtual Private Cloud (VPC) networks in Google Cloud and Microsoft Azure Virtual Network Gateways.

This document assumes that you're familiar with the basic concepts of VPC networks, Border Gateway Protocol (BGP), VPNs, and Internet Protocol Security (IPsec) tunnels.

Google Cloud provides a [highly available (HA) VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview#ha-vpn) service to connect your VPC network to environments running outside of Google Cloud, such as Microsoft Azure, through an IPsec VPN connection. An HA VPN provides a [service level agreement (SLA) of 99.99% service availability](https://docs.cloud.google.com/network-connectivity/docs/vpn/sla) when configured based on Google best practices.

## Architecture overview

The following diagram shows the architecture that is described in this document.

![Architecture
overview.](https://docs.cloud.google.com/static/network-connectivity/docs/vpn/images/ha-vpn-google-cloud-to-azure.svg)

The architecture shown in the diagram includes the following components:

  * **Cloud Router** : A fully distributed and managed Google Cloud service to provide dynamic routing using BGP for your VPC networks.
  * **HA VPN gateway** : A Google-managed VPN gateway running on Google Cloud. Each HA VPN gateway is a regional resource that has two interfaces: interface 0 and 1. Each of these interfaces has its own external IP address.
  * **VPN tunnels** : Connections from the HA VPN gateway on Google Cloud to the peer VPN gateway on Azure through which encrypted traffic passes.
  * **Virtual Network Gateway** : Two private networks defined in the Azure Cloud service.



Each Virtual Network Gateway connection comes with two tunnels that are pre-configured to point to a single customer gateway, which in this case is an HA VPN gateway interface in Google Cloud. With this configuration, the minimum number of Cloud VPN tunnels required to meet the 99.99% service availability SLA is two.

## IP addresses needed for the procedures

To complete the procedures in this document, you use a variety of IP addresses in both Google Cloud and Azure. Some of these IP addresses are automatically assigned when you create a resource.

For those addresses that are not automatically assigned, you define these IP addresses based upon the IP addresses that you have available and the needs of your organization.

Google Cloud resources require the following IP addresses:

  * Creating a subnet for a Virtual Private Cloud network requires a user-defined IP address range.
  * After creating the HA VPN gateway, Google Cloud automatically assigns two external IP addresses to the HA VPN gateway. Google assigns one IP address to each of the gateway's two interfaces. You need the IP addresses for these interfaces to set up the local network gateways in Azure.
  * When you create HA VPN tunnels in Google Cloud, each tunnel needs a BGP interface to the Cloud Router and a BGP interface to the active-active virtual network gateway (VPN gateway) in Azure. For each tunnel, decide on a pair of link-local BGP peering IPv4 addresses in a /30 block from the `169.254.21.*` and `169.254.22.*` ranges. These ranges are the valid ranges for Azure APIPA BGP peering IPv4 addresses. You must select four IP addresses in total.

The BGP peering IPv4 addresses that you select must be unique among all Cloud Routers in all regions of a VPC network.




Azure resources require the following IP addresses:

  * When you create the virtual network (VNet), the VNet requires an IP address space for the network and an IP address space for the network's subnet. You can use the default address spaces or enter user-defined address spaces.
  * When you create the active-active virtual network gateway (VPN gateway), the gateway requires a subnet address range. You can use the default range or enter a user-defined range.
  * When you configure the BGP for the active-active VPN gateway, the gateway requires two APIPA BGP peering IP addresses. As mentioned previously, the valid ranges for Azure APIPA BGP peering IP addresses are `169.254.21.*` and `169.254.22.*`.
  * After you create an active-active VPN gateway, Azure automatically assigns an external IP address to each of the gateway's interfaces. You need these IP addresses to set up the peer VPN gateway in Google Cloud.



When defining IP addresses, make sure to use a unique set of IP addresses for each network.

## Objectives

  * Create an Azure virtual network (VNet) and an active-active virtual network gateway (VPN gateway).
  * Create the necessary components on Google Cloud: a VPC network, a Cloud Router, an HA VPN gateway, a peer VPN gateway, and two HA VPN tunnels with BGP sessions.
  * Create two local network gateways and two VPN connections in Azure. Verify the Cloud Router configuration and check the status of your HA VPN tunnels in Google Cloud.
  * Test the Cloud VPN connection between the VPC network on Google Cloud and the virtual network (VNet) on Azure.



## Costs

The procedures in this document use billable components of Google Cloud, including the following:

  * [Cloud VPN](https://cloud.google.com/vpc/network-pricing)
  * [Compute Engine](https://cloud.google.com/compute/all-pricing)



For an estimate of the costs for the Google Cloud components, use the [Google Cloud pricing calculator](https://cloud.google.com/products/calculator#id=b881814f-1a95-4c8e-a152-8237149589f7).

The procedures in this document use billable components of Microsoft Azure Cloud services, including the following:

  * VPN gateways
  * Local network gateways



For an estimate of the costs for the Azure components, use the [Azure pricing calculator](https://azure.microsoft.com/en-in/pricing/calculator/).

## Before you begin

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  3. Enable the Compute Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com)

  4. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  5. Make sure that you have the [required administrative roles](https://docs.cloud.google.com/vpc/docs/shared-vpc#iam_roles_required_for_shared_vpc) to configure networking components: 

     * Network Admin: `compute.networkAdmin`
     * Security Admin: `compute.securityAdmin`
     * Compute Admin: `compute.admin`

For more information about the purposes of these roles, see [IAM roles for networking-related job functions](https://docs.cloud.google.com/iam/docs/job-functions/networking). 




## Create a VNet and an active-active VPN gateway on Azure

In Azure, you need to set up the following components:

  * An Azure virtual network (VNet) that allows Azure resources to communicate with your Google Cloud VPN.
  * An active-active virtual network gateway (VPN gateway) that allows both instances of the gateway's virtual machines (VMs) to establish VPN tunnels to your Google Cloud VPN.



### Create a VNet

A VNet lets Azure resources securely communicate with each other, the internet, and other networks (such as Cloud VPN). For more information on creating a VNet, see the [Azure documentation on creating a VNet](https://docs.microsoft.com/en-us/azure/vpn-gateway/active-active-portal#vnet).

  1. Sign in to the Azure Portal.
  2. In the **Search resources, service, and docs (G+/)** box, type `virtual network`.
  3. In the list of **Marketplace** results, select **Virtual network**.
  4. On the **Virtual network** page, select **Create**.
  5. On the **Basics** tab of the **Create virtual network** page, configure the following VNet settings for **Project details** and **Instance details** :

     1. In the **Subscription** box, verify that the subscription that is listed is the correct one. To change the subscription, select the subscription from the list .
     2. To specify the resource group, click **Create new** to create a new group and enter a name such as `azure‑to‑google‑resgroup` for the name of the resource group.
     3. In the **Name** box, enter the name for your VNet such as `azure‑to‑google‑network`.
     4. In the **Region** box, select a location for your VNet.

The location that you select determines the storage location of the resources that you deploy to this virtual network.

  6. On the **IP Addresses** tab, in the **IPv4 address space** box, use the default address space and subnet that was created by Azure.

  7. On the **Security** tab, leave the values for **BastionHost** , **DDos Protection Standard** , and **Firewall** set to the default value of **Disable**.

  8. To validate the VNet settings, select **Review + create**.

  9. After the settings have been validated, select **Create**.




### Create an active-active VPN gateway

The following procedures create the active-active VPN gateway:

  * The first procedure defines the project and instance details
  * The second procedure specifies the IP address for the gateway.



You only create the active-active VPN gateway at this time. You need to create your Google Cloud components before you can configure the necessary tunnels in Azure. For more information about creating an active-active VPN gateway, see the [Configure active-active VPN gateways using the portal](https://docs.microsoft.com/en-us/azure/vpn-gateway/active-active-portal) topic in the Azure documentation.

#### Define the gateway details

  1. Sign in to the Azure Portal.
  2. In **Search resources, service, and docs (G+/)** , type `virtual network gateway`.
  3. Under **Services** in the search results, locate and select **Virtual network gateways**.
  4. On the **Virtual network gateway** page, select **Create**.
  5. On the **Basics** tab of the **Create virtual network gateway** page, specify the following values for options in the **Project details** and **Instance details** sections:

     1. In the **Subscription** list, select the subscription that you want to use.
     2. Optional: In the **Gateway subnet address range** box, enter the address range for the subnet.
     3. Verify that **Resource Group** displays the resource group that corresponds to the virtual network that you select on this page.
     4. For **Name** , enter the name of your gateway such as `azure‑to‑google‑gateway`.
     5. For **Region** , select the same region that you used to when you created your VNET.
     6. For **Gateway type** , select **VPN**.
     7. For **VPN type** , select the **Route-based** VPN type.

     8. In the **SKU** list, select the gateway SKU that you want to use.

The SKUs that are listed in the dropdown depend on the VPN type you select.

     9. In the **Generation** list, select the generation that you want to use.

     10. In the **Virtual network** list, select the VNet that you previously created

  6. Stay on this page for the next procedure.




#### Define the gateway IP addresses

  1. On the **Basics** tab of the **Create virtual network gateway** page, use the following steps to create the external IP addresses that are used by the active-active VPN gateway:

     1. For **Public IP address** , select **Create new**.

Azure automatically assigns the external IP address to your active-active VPN gateway.

     2. In the **Public IP address name** box, type a name for your external IP address instance, such as `azure‑to‑google‑network‑ip1`.

     3. For **Enable active-active mode** , select **Enabled**.

     4. Optional: If available for your region, configure the **Availability Zone**. For example, you can select **Zone-redundant**.

     5. For **Second Public IP Address** , select **Create new**.

     6. In the **Public IP address name** box, type the name of the second external IP address, such as `azure‑to‑google‑network‑ip2`.

     7. For **Configure BGP** , select **Enabled**.

     8. For **Autonomous system numbers (ASN)** , set the ASN to an allowable and valid value.

You use this ASN value when you set up the BGP sessions for the tunnels in Google Cloud. Record this value as `AZURE_ASN` to refer to this active-active VPN gateway.

     9. For **Custom Azure APIPA BGP IP address** , enter the first APIPA BGP IP address and record the value as `AZURE_BGP_IP_0`. The valid ranges for Azure APIPA BGP IP addresses are `169.254.21.*` and `169.254.22.*`.

     10. For **Second Custom Azure APIPA BGP IP address** , enter the second APIPA BGP IP address and record the value as `AZURE_BGP_IP_1`. You'll use these variables when you configure the BGP sessions in Google Cloud.

  2. To run validation, select **Review + create**.

  3. After validation is complete, select **Create** to deploy the VPN gateway.




### View and record the external IP addresses for the active-active VPN gateway

You need the external IP addresses that Azure automatically assigned to the active-active VPN gateway. You use these IP addresses to create the peer VPN gateway resource in Google Cloud.

  1. On the **Overview** page for the active-active gateway that you just created, locate the external IP addresses for the gateway.
  2. Record the IP addresses that you see on the screen: 
     * Record the first external IP address as `AZURE_GW_IP_0`.
     * Record the second external IP address as `AZURE_GW_IP_1`.



Later on, this document refers to these IP addresses as `AZURE_GW_IP_0` and `AZURE_GW_IP_1`.

## Create your Google Cloud components

On Google Cloud, you need to set up the following components:

  * A VPC network.
  * An HA VPN gateway.
  * A Cloud Router.
  * A peer VPN gateway.
  * HA VPN tunnels with BGP sessions.



The following procedures assume that you have set up Google Cloud as described in Before you begin. If you haven't completed those steps, do so now.

### Create a VPC network, subnet, HA VPN gateway, and Cloud Router on Google Cloud

On Google Cloud, you create a VPC network, create an HA VPN gateway, create a Cloud Router, and then configure the firewall rules on Google Cloud.

  1. In Google Cloud Shell, make sure that you're working in the Cloud project that you created or selected:
         
         gcloud config set project YOUR_PROJECT_ID
         
         export PROJECT_ID=`gcloud config list   --format="value(core.project)"`

Replace `YOUR_PROJECT_ID` with your Cloud project ID.

  2. Create a custom VPC network with a single subnet:
         
         gcloud compute networks create NETWORK \
             --subnet-mode SUBNET_MODE \
             --bgp-routing-mode BGP_ROUTING_MODE

Replace the following:

     * `NETWORK`: The name of the network, such as `google‑to‑azure‑vpc`.
     * `SUBNET_MODE`: The [subnet mode](https://cloud.google.com/sdk/gcloud/reference/compute/networks/create#--subnet-mode) set to `custom`.
  3. `BGP_ROUTING_MODE`: The [BGP routing mode](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/create#--bgp-routing-mode) set to `global`.

The command should look similar to the following example:
         
         gcloud compute networks create google-to-azure-vpc \
             --subnet-mode custom \
             --bgp-routing-mode global

  4. Create one subnet to host the test VMs:
         
         gcloud compute networks subnets create SUBNET_NAME \
             --network NETWORK \
             --region SUBNET_REGION \
             --range SUBNET_IP_ADDRESS_RANGE

Replace the following:

     * `SUBNET_NAME`: The subnet name.
     * `SUBNET_REGION`: The region in which to create the subnet.
     * `SUBNET_IP_ADDRESS_RANGE`: The [IP address range for the subnet](https://docs.cloud.google.com/vpc/docs/subnets#manually_created_subnet_ip_ranges).

The command should look similar to the following example:
    
    gcloud compute networks subnets create subnet-central1  \
        --network google-to-azure-vpc \
        --region us-central1 \
        --range 10.1.1.0/24
    

  5. Create the HA VPN gateway:
         
         gcloud compute vpn-gateways create HA_VPN_GATEWAY_NAME \
             --network NETWORK \
             --region REGION

Replace `HA_VPN_GATEWAY_NAME` with the name for the HA VPN gateway.

The command should look similar to the following example:
         
         gcloud compute vpn-gateways create ha-vpn-gw-a \
            --network google-to-azure-vpc \
            --region us-central1
         

The gateway that you create should look similar to the following example output:
         
         Created [https://www.googleapis.com/compute/v1/projects/YOUR_PROJECT_ID/regions/us-central1/vpnGateways/ha-vpn-gw-a].
         NAME          INTERFACE0     INTERFACE1     NETWORK     REGION
         ha-vpn-gw-a   203.0.113.1   203.0.113.2   google-to-azure-vpc   us-central1
         

The output lists the external IPv4 addresses that have been automatically assigned to each gateway interface (`INTERFACE0` and `INTERFACE1`). You need these IP addresses when you set up the local network gateways on Azure:

     * Record the IP address for `INTERFACE0` in `HA_VPN_INT_0`.
     * Record the IP address for `INTERFACE1` in `HA_VPN_INT_1`.
  6. Create a Cloud Router:
         
         gcloud compute routers create ROUTER_NAME \
             --region REGION \
             --network NETWORK \
             --asn GOOGLE_ASN \

Replace the following:

     * `ROUTER_NAME`: The name for your Cloud Router.
     * `REGION`: The region where you are creating the HA VPN gateway and tunnels.
     * `GOOGLE_ASN`: The private autonomous system number (ASN) for the Cloud Router that you're creating. It can be any private ASN in the range `64512-65534` or `4200000000-4294967294` that you aren't already using as a peer ASN in the same region and network.

The command should look similar to the following example:
    
    gcloud compute routers create cloud-router \
        --region us-central1 \
        --network google-to-azure-vpc \
        --asn 65534
    




### Create a peer VPN gateway for the Azure VPN

In this section, you create an external VPN gateway resource that provides information to Google Cloud about your active-active VPN gateway in Azure. You create a single peer VPN gateway that uses two separate interfaces, each with its own external IP address.

Create a single external peer VPN gateway with two interfaces:
    
    
    gcloud compute external-vpn-gateways create AZURE_GW_NAME \
         --interfaces 0=AZURE_GW_IP_0,1=AZURE_GW_IP_1

Replace the following:

  * `AZURE_GW_NAME`: the name of your Azure active-active VPN gateway
  * `AZURE_GW_IP_0`: the external IP address for one interface from the peer gateway
  * `AZURE_GW_IP_1`: the external IP address for another interface from the peer gateway



The peer VPN gateway resource that you created should look similar to the following example where `AZURE_GW_IP_0` and `AZURE_GW_IP_1` show the actual external IP addresses of the peer gateway interfaces:
    
    
    gcloud compute external-vpn-gateways create azure-peer-gw \
         --interfaces 0=203.0.113.1,1=203.0.113.2
    
    Created [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/externalVpnGateways/peer-gw].
    NAME     INTERFACE0    INTERFACE1
    azure-peer-gw  203.0.113.1  203.0.113.2
    

### Create VPN tunnels

You need to create two VPN tunnels: one tunnel for each interface in the peer VPN gateway. When configuring VPN tunnels to Azure, use the IKEv2 encryption protocol.

**Note:** The VPN tunnels that you create are not available until you have finished creating the VPN connections in Azure.

For the commands used in this section, replace the following:

  * `TUNNEL_NAME_IF0` and `TUNNEL_NAME_IF1`: a name for the tunnel; naming the tunnels by including the gateway interface name can help identify the tunnels later.
  * `AZURE_GW_NAME`: the name of the external peer gateway created earlier
  * `AZURE_GW_INT_NUM_0` and `AZURE_GW_INT_NUM_1`: the interface numbers configured earlier on the external peer gateway.
  * `IKE_VERS`: use `2` for IKEv2.
  * `SHARED_SECRET`: your pre-shared key (shared secret), which must correspond with the pre-shared key that you specify when you set up VPN connections in Azure. For recommendations, see [Generate a strong pre-shared key](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/generating-pre-shared-key).
  * `HA_VPN_GATEWAY_NAME`: the name of the HA VPN gateway.
  * `INT_NUM_0`: the number `0` for the first interface on the HA VPN gateway that you created earlier.
  * `INT_NUM_1`: the number `1` for the second interface on the HA VPN gateway that you created earlier.



Use the following steps to create the VPN tunnels:

  1. Create the VPN tunnel for interface 0:
         
         gcloud compute vpn-tunnels create TUNNEL_NAME_IF0 \
            --peer-external-gateway=AZURE_GW_NAME \
            --peer-external-gateway-interface=AZURE_GW_INT_NUM_0  \
            --region=REGION \
            --ike-version=IKE_VERS \
            --shared-secret=SHARED_SECRET \
            --router=ROUTER_NAME \
            --vpn-gateway=HA_VPN_GATEWAY_NAME \
            --interface=INT_NUM_0

The command should look similar to the following example:
         
         gcloud compute vpn-tunnels create azure-tunnel-1 \
            --peer-external-gateway azure-peer-gw \
            --peer-external-gateway-interface 0  \
            --region us-central1  \
            --ike-version 2 \
            --shared-secret xo2aTKHipD/oE1GAXgj3lMwjBmJXZjqD \
            --router cloud-router \
            --vpn-gateway ha-vpn-gw-a \
            --interface 0

  2. Create the VPN tunnel for interface 1:
         
         gcloud compute vpn-tunnels create TUNNEL_NAME_IF1 \
           --peer-external-gateway=AZURE_GW_NAME \
           --peer-external-gateway-interface=AZURE_GW_INT_NUM_1 \
           --region=REGION \
           --ike-version=IKE_VERS \
           --shared-secret=SHARED_SECRET \
           --router=ROUTER_NAME \
           --vpn-gateway=HA_VPN_GATEWAY_NAME \
           --interface=INT_NUM_1

The command should look similar to the following example:
         
         gcloud compute vpn-tunnels create azure-tunnel-2 \
            --peer-external-gateway azure-peer-gw \
            --peer-external-gateway-interface 1  \
            --region us-central1  \
            --ike-version 2 \
            --shared-secret xo2aTKHipD/oE1GAXgj3lMwjBmJXZjqD \
            --router cloud-router \
            --vpn-gateway ha-vpn-gw-a \
            --interface 1




### Create BGP sessions

For dynamic routing, you use [Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview) to establish BGP sessions between Google Cloud and Azure. We recommend using dynamic routing instead of static routing whenever possible, as discussed in the [Cloud VPN Overview](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) and [Cloud VPN Network and Tunnel Routing](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/choosing-networks-routing).

You need to create a BGP session for each VPN tunnel. Each BGP session consists of a BGP interface to the Cloud Router and a BGP peer. You create a BGP peer for each of the two VPN tunnels that you just created.

For the commands used in this section, replace the following:

  * `ROUTER_NAME`: the name you assigned to the Cloud Router.
  * `ROUTER_INTERFACE_NAME_0` and `ROUTER_INTERFACE_NAME_1`: the name for the Cloud Router BGP interface; it can be helpful to use names related to the tunnel names configured previously.
  * `MASK_LENGTH`: specify `30`; each BGP session on the same Cloud Router must use a unique `/30`CIDR from the `169.254.0.0/16` block.
  * `GOOGLE_BGP_IP_0` and `GOOGLE_BGP_IP_1`: the BGP peering IP addresses for the HA VPN gateway interfaces that you configure; each tunnel uses a different gateway interface. Because the allowed ranges for Azure APIPA BGP peering IP addresses are `169.254.21.*` and `169.254.22.*`, you must select an available IP address in the `/30` CIDR of those ranges for your Cloud Router BGP peering IP addresses.
  * `AZURE_BGP_IP_0` and `AZURE_BGP_IP_1`: the APIPA BGP peering IP addresses that you already configured on the Azure active-active VPN gateway; each tunnel uses a different address.
  * `TUNNEL_NAME_IF0` and `TUNNEL_NAME_IF1`: the tunnels associated with the HA VPN gateway interface that you configured.
  * `AZURE_ASN`: the ASN that you configured for the active-active peer VPN gateway in Azure.
  * `BGP_PEER_NAME_1` and `BGP_PEER_NAME_2` with unique names for each BGP peer. For example, `azure‑bgp‑peer‑1` and `azure‑bgp‑peer‑2`.



To create BGP sessions for the VPN tunnels, follow these steps:

  1. For the first VPN tunnel, add a BGP interface to the Cloud Router:
         
         gcloud compute routers add-interface ROUTER_NAME \
            --interface-name=ROUTER_INTERFACE_NAME_0 \
            --mask-length=MASK_LENGTH \
            --vpn-tunnel=TUNNEL_NAME_IF0 \
            --ip-address=GOOGLE_BGP_IP_0 \
            --region=REGION

The command should look similar to the following example:
         
         gcloud compute routers add-interface cloud-router \
            --interface-name azure-tunnel-1-int-0 \
            --mask-length 30 \
            --vpn-tunnel azure-tunnel-1 \
            --ip-address 169.254.21.2 \
            --region us-central1
         

  2. For the first VPN tunnel, add a BGP peer to the interface:
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
            --peer-name=BGP_PEER_NAME_1 \
            --peer-asn=AZURE_ASN \
            --interface=ROUTER_INTERFACE_NAME_0 \
            --peer-ip-address=AZURE_BGP_IP_0 \
            --region=REGION

The command should look similar to the following example:
         
         gcloud compute routers add-bgp-peer cloud-router \
            --peer-name azure-bgp-peer-1 \
            --peer-asn 65515 \
            --interface azure-tunnel-1-int-0 \
            --peer-ip-address 169.254.21.1 \
            --region us-central1
         

  3. For the second VPN tunnel, add a BGP interface to the Cloud Router:
         
         gcloud compute routers add-interface ROUTER_NAME \
            --interface-name=ROUTER_INTERFACE_NAME_1 \
            --mask-length=MASK_LENGTH \
            --vpn-tunnel=TUNNEL_NAME_IF1 \
            --ip-address=GOOGLE_BGP_IP_1 \
            --region=REGION

The command should look similar to the following example:
         
         gcloud compute routers add-interface cloud-router \
            --interface-name azure-tunnel-2-int-1 \
            --mask-length 30 \
            --vpn-tunnel azure-tunnel-2 \
            --ip-address 169.254.22.2 \
            --region us-central1
         

  4. For the second VPN tunnel, add a BGP peer to the interface:
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
            --peer-name=BGP_PEER_NAME_2 \
            --peer-asn=AZURE_ASN \
            --interface=ROUTER_INTERFACE_NAME_1 \
            --peer-ip-address=AZURE_BGP_IP_1 \
            --region=REGION

The command should look similar to the following example:
         
         gcloud compute routers add-bgp-peer cloud-router \
           --peer-name azure-bgp-peer-2 \
           --peer-asn 65515 \
           --interface azure-tunnel-2-int-1 \
           --peer-ip-address 169.254.22.1 \
           --region us-central1
         




## Create local network gateways and VPN connections in Azure

With your Google Cloud components created and configured, you return to your Azure environment to finish connecting Google Cloud to Azure. To finish this connection, you create the following components in Azure:

  * Two local network gateways that represent your Google Cloud VPN in Azure.
  * Two VPN connections that correspond to the two HA VPN tunnels that you configured in Google Cloud.



### Create two local network gateways

A local network gateway is a specific object that represents your Google Cloud VPN in Azure. When you create a local network gateway, you specify the following information:

  * A name for the local network gateway.
  * The IP address of the HA VPN interface to be used in the connection.
  * The IP address of the Google Cloud Router to which you want to create a connection.
  * The IP address prefixes that are routed through the VPN gateway to the Cloud Router. The address prefixes that you specify are the prefixes that are located on your Cloud VPN. If your Cloud virtual private network changes or you need to change the external IP address for the Cloud Router, you can update the values later.



You need to create two local network gateways: one gateway that connects to the first HA VPN tunnel interface on Google Cloud and another gateway that connects to the second HA VPN tunnel interface.

For more information, see the [create a local network gateway](https://docs.microsoft.com/en-us/azure/vpn-gateway/tutorial-site-to-site-portal#LocalNetworkGateway) section of the **Create a site-to-site VPN connection in the Azure portal** tutorial in the Azure documentation.

To create the first local network gateway, follow these steps:

  1. Sign in to the Azure Portal.
  2. In **Search resources, service, and docs (G+/)** , type **local network gateway**.
  3. In the search results under **Marketplace** , locate and select **local network gateway**.
  4. Click **Create**.
  5. On the **Basics** tab of the **Create local network gateway** page, specify the following values for your local network gateway:

     1. In the **Subscription** list, verify that the correct subscription is showing.
     2. In the **Resource group** list, select the same resource group as the one that you created for the VNet earlier in this document.
     3. For **Region** , select the same location that your VNet resides in.
     4. For **Name** , enter a name for your local network gateway, such as `azure-to-google-locgateway1`.
     5. For **Endpoint** , select **IP address.**
     6. In the **IP address** box, enter the IP address for `INTERFACE0` of your HA VPN (that is, enter `HA_VPN_INT_0`).
     7. For **Address Space,** enter the address ranges for the network that this local network represents.

You can add multiple address space ranges. Make sure that the ranges you specify here do not overlap with ranges of other networks that you want to connect to.

  6. On the **Advanced** tab, configure the BGP settings as follows:

     1. For **Configure BGP settings** , select **Yes**.
     2. For **Autonomous system number (ASN)** , enter the ASN for your Cloud Router (that is, enter `GOOGLE_ASN`).
     3. For **BGP peer IP address** , enter the BGP IP address for the Cloud Router in tunnel 1 (that is, enter `GOOGLE_BGP_IP_0`).
  7. To validate the local network gateway configuration, click **Review and** **create** at the bottom of the page.

  8. After the validation passes, click **Create** to create the local network gateway.




To create the second local network gateway, follow these steps:

  1. In the Azure Portal, in **Search resources, service, and docs (G+/)** , type `local network gateway`.
  2. Under **Marketplace** , in the search results, locate and select **local network gateway**.
  3. On the **Basics** tab of the **Create local network gateway** page, specify the following values for your local network gateway:

     1. In the **Subscription** list, verify that the correct subscription is showing.
     2. In the **Resource group** list, select the same resource group as the one that you created for the VNet earlier in this document.
     3. For **Region** , select the same region as that of your VNet.
     4. For **Name** , enter a name for your local network gateway, such as `azure-to-google-locgateway2`.
     5. For **Endpoint** , select **IP address.**
     6. In the **IP address** box, enter the IP address for `INTERFACE1` of your HA VPN (that is, enter `HA_VPN_INT_1`).
     7. For **Address Space,** enter the address ranges for the network that this local network represents.

You can add multiple address space ranges. Make sure that the ranges you specify here do not overlap with ranges of other networks that you want to connect to.

  4. On the **Advanced** tab, configure the BGP settings as follows:

     1. For **Configure BGP settings** , select **Yes**.
     2. For **Autonomous system number (ASN)** , enter the ASN for your Cloud Router (that is, enter `GOOGLE_ASN`).
     3. For **BGP peer IP address** , enter the BGP IP address for the Cloud Router in tunnel 1 (that is, enter `GOOGLE_BGP_IP_1`).
  5. To validate your local network gateway configuration, click **Review and** **create** at the bottom of the page.

  6. After the validation passes, click **Create** to create the local network gateway.




### Create two VPN connections

To create the VPN connections in Azure, you need the preshared keys, or SHARED_SECRET, that you configured when you set up the HA VPN tunnels on Google Cloud.

  1. In the Azure Portal, locate the active-active VPN gateway that you created in Create an active-active VPN gateway.
  2. Select **Connections**.
  3. At the top of the **Connections** page, select **+Add**.
  4. On the **Add connection** page, specify the following values for your first connection: 
     1. For **Name** , enter a name for the connection, such as `azure-vnet-to-google1`.
     2. For **Connection type** , select **Site-to-site (IPsec)**.
     3. For **Local network gateway** , specify the first local network gateway that you created, such as `azure-to-google-locgateway1`.
     4. For **Shared key (PSK)** , specify the shared key that you configured for the first HA VPN tunnel.
     5. Select **Enable BGP**.
     6. For **IKE Protocol** , select **IKEv2**.
     7. Click **OK**.
     8. On the **Connections** page, select **+Add** to add a second connection with the following values:
     9. For **Name** , enter a name for the connection, such as `azure-vnet-to-google2`.
     10. For **Connection type** , select **Site-to-site (IPsec)**.
     11. For **Local network gateway** , specify the second local network gateway that you created, such as `azure-to-google-locgateway2`.
     12. For **Shared key (PSK)** , specify the shared key that you configured for the second HA VPN tunnel.
     13. Select **Enable BGP**.
     14. For **IKE Protocol** , select **IKEv2**.
     15. Click **OK**.
  5. On the **Connections** page, verify that the status of both connections is listed as **Connected**.



## Verify the configuration

In Google Cloud, you can verify your HA VPN configuration by first examining (listing) your Cloud Router configuration and then checking the status of the HA VPN tunnels.

  1. In Cloud Shell, list the BGP peering IP addresses chosen by Cloud Router:
         
         gcloud compute routers get-status ROUTER_NAME \
            --region=REGION \
            --format='flattened(result.bgpPeerStatus[].name,
              result.bgpPeerStatus[].ipAddress, result.bgpPeerStatus[].peerIpAddress)'

The command should look similar to the following example:
         
         gcloud compute routers get-status cloud-router \
             --region us-central1 \
         --format='flattened(result.bgpPeerStatus[].name,result.bgpPeerStatus[].ipAddress,result.bgpPeerStatus[].peerIpAddress)'
         

The expected output for a Cloud Router managing two HA VPN tunnels (index `0` and index `1`) should look like the following example:
         
         result.bgpPeerStatus[0].ipAddress:     169.254.21.2
         result.bgpPeerStatus[0].name:          azure-bgp-peer-1
         result.bgpPeerStatus[0].peerIpAddress: 169.254.21.1
         result.bgpPeerStatus[1].ipAddress:     169.254.22.2
         result.bgpPeerStatus[1].name:          azure-bgp-peer-2
         result.bgpPeerStatus[1].peerIpAddress: 169.254.22.1
         

  2. In Cloud Shell, view the status of the first HA VPN tunnel:
         
         gcloud compute vpn-tunnels describe TUNNEL_NAME_IF0 \
            --region=REGION

Replace the following:

     * `TUNNEL_NAME_IF0`: the tunnel associated with the first HA VPN gateway interface that you configured.
     * `REGION`: region where you deployed the HA VPN gateway.

The command should look similar to the following example:
    
    gcloud compute vpn-tunnels describe azure-tunnel-1 -–region=us-central1
    

The expected output for the tunnel should look similar to the following example:
    
    creationTimestamp: '2022-09-28T17:13:21.592-07:00'
    description: ''
    detailedStatus: Tunnel is up and running.
    id: '278561789474069966'
    ikeVersion: 2
    kind: compute#vpnTunnel
    localTrafficSelector:
    -   0.0.0.0/0
    name: azure-tunnel-1
    peerExternalGateway: https://www.googleapis.com/compute/v1/projects/PROJECT-ID/global/externalVpnGateways/azure-peer-gw
    peerExternalGatewayInterface: 0
    peerIp: 203.0.113.1
    region: https://www.googleapis.com/compute/v1/projects/PROJECT-ID/regions/us-central1
    remoteTrafficSelector:
    -   0.0.0.0/0
    router: https://www.googleapis.com/compute/v1/projects/PROJECT-ID/regions/us-central1/routers/cloud-router
    selfLink: https://www.googleapis.com/compute/v1/projects/PROJECT-ID/regions/us-central1/vpnTunnels/azure-tunnel-1
    sharedSecret: '*************'
    sharedSecretHash: ALDZGgSMUxj8KFahMoG_L0Fz9paz
    status: ESTABLISHED
    vpnGateway: https://www.googleapis.com/compute/v1/projects/PROJECT-ID/regions/us-central1/vpnGateways/ha-vpn-gw-a
    vpnGatewayInterface: 0
    

  3. In Cloud Shell, view the status of the second HA VPN tunnel:
         
         gcloud compute vpn-tunnels describe TUNNEL_NAME_IF1 \
            --region=REGION

Replace the following:

     * `TUNNEL_NAME_IF1`: the tunnel associated with the second HA VPN gateway interface that you configured.
     * `REGION`: region where you deployed the HA VPN gateway.

The command should look similar to the following example:
    
    gcloud compute vpn-tunnels describe azure-tunnel-2 --region=us-central1
    

The expected output for the tunnel should look similar to the following example:
    
    creationTimestamp: '2022-09-28T17:13:21.592-07:00'
    description: ''
    detailedStatus: Tunnel is up and running.
    id: '5665972275117479944'
    ikeVersion: 2
    kind: compute#vpnTunnel
    localTrafficSelector:
    -   0.0.0.0/0
    name: azure-tunnel-2
    peerExternalGateway: https://www.googleapis.com/compute/v1/projects/PROJECT-ID/global/externalVpnGateways/azure-peer-gw
    peerExternalGatewayInterface: 1
    peerIp: 203.0.113.2
    region: https://www.googleapis.com/compute/v1/projects/PROJECT-ID/regions/us-central1
    remoteTrafficSelector:
    -   0.0.0.0/0
    router: https://www.googleapis.com/compute/v1/projects/PROJECT-ID/regions/us-central1/routers/cloud-router
    selfLink: https://www.googleapis.com/compute/v1/projects/PROJECT-ID/regions/us-central1/vpnTunnels/azure-tunnel-2
    sharedSecret: '*************'
    sharedSecretHash: ALDZGgSMUxj8KFahMoG_L0Fz9ddd
    




## Test connectivity

To test HA VPN connections, you first need to create VMs on each side of the tunnel.

Next, you need to make sure that you have [firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls#firewall_rule_components) defined in Google Cloud that allow inbound ICMP traffic from the Azure network subnets. With the VMs and firewall rules in place, you can then test connectivity by using [ping](https://wikipedia.org/wiki/Ping_\(networking_utility\)) and test bandwidth by using [iperf](https://iperf.fr/iperf-download.php).

  1. Create test VMs on each side of the tunnels to test ping requests.

You must also configure the Azure network firewall to allow inbound traffic from the subnet prefixes that are used in your Virtual Private Cloud.

  2. On Google Cloud, configure a firewall rule that allows inbound ICMP traffic from your Azure VPN:
         
         gcloud compute firewall-rules create RULE_NAME \
             --network NETWORK \
             --direction ingress \
             --action allow \
             --source-ranges AZURE_VNET_RANGE \
             --rules icmp \

Replace `AZURE_VNET_RANGE` with the IP address range that is assigned to your Azure VNet.

The command should look similar to the following example:
         
         gcloud compute firewall-rules create allow-azure-icmp \
           --network google-to-azure-vpc \
           --direction ingress \
           --action allow \
           --source-ranges 10.0.0.0/16 \
           --rules icmp
         

  3. Test the connection using the [ping](https://wikipedia.org/wiki/Ping_\(networking_utility\)) command.

  4. Measure bandwidth between your test machines using [iperf](https://iperf.fr/iperf-download.php).




## Clean up

Delete the Google Cloud and Azure resources that you have created during this tutorial.

### Delete the Google Cloud project

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, you can delete your project:

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete Azure resource group

Delete the Azure Manager resource group that you created when you created the VNet. In this tutorial, the name of the example resource group is `azure-to-google-resgroup`.

For more information, see [Azure Resource Manager resource group and resource deletion](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/delete-resource-group).

## What's next

  * Learn more about [Google Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview).
  * Learn more about [best practices and reference architectures for VPC design](https://docs.cloud.google.com/solutions/best-practices-vpc-design).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
