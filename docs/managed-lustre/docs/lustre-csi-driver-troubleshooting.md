---
url: https://docs.cloud.google.com/managed-lustre/docs/lustre-csi-driver-troubleshooting/
title: Troubleshoot Managed Lustre volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:39:57.547699+00:00
---

# Troubleshoot Managed Lustre volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-lustre/docs/lustre-csi-driver-troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Managed Lustre ](https://docs.cloud.google.com/managed-lustre/docs/overview)



Send feedback 

#  Troubleshoot Managed Lustre volumes Stay organized with collections  Save and categorize content based on your preferences. 

This page includes troubleshooting steps for common issues and errors when using the Google Cloud Managed Lustre CSI driver on Google Kubernetes Engine.

Before following the troubleshooting steps in this section, refer to the [limitations when connecting to Managed Lustre from GKE](https://docs.cloud.google.com/managed-lustre/docs/connect-from-kubernetes-engine-existing-instance#limitations).

## Updated minimum instance capacity

The minimum capacity for Managed Lustre instances has been updated to 9000 GiB. To create 9000 GiB instances using the Managed Lustre CSI driver, upgrade your cluster version to `1.34.0-gke.2285000` or later.

## Incorrect performance tier for dynamically provisioned Lustre instances

When dynamically provisioning a Lustre instance, the instance creation fails with an `InvalidArgument` error for PerUnitStorageThroughput, regardless of the perUnitStorageThroughput value specified in the API request. This affects GKE 1.33 versions before 1.33.4-gke.1036000.

**Workaround:**

Upgrade the GKE cluster to version 1.33.4-gke.1036000 or later. If using the Stable channel, a newer version might not be available yet. In this case, you can manually select a version from the Regular or Rapid channels that includes the fix.

## Managed Lustre communication ports

The Managed Lustre CSI driver uses different ports for communication with Managed Lustre instances, depending on your GKE cluster version and existing Managed Lustre configurations.

  * **Default port (`988`):** For new GKE clusters that run version `1.33.2-gke.4780000` or later, the driver uses port `988` for Lustre communication by default.

  * **Legacy port (`6988`):** The driver uses port `6988` in the following scenarios:

    * **Earlier GKE versions:** If your GKE cluster runs a version earlier than `1.33.2-gke.4780000`, the `--enable-legacy-lustre-port` flag is required when enabling the CSI driver. Enabling this flag works around a port conflict with the `gke-metadata-server` on GKE nodes.
    * **Existing Managed Lustre instances with GKE support:** If you are connecting to an existing Managed Lustre instance that was created with the `--gke-support-enabled` flag, you must include `--enable-legacy-lustre-port` when enabling the CSI driver, irrespective of your cluster version. Without this flag, your GKE cluster will fail to mount the existing Lustre instance.

For more information on enabling the CSI driver with the legacy port, see [Lustre communication ports](https://docs.cloud.google.com/managed-lustre/docs/lustre-csi-driver-new-volume#lustre_communication_ports).




## Log queries

To check logs, run the following query in [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

To return Managed Lustre CSI driver node server logs:
    
    
    resource.type="k8s_container"
    resource.labels.pod_name=~"lustre-csi-node*"
    

## Troubleshoot volume provisioning

If the PersistentVolumeClaim (PVC) remains in a `Pending` state and no PersistentVolume (PV) is created after 20-30 minutes, an error might have occurred.

  1. Check the PVC events:
         
         kubectl describe pvc PVC_NAME
         

  2. If the error indicates configuration issues or invalid arguments, verify your [StorageClass parameters](https://docs.cloud.google.com/managed-lustre/docs/lustre-csi-driver-new-volume#create_a_storageclass).

  3. Recreate the PVC.

  4. If the issue persists, contact [Cloud Customer Care](https://cloud.google.com/support).




## Troubleshoot volume mounting

After the Pod is scheduled to a node, the volume is mounted. If this fails, check the Pod events and kubelet logs.
    
    
    kubectl describe pod POD_NAME
    

### CSI driver enablement issues

**Symptom:**
    
    
    MountVolume.MountDevice failed for volume "yyy" : kubernetes.io/csi: attacher.MountDevice failed to create newCsiDriverClient: driver name lustre.csi.storage.gke.io not found in the list of registered CSI drivers
    

or
    
    
    MountVolume.SetUp failed for volume "yyy" : kubernetes.io/csi: mounter.SetUpAt failed to get CSI client: driver name lustre.csi.storage.gke.io not found in the list of registered CSI drivers
    

**Cause:** The CSI driver is not enabled or not yet running.

**Resolution:**

  1. Verify the CSI driver is [enabled](https://docs.cloud.google.com/managed-lustre/docs/lustre-csi-driver-existing-instance#enable_the_csi_driver).
  2. If the cluster was recently scaled or upgraded, wait a few minutes for the driver to become functional.
  3. If the error persists, check the `lustre-csi-node` logs for "Operation not permitted". This indicates that the node version is too old to support Managed Lustre. To resolve this, upgrade your node pool to version `1.33.2-gke.1111000` or later.
  4. If the logs show "LNET_PORT mismatch", upgrade your node pool to ensure compatible Lustre kernel modules are installed.



### Mountpoint already exists

**Symptom:**
    
    
    MountVolume.MountDevice failed for volume "yyy" : rpc error: code = AlreadyExists
    desc = A mountpoint with the same lustre filesystem name "yyy" already exists on
    node "yyy". Please mount different lustre filesystems
    

**Cause:** Mounting multiple volumes from different Managed Lustre instances with the same file system name on a single node is not supported.

**Resolution:** Use a unique file system name for each Managed Lustre instance.

### Mount failed: No such file or directory

**Symptom:**
    
    
    MountVolume.MountDevice failed for volume "yyy" : rpc error: code = Internal desc = Could not mount ... failed: No such file or directory
    

**Cause:** The file system name specified is incorrect or does not exist.

**Resolution:** Verify the `fs_name` in your StorageClass or PV configuration matches the Managed Lustre instance.

### Mount failed: Input/output error

**Symptom:**
    
    
    MountVolume.MountDevice failed for volume "yyy" : rpc error: code = Internal desc = Could not mount ... failed: Input/output error
    

**Cause:** The cluster cannot connect to the Managed Lustre instance.

**Resolution:**

  1. Verify the IP address of the Managed Lustre instance.
  2. Ensure the GKE cluster and Managed Lustre instance are in the same VPC network or are correctly peered.



### Internal errors

**Symptom:** `rpc error: code = Internal desc = ...`

**Resolution:** If the error persists, contact [Cloud Customer Care](https://cloud.google.com/support).

## Troubleshoot volume unmounting

**Symptom:**
    
    
    UnmountVolume.TearDown failed for volume "yyy" : rpc error: code = Internal desc = ...
    

**Resolution:**

  1. Force delete the Pod:
         
         kubectl delete pod POD_NAME --force
         

  2. If the issue persists, contact [Cloud Customer Care](https://cloud.google.com/support).




## Troubleshoot volume deletion

If the PV remains in a "Released" state for an extended period (for example, more than an hour) after deleting the PVC, contact [Cloud Customer Care](https://cloud.google.com/support).

## Troubleshoot volume expansion

### PVC stuck in ExternalExpanding

**Symptom:** The PVC status does not change to `Resizing`, and events show `ExternalExpanding`.

**Cause:** The `allowVolumeExpansion` field might be missing or set to `false`.

**Resolution:** Ensure the `StorageClass` has `allowVolumeExpansion: true`.
    
    
    kubectl get storageclass STORAGE_CLASS_NAME -o yaml
    

### Expansion fails: Invalid argument

**Symptom:** `VolumeResizeFailed: rpc error: code = InvalidArgument ...`

**Cause:** The requested size is invalid (for example, not a multiple of the step size or outside limits).

**Resolution:** Check the [valid capacity ranges](https://docs.cloud.google.com/managed-lustre/docs/create-instance#capacity) and update the PVC with a valid size.

### Expansion fails: Internal error

**Symptom:** `VolumeResizeFailed ... rpc error: code = Internal`

**Resolution:** Retry the expansion by reapplying the PVC. If it fails repeatedly, contact [Cloud Customer Care](https://cloud.google.com/support).

### Deadline exceeded

**Symptom:** `VolumeResizeFailed` with `DEADLINE_EXCEEDED`.

**Cause:** The operation is taking longer than expected but may still be in progress.

**Resolution:** Wait for the operation to complete. The resizer will retry automatically. If it remains stuck for a long time (for example, > 90 minutes), contact support.

### Quota exceeded

**Symptom:** Expansion fails due to quota limits.

**Resolution:** Request a [quota increase](https://docs.cloud.google.com/managed-lustre/docs/quotas#requesting_additional_quota) or request a smaller capacity increase.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
