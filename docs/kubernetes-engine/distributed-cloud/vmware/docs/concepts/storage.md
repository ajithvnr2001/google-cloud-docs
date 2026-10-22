---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/storage/
title: Storage \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:04.913744+00:00
---

# Storage  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Storage Stay organized with collections  Save and categorize content based on your preferences. 

This page explains Google Distributed Cloud (software only) for VMware storage concepts.

## Summary

Google Distributed Cloud integrates with external block or file storage systems through:

  * The vSphere Container Storage Interface (CSI) driver
  * Third party CSI drivers
  * Kubernetes in-tree volume plugins



## vSphere datastores

When you create an admin cluster, you specify an existing vSphere [datastore](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-storage.html) for the cluster's etcd data.

When you create a user cluster, you can use the same datastore as the admin cluster, or you can specify a different datastore. You can also specify datastores for individual node pools.

The vSphere datastores used by the admin and user clusters can be backed by NFS, vSAN, or VMFS on a block device, such as an external storage array. In a multi-host environment, each block device must be attached to all the hosts in the environment, and the datastore must be configured on each host via the [**Mount Datastore on Additional Hosts**](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-storage/working-with-datastores-in-vsphere-storage-environment/basic-administrative-operations-for-vsphere-datastores/mount-datastores.html) option.

## StorageClasses

When you create a [PersistentVolumeClaim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims), you can specify a StorageClass that provides information about how the storage will be provisioned. If you don't specify a StorageClass, then the default StorageClass gets used.

### Admin cluster StorageClass

In admin clusters, there is a StorageClass named `standard`, and it is designated as the default StorageClass. The `standard` StorageClass lists the vSphere in-tree volume plugin as the provisioner.

To view the `standard` StorageClass:
    
    
    kubectl --kubeconfig ADMIN_CLUSTER_KUBECONFIG get storageclass \
        standard --output yaml
    

In the output, you can see that `standard` is the default StorageClass and the provisioner is the vSphere in-tree volume plugin, `kubernetes.io/vsphere-volume`. You can also see the name of a vSphere datastore.
    
    
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      annotations:
        storageclass.kubernetes.io/is-default-class: "true"
      ...
      labels:
        bundle.gke.io/component-name: admin-storage-class
      name: standard
    ...
    parameters:
      datastore: vsanDatastore
    provisioner: kubernetes.io/vsphere-volume
    ...
    

### User cluster StorageClasses

In user clusters, there is a StorageClass named `standard` and another StorageClass named `standard-rwo`.

The `standard-rwo` StorageClass is designated as the default StorageClass, and it lists the vSphere CSI driver as the provisioner.

To view the `standard-rwo` StorageClass:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get storageclass \
        standard-rwo --output yaml
    

In the output, you can see that `standard-rwo` is the default StorageClass and the provisioner is the vSphere CSI driver, `csi.vsphere.vmware.com`. You can also see the URL of a vSphere datastore:
    
    
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      annotations:
        storageclass.kubernetes.io/is-default-class: "true"
        ...
      labels:
        bundle.gke.io/component-name: user-vsphere-csi-driver-addon
        ...
      name: standard-rwo
    ...
    parameters:
      datastoreURL: ds:///vmfs/volumes/vsan:52fb6ca22be2454e-e67f620175964a9f/
    provisioner: csi.vsphere.vmware.com
    ...
    

