---
url: https://docs.cloud.google.com/filestore/docs/release-notes/
title: Filestore release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:32.782364+00:00
---

# Filestore release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Resources ](https://docs.cloud.google.com/filestore/docs/resources)



Send feedback 

#  Filestore release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Filestore. You can periodically check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/filestore-release-notes.xml) directly. 

## September 16, 2026

Feature

Small capacity Filestore instances for the Regional service tier are [generally available (GA)](https://cloud.google.com/products#product-launch-stages). Small capacity instances start at 100 GiB and scale in 1 GiB increments, providing an option for development, testing, and applications with low traffic or basic storage needs.

For more information, see [Small capacity instances](https://docs.cloud.google.com/filestore/docs/service-tiers#small-instances).

Feature

Filestore agent volumes provide managed, high-density elastic NFS storage backed by regional volume pools for stateful AI agent sandboxes, autonomous agent fleets, and multi-agent developer environments.

The Filestore agent volumes feature is available to all Google Cloud customers for evaluation and non-production use. To request access for your Google Cloud project, submit the Filestore agent volumes [access request form](https://forms.gle/vYPkcFiZVoTjf7Ah7). Production support is offered on an allow list basis under a limited [General Availability (GA)](https://cloud.google.com/products#product-launch-stages) program. To check your eligibility or to request production support, use the access form.

For more information, see [About Filestore agent volumes](https://docs.cloud.google.com/filestore/docs/agent-volumes-overview).

## June 02, 2026

Feature

You can configure your Filestore instances to use Private Service Connect with NFSv3 or NFSv4.1 file system protocols and IPv4 or IPv6 address families to allow consumers access managed services privately from inside their VPC network. This feature is [generally available](https://cloud.google.com/products#product-launch-stages).

For more information, see [Create a Filestore instance with Private Service Connect](https://docs.cloud.google.com/filestore/docs/configure-psc).

## June 01, 2026

Feature

The [Filestore remote Model Context Protocol (MCP) server](https://docs.cloud.google.com/filestore/docs/use-filestore-mcp) is [generally available (GA)](https://cloud.google.com/products#product-launch-stages). The Filestore remote MCP server lets you create and manage Filestore instances from LLMs, AI applications, and AI-enabled development platforms.

## April 13, 2026

Feature

You can use [Filestore CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/filestore-csi-driver) to dynamically scale custom performance for zonal and regional Filestore instances.

For more information, see [Dynamically scale Filestore performance using VolumeAttributesClass](https://docs.cloud.google.com/filestore/docs/csi-driver#custom-performance).

## April 09, 2026

Feature

Filestore is integrated with [Backup and Disaster Recovery (DR) Service](https://docs.cloud.google.com/backup-disaster-recovery/docs) allowing you to centrally manage your backups with advanced features for data protection. This feature is [generally available](https://cloud.google.com/products#product-launch-stages) for Filestore instances.

For more information, see [Backups overview](https://docs.cloud.google.com/filestore/docs/backups).

## January 20, 2026

Feature

Filestore is available in `asia-southeast3` (Bangkok). For more information, see [Filestore regions and zones](https://docs.cloud.google.com/filestore/docs/regions).

## October 20, 2025

Feature

You can now create regional Filestore instances starting at 100 GiB and scale them in 1 GiB units. The small instances feature is available under Restricted GA in `us-central1` and `us-east4` regions. For more information, see [Small capacity Filestore instances](https://cloud.google.com/filestore/docs/service-tiers#small-instances).

## September 25, 2025

Feature

You can now use the [Filestore CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/filestore-csi-driver) to create Filestore regional instances. For more information, see [Access Filestore instances with the Filestore CSI driver](https://cloud.google.com/filestore/docs/csi-driver).

## June 04, 2025

Feature

The [promoteReplica API](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.instances/promoteReplica) is available for promoting replicas to regular instances. For more information, see [About instance replication](https://docs.cloud.google.com/filestore/docs/instance-replication).

## May 27, 2025

Feature

You can now use the [Filestore CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/filestore-csi-driver) to create Filestore instances with the NFSv4.1 protocol from the Google Kubernetes Engine (GKE) cluster. This feature is available for zonal, regional, and enterprise [service tiers](https://docs.cloud.google.com/filestore/docs/service-tiers).

## April 28, 2025

Feature

[Custom performance](https://docs.cloud.google.com/filestore/docs/custom-performance) is now [generally available](https://cloud.google.com/products#product-launch-stages) for Filestore instances.

## April 17, 2025

Feature

You can now use custom constraints with Organization Policy to provide more granular control over specific fields for some Filestore resources. For more information, see [Creating custom constraints for Filestore](https://docs.cloud.google.com/filestore/docs/create-custom-constraints).

## April 07, 2025

Feature

The [basic HDD extended range tier](https://docs.cloud.google.com/filestore/docs/service-tiers) is now [generally available](https://cloud.google.com/products#product-launch-stages) to all GKE customers through the [Filestore CSI driver](https://docs.cloud.google.com/filestore/docs/csi-driver).

## March 28, 2025

Feature

[Instance replication](https://docs.cloud.google.com/filestore/docs/instance-replication) is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## November 18, 2024

Feature

Filestore is now available in Mexico ([`northamerica-south1`](https://docs.cloud.google.com/filestore/docs/regions) region).

## October 07, 2024

Feature

[Deletion protection](https://docs.cloud.google.com/filestore/docs/deletion-protection) is now [generally available](https://cloud.google.com/products#product-launch-stages) for Filestore instances.

## September 30, 2024

Feature

[NFSv4.1 protocol](https://docs.cloud.google.com/filestore/docs/about-supported-protocols) support, integrated with Managed Service for Microsoft Active Directory, is now generally available for zonal, regional, and enterprise instances.

## August 19, 2024

Change

Access Transparency supports Filestore in GA stage. For more information, see [Access Transparency supported services](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/supported-services).

## June 04, 2024

Change

Filestore instances no longer require reserved capacity for certain internal operations. For more information, see [Monitoring instances](https://docs.cloud.google.com/filestore/docs/monitoring-instances#anticipating-capacity).

## May 23, 2024

Feature

The [regional service tier](https://docs.cloud.google.com/filestore/docs/service-tiers) is now [generally available](https://cloud.google.com/products#product-launch-stages).

## May 02, 2024

Feature

You can now [revert an instance to a snapshot state](https://docs.cloud.google.com/filestore/docs/revert-snapshot). This feature is [generally available](http://cloud.google.com/products#product-launch-stages) for instances created in the zonal and enterprise service tiers.

Change

Filestore supports [IP-based access control for your volumes](https://docs.cloud.google.com/filestore/docs/csi-driver#ipacl). You can now use the Filestore CSI driver to configure IP-based access control at volume creation.

## March 28, 2024

Change

You can use [CMEK organization policies](https://docs.cloud.google.com/filestore/docs/cmek-organization-policy) to manage key usage with your new Filestore resources. This feature is now [generally available](https://cloud.google.com/products#product-launch-stages).

## February 22, 2024

Feature

[NFSv4.1 protocol support](https://docs.cloud.google.com/filestore/docs/protocols), integrated with [Managed Service for Microsoft Active Directory](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview), is now available in [Preview](https://cloud.google.com/products#product-launch-stages) for Filestore [enterprise and zonal](https://docs.cloud.google.com/filestore/docs/service-tiers) instances.

## February 13, 2024

Feature

Filestore is now available in Johannesburg, South Africa ([`africa-south1`](https://docs.cloud.google.com/filestore/docs/regions) region).

## January 16, 2024

Feature

Zonal tier [backups](https://docs.cloud.google.com/filestore/docs/backups) are now [generally available](https://cloud.google.com/products#product-launch-stages).

## November 02, 2023

Change

The [zonal service tier](https://docs.cloud.google.com/filestore/docs/service-tiers) is now [generally available](https://cloud.google.com/products#product-launch-stages).

## October 23, 2023

Change

Filestore is now available in Berlin (`europe-west10` [region](https://docs.cloud.google.com/filestore/docs/regions)).

## October 16, 2023

Feature

[Filestore enterprise singleshare backups for GKE](https://docs.cloud.google.com/filestore/docs/backup-persistent-storage-gke) are now [generally available](https://cloud.google.com/products#product-launch-stages).

## October 02, 2023

Feature

Filestore [enterprise tier](https://docs.cloud.google.com/filestore/docs/service-tiers) [backups](https://docs.cloud.google.com/filestore/docs/backups) are now [generally available](https://cloud.google.com/products#product-launch-stages).

## September 25, 2023

Change

Filestore is now available in Dammam (`me-central2` [region](https://docs.cloud.google.com/filestore/docs/regions)).

## August 10, 2023

Feature

The [zonal service tier](https://docs.cloud.google.com/filestore/docs/service-tiers) with options for a higher or lower capacity band is now available in [Preview](https://cloud.google.com/products#product-launch-stages).

## July 27, 2023

Change

[Filestore multishares for GKE](https://docs.cloud.google.com/filestore/docs/multishares) now supports up to 80 shares per instance ([GA](https://cloud.google.com/products#product-launch-stages)).

## June 30, 2023

Feature

Support for [revert snapshot](https://docs.cloud.google.com/filestore/docs/create-snapshots#revert_file_share_to_a_snapshot_state) operations is now available for [high scale SSD instances](https://docs.cloud.google.com/filestore/docs/service-tiers) ([Preview](https://cloud.google.com/products#product-launch-stages)).

## May 22, 2023

Feature

[Cloud EKM support for Filestore](https://docs.cloud.google.com/filestore/docs/cmek) is now [generally available](https://cloud.google.com/products#product-launch-stages).

## April 24, 2023

Feature

Filestore is now available in Doha (`me-central1` [region](https://docs.cloud.google.com/filestore/docs/regions)).

Filestore is now available in Turin (`europe-west12` [region](https://docs.cloud.google.com/filestore/docs/regions)).

## April 17, 2023

Feature

[Support for Filestore as an NFS datastore for Google Cloud VMware Engine (GCVE)](https://docs.cloud.google.com/filestore/docs/gcve-datastores) is now [generally available](https://cloud.google.com/products#product-launch-stages).

## April 13, 2023

Feature

[High Scale tier snapshots](https://docs.cloud.google.com/filestore/docs/create-snapshots) are now [generally available](https://cloud.google.com/products#product-launch-stages).

## March 13, 2023

Feature

[Filestore instance support for non-RFC 1918 IP addresses](https://docs.cloud.google.com/filestore/docs/creating-instances#configuring_a_reserved_ip_address_range) is now [generally available](https://cloud.google.com/products#product-launch-stages).

## March 10, 2023

Feature

[Support for Filestore as an NFS datastore for Google Cloud VMware Engine (GCVE)](https://docs.cloud.google.com/filestore/docs/gcve-datastores) is now available in [Preview](https://cloud.google.com/products#product-launch-stages).

## March 06, 2023

Feature

Filestore data is compliant with at-rest and in-use [data residency requirements](https://cloud.google.com/terms/data-residency) pursuant with Google Cloud terms of service.

## February 28, 2023

Feature

High Scale and Enterprise tier instances now support [overlapping permissions](https://docs.cloud.google.com/filestore/docs/access-control#overlapping-permissions) ([GA](https://cloud.google.com/products#product-launch-stages)).

## November 23, 2022

Announcement

[Filestore (Basic HDD and Basic SSD tiers)](https://docs.cloud.google.com/filestore/docs/service-tiers) are now in compliance with the [FedRAMP Moderate](https://docs.cloud.google.com/security/compliance/fedramp) standard.

## November 16, 2022

Feature

[Filestore Backups for High Scale and Enterprise](https://docs.cloud.google.com/filestore/docs/backups) tier instances is available in [Preview](https://cloud.google.com/products#product-launch-stages).

Feature

[Filestore Multishares for GKE](https://docs.cloud.google.com/filestore/docs/multishares) is now [generally available](https://cloud.google.com/products#product-launch-stages).

## October 27, 2022

Feature

Filestore is now available in Columbus (`us-east5` [region](https://docs.cloud.google.com/filestore/docs/regions)).

Filestore is now available in Dallas (`us-south1` [region](https://docs.cloud.google.com/filestore/docs/regions)).

Filestore is now available in Tel Aviv (`me-west1` [region](https://docs.cloud.google.com/filestore/docs/regions)).

## September 29, 2022

Change

Filestore High Scale and Enterprise tier instances now support IP address allocations with the /26 prefix.

## August 29, 2022

Feature

Filestore is now available in Madrid, Spain (`europe-southwest1` [region](https://docs.cloud.google.com/filestore/docs/regions)).

Feature

Filestore is now available in Milan, Italy (`europe-west8` [region](https://docs.cloud.google.com/filestore/docs/regions)).

Feature

Filestore is now available in Paris, France (`europe-west9` [region](https://docs.cloud.google.com/filestore/docs/regions)).

## July 22, 2022

Feature

[**Preview**](https://cloud.google.com/products#product-launch-stages): Filestore Multishares for GKE provides a file service option for GKE users that require multiple, smaller NFS-mounted Persistent Volumes from a single Filestore instance.

Each Persistent Volume can start with just 100GiB of storage, providing a more cost-efficient option for customers. 

For more information, see [Filestore Multishares for GKE](https://docs.cloud.google.com/filestore/docs/multishares).

## June 30, 2022

Feature

[Filestore High Scale SSD tier](https://docs.cloud.google.com/filestore/docs/high-scale) is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## April 21, 2022

Feature

Filestore is now available in Santiago, Chile (`southamerica-west1` [region](https://docs.cloud.google.com/filestore/docs/regions)) for Basic HDD and Basic SSD instances.

## April 11, 2022

Feature

You can now use [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/filestore/docs/cmek) to protect data at rest in Filestore's High Scale SSD Tier instances. 

  * High Scale SSD instances stop and restart automatically when the state of an associated key changes
  * This feature is currently in [Preview](https://cloud.google.com/products/#product-launch-stages)



## December 16, 2021

Feature

The following Filestore features are now [generally available](https://cloud.google.com/products/#product-launch-stages) (GA):

  * Enterprise tier
  * Customer-managed encryption key support
  * Snapshots
  * Private services access support



Feature

Filestore snapshots now support [reverting to a snapshot](https://docs.cloud.google.com/filestore/docs/create-snapshots#revert_file_share_to_a_snapshot_state).

## October 05, 2021

Announcement

You can now get support for preview features for Filestore. For details see the [Support](https://docs.cloud.google.com/filestore/docs/getting-support) page.

## September 30, 2021

Feature

Filestore's Enterprise tier now supports snapshots. A snapshot is a preserved state of your file share data that can be used to restore data. For more information, see the [snapshots documentation page](https://docs.cloud.google.com/filestore/docs/snapshots).

Feature

You can now use Customer-Managed Encryption Keys (CMEK) to protect all data at rest in Filestore's Enterprise tier instances. CMEK in Filestore is a [preview](https://cloud.google.com/products/#product-launch-stages) feature. For more information, see [Encrypt data with customer-managed encryption keys](https://docs.cloud.google.com/filestore/docs/cmek).

## August 03, 2021

Feature

Filestore is available in the northamerica-northeast2 (Toronto) region. See [Regions and zones](https://docs.cloud.google.com/filestore/docs/regions).

## August 02, 2021

Feature

Filestore now has a new [Enterprise tier](https://docs.cloud.google.com/filestore/docs/enterprise), which lets you create 1–10 TiB regional instances that can scale up and down with your storage needs.

Feature

Filestore now supports [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access), which lets you [create instances on a Shared VPC network in service projects](https://docs.cloud.google.com/filestore/docs/shared-vpc).

## June 29, 2021

Feature

Filestore is available in the europe-central2 (Warsaw) region. See [Regions and zones](https://docs.cloud.google.com/filestore/docs/regions).

Feature

Filestore is now available in Delhi (`asia-south2` [region](https://docs.cloud.google.com/filestore/docs/regions)).

## June 25, 2021

Feature

You can now secure your Filestore instances using a VPC service perimeter. For details, see [Securing instances with a service perimeter](https://docs.cloud.google.com/filestore/docs/vpc-sc).

## June 21, 2021

Feature

Filestore is now available in Melbourne (`australia-southeast2` [region](https://docs.cloud.google.com/filestore/docs/regions)).

## March 15, 2021

Feature

Filestore is available in the `europe-central2` (Warsaw) region. See [Regions and zones](https://docs.cloud.google.com/filestore/docs/regions).

## December 22, 2020

Announcement

IP-based access control is now generally available.

## November 18, 2020

Feature

Filestore now supports access over VPN. You can mount Filestore file shares on an on-premises client and clients on a remote [VPC](https://docs.cloud.google.com/vpc/docs/vpc) with this new capability. To learn how to set up a VPN connection with Cloud VPN, see [Creating an HA VPN gateway to a Peer VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn).

## September 25, 2020

Feature

[Filestore backups](https://docs.cloud.google.com/filestore/docs/backups) has launched to beta. Now you can [back up your Filestore instances](https://docs.cloud.google.com/filestore/docs/backup-restore).

## September 01, 2020

Feature

Filestore [Troubleshooting](https://docs.cloud.google.com/filestore/docs/troubleshooting) page published. Now you can troubleshoot common Filestore issues.

## June 08, 2020

Feature

[**High Scale SSD**](https://docs.cloud.google.com/filestore/docs/high-scale) tier released to beta. This new service tier for Filestore provides greater performance and lets you grow and shrink capacity between 60–320 TB.

Feature

[**IP-based access control**](https://docs.cloud.google.com/filestore/docs/creating-instances#configuring_ip-based_access_control) released to beta. This feature lets you control access to file shares by the IP addresses of clients.

Feature

Filestore is available in the `asia-southeast2` (Jakarta) region. See [Regions and zones](https://docs.cloud.google.com/filestore/docs/regions).

Change

Filestore service tier name change:

  * **Standard** tier is now called **Basic HDD**.
  * **Premium** tier is now called **Basic SSD**.
  * You can still use the old tier names and they continue to be supported.



This change may affect you if you use:  
* The `gcloud beta filestore` command-line tool (beta). * The Filestore beta API (v1beta1). * The Cloud Console with the Filestore API. * The Cloud Console with the `gcloud` tool.

For details, see [New service tier names](https://docs.cloud.google.com/filestore/docs/high-scale#new_service_tier_names).

## May 19, 2020

Feature

Learn how to create [low disk space alerts](https://docs.cloud.google.com/filestore/docs/monitoring-instances) for your Filestore instances.

## April 20, 2020

Feature

Filestore is available in the `us-west4` (Las Vegas) region. See [Regions and zones](https://docs.cloud.google.com/filestore/docs/regions).

## January 24, 2020

Feature

Cloud Filestore is now available in the Seoul (`asia-northeast3`) [region](https://docs.cloud.google.com/filestore/docs/regions).

## April 08, 2019

Feature

GA release of Cloud Filestore

  * Cloud Filestore is now generally available for use.



## July 12, 2018

Feature

Beta release of Cloud Filestore

  * The Beta version of Cloud Filestore is now available for use.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
