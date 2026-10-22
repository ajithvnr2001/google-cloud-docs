---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/handle-filestore-volumes/
title: Handle Filestore volumes with Backup for GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:38.668404+00:00
---

# Handle Filestore volumes with Backup for GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/handle-filestore-volumes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke)



Send feedback 

#  Handle Filestore volumes with Backup for GKE Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot  Standard 

This page describes how to handle Filestore volumes with Backup for GKE.

Backup for GKE doesn't integrate with Filestore volumes. This means that backing up and restoring data directly from these volumes is not supported. However, Backup for GKE can be used to provide solutions for workloads that are backed by Filestore volumes in certain disaster recovery scenarios.

With these solutions, you can back up Filestore volume configurations by enabling permissive mode. For restoration, you can use the reconnect Filestore volumes or restore Filestore volumes data out-of-band solutions.

**Note:** The solution applies only to Filestore volumes provisioned through the GKE Filestore CSI driver. It may not work for other types of NFS volumes.

## Back up Filestore volume configurations

By default, backing up clusters that contain Filestore volumes fail if permissive mode is not enabled. When permissive mode is enabled, Backup for GKE captures the configuration of workloads and volumes. For more information about permissive mode, see [Enable permissive mode on a backup plan](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/permissive-mode).

## Reconnect Filestore volumes

Backup for GKE allows restore plans to specify the volume data restore policy to **Reuse existing volumes containing your data**. In this case, it creates `PersistentVolumeClaim` and `PersistentVolume` resources directly and references existing Filestore volumes without provisioning new ones.

If the backup contains Compute Engine Persistent Disk volumes and you want to restore data for those volumes, see [Define volume data restore behavior](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/volume-data-restore-policy) for how to configure volume data restore policy bindings.

**Note:** To reconnect Filestore volumes during a restore, ensure that volumes are available and accessible in the target cluster.

## Back up and restore Filestore volumes out-of-band

You can use the Filestore backup capability to create separate backups of your Filestore volumes. These backups are independent of Backup for GKE, ensuring you have a complete copy of the data.

### Back up Filestore volumes out-of-band

Filestore provides [backups](https://docs.cloud.google.com/filestore/docs/backup-restore#back-up-file-share) that create a copy of a file share, including all file data and metadata from the point in time the backup is created. You can create separate backups for Filestore volumes in addition to Backup for GKE backups containing Filestore volume configuration. For instructions, see [create a backup](https://docs.cloud.google.com/filestore/docs/backup-restore#create-backup) from the Filestore.

### Restore Filestore volumes out-of-band

With both Filestore backups and Backup for GKE backups, you can restore workloads using the following steps:

  1. [Restore](https://docs.cloud.google.com/filestore/docs/backup-restore#restore) Filestore volumes out-of-band using the Filestore backup.
  2. Create [static](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#static) `PersistentVolumes` that reference the restored Filestore volumes in the target cluster. Restoring a Filestore backup out-of-band provisions a new instance with a new IP address.

To retrieve the IP address of the newly restored Filestore instance, run the following:
         
         gcloud filestore instances describe NEW_INSTANCE_NAME \
              --location=LOCATION \
              --format="value(networks.ipAddresses[0])"
         

You must explicitly set this new IP address in the `csi.volumeAttributes.ip` field. You must also pre-bind the volume. To do so, in the `.spec.claimRef` block, define the `namespace` and `name` fields based on the `PersistentVolumeClaim` that you'll create. For example, see the following:
         
         apiVersion: v1
          kind: PersistentVolume
          metadata:
            name: RESTORED_PV_NAME
          spec:
            capacity:
              storage: VOLUME_CAPACITY
            accessModes:
              - ReadWriteMany
            persistentVolumeReclaimPolicy: Retain
            csi:
              driver: filestore.csi.storage.gke.io
              volumeHandle: NEW_VOLUME_HANDLE
              volumeAttributes:
                ip: NEW_FILESTORE_IP_ADDRESS  # Crucial: Use the newly provisioned IP
                share: FILESTORE_SHARE_NAME
            claimRef:
              namespace: RESTORED_PVC_NAMESPACE  # Required: Exact namespace of the backed-up PVC
              name: RESTORED_PVC_NAME  # Required: Exact name of the backed-up PVC
         

  3. From Backup for GKE, initiate a restore using the volume data restore policy **Don't restore volume data**. The newly created PVCs bind to the `PersistentVolumes` created in the earlier step.

If the backup contains Compute Engine Persistent Disk volumes and you want to restore data for those volumes, see [Define volume data restore behavior](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/volume-data-restore-policy) for how to configure volume data restore policy bindings.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
