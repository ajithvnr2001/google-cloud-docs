---
url: https://docs.cloud.google.com/vmware-engine/docs/maintain-private-cloud-configuration-health/
title: Maintain private cloud configuration health \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:38.327410+00:00
---

# Maintain private cloud configuration health  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/maintain-private-cloud-configuration-health/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Maintain private cloud configuration health

This page describes how Cloud Administrators can use Google Cloud VMware Engine to regularly monitor their configuration to ensure it remains ready for future upgrades. To help you maintain private cloud stability, Google Cloud VMware Engine performs regular health checks for configuration drift, logs details in Cloud Logging, and notifies you of any critical issues in email summaries. This approach helps you identify and resolve configuration drift in your private cloud.

**Caution:** When Google Cloud VMware Engine detects configuration drift, remediate it immediately. Failure to act can result in repetitive notifications and might leave your environment in an unsupported state. 

## Configuration health checks

VMware Engine performs the following checks to ensure your environment remains in a supported and efficient state.

### NSX-T Tier-0 gateway name

To enable automated lifecycle management and updates, ensure the management NSX-T Tier-0 gateway is named exactly `Provider-LR`. You can verify the gateway name in NSX-T Manager by navigating to **Networking > Tier-0 Gateways**.

#### Impact

If you rename this gateway to a name other than `Provider-LR`, you might experience failed upgrades or delays in scheduled maintenance.

#### Gateway name remediation

  1. [Access NSX-T Manager](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-manage-subnets#access_nsx_manager).
  2. Navigate to **Networking > Tier-0 Gateways**.
  3. Identify the provider gateway and click **Edit**.
  4. Change the name of the gateway to `Provider-LR` and save the changes.



### NSX-T Edge high-availability mode

To maintain predictable throughput and support stateful services, ensure your NSX-T Tier-0 gateway uses the **Active-Standby** configuration.

#### Impact

If you use other modes (such as **Active-Active**), you may encounter traffic disruptions during failovers or inconsistent performance if a node fails.

#### High-availability mode remediation

  1. [Access NSX-T Manager](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-manage-subnets#access_nsx_manager).
  2. Navigate to **Networking > Tier-0 Gateways**.
  3. Locate the identified gateway and click **Edit**.
  4. Set the **High Availability Mode** to **Active-Standby** and save.



### Storage policy for VMs

To protect your data from physical host failures, ensure your virtual machines (VMs) use a storage policy with **Failures to Tolerate (FTT)** set to at least 1. An FTT of 0 means you have no data redundancy.

#### Impact

If a physical host fails and your FTT is 0, you will experience permanent data loss or corruption. Maintenance operations also take longer without a redundant storage policy.

#### Storage policy for VMs remediation

  1. [Access vSphere Client](https://docs.cloud.google.com/vmware-engine/docs/vmware-platform/howto-access-management).
  2. Locate the affected VM and select **Edit Settings**.
  3. Identify the specific disks (for example, **Hard disk 1**).
  4. Change the **VM storage policy** to a resilient policy such as FTT 1 or higher.



## Private cloud network monitoring

VMware Engine deploys specialized prober VMs in your private cloud to help maintain high availability and network reliability.

### Purpose

The prober VMs perform the following functions:

  * Actively monitor network reachability and latency.
  * Proactive simulation of data path traffic patterns to identify connectivity issues early.
  * Validation that the network correctly processes traffic between NSX-T segments and the underlay.



### Operating system and footprint

Prober VMs run on Rocky Linux and have a minimal resource footprint (2 vCPU, 1 GB RAM).

### Deployment

VMware Engine deploys prober VMs in the management folder and resource pool. Depending on the private cloud, prober VMs are present in multiple clusters and availability zones, with a maximum of a single prober VM per cluster.

### Security

VMware Engine manages the lifecycle and security of these VMs, including regular security scans and software updates.

### Restrictions

Don't delete or power-cycle prober VMs. These actions can impact the ability of VMware Engine to monitor your environment and proactively resolve issues.

## Extension and interoperability checks

The following checks and recommended actions ensure your extensions and paired on-premises environments are compatible with upcoming VMware Engine updates.

Service check | Benefit | Action  
---|---|---  
**Zerto version** | Enables system-wide upgrades and prevents disaster recovery failures. | In **vCenter** , go to **Administration > Solutions > Client Plug-ins** to upgrade the Zerto plugin.  
**HCX local version** | Maintains compatibility with infrastructure updates and migration features. | Install latest updates in **HCX Cloud Manager UI > System Updates**.  
**HCX remote version** | Prevents Network Extension failures during site-pairing upgrades. | Upgrade on-premises HCX Connector by using its management UI.  
**Remote vCenter version** | Ensures API compatibility and inventory discovery during migrations. | Upgrade on-premises vCenter to meet the minimum required version.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
