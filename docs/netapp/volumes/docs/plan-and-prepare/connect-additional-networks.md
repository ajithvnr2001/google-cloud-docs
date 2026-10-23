---
url: https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/connect-additional-networks/
title: Connect additional networks \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:14.129396+00:00
---

# Connect additional networks  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/connect-additional-networks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Connect additional networks Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to connect additional networks to your volumes.

Google Cloud NetApp Volumes uses [private services access](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/networking) to host your volumes. Volumes are provisioned on a tenant VPC within a service-internal project. The tenant VPC is connected to your project VPC using VPC peering. Therefore, only clients connected to your project VPC can access the volumes. If you want to grant access to the volumes to clients on different networks, you have to establish additional network connections.

The following are the connectivity options:

  * **Shared VPCs** : a common approach is to put both NetApp Volumes and all client VMs on the same shared VPC, while keeping the VMs in different service projects for workload isolation and billing purposes.

  * **Flex Unified and Flex File service levels only** : [Network Connectivity Center (NCC) offers service transitivity](https://docs.cloud.google.com/vpc/docs/private-services-access#service-transitivity). For more information, see Connect additional networks with NCC.

  * **VPN connection** : if you connect an additional VPC to your project VPC using VPN instead of VPC peering, you can bypass the transitive routing restriction of VPCs.

  * **VPC peering** : if you connect additional VPCs to your project's VPC using peering, clients on those VPCs can't connect to your volumes as [VPC peering doesn't provide transitive routing](https://docs.cloud.google.com/vpc/docs/vpc-peering#spec-general). However, you can establish direct peerings between these additional VPCs and the tenant VPC. For more information, see Connect additional networks with manual peering.

  * **Interconnects** : if you connect additional networks to your project VPC using interconnects, you can configure transitive routing.




## Connect additional networks with manual peering

NetApp Volumes establishes connectivity by creating a private services access tenant project and network, which is then connected with your specified project network by VPC peering. To enable clients in other networks to access the same volumes, you can peer additional VPCs from your projects to this tenant network.

For any requests to peer an additional VPC with a NetApp Volumes tenant project, contact [Google Cloud Customer Care](https://cloud.google.com/support-hub/).

Before you proceed, we recommend that you review the [VPC peering](https://docs.cloud.google.com/vpc/docs/vpc-peering) documentation to learn about VPC peering limitations, limits, and billing.

## Connect additional networks with NCC

You can connect storage pools that use either the Flex Unified or Flex File service level to other networks by using Google [NCC](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview).

### Considerations

  * Use NCC to connect your consumer VPC to your NCC hub, and create a [producer VPC spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/producer-vpc-spokes-overview) for the NetApp Volumes service. Your project VPC must be peered with NetApp Volumes using private services access as described in [Configure private services access](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/networking#configure_private_services_access). Creating the producer VPC spoke doesn't affect the peering, and the spoke doesn't create connectivity.

  * NCC connections support only the Flex Unified and Flex File service levels. Your project VPC might also include resources of the Standard, Premium, and Extreme service levels, but resources using these service levels won't be accessible from other NCC spokes.

  * Using NCC incurs additional [charges](https://docs.cloud.google.com/network-connectivity/pricing#ncc-pricing). These include an hourly charge for VPC spokes connected to the hub and data transfer charges for VPC spokes. The data transfer charges from the NetApp Volumes VPC producer spoke are billed to the user project that owns the volumes where the spoke is created.

  * You can only change the description of the VPC producer spokes. To change other parameters, you must delete and re-create the spoke.

  * NCC quotas apply to VPC producer spokes, which count towards active spoke limits, and to exported routes to the hub's route table.

  * To create the spoke, administrators need `network.use` permissions for the consumer VPC and `spokes.create` and `spokes.update` permissions.




### Create a producer VPC spoke

Use the following instructions to create a producer VPC spoke using the Google Cloud console or Google Cloud CLI.

### Console

  1. In the Google Cloud console, go to the **Network Connectivity Center** page.

[Go to NCC](https://console.cloud.google.com/hybrid/hubs/list)

  2. Create an NCC hub, if needed.

  3. Make sure you have created a spoke to your consumer VPC that's already peered with NetApp Volumes using private services access.

  4. To create a VPC producer spoke to the NetApp Volumes service, complete the following steps:

     1. Click the **Spokes** tab.

     2. Click **Add spokes**.

     3. In the **Select hub** section, select your hub.

     4. Click **Next step**.

     5. In the **Add spokes** section, complete the following steps:

        1. Choose the **Spoke type** as **Producer VPC network**.

        2. Click the **Consumer VPC spoke** drop-down list, and select your consumer VPC spoke peered to NetApp Volumes.

        3. Enter the peering name as **sn-netapp-prod** in the **Peering name** field.

        4. Click **Done**.

        5. After you create the VPC producer spoke, click **Add a spoke** to add more producer spokes for other consumer VPCs that are also peered with NetApp Volumes.

        6. When you have finished adding spokes, click **Create**. The NCC page shows details about the spokes you created.




### gcloud

After you create the NCC hub and spoke to your consumer VPC that's already peered with NetApp Volumes using private services access, run the following command to create a VPC producer spoke.
    
    
        gcloud network-connectivity spokes linked-producer-vpc-network create SPOKE_NAME \
           --hub=HUB_URI \
           --description=DESCRIPTION \
           --network=HOME_VPC_URI \
           --peering=sn-netapp-prod \
           --group="center" \
           --global \
           --exclude-export-ranges=EXCLUDE_RANGE \
           --include-export-ranges=INCLUDE_RANGE

Replace the following information:

  * `SPOKE_NAME`: the name of the new VPC producer spoke.

  * `HUB_URI`: the Uniform Resource Identifier (URI) for the existing NCC hub.

  * `DESCRIPTION`: the description for the spoke.

  * `HOME_VPC_URI`: the URI for the VPC peered with NetApp Volumes using private services access. The peering must already exist and be in the `ACTIVE` state.

  * `EXCLUDE_RANGE`: Optional: to exclude subnets from being exported by the producer VPC to the NCC hub. Exclude these subnets on both the consumer and VPC producer spokes.

  * `INCLUDE_RANGE`: Optional: to include subnets that can be exported by the producer VPC to the NCC hub.

The peering name for the consumer VPC with NetApp Volumes is `sn-netapp-prod`. Setting the group to `center` is used with NCC star [topologies](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connectivity-topologies), but not for mesh topologies.




## What's next

  * [Manage hubs and spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes).

  * [Supported services for producer VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/producer-vpc-spokes-supported-services).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
