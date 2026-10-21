---
url: https://docs.cloud.google.com/feeds/vmware-engine-release-notes.xml
title: Google Cloud VMware Engine - Release notes
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:32:14.901479+00:00
---

# Google Cloud VMware Engine - Release notes

> Source: https://docs.cloud.google.com/feeds/vmware-engine-release-notes.xml

tag:google.com,2016:vmware-engine-release-notesGoogle Cloud VMware Engine - Release notesGoogle Cloud Platform2026-10-01T00:00:00-07:00October 01, 2026tag:google.com,2016:vmware-engine-release-notes#October_01_20262026-10-01T00:00:00-07:00Feature 

**Generally available** : Bring Your Own License (BYOL) license management for Google Cloud VMware Engine is generally available (GA). BYOL license management lets you register and manage portable VMware Cloud Foundation (VCF) license keys in the Google Cloud console across projects associated with your Cloud Billing account.

For more information, see [License management](https://docs.cloud.google.com/vmware-engine/docs/license-management).

]]> August 24, 2026tag:google.com,2016:vmware-engine-release-notes#August_24_20262026-08-24T00:00:00-07:00Announcement 

**VMware component updates:** The VMware Engine operations team is updating vCenter Server and ESXi to version 8.0 Update 3k to address security vulnerabilities described in Broadcom Security Advisory [VMSA-2026-0006](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017). For details about the update and schedule, see the [Latest service announcements](https://docs.cloud.google.com/vmware-engine/docs/service-announcements#2026-08-24).

]]> August 01, 2026tag:google.com,2016:vmware-engine-release-notes#August_01_20262026-08-01T00:00:00-07:00Feature 

**Preview** : Google Cloud VMware Engine capacity allocations are available in preview. A capacity allocation is a global reservation of physical nodes for your Cloud Billing account. Your reserved nodes are organized into placement groups (PGs), which represent the specific physical hardware and location of your reserved capacity.

Google Cloud VMware Engine capacity allocations let you do the following: * Use a capacity allocation during private cloud creation by selecting a PG. * Use a capacity allocation when adding a cluster. * Configure a hybrid private cloud across multiple PGs.

For more information, see [Manage capacity allocations](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-manage-capacity-allocations).

]]> July 08, 2026tag:google.com,2016:vmware-engine-release-notes#July_08_20262026-07-08T00:00:00-07:00Feature 

**Preview** : You can configure disaster recovery for Google Cloud VMware Engine by using JetStream. Disaster recovery options include the following:

  * Set up a Google Cloud VMware Engine private cloud as a recovery site for your on-premises VMware applications.
  * Protect workloads on a primary private cloud by using a recovery site in another Google Cloud location or on-premises environment.



For more information, see [Configure disaster recovery using JetStream](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-disaster-recovery-jetstream).

### Feature

**Generally available** : Google Cloud VMware Engine offers self-service management for [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-vsan-encryption) using the Google Cloud console and the VMware Engine API. You can enable CMEK for your private clouds, using Cloud Key Management Service (Cloud KMS) to manage encryption keys for vSAN and [vTPM](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-vtpm). Key features and considerations include:

  * You can transition between CMEK and Google-owned and Google-managed encryption keys (GMEK) as needed.
  * The "Auto-Rekey" feature integrates with Cloud KMS key rotation to perform automated key rotation for the key encryption key (KEK), maintaining security without manual intervention or service downtime.



**Limitations** : This self-service functionality is unavailable for private clouds that use CMEK through service tickets.

]]> July 07, 2026tag:google.com,2016:vmware-engine-release-notes#July_07_20262026-07-07T00:00:00-07:00Feature 

Custom organization policy constraints are generally available (GA) for Google Cloud VMware Engine. You can use custom constraints to enforce security policies and restrict configuration of your VMware Engine resources.

