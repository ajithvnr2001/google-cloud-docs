---
url: https://docs.cloud.google.com/architecture/infra-reliability-guide/building-blocks/
title: Building blocks of reliability in Google Cloud \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:54.258039+00:00
---

# Building blocks of reliability in Google Cloud  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/infra-reliability-guide/building-blocks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Building blocks of reliability in Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-09-23 UTC

Google Cloud infrastructure services run in locations around the globe. The locations are divided into failure domains, called _regions_ and _zones_ , which are the foundational building blocks for designing reliable infrastructure for your cloud workloads.

A failure domain is a resource or a group of resources that can fail independently of other resources. A standalone Compute Engine VM is an example of a resource that's a failure domain. A Google Cloud region or zone is an example of a failure domain that consists of a group of resources. When an application is distributed redundantly across failure domains, it can achieve a higher aggregated level of availability than that provided by each failure domain.

This part of the [Google Cloud infrastructure reliability guide](https://docs.cloud.google.com/architecture/infra-reliability-guide) describes the building blocks of reliability in Google Cloud and how they affect the availability of your cloud resources.

## Regions and zones

_Regions_ are independent geographic areas that consist of _zones_. Zones and regions are logical abstractions of underlying physical resources. For more information about region-specific considerations, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). 

## Platform availability

