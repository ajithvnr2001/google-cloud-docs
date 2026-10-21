---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/creating-vlan-attachments/
title: Create VLAN attachments \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:55:05.043222+00:00
---

# Create VLAN attachments  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/creating-vlan-attachments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Create VLAN attachments Stay organized with collections  Save and categorize content based on your preferences. 

VLAN attachments for Partner Interconnect connections (also known as `interconnectAttachments`) connect your Virtual Private Cloud (VPC) networks with your on-premises network through your service provider's network by allocating VLANs on your service provider's connection.

You can create unencrypted VLAN attachments or encrypted VLAN attachments. Unencrypted VLAN attachments support IPv4 only (single stack) or IPv4 and IPv6 (dual stack). Encrypted VLAN attachments are used in HA VPN over Cloud Interconnect deployments, and they only support IPv4 (single stack).

Before you can create VLAN attachments for Partner Interconnect, you must already have connectivity with a [supported service provider](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/service-providers).

Billing for VLAN attachments starts when your service provider completes their configurations, whether or not you pre-activated your attachments. Your service provider configures your attachments when they are in the `PENDING_CUSTOMER` or `ACTIVE` state. Billing stops when you or the service provider deletes the attachments (when they are in the `DEFUNCT` state).

The VLAN ID is unique to your Partner Interconnect connection, and therefore you can reuse the same VLAN ID on a different connection, regardless of where that connection is located.

For VLAN attachments for Dedicated Interconnect, see [Creating VLAN attachments for Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments).

For definitions of terms used on this page, see [Cloud Interconnect key terms](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology).

To help you solve common issues that you might encounter when using Partner Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting#partner).

## Utilize multiple VLAN attachments