For more information, see [Use custom organization policies](https://docs.cloud.google.com/vmware-engine/docs/custom-constraints).

]]> June 24, 2026tag:google.com,2016:vmware-engine-release-notes#June_24_20262026-06-24T00:00:00-07:00Announcement 

**HCX upgrade to 4.11.4:** The VMware Engine operations team is initiating updates of the HCX Manager Appliance to version 4.11.4. This upgrade resolves an issue with MON-enabled segments. You are responsible for upgrading the HCX On-Prem/Connectors and Service Mesh Appliances. For more details, see the [Latest service announcements](https://docs.cloud.google.com/vmware-engine/docs/service-announcements#2026-06-24).

]]> June 11, 2026tag:google.com,2016:vmware-engine-release-notes#June_11_20262026-06-11T00:00:00-07:00Announcement 

The VMware Engine [`ve2` node type](https://docs.cloud.google.com/vmware-engine/docs/concepts/node-types) is now available in the following additional region:

  * Mexico City (`northamerica-south1`)

]]> June 01, 2026tag:google.com,2016:vmware-engine-release-notes#June_01_20262026-06-01T00:00:00-07:00Announcement 

All 3-year (36-month) post-paid `ve2` [committed use discounts (CUDs)](https://docs.cloud.google.com/vmware-engine/docs/cud) for Google Cloud VMware Engine purchased after May 31, 2026, will terminate on October 15, 2028. 3-year CUD pricing will apply, regardless of the actual term of the CUD. Additionally, 3-year pre-paid CUDs are no longer available; only 1-year pre-paid CUDs are available.

]]> May 20, 2026tag:google.com,2016:vmware-engine-release-notes#May_20_20262026-05-20T00:00:00-07:00Announcement 

All 1-year [committed use discounts (CUDs)](https://docs.cloud.google.com/vmware-engine/docs/cud) for Google Cloud VMware Engine `ve1` SKUs are now End-of-Sale across the europe-west2 (London, UK) region. You can continue to use `ve1` nodes with on-demand pricing. This change doesn't affect existing CUDs. You can also use `ve2` nodes, including `ve2` CUDs.

]]> May 15, 2026tag:google.com,2016:vmware-engine-release-notes#May_15_20262026-05-15T00:00:00-07:00Announcement 

**ve1 hardware End-of-Life (EoL) migration guide:** You can now refer to the public documentation to [migrate workloads from retiring ve1 hardware](https://docs.cloud.google.com/vmware-engine/docs/howto-migrate-ve1-hardware). First-generation `ve1` bare metal nodes are reaching the end of their useful life on a rolling basis. When your hardware is scheduled for retirement, you receive an EoL notification containing timelines and instructions to migrate your clusters.

]]> May 11, 2026tag:google.com,2016:vmware-engine-release-notes#May_11_20262026-05-11T00:00:00-07:00Feature 

You can now use Privileged Access Manager (PAM) to [delete clusters](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-manage-private-cloud#delete-cluster) in the private clouds.

]]> May 05, 2026tag:google.com,2016:vmware-engine-release-notes#May_05_20262026-05-05T00:00:00-07:00Announcement 

The VMware Engine [`ve2` node type](https://docs.cloud.google.com/vmware-engine/docs/concepts/node-types) is now available in the following additional region:

  * Eemshaven, Netherlands (`europe-west4-a`)

]]> April 27, 2026tag:google.com,2016:vmware-engine-release-notes#April_27_20262026-04-27T00:00:00-07:00Feature 

**Generally available (GA) with an allowlist:** You can now [migrate VMware management VMs](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-manage-private-cloud#migrate-vms) from their host cluster to a different cluster within the same private cloud. This feature is available to select customers through an allowlist. To migrate management VMs, you must have at least two clusters in your private cloud, and the destination cluster must be a workload cluster. This operation transitions the target workload cluster to a management cluster, and the source management cluster becomes a workload cluster.

]]> March 10, 2026tag:google.com,2016:vmware-engine-release-notes#March_10_20262026-03-10T00:00:00-07:00Feature 

