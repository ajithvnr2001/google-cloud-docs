---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/storage-errors/
title: Troubleshoot storage errors in Backup for GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:42.019650+00:00
---

# Troubleshoot storage errors in Backup for GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/storage-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke)



Send feedback 

#  Troubleshoot storage errors in Backup for GKE Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot  Standard 

This page describes storage-related errors you might experience when using Backup for GKE, things to consider when performing the action, and steps on how to troubleshoot the issue.

## Error 100010105: Failed to backup PersistentVolumeClaim - Disk referenced by PersistentVolume does not exist

Error `100010105` occurs when an attempt to back up a `PersistentVolumeClaim` fails because it references a disk that doesn't exist, resulting in an error message stating `Failed to backup PersistentVolumeClaim - Disk referenced by PersistentVolume does not exist`.

In Google Kubernetes Engine, `PersistentVolumeClaims` request storage from `PersistentVolumes`. A `PersistentVolume`, in turn, represents a piece of storage, often an underlying Compute Engine Persistent Disk. An error can occur when a `PersistentVolumeClaim` is bound to a `PersistentVolume` and the `PersistentVolume`'s configuration specifies a Compute Engine Persistent Disk. However, the actual disk with the name and location specified in the `PersistentVolume` configuration cannot be found in your Google Cloud project. Thus, Backup for GKE cannot proceed with backing up a non-existent disk, and a failure occurs.

To resolve this error, use the following instructions:

  1. Identify the problematic `PersistentVolumeClaim` and `PersistentVolume`. The names of both the problematic `PersistentVolumeClaim` and its associated `PersistentVolume` are listed in the `state reason` field of your failed Backup for GKE operation. We recommend documenting both the `PersistentVolumeClaim` name, its namespace, and the name of the `PersistentVolume`.

  2. Inspect the `PersistentVolume`. To describe the `PersistentVolume`, use the `PersistentVolume` name you identified from the state reason field in the following command:
         
         kubectl describe pv PERSISTENTVOLUME_NAME
         

Replace `PERSISTENTVOLUME_NAME` with the name of your PersistentVolume.

  3. In the output, examine the `source` section, specifically under `csi`. This section describes the `VolumeHandle` that the `PersistentVolume` is trying to reference. For example:
         
         Source:
           Type: GCEPersistentDisk (a Persistent Disk resource in Google Compute Engine)
         PDName: my-non-existent-disk
         FSType: ext4
         Partition: 0
         ReadOnly: false
                     In this example, the PD name is my-non-existent-disk.
         
             Source:
           Type:       CSI (a Container Storage Interface (CSI) volume)
           Driver:     pd.csi.storage.gke.io
           VolumeHandle: projects/PROJECT_ID/zones/ZONE/disks/DISK_NAME
         ...
         

In this example, the `VolumeHandle` contains the full path to the disk, including its name and location. For example, `projects/my-gcp-project/zones/us-central1-a/disks/my-disk-name`.

  4. Use the `VolumeHandle` obtained from the `PersistentVolume` description to identify the disk name and zone.

  5. Verify that the disk exists in your Google Cloud project by using one of the following methods:

### Zonal disk

If you're using a zonal disk, use Google Cloud CLI to run the `gcloud compute disks describe` command:
         
         gcloud compute disks describe DISK_NAME \
             --zone=ZONE_NAME \
             --project=PROJECT_ID
         

Replace the following:

     * `DISK_NAME`: the name of the disk you obtained from the `PersistentVolume` description.

     * `ZONE_NAME`: the zone of the disk you obtained from the `PersistentVolume` description.

     * `PROJECT_ID`: your Google Cloud project ID.

### Regional disk

If you're using a regional disk, use Google Cloud CLI to run the `gcloud compute disks describe` command:
    
    gcloud compute disks describe DISK_NAME \
        --region=REGION_NAME \
        --project=PROJECT_ID
    

Replace the following:

     * `DISK_NAME`: the name of the disk you obtained from the `PersistentVolume` description.

     * `REGION_NAME`: the region of the disk you obtained from the `PersistentVolume` description.

     * `PROJECT_ID`: your Google Cloud project ID.

