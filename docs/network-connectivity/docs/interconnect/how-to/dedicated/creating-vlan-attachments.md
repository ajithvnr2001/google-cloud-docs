---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments/
title: Create VLAN attachments \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:00:11.398085+00:00
---

# Create VLAN attachments  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Create VLAN attachments Stay organized with collections  Save and categorize content based on your preferences. 

VLAN attachments (also known as `interconnectAttachments`) determine which Virtual Private Cloud (VPC) networks can reach your on-premises network through a Dedicated Interconnect connection. You can create VLAN attachments over connections that have [passed all tests](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/testing-connections) and are ready to use.

You can create unencrypted VLAN attachments or encrypted VLAN attachments. Encrypted VLAN attachments are used in HA VPN over Cloud Interconnect deployments. You can create unencrypted VLAN attachments that are single stack (IPv4 only) or dual stack (IPv4 and IPv6).

By default, when you create an unencrypted VLAN attachment, the VLAN attachment is single stack (IPv4 only). Unless you specify otherwise, the interface that you create for your unencrypted VLAN attachment is a single interface with an IPv4 address and the resulting BGP session exchanges only IPv4 routes.

If you need to support IPv6 traffic, you must configure a dual-stack (IPv4 and IPv6) unencrypted VLAN attachment. With a dual-stack VLAN attachment, you can create an IPv4 BGP session, an IPv6 BGP session, or you can create both.

Encrypted VLAN attachments are always configured to be IPv4 only. If you want to support IPv6 traffic in your encrypted attachments for an HA VPN over Cloud Interconnect deployment, you can deploy configure dual-stack HA VPN gateways and tunnels.

Billing for VLAN attachments starts when you create them and stops when you delete them.

