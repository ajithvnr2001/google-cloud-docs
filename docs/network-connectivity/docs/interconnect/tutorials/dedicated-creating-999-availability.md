---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/dedicated-creating-999-availability/
title: Establish 99.9% availability for Dedicated Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:55:04.936544+00:00
---

# Establish 99.9% availability for Dedicated Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/dedicated-creating-999-availability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Establish 99.9% availability for Dedicated Interconnect Stay organized with collections  Save and categorize content based on your preferences. 

Note: For production-level applications, see [Establish 99.99% availability for Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/dedicated-creating-9999-availability). Google recommends this configuration for high availability. 

The topology for 99.9% [availability](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview#redundancy) is suitable for non-critical applications that can tolerate some downtime. For example, your organization might do batch uploads for which the timing of the operation isn't critical. If a connection isn't available, the operation continues when connectivity is restored.

For Cloud Interconnect terminology used on this page, see [Key terms](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology).

For information about creating redundant Cloud Interconnect connections that have sufficient capacity in a failover scenario, see [Best practices](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/best-practices#capacity).

## Requirements

The following are the requirements to achieve 99.9% availability.

  * You must configure at least two Dedicated Interconnect connections, distributed strategically between a pair of _facility and edge availability domain combinations_ within a single metro:

    * **Identify facility and edge availability domain combinations** : 

      * If the metro has a single facility, the pair of facility and edge availability domain combinations are the two edge availability domains in the one facility of that metro (for example, `bos-zone1-219` and `bos-zone2-219`).

      * If the metro has two or more facilities, a valid pair of facility and edge availability domain combinations consists of zone 1 in one facility and zone 2 in a different facility of the metro (for example, `atl-zone1-3725` and `atl-zone2-940`).

    * **Use both facility and edge availability domain combinations** : within the metro, at least one interconnect connection must be in one facility and edge availability domain combination, and at last one interconnect connection must be in the other combination of the pair.

  * The following requirements apply to each VPC network in which you create VLAN attachments that depend on the Cloud Interconnect connections.

    * **VLAN attachments** : you must configure at least two VLAN attachments, all in one region. Each VLAN attachment must depend on a unique interconnect connection. Collectively, the VLAN attachments must use all configured interconnect connections.

    * **Cloud Routers** : you must use at least one Cloud Router in the region where VLAN attachments are configured. Using more than one Cloud Router doesn't add reliability or change the SLA because Cloud Routers automatically distribute the BGP sessions of VLAN attachments between two [BGP software tasks](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/how-cloud-router-works#bgp-tasks), based on the edge availability domain of the interconnect connection that each VLAN attachment depends on.

    * **Dynamic routing mode** : the VPC network can use either regional or global [dynamic routing mode](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes#dynamic-routing-mode).




### On-premise router and route advertisement requirements

Consult the documentation for your on-premises routers to determine how to configure them for a 99.9% SLA. You might need to connect a unique physical router to each interconnect connection.

On-premises routers must advertise the same prefixes over the BGP sessions of each VLAN attachment. You can use different BGP metrics (like MED) to achieve your connectivity goals. For more information about how Cloud Router BGP tasks, the dynamic route control plane, and the VPC network control plane create dynamic routes from received prefixes, see [Learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes#custom-learned-routes) in the Cloud Router documentation.

### Example topology

The following example topology meets the 99.9% availability with two Cloud Interconnect connections in the following facility and edge availability domain combinations:

  * `lga-zone1-16`
  * `lga-zone2-1422`



Two VLAN attachments, collectively using both interconnect connections, are located in the `us-central1` region of a single VPC network.

[ ![Redundant connections for 99.9% availability \(click to enlarge\).](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/sla-999.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/sla-999.svg) Redundant connections for 99.9% availability (click to enlarge)

## Configure preferred paths

Dedicated Interconnect VLAN attachments depend on Cloud Routers to learn prefixes from remote peer routers (for example, routers in an on-premises network). The dynamic routing mode and best path selection mode of the VPC network that contains the Cloud Routers control which next hops are considered, and how BGP attributes are processed to produce [dynamic routes](https://docs.cloud.google.com/vpc/docs/routes#dynamic_routes). The dynamic routes in a VPC network define paths from the VPC network to a connected network (like an on-premises network). For more information, see [Learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes) in the Cloud Router documentation.

To create paths from the connected network to the VPC network, you configure Cloud Router BGP advertisements. You can configure advertisements on each BGP session individually, or define advertisement defaults for the Cloud Router. These advertisements can include subnet ranges, custom prefixes, or a combination of subnet ranges and custom prefixes. For more information, see [Advertised routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes) in the Cloud Router documentation.

## Create a 99.9% topology

The following sections walk through the steps for creating this topology. To create a topology that's tailored for you, replace the sample input values with your own. For example, replace the `vpc1` network name with your VPC network name.

### Order Cloud Interconnect connections

Order duplicate connections by using the Google Cloud console or the Google Cloud CLI.

###  Console 

  1. In the Google Cloud console, go to the **Interconnect Hybrid Connectivity** page.

[Go to Interconnect Hybrid Connectivity](https://console.cloud.google.com/hybrid/interconnects/list?tab=interconnects)

  2. Click **Get started**.

  3. Select **Dedicated Interconnect** , and then click **Continue**.

  4. Select **Order new Dedicated Interconnect** , and then click **Continue**.

  5. Specify the details for the Cloud Interconnect connection:

     * **Name** : Enter `int-lga1`.
     * **Description** : Enter `Example Cloud Interconnect connection in LGA ZONE1`.
     * **Location** : Choose `Digital Realty | Telx New York (111 8th Ave)`, which is the PeeringDB name for the `lga-zone1-16` location.
     * **Capacity** : Use the default capacity (10 Gb/s).
  6. Click **Next**.

  7. Specify the details for the redundant Cloud Interconnect connection:

     * **Name** : Enter `int-lga2`.
     * **Description** : Enter `Example Cloud Interconnect connection in LGA ZONE2`.
     * **Location** : Choose `zColo New York - 60 Hudson St`, which is the PeeringDB name for the `lga-zone2-1422` location.
     * **Capacity** : Use the default capacity (10 Gb/s).
  8. Click **Next**.

  9. Specify your contact information:

     * **Company name** : Enter `The Customer`. This name is used in the LOA-CFA as the party authorized to request a Cloud Interconnect connection.
     * **Technical contact** : Enter `customer@customer.com`. You don't need to enter your own address; you are included in all notifications.
  10. Click **Next**.

  11. Review your order. Check that your Cloud Interconnect connections details and contact information are correct. If everything is correct, click **Place order**. If not, go back and edit the connection details.

  12. On the order confirmation page, review the next steps, and then click **Done**.




###  gcloud 

  * Order two Cloud Interconnect connections with the names `int-lga1` and `int-lga2`:
        
        gcloud compute interconnects create int-lga1 \
          --customer-name "The Customer" \
          --description "Example Cloud Interconnect connection in LGA ZONE1" \
          --interconnect-type DEDICATED \
          --link-type ETHERNET_10G_LR \
          --location lga-zone1-16 \
          --requested-link-count 1 \
          --noc-contact-email customer@customer.com
        
        gcloud compute interconnects create int-lga2 \
          --customer-name "The Customer" \
          --description "Example Cloud Interconnect connection in LGA ZONE2" \
          --interconnect-type DEDICATED \
          --link-type ETHERNET_10G_LR \
          --location lga-zone2-1422 \
          --requested-link-count 1 \
          --noc-contact-email customer@customer.com




After you order Cloud Interconnect connections, Google emails you a confirmation and allocates ports for you. When the allocation is complete, Google generates [LOA-CFAs](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology#loa) for your connections and emails them to you. All the automated emails are sent to the NOC contact and the person who ordered the connections.

You are able to use the Cloud Interconnect connections only after your connections have been provisioned and tested. For more information about the provisioning process, see the [Provisioning overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/provisioning-overview).

### Create a Cloud Router

To create a Cloud Router, follow the instructions in this section.

Make sure that your Cloud Router advertises the same prefixes on all links, possibly with different priorities.

###  Console 

  1. In the Google Cloud console, go to the **Create a Cloud Router** page.

[Go to Create a Cloud Router](https://console.cloud.google.com/networking/routers/add)

  2. Specify the Cloud Router details:

     * **Name** : Enter `router1` for the name of the Cloud Router.
     * **Network** : Select `vpc1`, which is the name of the network where the on-premises network extends to.
     * **Region** : Select `us-central1`, which is the region where the Cloud Router advertises all subnets, as shown in the example topology.
     * **Google ASN** : Enter `64513`, which is the ASN for the example Cloud Router.
  3. Under **Routes** , select **Advertise all subnets visible to the Cloud Router (default)** , and then click **Create**.




###  gcloud 

  * Create a Cloud Router in the `vpc1` network in the `us-central1` region; use ASN `64513`:
        
        gcloud compute routers create router1 \
          --asn 64513 \
          --network vpc1 \
          --region us-central1




You must verify that both your Cloud Router and the on-premises routers are configured correctly to advertise the same prefixes for the respective direction on each link. After configuring your Cloud Router, check the router status by following instructions in [Get Cloud Router status](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/managing-routers#get-router-status).

### Create VLAN attachments

After your Cloud Interconnect connections are ready to use (in the `ACTIVE` state), create VLAN attachments to connect the connections with Cloud Router. Create duplicate attachments, one for each connection. In the example, `int-lga1` and `int-lga2` are connected to `router1`.

###  Console 

  1. In the Google Cloud console, go to the **VLAN attachments** tab.

[Go to VLAN attachments](https://console.cloud.google.com/hybrid/interconnects/list?tab=attachments)

  2. Click **Add VLAN attachment**.

  3. Select **Dedicated Interconnect** , and then click **Continue**.

  4. Select **In this project**.

  5. Select the `int-lga1` Cloud Interconnect connection, and then click **Continue**.

  6. Select **Add VLAN attachment** :

     * **Name** : Enter `attachment-lga1-central1`.
     * **Router** : Select the `router1` Cloud Router.
  7. Click **Create**. The attachment takes a few moments to create.

  8. For the attachment, to add a BGP session to `router1`, click **Configure**. The VLAN attachment has already populated the Google and Peer BGP IP addresses.

  9. Record the IP addresses, ASNs, and VLAN tag for each attachment. This information is required to configure the on-premises router.

  10. To add the BGP session, click **Save configuration**. The BGP sessions are inactive until you configure BGP on your on-premises router.

  11. Create another attachment named `attachment-lga2-central1` for the `int-lga2` connection. Use `router1` for the attachment's Cloud Router.




###  gcloud 

  1. Create two attachments, one for the `int-lga1` Cloud Interconnect connection and the `router1` Cloud Router and another for the `int-lga2` connection and `router1`:
         
         gcloud compute interconnects attachments dedicated create attachment-lga1-central1 \
            --interconnect int-lga1 \
            --router router1
         
         gcloud compute interconnects attachments dedicated create attachment-lga2-central1 \
            --interconnect int-lga2 \
            --router router1

  2. Describe the `attachment-lga1-central1` attachment to retrieve the resources that it allocated, such as the VLAN ID and BGP peering addresses; use these values to configure the Cloud Router and on-premises router:
         
         gcloud compute interconnects attachments describe attachment-lga1-central1 \
            --region us-central1

The previous command outputs the following information:
         
         cloudRouterIpAddress: 169.254.58.49/29
         creationTimestamp: '2017-08-15T08:34:11.137-07:00'
         customerRouterIpAddress: 169.254.58.50/29
         id: '5630382895290821276'
         interconnect:
         https://www.googleapis.com/compute/v1/projects/customer-project/global/interconnects/int-lga1
         kind: compute#interconnectAttachment
         name: attachment-lga1-central1
         operationalStatus: ACTIVE
         privateInterconnectInfo:
           tag8021q: 1000
         region: https://www.googleapis.com/compute/v1/projects/customer-project/regions/us-central1
         router: https://www.googleapis.com/compute/v1/projects/customer-project/regions/us-central1/routers/router1
         selfLink: https://www.googleapis.com/compute/v1/projects/customer-project/regions/us-central1/interconnectAttachments/attachment-lga1-central1
           

  3. Record the following values:

     * **tag8021q** : Specifies the VLAN ID, which is `1000`. The VLAN ID identifies traffic that goes across this attachment. Use this value to configure a tagged VLAN subinterface on the on-premises router.
     * **cloudRouterIpAddress** : The Cloud Router IP address, which is `169.254.58.49/29`. Assign this address to a Cloud Router interface, and specify this address as the BGP neighbor on the on-premises router.
     * **customerRouterIpAddress** : The customer router IP address, which is `169.254.58.50/29`. On the Cloud Router, specify this address as the BGP peer address on the interface that has the Cloud Router IP address assigned to it. Assign this address to the VLAN subinterface on the on-premises router.
  4. On the `router1` Cloud Router, add an interface for the `attachment-lga1-central1` attachment:
         
         gcloud compute routers add-interface router1 \
           --interface-name router1-1 \
           --interconnect-attachment attachment-lga1-central1 \
           --ip-address 169.254.58.49 \
           --mask-length 29 \
           --region us-central1

  5. Add a BGP peer to the interface; for this example, the on-premises ASN is `12345`:
         
         gcloud compute routers add-bgp-peer router1 \
           --interface router1-1 \
           --peer-name central1 \
           --peer-ip-address 169.254.58.50 \
           --peer-asn 12345 \
           --region us-central1

  6. Describe the `attachment-lga2-central1` attachment, and then configure another BGP session on the `router1` Cloud Router.




### Configure on-premises routers

To configure the on-premises routers, use the information from the VLAN attachments. The following example is an excerpt from a Juniper router configuration. Use the sample as a starting point for configuring your own routers. For more information, see [Configuring on-premises routers](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/configuring-onprem-routers).
    
    
    interface ae20 {
      flexible-vlan-tagging;
      native-vlan-id 1;
      aggregated-ether-options {
        lacp {
          active;
         }
       }
      unit 1000 {
        vlan-id 1000;
        family inet {
          address 169.254.58.50/29;
        }
      }
    }
    
    protocols bgp {
      group google {
        type external;
        multihop {
          ttl 4;
        }
        hold-time 60;
        peer-as 64513;
        local-as 12345;
        local-address 169.254.58.50;
        neighbor 169.254.58.49 {
          ...
        }
      }
    }
    

## What's next

  * To learn more about each of these steps, see the [Dedicated Interconnect provisioning overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/provisioning-overview).

  * To help you solve common issues that you might encounter when using Cloud Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
