---
url: https://docs.cloud.google.com/architecture/oracle-ebs-on-compute-engine-vm/
title: Oracle E-Business Suite with Oracle Database on Compute Engine \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:09.463416+00:00
---

# Oracle E-Business Suite with Oracle Database on Compute Engine  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/oracle-ebs-on-compute-engine-vm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Oracle E-Business Suite with Oracle Database on Compute Engine Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-02-09 UTC

This document provides reference architectures to help you build the infrastructure to run [Oracle E‑Business Suite](https://www.oracle.com/applications/ebusiness/) applications with Oracle Database on Compute Engine VMs in Google Cloud. Oracle E‑Business Suite is a suite of enterprise applications for business functions like finance, human resources, supply chain, and customer relationship.

The intended audience for this document is cloud architects and administrators of Oracle databases and Oracle E‑Business Suite applications. The document assumes that your team is familiar with Oracle Database and the [Oracle E‑Business Suite technology stack and architecture](https://docs.oracle.com/cd/E26401_01/doc.122/e22949/T120505T120508.htm).

If you need to use Oracle Exadata or Oracle Real Application Clusters (Oracle RAC), you can migrate your applications to Google Cloud and run your databases on Oracle Database@Google Cloud. For more information, see [Oracle E‑Business Suite on Compute Engine with Oracle Exadata](https://docs.cloud.google.com/architecture/oracle-ebs-with-oci-exadata).

## Architecture

Depending on your use case and requirements for availability and disaster recovery (DR), you can choose one of the following Google Cloud [deployment archetypes](https://docs.cloud.google.com/architecture/deployment-archetypes#what_is_a_deployment_archetype) to run Oracle E‑Business Suite applications on Google Cloud:

  * **Zonal** : Your applications run within a single Google Cloud zone. This deployment archetype is well suited for development and test environments and for non-critical applications that don't need high availability.
  * **Regional** : Your applications run independently in two or more zones within a single Google Cloud [region](https://docs.cloud.google.com/docs/geography-and-regions). We recommend this deployment archetype for applications that aren't mission-critical but need robustness against zone outages.
  * **Multi-regional** : Your applications run independently in multiple zones across two or more Google Cloud regions, either in active-active or active-passive mode. This deployment archetype is ideal to support DR scenarios. We recommend this archetype for mission-critical applications that need resilience to region outages and disasters.



Choosing an appropriate deployment archetype helps to simplify your subsequent decisions regarding the Google Cloud products and features that you need for your architecture.

The following sections present four architecture options. Each option is based on one of the deployment archetypes:

  * Zonal architecture
  * Zonal architecture with a DMZ
  * Regional architecture
  * Multi-regional active-passive (DR) architecture



### Zonal architecture

The following diagram shows an architecture for Oracle E‑Business Suite applications with Oracle Database running in a single zone within a Google Cloud region. This architecture is aligned with the [zonal deployment archetype](https://docs.cloud.google.com/architecture/deployment-archetypes/zonal).

![An architecture for Oracle E-Business Suite applications runs in a single zone within a Google Cloud region.](https://docs.cloud.google.com/static/architecture/images/oracle-ebs-on-compute-engine-vm-zonal.svg)![](https://docs.cloud.google.com/static/architecture/images/oracle-ebs-on-compute-engine-vm-zonal.svg)

The architecture in the preceding diagram includes the following components:

Component | Description  
---|---  
[Regional external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https) |  The load balancer distributes user requests to the Oracle E‑Business Suite applications.  
[Google Cloud Armor security policy](https://docs.cloud.google.com/armor/docs/security-policy-overview) |  The Cloud Armor security policy helps to protect your applications against threats like [DDoS](https://en.wikipedia.org/wiki/Denial-of-service_attack#Distributed_DoS) attacks and [XSS](https://en.wikipedia.org/wiki/Cross-site_scripting).  
Oracle E‑Business Suite (BYOL) |  The Oracle E‑Business Suite application-layer components (Oracle HTTP Server, Oracle WebLogic Server, and a concurrent processing server) run on [Compute Engine VMs](https://docs.cloud.google.com/compute/docs/overview). Each VM hosts an independent instance of the application layer. The boot disk for each VM is a [Google Cloud Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) volume. You bring your own licenses (BYOL) for Oracle E‑Business Suite, and you manage the VMs and the applications.  
Application binaries and data |  A [Filestore](https://docs.cloud.google.com/filestore/docs/overview) zonal instance contains the application binaries and data. The Filestore instance is mounted on the Compute Engine VMs that host the application-layer components.  
[Oracle Database](https://www.oracle.com/database/) (BYOL) |  The Oracle E‑Business Suite applications use an Oracle Database instance that's deployed on a Compute Engine VM. The boot and data disks for the VM are Hyperdisk volumes. You bring your own license (BYOL) for the Oracle Database instance, and you manage the VM and the database.  
Application and database backups |  Backups of the application data and the database are created, stored, and managed by using [Backup and DR Service](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr).  
[Virtual Private Cloud (VPC) network](https://docs.cloud.google.com/vpc/docs/vpc) and [subnets](https://docs.cloud.google.com/vpc/docs/subnets) |  All of the Google Cloud resources in the architecture use a single VPC network. The VMs that host the application layer and the database use separate subnets. Depending on your requirements, you can choose to build an architecture that uses multiple VPC networks. For more information, see [Deciding whether to create multiple VPC networks](https://docs.cloud.google.com/architecture/best-practices-vpc-design#decide-whether-to-create-multiple-vpcs).  
Public NAT gateway |  The architecture includes a public [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) gateway for secure outbound connections from the Compute Engine VMs, which have only internal IP addresses. For example, the VMs can access the [Oracle Linux Yum](https://yum.oracle.com/) server to download OS packages.  
[Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview) and [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) |  To connect your on-premises network to the VPC network in Google Cloud, you can use Cloud Interconnect or Cloud VPN. For information about the relative advantages of each approach, see [Choosing a Network Connectivity product](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product).  
  
### Zonal architecture with a DMZ

The following diagram shows an architecture with two independent Oracle E‑Business Suite application layers running on Compute Engine VMs. One of the application layers is a [demilitarized zone (DMZ)](https://en.wikipedia.org/wiki/DMZ_\(computing\)), which serves external users of the Oracle E‑Business Suite applications. The other layer serves internal users. Both of the application layers run within a single zone in a Google Cloud region and use a single Oracle Database instance. Like the architecture in the preceding section, this architecture is aligned with the [zonal deployment archetype](https://docs.cloud.google.com/architecture/deployment-archetypes/zonal).

![An architecture for Oracle E-Business Suite applications runs in a single zone with a DMZ within a Google Cloud region.](https://docs.cloud.google.com/static/architecture/images/oracle-ebs-on-compute-engine-vm-zonal-with-dmz.svg)![](https://docs.cloud.google.com/static/architecture/images/oracle-ebs-on-compute-engine-vm-zonal-with-dmz.svg)

The architecture in the preceding diagram includes the following components:

Component | Description  
---|---  
Regional external Application Load Balancer |  The external load balancer distributes requests from external users to the _external_ -facing application layer.  
[Regional internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal) |  The internal load balancer distributes requests from internal users to an _internal_ application layer.  
[Cloud Armor security policy](https://docs.cloud.google.com/armor/docs/security-policy-overview) |  The Cloud Armor security policy helps to protect your applications against external threats like DDoS attacks and XSS.  
Oracle E‑Business Suite (BYOL) |  The Oracle E‑Business Suite application-layer components (Oracle HTTP Server, Oracle WebLogic Server, and a concurrent processing server) run on [Compute Engine VMs](https://docs.cloud.google.com/compute/docs/overview). Each VM hosts an independent instance of the application layer. The internal and external applications are served from distinct sets of VMs. The boot disk for each VM is a [Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) volume. You bring your own licenses (BYOL) for Oracle E‑Business Suite, and you manage the VMs and the applications.  
Application binaries and data |  A [Filestore](https://docs.cloud.google.com/filestore/docs/overview) zonal instance contains the application binaries and data. The Filestore instance is mounted on the Compute Engine VMs that host the application-layer components.  
[Oracle Database](https://www.oracle.com/database/) (BYOL) |  The Oracle E‑Business Suite applications use an Oracle Database instance that's deployed on a Compute Engine VM. The boot and data disks for the VM are Hyperdisk volumes. You bring your own license (BYOL) for the Oracle Database instance, and you manage the VM and the database.  
Application and database backups |  Backups of the application data and database are created, stored, and managed by using [Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr).  
[Virtual Private Cloud (VPC) network](https://docs.cloud.google.com/vpc/docs/vpc) and [subnets](https://docs.cloud.google.com/vpc/docs/subnets) |  All of the Google Cloud resources in the architecture use a single VPC network. The VMs that host the application layer and the database use separate subnets. Depending on your requirements, you can choose to build an architecture that uses multiple VPC networks. For more information, see [Deciding whether to create multiple VPC networks](https://docs.cloud.google.com/architecture/best-practices-vpc-design#decide-whether-to-create-multiple-vpcs).  
Public NAT gateway |  The architecture includes a public [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) gateway for secure outbound connections from the Compute Engine VMs, which have only internal IP addresses. For example, the VMs can access the [Oracle Linux Yum](https://yum.oracle.com/) server to download OS packages.  
[Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview) and [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) |  To connect your on-premises network to the VPC network in Google Cloud, you can use Cloud Interconnect or Cloud VPN. Administrators and internal application users use these connections to access the resources and applications, respectively. For information about the relative advantages of each approach, see [Choosing a Network Connectivity product](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product).  
  
### Regional architecture

The following diagram shows an architecture where Oracle E‑Business Suite applications run in active-active mode on Compute Engine VMs that are distributed across two zones within a Google Cloud region. Both of the application deployments use a primary Oracle Database instance that runs on a VM in one of the zones. [Oracle Data Guard](https://docs.oracle.com/en/database/oracle/oracle-database/26/sbydb/introduction-to-oracle-data-guard-concepts.html) manages replication and failover of the database to a standby Oracle Database instance in the second zone. This architecture is based on the [regional deployment archetype](https://docs.cloud.google.com/architecture/deployment-archetypes/regional).

![An architecture for Oracle E-Business Suite applications runs in two zones within a Google Cloud region.](https://docs.cloud.google.com/static/architecture/images/oracle-ebs-on-compute-engine-vm-regional.svg)![](https://docs.cloud.google.com/static/architecture/images/oracle-ebs-on-compute-engine-vm-regional.svg)

The architecture in the preceding diagram includes the following components:

Component | Description  
---|---  
Regional external Application Load Balancer |  The load balancer distributes user requests to the Oracle E‑Business Suite applications.  
[Cloud Armor security policy](https://docs.cloud.google.com/armor/docs/security-policy-overview) |  The Cloud Armor security policy helps to protect your applications against threats like distributed DDoS attacks and XSS.  
Oracle E‑Business Suite (BYOL) |  The Oracle E‑Business Suite application-layer components (Oracle HTTP Server, Oracle WebLogic Server, and a concurrent processing server) run on [Compute Engine VMs](https://docs.cloud.google.com/compute/docs/overview) that are distributed across two zones. Each VM hosts an independent instance of the application layer. The boot disk for each VM is a [Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) volume. You bring your own licenses (BYOL) for Oracle E‑Business Suite, and you manage the VMs and the applications.  
Application binaries and data |  A [Filestore](https://docs.cloud.google.com/filestore/docs/overview) regional instance contains the application binaries and data. The Filestore instance is mounted on all of the Compute Engine VMs that host the application-layer components in both zones.  
[Oracle Database](https://www.oracle.com/database/) (BYOL) |  The Oracle E‑Business Suite applications use a primary-standby pair of Oracle Database instances that are deployed on Compute Engine VMs in separate zones. The boot and data disks for the VM are Hyperdisk volumes. Oracle Data Guard manages replication and failover of the database from the primary instance to the standby instance.  You bring your own licenses (BYOL) for the Oracle Database instances, and you manage the VMs and databases.  
Application and database backups |  Backups of the application data and database are created, stored, and managed by using [Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr).  
[Virtual Private Cloud (VPC) network](https://docs.cloud.google.com/vpc/docs/vpc) and [subnets](https://docs.cloud.google.com/vpc/docs/subnets) |  All of the Google Cloud resources in the architecture use a single VPC network. The VMs that host the application layer and database use separate subnets. Depending on your requirements, you can choose to build an architecture that uses multiple VPC networks. For more information, see [Deciding whether to create multiple VPC networks](https://docs.cloud.google.com/architecture/best-practices-vpc-design#decide-whether-to-create-multiple-vpcs).  
Public NAT gateway |  The architecture includes a public [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) gateway for secure outbound connections from the Compute Engine VMs, which have only internal IP addresses. For example, the VMs can access the [Oracle Linux Yum](https://yum.oracle.com/) server to download OS packages.  
[Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview) and [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) |  To connect your on-premises network to the VPC network in Google Cloud, you can use Cloud Interconnect or Cloud VPN. For information about the relative advantages of each approach, see [Choosing a Network Connectivity product](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product).  
  
### Multi-regional active-passive (DR) architecture

The following diagram shows an architecture where Oracle E‑Business Suite applications run in active-active mode on Compute Engine VMs that are distributed across two zones within a Google Cloud region. Both of the application deployments use a primary Oracle Database instance that runs on a VM in one of the zones. Oracle Data Guard manages replication and failover of the database to a standby Oracle Database instance in the second zone. The architecture includes a smaller scale replica of the application stack in a remote (failover) region for DR. Like the architecture in the preceding section, this architecture is based on the [regional deployment archetype](https://docs.cloud.google.com/architecture/deployment-archetypes/regional).

**Note:** If you need an active-active multi-regional architecture where the application runs and serves requests independently in two regions, you can use the [multi-regional deployment archetype](https://docs.cloud.google.com/architecture/multiregional-vms).

![An architecture for Oracle E-Business Suite applications runs in two zones within a Google Cloud region, with a replica in a remote region for DR.](https://docs.cloud.google.com/static/architecture/images/oracle-ebs-on-compute-engine-vm-multi-regional.svg)![](https://docs.cloud.google.com/static/architecture/images/oracle-ebs-on-compute-engine-vm-multi-regional.svg)

The architecture in the preceding diagram includes the following components:

Component | Description  
---|---  
DNS failover routing policy |  A [Cloud DNS](https://docs.cloud.google.com/dns/docs/overview) public zone that's configured with a failover routing policy routes user requests to the load balancer in the region that's serving requests.  
Regional external Application Load Balancer |  The load balancer distributes user requests to the Oracle E‑Business Suite applications.  
[Cloud Armor security policy](https://docs.cloud.google.com/armor/docs/security-policy-overview) |  The Cloud Armor security policy helps to protect your applications against threats like distributed DDoS attacks and XSS.  
Oracle E‑Business Suite (BYOL) |  The Oracle E‑Business Suite application-layer components (Oracle HTTP Server, Oracle WebLogic Server, and a concurrent processing server) run on [Compute Engine VMs](https://docs.cloud.google.com/compute/docs/overview) that are distributed across two zones in the primary region. Each VM hosts an independent instance of the application layer. The boot disk for each VM is a [Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) volume. You bring your own licenses (BYOL) for Oracle E‑Business Suite, and you manage the VMs and the applications.  
Application binaries and data |  A [Filestore](https://docs.cloud.google.com/filestore/docs/overview) regional instance in the primary region contains the application binaries and data. The Filestore instance is mounted on all of the Compute Engine VMs that host the application-layer components in both zones in the primary region. The Filestore instance is replicated to the failover region.  
[Oracle Database](https://www.oracle.com/database/) (BYOL) |  The Oracle E‑Business Suite applications use a primary-standby pair of Oracle Database instances that are deployed on Compute Engine VMs in separate zones in the primary region. The boot and data disks for the VM are Hyperdisk volumes. Oracle Data Guard manages replication and failover of the database from the primary instance to the standby instance.  You bring your own licenses (BYOL) for the Oracle Database instances, and you manage the VMs and databases.  
Application and database backups |  Backups of the application data and the database are created, stored, and managed by using [Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr).  
[Virtual Private Cloud (VPC) network](https://docs.cloud.google.com/vpc/docs/vpc) and [subnets](https://docs.cloud.google.com/vpc/docs/subnets) |  All of the Google Cloud resources in the architecture use a single VPC network. The VMs that host the application layer and database use separate regional subnets. Depending on your requirements, you can choose to build an architecture that uses multiple VPC networks. For more information, see [Deciding whether to create multiple VPC networks](https://docs.cloud.google.com/architecture/best-practices-vpc-design#decide-whether-to-create-multiple-vpcs).  
Public NAT gateway |  The architecture includes a public [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) gateway in each region for secure outbound connections from the Compute Engine VMs, which have only internal IP addresses. For example, the VMs can access the [Oracle Linux Yum](https://yum.oracle.com/) server to download OS packages.  
[Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview) and [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) |  To connect your on-premises network to the VPC network in Google Cloud, you can use Cloud Interconnect or Cloud VPN. For information about the relative advantages of each approach, see [Choosing a Network Connectivity product](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product).  
  
## Products used

These reference architectures use the following Google Cloud products:

  * [ Compute Engine](https://cloud.google.com/compute): A secure and customizable compute service that lets you create and run VMs on Google's infrastructure.
  * [ Google Cloud Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks): A network storage service that you can use to provision and dynamically scale block storage volumes with configurable and predictable performance. 
  * [ Filestore](https://cloud.google.com/filestore): A service that provides high-performance, fully managed file storage on Google Cloud that you can connect to a variety of client types. 
  * [ Backup and DR Service](https://cloud.google.com/backup-disaster-recovery): A secure, centrally-managed backup and recovery service for Google Cloud workloads that helps protect backup data from malicious or accidental deletion. 
  * [ Cloud DNS](https://cloud.google.com/dns): A service that provides resilient, low-latency DNS serving from Google's worldwide network. 
  * [ Cloud Load Balancing](https://cloud.google.com/load-balancing): A portfolio of high performance, scalable, global and regional load balancers. 
  * [ Google Cloud Armor](https://cloud.google.com/security/products/armor): A network security service that offers web application firewall (WAF) rules and helps to protect against DDoS and application attacks. 
  * [ Virtual Private Cloud (VPC)](https://cloud.google.com/vpc): A virtual system that provides global, scalable networking functionality for your Google Cloud workloads. VPC includes VPC Network Peering, Private Service Connect, private services access, and Shared VPC.
  * [ Cloud NAT](https://cloud.google.com/nat): A service that provides Google Cloud-managed high-performance network address translation. 
  * [ Cloud Interconnect](https://cloud.google.com/network-connectivity/docs/interconnect/concepts/overview): A service that extends your external network to the Google network through a high-availability, low-latency connection.
  * [ Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn): A service that securely extends your peer network to Google's network through an IPsec VPN tunnel.



These reference architectures use the following Oracle products:

  * Oracle E-Business Suite: A suite of applications for business operations like finance, human resources, and supply chain. 
  * Oracle Database: A relational database management system (RDBMS) that extends the relational model to an object-relational model. 
  * Oracle Data Guard: A set of services to create, maintain, manage, and monitor one or more standby databases. 



You're responsible for procuring licenses for the Oracle products that you deploy in Google Cloud, and you're responsible for complying with the terms and conditions of the Oracle licenses.

## Design considerations

This section describes design factors, best practices, and design recommendations that you should consider when you use these reference architectures to develop a topology that meets your specific requirements for security, reliability, operational efficiency, cost, and performance.

**Note:** The guidance in this section isn't exhaustive. Depending on the specific requirements of your application and the Google Cloud and third-party products and features that you use, there might be additional design factors and trade-offs that you should consider.

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

#### Database migration

When you plan to migrate on-premises Oracle Database deployments to Google Cloud, assess your current database environment and get configuration and sizing recommendations by using the [Database Migration Assessment (DMA)](https://googlecloudplatform.github.io/database-assessment/) tool.

To migrate on-premises data to Oracle database deployments in Google Cloud, you can use standard Oracle tools like [Oracle GoldenGate](https://www.oracle.com/integration/goldengate/).

#### Storage options

For the Compute Engine VMs in the architecture, you can use [Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) or [Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks) boot volumes. Hyperdisk volumes provide better performance, flexibility, and efficiency than Persistent Disk. With [Hyperdisk Balanced](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced), you can provision IOPS and throughput separately and dynamically, which lets you tune the volume to a wide variety of workloads.

To store application binaries, use [Filestore](https://docs.cloud.google.com/filestore/docs/overview). Files that you store in a [Filestore Regional](https://docs.cloud.google.com/filestore/docs/service-tiers#regional) instance are replicated synchronously across three zones within the [region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). This replication helps to ensure [high availability](https://cloud.google.com/filestore/sla) and robustness against zone outages. For robustness against region outages, you can replicate a Filestore instance to a different region. For more information, see [Instance replication](https://docs.cloud.google.com/filestore/docs/instance-replication#instance-replication).

When you design storage for your workloads, consider the functional characteristics of the workloads, resilience requirements, performance expectations, and cost goals. For more information, see [Design an optimal storage strategy for your cloud workload](https://docs.cloud.google.com/architecture/storage-advisor).

#### Network design

Choose a network design that meets your business and technical requirements. You can use a single VPC network or multiple VPC networks. For more information, see the following documentation:

  * [Deciding whether to create multiple VPC networks](https://docs.cloud.google.com/architecture/best-practices-vpc-design#decide-whether-to-create-multiple-vpcs)
  * [Decide the network design for your Google Cloud landing zone](https://docs.cloud.google.com/architecture/landing-zones/decide-network-design)



#### Data analytics

For advanced analytics, you can use the Google Cloud Cortex Framework to ingest data from your Oracle E‑Business Suite applications into BigQuery. For more information, see [Cortex Framework: integration with Oracle E‑Business Suite](https://docs.cloud.google.com/cortex/docs/v6/operational-oracle-ebs).

### Security, privacy, and compliance

This section describes factors to consider when you use these reference architectures to design a topology in Google Cloud that meets the security and compliance requirements of your workloads.

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

By default, the data that's stored in Hyperdisk volumes and in Filestore is encrypted using Google-owned and Google-managed encryption keys. As an additional layer of protection, you can choose to encrypt the Google-owned and managed key by using keys that you own and manage in Cloud Key Management Service (Cloud KMS). For more information, see [About disk encryption](https://docs.cloud.google.com/compute/docs/disks/disk-encryption) for Hyperdisk volumes and [Encrypt data with customer-managed encryption keys](https://docs.cloud.google.com/filestore/docs/cmek) for Filestore.

#### Network security

To control network traffic between the resources in the architecture, you must configure appropriate [Cloud Next Generation Firewall (NGFW) policies](https://docs.cloud.google.com/firewall/docs/about-firewalls).

#### More security considerations

When you build the architecture for your workload, consider the platform-level security best practices and recommendations that are provided in the [Enterprise foundations blueprint](https://docs.cloud.google.com/architecture/blueprints/security-foundations) and [Google Cloud Well-Architected Framework: Security, privacy, and compliance](https://docs.cloud.google.com/architecture/framework/security).

### Reliability

This section describes design factors to consider when you use these reference architectures to build and operate reliable infrastructure for your deployment in Google Cloud.

#### Robustness of the application layer against VM failures

With all of the architecture options in this document, if some (but not all) of the application VMs fail, the applications continue to be available because the load balancer forwards requests to other application VMs.

Sometimes an application VM might be running and available, but there might be issues with the application itself. The application might freeze, crash, or not have enough memory. In this scenario, the VM won't respond to load-balancer health checks, and the load balancer won't route traffic to the unresponsive VM.

#### Robustness of the database against VM failures

In a zonal architecture, if the database VM fails, you can restore the database to production on a new VM by using the backups that are stored in Backup and DR. After you restore the database, you need to connect the applications to the new database instance.

If [data consistency](https://en.wikipedia.org/wiki/Consistency_\(database_systems\)) is a priority, then set up a primary and a standby database instance, preferably on VMs that are in different zones as shown in Regional architecture. For replication and failover to the standby database instance, use Oracle Data Guard. You can configure Oracle Data Guard to replicate transactions to the standby database instance _before_ the primary database instance acknowledges the commits. The primary-standby database architecture involves additional costs for infrastructure and licensing.

In a regional or multi-regional architecture, if the VM that hosts the primary database fails, Oracle Data Guard initiates a failover to the standby Oracle Database instance. During the failover process, the applications can't access the database.

#### Robustness against zone outages

In a zonal architecture, if the zone that hosts your deployment has an outage, the applications and the database are down. You can restore the applications and database to production in a different zone or region by using the backups that are stored in Backup and DR.

In a regional architecture, if one of the zones has an outage, the load balancer forwards requests to instances of the applications that run in the other zone. Filestore continues to be available because the architecture uses the Filestore Regional service tier.

To ensure high availability of data in Hyperdisk volumes during a single-zone outage, you can use [Hyperdisk Balanced High Availability](https://docs.cloud.google.com/compute/docs/disks/about-regional-persistent-disk). When data is written to a Hyperdisk Balanced High Availability volume, the data is replicated synchronously between two zones in the same region.

#### Robustness against region outages

If a region outage occurs, the applications and the database are unavailable. You can restore the applications and database to production in a different region by using the backups that are stored in Backup and DR. To reduce the downtime, use the multi-regional active-passive (DR) architecture. After you bring up the applications and the database, you need to update the [DNS routing policy](https://docs.cloud.google.com/dns/docs/policies-overview#routing_policies) to route traffic to the load balancer in the failover region.

For business-critical applications that can't tolerate downtime even when a region outage occurs, use the [multi-regional active-active deployment archetype](https://docs.cloud.google.com/architecture/multiregional-vms).

#### VM capacity planning

To make sure that capacity for Compute Engine VMs is available when VMs need to be provisioned, you can create _reservations_. A reservation provides assured capacity in a specific zone for a specified number of VMs of a machine type that you choose. A reservation can be specific to a project, or shared across multiple projects. For more information about reservations, see [Choose a reservation type](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type).

#### Data durability

The architectures in this document use Backup and DR to create, store, and manage backups of Compute Engine VMs. Backup and DR stores backup data in its original, application-readable format. When required, you can restore workloads to production by directly using data from long-term backup storage and avoid the need to prepare or move data.

Backup and DR supports the following methods for creating backups:

  * **Backup vault storage** : The backup data is stored within the same region as the source data, and the data can't be changed or deleted.
  * **Self-managed storage** : Authorized users can modify or delete the backup data, and you can store data in multiple regions.



For more information, see the following documentation:

  * [Backup and DR overview](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)
  * [Backup and DR for Compute Engine instance backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-compute-engine)
  * [Backup and DR for Filestore and file systems](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-filesystems)
  * [Backup and DR for Oracle](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-for-oracle)



#### More reliability considerations

When you build the cloud architecture for your workload, review the reliability-related best practices and recommendations that are provided in the following documentation:

  * [Google Cloud infrastructure reliability guide](https://docs.cloud.google.com/architecture/infra-reliability-guide)
  * [Patterns for scalable and resilient apps](https://docs.cloud.google.com/architecture/scalable-and-resilient-apps)
  * [Designing resilient systems](https://docs.cloud.google.com/compute/docs/tutorials/robustsystems)
  * [Google Cloud Well-Architected Framework: Reliability](https://docs.cloud.google.com/architecture/framework/reliability)



### Cost optimization

This section provides guidance to optimize the cost of setting up and operating a Google Cloud topology that you build by using these reference architectures.

#### VM machine types

To help you optimize the resource utilization of your VM instances, Compute Engine provides [machine type recommendations](https://docs.cloud.google.com/compute/docs/instances/apply-machine-type-recommendations-for-instances). Use the recommendations to choose machine types that match your workload's compute requirements. For workloads with predictable resource requirements, you can customize the machine type to your needs and save money by using [custom machine types](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type).

#### Oracle product licenses

You're responsible for procuring licenses for the Oracle products that you deploy on Compute Engine, and you're responsible for complying with the terms and conditions of the Oracle licenses. For more information, see [Licensing Oracle Software in the Cloud Computing Environment](https://www.oracle.com/a/ocom/docs/cloud-licensing-070579.pdf).

#### More cost considerations

When you build the architecture for your workload, also consider the general best practices and recommendations that are provided in [Google Cloud Well-Architected Framework: Cost optimization](https://docs.cloud.google.com/architecture/framework/cost-optimization).

### Operational efficiency

This section describes the factors to consider when you use these reference architectures to design a Google Cloud topology that you can operate efficiently.

#### Oracle Linux images

For your VMs, you can use [Oracle Linux images](https://docs.cloud.google.com/compute/docs/images/os-details#oracle_linux) that are available in Compute Engine or you can [import Oracle Linux images](https://docs.cloud.google.com/compute/docs/images#oracle_linux) that you build and maintain.

You can also create and use [custom OS images](https://docs.cloud.google.com/compute/docs/images#custom_images) that include the configurations and software that your applications require. Group your custom images into a custom image family. An image family always points to the most recent image in that family, so your instance templates and scripts can use that image without you having to update references to a specific image version. Regularly update your custom images to include the security updates and patches that are provided by the OS vendor.

#### Application server to database connectivity

For connections from your applications to Oracle Database, we recommend that you use the database VM's [zonal internal DNS name](https://docs.cloud.google.com/compute/docs/internal-dns) rather than its IP address. Google Cloud automatically resolves the DNS name to the VM's primary internal IP address. An added advantage with this approach is that you don't need to reserve and assign static internal IP addresses for the database VMs.

#### Oracle documentation and support

Oracle products that run on Compute Engine VMs have similar operational concerns as Oracle products that run on-premises. However, you don't need to manage the underlying compute, networking, and storage infrastructure.

  * For guidance about operating and managing Oracle products, see the Oracle-provided documentation for the relevant product.
  * For information about Oracle's support policy for Oracle Database instances that you deploy in Google Cloud, see [Oracle Database Support for Non-Oracle Public Cloud Environments (Doc ID 2688277.1)](https://support.oracle.com/knowledge/Oracle%20Database%20Products/2688277_1.html).
  * For a summary of Oracle support policies for Oracle E‑Business Suite, see [EBS Certifications](https://blogs.oracle.com/ebstech/post/ebs-certifications).



#### Observability for Oracle applications

To implement observability for Oracle workloads deployed in Google Cloud, you can use [Google Cloud Observability](https://docs.cloud.google.com/stackdriver/docs) services or [Oracle Enterprise Manager](https://docs.oracle.com/en/enterprise-manager/). Choose an appropriate monitoring strategy depending on your requirements and constraints. For example, if you run other workloads in Google Cloud in addition to Oracle workloads, then you can use Google Cloud Observability services to build a unified monitoring dashboard for all of the workloads.

#### More operational considerations

When you build the architecture for your workload, consider the general best practices and recommendations for operational efficiency that are described in [Google Cloud Well-Architected Framework: Operational excellence](https://docs.cloud.google.com/architecture/framework/operational-excellence).

### Performance optimization

This section describes the factors to consider when you use these reference architectures to design a topology in Google Cloud that meets the performance requirements of your workloads.

#### Compute performance

Compute Engine offers a wide range of predefined and customizable machine types that you can choose from depending on the performance requirements of your workloads.

  * For the VMs that host the applications and the database, choose an appropriate machine type based on your performance requirements. For information about the machine types that support Hyperdisk volumes and that meet your performance and other requirements, see [Machine series comparison](https://docs.cloud.google.com/compute/docs/machine-resource#machine_type_comparison).
  * For the VM that hosts the Oracle Database instances, we recommend that you use a machine type in the [C4 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4_series) from the general-purpose machine family. C4 machine types provide consistently high performance for database workloads.



#### Network performance

Compute Engine has a per-VM limit for egress [network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth). This limit depends on the VM's machine type and whether traffic is routed through the same VPC network as the source VM. For VMs with certain machine types, to improve network performance, you can get a higher maximum egress bandwidth by enabling _Tier_1 networking_. For more information, see [Configure per VM Tier_1 networking performance](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration).

#### Hyperdisk storage performance

The architectures that are described in this document use Hyperdisk volumes for all of the boot disks of the VMs and for the database VM's data disks. Hyperdisk lets you scale performance and capacity dynamically. You can adjust the provisioned IOPS, throughput, and the size of each volume to match your workload's storage performance and capacity needs. The performance of Hyperdisk volumes depends on the Hyperdisk type and the machine type of the VMs to which the volumes are attached. For more information about Hyperdisk performance limits and tuning, see the following documentation:

  * [Machine types that support Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#machine-type-support)
  * [Hyperdisk performance limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#hd-performance-limits)
  * [Optimize Hyperdisk performance](https://docs.cloud.google.com/compute/docs/disks/optimize-hyperdisk)



#### More performance considerations

When you build the architecture for your workload, consider the general best practices and recommendations that are provided in [Google Cloud Well-Architected Framework: Performance optimization](https://docs.cloud.google.com/architecture/framework/performance-optimization).

## Deployment

To deploy an Oracle E‑Business Suite Vision demonstration environment in a single Google Cloud zone, use the [Terraform configuration sample](https://github.com/GoogleCloudPlatform/architecture-center-samples/blob/main/oracle-ebs-framework/README.md) that's available in GitHub. This sample isn't intended for production use cases.

## What's next

  * [Cloud Transformation with Google Cloud and Oracle](https://cloud.google.com/blog/products/databases/accelerating-cloud-transformation-with-google-cloud-and-oracle?e=48754805)
  * [Oracle MAA Reference Architectures](https://docs.oracle.com/en/database/oracle/oracle-database/23/haiad/)
  * [Enterprise application on Compute Engine VMs with Oracle Exadata in Google Cloud](https://docs.cloud.google.com/architecture/enterprise-app-oracle-exadata-database-compute-engine)
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Authors: 

  * [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer
  * [Samantha He](https://www.linkedin.com/in/samantha-he-05a98173) | Technical Writer



Other contributors: 

  * [Andy Colvin](https://www.linkedin.com/in/andycolvin) | Database Black Belt Engineer, Oracle on Google Cloud
  * [Balazs Pinter](https://www.linkedin.com/in/predy) | Staff Partner Solutions Architect
  * [Celia Antonio](https://www.linkedin.com/in/celia-antonio-13483a2a) | Database Customer Engineer
  * [Majed Al-Halaseh](https://www.linkedin.com/in/m-b-88b309164) | Customer Engineer, Infrastructure Modernization
  * [Marc Fielding](https://www.linkedin.com/in/mfielding) | Data Infrastructure Architect
  * [Mark Schlagenhauf](https://www.linkedin.com/in/mark-schlagenhauf-63b98) | Technical Writer, Networking
  * [Nelson Gonzalez](https://www.linkedin.com/in/nelgonzal) | Product Manager
  * [Michelle Burtoft](https://www.linkedin.com/in/michellecburtoft) | Senior Product Manager
  * [Sean Derrington](https://www.linkedin.com/in/seanderrington) | Group Product Manager, Storage
  * [Sekou Page](https://www.linkedin.com/in/sekoupage) | Outbound Product Manager
  * [Souji Madhurapantula](https://www.linkedin.com/in/soujanyamadhurapantula) | Group Product Manager
  * [Victor Moreno](https://www.linkedin.com/in/vimoreno) | Product Manager, Cloud Networking



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-09 UTC."],[],[]] 
