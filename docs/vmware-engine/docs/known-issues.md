---
url: https://docs.cloud.google.com/vmware-engine/docs/known-issues/
title: Known issues \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:23.830344+00:00
---

# Known issues  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/known-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Resources ](https://docs.cloud.google.com/vmware-engine/docs/resources)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Known issues

This page describes known issues that you might run into while using Google Cloud VMware Engine.

## General issues

The following are known general issues affecting VMware Engine.

### Built-in vCenter pNIC error alarms trigger on transient network events

**Issue** : Built-in vCenter infrastructure alarms—such as "High pNIC error rate detected"—can intermittently trigger in the vSphere Client console due to transient localized packet anomalies.

**Details** : The built-in VMware alerting framework evaluates underlying physical network interface card (pNIC) counters over short, rigid sampling windows. Because of this design, vCenter can trigger immediate alerts for routine, non-impactful events—such as transient noise or expected packet drop behavior on standby vSAN uplinks—even when the network layer is healthy. Due to built-in path redundancy, these alerts don't impact environment availability or data integrity.

**Workaround** : No customer action or workaround is required. Because an update to built-in vCenter alarm sampling sensitivity isn't expected in the short term, Google has deployed underlying platform intelligence to manage and filter these false positives. For targeted production environments, Google suppresses these built-in customer-facing console alerts. Instead, the Google analytics engine monitors infrastructure data and evaluates the physical layer continuously using a 30-minute rolling average. If Google's analytics engine identifies persistent physical degradation, such as a faulty cable or optic, the platform automatically alerts Google support to investigate and resolve the issue, and systematically dispatches an automated notification to you.

**Status** : This is a known limitation of built-in vCenter alarm evaluation logic. Google manages this behavior through integrated, underlying platform intelligence. VMware is aware of this issue and has advised on the workaround.

### HCX Manager upgrade incorrectly labeled as vSphere version upgrade

**Issue** : HCX Manager upgrade is incorrectly labeled as a "vSphere version upgrade" in the Google Cloud console.

**Details** : Although specific email notifications identifying the HCX upgrade are sent at least 14 days and 24 hours before the event, the automated "Your Private Cloud update has started" and "Your Private Cloud update has completed" notifications reflect a general private cloud update. Furthermore, the Google Cloud console interface explicitly labels the operation as a vSphere version upgrade. This mismatch can cause confusion, particularly for customers who have recently completed a full stack upgrade (for example, vSphere 7.x to 8.x), as it appears the environment is undergoing another major platform update.

**Workaround** : Review the HCX-specific notification emails sent before the maintenance window to confirm the scope of work. If the schedule aligns, the "vSphere version upgrade" status in the Google Cloud console refers strictly to the HCX Manager update. No action is required.

**Status** : This is a known limitation of the current notification system design.

### Provisioning time for vSphere 8.0 update 3 private clouds

**Issue** : VMware Engine now deploys new private clouds with VMware vSphere version 8.0 Update 3 and NSX-T 4.2.1.2. During this upgrade period, private cloud creation and expansion use standard provisioning speeds for all new deployments with the updated versions.

**Details** : Private cloud creation can take up to 140 minutes.

**Workaround** : No workaround is necessary, but plan for additional time when you deploy new private clouds or expand existing clusters.

**Detection** : You might observe longer than usual deployment times for new private clouds or when you expand existing clusters.

**Status** : This is expected behavior due to the version updates and ongoing upgrades.

### Virtual Machine with Windows Server 2022 KB5022842 (OS Build 20348.1547) configured with secure boot enabled not booting up ([90947](https://kb.vmware.com/s/article/90947))

