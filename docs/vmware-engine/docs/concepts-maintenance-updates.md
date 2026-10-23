---
url: https://docs.cloud.google.com/vmware-engine/docs/concepts-maintenance-updates/
title: Private cloud maintenance and updates \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:05.765853+00:00
---

# Private cloud maintenance and updates  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/concepts-maintenance-updates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Private cloud maintenance and updates

Private cloud environments are designed in the following ways to have no single point of failure:

  * ESXi clusters are configured with vSphere high availability (HA). Clusters are sized to have at least one spare node for resiliency.
  * vSAN provides redundant primary storage, requiring at least three nodes to provide protection against a single failure. For larger clusters, you can configure vSAN to provide higher resiliency.
  * vCenter, PSC, and NSX Manager virtual machines (VMs) are configured with RAID-10 storage to protect against storage failure. The VMs are additionally protected against node and network failures by vSphere HA.
  * ESXi hosts have redundant fans and NICs.
  * TOR and spine switches are configured in HA pairs to provide resiliency.



VMware Engine continuously monitors uptime, monitors availability, and provides availability SLAs for the following types of VMs:

  * ESXi hosts
  * vCenter
  * PSC
  * NSX Manager



VMware Engine continuously monitors the following for failures:

  * Hard disks
  * Physical NIC ports
  * Servers
  * Fans
  * Power
  * Switches
  * Switch ports



If a disk or node fails, VMware Engine immediately and automatically adds a new node to the affected VMware cluster to restore service operability. The following processes take place on your private cloud:

  * **Automated monitoring and alerting** : Our monitoring system constantly tracks the health of your nodes. When an issue is detected that indicates a potential hardware failure, an alert is triggered.
  * **Human-in-the-loop for diagnosis** : While the system is designed for automated replacement, our engineers review these alerts to quickly determine the root cause. This ensures that we're addressing the correct issue and prevents unnecessary node replacements when a simpler solution (like a reboot) is recommended. For example, temporary network issues or software glitches can trigger similar alerts to hardware failures, and we want to avoid impacting your cluster with node replacement when it might not be the recommended action. An unnecessary node replacement triggers a full vSAN Resync, which is a storage I/O intensive operation. 
  * **Automated node replacement for hardware failures** : If our engineers confirm a hardware failure, the automated node replacement process begins immediately. A new node is added to your cluster, and vSAN initiates the data resync on that node.



The following VMware elements in private clouds are backed up, maintained, and updated:

  * ESXi
  * vCenter Platform Services Controller
  * vSAN
  * NSX



## Backup and restore

Backups include the following:

  * Nightly incremental backups of vCenter, PSC, and DVS rules.
  * vCenter built-in APIs to back up components at the application layer.
  * Automatic backup prior to update or upgrade of the VMware management software.



## Maintenance

The following types of planned maintenance are included.

### Backend and internal maintenance

Backend and internal maintenance typically involves reconfiguring physical assets or installing software patches. It doesn't affect normal consumption of the assets being serviced. With redundant NICs going to each physical rack, normal network traffic and private cloud operations aren't affected. You might notice a performance impact only if your organization expects to use the full redundant bandwidth during the maintenance interval.

### Portal maintenance

Some limited service downtime is required when the control plane or infrastructure is updated. Maintenance intervals can be as frequent as once per month, and are expected to decline in frequency over time. VMware Engine notifies you about impending portal maintenance and makes an effort to keep the maintenance interval as short as possible. During a portal maintenance interval, the following services continue to function without any impact:

  * VMware management plane and applications
  * vCenter access
  * All networking and storage



### VMware infrastructure maintenance

It's occasionally necessary to make changes to the configuration of the VMware infrastructure. These intervals can occur every one to two months, but the frequency is expected to decline over time. Google can usually perform this type of maintenance, including certificate updates, without interrupting normal private cloud consumption. During a VMware maintenance interval, the following services continue to function without any impact:

  * VMware management plane and applications
  * vCenter access
  * All networking and storage



## Updates and upgrades

VMware Engine is responsible for lifecycle management of VMware software (ESXi, vCenter, PSC, and NSX) in private clouds.

Software updates include the following:

  * **Patches:** security patches or bug fixes released by VMware
  * **Updates:** minor version change of a VMware stack component
  * **Upgrades:** major version change of a VMware stack component



VMware Engine tests critical security patches as soon as they become available from VMware. Google will aim to commence the rollouts of relevant critical patches to private cloud environments within one week of their availability. The actual patching completion timeline will vary depending on scheduling availability and the need to time the patching to avoid any downtime for customer workloads.

