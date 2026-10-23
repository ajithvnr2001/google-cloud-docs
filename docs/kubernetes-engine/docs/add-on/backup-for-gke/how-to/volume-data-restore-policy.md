---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/volume-data-restore-policy/
title: Define volume data restore behavior \u00a0|\u00a0 Backup for GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:36.678083+00:00
---

# Define volume data restore behavior  |  Backup for GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/volume-data-restore-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke)



Send feedback 

#  Define volume data restore behavior Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot  Standard 

This page provides an overview of volume data restore policies. It also explains how to configure volume data restore policy bindings and overrides.

## Overview

The volume data restore policy defines how to restore volume data from a backup. You can configure it at the restore plan level. It has the following policy options:

  * **Provision new volumes and restore volume data from backup** : New persistent volumes (PVs) are restored using the corresponding volume backup data in the backup.
  * **Reuse existing volumes containing your data** : PVs are pre-provisioned using the volume handle of the original PV in the backup.
  * **Don't restore volume data** : PVs aren't restored. Backup for GKE only restores the selected persistent volume claims (PVCs) and expects the corresponding storage driver to either dynamically provision blank PVs or bind them to pre-provisioned PVs created out-of-band.



For instructions on creating a restore plan with volume data restore policy, see [Create a restore plan](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/restore-plan#create_a_restore_plan).

There are a few reasons why you might want to define custom volume restore behavior apart from the default volume data restore policy:

  * To restore a workload with a storage environment that includes different types of volumes with varying levels of data backup support. For example, your workload may contain NFS volumes and Persistent Disk volumes.
  * To apply a different restore process to a specific volume.



Backup for GKE provides two mechanisms for defining custom volume restore behavior:

  * Volume type specific bindings, which you can define as part of a [restore plan](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/restore-plan#create_a_restore_plan).
  * Volume specific overrides, which you can define as part of a [restore](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/restore#create_a_restore).



## Volume data restore policy selection process

During the restore process, Backup for GKE selects the appropriate volume restore policy for each PersistentVolumeClaim (PVC) using the following sequence:

  1. Before any transformation rules are applied, each PVC to be restored moves through a selection process and applies the first in-scope policy.
  2. If the PVC is not bound to a backed up PersistentVolume (PV), only the PVC configuration is restored. This doesn't include any data.
  3. If the PVC is included in a volume data restore policy override, the override policy takes precedence.
  4. If the PVC's volume type is included in a volume data restore policy binding, the binding policy is applied.
  5. If none of the earlier conditions match, the PVC uses the default volume data restore policy.

**Note:** If the **Provision new volumes and restore volume data from backup** policy is applied to a volume without a volume backup, Backup for GKE restores the PVC configuration without data.

## Volume data restore policy bindings

The volume data restore policy bindings let you restore volume data with a policy for a specific volume type. This policy takes precedence over the default volume restore policy. The volume data restore policy binding is only supported for Compute Engine Persistent Disks.

### gcloud

Add volume data restore policy bindings to an existing restore plan:
    
    
      gcloud beta container backup-restore restore-plans update RESTORE_PLAN \
          --project=PROJECT_ID \
          --location=LOCATION \
          --volume-data-restore-policy-bindings=[VOLUME_TYPE=POLICY,...]
    

Replace the following:

  * `RESTORE_PLAN`: the name of the restore plan that you want to update.
  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION`: the [compute region](https://docs.cloud.google.com/compute/docs/regions-zones#available) for the resource, such as `us-central1`.
  * `VOLUME_TYPE=POLICY`: binds a supported volume type to a volume data restore policy. For example, `gce-persistent-disk=restore-volume-data-from-backup` creates a binding that results in Persistent Disk volumes being restored using the **Restore volume data from backup** policy.



### Console

Use the following instructions to add bindings to an existing restore plan in the Google Cloud console:

  1. In the Google Cloud console, go to the **Google Kubernetes Engine** page.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the navigation menu, click **Backup for GKE**.

  3. Click the **Restore plans** tab.

  4. Click the restore plan name.

  5. Click the **Details** tab.

  6. In the **Restore configuration** section, click **Edit** that is next to **Scope**.

  7. In the **Define policy override for specific volume types** section, click the **GCE Persistent Disk** checkbox.

  8. From the **Volume data restore policy** list, choose a restore policy type that you want to use for Compute Engine Persistent Disk.

  9. Click **Save changes**.




## Volume data restore policy overrides

The volume data restore policy overrides define how to restore specific volumes. Volumes are selected by their PVC namespaces and PVC names. You can include multiple volumes in a single override.

Overrides don't enforce unique scoping, unlike bindings. This means that during volume restoration, the policy from the latest override that matches a volume's namespace and name is used.

### Override example

The following example overrides `ns-1/test-pvc` and `ns-1/test-pvc-2` to use the **Reuse existing volumes containing your data** policy and `ns-2/test-pvc-3` to use the **Don't restore volume data** policy.
    
    
    volumeDataRestorePolicyOverrides:
    - policy: REUSE_VOLUME_HANDLE_FROM_BACKUP
      selectedPvcs:
        namespacedNames:
        - namespace: ns-1
          name: test-pvc
        - namespace: ns-1
          name: test-pvc-2
    - policy: NO_VOLUME_DATA_RESTORATION
      selectedPvcs:
        namespacedNames:
        - namespace: ns-2
          name: test-pvc-3
    

### gcloud

Create a restore with overrides:
    
    
    gcloud beta container backup-restore restores create RESTORE \
        --project=PROJECT_ID \
        --location=LOCATION \
        --restore-plan=RESTORE_PLAN \
        --backup=BACKUP \
        --volume-data-restore-policy-overrides-file=OVERRIDES_FILE
    

Replace the following:

  * `RESTORE`: the name of the restore that you want to create.
  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION`: the [compute region](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the parent restore plan.
  * `RESTORE_PLAN`: the name of the parent restore plan this restore is derived from.
  * `BACKUP`: the backup to restore.
  * `OVERRIDES_FILE`: the path to a YAML file that defines overrides in the schema as seen in the example.



### Console

To create a volume data restore policy override, you need to provide the PVC name, PVC namespace, and a restore policy.

Use the following instructions to create a restore with overrides in the Google Cloud console:

  1. In the Google Cloud console, go to the **Google Kubernetes Engine** page.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the navigation menu, click **Backup for GKE**.

  3. Click the **Backups** tab.

  4. In the list of backups, find the backup that you want to restore and click **Set up a restore**.

  5. Choose a restore plan from the list of plans that apply to this backup.

  6. In the **Name the restore** section, enter a name and optional description for the restore.

  7. In the **Override volume data restore policy** section, click **Add policy** and complete the following for each override:

     1. In **PVC name** , enter the name of the PVC.
     2. In **Namespace** , enter the namespace of the PVC.
     3. From the **Volume restore policy** list, choose how to restore that PVC's volume data.
  8. Click **Restore**.




## What's next

  * Learn more about [restoring a backup](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/restore).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