Google Cloud infrastructure is designed to tolerate and recover from failures. Google continually invests in innovative approaches to maintain and improve the reliability of Google Cloud. The following capabilities of Google Cloud infrastructure help to provide a reliable platform for your cloud workloads:

  * Geographically separated regions to mitigate the effects of natural disasters and region outages on global services.
  * Hardware redundancy and replication to avoid single points of failure.
  * Live migration of resources during maintenance events. For example, during planned infrastructure maintenance, Compute Engine VMs can be moved to another host in the same zone by using [live migration](https://docs.cloud.google.com/compute/docs/instances/live-migration-process).
  * A secure-by-design infrastructure foundation for the physical infrastructure and software on which Google Cloud runs, and operational security controls to protect your data and workloads. For more information, see [Google infrastructure security design overview](https://docs.cloud.google.com/docs/security/infrastructure/design).
  * A high-performance backbone network that uses an advanced[ software-defined networking (SDN)](https://en.wikipedia.org/wiki/Software-defined_networking) approach to network management, with edge-caching services to deliver consistent performance that scales well.
  * Continuous monitoring and reporting. You can view the status of Google Cloud services in every location by using the [Google Cloud Service Health Dashboard](https://status.cloud.google.com/).
  * Annual, company-wide [Disaster Recovery Testing (DiRT) events](https://cloud.google.com/blog/products/management-tools/sre-principles-in-practice-for-business-continuity) to help ensure that Google Cloud services and internal business operations continue to run during a disaster.
  * A [change management approach](https://docs.cloud.google.com/docs/cloud-approach-to-change) that emphasizes reliability across all the phases of the software development lifecycle for any changes to the Google Cloud platform and services.



Google Cloud infrastructure is designed to support the following target levels of availability for most customer workloads:

Deployment location | Availability (uptime) % | Estimated maximum downtime  
---|---|---  
Single zone | 3 nines: 99.9% | 43.2 minutes in a 30-day month  
Multiple zones in a region | 4 nines: 99.99% | 4.3 minutes in a 30-day month  
Multiple regions | 5 nines: 99.999% | 26 seconds in a 30-day month  
**Note:** For more information about region-specific considerations, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). 

The availability percentages in the preceding table are targets. The uptime [Service Level Agreements (SLAs)](https://cloud.google.com/terms/sla) for specific Google Cloud services might be different from these availability targets. For example, the [uptime SLA for a Bigtable instance](https://cloud.google.com/bigtable/sla) depends on the number of [clusters](https://docs.cloud.google.com/bigtable/docs/instances-clusters-nodes#clusters), their distribution across locations, and the [routing policy](https://docs.cloud.google.com/bigtable/docs/app-profiles#routing) that you configure.

The minimum uptime SLA for a Bigtable instance with clusters in three or more regions is 99.999% if the _multi-cluster_ routing policy is configured. But, if the _single-cluster_ routing policy is configured, then the minimum uptime SLA is 99.9% regardless of the number of clusters and their distribution.

The diagrams in this section show Bigtable instances with varying cluster sizes and the consequent differences in their uptime SLAs.

### Single cluster

The following diagram shows a single-cluster Bigtable instance, with a minimum uptime SLA of 99.9%:

![Single-cluster Bigtable instance \(minimum uptime SLA: 99.9%\).](https://docs.cloud.google.com/static/architecture/images/infra-reliability-guide/bigtable-1cluster.svg)

### Multiple clusters

The following diagram shows a multi-cluster Bigtable instance in multiple zones within a single region, with multi-cluster routing (minimum uptime SLA: 99.99%):

![Multi-cluster Bigtable instance in multiple zones within a single region, with multi-cluster routing \(minimum uptime SLA: 99.99%\).](https://docs.cloud.google.com/static/architecture/images/infra-reliability-guide/bigtable-2clusters-2zones.svg)

### Multiple clusters

The following diagram shows a multi-cluster Bigtable instance in three regions, with multi-cluster routing (minimum uptime SLA: 99.999%):

![Multi-cluster Bigtable instance in three regions, with multi-cluster routing \(minimum uptime SLA: 99.999%\).](https://docs.cloud.google.com/static/architecture/images/infra-reliability-guide/bigtable-3clusters.svg)

## Aggregate infrastructure availability

This section describes how to calculate the aggregate availability of an infrastructure stack in Google Cloud. It describes the factors that influence aggregate availability and provides example calculations.

To run your applications in Google Cloud, you use infrastructure resources like VMs and databases. These infrastructure resources, together, constitute your application's infrastructure _stack_. The following diagram shows an example of an infrastructure stack in Google Cloud and the availability SLA for each resource in the stack:

![Dual-zone deployment.](https://docs.cloud.google.com/static/architecture/images/infra-reliability-guide/dual-zones-with-slas.svg)

This example infrastructure stack includes the following Google Cloud resources:

  * A regional external Application Load Balancer receives and responds to user requests.
  * A regional managed instance group (MIG) is the backend for the regional external Application Load Balancer. The MIG contains two Compute Engine VMs in different zones. Each VM hosts an instance of a web server.
  * An internal load balancer handles communication between the web servers and the application servers.
  * A second regional MIG is the backend for the internal load balancer. This MIG has two Compute Engine VMs in different zones. Each VM hosts an instance of an application server.
  * A Cloud SQL instance that's configured for HA is the database for the application. The primary database instance is replicated synchronously to a standby database instance.



The aggregate availability that you can expect from an infrastructure stack like the preceding example depends on the following factors:

  * Google Cloud SLAs
  * Resource redundancy
  * Stack depth



### Google Cloud SLAs

The uptime SLAs of the Google Cloud services that you use in your infrastructure stack influence the minimum aggregate availability that you can expect from the stack.

The following tables present a comparison of the uptime SLAs for some services:

**Compute services** | **Monthly Uptime SLA** | **Estimated maximum downtime in a 30-day month**  
---|---|---  
Compute Engine VM | [99.9%](https://cloud.google.com/compute/sla) | 43.2 minutes  
Google Kubernetes Engine (GKE) Autopilot pods in multiple zones | [99.9%](https://cloud.google.com/kubernetes-engine/sla) | 43.2 minutes  
Cloud Run service | [99.95%](https://cloud.google.com/run/sla) | 21.6 minutes  
**Database services** | **Monthly Uptime SLA** | **Estimated maximum downtime in a 30-day month**  
---|---|---  
Cloud SQL for PostgreSQL instance (Enterprise edition, HA configuration) | [99.95%](https://cloud.google.com/sql/sla) | 21.6 minutes  
AlloyDB for PostgreSQL instance (HA configuration) | [99.99%](https://cloud.google.com/alloydb/sla) | 4.3 minutes  
Spanner multi-region instance | [99.999%](https://cloud.google.com/spanner/sla) | 26 seconds  
  
For the SLAs of other Google Cloud services, see [Google Cloud Service Level Agreements](https://cloud.google.com/terms/sla).

As the preceding tables show, the Google Cloud services that you choose for each tier of your infrastructure stack directly affect the overall uptime that you can expect from the infrastructure stack. To increase the expected availability of a workload that's deployed on a Google Cloud resource, you can provision redundant instances of the resource, as described in the next section.

### Resource redundancy

Resource redundancy means provisioning two or more identical instances of a resource and deploying the same workload on all the resources in the group. For example, to host the web tier of an application, you might provision a MIG containing multiple, identical Compute Engine VMs.

If you distribute a group of resources redundantly across multiple failure domains—for example, two Google Cloud zones—the resource availability that you can expect from that group is higher than the uptime SLA of each resource in the group. This higher availability is because the probability that _every_ resource in the group fails at the same time is lower than the probability that resources in a single failure domain have a coordinated failure.

For example, if the availability SLA for a resource is 99.9%, the probability that the resource fails is 0.001 (1 minus the SLA). If you distribute a workload across two instances of this resource that are provisioned in separate failure domains, then the probability that both the resources fail at the same time is 0.000001 (that is, 0.001 x 0.001). This failure probability translates to a _theoretical_ availability of 99.9999% for the group of two resources. However, the actual availability that you can expect is limited to the target availability of the deployment location: 99.9% if the resources are in a single Google Cloud zone, 99.99% for a multi-zone deployment, and 99.999% if the redundant resources are distributed across multiple regions.

**Note:** For more information about region-specific considerations, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). 

### Stack depth

The depth of an infrastructure stack is the number of distinct tiers (or layers) in the stack. Each tier in an infrastructure stack contains resources that provide a distinct function for the application. For example, the middle tier in a three-tier stack might use Compute Engine VMs or a GKE cluster to host application servers. Each tier in an infrastructure stack typically has a tight interdependence with its adjacent tiers. That means if any tier of the stack is unavailable, the entire stack becomes unavailable.

You can calculate the expected aggregate availability of an N-tier infrastructure stack by using the following formula:

$$ tier1\\_availability * tier2\\_availability * tierN\\_availability $$ 

For example, if every tier in a three-tier stack is designed to provide 99.9% availability, then the aggregate availability of the stack is approximately 99.7% (0.999 x 0.999 x 0.999). That means, the aggregate availability of a multi-tier stack is lower than the availability of the tier that provides the least availability.

As the number of interdependent tiers in a stack increases, the aggregate availability of the stack decreases, as shown in the following table. Each example stack in the table has a different number of tiers and every tier is assumed to provide 99.9% availability.

**Tier** | **Stack A** | **Stack B** | **Stack C**  
---|---|---|---  
Frontend | 99.9% | 99.9% | 99.9%  
Application tier | 99.9% | 99.9% | 99.9%  
Middle tier | – | 99.9% | 99.9%  
Data tier | – | – | 99.9%  
**Aggregate availability of the stack** | **99.8%** | **99.7%** | **99.6%**  
**Estimated maximum downtime of the stack in a 30-day month** | **86 minutes** | **130 minutes** | **173 minutes**  
  
### Summary of design considerations

When you design your applications, consider the aggregate availability of the Google Cloud infrastructure stack.

  * The availability of each Google Cloud resource in your infrastructure stack influences the aggregate availability of the stack. When you choose Google Cloud services to build your infrastructure stack, consider the availability SLA of the services.
  * To improve the availability of the function (for example, compute or database) that's provided by a resource, you can provision redundant instances of the resource. When you design an architecture with redundant resources, besides the availability benefits, you must also consider the potential effects on operational complexity, latency, and cost.
  * The number of tiers in an infrastructure stack (that is, the depth of the stack) has an inverse relationship with the aggregate availability of the stack. Consider this relationship when you design or modify your stack.



For more example calculations of aggregate availability, see the following sections:

  * [Example calculation: Single-zone deployment](https://docs.cloud.google.com/architecture/infra-reliability-guide/design#single-zone-aa-calc)
  * [Example calculation: Multi-zone deployment](https://docs.cloud.google.com/architecture/infra-reliability-guide/design#dual-zone-aa-calc)
  * [Example calculation: Multi-region deployment with regional load balancing](https://docs.cloud.google.com/architecture/infra-reliability-guide/design#multi-region-regional-lb-aa-calc)
  * [Example calculation: Multi-region deployment with global load balancing](https://docs.cloud.google.com/architecture/infra-reliability-guide/design#multi-region-global-lb-aa-calc)



## Location scopes

The location scope of a Google Cloud resource determines the extent to which an infrastructure failure can affect the resource. Most resources that you provision in Google Cloud have one of the following location scopes: zonal, regional, multi-region, or global.

The location scope of some resource types is fixed; that is, you can't choose or change the location scope. For example, Virtual Private Cloud (VPC) networks are global resources, and Compute Engine virtual machines (VMs) are zonal resources. For certain resources, you can choose the location scope while provisioning the resource. For example, when you create a GKE cluster, you can choose to create a zonal or regional GKE cluster.

The following sections describe location scopes in more detail.

### Zonal resources

Zonal resources are deployed within a single zone in a Google Cloud region. The following are examples of zonal resources. This list is not exhaustive.

  * Compute Engine VMs
  * Zonal MIGs
  * Google Cloud Hyperdisk volumes
  * Single-zone GKE clusters
  * Filestore Basic and Zonal instances
  * Dataflow jobs
  * Cloud SQL instances
  * Managed Service for Apache Spark clusters on Compute Engine



A failure in a zone might affect the zonal resources that are provisioned within that zone. Zones are designed to minimize the risk of correlated failures with other zones in the region. A failure in one zone usually does not affect the resources in the other zones in the region. Also, a failure in a zone doesn't necessarily cause _all_ the infrastructure in that zone to be unavailable. The zone merely defines the expected boundary for the effect of a failure.

To protect applications that use zonal resources against zonal incidents, you can distribute or replicate the resources across multiple zones or regions. For more information, see [Design reliable infrastructure for your workloads in Google Cloud](https://docs.cloud.google.com/architecture/infra-reliability-guide/design).

### Regional resources

Regional resources are deployed redundantly across multiple zones within a region. The following are examples of regional resources. This list is not exhaustive.

  * Regional MIGs
  * Regional Cloud Storage buckets
  * Google Cloud Hyperdisk Balanced High Availability volumes
  * Regional GKE clusters with the default (multi-zone) configuration
  * VPC subnets
  * Regional external Application Load Balancers
  * Regional Spanner instances
  * Filestore Enterprise instances
  * Cloud Run services



Regional resources are resilient to incidents in a specific zone. A region outage can affect some or all the regional resources provisioned within that region. Such outages can be caused by natural disasters or by large-scale infrastructure failures.

**Note:** For more information about region-specific considerations, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). 

### Multi-region resources

Multi-region resources are distributed across specific regions. The following are examples of multi-region resources. This list is not exhaustive.

  * Dual-region and multi-region Cloud Storage buckets
  * Multi-region Spanner instances
  * Multi-cluster (multi-region) Bigtable instances
  * Multi-region key rings in Cloud Key Management Service



For a complete list of the Google Services that are available in multi-region configurations, see [Products available by location](https://cloud.google.com/about/locations#multi-region).

Multi-region resources are resilient to incidents in specific regions and zones. An infrastructure outage that occurs in multiple regions can affect the availability of some or all the multi-region resources that are provisioned in the affected regions.

### Global resources

Global resources are available across all Google Cloud locations. The following are examples of global resources. This list is not exhaustive.

  * Projects. For guidance and best practices about organizing your Google Cloud resources into folders and projects, see [Decide a resource hierarchy for your Google Cloud landing zone](https://docs.cloud.google.com/architecture/landing-zones/decide-resource-hierarchy).

  * VPC networks, including associated routes and firewall rules

  * Cloud DNS zones

  * Global external Application Load Balancers

  * Global key rings in Cloud KMS

  * Pub/Sub topics

  * Secrets in Secret Manager




For a complete list of the Google Services that are available globally, see [Global products](https://cloud.google.com/about/locations#global-products).

Global resources are resilient to zonal and regional incidents. These resources don't rely on infrastructure in any specific region. Google Cloud has systems and processes that help to minimize the risk of global infrastructure outages. Google also continually monitors the infrastructure, and quickly resolves any global outages.

The following table summarizes the relative resilience of zonal, regional, multi-region, and global resources to application and infrastructure issues. It also describes the effort required to set up these resources, and recommendations to mitigate the effects of outages.

Resource scope | Resilience | Recommendations to mitigate the effects of infrastructure outages  
---|---|---  
Zonal | Low | Deploy the resources redundantly in multiple zones or regions.  
Regional | Medium | Deploy the resources redundantly in multiple regions.  
Multi-region or global | High | Manage changes carefully, and use defense-in-depth fallbacks where possible. For more information, see Recommendations to manage the risk of outages of global resources.  
**Note:** For more information about region-specific considerations, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). 

## Recommendations to manage the risk of outages of global resources

To take advantage of the resilience of global resources to zone and region outages, you might consider using certain global resources in your architecture. Google recommends the following approaches to manage the risk of outages of global resources:

### Careful management of changes to global resources

Global resources are resilient to physical failures. The configuration for such resources is globally scoped. Thus, setting up and configuring a single global resource is easier than operating multiple regional resources. However, a critical error in the configuration of a global resource might make it a single point of failure (SPOF). For example, you might use a global load balancer as the frontend for a geographically-distributed application. A global load balancer is often a good choice for such an application. However, an error in the configuration of the load balancer can cause it to become unavailable across all geographies. To avoid this risk, you must manage configuration changes to global resources carefully. For more information, see [Control changes to global resources](https://docs.cloud.google.com/architecture/infra-reliability-guide/manage-and-monitor#control-changes-global-resources).

### Use of regional resources as defense-in-depth fallbacks

For applications that have exceptionally high availability requirements, regional [defense-in-depth](https://en.wikipedia.org/wiki/Defense_in_depth_\(computing\)) fallbacks can help minimize the effect of outages of global resources. Consider the example of a geographically-distributed application that has a global load balancer as the frontend. To ensure that the application remains accessible even if the global load balancer is affected by a global outage, you can deploy regional load balancers. You can configure the clients to prefer the global load balancer, but fail over to the nearest regional load balancer if the global load balancer is not available.

To protect against global load balancer outages and configuration errors, you can implement an automated failover or bypass strategy by using Cloud DNS and regional backup load balancers. For more information, see [Failover strategies for global external Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https/global-applb-failover-overview).

## Example architecture with zonal, regional, and global resources

Your cloud topology can include a combination of zonal, regional, and global resources, as shown in the following diagram. The following diagram shows an example architecture for a multi-tier application that's deployed in Google Cloud.

![Location scopes of Google Cloud resources.](https://docs.cloud.google.com/static/architecture/images/infra-reliability-guide/location-scopes.svg)

As shown in the preceding diagram, a global external Application Load Balancer receives client requests. The load balancer distributes the requests to the backend, which is a regional MIG that has two Compute Engine VMs. The application running on the VMs writes data to and reads from a Cloud SQL database. The database is configured for HA. The primary and standby instances of the database are provisioned in separate zones, and the primary database is replicated synchronously to the standby database. In addition, the database is backed up automatically to a multi-region bucket in Cloud Storage.

The following table summarizes the Google Cloud resources in the preceding architecture and the resilience of each resource to zone and region outages:

Resource | Resilience to outages  
---|---  
VPC network | VPC networks, including associated routes and firewall rules, are global resources. They are resilient to zone and region outages.  
Subnets | VPC subnets are regional resources. They are resilient to zone outages.  
Global external Application Load Balancer | Global external Application Load Balancers are resilient to zone and region outages.  
Regional MIG | Regional MIGs are resilient to zone outages.  
Compute Engine VMs | Compute Engine VMs are zonal resources. If a zone outage occurs, the individual Compute Engine VMs might be affected. However, the application can continue to serve requests because the backend for the load balancer is a regional MIG, and not standalone VMs.  
Cloud SQL instances | The Cloud SQL deployment in this architecture is configured for HA; that is, the deployment includes a primary-standby pair of database instances. The primary database is replicated synchronously to the standby database by using Hyperdisk Balanced High Availability volumes. 

  * If an outage occurs in the zone that hosts the primary database, the Cloud SQL service fails over to the standby database automatically. 
  * If a region outage occurs, you can restore the database in a different region by using the database backups.

  
Multi-region Cloud Storage bucket | Data that's stored in multi-region Cloud Storage buckets is resilient to single-region outages.  
Hyperdisk volumes | Hyperdisk volumes are zonal resources. For HA, you can use Hyperdisk Balanced High Availability volumes. Data is replicated synchronously across two zones in the same region. To prepare for recovery from region outages, you can schedule snapshots of Hyperdisk volumes and store the snapshots in a multi-region Cloud Storage bucket.  
**Note:** For more information about region-specific considerations, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). 

[ Previous arrow_back  Overview of reliability  ](https://docs.cloud.google.com/architecture/infra-reliability-guide)

[ Next Assess reliability requirements  arrow_forward  ](https://docs.cloud.google.com/architecture/infra-reliability-guide/requirements)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-23 UTC."],[],[]] 
