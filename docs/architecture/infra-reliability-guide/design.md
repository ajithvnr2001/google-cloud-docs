---
url: https://docs.cloud.google.com/architecture/infra-reliability-guide/design/
title: Design reliable infrastructure for your workloads in Google Cloud \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:53.688777+00:00
---

# Design reliable infrastructure for your workloads in Google Cloud  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/infra-reliability-guide/design/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Design reliable infrastructure for your workloads in Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-09-23 UTC

As described in [Platform availability](https://docs.cloud.google.com/architecture/infra-reliability-guide/building-blocks#platform-availability), Google Cloud infrastructure is designed to support a target availability of 99.9% for a workload that's deployed in a single zone. The target availability is 99.99% for a multi-zone deployment1 and 99.999% for a multi-region deployment. This part of the [Google Cloud infrastructure reliability guide](https://docs.cloud.google.com/architecture/infra-reliability-guide) provides deployment guidance, example architectures, and design techniques that can help to protect your workloads against failures at the resource, zone, and region level.

## Avoid single points of failure

Applications are typically composed of multiple interdependent components, each designed to perform a specific function. These components are typically grouped into tiers based on the function that they perform and their relationship with the other components. For example, a content-serving application might have three tiers: a web tier containing a load balancer and web servers; an application tier with a cluster of application servers; and a data tier for persistence. If any component of this application stack depends on a single infrastructure resource, a failure of that resource can affect the availability of the entire stack. For example, if the application tier runs on a single VM, and if the VM crashes, then the entire stack is effectively unavailable. Such a component is a [single point of failure (SPOF)](https://en.wikipedia.org/wiki/Single_point_of_failure).

An application stack might have more than one SPOF. Consider the multi-tier application stack that's shown in the following diagram:

![Example application stack with potential single points of failure.](https://docs.cloud.google.com/static/architecture/images/infra-reliability-guide/spof.svg)

As shown in the preceding diagram, this example architecture contains a single load balancer, two web servers, a single application server, and a single database. The load balancer, application server, and database in this example are SPOFs. A failure of any of these components can cause user requests to the application to fail.

To remove the SPOFs in your application stack, distribute resources across locations and deploy redundant resources.

**Note:** You might accept the Google Cloud global load balancer as a SPOF considering the stringent controls in Google Cloud and the defense-in-depth measures that Google implements to prevent global outages. To help reduce the risk of failure, manage changes to the load balancer carefully. Also, avoid or minimize dependencies on non-data plane actions, such as creating a new load balancer.

## Distribute resources and create redundancy

Depending on the reliability requirements of your application, you can choose from the following deployment architectures:

Architecture | Workload recommendation  
---|---  
Multi-region | Workloads that are business-critical and where high availability (HA) is essential, such as retail and social media applications.  
Multi-zone | Workloads that need resilience against zone outages but can tolerate some downtime caused by region outages.  
Single-zone | Workloads that can tolerate downtime or can be deployed at another location when necessary with minimal effort.  
  
## Cost, latency, and operational considerations

When you design a distributed architecture with redundant resources, besides the availability requirements of the application, you must also consider the effects on operational complexity, latency, and cost.

In a distributed architecture, you provision and manage a higher number of resources. The volume of cross-location network traffic is higher. You also store and replicate more data. As a result, the cost of your cloud resources in a distributed architecture is higher, and operating such deployments involves more complexity. For business-critical applications, the availability advantage of a distributed architecture might outweigh the increased cost and operational complexity.

For applications that aren't business-critical, the high availability that a distributed architecture provides might not be essential. Certain applications have other requirements that are more important than availability. For example, batch computing applications require low-latency and high-bandwidth network connections between the VMs. A single-zone architecture might be well suited for such applications, and it can also help you reduce data transfer costs.

## Deployment architectures

This section presents the following architectural options to build infrastructure for your workloads in Google Cloud:

  * Single-zone deployment
  * Multi-zone deployment
  * Multi-region deployment with regional load balancing
  * Multi-region deployment with global load balancing



### Single-zone deployment

The following diagram shows a single-zone application architecture with redundancy in every tier, to achieve higher availability of the functions performed by each component:

![Deployment in a single zone.](https://docs.cloud.google.com/static/architecture/images/infra-reliability-guide/single-zone.svg)

As shown in the preceding diagram, this example architecture includes the following components:

  * A regional external Application Load Balancer to receive and respond to user requests.
  * A zonal managed instance group (MIG) as the backend for the regional external Application Load Balancer. The MIG has two Compute Engine VMs. Each VM hosts an instance of a web server.
  * A regional internal passthrough Network Load Balancer to handle communication between the web servers and application servers.
  * A second zonal MIG as the backend for the internal load balancer. This MIG contains two Compute Engine VMs. Each VM hosts an instance of an application server. 
  * A Cloud SQL database instance (Enterprise edition) that the application writes data to and reads from. The database is replicated manually to a second Cloud SQL database instance in the same zone.



#### Aggregate availability: Single-zone deployment

The following table shows the availability of each tier in the preceding single-zone architecture diagram:

**Resource** | **SLA**  
---|---  
External load balancer | 99.99%  
Web tier: Compute Engine VMs in a single zone | 99.9%  
Internal load balancer | 99.99%  
Application tier: Compute Engine VMs in a single zone | 99.9%  
Cloud SQL instance (Enterprise edition, HA configuration)  | 99.95%  
  
You can expect the Google Cloud infrastructure resources that are listed in the preceding table to provide the following aggregate availability and estimated maximum monthly downtime:

  * Aggregate availability: 0.9999 x 0.999 x 0.9999 x 0.999 x 0.9995 = 99.73% 
  * Estimated maximum monthly downtime: Approximately 1 hour and 57 minutes



This calculation considers only the infrastructure resources that are shown in the preceding architecture diagram. To assess the availability of an application in Google Cloud, you must also consider other factors, like the following:

  * The internal design of the application
  * The DevOps processes and tools used to build, deploy, and maintain the application, its dependencies, and the Google Cloud infrastructure



For more information, see [Factors that affect application reliability](https://docs.cloud.google.com/architecture/infra-reliability-guide#factors-that-affect-application-reliability). 

#### Effects of outages, and guidance for recovery

In a single-zone deployment architecture, if any component fails, the application can process requests if each tier contains at least one functioning component with adequate capacity. For example, if a web server instance fails, the load balancer forwards user requests to the other web server instances. If a VM that hosts a web server or application server crashes, the MIG ensures that a new VM is created automatically. If the database crashes, you must manually activate the second database and update the application server instances to connect to the database.

A zone outage or region outage affects the Compute Engine VMs and the Cloud SQL database instances in a single-zone deployment. A zone outage doesn't affect the load balancer in this architecture because it is a regional resource. However, the load balancer can't distribute traffic, because there are no available backends. If a zone outage occurs, you must wait for Google to resolve the outage, and then verify that the application works as expected.

The next section describes an architectural approach that you can use to distribute resources across multiple zones, which helps to improve the resilience of the application to zone outages.

### Multi-zone deployment

In a single-zone deployment, if a zone outage occurs, the application might not be able to serve requests until the issue is resolved. To help to improve the resilience of your application against zone outages, you can provision multiple instances of zonal resources (such as Compute Engine VMs) across two or more zones. For services that support region-scoped resources (such as Cloud Storage buckets), you can deploy regional resources.

The following diagram shows a highly available cross-zone architecture, with the components in each tier of the application stack distributed across two zones:

![Deployment in two zones.](https://docs.cloud.google.com/static/architecture/images/infra-reliability-guide/dual-zones.svg)

As shown in the preceding diagram, this example architecture includes the following components:

  * A regional external Application Load Balancer receives and responds to user requests.
  * A regional MIG is the backend for the regional external Application Load Balancer. The MIG contains two Compute Engine VMs in different zones. Each VM hosts an instance of a web server. 
  * A regional internal passthrough Network Load Balancer handles communication between the web servers and application servers.
  * A second regional MIG is the backend for the internal load balancer. This MIG has two Compute Engine VMs in different zones. Each VM hosts an instance of an application server.
  * A Cloud SQL instance (Enterprise edition) that's configured for HA is the database for the application. The primary database instance is replicated synchronously to a standby database instance.



#### Aggregate availability: Multi-zone deployment

The following table shows the availability of each tier in the preceding dual-zone architecture diagram:

**Resource** | **SLA**  
---|---  
External load balancer | 99.99%  
Web tier: Compute Engine VMs in separate zones | 99.99%  
Internal load balancer | 99.99%  
Application tier: Compute Engine VMs in separate zones | 99.99%  
Cloud SQL instance (Enterprise edition, HA configuration)  | 99.95%  
  
You can expect the Google Cloud infrastructure resources that are listed in the preceding table to provide the following aggregate availability and estimated maximum monthly downtime:

  * Aggregate availability: 0.9999 x 0.9999 x 0.9999 x 0.9999 x 0.9995 = 99.91% 
  * Estimated maximum monthly downtime: Approximately 39 minutes



This calculation considers only the infrastructure resources that are shown in the preceding architecture diagram. To assess the availability of an application in Google Cloud, you must also consider other factors, like the following:

  * The internal design of the application
  * The DevOps processes and tools used to build, deploy, and maintain the application, its dependencies, and the Google Cloud infrastructure



For more information, see [Factors that affect application reliability](https://docs.cloud.google.com/architecture/infra-reliability-guide#factors-that-affect-application-reliability). 

#### Effects of outages, and guidance for recovery

In a dual-zone deployment, if any component fails, the application can process requests if at least one functioning component with adequate capacity exists in each tier. For example, if a web server instance fails, the load balancer forwards user requests to the web server instance in the other zone. If a VM that hosts a web server or application server instance crashes, the MIG ensures that a new VM is created automatically. If the primary Cloud SQL database crashes, Cloud SQL automatically fails over to the standby database instance.

The following diagram shows the same architecture as the previous diagram and the effects of a zone outage on the availability of the application:

![Dual-zone deployment: zone outage scenario.](https://docs.cloud.google.com/static/architecture/images/infra-reliability-guide/dual-zones-outage.svg)

As shown in the preceding diagram, if an outage occurs at one of the zones, the load balancer in this architecture is not affected, because it is a regional resource. A zone outage might affect individual Compute Engine VMs and one of the Cloud SQL database instances. But the application remains available and responsive, because the VMs are in regional MIGs and the Cloud SQL database is configured for HA. The MIGs ensure that new VMs are created automatically to maintain the configured minimum number of VMs. If the primary Cloud SQL database instance is affected by a zone outage, Cloud SQL [fails over](https://docs.cloud.google.com/sql/docs/mysql/high-availability) automatically to the standby instance in the other zone. After Google resolves the outage, you must verify that the application runs as expected in all the zones where it's deployed.

For more information about region-specific considerations, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). 

If both the zones in this architecture have an outage, then the application is unavailable. The load balancer continues to be available unless a region-wide outage occurs. However, the load balancer can't distribute traffic, because there are no available backends. If a multi-zone outage or region outage occurs, you must wait for Google to resolve the outage, and then verify that the application works as expected.

The next sections present architectural options to protect your application against multi-zone outages and region outages. 

### Multi-region deployment with regional load balancing

In a single-zone or multi-zone deployment, if a region outage occurs, the application can't serve requests until the issue is resolved. To protect your application against region outages, you can distribute the Google Cloud resources across two or more regions.

The following diagram shows a highly available cross-region architecture, with the components in each tier of the application stack distributed across multiple regions:

![Multi-region deployment with regional load balancing.](https://docs.cloud.google.com/static/architecture/images/infra-reliability-guide/multi-region-regional-lb.svg)

![](https://docs.cloud.google.com/static/architecture/images/infra-reliability-guide/multi-region-regional-lb.svg)

As shown in the preceding diagram, this example architecture includes the following components:

  * A public Cloud DNS zone with a [routing policy](https://docs.cloud.google.com/load-balancing/docs/https/reg-applb-ha-overview) that steers traffic to two Google Cloud regions.
  * A regional external Application Load Balancer in each region to receive and respond to user requests.
  * The backend for each regional external Application Load Balancer is a regional MIG. Each MIG contains two Compute Engine VMs in different zones. Each of these VMs hosts an instance of a web server.
  * A regional internal passthrough Network Load Balancer in each region handles communication between the web servers and application servers.
  * A second pair of regional MIGs is the backend for the internal load balancers. Each of these MIGs contains two Compute Engine VMs in different zones. Each VM hosts an instance of an application server.
  * The application writes data to and reads from a multi-region Spanner instance. The multi-region configuration that's used in this architecture (`eur6`) includes four read-write replicas. The read-write replicas are provisioned equally across two regions and in separate zones. The multi-region Spanner configuration also includes a witness replica in a third region.



#### Aggregate availability: Multi-region deployment with regional load balancing

In the multi-region deployment that's shown in the preceding diagram, the load balancers and the VMs are provisioned redundantly in two regions. The DNS zone is a [ global resource](https://docs.cloud.google.com/architecture/infra-reliability-guide/building-blocks#global-resources), and the Spanner instance is a multi-region resource.

To calculate the aggregate availability of the Google Cloud infrastructure that's shown in this architecture, we must first calculate the aggregate availability of the resources in each region, and then consider the resources that span multiple regions. Use the following process:

  1. Calculate the aggregate availability of the infrastructure resources _per region_ ; that is, excluding the DNS and database resources: **Resource and SLA** | **SLA**  
---|---  
External load balancer | 99.99%  
Web tier: Compute Engine VMs in separate zones | 99.99%  
Internal load balancer | 99.99%  
Application tier: Compute Engine VMs in separate zones | 99.99%  
  
Aggregate availability per region: 0.9999 x 0.9999 x 0.9999 x 0.9999 = 99.96% 

  2. Calculate the aggregate availability of the infrastructure resources considering the dual-region redundancy of the load balancers and the Compute Engine VMs.

The theoretical availability is 1-(1-0.9996)(1-0.9996) = 99.999984%. However, the actual availability that you can expect is limited to the target availability for multi-region deployments, which is 99.999%. 

  3. Calculate the aggregate availability of all the infrastructure resources, including the Cloud DNS and Spanner resources:

     * Aggregate availability: 0.99999 x 1 x 0.99999 = 99.998%
     * Estimated maximum monthly downtime: Approximately 52 seconds



This calculation considers only the infrastructure resources that are shown in the preceding architecture diagram. To assess the availability of an application in Google Cloud, you must also consider other factors, like the following:

  * The internal design of the application
  * The DevOps processes and tools used to build, deploy, and maintain the application, its dependencies, and the Google Cloud infrastructure



For more information, see [Factors that affect application reliability](https://docs.cloud.google.com/architecture/infra-reliability-guide#factors-that-affect-application-reliability). 

#### Effects of outages, and guidance for recovery

If any component in this multi-region deployment fails but there is at least one functioning component with adequate capacity in each tier, the application continues to work. For example, if a web server instance fails, the regional external Application Load Balancer forwards user requests to the other web server instances in the region. Similarly, if one of the application server instances crashes, the internal load balancers send requests to the other application server instances. If any of the VMs crash, the MIGs ensure that new VMs are created automatically to maintain the minimum configured number of VMs.

An outage at a single zone doesn't affect the load balancers, because they are regional resources and are resilient to zone outages. A zone outage might affect individual Compute Engine VMs. But the web server and application server instances remain available, because the VMs are part of regional MIGs. The MIGs ensure that new VMs are created automatically to maintain the minimum configured number of VMs. The Spanner instance in this architecture uses a multi-region configuration, which is resilient to zone outages.

For information about how multi-region replication works in Spanner, see [ Regional and multi-region configurations](https://docs.cloud.google.com/spanner/docs/instance-configurations#multi-region-replication) and [ Demystifying Spanner multi-region configurations](https://cloud.google.com/blog/topics/developers-practitioners/demystifying-cloud-spanner-multi-region-configurations).

The following diagram shows the same multi-region architecture as the previous diagram and the effects of a single-region outage on the availability of the application:

![Multi-region deployment with regional load balancing: region outage scenario.](https://docs.cloud.google.com/static/architecture/images/infra-reliability-guide/multi-region-regional-lb-outage.svg)

![](https://docs.cloud.google.com/static/architecture/images/infra-reliability-guide/multi-region-regional-lb-outage.svg)

As shown in the preceding diagram, even if an outage occurs at both the zones in any region, the application remains available, because an independent application stack is deployed in each region. The DNS zone steers user requests to the region that's not affected by the outage. The multi-region Spanner instance is resilient to region outages. After Google resolves the outage, you must verify that the application runs as expected in the region that had the outage.

If any two of the regions in this architecture have outages, then the application is unavailable. Wait for Google to resolve the outages. Then, verify that the application runs as expected in all the regions where it's deployed.

For multi-region deployments, instead of using regional load balancers, you can consider using a global load balancer. The next section presents a multi-region deployment architecture that uses a global load balancer and describes the benefits and risks of that approach.

To learn how to design and configure Cloud DNS routing policies with regional external load balancers for multi-region resilience, see [ High availability for regional external Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https/reg-applb-ha-overview).

###  Multi-region deployment with global load balancing

The following diagram shows an alternative multi-region deployment that uses a global load balancer instead of regional load balancers:

![Multi-region deployment with global load balancing.](https://docs.cloud.google.com/static/architecture/images/infra-reliability-guide/multi-region-global-lb.svg)

![](https://docs.cloud.google.com/static/architecture/images/infra-reliability-guide/multi-region-global-lb.svg)

As shown in the preceding diagram, this architecture uses a global external Application Load Balancer (with Cloud CDN enabled) to receive and respond to user requests. Each forwarding rule of the load balancer uses a single external IP address; you don't need to configure a separate DNS record for each region. The backends for the global external Application Load Balancer are two regional MIGs. The load balancer routes requests to the region that's closest to the users.

All the other components in this architecture are identical to the architecture shown in  Multi-region deployment with regional load balancing.

**Note:** For internal load balancing between the web and application tiers, instead of regional internal load balancers, you can consider using [ cross-region internal load balancing](https://docs.cloud.google.com/load-balancing/docs/proxy-network-load-balancer#high_availability_and_cross-region_failover). If the application-tier MIG in a particular region is down, traffic from the web tier in that region is sent to the application-tier MIG in the other region. This pattern matches the [ Google Cloud global deployment archetype](https://docs.cloud.google.com/architecture/deployment-archetypes/global). 

####  Benefits and risks of global load balancing for multi-region deployments

To load-balance external traffic to an application that's distributed across multiple regions, you can use either a global load balancer or multiple regional load balancers.

The following are the benefits of an architecture that uses a global load balancer:

  * You need to manage only a single load balancer.
  * Global load balancers use a single anycast IP address to provide load balancing across Google Cloud regions.
  * Global load balancers are resilient to region outages, and provide automatic cross-region failover.
  * Global load balancers support the following features, which can help enhance the reliability of your deployments: 
    * Edge caching using [Cloud CDN](https://docs.cloud.google.com/cdn/docs/overview)
    * Ability to [ use highly durable Cloud Storage buckets as backends](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-buckets)
    * [Google Cloud Armor security policies](https://docs.cloud.google.com/armor/docs/security-policy-overview)



The following are the risks of an architecture that uses a global load balancer:

  * An incorrect configuration change to the global load balancer might make the application unavailable to users. For example, while updating the frontend of the global load balancer, if you accidentally delete a forwarding rule, the load balancer stops receiving user requests. The effect of this risk is lower in the case of a multi-region architecture that uses regional load balancers, because even if the regional load balancer in one of the regions is affected by a configuration error, the load balancers in the other regions continue to work. 
  * An infrastructure outage that affects [ global resources](https://docs.cloud.google.com/architecture/infra-reliability-guide/building-blocks#global-resources) might make the global load balancer unavailable.



To mitigate these risks, you must manage changes to the global load balancer carefully, and consider using defense-in-depth fallbacks where possible. For more information, see [ Recommendations to manage the risk of outages of global resources](https://docs.cloud.google.com/architecture/infra-reliability-guide/building-blocks#manage-risk-outages-global-resources).

#### Aggregate availability: Multi-region deployment with global load balancing

In the multi-region deployment that's shown in the preceding diagram, the VMs and the internal load balancers are deployed redundantly across two regions. The external load balancer is a [ global resource](https://docs.cloud.google.com/architecture/infra-reliability-guide/building-blocks#global-resources), and the Spanner instance is a multi-region resource.

To calculate the aggregate availability of this deployment, we first calculate the aggregate availability of the resources in each region, and then consider the resources that span multiple regions.

  1. Calculate the aggregate availability of the infrastructure resources _per region_ , excluding the external load balancer and the database: **Resource** | **SLA**  
---|---  
Web tier: Compute Engine VMs in separate zones | 99.99%  
Internal load balancer | 99.99%  
Application tier: Compute Engine VMs in separate zones | 99.99%  
  
Aggregate availability per region: 0.9999 x 0.9999 x 0.9999 = 99.97% 

  2. Calculate the aggregate availability of the infrastructure resources considering the dual-region redundancy of the internal load balancer and the Compute Engine VMs.

The theoretical availability is 1-(1-0.9997)(1-0.9997) = 99.999991%. However, the actual availability that you can expect is limited to the target availability for multi-region deployments, which is 99.999%.

  3. Calculate the aggregate availability of all the infrastructure resources, including the global load balancer and Spanner resources:

     * Aggregate availability: 0.99999 x 0.9999 x 0.99999 = 99.988%
     * Estimated maximum monthly downtime: Approximately 5 minutes and 11 seconds



This calculation considers only the infrastructure resources that are shown in the preceding architecture diagram. To assess the availability of an application in Google Cloud, you must also consider other factors, like the following:

  * The internal design of the application
  * The DevOps processes and tools used to build, deploy, and maintain the application, its dependencies, and the Google Cloud infrastructure



For more information, see [Factors that affect application reliability](https://docs.cloud.google.com/architecture/infra-reliability-guide#factors-that-affect-application-reliability). 

#### Effects of outages, and guidance for recovery

If any component in this architecture fails, the application continues to work if at least one functioning component with adequate capacity exists in each tier. For example, if a web server instance fails, the global external Application Load Balancer forwards user requests to the other web server instances. If an application server instance crashes, the internal load balancers send the requests to the other application server instances. If any of the VMs crash, the MIGs ensure that new VMs are created automatically to maintain the minimum configured number of VMs.

If an outage occurs at one of the zones in any region, the load balancer is not affected. The global external Application Load Balancer is resilient to zone and region outages. The internal load balancers are regional resources; they're resilient to zone outages. A zone outage might affect individual Compute Engine VMs. But the web servers and application servers remain available, because the VMs are part of regional MIGs. The MIGs ensure that new VMs are created automatically to maintain the minimum configured number of VMs. The Spanner instance in this architecture uses a multi-region configuration, which is resilient to zone outages.

The following diagram shows the same multi-region architecture as the previous diagram and the effects of a single-region outage on the availability of the application:

![Multi-region deployment with global load balancing: region outage scenario.](https://docs.cloud.google.com/static/architecture/images/infra-reliability-guide/multi-region-global-lb-outage.svg)

![](https://docs.cloud.google.com/static/architecture/images/infra-reliability-guide/multi-region-global-lb-outage.svg)

As shown in the preceding diagram, even if an outage occurs at both the zones in any region, the application remains available, because an independent application stack is deployed in each region. The global external Application Load Balancer routes user requests to the application in the region that's not affected by the outage. The multi-region Spanner instance is resilient to region outages. After Google resolves the outage, you must verify that the application runs as expected in the region that had the outage.

For information about how multi-region replication works in Spanner, see [ Regional and multi-region configurations](https://docs.cloud.google.com/spanner/docs/instance-configurations#multi-region-replication) and [ Demystifying Spanner multi-region configurations](https://cloud.google.com/blog/topics/developers-practitioners/demystifying-cloud-spanner-multi-region-configurations).

If any two of the regions in this architecture have outages, then the application is unavailable. The global external Application Load Balancer is available, but it can't distribute traffic because there are no available backends. Wait for Google to resolve the outages. Then, verify that the application runs as expected in all the regions where it's deployed.

Multi-region deployments can help ensure HA for your most critical business applications. To ensure business continuity during failure events, besides deploying the application across multiple regions, you must take certain additional steps. For example, you must perform [ capacity planning](https://docs.cloud.google.com/architecture/infra-reliability-guide/traffic-load#capacity-planning) to ensure that either sufficient capacity is reserved in all the regions or the risks associated with emergency autoscaling are acceptable. You must also implement operational practices for DR testing, managing incidents, verifying application status after incidents, and performing retrospectives.

To protect against global load balancer outages and configuration errors, you can implement an automated failover or bypass strategy by using Cloud DNS and regional backup load balancers. For more information, see [ Failover strategies for global external Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https/global-applb-failover-overview).

* * *

  1. For more information about region-specific considerations, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). ↩




[ Previous arrow_back  Assess reliability requirements  ](https://docs.cloud.google.com/architecture/infra-reliability-guide/requirements)

[ Next Manage traffic and load  arrow_forward  ](https://docs.cloud.google.com/architecture/infra-reliability-guide/traffic-load)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-23 UTC."],[],[]] 
