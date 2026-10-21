---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/configure-google-resources/
title: Configure your Google Cloud resources \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:55:09.664347+00:00
---

# Configure your Google Cloud resources  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/configure-google-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Configure your Google Cloud resources Stay organized with collections  Save and categorize content based on your preferences. 

You can extend your network across different cloud providers by using Google Cloud's Cross-Cloud Interconnect. To do this, you must configure the Google Cloud resources needed for Cross-Cloud Interconnect by completing the following tasks: 

  * Create two VLAN attachments, one for each of your Cross-Cloud Interconnect connections.
  * Configure Border Gateway Protocol (BGP) sessions, one for each VLAN attachment.



## Before you begin

This section lists required permissions, resources, and setup steps.

### Required roles

Before proceeding, you need the required permissions. Ask your administrator to make sure that you have the [Compute Network Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin) (`roles/compute.networkAdmin`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

### Required resources

Make sure that you have the following resources. 

#### VPC network

If you don't already have a Virtual Private Cloud (VPC) network, create one. For more information, see [Create and manage VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks). 

#### Cloud Router

To configure Cross-Cloud Interconnect, you need a Cloud Router. If you're working in the Google Cloud console, you can create your Cloud Router at the same time that you create your VLAN attachments. 

If you want to create a Cloud Router in advance, see [Create a Cloud Router to connect a VPC network to a peer network](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/create-router-vpc-network). Give the Cloud Router an ASN of `16550` or any private ASN in the `64512`-`65534` (inclusive) range. 

Place the Cloud Router in a region that's [supported for your Google Cloud location](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/choose-locations#supported-locations). 

### Project selection

If you're using the Google Cloud CLI, set your project ID by using the [`gcloud config set` command](https://docs.cloud.google.com/sdk/gcloud/reference/config/set).
    
    
    gcloud config set project PROJECT_ID

The gcloud CLI instructions on this page assume that you have set your project ID. 

## Check port status in Google Cloud

Before proceeding, verify that each of your Cross-Cloud Interconnect ports is receiving a signal from Alibaba.

### Console

  1. In the Google Cloud console, go to the Cloud Interconnect page.

[Go to Cloud Interconnect](https://console.cloud.google.com/hybrid/interconnects/list?tab=interconnects\))

  2. Click the name of your Cross-Cloud Interconnect connection.
  3. On the **Interconnect details** page, make sure that the value in the **Status** column is **Active**. 

If Google Cloud displays a page titled **Cross-Cloud Interconnect order confirmation** , then your connection isn't ready for configuration. 




## Create VLAN attachments

A VLAN attachment is a logical connection between a single region in your VPC network and a peer network (in this case, your Alibaba network).

To qualify for the service level agreement (SLA), create at least one VLAN attachment for each Cross-Cloud Interconnect connection. You can also create more attachments for each connection, but certain [quotas and limits](https://docs.cloud.google.com/network-connectivity/docs/interconnect/quotas#quotas) apply.

### Console

  1. In the Google Cloud console, go to the Cloud Interconnect page.

[Go to Cloud Interconnect](https://console.cloud.google.com/hybrid/interconnects/list?tab=interconnects\))

  2. Click the name of your primary Cross-Cloud Interconnect connection.
  3. On the **Interconnect details** page, click **Add VLAN attachment**.
  4. Fill out the **Select interconnects & redundancy** form: 
     * In the **Redundancy** section, select **Create a redundant pair of VLAN attachments (recommended)**.
     * In the **Interconnects** section, do the following:
       * Make sure that the **Interconnect A** field displays the name of your primary Cross-Cloud Interconnect port.
       * Set the **Interconnect B** field to the name of your redundant Cross-Cloud Interconnect port.
  5. Click **Continue**.
  6. Fill out the **Create VLAN attachment for Interconnect A** form: 
     * Enter a name.
     * Optional: Enter a description.
     * Select a stack type: either **IPv4 (single-stack)** or **IPv4 and IPv6 (dual-stack)**.
     * Select a Cloud Router from the **Cloud Router** list. If no routers are listed, click **Create new router** and follow the prompts to add a new one. The Cloud Router must be located in a region that's [supported for your Google Cloud location](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/choose-locations#supported-locations). Give the Cloud Router an ASN of `16550` or any private ASN in the `64512`-`65534` (inclusive) range. 
     * Enter a **VLAN ID** that's between **2** and **4094** and unique among the VLAN attachments associated with this connection. Typically, in Google Cloud, you can enter a broader range of possible IDs. However, you must use this value again in Alibaba, and Alibaba has more narrow requirements than Google Cloud.
  7. Expand the **Advanced options** section of the form and make any needed changes: 
     * If you want to specify an IP address range for the attachment, do one of the following: 
       * Set the **Allocate BGP IP address** field to **Specify a candidate link-local range** and enter an IP address range.
       * Set the **Allocate BGP IP address** field to **Specify custom IP address**.

For more information about custom IP addresses, see [Custom IP address ranges](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview#custom-ip).

Note that you can't combine custom IPv4 addresses with candidate subnets. In addition, if you use the **dual stack** stack type, you can choose to set custom IP addresses for only your IPv4 addresses, only your IPv6 addresses, or both your IPv4 and IPv6 addresses; you can combine custom IP addresses in one field with automatic allocation or candidate link-local ranges in the other field if those options are available.

In the **Allocate BGP IPv4 addresses** or **Allocate BGP IPv6 addresses** sections, enter the following information:

         * In the **Cloud Router IP** field, enter the IPv4/IPv6 CIDR address that you want to assign to the Cloud Router end of your VLAN attachment, like `192.0.2.0/29` or `2001:db8::1/125`.
         * In the **Peer IP** field, enter the IPv4/IPv6 CIDR address that you want to assign to the customer router end of your VLAN attachment.
     * For **Capacity** , choose a capacity setting for the attachment.
     * Optional: If appropriate, change the **MTU** value from its default of **1440**. For help with this field, see [Cloud Interconnect MTU](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview#interconnect-mtu).

We recommend leaving the **IPv4 subnet mask** set to `/29`.

  8. Click **Next**. 

The page updates to show a form for the second attachment.

  9. Enter details about the redundant attachment: 
     * Enter a name.
     * Optional: Enter a description.
     * Select a Cloud Router that's in the same region as the router that you used for the first attachment. You can use the same Cloud Router.
     * Enter a **VLAN ID** for the redundant attachment. We recommend that you use the same value that you used for the first attachment.
     * If you want to specify an IP address range for the attachment, do one of the following: 
       * Set the **Allocate BGP IP address** field to **Specify a candidate link-local range** and enter an IP address range.
       * Set the **Allocate BGP IP address** field to **Specify custom IP address** For more information about custom IP addresses, see [Custom IP address ranges](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview#custom-ip).

For more information about prerequisites, limitations and why you might use custom IP address ranges, see [Custom IP address ranges](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview#custom-ip).

Note that you can't combine custom IPv4 addresses with candidate subnets. In addition, if you use the **dual stack** stack type, you can choose to set custom IP addresses for only your IPv4 addresses, only your IPv6 addresses, or both your IPv4 and IPv6 addresses; you can combine custom IP addresses in one field with automatic allocation or candidate link-local ranges in the other field if those options are available.

In the **Allocate BGP IPv4 addresses** or **Allocate BGP IPv6 addresses** sections, enter the following information:

         * In the **Cloud Router IP** field, enter the IPv4/IPv6 CIDR address that you want to assign to the Cloud Router end of your VLAN attachment, like `192.0.2.0/29` or `2001:db8::1/125`.
         * In the **Peer IP** field, enter the IPv4/IPv6 CIDR address that you want to assign to the customer router end of your VLAN attachment.
  10. Click **Next** , and continue to the next section, Configure BGP sessions.



### gcloud

Use the [`gcloud compute interconnects attachments dedicated create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/dedicated/create). 

We recommend that you do not set a value for `--subnet-length` but accept the default value of `29`. 

Complete the following steps: 

  1. Create the primary attachment:
         
         gcloud compute interconnects attachments dedicated create VLAN_ATTACHMENT_NAME \
             --interconnect CONNECTION \
             --router ROUTER \
             --region REGION \
             --bandwidth BANDWIDTH \
             --vlan ID \
             --mtu MTU

Replace the following:

     * `VLAN_ATTACHMENT_NAME`: the name for this VLAN attachment
     * `CONNECTION`: the name of your primary Cross-Cloud Interconnect connection
     * `ROUTER`: the Cloud Router that you want to use for the attachment; unless you are using [global dynamic routing mode](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#am-subnets-global), the router must be located in a [supported Google Cloud location](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/choose-locations#supported-locations)
     * `REGION`: the region where the Cloud Router is located
     * `BANDWIDTH`: the bandwidth for this VLAN attachment in Mbps or Gbps—for example, for 50 Mbps, enter `50m`, or for 10 Gbps, enter `10g`
     * `ID`: a number between `2` and `4094` that's unique among the VLAN attachments associated with this connection 
     * `MTU`: the MTU to use 

If you don't set a value, the default of `1440` is used. For help with setting this field, see [Cloud Interconnect MTU](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview#interconnect-mtu).

#### Configure custom IP address ranges

Alternatively, you can create the VLAN attachments with custom IP address ranges. For more information about custom IP addresses, see [Custom IP address ranges](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview#custom-ip).

Use the following command to configure custom IP address ranges for an attachment with the `IPV4_ONLY` stack type:
    
    gcloud compute interconnects attachments dedicated create VLAN_ATTACHMENT_NAME \
        --interconnect CONNECTION \
        --router ROUTER \
        --region REGION \
        --bandwidth BANDWIDTH \
        --vlan ID \
        --mtu MTU \
        --stack-type=IPV4_ONLY \
        --candidate-cloud-router-address=ADDRESS_RANGE_1 \
        --candidate-customer-router-address=ADDRESS_RANGE_2

Replace the following:

     * `VLAN_ATTACHMENT_NAME`: the name for this VLAN attachment
     * `CONNECTION`: the name of your primary Cross-Cloud Interconnect connection
     * `ROUTER`: the Cloud Router that you want to use for the attachment; unless you are using [global dynamic routing mode](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#am-subnets-global), the router must be located in a [supported Google Cloud location](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/choose-locations#supported-locations)
     * `REGION`: the region where the Cloud Router is located
     * `BANDWIDTH`: the bandwidth for this VLAN attachment in Mbps or Gbps—for example, for 50 Mbps, enter `50m`, or for 10 Gbps, enter `10g`
     * `ID`: a number that's unique among the VLAN attachments associated with this connection
     * `MTU`: the MTU to use 

If you don't set a value, the default of `1440` is used. For help with setting this field, see [Cloud Interconnect MTU](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview#interconnect-mtu).

     * `ADDRESS_RANGE_1`: the IPv4 address range that you want to assign to the Cloud Router end of your VLAN attachment
     * `ADDRESS_RANGE_2`: the IPv4 address range that you want to assign to the customer router end of your VLAN attachment

Alternatively, use the following command to configure custom IP address ranges for an attachment with the `IPV4_IPV6` stack type:
    
    gcloud compute interconnects attachments dedicated create VLAN_ATTACHMENT_NAME \
        --interconnect CONNECTION \
        --router ROUTER \
        --region REGION \
        --bandwidth BANDWIDTH \
        --vlan ID \
        --mtu MTU \
        --stack-type=IPV4_IPV6 \
        --candidate-cloud-router-address=ADDRESS_RANGE_1 \
        --candidate-customer-router-address=ADDRESS_RANGE_2 \
        --candidate-cloud-router-ipv6-address=ADDRESS_RANGE_3 \
        --candidate-customer-router-ipv6-address=ADDRESS_RANGE_4

Replace the following:

     * `VLAN_ATTACHMENT_NAME`: the name for this VLAN attachment
     * `CONNECTION`: the name of your primary Cross-Cloud Interconnect connection
     * `ROUTER`: the Cloud Router that you want to use for the attachment; unless you are using [global dynamic routing mode](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#am-subnets-global), the router must be located in a [supported Google Cloud location](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/choose-locations#supported-locations)
     * `REGION`: the region where the Cloud Router is located
     * `BANDWIDTH`: the bandwidth for this VLAN attachment in Mbps or Gbps—for example, for 50 Mbps, enter `50m`, or for 10 Gbps, enter `10g`
     * `ID`: a number that's unique among the VLAN attachments associated with this connection
     * `MTU`: the MTU to use 

If you don't set a value, the default of `1440` is used. For help with setting this field, see [Cloud Interconnect MTU](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview#interconnect-mtu).

     * Use the following values to configure custom IP address ranges. You can omit the flags that use these values if you have configured candidate subnets, or if you don't want to configure custom IP address ranges. In addition, you might choose to omit either pair of IPv4 or IPv6 address ranges if you want to use automatic allocation for that protocol. 
       * `ADDRESS_RANGE_1`: the IPv4 address range that you want to assign to the Cloud Router end of your VLAN attachment
       * `ADDRESS_RANGE_2`: the IPv4 address range that you want to assign to the customer router end of your VLAN attachment
       * `ADDRESS_RANGE_3`: the IPv6 address range that you want to assign to the Cloud Router end of your VLAN attachment, like `2001:db8::1/125`
       * `ADDRESS_RANGE_4`: the IPv6 address range that you want to assign to the customer router end of your VLAN attachment
  2. Create the redundant attachment:
         
         gcloud compute interconnects attachments dedicated create VLAN_ATTACHMENT_NAME_2 \
             --interconnect CONNECTION_2 \
             --router ROUTER_2 \
             --region REGION\
             --bandwidth BANDWIDTH \
             --vlan ID \
             --mtu MTU

Replace the following:

     * `VLAN_ATTACHMENT_NAME_2`: the name that you want to give to this VLAN attachment
     * `CONNECTION_2`: the name of your redundant Cross-Cloud Interconnect connection
     * `ROUTER_2`: the Cloud Router that you want to use for the redundant attachment 

It must be located in the same region as the Cloud Router that you used for the primary attachment. You can also use the same Cloud Router that you used for the primary attachment.

     * `REGION`: the region where the Cloud Router is located

The following fields use the same values as the primary attachment:

     * `BANDWIDTH`
     * `ID`
     * `MTU`



## Configure BGP sessions

Cross-Cloud Interconnect uses BGP to exchange routes between your VPC network and your Alibaba network. To that end, configure a BGP session for each of your VLAN attachments. The sessions aren't active until you configure your Alibaba resources, but you can configure the Google Cloud side of the sessions now.

### Console

  1. Configure the first session. 
     1. Do one of the following: 
        * If the **Configure Cloud Routers** form is displayed, locate the name of your primary VLAN attachment and click **Configure**.
        * If the form isn't open, go to the Cloud Interconnect [**VLAN attachments**](https://console.cloud.google.com/hybrid/interconnects/list?tab=attachments) tab. Click the name of the attachment. In the **Connection** section of the form, click **Configure BGP session**.
     2. Fill out the **Create BGP session** form: 
        * Enter a name for the session.
        * In the **Peer ASN** field, enter a value to represent the Alibaba side of the peering. Use `45104`.
        * Optional: Enter a value in the **Advertised route priority** field. For information about this field, see [Advertised prefixes and priorities](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#advertised-priority).
        * Optional: Set **MD5 Authentication** to **Enabled** , and enter your secret MD5 authentication key. Later, when you configure peering in Alibaba, you must use the same key on the Alibaba side of peering. Alibaba supports only alphanumeric characters for the key. For more information about Google Cloud support for MD5 authentication, see [Use MD5 authentication](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication). 
        * Click **Save and continue**.
  2. Configure the second session. 
     1. Do one of the following: 
        * If you are in the **Configure Cloud Routers** form, locate the name of your redundant VLAN attachment and click **Configure**.
        * If the form isn't open, go to the Cloud Interconnect [**VLAN attachments**](https://console.cloud.google.com/hybrid/interconnects/list?tab=attachments) tab. Click the name of the redundant attachment, and then click **Configure**.
     2. In the **Create BGP session** form, enter the following values: 
        * Enter a name for the session.
        * For **Peer ASN** , enter the same peer ASN that you used for the BGP session on the primary attachment.
        * Optional: Enter a value for **Advertised route priority**. For information about this field, see [Advertised prefixes and priorities](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#advertised-priority).
        * Optional: Set **MD5 Authentication** to **Enabled** , and enter your secret MD5 authentication key. Later, when you configure peering in Alibaba, you must use the same key on the Alibaba side of peering. 
        * Click **Save and continue**.
  3. Click **Save configuration**.
  4. Click **Finish setup**.



### gcloud

To create the required BGP sessions, you must create two interfaces on the Cloud Router used by your VLAN attachments. If each of your attachments uses a different Cloud Router, configure an interface on each Cloud Router. After you create your interfaces, create a peering session for each interface.

To complete this setup, you use the [`gcloud compute routers add-interface` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/add-interface) and the [`gcloud compute routers add-bgp-peer` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/add-bgp-peer).

Complete the following steps:

  1. Create the primary interface: 
         
         gcloud compute routers add-interface ROUTER_NAME \
             --interface-name=INTERFACE \
             --interconnect-attachment=ATTACHMENT \
             --region=REGION

Replace the following:

     * `ROUTER_NAME`: the name of the Cloud Router used by your primary VLAN attachment
     * `INTERFACE`: the name of the new interface
     * `ATTACHMENT`: the name of your primary VLAN attachment
     * `REGION`: the region where the Cloud Router is located
  2. Create the redundant interface: 
         
         gcloud compute routers add-interface ROUTER_NAME_2 \
             --interface-name=INTERFACE_2 \
             --interconnect-attachment=ATTACHMENT_2 \
             --region=REGION

Replace the following:

     * `ROUTER_NAME_2`: the name of the Cloud Router used by your redundant VLAN attachment
     * `INTERFACE_2`: the name of the redundant interface
     * `ATTACHMENT_2`: the name of your redundant VLAN attachment
     * `REGION`: the region where the Cloud Router is located
  3. Create a BGP session for the primary VLAN attachment: 
         
         gcloud compute routers add-bgp-peer ROUTER_NAME \
             --interface=INTERFACE \
             --peer-asn=--peer-asn=45104 \
             --peer-name=PEER_NAME \
             --region=REGION \
             --md5-authentication-key=YOUR_KEY

Replace the following:

     * `ROUTER_NAME`: the name of the Cloud Router used by your primary VLAN attachment
     * `INTERFACE`: the name of the primary interface
     * `PEER_NAME` the name of the peer
     * `REGION`: the region where the Cloud Router is located
     * `YOUR_KEY`: the secret key to use for MD5 authentication; later, when you configure peering in Alibaba, you must use the same key 
  4. Create a BGP session for the redundant VLAN attachment: 
         
         gcloud compute routers add-bgp-peer ROUTER_NAME_2 \
             --interface=INTERFACE_2 \
             --peer-asn=--peer-asn=45104 \
             --peer-name=PEER_NAME_2 \
             --region=REGION \
             --md5-authentication-key=YOUR_KEY_2

Replace the following:

     * `ROUTER_NAME_2`: the name of the Cloud Router used by your primary VLAN attachment
     * `INTERFACE_2`: the name of the primary interface
     * `PEER_NAME_2`:the name of the peer
     * `REGION`: the region where the Cloud Router is located
     * `YOUR_KEY_2`: the secret key to use for MD5 authentication; later, when you configure peering in Alibaba, you must use the same key 



## Get details about your VLAN attachments

After you create your VLAN attachments, retrieve the details that you need to configure your Alibaba resources.

### Console

  1. In the Google Cloud console, go to the Cloud Interconnect page.

[Go to Cloud Interconnect](https://console.cloud.google.com/hybrid/interconnects/list?tab=attachments)

  2. Click the name of your primary VLAN attachment.
  3. Make a note of the **Cloud Router BGP IP** and **BGP Peer IP** values. You need these values when you configure your Alibaba resources.
  4. Repeat the preceding steps for your redundant attachment.



### gcloud

Use the [`gcloud compute interconnects attachments describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/describe). Run the following command twice—once for each attachment: 
    
    
    gcloud compute interconnects attachments describe NAME --region REGION
         

Replace the following:

  * `NAME`: the name of the VLAN attachment
  * `REGION`: the region where the VLAN attachment is located



The command returns output that includes `cloudRouterIpAddress` and `customerRouterIpAddress`. Make a note of these values. You need them when you configure your Alibaba resources.

[ Previous arrow_back  Order Alibaba Cloud ports  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/order-alibaba-ports)

[ Next Configure your Alibaba Cloud resources  arrow_forward  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/configure-alibaba)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
