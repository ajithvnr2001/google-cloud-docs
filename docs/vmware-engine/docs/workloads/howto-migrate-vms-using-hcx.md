---
url: https://docs.cloud.google.com/vmware-engine/docs/workloads/howto-migrate-vms-using-hcx/
title: Use VMware HCX to migrate VMware VMs \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:18.653412+00:00
---

# Use VMware HCX to migrate VMware VMs  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/workloads/howto-migrate-vms-using-hcx/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use VMware HCX to migrate VMware VMs

This page describes how to use VMware HCX to migrate your virtual machines (VMs) from your VMware environment to Google Cloud VMware Engine. VMware HCX abstracts vSphere-based resources in your VMware environment and cloud resources, presenting them to applications as one continuous resource. This abstraction creates a hybrid infrastructure, which simplifies workload migration, mobility, and protection between your on-premises data center and Google Cloud VMware Engine.

## Before you begin

  1. Make sure that the VMware product versions that you use on-premises are supported by HCX for your selected migration type (live, cold, or bulk). For more information about source vSphere versions and their corresponding supported HCX features, see the [VMware product interoperability matrix](https://interopmatrix.vmware.com/Interoperability).

The HCX download depot is decommissioned. HCX Connector upgrades are managed as part of the VMware Engine service. [Contact support](https://cloud.google.com/support-hub) if you need help to upgrade the HCX Connector.

  2. You need a [Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) and a [Virtual Private Cloud (VPC) network](https://docs.cloud.google.com/vpc/docs/vpc).

  3. Connect your VMware environment to the VPC network in your project by using [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn) or [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect). If you use Cloud VPN, review the [minimum network underlay requirements for VMware HCX](https://techdocs.broadcom.com/us/en/vmware-cis/hcx/vmware-hcx/4-11/vmware-hcx-user-guide-4-11/preparing-for-hcx-installations/network-underlay-minimum-requirements.html).




The overview described in this page is independent of the specific versions of vSphere in your VMware environment as long as your vSphere version is compatible with HCX.

## Deploy a hybrid infrastructure solution using VMware HCX in your private cloud

To deploy the HCX migration solution for Google Cloud VMware Engine, complete the following steps:

  * Create a private cloud in your VMware Engine environment.
  * Connect your VMware environment network to your private cloud.
  * Prepare, install, configure, and use VMware HCX components in your VMware environment.



### Create a private cloud in your environment

To create a private cloud in your Google Cloud VMware Engine environment, see [Creating a Google Cloud VMware Engine private cloud](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-create-private-cloud). When you create a private cloud, VMware Engine performs the following actions:

  * Deploys the HCX Cloud Manager appliance in the system management network and the management resource pool in your private cloud.
  * Configures HCX Cloud Manager with the compute profile (network pool) information.
  * Establishes network connectivity between the various HCX service appliances and HCX Cloud Manager.
  * Generates a license activation key and configures HCX Cloud Manager to use it.
  * Registers HCX Cloud Manager with the VMware HCX service.



Because VMware Engine automatically deploys HCX during private cloud creation, you don't need to provide a subnet IP address range for HCX services.

### Connect your VMware environment network to your private cloud

  1. [Connect your VMware environment network to your private cloud](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-connect-to-onpremises) by using your Cloud Interconnect.
  2. Add your VMware Engine subnet IP address ranges to [custom routes](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/advertising-custom-ip) for the Cloud Router that terminates the Cloud Interconnect attachment.
  3. Open the [required network ports](https://docs.cloud.google.com/vmware-engine/docs/quickstart-networking-requirements#ports-required-for-accessing-vcenter) on your VMware environment firewall.



## Prepare for HCX Connector installation in your VMware environment

**Note:** As of May 19, 2025, VMware Engine uses HCX 4.10.3 or later. In this version, HCX Connector keys are no longer required for activation. HCX is automatically activated, and inherits licensing when the HCX Connector is paired with HCX Cloud Manager. For more information, see the [May 19, 2025 service announcement](https://docs.cloud.google.com/vmware-engine/docs/service-announcements#2025-05-19).

  1. Verify the current HCX Cloud Manager version in your private cloud: 
     1. Sign in to the vCenter client UI.
     2. Go to the **HCX** section.
     3. Select **System Updates** and record the local HCX version.
  2. Download the equivalent version of the HCX Connector OVA (matching the version you recorded in the previous step). For more information, see [Broadcom KB395372](https://knowledge.broadcom.com/external/article/395372) and the Broadcom documentation for [downloading the HCX OVAs for private clouds](https://techdocs.broadcom.com/us/en/vmware-cis/hcx/vmware-hcx/4-11/vmware-hcx-user-guide-4-11/installing-the-hcx-manager-appliance/about-hcx-manager-ovas/download-the-hcx-ovas-for-private-clouds.html). 
     * If you have a Broadcom support account, download the OVA from the Broadcom Support Portal: 
       1. Go to the [Broadcom Support Portal](https://support.broadcom.com).
       2. Sign in with your credentials.
       3. Navigate to the HCX product section to download the HCX OVA and the required upgrade bundles.
     * If you don't have a Broadcom support account, [contact support](https://cloud.google.com/support-hub) to obtain the HCX OVA.
  3. Update or install the HCX Connector to the same version as the HCX Cloud Manager deployed in the VMware Engine private cloud.



### Install HCX Connector in your VMware environment

Install and configure HCX Connector in your VMware environment by following the instructions in the [VMware HCX User Guide](https://techdocs.broadcom.com/us/en/vmware-cis/hcx/vmware-hcx/4-11/vmware-hcx-user-guide-4-11/about-the-vmware-hcx-user-guide.html).

  1. Prepare your VMware environment for HCX Connector installation. 
     1. Identify available IP addresses.
     2. If necessary, create VLANs or subnets.
  2. Deploy the HCX Connector OVA on your VMware environment.
  3. Activate HCX Connector. For details, see the Broadcom documentation for [managing HCX licenses](https://techdocs.broadcom.com/us/en/vmware-cis/hcx/vmware-hcx/4-11/vmware-hcx-user-guide-4-11/managing-licenses.html). You can use one of the following options: 
     * Use a VCF license.
     * Use an Evaluation license with [service inheritance](https://techdocs.broadcom.com/us/en/vmware-cis/hcx/vmware-hcx/4-11/vmware-hcx-user-guide-4-11/preparing-for-hcx-installations/hcx-activation-and-licensing/understanding-service-inheritance.html) from HCX Cloud running on VMware Engine.
     * Use activation keys provided in HCX 4.10 or earlier. These keys remain active for up to 450 days after upgrading to HCX 4.11. You must replace activation keys with a valid license before they expire.
  4. Configure HCX Connector.



## Use HCX Cloud Manager for workload migration

To migrate workloads from your VMware environment to your private cloud using HCX, see the [VMware HCX User Guide](https://techdocs.broadcom.com/us/en/vmware-cis/hcx/vmware-hcx/4-11/vmware-hcx-user-guide-4-11/about-the-vmware-hcx-user-guide.html).

You can perform the following operations:

  * Pair the two sites (VMware environment and private cloud)
  * Perform and schedule migrations: 
    * Cold migrations
    * Bulk migrations
    * vMotion migrations
  * Extend Layer 2 networks

**Note:** Before extending a Layer 2 network, review the [recommended MTU settings](https://docs.cloud.google.com/vmware-engine/docs/concepts-vlans-subnets#recommended_mtu_settings) and apply them to the HCX uplink profiles in both your VMware environment and in VMware Engine.

## External references

  * [VMware HCX User Guide](https://techdocs.broadcom.com/us/en/vmware-cis/hcx/vmware-hcx/4-11/vmware-hcx-user-guide-4-11/about-the-vmware-hcx-user-guide.html)
  * [Learning Hybrid Cloud Extension (HCX)](https://emadyounis.com/learning-hybrid-cloud-extension-hcx-part-1-overview/)
  * [Learning Hybrid Cloud Extension (HCX) Part 2: Migration Types](https://emadyounis.com/learning-hybrid-cloud-extension-hcx-part-2-migration-types/)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
