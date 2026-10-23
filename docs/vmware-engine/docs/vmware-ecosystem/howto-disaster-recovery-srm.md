---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-disaster-recovery-srm/
title: Configure disaster recovery using VMware SRM \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:07.642871+00:00
---

# Configure disaster recovery using VMware SRM  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-disaster-recovery-srm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure disaster recovery using VMware SRM

You can use your Google Cloud VMware Engine private cloud as a disaster recovery (DR) site for on-premises VMware workloads. This DR solution is based on vSphere Replication and VMware Site Recovery Manager (SRM). You can follow a similar approach to use your private cloud as a primary site that's protected by your on-premises recovery site.

This recovery solution offers the following benefits:

  * Eliminates the need to set up a data center specifically for DR.
  * Lets you reduce deployment costs and total cost of ownership for establishing DR.



This solution requires the following from you:

  * Install, configure, and manage vSphere Replication and SRM in your private cloud.
  * Provide your own licenses for VMware SRM.



You can use any versions of vSphere Replication and SRM that are compatible with your private cloud and on-premises environments. The examples in this guide use vSphere Replication 8.3 and SRM 8.3.

## Before you begin

The steps in this document assume that you first do the following:

  * Create a private cloud in the VMware Engine portal by following the instructions in [Creating a private cloud](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-create-private-cloud).
  * Verify that VMware product versions are compatible. The configurations in this guide are subject to the following compatibility requirements:

    * The same version of SRM must be deployed in your private cloud and your on-premises environment.
    * The same version of vSphere Replication must be deployed in your private cloud and your on-premises environment.
    * The versions of vCenter in your private cloud and your on-premises environment must be compatible.
    * The versions of SRM and vSphere Replication must be compatible with each other and with the versions of vCenter. For more information, see the [VMware Site Recovery Manager documentation](https://docs.vmware.com/en/Site-Recovery-Manager/index.html).



## Deploy a DR solution using SRM in your private cloud

This following sections describe how to deploy a DR solution using SRM in a private cloud. The process consists of the following steps:

  1. Estimate the size of your disaster recovery environment.
  2. Set up private cloud networking for SRM.
  3. Set up connectivity between your on-premises and cloud environments.
  4. Set up infrastructure services in your private cloud.
  5. Install a vSphere Replication appliance in your on-premises environment.
  6. Install a vSphere Replication appliance in your private cloud.
  7. Install a SRM server in your on-premises environment.
  8. Install a SRM server in your private cloud



### Estimate the size of your DR environment

Start by estimating the size of your disaster recovery environment:

  * Verify that your identified on-premises configuration is within supported limits. VMware documents these limits in [Operational Limits of Site Recovery Manager](https://docs.vmware.com/en/Site-Recovery-Manager/8.3/com.vmware.srm.install_config.doc/GUID-3AD7D565-8A27-450C-8493-7B53F995BB14.html).
  * Ensure that you have sufficient network bandwidth to meet your workload size and RPO requirements. For more information, see [Calculate Bandwidth for vSphere Replication](https://docs.vmware.com/en/vSphere-Replication/8.3/com.vmware.vsphere.replication-admin.doc/GUID-4A34D0C9-8CC1-46C4-96FF-3BF7583D3C4F.html).
  * Use the sizer tool to estimate the resources that are needed in your DR site to protect your on-premises environment.



### Set up private cloud networking for SRM

From the VMware Engine portal, set up private cloud networking for SRM. Create a subnet for the SRM network and assign it a subnet CIDR.

For more information, see [Creating and managing subnets](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-manage-subnets).

### Set up on-premises to cloud connectivity

Set up a connection between your on-premises and cloud environments using either site-to-site VPN or Cloud Interconnect. To set up a site-to-site VPN connection, see the [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn) documentation. To set up a connection using either Dedicated Interconnect or Partner Interconnect, see the [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview) documentation.

### Set up infrastructure services in your private cloud

To help you manage your workloads and tools, configure the following infrastructure services in your private cloud:

  * **Active Directory (AD):** Identify users from your on-premises AD in your private cloud. Set up an AD in your private cloud for all users.
  * **DNS forwarding:** The `gve.goog` domain is used by management VMs and hosts in your private cloud. To resolve requests to this domain, configure DNS forwarding on the DNS server as described in [Configuring DNS for management appliance access](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-dns-on-premises). This also lets you use fully qualified domain names (FQDNs) instead of IP addresses during the vSphere Replication appliance and SRM installation.



### Install a vSphere Replication appliance in your on-premises environment

Install a vSphere Replication appliance in your on-premises environment by following the VMware documentation. The installation consists of these high-level steps:

  1. Prepare your on-premises environment for installation.
  2. Deploy a vSphere Replication appliance in your on-premises environment using the OVF in the vSphere Replication ISO from VMware by following the steps in [Deploy the vSphere Replication Virtual Appliance](https://docs.vmware.com/en/vSphere-Replication/8.3/com.vmware.vsphere.replication-admin.doc/GUID-E654F2D8-7D56-4A81-9568-E85172A7022D.html).
  3. Register your on-premises vSphere Replication appliance with vCenter SSO at the on-premises site.



For information about vSphere Replication, see [Install vSphere Replication](https://docs.vmware.com/en/vSphere-Replication/8.3/com.vmware.vsphere.replication-admin.doc/GUID-90012981-52B4-4CF2-90C1-0DCFE2350BD1.html).

### Install a vSphere Replication appliance in your private cloud

Before you install a vSphere Replication appliance in your on-premises environment, verify that you have the following:

  * IP reachability from subnets in your on-premises environment to the management subnet of your private cloud
  * IP reachability from the replication subnet in your on-premises vSphere environment to the SRM subnet of your private cloud



For more information, see [Connecting by using VPN](https://docs.cloud.google.com/vmware-engine/docs/networking/classic-console/howto-vpn-connect). The steps are similar to those for the on-premises installation.

Google recommends using fully qualified domain names (FQDNs) instead of IP addresses during the vSphere Replication appliance and SRM installation. To find the FQDN of the vCenter in your private cloud, follow [Accessing management appliances](https://docs.cloud.google.com/vmware-engine/docs/vmware-platform/howto-access-management).

#### Prepare a solution user account for installation

You must install the vSphere Replication appliance and SRM using a user with administrator privileges in the vCenter SSO domain. This helps ensure high uptime and availability for your private cloud vCenter environment.

For the installation process, use one of the [solution user accounts](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-elevate-privilege#solution_user_accounts) available in your private cloud.

#### Configure firewall rules for the vSphere Replication appliance

Ensure the following is permitted If there are firewalls configured in the environment:

  * A vSphere Replication appliance in the SRM network and vCenter and ESXi hosts in the management network
  * The vSphere Replication appliances at the two sites



For a list of port numbers that must be open for vSphere Replication, see [Port numbers that must be open for vSphere Replication 5.8.x, 6.x, and 8.x](https://kb.vmware.com/s/article/2087769).

### Install a SRM server in your on-premises environment

Verify the following requirements before installing a SRM server in your on-premises environment:

  * A vSphere Replication appliance is installed in your on-premises and private cloud environments.
  * The vSphere Replication appliances at both sites are connected to each other.
  * You have reviewed the VMware information on prerequisites and best practices. For SRM, refer to [Prerequisites and Best Practices for Site Recovery Manager Server Installation](https://docs.vmware.com/en/Site-Recovery-Manager/8.3/com.vmware.srm.install_config.doc/GUID-BB0C03E4-72BE-4C74-96C3-97AC6911B6B8.html).



Follow VMware documentation to install a SRM server in the deployment model _Two-Site Topology with One vCenter Instance per Platform Services Controller_ , as described in [Site Recovery Manager in a Two-Site Topology with One vCenter Server Instance per Platform Services Controller](https://docs.vmware.com/en/Site-Recovery-Manager/8.3/com.vmware.srm.install_config.doc/GUID-F474543A-88C5-4030-BB86-F7CC51DADE22.html).

VMware describes the SRM installation process in [About VMware Site Recovery Manager Installation and Configuration](https://docs.vmware.com/en/Site-Recovery-Manager/8.3/com.vmware.srm.install_config.doc/GUID-B3A49FFF-E3B9-45E3-AD35-093D896596A0.html).

### Install a SRM server in your private cloud

After you successfully install a SRM server in your on-premises environment, perform the following steps to install SRM in your private cloud.

#### Deploy SRM and register to vCenter

Sign in to vCenter using the `CloudOwner` or equivalent credentials. Then, follow the VMware documentation to deploy SRM. Use a [solution user account](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-elevate-privilege#solution_user_accounts) to register the SRM server on vCenter and manage the cross-site sessions while pairing the sites.

For more information, you can see the VMware deployment reference model in [Site Recovery Manager in a Two-Site Topology with One vCenter Server Instance per Platform Services Controller](https://docs.vmware.com/en/Site-Recovery-Manager/8.3/com.vmware.srm.install_config.doc/GUID-F474543A-88C5-4030-BB86-F7CC51DADE22.html).

#### Configure firewall rules for SRM

Ensure the following is permitted if there are firewalls configured in the environment:

  * The SRM server and vCenter in the private cloud
  * The SRM servers at both sites



For a list of port numbers that must be open for SRM, see the [VMware page on SRM ports and protocols](https://ports.vmware.com/home/Site-Recovery-Manager).

#### Configure SRM through vCenter

After SRM is installed in the private cloud, perform the following steps to configure SRM through vCenter:

  * Connect the SRM server instances on the protected and recovery sites.
  * Establish a client connection to the cloud SRM server instance.
  * Install the SRM license key.



## Ongoing management of SRM

You have full control over vSphere Replication and SRM software in your private cloud and are expected to perform necessary software lifecycle management. Ensure that any new version of software is compatible with the private cloud vCenter before updating or upgrading vSphere Replication or SRM.

## Multiple replication configuration

You can use both array-based replication and vSphere Replication technologies together with SRM at the same time in your on-premises environment. For more information, see [Array-Based Replication Versus vSphere Replication](https://docs.vmware.com/en/vRealize-Suite/2019/com.vmware.vrsuite.srm.doc/GUID-A554FF29-7A82-4D92-B8AA-8B528AEF399F.html).

Either array-based replication or vSphere Replication must be applied to a set of VMs. A given VM can be protected either by array-based replication or vSphere Replication, but not both. You can configure the VMware Engine site as a recovery site for multiple protected sites. For information about multi-site configurations, see [SRM Multi-Site Options](https://blogs.vmware.com/virtualblocks/2016/07/28/srm-multisite/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