VLAN attachments are subject to the maximum bandwidth capacity for each VLAN attachment, as well as for each traffic flow on a VLAN attachment, as described in the [Quotas and limits](https://docs.cloud.google.com/network-connectivity/docs/interconnect/quotas#limits) page.

To achieve higher throughput into a VPC network, you must configure multiple VLAN attachments into the VPC network. For each Border Gateway Protocol (BGP) session, you should use the same MED values to let the traffic use equal-cost multipath (ECMP) routing over all the configured VLAN attachments.

**Note:** Creating VLAN attachments with a combined bandwidth greater than the Cloud Interconnect connection doesn't give you more than the maximum stated bandwidth of the connection.

If you have multiple VLAN attachments, including attachments in different projects, you can pair them with a Partner Interconnect connection from the same service provider, or with Partner Interconnect connections from different service providers.

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

  3. Select **Partner Interconnect connection**.

  4. In the **Encrypt interconnect** section, select **Set up unencrypted Interconnect** , and then click **Continue**.

  5. Select **I already have a service provider**.

  6. Select **Create a redundant pair of VLAN attachments**. Redundancy provides higher availability than a single connection. Both attachments serve traffic, and the traffic is load balanced between them. If one attachment goes down, for example during scheduled maintenance, the other attachment continues to serve traffic. For more information, see [Redundancy and SLA](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview#redundancy).

If you're creating an attachment for testing purposes or don't require high availability, select **Create a single VLAN** to create only one VLAN attachment.

  7. For the **Network** and **Region** fields, select the VPC network and [Google Cloud region](https://docs.cloud.google.com/docs/geography-and-regions) where your attachments will connect.

  8. Specify the details of your VLAN attachments:

     * **Cloud Router** : A Cloud Router to associate with this attachment. You can only choose a Cloud Router in the VPC network and region that you selected with an ASN of `16550`. If you don't have an existing Cloud Router, [create one](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/create-router-vpc-network) with an ASN of `16550`. Each VLAN attachment can be associated with a single Cloud Router. Google automatically adds an interface and a BGP peer on the Cloud Router.

     * **VLAN attachment name** : A name for the attachment. This name is displayed in the Google Cloud console and is used by the Google Cloud CLI to reference the attachment—for example, `my-attachment`.

     * **IP stack type** : Select the IP stack type. Either **IPv4 (single-stack)** , or **IPv4 and IPv6 (dual-stack)**.

       * In the **Allocate BGP IPv4 address** and **Allocate BGP IPv6 address** sections, you can choose **Automatically allocate link-local range** or **Specify custom IP address.** If you choose **Automatically allocate link-local range** , skip the rest of the instructions in this step.

**Note:** The following instructions describe how to configure custom IP address ranges for a Layer 2 connection. If you want to use custom IP address ranges with a Layer 3 connection, you create a VLAN attachment and then your service provider configures the custom IP address ranges during their VLAN attachment configuration process. If you have a Layer 3 connection, contact your service provider for instructions.

For more information about prerequisites, limitations and why you might use custom IP address ranges, see [Custom IP address ranges](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview#custom-ip).

In the **Cloud Router IP** field, enter the IPv4 CIDR address that you want to assign to the Cloud Router end of your VLAN attachment, like `192.0.2.1/29`. Then, in the **Peer IP** field, enter the IPv4 CIDR address that you want to assign to the customer router end of your VLAN attachment.

If you selected **IPv4 and IPv6 (dual stack)** , you must also select one of the options in the **Allocate BGP IPv6 address** section. In the **Cloud Router IPv6** field, enter the IPv6 CIDR address that you want to assign to the Cloud Router end of your VLAN attachment, like `2001:db8::1/125`. Then, in the **Peer IPv6** field, enter the IPv6 CIDR address that you want to assign to the customer router end of your VLAN attachment.

     * **Maximum transmission unit (MTU)** for the attachment: To make use of the 1460-, 1500-, or 8896-byte maximum transmission unit (MTU), [the VPC network that uses the attachment must have an MTU set to the same value](https://docs.cloud.google.com/vpc/docs/mtu). In addition, the on-premises virtual machine (VM) instances and routers must have their MTU set to the same value as well. If your network has the default MTU of `1460`, then select `1460` as the VLAN attachment MTU.

  9. To create the attachments, click **Create**. This action takes a few minutes to complete.

  10. After creation is complete, copy the [pairing keys](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology#pairingkey). You share these keys with your service provider when you request a connection with them.

If you're requesting a Layer 3 connection from your service provider, you can [pre-activate](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview#pre-activate) the attachment by selecting **Enable**. Activating attachments enables you to confirm that you're connecting to the expected service provider. Pre-activating attachments enables you to skip the [activation step](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/activating-connections) and lets the attachments start passing traffic immediately after your service provider completes their configuration.

  11. To view a list of your VLAN attachments, click **OK**.




You can optionally update your BGP sessions to [use MD5 authentication](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication).

If you have a Layer 2 connection, follow the steps in [Add authentication to an existing session](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication#add-authentication). If you have a Layer 3 connection, contact your service provider for instructions.

Optional: You can update your BGP session to use custom learned routes. When you use this feature, the Cloud Router behaves as if it learned these routes from the BGP peer. For more information, see [Update an existing session to use custom learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configure-custom-learned-routes#add-routes-to-existing-session).

Optional: [Bidirectional Forwarding Detection (BFD)](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd) for Cloud Router detects forwarding path outages such as link down events, allowing for more resilient hybrid networks. To update your BGP session to use BFD, see [Configuring BFD](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-bfd).

**Important:** BFD can only be enabled on provisioned VLAN attachments that use Dataplane version 2. You can view the `dataplaneVersion` for a VLAN attachment by viewing the attachment details in one of the following ways:

  * **API** : Use the [interconnectAttachments.get](https://docs.cloud.google.com/compute/docs/reference/rest/v1/interconnectAttachments/get) method. You can use this method on VLAN attachments for either Dedicated Interconnect or Partner Interconnect. 
  * **Google Cloud CLI** : Use the `gcloud compute interconnects attachments describe ATTACHMENT-NAME` command where ATTACHMENT-NAME is the name of the VLAN attachment for either Dedicated Interconnect or Partner Interconnect. 



In the output of the API or gcloud CLI command, look for the `dataplaneVersion` field with a value of `2`. If the field is absent from the output, the VLAN attachment is using version 1 and cannot be used with BFD. For more information, contact your customer account team.

The Cloud Interconnect Dataplane v2 is unrelated to [ Google Kubernetes Engine (GKE) Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2)

###  gcloud 

Before you create a VLAN attachment, you must have an existing Cloud Router in the network and region that you want to reach from your on-premises network. If you don't have an existing Cloud Router, [create one](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/create-router-vpc-network). The Cloud Router must have a BGP ASN of `16550`.

  1. Create a VLAN attachment of type `PARTNER`, specifying the names of your Cloud Router and the [edge availability domain](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology#edge-availability-domain) (metro availability zone) of the VLAN attachment. Google automatically adds an interface and a BGP peer on the Cloud Router. The attachment generates a [pairing key](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology#pairingkey) that you need to share with your service provider.

You can specify the MTU of your attachment. Valid values are `1440` (default), `1460`, `1500`, and `8896`. To specify an MTU of `1460`, `1500`, or `8896` use the`--mtu` parameter—for example, `--mtu 1500`. To make use of the 1460-, 1500-, or 8896-byte MTU, [the VPC network that uses the attachment must set the same MTU](https://docs.cloud.google.com/vpc/docs/mtu). In addition, the on-premises VMs and routers must set the same MTU

You can specify the stack type of your VLAN attachment. The default stack type is IPv4.

The following example creates a VLAN attachment in edge availability domain `availability-domain-1`:
         
         gcloud compute interconnects attachments partner create ATTACHMENT_NAME \
             --region=REGION \
             --router=ROUTER_NAME \
             --stack-type=STACK_TYPE \
             --edge-availability-domain availability-domain-1
         

Replace the following:

     * `ATTACHMENT_NAME`: a name for your VLAN attachment.
     * `REGION`: the region of your VLAN attachment.
     * `ROUTER_NAME`: the name of your Cloud Router.
     * `STACK_TYPE`: the stack type for your VLAN attachment. The stack type can be one of the following: 
       * `IPV4_ONLY`: selects IPv4 only (single stack).
       * `IPV4_IPV6`: selects IPv4 and IPv6 (dual stack).
**Note:** You can specify `any` for the edge availability domain, and then your service provider assigns the domain for you. However, to create a redundant attachment (the second attachment), you need to wait until your service provider configures your first VLAN attachment. You won't know which domain to use for your redundant attachment until they complete the configuration.

If you're requesting a Layer 3 connection from your service provider, you can [pre-activate](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview#pre-activate) the attachment by selecting `--admin-enabled` flag. Activating attachments enables you to confirm that you're connecting to the expected service provider. Pre-activating attachments enables you to skip the [activation step](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/activating-connections) and lets the attachments start passing traffic immediately after your service provider completes their configuration.
    
    gcloud compute interconnects attachments partner create ATTACHMENT_NAME \
        --region=REGION \
        --router=ROUTER_NAME \
        --stack-type=STACK_TYPE \
        --edge-availability-domain availability-domain-1 \
        --admin-enabled
    

     * `ATTACHMENT_NAME`: a name for your VLAN attachment.
     * `REGION`: the region of your VLAN attachment.
     * `ROUTER_NAME`: the name of your Cloud Router.
     * `STACK_TYPE`: the stack type for your VLAN attachment. The stack type can be one of the following: 
       * `IPV4_ONLY`: selects IPv4 only (single stack).
       * `IPV4_IPV6`: selects IPv4 and IPv6 (dual stack).
  2. Describe the attachment to retrieve its pairing key; you need to share this key with your service provider when you request a connection with them:
         
         gcloud compute interconnects attachments describe ATTACHMENT_NAME \
             --region=REGION
         

The output is similar to the following for IPv4 VLAN attachments:
         
         adminEnabled: false
         edgeAvailabilityDomain: AVAILABILITY_DOMAIN_1
         creationTimestamp: '2017-12-01T08:29:09.886-08:00'
         id: '7976913826166357434'
         kind: compute#interconnectAttachment
         labelFingerprint: 42WmSpB8rSM=
         name: ATTACHMENT_NAME
         pairingKey: 7e51371e-72a3-40b5-b844-2e3efefaee59/REGION/1
         region: https://www.googleapis.com/compute/v1/projects/customer-project/regions/REGION
         router: https://www.googleapis.com/compute/v1/projects/customer-project/regions/REGION/routers/ROUTER_NAME
         selfLink: https://www.googleapis.com/compute/v1/projects/customer-project/regions/REGION/interconnectAttachments/ATTACHMENT_NAME
         stackType: IPV4_ONLY
         state: PENDING_PARTNER
         type: PARTNER
         

The output is similar to the following for IPv4 and IPv6 (dual stack) VLAN attachments:
         
         bandwidth: BPS_1G
         cloudRouterIpAddress: 169.254.67.201/29
         cloudRouterIpv6Address: 2600:2d00:0:1::1/125
         creationTimestamp: '2017-12-01T08:31:11.580-08:00'
         customerRouterIpAddress: 169.254.67.202/29
         customerRouterIpv6Address: 2600:2d00:0:1::2/125
         description: Interconnect for Customer 1
         id: '7193021941765913888'
         interconnect: https://www.googleapis.com/compute/alpha/projects/partner-project/global/interconnects/lga-2
         kind: compute#interconnectAttachment
         labelFingerprint: 42WmSpB8rSM=
         name: partner-attachment
         partnerMetadata:
           interconnectName: New York (2)
           partnerName: Partner Inc
           portalUrl: https://partner-portal.com
         region: https://www.googleapis.com/compute/alpha/projects/partner-project/regions/REGION
         selfLink: https://www.googleapis.com/compute/alpha/projects/partner-project/regions/REGION/interconnectAttachments/ATTACHMENT_NAME
         stackType: IPV4_IPV6
         state: ACTIVE
         type: PARTNER
         vlanTag8021q: 1000
         

The `pairingKey` field contains the pairing key that you need to share with your service provider. Treat the pairing key as sensitive information until your VLAN attachment is configured.

The state of the VLAN attachment is `PENDING_PARTNER` until you request a connection with your service provider and they complete your VLAN attachment configuration. After the configuration is complete, the state of the attachment changes to `ACTIVE` or `PENDING_CUSTOMER`.




Optional: You can update your BGP session to use custom learned routes. When you use this feature, the Cloud Router behaves as if it learned these routes from the BGP peer. For more information, see [Update an existing session to use custom learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configure-custom-learned-routes#add-routes-to-existing-session).

Optional: You can update your BGP sessions to [use MD5 authentication](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication). If you have a Layer 2 connection, follow the steps in [Add authentication to an existing session](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication#add-authentication). If you have a Layer 3 connection, contact your service provider for instructions.

Optional: [Bidirectional Forwarding Detection (BFD)](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd) for Cloud Router detects forwarding path outages such as link down events, allowing for more resilient hybrid networks. To update your BGP session to use BFD, see [Configuring BFD for Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-bfd).

If you're building redundancy with a duplicate VLAN attachment, repeat these steps for the second attachment. Use the same Cloud Router, but specify a different edge availability domain. Also, when you request connections from your service provider, you must select the same metropolitan area (city) for both attachments for them to be redundant. For more information, see [Redundancy and SLA](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview#redundancy).

#### Use custom IP address ranges with Layer 2 connections

If you want to use custom IP address ranges with a Layer 2 connection, add the `--candidate-customer-router-ip-address` and `--candidate-cloud-router-ip-address` flags, which also support link-local IP addresses. Note that you can't combine these flags with the `--candidate-subnets` and `--subnet-length` flags, but you can use `--candidate-subnets` for link-local IPv4 attachments with the `--candidate-customer-router-ipv6-address` and `--candidate-cloud-router-ipv6-address` flags. For more information about why you might use custom IP address ranges, see [Custom IP address ranges](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview#custom-ip).

For more information about prerequisites, limitations and why you might use custom IP address ranges, see [Custom IP address ranges](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview#custom-ip).
    
    
    gcloud compute interconnects attachments partner create ATTACHMENT_NAME \
        --project=PROJECT_ID \
        --region=REGION \
        --router=ROUTER_NAME \
        --candidate-cloud-router-ip-address=CANDIDATE_CLOUD_ROUTER_IP_ADDRESS \
        --candidate-customer-router-ip-address=CANDIDATE_CUSTOMER_ROUTER_IP_ADDRESS
    

Replace the following:

  * `CANDIDATE_CLOUD_ROUTER_IP_ADDRESS`: the IPv4 CIDR address that you want to assign to the Cloud Router end of your VLAN attachment, like `192.0.2.1/29`
  * `CANDIDATE_CUSTOMER_ROUTER_IP_ADDRESS`: the IPv4 CIDR address that you want to assign to the customer router end of your VLAN attachment



If you use IPv6 dual-stack attachments, use the following command.
    
    
    gcloud compute interconnects attachments partner create ATTACHMENT_NAME \
        --project=PROJECT_ID \
        --region=REGION \
        --router=ROUTER_NAME \
        --stack-type=IPV4_IPV6 \
        --candidate-cloud-router-ipv6-address=CANDIDATE_CLOUD_ROUTER_IP_ADDRESS \
        --candidate-customer-router-ipv6-address=CANDIDATE_CUSTOMER_ROUTER_IP_ADDRESS
    

Replace the following:

  * `CANDIDATE_CLOUD_ROUTER_IP_ADDRESS`: an IPv6 CIDR address, like `2001:db8::1/125`
  * `CANDIDATE_CUSTOMER_ROUTER_IP_ADDRESS`: an IPv6 CIDR address



You can use the `--candidate-cloud-router-ip-address` and `--candidate-customer-router-ip-address` flags alongside the `--candidate-cloud-router-ipv6-address` and `--candidate-customer-router-ipv6-address` flags to create an attachment that uses both IPv4 and IPv6 custom address ranges.

#### Use custom IP address ranges with Layer 3 connections

If you want to use custom IP address ranges with a Layer 3 connection, you create a VLAN attachment and then your service provider configures the custom IP address ranges during their VLAN attachment configuration process. If you have a Layer 3 connection, contact your service provider for instructions.

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



**Note:** If you're deploying the 99.99% availability topology of HA VPN over Cloud Interconnect, repeat the following procedure for both Cloud Interconnect connection pairs. When you create the second set of VLAN attachments for the second Cloud Interconnect connection pair, specify a different region with another encrypted Cloud Router.

For more information about obtaining 99.99% availability with HA VPN over Cloud Interconnect, see [SLA](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/ha-vpn-interconnect#sla).

###  Console 

  1. In the Google Cloud console, go to the Cloud Interconnect **VLAN attachments** tab.

[Go to VLAN attachments](https://console.cloud.google.com/hybrid/interconnects/list?tab=attachments)

  2. Click **Create VLAN attachments**.

  3. Select **Partner Interconnect connection**.

  4. In the **Encrypt interconnect** section, select **Set up HA VPN over Interconnect** , and then click **Continue**.

  5. Select **I already have a service provider**.

  6. On the **Create VLAN attachments** page, select a **VPC Network**.

  7. In the **Encrypted interconnect router** field, select a Cloud Router to associate with both encrypted VLAN attachments. The Cloud Router must be in the VPC network that you want to connect to. In addition, the Cloud Router that you specify can only be used with encrypted VLAN attachments. This router only advertises the routes for HA VPN and peer VPN tunnel interfaces.

If you don't have an existing Cloud Router that you can use specifically for encrypted Cloud Interconnect, do the following:

     1. Select **Create new router**.
     2. Specify a **Region**.
     3. For the BGP AS number, use `16550`.
  8. Configure the two VLAN attachments. For **VLAN attachment 1** and **VLAN attachment 2** , configure the following fields:

     * **Name** : A name for the attachment. This name is displayed in the Google Cloud console and is used by the Google Cloud CLI to reference the attachment, such as `attachment-a-zone1` or `attachment-a-zone2`.
     * **Description** : Enter an optional description.
  9. To configure a VLAN ID or a specific IP address range for the BGP session, click **VLAN ID, BGP IPs**.

     * To specify a VLAN ID, in the **VLAN ID** section, select **Customize**.
     * To specify an IP address range for the BGP session, in the **Allocate BGP IP address** section, select **Specify a candidate link-local range** or **Specify custom IP address** , then enter an IP address range or an IP address respectively.

If you do not specify a VLAN ID or manually allocate BGP IP addresses, Google Cloud automatically assigns these values for you.

**Note:** The following instructions describe how to configure custom IP address ranges for a Layer 2 connection. If you want to use custom IP address ranges with a Layer 3 connection, you create a VLAN attachment and then your service provider configures the custom IP address ranges during their VLAN attachment configuration process. If you have a Layer 3 connection, contact your service provider for instructions.

**Custom IP address:** For more information about prerequisites, limitations and why you might use custom IP address ranges, see [Custom IP address ranges](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview#custom-ip).

In the **Cloud Router IP** field, enter the IPv4 CIDR address that you want to assign to the Cloud Router end of your VLAN attachment, like `192.0.2.1/29`. Then, in the **Peer IP** field, enter the IPv4 CIDR address that you want to assign to the customer router end of your VLAN attachment.

  10. In the **Capacity** field, select the maximum bandwidth for each VLAN attachment. The value that you select for **VLAN attachment 1** is automatically applied to **VLAN attachment 2**. If you don't select a value, Cloud Interconnect uses 10 Gbps. The capacity that you select determines how many HA VPN tunnels you need to deploy.

  11. Under **VPN Gateway IP addresses** , select the type of IP addresses to use for your HA VPN gateway interfaces.

     * If you select **Internal regional IP addresses** , click **Add new IP address range** , and enter a **Name** and **IP range**. For the **IP range** , specify a regional internal IPv4 range with a prefix length between `26` and `29`. The prefix length determines the number of IP addresses available for the VPN gateway interfaces and must be based on the capacity of the attachment. For more information, see [Assign internal IP address ranges to HA VPN gateways](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/ha-vpn-interconnect-internal-ips).
     * If you select **External regional IP addresses** , Cloud Interconnect automatically assigns regional external IP addresses to the HA VPN tunnel interfaces that you create on your VLAN attachment.

Both VLAN attachments must use the same type of addressing, either internal or external, for their VPN gateway IP addresses.

  12. When you have created both VLAN attachments, click **Create**. The attachments take a few moments to create.

  13. After creation is complete, copy the [pairing keys](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology#pairingkey). You share these keys with your service provider when you request a connection with them.

If you're requesting a Layer 3 connection from your service provider, you can [pre-activate](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview#pre-activate) the attachment by selecting **Enable**. Activating attachments enables you to confirm that you're connecting to the expected service provider. Pre-activating attachments enables you to skip the [activation step](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/activating-connections) and lets the attachments start passing traffic immediately after your service provider completes their configuration.

  14. To view a list of your VLAN attachments, click **OK**.

The state of the VLAN attachment is `PENDING_PARTNER` until you request a connection with your service provider and they complete your VLAN attachment configuration. After the configuration is complete, the state of the attachment changes to `ACTIVE` or `PENDING_CUSTOMER`.

To activate your VLAN attachments, see [Activate connections](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/activating-connections).

**Note** : If your encrypted VLAN attachment remains in the `PENDING_PARTNER` or `Waiting for service provider` state for an extended period of time, contact your service provider for assistance.

Optional: You can update your BGP session to use custom learned routes. When you use this feature, the Cloud Router behaves as if it learned these routes from the BGP peer. For more information, see [Update an existing session to use custom learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configure-custom-learned-routes#add-routes-to-existing-session).

Optional: You can update your BGP sessions to use MD5 authentication. If you have a Layer 2 connection, follow the steps in [Add authentication to an existing session](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication#add-authentication). If you have a Layer 3 connection, contact your service provider for instructions.

Do not enable [Bidirectional Forwarding Detection (BFD)](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd). Enabling BFD at the Cloud Interconnect level does not provide faster failure detection for HA VPN tunnel traffic.

  15. After both of your VLAN attachments are active, you can complete the HA VPN over Cloud Interconnect deployment by configuring HA VPN for your VLAN attachments.

See [Configure HA VPN over Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/configure-ha-vpn-interconnect).




###  gcloud 

  1. Create an encrypted Cloud Router for Cloud Interconnect in the network and region that you want to reach from your on-premises network. Specify the `--encrypted-interconnect-router` flag to identify this router to use with the HA VPN over Cloud Interconnect deployment.

The Cloud Router must have a BGP ASN of `16550`.

The following example creates a router ASN of `16550`:
         
         gcloud compute routers create ROUTER_NAME \
              --region=REGION \
              --network=NETWORK_NAME \
              --asn 16550 \
              --encrypted-interconnect-router
         

Replace `NETWORK_NAME` with the name of your network.

  2. Optional: Reserve a regional internal IPv4 range with a prefix length between `26` and `29`. The prefix length determines the number of IP addresses available for the VPN gateway interfaces The number of addresses you need to reserve depends on the capacity of the associated VLAN attachment.

For example, to reserve a range for the first VLAN attachment with 10-Gbps capacity:
         
         gcloud compute addresses create ip-range-1 \
              --region=REGION \
              --addresses=192.168.1.0 \
              --prefix-length=29 \
              --network=NETWORK_NAME \
              --purpose=IPSEC_INTERCONNECT
         

To reserve an address range for the second VLAN attachment:
         
         gcloud compute addresses create ip-range-2 \
              --region=REGION \
              --addresses=192.168.2.0 \
              --prefix-length=29 \
              --network=NETWORK_NAME \
              --purpose=IPSEC_INTERCONNECT
         

For more information about reserving regional internal addresses, see [Assign internal IP address ranges to HA VPN gateways](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/ha-vpn-interconnect-internal-ips#gcloud).

  3. Create the first encrypted VLAN attachment of type `PARTNER`, specifying the names of your encrypted Cloud Router and the [edge availability domain](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology#edge-availability-domain) (metro availability zone) of the VLAN attachment. Google automatically adds an interface and a BGP peer on the Cloud Router. The attachment generates a [pairing key](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology#pairingkey) that you need to share with your service provider.

The following example creates an encrypted attachment for the edge availability domain `availability-domain-1`. The command also specifies the regional internal IP address range, `ip-range-1`, to use for all HA VPN gateway interfaces that are created on this attachment.
         
         gcloud compute interconnects attachments partner create ATTACHMENT_NAME_1 \
             --region=REGION \
             --router=ROUTER_NAME \
             --edge-availability-domain availability-domain-1 \
             --encryption IPSEC \
             --ipsec-internal-addresses ip-range-1
         

**Note:** You can specify `any` for the edge availability domain, and then your service provider assigns the domain for you. However, to create a redundant attachment (the second attachment), you need to wait until your service provider configures your first VLAN attachment. You won't know which domain to use for your redundant attachment until they complete the configuration.

If you want to use regional external IP addresses for the HA VPN gateway interfaces on your attachment, omit the `--ipsec-internal-addresses` flag. All HA VPN gateway interfaces are automatically assigned regional external IPv4 addresses.
         
         gcloud compute interconnects attachments partner create ATTACHMENT_NAME_1 \
             --region=REGION \
             --router=ROUTER_NAME \
             --edge-availability-domain availability-domain-1 \
             --encryption IPSEC
         

If you're requesting a Layer 3 connection from your service provider, you can [pre-activate](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview#pre-activate) the attachment by selecting `--admin-enabled` flag. Activating attachments enables you to confirm that you're connecting to the expected service provider. Pre-activating attachments enables you to skip the [activation step](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/activating-connections) and lets the attachments start passing traffic immediately after your service provider completes their configuration.

You cannot set a custom MTU (`--mtu`) with encrypted VLAN attachments. All encrypted VLAN attachments must use an MTU of 1440 bytes, which is the default value.

#### Use custom IP address ranges with Layer 2 connections

If you want to use custom IP address ranges with a Layer 2 connection, add the `--candidate-customer-router-ip-address` and `--candidate-cloud-router-ip-address` flags, which also support link-local IP addresses. Note that you can't combine these flags with the `--candidate-subnets` and `--subnet-length` flags, but you can use `--candidate-subnets` for link-local IPv4 attachments with the `--candidate-customer-router-ipv6-address` and `--candidate-cloud-router-ipv6-address` flags. For more information about why you might use custom IP address ranges, see [Custom IP address ranges](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview#custom-ip).

For more information about prerequisites, limitations and why you might use custom IP address ranges, see [Custom IP address ranges](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview#custom-ip).
         
         gcloud compute interconnects attachments partner create ATTACHMENT_NAME \
             --project=PROJECT_ID \
             --region=REGION \
             --router=ROUTER_NAME \
             --encryption IPSEC \
             --candidate-cloud-router-ip-address=CANDIDATE_CLOUD_ROUTER_IP_ADDRESS \
             --candidate-customer-router-ip-address=CANDIDATE_CUSTOMER_ROUTER_IP_ADDRESS
         

Replace the following:

     * `CANDIDATE_CLOUD_ROUTER_IP_ADDRESS`: the IPv4 CIDR address that you want to assign to the Cloud Router end of your VLAN attachment, like `192.0.2.1/29`
     * `CANDIDATE_CUSTOMER_ROUTER_IP_ADDRESS`: the IPv4 CIDR address that you want to assign to the customer router end of your VLAN attachment

If you use IPv6 dual-stack attachments, use the following command. 
    
    gcloud compute interconnects attachments partner create ATTACHMENT_NAME \
        --project=PROJECT_ID \
        --region=REGION \
        --router=ROUTER_NAME \
        --stack-type=IPV4_IPV6 \
        --encryption IPSEC \
        --candidate-cloud-router-ipv6-address=CANDIDATE_CLOUD_ROUTER_IP_ADDRESS \
        --candidate-customer-router-ipv6-address=CANDIDATE_CUSTOMER_ROUTER_IP_ADDRESS
    

Replace the following:

     * `CANDIDATE_CLOUD_ROUTER_IP_ADDRESS`: an IPv6 CIDR address, like `2001:db8::1/125`
     * `CANDIDATE_CUSTOMER_ROUTER_IP_ADDRESS`: an IPv6 CIDR address

You can use the `--candidate-cloud-router-ip-address` and `--candidate-customer-router-ip-address` flags alongside the `--candidate-cloud-router-ipv6-address` and `--candidate-customer-router-ipv6-address` flags to create an attachment that uses both IPv4 and IPv6 custom address ranges.

#### Use custom IP address ranges with Layer 3 connections

If you want to use custom IP address ranges with a Layer 3 connection, you create a new VLAN attachment and then your service provider configures the custom IP address ranges during their VLAN attachment configuration process. If you have a Layer 3 connection, contact your service provider for instructions.

Create the second encrypted VLAN attachment, specifying the names of your second Cloud Interconnect connection and the Cloud Router for Cloud Interconnect.

The following example creates an encrypted attachment for edge availability domain `availability-domain-2`. The command also specifies the regional internal IP address range, `ip-range-2`, to use for all HA VPN gateway interfaces that are created on this attachment.
    
    gcloud compute interconnects attachments partner create ATTACHMENT_NAME_2   
    
          --region=REGION   
    
          --router=ROUTER_NAME   
    
          --edge-availability-domain availability-domain-2   
    
          --encryption IPSEC   
    
          --ipsec-internal-addresses ip-range-2
      

When creating the second VLAN attachment, you must specify the same type of addressing scheme, either internal or external, that you used when you created the first attachment. Each VLAN attachment must be assigned a different internal address range. You can only specify one IP range for each attachment.

  4. Describe the attachments to retrieve their pairing keys; you need to share these keys with your service provider when you request a connection with them:

For the first VLAN attachment:
         
         gcloud compute interconnects attachments describe ATTACHMENT_NAME_1 \
              --region=REGION
         

The output is similar to the following:
         
         adminEnabled: false
         creationTimestamp: '2021-12-01T08:29:09.886-08:00'
         edgeAvailabilityDomain: AVAILABILITY_DOMAIN_1
         encryption: IPSEC
         id: '7976913826166357434'
         kind: compute#interconnectAttachment
         name: ATTACHMENT_NAME_1
         pairingKey: 7e51371e-72a3-40b5-b844-2e3efefaee59/REGION/1
         region: https://www.googleapis.com/compute/v1/projects/customer-project/regions/REGION
         router: https://www.googleapis.com/compute/v1/projects/customer-project/regions/REGION/routers/interconnect-router
         selfLink: https://www.googleapis.com/compute/v1/projects/customer-project/regions/REGION/interconnectAttachments/ATTACHMENT_NAME_1
         stackType: IPV4_ONLY
         state: PENDING_PARTNER
         type: PARTNER
         

For the second VLAN attachment:
         
         gcloud compute interconnects attachments describe ATTACHMENT_NAME_2 \
              --region=REGION
         

The output is similar to the following:
         
         adminEnabled: false
         creationTimestamp: '2021-12-01T08:29:09.886-08:00'
         edgeAvailabilityDomain: AVAILABILITY_DOMAIN_2
         encryption: IPSEC
         id: '7976913826166334235'
         kind: compute#interconnectAttachment
         name: ATTACHMENT_NAME_2
         pairingKey: 9f5fg371e-72a3-40b5-b844-2e3efefaee59/REGION/2
         region: https://www.googleapis.com/compute/v1/projects/customer-project/regions/REGION
         router: https://www.googleapis.com/compute/v1/projects/customer-project/regions/REGION/routers/interconnect-router
         selfLink: https://www.googleapis.com/compute/v1/projects/customer-project/regions/REGION/interconnectAttachments/ATTACHMENT_NAME_2
         stackType: IPV4_ONLY
         state: PENDING_PARTNER
         type: PARTNER
         

The `pairingKey` fields contain the pairing keys that you need to share with your service provider. Treat the pairing keys as sensitive information until your VLAN attachments are configured.

The state of the VLAN attachment is `PENDING_PARTNER` until you request a connection with your service provider and they complete your VLAN attachment configuration. After the configuration is complete, the state of the attachment changes to `ACTIVE` or `PENDING_CUSTOMER`.

To activate your VLAN attachments, see [Activate connections](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/activating-connections).

**Note** : If your encrypted VLAN attachment remains in the `PENDING_PARTNER` or `Waiting for service provider` state for an extended period of time, contact your service provider for assistance.

Optional: You can update your BGP session to use custom learned routes. When you use this feature, the Cloud Router behaves as if it learned the custom learned routes from the BGP peer. For more information, see [Update an existing session to use custom learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configure-custom-learned-routes#add-routes-to-existing-session).

Optional: You can update your BGP sessions to use MD5 authentication. If you have a Layer 2 connection, follow the steps in [Add authentication to an existing session](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication#add-authentication). If you have a Layer 3 connection, contact your service provider for instructions.

Do not enable [Bidirectional Forwarding Detection (BFD)](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/bfd). Enabling BFD at the Cloud Interconnect level does not provide faster failure detection for HA VPN tunnel traffic.

  5. After both of your VLAN attachments are active, you can complete the HA VPN over Cloud Interconnect deployment by configuring HA VPN for your VLAN attachments.

See [Configure HA VPN over Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/configure-ha-vpn-interconnect).




## Restrict Partner Interconnect usage

By default, any VPC network can use Cloud Interconnect. To control which VPC networks can use Cloud Interconnect, you can set an organization policy. For more information, see [Restrict Cloud Interconnect usage](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/restricting-usage). 

## What's next

  * To modify VLAN attachments, see [Modify VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/modifying-vlans).
  * To configure on-premises routers for Dedicated Interconnect, see [Configure on-premises routers](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/configuring-onprem-routers).



[ Previous arrow_back  Provisioning overview  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/provisioning-overview)

[ Next Request connections  arrow_forward  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/requesting-connections)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
