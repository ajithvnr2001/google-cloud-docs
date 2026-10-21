---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/back-up-and-restore-advanced-cluster-with-gkectl/
title: Back up and restore advanced clusters with gkectl \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:16:02.487819+00:00
---

# Back up and restore advanced clusters with gkectl  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/back-up-and-restore-advanced-cluster-with-gkectl/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Back up and restore advanced clusters with gkectl Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to back up and restore Google Distributed Cloud version 1.32 and higher admin and user clusters that have [advanced cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/advanced-clusters) enabled. The backup and restore feature is in Preview in version 1.32 and GA in version 1.33 and higher.

**Warning:** Using a backup file to restore your cluster is a last resort. The restore process resets the existing cluster and overwrites the cluster information. We don't recommend restoring from a backup file unless the cluster has failed catastrophically. Contact Cloud Customer Care for help in deciding the best course of action.

The `gkectl` backup and restore process does not include persistent volumes. Any volumes created by the local volume provisioner (LVP) are left unaltered.

### Back up a cluster

The `gkectl backup cluster` command adds the cluster information from the etcd store and the PKI certificates for the specified cluster to a tar file. The etcd store is the Kubernetes backing store for all cluster data and contains all the Kubernetes objects and custom objects required to manage cluster state. The PKI certificates are used for authentication over Transport Layer Security (TLS). This data is backed up from the cluster's control plane or from one of the control planes for a high-availability (HA) deployment.

The backup tar file contains sensitive credentials, including your service account keys and the SSH key. Store backup files in a secure location. To prevent unintended file exposure, the backup process uses in-memory files only.

Back up your clusters regularly to ensure your snapshot data is relatively current. Adjust the rate of backups to reflect the frequency of significant changes to your clusters.

Before you begin, ensure your cluster is operating properly, with working credentials and SSH connectivity to all nodes. The intent of the backup process is to capture your cluster in a known good state so that you can restore operation if a catastrophic failure occurs.

To back up a cluster:

  1. Run the following command to check your cluster:
         
         gkectl diagnose cluster --cluster-name CLUSTER_NAME \
             --kubeconfig ADMIN_KUBECONFIG
         

Replace the following:

     * CLUSTER_NAME: the name of the cluster you plan to back up.

     * ADMIN_KUBECONFIG: the path of the kubeconfig file for the admin cluster.

  2. Run the applicable command to back up the cluster:

### Admin cluster
         
         gkectl backup admin --kubeconfig ADMIN_KUBECONFIG
         

### User cluster
         
         gkectl backup cluster --cluster-name CLUSTER_NAME \
             --kubeconfig ADMIN_KUBECONFIG
         




By default, the backup tar file is saved to the directory `gkectl-workspace/backups` on your admin workstation. The tar file is named `CLUSTER_NAME_backup_TIMESTAMP.tar.gz`, where `CLUSTER_NAME` is the name of the cluster being backed up and `TIMESTAMP` is the date and time the backup was made. For example, if the cluster name is `testuser`, the backup file has a name like `testuser_backup_2025-08-23T150405Z0700.tar.gz`.

Optionally, you can specify a different name and location for your backup file with the `--backup-file` flag, for example:
    
    
    gkectl backup cluster testuser \
        --kubeconfig admin-cluster/kubeconfig \
        --backup-file cluster-backups/testuser-backup-aug-23-2025.tar.gz
    

The backup file expires after a year and the cluster restore process doesn't work with expired backup files.

#### Backup to vSphere

