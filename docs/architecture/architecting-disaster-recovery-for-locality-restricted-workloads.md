---
url: https://docs.cloud.google.com/architecture/architecting-disaster-recovery-for-locality-restricted-workloads/
title: Architecting disaster recovery for locality-restricted workloads \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:32:22.868566+00:00
---

# Architecting disaster recovery for locality-restricted workloads  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/architecting-disaster-recovery-for-locality-restricted-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Architecting disaster recovery for locality-restricted workloads Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-07-20 UTC

This document discusses how you can use Google Cloud to architect for disaster recovery (DR) to meet location-specific requirements. For some regulated industries, workloads must adhere to these requirements. In this scenario, one or more of the following requirements apply:

  * Data at rest must be restricted to a specified location.
  * Data must be processed in the location where it resides.
  * Workloads are accessible only from predefined locations.
  * Data must be encrypted by using keys that the customer manages.
  * If you are using cloud services, each cloud service must provide a minimum of two locations that are redundant to each other. For an example of location redundancy requirements, see the [Cloud Computing Compliance Criteria Catalogue (C5)](https://cloud.google.com/security/compliance/bsi-c5).



The series consists of these parts:

  * [Disaster recovery planning guide](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide)
  * [Disaster recovery building blocks](https://docs.cloud.google.com/architecture/dr-scenarios-building-blocks)
  * [Disaster recovery scenarios for data](https://docs.cloud.google.com/architecture/dr-scenarios-for-data)
  * [Disaster recovery scenarios for applications](https://docs.cloud.google.com/architecture/dr-scenarios-for-applications)
  * Architecting disaster recovery for locality-restricted workloads (this document)
  * [Disaster recovery use cases: locality-restricted data analytic applications](https://docs.cloud.google.com/architecture/dr-scenarios-locality-restricted-data-analytics)
  * [Architecting disaster recovery for cloud infrastructure outages](https://docs.cloud.google.com/solutions/disaster-recovery/architecture)



## Terminology

Before you begin architecting for DR for locality-restricted workloads, it's a good idea to review locality terminology used in Google Cloud.

Google Cloud provides services in [_regions_](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) throughout the Americas, Europe and the Middle East, and Asia Pacific. For example, London (`europe-west2`) is a region in Europe, and Oregon (`us-west1`) is a region in North America. Some Google Cloud products group multiple regions into a specific [_multi-region_](https://cloud.google.com/about/locations/#multi-region) location which is accessible in the same way that you would use a region.

[Regions are further divided into _zones_](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) where you deploy certain Google Cloud _resources_ such as virtual machines, Kubernetes clusters, or Cloud SQL databases. [Resources](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) on Google Cloud are multi-regional, regional, or zonal. Some resources and products that are by default designated as [multi-regional](https://docs.cloud.google.com/docs/geography-and-regions#multiregional_resources) can also be restricted to a region. The different types of resources are explained as follows:

  * Multi-regional resources are designed by Google Cloud to be redundant and distributed in and across regions. Multi-regional resources are resilient to the failure of a single region.
  * Regional resources are redundantly deployed across multiple zones in a region, and are resilient to the failure of a zone within the region.

**Note:** For more information about region-specific considerations, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). 
  * Zonal resources operate in a single zone. If a zone becomes unavailable, all zonal resources in that zone are unavailable until service is restored. Consider a zone as a single-failure domain. You need to architect your applications to mitigate the effects of a single zone becoming unavailable.




For more information, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions).

## Planning for DR for locality-restricted workloads

The approach you take to designing your application depends on the type of workload and the locality requirements you must meet. Also consider why you must meet those requirements because what you decide directly influences your DR architecture.

Start by reading the [Google Cloud disaster recovery planning guide](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide). And as you consider locality-restricted workloads, focus on the requirements discussed in this planning section.

### Define your locality requirements

Before you start your design, define your locality requirements by answering these questions:

  * **Where is the data at rest?** The answer dictates what services you can use and the high availability (HA) and DR methods you can employ to achieve your RTO/RPO values. Use the [Cloud locations](https://cloud.google.com/about/locations) page to determine what products are in scope.
  * **Can you use encryption techniques to mitigate the requirement?** If you are able to mitigate locality requirements by employing encryption techniques using Cloud External Key Manager and Cloud Key Management Service, you can use multi-regional and dual-regional services and follow the standard HA/DR techniques outlined in [Disaster recovery scenarios for data](https://docs.cloud.google.com/architecture/dr-scenarios-for-data).
  * **Can data be processed outside of where it rests?** You can use products such as [Google Distributed Cloud](https://docs.cloud.google.com/distributed-cloud/docs) to help create a hybrid environment to address your requirements or implement product-specific controls such as load-balancing Compute Engine instances across [multiple zones](https://docs.cloud.google.com/compute/docs/regions-zones#choosing_a_region_and_zone) in a region. Use the Organization policy [Resource Location constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) to restrict where resources can be deployed .

If data can be processed outside of where it needs to be at rest, you can design the "processing" parts of your application by following the guidance in [Disaster recovery building blocks](https://docs.cloud.google.com/architecture/dr-scenarios-building-blocks) and [Disaster recovery scenarios for applications](https://docs.cloud.google.com/architecture/dr-scenarios-for-applications).

Configure a VPC Security Controls perimeter to control who can access the data and to restrict what resources can process the data.

  * **Can you use more than one region?** If you can use more than one region, you can use many of the techniques outlined in the Disaster Recovery series. Check the [multi-region](https://cloud.google.com/about/locations#multi-region) and region constraints for Google Cloud products.

  * **Do you need to restrict who can access your application?** Google Cloud has several products and features that help you restrict who can access your applications:

    * [Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap/docs/concepts-overview). Verifies a user's identity and then determines whether that user should be permitted to access an application. Organization policy uses the [domain-restricted sharing](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) constraint to define the allowed Cloud Identity or Google Workspace IDs that are permitted in Identity and Access Management (IAM) policies.
    * Product-specific locality controls. Refer to each product you want to use in your architecture for appropriate locality constraints. For example, if you're using Cloud Storage, create buckets in specified regions.



### Identify the services that you can use

Identify what services can be used based on your locality and regional granularity requirements. Designing applications that are subject to locality restrictions requires understanding what products can be restricted to what region and what controls can be applied to enforce location restriction requirements.

### Identify the regional granularity for your application and data

Identify the regional granularity for your application and data by answering these questions:

  * **Can you use multi-regional services in your design?** By using multi-regional services, you can create highly available resilient architectures.
  * **Does access to your application have location restrictions?** Use these Google Cloud products to help enforce where your applications can be accessed from: 
    * [Google Cloud Armor](https://docs.cloud.google.com/armor). Lets you implement IP and geo-based constraints.
    * [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview). Provides context-based perimeter security.
  * **Is your data at rest restricted to a specific region?** If you use managed services, ensure that the services you are using can be configured so that your data stored in the service is restricted to a specific region. For example, use BigQuery [locality restrictions](https://docs.cloud.google.com/bigquery/docs/locations#multi-regional_locations) to dictate where your datasets are stored and backed up to.
  * **What regions do you need to restrict your application to?** Some Google Cloud products do not have regional restrictions. Use the [Cloud locations](https://cloud.google.com/about/locations) page and the product-specific pages to validate what regions you can use the product in and what mitigating features if any are available to restrict your application to a specific region.



## Meeting locality restrictions using Google Cloud products

This section details features and mitigating techniques for using Google Cloud products as part of your DR strategy for locality-restricted workloads. We recommend reading this section along with [Disaster recovery building blocks](https://docs.cloud.google.com/architecture/dr-scenarios-building-blocks).

### Organization policies

The [Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) gives you centralized control over your Google Cloud resources. Using organization policies, you can configure restrictions across your entire [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). Consider the following [policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) when architecting for locality-restricted workloads:

  * [Domain-restricted sharing](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains): By default, all user identities are allowed to be added to IAM policies. The `allowed_values` list must specify one or more Cloud Identity or Google Workspace customer identities. If this constraint is active, only identities in the allowed list are eligible to be added to IAM policies.

  * [Location-restricted resources](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations): This constraint refers to the set of locations where location-based Google Cloud resources can be created. Policies for this constraint can specify as allowed or denied locations any of the following: multi-regions such as Asia and Europe, regions such as `us-east1` or `europe-west1`, or individual zones such as `europe-west1-b`. For a list of supported services, see [Resource locations supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations-supported-services).




### Encryption

If your data locality requirements concern restricting who can access the data, then implementing encryption methods might be an applicable strategy. By using external key management systems to manage keys that you supply outside of Google Cloud, you might be able to deploy a multi-region architecture to meet your locality requirements. Without the keys available, the data cannot be decrypted.

Google Cloud has two products that let you use keys that you manage:

  * [Cloud External Key Manager (Cloud EKM)](https://docs.cloud.google.com/kms/docs/ekm): Cloud EKM lets you encrypt data in BigQuery and Compute Engine with encryption keys that are stored and managed in a third-party key management system that's deployed outside Google's infrastructure.
  * [Customer-supplied encryption keys](https://cloud.google.com/security/encryption/customer-supplied-encryption-keys) (CSEK): You can use CSEK with [Cloud Storage](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys) and [Compute Engine](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption). Google uses your key to protect the Google-generated keys that are used to encrypt and decrypt your data.

If you provide a customer-supplied encryption key, Google does not permanently store your key on Google's servers or otherwise manage your key. Instead, you provide your key for each operation, and your key is purged from Google's servers after the operation is complete.




When managing your own key infrastructure, you must carefully consider latency and reliability issues and ensure that you implement appropriate HA and recovery processes for your external key manager. You must also understand your RTO requirements. The keys are integral to writing the data, so RPO isn't the critical concern because no data can be safely written without the keys. The real concern is RTO because without your keys you cannot unencrypt or safely write data.

### Storage

When architecting DR for locality-restricted workloads, you must ensure that data at rest is located in the region you require. You can configure Google Cloud object and file store services to meet your requirements

#### Cloud Storage

You can create Cloud Storage buckets that meet [locality restrictions](https://docs.cloud.google.com/storage/docs/locations#available-locations).

Beyond the features discussed in the Cloud Storage section of the Disaster Recovery Building Blocks article, when you architect for DR for locality-restricted workloads, consider whether [redundancy across regions](https://docs.cloud.google.com/storage/docs/availability-durability#cross-region-redundancy) is a requirement: objects stored in [multi-regions](https://docs.cloud.google.com/storage/docs/bucket-locations#location-mr) and [dual-regions](https://docs.cloud.google.com/storage/docs/bucket-locations#location-dr) are stored in at least two geographically separate areas, regardless of their storage class. This redundancy ensures maximum availability of your data, even during large-scale disruptions, such as natural disasters. Dual-regions achieve this redundancy by using a pair of regions that you choose. Multi-regions achieve this redundancy by using any combination of data centers in the specified multi-region, which might include data centers that are not [explicitly listed as available regions](https://docs.cloud.google.com/storage/docs/bucket-locations#location-r).

Data synchronization between the buckets occurs asynchronously. If you need a high degree of confidence that the data has been written to an alternative region to meet your RTO and RPO values, one strategy is to use two single-region buckets. You can then either dual-write the object or write to one bucket and have Cloud Storage [copy](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/rewrite) it to the second bucket.

#### Single-region mitigation strategies when using Cloud Storage

If your requirements restrict you to using a single region, then you can't implement an architecture that is redundant across geographic locations using Google Cloud alone. In this scenario, consider using one or more of the following techniques:

  * Adopt a multi-cloud or hybrid strategy. This approach lets you choose another cloud or on-premises solution in the same geographic area as your Google Cloud region. You can store copies of your data in Cloud Storage buckets on-premises, or alternatively, use Cloud Storage as the target for your backup data.

To use this approach, do the following:

    * Ensure that distance requirements are met.
    * If you are using AWS as your other cloud provider, refer to the [Cloud Storage interoperability](https://docs.cloud.google.com/storage/docs/interoperability) guide for how to configure access to Amazon S3 using Google Cloud tools.
    * For other clouds and on-premises solutions, consider open source solutions such as [minIO](https://min.io/) and [Ceph](https://github.com/ceph/ceph) to provide an on-premises object store.
    * Consider using Managed Service for Apache Airflow with the `gcloud storage` command-line utility to transfer data from an on-premises object store to Cloud Storage.
    * Use the [Transfer service for on-premises data](https://docs.cloud.google.com/storage-transfer/docs/on-prem-overview) to copy data stored on-premises to Cloud Storage.
  * Implement encryption techniques. If your locality requirements permit using encryption techniques as a workaround, you can then use multi-region or dual-region buckets.




#### Filestore

[Filestore](https://docs.cloud.google.com/filestore/docs) provides managed file storage that you can deploy in [regions and zones](https://docs.cloud.google.com/filestore/docs/regions) according to your locality restriction requirements.

### Managed databases

[Disaster recovery scenarios for data](https://docs.cloud.google.com/architecture/dr-scenarios-for-data) describes methods for implementing backup and recovery strategies for Google Cloud [managed database services](https://docs.cloud.google.com/architecture/dr-scenarios-for-data#managed-database-services-on-gcp). In addition to using these methods, you must also consider locality restrictions for each managed database service that you use in your architecture—for example:

  * Bigtable is available in zonal locations in a region. Production instances have a minimum of two clusters, which must be in unique zones in the region. [Replication](https://docs.cloud.google.com/bigtable/docs/replication-overview#how-it-works) between clusters in a Bigtable instance is automatically managed by Google. Bigtable synchronizes your data between the clusters, creating a separate, independent copy of your data in each zone where your instance has a cluster. Replication makes it possible for incoming traffic to [fail over](https://docs.cloud.google.com/bigtable/docs/failovers) to another cluster in the same instance.

  * BigQuery has [locality restrictions](https://docs.cloud.google.com/bigquery/docs/locations#multi-regional_locations) that dictate where your datasets are stored. Dataset locations can be regional or multi-regional. To provide resilience during a regional disaster, you need to back up data to another geographic location. In the case of BigQuery multi-regions, we recommend that you avoid backing up to regions within the scope of the multi-region. If you select the EU multi-region, you exclude Zürich and London from being part of the multi-region configuration. For guidance on implementing a DR solution for BigQuery that addresses the unlikely event of a physical regional loss, see [Loss of region](https://docs.cloud.google.com/bigquery/docs/reliability-intro#scenario_loss_of_region).

To understand the implications of adopting single-region or multi-region BigQuery configurations, see the [BigQuery documentation](https://docs.cloud.google.com/bigquery/docs/availability).

  * You can use [Firestore](https://docs.cloud.google.com/firestore/docs) to store your Firestore data in either a multi-region location or a regional location. Data in a multi-region location operates in a [multi-zone and multi-region replicated configuration](https://docs.cloud.google.com/docs/geography-and-regions#multi-regional_resources). Select a multi-region location if your locality restriction requirements permit it and you want to maximize the availability and durability of your database. multi-region locations can withstand loss of entire regions and maintain availability without data loss. Data in a [regional location ](https://docs.cloud.google.com/firestore/docs/locations#location-r)operates in a [multi-zone replicated configuration](https://docs.cloud.google.com/docs/geography-and-regions#regional_resources).

  * You can configure Cloud SQL for [high availability](https://docs.cloud.google.com/sql/docs/mysql/high-availability). A Cloud SQL instance configured for HA is also called a regional instance and is located in a primary and secondary zone in the configured region. In a regional instance, the configuration is made up of a primary instance and a standby instance. Ensure that you understand the [typical failover time](https://docs.cloud.google.com/sql/docs/mysql/high-availability#applications-and-instances) from the primary to the standby instance.

If your requirements permit, you can configure Cloud SQL with [cross-region replicas](https://docs.cloud.google.com/sql/docs/mysql/replication/cross-region-replicas). If a disaster occurs, the read replica in a different region can be [promoted](https://docs.cloud.google.com/sql/docs/mysql/replication/cross-region-replicas#promote-a-replica). Because read replicas [can be configured for HA in advance](https://docs.cloud.google.com/sql/docs/mysql/high-availability#read_replicas), they don't need to go through additional changes after that promotion for HA. You can also [configure read replicas to have their own cross-region replicas](https://docs.cloud.google.com/sql/docs/postgres/replication#cascading-replicas) that can offer immediate protection from regional failures after replica promotion.

  * You can configure Spanner as either [regional](https://docs.cloud.google.com/spanner/docs/instances#regional_configurations) or multi-region. For any regional configuration, Spanner maintains three [read-write replicas](https://docs.cloud.google.com/spanner/docs/replication#read-write), each in a different Google Cloud [zone](https://docs.cloud.google.com/docs/geography-and-regions) in that region. Each read-write replica contains a full copy of your operational database that is able to serve read-write and read-only requests.

Spanner uses replicas in different zones so that if a single-zone failure occurs, your database remains available. A Spanner multi-region deployment provides a consistent environment across multiple regions, including two read-write regions and one [witness region](https://docs.cloud.google.com/spanner/docs/instances#witness_regions) containing a [witness replica](https://docs.cloud.google.com/spanner/docs/replication#witness). You must validate that the [locations of all the regions](https://docs.cloud.google.com/spanner/docs/instances#available-configurations-multi-region) meet your locality restriction requirements.




### Compute Engine

Compute Engine resources are [global, regional, or zonal](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources). Compute Engine resources such as [virtual machine instances](https://docs.cloud.google.com/compute/docs/instances) or zonal [persistent disks](https://docs.cloud.google.com/compute/docs/disks) are referred to as _zonal resources_. Other resources, such as [static external IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses#reservedaddress), are regional. Regional resources can be used by any resources in that region, regardless of zone, while zonal resources can only be used by other resources in the same zone.

Putting resources in different zones in a region isolates those resources from most types of physical infrastructure failure and infrastructure software-service failures. Also, putting resources in different regions provides an even higher degree of failure independence. This approach lets you design robust systems with resources spread across different failure domains.

For more information, see [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones).

## Using on-premises or another cloud as a production site

You might be using a Google Cloud region that prevents you from using dual or multi-region combinations for your DR architecture. To meet locality restrictions in this case, consider using your own data center or another cloud as the production site or as the failover site.

This section discusses Google Cloud products that are optimized for hybrid workloads. DR architectures that use on-premises and Google Cloud are discussed in [Disaster recovery scenarios for applications](https://docs.cloud.google.com/architecture/dr-scenarios-for-applications#dr_and_ha_architectures_for_production_on-premises).

### Google Kubernetes Engine

With products like Google Kubernetes Engine (GKE), Google Distributed Cloud, and GKE attached clusters, you can securely run your container-based workloads anywhere. These products enable consistency between on-premises and cloud environments, letting you have a consistent operating model.

As part of your DR strategy, GKE simplifies the configuration and operation of HA and failover architectures across dissimilar environments (between Google Cloud and on-premises or another cloud). You can run your production GKE clusters on-premises and if a disaster occurs, you can fail over to run the same workloads on GKE clusters in Google Cloud.

GKE has three types of clusters:

  * Single-zone cluster. A single-zone cluster has a single control plane running in one zone. This control plane manages workloads on nodes that are running in the same zone.
  * Multi-zonal cluster. A multi-zonal cluster has a single replica of the control plane running in a single zone, and has nodes running in multiple zones
  * Regional cluster. [Regional clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/regional-clusters) replicate cluster primaries and nodes across multiple zones in a single region. For example, a regional cluster in the `us-east1` region creates replicas of the control plane and nodes in three `us-east1` zones: `us-east1-b`, `us-east1-c`, and `us-east1-d`.



Regional clusters are the most resilient to zonal outages.

**Note:** For more information about region-specific considerations, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). 

### Google Cloud VMware Engine

[Google Cloud VMware Engine](https://cloud.google.com/vmware-engine/) lets you run VMware workloads in the cloud. If your on-premises workloads are VMware based, you can architect your DR solution to run on the same virtualization solution that you are running on-premises. You can select the region that meets your locality requirements.

### Networking

When your DR plan is based on moving data from on-premises to Google Cloud or from another cloud provider to Google Cloud, then you must address your networking strategy. For more information, see the [Transferring data to and from Google Cloud](https://docs.cloud.google.com/architecture/dr-scenarios-building-blocks#transferring_data_to_and_from_gcp) section of the "Disaster recovery building blocks" document.

### VPC Service Controls

When planning your DR strategy, you must ensure that the security controls that apply to your production environment also extend to your failover environment. By using VPC Service Controls, you can define a security perimeter from on-premises networks to your projects in Google Cloud.

VPC Service Controls enables a [context-aware access](https://docs.cloud.google.com/vpc-service-controls/docs/context-aware-access) approach to controlling your cloud resources. You can create granular access control policies in Google Cloud based on attributes like user identity and IP address. These policies help ensure that the appropriate security controls are in place in your on-premises and Google Cloud environments.

## What's next

  * Read other articles in this DR series: 
    * [Disaster recovery planning guide](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide)
    * [Disaster recovery building blocks](https://docs.cloud.google.com/architecture/dr-scenarios-building-blocks)
    * [Disaster recovery scenarios for data](https://docs.cloud.google.com/architecture/dr-scenarios-for-data)
    * [Disaster recovery scenarios for applications](https://docs.cloud.google.com/architecture/dr-scenarios-for-applications)
    * [Disaster recovery use cases: locality-restricted data analytic applications](https://docs.cloud.google.com/architecture/dr-scenarios-locality-restricted-data-analytics)
    * [Architecting disaster recovery for cloud infrastructure outages](https://docs.cloud.google.com/solutions/disaster-recovery/architecture)
  * Read the whitepaper [Data residency, operational transparency, and privacy for European customers on Google Cloud (PDF)](https://services.google.com/fh/files/misc/googlecloud_european_commitments_whitepaper.pdf).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-07-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-07-20 UTC."],[],[]] 
