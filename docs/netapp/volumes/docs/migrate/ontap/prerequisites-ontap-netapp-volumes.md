---
url: https://docs.cloud.google.com/netapp/volumes/docs/migrate/ontap/prerequisites-ontap-netapp-volumes/
title: Prerequisites for ONTAP to Google Cloud NetApp Volumes communication \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:34.367424+00:00
---

# Prerequisites for ONTAP to Google Cloud NetApp Volumes communication  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/migrate/ontap/prerequisites-ontap-netapp-volumes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Prerequisites for ONTAP to Google Cloud NetApp Volumes communication Stay organized with collections  Save and categorize content based on your preferences. 

To establish a connection between an ONTAP-based system and NetApp Volumes, the following prerequisites must be met:

  * Source ONTAP system

  * Network connection to Google Cloud project

  * IP address allocation

  * NetApp Volumes settings




## Source ONTAP system

The following requirements must be met for the source ONTAP system:

  * The ONTAP system hosting the source volumes must be running ONTAP version 9.13.1 or higher to ensure compatibility with NetApp Volumes. During the allow-listing process, your ONTAP version is verified against the service version using the [SnapMirror compatibility matrix](https://docs.netapp.com/us-en/ontap/data-protection/compatible-ontap-versions-snapmirror-concept.html#unified-replication-relationships).

  * The SnapMirror feature must be licensed and enabled on the source cluster.

  * On the source ONTAP system, you must configure one InterCluster-LIF per node on the network that is connected to your Google project.

  * The TCP ports 10000, 11104, 11105, and ICMP must be reachable on all InterCluster-LIFs. HTTPS access isn't required. These ports are included in the _default-intercluster_ service policy, which is used on intercluster-LIFs on your source system by default.

  * You must have the required ONTAP administrator permissions to accept cluster and SVM peerings.

  * Flex Unified ONTAP-mode systems can act as a migration source, but not as a migration destination. Use ONTAP SnapMirror to migrate ONTAP-based systems, including ONTAP-mode storage pools, to ONTAP-mode volumes. For more information, see [Learn about ONTAP SnapMirror asynchronous disaster recovery](https://docs.netapp.com/us-en/ontap/data-protection/snapmirror-svm-replication-concept.html). ONTAP doesn't support [SVM data mobility](https://docs.netapp.com/us-en/ontap/svm-migrate/index.html), also known as SVM migrate.




## Network connection to Google Cloud project

NetApp Volumes uses private service access to connect to your Virtual Private Cloud (VPC), and private service access uses VPC peering. Due to the non-transitive routing attribute of VPC peering connections, traffic can't traverse more than one sequential VPC peering hop.

For example, using a hub and spoke network connected through VPC peering can cause connectivity issues. If your on-premise connection arrives in a transit VPC (hub) that is connected using VPC peering to a workload VPC (spoke), which is then connected to NetApp Volumes, no traffic from on-premises or the transit gateway can be routed to NetApp Volumes, and the other way around.

As a rule of thumb, NetApp Volumes is VPC peered to your user-VPC. Therefore, make sure your user-VPC doesn't use VPC peering for the next hop in the network traffic's path to your source system.

The working deployment models include the following:

  * Terminate the interconnect connection directly in the user-VPC.

  * Use a VPN connection that terminates in the user-VPC.

  * Use non-VPC peering routing for the upstream connection of your user-VPC.




## IP address allocation

For the Flex Unified service level, NetApp Volumes provisions intercluster LIF IP addresses during pool creation from the same CIDR range as other pool IP addresses.

For all other supported service levels, NetApp Volumes reserves dedicated `/27` CIDRs from the `psaRange` you delegated to the private service access peering for migration traffic. This CIDR range is used to receive one or more volume migrations to destination volumes within the same project or region pair. These migrations can originate from multiple source clusters. Provisioning migrations to different projects or region pairs results in the reservation of an additional `/27` CIDR. External replication and volume migration use the same CIDR allocations and cluster peerings.

## NetApp Volumes settings

The following requirements must be met for NetApp Volumes:

  * You must have sufficient IAM permissions to manage hybrid replication. The `roles/netapp.admin` includes all required permissions.

  * Provide a storage pool that is large enough to host the destination volume. Make sure that the pool has the correct Active Directory, LDAP, and CMEK settings required by the destination volume you are creating.

  * If your volume contains SMB data, create the destination volume in a storage pool which is connected to the same Windows domain as the source volume.




If you use firewalls in your network, make sure that your source intercluster-LIFs and NetApp Volumes are allowed for TCP ports 10000, 11104, 11105, and ICMP.

## What's next

[Create a volume migration](https://docs.cloud.google.com/netapp/volumes/docs/migrate/ontap/create-volume-migration).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
