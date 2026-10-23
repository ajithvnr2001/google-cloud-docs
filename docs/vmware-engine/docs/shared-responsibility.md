---
url: https://docs.cloud.google.com/vmware-engine/docs/shared-responsibility/
title: VMware Engine shared responsibility model \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:39.899538+00:00
---

# VMware Engine shared responsibility model  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/shared-responsibility/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# VMware Engine shared responsibility model

This page describes what you, as a Google Cloud VMware Engine customer, are responsible for and what Google is responsible for.

## Introduction

Trusted security in Google Cloud is achieved through the shared responsibilities of customers and Google as a service provider. This model is intended to provide higher security and eliminate single points of failure. The following sections list the responsibilities by role.

## Shared responsibility matrix

The following table describes the shared responsibility matrix, detailing the activities managed by Google and the customer:

Activity | Responsibility | Comments  
---|---|---  
**Monitoring and alerting**  
VM OS and applications (infrastructure) | Google | Google monitors the health and availability of VM infrastructure.  
VM OS and applications (performance) | Customer | The customer is responsible for providing VMware expertise and following [VMware performance guidelines](https://docs.cloud.google.com/vmware-engine/docs/best-practices-compute).  
vSAN | Google | Google monitors the health and availability of vSAN storage.  
Network overlay | Google | Google monitors the health of NSX infrastructure devices (Edge Gateway devices, Controllers) and the underlying networking of the infrastructure (underlay) provided through physical VLANs.  
NSX | Customer | The customer can self-manage their overlay networking through NSX. All features of NSX are available and are monitored/managed by the customer. The customer can configure firewall rules, public IP addresses, and VPC peering of the underlay.  
VPN/Site-to-Site IPsec (service health) | Google | Google provides VPN as a service using Cloud VPN and monitors the health of the VPN devices.   
VPN/Site-to-Site IPsec (VPN devices on-premises and in NSX) | Customer | The customer must monitor on-premises devices and can also self-manage and monitor VPN devices in NSX.  
ESXi hosts | Google | If a VMware platform (ESXi, vCenter, vSAN, NSX) or infrastructure hardware support need is identified, Google provides support.  
Security and network devices | Google | Google Cloud and the VMware platform provide default VPN, gateway, and firewall capabilities. Google manages the health of these devices, and the customer manages any customer-specific tools.  
HCX | Google | Google monitors the health and availability of the default HCX deployment.  
**Support**  
VM OS and applications | Customer | The customer is responsible for any OS or application support.  
vSAN | Google | If a VMware platform (ESXi, vCenter, vSAN, NSX) or infrastructure hardware support need is identified, Google provides support.  
Network overlay | Google | Google provides support for overlay networking.  
ESXi hosts - hardware | Google | If a VMware platform (ESXi, vCenter, vSAN, NSX) or infrastructure hardware support need is identified, Google provides support, including host replacement.  
ESXi hosts - default software | Google | Google manages software deployed on the node by default.  
ESXi hosts - customer-deployed software | Customer | The customer is responsible for any software they deploy with elevated privileges (for example, Zerto).  
Security and network devices | Google | If a VMware platform (ESXi, vCenter, vSAN, NSX) or infrastructure hardware support need is identified, Google provides support.  
NSX | Google | If a VMware platform (ESXi, vCenter, vSAN, NSX) or infrastructure hardware support need is identified, Google provides support.  
VPN/Site-to-Site IPsec (service health) | Google | Google provides VPN as a service via Cloud VPN.  
VPN/Site-to-Site IPsec (VPN devices on-premises) | Customer | Google provides VPN as a service via Cloud VPN. The customer must support on-premises devices.  
ISV software support | Customer | The customer must confirm support with independent software vendors (ISVs) before deploying specific software to the private cloud.  
**Identity management**  
Implementation | Customer | The customer can integrate on-premises ID sources with the Google Cloud console and with vCenter.  
Configuration and management | Customer | The customer manages and configures identity sources, including vCenter and NSX user management (identity, access control).  
**Installation and provisioning**  
Private clouds (deployment) | Customer | The customer triggers the deployment of private clouds via the console, API, or CLI.  
ESXi hosts | Google | Google installs and provisions ESXi hosts.  
vSAN | Google | Google installs and provisions vSAN.  
vCenter | Google | Google deploys and performs the basic configuration of vCenter.  
Aria Suite Lifecycle Manager (LCM) | Google | Google deploys and performs the basic configuration of Aria Suite Lifecycle Manager (LCM).  
Aria Suite | Customer | The customer is responsible for installing and provisioning the Aria Suite, which includes VMware Aria Operations, VMware Aria Operations for Networks, VMware Aria Operations for Logs, VMware Aria Automation, and VMware Identity Manager.  
OS and applications | Customer | The customer installs and provisions operating systems and applications.  
Databases | Customer | The customer installs and provisions databases.  
Security and network devices | Google | Google Cloud and the VMware platform provide default VPN, gateway, and firewall capabilities. The customer manages any customer-specific tools.  
NSX | Google | Google deploys and performs the basic configuration of NSX.  
VPN/Site-to-Site IPsec | Customer | The customer must provision Cloud VPN in their Google Cloud project.  
HCX (initial deployment) | Google | Google deploys and performs the basic configuration of HCX.  
Workload migration | Customer | The customer is responsible for migrating VMs and workloads to the private cloud, and managing migration tools (such as HCX).  
**Backup and restore**  
Management services | Google | Google manages backup and restore of management services, including vCenter Server and NSX Manager. This does not include customer workloads.  
Customer workloads | Customer | The customer is responsible for installing, configuring, and managing backup software for customer environments and workloads.  
**Configuration and management**  
ESXi hosts | Google | Google manages the configuration of ESXi hosts.  
vSAN (initial and default configuration) | Google | Google manages vSAN initial configuration.  
vSAN (non-default configuration) | Customer | The customer can change configuration (for example, change storage policy).  
vCenter (initial configuration) | Google | Google deploys and performs the basic configuration of vCenter.  
vCenter (customization) | Customer | The customer must configure ID sources, external users, DRS/HA policies, vSAN policies, NSX subnets, and add-on applications.  
Aria Suite Lifecycle Manager (LCM) | Google | Google manages Aria Suite Lifecycle Manager (LCM) configuration.  
Aria Suite | Customer | The customer manages the configuration of Aria Suite components (VMware Aria Operations, VMware Aria Operations for Networks, VMware Aria Operations for Logs, VMware Aria Automation, and VMware Identity Manager).  
OS and applications | Customer | The customer manages operating system and application configurations.  
Databases | Customer | The customer manages database configurations.  
Security and network devices | Google | Google manages the configuration of default security and network devices.  
SAN/storage | Google | Google manages storage-area network (SAN) and storage configurations.  
NSX (initial configuration) | Google | Google deploys and performs the basic configuration of NSX, NSX Edge, and Controllers.  
NSX (customization) | Customer | The customer must configure subnets, firewalls/micro-segmentation, and other optional devices, and perform ongoing management.  
VPN/Site-to-Site IPsec | Google | Google manages the configuration of default VPN and Site-to-Site IPsec capabilities.  
VM tuning | Customer | The customer must follow [VMware performance guidelines](https://docs.cloud.google.com/vmware-engine/docs/best-practices-compute).  
Management network ranges | Customer | The customer must allocate and define the CIDR network range for management appliances and resources.  
Configuration management tools | Customer | The customer is responsible for installing and managing any guest configuration management tools.  
**Patching, updates, and upgrades**  
ESXi hosts - hardware | Google | Google handles patching, updates, and upgrades for ESXi host hardware.  
ESXi hosts - firmware | Google | Google handles patching, updates, and upgrades for ESXi host firmware.  
vSAN | Google | Google handles patching, updates, and upgrades for vSAN.  
vCenter | Google | Google handles patching, updates, and upgrades for vCenter.  
Aria Suite Lifecycle Manager (LCM) | Google | Google handles patching, updates, and upgrades for Aria Suite Lifecycle Manager (LCM).  
Aria Suite | Customer | The customer is responsible for patching, updates, upgrades, and maintenance of Aria Suite components (VMware Aria Operations, VMware Aria Operations for Networks, VMware Aria Operations for Logs, VMware Aria Automation, and VMware Identity Manager) in a timely manner after receiving updates from Google.  
OS and applications | Customer | The customer handles patching, updates, and upgrades for guest operating systems and applications.  
Databases | Customer | The customer handles patching, updates, and upgrades for databases.  
Security and network devices (standard configuration) | Google | Google Cloud and the VMware platform provide default VPN, gateway, and firewall capabilities. Google handles the patching, updates, and upgrades for these capabilities.  
Security and network devices (additional configuration) | Customer | The customer manages any customer-specific tools.  
NSX | Google | Google handles patching, updates, and upgrades for NSX.  
**Upgrades and modifications**  
VPN/Site-to-Site IPsec (initial configuration) | Google | Google upgrades the Cloud VPN infrastructure.  
VPN/Site-to-Site IPsec (customization) | Customer | The customer can perform modifications.  
**Security software and configuration**  
VM OS and applications | Customer | Customer is responsible for following [VMware security best practices](https://docs.cloud.google.com/vmware-engine/docs/best-practices-security).  
Antivirus and security tools | Customer | The customer is responsible for installing and managing antivirus, security software, and agents in guest environments and workloads.  
vSAN encryption (data at rest) | Customer | The customer is responsible for keeping vSAN data-at-rest encryption enabled and managing the lifecycle (rotation) of the Key Encryption Key (KEK).  
**Core network security**  
Initial configuration | Google | The platform provides default features such as firewall and micro-segmentation.  
Customization | Customer | The customer must configure these features to match their policies and needs.  
**Compliance**  
Google-managed services and infrastructure | Google | Google acquires and maintains industry and regulatory compliance certifications for Google-managed services and infrastructure.  
Customer environments and workloads | Customer | The customer is responsible for acquiring and maintaining industry and regulatory compliance certifications for customer-owned environments and workloads.  
**Physical infrastructure**  
Physical elements and facilities | Google | Google deploys, manages, and maintains the physical infrastructure, facility power and cooling, Google Cloud regions, bare-metal hosts, and network equipment.  
**Capacity monitoring and management**  
Capacity monitoring, management, and planning | Customer | The customer must monitor and manage capacity, including planning and reservations when provisioning more VMs or adding host nodes.  
**Capacity planning and infrastructure resource provisioning**  
Ensuring capacity | Google | Google ensures sufficient backend infrastructure capacity.  
Capacity deployment | Google | Google deploys additional infrastructure capacity as required.  
**Infrastructure lifecycle management**  
Core infrastructure | Google | Google offers the core infrastructure—specifically the VMware core platform (ESXi, vCenter, vSAN, NSX) and all access networking services such as Cloud VPN and Interconnect—as a service.  
Additional infrastructure and workloads | Customer | The customer must manage any add-on components, operating systems, and workloads.  
HCX lifecycle management | Customer | The customer is responsible for the lifecycle management of HCX Cloud and service appliances, such as the HCX-IX Interconnect.  
  
## What's next

  * Learn about security controls and infrastructure security in VMware Engine with the [Security overview](https://docs.cloud.google.com/vmware-engine/docs/concepts-security).
  * Understand how monitoring and alerts are configured for your environments in the [Overview of monitoring](https://docs.cloud.google.com/vmware-engine/docs/concepts-monitoring).
  * Review security advisories and check recommendations for upgrades using the [Security bulletins](https://docs.cloud.google.com/vmware-engine/docs/security-bulletins).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