When a new major version of VMware software is available, VMware Engine works with customers to coordinate a suitable maintenance window for applying the upgrade. VMware Engine applies major version upgrades at least six months after the major version is released and notifies customers one month in advance of applying major version upgrades.

VMware Engine also works with key industry vendors to ensure that they support the latest VMware software version before rolling out a major version upgrade. For information about support for specific vendors, [contact Cloud Customer Care](https://docs.cloud.google.com/vmware-engine/docs/getting-support).

### Certificate update responsibility

Certificate updates are a Google-owned responsibility. If you get a certificate update error, no action is required and the certificate is renewed before expiration. However, if LDAPS is configured in your private cloud, you are solely responsible for the specific certificate associated with that error. Certificate updates can occur during VMware infrastructure maintenance.

### Preparation

Google recommends taking the following preparations before starting an update or upgrade:

  * **Check storage capacity:** Ensure your vSphere cluster's storage space utilization is lower than 80% to maintain the [SLA](https://docs.cloud.google.com/vmware-engine/sla). If the utilization is higher than 80%, upgrades might take longer than normal or fail completely. If your storage utilization is higher than 70%, [add a node](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-manage-private-cloud#add-nodes) to expand the cluster and avoid any potential downtime during upgrades.
  * **Change vSAN storage policies with FTT of 0:** Change VMs configured with a vSAN storage policy for Failures to Tolerate (FTT) of 0 to a vSAN storage policy with FTT of 1 to maintain the SLA.
  * **Remove VM CD mounts:** Remove any CDs mounted on your workload VMs that are not compatible with vMotion.
  * **Complete VMware tool installations:** Complete any installations or upgrades of VMware tools before the scheduled upgrade begins.
  * **Remove SCSI bus sharing on VMs:** Remove SCSI bus sharing on VMs if you don't want the VMs to be powered off.
  * **Remove inaccessible VMs and datastores:** Remove unused and inaccessible VMs from the vCenter inventory. Remove any inaccessible external datastores.
  * **Disable Distributed Resource Scheduler (DRS) rules:** DRS rules that pin a VM to a host prevent a node from entering maintenance mode. You can disable the DRS rules before the upgrade and enable them after the upgrade is complete.
  * **Update VMware add-ons and third-party solutions:** Verify that VMware add-ons and third party solutions deployed on your private cloud vCenter are compatible with the post-upgrade versions mentioned previously. Examples of tools include those for backup, monitoring, disaster recovery orchestration, and other similar functions. Check with the solution vendor and update ahead of time if necessary to ensure compatibility after the upgrade.



### Upgrade duration and background processes

The following factors can affect upgrade duration:

  * **vSAN Resyncs** : The duration of the upgrade process, specifically the removal of temporary nodes, varies based on vSAN data resynchronization requirements. vSAN resync and cluster rebalancing tasks might extend beyond the designated maintenance window. These are expected background processes and won't disrupt workload availability.
  * **Underlying hardware issues** : In rare cases, host reboots during the upgrade might reveal underlying hardware faults. To maintain SLA and cluster health, the system prioritizes replacing the faulty hardware before proceeding. This necessary intervention might extend the overall upgrade duration.



## Configurations that might affect maintenance processes

VMware Engine leverages VMware's Maintenance Mode to carry out upgrades, updates, and node maintenance. This helps ensure continued operation of your Private Cloud workloads. However, the following configurations might require additional steps before a node can enter Maintenance Mode:

  * **DRS rules:** MUST rules that force VMs to stay on a specific node.
  * **SCSI bus sharing:** VMs configured to share SCSI buses.
  * **CD-ROM mounts:** VMs with CD-ROMs attached, especially if those CD-ROMs cannot be moved to another node using vMotion.
  * **Serial port connections:** VMs using serial port connections that prevent them from being moved to another node using vMotion.
  * **Raw device mappings (RDM):** VMs directly accessing physical storage devices.

**Important:** Proactively managing these configurations can help streamline future VMware Engine maintenance procedures.

### If action is necessary

If any of these configurations exist on a node, Cloud Customer Care notifies you at least 24 hours before taking the remediation steps required to maintain the availability of your Private Cloud. In some cases, steps such as powering off a VM and moving it with vMotion and then powering it on, or removal of CD-ROMs, might briefly disrupt your workload.

## What's next

  * Learn about [VMware Engine security](https://docs.cloud.google.com/vmware-engine/docs/concepts-security)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
