---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/configure-ha-vpn-interconnect/
title: Configure HA VPN over Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:22.262227+00:00
---

# Configure HA VPN over Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/configure-ha-vpn-interconnect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Configure HA VPN over Cloud Interconnect Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to deploy HA VPN on top of the encrypted VLAN attachments of your Cloud Interconnect connection. These steps apply to HA VPN for both Dedicated Interconnect and Partner Interconnect.

When you create an HA VPN gateway for an HA VPN over Cloud Interconnect deployment, you associate that HA VPN gateway with your encrypted VLAN attachment. Each VLAN attachment that you want to configure must be associated with an HA VPN gateway interface.

Only a single VLAN attachment is required but to configure [failover](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/ha-vpn-interconnect#failover), you must associate two VLAN attachments in your [edge availability domain](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology#edge-availability-domain):

  * The first VLAN attachment in `zone1` corresponds to HA VPN interface `0`.
  * The second VLAN attachment in `zone2` corresponds to HA VPN interface `1`.



After you create your encrypted VLAN attachments and HA VPN gateways, you can create the HA VPN tunnels to the peer VPN gateways. Each HA VPN tunnel has a bandwidth of 3 Gbps. Therefore, to match the capacity of your VLAN attachment, you must create multiple HA VPN tunnels.

**Important:** After you associate an HA VPN gateway with an encrypted VLAN attachment, you cannot change the associations between the attachment and the interfaces of the HA VPN gateway. You can only delete the HA VPN gateway and its tunnels or delete the VLAN attachment itself.

## VLAN capacity and recommended number of tunnels

The section provides an estimate of the number of tunnels that you might need based on the capacity of your VLAN attachment. VLAN attachment capacity covers both egress and ingress traffic, and the number of tunnels in the table might not reflect your network's particular traffic patterns.

Use the following table as a starting point and monitor traffic utilization of your HA VPN tunnels. To ensure adequate capacity for failover in your tunnels, we recommend that you not exceed 50% of either the 3-Gbps bandwidth limit or the 250,000-pps packet rate limit for a given VPN tunnel.

For more information about setting up monitoring and alerts for Cloud VPN tunnels, see [View logs and metrics](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/viewing-logs-metrics#define_alerts).

VLAN attachment capacity | Number of tunnels for each VLAN attachment | Total number of tunnels for 2 VLAN attachments (failover)  
---|---|---  
2 Gbps or fewer | 1 | 2  
5 Gbps | 2 | 4  
10 Gbps | 4 | 8  
20 Gbps | 7 | 14  
50 Gbps | 17 | 34  
100 Gbps | 34 | 68  
  
## Gateway and tunnel mapping

You don't need to have a one-to-one mapping of peer VPN gateways to HA VPN gateways. You can add multiple tunnels to each interface of the HA VPN gateway as long as there are interfaces on the peer VPN gateway that have not yet been mapped to that particular HA VPN gateway interface. There can only be one unique mapping or tunnel between a specific HA VPN gateway interface and a specific peer VPN gateway interface.

Thus, you can have the following configurations:

  * Multiple HA VPN gateways that tunnel to a single peer VPN gateway (with multiple interfaces)
  * A single HA VPN gateway that tunnels to multiple peer VPN gateways
  * Multiple HA VPN gateways that tunnel to multiple peer VPN gateways



As a general rule, the number of HA VPN gateways that you need to deploy is determined by how many peer VPN gateways with unused interfaces you have available in your on-premises network.

**Note:** The peer VPN gateway cannot be hosted in Google Cloud.

The following diagrams provide examples of tunnel mappings between HA VPN and peer VPN gateways.

### Example 1: One HA VPN to two peer VPN

[ ![Example of one HA VPN gateway to two peer VPN gateways \(click to enlarge\).](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/havpn-ic-tunnel-mapping-option1.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/havpn-ic-tunnel-mapping-option1.svg) **Figure 1:** Example of one HA VPN gateway to two peer VPN gateways (click to enlarge).

### Example 2: Two HA VPN to one peer VPN

[ ![Example of two HA VPN gateways to one peer VPN gateway \(click to enlarge\).](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/havpn-ic-tunnel-mapping-option2.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/havpn-ic-tunnel-mapping-option2.svg) **Figure 2:** Example of two HA VPN gateways to one peer VPN gateway (click to enlarge).

## Create HA VPN gateways

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `compute.vpnGateways.create`
  * `compute.vpnGateways.delete`
  * `compute.vpnGateways.get`
  * `compute.vpnGateways.list`
  * `compute.vpnGateways.use`
  * `compute.vpnGateways.setLabels`
  * `compute.externalVpnGateways.get`
  * `compute.externalVpnGateways.list`
  * `compute.externalVpnGateways.create`
  * `compute.externalVpnGateways.delete`
  * `compute.externalVpnGateways.use`
  * `compute.externalVpnGateways.setLabels`



**Roles**

  * Compute Network Admin role(`roles/compute.networkAdmin`)

**Important:** For Partner Interconnect, you must wait until both your encrypted VLAN attachments are in an `ACTIVE` state before you configure your HA VPN gateways and tunnels. Two VLAN attachments are required for proper HA VPN over Cloud Interconnect failover and SLA configuration.

This procedure assumes that you have already created and configured your encrypted VLAN attachments by using the Google Cloud console:

  * For Dedicated Interconnect, see [Create encrypted VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments#encrypted-attachments).

  * For Partner Interconnect, see [Create encrypted VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/creating-vlan-attachments#encrypted-attachments).




###  Console 

This procedure assumes that you have already created and configured your encrypted VLAN attachments by using the Google Cloud console:

  * For Dedicated Interconnect, see [Create encrypted VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments#encrypted-attachments).

  * For Partner Interconnect, see [Create encrypted VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/creating-vlan-attachments#encrypted-attachments).




To create an HA VPN gateway, follow these steps:

  1. In the Google Cloud console, continue to the next section of the HA VPN over Cloud Interconnect deployment wizard.

After you complete the Cloud Router for Cloud Interconnect configuration, the **Create VPN gateways** page appears.

The HA VPN over Cloud Interconnect configuration wizard automatically creates HA VPN gateways based on the capacity that you configured for your VLAN attachments. For example, if you specified 5 Gbps as the capacity of each VLAN attachment, the wizard creates two HA VPN gateways.

  2. Optional: Click expand_more**Expand** to change the generated name of each HA VPN gateway.

  3. Optional: If you want to add more HA VPN gateways, click **Add another gateway**. Specify a **Name** and an optional **Description**. Then, click **Done**.

  4. Click **Create and Continue**.




###  gcloud 

  1. Use the VLAN capacity and tunnels table to estimate how many VPN tunnels are needed to match the capacity of your VLAN attachment. You need to create at least one HA VPN gateway to be able to create these HA VPN tunnels.

In the following example, a 5-Gbps capacity VLAN attachment might require four tunnels.

  2. Create the HA VPN gateways.

For example, the following commands create two HA VPN gateways and assign the gateway interfaces to your encrypted VLAN attachments:
         
         gcloud compute vpn-gateways create vpn-gateway-a \
             --network=network-a \
             --region=REGION \
             --interconnect-attachments \
             attachment-a-zone1,attachment-a-zone2
         
         
         gcloud compute vpn-gateways create vpn-gateway-b \
             --network=network-a \
             --region=REGION \
             --interconnect-attachments \
             attachment-a-zone1,attachment-a-zone2
         

Replace `REGION` with the region in which your VLAN attachment is located.




For the `--interconnect-attachments` parameter, you list both VLAN attachments. The first VLAN attachment that you list is assigned to interface 0 (`if0`) of the HA VPN gateway and the second VLAN attachment is assigned to interface 1 (`if1`).

## Configure the HA VPN Cloud Router, peer VPN gateway resources, and HA VPN tunnels

###  Console 

  1. In the Google Cloud console, continue to the next section of the HA VPN over Cloud Interconnect deployment wizard.

  2. In the **Cloud Router** section, select a Cloud Router. This router is dedicated to managing the BGP sessions for all of your HA VPN tunnels.

You can use an existing Cloud Router if the router does not already manage a BGP session for a VLAN attachment associated with a Partner Interconnect connection.

You cannot use the encrypted Cloud Router used for the Interconnect tier of your HA VPN over Cloud Interconnect deployment.

  3. If you don't have an available Cloud Router, select **Create new router** , and specify the following:

     * A name
     * An optional description
     * A Google ASN for the new router

You can use any private ASN (`64512` through `65534`, `4200000000` through `4294967294`) that you are not using elsewhere in your network. The Google ASN is used for all BGP sessions on the same Cloud Router, and you cannot change the ASN later.

To create the new router, click **Create**.

  4. Configure the **IKE version** by selecting either **IKEv1** or **IKEv2**. This version is used across all HA VPN tunnels in the deployment.

  5. Optional: Click **Generate keys** to generate the IKE pre-shared key for all VPN tunnels. If you select this option, the same IKE pre-shared key is populated for all tunnels across all HA VPN gateways. Make sure that you record the pre-shared key in a secure location because it cannot be retrieved after you create your VPN tunnels.

  6. In the **VPN Configurations** section, click a VPN configuration, and then specify the following:

     1. **Peer VPN gateway** : Select an existing peer VPN gateway, or create one by selecting **Create a new peer VPN gateway**. To create a peer VPN gateway, specify the following:

        * A name
        * Two interfaces

If you need to specify a single interface or four interfaces, you cannot create this peer VPN gateway in the Google Cloud console. Use the Google Cloud CLI instead. Specifically, you must assign four interfaces on your peer VPN gateway if you are connecting to Amazon Web Services (AWS).

     2. In the **IP addresses** field, enter the IPv4 addresses of the two peer VPN gateway interfaces.

     3. Click **Create**.

  7. Under **VPN Tunnel over` ENCRYPTED VLAN_ATTACHMENT_1`** and **VPN Tunnel over` ENCRYPTED VLAN_ATTACHMENT_2`**, configure the following fields for each tunnel:

     * **Name** : You can leave the generated tunnel name or modify it.
     * **Description** : Optional.
     * **Associated peer VPN gateway interface** : Select the peer VPN gateway interface and IP address combination that you want to associate with this tunnel and HA VPN interface. This interface must match the interface on your actual peer router.
     * **IKE pre-shared key** : If you did not already generate a pre-shared key for all tunnels, specify an **IKE pre-shared key**. Use the pre-shared key (shared secret) that corresponds with the pre-shared key that you create on your peer gateway. If you haven't configured a pre-shared key on your peer VPN gateway and want to generate one, click **Generate and copy**. Make sure that you record the pre-shared key in a secure location because it cannot be retrieved after you create your VPN tunnels.
  8. Click **Done** when you have completed the configuration of both tunnels.

  9. Repeat the previous two steps for each HA VPN gateway until you have configured all the gateways and their tunnels.

  10. If you need to add more tunnels, click **Add VPN configuration** and configure the following fields:

     1. **VPN gateway** : Select one of the HA VPN gateways that are associated with the encrypted VLAN attachments.
     2. **Peer VPN gateway** : Select an existing peer VPN gateway or create a new one by selecting **Create a new peer VPN gateway**. To create a new peer VPN gateway, specify the following:

        * A name
        * Two interfaces

If you need to specify a single interface or four interfaces, you cannot create this peer VPN gateway in the Google Cloud console. Use the Google Cloud CLI instead. Specifically, you must assign four interfaces on your peer VPN gateway if you are connecting to AWS.

     3. In the **IP addresses** field, enter the IPv4 addresses of the two peer VPN gateway interfaces.

     4. Click **Create**.

  11. When you have finished configuring all your HA VPN tunnels, click **Create and Continue**.




###  gcloud 

This router is dedicated to managing the BGP sessions for all of your HA VPN tunnels.

You can use an existing Cloud Router if the router does not already manage a BGP session for a VLAN attachment associated with a Partner Interconnect connection. You cannot use the encrypted Cloud Router used for the Cloud Interconnect tier of your HA VPN over Cloud Interconnect deployment.

  1. To create a Cloud Router, run the following command:
         
         gcloud compute routers create ROUTER_NAME \
              --region=REGION \
              --network=NETWORK \
              --asn=GOOGLE_ASN
         

Replace the following:

     * `ROUTER_NAME`: the name of the Cloud Router in the same region as the Cloud VPN gateway
     * `REGION`: the [Google Cloud region](https://docs.cloud.google.com/compute/docs/regions-zones) where you create the gateway and tunnel
     * `NETWORK`: the name of your Google Cloud network
     * `GOOGLE_ASN`: any private ASN (`64512` through `65534`, `4200000000` through `4294967294`) that you are not already using in the peer network; the Google ASN is used for all BGP sessions on the same Cloud Router, and it cannot be changed later

The router that you create should look similar to the following example output:
    
    Created [https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/routers/router-a].
    NAME       REGION        NETWORK
    router-a   us-central1   network-a
    

  2. Create at least one external peer VPN gateway.
         
         gcloud compute external-vpn-gateways create peer-gw \
              --interfaces 0=ON_PREM_GW_IP_0,1=ON_PREM_GW_IP_1
         

Replace the following:

     * `ON_PREM_GW_IP_0`: the IP address assigned to interface `0` on your peer VPN gateway
     * `ON_PREM_GW_IP_1`: the IP address assigned to interface `1` on your peer VPN gateway

Create as many external peer VPN gateways as needed in your deployment.

  3. For each HA VPN gateway that you created in Create HA VPN gateways, create a VPN tunnel for each interface, `0` and `1`. In each command, you specify the peer side of the VPN tunnel as the external VPN gateway and interface that you created earlier.

For example, to create four tunnels for the two example HA VPN gateways created in Create HA VPN gateways, run the following commands:
         
         gcloud compute vpn-tunnels create tunnel-a-to-on-prem-if-0 \
              --peer-external-gateway=peer-gw \
              --peer-external-gateway-interface=0 \
              --region=REGION \
              --ike-version=2 \
              --shared-secret=SHARED_SECRET \
              --router=vpn-router \
              --vpn-gateway=vpn-gateway-a \
              --interface=0
         
         
         gcloud compute vpn-tunnels create tunnel-a-to-on-prem-if-1 \
              --peer-external-gateway=peer-gw \
              --peer-external-gateway-interface=1 \
              --region=REGION \
              --ike-version=2 \
              --shared-secret=SHARED_SECRET \
              --router=vpn-router \
              --vpn-gateway=vpn-gateway-a \
              --interface=1
         
         
         gcloud compute vpn-tunnels create tunnel-b-to-on-prem-if-0 \
              --peer-external-gateway peer-gw \
              --peer-external-gateway-interface 0 \
              --region=REGION \
              --ike-version=2 \
              --shared-secret=SHARED_SECRET \
              --router=vpn-router \
              --vpn-gateway=vpn-gateway-b \
              --interface=0
         
         
         gcloud compute vpn-tunnels create tunnel-b-to-on-prem-if-1 \
              --peer-external-gateway peer-gw \
              --peer-external-gateway-interface 1 \
              --region=REGION \
              --ike-version=2 \
              --shared-secret=SHARED_SECRET \
              --router=vpn-router \
              --vpn-gateway=vpn-gateway-b \
              --interface=1
         




## Configure BGP sessions

###  Console 

In the Google Cloud console, continue to the next section of the HA VPN over Cloud Interconnect deployment wizard.

After you have created all the HA VPN tunnels, you must configure the BGP sessions for each tunnel.

Next to each tunnel, click **Configure BGP session**.

Follow the instructions in [Create BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn#bgp-sessions) to configure BGP for each VPN tunnel.

###  gcloud 

After you have created all the HA VPN tunnels, you must configure the BGP sessions for each tunnel.

For each tunnel, follow the instructions in [Create BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn#bgp-sessions?tab=gcloud).

## Complete the HA VPN configuration

Before you can use the new Cloud VPN gateways and their associated VPN tunnels, complete the following steps:

  1. Set up the peer VPN gateways for your on-premises networks and configure the corresponding tunnels there. For instructions, see the following: 
     * For specific configuration guidance for certain peer VPN devices, see [Use third-party VPNs](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/interop-guides).
     * For general configuration parameters, see [Configure the peer VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/configuring-peer-gateway).
  2. [Configure firewall rules](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/configuring-firewall-rules) in Google Cloud and your peer network as required.
  3. [Check the status of your VPN tunnels](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/checking-vpn-status). This step includes checking the high-availability configuration of your HA VPN gateway.



## What's next?

  * If you need to add more HA VPN tunnels, see [Add a VPN tunnel](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/adding-a-tunnel).

  * To learn about HA VPN monitoring, see [View logs and metrics](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/viewing-logs-metrics).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
