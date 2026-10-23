---
url: https://docs.cloud.google.com/vmware-engine/docs/concepts-vmware-components/
title: Private cloud VMware components \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:02.599276+00:00
---

# Private cloud VMware components  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/concepts-vmware-components/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Private cloud VMware components

A private cloud is an isolated VMware stack (ESXi hosts, vCenter, vSAN, and NSX) environment managed by a vCenter Server in a management domain. Google Cloud VMware Engine deploys private clouds with the following VMware stack components:

  * **VMware ESXi:** hypervisor on dedicated nodes
  * **VMware vCenter:** centralized management of private cloud vSphere environment
  * **VMware vSAN:** hyper-converged, software-defined storage platform
  * **VMware NSX Data Center:** network virtualization and security software
  * **VMware HCX:** application migration and workload rebalancing across data centers and clouds



You can [retrieve generated sign-in credentials](https://docs.cloud.google.com/vmware-engine/docs/vmware-platform/howto-access-vsphere-client#sign-in) for VMware stack components from the private cloud details page.

## VMware component versions

A private cloud VMware stack has the following software versions:

Component | Version | Licensed version  
---|---|---  
ESXi | 8.0 Update 3f | VMware Cloud Foundation  
vCenter | 8.0 Update 3e | VMware Cloud Foundation  
vSAN | 8.0 Update 3 | VMware Cloud Foundation  
NSX Data Center | 4.2.2.1 | VMware Cloud Foundation  
HCX | 4.10.3 | VMware Cloud Foundation  
Aria | 8.16 | VMware Cloud Foundation  
  
1VMware Engine deploys a version of HCX made available to Google Cloud by VMware. Update HCX after private cloud creation to retrieve the latest version of HCX for your environment.

## ESXi

When you create a private cloud, VMware ESXi is installed on provisioned Google Cloud VMware Engine nodes. ESXi provides the hypervisor for deploying workload virtual machines (VMs). Nodes provide hyper-converged infrastructure (compute and storage) and are a part of the vSphere cluster on your private cloud.

Each node has four physical network interfaces connected to the underlying network. VMware Engine creates a vSphere distributed switch (VDS) on the vCenter using these physical network interfaces as uplinks. Network interfaces are configured in active mode for high availability.

## vCenter Server Appliance

vCenter Server Appliance (VCSA) provides the authentication, management, and orchestration functions for VMware Engine. When you create and deploy your private cloud, VMware Engine deploys a VCSA with an embedded Platform Services Controller (PSC) on the vSphere cluster. Each private cloud has its own VCSA. Adding nodes to a private cloud adds nodes to the VCSA.

### vCenter Single Sign-On

The embedded platform services controller on VCSA is associated with a vCenter Single Sign-On. The domain name is `gve.local`. To access vCenter, use the default user, `CloudOwner@gve.local`, which is created for you to access vCenter. You can add your on-premises/Active Directory [identity sources for vCenter](https://docs.cloud.google.com/vmware-engine/docs/vmware-platform/howto-identity-sources).

## vSAN storage

**Important:** To be compliant with service-level agreement (SLA), VMware Engine requires slack space of 20% available on vSAN.

Clusters in private clouds have fully configured all-flash vSAN storage. The all-flash storage is provided by local SSDs. At least three nodes of the same node type are required to create a vSphere cluster with a vSAN Datastore.

By default, VMware Engine enables compression only on the vSAN Datastore when a new cluster is created. Each cluster on your private cloud contains a vSAN Datastore. If the stored virtual machine data isn't suitable for vSAN space efficiency by compression, you can select no space efficiency on the individual vSAN Datastore. For more information about space efficiency, see [About vSAN Space Efficiency](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vsan.doc/GUID-3D2D80CC-444E-454E-9B8B-25C3F620EFED.html).

**Warning:** Disabling compression requires a vSAN resync, which can take a long time when large amounts of data is stored.

In addition to vSAN Advanced features, VMware Engine also provides access to vSAN Enterprise data encryption for data at rest and data in transit.

### vSAN storage policies

A vSAN storage policy defines the **Failures to tolerate (FTT)** and the **Failure tolerance method**. You can create new storage policies and apply them to VMs. To maintain [SLA](https://docs.cloud.google.com/vmware-engine/sla), you must maintain 20% spare capacity on the vSAN Datastore.

On each vSphere cluster, there's a default vSAN storage policy that applies to the vSAN Datastore. The storage policy determines how to provision and allocate VM storage objects within the datastore to ensure a level of service.

The following table shows the default vSAN storage policy parameters:

FTT | Failure tolerance method | Number of nodes in vSphere cluster  
---|---|---  
1 | RAID 1 (mirroring)  
Creates 2 copies | 3 and 4 nodes  
2 | RAID 1 (mirroring)  
Creates 3 copies | 5 to 32 nodes  
  
### Supported vSAN storage policies

The following table shows the supported vSAN storage policies and the minimum number of nodes required to enable the policy:

FTT | Failure tolerance method | Minimum number of nodes required in vSphere cluster  
---|---|---  
1 | RAID 1 (mirroring) | 3  
1 | RAID 5 (erasure coding) | 4  
2 | RAID 1 (mirroring) | 5  
2 | RAID 6 (erasure coding) | 6  
3 | RAID 1 (mirroring) | 7  
  
## NSX Data Center

NSX Data Center provides network virtualization, micro segmentation, and network security capabilities on your private cloud. You can configure services supported by NSX Data Center on your private cloud by using NSX.

### Available features

The following list describes NSX features supported by VMware Engine, organized by category:

  * Switching, DNS, DHCP, and IPAM (DDI): 
    * Optimized ARP learning and broadcast suppression
    * Unicast replication
    * Head-end replication
    * SpoofGuard
    * IP address management
    * IP blocks
    * IP subnets
    * IP pools
    * IPv4 DHCP server
    * IPv4 DHCP relay
    * IPv4 DHCP static bindings or fixed addresses
    * IPv4 DNS relay/DNS proxy
  * Routing: 
    * Null routes
    * Static routing
    * Device routing
    * BGP route controls using route maps and Prefix-lists
  * NAT: 
    * NAT on North or South and East or West logical routers
    * Source NAT
    * Destination NAT
    * N:N NAT
  * Firewall: 
    * Edge Firewall
    * Distributed Firewall
    * Common firewall user interface
    * Firewall sections
    * Firewall logging
    * Stateful Layer 2 and Layer 3 firewall rules
    * Tag-based rules
    * Distributed firewall-based IPFIX
  * Firewall policies, tags, and groups: 
    * Object tagging or security tags
    * Network-centric grouping
    * Workload-centric grouping
    * IP-based grouping
    * MAC-based grouping
  * VPN: 
    * Layer 2 VPN
    * Layer 3 VPN (IPv4)
  * Integrations: 
    * Container networking and security using Tanzu Kubernetes Grid (TKG) only
    * VMware Cloud Director service
    * VMware Aria Automation
    * VMware Aria Operations for Logs
  * Authentication and authorization: 
    * Direct Active Directory integration using LDAP
    * Authentication using OpenLDAP
    * Role-based access control (RBAC)
  * Automation: 
    * REST API
    * Java SDK
    * Python SDK
    * Terraform provider
    * Ansible modules
    * OpenAPI/Swagger specifications and auto-generated API documentation for REST API
  * Inspection: 
    * Port mirroring
    * Traceflow
    * Switch-based IPFIX



### Feature limitations

Some NSX Data Center features have very specific networking and security use cases. Customers who created their Google Cloud account on or before August 30, 2022 can request access to features for those use cases by reaching out to Cloud Customer Care.

The following table describes those features, their corresponding use cases, and potential alternatives:

Feature | Use case | Recommended alternative | Google Cloud customers on or before August 30, 2022 | Google Cloud customers after August 30, 2022  
---|---|---|---|---  
Layer 3 multicast | Multi-hop Layer 3 multicast routing | Layer 2 multicast is supported within a NSX subnet. This allows for all multicast traffic to be delivered to workloads on the same NSX subnet. | Supported | Unsupported  
Quality of Service (QoS) | VoIP and latency sensitive application where network oversubscription occurs | None required, as VMware Engine delivers a non-oversubscribed network architecture. Further, any QoS tags exiting a private cloud are stripped when entering the VPC through a peering connection. | Supported | Unsupported  
Simple Network Management Protocol (SNMP) traps | Legacy alerting protocol for notifying users of events | Events and alarms can be [configured within NSX](https://docs.vmware.com/en/VMware-NSX-T-Data-Center/3.0/administration/GUID-2C022ED8-075E-48F1-8F0C-648F038AF68A.html) using modern protocols. | Supported | Unsupported  
NAT features such as stateless NAT, NAT logging, and NAT64 | Used for carrier-grade NAT in large telecommunication deployments | NSX supports source/destination NAT and N:N NAT on North/South and East/West logical routers. | Supported | Unsupported  
Intent-based networking and security policies | Used in conjunction with VMware Aria to create business-based firewall policies within NSX | NSX Gateway and Distributed Firewall features can be used to create and enforce security policies. | Supported | Unsupported  
Identity-based groups using Active Directory | VDI deployments where the user logged into a specific VDI guest can be detected and receive a custom set of NSX firewall rules | Users can be assigned specific workstations using the dedicated-assignment pool. Use NSX tags to then apply specific firewall rules by pool. | Supported | Unsupported  
Layer 7 attribute (App ID) rules | Used in NSX firewall rules | Use [NSX Service Groups](https://docs.vmware.com/en/VMware-NSX-T-Data-Center/3.1/administration/GUID-B6AA9E5C-AD23-4629-8272-09C2EB686A77.html) to define a set of ports and services for reference when creating one or more firewall rules.  | Supported | Unsupported  
Stateless Layer 2 and Layer 3 firewall rules | Used for carrier-grade high speed firewalls in large telecommunication deployments | NSX supports stateful high-performance Layer 2 and Layer 3 rules. | Supported | Unsupported  
NSX service insertion | Used to automate the North/South or East/West deployment of third-party network services by using NSX to secure and inspect traffic | For third-party security vendor deployments, VMware Engine recommends a routed model over service insertion to ensure that routine service upgrades don't impact network availability. |  [Contact Cloud Customer Care](https://docs.cloud.google.com/vmware-engine/docs/getting-support) | Unsupported  
  
## Using licenses

Google Cloud is a VMware Cloud partner. You can choose a [committed use discount (CUD) type](https://docs.cloud.google.com/vmware-engine/docs/cud#discountsandpricing) that includes licenses as part of the managed VMware Engine service, or you can choose to bring your own licenses.

## Updates and upgrades

This section describes update and upgrade considerations and lifecycle management responsibilities for software components.

### HCX

VMware Engine handles initial installation, configuration, and monitoring of HCX in private clouds. After that, you are responsible for lifecycle management of HCX Cloud and service appliances like HCX-IX Interconnect.

VMware provides updates for HCX Cloud through its HCX service. You can upgrade HCX Manager and deployed HCX service appliances from the HCX Cloud interface. To find the end of support date for a product release, refer to the [VMware Product Lifecycle Matrix](https://lifecycle.vmware.com/).

### Other VMware software

Google is responsible for lifecycle management of VMware software (ESXi, vCenter, PSC, and NSX) in the private cloud.

Software updates include:

  * **Patches:** security patches or bug fixes released by VMware
  * **Updates:** minor version change of a VMware stack component
  * **Upgrades:** major version change of a VMware stack component



VMware Engine tests critical security patches as soon as they become available from VMware. Google will aim to commence the rollouts of relevant critical patches to private cloud environments within one week of their availability. The actual patching completion timeline will vary depending on scheduling availability and the need to time the patching to avoid any downtime for customer workloads.

Google provides quarterly maintenance updates to VMware software components. For a new major version of VMware software version, Google works with customers to coordinate a suitable maintenance window for upgrade.

## vSphere cluster

To ensure high availability of the private cloud, ESXi hosts are configured as a cluster. When you create a private cloud, VMware Engine deploys management components of vSphere on the first cluster. VMware Engine creates a resource pool for management components, and deploys all management VMs in this resource pool.

The first cluster cannot be deleted to shrink the private cloud. The vSphere cluster uses vSphere HA to provide high availability for VMs. Failures to tolerate (FTT) are based on the number of available nodes in the cluster. The formula `Number of nodes = 2N+1`, where `N` is the FTT, describes the relationship between available nodes in a cluster and FTT.

For production workloads, use a private cloud that contains at least 3 nodes.

### Single-node private clouds

For testing and proofs of concept with VMware Engine, you can create a private cloud that contains only a single node and cluster. VMware Engine permits single-node private clouds without a time limit.

You can resize a single-node private cloud to contain three or more nodes. When you do so, VMware Engine initiates vSAN data replication. A private cloud must contain at least three nodes and complete vSAN data replication to be eligible for coverage based on the [SLA](https://docs.cloud.google.com/vmware-engine/sla).

Features or operations that require more than one node won't work with a single-node private cloud. For example, you won't be able to use vSphere Distributed Resource Scheduler (DRS) or high availability (HA).

### vSphere cluster limits

The following table describes vSphere cluster limits in standard private clouds that meet [SLA](https://docs.cloud.google.com/vmware-engine/sla) requirements:

Resource | Limit  
---|---  
Minimum number of nodes to create a private cloud (first cluster) | 3  
Minimum number of nodes to create a cluster | 3  
Maximum number of nodes per cluster | 32  
Maximum number of nodes per private cloud | 128  
Maximum number of clusters per private cloud | 21  
  
The following table describes vSphere cluster limits in stretched private clouds:

Resource | Limit  
---|---  
Minimum number of nodes to create a stretched private cloud (first cluster) | 6  
Minimum number of nodes to create a stretched cluster | 6  
Maximum number of nodes per stretched cluster | 30  
Maximum number of nodes per stretched private cloud | 128  
Maximum number of clusters per stretched private cloud | 16  
  
## Guest operating system support

You can install a VM with any guest operating system supported by VMware for the ESXi version in your private cloud. For a list of supported guest operating systems, see the [VMware Compatibility Guide for Guest OS](https://www.vmware.com/resources/compatibility/search.php?deviceCategory=software&details=1&productNames=15&page=1&display_interval=10&sortColumn=Partner&sortOrder=Asc&testConfig=16).

## VMware infrastructure maintenance

Occasionally it's necessary to make changes to the configuration of the VMware infrastructure. These intervals can occur every 1‑2 months, but the frequency is expected to decline over time. This type of maintenance can usually be done without interrupting normal usage of the services.

During a VMware maintenance interval, the following services continue to function without any effect:

  * VMware management plane and applications
  * vCenter access
  * All networking and storage
  * All cloud traffic



## External Storage

You can expand the storage capacity of a Google Cloud VMware Engine cluster by adding more nodes. Alternatively, you can use external storage if you only want to scale storage. Scaling storage increases the storage capacity without increasing the compute capacity of the cluster, allowing you to scale your resource independently.

Contact Google Support or your sales representative for more information about using external storage.

## What's next

  * Learn about [private cloud maintenance and updates](https://docs.cloud.google.com/vmware-engine/docs/concepts-maintenance-updates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
