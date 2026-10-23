---
url: https://docs.cloud.google.com/network-connectivity/docs/vpn/tutorials/create-ha-vpn-connections-google-cloud-aws/
title: Create HA VPN connections between Google Cloud and AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:17.373517+00:00
---

# Create HA VPN connections between Google Cloud and AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/vpn/tutorials/create-ha-vpn-connections-google-cloud-aws/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud VPN ](https://docs.cloud.google.com/network-connectivity/docs/vpn)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)



Send feedback 

#  Create HA VPN connections between Google Cloud and AWS Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial demonstrates how to create highly available VPN connections between Google Cloud and Amazon Web Services (AWS) for direct communication between VPC networks across the two cloud platforms. 

This tutorial assumes that you're familiar with basic concepts of Virtual Private Cloud (VPC) networks, Border Gateway Protocol (BGP), virtual private networks (VPNs), and IPsec tunnels.

Google Cloud provides a highly available [HA VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview#ha-vpn) service to connect your VPC network to environments running outside of Google Cloud, such as on-premises or on AWS through an IPsec VPN connection. HA VPN provides an SLA of 99.99% service availability when configured based on Google best practices. For more information, see [Cloud VPN Service Level Agreement (SLA)](https://docs.cloud.google.com/network-connectivity/docs/vpn/sla).

## Architecture overview

The architecture described on this page includes the following components:

  * **Cloud Router** : A fully distributed and managed Google Cloud service to provide dynamic routing using BGP for your VPC networks.
  * **HA VPN gateway** : A Google-managed VPN gateway running on Google Cloud. Each HA VPN gateway is a regional resource that has two interfaces, each with its own external IP addresses: interface 0 and 1.
  * **VPN tunnels** : Connections from the HA VPN gateway to the peer VPN gateway on AWS through which encrypted traffic passes.
  * **Peer VPN gateway** : Two AWS site-to-site VPN endpoints, which can be from an AWS virtual private gateway or AWS transit gateway. For more information, see [What is AWS Site-to-Site VPN?](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html)



Each of the peer VPN gateway connections comes with two tunnels that are pre-configured to point to a single customer gateway, which in this case is a Google Cloud HA VPN interface. With this configuration, the minimum number of tunnels to meet the 99.99% service availability SLA is four.

Routing options and combined bandwidth over the VPN tunnels vary based on the Site-to-Site VPN option used on the AWS side:

  * **Transit gateway** : If you create the AWS transit gateway with no BGP preference, ECMP equally distributes traffic across active tunnels.

To use the VPN connectivity across multiple Google Virtual Private Cloud networks, [use a connectivity VPC network to scale a hub-and-spoke architecture with multiple VPC networks](https://docs.cloud.google.com/solutions/best-practices-vpc-design#scale-hub-spoke).

For more information about AWS transit gateways, see [What is Amazon VPC Transit Gateways?](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html).

  * **Virtual private gateway** : If you use an AWS virtual private gateway, only one tunnel across all connections on the gateway is selected. To use more than one tunnel, instead use an AWS transit gateway so that equal-cost multipath (ECMP) is available.

For details about VPN route priority with AWS, see [Site-to-Site VPN routing options](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPNRoutingTypes.html#vpn-route-priority).

For more information about AWS virtual private gateways, see [Tunnel options for your Site-to-Site VPN connection](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPNTunnels.html).




The following diagram shows the architecture.

![Architecture overview.](https://docs.cloud.google.com/static/network-connectivity/docs/vpn/images/build-ha-vpn-connections-google-cloud-aws.svg)

## Objectives

  * Create a VPC network on Google Cloud.
  * Create an HA VPN gateway and Cloud Router on Google Cloud.
  * Create customer gateways on AWS.
  * Create a VPN connection with dynamic routing on AWS.
  * Create an external VPN gateway and VPN tunnels on Google Cloud.
  * Verify and test the VPN connection between VPC networks on Google Cloud and AWS.
  * Use [Cloud Location Finder](https://docs.cloud.google.com/location-finder/docs/overview) to identify the closest Google Cloud regions.



## Example Terraform module

You can use the [`gcp-to-aws-ha-vpn-terraform-module`](https://github.com/GoogleCloudPlatform/gcp-to-aws-ha-vpn-terraform-module) module to provision HA VPN between Google Cloud and AWS.

## Costs

This tutorial uses billable components of Google Cloud, including the following:

  * [Cloud VPN](https://cloud.google.com/vpc/network-pricing)
  * [Compute Engine](https://cloud.google.com/compute/all-pricing)



For an estimate of the costs for the Google Cloud components, use the [Google Cloud pricing calculator](https://cloud.google.com/products/calculator/#id=b881814f-1a95-4c8e-a152-8237149589f7).

This tutorial uses billable components of Amazon Web Services, including the following:

  * AWS Transit Gateway
  * AWS Site-to-Site VPN



For an estimate of the costs for the AWS components, use the [AWS pricing calculator](https://calculator.aws/#/).

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




## Create the HA VPN gateway and Cloud Router on Google Cloud

In this section, you create a VPC network, an HA VPN gateway, and a Cloud Router on Google Cloud.

  1. In Cloud Shell, make sure that you're working in the Google Cloud project that you created or selected.
         
         gcloud config set project YOUR_PROJECT_ID
         
         export PROJECT_ID=`gcloud config list --format="value(core.project)"`

Replace `YOUR_PROJECT_ID` with your Google Cloud project ID.

  2. To create a custom VPC network with a single subnet, use the [`gcloud compute networks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/create):
         
         gcloud compute networks create NETWORK \
             --subnet-mode SUBNET_MODE \
             --bgp-routing-mode BGP_ROUTING_MODE

Replace the following:

     * `NETWORK`: The name of the network
     * `SUBNET_MODE`: The [subnet mode](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/create#--subnet-mode)
     * `BGP_ROUTING_MODE`: The [BGP routing mode](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/create#--bgp-routing-mode)

For example, the following command creates a custom VPC network named `gc-vpc` with a single subnet:
    
    gcloud compute networks create gc-vpc \
        --subnet-mode custom \
        --bgp-routing-mode global
    

  3. To create one subnet to host the test VMs, use the [`gcloud compute networks subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create):
         
         gcloud compute networks subnets create SUBNET_NAME \
             --network NETWORK \
             --region SUBNET_REGION \
             --range IP_ADDRESS_RANGE

Replace the following:

     * `SUBNET_NAME`: The subnet name
     * `SUBNET_REGION`: The region in which to create the subnet
     * `IP_ADDRESS_RANGE`: The IP address range for the subnet

For example, the following command creates a subnet named `subnet-east4` in the VPC network `gc-vpc`.
    
    gcloud compute networks subnets create subnet-east4  \
        --network gc-vpc \
        --region us-east4 \
        --range 10.1.1.0/24
    

  4. To create a HA VPN gateway, use the [`gcloud compute vpn-gateways create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/vpn-gateways/create):
         
         gcloud compute vpn-gateways create HA_VPN_GATEWAY_NAME \
             --network NETWORK \
             --region REGION

Replace `HA_VPN_GATEWAY_NAME` with the name for the HA VPN gateway.

  5. To create a Cloud Router, use the [`gcloud compute routers create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/create):
         
         gcloud compute routers create ROUTER_NAME \
             --region REGION \
             --network NETWORK \
             --asn GOOGLE_ASN \
             --advertisement-mode custom \
             --set-advertisement-groups all_subnets

Replace the following:

     * `ROUTER_NAME`: The name for your Cloud Router
     * `GOOGLE_ASN`: The private ASN (autonomous system number) for the Cloud Router that you're creating. It can be any private ASN in the range `64512-65534` or `4200000000-4294967294` that you aren't already using as a peer ASN in the same region and network.

For example, the following command creates a Cloud Router named `cloud-router`.
    
    gcloud compute routers create cloud-router \
        --region us-east4 \
        --network gc-vpc \
        --asn 65534 \
        --advertisement-mode custom \
        --set-advertisement-groups all_subnets
    




To create a VPN gateway with two interfaces, make a note of the external IP addresses. You need these addresses when setting up your environment on the AWS side.

## Create gateways and VPN connections on AWS

In this section, you create customer gateways, a target gateway, and VPN connections with dynamic routing.

You run AWS commands by using the [AWS Command Line Interface](https://aws.amazon.com/cli/).

  1. To create two customer gateways by using the following AWS command, use the [`create-customer-gateway` AWS CLI command](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-customer-gateway.html):
         
         aws ec2 create-customer-gateway --type ipsec.1 --public-ip INTERFACE_0_IP_ADDRESS --bgp-asn GOOGLE_ASN
         
         aws ec2 create-customer-gateway --type ipsec.1 --public-ip INTERFACE_1_IP_ADDRESS --bgp-asn GOOGLE_ASN

Replace `INTERFACE_0_IP_ADDRESS` and `INTERFACE_1_IP_ADDRESS` with the external IP addresses from the final step in the previous section.

  2. To create a target gateway and attach it to your Amazon VPC, do the following:

The target gateway can be a virtual private gateway or a transit gateway. For more information, see [Create a target gateway](https://docs.aws.amazon.com/vpn/latest/s2svpn/SetUpVPNConnections.html#vpn-create-target-gateway).

### Virtual private gateway

     1. Create a virtual private gateway with a specific AWS-side ASN by using the [`create-vpn-gateway` AWS CLI command](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpn-gateway.html):
            
            aws ec2 create-vpn-gateway --type ipsec.1 --amazon-side-asn AWS_SIDE_ASN

Replace `AWS_SIDE_ASN` with the ASN for the AWS side.

This command should look similar to the following example:
            
            aws ec2 create-vpn-gateway --type ipsec.1 --amazon-side-asn 65001
            

     2. Attach the virtual private gateway to your VPC network by using the [`attach-vpn-gateway` AWS CLI command](https://docs.aws.amazon.com/cli/latest/reference/ec2/attach-vpn-gateway.html):
            
            aws ec2 attach-vpn-gateway --vpn-gateway-id VPN_GATEWAY_ID --vpc-id VPC_ID

### Transit gateway

     1. Create a transit gateway by using the [`create-transit-gateway` AWS CLI command](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-transit-gateway.html):
            
            aws ec2 create-transit-gateway --description TRANSIT_GATEWAY_DESCRIPTION \
                --options=AmazonSideAsn=65001,AutoAcceptSharedAttachments=enable,DefaultRouteTableAssociation=enable,DefaultRouteTablePropagation=enable,VpnEcmpSupport=enable,DnsSupport=enable

Replace `TRANSIT_GATEWAY_DESCRIPTION` with a description for your transit gateway.

     2. Attach your VPC network to the transit gateway by using the [`create-transit-gateway-vpc-attachment` AWS CLI command](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-transit-gateway-vpc-attachment.html):
            
            aws ec2 create-transit-gateway-vpc-attachment \
                --transit-gateway-id TRANSIT_GATEWAY_ID \
                --vpc-id VPC_ID \
                --subnet-ids "SUBNET_ID"

Replace the following:

        * `TRANSIT_GATEWAY_ID`: The ID of the transit gateway
        * `VPC_ID`: The ID of the VPC
        * `SUBNET_ID`: The IDs of one or more subnets

  3. To create a VPN connection with dynamic routing, do the following:

The method for creating a VPN connection with dynamic routing differs depending on whether your target gateway is a virtual private gateway or a transit gateway. For more information, see [Create a VPN connection](https://docs.aws.amazon.com/vpn/latest/s2svpn/SetUpVPNConnections.html#vpn-create-vpn-connection).

### Virtual private gateway

Create a VPN connection with dynamic routing between the virtual private gateway and the customer gateways, and apply tags to the VPN connection:
         
         aws ec2 create-vpn-connection \
                 --type ipsec.1 \
                 --customer-gateway-id CUSTOMER_GATEWAY_1 \
                 --vpn-gateway-id VPN_GATEWAY_ID \
                 --options TunnelOptions='[{TunnelInsideCidr=AWS_T1_IP,PreSharedKey=SHARED_SECRET_1},{TunnelInsideCidr=AWS_T2_IP,PreSharedKey=SHARED_SECRET_2}]'
         
             aws ec2 create-vpn-connection \
                 --type ipsec.1 \
                 --customer-gateway-id CUSTOMER_GATEWAY_2 \
                 --vpn-gateway-id VPN_GATEWAY_ID \
                 --options TunnelOptions='[{TunnelInsideCidr=AWS_T3_IP,PreSharedKey=SHARED_SECRET_3},{TunnelInsideCidr=AWS_T4_IP,PreSharedKey=SHARED_SECRET_4}]'

Replace the following:

     * `CUSTOMER_GATEWAY_1`: Google Cloud VPN gateway, interface 0
     * `CUSTOMER_GATEWAY_2`: Google Cloud VPN gateway, interface 1
     * `AWS_T1_IP`: Inside IP address for virtual private gateway for connection 1, tunnel 1
     * `AWS_T2_IP`: Inside IP address for virtual private gateway for connection 1, tunnel 2
     * `AWS_T3_IP`: Inside IP address for virtual private gateway for connection 2, tunnel 1
     * `AWS_T4_IP`: Inside IP address for virtual private gateway for connection 2, tunnel 2
     * `SHARED_SECRET_1`: Pre-shared key for connection 1, tunnel 1
     * `SHARED_SECRET_2`: Pre-shared key for connection 1, tunnel 2
     * `SHARED_SECRET_3`: Pre-shared key for connection 2, tunnel 1
     * `SHARED_SECRET_4`: Pre-shared key for connection 2, tunnel 2

### Transit gateway

Create a VPN connection with dynamic routing between the transit gateway and the customer gateways:
    
    aws ec2 create-vpn-connection \
        --type ipsec.1 \
        --customer-gateway-id CUSTOMER_GATEWAY_1 \
        --transit-gateway-id TRANSIT_GATEWAY_ID \
        --options TunnelOptions='[{TunnelInsideCidr=AWS_T1_IP,PreSharedKey=SHARED_SECRET_1},{TunnelInsideCidr=AWS_T2_IP,PreSharedKey=SHARED_SECRET_2}]'
    
    aws ec2 create-vpn-connection \
        --type ipsec.1 \
        --customer-gateway-id CUSTOMER_GATEWAY_2 \
        --transit-gateway-id TRANSIT_GATEWAY_ID \
        --options TunnelOptions='[{TunnelInsideCidr=AWS_T3_IP,PreSharedKey=SHARED_SECRET_3},{TunnelInsideCidr=AWS_T4_IP,PreSharedKey=SHARED_SECRET_4}]'

Replace the following:

     * `CUSTOMER_GATEWAY_1`: Google Cloud VPN gateway, interface 0
     * `CUSTOMER_GATEWAY_2`: Google Cloud VPN gateway, interface 1
     * `TRANSIT_GATEWAY_ID`: The ID of the transit gateway associated with the VPN connection
     * `AWS_T1_IP`: Inside IP address for virtual private gateway for connection 1, tunnel 1
     * `AWS_T2_IP`: Inside IP address for virtual private gateway for connection 1, tunnel 2
     * `AWS_T3_IP`: Inside IP address for virtual private gateway for connection 2, tunnel 1
     * `AWS_T4_IP`: Inside IP address for virtual private gateway for connection 2, tunnel 2
     * `SHARED_SECRET_1`: Pre-shared key for connection 1, tunnel 1
     * `SHARED_SECRET_2`: Pre-shared key for connection 1, tunnel 2
     * `SHARED_SECRET_3`: Pre-shared key for connection 2, tunnel 1
     * `SHARED_SECRET_4`: Pre-shared key for connection 2, tunnel 2
     * `CUSTOMER_GATEWAY_1`: Google Cloud VPN gateway, interface 0
     * `CUSTOMER_GATEWAY_2`: Google Cloud VPN gateway, interface 1
     * `TRANSIT_GATEWAY_ID`: The ID of the transit gateway associated with the VPN connection
     * `AWS_T1_IP`: Inside IP address for virtual private gateway for connection 1, tunnel 1
     * `AWS_T2_IP`: Inside IP address for virtual private gateway for connection 1, tunnel 2
     * `AWS_T3_IP`: Inside IP address for virtual private gateway for connection 2, tunnel 1
     * `AWS_T4_IP`: Inside IP address for virtual private gateway for connection 2, tunnel 2
     * `SHARED_SECRET_1`: Pre-shared key for connection 1, tunnel 1
     * `SHARED_SECRET_2`: Pre-shared key for connection 1, tunnel 2
     * `SHARED_SECRET_3`: Pre-shared key for connection 2, tunnel 1
     * `SHARED_SECRET_4`: Pre-shared key for connection 2, tunnel 2

AWS reserves some CIDR ranges, so you can't use values in these ranges as inside IP addresses (`AWS_T1_IP`, `AWS_T2_IP`, `AWS_T3_IP`, `AWS_T4_IP`). For information about what CIDR blocks AWS reserves, see [Tunnel options for your Site-to-Site VPN connection](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPNTunnels.html).

You create four tunnels to Google Cloud by using these commands.

  4. [Download the configuration file](https://docs.aws.amazon.com/vpn/latest/s2svpn/SetUpVPNConnections.html#vpn-download-config) for the two VPN connections.

In the next steps, you use values from the configuration file that you downloaded to create and configure resources on the Google Cloud side.




## Create VPN tunnels and Cloud Router interfaces on Google Cloud

In this section, you use the information from the AWS VPN connection that you created in the previous section to create an [external VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/key-terms#external-vpn-gateway-definition), VPN tunnels, and Cloud Router interfaces in Google Cloud.

When you configure Cloud VPN tunnels to AWS, you must use the IKEv2 protocol and select only one IKE cipher set to help ensure successful tunnel establishment. For example, select one Phase 1 and one Phase 2 encryption algorithm, integrity algorithm, and Diffie-Hellman (DH) group. The default AWS transform sets create a large [security association (SA)](https://en.wikipedia.org/wiki/Security_association) payload, which can cause IP fragmentation of IKE packets. Cloud VPN doesn't support fragmented IKE packets.

  1. In Cloud Shell, create an external VPN gateway with four interfaces for the AWS outside IP addresses.

Before you create the external VPN gateway, verify that the AWS outside IP addresses match the values in the configuration file that you downloaded. You can't modify these IP addresses after you create the external VPN gateway. If the addresses don't match, the HA VPN tunnel connection can't be established.
         
         gcloud compute external-vpn-gateways create PEER_GATEWAY_NAME --interfaces \
           0=AWS_GW_IP_1,1=AWS_GW_IP_2,2=AWS_GW_IP_3,3=AWS_GW_IP_4

**Caution:** Before you create the HA VPN gateway, verify that the AWS outside IP addresses (`OutsideIpAddress`) match the values in the downloaded configuration file. You cannot change these IP addresses later. If the addresses don't match, the VPN tunnel connection won't be established.

Replace the following:

     * `AWS_GW_IP_1`: Outside IP address for virtual private gateway for connection 1, tunnel 1
     * `AWS_GW_IP_2`: Outside IP address for virtual private gateway for connection 1, tunnel 2
     * `AWS_GW_IP_3`: Outside IP address for virtual private gateway for connection 2, tunnel 1
     * `AWS_GW_IP_4`: Outside IP address for virtual private gateway for connection 2, tunnel 2
  2. Create four VPN tunnels.

     * Tunnel 1:
           
           gcloud compute vpn-tunnels create tunnel-1 \
               --peer-external-gateway PEER_GATEWAY_NAME \
               --peer-external-gateway-interface 0 \
               --region REGION \
               --ike-version 2 \
               --shared-secret SHARED_SECRET_1 \
               --router ROUTER_NAME \
               --vpn-gateway HA_VPN_GATEWAY_NAME \
               --interface 0

     * Tunnel 2:
           
           gcloud compute vpn-tunnels create tunnel-2 \
               --peer-external-gateway PEER_GATEWAY_NAME \
               --peer-external-gateway-interface 1 \
               --region REGION \
               --ike-version 2 \
               --shared-secret SHARED_SECRET_2 \
               --router ROUTER_NAME \
               --vpn-gateway HA_VPN_GATEWAY_NAME \
               --interface 0

     * Tunnel 3:
           
           gcloud compute vpn-tunnels create tunnel-3 \
               --peer-external-gateway PEER_GATEWAY_NAME \
               --peer-external-gateway-interface 2 \
               --region REGION \
               --ike-version 2 \
               --shared-secret SHARED_SECRET_3 \
               --router ROUTER_NAME \
               --vpn-gateway HA_VPN_GATEWAY_NAME \
               --interface 1

     * Tunnel 4:
           
           gcloud compute vpn-tunnels create tunnel-4 \
               --peer-external-gateway PEER_GATEWAY_NAME \
               --peer-external-gateway-interface 3 \
               --region REGION \
               --ike-version 2 \
               --shared-secret SHARED_SECRET_4 \
               --router ROUTER_NAME \
               --vpn-gateway HA_VPN_GATEWAY_NAME \
               --interface 1

Replace the following:

       * `PEER_GATEWAY_NAME`: a name of the external peer gateway that you created in step 1
       * `REGION`: the [Google Cloud region](https://docs.cloud.google.com/docs/geography-and-regions) where you create the tunnel
       * `SHARED_SECRET`: your pre-shared key (PSK), which must correspond with the pre-shared key for the partner tunnel that you create on your peer gateway; to generate a strong pre-shared key, see [Generate a strong pre-shared key](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/generating-pre-shared-key)
       * `ROUTER_NAME`: the name of the Cloud Router gateway that you created in the Create the HA VPN gateway and Cloud Router on Google Cloud section.
       * `HA_VPN_GATEWAY_NAME`: the name of the HA VPN gateway that you created in the Create the HA VPN gateway and Cloud Router on Google Cloud section.
  3. Create four Cloud Router interfaces.

In the following commands, replace each `GOOGLE_BGP_IP_TUNNEL` placeholder with the tunnel's inside IP address on the Google Cloud side. You can find the values in the AWS VPN configuration files as the customer gateway address for each tunnel. Each of these addresses must be in the `/30` CIDR range within the `169.254.0.0/16` network range.

     * Cloud Router interface 1:
           
           gcloud compute routers add-interface ROUTER_NAME \
               --interface-name int-1 \
               --vpn-tunnel tunnel-1 \
               --ip-address GOOGLE_BGP_IP_TUNNEL_1 \
               --mask-length 30 \
               --region REGION

     * Cloud Router interface 2:
           
           gcloud compute routers add-interface ROUTER_NAME \
               --interface-name int-2 \
               --vpn-tunnel tunnel-2 \
               --ip-address GOOGLE_BGP_IP_TUNNEL_2 \
               --mask-length 30 \
               --region REGION

     * Cloud Router interface 3:
           
           gcloud compute routers add-interface ROUTER_NAME \
               --interface-name int-3 \
               --vpn-tunnel tunnel-3 \
               --ip-address GOOGLE_BGP_IP_TUNNEL_3 \
               --mask-length 30 \
               --region REGION

     * Cloud Router interface 4:
           
           gcloud compute routers add-interface ROUTER_NAME \
               --interface-name int-4 \
               --vpn-tunnel tunnel-4 \
               --ip-address GOOGLE_BGP_IP_TUNNEL_4 \
               --mask-length 30 \
               --region REGION

  4. Add BGP peers.

In the following commands, replace `PEER_ASN` with the ASN for the AWS side of the BGP session.

     * AWS connection 1, tunnel 1:
           
           gcloud compute routers add-bgp-peer ROUTER_NAME \
               --peer-name aws-conn1-tunn1 \
               --peer-asn PEER_ASN \
               --interface int-1 \
               --peer-ip-address AWS_T1_IP \
               --region REGION

     * AWS connection 1, tunnel 2:
           
           gcloud compute routers add-bgp-peer ROUTER_NAME \
               --peer-name aws-conn1-tunn2 \
               --peer-asn PEER_ASN \
               --interface int-2 \
               --peer-ip-address AWS_T2_IP \
               --region REGION

     * AWS connection 2, tunnel 1:
           
           gcloud compute routers add-bgp-peer ROUTER_NAME \
               --peer-name aws-conn2-tunn1 \
               --peer-asn PEER_ASN \
               --interface int-3 \
               --peer-ip-address AWS_T3_IP \
               --region REGION

     * AWS connection 2, tunnel 2:
           
           gcloud compute routers add-bgp-peer ROUTER_NAME \
               --peer-name aws-conn2-tunn2 \
               --peer-asn PEER_ASN \
               --interface int-4 \
               --peer-ip-address AWS_T4_IP \
               --region REGION




## Verify the configuration

  1. In Cloud Shell, verify the Cloud Router status:
         
         gcloud compute routers get-status ROUTER_NAME \
             --region REGION \
             --format='flattened(result.bgpPeerStatus[].name, result.bgpPeerStatus[].ipAddress, result.bgpPeerStatus[].peerIpAddress)'

The output is similar to the following:
         
         result.bgpPeerStatus[].peerIpAddress)'
         result.bgpPeerStatus[0].ipAddress:     169.254.171.18
         result.bgpPeerStatus[0].name:          aws-conn1-tunn1
         result.bgpPeerStatus[0].peerIpAddress: 169.254.171.17
         result.bgpPeerStatus[1].ipAddress:     169.254.156.154
         result.bgpPeerStatus[1].name:          aws-conn1-tunn2
         result.bgpPeerStatus[1].peerIpAddress: 169.254.156.153
         result.bgpPeerStatus[2].ipAddress:     169.254.123.38
         result.bgpPeerStatus[2].name:          aws-conn2-tunn1
         result.bgpPeerStatus[2].peerIpAddress: 169.254.123.37
         result.bgpPeerStatus[3].ipAddress:     169.254.48.186
         result.bgpPeerStatus[3].name:          aws-conn2-tunn2
         result.bgpPeerStatus[3].peerIpAddress: 169.254.48.185
         

  2. List all tunnels:
         
         gcloud compute vpn-tunnels list

The output is similar to the following:
         
         NAME      REGION    GATEWAY    PEER_ADDRESS
         tunnel-1  us-east4  ha-vpn-gw  34.205.x.x
         tunnel-2  us-east4  ha-vpn-gw  52.203.x.x
         tunnel-3  us-east4  ha-vpn-gw  3.208.x.x
         tunnel-4  us-east4  ha-vpn-gw  52.204.x.x
         

  3. Check the tunnel status:
         
         gcloud compute vpn-tunnels describe tunnel-1 \
              --region REGION \
              --format='flattened(status,detailedStatus)'

The output is similar to the following:
         
         detailed_status: Tunnel is up and running.
         status:          ESTABLISHED
         

  4. List dynamic routes learned by Cloud Router:
         
         gcloud compute routers get-status ROUTER_NAME \
             --region REGION \
             --format="flattened(result.bestRoutes)"

The output is similar to the following:
         
         result.bestRoutes[0].creationTimestamp: 2021-01-19T20:42:07.366-08:00
         result.bestRoutes[0].destRange:         10.2.2.0/24
         result.bestRoutes[0].kind:              compute#route
         result.bestRoutes[0].nextHopIp:         169.254.171.17
         result.bestRoutes[0].priority:          100
         result.bestRoutes[1].creationTimestamp: 2021-01-19T20:42:07.366-08:00
         result.bestRoutes[1].destRange:         10.2.2.0/24
         result.bestRoutes[1].kind:              compute#route
         result.bestRoutes[1].nextHopIp:         169.254.156.153
         result.bestRoutes[1].priority:          100
         result.bestRoutes[2].creationTimestamp: 2021-01-19T20:56:26.588-08:00
         result.bestRoutes[2].destRange:         10.2.2.0/24
         result.bestRoutes[2].kind:              compute#route
         result.bestRoutes[2].nextHopIp:         169.254.123.37
         result.bestRoutes[2].priority:          100
         result.bestRoutes[3].creationTimestamp: 2021-01-19T20:56:26.588-08:00
         result.bestRoutes[3].destRange:         10.2.2.0/24
         result.bestRoutes[3].kind:              compute#route
         result.bestRoutes[3].nextHopIp:         169.254.48.185
         result.bestRoutes[3].priority:          100
         




## Test the VPN connection

  1. Create test VMs on each side of the tunnels to test ping requests.

Make sure that you have [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls) to allow ICMP traffic.

     * For instructions on how to create Compute Engine VMs, see [Create and start a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).

     * For instructions on how to create EC2 instances on AWS, see [Launch an Amazon EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/LaunchingAndUsingInstances.html).

  2. Test the connection by using the [`ping` command](https://wikipedia.org/wiki/Ping_\(networking_utility\)).

     1. If the `ping` test fails, view the logs in Google Cloud and the [AWS Site-to-Site VPN logs](https://docs.aws.amazon.com/vpn/latest/s2svpn/monitoring-logs.html). Error messages in the logs can help you to identify the issue. To learn how to troubleshoot issues with your VPN connection, see the following resources: 
        * [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/vpn/support/troubleshooting) Cloud VPN
        * [Troubleshoot AWS Site-to-Site VPN connectivity when using Border Gateway Protocol](https://docs.aws.amazon.com/vpn/latest/s2svpn/Generic_Troubleshooting.html)
  3. Measure bandwidth between your test machines by using [iperf](https://iperf.fr/iperf-download.php).

     * Server side:
           
           iperf3 -s

     * Client side:
           
           iperf3 -c SERVER_IP_ADDRESS -P NUMBER_OF_PARALLEL_SESSIONS




## Clean up

Delete the Google Cloud and AWS resources that you have created during this tutorial.

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



### Delete AWS resources

  1. [Delete a Site-to-Site VPN connection](https://docs.aws.amazon.com/vpn/latest/s2svpn/delete-vpn.html)
  2. [Delete the transit gateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-transit-gateway.html)
  3. [Terminate Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#terminating-instances-console)



## What's next

  * Learn more about [Google Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview).
  * Learn more about [best practices and reference architectures for VPC design](https://docs.cloud.google.com/solutions/best-practices-vpc-design).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