**Public Preview:** You can now [migrate VMware management VMs](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-manage-private-cloud#migrate-vms) from their host cluster to a different cluster within the same private cloud. To migrate management VMs, you must have at least two clusters in your private cloud, and the destination cluster must be a workload cluster. This operation transitions the target workload cluster to a management cluster, and the source management cluster becomes a workload cluster.

]]> March 09, 2026tag:google.com,2016:vmware-engine-release-notes#March_09_20262026-03-09T00:00:00-07:00Announcement 

The VMware Engine [`ve2` node type](https://docs.cloud.google.com/vmware-engine/docs/concepts/node-types) is now available in the following additional region:

  * Los Angeles, USA, North America (`us-west2-b`)

]]> February 20, 2026tag:google.com,2016:vmware-engine-release-notes#February_20_20262026-02-20T00:00:00-08:00Announcement 

The VMware Engine [`ve2` node type](https://docs.cloud.google.com/vmware-engine/docs/concepts/node-types) is now available in the following additional region:

  * Paris, France, Europe (`europe-west9-b`)

]]> February 13, 2026tag:google.com,2016:vmware-engine-release-notes#February_13_20262026-02-13T00:00:00-08:00Announcement 

The VMware Engine [`ve2` node type](https://docs.cloud.google.com/vmware-engine/docs/concepts/node-types) is now available in the following additional region:

  * Osaka, Japan, Asia Pacific (`asia-northeast2`)

]]> January 29, 2026tag:google.com,2016:vmware-engine-release-notes#January_29_20262026-01-29T00:00:00-08:00Announcement 

Stretched private clouds capable of hosting both `ve1` and `ve2` node-family clusters are now available in the following regions:

  * Sydney, Australia, Asia Pacific (`australia-southeast1-a`, `australia-southeast1-b`)
  * Frankfurt, Germany, Europe (`europe-west3-a`, `europe-west3-b`)



While a stretched private cloud can contain mixed node families, each individual stretched cluster must be comprised of nodes from the same family type.

**Note:** To create a new stretched cluster of a different node family, contact Cloud Customer Care. ]]> January 13, 2026tag:google.com,2016:vmware-engine-release-notes#January_13_20262026-01-13T00:00:00-08:00Announcement 

Private clouds capable of hosting both `ve1` and `ve2` node-family clusters are available in the following additional regions:

  * London, England, Europe (`europe-west2-a`, `europe-west2-b`)
  * São Paulo, Brazil, South America (`southamerica-east1-a`)
  * Dallas, Texas, North America (`us-south1-b`)



While a private cloud can contain mixed node families, each individual cluster must be comprised of nodes from the same family type.

**Note:** To create a new cluster of a different node family, contact Cloud Customer Care. ]]> January 06, 2026tag:google.com,2016:vmware-engine-release-notes#January_06_20262026-01-06T00:00:00-08:00Feature 

VMware Engine introduces enhancements to simplify using external NFS datastores. External NFS datastores let you scale storage independently of compute resources for your VMware workloads. You can use Filestore or Google Cloud NetApp Volumes as external NFS datastores for ESXi hosts in Google Cloud VMware Engine. For more information, see [NFS datastores overview](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/concepts-nfs-datastores-overview).

]]> December 25, 2025tag:google.com,2016:vmware-engine-release-notes#December_25_20252025-12-25T00:00:00-08:00Announcement 

VMware Engine [`ve2` nodes](https://docs.cloud.google.com/vmware-engine/docs/concepts/node-types) are now available in the Milan, Italy (`europe-west8-b`) zone in the Milan, Italy, Europe region (`europe-west8`).

]]> December 05, 2025tag:google.com,2016:vmware-engine-release-notes#December_05_20252025-12-05T00:00:00-08:00Announcement 

