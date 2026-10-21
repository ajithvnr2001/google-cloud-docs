---
url: https://docs.cloud.google.com/alloydb/docs/backup/restore-pitr/
title: Use point-in-time recovery (PITR) \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:43:38.304999+00:00
---

# Use point-in-time recovery (PITR)  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/backup/restore-pitr/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Use point-in-time recovery (PITR) Stay organized with collections  Save and categorize content based on your preferences. 

To recover rapidly from accidental data modification or large-scale data loss, you can use point-in-time recovery (PITR) to restore an AlloyDB for PostgreSQL cluster to a specific state from the recent past.

## Before you begin

  * The Google Cloud project you are using must have been [enabled to access AlloyDB](https://docs.cloud.google.com/alloydb/docs/quickstart/create-and-connect#before-you-begin). 
  * You must have one of these IAM roles in the Google Cloud project you are using: 
    * `roles/alloydb.admin` (the AlloyDB Admin predefined IAM role)
    * `roles/owner` (the Owner basic IAM role)
    * `roles/editor` (the Editor basic IAM role)

If you don't have any of these roles, contact your Organization Administrator to request access.




  * You must have all of the following Identity and Access Management (IAM) permissions in the Google Cloud project that you're using: 
    * `compute.networks.list`
    * `compute.addresses.create`
    * `compute.addresses.list`
    * `compute.globalAddresses.create`
    * `compute.globalAddresses.list`
    * `servicenetworking.services.addPeering`

To gain these permissions while following the principle of least privilege, ask your administrator to grant you the AlloyDB Admin (`roles/alloydb.admin`) predefined IAM role, which includes the required `alloydb.clusters.restore` and networking permissions. 




## Restore from a recent point in time

AlloyDB lets you fully restore an active cluster's data from any point in time within a specific, recent range.

### Available PITR windows

You can restore from any point in time after the more recent of the following two moments:

  * **The moment represented by the limit of your recovery window.** For example, if you have a 14-day recovery window, then this moment is 14 days in the past.

  * **The creation time of the oldest backup taken since you last enabled continuous backup.** If you created the cluster with continuous backup enabled, and you have not disabled continuous backup since then, then this moment effectively becomes the creation time of your cluster's oldest backup.




If you disable and subsequently re-enable continuous backup, then you cannot perform a point-in-time recovery until either you or AlloyDB creates the cluster's first new backup. This can be an on-demand backup, or the first of the daily backups that AlloyDB takes after you enable continuous backup. For more information about backup types, see [Data backup and recovery overview](https://docs.cloud.google.com/alloydb/docs/backup/overview).

You can only perform a point-in-time recovery if the original cluster exists. You can't perform this type of restore on a deleted cluster.

You can perform a point-in-time recovery on a cluster in a ready state, even if its primary instance is deleted. However, the recovery can only restore the cluster to a point in time before the instance was deleted.

**Note:** Point-in-time recovery is paused for the original primary cluster during a [cross-region failover](https://docs.cloud.google.com/alloydb/docs/cross-region-replication/work-with-cross-region-replication#promote-secondary-cluster). Coverage resumes automatically after the original primary cluster becomes the secondary cluster and a new baseline backup is established.

### Perform a point-in-time restore

  1. Use either the Google Cloud console or the Google Cloud CLI to perform the restore.

### Console

     1. Go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

     2. Click a cluster in the **Resource Name** column.

     3. Click **Data protection**.

     4. Under **Restore from a point in time** , click **Restore**.

     5. In the **Target time** field, enter the date and time to restore from.

     6. In the **Cluster ID** field, enter a name for the new cluster.

     7. In the **Network** field, select a Virtual Private Cloud network for the new cluster to use.

     8. If you want to encrypt this cluster's continuous backups and data-change logs using a [customer-managed encryption key (CMEK)](https://docs.cloud.google.com/alloydb/docs/cmek) instead of the default Google-managed encryption, follow these additional steps:

        1. Click **Advanced encryption options**.

        2. Click the **Customer-managed encryption key (CMEK)** radio button.

        3. Click the **Select a customer-managed key** list, and select a key.

     9. Click **Restore**.

### gcloud

Use the [`gcloud alloydb clusters restore`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/clusters/restore) command, specifying a cluster and a timestamp.
    
    gcloud alloydb clusters restore NEW_CLUSTER \
      --source-cluster=SOURCE_CLUSTER \
      --point-in-time=TIMESTAMP \
      --region=REGION

This command returns an operation, whose status you can query using the [`gcloud alloydb operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/operations/describe) command.
    
    gcloud alloydb operations describe OPERATION_ID \
      --region=REGION

Replace the following:

     * `NEW_CLUSTER`: The ID to use with the new cluster.

     * `SOURCE_CLUSTER`: The ID of the cluster to recover data from.  
To restore from a cluster in a different project, replace with the full cluster path in the following format:  
`projects/SOURCE_PROJECT/locations/SOURCE_REGION/clusters/SOURCE_CLUSTER`

     * `TIMESTAMP`: A description of the point in time to recover data from, expressed in [RFC 3339 format](https://datatracker.ietf.org/doc/html/rfc3339)—for example, `2012-11-15T16:19:00.094Z`. You can specify a fractional second as small as a microsecond.

Note that this timestamp must exist within the retention period you specified when you created the cluster.

     * `REGION`: The region that contains the source cluster, and where AlloyDB creates the new cluster. For example: `us-central1`.

     * `PROJECT_ID`: The ID of the project where the new cluster is.

If you want to encrypt the new cluster's data with a [customer-managed encryption key (CMEK)](https://docs.cloud.google.com/alloydb/docs/cmek) instead of Google-managed encryption, then you must provide these additional arguments:

     * `--kms-key=KEY_ID`: The ID of the CMEK key to use.
     * `--kms-keyring=KEYRING_ID`: The ID of the key's key ring.
     * `--kms-location=LOCATION_ID`: The ID of that keyring's region. Note that it must match the cluster's region.
     * `--kms-project=PROJECT_ID`: The ID of the keyring's project.

To restore to a cluster with Private Service Connect enabled, make sure that you add the `--enable-private-service-connect` flag.

  2. After AlloyDB finishes creating the cluster, [create a primary instance for it](https://docs.cloud.google.com/alloydb/docs/instance-primary-create). That instance lets you access the restored data. Note that the new instance's configuration need not exactly match that of the original primary instance.

  3. Optional: [Create read-pool instances.](https://docs.cloud.google.com/alloydb/docs/instance-read-pool-create)




You can start using the cluster after the restore operation completes.

## What's next

  * [Restore a cluster from a stored backup.](https://docs.cloud.google.com/alloydb/docs/backup/restore)
  * [Create a read pool instance.](https://docs.cloud.google.com/alloydb/docs/instance-read-pool-create)
  * [Create a secondary cluster and instance.](https://docs.cloud.google.com/alloydb/docs/cross-region-replication/work-with-cross-region-replication)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