To configure backups so that the backup file for both admin and user clusters are uploaded to vSphere in addition to being saved on your admin workstation, do the following:

  1. Add the [clusterBackup.datastore](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#clusterbackup-datastore-field) field to your admin cluster configuration file:
         
         clusterBackup:
             datastore: DATASTORE
         

Replace `DATASTORE` with the datastore where you want to store the backup. The datastore must be in the same datacenter as the admin cluster. The backups are located in the `anthos/CLUSTER_NAME/backup` directory of the specified datastore.

  2. Update the admin cluster:
         
         gkectl update admin --kubeconfig ADMIN_KUBECONFIG \
             --config ADMIN_CONFIG
         

Replace the following:

     * `ADMIN_KUBECONFIG`: the path of the kubeconfig file for the admin cluster.

     * `ADMIN_CONFIG`: the path of the admin cluster configuration file.




By default, the `gkectl backup` command saves the three most recent backup files in vSphere and deletes older backup files. If you want to keep the older backup files, add the flag `--keep-all-backups`, which is available in version 1.32.100 and higher.

### Restore a cluster

Restoring a cluster from a backup is a last resort and should only be used when a cluster has failed catastrophically and can't be returned to service any other way. For example, the etcd data is corrupted or the etcd Pod is in a crash loop.

Use the `gkectl restore` command only if all three control plane nodes have failed.

  * If only one node has failed, and [`autoRepair.enabled`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#autorepair-enabled-field) is set to `true` in the admin cluster configuration file, the failed node is automatically repaired. If `autoRepair.enabled` isn't configured, add it to the admin cluster configuration file and run `gkectl update admin`. After the update, the node is automatically recreated.

  * If two control plane nodes have failed, see the Restore quorum section on this page.


**Note:** To improve cluster performance, Google Distributed Cloud uses a separate etcd instance to store Event objects. These Event objects have a time to live (TTL) of one hour. The cluster restore operation creates a new, empty etcd-events instance, so you lose existing Event objects. However, the loss of Event objects has no impact on cluster operation. Events should be treated as informative, best-effort, supplemental data only.

The backup tar file contains sensitive credentials, including your service account keys and the SSH key. To prevent unintended file exposure, the Google Distributed Cloud restore process uses in-memory files only.

Before you restore a cluster, make sure that the following conditions are met:

  * All control plane node machines that were available for the cluster at the time of the backup are operating properly and reachable.
  * SSH connectivity between nodes works with the SSH keys that were used at the time of the backup. These SSH keys are reinstated as part of the restore process.
  * The service-account keys that were used at the time of the backup are still active. These service-account keys are reinstated for the restored cluster.



To restore a cluster:

  1. Run the applicable command to restore the cluster:

### Admin cluster
         
         gkectl restore admin --backup-file BACKUP_FILE \
             --config ADMIN_CONFIG
         

Replace the following:

     * `BACKUP_FILE`: the path and name of the backup file you are using.

     * `ADMIN_CONFIG`: the path to the admin cluster config file.

### User cluster
    
    gkectl restore cluster --cluster-name CLUSTER_NAME \
        --backup-file BACKUP_FILE \
        --kubeconfig ADMIN_KUBECONFIG
    

Replace the following:

     * `CLUSTER_NAME`: the name of the cluster you are restoring.

     * `BACKUP_FILE`: the path and name of the backup file you are using.

     * `ADMIN_KUBECONFIG`: the path to the admin cluster kubeconfig file.

At the end of the restore process, a new kubeconfig file is generated for the restored cluster at the workspace directory `gkectl-workspace`.

  2. When the restore finishes, run the following command to verify that it was successful:
         
         gkectl diagnose cluster --cluster-name CLUSTER_NAME \
             --kubeconfig GENERATED_KUBECONFIG
         

Replace `GENERATED_KUBECONFIG` with the generated kubeconfig file.




### Restore quorum

When two control plane nodes have failed in a cluster, you can use the `gkectl restore` command to restore quorum. When restoring quorum, instead of specifying the backup file to the `gkectl restore` command, you specify the IP address of the working control plane node.

Before running the command, make sure that the following conditions are met:

  * There is one (and only one) control plane node working.
  * The working control plane node is accessible with the SSH key. For more information, see [Using SSH to connect to a cluster node](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ssh-cluster-node).



To restore quorum, run the applicable command for your cluster type:

### Admin cluster
    
    
    gkectl restore admin --kubeconfig ADMIN_KUBECONFIG \
        --config ADMIN_CONFIG \
        --control-plane-node WORKING_NODE_IP \
        --ssh-key ADMIN_SSH_KEY_PATH
    

Replace the following:

  * `ADMIN_KUBECONFIG`: the path of the kubeconfig file for the admin cluster.

  * `ADMIN_CONFIG`: the path of the admin cluster configuration file.

  * `WORKING_NODE_IP`: the IP address of the working control plane node.

  * `ADMIN_SSH_KEY_PATH`: the admin cluster SSH key path.




### User cluster
    
    
    gkectl restore cluster --cluster-name CLUSTER_NAME \
        --kubeconfig ADMIN_KUBECONFIG \
        --control-plane-node WORKING_NODE_IP \
        --ssh-key USER_SSH_KEY_PATH
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster you are restoring.

  * `ADMIN_KUBECONFIG`: the path to the admin cluster kubeconfig file.

  * `WORKING_NODE_IP`: the IP address of the working control plane node.

  * `USER_SSH_KEY_PATH`: the user cluster SSH key path.




### Troubleshoot

If you have problems with the backup or restore process, the following sections might help you to troubleshoot the issue.

If you need additional assistance, reach out to the Cloud Customer Care team.

#### Running out of memory during a backup or restore

If the workstation where you run the `gkectl` command doesn't have a lot of RAM, you might have insufficient memory to perform the backup or restore process. If needed, create and use a temporary scratch disk to process the backup or restore operations by using the `--use-disk` parameter in the backup command. To preserve the file permissions, this parameter modifies permissions of the files, so it requires that you run the command as a root user (or use `sudo`).

#### Refresh of SSH key after a backup breaks the restore process

SSH-related operations during the restore process might fail if the SSH key is refreshed after a backup was performed. In this case, the new SSH key becomes invalid for the restore process. To resolve this issue, you can temporarily add the original SSH key back, then perform the restore. After the restore process is complete, you can rotate the SSH key.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