After installing Windows Server 2022 update [KB5022842 (OS Build 20348.1547)](https://msrc.microsoft.com/update-guide/releaseNote/2023-Feb) guest OS can't boot up when the virtual machine(s) is configured with secure boot enabled. To work around this issue, you can do one of the following:

  * Skip [KB5022842](https://msrc.microsoft.com/update-guide/releaseNote/2023-Feb) and use [KB5023705](https://support.microsoft.com/en-gb/topic/march-14-2023-kb5023705-os-build-20348-1607-31770c64-430e-4b0e-8eb4-175980e29f3b)
  * Disable "Secure Boot" on affected VMs



### There is a 100 prefix limit for route advertisements from your private cloud to your VPC network

If your route advertisement exceeds this limit, some prefixes may be dropped. To stay within this limit, implement aggregation on NSX-T Edge.

VMware Engine relies on Cloud Routers to advertise IP address ranges (prefixes or CIDRs) from NSX to a service producer VPC network. These prefixes become custom dynamic routes in the service producer VPC network that is peered with your VPC network.

When you configure your VPC network to import custom dynamic routes in this peering relationship, the NSX prefixes peer custom routes in your VPC network. The number of NSX prefixes you can import is limited by two factors:

  * [Cloud Router's default limit for number of unique prefixes per region](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#limits), which VMware Engine inherits
  * The [maximum number of dynamic routes in a peering group](https://docs.cloud.google.com/vpc/docs/quota#vpc-peering) in your VPC network



### Private cloud operations attempted before the private cloud is fully deployed fail

Operations such as privilege escalation, private cloud expansion, and node replacement are allowed in the Google Cloud VMware Engine portal on operational private clouds that are not fully provisioned yet. However, if you attempt these operations in VMware Engine before the private cloud is fully deployed (including NSX-T and HCX), these operations fail. Don't attempt these operations until you have fully deployed your private cloud.

### VMware Engine is not yet fully supported by VPC Service Controls

VPC Service Controls implements an interim solution (workaround) to allow you to still consume VMware Engine from within a project in a VPC Service Controls perimeter. See [VPC Service Controls](https://docs.cloud.google.com/vmware-engine/docs/concepts-vpc-service-controls) for more information.

### Apigee interoperability with on-premises internet routing

If you use Apigee with VPC peering on the same VPC network as VMware Engine, and you configure VMware Engine to route internet traffic through an on-premises connection, then Apigee outbound communication might also be routed through your on-premises connection. This configuration occurs when you enable VPC Service Controls on the `servicenetworking.googleapis.com` peering as described in [Configure internet access for workload VMs](https://docs.cloud.google.com/vmware-engine/docs/networking/workload-internet-access#enable_routing_internet_traffic_through_an_on-premises_connection).

If Apigee traffic is routed through your on-premises connection, then Apigee no longer uses its configured external IP address for outbound communication to external API backend services. If you rely on Apigee's external IP address for firewall configurations, then you must update your firewall configurations to allow traffic from your on-premises network.

## ESXi hosts might temporarily lose connectivity during collection of diagnostic information

ESXi hosts in environments with NVMe PCIe devices might temporarily lose connectivity during the collection of diagnostic information.

### Root cause

When you use the `vm-support` command or vCenter UI to collect information about ESXi systems, logs are temporarily stored in the `ramdisk /tmp` directory. If the system has many NVMe PCIe devices or the log file is large, the `ramdisk /tmp` directory quickly becomes full, which can lead to your ESXi host to temporarily lose connectivity until the `vm-support` collection completes.

### Workaround:

Excluding the NVME manifest from the select logs section in the log bundle creation page prevents the `ramdisk /tmp` directory from becoming full and verifies that the EXSi host doesn't lose network connectivity. To exclude the NVMe manifest, do the following:

  1. Sign in to vCenter using the `cloudowner` username and password.
  2. In the inventory, right-click the vCenter Server instance where you want the exclusion.
  3. Click **Export System Logs...**.
  4. Select the ESXi host that you want to exclude the logs bundle from.
  5. Under **Select Logs** , scroll to **Storage** and clear the **NVMe** option, then click **Exported logs**. The NVMe manifest is now excluded.



For more information on this fix, see [VMware ESXi 7.0 Update 3q](https://docs.vmware.com/en/VMware-vSphere/7.0/rn/vsphere-esxi-70u3q-release-notes/index.html).

## Private cloud resource name translation error

If you are running VMware Engine Horizon (VDI) on Google Cloud VMware Engine, you may encounter errors after changing your private cloud resource naming to meet the standards for Google Cloud CLI and VMware Engine API.

The following example error occurs when changing private cloud resource names without editing properly provisioning Horizon Desktop Pools:
    
    
    Error during Provisioning Cloning of VM Desktop-UK-005 has failed. No resource pool available for the pool: ic-pool-1
    
    
    
    Error during Provisioning Cloning of VM Desktop-UK-005 has failed. No datastores available for the pool: {}ic-pool-1
    

To resolve this issue, complete the following steps before your scheduled name translation date:

  1. Access the VMware Horizon dashboard.
  2. Edit **all** Horizon Desktop Pools for both Full Clone and Instant Clone Pools and set them to **Disable Provisioning**.



Once the private cloud resource name change is complete, complete the following steps:

  1. Edit each Desktop Pool and reconfigure the following settings on the **vCenter Settings** tab for both Full Clone and Instant Clone Pools:

     * Resource Pool
     * Datastore
**Note:** Failure to edit these settings for both Full Clone and Instant Clone Pools will result in a provisioning error.
  2. Set each Pool status back to **Enable Provisioning**.

  3. Test each pool by adding or removing a desktop from the Pool to verify provisioning is functioning properly.




The VMware Engine team is actively working to provide an interoperability solution as soon as possible. To stay up to date on feature availability, contact your account team.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
