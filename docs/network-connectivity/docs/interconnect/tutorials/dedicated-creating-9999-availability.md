---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/dedicated-creating-9999-availability/
title: Establish 99.99% availability for Dedicated Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:58.921151+00:00
---

# Establish 99.99% availability for Dedicated Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/dedicated-creating-9999-availability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Establish 99.99% availability for Dedicated Interconnect Stay organized with collections  Save and categorize content based on your preferences. 

The following configuration uses Dedicated Interconnect to achieve 99.99% [availability](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview#redundancy). Google recommends this configuration for production-level applications, such as mission-critical operations that have a low tolerance for downtime.

For Cloud Interconnect terminology used on this page, see [Key terms](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology).

For information about creating redundant Dedicated Interconnect connections that have sufficient capacity in a failover scenario, see [Best practices](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/best-practices#capacity).

## Requirements

You can meet the a 99.99% availability using either a single region or two or more regions.

### Multi-region requirements

The following are the requirements to achieve 99.99% availability by using two or more regions.

  * You must configure at least four Dedicated Interconnect connections, with the following placement:

    * **Use two[metropolitan areas (metros)](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology#metro)**: at least two interconnect connections must be in one metro, and at least two interconnect connections must be in a different metro.

    * **Use both[edge availability domains](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology#edge-availability-domain) of each metro**: within each metro, at least one interconnect connection must be in zone 1, and at least one interconnect connection must be in zone 2. The edge availability domains you choose can be in the same facility of the metro (for example, `iad-zone1-5467` and `iad-zone2-5467`) or different facilities of the metro (for example, `iad-zone1-5467` and `iad-zone2-1`).

Using both edge availability domains of each metro is important because Google Cloud coordinates Cloud Interconnect maintenance between the edge availability domains within each metro. Google Cloud doesn't coordinate Cloud Interconnect maintenance events among different metros. Thus, it's possible for interconnect maintenance events to happen simultaneously in two or more metros, while within each metro only a single edge availability domain is affected at a time.

  * The following requirements apply to each VPC network in which you create VLAN attachments that depend on the Cloud Interconnect connections.

    * **VLAN attachments** : you must configure at least four VLAN attachments, collectively distributed between two [regions](https://docs.cloud.google.com/compute/docs/regions-zones), meeting both of the following criteria:

      * At least two VLAN attachments must be in one region of the VPC network, and at least two VLAN attachments must be in a different region of the VPC network.
      * Within each region of network, at least two VLAN attachments must each depend on a unique interconnect connection. Collectively, the VLAN attachments in each region must depend on interconnect connections that are in both edge availability domains of the metro.
    * **Cloud Routers** : you must use at least two Cloud Routers, one in each region where VLAN attachments are configured. Using more than two Cloud Routers doesn't add reliability or change the SLA because Cloud Routers automatically distribute the BGP sessions of VLAN attachments between two [BGP software tasks](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/how-cloud-router-works#bgp-tasks), based on the edge availability domain of the interconnect connection that each VLAN attachment depends on.

    * **Dynamic routing mode** : the VPC network must use global [dynamic routing mode](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes#dynamic-routing-mode). Global dynamic routing ensures that Cloud Router learned routes are programmed as dynamic routes in all regions of the VPC network.




### Single-region requirements

The following are the requirements to achieve 99.99% availability by using one region.

  * You must configure at least four Dedicated Interconnect connections, distributed strategically between a pair of _facility and edge availability domain combinations_ within a single metro:

    * **Identify facility and edge availability domain combinations** : use the [locations table](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/choosing-colocation-facilities#locations-table) to identify a pair of facility and edge availability domain combinations in a single metro.

    * **Use both facility and edge availability domain combinations** : within the metro, at least two interconnect connections must be in one facility and edge availability domain combination, and at last two interconnect connections must be in the other combination of the pair: for example, two interconnect connections in `iad-zone1-1`, and two interconnect connections in `iad-zone2-5467`.

    * **Order using a Dedicated Interconnect connection group** : to order interconnect connections that use the pair of facility and edge availability domain combinations, you must use an interconnect connection group whose intended topology capability is `PRODUCTION_CRITICAL`. For more information about connection groups, see [Modify connection groups](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/modifying-connection-groups).

  * The following requirements apply to each VPC network in which you create VLAN attachments that depend on the Cloud Interconnect connections.

    * **VLAN attachments** : you must configure at least four VLAN attachments, all in one region. The region must be the low latency region of the metro in which the interconnect connections are provisioned. Each VLAN attachment must depend on a unique interconnect connection. Collectively, the VLAN attachments must use all configured interconnect connections.

    * **Cloud Routers** : you must use at least one Cloud Router in the region where VLAN attachments are configured. Using more than one Cloud Router doesn't add reliability or change the SLA because Cloud Routers automatically distribute the BGP sessions of VLAN attachments between two [BGP software tasks](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/how-cloud-router-works#bgp-tasks), based on the edge availability domain of the interconnect connection that each VLAN attachment depends on.

    * **Dynamic routing mode** : the VPC network can use either regional or global [dynamic routing mode](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes#dynamic-routing-mode).




### On-premise router and route advertisement requirements

The on-premise router and route advertisement requirements are the same regardless of how many regions you use.

Consult the documentation for your on-premises routers to determine how to configure them for a 99.99% SLA. You might need to connect a unique physical router to each interconnect connection.

On-premises routers must advertise the same prefixes over the BGP sessions of each VLAN attachment. You can use different BGP metrics (like MED) to achieve your connectivity goals. For more information about how Cloud Router BGP tasks, the dynamic route control plane, and the VPC network control plane create dynamic routes from received prefixes, see [Learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes#custom-learned-routes) in the Cloud Router documentation.

## Example topologies

The following sections demonstrate example Cloud Interconnect topologies.

### Multi-region topology

The following example topology meets the 99.99% availability with four Cloud Interconnect connections in the following pairs of facility and edge availability domain combinations, one pair in the `LGA` metro and the other pair in the `IAD` metro:

  * `LGA` pair: `lga-zone1-16` and `lga-zone2-1422`
  * `IAD` pair: `iad-zone1-1` and `iad-zone2-2`



Four VLAN attachments are configured in a VPC network that uses the global dynamic routing mode: two in the `us-central1` region, and two in the `us-east1` region. Within each region:

  * Each VLAN attachment depends on a unique interconnect connection.
  * Collectively, both VLAN attachments depend on interconnect connections that are in both edge availability domains of the same metro.

[ ![Redundant connections for 99.99% availability \(click to enlarge\).](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/sla-9999-mr.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/sla-9999-mr.svg) Redundant connections for 99.99% availability (click to enlarge)

### Single-region topology

The following example topology meets the 99.99% availability with four Cloud Interconnect connections in a single metro, `IAD`. There are two interconnect connections are in each of the following facility and edge availability domain combinations:

  * `iad-zone1-1`
  * `iad-zone2-5467`



This pair of facility and edge availability domain combinations is a valid pair for single region 99.99% availability.

Four VLAN attachments are configured in a VPC network in the `us-east4` region, because the `us-east4` region is the low latency region corresponding to the `IAD` metro. The VPC network can use either regional or global dynamic routing mode.

In the `us-east4` region, each VLAN attachment depends on a unique interconnect connection, and collectively all four VLAN attachments depend on interconnect connections that are in both facility and edge availability domain combinations.

[ ![Redundant connections for 99.99% single-region availability \(click to enlarge\).](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/sla-9999-sr.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/sla-9999-sr.svg) Redundant connections for 99.99% single-region availability (click to enlarge)

## Configure preferred paths

Dedicated Interconnect VLAN attachments depend on Cloud Routers to learn prefixes from remote peer routers (for example, routers in an on-premises network). The dynamic routing mode and best path selection mode of the VPC network that contains the Cloud Routers control which next hops are considered, and how BGP attributes are processed to produce [dynamic routes](https://docs.cloud.google.com/vpc/docs/routes#dynamic_routes). The dynamic routes in a VPC network define paths from the VPC network to a connected network (like an on-premises network). For more information, see [Learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes) in the Cloud Router documentation.

To create paths from the connected network to the VPC network, you configure Cloud Router BGP advertisements. You can configure advertisements on each BGP session individually, or define advertisement defaults for the Cloud Router. These advertisements can include subnet ranges, custom prefixes, or a combination of subnet ranges and custom prefixes. For more information, see [Advertised routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes) in the Cloud Router documentation.

## Create a multi-region 99.99% topology

The following sections walk through the steps for creating this topology. To create a topology that's tailored for you, replace the sample input values with your own. For example, replace the `vpc1` network name with your VPC network name.

### Change VPC network's dynamic routing mode

For the `vpc1` network, change its dynamic routing mode to global.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Select the `vpc1` network, and then click edit**Edit**.

  3. Under **Dynamic routing mode** , select **Global**.

  4. Click **Save**.




###  gcloud 
    
    
    gcloud compute networks update vpc1 \
       --bgp-routing-mode global

### Order Dedicated Interconnect connections

Order duplicate connections by using the Google Cloud console or the Google Cloud CLI.

###  Console 

  1. In the Google Cloud console, go to the **Interconnect Hybrid Connectivity** page.

[Go to Interconnect Hybrid Connectivity](https://console.cloud.google.com/hybrid/interconnects/list?tab=interconnects)

  2. Click **Get started**.

  3. Select **Dedicated Interconnect** , and then click **Continue**.

  4. Select **Order new Dedicated Interconnect** , and then click **Continue**.

  5. Specify the details for the connection:

     * **Name** : Enter `int-lga1`.
     * **Description** : Enter `Example connection in LGA ZONE1`.
     * **Location** : Choose `Digital Realty | Telx New York (111 8th Ave)`, which is the PeeringDB name for the `lga-zone1-16` location.
     * **Capacity** : Use the default capacity (10 Gb/s).
  6. Click **Next**.

  7. Specify the details for the redundant connection:

     * **Name** : Enter `int-lga2`.
     * **Description** : Enter `Example connection in LGA ZONE2`.
     * **Location** : Choose `zColo New York - 60 Hudson St`, which is the PeeringDB name for the `lga-zone2-1422` location.
     * **Capacity** : Use the default capacity (10 Gb/s).
  8. Click **Next**.

  9. Specify your contact information:

     * **Company name** : Enter `The Customer`. This name is used in the LOA-CFA as the party authorized to request a Cloud Interconnect connection.
     * **Technical contact** : Enter `customer@customer.com`. You don't need to enter your own address; you are included in all notifications.
  10. Click **Next**.

  11. Review your order. Check that the details and contact information of your connections are correct. If everything is correct, click **Place order**. If not, go back and edit the connection details.

  12. On the order confirmation page, review the next steps, and then click **Done**.

  13. Order two more connections (`int-iad1` and `int-iad2`) in the location `Equinix Ashburn (DC1-DC11)`, which is the PeeringDB name for the `iad-zone1-1` and `iad-zone2-1` locations. Because the Ashburn facility has two zones, the Google Cloud console automatically selects the same facility but a different zone for the redundant connection.




###  gcloud 

  * Order four Dedicated Interconnect connections with the names `int-lga1`, `int-lga2`, `int-iad1`, and `int-iad2`:
        
        gcloud compute interconnects create int-lga1 \
          --customer-name "The Customer" \
          --description "Example connection in LGA ZONE1" \
          --interconnect-type DEDICATED \
          --link-type ETHERNET_10G_LR \
          --location lga-zone1-16 \
          --requested-link-count 1 \
          --noc-contact-email customer@customer.com
        
        gcloud compute interconnects create int-lga2 \
          --customer-name "The Customer" \
          --description "Example connection in LGA ZONE2" \
          --interconnect-type DEDICATED \
          --link-type ETHERNET_10G_LR \
          --location lga-zone2-1422 \
          --requested-link-count 1 \
          --noc-contact-email customer@customer.com
        
        gcloud compute interconnects create int-iad1 \
          --customer-name "The Customer" \
          --description "Example connection in IAD ZONE1" \
          --interconnect-type DEDICATED \
          --link-type ETHERNET_10G_LR \
          --location iad-zone1-1 \
          --requested-link-count 1 \
          --noc-contact-email customer@customer.com
        
        gcloud compute interconnects create int-iad2 \
          --customer-name "The Customer" \
          --description "Example connection in IAD ZONE2" \
          --interconnect-type DEDICATED \
          --link-type ETHERNET_10G_LR \
          --location iad-zone2-1 \
          --requested-link-count 1 \
          --noc-contact-email customer@customer.com




After you order Dedicated Interconnect connections, Google emails you a confirmation and allocates ports for you. When the allocation is complete, Google generates [LOA-CFAs](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology#loa) for your connections and emails them to you. All the automated emails are sent to the NOC contact and the person who ordered the connections.

You are able to use the connections only after your connections have been provisioned and tested. For more information about the provisioning process, see the [Provisioning overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/provisioning-overview).

### Create Cloud Routers

Create two Cloud Routers, one for each region.

###  Console 

  1. In the Google Cloud console, go to the **Create a Cloud Router** page.

[Go to Create a Cloud Router](https://console.cloud.google.com/networking/routers/add)

  2. Specify the Cloud Router details:

     * **Name** : Enter `rtr-cent1` for the name of the first Cloud Router.
     * **Network** : Select `vpc1`, which is the name of the network where the on-premises network extends to.
     * **Region** : Select `us-central1`, which is the region where the Cloud Router is configured, as shown in the example topology.
     * **Google ASN** : Enter `64513`, which is the ASN for the example Cloud Router.
  3. Under **Routes** , select **Advertise all subnets visible to the Cloud Router (default)** , and then click **Create**.

  4. Create one more Cloud Router with the same attributes in the `us-east1` region with the name `rtr-east1`.




###  gcloud 

  1. Create a Cloud Router in the `vpc1` network in the `us-central1` region; use ASN `64513`:
         
         gcloud compute routers create rtr-cent1 \
            --asn 64513 \
            --network vpc1 \
            --region us-central1

  2. Create a Cloud Router in the `vpc1` network in the `us-east1` region; use ASN `64513`:
         
         gcloud compute routers create rtr-east1 \
            --asn 64513 \
            --network vpc1 \
            --region us-east1




### Create VLAN attachments

After your connections are ready to use (in the `ACTIVE` state), create VLAN attachments to connect the connections with Cloud Routers. Create four attachments, one for each Cloud Interconnect connection, and use the routers as described in the following list:

  * `rtr-cent1` is connected to `int-lga1` and `int-lga2`
  * `rtr-east1` is connected to `int-iad1` and `int-iad2`




###  Console 

  1. In the Google Cloud console, go to the **VLAN attachments** tab.

[Go to VLAN attachments](https://console.cloud.google.com/hybrid/interconnects/list?tab=attachments)

  2. Click **Add VLAN attachment**.

  3. Select **Dedicated Interconnect** , and then click **Continue**.

  4. Select **In this project**.

  5. Select the `int-lga1` connection, and then click **Continue**.

  6. Select **Add VLAN attachment** :

     * **Name** : Enter `attachment-lga1-central1`.
     * **Router** : Select the `rtr-cent1` Cloud Router.
  7. Click **Create**. The attachment takes a few moments to create.

  8. For the attachment, to add a BGP session to `rtr-cent1`, click **Configure**. The VLAN attachment has already populated the Google and Peer BGP IP addresses.

  9. Record the IP addresses, ASNs, and VLAN tag for each attachment. This information is required to configure the on-premises router.

  10. To add the BGP session, click **Save configuration**. The BGP sessions are inactive until you configure BGP on your on-premises router.

  11. Create three more attachments for the other connections:

     * `int-lga2` (`rtr-cent1`)
     * `int-iad1` (`rtr-east1`)
     * `int-iad2` (`rtr-east1`)

Record the information for each attachment.




###  gcloud 

  1. Create four attachments:
         
         gcloud compute interconnects attachments dedicated create attachment-lga1-central1 \
            --interconnect int-lga1 \
            --router rtr-cent1 \
            --region us-central1
         
         gcloud compute interconnects attachments dedicated create attachment-lga2-central1 \
            --interconnect int-lga2 \
            --router rtr-cent1 \
            --region us-central1
         
         gcloud compute interconnects attachments dedicated create attachment-iad1-east1 \
            --interconnect int-iad1 \
            --router rtr-east1 \
            --region us-east1
         
         gcloud compute interconnects attachments dedicated create attachment-iad2-east1 \
            --interconnect int-iad2 \
            --router rtr-east1 \
            --region us-east1

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
  4. On the `rtr-cent1` Cloud Router, add an interface for the `attachment-lga1-central1` attachment:
         
         gcloud compute routers add-interface rtr-cent1 \
            --interface-name rtr-cent1-1 \
            --interconnect-attachment attachment-lga1-central1 \
            --ip-address 169.254.58.49 \
            --mask-length 29 \
            --region us-central1

  5. Add a BGP peer to the interface; for this example, the on-premises ASN is `12345`:
         
         gcloud compute routers add-bgp-peer rtr-cent1 \
            --interface rtr-cent1-1 \
            --peer-name central1 \
            --peer-ip-address 169.254.58.50 \
            --peer-asn 12345 \
            --advertised-route-priority 100 \
            --region us-central1

  6. Describe the other attachments, and then similarly configure a new BGP session on the appropriate Cloud Router.




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
    

## Create a single-region 99.99% topology

The following sections walk through the steps for creating this topology. To create a topology that's tailored for you, replace the sample input values with your own. For example, replace the `vpc1` network name with your VPC network name.

Note that only certain [supported metros](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/choosing-colocation-facilities#locations-table) qualify for the single-region 99.99% SLA.

### Order Dedicated Interconnect connections

Order duplicate connections by using the Google Cloud console or the Google Cloud CLI. This example uses Interconnect connection groups, which let you group your connections to receive feedback on how your resources meet your intended level of reliability. For more information, see [Cloud Interconnect groups](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview#groups).

###  Console 

First, create a Cloud Interconnect group to contain your connections:

  1. Click **Create group**.
  2. Specify the details for the group: 
     * **Name** : Enter `example-interconnect-group`.
     * **Description** : Enter `Example group in Ashburn`.
     * **Production SLA** : Select **Production critical (maximum resiliency)**.
  3. Click **Create**.



Next, add Dedicated Interconnect connections to the group:

  1. Select your group.
  2. Click **Set up physical connection**.
  3. Select **Dedicated Interconnect connection** , and then click **Continue**.
  4. Select **Order new Dedicated Interconnect** , and then click **Continue**.
  5. In the **Production SLA** field, do the following: 
     1. Select **Production critical (maximum resiliency)**.
     2. In the **Select topology type** field, select **Single region**.
     3. In the **Select Interconnect group** field, click **Select an existing group** , and then choose `example-interconnect-group`.
  6. In the **Capacity** field, use the default capacity (10 Gb/s).
  7. In the **Metropolitan area** field, select `Ashburn`.
  8. In the **New interconnect** field, specify the details for the connection: 
     * **Name** : Enter `interconnect-1-a`.
     * **Description** : Enter `Example connection in IAD`.
     * **Location** : Choose `Equinix Ashburn (DC1-DC11)`, which is the PeeringDB name for the `iad-1` location.
  9. Click **Add interconnect**.
  10. Specify the details for the redundant connection: 
     * **Name** : Enter `interconnect-1-b`.
     * **Description** : Enter `Example redundant connection in IAD`.
     * **Location** : Choose `Equinix Ashburn (DC1-DC11)`, which is the PeeringDB name for the `iad-1` location.
  11. Repeat the previous two steps to add two more connections (`interconnect-2-a` and `interconnect-2-b`) in the location corresponding to `iad-5467`. Because the facility has two zones, the Google Cloud console automatically selects the same facility but a different zone for the redundant connection.
  12. Click **Next**.
  13. Specify your contact information: 
     * **Company name** : Enter `example.com`. This name is used in the LOA-CFA as the party authorized to request a Cloud Interconnect connection.
     * **Technical contact** : Enter `user@example.com`. You don't need to enter your own address; you are included in all notifications.
  14. Click **Next**.
  15. Review your order. Check that the details and contact information of your connections are correct. If everything is correct, click **Place order**. If not, go back and edit the connection details.
  16. On the order confirmation page, review the next steps, and then click **Done**.



###  gcloud 

  1. Create a Dedicated Interconnect group:
         
         gcloud compute interconnects groups create example-interconnect-group \
           --intended-topology-capability PRODUCTION_CRITICAL
         

  2. Add Dedicated Interconnect connections to the group:
         
         gcloud compute interconnects groups create-members example-interconnect-group \
            --interconnect='name=interconnect-1-a,facility=iad-1' \
            --interconnect='name=interconnect-1-b,facility=iad-1' \
            --interconnect='name=interconnect-2-a,facility=iad-5467' \
            --interconnect='name=interconnect-2-b,facility=iad-5467' \
            --customer-name=example.com \
            --noc-contact-email=user@example.com \
            --description="Single-Region 99.99% Topology" \
            --intent-mismatch-behavior=REJECT \
            --interconnect-type=DEDICATED \
            --link-type=LINK_TYPE_ETHERNET_100G_LR
         




After you order Dedicated Interconnect connections, Google emails you a confirmation and allocates ports for you. When the allocation is complete, Google generates [LOA-CFAs](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology#loa) for your connections and emails them to you. All the automated emails are sent to the NOC contact and the person who ordered the connections.

You are able to use the connections only after your connections have been provisioned and tested. For more information about the provisioning process, see the [Provisioning overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/provisioning-overview).

### Create a Cloud Router

Create a Cloud Router.

###  Console 

  1. In the Google Cloud console, go to the **Create a Cloud Router** page.

[Go to Create a Cloud Router](https://console.cloud.google.com/networking/routers/add)

  2. Specify the Cloud Router details:

     * **Name** : Enter `rtr-east4` for the name of the first Cloud Router.
     * **Network** : Select `vpc1`, which is the name of the network where the on-premises network extends to.
     * **Region** : Select `us-east4`, which is the region where the Cloud Router is configured.
     * **Google ASN** : Enter `64513`, which is the ASN for the example Cloud Router.
  3. Under **Routes** , select **Advertise all subnets visible to the Cloud Router (default)** , and then click **Create**.




###  gcloud 

  1. Create a Cloud Router in the `vpc1` network in the region `us-east4`; use ASN `64513`:
         
         gcloud compute routers create rtr-east4 \
            --asn 64513 \
            --network vpc1 \
            --region us-east4




### Create VLAN attachments

After your connections are ready to use (in the `ACTIVE` state), create VLAN attachments to connect the connections with Cloud Routers. Create four attachments, one for each Cloud Interconnect connection, and connect them to `rtr-east4`.

###  Console 

  1. In the Google Cloud console, go to the **VLAN attachments** tab.

[Go to VLAN attachments](https://console.cloud.google.com/hybrid/interconnects/list?tab=attachments)

  2. Click **Add VLAN attachment**.

  3. Select **Dedicated Interconnect** , and then click **Continue**.

  4. Select **In this project**.

  5. Select the `int-iad1` connection, and then click **Continue**.

  6. Select **Add VLAN attachment** :

     * **Name** : Enter `attachment-iad1`.
     * **Router** : Select the `rtr-east4` Cloud Router.
  7. Click **Create**. The attachment takes a few moments to create.

  8. For the attachment, to add a BGP session to `rtr-east4`, click **Configure**. The VLAN attachment has already populated the Google and Peer BGP IP addresses.

  9. Record the IP addresses, ASNs, and VLAN tag for each attachment. This information is required to configure the on-premises router.

  10. To add the BGP session, click **Save configuration**. The BGP sessions are inactive until you configure BGP on your on-premises router.

  11. Create three more attachments for the other connections:

     * `int-iad2` (`rtr-east4`)
     * `int-iad3` (`rtr-east4`)
     * `int-iad4` (`rtr-east4`)

Record the information for each attachment.




###  gcloud 

  1. Create four attachments:
         
         gcloud compute interconnects attachments dedicated create attachment-iad1 \
            --interconnect int-iad1 \
            --router rtr-east4 \
            --region us-east4
         
         gcloud compute interconnects attachments dedicated create attachment-iad2 \
            --interconnect int-iad2 \
            --router rtr-east4 \
            --region us-east4
         
         gcloud compute interconnects attachments dedicated create attachment-iad3 \
            --interconnect int-iad3 \
            --router rtr-east4 \
            --region us-east4
         
         gcloud compute interconnects attachments dedicated create attachment-iad4 \
            --interconnect int-iad4 \
            --router rtr-east4 \
            --region us-east4

  2. Describe the `attachment-iad1` attachment to retrieve the resources that it allocated, such as the VLAN ID and BGP peering addresses; use these values to configure the Cloud Router and on-premises router:
         
         gcloud compute interconnects attachments describe attachment-iad1 \
            --region us-east4

The previous command outputs the following information:
         
         cloudRouterIpAddress: 169.254.58.49/29
         creationTimestamp: '2017-08-15T08:34:11.137-07:00'
         customerRouterIpAddress: 169.254.58.50/29
         id: '5630382895290821276'
         interconnect:
         https://www.googleapis.com/compute/v1/projects/customer-project/global/interconnects/int-iad1
         kind: compute#interconnectAttachment
         name: attachment-iad1
         operationalStatus: ACTIVE
         privateInterconnectInfo:
           tag8021q: 1000
         region: https://www.googleapis.com/compute/v1/projects/customer-project/regions/us-east4
         router: https://www.googleapis.com/compute/v1/projects/customer-project/regions/us-east4/routers/router1
         selfLink: https://www.googleapis.com/compute/v1/projects/customer-project/regions/us-east4/interconnectAttachments/attachment-iad1
           

  3. Record the following values:

     * **tag8021q** : Specifies the VLAN ID, which is `1000`. The VLAN ID identifies traffic that goes across this attachment. Use this value to configure a tagged VLAN subinterface on the on-premises router.
     * **cloudRouterIpAddress** : The Cloud Router IP address, which is `169.254.58.49/29`. Assign this address to a Cloud Router interface, and specify this address as the BGP neighbor on the on-premises router.
     * **customerRouterIpAddress** : The customer router IP address, which is `169.254.58.50/29`. On the Cloud Router, specify this address as the BGP peer address on the interface that has the Cloud Router IP address assigned to it. Assign this address to the VLAN subinterface on the on-premises router.
  4. On the `rtr-east4` Cloud Router, add an interface for the `attachment-iad1` attachment:
         
         gcloud compute routers add-interface rtr-east4 \
            --interface-name rtr-east4-1 \
            --interconnect-attachment attachment-iad1 \
            --ip-address 169.254.58.49 \
            --mask-length 29 \
            --region us-east4

  5. Add a BGP peer to the interface; for this example, the on-premises ASN is `12345`:
         
         gcloud compute routers add-bgp-peer rtr-east4 \
            --interface rtr-east4-1 \
            --peer-name central1 \
            --peer-ip-address 169.254.58.50 \
            --peer-asn 12345 \
            --advertised-route-priority 100 \
            --region us-east4

  6. Describe the other attachments, and then similarly configure a new BGP session on the appropriate Cloud Router.




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

  * To learn more about each of these steps, see the [Dedicated Interconnect Provisioning overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/provisioning-overview).

  * To get information about non-critical applications, see [Establish 99.9% availability for Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/dedicated-creating-999-availability).

  * To help you solve common issues that you might encounter when using Cloud Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
