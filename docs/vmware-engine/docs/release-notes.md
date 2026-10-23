---
url: https://docs.cloud.google.com/vmware-engine/docs/release-notes/
title: VMware Engine release notes \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:40:55.974069+00:00
---

# VMware Engine release notes  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Resources ](https://docs.cloud.google.com/vmware-engine/docs/resources)



Send feedback 

#  VMware Engine release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Google Cloud VMware Engine. Check this page for announcements about new or updated features, bug fixes, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/vmware-engine-release-notes.xml) directly. 

## October 01, 2026

Feature

**Generally available** : Bring Your Own License (BYOL) license management for Google Cloud VMware Engine is generally available (GA). BYOL license management lets you register and manage portable VMware Cloud Foundation (VCF) license keys in the Google Cloud console across projects associated with your Cloud Billing account.

For more information, see [License management](https://docs.cloud.google.com/vmware-engine/docs/license-management).

## August 24, 2026

Announcement

**VMware component updates:** The VMware Engine operations team is updating vCenter Server and ESXi to version 8.0 Update 3k to address security vulnerabilities described in Broadcom Security Advisory [VMSA-2026-0006](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017). For details about the update and schedule, see the [Latest service announcements](https://docs.cloud.google.com/vmware-engine/docs/service-announcements#2026-08-24).

## August 01, 2026

Feature

**Preview** : Google Cloud VMware Engine capacity allocations are available in preview. A capacity allocation is a global reservation of physical nodes for your Cloud Billing account. Your reserved nodes are organized into placement groups (PGs), which represent the specific physical hardware and location of your reserved capacity.

Google Cloud VMware Engine capacity allocations let you do the following: * Use a capacity allocation during private cloud creation by selecting a PG. * Use a capacity allocation when adding a cluster. * Configure a hybrid private cloud across multiple PGs.

For more information, see [Manage capacity allocations](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-manage-capacity-allocations).

## July 08, 2026

Feature

**Preview** : You can configure disaster recovery for Google Cloud VMware Engine by using JetStream. Disaster recovery options include the following:

  * Set up a Google Cloud VMware Engine private cloud as a recovery site for your on-premises VMware applications.
  * Protect workloads on a primary private cloud by using a recovery site in another Google Cloud location or on-premises environment.



For more information, see [Configure disaster recovery using JetStream](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-disaster-recovery-jetstream).

Feature

**Generally available** : Google Cloud VMware Engine offers self-service management for [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-vsan-encryption) using the Google Cloud console and the VMware Engine API. You can enable CMEK for your private clouds, using Cloud Key Management Service (Cloud KMS) to manage encryption keys for vSAN and [vTPM](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-vtpm). Key features and considerations include:

  * You can transition between CMEK and Google-owned and Google-managed encryption keys (GMEK) as needed.
  * The "Auto-Rekey" feature integrates with Cloud KMS key rotation to perform automated key rotation for the key encryption key (KEK), maintaining security without manual intervention or service downtime.



**Limitations** : This self-service functionality is unavailable for private clouds that use CMEK through service tickets.

## July 07, 2026

Feature

Custom organization policy constraints are generally available (GA) for Google Cloud VMware Engine. You can use custom constraints to enforce security policies and restrict configuration of your VMware Engine resources.

For more information, see [Use custom organization policies](https://docs.cloud.google.com/vmware-engine/docs/custom-constraints).

## June 24, 2026

Announcement

**HCX upgrade to 4.11.4:** The VMware Engine operations team is initiating updates of the HCX Manager Appliance to version 4.11.4. This upgrade resolves an issue with MON-enabled segments. You are responsible for upgrading the HCX On-Prem/Connectors and Service Mesh Appliances. For more details, see the [Latest service announcements](https://docs.cloud.google.com/vmware-engine/docs/service-announcements#2026-06-24).

## June 11, 2026

Announcement

The VMware Engine [`ve2` node type](https://docs.cloud.google.com/vmware-engine/docs/concepts/node-types) is now available in the following additional region:

  * Mexico City (`northamerica-south1`)



## June 01, 2026

Announcement

All 3-year (36-month) post-paid `ve2` [committed use discounts (CUDs)](https://docs.cloud.google.com/vmware-engine/docs/cud) for Google Cloud VMware Engine purchased after May 31, 2026, will terminate on October 15, 2028. 3-year CUD pricing will apply, regardless of the actual term of the CUD. Additionally, 3-year pre-paid CUDs are no longer available; only 1-year pre-paid CUDs are available.

## May 20, 2026

Announcement

All 1-year [committed use discounts (CUDs)](https://docs.cloud.google.com/vmware-engine/docs/cud) for Google Cloud VMware Engine `ve1` SKUs are now End-of-Sale across the europe-west2 (London, UK) region. You can continue to use `ve1` nodes with on-demand pricing. This change doesn't affect existing CUDs. You can also use `ve2` nodes, including `ve2` CUDs.

## May 15, 2026

Announcement

**ve1 hardware End-of-Life (EoL) migration guide:** You can now refer to the public documentation to [migrate workloads from retiring ve1 hardware](https://docs.cloud.google.com/vmware-engine/docs/howto-migrate-ve1-hardware). First-generation `ve1` bare metal nodes are reaching the end of their useful life on a rolling basis. When your hardware is scheduled for retirement, you receive an EoL notification containing timelines and instructions to migrate your clusters.

## May 11, 2026

Feature

You can now use Privileged Access Manager (PAM) to [delete clusters](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-manage-private-cloud#delete-cluster) in the private clouds.

## May 05, 2026

Announcement

The VMware Engine [`ve2` node type](https://docs.cloud.google.com/vmware-engine/docs/concepts/node-types) is now available in the following additional region:

  * Eemshaven, Netherlands (`europe-west4-a`)



## April 27, 2026

Feature

**Generally available (GA) with an allowlist:** You can now [migrate VMware management VMs](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-manage-private-cloud#migrate-vms) from their host cluster to a different cluster within the same private cloud. This feature is available to select customers through an allowlist. To migrate management VMs, you must have at least two clusters in your private cloud, and the destination cluster must be a workload cluster. This operation transitions the target workload cluster to a management cluster, and the source management cluster becomes a workload cluster.

## March 10, 2026

Feature

**Public Preview:** You can now [migrate VMware management VMs](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-manage-private-cloud#migrate-vms) from their host cluster to a different cluster within the same private cloud. To migrate management VMs, you must have at least two clusters in your private cloud, and the destination cluster must be a workload cluster. This operation transitions the target workload cluster to a management cluster, and the source management cluster becomes a workload cluster.

## March 09, 2026

Announcement

The VMware Engine [`ve2` node type](https://docs.cloud.google.com/vmware-engine/docs/concepts/node-types) is now available in the following additional region:

  * Los Angeles, USA, North America (`us-west2-b`)



## February 20, 2026

Announcement

The VMware Engine [`ve2` node type](https://docs.cloud.google.com/vmware-engine/docs/concepts/node-types) is now available in the following additional region:

  * Paris, France, Europe (`europe-west9-b`)



## February 13, 2026

Announcement

The VMware Engine [`ve2` node type](https://docs.cloud.google.com/vmware-engine/docs/concepts/node-types) is now available in the following additional region:

  * Osaka, Japan, Asia Pacific (`asia-northeast2`)



## January 29, 2026

Announcement

Stretched private clouds capable of hosting both `ve1` and `ve2` node-family clusters are now available in the following regions:

  * Sydney, Australia, Asia Pacific (`australia-southeast1-a`, `australia-southeast1-b`)
  * Frankfurt, Germany, Europe (`europe-west3-a`, `europe-west3-b`)



While a stretched private cloud can contain mixed node families, each individual stretched cluster must be comprised of nodes from the same family type.

**Note:** To create a new stretched cluster of a different node family, contact Cloud Customer Care.

## January 13, 2026

Announcement

Private clouds capable of hosting both `ve1` and `ve2` node-family clusters are available in the following additional regions:

  * London, England, Europe (`europe-west2-a`, `europe-west2-b`)
  * São Paulo, Brazil, South America (`southamerica-east1-a`)
  * Dallas, Texas, North America (`us-south1-b`)



While a private cloud can contain mixed node families, each individual cluster must be comprised of nodes from the same family type.

**Note:** To create a new cluster of a different node family, contact Cloud Customer Care.

## January 06, 2026

Feature

VMware Engine introduces enhancements to simplify using external NFS datastores. External NFS datastores let you scale storage independently of compute resources for your VMware workloads. You can use Filestore or Google Cloud NetApp Volumes as external NFS datastores for ESXi hosts in Google Cloud VMware Engine. For more information, see [NFS datastores overview](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/concepts-nfs-datastores-overview).

## December 25, 2025

Announcement

VMware Engine [`ve2` nodes](https://docs.cloud.google.com/vmware-engine/docs/concepts/node-types) are now available in the Milan, Italy (`europe-west8-b`) zone in the Milan, Italy, Europe region (`europe-west8`).

## December 05, 2025

Announcement

VMware Engine now supports private clouds with mixed node families (`ve1` and `ve2`). While a private cloud can contain mixed node families, each cluster within that private cloud must contain nodes of the same type. This feature is available in the following regions and zones:

  * Ashburn, North America (`us-east4-a`, `us-east4-b`)
  * Iowa, North America (`us-central1-a`)
  * Montreal, North America (`northamerica-northeast1-a`)
  * Sydney, Australia (`australia-southeast1-a`, `australia-southeast1-b`)
  * Frankfurt, Europe (`europe-west3-a`, `europe-west3-b`)
  * Santiago, South America (`southamerica-west1-b`)

**Note:** To create a new cluster of a different node family, contact Cloud Customer Care.

## November 26, 2025

Announcement

VMware Engine [`ve2` nodes](https://docs.cloud.google.com/vmware-engine/docs/concepts/node-types) are now available in the Dallas, Texas, North America region (`us-south1-b`).

## November 14, 2025

Announcement

VMware Engine [`ve2` nodes](https://docs.cloud.google.com/vmware-engine/docs/concepts/node-types) are now available in the Tokyo, Japan region (`asia-northeast1-a`).

## November 04, 2025

Announcement

VMware Engine [`ve2` nodes](https://docs.cloud.google.com/vmware-engine/docs/concepts/node-types) are now available in the London, England, Europe (`europe-west2-b`) zone in the London, England, Europe region (`europe-west2`).

## October 31, 2025

Announcement

VMware Engine [`ve1` nodes](https://docs.cloud.google.com/vmware-engine/docs/concepts/node-types) are now available in the Mumbai, India (`asia-south1-b`) zone in the Mumbai region (`asia-south1`).

## October 03, 2025

Announcement

This is to notify you about upcoming changes in licensing model with Google Cloud VMware Engine following [Broadcom's recent announcement](https://blogs.vmware.com/cloud-foundation/2025/08/29/vmware-cloud-foundation-cloud-on-your-terms/) to move to a "bring your own" subscription model for VMware Cloud Foundation (VCF).

You can renew or add additional capacity of VMware Engine nodes with VCF-license included until **October 15, 2025**. After that, Google Cloud will not be able to sell new VMware Engine VCF license-included nodes. You can buy new VMware Engine BYOL nodes and use them with "bring your own" VCF subscriptions (purchased by you from Broadcom) for new capacity after **October 15, 2025**.

For any questions, please reach out to your Google Cloud sales team, who can help review your specific scenarios, discuss the implications of these changes for your organization, and help you manage this transition.

For more details, see the [October 3, 2025](https://docs.cloud.google.com/vmware-engine/docs/service-announcements#2025-10-03) service announcement.

## September 26, 2025

Announcement

VMware Engine `ve2` nodes are now available in the following additional region:

  * Doha, Qatar (`me-central1`, `v-zone-a`)



## September 24, 2025

Announcement

All 3-year [Committed Use Discounts (CUDs)](https://docs.cloud.google.com/vmware-engine/docs/cud) for VMware Engine `ve1` SKUs are now End-of-Sale across all regions where the service is available.

The following specific 3-year commitments are impacted by this change:

  * 3-year commitment (monthly payments), Fully Licensed Pricing - "postpaid"
  * 3-year commitment (upfront payments), Fully Licensed Pricing - "prepay"
  * 3-year commitment (monthly payments), Fully Licensed convertible commitment - "postpaid"
  * 3-year commitment (upfront payments), Fully Licensed convertible commitment - "prepay"
  * 3-year commitment (monthly payments), Portable License Pricing - "postpaid"
  * 3-year commitment (upfront payments), Portable License Pricing - "prepay"
  * 3-year commitment (monthly payments), Protected License Pricing - "postpaid"
  * 3-year commitment (upfront payments), Protected License Pricing - "prepay"



Refer to [VMware Engine node types](https://docs.cloud.google.com/vmware-engine/docs/concepts-node-types) for the regional availability of `ve1` SKUs.

## September 15, 2025

Announcement

VMware Engine `ve2` nodes are now available in the following additional region and zone:

  * The Milan, Italy, Europe region (`europe-west8-a`).
  * The Melbourne, Australia (`australia-southeast2-b`) zone in the Melbourne, Australia region (`australia-southeast2`).



## September 11, 2025

Feature

You can now use Privileged Access Manager (PAM) to accelerate the deletion of "soft deleted" private clouds. For more information, see the documentation on how to [delete a private cloud](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-delete-private-cloud).

## August 28, 2025

Announcement

VMware Engine `ve2` nodes are now available in the London, England, Europe region (`europe-west2-a`).

## August 14, 2025

Announcement

VMware Engine `v2` nodes are now available in the Santiago, Chile (`southamerica-west1-b`) zone in the Santiago region (`southamerica-west1`) region.

## August 08, 2025

Announcement

VMware Engine `ve2` nodes are now available in the Dammam, KSA (`me-central2`) region.

## July 14, 2025

Announcement

VMware Engine `ve2` nodes are now available in the São Paulo, Brazil (`southamerica-east1-c`) zone in the São Paulo region (`southamerica-east1`).

## July 07, 2025

Feature

When upgrading to Windows Server 2022 or newer images on your GCVE private clouds, you can use a combination of Windows Server BYOL for Windows Server 2019 and earlier images and on-demand licensing for Google-provided Windows Server 2022. For more information, see [Use a combination of BYOL and on-demand Windows Server licenses from Google](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/microsoft-licensing#combination-mode).

## July 01, 2025

Feature

VMware Engine single-node private clouds, created after June 4th 2025, will no longer delete after 60 days. All single-node private clouds will have no time limit. Single-node private clouds have limitations to [SLA](https://cloud.google.com/vmware-engine/sla?e=48754805&hl=en), [patching](https://docs.cloud.google.com/vmware-engine/docs/concepts-private-cloud#single-node), and [upgrades](https://docs.cloud.google.com/vmware-engine/docs/concepts-private-cloud#single-node).

## June 11, 2025

Announcement

VMware Engine `ve2` nodes are now available in Toronto, Canada (`northamerica-northeast2`).

## June 09, 2025

Announcement

VMware Engine `ve2` nodes are now available in the following additional region:

  * Melbourne, Australia (`australia-southeast2-a`)



## May 22, 2025

Announcement

All new VMware Engine private clouds now deploy with the following versions:

  * VMware vSphere version 8.0 update 3
  * [NSX-T 4.2.1.2](https://techdocs.broadcom.com/us/en/vmware-cis/nsx/vmware-nsx/4-2/release-notes/vmware-nsx-4212-release-notes.html)



Existing private clouds will be upgraded starting June 2025. See [Service announcements](https://docs.cloud.google.com/vmware-engine/docs/service-announcements#2025-05-19) for more details on the contents of this update.

## May 09, 2025

Announcement

VMware Engine `ve2` nodes are available in Montreal, Canada (`northamerica-northeast1`).

## April 03, 2025

Announcement

Google Cloud VMware Engine now supports 24 ve2 node types, enabling precise and efficient environment sizing. See [VMware Engine node types](https://docs.cloud.google.com/vmware-engine/docs/concepts-node-types) for full details.

## March 18, 2025

Announcement

VMware Engine is integrated with Google Cloud Essential Contacts for email notifications. Automatic emails are sent to the appropriate Essential Contacts notification categories for service-impacting events. For more information, see [Overview of VMware Engine monitoring](https://docs.cloud.google.com/vmware-engine/docs/concepts-monitoring).

## February 25, 2025

Feature

**Generally available:** VMware Engine **Update center** on the Google Cloud console is now generally available. Update center lets you view and manage updates to your private clouds, including specifying start dates and times for schedulable VMware version updates, and viewing the status of in-progress schedulable and non-schedulable updates, such as security patches. For more information, see [Update a private cloud](https://docs.cloud.google.com/vmware-engine/docs/update-center).

## February 13, 2025

Feature

Google Cloud VMware Engine now supports soft deletion for private clouds. This feature provides seven days of post delete data protection. See [Delete a private cloud](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-delete-private-cloud) for more information.

## January 23, 2025

Change

Google Cloud VMware Engine Committed use discounts (CUD) are now managed exclusively in the VMware Engine section of the Google Cloud console. For more details, see [VMware Engine CUDs](https://docs.cloud.google.com/vmware-engine/docs/cud) documentation.

## January 13, 2025

Announcement

VMware Engine ve1 nodes are now available in the following additional region:

  * Paris, France (`europe-west9-b`)



## November 21, 2024

Announcement

VMware Engine ve1 nodes are now available in the following additional region:

  * Dallas, Texas, North America (`us-south1-b`).



## November 20, 2024

Announcement

VMware Engine ve2 nodes are now available in the following regions:

  * São Paulo, Brazil (`southamerica-east1`)
  * Santiago, Chile (`southamerica-west1`)



## October 17, 2024

Announcement

Stretched private clouds using `ve2' node types are now available in the following region:

  * Frankfurt, Germany, Europe (`europe-west3`)



## October 16, 2024

Fixed

Added missing release notes for stretched private cloud availability using `ve2` node types in Sydney, Australia, APAC (`australia-southeast1-b`)

## October 09, 2024

Announcement

VMware Engine ve2 nodes are available in Frankfurt, Germany, Europe (`europe-west3-b`).

Announcement

VMware Engine ve1 nodes are available in Jurong West, Singapore, APAC (`asia-southeast1-b`).

## September 26, 2024

Announcement

VMware Engine `ve2` nodes are available in Frankfurt, Germany, Europe (`europe-west3-a`).

## September 03, 2024

Feature

VMware Engine now offers GA support for VPC Service Controls. VPC Service Controls provides an additional layer of security to prevent data exfiltration and unauthorized access. For more information, see [VPC Service Controls](https://docs.cloud.google.com/vmware-engine/docs/concepts-vpc-service-controls).

## August 09, 2024

Announcement

VMware Engine `ve2-mega-64` node type is generally available in the `australia-southeast1` region. For more information on the node type, see [Node types](https://docs.cloud.google.com/vmware-engine/docs/concepts-node-types). To use the node type in the `australia-southeast1` region, contact your Google account team.

## August 04, 2024

Announcement

Stretched Private Clouds using `ve2' node types are now available in the following region:

Sydney, Australia, APAC (`australia-southeast1-b`)

## July 29, 2024

Feature

You can now purchase Fully licensed commitments, Fully licensed convertible commitments, and Portable License commitments. For more information, see [Purchasing VMware Engine commitments](https://docs.cloud.google.com/vmware-engine/docs/cud#purchasingvmwareenginecommitments).

## July 25, 2024

Announcement

VMware Engine `ve2` nodes are available in the following additional zones:

  * Sydney, Australia, APAC (`australia-southeast1-b`)
  * Ashburn, Virginia, North America (`us-east4-b`)



## July 24, 2024

Announcement

New VMware Engine `ve2` node types are available in the `australia-southeast1`, `us-central1`, and `us-east4` regions:

HCI node types

  * `ve2-standard-96`
  * `ve2-mega-96`
  * `ve2-mega-128`



Storage only node types

  * `ve2-standard-so`
  * `ve2-mega-so`



See [VMware Engine node types](https://docs.cloud.google.com/vmware-engine/docs/concepts-node-types) for more information on node types.

## July 19, 2024

Announcement

VMware Engine `ve2-standard-128` node type is generally available in `us-central1` region. For more information on the node type, see [Node types](https://vmware-engine/docs/concepts-private-cloud#node-types). To use the node type in `us-central1` region, contact your Google account team.

## July 11, 2024

Fixed

Added missing release notes for `ve2-standard-128` availability in `australia-southeast1` region

## June 14, 2024

Announcement

VMware Engine `ve2-standard-128` node type is generally available in `australia-southeast1` region. For more information on the node type, see [Node types](https://vmware-engine/docs/concepts-private-cloud#node-types). To use the node type in `australia-southeast1` region, contact your Google account team.

## May 24, 2024

Change

When you initiate deletion of a private cloud, billing now stops immediately, but the deletion might take up to 24 hours to complete.

This lets you contact support if you need to stop the deletion. During the deletion of the private cloud, it is still visible in the console, and your VMs continue to run.

If necessary, disable or reconfigure networking components.

## May 21, 2024

Announcement

All new VMware Engine private clouds now deploy with the following:

  * VMware vSphere version 7.0 Update 3
  * NSX-T version 3.2.3.1



Existing private clouds will be upgraded in May and June 2024.

For more details on the contents of this upgrade, see [Service announcements](https://docs.cloud.google.com/vmware-engine/docs/service-announcements#2024-03-07).

## April 01, 2024

Feature

Storage-only nodes are now generally available. For more information, see [Use storage-only nodes](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-use-storage-only-nodes).

## March 11, 2024

Feature

Google Cloud VMware Engine now leverages Cloud Logging to provide status updates about hardware health and VMware management components. The logs are available in [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) with the following log name:

  * `projects/PROJECT_ID/logs/vmwareengine.googleapis.com%2Falerts`



These logs are also available in the **Google Cloud VMware Engine UI** on the **Dashboard** in **Logs**.

## March 07, 2024

Announcement

Beginning mid-March 2024, the VMware Engine operations team will upgrade VMware components to newer versions. Users affected by this upgrade will receive an email with planned maintenance dates and times.

For details about the upgrade and steps to prepare, see [Latest service annoucements](https://docs.cloud.google.com/vmware-engine/docs/service-announcements).

## February 28, 2024

Announcement

Beginning on March 12, 2024, the VMware Engine operations team will perform essential maintenance of the network infrastructure to improve equipment robustness and apply security patches. Users affected by this upgrade will receive an email with planned maintenance dates and times.

For details about the upgrade and steps to prepare, see [Service annoucements](https://docs.cloud.google.com/vmware-engine/docs/service-announcements).

## February 27, 2024

Feature

Purchasing commitments for node types is now generally available. For more information, see [Purchasing commitments for node types](https://docs.cloud.google.com/vmware-engine/docs/cud#purchasingcommitmentsfornodetypes).

## February 16, 2024

Announcement

VMware Engine `ve2-standard-128` node type is generally available in `us-east4` region. For more information on the node type, see [Node types](https://vmware-engine/docs/concepts-private-cloud#node-types). To use the node type in `us-east4` region, contact your Google account team.

## December 18, 2023

Feature

Google Cloud VMware Engine now supports additional Terraform resources for automating private cloud, cluster, and network management. These enhancements to the VMware Engine Terraform provider enables full environment Infrastructure-as-Code for your VMware Engine Environment. This release includes support for:

  * Standard PC (GA Promotion)
  * Cluster (GA Promotion)
  * Standard VEN support
  * Network peering 
  * Network policy management
  * Dns server ip 
  * Subnet management
  * External IP addresses
  * Nsx credential management
  * Vcenter credential management
  * Time limited PC (Single node PC)



To learn more about these new features and how to get started, please visit the [VMware Engine documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/vmwareengine_private_cloud) on the Hashicorp site and review the [IaC Foundations blueprint](https://github.com/GoogleCloudPlatform/gcve-iac-foundations).

## December 12, 2023

Feature

Specific Google Cloud VMware Engine resources have been onboarded to **Cloud Asset Inventory and Search (CAIS)** and are now available through the CloudAsset APIs. This allows you to search, export, and analyze asset metadata associated with the onboarded resources.

The following resources have been onboarded:

  * [PrivateCloud](https://docs.cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.privateClouds)
  * [Cluster](https://docs.cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.privateClouds.clusters)
  * [VMwareEngineNetwork](https://docs.cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.vmwareEngineNetworks)
  * [NetworkPeering](https://docs.cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.networkPeerings)
  * [PrivateConnection](https://docs.cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.privateConnections)
  * [NetworkPolicy](https://docs.cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.networkPolicies)
  * [ExternalAccessRule](https://docs.cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.networkPolicies.externalAccessRules)
  * [ExternalAddress](https://docs.cloud.google.com/vmware-engine/docs/reference/rest/v1/projects.locations.privateClouds.externalAddresses)



These resources are also available using the global search on the Google Cloud Console and under the Asset Inventory UI.

Learn more about:

  * the [list of resources available using CAIS](https://docs.cloud.google.com/asset-inventory/docs/supported-asset-types) and search for VMware.
  * what you can do with [CAIS](https://docs.cloud.google.com/asset-inventory/docs/overview).



## November 14, 2023

Feature

[VMware Engine network](https://docs.cloud.google.com/vmware-engine/docs/networking/vmware-engine-network): Further simplification of the networking architecture and experience in VMware Engine removes the need for private service networking. With VMware Engine networks, you can create multiple isolated networks within the same project and connect them as needed to consumer VPCs to deliver complex topologies.

Feature

[DNS Server IP](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-create-dns-bindings#get_a_private_cloud_workload_dns_server_ip): Workloads within your private cloud can now use native Cloud DNS for DNS resolution.

Feature

[ESXi (NSX-T Distributed Log Forwarding)](https://docs.cloud.google.com/vmware-engine/docs/environment/howto-forward-syslog): You can now configure both ESXi logs, including NSX-T Distributed Firewall (DFW) Logs, to a remote syslog server.

Feature

[Google Cloud console experience for VMware Engine](https://docs.cloud.google.com/vmware-engine/docs/whats-new): You can use the Google Cloud console to manage your VMware Engine environments without opening another tab. For more information on migrating to this refreshed experience, see [What's new with VMware Engine](https://docs.cloud.google.com/vmware-engine/docs/whats-new#data-migration).

Feature

[Management DNS for private clouds](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-private-cloud-management-dns): Automatic Management DNS Peering is now Automatic Management DNS for Private Clouds. You can now view and manage the DNS bindings for the private cloud management zone.

Feature

Integrated networking: Private cloud deployment is now just one simple step. VMware Engine network and initial VPC peering to your VPC can be done at the time of private cloud creation.

Breaking

Elevate privilege option is no longer available. You can sign in using one of the solution users to perform elevated privileges actions. For details, see [Elevating VMware Engine privileges](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-elevate-privilege).

Feature

Finer-grained access controls for additional resources: VMware Engine provides finer-grained, per-action access controls for actions performed on new resources added. To view a comprehensive list of permissions for VMware Engine, go to the [Permissions reference](https://docs.cloud.google.com/iam/docs/permissions-reference) and search for the prefix _vmwareengine_.

Breaking

Firewall Tables: Existing firewall tables and rules have been migrated to [external access rules](https://docs.cloud.google.com/vmware-engine/docs/networking/external-access-rules).

Feature

[Integrated Cloud DNS for workloads (DNS Bindings)](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-create-dns-bindings): Bi-directional Cloud DNS capabilities that enable DNS resolution for VMware Engine workloads, delivering enterprise needs in a simplified and more streamlined manner. Cloud DNS administrators can bind the VMware Engine network just as any other VPC.

Feature

[(Legacy Networks) DNS forwarding rules](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-legacy-conditional-dns-forwarding): Allows configuration of management appliance DNS resolution for private clouds attached to legacy VMware Engine networks.

Feature

Additional Google Cloud CLI and VMware Engine API Endpoints: More capabilities delivered using VMware Engine API and Google Cloud CLI enables you to programmatically manage VMware Engine environments, including VMware Engine API and Google Cloud CLI functions for managing the new networking model, network peering, external access rules and external IP service, consumer DNS, and more.

Breaking

DNS Profiles: Existing DNS Profiles will be migrated to each private cloud in which the DNS Profile was assigned. [DNS forwarding rules](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-legacy-conditional-dns-forwarding) can be configured within each private cloud.

Feature

[Advanced VPC Peering](https://docs.cloud.google.com/vmware-engine/docs/networking/peer-vpc-network): Virtual Private Cloud network peerings define network connectivity between VMware Engine networks, Google VPCs, and other services. You can now create a complex set of VPC peerings within the Google Cloud console.

Deprecated

[Announced August 10, 2022](https://docs.cloud.google.com/vmware-engine/docs/release-notes#August_10_2022): Removed ability to manage point-to-site (P2S) VPN gateways for projects with existing P2S VPN gateways. You can continue to use an alternative VPN solution. For details, see [Connecting using VPN](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-vpn-connect#connect-to-gcve-using-point-to-site-vpn). Contact customer care for P2S VPN gateway removal.

Feature

[External access rules](https://docs.cloud.google.com/vmware-engine/docs/networking/external-access-rules): Control access to external IP addresses. We have simplified the rule creation process to no longer require creation of a table and attachment to a subnet. External access rules now support one or more [external IP address](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-allocate-external-ip) within a single rule.

Feature

[Increase to the default VPC Peer count](https://docs.cloud.google.com/vmware-engine/docs/networking/peer-vpc-network): Any standard VMware Engine network now supports 25 VPC Peers by default.

## September 30, 2023

Announcement

VMware Engine nodes are now available in the following additional zone:

  * Tel Aviv (`me-west1-b`)



## September 13, 2023

Announcement

VMware Engine nodes are now available in the following additional zone:

  * Tel Aviv (`me-west1-a`)



## June 28, 2023

Feature

Google Cloud VMware Engine now supports Terraform for private cloud, cluster, and network management. This release covers Create, Update, and Delete commands for private cloud resources. The VMware Engine Terraform provider enables Infrastructure-as-Code for your VMware Engine Environment.

To learn more about these new features and how to get started, please visit the [VMware Engine documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/vmwareengine_private_cloud) on the Hashicorp site and review the [IaC Foundations blueprint](https://github.com/GoogleCloudPlatform/gcve-iac-foundations).

Feature

Google Cloud VMware Engine now supports ESXi syslog forwarding, including distributed firewall logs, which provides more visibility into security events on VMware Engine instances. 

Enhanced Service Controls: VMware Engine is also releasing additional security controls that will enable you to manage permissions elevation. This enhanced security model gives you more granular control over how Google support staff access your VMware Engine instances for workloads that require additional controls due to regulatory or compliance reasons. Please contact support for assistance with configuring these services.

## June 26, 2023

Announcement

Pay-as-you-go (PAYG) licenses for Windows Server are now available in Preview.

## June 21, 2023

Announcement

Stretched Private Clouds are now available in the following region:

  * London, England, Europe (`europe-west2`)



Stretched Private Clouds allow you to stretch your vSphere/vSAN clusters across Google Cloud zones and protect against zone-level failures. This functionality enables high levels of availability for business critical applications.

## June 14, 2023

Feature

Google Cloud VMware Engine now supports the provisioning of Single Node Private Clouds, configuration of Management Subnets (HCX and Service Subnets), as well as CRUD of Private Connections using the GCloud CLI and VMware Engine API. These features streamline your VMware Engine process flows by using higher degrees of automation.

## May 25, 2023

Announcement

VMware Engine nodes are now available in the following additional region:

  * Turin, Italy (`europe-west12`)



## May 16, 2023

Feature

VMware Aria Operations for Logs is now certified for Google Cloud VMware Engine. You can use VMware Aria Operations for Logs to collect and manage logs from VMware Engine and on-prem environments into a centralized solution. 

VMware Aria Operations for Logs with VMware Engine enables more operational visibility and intelligent analytics for both troubleshooting and auditing purposes, making it easier for you to manage and operate your VMware Engine environment. See the [VMware blog announcement](https://blogs.vmware.com/management/2023/05/google-cloud-vmware-engine-and-vmware-aria-operations-for-logs.html) for more information.

## May 02, 2023

Issue

After installing Windows Server 2022 update KB5022842 (OS Build 20348.1547), guest OS can not boot up when virtual machine(s) is configured with secure boot enabled. For more information, see [Virtual Machine with Windows Server 2022 KB5022842 (OS Build 20348.1547) configured with secure boot enabled not booting up](https://docs.cloud.google.com/vmware-engine/docs/known-issues#vm-secure-boot). To work around this issue, you can do one of the following:

  * Skip KB5022842 and use KB5023705
  * Disable "Secure Boot" on affected VMs



## April 25, 2023

Feature

VMware Engine adds a VPC Service Controls guided opt-in and policy export that enables you to attach VMware Engine services to a new or existing VPC Service Controls perimeter. For more information, see [VPC Service Controls](https://docs.cloud.google.com/vmware-engine/docs/concepts-vpc-service-controls).

## March 31, 2023

Announcement

VMware Engine nodes are now available in the following additional region:

  * Santiago (`southamerica-west1`)



Announcement

VMware Engine nodes are now available in the following additional zone:

  * London, England (`europe-west2-b`)



## March 14, 2023

Change

Resource name translation will be required after April 2023.

For more information on resource name translation, see [Resource Name Translation](https://docs.cloud.google.com/vmware-engine/docs/resource-name-translation).

## March 09, 2023

Announcement

VMware Engine nodes are now available in the following additional region:

  * Delhi (`asia-south2`)



## February 22, 2023

Feature

VMware Engine private clouds support the addition of a Trusted Platform Module (TPM) 2.0 virtual cryptoprocessor to a virtual machine. 

For details about this feature, see [About Virtual Trusted Platform Module](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-vtpm).

## January 23, 2023

Breaking

Removed ability to create stateful outbound firewall rules for new projects and projects that have not yet created stateful outbound rules. Customers can continue to create a firewall rule set in NSX-T Gateway or NSX-T Distributed Firewall rules to limit or control outbound access.

## January 17, 2023

Issue

If you are running VMware Engine Horizon (VDI) on Google Cloud VMware Engine, you may encounter errors after changing your private cloud resource naming to meet the standards for Google Cloud CLI and VMware Engine API.

To troubleshoot this issue, see [VMware Engine Known issues](https://docs.cloud.google.com/vmware-engine/docs/known-issues#pc-name-translation-error).

## January 13, 2023

Change

Stretched private clouds are now available in the `australia-southeast1` (Sydney) Google Cloud region. Stretched private clouds enable you to stretch your vSphere/vSAN clusters across Google Cloud zones and protect against zone level failures. This functionality enables high levels of availability for business critical applications.

## December 21, 2022

Announcement

VMware Engine nodes are now available in the following additional region:

  * Milan, Italy, Europe (`europe-west8`)



## December 08, 2022

Feature

In order to support new features in the future, Google Cloud VMware Engine will convert the resource names for private clouds to a standardized format that is more consistent with Google Cloud. Specifically, this resource name translation will make minor changes to the names of resources in your project, such as:

  * Changing capital letters to lowercase
  * Changing white space to hyphens



Resource name translation is currently optional, but existing private clouds must perform a resource name translation in order to access the gcloud CLI or VMware Engine API. Resource name translation will be required after September 2023.

For more information on resource name translation, see [Resource Name Translation](https://docs.cloud.google.com/vmware-engine/docs/resource-name-translation).

## November 28, 2022

Feature

**Preview:** VMware Engine private clouds support the addition of a Trusted Platform Module (TPM) 2.0 virtual cryptoprocessor to a virtual machine. 

For details about this feature, see [About Virtual Trusted Platform Module](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-vtpm).

Announcement

Zerto Solution version 9.5u1 is now supported as a disaster recovery solution with VMware Engine. Learn more about setting up [Zerto Solution](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-disaster-recovery-zerto).

## November 17, 2022

Feature

Starting November 17, 2022, newly created private clouds will utilize IP address layout (IP Plan) version 2.0 subnet allocations. HCX addressing is now included in the management CIDR allocation, simplifying the process of starting data center VM migrations. IP Plan version 2.0 also enables additional scale and features delivered to your public cloud in upcoming releases. 

**Note:** Management appliances use different IP allocations in IP Plan version 2.0. See [Networking requirements](https://docs.cloud.google.com/vmware-engine/docs/quickstart-networking-requirements) for more information on the new subnet allocations.

Announcement

You can now use the `gcloud` command-line tool or the API to manage VMWare Engine networks, network policies, and private clouds. See the [API reference](https://docs.cloud.google.com/vmware-engine/docs/reference/rest) or the [gcloud SDK](https://docs.cloud.google.com/sdk/gcloud/reference/vmware) for more information.

Feature

Stretched private clouds are now available in the `europe-west3` (Frankfurt) region. You can use stretched private clouds to stretch vSphere/vSAN clusters across zones and protect against zone level failures. This functionality enables high levels of availability for business critical applications.

## October 06, 2022

Feature

VMware Engine adds five service subnets for newly created private clouds. Service subnets are used for appliance or service deployment scenarios, such as storage, backup, Site Recovery Manager (SRM), disaster recovery (DR), media streaming, and providing high scale linear throughput and packet processing for private clouds at any scale. 

See [Subnets](https://docs.cloud.google.com/vmware-engine/docs/concepts-vlans-subnets#service_subnets) for more information on service subnets.

## September 23, 2022

Feature

Dell PowerScale is now available for in-guest file share access for Google Cloud VMWare Engine VMs:

  * NFS and SMB shares supported
  * PowerScale file shares may be accessed across Google Cloud VMWare Engine and other Google Cloud services
  * Private connection configured via the VMware Engine UI



Learn more about [PowerScale for Google Cloud VMWare Engine](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-cloud-dell-powerscale).

## August 10, 2022

Breaking

Removed ability to create point-to-site (P2S) VPN gateways for new projects and projects that have not yet created P2S VPN gateways. Projects containing existing gateways can continue to modify those gateways. Customers can continue to use an alternative VPN solution. For details, see [Point-to-site VPN gateways](https://docs.cloud.google.com/vmware-engine/docs/concepts-vpn-gateways#point-to-site_vpn_gateways).

In March 2023, we plan to remove any remaining VPN gateways that have not been transitioned to an alternative VPN solution. If there are any questions about how to make this transition, contact [Cloud Customer Care](http://cloud.google.com/vmware-engine/docs/getting-support).

Breaking

Removed ability to create stateless firewall rules for new projects and projects that have not yet created stateless rules. Projects containing existing stateless rules can continue to modify those rules. Customers can continue to create a firewall rule set in NSX-T Gateway or NSX-T Distributed Firewall rules.

In March 2023, we plan to remove any remaining stateless rules that have not been transitioned to NSX-T Gateway or NSX-T Distributed Firewall rules. If there are any questions about how to make this transition, contact [Cloud Customer Care](http://cloud.google.com/vmware-engine/docs/getting-support).

## July 27, 2022

Change

Resource creation of named objects now enforce naming requirements that match other Google Cloud products [like Compute Engine](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format). New resources must use names that are 1-63 characters long, comply with [RFC 1035](https://www.ietf.org/rfc/rfc1035.txt), and consist of lowercase letters, digits, and hyphens. For example, "privatecloud-123".

## July 13, 2022

Announcement

VMware Engine nodes are now available in the following additional region:

  * Zurich, Switzerland, Europe (`europe-west6`)



## May 31, 2022

Feature

Private cloud creation now uses the HCX Enterprise license level by default, enabling the following premium HCX features:

  * HCX Replication Assisted vMotion (bulk, no-downtime migration)
  * Migrations from KVM and Hyper-V to vSphere
  * Traffic engineering
  * Mobility groups
  * Mobility-optimized networking



For more information about private cloud VMware components, see [Private cloud VMware components](https://docs.cloud.google.com/vmware-engine/docs/concepts-vmware-components).

## May 20, 2022

Announcement

Beginning on May 30 2022, the VMware Engine operations team will continue performing essential maintenance of the network infrastructure to improve equipment robustness and apply security patches. Users affected by this upgrade will receive an email with planned maintenance dates and times.

For details about the upgrade and steps to prepare, see [Service announcements](https://docs.cloud.google.com/vmware-engine/docs/service-announcements).

## April 29, 2022

Announcement

The VMware Engine operations team will apply important security updates to vCenter Server and NSX-T beginning early May 2022. Users affected by this upgrade will receive an email with planned maintenance dates and times.

For details about the maintenance scope and impact, see [Service announcements](https://docs.cloud.google.com/vmware-engine/docs/service-announcements).

## April 04, 2022

Feature

VMware Engine nodes are now available in the following additional zone:

  * Ashburn, Northern Virginia, North America (`us-east4-b`)



## March 25, 2022

Feature

Added ability to set the number of cores available per node in a cluster to meet your application-specific requirements during cluster creation. When you use a [custom core count](https://docs.cloud.google.com/vmware-engine/docs/concepts-private-cloud#custom-core-count), any future expansions or maintenance of that cluster will also use the custom core count.

Feature

The [public IP service](https://docs.cloud.google.com/vmware-engine/docs/networking/workload-internet-access) now supports the ICMP protocol, and default firewall rules for new projects expand the previous outbound rule to allow outbound TCP, UDP, and ICMP any.

Users with Google Cloud projects created before March 8, 2022 must contact Cloud Customer Care to enable the `allow-icmp-to-internet` firewall rule.

## February 15, 2022

Announcement

Beginning on February 21 2022, the VMware Engine operations team will perform essential maintenance of the network infrastructure to improve equipment robustness and apply security patches. Users affected by this upgrade will receive an email with planned maintenance dates and times.

For details about the upgrade and steps to prepare, see [Service announcements](https://docs.cloud.google.com/vmware-engine/docs/service-announcements).

## December 28, 2021

Announcement

VMware Engine nodes are now available in the following additional zone:

  * Sydney, Australia, APAC (`australia-southeast1-b`)



Announcement

VMware Engine nodes are now available in the following additional region:

  * Toronto, Ontario, North America (`northamerica-northeast2`)



## December 15, 2021

Feature

Added ability to forward syslog messages of a desired severity (like Error or Warning) to Cloud Logging from NSX-T. You can set up alerts and dashboards based on those messages in Google Cloud's operations suite.

For details about this feature, see [Configure a private cloud for syslog forwarding](https://docs.cloud.google.com/vmware-engine/docs/environment/howto-cloud-monitoring-standalone#configure-private-cloud-syslog).

## November 30, 2021

Feature

Added ability to create private clouds that contain a single node for testing and proofs of concept with VMware Engine.

Note that VMware Engine deletes private clouds that contain only 1 node after 60 days, and a private cloud must contain at least 3 nodes to be eligible for coverage based on the [SLA](https://cloud.google.com/vmware-engine/sla).

Change

The process of allocating an external IP address for an internal workload VM now includes the private cloud field. This field is visible when viewing IP address details and logically associates the external IP address to the private cloud that contains the workload VM.

## November 22, 2021

Announcement

As of November 4, 2021, Google Cloud VMware Engine achieves the following compliance certifications:

  * [ISO/IEC 27001](https://docs.cloud.google.com/security/compliance/iso-27001)
  * [ISO/IEC 27017](https://docs.cloud.google.com/security/compliance/iso-27017)
  * [ISO/IEC 27018](https://docs.cloud.google.com/security/compliance/iso-27018)



Announcement

Added an update to the September 22, 2021 service announcement. Continuing in December 2021, VMware Engine will upgrade the VMware stack from version 7.0 Update 1 to 7.0 Update 2 and the NSX-T stack from version 3.0 to 3.1.2. Users affected by this upgrade will receive an email with planned maintenance dates and times.

For details about the upgrade and steps to prepare, see [Service announcements](https://docs.cloud.google.com/vmware-engine/docs/service-announcements).

## November 10, 2021

Feature

VMware Engine nodes are now available in the following additional zone:

  * Frankfurt, Germany: `europe-west3-b`



## October 29, 2021

Feature

**Generally available:** VMware Engine integration with Google Cloud's operations suite using a standalone metrics and logs agent. The agent brings syslog messages and metrics from vCenter and vSAN to Google Cloud's operations suite, where you can set up your own dynamic alerts on over 50 metrics and leverage pre-built dashboards.

For details about this feature, see [Setting up Cloud Monitoring with a standalone agent](https://docs.cloud.google.com/vmware-engine/docs/environment/howto-cloud-monitoring-standalone).

## October 13, 2021

Feature

**Generally available:** vSAN data encryption for data at rest now uses keys generated by [Cloud Key Management Service](https://docs.cloud.google.com/kms) for all new private clouds.

For details about this feature, see [About vSAN encryption](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-vsan-encryption).

Feature

All new VMware Engine private clouds now deploy with VMware vSphere version 7.0 Update 2 and NSX-T version 3.1.2. Existing private clouds will be upgraded to vSphere version 7.0 Update 2 and NSX-T version 3.1.2 over a period of time in October 2021.

See [Service announcements](https://docs.cloud.google.com/vmware-engine/docs/service-announcements#2021-09-22) for more details on the contents of this upgrade.

## September 22, 2021

Announcement

Beginning in the middle of October 2021, VMware Engine will upgrade the VMware stack from version 7.0 Update 1 to 7.0 Update 2 and the NSX-T stack from version 3.0 to 3.1.2. Users affected by this upgrade will receive an email with planned maintenance dates and times.

For details about the upgrade and steps to prepare, see [Service announcements](https://docs.cloud.google.com/vmware-engine/docs/service-announcements).

## September 21, 2021

Security

Added [security bulletin](https://docs.cloud.google.com/vmware-engine/docs/security-bulletins) for the VMware Engine response to VMware security advisory VMSA-2021-0020.

## August 20, 2021

Feature

**Preview:** VMware Engine integration with Google Cloud's operations suite using a standalone metrics and logs agent. The agent brings syslog messages and metrics from vCenter and vSAN to Google Cloud's operations suite, where you can set up your own dynamic alerts on over 50 metrics and leverage pre-built dashboards.

For details about this feature, see [Setting up Cloud Monitoring with a standalone agent](https://docs.cloud.google.com/vmware-engine/docs/environment/howto-cloud-monitoring-standalone).

## July 14, 2021

Change

Changed [MTU recommendation](https://docs.cloud.google.com/vmware-engine/docs/concepts-vlans-subnets#recommended_mtu_settings) for private cloud-to-private cloud external communications to 1500 bytes.

## June 17, 2021

Feature

**Preview:** vSAN data encryption for data at rest now uses keys generated by [Cloud Key Management Service](https://docs.cloud.google.com/kms) for all new private clouds.

For details about this feature, see [Configuring vSAN encryption for your private cloud](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-vsan-encryption#default-provider).

Feature

Added autoscale policies that can automatically expand or shrink a cluster in your private cloud based on factors like CPU utilization or storage capacity thresholds. All clusters begin with a default autoscale policy that adds a node based on a storage capacity threshold.

For details about this feature, see [Autoscale policies](https://docs.cloud.google.com/vmware-engine/docs/howto-autoscale).

Breaking

Removed vCenter privilege `Host > Configuration > Storage partition configuration` for role `Cloud-Owner-Global-Role`. This prevents the mounting of iSCS or NFS storage as a datastore on your private cloud vSphere cluster. If you have any iSCSI or NFS datastore mounted on your private cloud cluster, contact Cloud Customer Care.

Change

Added vSphere content library management privileges to the [`Cloud-Global-VM-admin-group`](https://docs.cloud.google.com/vmware-engine/docs/concepts-permission-model#pre-created-vcenter-user-groups) group. With this change, a VM admin can add, delete, and read content library items.

Change

Enabled TRIM/UNMAP support on vSAN at the time of private cloud creation for more efficient vSAN storage by default. To enable this feature on existing workload VMs, you must reboot the VMs.

Change

Added the following vCenter privileges to the [`Cloud-Owner-Global-Role`](https://docs.cloud.google.com/vmware-engine/docs/concepts-permission-model#cloud-owner-global-role) role:

  * Guest operation alias modification
  * Guest operation alias query
  * Guest operation modifications
  * Guest operation program execution
  * Guest operation queries



Fixed

The **Quotas** page in the Cloud Console no longer shows VMware Engine node usage as 0 when you have an active private cloud.

## May 25, 2021

Security

Added [security bulletin](https://docs.cloud.google.com/vmware-engine/docs/security-bulletins) for the VMware Engine response to VMware security advisory VMSA-2021-0010.

## May 17, 2021

Announcement

VMware Engine nodes are now available in the following additional region:

  * Mumbai, India, APAC (`asia-south1`)



## April 09, 2021

Change

Updated the display name of VMware Engine quota entries to reflect the resource type and assignment level. Quotas available to assign for VMware Engine are as follows:

  * VMware Engine standard 72 vCPUs nodes across regions
  * VMware Engine standard 72 vCPUs nodes per region



Announcement

Added global quota limits for VMware Engine nodes so users have more flexibility in distributing resources across regions.

For details, see [Quotas and limits](https://docs.cloud.google.com/vmware-engine/quotas).

## April 01, 2021

Announcement

The Google Cloud Business Associate Agreement (BAA) now also covers Google Cloud VMware Engine. Businesses in the healthcare vertical who need HIPAA compliance can run their workloads on Google Cloud VMware Engine.

For details, see [HIPAA Compliance on Google Cloud Platform](https://docs.cloud.google.com/security/compliance/hipaa).

Change

Restructured documentation to better group content and improve workflow discoverability.

## March 25, 2021

Feature

Added support for using NetApp Cloud Volumes Service for Google Cloud. You can use cloud volumes as NFS mount points or SMB shares in your workload virtual machines. 

For details, see [Connecting workload VMs to NetApp Cloud Volumes Service](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-cloud-volumes-service).

## March 17, 2021

Announcement

VMware Engine nodes are now available in the following additional region:

  * Council Bluffs, Iowa, North America (`us-central1`)



## March 05, 2021

Security

Added [security bulletin](https://docs.cloud.google.com/vmware-engine/docs/security-bulletins) for the VMware Engine response to VMware security advisory VMSA-2021-0002.

## February 19, 2021

Announcement

Added upfront prepay option for 3-year and 1-year commitment contracts. VMware Engine provides an option to unlock up to 50% off the hourly rate savings on resources through the prepay upfront option. [Contact Sales](https://docs.cloud.google.com/contact/?form=vmwareengine) for more information.

## February 17, 2021

Feature

Added password management of the `CloudOwner@gve.local` user for vCenter and the `admin` user for NSX-T Manager. VMware Engine generates a password for these users when you deploy a private cloud. You can view and reset credentials from the private cloud details page.

Feature

Added the ability to peer multiple VPCs with private clouds in a region. This improvement enables you to establish a many-to-many relationship between your VPCs and regions.

Feature

Added support for global DNS name resolution for management components of your private cloud using Cloud DNS. You can set up Cloud DNS to resolve domain names of management components of multiple private clouds (in the same or different regions) in your project.

For more information, see [Configuring DNS for vCenter access](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-dns-on-premises).

Fixed

Added missing release notes for previous region launches of VMware Engine resources:

  * Montréal, Québec (`northamerica-northeast1`)
  * São Paulo, Brazil (`southamerica-east1`)
  * Jurong West, Singapore (`asia-southeast1`)
  * Eemshaven, Netherlands (`europe-west4`)
  * Sydney, Australia (`australia-southeast1`)
  * London, England (`europe-west2`)
  * Tokyo, Japan (`asia-northeast1`)
  * Frankfurt, Germany (`europe-west3`)



Change

Updated private cloud nodes so that the ESXi advanced parameter `fakescsireservation` and MAC learning are now enabled by default. This allows creation of a nested ESXi environment on your private cloud.

## January 22, 2021

Announcement

VMware Engine nodes are now available in the following additional region:

  * Montréal, Québec (`northamerica-northeast1`)



## December 27, 2020

Announcement

VMware Engine nodes are now available in the following additional region:

  * Osasco, São Paulo, Brazil (`southamerica-east1`)



## December 14, 2020

Announcement

All new VMware Engine private clouds now deploy with VMware vSphere version 7.0 and NSX-T version 3.0. Existing private clouds will be upgraded to vSphere version 7.0 and NSX-T version 3.0 over a period of time in December 2020 and January 2021.

See [Service announcements](https://docs.cloud.google.com/vmware-engine/docs/service-announcements#2020-nov20) for more details on the contents of this upgrade.

Change

Increased maximum number of nodes in a private cloud cluster to 32. This change applies to new clusters. Existing clusters can be expanded up to 32 nodes after the upgrade to vSphere 7.0 version.

Feature

VMware Engine now advertises routes learned from a VPC to your VMware Engine private cloud network, and advertises routes learned from your private cloud to a VPC. This allows network communication between Google Cloud resources and private cloud resources.

Feature

When VMware Engine replaces a failed node, node customizations now transfer from the failed node to the replacement node. Customizations include vSphere labels, vSphere custom attributes, vSphere tags, and any affinity and anti-affinity rules.

## November 23, 2020

Announcement

Beginning in the middle of December 2020, VMware Engine will upgrade the VMware stack from version 6.7 to 7.0 and the NSX-T stack from version 2.5 to 3.0. Users affected by this upgrade will receive an email with planned maintenance dates and times.

For details about the upgrade and steps to prepare, see [Service announcements](https://docs.cloud.google.com/vmware-engine/docs/service-announcements#2020-nov20).

## November 20, 2020

Announcement

VMware Engine nodes are now available in the following additional region:

  * Jurong West, Singapore (`asia-southeast1`)



## October 30, 2020

Announcement

VMware Engine nodes are now available in the following additional region:

  * Eemshaven, Netherlands (`europe-west4`)



## October 12, 2020

Feature

Enabled HCX private cloud to private cloud migration. You can now use HCX to migrate VMs between two private clouds.

Feature

Multi-region private cloud to private cloud connectivity is now available. Private clouds of your project in different regions can automatically route traffic between them. No additional connectivity is required to enable this routing.

Feature

End-to-end dynamic routing is now available between on-premises networks and VMware Engine regions. With this feature, your VMware Engine private clouds can learn custom or reserved-block Public IP (non RFC-1918) range networks in your VPC or on-premises dynamically.

Feature

RFC 6598 (non-private) address range support for management and workload networks is now available. With this release, you can specify non-private address ranges for management and workload networks when you create your private cloud. Those addresses will then be included for any route exchange with VPC and on-premises networks.

## October 06, 2020

Announcement

VMware Engine nodes are now available in the following additional region:

  * Sydney, Australia (`australia-southeast1`)



## September 28, 2020

Change

Committed use discounts (CUDs) are available to purchase for Google Cloud VMware Engine. CUDs provide discounted prices in exchange for your commitment to use a minimum level of resources for a specified term. With spend-based committed use discounts for VMware Engine, you can earn a deep discount off your cost of use in exchange for committing to continuously use VMware Engine nodes in a particular region for a 1- or 3-year term. See the [documentation](https://docs.cloud.google.com/vmware-engine/docs/cud) for more details.

## August 31, 2020

Announcement

VMware Engine nodes are now available in the following additional region:

  * London, England, Europe (`europe-west2`)



## August 24, 2020

Announcement

VMware Engine nodes are now available in the following additional region:

  * Tokyo, Japan (`asia-northeast1`)



## August 20, 2020

Announcement

VMware Engine nodes are now available in the following additional region:

  * Frankfurt, Germany Europe (`europe-west3`).



## June 30, 2020

Feature

[Google Cloud VMware Engine](https://docs.cloud.google.com/vmware-engine) is **generally available**. This service delivers a fully managed VMware platform stack—VMware ESXi, vCenter, vSAN, NSX-T, and HCX—in a dedicated environment on Google Cloud's infrastructure to support your enterprise production workloads. Using VMware Engine, you can bring your on-premises workloads to Google Cloud by connecting to a dedicated VMware environment.

You can run the service in the `us-east4` (Ashburn, Northern Virginia) and `us-west2` (Los Angeles, California) regions.

For more information, read the [VMware Engine documentation](https://docs.cloud.google.com/vmware-engine/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
