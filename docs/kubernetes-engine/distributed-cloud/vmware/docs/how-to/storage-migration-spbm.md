---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/storage-migration-spbm/
title: Storage migration with Storage Policy Based Management \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:33.155930+00:00
---

# Storage migration with Storage Policy Based Management  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/storage-migration-spbm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Storage migration with Storage Policy Based Management Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to migrate disks from one [vSphere datastore](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-storage.html) to another vSphere datastore with [Storage Policy Based Management (SPBM)](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/configure-storage-policy).

1.29: Generally available  
1.28: Preview  
1.16: Not available

You can migrate the following kinds of storage:

  * Storage for system components managed by Google Distributed Cloud, including:

    * Data disks (VMDK files) used by the control-plane nodes of admin clusters and Controlplane V2 user clusters

    * Boot disks (VMDK files) used by all admin cluster and user cluster nodes

    * vSphere Volumes represented by PV/PVCs in the admin cluster and used by the control-plane components of [kubeception](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/plan-ip-addresses-kubeception) user clusters

  * Storage for workloads that you deploy on user cluster worker nodes with PV/PVCs provisioned by the in-tree vSphere volume plugin or the [vSphere CSI driver](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/using-vsphere-csi-driver)




## Prerequisites for an admin cluster

  1. The admin cluster must have an HA control plane. If your admin cluster has a non-HA control plane, [migrate to HA](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-admin-cluster-ha) before you continue.

  2. Verify that the admin cluster has an HA control plane:
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG get nodes
         

Replace ADMIN_CLUSTER_KUBECONFIG with the path of the admin cluster kubeconfig file.

In the output, make sure that you see three control-plane nodes. For example:
         
         admin-cp-1   Ready    control-plane,master ...
         admin-cp-2   Ready    control-plane,master ...
         admin-cp-3   Ready    control-plane,master ...
         




## Prerequisites for all clusters (admin and user)

  1. The cluster must have node auto repair disabled. If node auto repair is enabled, [disable node auto repair](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/node-auto-repair#disabling_node_repair_and_health_checking_for_a_user_cluster).

  2. The cluster must use [Storage Policy Based Management (SPBM)](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-storage.html). If your cluster doesn't use SPBM, [create a storage policy](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/configure-storage-policy) before you continue.

  3. Verify that the cluster uses SPBM:
         
         kubectl --kubeconfig CLUSTER_KUBECONFIG get onpremadmincluster --namespace kube-system \
           -ojson | jq '{datastore: .items[0].spec.vCenter.datastore, storagePolicyName: .items[0].spec.vCenter.storagePolicyName}'
         

(User cluster only) Verify that the node pools use SPBM:
         
         kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG get onpremnodepools --namespace USER_CLUSTER_NAME-gke-onprem-mgmt \
           -ojson | jq '.items[] | {name: .metadata.name, datastore: .spec.vsphere.datastore, storagePolicyName: .spec.vsphere.storagePolicyName}'
         

Replace the following:

     * CLUSTER_KUBECONFIG: the path of the cluster kubeconfig file (admin or user).

     * ADMIN_CLUSTER_KUBECONFIG: the path of the admin cluster kubeconfig file

     * USER_CLUSTER_NAME: the name of the user cluster

In the output, if the `datastore` field is empty and the `storagePolicyName` field is non-empty, then the cluster is using SPBM.

  4. The cluster must not use the vSphere in-tree volume plugin.

If your cluster was upgraded from an earlier version of Google Distributed Cloud, it might have PV/PVCs that were provisioned by the [vSphere in-tree volume plugin](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/storage#kubernetes_in-tree_volume_plugins). This kind of volume might be in use by a control-plane node of a kubeception user cluster or by a workload that you created on a worker node.

List of all PVCs and their StorageClasses:
         
         kubectl --kubeconfig CLUSTER_KUBECONFIG get pvc --all-namespaces  \
            -ojson | jq '.items[] | {namespace: .metadata.namespace, name: .metadata.name, storageClassName: .spec.storageClassName}'
         

List all StorageClasses and see what provisioners they are using:
         
         kubectl --kubeconfig CLUSTER_KUBECONFIG get storageclass
         

In the output, if the `PROVISIONER` column is `kubernetes.io/vsphere-volume`, then PVCs created with this StorageClass are using the vSphere in-tree volume plugin. For the StatefulSets using these PV/PVCs, [migrate them to the vSphere CSI driver](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/using-statefulset-csi-migration-tool).




## Perform the storage migration

Google Distributed Cloud supports two categories of storage migration:

  * Storage vMotion for VMs, which moves VM storage, including attached vSphere CNS volumes used by Pods running on a node, and VMDKs used by these VM CNS volumes attached to the nodes

  * CNS volume relocation, which moves specified vSphere CNS volumes to a compatible datastore without performing storage vMotion for VMs




### Perform storage vMotion for VMs

Migration involves steps that you do in your vSphere environment and commands that you run on your admin workstation:

  1. In your vSphere environment, add your target datastores to your storage policy.

  2. In your vSphere environment, migrate cluster VMs using the old datastore to the new datastore. For instructions, see [Migrate a Virtual Machine to a New Compute Resource and Storage](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1.html).

  3. On your admin workstation, verify that the VMs have been successfully migrated to the new datastore.

Get the Machine objects in the cluster:
         
         kubectl --kubeconfig CLUSTER_KUBECONFIG get machines --output yaml

In the output, under `status.disks`, you can see the disks attached to the VMs. For example:
         
         status:
         addresses:
         – address: 172.16.20.2
           type: ExternalIP
         disks:
         – bootdisk: true
           datastore: pf-ds06
           filepath: me-xvz2ccv28bf9wdbx-2/me-xvz2ccv28bf9wdbx-2.vmdk
           uuid: 6000C29d-8edb-e742-babc-9c124013ba54
         – datastore: pf-ds06
           filepath: anthos/gke-admin-nc4rk/me/ci-bluecwang-head-2-data.vmdk
           uuid: 6000C29e-cb12-8ffd-1aed-27f0438bb9d9
         

Verify that all the disks of all the machines in the cluster have been migrated to the target datastore.

  4. On your admin workstation, run [`gkectl diagnose`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/diagnose) to verify that the cluster is healthy.




### Call CNS Relocation APIs for moving CNS volumes

If you only want to move CNS volumes provisioned by the vSphere CSI driver, you can follow the instructions in [Migrating Container Volumes in vSphere](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-storage.html). This might be simpler if you only have CNS volumes in the old datastore.

## Update your storage policy if needed

In your vSphere environment, update the storage policy to exclude the old datastores. Otherwise, new volumes and re-created VMs might get assigned to an old datastore.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
