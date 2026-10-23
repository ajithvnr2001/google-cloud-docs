---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/partner-creating-9999-availability/
title: Establish 99.99% availability for Partner Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:55:49.605094+00:00
---

# Establish 99.99% availability for Partner Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/partner-creating-9999-availability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Establish 99.99% availability for Partner Interconnect Stay organized with collections  Save and categorize content based on your preferences. 

In this tutorial, you use Partner Interconnect to create and configure resources to achieve 99.99% [availability](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview#redundancy). Google recommends this configuration for production-level applications, such as mission-critical operations that have a low tolerance for downtime.

For Cloud Interconnect terminology used on this page, see [Key terms](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology).

For information about redundant Partner Interconnect connections that have sufficient capacity in a failover scenario, see [Best practices](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/best-practices#capacity).

**Note:** Before you begin, you must have an existing connection with a [supported service provider](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/service-providers).

## Requirements

The following resources and settings are required to achieve 99.99% availability:

  * _At least_ four VLAN attachments, two per [Google Cloud region](https://docs.cloud.google.com/compute/docs/regions-zones). Even if you only have virtual machine (VM) instances in a single region, you must use two regions. If a region-wide issue occurs, Google Cloud can reroute traffic through the other region to your VMs. Each pair of VLAN attachments must have its own Cloud Router (two different Cloud Routers).

When Cloud Router is connected to VLAN attachments in different [edge availability domains](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology#edge-availability-domain), Google Cloud uses two [software tasks](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes#software-task-processing) for redundancy. Even though only two Cloud Routers are required, topologies with four Cloud Routers, one for each VLAN attachment, also meet the SLA requirement.

  * The VLAN attachments in one region must connect to a Partner Interconnect connection in one metropolitan area (metro), and attachments in the other region must connect to a connection in another metro.

The Google Cloud console automatically assigns a Partner Interconnect connection and a different edge availability domain (metro availability zone) to each attachment when you configure a redundant pair of attachments.

**Important:** If you use the API, you must manually assign each attachment to a different connection and to a different edge availability domain. This is because maintenance windows aren't coordinated across different metros, but they are coordinated for different edge availability domains within the same metro.

For more information about choosing a Partner Interconnect connection location, see [Requesting connections](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/requesting-connections).

  * Make sure that your Cloud Router advertises the same prefixes on all links, possibly with different priorities.

  * The dynamic routing mode for the Virtual Private Cloud (VPC) network must be global. With global dynamic routing, Cloud Router can advertise all subnets and propagate learned routes to all subnets regardless of the subnet's region.

  * Depending on your hardware and availability requirements, you might have one or more routers in your on-premises network.




### Example topology

This example topology uses the following resource names, regions, and connection locations. As you walk through the tutorial, replace these values with your own.

Region | Router name | VLAN attachment name | Connection location | Edge availability domain  
---|---|---|---|---  
`us-central1` | `router-central1` | `attach-central-a` | Dallas | 1  
`us-central1` | `router-central1` | `attach-central-b` | Dallas | 2  
`us-east4` | `router-east4` | `attach-east-a` | Ashburn | 1  
`us-east4` | `router-east4` | `attach-east-b` | Ashburn | 2  
  
The following diagram shows four layer 2 connections in two different metros. Within each metro, each connection is in a different edge availability domain: `Dallas - domain 1`, `Dallas - domain 2`, `Ashburn - domain 1`, and `Ashburn - domain 2`.

The Cloud Routers (one for each region) are in the `vpc1` network in the `us-central1` and `us-east4` regions. For layer 2 connections, users configure Border Gateway Protocol (BGP) sessions on their on-premises routers to each of their Cloud Routers.

[ ![Redundant connections for 99.99% availability using layer 2 \(click to enlarge\).](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/9999-layer2.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/9999-layer2.svg) Redundant connections for 99.99% availability using layer 2 (click to enlarge)

Similar to the layer 2 topology, the following layer 3 topology shows four Partner Interconnect connections in two different metros and in different edge availability domains. The Cloud Routers (one for each region) are in the `vpc1` network in the `us-central1` and `us-east4` regions. For layer 3 connections, the service provider configures the BGP sessions.

[ ![Redundant connections for 99.99% availability using layer 3 \(click to enlarge\).](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/9999-layer3.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/interconnect/images/9999-layer3.svg) Redundant connections for 99.99% availability using layer 3 (click to enlarge)

## Configure the preferred path

For 99.99% availability, you must set the dynamic routing mode of your VPC networks to global. With global dynamic routing, Cloud Router advertises routes to all subnets in the VPC network. Cloud Router advertises routes to _remote subnets_ (subnets outside of the Cloud Router's region) with a lower priority compared to _local subnets_ (subnets that are in the Cloud Router's region). For more information, see [Dynamic routing mode](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes#dynamic-routing-mode-effects-on-learned-routes) in the Cloud Router documentation.

In the example topology, ingress traffic to the VPC network prefers to go through the `us-central1` region because those routes have a higher priority compared to routes from the `us-east4` region. Traffic traverses through `us-east4` only if the connections in `us-central1` fail.

You can change route priorities when you configure a Cloud Router's BGP session. The BGP session has an option for an advertised route priority (a MED value). A lower value means a higher priority. You can, for example, configure the BGP sessions in `us-east4` with a higher priority, making that region the preferred path. For more information, see [Advertised prefixes and priorities](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#advertised-priority) in the Cloud Router documentation.

## Create a 99.99% topology

The following sections walk through the steps for creating this topology. To create a topology that's tailored for you, replace the sample input values with your own. For example, replace the `vpc1` network name with your VPC network name.

### Create the VPC network

For the `vpc1` network, create a network with custom subnets and set its dynamic routing mode to global. For more information, see [Creating a custom mode network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#create-custom-network) in the VPC documentation.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network**.

  3. For **Name** , enter `vpc1`.

  4. For **Subnet creation mode** , select **Custom**.

  5. Specify the details of your subnet:

     1. **Name** : Enter `subnet-uscentral1`.
     2. **Region** : Select `us-central1`.
     3. **IP address range** : Specify an IP range, such as `192.168.1.0/24`. Use a range that doesn't overlap with your on-premises network.
  6. Click **Add subnet**.

  7. Specify the details of your second subnet:

     1. **Name** : Enter `subnet-useast4`.
     2. **Region** : Select `us-east4`.
     3. **IP address range** : Specify an IP range, such as `192.168.2.0/24`. Use a range that doesn't overlap with your on-premises network.
  8. In the **Dynamic routing mode** section, select **Global**.

  9. Click **Create**.




###  gcloud 

  1. Create a custom subnet:
         
         gcloud compute networks create vpc1 \
            --subnet-mode custom \
            --bgp-routing-mode global
         

  2. Specify the subnet prefixes for the `us-central1` and `us-east4` regions:
         
         gcloud compute networks subnets create subnet-uscentral1 \
            --network vpc1 \
            --region us-central1 \
            --range 192.168.1.0/24
         
         
         gcloud compute networks subnets create subnet-useast4 \
            --network vpc1 \
            --region us-east4 \
            --range 192.168.2.0/24
         




### Create Cloud Routers

Create two Cloud Routers, one in each region. For Partner Interconnect, all Cloud Routers must have a local ASN of `16550`.

###  Console 

  1. In the Google Cloud console, go to the **Create a Cloud Router** page.

[Go to Create a Cloud Router](https://console.cloud.google.com/networking/routers/add)

  2. Specify the Cloud Router details:

     * **Name** : Enter `router-central1` for the name of the first Cloud Router.
     * **Network** : Select `vpc1`, which is the name of the network where the on-premises network extends to.
     * **Region** : Select `us-central1`, which is the region where the Cloud Router is configured, as shown in the example topology.
     * **Google ASN** : Enter `16550`, which is required for Partner Interconnect.
  3. Under **Routes** , select **Advertise all subnets visible to the Cloud Router (default)** , and then click **Create**.

  4. Create another Cloud Router with the same attributes in the `us-east4` region with the name `router-east4`.




###  gcloud 

  1. Create a Cloud Router in the `vpc1` network in the `us-central1` region; use ASN `16550`:
         
         gcloud compute routers create router-central1 \
           --asn 16550 \
           --network vpc1 \
           --region us-central1
         

  2. Create a Cloud Router in the `vpc1` network in the `us-east4` region; use ASN `16550`:
         
         gcloud compute routers create router-east4 \
           --asn 16550 \
           --network vpc1 \
           --region us-east4
         




### Create VLAN attachments

Create four VLAN attachments and pair them with Cloud Routers, as shown in the following list:

  * `router-central1` is associated with `attach-central-a` and `attach-central-b`
  * `router-east4` is associated with `attach-east-a` and `attach-east-b`

**Note:** For layer 3 connections, you can [pre-activate](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview#pre-activate) your VLAN attachments so that you don't have to come back to Google Cloud and activate them after your service provider has configured them. For this tutorial, the VLAN attachments aren't pre-activated because pre-activation skips a verification step when working with Partner Interconnect VLAN attachments.

###  Console 

  1. In the Google Cloud console, go to the **Interconnect Hybrid Connectivity** page.

[Go to Interconnect Hybrid Connectivity](https://console.cloud.google.com/hybrid/interconnects/list?tab=attachments)

  2. Click **Get started**.

  3. Select **Partner Interconnect** , and then click **Continue**.

  4. Select **I already have a service provider**.

  5. Select **Create a redundant pair of VLAN attachments (recommended)**.

  6. For the **Network** and **Region** fields, select the `vpc1` network and the `us-central1` region, which specifies the VPC network and region to connect to.

  7. Specify the details of the first VLAN attachment (VLAN A):

     * **Cloud Router** : Select `router-central1`.
     * **VLAN attachment name** : Enter `attach-central-a`. This name is displayed in the Google Cloud console and is used by the Google Cloud CLI to reference the attachment.
  8. Specify the details of the second VLAN attachment (VLAN B):

     * **Cloud Router** : Select `router-central1`.
     * **VLAN attachment name** : Enter `attach-central-b`.
  9. Click **Create** to create the attachments, which takes a few moments to complete.

  10. Click **OK** to view a list of your VLAN attachments.

  11. Repeat these steps to create another redundant pair of attachments for the `us-east4` region.




###  gcloud 

  * Create four attachments:
        
        gcloud compute interconnects attachments partner create attach-central-a \
           --router router-central1 \
           --region us-central1 \
           --edge-availability-domain availability-domain-1
        
        
        gcloud compute interconnects attachments partner create attach-central-b \
           --router router-central1 \
           --region us-central1 \
           --edge-availability-domain availability-domain-2
        
        
        gcloud compute interconnects attachments partner create attach-east-a \
           --router router-east4 \
           --region us-east4 \
           --edge-availability-domain availability-domain-1
        
        
        gcloud compute interconnects attachments partner create attach-east-b \
           --router router-east4 \
           --region us-east4 \
           --edge-availability-domain availability-domain-2
        




### Retrieve pairing keys

After you create your VLAN attachments, Google Cloud generates pairing keys for each one. Pairing keys enable service providers to identify your VLAN attachment without you having to share information about your project or resource names.

###  Console 

  1. In the Google Cloud console, go to the **VLAN attachments** tab.

[Go to VLAN attachments](https://console.cloud.google.com/hybrid/interconnects/list?tab=attachments)

  2. Find the `attach-central-a` VLAN attachment, and then click **View instructions**.

The Google Cloud console shows the pairing key for the attachment. Copy and record the key; you'll share these keys with your service provider when you request a connection with them.

  3. Click **OK** to return to the list of VLAN attachments.

  4. Retrieve the pairing keys for the `attach-central-b`, `attach-east-a`, and `attach-east-b` VLAN attachments.




###  gcloud 

  1. Retrieve the VLAN attachment pairing keys by describing each one; use these keys to request connections with your service provider:
         
         gcloud compute interconnects attachments describe attach-central-a \
            --region us-central1
         

The previous command outputs the following information:
         
         adminEnabled: false
         edgeAvailabilityDomain: AVAILABILITY_DOMAIN_1
         creationTimestamp: '2017-12-01T08:29:09.886-08:00'
         id: '7976913826166357434'
         kind: compute#interconnectAttachment
         labelFingerprint: 42WmSpB8rSM=
         name: attach-central-a
         pairingKey: 7e51371e-72a3-40b5-b844-2e3efefaee59/us-central1/1
         region: https://www.googleapis.com/compute/v1/projects/customer-project/regions/us-central1
         router: https://www.googleapis.com/compute/v1/projects/customer-project/regions/us-central1/routers/router-central1
         selfLink: https://www.googleapis.com/compute/v1/projects/customer-project/regions/us-central1/interconnectAttachments/attach-central-a
         state: PENDING_PARTNER
         type: PARTNER
         

  2. Record the value of the `pairingKey` for each VLAN attachment.




### Request connections from your service provider

Contact your service provider and request four connections, one for each VLAN attachment. The service provider requires the pairing key, capacity, and location for each attachment.

Attachments from one Google Cloud region must connect to a single location (city). In this example, `attach-central-a` and `attach-central-b` are connected to Dallas, and `attach-east-a` and `attach-east-b` are connected to Ashburn.

After the connection configuration is complete, you receive an email notification indicating that you can activate your attachments.

### Activate VLAN attachments

After your service provider configures your VLAN attachments, you must activate them before they can start passing traffic. If you pre-activated your attachments, you can skip this step.

###  Console 

  1. In the Google Cloud console, go to the **VLAN attachments** tab.

[Go to VLAN attachments](https://console.cloud.google.com/hybrid/interconnects/list?tab=attachments)

  2. Select the `attach-central-a` VLAN attachment to view its details page.

  3. If the status of your attachment is `Waiting for service provider`, wait until your service provider has completed the VLAN configuration.

  4. Review the **Interconnect** information to check that the expected service provider configured the VLAN attachment.

  5. Click **Activate** to activate the attachment.

  6. Go back to the **VLAN attachments** tab and activate the other attachments.




###  gcloud 

  1. Describe each VLAN attachment to verify whether your service provider completed configuring them:
         
         gcloud compute interconnects attachments describe attach-central-a \
            --region us-central1 \
            --format '(name,state,partnerMetadata)'
         
         
         gcloud compute interconnects attachments describe attach-central-b \
            --region us-central1 \
            --format '(name,state,partnerMetadata)'
         
         
         gcloud compute interconnects attachments describe attach-east-a \
            --region us-east4 \
            --format '(name,state,partnerMetadata)'
         
         
         gcloud compute interconnects attachments describe attach-east-b \
             --region us-east4 \
             --format '(name,state,partnerMetadata)'
         

After your service provider configures your VLAN attachments, the state of your attachments changes from `PENDING_PARTNER` to `PENDING_CUSTOMER`. If the state is still `PENDING_PARTNER`, wait until your service provider has completed the VLAN configuration.

  2. Check the `partnerMetadata` field to verify that the correct service provider configured each VLAN attachment.

If an unexpected third party configured your VLAN attachment, delete the attachment and then create a new one, which generates a new pairing key. Use the new pairing key to request another connection with your service provider.

  3. If the correct service provider has configured your VLAN attachments, activate them by using the `--admin-enabled` flag:
         
         gcloud compute interconnects attachments partner update attach-central-a \
            --region us-central1 \
            --admin-enabled
         
         
         gcloud compute interconnects attachments partner update attach-central-b \
            --region us-central1 \
            --admin-enabled
         
         
         gcloud compute interconnects attachments partner update attach-east-a \
            --region us-east4 \
            --admin-enabled
         
         
         gcloud compute interconnects attachments partner update attach-east-b \
            --region us-east4 \
            --admin-enabled
         




### Configure routers

Google automatically adds a BGP peer on each Cloud Router. For layer 2 connections, you must add your on-premises ASN to each BGP peer. For layer 3 connections, you don't need to do anything; Google automatically configures your Cloud Routers with your service provider's ASN.

###  Console 

  1. In the Google Cloud console, go to the **VLAN attachments** tab.

[Go to VLAN attachments](https://console.cloud.google.com/hybrid/interconnects/list?tab=attachments)

  2. Select the `attach-central-a` VLAN attachment to view its details page.

  3. Click **Configure BGP** to configure the Cloud Router that's associated with this VLAN attachment.

  4. In the **Peer ASN** field, add the ASN of your on-premises router.

  5. Click **Save and continue**.

  6. Go back to the **VLAN attachments** tab and add your on-premises ASN to the other Cloud Router.




###  gcloud 

  1. Describe the Cloud Router that's associated with the `attach-central-a` VLAN attachment. In the output, find the name of the automatically created BGP peer that's associated with your VLAN attachment. The values of `ipAddress` and `peerIpAddress` of the BGP peer must match the values of `cloudRouterIpAddress` and `customerRouterIpAddress` of your attachment.
         
         gcloud compute routers describe router-central1 \
              --region us-central1
         
         
         bgp:
           advertiseMode: DEFAULT
           asn: 16550
         bgpPeers:
         — interfaceName: auto-ia-if-attachment-central-a-c2c53a710bd6c2e
           ipAddress: 169.254.67.201
           managementType: MANAGED_BY_ATTACHMENT
           name: auto-ia-bgp-attachment-central-a-c2c53a710bd6c2e
           peerIpAddress: 169.254.67.202
         creationTimestamp: '2018-01-25T07:14:43.068-08:00'
         description: 'test'
         id: '4370996577373014668'
         interfaces:
         — ipRange: 169.254.67.201/29
           linkedInterconnectAttachment: https://www.googleapis.com/compute/alpha/projects/customer-project/regions/us-central1/interconnectAttachments/customer-attachment1-partner
           managementType: MANAGED_BY_ATTACHMENT
           name: auto-ia-if-attachment-central-a-c2c53a710bd6c2e
         kind: compute#router
         name: partner
         network: https://www.googleapis.com/compute/v1/projects/customer-project/global/networks/vpc1
         region: https://www.googleapis.com/compute/v1/projects/customer-project/regions/us-central1
         selfLink: https://www.googleapis.com/compute/v1/projects/customer-project/regions/us-central1/routers/router-central1
         

  2. Update the BGP peer with your on-premises router's ASN:
         
         gcloud compute routers update-bgp-peer router-central1 \
              --peer-name auto-ia-bgp-attachment-central-a-c2c53a710bd6c2e \
              --peer-asn ON_PREM_ASN \
              --region us-central1
         




After the BGP sessions are established, you can pass between your VPC network and on-premises network through your service provider's network.

## What's next

  * To learn more about each of these steps, see the [Partner Interconnect provisioning overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/provisioning-overview).

  * To get information about non-critical applications, see [Establish 99.9% availability for Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/partner-creating-999-availability).

  * To help you solve common issues that you might encounter when using Cloud Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
