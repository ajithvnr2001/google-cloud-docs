---
url: https://docs.cloud.google.com/architecture/migrate-across-regions/design-resilient-single-region-environments/
title: Migrate across Google Cloud regions: Design resilient single-region environments on Google Cloud \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:56.920031+00:00
---

# Migrate across Google Cloud regions: Design resilient single-region environments on Google Cloud  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/migrate-across-regions/design-resilient-single-region-environments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Migrate across Google Cloud regions: Design resilient single-region environments on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-12-08 UTC

This document helps you design resilient, single-region environments on Google Cloud. This document is useful if you're planning to migrate a single-region environment or if you're evaluating the opportunity to do so in the future and want to explore what it might look like.

This document is part of a series:

  * [Get started](https://docs.cloud.google.com/architecture/migrate-across-regions)
  * Architect single-region environments on Google Cloud (this document)
  * [Architect your workloads](https://docs.cloud.google.com/architecture/migrate-across-regions/architect-workloads)
  * [Prepare data and batch workloads for migration across regions](https://docs.cloud.google.com/architecture/migrate-across-regions/prepare-data-and-batch-workloads)



This document aims to provide guidance about how to design resilient, single-region environments on Google Cloud, and it focuses on the following architectural components:

  * **Network services** , such as [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs).
  * **Computing services** , such as [Compute Engine](https://docs.cloud.google.com/compute/docs), [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs), [Google Cloud VMware Engine](https://docs.cloud.google.com/vmware-engine/docs), and [Cloud Run](https://docs.cloud.google.com/run/docs).
  * **Data storage services** , such as [Cloud Storage](https://docs.cloud.google.com/storage/docs), [Filestore](https://docs.cloud.google.com/filestore/docs), [Bigtable](https://docs.cloud.google.com/bigtable/docs), [Firestore](https://firebase.google.com/docs/firestore), [Memorystore](https://docs.cloud.google.com/memorystore/docs), and [Spanner](https://docs.cloud.google.com/spanner/docs).
  * **Data analytics services** , such as [BigQuery](https://docs.cloud.google.com/bigquery/docs), [Pub/Sub](https://docs.cloud.google.com/pubsub/docs), [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/docs), and [Dataflow](https://docs.cloud.google.com/dataflow/docs).
  * **Workloads** that you deploy in the environment.



The guidance in this document assumes that you're designing and implementing single-region environments. If you use a single-region environment now, in the future you can migrate to a multi-region environment. If you're considering a future migration and evolution of your zonal and single-region environments to multi-region environments, see [Migrate across Google Cloud regions: Get started](https://docs.cloud.google.com/architecture/migrate-across-regions).

## Properties of different deployment archetypes

Google Cloud products are provided across many [regions and zones](https://docs.cloud.google.com/docs/geography-and-regions).

When you design your Google Cloud environment, you can choose between the following deployment archetypes, presented in order of increasing reliability and operational overhead:

  * **Zonal** : You provision Google Cloud resources in a single zone within a region, and you use zonal services where they're available. If zonal services aren't available, you use regional services.
  * **Regional** : You provision Google Cloud resources in multiple zones within a region, and you use regional services when possible.
  * **Multi-regional** : You provision Google Cloud resources in multiple zones across different regions. Zonal resources are provisioned in one or more zones in each region.
  * **Global** : You provision Google Cloud resources in multiple zones across different regions worldwide. Zonal resources are provisioned in one or more zones in each region.



The preceding deployment archetypes have different reliability properties, and you can use them to provide the reliability guarantees that your environment needs. For example, a multi-region environment is more likely to survive a regional outage compared to a single-region or zonal environment. For more information about the reliability properties of each deployment archetype, see [How to leverage zones and regions to achieve reliability](https://docs.cloud.google.com/architecture/disaster-recovery#how_to_leverage_zones_and_regions_to_achieve_reliability) and the [Google Cloud infrastructure reliability guide](https://docs.cloud.google.com/architecture/infra-reliability-guide).

Designing, implementing, and operating an environment based on these deployment archetypes requires different levels of effort due to the cost and complexity properties of each deployment archetype. For example, a zonal environment might be cheaper and easier to design, implement, and operate compared to a regional or a multi-region environment. The potentially lower effort and cost of the zonal environment is because of the additional overhead that you have to manage to coordinate workloads, data, and processes that reside in different regions.

The following table summarizes the resource distribution, the reliability properties, and the complexity of each deployment archetype. It also describes the effort that's required to design and implement an environment based on each.

**Deployment archetype name** | **Resource distribution** | **Helps to resist** | **Design complexity**  
---|---|---|---  
Zonal environment | In a single zone | Resource failures | Requires coordination inside a single zone  
Single-region environment | Across multiple zones, in a single region | Resource failures, zonal outages | Requires coordination across multiple zones, in a single region  
Multi-region environment | Across multiple zones, across multiple regions | Resource failures, zonal outages, regional outages, multi-region outages | Requires coordination across multiple zones, across multiple regions  
Global environment | Across multiple zones, across multiple regions globally | Resource failures, zonal outages, regional outages, multi-region outages | Requires coordination across multiple zones, across multiple regions  
**Note:** For more information about region-specific considerations, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). 

For more information about these and other deployment archetypes, see [Google Cloud deployment archetypes](https://docs.cloud.google.com/architecture/deployment-archetypes).

## Choose deployment archetypes for your environments

To choose the deployment archetype that best fits your needs, do the following:

  1. Define the failure models that you want to guard against.
  2. Evaluate the deployment archetypes to determine what will best fit your needs.



### Define failure models

To define failure models, consider the following questions:

  * **Which components of your environment need failure models**? Failure models can apply to anything that you provision or deploy on Google Cloud. A failure model can apply to an individual, or you can apply a failure model to all resources in an entire zone or region. We recommend that you apply a failure model to anything that provides you value, such as workloads, data, processes, and any Google Cloud resource.
  * **What are your high availability, business continuity, and disaster recovery requirements for these components**? Each component of your environment might have its own [service level objectives (SLOs)](https://sre.google/sre-book/service-level-objectives/) that define the acceptable service levels for that component, and its own disaster recovery requirements. For example, the [Compute Engine SLA](https://cloud.google.com/compute/sla) indicates that if you need to achieve more than 99.5% of monthly uptime, you need to provision instances in multiple zones across a single region. For more information, see the [Disaster recovery planning guide](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide#basics_of_dr_planning).
  * **How many failure models do you need to define**? In a typical environment, not all components have to provide the same reliability guarantees. If you offer guarantees for higher uptime and stronger resilience, you usually have to expend more effort and resources. When you define your failure models, we recommend that you consider an approach where you define multiple failure models for each component, and not just one for all your components. For example, business-critical workloads usually need to offer higher reliability, although it might be acceptable to offer lesser reliability guarantees for other, less critical workloads.
  * **How many resources do the failure models need in order to guard against failures**? To guard against the failure models that you defined, you expend resources such as the time and cost required for people to design, provision, and configure protection mechanisms and automated processes. We recommend that you assess how many resources you need to guard against each failure model that you define.
  * **How will you detect that a failure is happening**? Being able to detect that a failure is happening or is about to happen is critical so that you can start mitigation, recovery, and reconciliation processes. For example, you can configure [Google Cloud Observability](https://docs.cloud.google.com/stackdriver/docs) to alert you about degraded performance.
  * **How can you test the failure models that you're defining**? When you define failure models, we recommend that you think about how to continuously test each model to verify that it effectively guards against the failures that the models are aimed at. For example, you can [inject faults](https://en.wikipedia.org/wiki/Fault_injection) in your environments, or to assess the ability of your environments to tolerate failures, you can adopt [chaos engineering](https://en.wikipedia.org/wiki/Chaos_engineering).
  * **How much impact do you expect if a particular failure model occurs**? To gain an understanding of the impact that a failure might have on your business, we recommend that, for each failure model, you estimate the consequences of each failure the model is designed against. This understanding is useful in establishing priorities and recovery orders so that you and your processes deal with the most critical components first.
  * **How long do you expect the failures to last in the failure models that you're defining**? The duration of a failure can greatly affect mitigation and recovery plans. Therefore, when you define failure models, we recommend that you account for how much time a failure can last. When you consider how much time that a failure can last, also consider how much time it takes to: identify a failure, reconcile the failure, and to restore the resources that failed.



For more considerations about failure models and how to design a reliable disaster recovery plan, see [Architecting disaster recovery for cloud infrastructure outages](https://docs.cloud.google.com/architecture/disaster-recovery).

### Evaluate deployment archetypes

After you define the failure models that you want to guard against, you evaluate the deployment archetypes to determine what will best fit your needs. When you evaluate the deployment archetypes, consider the following questions:

  * **How many deployment archetypes do you need**? You don't have to choose just one deployment archetype to fit all your environments. Instead, you can implement a hybrid approach where you pick multiple deployment archetypes according to the reliability guarantees that you need in order to guard against the failure models you defined. For example, if you defined two failure models—one that requires a zonal environment, and one that requires a regional environment—you might want to choose separate deployment archetypes to guard against each failure model. If you choose multiple deployment archetypes, we recommend that you evaluate the potentially increasing complexity of designing, implementing, and operating multiple environments.
  * **How many resources do you need to design and implement environments based on the deployment archetypes**? Designing and implementing any kind of environment requires resources and effort. We recommend that you assess how many resources you think that you'll need in order to design and implement each environment based on the archetype you choose. When you have a complete understanding of how many resources you need, you can balance the trade-offs between the reliability guarantees that each deployment archetype offers, and the cost and the complexity of designing, implementing, and operating environments based on those archetypes.
  * **Do you expect to migrate an environment based on one deployment archetype to an environment based on a different archetype**? In the future, you might migrate workloads, data, and processes from one Google Cloud environment to a different Google Cloud environment. For example, you might migrate from a zonal environment to a regional environment.
  * **How business-critical are the environments that you're designing and implementing**? Business-critical environments likely need more reliability guarantees. For example, you might choose to design and implement a multi-region environment for business-critical workloads, data, and processes, and design a zonal or regional environment for less critical workloads, data, and processes.
  * **Do you need the features that are offered by particular deployment archetypes for certain environments**? Aside from the reliability guarantees that each deployment archetype offers, the archetypes also offer different scalability, geographical proximity, latency, and data locality guarantees. We recommend that you consider those guarantees when you choose the deployment archetypes for your environments.



Along with the technical aspects of the failure modes that you defined by following the preceding guidance, we recommend that you consider any non-functional requirements such as regulatory, locality, and sovereignty requirements. Those requirements can restrict the options that are available to you. For example, if you need to meet regulatory requirements that mandate the usage of a specific region, then you have to design and implement either a single-region environment, or a zonal environment in that region.

## Choose a Google Cloud region for your environment

When you start designing your single-region environments, you have to determine the region that best fits the requirements of each environment. The following sections describe these two categories of selection criteria:

  * **Functional criteria**. These criteria are about which Google Cloud products a particular region offers, and whether a particular region meets your latency and geographical proximity to users and other environments outside Google Cloud. For example, if your workloads and data have latency requirements for your users or other environments outside Google Cloud, you might need to choose the region that's closest to your users or other environments to minimize that latency.
  * **Non-functional criteria**. These criteria are about the product prices that are associated with specific regions, carbon footprint requirements, and mandatory requirements and regulations that are in place for your business. For example, highly regulated markets such as banking and public sector have very stringent and specific requirements about data and workload locality, and how they share the cloud provider infrastructure with other customers.



If you choose a particular Google Cloud region now, in the future you can migrate to different regions or to a multi-region environment. If you're considering a future migration to other regions, see [Migrate across Google Cloud regions: Get started](https://docs.cloud.google.com/architecture/migrate-across-regions).

### Evaluate functional criteria

To evaluate functional criteria, consider the following questions:

  * **What are your geographical proximity requirements**? When you choose a Google Cloud region, you might need to place your workloads, data, and processes near your users or your environments outside Google Cloud, such as your on-premises environments. For example, if you're targeting a user base that's concentrated in a particular geographic area, we recommend that you choose a Google Cloud region that's closest to that geographic area. Choosing a Google Cloud region that best fits your geographical proximity requirements lets your environments guarantee lower latency and lower reaction times to requests from your users and from your environments outside Google Cloud. Tools like [Performance Dashboard](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/concepts/overview) to [view Google Cloud latency](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/view-google-cloud-latency), and unofficial tools such as the [Google Cloud Region Picker](https://googlecloudplatform.github.io/region-picker/) can give you a high-level idea of the latency characteristics of Google Cloud regions. However, we recommend that you perform a comprehensive assessment to evaluate if the latency properties fit your requirements, workloads, data, and processes.
  * **Which of the regions that you want to use offer the products that you need**? We recommend that you assess the products that are available in each Google Cloud region, and which regions provide the services that you need to design and implement your environments. For more information about which products are available in each region and their availability timelines, see [Cloud locations](https://cloud.google.com/about/locations). Additionally, some products might not offer all their features in every region where they're available. For example, the [available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available) for Compute Engine offer specific machine types in specific Google Cloud regions. For more information about what features each product offers in each region, see the product documentation.
  * **Are the resources that you need in each Google Cloud region within the per-region quota limits**? Google Cloud uses quotas to restrict how much of a shared Google Cloud resource that you can use. Some quotas are global and apply to your usage of the resource anywhere in Google Cloud, while others are regional or zonal and apply to your usage of the resource in a specific Google Cloud region. For example, most [Compute Engine resource usage quotas](https://docs.cloud.google.com/compute/resource-usage#regional_and_global_quotas), such as the number of virtual machines that you can create, are regional. For more information about quotas and how to adjust them, see the [Cloud Quotas documentation](https://docs.cloud.google.com/docs/quotas/overview).



### Evaluate non-functional criteria

To evaluate non-functional criteria, consider the following questions:

  * **Do you prefer a low carbon footprint**? Google Cloud continuously invests in [sustainability](https://cloud.google.com/sustainability) and in carbon-free energy for Google Cloud regions, and it's [committed to carbon free energy for all cloud regions](https://cloud.google.com/blog/topics/inside-google-cloud/announcing-round-the-clock-clean-energy-for-cloud). Google Cloud regions have different carbon footprints. For information about the carbon footprint of each Google Cloud region, and how to incorporate carbon-free energy in your location strategy, see [Carbon free energy for Google Cloud regions](https://cloud.google.com/sustainability/region-carbon).
  * **Do your environments need to meet particular regulations**? Governments and national and supranational entities often strictly regulate certain markets and business areas, such as banking and public sector. These regulations might mandate that workloads, data, and processes reside only in certain geographic regions. For example, your environments might need to comply with [data, operational, and software sovereignty requirements](https://cloud.google.com/blog/products/identity-security/advancing-digital-sovereignty-on-europes-terms) to guarantee certain levels of control and transparency for sensitive data and workloads running in the cloud. We recommend that you assess your current and upcoming regulatory requirements when choosing the Google Cloud regions for your environments, and select the Google Cloud regions that best fit your regulatory requirements.



## Design and build your single-region environments

To design a single-region environment, do the following:

  1. Build your foundation on Google Cloud.
  2. Provision and configure computing resources.
  3. Provision and configure data storage resources.
  4. Provision and configure data analytics resources.



When you design your environment, consider the following general design principles:

  * **Provision regional resources**. Many Google Cloud products support provisioning resources in multiple zones across a region. We recommend that you provision regional resources instead of zonal resources when possible. Theoretically, you might be able to provision zonal resources in multiple zones across a region and manage them yourself to achieve a higher reliability. However, that configuration wouldn't fully benefit from all the reliability features of the Google infrastructure that underpins Google Cloud services.
  * **Verify that the environments work as expected with the failure model assumptions**. When you design and implement your single-region environments, we recommend that you verify whether those environments meet the requirements to guard against the failure models that you're considering, before you promote those environments as part of your production environment. For example, you can [simulate zonal outages](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-simulate-zonal-outage) to verify that your single-region environments can survive with minimal disruption.



For more general design principles for designing reliable single- and multi-region environments and for information about how Google achieves better reliability with regional and multi-region services, see [Architecting disaster recovery for cloud infrastructure outages: Common themes](https://docs.cloud.google.com/architecture/disaster-recovery#common_themes).

### Build your foundation on Google Cloud

To build the foundation of your single-region environments, see [Migrate to Google Cloud: Plan and build your foundation](https://docs.cloud.google.com/architecture/migration-to-google-cloud-building-your-foundation). The guidance in that document is aimed at building a foundation for migrating workloads, data, and processes to Google Cloud, but it's also applicable to build the foundation for your single-region environments. After you read that document, continue to read this document.

After you build your foundation on Google Cloud, you design and implement security controls and boundaries. Those security measures help to ensure that your workloads, data, and processes stay inside their respective regions. The security measures also help to ensure that your resources don't leak anything to other regions due to bugs, misconfigurations, or malicious attacks.

### Provision and configure computing resources

After you build the foundation of your single-region environments, you provision and configure computing resources. The following sections describe the Google Cloud computing products that support regional deployments.

#### Compute Engine

Compute Engine is Google Cloud's infrastructure as a service (IaaS). It uses Google's worldwide infrastructure to offer virtual machines and related services to customers.

Compute Engine resources are either zonal, such as [virtual machines](https://docs.cloud.google.com/compute/docs/instances) or [zonal Persistent Disk](https://docs.cloud.google.com/compute/docs/disks); regional, such as [static external IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses#reservedaddress); or global, such as [Persistent Disk snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshots). For more information about the zonal, regional, and global resources that Compute Engine supports, see [Global, regional, and zonal resources](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources).

To allow for better flexibility and resource management of physical resources, Compute Engine decouples zones from their physical resources. For more information about this abstraction and what it might imply for you, see [Zones and clusters](https://docs.cloud.google.com/compute/docs/regions-zones#zones_and_clusters).

To increase the reliability of your environments that use Compute Engine, consider the following:

  * **Regional managed instance groups (MIGs)**. Compute Engine virtual machines are zonal resources, so they will be unavailable in the event of a zonal outage. To mitigate this issue, Compute Engine lets you [create regional MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups) that provision virtual machines across multiple zones in a region automatically, according to demand and regional availability.

**Note:** For more information about region-specific considerations, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). 

If your workloads are stateful, you can also [create regional stateful MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-migs) to preserve stateful data and configurations. Regional MIGs support simulating zonal failures. For information about simulating a zonal failure when using a regional MIG, see [Simulate a zone outage for a regional MIG](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-simulate-zonal-outage). For information about how regional MIGs compare to other deployment options, see [Choose a Compute Engine deployment strategy for your workload](https://docs.cloud.google.com/compute/docs/choose-compute-deployment-option).

  * **Target distribution shape**. Regional MIGs distribute virtual machines according to the target distribution shape. To ensure that virtual machine distribution doesn't differ by more than one unit between any two zones in a region, we recommend that you choose the `EVEN` distribution shape when you create regional MIGs. For information about the differences between target distribution shapes, see [Comparison of shapes](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-distribution-shape#comparison_of_shapes).

  * **Instance templates**. To define the virtual machines to provision, MIGs use a global resource type called [instance templates](https://docs.cloud.google.com/compute/docs/instance-templates). Although instance templates are global resources, they might reference zonal or regional resources. When you create instance templates, we recommend that you reference regional resources over zonal resources when possible. If you use zonal resources, we recommend that you assess the impact of using them. For example, if you create an instance template that references a Persistent Disk volume that's available only in a given zone, you can't use that template in any other zones because the Persistent Disk volume isn't available in those other zones.

  * **Configure load balancing and scaling**. Compute Engine supports load balancing traffic between Compute Engine instances, and it supports autoscaling to automatically add or remove virtual machines from MIGs, according to demand. To increase the reliability and the flexibility of your environments, and to avoid the management burden of self-managed solutions, we recommend that you configure load balancing and autoscaling. For more information about configuring load balancing and scaling for Compute Engine, see [Load balancing and scaling](https://docs.cloud.google.com/compute/docs/load-balancing-and-autoscaling).

  * **Configure resource reservations**. To ensure that your environments have the necessary resources when you need them, we recommend that you configure [resource reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type) to provide assurance in obtaining capacity for zonal Compute Engine resources. For example, if there is a zonal outage, you might need to provision virtual machines in another zone to supply the necessary capacity to make up for the ones that are unavailable because of the outage. Resource reservations ensure that you have the resources available to provision the additional virtual machines.

  * **Use zonal DNS names**. To mitigate the risk of cross-regional outages, we recommend that you use [zonal DNS names](https://docs.cloud.google.com/compute/docs/internal-dns#instance-fully-qualified-domain-names) to uniquely identify virtual machines that use DNS names in your environments. Google Cloud uses zonal DNS names for Compute Engine virtual machines by default. For more information about how the Compute Engine internal DNS works, see [Internal DNS](https://docs.cloud.google.com/compute/docs/internal-dns). To facilitate a future migration across regions, and to make your configuration more maintainable, we recommend that you consider zonal DNS names as configuration parameters that you can eventually change in the future.

  * **Choose appropriate storage options**. Compute Engine supports several [storage options](https://docs.cloud.google.com/compute/docs/disks) for your virtual machines, such as Persistent Disk volumes and local solid state drives (SSDs):

    * Persistent Disk volumes are distributed across several physical disks, and they're located independently from your virtual machines. Persistent disks can either be zonal or regional. Zonal persistent disks store data in a single zone, while regional persistent disks replicate data across two different zones. When you choose storage options for your single-region environments, we recommend that you choose regional persistent disks because they provide you with failover options if there are zonal failures. For more information about how to react to zonal failures when you use regional persistent disks, see [High availability options using regional Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/high-availability-regional-persistent-disk) and [Regional Persistent Disk failover](https://docs.cloud.google.com/compute/docs/disks/repd-failover).
    * Local SSDs have high throughput, but they store data only until an instance is stopped or deleted. Therefore, local SSds are ideal to store temporary data, caches, and data that you can reconstruct by other means. Persistent disks are durable storage devices that virtual machines can access like physical disks.
  * **Design and implement mechanisms for data protection**. When you design your single-region environments, we recommend that you put in place automated mechanisms to protect your data if there are adverse events, such as zonal, regional, or multi-regional failures, or deliberate attacks by malicious third parties. Compute Engine provides [several options to protect your data](https://docs.cloud.google.com/compute/docs/disks/data-protection). You can use those data options features as building blocks to design and implement your data protection processes.




#### GKE

GKE helps you to deploy, manage, and scale containerized workloads on Kubernetes. GKE builds on top of Compute Engine, so the recommendations in the previous section about Compute Engine partially apply to GKE.

To increase the reliability of your environments that use GKE, consider the following design points and GKE features:

  * **Use regional GKE clusters to increase availability**. GKE supports different [availability types](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters#availability) for your clusters, depending on the type of cluster that you need. GKE clusters can have a zonal or regional control plane, and they can have nodes that run in a single zone or across multiple zones within a region. Different cluster types also offer different service level agreements (SLAs). To increase the reliability of your environments, we recommend that you choose regional clusters.

**Note:** For more information about region-specific considerations, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). 

If you're using the GKE Autopilot feature, you can provision regional clusters only.

  * **Consider a multi-cluster environment**. Deploying multiple GKE clusters can [increase the flexibility and the availability properties](https://docs.cloud.google.com/anthos/fleet-management/docs/multi-cluster-use-cases) of your environment, at the cost of increasing complexity. For example, if you need to use a new GKE feature that you can only enable when you create a GKE cluster, you can avoid downtime and reduce the complexity of the migration by adding a new GKE cluster to your multi-cluster environment, deploying workloads in the new cluster, and destroying the old cluster. For more information about the benefits of a multi-cluster GKE environment, see [Multi-cluster use cases](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/multi-cluster-use-cases). To help you manage the complexity of the migration, Google Cloud offers [Fleet management](https://docs.cloud.google.com/anthos/fleet-management/docs), a set of capabilities to manage a group of GKE clusters, their infrastructure, and the workloads that are deployed in those clusters.

  * **Set up Backup for GKE**. Backup for GKE is a [regional service](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/about-locations) for backing up workload configuration and volumes in a source GKE cluster, and restoring them in a target GKE cluster. To protect workload configuration and data from possible losses, we recommend that you enable and configure Backup for GKE. For more information, see [Backup for GKE Overview](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke).




#### Cloud Run

[Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run) is a managed compute platform to run containerized workloads. Cloud Run uses services to provide you with the infrastructure to run your workloads. Cloud Run services are regional resources, and the services are [replicated across multiple zones in the region that they're in](https://docs.cloud.google.com/run/docs/resource-model#services). When you [deploy a Cloud Run service](https://docs.cloud.google.com/run/docs/deploying#service), you can choose a region. Then, Cloud Run automatically chooses the zones inside that region in which to deploy instances of the service. Cloud Run automatically balances traffic across service instances, and it's designed to [greatly mitigate the effects of a zonal outage](https://docs.cloud.google.com/architecture/disaster-recovery#cloud_run).

**Note:** For more information about region-specific considerations, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). 

#### VMware Engine

[VMware Engine](https://docs.cloud.google.com/vmware-engine/docs/overview) is a fully managed service that lets you run the VMware platform in Google Cloud. To increase the reliability of your environments that use VMware Engine, we recommend the following:

  * **Provision multi-node VMware Engine private clouds**. VMware Engine supports provisioning isolated VMware stacks called [private clouds](https://docs.cloud.google.com/vmware-engine/docs/concepts-private-cloud), and all nodes that compose a private cloud reside in the same region. Private cloud nodes run on dedicated, isolated bare-metal hardware nodes, and they're configured to eliminate single points of failure. VMware Engine supports single-node private clouds, but we only recommend using single-node private clouds for proofs of concept and testing purposes. For production environments, we recommend that you use the default, multi-node private clouds.
  * **Provision VMware Engine stretched private clouds**. A [stretched private cloud](https://docs.cloud.google.com/vmware-engine/docs/concepts-stretched-private-cloud) is a multi-node private cloud whose nodes are distributed across the zones in a region. A stretched private cloud protects your environment against zonal outages.



For more information about the high-availability and redundancy features of VMware Engine, see [Availability and redundancy](https://docs.cloud.google.com/vmware-engine/docs/concepts-high-availability-vmware).

### Provision and configure data storage resources

After you provision and configure computing resources for your single-region environments, you provision and configure resources to store and manage data. The following sections describe on the Google Cloud data storage and management products that support regional and multi-regional configurations.

#### Cloud Storage

[Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction) is a service to store _objects_ , which are immutable pieces of data, in [_buckets_](https://docs.cloud.google.com/storage/docs/buckets), which are basic containers to hold your data. When you [create a bucket](https://docs.cloud.google.com/storage/docs/creating-buckets), you select the [bucket location type](https://docs.cloud.google.com/storage/docs/locations) that best meets your availability, regulatory, and other requirements. Location types have [different availability guarantees](https://cloud.google.com/storage/sla). To protect your data against failure and outages, Cloud Storage makes your data redundant across at least two zones for buckets that have a region location type, across two regions for buckets that have a dual-region location type, and across two or more regions for buckets that have a multi-region location type. For example, if you need to make a Cloud Storage bucket available if there are zonal outages, you can provision it with a region location type.

For more information about how to design disaster mechanisms for data stored in Cloud Storage, and about how Cloud Storage reacts to zonal and regional outages, see [Architecting disaster recovery for cloud infrastructure outages: Cloud Storage](https://docs.cloud.google.com/architecture/disaster-recovery#cloud_storage).

#### Filestore

[Filestore](https://docs.cloud.google.com/filestore/docs/overview) provides fully managed file servers on Google Cloud that can be connected to Compute Engine instances, GKE clusters, and your on-premises machines. Filestore offers several [service tiers](https://docs.cloud.google.com/filestore/docs/service-tiers). Each tier offers unique availability, scalability, performance, capacity, and data-recovery features. When you provision Filestore instances, we recommend that you choose the **Enterprise tier** because it supports high availability and [data redundancy across multiple zones in a region](https://docs.cloud.google.com/filestore/docs/overview#reliability); instances that are in other tiers are zonal resources.

**Note:** For more information about region-specific considerations, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). 

#### Bigtable

[Bigtable](https://docs.cloud.google.com/bigtable/docs/overview) is a fully managed, high-performance, and high-scalability database service for large analytical and operational workloads. Bigtable instances are [zonal resources](https://docs.cloud.google.com/bigtable/docs/locations). To increase the reliability of your instances, you can configure Bigtable to replicate data across multiple zones within the same region or across multiple regions.

**Note:** For more information about region-specific considerations, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). 

When replication is enabled, if there is an outage, Bigtable automatically fails requests over to other available instances where you replicated data to.

For more information about how replication works in Bigtable, see [About replication](https://docs.cloud.google.com/bigtable/docs/replication-overview) and [Architecting disaster recovery for cloud infrastructure outages: Bigtable](https://docs.cloud.google.com/architecture/disaster-recovery#cloud_bigtable).

#### Firestore

Firestore is a flexible, scalable database for mobile, web, and server development from Firebase and Google Cloud. When you provision a Firestore database, you select its location. Locations can be either multi-region or regional, and they offer different reliability guarantees. If a database has a regional location, it replicates data across different zones within a region. A multi-region database replicates data across more than one region.

For information about how replication works in Firestore, and about how Firestore reacts to zonal and regional outages, see [Firestore locations](https://firebase.google.com/docs/firestore/locations) and [Architecting disaster recovery for cloud infrastructure outages: Firestore](https://docs.cloud.google.com/architecture/disaster-recovery#firestore).

#### Memorystore

Memorystore lets you configure scalable, secure, and highly available in-memory data storage services. It supports data backends for [Redis](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview), [Memcached](https://docs.cloud.google.com/memorystore/docs/memcached/memcached-overview), and [Valkey](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview).

When you provision [Memorystore for Redis instances](https://docs.cloud.google.com/memorystore/docs/redis/instances), you select a [service tier](https://docs.cloud.google.com/memorystore/docs/redis/redis-tiers) for that instance. Memorystore for Redis supports several instance service tiers, and each tier offers unique availability, node size, and bandwidth features. When you provision a Memorystore for Redis instance, we recommend that you choose a **Standard tier** or a **Standard tier with read replicas**. Memorystore instances in those two tiers automatically replicate data across multiple zones in a region.

**Note:** For more information about region-specific considerations, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). 

For more information about how Memorystore for Redis achieves high availability, see [High availability for Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis/high-availability).

When you provision [Memorystore for Memcached instances](https://docs.cloud.google.com/memorystore/docs/memcached/instance-node-properties), consider the following:

  * **Zone selection**. When you [provision Memorystore for Memcached instances](https://docs.cloud.google.com/memorystore/docs/memcached/create-manage-instances), you select the region in which you want to deploy the instance. Then, you can either select the zones within that region where you want to deploy the nodes of that instance, or you can let Memorystore for Memcached automatically distribute the nodes across zones. To optimally place instances, and to avoid provisioning issues such as placing all the nodes inside the same zone, we recommend that you let Memorystore for Memcached automatically distribute nodes across zones within a region.
  * **Data replication across zones**. Memorystore for Memcached instances don't replicate data across zones or regions. For more information about how Memorystore for Memcached instances work if there are zonal or regional outages, see [Architecting disaster recovery for cloud infrastructure outages: Memorystore for Memcached](https://docs.cloud.google.com/architecture/disaster-recovery#memorystore_for_memcached).



When you provision [Memorystore for Valkey instances](https://docs.cloud.google.com/memorystore/docs/valkey/create-instances), you choose availability and reliability options. Memorystore for Valkey supports several configurations, such as zonal and multi-zonal instances. For more information about Memorystore for Valkey availability and reliability, see [Memorystore for Valkey: High availability and replicas](https://docs.cloud.google.com/memorystore/docs/valkey/ha-and-replicas).

#### Spanner

[Spanner](https://docs.cloud.google.com/spanner) is a fully managed relational database with unlimited scale, strong consistency, and up to 99.999% availability. To use Spanner, you provision [Spanner instances](https://docs.cloud.google.com/spanner/docs/instances). When you provision Spanner instances, consider the following:

  * **Instance configuration**. An [instance configuration](https://docs.cloud.google.com/spanner/docs/instance-configurations) defines the geographic placement and replication of the databases in a Spanner instance. When you create a Spanner instance, you configure it as either regional or multi-region.
  * **Replication**. Spanner supports automatic, byte-level replication, and it supports the creation of [replicas](https://docs.cloud.google.com/spanner/docs/replication) according to your availability, reliability, and scalability needs. You can distribute replicas across regions and environments. Spanner instances that have a regional configuration maintain one [read-write replica](https://docs.cloud.google.com/spanner/docs/replication#read-write) for each zone within a region. Instances that have a multi-region configuration replicate data in multiple zones across multiple regions.
  * **Moving instances**. Spanner lets you [move an instance](https://docs.cloud.google.com/spanner/docs/move-instance) from any instance configuration to any other instance configuration without causing any downtime, or disruption to transaction guarantees during the move.



For more information about Spanner replication, and about how Spanner reacts to zonal and regional outages, see [Spanner replication](https://docs.cloud.google.com/spanner/docs/replication) and [Architecting disaster recovery for cloud infrastructure outages: Spanner](https://docs.cloud.google.com/architecture/disaster-recovery#cloud_spanner).

### Provision and configure data analytics resources

After you provision and configure data storage resources for your single-region environments, you provision and configure data analytics resources. The following sections describe on the Google Cloud data analytics products that support regional configurations.

#### BigQuery

[BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction) is a fully managed enterprise data warehouse that helps you to manage and analyze your data with built-in features like machine learning, geospatial analysis, and business intelligence.

To organize and control access to data in BigQuery, you provision top-level containers called [datasets](https://docs.cloud.google.com/bigquery/docs/datasets-intro). When you provision BigQuery datasets, consider the following:

  * **Dataset location**. To select the [BigQuery location](https://docs.cloud.google.com/bigquery/docs/locations) where you want to store your data, you configure the dataset location. A location can either be regional or multi-region. For either location type, BigQuery stores copies of your data in two different zones within the selected location. You can't change the dataset location after you create a dataset.
  * **Disaster planning**. BigQuery is a regional service, and it handles zonal failures automatically, for computing and for data. However, there are certain scenarios that you have to plan for yourself, such as regional outages. We recommend that you consider those scenarios when you design your environments.



For more information about BigQuery disaster recovery planning and features, see [Understand reliability: Disaster planning](https://docs.cloud.google.com/bigquery/docs/reliability-intro#disaster_planning) in the BigQuery documentation, and see [Architecting disaster recovery for cloud infrastructure outages: BigQuery](https://docs.cloud.google.com/architecture/disaster-recovery#bigquery).

#### Managed Service for Apache Spark

[Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/docs/concepts/overview) is a managed service that lets you take advantage of open source data tools for batch processing, querying, streaming, and machine learning. Managed Service for Apache Spark builds on top of Compute Engine, so the recommendations in the previous section about Compute Engine partially apply to Managed Service for Apache Spark as well.

To use Managed Service for Apache Spark, you [create Managed Service for Apache Spark clusters](https://docs.cloud.google.com/dataproc/docs/guides/create-cluster). Managed Service for Apache Spark clusters are [zonal resources](https://docs.cloud.google.com/dataproc/docs/concepts/regional-endpoints). When you create Managed Service for Apache Spark clusters, consider the following:

  * **Automatic zone placement**. When you create a cluster, you can either specify the zone within a region where you want to provision the nodes of the cluster, or let [Managed Service for Apache Spark auto zone placement](https://docs.cloud.google.com/dataproc/docs/concepts/configuring-clusters/auto-zone) select the zone automatically. We recommend that you use auto zone placement unless you need to fine tune the zone placement of cluster nodes inside the region.
  * **High availability mode**. When you create a cluster, you can enable [high availability mode](https://docs.cloud.google.com/dataproc/docs/concepts/configuring-clusters/high-availability). You can't enable high availability mode after you create a cluster. We recommend that you enable high availability mode if you need the cluster to be resilient to the failure of a single coordinator node, or to partial zonal outages. High availability Managed Service for Apache Spark clusters are zonal resources.



For more information about how Managed Service for Apache Spark reacts to zonal and regional outages and how to increase the reliability of your Managed Service for Apache Spark clusters if there are failures, see [Architecting disaster recovery for cloud infrastructure outages: Managed Service for Apache Spark](https://docs.cloud.google.com/architecture/disaster-recovery#dataproc).

#### Dataflow

[Dataflow](https://docs.cloud.google.com/dataflow/docs/about-dataflow) is a fully managed service for running stream and batch data processing pipelines. To use Dataflow, you [create Dataflow pipelines](https://docs.cloud.google.com/dataflow/docs/guides/beam-creating-a-pipeline), and then Dataflow runs _jobs_ , which are instances of those pipelines, on worker nodes. Because [jobs are zonal resources](https://docs.cloud.google.com/dataflow/docs/guides/pipeline-workflows#zonal-failures), when you use Dataflow resources, you should consider the following:

  * **Regional endpoints**. When you create a job, Dataflow requires that you configure a [regional endpoint](https://docs.cloud.google.com/dataflow/docs/concepts/regional-endpoints). By configuring a regional endpoint for your job, you restrict the computing and data resource placement to a particular region.
  * **Zonal placement**. Dataflow automatically distributes worker nodes either across all the zones within a region or in the best zone within a region, according to the job type. Dataflow lets you override the zonal placement of worker nodes by placing all of the worker nodes in the same zone within a region. To mitigate the issues caused by zonal outages, we recommend that you let Dataflow automatically select the best zone placement unless you need to place the worker nodes in a specific zone.



For more information about how Managed Service for Apache Spark reacts to zonal and regional outages and how to increase the reliability of your Managed Service for Apache Spark clusters if there are failures, see [Architecting disaster recovery for cloud infrastructure outages: Dataflow](https://docs.cloud.google.com/architecture/disaster-recovery#dataflow).

#### Pub/Sub

[Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview) is an asynchronous and scalable messaging service that decouples services that produce messages from the services that process those messages. Pub/Sub organizes messages in topics. _Publishers_ (services that produce messages) send messages to topics, and _subscribers_ receive messages from topics. Pub/Sub stores each message in a single region, and replicates it in at least two zones within that region. For more information, see [Architectural overview of Pub/Sub](https://docs.cloud.google.com/pubsub/architecture).

When you configure your Pub/Sub environment, consider the following:

  * **Global and regional endpoints**. Pub/Sub supports [global and regional endpoints to publish messages](https://docs.cloud.google.com/pubsub/docs/reference/service_apis_overview#pubsub_endpoints). When a publisher sends a message to the global endpoint, Pub/Sub automatically selects the closest region to process that message. When a producer sends a message to a regional endpoint, Pub/Sub processes the message in that region.
  * **Message storage policies**. Pub/Sub lets you configure [message storage policies](https://docs.cloud.google.com/pubsub/docs/resource-location-restriction) to restrict where Pub/Sub processes and stores messages, regardless of the origin of the request and the endpoint that the publisher used to publish the message. We recommend that you configure message storage policies to ensure that messages don't leave your single-region environment.



For more information about how Pub/Sub handles zonal and regional outages, see [Architecting disaster recovery for cloud infrastructure outages: Pub/Sub](https://docs.cloud.google.com/architecture/disaster-recovery#pubsub).

### Adapt your workloads to single-region environments

When you complete the provisioning and the configuration of your environments, you need to consider how to make your workloads more resilient to zonal and regional failures. Each workload can have its own availability and reliability requirements and properties, but there are a few design principles that you can apply, and strategies that you can adopt to improve your overall resilience posture in the unlikely event of zonal and regional failures. When you design and implement your workloads, consider the following:

  * **Implement Site Reliability Engineering (SRE) practices and principles**. Automation and extensive monitoring are part of the core principles of SRE. [Google Cloud provides the tools and the professional services to implement SRE](https://cloud.google.com/sre) to increase the resilience and the reliability of your environments and to reduce toil.
  * **Design for scalability and resiliency**. When you design workloads aimed at cloud environments, we recommend that you consider scalability and resiliency to be inherent requirements that your workloads must respect. For more information about this kind of design, see [Patterns for scalable and resilient apps](https://docs.cloud.google.com/architecture/scalable-and-resilient-apps).
  * **Design for recovering from cloud infrastructure outages**. Google Cloud availability guarantees are defined by the [Google Cloud Service Level Agreements](https://cloud.google.com/terms/sla). In the unlikely event that a zonal or a regional failure occurs, we recommend that you [design your workloads so that they're resilient to zonal and regional failures](https://docs.cloud.google.com/architecture/disaster-recovery#common_themes).
  * **Implement[load shedding and graceful degradation](https://sre.google/sre-book/addressing-cascading-failures/#xref_cascading-failure_load-shed-graceful-degredation)**. If there are cloud infrastructure failures, or failures in other dependencies of your workloads, we recommend that you design your workloads so that they're resilient. Your workloads should maintain certain and well-defined levels of functionality even if there are failures (_graceful degradation_) and they should be able to drop some proportion of their load as they approach overload conditions (_load shedding_).
  * **Plan for regular maintenance**. When you design your [deployment processes](https://docs.cloud.google.com/architecture/migration-to-gcp-deploying-your-workloads) and your operational processes, we recommend that you also think about all the activities that you need to perform as part of the regular maintenance of your environments. Regular maintenance should include activities like applying updates and configuration changes to your workloads and their dependencies, and how those activities might impact the availability of your environments. For example, you can configure a [host maintenance policy](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview) for your Compute Engine instances.
  * **Adopt a test-driven development approach**. When you design your workloads, we recommend that you adopt a [test-driven development approach](https://en.wikipedia.org/wiki/Test-driven_development) to ensure that your workloads behave as intended from all angles. For example, you can test if your workloads and cloud infrastructure meet the functional, non-functional, and security requirements that you require.



## What's next

  * Learn about how to [design scalable and resilient apps](https://docs.cloud.google.com/architecture/scalable-and-resilient-apps).
  * Read about [Google Cloud infrastructure reliability](https://docs.cloud.google.com/architecture/infra-reliability-guide).
  * To improve the reliability and the resilience of your environments, read about [Site Reliability Engineering (SRE)](https://cloud.google.com/sre).
  * Read about how to [architect your disaster recovery for cloud infrastructure outages](https://docs.cloud.google.com/architecture/disaster-recovery).
  * To learn about the migration framework, read [Migrate to Google Cloud: Get started](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started).
  * Learn where to [find help for your migrations](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started#finding_help).
  * Take the [Google Skills training course on migrating to Google Cloud](https://www.skills.google/course_templates/1561).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Author: [Marco Ferrari](https://www.linkedin.com/in/ferrarimark) | Cloud Solutions Architect

Other contributors: 

  * [Henry Bell](https://www.linkedin.com/in/henry-bell-uk) | Cloud Solutions Architect
  * [Elliot Eaton](https://www.linkedin.com/in/elliot-eaton-13a88052) | Cloud Solutions Architect
  * [Grace Mollison](https://www.linkedin.com/in/grace-mollison-6296614) | Solutions Lead
  * [Ido Flatow](https://www.linkedin.com/in/idoflatow) | Cloud Solutions Architect



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-12-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-12-08 UTC."],[],[]] 