If you are using VLAN attachments located in different [Google Cloud regions](https://docs.cloud.google.com/docs/geography-and-regions) than your Dedicated Interconnect connection, then [change your VPC network's dynamic routing mode](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/create-network-set-modes#change-network-modes) to **Global**.

VLAN attachments are subject to [vlan attachment related quotas](https://docs.cloud.google.com/network-connectivity/docs/interconnect/quotas#quotas). Request a higher quota for increased attachments or bandwidth.

If you need to create a VLAN attachment for a connection in another Google Cloud project, see [Use Dedicated Interconnect connections in other projects](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/using-interconnects-other-projects).

For VLAN attachments for Partner Interconnect, see [Create VLAN attachments for Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/creating-vlan-attachments).

For definitions of terms used on this page, see [Cloud Interconnect key terms](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology).

To help you solve common issues that you might encounter when using Dedicated Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting).

## Associate VLAN attachments with a Cloud Router

For Dedicated Interconnect, the VLAN attachment allocates a VLAN on a connection and associates that VLAN with the specified [Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview). It is possible to associate multiple, different VLAN attachments to the same Cloud Router.

When you create the VLAN attachment, specify a Cloud Router that's in the region that contains the subnets that you want to reach. The VLAN attachment automatically allocates a VLAN ID and Border Gateway Protocol (BGP) peering IP addresses. Use that information to configure your on-premises router and establish a BGP session with your Cloud Router.

Optionally, you can manually specify link-local candidate subnets for IPv4 BGP addresses when you create the VLAN attachment. Cloud Router selects IPv4 addresses from this range for the interface and the BGP peer. These IPv4 addresses can't be modified after they have been selected. The BGP IPv4 address range that you specify as a candidate must be unique among all Cloud Routers in all regions of a VPC network.

Instead of configuring link-local candidate subnets for your IPv4 BGP addresses, you can specify custom IP addresses for both the Cloud Router and customer router ends of your VLAN attachments. For more information about custom IP address ranges, see [Custom IP address ranges](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview#custom-ip).

You can't manually specify candidate subnets for IPv6 addresses when creating your VLAN attachment, but you can specify custom IP address ranges.

For HA VPN over Cloud Interconnect, you must create a Cloud Router that is used exclusively with encrypted VLAN attachments. The Cloud Router only exchanges routes for the VPN gateways over the VLAN attachments, which ensures that only encrypted traffic egresses the attachments. You can't use this Cloud Router for any unencrypted VLAN attachments or for any VPN tunnels.

## Utilize multiple VLAN attachments

Each VLAN attachment supports a maximum bandwidth of 400 Gbps in increments described on the [Pricing](https://docs.cloud.google.com/network-connectivity/docs/interconnect/pricing) page, and a maximum packet rate as documented in [Cloud Interconnect limits](https://docs.cloud.google.com/network-connectivity/docs/interconnect/quotas#limits). This is true even if the attachment is configured on a connection that has a greater bandwidth capacity than the attachment.

To fully use the bandwidth of a connection, you might need to create multiple VLAN attachments.

**Note:** Creating VLAN attachments with a combined bandwidth greater than the Dedicated Interconnect connection doesn't give you more than the maximum stated bandwidth of the connection:

  * To use a 20-Gbps attachment, you need at least a 2 x 10-Gbps Dedicated Interconnect connection or a 100-Gbps connection.
  * To use a 50-Gbps attachment, you need at least a 5 x 10-Gbps Dedicated Interconnect connection or a 100-Gbps connection.



To use multiple VLAN attachments simultaneously for egress traffic in a VPC network, create them in the same region. Then configure your on-premises router to advertise routes with the same MED. The custom dynamic routes, learned through BGP sessions on one or more Cloud Routers that manage the VLAN attachments, are applied to your VPC network with a route priority corresponding to the MED.

When multiple available routes have the same priority, Google Cloud distributes traffic among them by using a five-tuple hash for affinity, implementing an equal-cost multipath (ECMP) routing design. For more information, see [Applicability and order](https://docs.cloud.google.com/vpc/docs/routes#instancerouting) in the VPC documentation.

## Create unencrypted VLAN attachments

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following Identity and Access Management (IAM) roles.

**Permissions**

  * `compute.interconnects.use`
  * `compute.interconnectAttachments.create`
  * `compute.interconnectAttachments.get`
  * `compute.routers.create`
  * `compute.routers.get`
  * `compute.routers.update`



**Roles**

  * `roles/owner`
  * `roles/editor`
  * `roles/compute.networkAdmin`



###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **VLAN attachments** tab.

[Go to VLAN attachments](https://console.cloud.google.com/hybrid/interconnects/list?tab=attachments)

  2. Click **Create VLAN attachments**.

  3. Select **Dedicated Interconnect connection**

  4. In the **Encrypt interconnect** section, select **Set up unencrypted Interconnect** , and then click **Continue**.

  5. To create attachments in your project, in the **Select interconnects & redundancy** section, select **In this project**. For other projects, see [Use Dedicated Interconnect connections in other projects](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/using-interconnects-other-projects).

  6. Select an existing Dedicated Interconnect connection in your project, and then click **Continue**.

  7. Select **Add VLAN attachment** , and then specify the following details:

     * **Name** : A name for the attachment. This name is displayed in the Google Cloud console and is used by the Google Cloud CLI to reference the attachment—for example, `my-attachment`.
     * **Description** (optional): A description of the attachment.
  8. Select a stack type for the attachment, either **IPv4 (single stack)** or **IPv4 and IPv6 (dual stack)**.

  9. Select a **Cloud Router** to associate with this attachment. The Cloud Router must be in the VPC network that you want to connect to.

If you don't have an existing Cloud Router, select **Create new router**. For the BGP AS number, use any private ASN (`64512-65534` or `4200000000-4294967294`) or `16550`.

  10. Optional: To specify a VLAN ID, a specific IP address range for the BGP session, the VLAN attachment's capacity, or the maximum transmission unit (MTU), click **VLAN ID, BGP IPs, capacity, MTU**.

     * To specify a VLAN ID, in the **VLAN ID** section, select **Customize**.

By default, Google automatically generates a VLAN ID. You can specify a VLAN ID in the range 2-4093. You can't specify a VLAN ID that is already in use on the connection. If your VLAN ID is in use, you are asked to choose another one.

If you don't enter a VLAN ID, an unused, random VLAN ID is automatically selected for the VLAN attachment.

     * To specify an IPv4 address range for the BGP session, in the **Allocate BGP IPv4 address** section, select **Specify a candidate link-local range** or **Specify custom IP address** , then enter an IP address range or an IP address respectively.

**Candidate link-local range** : The BGP IPv4 address range that you specify must be unique among all Cloud Routers in all regions of a VPC network.

IPv4 addresses used for the BGP session between a Cloud Router and your on-premises router are allocated from the IPv4 link-local address space (`169.254.0.0/16`). By default, Google selects unused addresses from the IPv4 link-local address space.

To restrict the IPv4 range that Google selects from, you can specify up to 16 prefixes from the IPv4 link-local address space. All prefixes must reside within `169.254.0.0/16` and must have a prefix length of `/29` or shorter, for example, `/29` or `/28`. An unused `/29` range is automatically selected from your specified prefix. The address allocation request fails if all possible `/29` ranges are in use by Google Cloud.

If you don't supply a range of prefixes, Google Cloud picks a `/29` address allocation from `169.254.0.0/16` that is not already used by any BGP session in your VPC network. If you supply one or more prefixes, Google Cloud picks an unused `/29` address allocation from the supplied prefixes.

After the `/29` address range is selected, Google Cloud assigns the Cloud Router one address and your on-premises router another address. The rest of the address space in the `/29` prefix is reserved for Google's use.

**Custom IP address** : For more information about prerequisites, limitations and why you might use custom IP address ranges, see [Custom IP address ranges](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview#custom-ip).

Note that you can't combine custom IPv4 addresses with candidate subnets. In addition, if you use the _dual stack_ stack type, you can choose to set custom IP addresses for only your IPv4 addresses, only your IPv6 addresses, or both your IPv4 and IPv6 addresses; you can combine custom IP addresses in one field with automatic allocation or candidate link-local ranges in the other field if those options are available.

In the **Cloud Router IP** field, enter the IPv4 CIDR address that you want to assign to the Cloud Router end of your VLAN attachment, like `192.0.2.1/29`. Then, in the **Peer IP** field, enter the IPv4 CIDR address that you want to assign to the customer router end of your VLAN attachment.

If you selected **IPv4 and IPv6 (dual stack)** , you must also select one of the options in the **Allocate BGP IPv6 address** section. In the **Cloud Router IPv6** field, enter the IPv6 CIDR address that you want to assign to the Cloud Router end of your VLAN attachment, like `2001:db8::1/125`. Then, in the **Peer IPv6** field, enter the IPv6 CIDR address that you want to assign to the customer router end of your VLAN attachment.

     * To specify the maximum bandwidth, in the **Capacity** field, select a value. If you don't select a value, Cloud Interconnect uses 10 Gbps.

If you have multiple VLAN attachments on a connection, the capacity setting helps you control how much bandwidth each attachment can use. The maximum bandwidth is approximate, so it's possible for VLAN attachments to use more bandwidth than the selected capacity.

     * To specify the **maximum transmission unit (MTU)** for the attachment, select a value from the field.

To make use of a 1460-, 1500-, or 8896-byte MTU, [the VPC network that uses the attachment must set an MTU to the same value](https://docs.cloud.google.com/vpc/docs/mtu). In addition, the on-premises virtual machine (VM) instances and routers must set their MTU to the same value. If your network has the default MTU of `1460`, then select an MTU of `1460` for your attachment.

  11. If you want to connect multiple VPC networks (for example, to build redundancy), click **\+ Add VLAN attachment** to attach additional VLANs to your connection. Choose a different Cloud Router for each VLAN attachment. For more information, see the [Redundancy section](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview#redundancy) in the overview.

  12. When you have created all needed VLAN attachments, click **Create**. The attachment takes a few moments to create.

The **Configure BGP sessions** page shows each VLAN attachment and its configuration status.

  13. For each VLAN attachment, create a BGP session to exchange BGP routes between your Cloud Router network and your on-premises router. Click **Configure** , and then enter the following information:

     * **Name** : A name for the BGP session.
     * **Peer ASN** : The public or private ASN of your on-premises router.
     * **Advertised route priority (MED)** (optional): The base value that Cloud Router uses to calculate route metrics. All routes advertised for this session use this base value. For more information, see [Advertised prefixes and priorities](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#advertised-priority).
     * **BGP peer** : Lets you enable or disable the BGP session with this peer. If disabled, this Cloud Router does not send BGP connection requests and rejects all BGP connection requests from this peer.
     * **MD5 authentication** (optional): Lets you authenticate BGP sessions between Cloud Router and its peers. For instructions about how to use MD5 authentication, see [Use MD5 authentication](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication).
     * [**Custom advertised routes**](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#overview-am-custom) (optional): Lets you choose which routes Cloud Router advertises to your on-premises router through BGP. For configuration steps, see the [overview for custom advertised routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes).
     * [**Custom learned routes**](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/custom-learned-routes): Lets you manually define additional learned routes for a BGP session. The Cloud Router behaves as if it learned the routes from the BGP peer.
     * [**Bidirectional forwarding detection (BFD) for Cloud Router**](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd) (optional): Detects forwarding path outages such as link down events, allowing for more resilient hybrid networks. For instructions about how to update a BGP session to use BFD, see [Configuring BFD](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-bfd).

**Important:** BFD can only be enabled on provisioned VLAN attachments that use Dataplane version 2. You can view the `dataplaneVersion` for a VLAN attachment by viewing the attachment details in one of the following ways:

       * **API** : Use the [interconnectAttachments.get](https://docs.cloud.google.com/compute/docs/reference/rest/v1/interconnectAttachments/get) method. You can use this method on VLAN attachments for either Dedicated Interconnect or Partner Interconnect. 
       * **Google Cloud CLI** : Use the `gcloud compute interconnects attachments describe ATTACHMENT-NAME` command where ATTACHMENT-NAME is the name of the VLAN attachment for either Dedicated Interconnect or Partner Interconnect. 

In the output of the API or gcloud CLI command, look for the `dataplaneVersion` field with a value of `2`. If the field is absent from the output, the VLAN attachment is using version 1 and cannot be used with BFD. For more information, contact your customer account team.

The Cloud Interconnect Dataplane v2 is unrelated to [ Google Kubernetes Engine (GKE) Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2)

  14. Click **Save and continue**.

  15. After you add BGP sessions for all your VLAN attachments, click **Save configuration**. The BGP sessions that you configured are inactive until you configure BGP on your on-premises router.




###  gcloud 

Before you create a VLAN attachment, you must have an existing Cloud Router in the network and region that you want to reach from your on-premises network. If you don't have an existing Cloud Router, [create one](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/create-router-vpc-network). The Cloud Router must have a BGP ASN of `16550`, or you can use any private ASN (`64512-65534` or `4200000000-4294967294`).

  1. Create a VLAN attachment. The attachment allocates a VLAN on your connection that connects to the Cloud Router.
         
         gcloud compute interconnects attachments dedicated create ATTACHMENT_NAME \
             --region=REGION \
             --router=ROUTER_NAME \
             --interconnect=INTERCONNECT_NAME
         

Replace the following:

     * `ATTACHMENT_NAME`: the name of your VLAN attachment
     * `REGION`: the region that your Cloud Router is located in
     * `ROUTER_NAME`: the name of the Cloud Router that this VLAN attachment connects to
     * `INTERCONNECT_NAME`: the name of your Dedicated Interconnect connection

**Dual-stack (IPv4 and IPv6) VLAN attachment**

To create a dual-stack VLAN attachment that can support both IPv4 and IPv6 traffic, specify `--stack-type IPV4_IPV6`:
    
    gcloud compute interconnects attachments dedicated create ATTACHMENT_NAME \
        --region=REGION \
        --router=ROUTER_NAME \
        --interconnect=INTERCONNECT_NAME \
        --stack-type=IPV4_IPV6
    

When you create a VLAN attachment with the `IPV4_IPV6` (dual stack) stack type, Google Cloud automatically assigns an unused `/125` CIDR from the `2600:2d00:0:1::/64` range as the IPv6 address for the VLAN attachment.

If you select the `IPV4_IPV6` (dual stack) stack type, you can configure the VLAN attachment later with an IPv4 BGP session, an IPv6 BGP session, or both.

If you omit the `--stack-type` flag, the VLAN attachment is configured as an IPv4-only (single stack) attachment. An `IPV4_ONLY` (single stack) VLAN attachment can exchange only IPv4 routes. You can also change the stack type of an attachment after you create it. See [Modify stack type](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/modifying-vlan-attachments#modify_stack_type).

**Allocate IPv4 addresses for BGP peering**

For BGP peering, Google can allocate unused IPv4 addresses from the IPv4 link-local address space (`169.254.0.0/16`). To constrain the range of IPv4 addresses that Google can select from, you can use the `--candidate-subnets` flag, as shown in the following example.

The BGP peering IPv4 address range that you specify must be unique among all Cloud Routers in all regions of a VPC network.
    
    gcloud compute interconnects attachments dedicated create ATTACHMENT_NAME \
        --region=REGION \
        --router=ROUTER_NAME \
        --interconnect=INTERCONNECT_NAME \
        --candidate-subnets=CANDIDATE_SUBNETS
    

Replace `CANDIDATE_SUBNETS` with a comma-delimited list link-local IP address ranges that Google Cloud uses for the BGP session that managed routes for the VLAN attachment—for example, `169.254.0.0/29,169.254.10.0/24`.

You can specify a range of up to 16 prefixes from the IPv4 link-local address space. All prefixes must reside within `169.254.0.0/16` and must be a `/29` or shorter, for example, `/28` or `/27`. An unused `/29` is automatically selected from your specified range of prefixes. The address allocation request fails if all possible `/29` prefixes are in use by Google Cloud.

You can specify candidate subnet ranges for IPv4 addresses only. You can't specify a candidate subnet range for IPv6 addresses.

**Configure custom IP address ranges**

If you want to use custom IP address ranges, add the `--candidate-customer-router-ip-address` and `--candidate-cloud-router-ip-address` flags, which also support link-local IP addresses. Note that you can't combine these flags with the `--candidate-subnets` and `--subnet-length` fields, but you can use `--candidate-subnets` for link-local IPv4 attachments with the `--candidate-customer-router-ipv6-address` and `--candidate-cloud-router-ipv6-address` flags.

For more information about prerequisites, limitations and why you might use custom IP address ranges, see [Custom IP address ranges](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview#custom-ip).
    
    gcloud compute interconnects attachments dedicated create ATTACHMENT_NAME \
        --project=PROJECT_ID \
        --region=REGION \
        --router=ROUTER_NAME \
        --candidate-cloud-router-ip-address=CANDIDATE_CLOUD_ROUTER_IP_ADDRESS \
        --candidate-customer-router-ip-address=CANDIDATE_CUSTOMER_ROUTER_IP_ADDRESS
    

Replace the following:

     * `CANDIDATE_CLOUD_ROUTER_IP_ADDRESS`: the IPv4 CIDR address that you want to assign to the Cloud Router end of your VLAN attachment, like `192.0.2.1/29`
     * `CANDIDATE_CUSTOMER_ROUTER_IP_ADDRESS`: the IPv4 CIDR address that you want to assign to the customer router end of your VLAN attachment

If you use IPv6 dual-stack attachments, use the following command:
    
    gcloud compute interconnects attachments dedicated create ATTACHMENT_NAME \
        --project=PROJECT_ID \
        --region=REGION \
        --router=ROUTER_NAME \
        --stack-type=IPV4_IPV6 \
        --candidate-cloud-router-ipv6-address=CANDIDATE_CLOUD_ROUTER_IP_ADDRESS \
        --candidate-customer-router-ipv6-address=CANDIDATE_CUSTOMER_ROUTER_IP_ADDRESS
    

Replace the following:

     * `CANDIDATE_CLOUD_ROUTER_IP_ADDRESS`: the IPv6 CIDR address that you want to assign to the Cloud Router end of your VLAN attachment, like `2001:db8::1/125`
     * `CANDIDATE_CUSTOMER_ROUTER_IP_ADDRESS`: the IPv6 CIDR address that you want to assign to the customer router end of your VLAN attachment

You can use the `--candidate-cloud-router-ip-address` and `--candidate-customer-router-ip-address` flags alongside the `--candidate-cloud-router-ipv6-address` and `--candidate-customer-router-ipv6-address` flags to create an attachment that uses both IPv4 and IPv6 custom address ranges.

**VLAN ID configuration**

To specify a VLAN ID, use the `--vlan` flag, as shown in the following example:
    
    gcloud compute interconnects attachments dedicated create ATTACHMENT_NAME \
        --region=REGION \
        --router=ROUTER_NAME \
        --interconnect=INTERCONNECT_NAME \
        --vlan=5
    

By default, Google automatically generates a VLAN ID. You can specify a VLAN ID in the range 2-4093. You can't specify a VLAN ID that is already in use on the Dedicated Interconnect connection. If your VLAN ID is in use, you are asked to choose another one.

If you don't enter a VLAN ID, an unused, random VLAN ID is automatically selected for the VLAN attachment.

**Maximum bandwidth configuration**

To specify the attachment's maximum bandwidth, use the `--bandwidth` flag, as shown in the following example. If you have multiple VLAN attachments on a connection, the capacity setting helps you control how much bandwidth each attachment can use. The maximum bandwidth is approximate, so it's possible for VLAN attachments to use more bandwidth than the selected capacity.
    
    gcloud compute interconnects attachments dedicated create ATTACHMENT_NAME \
        --region=REGION \
        --router=ROUTER_NAME \
        --interconnect=INTERCONNECT_NAME \
        --bandwidth=500M
    

If you don't specify a capacity, Cloud Interconnect uses the default of 10 Gbps. For more information, see the [`gcloud compute interconnects attachments dedicated create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/dedicated/create) reference.

**MTU configuration**

The default MTU of an attachment is 1440 bytes. You can also specify an attachment MTU of 1460, 1500, or 8896 bytes. To specify an MTU of 1460, 1500, or 8896 bytes for the attachment, use the `--mtu` flag, as shown in the following example:
    
    gcloud compute interconnects attachments dedicated create ATTACHMENT_NAME \
        --region=REGION \
        --router=ROUTER_NAME \
        --interconnect=INTERCONNECT_NAME \
        --mtu=1500
    

To make use of a 1460, 1500 or 8896-byte MTU, the VPC network that uses the attachment and the on-premises systems and routers must all have the same [MTU value set](https://docs.cloud.google.com/vpc/docs/mtu).

  2. Describe the attachment to retrieve the resources that it allocated, such as the VLAN ID and BGP peering addresses, as shown in the following example. Use these values to configure your Cloud Router and your on-premises router.
         
         gcloud compute interconnects attachments describe ATTACHMENT_NAME \
             --region=REGION
         

The output is similar to the following: 
         
         **cloudRouterIpAddress: 169.254.180.81/29**
         creationTimestamp: '2022-03-22T10:31:40.829-07:00'
         **customerRouterIpAddress: 169.254.180.82/29**
         dataplaneVersion: 2
         id: '2973197662755397267'
         interconnect: https://www.googleapis.com/compute/v1/projects/my-project/global/interconnects/myinterconnect
         kind: compute#interconnectAttachment
         mtu: 1500
         name: my-attachment
         operationalStatus: ACTIVE
         privateInterconnectInfo:
           tag8021q: 1000
         region: https://www.googleapis.com/compute/v1/projects/my-project/regions/us-central1
         router: https://www.googleapis.com/compute/v1/projects/my-project/regions/us-central1/routers/my-router
         **stackType: IPV4_ONLY**
         state: ACTIVE
         type: DEDICATED
         **vlanTag8021q: 1000**
         

     * The `cloudRouterIpAddress` value (`169.254.180.81/29`) is an IPv4 link-local address. When you create a Cloud Router interface for this attachment, the interface uses this IP address. You use this same address for the BGP neighbor on your on-premises router.

     * The `customerRouterIpAddress` value (`169.254.180.82/29`) is an IPv4 link-local address. On the Cloud Router, configure a BGP peer with this address over the interface that has the Cloud Router address assigned to it. You assign this address to the VLAN subinterface on your on-premises router.

     * The `stackType` value (`IPV4_ONLY`) indicates the type of traffic supported by the VLAN attachment.

     * The `vlanTag8021q` value (`1000`) identifies traffic that goes across this attachment. You need this value to configure a tagged VLAN subinterface on your on-premises router.

  3. On your Cloud Router, add the interface or interfaces that connect to the VLAN attachment.

     * If your VLAN attachment is IPv4-only, you must create an interface with an IPv4 address.

     * If your VLAN attachment uses the `IPV4_IPV6` (dual stack) stack type, you can create an interface with an IPv4 address, an interface with an IPv6 address, or you can create both.

Creating both an interface with an IPv4 address and an interface with an IPv6 address lets you run two BGP sessions in parallel over the same VLAN attachment. For more information, see [Establish BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-bgp) in the Cloud Router documentation.

To create an interface with an IPv4 address, run the following command.
           
           gcloud compute routers add-interface ROUTER_NAME \
               --region=REGION \
               --interface-name=IPV4_INTERFACE_NAME \
               --interconnect-attachment=ATTACHMENT_NAME
           

Replace `IPV4_INTERFACE_NAME` with a name for this interface.

The IPv4 address of an interface is automatically configured using your attachment's `cloudRouterIpAddress`.

To create an interface with an IPv6 address, run the following command.
           
           gcloud beta compute routers add-interface ROUTER_NAME \
               --region=REGION \
               --interface-name=IPV6_INTERFACE_NAME \
               --interconnect-attachment=ATTACHMENT_NAME \
               --ip-version=IPV6
           

Replace `IPV6_INTERFACE_NAME` with a name for this interface.

The IPv6 address of an interface is automatically configured using your attachment's `cloudRouterIpv6Address`.

  4. Add a BGP peer for each interface that you created:
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
             --interface=IPV4_INTERFACE_NAME \
             --region=REGION \
             --peer-name=IPV4_BGP_PEER_NAME \
             --peer-asn=PEER_ASN
         

Replace the following:

     * `IPV4_BGP_PEER_NAME`: a name for this BGP peer.

     * `PEER_ASN`: the same ASN that you configured on your on-premises router.

The BGP peer's IPv4 address is automatically configured using your attachment's `customerRouterIpAddress`.
    
    gcloud compute routers add-bgp-peer ROUTER_NAME \
          --interface=IPV6_INTERFACE_NAME \
          --region=REGION \
          --peer-name=IPV6_BGP_PEER_NAME \
          --peer-asn=PEER_ASN
    

Replace `IPV6_BGP_PEER_NAME` with a name for this BGP peer.

The peer's IPv6 address is automatically configured using your attachment's `customerRouterIpv6Address`.

**Multiprotocol BGP (MP-BGP) configuration**

If you configured the VLAN attachment with the `IPV4_IPV6` (dual stack) stack type, you can use multiprotocol BGP (MP-BGP) in your single IPv4 BGP or single IPv6 BGP session. You can't use MP-BGP if you're using both BGP sessions.

With MP-BGP, you can exchange IPv6 routes over an IPv4 BGP session or you can exchange IPv4 routes over an IPv6 BGP session.

To enable IPv6 route exchange in an IPv4 BGP session, run the following command.
    
    gcloud compute routers add-bgp-peer ROUTER_NAME \
        --interface=IPV4_INTERFACE_NAME \
        --region=REGION \
        --peer-name=IPV4_BGP_PEER_NAME \
        --peer-asn=PEER_ASN \
        **--enable-ipv6**
    

If you omit the `--enable-ipv6` flag, the IPv4 BGP session exchanges only IPv4 routes. You can also enable IPv6 route exchange in the BGP session at a later time.

To enable IPv4 route exchange in an IPv6 BGP session, run the following command.
    
    gcloud beta compute routers add-bgp-peer ROUTER_NAME \
        --interface=IPV6_INTERFACE_NAME \
        --region=REGION \
        --peer-name=IPV6_BGP_PEER_NAME \
        --peer-asn=PEER_ASN \
        **--enable-ipv4**
    

For more information, see [Configure multiprotocol BGP for IPv4 or IPv6 BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-mp-bgp).

If you enable IPv6 route exchange in your IPv4 BGP session, you must configure your on-premises router to advertise its IPv6 routes with your attachment's `customerRouterIpv6Address` as the next hop.

If you enable IPv4 route exchange in your IPv6 BGP session, you must configure your on-premises router to advertise its IPv4 routes with your attachment's `customerRouterIpAddress` as the next hop.

Describe the attachment to retrieve the IPv4 or IPv6 next hop address.
    
    gcloud compute interconnects attachments describe ATTACHMENT_NAME \
        --region=REGION
    

The output is similar to the following:
    
    cloudRouterIpAddress: 169.254.180.81/29
    cloudRouterIpv6Address: 2600:2d00:0:1:8000:12:0:299/125
    creationTimestamp: '2022-03-22T10:31:40.829-07:00'
    customerRouterIpAddress: 169.254.180.82/29
    customerRouterIpv6Address: 2600:2d00:0:1:8000:12:0:29a/125
    dataplaneVersion: 2
    id: '2973197662755397267'
    interconnect: https://www.googleapis.com/compute/v1/projects/my-project/global/interconnects/myinterconnect
    kind: compute#interconnectAttachment
    mtu: 1500
    name: my-attachment
    operationalStatus: ACTIVE
    privateInterconnectInfo:
      tag8021q: 1000
    region: https://www.googleapis.com/compute/v1/projects/my-project/regions/us-central1
    router: https://www.googleapis.com/compute/v1/projects/my-project/regions/us-central1/routers/my-router
    stackType: IPV4_IPV6
    state: ACTIVE
    type: DEDICATED
    vlanTag8021q: 1000
    

**Custom advertised route and MED value configuration**

To specify a base MED value, use the `--advertised-route-priority` flag. Cloud Router uses this value to calculate route metrics for all routes that it advertises for this session. For more information, see [Advertised prefixes and priorities](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#advertised-priority) in the Cloud Router documentation.

You can also use the `--advertisement-mode` flag to enable [custom advertisement mode](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#overview-am-custom) for this BGP session. Use `--advertisement-groups` and `--advertisement-ranges` to define the custom advertised routes for the BGP session. Custom advertised routes let you choose which routes Cloud Router advertises to your on-premises router through BGP. You can specify both IPv4 and IPv6 custom advertised routes. However, IPv6 custom advertised routes are advertised only in BGP sessions where IPv6 route exchange is enabled. IPv4 custom advertised routes are advertised only in BGP sessions where IPv4 route exchange is enabled.

For configuration steps, see the [overview for custom advertised routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes).

**Custom learned route configuration**

If you want to configure custom learned routes, use the `--set-custom-learned-route-ranges` flag. You can also optionally use the `--custom-learned-route-priority` flag to set a MED value for the routes. Each BGP session can have MED value that applies to all the custom learned routes that you configured for the session. When you use this feature, the Cloud Router behaves as if it learned these routes from the BGP peer. For more information about how learned routes work in VPC, see [Learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes).
    
    gcloud compute routers add-bgp-peer ROUTER_NAME \
        --interface=my-router-i1-intf-v4 \
        --region=REGION \
        --peer-name=BGP_PEER_NAME \
        --peer-asn=PEER_ASN \
        --set-custom-learned-route-ranges=IP_PREFIXES \
        --custom-learned-route-priority=MED_VALUE
    

Replace the following:

     * `IP_PREFIXES`: a comma-separated list of IP address prefixes—for example, `1.2.3.4,6.7.0.0/16`

     * `MED_VALUE`: a MED value for the specified IP prefixes. You can set a MED value between `0` and `65535` inclusive.

**MD5 authentication configuration**

If you want to use MD5 authentication, add the `md5-authentication-key` flag. For more information about this feature, see [Use MD5 authentication](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication).
    
    gcloud compute routers add-bgp-peer ROUTER_NAME \
        --interface=my-router-i1-intf-v4 \
        --region=REGION \
        --peer-name=BGP_PEER_NAME \
        --peer-asn=PEER_ASN \
        --md5-authentication-key=MD5_AUTHENTICATION_KEY
    

Replace `MD5_AUTHENTICATION_KEY` with the MD5 authentication key for this BGP peer.

**Bidirectional Forwarding Detection (BFD)**

If you want to add [Bidirectional Forwarding Detection (BFD)](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd) for Cloud Router, you can configure your BGP peer with a BFD session. BFD detects forwarding path outages such as link down events, allowing for more resilient hybrid networks. To update your BGP session to use BFD, see [Configuring BFD for Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-bfd).




If you're building redundancy with a duplicate Dedicated Interconnect connection, repeat these steps for the second connection and specify the same Cloud Router. For more information, see [Redundancy and SLA](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview#redundancy).

## Create encrypted VLAN attachments

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following Identity and Access Management (IAM) roles.

**Permissions**

  * `compute.interconnects.use`
  * `compute.interconnectAttachments.create`
  * `compute.interconnectAttachments.get`
  * `compute.routers.create`
  * `compute.routers.get`
  * `compute.routers.update`



**Roles**

  * `roles/owner`
  * `roles/editor`
  * `roles/compute.networkAdmin`



**Note:** If you're deploying a 99.99% topology of HA VPN over Cloud Interconnect, repeat the following procedure for both Dedicated Interconnect connection pairs. When you create the second set of VLAN attachments for the second Dedicated Interconnect connection pair, specify a different region with another encrypted Cloud Router.

For more information about the 99.99% topology, see [SLA](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/ha-vpn-interconnect#sla).

**Note:** You can optionally configure [custom learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/custom-learned-routes) for the BGP session used by a VLAN attachment. You can also [add custom learned routes to an existing session](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configure-custom-learned-routes#add-routes-to-existing-session).

###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **VLAN attachments** tab.

[Go to VLAN attachments](https://console.cloud.google.com/hybrid/interconnects/list?tab=attachments)

  2. Click **Create VLAN attachments**.

  3. Select **Dedicated Interconnect connection**.

  4. In the **Encrypt interconnect** section, select **Set up HA VPN over Interconnect** , and then click **Continue**.

  5. In the **Select interconnects** section, select two existing Dedicated Interconnect connections where you want to deploy HA VPN over Cloud Interconnect.

     * To use connections in the current project, select **In this project**.
     * To use connections in another project, select **In another project** , and then enter the **Project ID** of the project.
     * In the **Interconnect 1** field, select the first connection.
     * In the **Interconnect 2** field, select the second connection. Make sure that you select a connection that is hosted in the same metropolitan area (metro) but in a different edge availability domain than the first connection. For example, if the first connection is in `ord-zone1`, make sure that the second connection is in `ord-zone2`.
  6. After you select two existing Dedicated Interconnect connections, click **Continue**.

  7. On the **Create VLAN attachments** page, select **VPC Network**.

  8. In the **Encrypted interconnect router** field, select a Cloud Router to associate with both encrypted VLAN attachments. The Cloud Router must be in the VPC network that you want to connect to. In addition, the Cloud Router that you specify can only be used with encrypted VLAN attachments. This router only advertises the routes for HA VPN and peer VPN tunnel interfaces.

If you don't have an existing encrypted Cloud Router that you can use, select **Create new router** , and specify a **Region**.

For the BGP AS number, use any private ASN (`64512-65534` or `4200000000-4294967294`) or `16550`.

  9. Configure the two VLAN attachments. For **VLAN attachment 1** and **VLAN attachment 2** , configure the following fields:

     * **Name** : A name for the attachment. This name is displayed in the Google Cloud console and is used by the Google Cloud CLI to reference the attachment—for example, `my-attachment`.
     * **Description** : Enter an optional description.
  10. To configure a VLAN ID or a specific IP address range for the BGP session, click **VLAN ID, BGP IPs**.

     * To specify a VLAN ID, in the **VLAN ID** section, select **Customize**.
     * To specify an IPv4 address range for the BGP session, in the **Allocate BGP IPv4 address** section, select **Specify a candidate link-local range** or **Specify custom IP address** , then enter an IP address range or an IP address respectively.

If you don't specify a VLAN ID or manually allocate BGP IPv4 addresses, Google Cloud automatically assigns these values for you.

**Custom IP address** : For more information about prerequisites, limitations and why you might use custom IP address ranges, see [Custom IP address ranges](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview#custom-ip).

In the **Cloud Router IP** field, enter the IPv4 CIDR address that you want to assign to the Cloud Router end of your VLAN attachment, like `192.0.2.1/29`. Then, in the **Peer IP** field, enter the IPv4 CIDR address that you want to assign to the customer router end of your VLAN attachment.

  11. In the **Capacity** field, select the maximum bandwidth for each VLAN attachment. The value that you select for **VLAN attachment 1** is automatically applied to **VLAN attachment 2**. If you don't select a value, Cloud Interconnect uses 10 Gbps. The capacity that you select determines how many HA VPN tunnels you need to deploy.

  12. In the **VPN Gateway IP addresses** section, select the type of IP addresses to use for your HA VPN tunnel interfaces.

     * If you select **Internal regional IP addresses** , click **Add new IP address range** , and enter a **Name** and **IP range**. For the **IP range** , specify a regional internal IPv4 range with a prefix length between `26` and `29`. The prefix length determines the number of IPv4 addresses available for the VPN tunnel interfaces and must be based on the capacity of the attachment. For more information, see [Assign internal IP address ranges to HA VPN gateways](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/ha-vpn-interconnect-internal-ips).
     * If you select **External regional IP addresses** , Cloud Interconnect automatically assigns regional external IP addresses to the HA VPN tunnel interfaces that you create on your VLAN attachment.

Both VLAN attachments must use the same type of addressing, either internal or external, for their VPN gateway IPv4 addresses.

  13. When you have created both VLAN attachments, click **Create**. The attachments take a few moments to create.

  14. The **Configure interconnect router** page shows each VLAN attachment and its configuration status.

  15. For each VLAN attachment, to create a BGP session to exchange routes between your Cloud Router network and your on-premises router, click **Configure** , and then enter the following information:

     * **Name** : A name for the BGP session.
     * **Peer ASN** : The public or private ASN of your on-premises router.
     * **Advertised route priority (MED)** (optional): The base value that Cloud Router uses to calculate route metrics. All routes advertised for this session use this base value. For more information, see [Advertised prefixes and priorities](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#advertised-priority).

This Cloud Router only advertises routes for HA VPN and peer VPN tunnel interfaces.

     * **BGP peer** : Lets you enable or disable the BGP session with this peer. If disabled, this Cloud Router does not send BGP connection requests and rejects all BGP connection requests from this peer.

     * **MD5 authentication** (optional): Lets you authenticate BGP sessions between Cloud Router and its peers. For instructions about how to use MD5 authentication, see [Use MD5 authentication](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication).

Don't enable [Bidirectional Forwarding Detection (BFD)](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd). Enabling BFD at the Cloud Interconnect level does not provide faster failure detection for HA VPN tunnel traffic.

  16. Click **Save and continue**.

  17. After you add BGP sessions for all your VLAN attachments, click **Save configuration**. The BGP sessions that you configured are inactive until you configure BGP on your on-premises router.

  18. On the **Create VPN gateways** page, complete the HA VPN over Cloud Interconnect deployment by configuring HA VPN for your VLAN attachments (see [Configure HA VPN over Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/configure-ha-vpn-interconnect)), and then click **Create & continue**.

  19. On the **Create VPN tunnels** page, create two VPN tunnels for each HA VPN gateway, one tunnel on each interface. Specify the peer side of the VPN tunnel as the corresponding interface on the peer VPN gateway, and then click **Create & continue**.

  20. On the **Configure VPN router** page, click **Configure BGP session** to set up the BGP session on the Cloud Router for each HA VPN tunnel (see [Specify and manage custom learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configure-custom-learned-routes)).




###  gcloud 

  1. Create an encrypted Cloud Router for Cloud Interconnect.

Create the Cloud Router in the network and region that you want to reach from your on-premises network. Specify the `--encrypted-interconnect-router` flag to identify this router to use with the HA VPN over Cloud Interconnect deployment.
         
         gcloud compute routers create ROUTER_NAME \
             --region=REGION \
             --network=NETWORK_NAME \
             --asn=ROUTER_ASN \
             --encrypted-interconnect-router
         

Replace the following:

     * `ROUTER_NAME`: a name for your Cloud Router—for example, `interconnect-router`.

     * `NETWORK_NAME`: a name for this network—for example, `network-a`.

     * `ROUTER_ASN`: an ASN for this router. The Cloud Router must have a BGP ASN of `16550`, or you can use any private ASN (`64512-65534` or `4200000000-4294967294`).

  2. Optional: Reserve a regional internal IPv4 range with a prefix length between `26` and `29`.

The prefix length determines the number of IPv4 addresses available for the VPN gateway interfaces. The number of IPv4 addresses you need to reserve depends on the capacity of the associated VLAN attachment.

For example, to reserve a range for the first VLAN attachment with a 10-Gbps capacity:
         
         gcloud compute addresses create IP_ADDRESS_RANGE_NAME_1 \
              --region=REGION \
              --addresses=192.168.1.0 \
              --prefix-length=29 \
              --network=NETWORK_NAME \
              --purpose=IPSEC_INTERCONNECT
         

Replace `IP_ADDRESS_RANGE_NAME_1` with a name for this IP address range.

To reserve an address range for the second VLAN attachment:
         
         gcloud compute addresses create IP_ADDRESS_RANGE_NAME_2 \
              --region=REGION \
              --addresses=192.168.2.0 \
              --prefix-length=29 \
              --network=NETWORK_NAME \
              --purpose=IPSEC_INTERCONNECT
         

Replace `IP_ADDRESS_RANGE_NAME_2` with a name for this IP address range.

For more information about reserving regional internal addresses, see [Assign internal IP address ranges to HA VPN gateways](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/ha-vpn-interconnect-internal-ips#gcloud).

  3. Create the first encrypted VLAN attachment, specifying the names of your first connection and the encrypted Cloud Router:
         
         gcloud compute interconnects attachments dedicated create ATTACHMENT_NAME \
              --region=REGION \
              --router=INTERCONNECT_ROUTER_NAME \
              --interconnect=INTERCONNECT_NAME_1 \
              --bandwidth=10g \
              --encryption=IPSEC \
              --ipsec-internal-addresses=IP_RANGE_1
         

Replace the following:

     * `INTERCONNECT_NAME_1`: the name of the Cloud Interconnect this attachment belongs to.

     * `IP_RANGE_1`: the IP range for this attachment—for example, the regional internal IPv4 address range `ip-range-1`.

If you want to use regional external IPv4 addresses for the HA VPN gateway interfaces on your attachment, omit the `--ipsec-internal-addresses` flag. All HA VPN gateway interfaces are automatically assigned regional external IPv4 addresses.
    
    gcloud compute interconnects attachments dedicated create ATTACHMENT_NAME_1 \
         --region=REGION \
         --router=INTERCONNECT_ROUTER_NAME \
         --interconnect=INTERCONNECT_NAME_1 \
         --bandwidth=10g \
         --encryption=IPSEC
    

You can't set a custom MTU (`--mtu`) with encrypted VLAN attachments. All encrypted VLAN attachments must use an MTU of 1440 bytes, which is the default value.

In addition, you can't create dual-stack VLAN attachments for HA VPN over Cloud Interconnect. Encrypted VLAN attachments only support the `IPV4_ONLY` (single stack) stack type.

#### Configure custom IP address ranges

If you want to use custom IP address ranges, add the `--candidate-customer-router-ip-address` and `--candidate-cloud-router-ip-address` flags, which also support link-local IP addresses. Note that you can't combine these flags with the `--candidate-subnets` and `--subnet-length` fields, but you can use `--candidate-subnets` for link-local IPv4 attachments with the `--candidate-customer-router-ipv6-address` and `--candidate-cloud-router-ipv6-address` flags.

For more information about prerequisites, limitations and why you might use custom IP address ranges, see [Custom IP address ranges](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview#custom-ip).
    
    gcloud compute interconnects attachments dedicated create ATTACHMENT_NAME_1 \
        --project=PROJECT_ID \
        --region=REGION \
        --router=ROUTER_NAME \
        --encryption=IPSEC \
        --candidate-cloud-router-ip-address=CANDIDATE_CLOUD_ROUTER_IP_ADDRESS \
        --candidate-customer-router-ip-address=CANDIDATE_CUSTOMER_ROUTER_IP_ADDRESS
    

Replace the following:

     * `CANDIDATE_CLOUD_ROUTER_IP_ADDRESS`: the IPv4 CIDR address that you want to assign to the Cloud Router end of your VLAN attachment, like `192.0.2.1/29`
     * `CANDIDATE_CUSTOMER_ROUTER_IP_ADDRESS`: the IPv4 CIDR address that you want to assign to the customer router end of your VLAN attachment

If you use IPv6 dual-stack attachments, use the following command:
    
    gcloud compute interconnects attachments dedicated create ATTACHMENT_NAME_1 \
        --project=PROJECT_ID \
        --region=REGION \
        --router=ROUTER_NAME \
        --stack-type=IPV4_IPV6 \
        --encryption=IPSEC \
        --candidate-cloud-router-ipv6-address=CANDIDATE_CLOUD_ROUTER_IP_ADDRESS \
        --candidate-customer-router-ipv6-address=CANDIDATE_CUSTOMER_ROUTER_IP_ADDRESS
    

Replace the following:

     * `CANDIDATE_CLOUD_ROUTER_IP_ADDRESS`: the IPv6 CIDR address that you want to assign to the Cloud Router end of your VLAN attachment, like `2001:db8::1/125`
     * `CANDIDATE_CUSTOMER_ROUTER_IP_ADDRESS`: the IPv6 CIDR address that you want to assign to the customer router end of your VLAN attachment

You can use the `--candidate-cloud-router-ip-address` and `--candidate-customer-router-ip-address` flags alongside the `--candidate-cloud-router-ipv6-address` and `--candidate-customer-router-ipv6-address` flags to create an attachment that uses both IPv4 and IPv6 custom address ranges.

  4. Create the second encrypted VLAN attachment, specifying the names of your second Cloud Interconnect connection and the Cloud Router for Cloud Interconnect:
         
         gcloud compute interconnects attachments dedicated create ATTACHMENT_NAME_2 \
               --region=REGION \
               --router=INTERCONNECT_ROUTER_NAME \
               --interconnect=INTERCONNECT_NAME_2 \
               --bandwidth=10g \
               --encryption=IPSEC \
               --ipsec-internal-addresses=IP_RANGE_2
         

Replace the following:

     * `INTERCONNECT_NAME_2`: the name of the Cloud Interconnect this attachment belongs to.

     * `IP_RANGE_2`: the IP range for this attachment—for example, the regional internal IPv4 address range `ip-range-2`.

When creating the second VLAN attachment, specify the same type of IPv4 addressing scheme, either internal or external, that you used when you created the first attachment. If you specified an internal address range for the first attachment, specify a different reserved internal IPv4 address range.

  5. Describe the attachment to retrieve the resources that it allocated, such as the VLAN ID and BGP peering IPv4 addresses, as shown in the following example. Use these values to configure your Cloud Router and your on-premises router.

For the first VLAN attachment:
         
         gcloud compute interconnects attachments describe ATTACHMENT_NAME_1 \
             --region=REGION
         

The output is similar to the following:
         
         adminEnabled: true
         bandwidth: BGP_10G
         **cloudRouterIpAddress: 169.254.61.89/29**
         creationTimestamp: '2022-05-22T10:31:40.829-07:00'
         **customerRouterIpAddress: 169.254.61.90/29**
         dataplaneVersion: 2
         encryption: IPSEC
         id: '2973197662755397267'
         interconnect: https://www.googleapis.com/compute/v1/projects/my-project/global/interconnects/INTERCONNECT_NAME_1
         kind: compute#interconnectAttachment
         name: my-attachment-1
         operationalStatus: OS_ACTIVE
         privateInterconnectInfo:
           tag8021q: 1000
         region: https://www.googleapis.com/compute/v1/projects/my-project/regions/us-central1
         router: https://www.googleapis.com/compute/v1/projects/my-project/regions/us-central1/routers/INTERCONNECT_ROUTER_NAME
         selfLink: https://www.googleapis.com/compute/v1/projects/my-project/regions/us-central1/interconnectAttachments/my-attachment-1
         **stackType: IPV4_ONLY**
         state: ACTIVE
         type: DEDICATED
         **vlanTag8021q: 1000**
         

For the second VLAN attachment:
         
         gcloud compute interconnects attachments describe ATTACHMENT_NAME_2 \
             --region=REGION
         

The output is similar to the following:
         
         adminEnabled: true
         bandwidth: BGP_10G
         **cloudRouterIpAddress: 169.254.116.185/29**
         creationTimestamp: '2022-05-22T10:31:40.829-07:00'
         **customerRouterIpAddress: 169.254.116.186/29**
         dataplaneVersion: 2
         encryption: IPSEC
         id: '2973197662755397269'
         interconnect: https://www.googleapis.com/compute/v1/projects/my-project/global/interconnects/INTERCONNECT_NAME_2
         kind: compute#interconnectAttachment
         name: my-attachment-2
         operationalStatus: OS_ACTIVE
         privateInterconnectInfo:
           tag8021q: 1000
         region: https://www.googleapis.com/compute/v1/projects/my-project/regions/us-central1
         router: https://www.googleapis.com/compute/v1/projects/my-project/regions/us-central1/routers/INTERCONNECT_ROUTER_NAME
         selfLink: https://www.googleapis.com/compute/v1/projects/my-project/regions/us-central1/interconnectAttachments/my-attachment-2
         **stackType: IPV4_ONLY**
         state: ACTIVE
         type: DEDICATED
         **vlanTag8021q: 1000**
         

     * The `cloudRouterIpAddress` values (`169.254.61.89/29` and `169.254.116.185/29`) are IPv4 link-local addresses. When you create Cloud Router interfaces for the attachments, the interfaces use these IP addresses. You use the same addresses for the BGP neighbor on your on-premises router.

     * `customerRouterIpAddress` values (`169.254.61.90/29` and `169.254.116.186/29`) are IPv4 link-local addresses. On the Cloud Router, configure a BGP peer with these addresses over the interfaces that have the Cloud Router addresses assigned to them. You assign these addresses to the VLAN subinterface on your on-premises router.

     * `stackType` value (`IPV4_ONLY`) indicates the type of traffic supported by the VLAN attachment.

     * `vlanTag8021q` value (`1000`) identifies traffic that goes across this attachment. You need this value to configure a tagged VLAN subinterface on your on-premises router.

  6. On your Cloud Router, add two interfaces.

Each interface connects to one of the VLAN attachments. The interface IP address is automatically configured by using your attachment's `cloudRouterIpAddress`.
         
         gcloud compute routers add-interface INTERCONNECT_ROUTER_NAME \
             --region=REGION \
             --interface-name=ROUTER_INTERFACE_NAME_1 \
             --interconnect-attachment=ATTACHMENT_NAME_1
         
         
         gcloud compute routers add-interface INTERCONNECT_ROUTER \
             --region=REGION \
             --interface-name=ROUTER_INTERFACE_NAME_2 \
             --interconnect-attachment=ATTACHMENT_NAME_2
         

Replace the following:

     * `ROUTER_INTERFACE_NAME_1`: a name for the first Cloud Router interface.

     * `ROUTER_INTERFACE_NAME_2`: a name for the second Cloud Router interface.

  7. Add BGP peers to the interfaces.

The peer IPv4 addresses are automatically configured by using the `customerRouterIpAddress` of your attachments.
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
              --interface=ROUTER_INTERFACE_NAME_1 \
              --region=REGION \
              --peer-name=BGP_PEER_NAME \
              --peer-asn=PEER_ASN
         

Replace `PEER_ASN` with the same ASN that you configured on your on-premises router.

To specify a base priority value, use the `--advertised-route-priority` flag. Cloud Router uses this value to calculate route metrics for all routes that it advertises for this session. For more information, see [Advertised prefixes and priorities](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#advertised-priority) in the Cloud Router documentation.

If you want to configure custom learned routes, use the `--set-custom-learned-route-ranges` flag. You can also optionally use the `--custom-learned-route-priority` flag. Each BGP session can have one priority value that applies to all the custom learned routes that you configured for the session. When you use this feature, the Cloud Router behaves as if it learned these routes from the BGP peer. For more information, see [Custom learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/custom-learned-routes).
         
         gcloud compute routers add-bgp-peer my-router \
              --interface=INTERCONNECT_ROUTER_INTERFACE_NAME \
              --region=REGION \
              --peer-name=BGP_PEER_NAME \
              --peer-asn=PEER_ASN \
              --set-custom-learned-route-ranges=IP_PREFIXES \
              --custom-learned-route-priority=MED_VALUE
         

Replace the following:

     * `IP_PREFIXES`: a comma-separated list of IP address prefixes—for example, `1.2.3.4,6.7.0.0/16`

     * `MED_VALUE`: a MED value for the specified IP prefixes. You can set a MED value between `0` and `65535` inclusive.

If you want to use MD5 authentication, add the `md5-authentication-key` flag. For more information about this feature, see [Use MD5 authentication](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication).

Do not enable [Bidirectional Forwarding Detection (BFD)](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd). Enabling BFD at the Cloud Interconnect level does not provide faster failure detection for HA VPN tunnel traffic.

  8. Complete the HA VPN over Cloud Interconnect deployment by configuring HA VPN for your VLAN attachments.

See [Configure HA VPN over Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/configure-ha-vpn-interconnect).




## VLAN attachment groups

You can group your VLAN attachments within a VLAN attachment group, which provides information about configuration issues that can prevent your deployment from qualifying for your intended level of reliability. When you create a VLAN attachment group, it can be empty. You can add members to the VLAN attachment group when you create it, and you can add and remove members after the group is created.

### Create VLAN attachment groups

Use this procedure to create a new VLAN attachment group. You need the `compute.interconnectAttachmentGroups.create` permission to create a new attachment group.

###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **VLAN attachments** tab.

[Go to VLAN attachments](https://console.cloud.google.com/hybrid/interconnects/list?tab=attachments)

  2. In the **Attachment groups** field, click **Create group**.

  3. Specify the details of the VLAN attachment group:

     * **Name** : a name for the VLAN attachment group. This name is displayed in the Google Cloud console and is used by the Google Cloud CLI to reference the group, such as `my-group`.
     * **Description** : an optional description of the VLAN attachment group.
     * In the **Production SLA** field, select one of the intended SLA options.
     * In the **Group members** field, select the VLAN attachments that you want to add to the attachment group from each numbered **Attachment** box.
  4. Optional: You can click **Add attachment** to add more attachments than you are required to add based on your intended SLA.

  5. Click **Save**.




###  gcloud 

In the following example, you create an empty VLAN attachment group called `GROUP_NAME` with an intended reliability level of `INTENDED_SLA`:
    
    
    gcloud compute interconnects attachments groups create GROUP_NAME \
        --intended_availability_sla INTENDED_SLA
    

In this example, you create a VLAN attachment group with two existing VLAN attachments, one named `ATTACHMENT_1` in `REGION_1` and the other named `ATTACHMENT_2` in `REGION_2`.
    
    
    gcloud compute interconnects attachments groups create GROUP_NAME \
        --intended_availability_sla INTENDED_SLA \
        --attachments=REGION_1/ATTACHMENT_1,REGION_2/ATTACHMENT_2
    

### Add VLAN attachments to a VLAN attachment group

Use this procedure to add VLAN attachments to the VLAN attachment group that you created in the previous section. You need the `compute.interconnectAttachmentGroups.get` and `compute.interconnectAttachmentGroups.update` permissions to add VLAN attachments to an attachment group.

###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **VLAN attachments** tab.

[Go to VLAN attachments](https://console.cloud.google.com/hybrid/interconnects/list?tab=attachments)

  2. Select the VLAN attachment group that you want to edit.

  3. Click **Edit**.

  4. In the **Group members** field, click **Add attachment**.

  5. In the box, choose the VLAN attachment that you want to add to the group.

  6. Optional: Repeat the previous steps for each additional attachment that you want to add to the group.

  7. Click **Done**.




###  gcloud 

In the following example, you add two new VLAN attachments to the group with the name `GROUP_NAME`:
    
    
    gcloud compute interconnects attachments groups add-members GROUP_NAME \
        --attachments=REGION_1/ATTACHMENT_1,REGION_2/ATTACHMENT_2
    

Replace the following values:

  * `GROUP_NAME`: the name of your attachment group
  * `REGION_1`: the name of the region of the first VLAN attachment
  * `ATTACHMENT_1`: the name of the first VLAN attachment that you want to create within this attachment group
  * `REGION_2`: the name of the region of the second VLAN attachment
  * `ATTACHMENT_2`: the name of the second VLAN attachment that you want to create within this attachment group



### Remove VLAN attachments from a VLAN attachment group

Use this procedure to remove VLAN attachments from the VLAN attachment group that you created in the previous section. You need the `compute.interconnectAttachmentGroups.get` and `compute.interconnectAttachmentGroups.update` permissions to remove VLAN attachments from an attachment group.

###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **VLAN attachments** tab.

[Go to VLAN attachments](https://console.cloud.google.com/hybrid/interconnects/list?tab=attachments)

  2. Select the VLAN attachment group that you want to edit.

  3. Click **Edit group**.

  4. In the **Group members** field, click the box with the VLAN attachment that you want to remove from the group, and either replace the selected VLAN attachment connection with another VLAN attachment or click delete**Delete**.

  5. Click **Done**.




###  gcloud 

In the following example, you remove two VLAN attachments from the group with the name `GROUP_NAME`:
    
    
    gcloud compute interconnects attachments groups remove-members GROUP_NAME \
        --attachments=REGION_1/ATTACHMENT_1,REGION_2/ATTACHMENT_2
    

Replace the following values:

  * `GROUP_NAME`: the name of your attachment group
  * `REGION_1`: the name of the region of the first VLAN attachment
  * `ATTACHMENT_1`: the name of the first VLAN attachment that you want to create within this attachment group
  * `REGION_2`: the name of the region of the second VLAN attachment
  * `ATTACHMENT_2`: the name of the second VLAN attachment that you want to create within this attachment group



## Restrict Dedicated Interconnect usage

By default, any VPC network can use Cloud Interconnect. To control which VPC networks can use Cloud Interconnect, you can set an organization policy. For more information, see [Restrict Cloud Interconnect usage](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/restricting-usage). 

## What's next

  * To modify VLAN attachments, see [Modify VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/modifying-vlan-attachments).
  * To configure on-premises routers for Dedicated Interconnect, see [Configure on-premises routers](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/configuring-onprem-routers).



[ Previous arrow_back  Test connections  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/testing-connections)

[ Next Configure on-premises routers  arrow_forward  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/configuring-onprem-routers)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
