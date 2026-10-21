---
url: https://docs.cloud.google.com/vmware-engine/docs/workloads/nsxt-layer2-stretch/
title: Stretch on-premises Layer 2 networks to a private cloud using NSX \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:34:55.254685+00:00
---

# Stretch on-premises Layer 2 networks to a private cloud using NSX  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/workloads/nsxt-layer2-stretch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Stretch on-premises Layer 2 networks to a private cloud using NSX

This document describes how to stretch a Layer 2 network from your on-premises environment to your Google Cloud VMware Engine private cloud by using NSX-based Layer 2 VPN. To stretch a Layer 2 network by using an HCX network extension instead, see the [VMware HCX documentation](https://docs.vmware.com/en/VMware-HCX/4.3/hcx-user-guide/GUID-4052AC3F-9FFC-4FA2-ACB4-18B21962F4D3.html).

Layer 2 VPN-based stretching of Layer 2 networks can work with or without NSX-based networks in your on-premises VMware environment. If you don't have NSX-based overlay networks for on-premises workloads, use an NSX-T Autonomous Edge, which has Data Plane Development Kit (DPDK)-enabled interfaces for high performance.

Stretching a Layer 2 network using NSX has the following advantages over using an HCX network extension:

  * Layer 2 VPN stretching in NSX supports use of a trunk interface.
  * Network throughput in NSX is higher than when using an HCX network extension.
  * NSX has fewer upgrades and less downtime compared to HCX.
  * An HCX network extension requires an on-premises vSphere Enterprise Plus license, but Layer 2 VPN stretching can function on an on-premises vSphere Standard license.



## Deployment scenario

To stretch your on-premises network using Layer 2 VPN, the described deployment scenario configures a Layer 2 VPN server and a Layer 2 VPN client. The process consists of the following major steps:

  1. In your on-premises environment, deploy the NSX-T Autonomous Edge (Layer 2 VPN client).
  2. In your private cloud, configure a Layer 2 VPN server on NSX-T Manager.
  3. In your on-premises environment, configure the Layer 2 VPN client on autonomous edge.
  4. (Optional) In your on-premises environment, deploy the secondary autonomous edge (Layer 2 VPN client) in HA mode.



Your private cloud is [connected to your on-premises environment](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-connect-to-onpremises) by either Cloud VPN or Cloud Interconnect. This setup ensures that a routing path exists between the tier-0 or tier-1 gateway in your private cloud and the autonomous edge client in your on-premises network.

![Layer 2 network stretches between an on-premises environment and a private cloud.](https://docs.cloud.google.com/static/vmware-engine/images/gcve-nsxt-layer2-stretch.svg)

For sample specifications of a Layer 2 VPN deployment, see the Sample Layer 2 VPN deployment section.

## Before you begin

Before you begin, do the following:

  * [Connect your on-premises environment](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-connect-to-onpremises) to your VPC network.
  * Identify the workload Layer 2 network you want to stretch to your private cloud.
  * Identify two VLANs in your on-premises environment for deploying your autonomous edge appliance (Layer 2 VPN client).
  * [Create a private cloud](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-create-private-cloud).
  * [Set up DNS forwarding](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-dns-on-premises) on the on-premises DNS servers so that the domain points to the private cloud DNS servers.
  * Allow UDP traffic on ports 500 and 4500 between the autonomous edge's uplink IP address and the local endpoint IP address to be used on the tier-0 or tier-1 gateway in your private cloud.



Additionally, verify that the following prerequisites are in place:

  * The on-premises vSphere version must be 6.7U1+ or 6.5P03+. The corresponding license must be at the Enterprise Plus level (for vSphere Distributed Switch).
  * The version of the autonomous edge appliance is compatible with the NSX-T Manager version used in your private cloud.
  * Round-trip time (RTT) latency is less than or equal to 150 ms, which is required for vMotion to work across the two sites (in case migration of workload is attempted).



### Limitations and considerations

The following table lists supported vSphere versions and network adaptor types:

vSphere version | Source vSwitch type | Virtual NIC driver | Target vSwitch type | Supported?  
---|---|---|---|---  
All | DVS | All | DVS | Yes  
vSphere 6.7UI or higher, 6.5P03 or higher | DVS | VMXNET3 | N-VDS | Yes  
vSphere 6.7UI or higher, 6.5P03 or higher | DVS | E1000 | N-VDS | [Not supported, per VMware](https://kb.vmware.com/s/article/56991)  
vSphere 6.7UI or 6.5P03, NSX-V or versions below NSX-T2.2, 6.5P03 or higher | All | All | N-VDS | [Not supported, per VMware](https://kb.vmware.com/s/article/56991)  
  
## Deploy the NSX-T Autonomous Edge (Layer 2 VPN client)

To deploy the NSX-T Autonomous Edge in your on-premises environment, build a trunk port group on-premises, and then create the autonomous edge using that port group.

### Create and configure a trunk port group

The following steps show how to create and configure a trunk port group:

  1. Create a distributed port group with **VLAN type** set to **VLAN trunking**. Provide the VLANs you want to stretch.

![Provide VLAN configuration settings for a new distributed port group.](https://docs.cloud.google.com/static/vmware-engine/images/gcve-create-port-group-vlan.svg)

  2. In the **Security** options, set both **Promiscuous mode** and **Forged transmits** to **Accept**.

  3. In the teaming and failover options, set **Load balancing** to **Use explicit failover order**.

  4. In the teaming and failover options, set **Active uplinks** to **uplink1** and **Standby uplinks** to uplink2.

  5. Complete the remaining port group creation steps.




### Deploy autonomous edge in your on-premises environment

The following steps show how to deploy NSX-T Autonomous Edge (Layer 2 VPN client) in your on-premises environment:

  1. [Contact Cloud Customer Care](https://docs.cloud.google.com/vmware-engine/docs/getting-support) to download the correct version of [NSX Edge for VMware ESXi](https://customerconnect.vmware.com/downloads/details?downloadGroup=NSX-T-312&productId=982&rPId=68714).
  2. Deploy the NSX Edge OVA as an OVF template.

     1. In the **Configuration** step, select the **Large** configuration to match the large form factor NSX Edges that come with your VMware Engine private cloud.
     2. In the **Select storage** step, select the datastore you want to use.
     3. In the **Select networks** step, provide the port groups to use for different traffic types:

        * **Network 0 (eth1 on the appliance):** Select the port group reserved for management traffic.
        * **Network 1 (eth2 on the appliance):** Select the port group reserved for uplink traffic.
        * **Network 2 (eth3 on the appliance):** Select the trunk port group.
        * **Network 3 (eth4 on the appliance):** Select the port group reserved for HA traffic. In the following image, the port group reserved for management traffic is used for HA traffic as well.

![Select destination networks for each source network during OVF template deployment.](https://docs.cloud.google.com/static/vmware-engine/images/gcve-nsx-ae-deployment-network.svg)

     4. In the **Customize template** step, enter the following details:

        1. In the **Application** section, do the following:

           1. Set the **System Root User Password**.
           2. Set the **CLI "admin" User Password**.
           3. Select the **Is Autonomous Edge** checkbox.
           4. Leave the remaining fields empty.
        2. In the **Network Properties** section, do the following:

           1. Set the **Hostname**.
           2. Set the **Default IPv4 Gateway**. This is the default gateway of the management network.
           3. Set the **Management Network IPv4 Address**. This is the management IP for the autonomous edge.
           4. Set the **Management Network Netmask**. This is the management network prefix length.
        3. In the **DNS** section, do the following:

           1. In the **DNS Server list** field, enter the DNS server IP addresses separated by spaces.
           2. In the **Domain Search List** field, enter the domain name.
        4. In the **Services Configuration** section, do the following:

           1. Enter the **NTP Server List**.
           2. Enter the **NTP Servers** , separated by spaces.
           3. Select the **Enable SSH** checkbox.
           4. Select the **Allow Root SSH logins** checkbox.
           5. Enter the logging server (if any).
        5. In the **External** section, do the following:

           1. Enter the **External Port** details in the following format: `VLAN ID,Exit Interface,IP,Prefix Length`. For example: `2871,eth2,172.16.8.46,28`. Replace the following values:

              * `VLAN ID`: VLAN ID of the uplink VLAN
              * `Exit Interface`: interface ID reserved for uplink traffic
              * `IP`: IP address reserved for the uplink interface
              * `Prefix Length`: prefix length for the uplink network
           2. In the **External Gateway** field, enter the default gateway of the uplink network.

        6. In the **HA** section, do the following:

           1. Enter the **HA Port** details in the following format: `VLAN ID,exitPnic,IP,Prefix Length`. For example: `2880,eth4,172.16.8.46,28`. Replace the following values:

              * `VLAN ID`: VLAN ID of the management VLAN
              * `exitPnic`: interface ID reserved for HA traffic
              * `IP`: IP address reserved for HA interface
              * `Prefix Length`: prefix length for HA network
           2. In the **HA Port Default Gateway** field, enter the default gateway of the management network. If using a different network for HA communication, supply the corresponding default gateway.

           3. Leave the remaining fields empty.

  3. Complete the remaining OVF template deployment steps.




## Configure Layer 2 VPN server on NSX-T Manager in your private cloud

The following steps describe how to configure Layer 2 VPN server on a tier-0 or tier-1 gateway in your private cloud NSX-T Manager.

### Create a Layer 2 VPN service

  1. In NSX-T Manager, go to **Networking > VPN > VPN Services > Add Service > IPSec**.
  2. Enter the following details to create an IPSec service:

     * Enter the **Name**.
     * In the **Tier0/Tier1 Gateway** column, select the gateway where you want the Layer 2 VPN server to run.
     * Leave the other fields blank.

![Create an IPSec VPN service in NSX-T Manager.](https://docs.cloud.google.com/static/vmware-engine/images/gcve-layer2-nsxt-ipsec-service.svg)

  3. Go to **Networking > VPN > Local Endpoints**.

  4. Enter the following details to create a local endpoint:

     * Enter the **Name**.
     * In the **VPN Service** column, select the IPSec VPN service you just created.
     * In the **IP Address** field, enter the IP address that's reserved for local endpoint, which will also be the IP address on which IPSec/Layer 2 VPN tunnel terminates.
     * In the **Local ID** field, enter the same reserved IP address.
     * Leave the other fields blank.
  5. Go to **Networking > VPN > VPN Services > Add Service > L2 VPN Server**.

  6. Enter the following details to create a Layer 2 VPN service:

     * Enter the **Name**.
     * In the **Tier0/Tier1 Gateway** column, select the gateway where you want the Layer 2 VPN server to run (same gateway used earlier in step 2).
     * Leave the other fields blank.



### Create a Layer 2 VPN session

  1. In NSX-T Manager, go to **Networking > VPN > L2 VPN Sessions > Add L2 VPN Session > L2 VPN Server**.
  2. Enter the following details to create a Layer 2 VPN session:

     * Enter the **Name**.
     * Select the **Local Endpoint/IP** created earlier in step 4 of Create a Layer 2 VPN service.
     * In the **Remote IP** field, enter the uplink IP address of the autonomous edge in your on-premises environment.
     * Enter the **Pre-shared key**.
     * In the **Tunnel Interface** field, enter one IP address from the reserved tunnel interface subnet.
     * In the **Remote ID** field, enter the value from **Remote IP**.
     * Leave the other fields blank.



### Create a network segment to extend to your on-premises VLAN

  1. In NSX-T Manager, go to **Networking > Segments > Add Segment**.
  2. Provide the following details to create a segment to extend to your on-premises VLAN:

     * Enter the **Segment Name**.
     * In the **Connected Gateway** field, select **None**.
     * For **Transport Zone** , select **TZ-Overlay**.
     * In the **L2 VPN** field, select the Layer 2 VPN session created earlier in Create a Layer 2 VPN session.
     * In the **VPN Tunnel ID** field, enter a unique tunnel ID (for example, 100). This tunnel ID must match the tunnel ID used when extending the VLAN from on-premises.
     * Leave the other fields blank.

![Create a network segment that includes a Layer 2 VPN session and VPN tunnel ID.](https://docs.cloud.google.com/static/vmware-engine/images/gcve-layer2-nsxt-add-segment-extend-onpremises.svg)

  3. Go to **Networking > VPN > L2 VPN Sessions**.

  4. Expand the **Session** and click **Download Config** to download the Layer 2 VPN configuration.

  5. Open the downloaded file using any text editor and copy the **peer_code** string without the quotes. You'll use this string later when configuring autonomous edge on-premises for Layer 2 VPN in subsequent sections.




### Advertise IPSec local endpoint IP to external network

This step varies depending on whether you use a tier-1 or tier-0 gateway for Layer 2 VPN services.

#### Advertise from a tier-0 gateway

If you use a tier-0 gateway, do the following to advertise the IPSec local endpoint IP from the tier-0 gateway to the external network:

  1. Go to **Networking > Tier-0 Gateways**.
  2. Edit the **Tier-0 Gateway** used for Layer 2 VPN (ideally Provider-LR).
  3. Expand **Route Re-Distribution**.
  4. In the **Tier-0 Subnets section** , select the **IPSec Local IP** checkbox.
  5. Click **Save**.
  6. Aggregate the **IPSec Local Endpoint subnet** on the tier-0 gateway. Router aggregation on the tier-0 gateway is needed so that the IPSec local endpoint is both reachable to the uplink IP of the on-premises autonomous edge and not filtered out in network fabric.

     1. Go to **Networking > Tier-0 Gateways**.
     2. Edit the selected **Tier-0 Gateway** used for Layer 2 VPN (ideally Provider-LR).
     3. Go to **BGP > Route Aggregation > Add Prefix**.
     4. In the **Prefix** column, enter the local endpoint network.
     5. In the **Summary-Only** column, select **Yes**.
     6. Click **Apply** and **Save**.



#### Advertise from a tier-1 gateway

If you use a tier-1 gateway for Layer 2 VPN services (like in the sample deployment), do the following steps instead:

  1. Aggregate the **IPSec Local Endpoint subnet** on the tier-0 gateway. Router aggregation on the tier-0 gateway is needed so that the IPSec local endpoint is both reachable to the uplink IP of the on-premises autonomous edge and not filtered out in network fabric.

     1. Go to **Networking > Tier-0 Gateways**.
     2. Edit the selected **Tier-0 Gateway** used for Layer 2 VPN (ideally Provider-LR).
     3. Go to **BGP > Route Aggregation > Add Prefix**.
     4. In the **Prefix** column, enter the local endpoint network.
     5. In the **Summary-Only** column, select **Yes**.
     6. Click **Apply** and **Save**.
  2. Go to **Networking > Tier-1 Gateways**.

  3. Edit the **Tier-1 Gateway** used for Layer 2 VPN (ideally Provider-LR).

  4. In the **Route Advertisement** section, enable the **IPSec Local Endpoint** toggle.

  5. Click **Save**.




## Configure Layer 2 VPN client on autonomous edge (on-premises)

The following steps show how to configure a Layer 2 VPN client on the autonomous edge deployed on-premises in Deploy the NSX-T Autonomous Edge:

  1. Sign in to NSX-T Autonomous Edge at its management appliance IP address.
  2. Add a Layer 2 VPN session:

     1. Go to **L2 VPN** and click **Add Session**.
     2. Enter the following details:

        * In the **Session Name** field, enter the session name configured in Create a Layer 2 VPN session.
        * Set **Admin Status** to **Enabled**.
        * In the **Local IP** field, enter the uplink IP address of autonomous edge.
        * In the **Remote IP** field, enter the IP address configured as a local endpoint in Configure Layer 2 VPN server on NSX-T Manager in your private cloud.
        * In the **Peer code** field, enter the **peer_code** string copied in Configure Layer 2 VPN server on NSX-T Manager in your private cloud.
     3. Click **Save**.

  3. Extend the on-premises VLAN:

     1. Go to **Port** and click **Add Port**.
     2. Enter the following details:

        * In the **Port Name** field, enter the port name.
        * Leave the **Subnet** field blank.
        * In the **VLAN** field, enter the VLAN ID of the on-premises VLAN to be extended.
        * For **Exit Interface** , select the uplink interface (like eth2).
     3. Click **Save**.

  4. Attach the port to the L2 VPN Session.

     1. Go to **L2 VPN** and click **Attach Port**.
     2. Enter the following details:

        * Select the **L2 VPN Session** previously created in step 2.
        * Select the **Port** previously created in step 3.
        * In the **Tunnel ID** field, enter the same tunnel ID used to extend the segment in your private cloud (in Configure Layer 2 VPN server on NSX-T Manager in your private cloud).
     3. The Layer 2 VPN session appears in the table with a **Status** of "UP". The on-premises VLAN is now extended to the VMware Engine private cloud (extended segment). Workloads attached to the on-premises extended VLAN become reachable to workloads attached to extended segment in your VMware Engine private cloud.




## Deploy the secondary NSX-T Autonomous Edge (Layer 2 VPN client) in HA mode

Optionally, use the following steps to deploy a secondary NSX-T Autonomous Edge (Layer 2 VPN client) in HA mode in your on-premises environment:

  1. Follow the steps in Deploy NSX-T Autonomous Edge in your on-premises environment until you reach the **Customize template** step.
  2. On the **Customize template** step, do the following instead:

     1. In the **Application** section, enter the following details:

        * Set the **System Root User Password**.
        * Set the **CLI "admin" User Password**.
        * Select the **Is Autonomous Edge** checkbox.
        * Leave every other field empty.
     2. In the **Network Properties** section, enter the following details:

        * Set the **Hostname**.
        * Set the **Default IPv4 Gateway**. This is the default gateway of the management network.
        * Set the **Management Network IPv4 Address**. This is the management IP for the secondary autonomous edge.
        * Set the **Management Network Netmask**. This is the management network prefix length.
     3. In the **DNS section** , enter the following details:

        * Enter the **DNS Server list**.
        * Enter the **DNS Server IP addresses** , separated by spaces.
        * Enter the **Domain Search List**.
        * Enter the **Domain name**.
     4. In the **Services Configuration** section, enter the following details:

        * Enter the **NTP Server List**.
        * Enter the **NTP Servers** , separated by spaces.
        * Select the **Enable SSH** checkbox.
        * Select the **Allow Root SSH logins** checkbox.
        * Enter the logging server (if any).
     5. Leave the **External** section empty.

     6. In the **HA section** , enter the following details:

        * Enter the **HA Port** details in the following format: `VLAN ID,exitPnic,IP,Prefix Length`. For example: `2880,eth4,172.16.8.11,28`. Replace the following values:

          * `VLAN ID`: VLAN ID of the management VLAN
          * `exitPnic`: interface ID reserved for HA traffic
          * `IP`: IP address reserved for the HA interface for the secondary autonomous edge
          * `Prefix Length`: prefix length for the HA network
        * In the **HA Port Default Gateway** field, enter the default gateway of the management network.

        * Select the **Secondary API Node** checkbox.

        * In the **Primary Node Management IP** field, enter the management IP address of the primary autonomous edge.

        * In the **Primary Node Username** field, enter the username of the primary autonomous edge (for example, "admin").

        * In the **Primary Node Password** field, enter the password of the primary autonomous edge.

        * In the **Primary Node Management Thumbprint** field, enter the API thumbprint of the primary autonomous edge. You can get this by connecting using SSH to the primary autonomous edge using admin credentials and running the `get certificate api thumbprint` command.

  3. Complete the remaining OVF template deployment steps to deploy the secondary autonomous edge (on-premises Layer 2 VPN client).




The resulting autonomous edge has a **High Availability Status** of **Active**.

## Sample Layer 2 VPN deployment

The following tables provide specifications for a sample Layer 2 VPN deployment.

### On-premises network to be stretched

Network property | Value  
---|---  
VLAN | 2875  
CIDR | 172.16.8.16/28  
  
### On-premises network where the autonomous edge is deployed

Network property | Value  
---|---  
Management VLAN | 2880  
Management CIDR | 172.16.8.0/28  
Uplink VLAN | 2871  
Uplink CIDR | 172.16.8.32/28  
HA VLAN (same as management) | 2880  
HA CIDR (same as management) | 172.16.8.0/28  
Primary autonomous edge management IP address | 172.16.8.14  
Primary autonomous edge uplink IP address | 172.16.8.46  
Primary autonomous edge HA IP address | 172.16.8.12  
Secondary autonomous edge management IP address | 172.16.8.13  
Secondary autonomous edge HA IP address | 172.16.8.11  
  
### Private cloud IP schema for NSX tier-1 router (Layer 2 VPN server)

Network property | Value  
---|---  
Local endpoint IP address | 192.168.198.198  
Local endpoint network | 192.168.198.198/31  
Tunnel interface | 192.168.199.1/30  
Segment (stretched) | L2 VPN-Seg-test  
Loopback interface (NAT IP address) | 104.40.21.81  
  
### Private cloud network to map to the stretched network

Network property | Value  
---|---  
Segment (stretched) | L2 VPN-Seg-test  
CIDR | 172.16.8.16/28  
  
## What's next

  * For more information about extending on-premises networks using NSX Layer 2 VPN, see the VMware documentation [Understanding Layer 2 VPN](https://docs.vmware.com/en/VMware-NSX-T-Data-Center/3.0/administration/GUID-86C8D6BB-F185-46DC-828C-1E1876B854E8.html).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
