---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/ha-apps/overview/
title: High availability for your apps \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:58:32.262432+00:00
---

# High availability for your apps  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/ha-apps/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  High availability for your apps Stay organized with collections  Save and categorize content based on your preferences. 

This document provides technical guidance and best practices for designing and deploying highly available (HA) workloads across multiple zones in a Google Distributed Cloud (GDC) air-gapped universe. The guide outlines key architectural patterns, service configurations, and operational considerations to minimize downtime and ensure business continuity.

The strategies in this document are intended for the following technical professionals:

  * Cloud architects designing resilient infrastructure and application architectures.

  * DevOps engineers and site reliability engineers implementing deployment strategies, automation, monitoring, and incident response for HA workloads.

  * Application developers building fault-tolerant applications that integrate with HA patterns.




For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Importance of high availability

In modern distributed systems, planning for high availability is critical. Downtime can lead to significant business disruption, revenue loss, and poor user experience.

For workloads running in private data centers using GDC, availability often correlates directly with core operational success, especially for latency-sensitive or mission-critical applications. Designing for HA from the outset is essential to build resilient and reliable services.

GDC provides hyperscale capabilities within your air-gapped environment with multiple disconnected data centers, or _zones_. HA for your multi-zone apps depends on multi-zone services, such as load balancing and asynchronous storage. For more information about important services to use for HA, see the Scalability and load balancing and HA app deployment across zones with asynchronous storage sections of this document.

## Hyperscale capabilities, delivered locally

GDC extends Google Cloud infrastructure and services to the edge and your data centers. GDC provides a fully managed hardware and software solution, letting you run Google Kubernetes Engine (GKE) on GDC clusters and other Google Cloud services closer to where your data is generated and consumed.

This document focuses on GDC universes configured in a multi-zone topology. In this configuration, a single [universe](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/mz-overview#deployment-hierarchy-overview) comprises multiple, physically isolated [zones](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/mz-overview#understading-a-zone) within the same location.

These zones have independent power, cooling, and networking, providing protection against localized physical infrastructure failures. The low-latency, high-bandwidth network connectivity between zones enables data replication and rapid failover, forming the foundation for building highly available applications.

## Scalability and load balancing

Beyond basic component redundancy, managing traffic effectively and enabling seamless scaling are crucial for maintaining high availability, especially with varying load conditions. GDC provides several mechanisms for load balancing and sophisticated traffic management.

### External load balancer for north-south traffic

To expose your applications to users or systems outside a GKE on GDC cluster (north-south traffic), use GDC's managed external load balancing capabilities. The external load balancer (ELB) service provides these capabilities and integrates seamlessly with Kubernetes.

The key characteristics of the ELB service that provides HA and scalability are the following:

  * **Managed service** : runs as a GDC-specific service, and is designed for high availability and resilience in an air-gapped environment.

  * **External access** : provisions stable external IP addresses from GDC-managed pools, providing a consistent entry point for external clients.

  * **Load balancer integration with Kubernetes** : automatically provisions and configures the load balancer when you create a Kubernetes `Service` of `type: LoadBalancer` without specific internal annotations.

  * **Zone awareness** : distributes incoming traffic across healthy application pods running in all available zones within the GDC universe. The ELB relies on pod readiness probes to determine backend health.

  * **Scalability** : handles distribution of external traffic as your application scales horizontally across nodes and zones.




To achieve HA for external traffic ingress so client requests are automatically routed away from failing zones or instances, we recommend using an external load balancer.

For more information, see [Configure external load balancers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/elb-service).

### Internal load balancer for east-west traffic

For communication between services running within the same GKE on GDC cluster (east-west traffic), GDC provides an internal load balancer (ILB). An ILB is crucial for decoupling internal services and providing internal communication paths that are also highly available and scalable.

The key characteristics of the ILB service that provides HA and scalability are the following:

  * **Internal access** : provisions a stable internal IP address accessible only from within the GDC network, such as cluster nodes or other internal services.

  * **Load balancer integration with Kubernetes** : provisions load balancing by creating a Kubernetes `Service` of `type: LoadBalancer` with a specific annotation to indicate it must be internal. For example, `networking.gke.io/load-balancer-type: "Internal"`.

  * **Zone awareness** : distributes traffic across healthy backend pods, which are identified with readiness probes, located in all available zones. This distribution prevents internal communication failures if one zone experiences issues.

  * **Service discovery and decoupling** : provides a stable internal IP address and DNS name with kube-dns and CoreDNS integration. Services can discover and communicate with each other, removing the need for clients to know individual pod IP addresses.

  * **Scalability** : facilitates scaling of internal backend services by distributing traffic across all available healthy replicas.




Using an ILB for internal service-to-service communication makes internal traffic flow resilient to zone failures and provides effective scaling, complementing the HA provided by the external ELB and underlying compute distribution. This strategy is often used for tiered applications where frontend APIs must communicate with backend APIs or databases within the Kubernetes cluster.

For more information, see [Configure internal load balancers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/ilb-service).

## HA app deployment across zones with asynchronous storage

GDC lets you run infrastructure and applications closer to your data sources. To deploy HA applications with a resilient data source, implement asynchronous storage replication for data persistence and disaster recovery.

Zones represent distinct failure domains within a single universe. By distributing application components and replicating data across zones, you significantly improve resilience against localized hardware failures or maintenance events.

For more information, see [Data protection with multi-zone storage](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/data-protection).

## What's next

  * To deploy a service as a collection of virtual machines (VMs) distributed across zones using asynchronous replicated block storage, see [Deploy an HA VM app](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/ha-apps/deploy-ha-vm-app).

  * To deploy a service as a containerized application on Kubernetes across zones using asynchronously replicated persistent volumes, see [Deploy an HA container app](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/ha-apps/deploy-ha-container-app).

  * To learn more about zones and universes, see [Zones in GDC air-gapped](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/mz-overview).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
