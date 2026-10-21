---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-oci/creating-vlan-attachments/
title: Create VLAN attachments \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:55:11.330178+00:00
---

# Create VLAN attachments  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-oci/creating-vlan-attachments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Create VLAN attachments Stay organized with collections  Save and categorize content based on your preferences. 

VLAN attachments for partner Cross-Cloud Interconnect for Oracle Cloud Infrastructure (OCI) connections (also known as `interconnectAttachment` resources) connect the Google Cloud Virtual Private Cloud (VPC) network to the Oracle Cloud Infrastructure virtual cloud network (VCN) by allocating VLANs over existing connections between the two cloud providers.

You can create unencrypted VLAN attachments, which support both IPv4 only (single stack) or IPv4 and IPv6 (dual stack).

Before you can create VLAN attachments for partner Cross-Cloud Interconnect for OCI, you must already have an OCI account.

Hourly billing for VLAN attachments starts when OCI completes its configurations, whether or not you pre-activated your attachments. OCI configures your attachments when they are in the `PENDING_CUSTOMER` or `ACTIVE` state. Billing stops when you or OCI deletes the attachments (when they are in the `DEFUNCT` state). You are not billed for data transfer between the two clouds.

For definitions of terms used on this page, see [Cloud Interconnect key terms](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology).

To help you solve common issues that you might encounter when using partner Cross-Cloud Interconnect for OCI, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting#partner).

To configure the Google Cloud resources needed for partner Cross-Cloud Interconnect for OCI, complete the following tasks: 

  * Create two VLAN attachments, one for each of your partnerCross-Cloud Interconnect for OCI connections.
  * Configure Border Gateway Protocol (BGP) sessions, one for each VLAN attachment.



## Before you begin

This section lists required permissions, resources, and setup steps.

### Required roles

Before proceeding, you need the required permissions. Ask your administrator to make sure that you have the [Compute Network Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin) (`roles/compute.networkAdmin`) IAM role on the project. For more information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

### Required resources

Make sure that you have the following resources. 

#### VPC network

If you don't already have a Virtual Private Cloud (VPC) network, create one. For more information, see [Create and manage VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks). 

#### Cloud Router

To configure partner Cross-Cloud Interconnect for OCI, you need a Cloud Router. If you're working in the Google Cloud console, you can create your Cloud Router at the same time that you create your VLAN attachments. 