**Note:** If you set [`storage.vSphereCSIDisabled`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#storagevspherecsidisabled) to `true` in the user cluster configuration file, then the cluster will not have a StorageClass named `standard-rwo`. This is OK if you provide your own CSI driver, and you don't have any PersistentVolumes that use the in-tree vSphere storage plugin.

## Kubernetes in-tree volume plugins

Kubernetes ships with a number of [in-tree volume plugin](https://kubernetes.io/docs/concepts/storage/volumes/). However, most of these in-tree volume plugins are deprecated (including the vSphere in-tree volume plugin), for more information, see the [CSI migration](https://kubernetes.io/blog/2022/09/26/storage-in-tree-to-csi-migration-status-update-1.25/) project.

## CSI Migration for the vSphere storage driver

In the past, the [in-tree vSphere volume plugin](https://kubernetes.io/docs/concepts/storage/volumes/#vspherevolume) was the provisioner for the default StorageClass in user clusters. But now the in-tree vSphere volume plugin is deprecated, and the vSphere CSI driver is the provisioner for the default StorageClass in user clusters. We recommend that you use the vSphere CSI driver instead of the in-tree volume plugin.

Starting in version 1.15 of Google Distributed Cloud, the Kubernetes CSI migration feature is enabled by default for the in-tree vSphere volume plugin. This means that if a workload uses an in-tree vSphere volume, all the internal storage operations calls are automatically redirected to the vSphere CSI driver.

For example, suppose a PersistentVolumeClaim specifies the `standard` StorageClass, which lists the vSphere in-tree volume plugin, `kubernetes.io/vsphere-volume`, as the provisioner. Then any workload that uses that PersistentVolumeClaim will have its storage operations calls redirected to the vSphere CSI driver, `csi.vsphere.vmware.com`.

### Preflight checks

When you create a new cluster or upgrade a cluster, there are preflight checks that make sure your environment is suitable for CSI migration.

For example, the preflight checks:

  * Verify that your vCenter and ESXI versions are appropriate.
  * Verify that the vSphere CSI driver is enabled if there are in-tree vSphere PersistentVolumes.
  * Verify that the vSphere StorageClasses don't have certain parameters that are ignored after CSI Migration.
  * Verify annotations on statically created in-tree PersistentVolumes and PersistentVolumeClaims required for CSI Migration.
  * Verify that the cluster can successfully run a workload using a CSI volume provisioned by the vSphere CSI driver.



For more information, see [Running preflight checks](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/preflight-checks).

### Known issues

There are several known issues related to the vSphere CSI Driver. For information and workarounds, see the Known Issues section in the [VMWare vSphere CSI Driver 3.0 release notes](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/container-storage-plugin/3-0/release-notes/vmware-vsphere-container-storage-plugin-30-release-notes.html).

### Complete migration to CSI

With the Kubernetes CSI migration feature enabled by default in 1.15, the `PersistentVolume` backed by the in-tree vSphere volume plugin continue functioning in a CSI-only environment, it just redirects in-tree plugin operation calls to the CSI plugin. Since `PersistentVolume` spec is immutable, the spec will be the same as for the in-tree volume plugin.

Due to this, the full feature set of CSI like Volume Expansion and Volume Snapshot features are not available for such volumes. To take advantage of these features, the stateful workload must be completely migrated to CSI by recreating Kubernetes resource spec with CSI fields. We have developed an [automated tooling](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/using-statefulset-csi-migration-tool) to help migrate stateful workload to CSI without application downtime that will allow you to use the full CSI featureset.

## Using third party drivers

If you want to provision storage volumes other than vSphere datastores, you can create a new StorageClass in a cluster that uses a different storage driver. Then, you can [set the StorageClass as the cluster's default](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/default-storage-class), or configure your workloads to use the StorageClass ([StatefulSet example](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/install-csi-driver#example_statefulset)).

### Storage partners

We have partnered with many storage vendors to qualify their storage systems with Google Distributed Cloud. See the full list of [qualified storage partners](https://docs.cloud.google.com/anthos/docs/resources/partner-storage).

## Volume expansion

You can expand the size of a persistent volume after it has been provisioned by editing the capacity request in the PersistentVolumeClaim. You can do an online expansion while the volume is in use by a Pod, or an offline expansion where the volume is not in use.

For the [vSphere CSI driver](https://vsphere-csi-driver.sigs.k8s.io/features/volume_expansion.html), offline expansion is available in vSphere versions >= 7.0, and online expansion is available in vSphere versions >= 7.0 Update 2.

The `standard-rwo` StorageClass sets `allowVolumeExpansion` to true by default for newly created clusters running on >= vSphere 7.0. You can use both online and offline expansion for volumes using this StorageClass. For an upgraded cluster, because StorageClasses are not modified on cluster upgrades, when a cluster is upgraded from 1.7 to 1.8, the `allowVolumeExpansion` setting in `standard-rwo` remains unset, which means volume expansion is not allowed.

For more information on volume expansion, see [Using volume expansion](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-expansion).

## CSI Volume snapshots

You can create snapshots of persistent storage by using the [VolumeSnapshot](https://kubernetes.io/docs/concepts/storage/volume-snapshots/) and [VolumeSnapshotClass](https://kubernetes.io/docs/concepts/storage/volume-snapshot-classes/) resources. To use this feature on a CSI volume, the CSI driver must support volume snapshots, and the `external-snapshotter` sidecar container must be included in the CSI driver deployment.

For more information on volume snapshots, see [Using volume snapshots](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/volume-snapshots).

The CSI snapshot controllers are deployed automatically when you create a cluster.

## Volume cleanup

When you delete a user cluster, volumes provisioned by the vSphere CSI driver are not deleted. You should delete all volumes, PersistentVolumeClaims, and StatefulSets are deleted before you delete the cluster.

## Troubleshooting

See [Troubleshooting Storage](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/storage).

## Further reading

  * [Persistent volumes in Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes)

  * [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)

  * [Storage Classes](https://kubernetes.io/docs/concepts/storage/storage-classes/)

  * [Container Storage Interface in Kubernetes](https://kubernetes.io/blog/2019/01/15/container-storage-interface-ga/)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
