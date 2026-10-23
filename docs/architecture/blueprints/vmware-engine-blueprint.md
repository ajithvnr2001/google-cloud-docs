---
url: https://docs.cloud.google.com/architecture/blueprints/vmware-engine-blueprint/
title: Migrate to a Google Cloud VMware Engine platform \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:20.801501+00:00
---

# Migrate to a Google Cloud VMware Engine platform  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/blueprints/vmware-engine-blueprint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Migrate to a Google Cloud VMware Engine platform Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-09-17 UTC

Many enterprises want to move their VMware clusters to the cloud to take advantage of the cloud's scalability, resiliency, elasticity, and higher-level services like Vertex AI Studio and BigQuery. Enterprises also want to shift expenditures from a capital-intensive hardware model to a more flexible operational expense model. To help enterprises rapidly build an operational environment that follows Google Cloud best practices, we have created the _Google Cloud VMware Engine enterprise blueprint_. This blueprint provides you with a comprehensive guide to deploying an enterprise-ready VMware environment so that you can migrate your VM workloads to the cloud.

VMware Engine is a fully managed service that lets you run the VMware platform on Google Cloud. Your VMware workloads operate on dedicated Google Cloud hardware, fully integrated with Google Cloud services. Google takes care of the infrastructure, networking, and management. The blueprint lets you deploy a Google Cloud project that contains a VMware Engine private cloud, a Google-managed VMware Engine network, and the VPC network peering connections that let traffic flow end to end.