If you want to create a Cloud Router in advance, see [Create a Cloud Router to connect a VPC network to a peer network](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/create-router-vpc-network). Give the Cloud Router an ASN of `16550` or any private ASN in the `64512`-`65533` (inclusive) range except ASN `65534`. For more information about the ASNs that OCI reserves for itself, see the [OCI documentation](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectcolocate.htm#FastConnect_Colocation_with_Oracle). 

Place the Cloud Router in a region that's [supported for your Google Cloud location](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/oci/choose-locations#supported-locations). 

### Project selection

If you're using the Google Cloud CLI, set your project ID by using the [`gcloud config set` command](https://docs.cloud.google.com/sdk/gcloud/reference/config/set).
    
    
    gcloud config set project PROJECT_ID

The gcloud CLI instructions on this page assume that you have set your project ID. 

## Utilize multiple VLAN attachments

VLAN attachments support traffic speeds up to 50 Gbps or 6.25 M packets per second (pps). Throughput depends on which limit you reach first. For example, if your traffic uses very small packets, you may reach the 6.25 M pps limit before the 50 Gbps limit.

To achieve higher throughput into a VPC network, you must configure multiple VLAN attachments into the VPC network. For each Border Gateway Protocol (BGP) session, you must use the same MED values to let the traffic use equal-cost multipath (ECMP) routing over all the configured VLAN attachments.

**Note:** Creating VLAN attachments with a combined bandwidth greater than the Cloud Interconnect connection doesn't give you more than the maximum stated bandwidth of the connection.

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

  1. In the Google Cloud console, go to the **Interconnect** page.

[Go to Interconnect](https://console.cloud.google.com/hybrid/interconnects/list?tab=attachments)

  2. On the **VLAN attachments** tab, click add**Create VLAN attachments**.

  3. Select **Partner Interconnect connection**.

  4. In the **Encrypt interconnect** section, select **Set up unencrypted Interconnect** , and then click **Continue**.

  5. Select **I already have a service provider**.

  6. Select **Create a redundant pair of VLAN attachments**. Redundancy provides higher availability than a single connection. Both attachments serve traffic, and the traffic is load balanced between them. If one attachment goes down, such as during a scheduled maintenance, the other attachment continues to serve traffic. For more information, see [Redundancy and SLA](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview#redundancy).

If you're creating an attachment for testing purposes or don't require high availability, select **Create a single VLAN** to create only one VLAN attachment.

  7. For the **Network** and **Region** fields, select the VPC network and [Google Cloud region](https://docs.cloud.google.com/docs/geography-and-regions) where your attachments are to connect.

  8. Specify the details of your VLAN attachments:

     * **Cloud Router** : a Cloud Router to associate with this attachment. You can only choose a Cloud Router in the VPC network and region that you selected with an ASN of `16550`. If you don't have an existing Cloud Router, [create one](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/create-router-vpc-network) with an ASN of `16550`. Each VLAN attachment can be associated with a single Cloud Router. Google automatically adds an interface and a BGP peer on the Cloud Router.

     * **VLAN attachment name** : a name for the attachment. This name is displayed in the Google Cloud console and is used by the Google Cloud CLI to reference the attachment—for example, `my-attachment`.

     * **IP stack type** : the IP stack type. Either **IPv4 (single-stack)** , or **IPv4 and IPv6 (dual-stack)**.

     * **Maximum transmission unit (MTU)** : the MTU for the attachment. To use the 1460-, 1500-, or 8896-byte maximum transmission unit (MTU), [the VPC network that uses the attachment must have an MTU set to the same value](https://docs.cloud.google.com/vpc/docs/mtu). In addition, the OCI VM must set the same MTU.

  9. To create the attachments, click **Create**. This action takes a few minutes to complete.

  10. After creation is complete, copy the [pairing keys](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology#pairingkey). You share these keys with OCI when you create your FastConnect virtual circuit with OCI.

You can [pre-activate](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview#pre-activate) the attachment by selecting **Enable**. Activating attachments lets you confirm that you're connecting to the expected service provider. Pre-activating attachments lets you skip the [activation step](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/activating-connections) and lets the attachments start passing traffic immediately after your virtual circuit is created.

  11. To view a list of your VLAN attachments, click **OK**.




You can optionally update your BGP sessions to [use MD5 authentication](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication).

Optional: You can update your BGP session to use custom learned routes. When you use this feature, the Cloud Router behaves as if it learned these routes from the BGP peer. For more information, see [Update an existing session to use custom learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configure-custom-learned-routes#add-routes-to-existing-session).

**Note:** OCI doesn't support Bidirectional Forwarding Detection (BFD).

###  gcloud 

Before you create a VLAN attachment, you must have an existing Cloud Router in the network and region that you want to reach from your on-premises network. If you don't have an existing Cloud Router, [create one](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/create-router-vpc-network). The Cloud Router must have a BGP ASN of `16550`.

  1. Create a VLAN attachment of type `PARTNER`, specifying the names of your Cloud Router and the [edge availability domain](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology#edge-availability-domain) (metro availability zone) of the VLAN attachment.

Google automatically adds an interface and a BGP peer on the Cloud Router. The attachment generates a [pairing key](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology#pairingkey) that you need to share with OCI.

You can specify the MTU of your attachment. Valid values are `1440` (default), `1460`, `1500`, and `8896`. To specify an MTU of `1460`, `1500`, or `8896` use the`--mtu` parameter—for example, `--mtu 1500`. To make use of the 1460-, 1500-, or 8896-byte MTU, [the VPC network that uses the attachment must set the same MTU](https://docs.cloud.google.com/vpc/docs/mtu). In addition, the OCI VM must set the same MTU.

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
**Note:** You can specify `any` for the edge availability domain, and then OCI assigns the domain for you. However, to create a redundant attachment (the second attachment), you need to wait until OCI configures your first VLAN attachment. You won't know which domain to use for your redundant attachment until OCI completes the configuration. You can [pre-activate](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview#pre-activate) the attachment by selecting the `--admin-enabled` flag. Activating attachments lets you confirm that you're connecting to the expected service provider. Pre-activating attachments lets you skip the [activation step](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/activating-connections) and lets the attachments start passing traffic immediately after your service provider completes their configuration.
    
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
  2. Describe the attachment to retrieve its pairing key; you need to share this key with OCI when you create the virtual circuit with OCI:
         
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
         

The `pairingKey` field contains the pairing key that you need to share with OCI. Treat the pairing key as sensitive information until your VLAN attachment is configured.

The state of the VLAN attachment is `PENDING_PARTNER` until you request a connection with OCI and it completes your VLAN attachment configuration. After the configuration is complete, the state of the attachment changes to `ACTIVE` or `PENDING_CUSTOMER`.

  3. Optional: You can update your BGP session to use custom learned routes. When you use this feature, the Cloud Router behaves as if it learned these routes from the BGP peer. For more information, see [Update an existing session to use custom learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configure-custom-learned-routes#add-routes-to-existing-session).

  4. Optional: You can update your BGP sessions to [use MD5 authentication](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/use-md5-authentication).


**Note:** OCI doesn't support Bidirectional Forwarding Detection (BFD).

If you're building redundancy with a duplicate VLAN attachment, repeat these steps for the second attachment. Use the same Cloud Router, but specify a different edge availability domain. Also, when you request connections from OCI, you must select the same metropolitan area (city) for both attachments for them to be redundant. For more information, see [Redundancy and SLA](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview#redundancy).

**Note:** When your service provider completes the VLAN attachment configuration, Google automatically configures an interface and a BGP peering session on the associated Cloud Router. Don't modify these Google-defined configurations because doing so shuts down the BGP session. However, if you delete your attachment, you can delete these configurations.

## Get details about your VLAN attachments

After you create your VLAN attachments, retrieve the details that you need to configure your OCI resources.

### Console

  1. In the Google Cloud console, go to the **Interconnect** page.

[Go to **Interconnect**](https://console.cloud.google.com/hybrid/interconnects/list?tab=attachments\))

  2. On the **VLAN attachments** tab, click the name of your primary VLAN attachment.
  3. Make a note of the **Cloud Router BGP IP** and **BGP Peer IP** values. You need these values when you configure your OCI resources.
  4. Repeat the preceding steps for your redundant attachment.



### gcloud

Use the [`gcloud compute interconnects attachments describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/interconnects/attachments/describe). Run the following command twice—once for each attachment: 
    
    
    gcloud compute interconnects attachments describe NAME --region REGION
         

Replace the following:

  * `NAME`: the name of the VLAN attachment
  * `REGION`: the region where the VLAN attachment is located



The command returns output that includes `cloudRouterIpAddress` and `customerRouterIpAddress`. Make a note of these values. You need them when you configure your OCI resources.

## Restrict partner Cross-Cloud Interconnect for Oracle Cloud Infrastructure (OCI) usage

By default, any VPC network can use Cloud Interconnect. To control which VPC networks can use Cloud Interconnect, you can set an organization policy. For more information, see [Restrict Cloud Interconnect usage](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/restricting-usage). 

For information about how to configure Oracle Cloud Infrastructure resources, see [Configure OCI resources](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/access-to-google-cloud-platform.htm#unique_1286836570) in the OCI documentation.

## What's next

  * To find answers to common questions about Cloud Interconnect architecture and features, see the [Cloud Interconnect FAQ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/faq).
  * To find out more about Cloud Interconnect, see the [Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview).
  * To learn about best practices when planning for and configuring Cloud Interconnect, see [Best practices](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/best-practices).
  * To find Google Cloud resource names, see the [Cloud Interconnect APIs](https://docs.cloud.google.com/network-connectivity/docs/interconnect/reference/apis).



[ Previous arrow_back  Paired locations  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-oci/paired-locations)

[ Next Request OCI connections  arrow_forward  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-oci/requesting-oci-connections)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
