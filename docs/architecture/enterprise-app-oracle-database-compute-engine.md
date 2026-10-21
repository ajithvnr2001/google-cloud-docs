---
url: https://docs.cloud.google.com/architecture/enterprise-app-oracle-database-compute-engine/
title: Enterprise application with Oracle Database on Compute Engine \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:14.965762+00:00
---

# Enterprise application with Oracle Database on Compute Engine  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/enterprise-app-oracle-database-compute-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Enterprise application with Oracle Database on Compute Engine Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-08-13 UTC

This document provides a reference architecture to help you build the infrastructure to host a highly available enterprise application that uses an Oracle database, with the entire stack deployed on Compute Engine VMs. You can use this reference architecture to efficiently [rehost (lift and shift)](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started#rehost_lift_and_shift) on-premises applications that use Oracle databases to Google Cloud. This document also includes guidance to help you build an Oracle Database topology in Google Cloud that meets [Oracle's maximum availability architecture (MAA)](https://www.oracle.com/database/technologies/maximum-availability-architecture/) requirements. The intended audience for this document is cloud architects and Oracle database administrators. The document assumes that you're familiar with Compute Engine and Oracle Database.

If you use Oracle Exadata or Oracle Real Application Clusters (Oracle RAC) to run Oracle databases on-premises, you can efficiently migrate your applications to Google Cloud and run your databases on Oracle Database@Google Cloud. For more information, see [Enterprise application on Compute Engine with Oracle Exadata](https://docs.cloud.google.com/architecture/enterprise-app-oracle-exadata-database-compute-engine).

## Architecture

The following diagram shows the infrastructure for a multi-tier enterprise application that uses Oracle Database. The web tier, application tier, and Oracle Database instances are hosted on Compute Engine VMs. The web tier and application tier run in active-active mode on VMs that are distributed across two zones within a Google Cloud [region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). The primary and standby database instances are deployed in separate zones. This architecture is aligned with the [regional deployment archetype](https://docs.cloud.google.com/architecture/deployment-archetypes/regional), which helps to ensure that your Google Cloud topology is robust against single-zone outages1.

**Note:** You can adapt the architecture in this document to build a topology that's robust against regional outages by using the multi-regional deployment archetype. For more information, see [Multi-regional deployment on Compute Engine](https://docs.cloud.google.com/architecture/multiregional-vms) and also the guidance in the Reliability section later in this document.

![A multi-tier enterprise application uses Oracle Database on Compute Engine VMs.](https://docs.cloud.google.com/static/architecture/images/enterprise-app-oracle-database-compute-engine.svg)

![](https://docs.cloud.google.com/static/architecture/images/enterprise-app-oracle-database-compute-engine.svg)

The architecture that's shown in the preceding diagram includes the following components:

Component | Purpose  
---|---  
[Regional external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https) |  The regional external Application Load Balancer receives and distributes user requests to the web tier VMs.   
[Google Cloud Armor security policy](https://docs.cloud.google.com/armor/docs/security-policy-overview) |  The Cloud Armor security policy helps to protect your application stack against threats like distributed denial-of-service (DDoS) attacks and cross-site scripting (XSS).   
Regional [managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups) for the web tier  |  The web tier of the application is deployed on Compute Engine VMs that are part of a regional MIG. This MIG is the backend for the external Application Load Balancer. The MIG contains Compute Engine VMs in two zones. Each of these VMs hosts an independent instance of the web tier of the application.   
Regional internal Application Load Balancer |  The regional internal Application Load Balancer distributes traffic from the web tier VMs to the application tier VMs.   
Regional MIG for the application tier |  The application tier, such as an Oracle WebLogic Server cluster, is deployed on Compute Engine VMs that are part of a regional MIG. This MIG is the backend for the internal Application Load Balancer. The MIG contains Compute Engine VMs in two zones. Each VM hosts an independent instance of the application server.   
[Oracle Database](https://www.oracle.com/database/) instances deployed on Compute Engine VMs  |  The application in this architecture uses a primary-standby pair of Oracle Database instances that are deployed on Compute Engine VMs in separate zones. You bring your own licenses (BYOL) for these Oracle Database instances, and you manage the VMs and database instances.   
[Google Cloud Hyperdisk Storage Pools](https://docs.cloud.google.com/compute/docs/disks/storage-pools) |  The VMs in each zone (across all the tiers in the application stack) use Hyperdisk Balanced volumes from a Hyperdisk Storage Pool. Creating and managing all the disks in a single storage pool lets you improve capacity utilization and reduce operational complexity while maintaining the storage capacity and performance that the VMs need.   
[Oracle Data Guard FSFO](https://www.oracle.com/technical-resources/articles/smiley-fsfo.html) observer  |  The Oracle Data Guard Fast-Start Failover (FSFO) observer is a lightweight program that initiates automatic failover to the standby Oracle Database instance when the primary instance is unavailable. The observer runs on a Compute Engine VM in a zone that's different from the zones where the primary and standby database instances are deployed.   
[Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction) bucket  |  To store backups of the Oracle Database instances, this architecture uses a Cloud Storage bucket. To facilitate recovery of the database during a region outage, you can store the backups geo-redundantly in a [dual-region or multi-region bucket](https://docs.cloud.google.com/storage/docs/locations).   
[Virtual Private Cloud (VPC) network](https://docs.cloud.google.com/vpc/docs/vpc) and [subnet](https://docs.cloud.google.com/vpc/docs/subnets) |  All the Google Cloud resources in the architecture use a single VPC network and subnet. Depending on your requirements, you can choose to build an architecture that uses multiple VPC networks or multiple subnets. For more information, see [Deciding whether to create multiple VPC networks](https://docs.cloud.google.com/architecture/best-practices-vpc-design#decide-whether-to-create-multiple-vpcs).   
Public [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) gateway  |  The architecture includes a public Cloud NAT gateway to enable secure outbound connections from the Compute Engine VMs that have only internal IP addresses.   
[Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview) and [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) |  To connect your on-premises network to the VPC network in Google Cloud, you can use Cloud Interconnect or Cloud VPN. For information about the relative advantages of each approach, see [Choosing a Network Connectivity product](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product).   
[Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) and [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview) |  Cloud Monitoring helps you to observe the behavior, health, and performance of your application and Google Cloud resources. [Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent) collects metrics and logs from the Compute Engine VMs, including the VMs that host the Oracle Database instances. The agent sends logs to Cloud Logging and sends metrics to Cloud Monitoring.   
  
## Products used

This reference architecture uses the following Google Cloud products:

  * [ Compute Engine](https://cloud.google.com/compute): A secure and customizable compute service that lets you create and run VMs on Google's infrastructure.
  * [ Google Cloud Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks): A network storage service that you can use to provision and dynamically scale block storage volumes with configurable and predictable performance. 
  * [ Cloud Load Balancing](https://cloud.google.com/load-balancing): A portfolio of high performance, scalable, global and regional load balancers. 
  * [ Cloud Storage](https://cloud.google.com/storage): A low-cost, no-limit object store for diverse data types. Data can be accessed from within and outside Google Cloud, and it's replicated across locations for redundancy.
  * [ Virtual Private Cloud (VPC)](https://cloud.google.com/vpc): A virtual system that provides global, scalable networking functionality for your Google Cloud workloads. VPC includes VPC Network Peering, Private Service Connect, private services access, and Shared VPC.
  * [ Google Cloud Armor](https://cloud.google.com/security/products/armor): A network security service that offers web application firewall (WAF) rules and helps to protect against DDoS and application attacks. 
  * [ Cloud NAT](https://cloud.google.com/nat): A service that provides Google Cloud-managed high-performance network address translation. 
  * [ Cloud Monitoring](https://cloud.google.com/monitoring): A service that provides visibility into the performance, availability, and health of your applications and infrastructure. 
  * [ Cloud Logging](https://cloud.google.com/logging): A real-time log management system with storage, search, analysis, and alerting.
  * [ Cloud Interconnect](https://cloud.google.com/network-connectivity/docs/interconnect/concepts/overview): A service that extends your external network to the Google network through a high-availability, low-latency connection.
  * [ Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn): A service that securely extends your peer network to Google's network through an IPsec VPN tunnel.



This reference architecture uses the following Oracle products:

  * Oracle Database: A relational database management system (RDBMS) that extends the relational model to an object-relational model. 
  * Oracle Data Guard: A set of services to create, maintain, manage, and monitor one or more standby databases. 



You're responsible for procuring licenses for the Oracle products that you deploy in Google Cloud, and you're responsible for complying with the terms and conditions of the Oracle licenses.

## Design considerations

This section describes design factors, best practices, and design recommendations that you should consider when you use this reference architecture to develop a topology that meets your specific requirements for security, reliability, operational efficiency, cost, and performance.

The guidance in this section isn't exhaustive. Depending on the specific requirements of your application and the Google Cloud and third-party products and features that you use, there might be additional design factors and trade-offs that you should consider.

### System design

This section provides guidance to help you to choose Google Cloud regions for your deployment and to select appropriate Google Cloud services.

#### Region selection

When you choose the Google Cloud regions where your applications must be deployed, consider the following factors and requirements:

  * Availability of Google Cloud services in each region. For more information, see [Products available by location](https://cloud.google.com/about/locations#products-available-by-location).
  * Availability of Compute Engine machine types in each region. For more information, see [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).
  * End-user [latency](https://docs.cloud.google.com/network-intelligence-center/docs/performance-dashboard/how-to/view-google-cloud-latency#global-latency) requirements.
  * [Cost](https://cloud.google.com/products/calculator) of Google Cloud resources.
  * Cross-regional data transfer costs.
  * Regulatory requirements.
  * [Sustainability requirements](https://docs.cloud.google.com/architecture/framework/sustainability/low-carbon-regions).



Some of these factors and requirements might involve trade-offs. For example, the most cost-efficient region might not have the lowest carbon footprint. For more information, see [Best practices for Compute Engine regions selection](https://docs.cloud.google.com/solutions/best-practices-compute-engine-region-selection).

#### Compute infrastructure

The reference architecture in this document uses Compute Engine VMs for certain tiers of the application. Depending on the requirements of your application, you can choose from other Google Cloud compute services:

  * **Containers** : You can run [containerized](https://cloud.google.com/discover/what-are-containerized-applications) applications in [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview) clusters. GKE is a container-orchestration engine that automates deploying, scaling, and managing containerized applications.
  * **Serverless** : If you prefer to focus your IT efforts on your data and applications instead of setting up and operating infrastructure resources, then you can use [serverless](https://cloud.google.com/discover/what-is-serverless-computing) services like [Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run).



The decision of whether to use VMs, containers, or serverless services involves a trade-off between configuration flexibility and management effort. VMs and containers provide more configuration flexibility, but you're responsible for managing the resources. In a serverless architecture, you deploy workloads to a preconfigured platform that requires minimal management effort. For more information about choosing appropriate compute services for your workloads in Google Cloud, see [Hosting Applications on Google Cloud](https://cloud.google.com/hosting-options).

#### Storage options

For the Compute Engine VMs in the architecture, you can use [Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) or [Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks) boot volumes. Hyperdisk volumes provide better performance, flexibility, and efficiency than Persistent Disk. With [Hyperdisk Balanced](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced), you can provision IOPS and throughput separately and dynamically, which lets you tune the volume to a wide variety of workloads.

To store application binaries, use [Filestore](https://docs.cloud.google.com/filestore/docs/overview). Files that you store in a [Filestore Regional](https://docs.cloud.google.com/filestore/docs/service-tiers#regional) instance are replicated synchronously across three zones within the [region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). This replication helps to ensure [high availability](https://cloud.google.com/filestore/sla) and robustness against zone outages. For robustness against region outages, you can replicate a Filestore instance to a different region. For more information, see [Instance replication](https://docs.cloud.google.com/filestore/docs/instance-replication#instance-replication).

When you design storage for your workloads, consider the functional characteristics of the workloads, resilience requirements, performance expectations, and cost goals. For more information, see [Design an optimal storage strategy for your cloud workload](https://docs.cloud.google.com/architecture/storage-advisor).

#### Network design

Choose a network design that meets your business and technical requirements. You can use a single VPC network or multiple VPC networks. For more information, see the following documentation:

  * [Deciding whether to create multiple VPC networks](https://docs.cloud.google.com/architecture/best-practices-vpc-design#decide-whether-to-create-multiple-vpcs)
  * [Decide the network design for your Google Cloud landing zone](https://docs.cloud.google.com/architecture/landing-zones/decide-network-design)



### Security, privacy, and compliance

This section describes factors to consider when you use this reference architecture to design a topology in Google Cloud that meets the security and compliance requirements of your workloads.

#### Protection against external threats

To protect your application against threats like distributed-denial-of-service (DDoS) attacks and cross-site scripting (XSS), you can use Google Cloud Armor security policies. Each policy is a set of rules that specifies certain conditions that should be evaluated and actions to take when the conditions are met. For example, a rule could specify that if the source IP address of the incoming traffic matches a specific IP address or CIDR range, then the traffic must be denied. You can also apply preconfigured web application firewall (WAF) rules. For more information, see [Security policy overview](https://docs.cloud.google.com/armor/docs/security-policy-overview).

#### External access for VMs

In the reference architecture that this document describes, the Compute Engine VMs don't need inbound access from the internet. Don't assign [external IP addresses](https://docs.cloud.google.com/load-balancing/docs/backend-service#backend_vms_and_external_ip_addresses) to the VMs. Google Cloud resources that have only a private, internal IP address can still access certain Google APIs and services by using Private Service Connect or Private Google Access. For more information, see [Private access options for services](https://docs.cloud.google.com/vpc/docs/private-access-options).

To enable secure outbound connections from Google Cloud resources that have only private IP addresses, like the Compute Engine VMs in this reference architecture, you can use [Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/overview#benefits) or [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview#benefits).

#### Service account privileges

For the Compute Engine VMs in the architecture, instead of using the default service accounts, we recommend that you create dedicated service accounts and specify the resources that the service account can access. The default service account has a broad range of permissions, including some that might not be necessary. You can tailor dedicated service accounts to have only the essential permissions. For more information, see [Limit service account privileges](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts#limit-service-account-privileges).

#### SSH security

To enhance the security of SSH connections to the Compute Engine VMs in your architecture, implement [Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap/docs/concepts-overview) and [Cloud OS Login API](https://docs.cloud.google.com/compute/docs/oslogin). IAP lets you control network access based on user identity and Identity and Access Management (IAM) policies. Cloud OS Login API lets you control Linux SSH access based on user identity and IAM policies. For more information about managing network access, see [Best practices for controlling SSH login access](https://docs.cloud.google.com/compute/docs/connect/ssh-best-practices/login-access).

#### Disk encryption

By default, the data that's stored in Hyperdisk volumes is encrypted using Google-owned and Google-managed encryption keys. As an additional layer of protection, you can choose to encrypt the Google-owned data encryption keys by using keys that you own and manage in Cloud Key Management Service (Cloud KMS). For more information, see [About disk encryption](https://docs.cloud.google.com/compute/docs/disks/disk-encryption).

#### Network security

To control network traffic between the resources in the architecture, you must configure appropriate [Cloud Next Generation Firewall (NGFW) policies](https://docs.cloud.google.com/firewall/docs/about-firewalls).

#### More security considerations

When you build the architecture for your workload, consider the platform-level security best practices and recommendations that are provided in the [Enterprise foundations blueprint](https://docs.cloud.google.com/architecture/blueprints/security-foundations) and [Google Cloud Well-Architected Framework: Security, privacy, and compliance](https://docs.cloud.google.com/architecture/framework/security).

### Reliability

This section describes design factors to consider when you use this reference architecture to build and operate reliable infrastructure for your deployment in Google Cloud.

#### Robustness against VM failures

In the architecture that's shown in this document, if a Compute Engine VM in any of the tiers fails, the application can continue to process requests.

  * If a VM in the web tier or application tier crashes, the relevant [MIG recreates the VM automatically](https://docs.cloud.google.com/compute/docs/instance-groups/about-repair#automatic_repair). The load balancers forward requests to only the available web server instances and application server instances.
  * If the VM that hosts the primary Oracle Database instance fails, the Oracle Data Guard FSFO observer initiates an automatic failover to the standby Oracle Database instance.



#### VM autohealing

Sometimes the VMs that host your application might be running and available, but there might be issues with the application itself. The application might freeze, crash, or not have sufficient memory. To verify whether an application is responding as expected, you can configure application-based health checks as part of the autohealing policy of your MIGs. If the application on a particular VM isn't responding, the MIG autoheals (repairs) the VM. For more information about configuring autohealing, see [About repairing VMs for high availability](https://docs.cloud.google.com/compute/docs/instance-groups/about-repair).

#### Robustness against zone outages

If a zone outage occurs, the application remains available.

  * The web tier and application tier are available (and responsive) because the VMs are in regional MIGs. The regional MIGs ensure that new VMs are created automatically in the other zone to maintain the configured minimum number of VMs. The load balancers forward requests to the available web server VMs and application server VMs.
  * If an outage affects the zone that has the primary Oracle Database instance, then the Oracle Data Guard FSFO observer initiates an automatic failover to the standby Oracle Database instance. The FSFO observer runs on a VM in a zone that's different from the zones that have the primary and standby database instances.
  * To ensure high availability of data in Hyperdisk volumes during a single-zone outage, you can use [Hyperdisk Balanced High Availability](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced-ha). When data is written to a volume, the data is replicated synchronously between two zones in the same region.



#### Robustness against region outages

If both of the zones in the architecture have an outage or if a region outage occurs, then the application is unavailable. To reduce the downtime caused by multi-zone or region outages, you can implement the following approach:

  * Maintain a passive (failover) replica of the infrastructure stack in another Google Cloud region.
  * Use a [dual-region or multi-region Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/locations) to store the Oracle Database backups. The backups are replicated asynchronously across at least two geographic locations. With replicated database backups, your architecture maps to [Oracle's Maximum Availability Architecture (MAA) Silver tier](https://docs.oracle.com/en/database/oracle/oracle-database/23/haovw/ha-requirements-architecture.html#GUID-84D6D56D-468B-4848-ACD1-E28ABF487822).

To achieve faster replication for backups stored in dual-region buckets, you can use turbo replication. For more information, see [Data availability and durability](https://docs.cloud.google.com/storage/docs/availability-durability).

  * If an outage occurs in the primary region, use the database backup to restore the database and activate the application in the failover region. Use [DNS routing policies](https://docs.cloud.google.com/dns/docs/policies-overview#routing_policies) to route traffic to the load balancer in the failover region.




For business-critical applications that must continue to be available even when a region outage occurs, consider using the [multi-regional deployment archetype](https://docs.cloud.google.com/architecture/multiregional-vms). For the database tier, you can use Oracle Active Data Guard FSFO to automatically failover to a standby Oracle Database instance in the failover region. This approach maps to [Oracle's MAA Gold tier](https://docs.oracle.com/en/database/oracle/oracle-database/23/haovw/ha-requirements-architecture.html#GUID-84D6D56D-468B-4848-ACD1-E28ABF487822).

#### MIG autoscaling

To control the autoscaling behavior of your stateless MIGs, you can specify target utilization metrics, such as average CPU utilization. You can also configure schedule-based autoscaling for stateless MIGs. [Stateful MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs) can't be autoscaled. For more information, see [Autoscaling groups of instances](https://docs.cloud.google.com/compute/docs/autoscaler).

#### MIG size limit

When you decide the size of your MIGs, consider the default and maximum limits on the number of VMs that can be created in a MIG. For more information, see [Add and remove VMs from a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#increase_the_groups_size_limit).

#### VM placement

To improve the robustness of the architecture, you can create a [spread placement policy](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-spread-policies) and apply it to the MIG template. When the MIG creates VMs, it places the VMs within each zone on different physical servers (called _hosts_), so your VMs are robust against failures of individual hosts. For more information, see [Create and apply spread placement policies to VMs](https://docs.cloud.google.com/compute/docs/instances/use-spread-placement-policies).

#### VM capacity planning

To make sure that capacity for Compute Engine VMs is available when VMs need to be provisioned, you can create _reservations_. A reservation provides assured capacity in a specific zone for a specified number of VMs of a machine type that you choose. A reservation can be specific to a project, or shared across multiple projects. For more information about reservations, see [Choose a reservation type](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type).

#### Block storage availability

The architecture in this document uses a Hyperdisk Storage Pool in each zone to provide block storage for the Compute Engine VMs. You create a pool of block storage capacity for a zone. You then create Hyperdisk volumes in the storage pool and attach the volumes to VMs in the zone. The storage pool attempts to add capacity automatically to ensure that the utilization rate doesn't exceed 80% of the pool's provisioned capacity. This approach ensures that block storage space is available when required. For more information, see [How Hyperdisk Storage Pools work](https://docs.cloud.google.com/compute/docs/disks/storage-pools#how-storage-pools-work).

#### Stateful storage

A best practice in application design is to avoid the need for stateful local disks. But if the requirement exists, you can configure your persistent disks to be stateful to ensure that the data is preserved when the VMs are repaired or recreated. However, we recommend that you keep the boot disks stateless, so that you can update them to the latest images with new versions and security patches. For more information, see [Configuring stateful persistent disks in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-disks-in-migs).

#### Backup and recovery

The architecture in this document uses Cloud Storage to store database backups. If you choose the dual-region or multi-region [location type](https://docs.cloud.google.com/storage/docs/locations) for the Cloud Storage bucket, the backups are replicated asynchronously across at least two geographic locations. If a region outage occurs, you can use the backups to restore the database in another region. With a dual-region bucket, you can achieve faster replication by enabling the turbo replication option. For more information, see [Data availability and durability](https://docs.cloud.google.com/storage/docs/availability-durability).

You can use Backup and DR Service to create, store, and manage backups of Compute Engine VMs. Backup and DR Service stores backup data in its original, application-readable format. When required, you can restore workloads to production by directly using data from long-term backup storage without time-consuming data-movement or preparation activities. For more information, see the following documentation:

  * [Backup and DR for Compute Engine instance backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-compute-engine)
  * [Backup and DR for Oracle](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-oracle)



#### More reliability considerations

When you build the cloud architecture for your workload, review the reliability-related best practices and recommendations that are provided in the following documentation:

  * [Google Cloud infrastructure reliability guide](https://docs.cloud.google.com/architecture/infra-reliability-guide)
  * [Patterns for scalable and resilient apps](https://docs.cloud.google.com/architecture/scalable-and-resilient-apps)
  * [Designing resilient systems](https://docs.cloud.google.com/compute/docs/tutorials/robustsystems)
  * [Google Cloud Well-Architected Framework: Reliability](https://docs.cloud.google.com/architecture/framework/reliability)



### Cost optimization

This section provides guidance to optimize the cost of setting up and operating a Google Cloud topology that you build by using this reference architecture.

#### VM machine types

To help you optimize the resource utilization of your VM instances, Compute Engine provides [machine type recommendations](https://docs.cloud.google.com/compute/docs/instances/apply-machine-type-recommendations-for-instances). Use the recommendations to choose machine types that match your workload's compute requirements. For workloads with predictable resource requirements, you can customize the machine type to your needs and save money by using [custom machine types](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type).

#### VM provisioning model

If your application is fault tolerant, then [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot) can help to reduce your Compute Engine costs for the VMs in the application and web tiers. The cost of Spot VMs is significantly lower than regular VMs. However, Compute Engine might preemptively stop or delete Spot VMs to reclaim capacity.

Spot VMs are suitable for batch jobs that can tolerate preemption and don't have high availability requirements. Spot VMs offer the same machine types, options, and performance as regular VMs. However, when the resource capacity in a zone is limited, MIGs might not be able to scale out (that is, create VMs) automatically to the specified target size until the required capacity becomes available again.

#### VM resource utilization

The [autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler) capability of stateless MIGs enables your application to handle increases in traffic gracefully, and it helps you to reduce cost when the need for resources is low. [Stateful MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs) can't be autoscaled.

#### Oracle product licenses

You're responsible for procuring licenses for the Oracle products that you deploy on Compute Engine, and you're responsible for complying with the terms and conditions of the Oracle licenses. For more information, see [Licensing Oracle Software in the Cloud Computing Environment](https://www.oracle.com/a/ocom/docs/cloud-licensing-070579.pdf).

#### Block storage resource utilization

The architecture in this document uses a Hyperdisk Storage Pool in each zone to provide block storage for the Compute Engine VMs. You can improve the overall utilization of block storage capacity and reduce cost by using [Advanced capacity storage pools](https://docs.cloud.google.com/compute/docs/disks/storage-pools#advcap-pools), which use [thin provisioning](https://en.wikipedia.org/wiki/Thin_provisioning) and data reduction technologies to improve storage efficiency.

#### More cost considerations

When you build the architecture for your workload, also consider the general best practices and recommendations that are provided in [Google Cloud Well-Architected Framework: Cost optimization](https://docs.cloud.google.com/architecture/framework/cost-optimization).

### Operational efficiency

This section describes the factors to consider when you use this reference architecture to design a Google Cloud topology that you can operate efficiently.

#### VM configuration updates

To update the configuration of the VMs in a MIG (such as the machine type or boot-disk image), you create a new instance template with the required configuration and then apply the new template to the MIG. The MIG updates the VMs by using the update method that you choose: automatic or selective. Choose an appropriate method based on your requirements for availability and operational efficiency. For more information about these MIG update methods, see [Apply new VM configurations in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs).

#### Oracle Linux images

For your VMs, you can use [Oracle Linux images](https://docs.cloud.google.com/compute/docs/images/os-details#oracle_linux) that are available in Compute Engine or you can [import Oracle Linux images](https://docs.cloud.google.com/compute/docs/images#oracle_linux) that you build and maintain.

You can also create and use [custom OS images](https://docs.cloud.google.com/compute/docs/images#custom_images) that include the configurations and software that your applications require. Group your custom images into a custom image family. An image family always points to the most recent image in that family, so your instance templates and scripts can use that image without you having to update references to a specific image version. Regularly update your custom images to include the security updates and patches that are provided by the OS vendor.

#### Deterministic instance templates

If the instance templates that you use for your MIGs include startup scripts to install third-party software, make sure that the scripts explicitly specify software-installation parameters such as the software version. Otherwise, when the MIG creates the VMs, the software that's installed on the VMs might not be consistent. For example, if your instance template includes a startup script to install Apache HTTP Server 2.4 (the `apache2` package), then make sure that the script specifies the exact `apache2` version that should be installed, such as version `2.4.69`. For more information, see [Deterministic instance templates](https://docs.cloud.google.com/compute/docs/instance-templates/deterministic-instance-templates).

#### Block storage management

The architecture in this document uses a Hyperdisk Storage Pool in each zone to provide block storage for the Compute Engine VMs. Hyperdisk Storage Pools help to simplify storage management. Instead of allocating and managing capacity individually for numerous disks, you define a pool of capacity that can be shared across multiple workloads in a zone. You then create Hyperdisk volumes in the storage pool and attach the volumes to the VMs in the zone. The storage pool attempts to add capacity automatically to ensure that the utilization rate doesn't exceed 80% of the pool's provisioned capacity.

#### Application server to database connectivity

For connections from your application to Oracle Database, we recommend that you use the database VM's [zonal internal DNS name](https://docs.cloud.google.com/compute/docs/internal-dns) rather than its IP address. Google Cloud automatically resolves the DNS name to the VM's primary internal IP address. An added advantage with this approach is that you don't need to reserve and assign static internal IP addresses for the database VMs.

#### Oracle Database administration and support

When you run a self-managed Oracle Database instance on a Compute Engine VM, there are similar operational concerns as when you run Oracle Database on-premises. However, with a Compute Engine VM you no longer need to manage the underlying compute, networking, and storage infrastructure.

  * For guidance about operating and managing your Oracle Database instances, see the Oracle-provided documentation for the relevant release.
  * For information about Oracle's support policy for Oracle Database instances that you deploy in Google Cloud, see [Oracle Database Support for Non-Oracle Public Cloud Environments (Doc ID 2688277.1)](https://support.oracle.com/knowledge/Oracle%20Database%20Products/2688277_1.html).



#### Observability for Oracle applications

To implement observability for Oracle workloads deployed in Google Cloud, you can use [Google Cloud Observability](https://docs.cloud.google.com/stackdriver/docs) services or [Oracle Enterprise Manager](https://docs.oracle.com/en/enterprise-manager/). Choose an appropriate monitoring strategy depending on your requirements and constraints. For example, if you run other workloads in Google Cloud in addition to Oracle workloads, then you can use Google Cloud Observability services to build a unified monitoring dashboard for all of the workloads.

#### More operational considerations

When you build the architecture for your workload, consider the general best practices and recommendations for operational efficiency that are described in [Google Cloud Well-Architected Framework: Operational excellence](https://docs.cloud.google.com/architecture/framework/operational-excellence).

### Performance optimization

This section describes the factors to consider when you use this reference architecture to design a topology in Google Cloud that meets the performance requirements of your workloads.

#### Compute performance

Compute Engine offers a wide range of predefined and customizable machine types that you can choose from depending on the performance requirements of your workloads.

  * For the VMs that host the web tier and application tier, choose an appropriate machine type based on your performance requirements for those tiers. To get a list of the available machine types that support Hyperdisk volumes and that meet your performance and other requirements, use the [Machine series comparison](https://docs.cloud.google.com/compute/docs/machine-resource#machine_type_comparison) table.
  * For the VMs that host the Oracle Database instances, we recommend that you use a machine type in the [C4 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4_series) from the general-purpose machine family. C4 machine types provide consistently high performance for database workloads.



#### VM multithreading

Each virtual CPU (vCPU) that you allocate to a Compute Engine VM is implemented as a single hardware multithread. By default, two vCPUs share a physical CPU core. For applications that involve highly parallel operations or that perform floating point calculations (such as genetic sequence analysis, and financial risk modeling), you can improve performance by reducing the number of threads that run on each physical CPU core. For more information, see [Set the number of threads per core](https://docs.cloud.google.com/compute/docs/instances/set-threads-per-core).

VM multithreading might have licensing implications for some third-party software, like databases. For more information, read the licensing documentation for the third-party software.

#### Network performance

For workloads that need low inter-VM network latency within the application and web tiers, you can create a compact placement policy and apply it to the MIG template that's used for those tiers. When the MIG creates VMs, it places the VMs on physical servers that are close to each other. While a compact placement policy helps improve inter-VM network performance, a spread placement policy can help improve VM availability as described earlier. To achieve an optimal balance between network performance and availability, when you create a compact placement policy, you can specify how far apart the VMs must be placed. For more information, see [Placement policies overview](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview).

Compute Engine has a per-VM limit for egress [network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth). This limit depends on the VM's machine type and whether traffic is routed through the same VPC network as the source VM. For VMs with certain machine types, to improve network performance, you can get a higher maximum egress bandwidth by enabling [Tier_1 networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration).

#### Hyperdisk storage performance

The architecture that's described in this document uses Hyperdisk volumes for the VMs in all the tiers. Hyperdisk lets you scale performance and capacity dynamically. You can adjust the provisioned IOPS, throughput, and the size of each volume to match your workload's storage performance and capacity needs. The performance of Hyperdisk volumes depends on the Hyperdisk type and the machine type of the VMs to which the volumes are attached. For more information about Hyperdisk performance limits and tuning, see the following documentation:

  * [Machine types that support Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#machine-type-support)
  * [About Hyperdisk performance](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-performance)
  * [Hyperdisk performance limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits)
  * [Optimize Hyperdisk performance](https://docs.cloud.google.com/compute/docs/disks/optimize-hyperdisk)



#### More performance considerations

When you build the architecture for your workload, consider the general best practices and recommendations that are provided in [Google Cloud Well-Architected Framework: Performance optimization](https://docs.cloud.google.com/architecture/framework/performance-optimization).

## What's next

  * [Accelerating cloud transformation with Google Cloud and Oracle](https://cloud.google.com/blog/products/databases/accelerating-cloud-transformation-with-google-cloud-and-oracle?e=48754805)
  * [Oracle MAA Reference Architectures](https://docs.oracle.com/en/database/oracle/oracle-database/23/haiad/)
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Authors: 

  * [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer
  * [Samantha He](https://www.linkedin.com/in/samantha-he-05a98173) | Technical Writer



Other contributors: 

  * [Andy Colvin](https://www.linkedin.com/in/andycolvin) | Database Black Belt Engineer, Oracle on Google Cloud
  * [Jeff Welsch](https://www.linkedin.com/in/jeffwelsch) | Director, Product Management
  * [Lee Gates](https://www.linkedin.com/in/gatesl) | Group Product Manager
  * [Marc Fielding](https://www.linkedin.com/in/mfielding) | Data Infrastructure Architect
  * [Mark Schlagenhauf](https://www.linkedin.com/in/mark-schlagenhauf-63b98) | Technical Writer, Networking
  * [Michelle Burtoft](https://www.linkedin.com/in/michellecburtoft) | Senior Product Manager
  * [Rajesh Kasanagottu](https://www.linkedin.com/in/rajesh-kasanagottu-8bb870) | Engineering Manager
  * [Sekou Page](https://www.linkedin.com/in/sekoupage) | Outbound Product Manager
  * [Souji Madhurapantula](https://www.linkedin.com/in/soujanyamadhurapantula) | Group Product Manager
  * [Victor Moreno](https://www.linkedin.com/in/vimoreno) | Product Manager, Cloud Networking
  * [Yeonsoo Kim](https://www.linkedin.com/in/yeonsoolizkim) | Product Manager



* * *

  1. For more information about region-specific considerations, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). ↩




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-13 UTC."],[],[]] 