If you get a `Resource not found` or `The resource DISK_NAME was not found` error message, the disk doesn't exist. Use one of the following methods to resolve the issue depending on the scenario that best fits your needs:

     * If the disk was accidentally deleted or misnamed and you want to keep the data or `PersistentVolumeClaim`, or the `PersistentVolume` was configured with an incorrect disk name, use one of the following methods to resolve the issue:

       * **Restore the disk** : if you have a backup of the disk, restore it with the exact same name and location that the `PersistentVolume` references.

       * **Create a new disk** : if restoring the disk isn't an option, create a new disk with the same name and location that's in the `PersistentVolume` configuration.

     * If the `PersistentVolumeClaim` or `PersistentVolume`, their data, or the application are no longer needed, we recommend removing the unneeded entity:

       * **Delete the`PersistentVolumeClaim`**: delete the `PersistentVolumeClaim` by using the `kubectl` command-line tool to run the `kubectl delete pvc` command:
    
    kubectl delete pvc PVC_NAME -n NAMESPACE
    

Replace the following:

       * `PVC_NAME`: the name of the `PersistentVolumeClaim` you want to delete.

       * `NAMESPACE`: the namespace of the `PersistentVolumeClaim` you want to delete.

     * **The`PersistentVolume` is still present after you delete the `PersistentVolumeClaim`**: if the `PersistentVolume`'s `PersistentVolumeReclaimPolicy` is set to `Delete`, the `PersistentVolume` is automatically deleted when the `PersistentVolumeClaim` is deleted. If the `persistentVolumeReclaimPolicy` is set to `Retain`, you need to manually delete the `PersistentVolume` after the `PersistentVolumeClaim` is deleted. To delete the `PersistentVolume`, use the `kubectl` command-line tool to run the `kubectl delete pv` command:
           
           kubectl delete pv PV_NAME
           

Replace `PV_NAME` with the name of the `PersistentVolume` you want to delete.


**Important:** If the `reclaimPolicy` is set to `Retain` and the underlying disk exists, deleting the `PersistentVolume` doesn't delete the disk. You must manually delete the disk from Google Cloud if it's truly no longer needed.

If the operation continues to fail, contact Cloud Customer Care for further assistance.

## Error 100010202: Snapshotting volume failed

Error `100010202` occurs when Compute Engine Persistent Disk snapshot creation fails, resulting in an error message stating `Snapshotting volume failed`.

A Compute Engine Persistent Disk snapshot operation fails if the disk's attachment state to a virtual machine (VM) instance changes during the snapshot creation process initiated by the Backup for GKE service. Common scenarios that trigger this include the following:

  * **Node auto-repair** : unhealthy nodes are recreated, which causes Pods to be rescheduled and disks to detach and reattach.
  * **Node upgrades** : during node pool upgrades, nodes are typically drained and replaced. Pods are gracefully terminated and rescheduled on the new nodes, triggering disk detach and reattach cycles.
  * **Cluster autoscaling** : during scale-down events, if the cluster autoscaler removes a node, any Pods on that node with Persistent Disks are evicted, causing disk detachments. If these Pods are rescheduled elsewhere, attachments will occur on the new nodes. During scale-up events, new nodes don't directly cause reattachments, but Pods scheduled on them will trigger initial attachments.



This is a transient error. The backup typically succeeds on the next automated run once the disk attachment stabilizes. To prevent cluster events from impacting your backups, apply the following recommendations:

  1. **Enable Smart scheduling** : Configure your backup plan using [Smart scheduling](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup-schedule#smart-scheduling) (an RPO-based schedule). This allows the system to automatically retry transient failures within your specified time window without impacting the backup plan's overall RPO.

  2. **Set up backup exclusion windows** : If you are performing node pool upgrades or cluster resizing operations, add a [backup exclusion window](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup-schedule#backup_exclusion_window) to your backup settings during those intervals. This ensures that Backup for GKE service will pause and avoid scheduling snapshots while your cluster is actively modifying disk attachments.

  3. **Retry Manual Backups** : In the case of manual or on-demand backups, retry the backup operation once the cluster event finishes.




If the operation continues to fail, contact Cloud Customer Care for further assistance.

## What's next

  * [Read the Backup for GKE error codes overview page](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/backup-error-codes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