The VMware Engine enterprise blueprint includes the following:

  * [GitHub repositories](https://github.com/GoogleCloudPlatform/enterprise-gcve-foundation/tree/main) that contain the Terraform code and ancillary scripts that are necessary to deploy the VMware Engine platform
  * A guide to the architecture, networking, and security controls that you use the GitHub repositories to implement (this document)



The blueprint is designed to run on a foundation of base-level services, such as VPC networks. You can use the [enterprise foundation blueprint](https://docs.cloud.google.com/architecture/blueprints/security-foundations) or [Fabric FAST](https://github.com/GoogleCloudPlatform/cloud-foundation-fabric) to create the foundation for this blueprint.

This document is intended for cloud architects, cloud platform administrators, VMware Engine administrators, and VMware Engine engineers who can use the blueprint to build and deploy VMware clusters on Google Cloud. The blueprint focuses on the design and deployment of a new VMware Engine private cloud and assumes that you are familiar with VMware and the VMware Engine managed service.

## VMware Engine enterprise blueprint overview

The VMware Engine enterprise blueprint relies on a layered approach to enable the VMware Engine platform. The following diagram shows the interaction of various components of this blueprint with other blueprints and services.

![Blueprint layers and components.](https://docs.cloud.google.com/static/architecture/blueprints/vmware-engine-blueprint/images/gcve-layers.svg)

This diagram includes the following:

  * The [Google Cloud infrastructure](https://cloud.google.com/infrastructure) provides you with security capabilities such as [encryption at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption) and [encryption in transit](https://docs.cloud.google.com/docs/security/encryption-in-transit), as well as basic building blocks such as compute and storage.
  * The enterprise foundation provides you with a baseline of resources such as networking, identity, policies, monitoring, and logging. These resources let you rapidly adopt Google Cloud while meeting your organization's architectural requirements.
  * The VMware Engine enterprise blueprint provides you with the following:

    * A [VMware Engine network](https://docs.cloud.google.com/vmware-engine/docs/networking/vmware-engine-network)
    * private connectivity to Google Virtual Private Cloud networks, APIs, and services
    * A [VMware Engine private cloud](https://docs.cloud.google.com/vmware-engine/docs/concepts-private-cloud)
    * [Backup capabilities](https://docs.cloud.google.com/backup-disaster-recovery/docs/quickstarts/vmware-backup-recovery)
    * [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)
    * [Google Cloud Armor](https://docs.cloud.google.com/vmware-engine/docs/best-practices-security#use-cloud-armore-to-protect-web-services-ddos-attacks)
    * Use cases include [data center migrations](https://cloud.google.com/blog/products/cloud-migration/how-to-migrate-with-google-cloud-vmware-engine), data center elastic capacity expansion, [virtual desktop infrastructure (VDI)](https://docs.vmware.com/en/VMware-Horizon/2306/horizon-installation/GUID-9B5984F5-D0AF-4C78-A39A-52EBAEA604E9.html), and data center disaster recovery scenarios.
  * Deployment automation using a CI/CD pipeline provides you with the tools to automate the provisioning, configuration, and management of infrastructure. Automation helps you ensure consistent, reliable, and auditable deployments; minimize manual errors; and accelerate the overall development cycle.




## Architecture

The following diagram shows the architecture that the VMware Engine enterprise blueprint deploys.

![Architecture for the blueprint.](https://docs.cloud.google.com/static/architecture/blueprints/vmware-engine-blueprint/images/gcve-architecture.svg)

The blueprint deploys the following:

  * A Google Cloud project called _standalone VMware Engine project_ that contains a VMware Engine private cloud
  * A Google-managed project for the VMware Engine network
  * The VPC network peering connections so that traffic can flow from VMware Engine applications to clients



The VMware Engine private cloud consists of the following components:

  * **Management tools:** VLAN and subnet for ESXi hosts' management network, DNS server, vCenter Server
  * **Backup:** backup infrastructure for workload VMs
  * **Virtual machines:** workload VMs
  * **vCenter Server:** centralized management of private cloud vSphere environment
  * **NSX Manager:** provides a single interface to configure, monitor, and manage NSX-T networking and security services
  * **ESXi hosts:** hypervisor on dedicated nodes
  * **vSAN storage:** hyper-converged, software-defined storage platform
  * **NSX-T overlay network:** network virtualization and security software
  * **VMware HCX:** application migration and workload rebalancing across data centers and clouds



### Overview of VMware Engine networking

The VMware Engine network is a dedicated network that connects the VMware Engine private cloud, VPC networks, and on-premises environments. The VMware Engine network has the following capabilities:

  * **Private cloud connectivity:** each VMware Engine private cloud is connected to a VMware Engine network, allowing communication between workloads within the private cloud.
  * **VMware Engine network connectivity:** you can use [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering) to establish connectivity between VMware Engine networks and a Google VPC. This connectivity enables communication between workloads that run on VMware Engine and those running on other services in Google Cloud.
  * **On-premises connectivity:** to create a hybrid cloud solution, you can extend VMware Engine networks to on-premises data centers using Cloud VPN or Cloud Interconnect.
  * **Network services:** VMware Engine networks use various network services, including the following: 
    * [Cloud DNS](https://docs.cloud.google.com/dns/docs/overview) for name resolution of internal and external resources
    * [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) for internet access for private cloud workloads
    * VPC Network Peering for network connectivity to other VPCs and other VMware Engine networks
    * Private connectivity to Google Cloud APIs and services



With VMware Engine, you are responsible for creating and managing workload VMs using the VMware application management surface. Google Cloud is responsible for patching and upgrading the infrastructure components and remediating failed components.

### Key architectural decisions

Decision area | Decision | Decision reasoning  
---|---|---  
Foundation | You can implement the VMware Engine enterprise blueprint on the enterprise foundation blueprint, Fabric FAST, or on a foundation that meets the defined prerequisites. | Both the enterprise foundation blueprint and Fabric FAST provide the base capabilities that help enterprises adopt Google Cloud.  
Compute | You can deploy a single private cluster in a particular [region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) or you can deploy two private clusters in two regions.  | The single private cluster configuration allows for simplified management and cost optimization.  
The blueprint deploys one spare node. | A single spare node lets you have capacity to handle failures, maintenance events, and workload fluctuations while minimizing costs.  
Backup and disaster recovery are managed using the [Backup and DR Service](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr).  | Backup and DR lets you use a managed service and lessen the amount of administration that is required for a VMware Engine deployment.  
Networking | The blueprint enables hybrid connectivity. | Hybrid connectivity lets you connect your on-premises environment with your Google Cloud environment.  
Private cloud uses a private, routable, and contiguous IP space. | Contiguous IP space makes IP address management easier. When the IP space is routable, the private cloud can communicate with your on-premises resources.  
Internet access is provided through a Cloud Load Balancing and is protected by Cloud Armor. | Cloud Armor enhances the workload security posture, while the Cloud Load Balancing helps enable workload scalability and high availability.  
The blueprint enables Cloud DNS.  | Cloud DNS resolves internal and external names.   
  
### Platform personas

The blueprint uses two user groups: a _cloud platform engineering group_ and a _VMware platform engineering group_. These groups have the following responsibilities:

  * The cloud platform engineering group is responsible for the deployment of the foundation for the VMware Engine blueprint and the deployment of the blueprint.
  * The VMware platform engineering group is responsible for the configuration and operation of the VMware components that are part of the private cloud.



If you are deploying the blueprint on the enterprise foundation blueprint or Fabric FAST, the cloud platform engineering group is created as part of the initial deployment process. The VMware platform engineering group is deployed as part of this blueprint.

### Organization structure

The VMware Engine enterprise blueprint builds on the existing organizational structure of the enterprise foundation blueprint and Fabric FAST. It adds a standalone VMware Engine project in the production, non-production, and development environments. The following diagram shows the blueprint's structure.

![Organization hierarchy for the blueprint.](https://docs.cloud.google.com/static/architecture/blueprints/vmware-engine-blueprint/images/gcve-org-structure.svg)

### Networking

The VMware Engine enterprise blueprint provides you with the following networking options:

  * A single Shared VPC network for a VMware Engine private cloud
  * Two Shared VPC instances for a private cloud



Both options are deployed in a single region and let you manage traffic from your on-premises environment.

The following diagram shows a single Shared VPC network for a single region.

![Networking with a single Shared VPC network.](https://docs.cloud.google.com/static/architecture/blueprints/vmware-engine-blueprint/images/gcve-networking-sharedvpc.svg)

Separate Shared VPC instances let you group costs and network traffic to distinct business units, while maintaining logic separation in the VMware Engine private cloud. The following diagram shows multiple Shared VPC networks in a single region.

![Networking with multiple Shared VPC networks.](https://docs.cloud.google.com/static/architecture/blueprints/vmware-engine-blueprint/images/gcve-networking-privatecloud.svg)

### Private cloud network

Within the private cloud, networking is powered by NSX-T, which provides a software-defined networking layer with advanced features like micro-segmentation, routing, and load balancing. The VMware Engine blueprint creates a network for your VMware Engine service. This network is a single Layer 3 address space. Routing is enabled by default, allowing all private clouds and subnets within the region to communicate without extra configuration. As shown in the following diagram, when a private cloud is created, [multiple subnets](https://docs.cloud.google.com/vmware-engine/docs/concepts-vlans-subnets) are created consisting of a management subnets, service subnets, workload subnets, and edge service subnets.

![Private cloud network for this blueprint.](https://docs.cloud.google.com/static/architecture/blueprints/vmware-engine-blueprint/images/gcve-private-cloud.svg)

When you configure your private cloud, you must select a CIDR range that doesn't overlap with other networks in your private cloud, your on-premises network, your private cloud management network, or subnet IP address ranges in your VPC network. After you select a CIDR range, VMware Engine automatically [allocates IP addresses](https://docs.cloud.google.com/vmware-engine/docs/quickstart-networking-requirements#example_management_network_cidr_range_division) for various subnets. Using an example 10.0.0.0/24 CIDR range, the following table shows the blueprint's IP address ranges for its management subnets.

Subnet | Description | IP address range   
---|---|---  
System management  | VLAN and subnet for the ESXi hosts' management network, DNS server, and vCenter Server  | 10.0.0.0/26   
VMotion  | VLAN and subnet for the vMotion network for ESXi hosts  | 10.0.0.64/28   
HCX uplink  | Uplink for HCX IX (mobility) and NE (extension) appliances to reach their peers and enable the creation of the HCX service mesh  | 10.0.0.216/29   
  
The workload VMs are contained in the NSX-T subnet. NST-T edge uplinks provide external connectivity. Your [private cloud CIDR range size](https://docs.cloud.google.com/vmware-engine/docs/quickstart-networking-requirements#vspherevsan_subnets_cidr_range_size) defines the number of ESXi nodes that can be supported in the NST-T subnet. ESXi nodes use the VSAN subnet for storage transport.

The following table shows the IP address ranges for the NSX-T host transport subnet, NSX-T edge uplink subnets, and VSAN subnets, based on a 10.0.0.0/24 CIDR range.

Subnet | Description | IP address range  
---|---|---  
VSAN  | The VSAN subnet is responsible for storage traffic between ESXI hosts and VSAN storage clusters.  | 10.0.0.80/28   
NSX-T host transport  | The VLAN and subnet for the ESXi host zone that is responsible for network connectivity, allowing firewalling, routing, load balancing, and other network services.  | 10.0.0.128/27   
NSX-T edge uplink-N [N=1-4]  | The NSX-T edge uplink lets external systems access services and applications running on the NSX-T network.  | 

  * 10.0.0.160/29
  * 10.0.0.168/29
  * 10.0.0.176/29
  * 10.0.0.184/29

  
  
For service subnets and the edge service subnet, the VMware Engine doesn't allocate a CIDR range or prefix. Therefore, you must specify a non-overlapping CIDR range and prefix. The following table shows the blueprint's CIDR blocks for the service subnets and the edge service subnet.

Subnet | Description | IP address range  
---|---|---  
Service-N [N=1-5]  | Service subnets let virtual machines bypass NSX transport and communicate directly with Google Cloud networking to enable high-speed communications.  | 

  * 10.0.2.0/24
  * 10.0.3.0/24
  * 10.0.4.0/24
  * 10.0.5.0/24

  
Edge service  | Required if optional edge services, such as point-to-site VPN, internet access, and external IP address are enabled. Ranges are determined for each region.  | 10.0.1.0/26   
  
#### Routing

Except for networks that are stretched from your on-premises network or from other VMware Engine private clouds, all communications within VMware Engine and to external IP addresses is routed (over Layer 3) by default. The blueprint configures a Cloud Router that is associated with the on-premises hybrid connection (using Cloud VPN or Cloud Interconnect) with summary [custom advertised routes](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/advertising-overview) for the VMware Engine IP address ranges. NSX segment routes are summarized at the Tier-0 level. The blueprint enables DHCP services through the [NSX-T DHCP Relay](https://docs.vmware.com/en/VMware-NSX-T-Data-Center/3.2/administration/GUID-C534FAED-EF68-4004-9487-FE4DFE83EDAA.html) to the DHCP services that are set up in the VMware Engine private cloud.

#### DNS configuration

VMware Engine lets you use a Cloud DNS zone in your project as a single DNS resolution endpoint for all connected management appliances in a peered VPC network. You can do this even if your private clouds are deployed across different regions.

When configuring address resolution for multiple and single private clouds, you can set up global address resolution using Cloud DNS.

By default, you can resolve the management zone from any of your VPC networks that has Cloud DNS enabled.

When the blueprint creates a private cloud that is linked to a standard VMware Engine network, an associated management DNS zone is created and auto-populated with the management appliances entries.

If the standard VMware Engine network is a VPC network that is peered with a VPC or another VMware Engine network, the blueprint automatically creates a management DNS zone binding. This zone binding ensures resolution of management appliances from your Google Cloud VMs on that network. The following diagram shows the Cloud DNS topology.

![The DNS configuration in the blueprint.](https://docs.cloud.google.com/static/architecture/blueprints/vmware-engine-blueprint/images/gcve-dns-configuration.svg)

#### Outbound traffic from VMware Engine to the internet

The blueprint provides you with the following three options for outbound traffic going from VMware Engine to the internet:

  1. Outbound through the customer's on-premises environment
  2. Outbound through the VMware Engine Internet Gateway
  3. Outbound through the customer's attached VPC using an external IP address



The following diagram shows these options.

![Outbound traffic options for VMware Engine.](https://docs.cloud.google.com/static/architecture/blueprints/vmware-engine-blueprint/images/gcve-egress-traffic.svg)

#### Inbound traffic from the internet to VMware Engine

The blueprint provides you with the following three options for traffic coming from the internet to VMware Engine:

  1. Inbound through the customer's on-premises environment
  2. Inbound through a customer VPC with Cloud Load Balancing and potentially Cloud Armor
  3. Inbound through VMware Engine using an external IP address



The following diagram shows these options.

![Inbound traffic options for VMware Engine.](https://docs.cloud.google.com/static/architecture/blueprints/vmware-engine-blueprint/images/gcve-ingress-traffic.svg)

### Logging

The blueprint lets you send the VMware Engine [administrative actions](https://docs.cloud.google.com/vmware-engine/docs/audit-logging) to [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit) using a [log sink](https://docs.cloud.google.com/logging/docs/routing/overview#sinks). By analyzing the VMware Engine audit logs, administrators can identify suspicious behavior, investigate incidents, and demonstrate compliance with regulatory requirements.

Logging exports can also serve as ingestion sources for security information and event management (SIEM) systems. Google supports the following ingestion sources that serve VMware Engine:

  * The hosting Google Cloud organization which includes cloud fabric and assets telemetry
  * VMware service components
  * Workloads running within VMware Engine



[Google SecOps](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview) includes a built-in automated log ingestion pipeline for ingesting organization data, and provides forwarding systems to push streaming telemetry from VMware Engine and workloads into the Google SecOps ingestion pipeline. Google SecOps enriches telemetry with contextual content and makes it searchable. You can use Google SecOps to find and track security issues as they develop.

### Monitoring

The blueprint installs a [standalone agent for Cloud Monitoring](https://docs.cloud.google.com/vmware-engine/docs/environment/howto-cloud-monitoring-standalone) to forward metrics from your private cloud to Cloud Monitoring. The blueprint sets up [predefined dashboards](https://docs.cloud.google.com/vmware-engine/docs/concepts-monitoring#cloud-monitoring-dashboards) that provide an overview of your VMware Engine resources and resource utilization. In VMware vCenter Server, VMware provides tools to help you monitor your environment and to locate the source of problems. You can use these tools as part of your ongoing operations and as a supplement to other monitoring options.

As seen in the following diagram, the blueprint automates the deployment of the [standalone agent](https://docs.cloud.google.com/vmware-engine/docs/environment/howto-cloud-monitoring-standalone) using a [Managed instance group](https://docs.cloud.google.com/compute/docs/instance-groups) that is deployed in the customer VPC. The agent collects metrics and syslog logs from VMware vCenter and forwards them to Cloud Monitoring and Cloud Logging.

![Monitoring for the blueprint.](https://docs.cloud.google.com/static/architecture/blueprints/vmware-engine-blueprint/images/gcve-monitoring.svg)

## Backups

The blueprint uses Backup and DR to provide data protection services to your VMware workloads. The service uses a managed appliance that is deployed in the customer VPC. The appliance is connected to the Google control plane through [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) and websockets. Backups are stored in [Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction) and the service provides granular recovery options, letting you restore individual files or entire VMs to a specific point in time.

## Operational best practices

This section describes some of the best practices that you can implement, depending on your environment and requirements, after deploying the blueprint.

### Add more spare nodes

VMware Engine clusters are automatically sized to have at least one spare node for resiliency. A spare node is an inherent behavior in vSphere HA, meaning that this node is available in the cluster and billed accordingly.

You can add more spare nodes to the cluster for guaranteed capacity during maintenance windows. This decision can incur additional consumption costs and these nodes are managed directly by your organization.

The spare nodes that you add appear as extra nodes in your vSphere cluster. Optionally, you can schedule workloads on the spare nodes.

### Consider the resource limits for private clouds

VMware Engine private clouds have [resource limits](https://docs.cloud.google.com/vmware-engine/docs/concepts-vmware-components#vsphere-limits) on compute, storage, and networking components. Consider these limits during your private cloud deployment so that your environment can scale with your workload demands.

### Implement cost management options

You can implement one or more of the following options to manage your costs:

  * Committed use discounts (CUDs)
  * Auto-scaling
  * Core count limits
  * Oversubscription of compute capacity



#### Use committed use discounts

CUDs provide discounted prices in exchange for your commitment to use a minimum level of resources for a specified term. [VMware Engine CUDs](https://docs.cloud.google.com/vmware-engine/docs/cud) apply to aggregate VMware Engine node usage in a region, giving you low, predictable costs, without requiring you to make any manual changes or updates. Discounts apply to VMware Engine node usage in the regions where the service is available and where you have purchased the CUDs.

#### Use autoscaling

VMware Engine lets you automatically add or remove nodes in a cluster based on [predefined thresholds and watermarks](https://docs.cloud.google.com/vmware-engine/docs/howto-autoscale). These policies are triggered if a specified condition is sustained for at least 30 minutes. When applying or updating an autoscale policy to a vSphere cluster (standard or stretched), consider the following:

  * By default, autoscaling is disabled. You must enable it explicitly for each cluster.
  * In a stretched cluster, the number of nodes that you specify in the policy are added or removed _per zone_ , which impacts billing accordingly.
  * Because compute, memory, and storage usage are often independent, autoscale policies that monitor multiple metrics use OR logic for node addition and AND logic for node removal.
  * Autoscale maximums are determined by the quotas that are available in your Google Cloud project and [VMware Engine private cloud](https://docs.cloud.google.com/vmware-engine/quotas).
  * Enabling autoscaling and manually adding or removing a node is _not_ mutually exclusive. For example, with the Storage Capacity Optimization Policy, you can manually remove a node if you can get the VM disk space reduced enough to accommodate all the VMs on the cluster. Although manually removing nodes is possible, it is not a best practice when using autoscaling.



#### Limit core count

VMware Engine lets administrators reduce the number of effective CPU cores that are exposed to the guest OS (which is the VM running on top of VMware Engine). Some software license agreements require that you reduce the cores that are exposed.

#### Oversubscribe VMware Engine compute capacity

Oversubscribing VMware Engine compute capacity is a standard practice and, [unlike Compute Engine sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/overcommitting-cpus-sole-tenant-vms), doesn't incur additional charges. A higher oversubscription ratio might help you to decrease the number of effective billable nodes in your environment, but can affect application performance. When sizing enterprise workloads, we recommend that you use a 4:1 ratio to start, and you then modify the ratio based on factors that are applicable to your use case.

## Deploy the blueprint

You can deploy the blueprint on the enterprise foundation blueprint or Fabric FAST.

To deploy the blueprint on the enterprise foundation blueprint, complete the following:

  * [Deploy the enterprise foundation blueprint](https://docs.cloud.google.com/architecture/blueprints/security-foundations/summary).
  * Deploy the VMware Engine enterprise blueprint. For instructions, see the [VMware Engine enterprise blueprint repository](https://github.com/GoogleCloudPlatform/enterprise-gcve-foundation/tree/main).



To deploy the blueprint on Fabric FAST, see the [Fabric FAST repository](https://github.com/GoogleCloudPlatform/cloud-foundation-fabric). The [Google Cloud VMware Engine Stage ](https://github.com/GoogleCloudPlatform/cloud-foundation-fabric/tree/master/fast/stages/3-gcve-dev) deploys the VMware Engine enterprise blueprint.

### Deploy the blueprint without the enterprise foundations blueprint or Fabric FAST

To deploy the blueprint without first deploying the enterprise foundation blueprint or Fabric FAST, verify the following resources exist in your environment:

  * An organization hierarchy with `development`, `nonproduction`, and `production` folders
  * A Shared VPC network for each folder
  * An IP address scheme that takes into account the required IP address ranges for your VMware Engine private clouds
  * A DNS mechanism for your VMware Engine private clouds
  * Firewall policies that are aligned with your security posture
  * A mechanism to access Google Cloud APIs through internal IP addresses
  * A connectivity mechanism with your on-premises environment
  * Centralized logging for security and audit
  * Organizational policies that are aligned with your security posture
  * A pipeline that you can use to deploy VMware Engine



## What's next

  * Read about [VMware Engine](https://docs.cloud.google.com/vmware-engine/docs/overview).
  * Learn how to [migrate VMware VM instances to your private cloud](https://docs.cloud.google.com/vmware-engine/docs/best-practices-migration).
  * Read [compute best practices](https://docs.cloud.google.com/vmware-engine/docs/best-practices-compute).
  * Read [networking best practices](https://docs.cloud.google.com/vmware-engine/docs/best-practices-networking).
  * Read the [best practices for VMware Engine security](https://docs.cloud.google.com/vmware-engine/docs/best-practices-security).
  * Read [storage best practices](https://docs.cloud.google.com/vmware-engine/docs/best-practices-storage).
  * Read [costing best practices](https://docs.cloud.google.com/vmware-engine/docs/best-practices-costs).
  * Access the [VMware Engine page from VMware](https://www.vmware.com/cloud-solutions/google-cloud.html).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-09-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-09-17 UTC."],[],[]] 
