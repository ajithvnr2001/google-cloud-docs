---
url: https://docs.cloud.google.com/vmware-engine/docs/quickstart-networking-requirements/
title: Networking requirements \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:23.418116+00:00
---

# Networking requirements  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/quickstart-networking-requirements/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Networking requirements

Google Cloud VMware Engine offers a private cloud environment that's accessible to users and applications from on-premises environments, enterprise-managed devices, and Google Cloud services like [Virtual Private Cloud (VPC)](https://docs.cloud.google.com/vpc/docs). To establish connectivity between VMware Engine private clouds and other networks, you use networking services such as [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn) and [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect).

Some network services require user-specified address ranges to enable functionality. To help you plan your deployment, this page lists networking requirements and their associated features.

## Before you begin

* Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
* In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

  * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
  * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

* If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

* [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

* Enable the Cloud DNS and VMware Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dns.googleapis.com,vmwareengine.googleapis.com)

* In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

  * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
  * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

* If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

* [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

* Enable the Cloud DNS and VMware Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dns.googleapis.com,vmwareengine.googleapis.com)

### Required roles

To get the permissions that you need to complete this quickstart, ask your administrator to grant you the [VMware Engine Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine#vmwareengine.vmwareengineViewer) (`roles/vmwareengine.vmwareengineViewer`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## VMware Engine private cloud connectivity

For an overview of private cloud networking, see [Private cloud networking for VMware Engine](https://docs.cloud.google.com/vmware-engine/docs/private-cloud-networking-for-vmware-engine).

The connection from your VPC network to a Standard VMware Engine network uses [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering).

## Global address resolution using Cloud DNS

If you want [global address resolution using Cloud DNS](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-dns-on-premises#global-address-resolution-cloud-dns), you must complete Cloud DNS setup before you create your private cloud.

## CIDR requirements and restrictions

VMware Engine uses set address ranges for services like hosting management appliances and deploying HCX networks. Some address ranges are mandatory and others depend on the services that you plan to deploy.

You must reserve address ranges such that they won't overlap with any of your on-premises subnets, VPC network subnets, or planned workload subnets.

Additionally, your workload VMs and vSphere/vSAN subnet CIDR range must not overlap with any IP addresses in the following ranges:

  * 127.0.0.0/8
  * 224.0.0.0/4
  * 0.0.0.0/8
  * 169.254.0.0/16
  * 198.18.0.0/15
  * 240.0.0.0/4



### vSphere/vSAN subnets CIDR range

VMware Engine deploys management components of a private cloud in the **vSphere/vSAN subnets CIDR range** that you provide during private cloud creation. IP addresses in this range are reserved for private cloud infrastructure, and can't be used for workload VMs. The CIDR range prefix must be between _/24_ and _/20_.

Each node in the private cloud has 5 VMkernel ports for VMware system use: ESXi management, vMotion, vSAN, NSX-T, and HCXIX. Each of these VMkernel ports consumes one IP address from the vSphere/vSAN subnets CIDR range.

**Note:** VMware Engine divides the vSphere/vSAN subnets CIDR range into different subnets during private cloud deployment, and you cannot change this range after private cloud creation without deleting the private cloud.

#### Subnets CIDR range division versions

Private clouds created after November 2022 adhere to IP address layout (IP Plan) version 2.0 subnet allocations. Almost all private clouds created before November 2022 adhere to IP Plan version 1.0 subnet allocations.

To find out which version your private cloud adheres to, complete the following steps:

  1. In the Google Cloud console, go to the **Private clouds** page.

[Go to Private clouds](https://console.cloud.google.com/vmwareengine/privateclouds)

  2. Click **Select a project** and then select the organization, folder, or project where the private cloud is located.

  3. Click the private cloud you want to review.

  4. Look for **IP Plan version** to find out what version this private cloud uses.




The version number is displayed under **IP Plan version**.

#### vSphere/vSAN subnets CIDR range size

The size of your vSphere/vSAN subnets CIDR range affects the maximum size of your private cloud. The following table shows the maximum number of nodes you can have, based on the size of the vSphere/vSAN subnets CIDR range.

Specified vSphere/vSAN subnets CIDR prefix | Maximum number of nodes (IP Plan version 1.0) | Maximum number of nodes (IP Plan version 2.0)  
---|---|---  
/24 | 26 | 10  
/23 | 58 | 20  
/22 | 118 | 40  
/21 | 200 | 90  
/20 | N/A | 200  
  
When selecting your CIDR range prefix, consider the [node limits on resources in a private cloud](https://docs.cloud.google.com/vmware-engine/docs/concepts-vmware-components#vsphere-limits). For example, CIDR range prefixes of _/24_ and _/23_ don't support the maximum number of nodes available to a private cloud. Alternatively, CIDR range prefixes of _/20_ support more than the current maximum number of nodes available to a private cloud.

#### Example management network CIDR range division

The vSphere/vSAN subnets CIDR range you specify is divided into multiple subnets. The following tables show examples of the breakdown for allowed prefixes. The first set of examples use _192.168.0.0_ as the CIDR range for IP Plan version 1.0, and the second set of examples use _10.0.0.0_ for IP Plan version 2.0.

Function | Subnet mask/prefix (IP Plan version 1.0)  
---|---  
vSphere/vSAN subnets CIDR range | 192.168.0.0/21 | 192.168.0.0/22 | 192.168.0.0/23 | 192.168.0.0/24  
System management | 192.168.0.0/24 | 192.168.0.0/24 | 192.168.0.0/25 | 192.168.0.0/26  
vMotion | 192.168.1.0/24 | 192.168.1.0/25 | 192.168.0.128/26 | 192.168.0.64/27  
vSAN | 192.168.2.0/24 | 192.168.1.128/25 | 192.168.0.192/26 | 192.168.0.96/27  
NSX host transport | 192.168.4.0/23 | 192.168.2.0/24 | 192.168.1.0/25 | 192.168.0.128/26  
NSX edge transport | 192.168.7.208/28 | 192.168.3.208/28 | 192.168.1.208/28 | 192.168.0.208/28  
NSX edge uplink1 | 192.168.7.224/28 | 192.168.3.224/28 | 192.168.1.224/28 | 192.168.0.224/28  
NSX edge uplink2 | 192.168.7.240/28 | 192.168.3.240/28 | 192.168.1.240/28 | 192.168.0.240/28  
Function | Subnet mask/prefix (IP Plan version 2.0)  
---|---  
vSphere/vSAN subnets CIDR range | 10.0.0.0/20 | 10.0.0.0/21 | 10.0.0.0/22 | 10.0.0.0/23 | 10.0.0.0/24  
System management | 10.0.0.0/22 | 10.0.0.0/23 | 10.0.0.0/24 | 10.0.0.0/25 | 10.0.0.0/26  
vMotion | 10.0.4.0/24 | 10.0.2.0/25 | 10.0.1.0/26 | 10.0.0.128/27 | 10.0.0.64/28  
vSAN | 10.0.5.0/24 | 10.0.2.128/25 | 10.0.1.64/26 | 10.0.0.160/27 | 10.0.0.80/28  
NSX transport | 10.0.6.0/23 | 10.0.3.0/24 | 10.0.1.128/25 | 10.0.0.192/26 | 10.0.0.128/27  
HCX uplink | 10.0.11.128/25 | 10.0.6.0/26 | 10.0.3.32/27 | 10.0.1.144/28 | 10.0.0.216/29  
NSX edge uplink1 | 10.0.8.0/28 | 10.0.4.0/28 | 10.0.2.0/28 | 10.0.1.0/28 | 10.0.0.160/29  
NSX edge uplink2 | 10.0.8.16/28 | 10.0.4.16/28 | 10.0.2.16/28 | 10.0.1.16/28 | 10.0.0.168/29  
NSX edge uplink3 | 10.0.8.32/28 | 10.0.4.32/28 | 10.0.2.32/28 | 10.0.1.32/28 | 10.0.0.176/29  
NSX edge uplink4 | 10.0.8.48/28 | 10.0.4.48/28 | 10.0.2.48/28 | 10.0.1.48/28 | 10.0.0.184/29  
  
### HCX and NSX Edge Scaling (IP Plan version 2.0 only)

Specified vSphere/vSAN subnets CIDR prefix | Maximum remote HCX sites | Maximum HCX Network Extension appliances | Maximum NSX Edge VMs  
---|---|---|---  
/24 | 2 | 1 | 2  
/23 | 4 | 2 | 4  
/22 | 14 | 8 | 8  
/21 | 25 | 32 | 8  
/20 | 25 | 64 | 8  
**Note:** CIDR range prefixes /23 and larger support more than the maximum number of NSX Edge VMs.

### HCX deployment network CIDR range (IP Plan version 1.0 only)

**Note:** The following information on HCX deployment is for reference only and does not apply to IP Plan version 2.0.

In IP Plan version 1.0, HCX was not integrated into the vSphere/vSAN subnets CIDR range. When you created a private cloud, you could optionally have VMware Engine install HCX on the private cloud by specifying a network CIDR range for use by HCX components. The CIDR range prefix was _/26_ or _/27_.

VMware Engine divided the network that you provided into three subnets:

  * **HCX management:** Used for installation of HCX Manager.
  * **HCX vMotion:** Used for vMotion of VMs between your on-premises environment and VMware Engine private cloud.
  * **HCX WANUplink:** Used for establishing the tunnel between your on-premises environment and VMware Engine private cloud.

**Note:** If you want to deploy HCX after private cloud creation, reserve the subnet IP address range for HCX and contact Cloud Customer Care.

#### Example HCX CIDR range breakdown

The HCX deployment CIDR range you specify is divided into multiple subnets. The following table shows examples of the breakdown for allowed prefixes. The examples use _192.168.1.0_ as the CIDR range.

Function | Subnet mask/prefix  
---|---  
HCX Deployment Network CIDR range | 192.168.1.0/26 | 192.168.1.64/26 | 192.168.1.0/27 | 192.168.1.32/27  
HCX Manager | 192.168.1.13 | 192.168.1.77 | 192.168.1.13 | 192.168.1.45  
  
### Private services access to VMware Engine

The following table describes the address range requirement for private connection to Google Cloud services.

Name/purpose | Description | CIDR prefix  
---|---|---  
Assigned address range | Address range to be used for private connection to Google Cloud services including VMware Engine. | /24 or larger  
  
For more information on setting up private service access, see [Set up private service access](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-setup-private-service-access).

### Edge networking services provided by VMware Engine

The following table describes the address range requirement for edge networking services provides by VMware Engine.

Name/purpose | Description | CIDR prefix  
---|---|---  
Edge Services CIDR | Required if optional edge services, such as internet access and public IP, are enabled, on a per region basis. | /26  
  
## Accessing Private and Restricted Google APIs

By default both Private `199.36.153.8/30` and Restricted `199.36.153.4/30` CIDRs are advertised into the VMware Engine network to support direct access to Google services. The Private CIDR `199.36.153.8/30` can be retracted upon configuration of [VPC Service Controls](https://docs.cloud.google.com/vmware-engine/docs/concepts-vpc-service-controls).

## Firewall port requirements

You can set up a connection from your on-premises network to your private cloud by using site-to-site VPN or Dedicated Interconnect. Use the connection to access your VMware private cloud vCenter and any workloads you run in the private cloud.

You can control what ports are opened on the connection by using a firewall in your on-premises network. This section lists common application port requirements. For port requirements of any other applications, see the documentation for that application.

For more information about ports used for VMware components, see [VMware Ports and Protocols](https://ports.esp.vmware.com/).

### Ports required for accessing vCenter

To access vCenter Server and NSX Manager in your private cloud, open the following ports on the on-premises firewall:

Port | Source | Destination | Purpose  
---|---|---|---  
53 (UDP) | On-premises DNS servers | Private cloud DNS servers | Required for forwarding DNS lookup of gve.goog to private cloud DNS servers from on-premises network.  
53 (UDP) | Private cloud DNS servers | On-premises DNS servers | Required for forwarding DNS lookup of on-premises domain names from private cloud vCenter to on-premises DNS servers.  
80 (TCP) | On-premises network | Private cloud management network | Required for redirecting vCenter URL from HTTP to HTTPS.  
443 (TCP) | On-premises network | Private cloud management network | Required for accessing vCenter and NSX Manager from on-premises network.  
8000 (TCP) | On-premises network | Private cloud management network | Required for vMotion of virtual machines (VMs) from on-premises to private cloud.  
8000 (TCP) | Private cloud management network | On-premises network | Required for vMotion of VMs from private cloud to on-premises.  
  
### Common ports required for accessing workload VMs

To access workload VMs running on your private cloud, you must open ports on your on-premises firewall. The following table lists common ports. For any application-specific port requirements, see to the application documentation.

Port | Source | Destination | Purpose  
---|---|---|---  
22 (TCP) | On-premises network | Private cloud workload network | Secure shell access to Linux VMs running on private cloud.  
3389 (TCP) | On-premises network | Private cloud workload network | Remote desktop to Windows Server VMs running on private cloud.  
80 (TCP) | On-premises network | Private cloud workload network | Access any web servers deployed on VMs running on private cloud.  
443 (TCP) | On-premises network | Private cloud workload network | Access any secure web servers deployed on VMs running on private cloud.  
389 (TCP/UDP) | Private cloud workload network | On-premises Active Directory network | Join Windows Server workload VMs to on-premises Active Directory domain.  
53 (UDP) | Private cloud workload network | On-premises Active Directory network | DNS service access for workload VMs to on-premises DNS servers.  
  
### Ports required for using on-premises Active Directory as an identity source

For a list of ports required to configure your on-premises Active Directory as an identity source on the private cloud vCenter, see [Configuring authentication using Active Directory](https://docs.cloud.google.com/vmware-engine/docs/vmware-platform/howto-identity-sources#ports-active-directory).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
