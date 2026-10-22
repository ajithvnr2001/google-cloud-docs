---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/infrastructure-incompatibility/
title: Infrastructure incompatibility \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:33.982647+00:00
---

# Infrastructure incompatibility  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/infrastructure-incompatibility/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Infrastructure incompatibility Stay organized with collections  Save and categorize content based on your preferences. 

## vSphere feature incompatibility

This section describes the vSphere features that are incompatible with Google Distributed Cloud.

### VM snapshot

[VM snapshot](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-virtual-machine-administration.html) is not compatible with Google Distributed Cloud. Taking snapshots of VMs created by Google Distributed Cloud will break many features including cluster upgrade, cluster update, [node auto-repair](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/node-auto-repair) and [admin cluster control plane recovery](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/repair-admin-control-plane). When Google Distributed Cloud tries to manage a VM with snapshots, you will see failures such as `Invalid configuration for device '0'` in the `csi-controller-manager` and `vsphere-controller-manager` logs. For more information on snapshots, see [Best Practices for using VMware snapshots](https://knowledge.broadcom.com/external/article?legacyId=1025279).

Don't create snapshots on Google Distributed Cloud VMs. To recover from VM or storage failures, see [Recovery from VM failures](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/high-availability-disaster-recovery#recovery_from_vm_failures) and [Recovery from storage failures](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/high-availability-disaster-recovery#recovery_from_storage_failures).

**Note:** Using a third-party solution, such as Commvault, to back up VMs isn't supported by Google Distributed Cloud. Backing up VMs with a third-party solution may lead to unforeseen errors in cluster operations.

### VM clone

[Cloning a VM](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-virtual-machine-administration.html) that is created and managed by Google Distributed Cloud may result in data and cluster state inconsistencies.

Don't clone Google Distributed Cloud VMs. To recover from VM or storage failures, see [Recovery from VM failures](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/high-availability-disaster-recovery#recovery_from_vm_failures) and [Recovery from storage failures](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/high-availability-disaster-recovery#recovery_from_storage_failures).

### vSAN File Service

[Using vSAN File Service to Provision File Volumes](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-storage.html) supports `ReadWriteMany` or `ReadOnlyMany` persistent volumes that can be shared between multiple pods or applications.

Don't use that in Google Distributed Cloud as it may block node drain and fail the diagnose.

You can run the following command to list all PVCs:
    
    
    kubectl --kubeconfig CLUSTER_KUBECONFIG get pvc --all-namespaces \
        -ojson | jq '.items[] | {namespace: .metadata.namespace, name: .metadata.name, accessModes: .spec.accessModes}'
    

If there is any PVC having `ReadWriteMany` or `ReadOnlyMany` in its `accessModes`, contact Google support for a workaround.

### Storage vMotion

[Storage vMotion](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vcenter-and-host-management.html) lets you migrate the virtual disks of a VM from one datastore to another. This is different from the regular [vMotion](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/high-availability-disaster-recovery#vsphere_ha_and_vmotion), which migrates a VM from one host to another. vMotion is supported by Google Distributed Cloud.

Storage vMotion is only compatible with Google Distributed Cloud when the clusters are configured with [storage policies](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/configure-storage-policy). Otherwise, operations such as cluster update, upgrade, user cluster creation and [node auto-repair](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/node-auto-repair) will fail when you use storage vMotion.

To recover from unplanned storage vMotion migration, or to plan a workaround, contact Google support.

### Storage DRS

[Storage DRS](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.resmgmt.doc/GUID-827DBD6D-08B7-4411-9214-9E126671457F.html) manages virtual machine disk placement and migration to balance the storage space or I/O resources between datastores in the datastore cluster.

Don't activate Storage DRS as it is not compatible with Google Distributed Cloud.

### Changed Block Tracking(CBT)

[Changed Block Tracking(CBT)](https://kb.vmware.com/s/article/1020128) is a VMkernel feature that identifies blocks of data that have changed or are in use, which is enabled through VMware API calls by 3rd-party backup software or appliances.

Don't use 3rd-party backup software or appliances to backup Google Distributed Cloud VMs. They usually enable CBT through the VMware API that is not compatible with Google Distributed Cloud.

## Networking incompatibility

This section applies to you if you are using the [Seesaw load balancer](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#loadbalancer-seesaw-section).

### Cisco ACI with Dataplane IP Learning

[ Cisco Application Centric Infrastructure (ACI)](https://www.cisco.com/site/us/en/products/networking/cloud-networking/application-centric-infrastructure/index.html) with [ Dataplane IP Learning](https://www.cisco.com/c/en/us/td/docs/dcn/aci/apic/5x/l3-configuration/cisco-apic-layer-3-networking-configuration-guide-51x/m_dataplane_ip_learning_v2.pdf) is incompatible with Seesaw and MetalLB load balancers. We recommend that you use [manual load balancing](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manual-load-balance), or disable Dataplane IP Learning when using Seesaw or MetalLB as your load balancer. Additionally, Seesaw is in maintenance mode. As of Google Distributed Cloud version 1.32, upgrades are blocked for clusters using Seesaw. You must [migrate clusters to recommended features](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/migrate-recommended-features) before upgrading to 1.32. 

### Stateful NSX-T Distributed Firewall (DFW)

Stateful [NSX-T DFW](https://docs.vmware.com/en/VMware-NSX-T-Data-Center/3.2/administration/GUID-6AB240DB-949C-4E95-A9A7-4AC6EF5E3036.html) is not compatible with the Seesaw load balancer. We recommend that you use MetalLB as your load balancer as Seesaw is in maintenance mode, or configure a stateless NSX-T DFW policy for the Seesaw VMs when using Seesaw as your load balancer. For more information, see [Configuring stateless NSX-T distributed firewall policies for use with Seesaw load balancer](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/bundled-load-balance#configuring_stateless_nsx-t_distributed_firewall_policies_for_use_with_seesaw_load_balancer) in the version 1.16 documentation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
