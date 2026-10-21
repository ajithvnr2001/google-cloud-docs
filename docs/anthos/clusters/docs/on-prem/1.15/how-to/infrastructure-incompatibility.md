---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/infrastructure-incompatibility/
title: Infrastructure incompatibility \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:11:50.966259+00:00
---

# Infrastructure incompatibility  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/infrastructure-incompatibility/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Infrastructure incompatibility Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/infrastructure-incompatibility)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/infrastructure-incompatibility)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



## vSphere feature incompatibility

This section describes the vSphere features that are incompatible with Google Distributed Cloud.

### VM snapshot

[VM snapshot](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vm_admin.doc/GUID-CA948C69-7F58-4519-AEB1-739545EA94E5.html) is not compatible with Google Distributed Cloud. Taking snapshots of VMs created by Google Distributed Cloud will break many features including cluster upgrade, cluster update, [node auto-repair](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/node-auto-repair) and [admin cluster control plane recovery](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/repair-admin-control-plane). When Google Distributed Cloud tries to manage a VM with snapshots, you will see failures such as `Invalid configuration for device '0'` in the `csi-controller-manager` and `vsphere-controller-manager` logs. For more information on snapshots, see [Best Practices for using VMware snapshots](https://kb.vmware.com/s/article/1025279).

Don't create snapshots on Anthos VMs. To recover from VM or storage failures, see [Recovery from VM failures](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/concepts/high-availability-disaster-recovery#recovery_from_vm_failures) and [Recovery from storage failures](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/concepts/high-availability-disaster-recovery#recovery_from_storage_failures).

**Note:** Using a third-party solution, such as Commvault, to back up VMs isn't supported by GKE Enterprise. Backing up VMs with a third-party solution may lead to unforeseen errors in cluster operations.

### VM clone

[Cloning a VM](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vm_admin.doc/GUID-1E185A80-0B97-4B46-A32B-3EF8F309BEED.html) that is created and managed by Google Distributed Cloud may result in data and cluster state inconsistencies.

Don't clone Anthos VMs. To recover from VM or storage failures, see [Recovery from VM failures](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/concepts/high-availability-disaster-recovery#recovery_from_vm_failures) and [Recovery from storage failures](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/concepts/high-availability-disaster-recovery#recovery_from_storage_failures).

### Storage vMotion

[Storage vMotion](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vcenterhost.doc/GUID-A15EE2F6-AAF5-40DC-98B7-0DF72E166888.html) lets you migrate the virtual disks of a VM from one datastore to another. This is different from the regular [vMotion](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/concepts/high-availability-disaster-recovery#vsphere_ha_and_vmotion), which migrates a VM from one host to another. vMotion is supported by Google Distributed Cloud.

Storage vMotion is not compatible with Google Distributed Cloud whether you use the in-tree driver or [Container Storage Interface (CSI)](https://docs.vmware.com/en/VMware-vSphere-Container-Storage-Plug-in/2.0/vmware-vsphere-csp-getting-started/GUID-5B7955AA-E720-4C73-8330-1C34A0B054B3.html#GUID-5B7955AA-E720-4C73-8330-1C34A0B054B3) driver. Operations such as cluster update, upgrade, user cluster creation and [node auto-repair](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/node-auto-repair) will fail when you use storage vMotion.

Don't perform a storage vMotion, if possible. To recover from unplanned storage vMotion, or to plan a workaround, contact Google support.

### Storage DRS

[Storage DRS](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.resmgmt.doc/GUID-827DBD6D-08B7-4411-9214-9E126671457F.html) manages virtual machine disk placement and migration to balance the storage space or I/O resources between datastores in the datastore cluster.

Don't activate Storage DRS as it is not compatible with Google Distributed Cloud.

### Changed Block Tracking(CBT)

[Chnged Block Tracking(CBT)](https://kb.vmware.com/s/article/1020128) is a VMkernel feature that identifies blocks of data that have changed or are in use, which is enabled through VMware API calls by 3rd-party backup software or appliances.

Don't use 3rd-party backup software or appliances to backup Google Distributed Cloud VMs. They usually enable CBT through the VMware API that is not compatible with Google Distributed Cloud.

## Networking incompatibility

This section applies to you if you are using the [Seesaw load balancer](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/bundled-load-balance).

### Cisco ACI with IP Data-plane Learning

[Cisco Application Centric Infrastructure (ACI)](https://www.cisco.com/site/us/en/products/networking/cloud-networking/application-centric-infrastructure/index.html) with [Dataplane IP Learning](https://www.cisco.com/c/en/us/td/docs/dcn/aci/apic/5x/l3-configuration/cisco-apic-layer-3-networking-configuration-guide-51x/m_dataplane_ip_learning_v2.pdf) is not compatible with Seesaw load balancer. We recommend that you use MetalLB as your load balancer as Seesaw is in maintenance mode, or disable Dataplane IP Learning when using Seesaw as your load balancer.

### Stateful NSX-T Distributed Firewall (DFW)

Stateful [NSX-T DFW](https://docs.vmware.com/en/VMware-NSX-T-Data-Center/3.2/administration/GUID-6AB240DB-949C-4E95-A9A7-4AC6EF5E3036.html) is not compatible with Seesaw load balancer. We recommend that you use MetalLB as your load balancer as Seesaw is in maintenance mode, or configure a stateless NSX-T DFW policy for the Seesaw VMs when using Seesaw as your load balancer. For more information, see [Configuring stateless NSX-T distributed firewall policies for use with Seesaw load balancer](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/bundled-load-balance#configuring_stateless_nsx-t_distributed_firewall_policies_for_use_with_seesaw_load_balancer).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