VMware Engine now supports private clouds with mixed node families (`ve1` and `ve2`). While a private cloud can contain mixed node families, each cluster within that private cloud must contain nodes of the same type. This feature is available in the following regions and zones:

  * Ashburn, North America (`us-east4-a`, `us-east4-b`)
  * Iowa, North America (`us-central1-a`)
  * Montreal, North America (`northamerica-northeast1-a`)
  * Sydney, Australia (`australia-southeast1-a`, `australia-southeast1-b`)
  * Frankfurt, Europe (`europe-west3-a`, `europe-west3-b`)
  * Santiago, South America (`southamerica-west1-b`)

**Note:** To create a new cluster of a different node family, contact Cloud Customer Care. ]]> November 26, 2025tag:google.com,2016:vmware-engine-release-notes#November_26_20252025-11-26T00:00:00-08:00Announcement 

VMware Engine [`ve2` nodes](https://docs.cloud.google.com/vmware-engine/docs/concepts/node-types) are now available in the Dallas, Texas, North America region (`us-south1-b`).

]]> November 14, 2025tag:google.com,2016:vmware-engine-release-notes#November_14_20252025-11-14T00:00:00-08:00Announcement 

VMware Engine [`ve2` nodes](https://docs.cloud.google.com/vmware-engine/docs/concepts/node-types) are now available in the Tokyo, Japan region (`asia-northeast1-a`).

]]> November 04, 2025tag:google.com,2016:vmware-engine-release-notes#November_04_20252025-11-04T00:00:00-08:00Announcement 

VMware Engine [`ve2` nodes](https://docs.cloud.google.com/vmware-engine/docs/concepts/node-types) are now available in the London, England, Europe (`europe-west2-b`) zone in the London, England, Europe region (`europe-west2`).

]]> October 31, 2025tag:google.com,2016:vmware-engine-release-notes#October_31_20252025-10-31T00:00:00-07:00Announcement 

VMware Engine [`ve1` nodes](https://docs.cloud.google.com/vmware-engine/docs/concepts/node-types) are now available in the Mumbai, India (`asia-south1-b`) zone in the Mumbai region (`asia-south1`).

]]> October 03, 2025tag:google.com,2016:vmware-engine-release-notes#October_03_20252025-10-03T00:00:00-07:00Announcement 

This is to notify you about upcoming changes in licensing model with Google Cloud VMware Engine following [Broadcom's recent announcement](https://blogs.vmware.com/cloud-foundation/2025/08/29/vmware-cloud-foundation-cloud-on-your-terms/) to move to a "bring your own" subscription model for VMware Cloud Foundation (VCF).

You can renew or add additional capacity of VMware Engine nodes with VCF-license included until **October 15, 2025**. After that, Google Cloud will not be able to sell new VMware Engine VCF license-included nodes. You can buy new VMware Engine BYOL nodes and use them with "bring your own" VCF subscriptions (purchased by you from Broadcom) for new capacity after **October 15, 2025**.

For any questions, please reach out to your Google Cloud sales team, who can help review your specific scenarios, discuss the implications of these changes for your organization, and help you manage this transition.

For more details, see the [October 3, 2025](https://docs.cloud.google.com/vmware-engine/docs/service-announcements#2025-10-03) service announcement.

]]> September 26, 2025tag:google.com,2016:vmware-engine-release-notes#September_26_20252025-09-26T00:00:00-07:00Announcement 

VMware Engine `ve2` nodes are now available in the following additional region:

  * Doha, Qatar (`me-central1`, `v-zone-a`)

]]> September 24, 2025tag:google.com,2016:vmware-engine-release-notes#September_24_20252025-09-24T00:00:00-07:00Announcement 

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

]]> September 15, 2025tag:google.com,2016:vmware-engine-release-notes#September_15_20252025-09-15T00:00:00-07:00Announcement 

VMware Engine `ve2` nodes are now available in the following additional region and zone:

  * The Milan, Italy, Europe region (`europe-west8-a`).
  * The Melbourne, Australia (`australia-southeast2-b`) zone in the Melbourne, Australia region (`australia-southeast2`).

]]>
