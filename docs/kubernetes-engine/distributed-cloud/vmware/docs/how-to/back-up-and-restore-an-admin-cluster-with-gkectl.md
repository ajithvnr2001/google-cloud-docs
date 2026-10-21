---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/back-up-and-restore-an-admin-cluster-with-gkectl/
title: Back up and restore an admin cluster with gkectl \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:19:45.439767+00:00
---

# Back up and restore an admin cluster with gkectl  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/back-up-and-restore-an-admin-cluster-with-gkectl/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Back up and restore an admin cluster with gkectl Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to back up and restore an admin cluster created with Google Distributed Cloud (software only) for VMware. The backup process includes backing up the cluster's etcd data, Secrets, and certificates using the `gkectl` command-line tool. You can also [back up and restore](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/back-up-admin-cluster) an admin cluster manually.

To back up and restore a cluster with [advanced cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/advanced-clusters) enabled, see [Back up and restore advanced clusters with gkectl](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/back-up-and-restore-advanced-cluster-with-gkectl).

**Note:** Using a third-party backup tool, such as Veeam, to back up an admin cluster isn't supported. Backing up the cluster with a third-party tool might lead to unforeseen errors in cluster operations.

## Back up an admin cluster

You can set up admin cluster backups so they are automatically performed before and after cluster creation, update, and upgrade. You can also perform an on-demand backup whenever you deem it necessary.

An admin cluster backup includes the following:

  * Admin cluster etcd data
  * Secrets
  * Certificates
  * Always-on secrets encryption keys and config files if always-on secrets encryption feature is enabled
  * Admin cluster kubeconfig file (1.29 and higher)
  * Admin cluster SSH key file (1.29 and higher)



The size of a backup can range from 3 MB–100 MB depending on the size of the cluster.

## Enable the admin cluster backup feature

By default this feature is disabled. To enable the admin cluster backup feature:

  1. Add the following section to the [admin cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest):
         
         clusterBackup:
           datastore: DATASTORE
         

Replace DATASTORE with the datastore where you want to store the backup. The datastore must be in the same datacenter as the admin cluster.

For non HA admin cluster, backups are located in the "anthos-backup/DATADISK_PATH" directory of the specified datastore.

For HA admin cluster, backups are located in "anthos/ADMIN_CLUSTER_NAME/backup" directory of the specified datastore.

  2. Update the admin cluster:
         
         gkectl update admin --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config ADMIN_CLUSTER_CONFIG
         

Replace:

     * ADMIN_CLUSTER_KUBECONFIG with the path of your admin cluster kubeconfig file.
     * ADMIN_CLUSTER_CONFIG with the path of your admin cluster configuration file.



## Disable the admin cluster backup feature

  1. Remove the `clusterBackup` section from the admin cluster configuration file.
         
         clusterBackup:
           datastore: DATASTORE
         

  2. Update the admin cluster with this change, using this command:
         
         gkectl update admin --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config ADMIN_CLUSTER_CONFIG
         




## Update the backup datastore

You can update the datastore where backups are stored by updating `clusterBackup.datastore` to reflect the new location. The new datastore must be in the same datacenter as the admin cluster.

  1. Edit the admin cluster configuration file to change the `clusterBackup.datastore` value.
         
         clusterBackup:
           datastore: new-datastore
         

  2. Update the admin cluster with this change, using this command:
         
         gkectl update admin --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config ADMIN_CLUSTER_CONFIG
         




## On-demand backup

To trigger an on-demand admin cluster backup, run the following command:
    
    
    gkectl  backup admin --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config ADMIN_CLUSTER_CONFIG
       

## Limit on number of backups

You can have a maximum total of six backups, divided into a maximum of three on-demand backups, and a maximum of three backups from cluster update, upgrade or create operations. These backups are automatically rotated should these limits be exceeded. No manual intervention is necessary.

## Restore an admin cluster

**Warning:** Using a backup to restore your admin cluster is a last resort. We do not recommend that you restore from a backup file unless the admin cluster is completely broken. Contact Google Support for help in deciding the best course of action.

You should restore an admin cluster only when it is completely broken with data loss or corruption. For example,

  * The admin master data disk is lost or corrupted.
  * The admin cluster's etcd is lost or corrupted.
  * The admin cluster's control plane secrets and certificates are lost or corrupted.



Do not use this approach to restore a working admin cluster to an arbitrary previous state. This restore feature should not be used as a way to revert admin cluster operations such as a cluster update or cluster upgrade.

Do not use this approach to restore HA admin cluster. For HA admin cluster we only support `gkectl repair admin-master`, but not `gkectl repair admin-master --restore-from-backup`.

To recreate the admin cluster from a backup, run the following command:
    
    
      gkectl repair admin-master --kubeconfig ADMIN_CLUSTER_KUBECONFIG --config ADMIN_CLUSTER_CONFIG --restore-from-backup
      

This command retrieves all of the backups of this admin cluster from the datastore defined in the `clusterBackup` section of the admin cluster configuration file, and it prompts you to select the one from which you want to use to restore the admin cluster.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
