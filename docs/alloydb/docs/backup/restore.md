---
url: https://docs.cloud.google.com/alloydb/docs/backup/restore/
title: Restore a cluster from a backup \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:23.093526+00:00
---

# Restore a cluster from a backup  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/backup/restore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Restore a cluster from a backup Stay organized with collections  Save and categorize content based on your preferences. 

To recover an AlloyDB for PostgreSQL cluster to the state it was in when a backup was taken—even if the original cluster has been deleted—you can restore a new cluster from a stored backup.

## Before you begin

  * The Google Cloud project you are using must have been [enabled to access AlloyDB](https://docs.cloud.google.com/alloydb/docs/quickstart/create-and-connect#before-you-begin). 
  * You must have one of these IAM roles in the Google Cloud project you are using: 
    * `roles/alloydb.admin` (the AlloyDB Admin predefined IAM role)
    * `roles/owner` (the Owner basic IAM role)
    * `roles/editor` (the Editor basic IAM role)

If you don't have any of these roles, contact your Organization Administrator to request access.




  * You must have all of the following Identity and Access Management (IAM) permissions in the Google Cloud project you are using: 
    * `compute.networks.list`
    * `compute.addresses.create`
    * `compute.addresses.list`
    * `compute.globalAddresses.create`
    * `compute.globalAddresses.list`
    * `servicenetworking.services.addPeering`

To gain these permissions while following the principle of least privilege, ask your administrator to grant you the AlloyDB Admin (`roles/alloydb.admin`) predefined IAM role, which includes the required `alloydb.clusters.restore` and networking permissions. 




## Restore from a backup

When you restore from a backup, you configure a new cluster. You must create this new cluster in the same region as the backup. The new cluster can be in a different Google Cloud project. AlloyDB creates the cluster and restores the backup's data to that cluster's data storage. Then, you create an instance in that cluster to access the data.

### Restore a cross-project backup

To restore a backup to a different project, use the Google Cloud CLI instructions in Restore a backup to a new AlloyDB cluster. Set `--project` to your destination project.

Cross-project backup restores aren't supported in the Google Cloud console.

### Restore a cross-regional backup

To restore a backup to a different region, you must create an on-demand backup in the target region. Then, you can use your on-demand backup for the restore in the target region.

To restore a backup to a different region, follow these steps:

  1. [Create an on-demand backup](https://docs.cloud.google.com/alloydb/docs/backup/create-on-demand) in the target region.
  2. Restore the on-demand backup to a new cluster in the target region.



### Restore a backup to a new AlloyDB cluster

You can restore your backup to a new AlloyDB cluster using the Google Cloud console or Google Cloud CLI.

  1. Restore the backup to a new AlloyDB cluster. 

### Console

     1. In the Google Cloud console, go to the **Backups** page. 

[Go to Backups](https://console.cloud.google.com/alloydb/backups)

     2. In the list of backups, locate the backup you want to restore and click **Restore** in its row.
     3. In the **Cluster ID** field, enter an ID for the cluster that will be created to host the restored data.
     4. In the **Network** list, select the network you want the newly created cluster to be accessible from.
     5. If you want to encrypt the new cluster's data with a [customer-managed encryption key (CMEK)](https://docs.cloud.google.com/alloydb/docs/cmek) instead of Google-managed encryption, follow these additional steps:

        1. Click **Advanced encryption options**.
        2. Select **Cloud KMS key**.
        3. In **Key type** , select **Cloud KMS**.
        4. Select a customer-managed key from the menu that appears.

The Google Cloud console limits this list to keys within the same Google Cloud project and region as the new cluster. To use a key that is not on this list, click **Don't see your key? Enter key resource name** , and then type the key's resource name into the resulting dialog.

Note that using CMEK with AlloyDB requires some additional setup. For more information, see [Using CMEK with AlloyDB](https://docs.cloud.google.com/alloydb/docs/use-cmek).

     6. Click **Restore**.

### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

Use the [ ` gcloud alloydb clusters restore`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/clusters/restore) command to create a cluster and restore the backup's data to it.
    
    gcloud alloydb clusters restore CLUSTER_ID \
        --backup=BACKUP_ID \
        --network=NETWORK \
        --region=REGION_ID \
        --project=PROJECT_ID \
        --async

This command returns an operation, whose status you can query using the [`gcloud alloydb operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/operations/describe) command.
    
    gcloud alloydb operations describe OPERATION_ID \
        --region=REGION_ID \
        --project=PROJECT_ID

     * `CLUSTER_ID`: The ID of the cluster to create.
     * `BACKUP_ID`: The ID of the backup to restore into the new cluster.  
To restore from a backup in a different project, replace with the full backup path in the following format:  
`projects/SOURCE_PROJECT/locations/SOURCE_REGION/backups/SOURCE_BACKUP`
     * `NETWORK`: The name of the VPC network you want the newly created cluster to be accessible from.
     * `REGION_ID`: The ID of the region where the source backup is stored and where the new cluster is created.
     * `PROJECT_ID`: The ID of the project where the new cluster is.

If you want to encrypt the new cluster's data using a [customer-managed encryption key (CMEK)](https://docs.cloud.google.com/alloydb/docs/cmek) instead of the default Google-managed encryption, then you must provide these additional arguments:

     * `--kms-key=KEY_ID`: The ID of the CMEK key to use.
     * `--kms-keyring=KEYRING_ID`: The ID of the key ring.
     * `--kms-location=LOCATION_ID`: The ID of that keyring's region. Note that it must match the cluster's region.
     * `--kms-project=PROJECT_ID`: The keyring's project ID.

To restore a cluster with Private Service Connect enabled, make sure that you add the `--enable-private-service-connect` flag.

  2. After AlloyDB finishes creating the cluster, [create a primary instance](https://docs.cloud.google.com/alloydb/docs/instance-primary-create) for it.

When creating the new primary instance, you need to specify its configuration, including its size and flags; AlloyDB does not store instance configuration as part of the backup. Note that the configuration need not exactly match that of the original primary instance.

When AlloyDB finishes creating the instance, you can use it to access your restored data.

  3. Finish configuring the new cluster by [setting up read-pool instances](https://docs.cloud.google.com/alloydb/docs/instance-read-pool-create), if necessary.



## What's next

  * [Restore an existing cluster to a recent past state](https://docs.cloud.google.com/alloydb/docs/backup/restore-pitr).
  * [Create a read pool instance](https://docs.cloud.google.com/alloydb/docs/instance-read-pool-create).
  * [Create a secondary cluster and instance](https://docs.cloud.google.com/alloydb/docs/cross-region-replication/work-with-cross-region-replication).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
