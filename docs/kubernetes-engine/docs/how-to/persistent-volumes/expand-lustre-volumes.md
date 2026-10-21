---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/expand-lustre-volumes/
title: Scale your Managed Lustre storage on GKE \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:02:05.620234+00:00
---

# Scale your Managed Lustre storage on GKE  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/expand-lustre-volumes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Scale your Managed Lustre storage on GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document describes how to dynamically increase the storage capacity of Managed Lustre volumes for your stateful workloads in Google Kubernetes Engine (GKE) without disrupting your applications.

For example, if your long-running AI/ML training jobs have dynamic and unpredictable storage requirements, enable Managed Lustre volume expansion to increase the storage capacity of your existing Managed Lustre PersistentVolume (PV).

This document is for Platform admins and operators, DevOps, Storage administrators, and Machine learning (ML) engineers who manage storage for stateful workloads on GKE.

When you expand a volume, your costs increase based on the new, larger capacity, according to the standard [Google Cloud Managed Lustre pricing](https://cloud.google.com/products/managed-lustre/pricing).

## Before you begin

[Prepare your environment](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/lustre-csi-driver-new-volume#before_you_begin).

### Requirements

Make sure that you meet the following requirements:

  * You must have a GKE cluster version 1.35.0-gke.2331000 or later.
  * You must enable the Managed Lustre CSI driver on an existing cluster. The driver is disabled by default in Standard and Autopilot clusters.



### Limitations

  * You can only increase the size of an existing volume, and you can't decrease its size.
  * You can't use volume expansion with the `ReadOnlyMany` access mode.
  * When you resize Lustre volumes, follow the minimum and maximum capacity limits and step sizes set by your volume's performance tier. For more information, see [Performance considerations](https://docs.cloud.google.com/managed-lustre/docs/performance).
  * Specify Lustre volume sizes in GiB as multiples of 1000. Kubernetes translates units such as Ti into binary values (for example, 18 Ti is interpreted as 18,432 GiB), which results in the Lustre API rejecting the request.



## Enable volume expansion for a StorageClass

  1. Verify whether your StorageClass supports volume expansion:
         
         kubectl get sc STORAGECLASS_NAME -o jsonpath='{.allowVolumeExpansion}{"\n"}'
         

Replace `STORAGECLASS_NAME` with the name of your StorageClass.

If the command outputs nothing or returns `false`, you must explicitly update the StorageClass configuration to allow expansion.

  2. Open the StorageClass configuration for editing:
         
         kubectl edit storageclass STORAGECLASS_NAME
         

  3. In the editor, add the `allowVolumeExpansion: true` field to your StorageClass configuration:
         
         apiVersion: storage.k8s.io/v1
         kind: StorageClass
         metadata:
           name: lustre-sc
         provisioner: lustre.csi.storage.gke.io
         ...
         **allowVolumeExpansion : true**




## Expand a PersistentVolumeClaim

To initiate volume expansion, edit your PersistentVolumeClaim (PVC) to request an increase in volume size.

**Important:** When you expand a volume, always update the PVC. Don't update the PV directly.

  1. Identify the new, valid size for expansion as described in Determine valid expansion sizes.
  2. Open the PVC configuration for editing:
         
         kubectl edit pvc PVC_NAME
         

Replace `PVC_NAME` with the name of your PVC.

  3. In the editor, update the `spec.resources.requests.storage` field with the valid expansion size. For example, to expand a volume from `9000Gi` to `18000Gi`, modify the `storage` field as follows:
         
         spec:
           accessModes:
           - ReadWriteOnce
           resources:
             requests:
               **storage : 18000Gi** # Changed from 9000Gi
         




## Verify the volume expansion

  1. Monitor the expansion progress by reviewing the PVC's events:
         
         kubectl describe pvc PVC_NAME
         

The following events in the PVC's output indicate the current progress or outcome of the volume expansion request:

     * `ExternalExpanding`: indicates that Kubernetes is waiting for the `external-resizer` to expand the PVC.
     * `Resizing`: indicates that the resize operation is in progress. This operation can take up to 90 minutes for larger capacity increases.
     * `VolumeResizeSuccessful`: confirms that the volume has been successfully expanded.
     * `VolumeResizeFailed`: indicates that an error occurred. The event message contains details from the Google Cloud Managed Lustre API. This state might be transient and might resolve on its own.
  2. After the expansion is complete, verify the PVC's updated configuration:
         
         kubectl get pvc PVC_NAME -o yaml
         

  3. Ensure the `status.capacity` field reflects the new, incremented size.




If you encounter any issues during the expansion process, see Troubleshooting.

## Determine valid expansion sizes

To determine your new volume size, first identify your volume's performance tier and its corresponding step size.

### Identify the volume's performance tier

You can find your volume's performance tier using either of the following options:

### StorageClass

Run the following command and look for the `perUnitStorageThroughput` value (for example, `1000`). This value indicates the performance tier in MBps per TiB.
    
    
    kubectl get sc STORAGECLASS_NAME -o yaml
    

Replace `STORAGECLASS_NAME` with the name of your StorageClass.

### Lustre instance

Identify your volume's performance tier by checking the underlying Managed Lustre instance's properties directly:

  1. Find the name of the PV bound to your PVC:
         
         kubectl get pvc PVC_NAME
         

Replace `PVC_NAME` with the name of your PVC.

The output is similar to the following. Note the **PV** name in the `VOLUME` column, for example, `pv-lustre`.
         
         NAME         STATUS   VOLUME      CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
         pvc-lustre   Bound    pv-lustre   9000Gi     RWX            lustre-rwx     <unset>                 26m
         

  2. Find the volume's location and instance name in the `volumeHandle` field:
         
         kubectl get pv PV_NAME -o yaml
         

Replace `PV_NAME` with the PV name from the previous step.

The `volumeHandle` value is formatted as `PROJECT_ID/LOCATION/INSTANCE_NAME`. Note the `INSTANCE_NAME` and `LOCATION` for the next step.

  3. Check the performance tier properties by describing the Managed Lustre instance:
         
         gcloud lustre instances describe INSTANCE_NAME --location=LOCATION
         

Replace `INSTANCE_NAME` and `LOCATION` with the values from the previous step.

In the output, look for the **`perUnitStorageThroughput`** field. This value indicates the performance tier in MBps per TiB.




### Capacity limits and step sizes

After you identify the performance tier, refer to the following table to find the associated capacity limits and required step size.

Tier (`perUnitStorageThroughput`) | Min capacity | Max capacity | Step size  
---|---|---|---  
1,000 MBps per TiB | 9,000 GiB | 954,000 GiB (~1 PiB) | 9,000 GiB  
500 MBps per TiB | 18,000 GiB | 1,908,000 GiB (~2 PiB) | 18,000 GiB  
250 MBps per TiB | 36,000 GiB | 3,816,000 GiB (~4 PiB) | 36,000 GiB  
125 MBps per TiB | 72,000 GiB | 7,632,000 GiB (~8 PiB) | 72,000 GiB  
  
Volumes must be increased according to the step size assigned to their tier. Any increase in capacity must be a multiple of that specific step size. For example, if your 1,000 MBps tier volume has a capacity of 9,000 GiB, you can increase it to 18,000 GiB, 27,000 GiB, and other multiples.

## Troubleshooting

This section provides solutions for common issues you might encounter with when you expand Lustre volumes.

### Expansion fails with an "Invalid Argument" error

**Symptom**

  * The PVC enters a `Resizing` state but then fails.
  * When you run the `kubectl describe pvc PVC_NAME` command, you see an error similar to `VolumeResizeFailed: rpc error: code = InvalidArgument desc = ...`.



**Cause**

This error typically means that the requested storage size is not valid for the Lustre volume's performance tier for one of the following reasons:

  * The requested size is not a multiple of the required step size for the tier.
  * The requested size is below the minimum or above the maximum capacity for the tier.



**Resolution**

  1. Review Capacity limits and step sizes to find the valid step sizes and capacity limits for your volume's performance tier.
  2. Edit the PVC again to request a valid storage size that meets the step size and capacity limits.



### Expansion fails with an "Internal Error"

**Symptom**

  * The PVC resize fails.
  * When you run the `kubectl describe pvc PVC_NAME` command, you might see a `VolumeResizeFailed` event with an error message containing `code = Internal`.



**Cause**

This error indicates a problem with the underlying Managed Lustre service.

**Resolution**

  1. Retry the expansion by applying the PVC manifest again with the new, requested size. This might resolve transient backend issues.
  2. If retrying fails, [contact Cloud Customer Care](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support).



### Expansion is stuck in "Resizing" state

**Symptom**

  * The PVC remains in the `Resizing` state for an extended period (more than 30 minutes for smaller expansions, or more than 90 minutes for larger expansions).
  * You might see a `VolumeResizeFailed` event with a `DEADLINE_EXCEEDED` error message.



**Cause**

This issue can happen with large capacity increases, which can take up to 90 minutes to complete. The `csi-external-resizer` component might time out while waiting for the Google Cloud Managed Lustre API to respond, even though the underlying expansion operation is still in progress.

**Resolution**

  * The `csi-external-resizer` automatically retries the operation after a backoff period. Continue to monitor the PVC events for a `VolumeResizeSuccessful` event.
  * If the PVC remains in the `Resizing` state for more than 90 minutes, contact Cloud Customer Care.



### Expansion does not start, or is stuck in an ExternalExpanding state

**Symptom**

  * You update the `spec.resources.requests.storage` field in your PVC, but the PVC status does not change to `Resizing`.
  * When you run the `kubectl describe pvc PVC_NAME` command, the event log only shows the `ExternalExpanding` state and does not progress to the `Resizing` state:


    
    
    Events:
      Type    Reason             Age                From             Message
      ----    ------             ----               ----             -------
      Normal  ExternalExpanding  21m (x2 over 58m)  volume_expand    waiting for an external controller to expand this PVC
    

**Cause**

This behavior typically indicates one of the following issues:

  * The StorageClass associated with the PVC does not permit volume expansion.
  * There is a problem with the `csi-external-resizer` sidecar container, which is the component responsible for initiating the expansion.



**Resolution**

  1. Check the StorageClass configuration and verify that the `allowVolumeExpansion: true` field is set:
         
         kubectl get sc STORAGECLASS_NAME -o jsonpath='{.allowVolumeExpansion}{"\n"}'
         

  2. If `allowVolumeExpansion` is missing or set to `false`, update the StorageClass to allow volume expansion.

  3. If the StorageClass is configured correctly, the issue is likely with the GKE control plane components that manage the resize operation. Contact Cloud Customer Care for assistance.




### Expansion fails due to a quota or capacity issue

**Symptom**

  * The PVC resize fails, and a `VolumeResizeFailed` event appears on the PVC.
  * When you run the `kubectl describe pvc PVC_NAME` command, the event message from the Managed Lustre backend indicates a quota or capacity issue.



**Cause**

The requested valid expansion can't be fulfilled because it exceeds the overall capacity or quota available for the Managed Lustre service in your project or region.

**Resolution**

  * Edit your PVC again and request a smaller storage increase.
  * Contact your organization's Google Cloud administrator to request an increase to the overall Lustre service quotas or capacity for your project.



## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this document, delete the PVC. This operation also deletes the associated PV and the underlying Managed Lustre instance if the `reclaimPolicy` is set to `Delete`.
    
    
    kubectl delete pvc PVC_NAME
    

Replace `PVC_NAME` with the name of your PVC.

## What's next

  * Learn more about [Storage for GKE clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/storage-overview).
  * Read the documentation about [GKE persistent volumes and provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
