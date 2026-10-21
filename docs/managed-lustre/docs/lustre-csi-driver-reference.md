---
url: https://docs.cloud.google.com/managed-lustre/docs/lustre-csi-driver-reference/
title: Managed Lustre CSI driver reference \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:11:24.430827+00:00
---

# Managed Lustre CSI driver reference  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-lustre/docs/lustre-csi-driver-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Managed Lustre ](https://docs.cloud.google.com/managed-lustre/docs/overview)



Send feedback 

#  Managed Lustre CSI driver reference Stay organized with collections  Save and categorize content based on your preferences. 

The following manifests describe supported CSI driver fields in the Storage Class and Persistent Volume resources.

## Storage Class

The following manifest includes all of the supported fields in the Storage Class.
    
    
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: lustre-csi-example-storage-class
    provisioner: lustre.csi.storage.gke.io
    parameters:
      network: VPC_NETWORK # optional
      filesystem: LUSTRE_FILESYSTEM_NAME # optional
      labels: KEY_1=VALUE_1,KEY_2=VALUE_2,...,KEY_N=VALUE_N # optional
      description: DESCRIPTION # optional
      perUnitStorageThroughput: 125 | 250 | 500 | 1000  # required
    volumeBindingMode: WaitForFirstConsumer | Immediate # default is Immediate
    allowedTopologies:
    - matchLabelExpressions:
      - key: topology.gke.io/zone
        values:
        - ZONE_1
        - ZONE_2
    mountOptions:
      - LUSTRE_MOUNT_OPTIONS
    

Replace the following values:

  * `network`: optional. The Virtual Private Cloud (VPC) network in which to create the Managed Lustre instance. If this property is not specified, the default network is used.

To create a Managed Lustre instance in a shared VPC network, the full name of the network must be provided. For example, `projects/PROJECT_ID/global/networks/VPC_NETWORK_NAME`.

  * `filesystem`: specifies the `fsname` for the Managed Lustre instance. This parameter is used for [dynamic provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/lustre-csi-driver-new-volume#new-volume). The `fsname` must be an alphanumeric string of up to eight characters, beginning with an alphabetic character. If you don't provide a value, the CSI driver generates an `fsname` with the format `"lfsNNNNN"` (for example, `"lfs97603"`).

**Note:** If you plan to mount multiple Managed Lustre instances on the same node, you'll need a separate StorageClass for each instance. Each of these StorageClasses must specify a unique `fsname` value to avoid conflicts when mounting on the same node.
  * `labels`: optional. Managed Lustre supports labels per instance, as a map of key-value pairs. The Managed Lustre CSI driver lets you attach user-provided labels to the instance.

  * `description`: optional. A description of the instance. Must be 2,048 characters or fewer.

  * `perUnitStorageThroughput`: specifies the per-unit storage throughput (MB/s/TiB) for the instance. Supported values are `125`, `250`, `500`, and `1000`. The default is `1000`.

  * `allowTopologies`: optional. Managed Lustre instances are zonal resources. If this property is not specified, the Managed Lustre instance is created in the same zone as the CSI controller Driver Pod, and the volume binding mode defaults to `Immediate`.

If `WaitForFirstConsumer` is specified, the topology is set to where the Pod is scheduled. However, this setting can cause Pods to be blocked while they wait for a volume to be provisioned.

The Managed Lustre CSI driver supports the [topology feature](https://kubernetes-csi.github.io/docs/topology.html#csi-topology-feature) to ensure that persistent volumes and Pods are placed in the allowed topologies, based on the topology provided in the StorageClass.

  * `mountOptions`: optional. Specifies [`mount.lustre`](https://doc.lustre.org/lustre_manual.xhtml#mount.lustre) mount options. Managed Lustre volumes inherit these mount options from the StorageClass in the `pv.spec.mountOptions` field.




## Persistent Volume

The following manifest includes all of the supported fields in the Persistent Volume.
    
    
    apiVersion: v1
    kind: PersistentVolume
    metadata:
     name: preprov-pv
     annotations:
       pv.kubernetes.io/provisioned-by: lustre.csi.storage.gke.io
    spec:
     mountOptions:
       - LUSTRE_MOUNT_OPTIONS
       ...
     storageClassName: ""
     capacity:
       storage: CAPACITY
     accessModes:
       - ReadWriteMany
     persistentVolumeReclaimPolicy: Retain
     volumeMode: Filesystem
     csi:
       driver: lustre.csi.storage.gke.io
       volumeHandle: EXISTING_LUSTRE_INSTANCE_NAME
       volumeAttributes:
         ip: EXISTING_LUSTRE_IP_ADDRESS
         filesystem: EXISTING_LUSTRE_FSNAME
    

Replace the following values:

  * `capacity.storage`: the capacity of the Managed Lustre instance. Refer to [Performance tiers](https://docs.cloud.google.com/managed-lustre/docs/performance#performance_tiers) for the supported minimum and maximum instance capacities.
  * `mountOptions`: Specifies [`mount.lustre`](https://doc.lustre.org/lustre_manual.xhtml#mount.lustre) mount options. This value is inherited from the `mountOptions` field in the StorageClass.
  * `csi.volumeHandle`: an exclusive identifier for a Managed Lustre instance. Must use the following format: PROJECT_ID/LOCATION/INSTANCE_NAME.
  * `csi.volumeAttributes.ip`: the IP address of the Managed Lustre instance, used for mounting.
  * `csi.volumeAttributes.filesystem`: the file system name of the Managed Lustre instance, which is an eight-character identifier.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
