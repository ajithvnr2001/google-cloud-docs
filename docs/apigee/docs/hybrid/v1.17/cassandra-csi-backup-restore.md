---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cassandra-csi-backup-restore/
title: Cassandra CSI backup and restore \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:11:04.830757+00:00
---

# Cassandra CSI backup and restore  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cassandra-csi-backup-restore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Cassandra CSI backup and restore Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.17 (latest)keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cassandra-csi-backup-restore.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cassandra-csi-backup-restore.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/cassandra-csi-backup-restore.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/cassandra-csi-backup-restore.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/cassandra-csi-backup-restore.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/cassandra-csi-backup-restore.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/cassandra-csi-backup-restore.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cassandra-csi-backup-restore.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/cassandra-csi-backup-restore.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/cassandra-csi-backup-restore.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/cassandra-csi-backup-restore.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/cassandra-csi-backup-restore.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/cassandra-csi-backup-restore.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/cassandra-csi-backup-restore.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/cassandra-csi-backup-restore.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/cassandra-csi-backup-restore.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/cassandra-csi-backup-restore.html)



You can back up and restore your [hybrid data](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cassandra-backup-overview#what-is-backed-up) using [CSI](https://kubernetes.io/docs/concepts/storage/volume-snapshots/) (Container Storage Interface) snapshots. CSI backup triggers disk snapshots taken by the underlying storage system using the provided CSI driver. CSI backup does not need a Google Cloud Storage bucket or a remote server to store backup data. 

CSI backup is recommended for hybrid instances hosted in Google Cloud, AWS, or Azure. 

This page describes the steps to use hybrid CSI backup and restore. For an overview of hybrid back up and restore in general, see the [Cassandra backup and restore overview](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cassandra-backup-overview). 

Warning about deleting: 

Be careful which version or release of the datastore components you delete. You can see your releases with the command `helm -n APIGEE_NAMESPACE ls`. To delete a specific release use `helm -n APIGEE_NAMESPACE delete RELEASE-NAME`. 

## Backup and restore limitations

Be aware of these limitations when using CSI backup and restore:

  * The CSI driver used by the configured storage class must support CSI snapshots. See this [Kubernetes CSI driver list](https://kubernetes-csi.github.io/docs/drivers.html) for driver information.
  * Not all platforms are supported. Only Google Cloud, AWS, and Azure platforms are supported.
  * OpenShift Container Platform is not supported due to volume snapshot [limitations](https://docs.openshift.com/container-platform/4.12/storage/container_storage_interface/persistent-storage-csi-snapshots.html#persistent-storage-csi-snapshots-create_persistent-storage-csi-snapshots).
  * Only cloud platforms are supported. On-prem platforms are not supported.
  * CSI backup data and non-CSI hybrid backup data are incompatible. Non-CSI backups cannot be used with CSI restore and CSI backups cannot be used with non-CSI restore.
  * CSI driver installation and functionality is the responsibility of the CSI driver vendor.
  * Users are responsible for ensuring adequate cluster resources are available for provisioning CSI snapshots.
  * Users are responsible for removing old snapshot data.



## Set up CSI backups

To schedule hybrid backups using CSI, perform the following steps: 

  1. If you have not previously set up hybrid backup: 
     1. Run the following `create-service-account` command to create a Google Cloud service account (SA) with the standard [ `roles/storage.objectAdmin`](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) role. This SA role allows you to write backup data to Cloud Storage. Execute the following command in the directory appropriate for your management tool: 
        * **Helm charts:** `$APIGEE_HELM_CHARTS_HOME/apigee-operator/etc/`
        * **`apigeectl`:** `HYBRID_BASE_DIRECTORY/hybrid-files/`
    
    ./tools/create-service-account --env non-prod --dir ./service-accounts

This command creates a single service account named `apigee-non-prod` for use in non-production environments and places the downloaded key file in the `./service-accounts` directory.

**Note:** If you prefer to create all the individual service accounts for a production environment, use the following command: 
    
    ./tools/create-service-account **--env prod** --dir ./service-accounts

For more information about Google Cloud service accounts, see [Creating and managing service accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts).

     2. The `create-service-account` command saves a JSON file containing the service account private key. The file is saved in the same directory where the command executes. You will need the path to this file in the following steps.
  2. Open your `overrides.yaml` file. Set the follow parameters, as shown in Example overrides files. 
     1. Set the general parameters shown below in the `backup` block. If you've already set these parameters for the non-CSI hybrid back up solution, you can use the same parameters for your CSI snapshots. See [backup properties reference table](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/schedule-cassandra-backup-gcs#backup-properties-ref) for more information about each value.  


For `backup`: 

        * **enabled:** Set to `true` to enable scheduled backups.
        * **pullPolicy in image:** Set to `Always`.
        * **schedule:** Provide a [cron expression schedule](https://en.wikipedia.org/wiki/Cron#Cron_expression).
     2. Set these parameters for CSI-specific backup: 
        * **Cassandra storage group values:** The configured Cassandra storage class must support CSI snapshots for CSI backup and restore to work. To check if a storage class supports CSI snapshots, run the following command to get the available storage classes: 
              
              kubectl get sc

Look at the "Provisioner" output for each storage class. Provisioners using CSI usually have a ".csi." part to their name like "pd.csi.storage.gke.io". Look for the provisioner name in this [Kubernetes CSI driver list](https://kubernetes-csi.github.io/docs/drivers.html). If the "Other Features" column for the provisioner contains the word "SNAPSHOT", then the storage class using the provisioner supports CSI snapshots. 

Add these parameters in the storage group. Both values are required.

          * **storageclass:** A CSI snapshot-enabled storage class name.
          * **capacity:** The capacity of the disk.
        * **Cloud provider type:**

Once the CSI snapshot capability has been verified, modify the overrides file to use CSI backup and restore: 

          * **cloudProvider:** Set `cloudProvider` in `backup` and `restore` to `CSI`.



### Example backup config

**Note:** If your initial Apigee Hybrid installation was configured without the ` cassandra.storage ` section in your overrides file, you should not add the ` cassandra.storage ` section in your overrides file. Adding this section post-installation to enable backups can lead to an upgrade failure as this may be interpreted as an attempt to modify the storage class of the existing Cassandra statefulset which is not a supported operation. This section shows the backup-related portions of an example `overrides.yaml` file. 
    
    
    cassandra:
      hostNetwork: false
      replicaCount: 3
      storage:
        storageclass: standard-rwo
        capacity: 100Gi
      image:
        pullPolicy: Always
    
      backup:
        enabled: true
        image:
          pullPolicy: Always
        cloudProvider: "CSI"
        schedule: "0 * * 11 *"

## Launch a manual backup

CSI backups generate automatically according to the cron schedule set in the `overrides.yaml` file. 

To initiate a manual CSI backup, use this command: 
    
    
    kubectl create job -n APIGEE_NAMESPACE --from=cronjob/apigee-cassandra-backup BACKUP_POD_NAME

where `BACKUP_POD_NAME` is the name of the backup pod that will be created. 

## Verify backups

One way to verify a backup was successfully created is to check the volume snapshots on the Kubernetes cluster, using this command: 
    
    
    kubectl get volumesnapshot -n APIGEE_NAMESPACE

The output shows the current list of snapshots on the cluster. The CSI backup process creates a snapshot of each Cassandra disk. The number of generated snapshots should match the total number of cassandra pods in the cluster.

## Restore a backup

Use this process to restore a previously generated CSI backup. For general information on restoring backups and an overview of the process, see the [restore overview page](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/restore-cassandra-backup). 

To initiate a restore of a CSI backup, follow the instructions for the [hybrid non-CSI single region restore](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/restore-cassandra-single-region), but use these values in the `restore` block in your `overrides.yaml`. See the [backup properties reference table](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/schedule-cassandra-backup-gcs#backup-properties-ref) for more information about each value and the example restore configuration for an example. 

  * **enabled:** Set to `true` to enable restore for the backup referenced with the `snapshotTimestamp` timestamp.
  * **snapshotTimestamp:** Provide the timestamp of a previous CSI backup.
  * **pullPolicy in image:** Set to `Always`.



To find the `snapshotTimestamp` value to restore, run this command to get the list of available snapshots: 
    
    
    kubectl get volumesnapshot -n APIGEE_NAMESPACE

In the returned list, the names of the snapshots contain the timestamp: 
    
    
    pvc-us-west2-b-20220803004907-47beff0e306d8861

In this example the timestamp is `20220803004907`.  Important: Terminating the Cassandra cluster is a normal part of the CSI restoration process. After terminating the cluster, the restore process creates new PVCs containing the backup data and then re-creates the Cassandra cluster using the new PVCs. Do not be concerned if you see the cluster terminating. 

### Example restore config

This section shows the restore-related portions of an example `overrides.yaml` file. 
    
    
    cassandra:
      hostNetwork: false
      replicaCount: 3
      storage:
        storageclass: standard-rwo
        capacity: 100Gi
      image:
        pullPolicy: Always
    
      restore:
        enabled: true
        snapshotTimestamp: "20220908222130"
        cloudProvider: "CSI"
        image:
          pullPolicy: Always

## Migrate to CSI backup and restore

If you have not previously used hybrid backup and restore, you can follow the instructions in Set up CSI backups to create a new CSI backups without the steps in this section. These steps guide you through migrating from the non-CSI backup and restore solution to CSI backups. 

  1. Generate a new backup using the currently configured non-CSI backup method.
  2. Change the backup configuration in the hybrid `overrides.yaml` file to use the CSI backup overrides as shown in the example backup config.
  3. Apply the changes in the `overrides.yaml` file: 
         
         helm upgrade datastore apigee-datastore/ \
           --namespace APIGEE_NAMESPACE \
           --atomic \
           -f OVERRIDES_FILE.yaml
         

**Note:** If you see an error saying `Error: UPGRADE FAILED: "datastore" has no deployed releases`, replace `upgrade` with `install` and try the command again.
  4. Verify the backup job: 
         
         kubectl get cronjob -n APIGEE_NAMESPACE

  5. After a backup job completes, verify snapshots have been created. The number of generated snapshots should be equivalent to the number of Cassandra nodes in the Hybrid instance. 
         
         kubectl get volumesnapshot -n APIGEE_NAMESPACE


**Note:** Apigee hybrid version 1.14.0 and newer supports [Enhanced per-environment proxy limits](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/enhanced-proxy-limits). However conversion of existing Hybrid orgs to use enhanced per-environment proxy limits is not supported. Therefore, a backup of an organization that was created without enhanced per-environment proxy limits enabled cannot be restored to an organization created with the feature enabled. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
