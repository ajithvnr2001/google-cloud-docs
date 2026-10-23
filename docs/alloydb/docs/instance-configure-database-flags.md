---
url: https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags/
title: Configure an instance's database flags \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:20.119002+00:00
---

# Configure an instance's database flags  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Configure an instance's database flags Stay organized with collections  Save and categorize content based on your preferences. 

To tune PostgreSQL parameters, adjust database options, and customize instance behavior in an AlloyDB for PostgreSQL cluster, you can add, modify, or remove database flags on an instance. Modifications to a database flag's value persist for its instance until you remove the flag or you modify its value again.

In some cases, setting one flag may require that you set another flag to fully enable the target functionality.

After you set, remove, or modify a flag for a database instance, AlloyDB might restart the instance. This depends upon the flag, as listed in [Supported database flags](https://docs.cloud.google.com/alloydb/docs/reference/database-flags).

When you modify a database flag in the primary or a read pool instance that needs a restart, you can choose one of the following maintenance policies:

  * **Low downtime.** This policy is enabled by default. We recommend using this policy for all your production AlloyDB clusters because it minimizes application downtime.

With the low downtime policy enabled, updating a flag that requires a restart on your cluster's primary instance has these effects:

    * The primary instance experiences less than one second of downtime for most workloads.

    * The flag on the primary instance finishes updating to its new value after about 15 minutes.

Updating a flag that requires a restart on a read pool instance has these effects:

    * The read pool instance does not require any downtime.

    * The flag on the read pool instance finishes updating to its new value after about 10 minutes.

  * **Force apply.** To apply flag updates faster, use the `FORCE_APPLY` option with the `gcloud beta alloydb instances update` command.

**Note:** Avoid using the `FORCE_APPLY` option for updates that can change the machine family. For example, updating an instance to the C4A machine family to a different machine family.

This policy is more appropriate for development environments, letting you quickly add or modify flags in exchange for longer instance downtime and a temporary decrease in database performance or throughput. Your cluster returns to peak performance several minutes after force applying a flag update.

With the force apply policy enabled, updating a flag that requires a restart on your cluster's primary instance has these effects:

    * The primary instance experiences about one minute of downtime.

    * The flag on the primary instance finishes updating to its new value after one or two minutes.

Updating a flag that requires a restart on a read pool instance has these effects:

    * The read pool instance experiences about one minute of downtime.

    * The flag on the read pool instance finishes updating to its new value after one or two minutes.




## Before you begin

  * The Google Cloud project you are using must have been [enabled to access AlloyDB](https://docs.cloud.google.com/alloydb/docs/quickstart/create-and-connect#before-you-begin). 
  * You must have one of these IAM roles in the Google Cloud project you are using: 
    * `roles/alloydb.admin` (the AlloyDB Admin predefined IAM role)
    * `roles/owner` (the Owner basic IAM role)
    * `roles/editor` (the Editor basic IAM role)

If you don't have any of these roles, contact your Organization Administrator to request access.




To ensure maintenance and updates can create temporary replication slots for state synchronization, ensure that the total number of replication slots is at least one less than the `max_wal_senders` limit. For more information about configuring this flag, see [Configure your source instances](https://docs.cloud.google.com/alloydb/docs/cluster-upgrade#configure-source-instances).

### Console

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click a cluster in the **Resource Name** column.

  3. In the **Overview** page, go to **Instances in your cluster** , select an instance, and then click **Edit**.

  4. Expand **Advanced configuration options**.

  5. Add, modify, or delete a database flag from your instance:

**Add a flag**

     1. To add a database flag to your instance, click **Add flag**.
     2. Select a flag from the **New database flag** list.
     3. Provide a value for the flag.
     4. Click **Done**.

**Modify a flag**

     1. To modify a database flag present in your instance, expand the database flag and modify the value of the existing flag in the **Edit database flag** section.
     2. Click **Done**.

**Delete a flag**

     1. To delete a database flag from your instance, select a flag and click the delete icon.
     2. Click **Done**.
  6. Click **Update instance**.




### gcloud

Use the [`gcloud alloydb instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/update) command to change the database flags for an instance.

**Caution:** Running the following command overwrites all database flags that are previously set. Any database flags that are not explicitly included in the `--database-flags` list are reset to its default value. To retain your instance's database flags while adding new flags, you must include both current and new flags in the `--database-flags` list.
    
    
       gcloud alloydb instances update INSTANCE_ID \
       --database-flags FLAGS_LIST \
       --region=REGION_ID \
       --cluster=CLUSTER_ID \
       --project=PROJECT_ID

To apply flag updates more rapidly, include the argument `--update-mode=FORCE_APPLY`. Because this can temporarily decrease database performance, avoid using this option in a production environment.
    
    
       gcloud beta alloydb instances update INSTANCE_ID \
       --database-flags FLAGS_LIST \
       --region=REGION_ID \
       --cluster=CLUSTER_ID \
       --project=PROJECT_ID \
       --update-mode=FORCE_APPLY

Replace the following:

  * `INSTANCE_ID`: The ID of the instance.
  * `FLAGS_LIST`: A comma-separated list of one or more database flag specifications. Each specification consists of the name of the flag, an equals sign (=), and the value to assign to the flags. For database flags that don't take values, provide the name of the flag followed by an equals sign (=).
  * `REGION_ID`: The region where the instance is placed—for example, `us-central1`.
  * `CLUSTER_ID`: The ID of the cluster where the instance is placed.
  * `PROJECT_ID`: The ID of the project where the cluster is placed.



To see the list of an instance's current, manually-set flags, run the following command:
    
    
       gcloud alloydb instances describe INSTANCE_ID \
       --region=REGION_ID \
       --cluster=CLUSTER_ID \
       --project=PROJECT_ID

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
