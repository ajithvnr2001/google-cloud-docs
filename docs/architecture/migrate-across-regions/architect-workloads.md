---
url: https://docs.cloud.google.com/architecture/migrate-across-regions/architect-workloads/
title: Architect your workloads \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:15.631707+00:00
---

# Architect your workloads  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/migrate-across-regions/architect-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Architect your workloads Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-07-24 UTC

This document helps you design workloads in a way that minimizes the impact of a future expansion and migration of workloads to other Google Cloud [regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones), or the impact of a migration of workloads across regions. This document is useful if you're planning to do any of these activities or if you're evaluating the opportunity to do so in the future and want to explore what the work might look like.

This document is part of a series:

  * [Get started](https://docs.cloud.google.com/architecture/migrate-across-regions)
  * [Design resilient single-region environments on Google Cloud](https://docs.cloud.google.com/architecture/migrate-across-regions/design-resilient-single-region-environments)
  * Architect your workloads (this document)
  * [Prepare data and batch workloads for the migration](https://docs.cloud.google.com/architecture/migrate-across-regions/prepare-data-and-batch-workloads)



The guidance in this series is also useful if you didn't plan for a migration across regions or for an expansion to multiple regions in advance. In this case, you might need to spend additional effort to prepare your infrastructure, workloads, and data for the migration across regions and for the expansion to multiple regions.

This document helps you to do the following:

  1. Prepare your landing zone
  2. Prepare your workloads for a migration across regions
  3. Prepare your computing resources
  4. Prepare your data storage resources
  5. Prepare for decommissioning the source environment



## Prepare your landing zone

This section focuses on the considerations that you must make to extend a [landing zone](https://docs.cloud.google.com/architecture/landing-zones) (also called a cloud foundation) when migrating across regions.

The first step is to re-evaluate the different aspects of any existing landing zone. Before you can migrate any workload, you must already have a landing zone in place. Although you might already have a landing zone in place for the region that's hosting the workloads, the landing zone might not support the deployment of workloads in a different region, so it must be extended to the target region. Some landing zones that are already in place might have a design that can support another region without significant rework to the landing zone (for example, identity and access management or resource management). However, additional factors such as network or data might require that you do some planning for the extension. Your re-evaluation process should take into account the major requirements of your workloads to allow you to set up a generic foundation that can be specialized later during the migration.

### Enterprise considerations

When it comes to aspects such as industry and government standards, regulations, and certifications, moving workloads to another region can have different requirements. Workloads running on Google regions that are physically located in different countries must follow the laws and regulations of that country. In addition, different industry standards might have particular requirements for workloads running abroad (especially in terms of security). Because Google Cloud regions are built to run resources in a single country, sometimes workloads are migrated from another Google region to that country to adhere to specific regulations. When you perform these "in-country" migrations, it's important to re-evaluate data running on-premise to check if the new region allows the migration of your data to Google Cloud.

### Identity and access management

When you are planning a migration, you probably don't have to plan for many identity and access changes for regions that are already on Google Cloud. Identity decisions on Google Cloud and access to resources are usually based on the nature of the resources rather than the region where the resources are running. Some considerations that you might need to make are as follows:

  * **Design of teams** : Some companies are structured to have different teams to handle different resources. When a workload is migrated to another region, due to change in structure of the resources, a different team may be the best candidate to be responsible for certain resources, in which case, accesses should be adjusted accordingly.
  * **Naming conventions** : Although naming conventions might not have any technical impact on the functionalities, some consideration might be needed if there are resources defined with name conventions that refer to the specific region. One typical example is when there are already multiple replicated regions in place, such as Compute Engine virtual machines (VMs), which are named with the region as prefix, for example, `europe-west1-backend-1`. During the migration process, to avoid confusion or, worse, breaking pipelines that rely on a specific naming convention, it's important to change names to reflect the new region.



### Connectivity and networking

Your network design impacts multiple aspects of how the migration is executed, so it's important to address this design before you plan how to move workloads.

Keep in mind that on-premises connectivity with Google Cloud is one of the factors that you must re-evaluate in the migration, since it can be designed to be region specific. One example of this factor is [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview), which is connected to Google Cloud through a VLAN attachment to specific regions. You must change the region where the VLAN attachment is connected before dismissing that region to avoid region-to-region traffic. Another factor to consider is that if you're using [Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview), migrating the region can help you select a different physical location on which to connect your VLAN attachments to Google Cloud. This consideration is also relevant if you use a Cloud VPN and decide to change subnet addresses in the migration: you must reconfigure your routers to reflect the new networking.

While virtual private clouds (VPCs) on Google Cloud are global resources, single subnets are always bound to a region, which means you can't use the same subnet for the workloads after migration. Since subnets can't be overlapping IPs, to maintain the same addresses, you should create a new VPC. This process is simplified if you're using Cloud DNS, which can exploit features like DNS peering to route traffic for the migrated workloads before dismissing the old region.

For more information about building a foundation on Google Cloud, see [Migrate to Google Cloud: Plan and build your foundation](https://docs.cloud.google.com/architecture/migration-to-google-cloud-building-your-foundation).

## Prepare your workloads for a migration across regions

Whether you're setting up your infrastructure on Google Cloud and you plan to later migrate to another region, or you're already on Google Cloud and you need to migrate to another region, you must make sure that your workloads can be migrated in the most straightforward way to reduce effort and minimize risks. To help you ensure that all the workloads are in a state that allows a path to the migration, we recommend that you take the following approach:

  * **Prefer network designs that are easily replicable and loosely coupled from the specific network topology**. Google Cloud offers different products that can help you to decouple your current network configuration from the resources using that network. An example of such a product is Cloud DNS, which lets you decouple internal subnet IPs from VMs.
  * **Set up products that support multi-region or global configurations**. Products that support a configuration that involves more than one region, usually simplify the process of migrating them to another region.
  * **Consider managed services with managed cross region replicas for data**. As described in the following sections of this document, some managed services allow you to create a replica in a different region, usually for backup or high availability purposes. This feature can be important to migrate data from one region to another.



Some Google Cloud services are designed to support [multi-region deployments](https://cloud.google.com/about/locations#multi-region) or [global deployment](https://cloud.google.com/about/locations#global-products). You don't need to migrate these services, although you might need to adjust some configurations.

## Prepare your computing resources

This section provides an overview of the compute resources on Google Cloud and design principles to prepare for a migration to another region.

This document focuses on the following Google Cloud computing products:

  * [Compute Engine](https://docs.cloud.google.com/compute/docs)
  * [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [Cloud Run](https://docs.cloud.google.com/run/docs)
  * [VMware Engine](https://docs.cloud.google.com/vmware-engine/docs)



### Compute Engine

Compute Engine is Google Cloud's service that provides VMs to customers.

To migrate Compute Engine resources from one region to another, you must evaluate different factors in addition to networking considerations.

We recommend that you do the following:

  * **Check compute resources** : One of the first limitations you can encounter when changing the hosting region of a VM is the [availability of the CPU platform](https://docs.cloud.google.com/compute/docs/regions-zones#available) in the new target region. If you have to change a machine series during the migration, check that the operating system of your current VM is supported [for the series](https://docs.cloud.google.com/compute/docs/cpu-platforms). Generally speaking, this problem can be extended to every Google Cloud computing service (some new regions may not have services like [Cloud Run](https://docs.cloud.google.com/run/docs/locations) or [Cloud GPU](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones)), so before you plan the migration, make sure that all the compute services that you require are available in the destination region.
  * **Configure load balancing and scaling** : Compute Engine supports load balancing traffic between Compute Engine instances and autoscaling to automatically add or remove virtual machines from MIGs, according to demand. We recommend that you configure load balancing and autoscaling to increase the reliability and the flexibility of your environments, avoiding the management burden of self-managed solutions. For more information about configuring load balancing and scaling for Compute Engine, see [Load balancing and scaling](https://docs.cloud.google.com/compute/docs/load-balancing-and-autoscaling).
  * **Use zonal DNS names** : To mitigate the risk of cross-regional outages, we recommend that you use [zonal DNS names](https://docs.cloud.google.com/compute/docs/networking/zonal-dns) to uniquely identify virtual machines using DNS names in your environments. Google Cloud uses zonal DNS names for Compute Engine virtual machines by default. For more information about how the Compute Engine internal DNS works, see [Overview of internal DNS](https://docs.cloud.google.com/compute/docs/internal-dns). To facilitate a future migration across regions, and to make your configuration more maintainable, we recommend that you consider zonal DNS names as configuration parameters that you can eventually change in the future.
  * **Use the same managed instance groups (MIGs) template** : Compute Engine lets you [create regional MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups) that automatically provision virtual machines across multiple zones in a region automatically. If you're using a template in your old region, you can use the same template to deploy the MIGs in the new region.



### GKE

Google Kubernetes Engine (GKE) helps you deploy, manage, and scale containerized workloads on Kubernetes.

To prepare your GKE workloads for a migration, consider the following design points and GKE features:

  * **[Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/overview)** : A managed implementation of Istio mesh. Adopting Cloud Service Mesh for your cluster lets you have a greater level of control on the network traffic into the cluster. One of the key features of Cloud Service Mesh is that it lets you create a service mesh between two clusters. You can use this feature to plan the migration from one region to another by creating the GKE cluster in the new region and adding it to the service mesh. By using this approach, it's possible to start deploying workloads in the new cluster and routing traffic to them gradually, allowing you to test the new deploy while having the option to rollback by editing mesh routing.
  * **[Config Sync](https://docs.cloud.google.com/anthos-config-management/docs/config-sync-overview#configuring_clusters)** : A GitOps service built on an open source core that lets cluster operators and platform administrators deploy configurations from a single source. Config Sync can support one or many clusters, allowing you to use a single source of truth to configure of the clusters. You can use this Config Sync function to replicate the configuration of the existing cluster on the cluster for the new region, and potentially customize a specific resource for the region.
  * **[Backup for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke)** : This feature lets you back up your cluster persistent data periodically and restore the data to the same cluster or to a new one.



### Cloud Run

[Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run) offers a lightweight approach to deploy containers on Google Cloud. Cloud Run services are regional resources, and [are replicated across multiple zones in the region they are in](https://docs.cloud.google.com/run/docs/resource-model#services). When you [deploy a Cloud Run service](https://docs.cloud.google.com/run/docs/deploying#service), you can choose a region where to deploy the instance, and then use this feature to deploy the workload in a different region.

### VMware Engine

Google Cloud VMware Engine is a fully managed service that lets you run the VMware platform in Google Cloud. The VMware environment runs natively on Google Cloud bare metal infrastructure in Google Cloud locations including vSphere, vCenter, vSAN, NSX-T, HCX, and corresponding tools.

To migrate VMware Engine instances to a different region you should [create your private cloud in the new region](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-create-private-cloud) and then use VMware tools to move the instances.

You should also consider DNS and load balancing in Compute Engine environments when you plan your migration. VMware Engine uses Google Cloud DNS, which is a managed DNS hosting service that provides authoritative DNS hosting published to the public internet, private zones visible to VPC networks, and DNS forwarding and peering for managing name resolution on VPC networks. Your migration plan can support testing of multi-region load balancing and DNS configurations.

## Prepare your data storage resources

This section provides an overview of the data storage resources on Google Cloud and the basics on how to prepare for a migration to another region.

The presence of the data already on Google Cloud simplifies the migration, because it implies that a solution to host them without any transformation exists or can be hosted on Google Cloud.

The ability to copy database data into a different region and restore the data elsewhere is a common pattern in [Disaster Recovery (DR)](https://docs.cloud.google.com/architecture/dr-scenarios-for-data#managed-database-services-on-gcp). For this reason, some of the patterns described in this document rely on DR mechanisms such as database backup and recovery.

The following managed services are described in this document:

  * [Cloud Storage](https://docs.cloud.google.com/storage/docs)
  * [Filestore](https://docs.cloud.google.com/filestore/docs)
  * [Bigtable](https://docs.cloud.google.com/bigtable/docs)
  * [Firestore](https://firebase.google.com/docs/firestore)



This document assumes that the storage solutions that you are using are regional instances which are co-located with compute resources.

### Cloud Storage

Cloud Storage offers [Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs/overview), which automates the transfer of files from different systems to Cloud Storage. It can be used to replicate data to a different region for backup, and also for region to region migration.

### Cloud SQL

[Cloud SQL](https://docs.cloud.google.com/sql/docs/introduction) offers a relational database service to host different types of databases. Cloud SQL offers a [cross-region replication functionality](https://cloud.google.com/blog/products/databases/introducing-cross-region-replica-for-cloud-sql) that allows instance data to be replicated in a different region. This feature is a common pattern for backup and restore of Cloud SQL instances, but also lets you promote the second replica in the other region to the main replica. You can use this feature to create a read replica in the second region and then promote it to the main replica once you migrate workloads. In general, for databases, managed services simplify the process of data replication, to make it easier to create a replica in the new region during migration.

Another way to handle the migration is by using [Database Migration Service](https://cloud.google.com/database-migration), which lets you migrate SQL databases from different sources to Google Cloud. Among the supported sources there is also another Cloud SQL instance, with the only limitation that you can migrate to a different region, but not to a different project.

### Filestore

As explained earlier in this document, the backup and restore feature of Filestore lets you create a backup of a file share that can be restored to another region. This feature can be used to perform region to region migration.

### Bigtable

As with Cloud SQL, Bigtable supports [replication](https://docs.cloud.google.com/bigtable/docs/replication-overview). You can use this feature to replicate the same pattern described. Check in the [Bigtable location list](https://docs.cloud.google.com/bigtable/docs/locations) if the service is available in the destination region.

In addition, as with Filestore, Bigtable supports [backup and restore](https://docs.cloud.google.com/bigtable/docs/backups). This feature can be used, as with Filestore, to implement the migration by creating a backup and restoring it in another instance in the new region.

The last option is [exporting tables](https://docs.cloud.google.com/bigtable/docs/import-export), for example, on Cloud Storage. These exports will host data in another service, and the data is then available to import to the instance in the region.

### Firestore

Firestore locations might be bound to the presence of [App Engine](https://docs.cloud.google.com/appengine/docs/language-landing) in your project, which in [some scenarios](https://docs.cloud.google.com/firestore/docs/locations#types) forces the Firestore instance to be multi-region. In these migration scenarios, it's also necessary to take into account App Engine to design the right solution for Firestore. In fact, if you already have an App Engine app with a location of either `us-central` or `europe-west`, your Firestore database is considered multi-regional.

If you have a [regional location](https://docs.cloud.google.com/firestore/docs/locations#location-r) and you want to migrate to a different location, the [managed export and import service](https://docs.cloud.google.com/firestore/docs/manage-data/export-import) lets you import and export Firestore entities by using a Cloud Storage bucket. This method can be used to move instances from one region to another. The other option is to use the Firestore [backup and restore feature](https://docs.cloud.google.com/firestore/docs/backups). This option is less expensive and more straightforward than import and export.

## Prepare for decommissioning the source environment

You must prepare in advance before you decommission your source environment and switch to the new one.

At a high level, you should consider the following before you decommission the source environment:

  * **New environment tests** : Before you switch the traffic from the old environment to the new environment, you can do tests to validate the correctness of the applications. Other than the classic unit and integration tests that can be done on newly migrated applications, there are different strategies of testing. The new environment can be treated as a new version of the software and the migration of traffic can be implemented with common patterns such as [A/B testing](https://en.wikipedia.org/wiki/A/B_testing) used for validation. Another approach is to replicate the incoming traffic in the source environment and in the new environment to check that functions are preserved.
  * **Downtime planning** : If you select a strategy of migration like blue-green, where you switch traffic from an environment to another, consider the adoption of planned downtime. The downtime allows the transition to be better monitored and to avoid unpredictable errors on the client side.
  * **Rollback** : Depending on the strategies adopted for migrating the traffic, it might be necessary to implement a rollback in the case of errors or misconfiguration of the new environment. To be able to rollback the environment, you must have a monitoring infrastructure in place to detect the status of the new environment.



It's only possible to shut down services in the first region after you perform extended tests in the new region and go live in the new region without error. We recommend that you keep backups of the first region for a limited amount of time, until you're sure that there are no issues in the newly migrated region.

You should also consider if you want to promote the old region to a disaster recovery site, assuming there isn't already a solution in place. This approach requires additional design to ensure that the site is reliable. For more information on how to correctly design and plan for DR, see the [Disaster recovery planning guide](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide).

## What's Next

  * For more general design principles for designing reliable single and multi-region environments and about how Google achieves better reliability with regional and multi-region services, see [Architecting disaster recovery for cloud infrastructure outages: Common themes](https://docs.cloud.google.com/architecture/disaster-recovery#common_themes).
  * Learn more about the Google Cloud products used in this design guide: 
    * [Compute Engine](https://docs.cloud.google.com/compute/docs)
    * [GKE](https://docs.cloud.google.com/kubernetes-engine/docs)
    * [Cloud Run](https://docs.cloud.google.com/run/docs)
    * [VMware Engine](https://docs.cloud.google.com/vmware-engine/docs)
    * [Cloud Storage](https://docs.cloud.google.com/storage/docs)
    * [Filestore](https://docs.cloud.google.com/filestore/docs)
    * [Bigtable](https://docs.cloud.google.com/bigtable/docs)
    * [Firestore](https://firebase.google.com/docs/firestore)
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Author: [Valerio Ponza](https://www.linkedin.com/in/valerio-ponza-753b8544) | Technical Solution Consultant

Other contributors: 

  * [Marco Ferrari](https://www.linkedin.com/in/ferrarimark) | Cloud Solutions Architect
  * [Travis Webb](https://www.linkedin.com/in/-traviswebb/) | Solution Architect
  * [Lee Gates](https://www.linkedin.com/in/gatesl) | Group Product Manager
  * [Rodd Zurcher](https://www.linkedin.com/in/roddzurcher/) | Solutions Architect



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-07-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-07-24 UTC."],[],[]] 
