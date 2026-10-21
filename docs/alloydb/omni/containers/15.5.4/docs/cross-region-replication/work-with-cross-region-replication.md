---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/cross-region-replication/work-with-cross-region-replication/
title: Work with cross-region replication \u00a0|\u00a0 AlloyDB Omni for containers: 15.5.4 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:22:44.383876+00:00
---

# Work with cross-region replication  |  AlloyDB Omni for containers: 15.5.4  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/cross-region-replication/work-with-cross-region-replication/

This page documents AlloyDB Omni version **15.5.4** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/overview)



Send feedback 

#  Work with cross-region replication Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.5.4keyboard_arrow_down

  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/cross-region-replication/work-with-cross-region-replication)

This page describes how to use cross-region replication by creating and working with secondary clusters. 

For a conceptual overview of cross-region replication, see [About cross-region replication](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/cross-region-replication/about-cross-region-replication).

## Before you begin

  * The Google Cloud project you are using must have been [enabled to access AlloyDB Omni](https://docs.cloud.google.com/alloydb/docs/project-enable-access). 
  * You must have one of these IAM roles in the Google Cloud project you are using: 
    * `roles/alloydb.admin` (the AlloyDB Admin predefined IAM role)
    * `roles/owner` (the Owner basic IAM role)
    * `roles/editor` (the Editor basic IAM role)

If you don't have any of these roles, contact your Organization Administrator to request access.




## Create a secondary cluster

When you create a secondary cluster, AlloyDB copies and applies some of the primary cluster configuration, including point-in-time recovery (PITR) and backup configuration, onto the secondary cluster. AlloyDB does not add any read pool instances to the secondary cluster after creating it, no matter how many read pool instances exist on the primary cluster.

If you update the primary cluster configuration after you create the secondary cluster, the changes are not available on the secondary cluster. However, you can manually update the secondary cluster to have the latest configuration that's available in the primary cluster.

To create an AlloyDB secondary cluster and secondary instance, follow these steps:

### Console

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click a cluster in the **Resource Name** column.

  3. In the **Overview** page, click **Create secondary cluster**.

  4. Configure your secondary cluster:

     1. In the **Cluster ID** field, enter a resource ID for your secondary cluster.
     2. Select a region for your secondary cluster that is different from the primary cluster region.
     3. Select the default Google-managed encryption or a customer-managed key (CMEK) as an encryption method to encrypt your secondary cluster.

If you want to encrypt this cluster using [CMEK](https://docs.cloud.google.com/alloydb/docs/cmek) key, follow these steps:

     1. Click **Advanced encryption options**.
     2. Select **Customer-managed encryption key (CMEK)**.
     3. Select a customer-managed key from the menu that appears.

The Google Cloud console limits this list to keys within the same Google Cloud project and region as the new cluster.

To use a key that is not on this list, follow these steps:

        1. Click **Don't see your key? Enter key resource name**.
        2. Enter the resource name in the **Key resource name** field.
        3. Click **Save**.
        4. Click **Continue**.

Using CMEK key with AlloyDB requires some additional setup. For more information, see [Use CMEK](https://docs.cloud.google.com/alloydb/docs/use-cmek).

If the associated primary instance is encrypted with a CMEK key, you must also encrypt its secondary cluster with a CMEK key.

  5. Configure your secondary instance:

     1. In the **Instance ID** field, enter a resource ID for your secondary instance. The resource ID must be unique within a cluster.
  6. Click **Create cluster**.




### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/starting-cloud-shell).

Use the [`gcloud alloydb clusters create-secondary`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/clusters/create-secondary) command:
    
    
     gcloud alloydb clusters create-secondary SECONDARY_CLUSTER_ID \
     --region=REGION_ID \
     --primary-cluster=projects/PROJECT_ID/locations/LOCATION_ID/clusters/ PRIMARY_CLUSTER_ID \
     gcloud alloydb instances create-secondary SECONDARY_INSTANCE_ID \
     --cluster=SECONDARY_CLUSTER_ID \
     --region=REGION_ID

Replace the following:

  * `SECONDARY_CLUSTER_ID`: The ID of the secondary cluster that you want to create.
  * `SECONDARY_INSTANCE_ID`: The ID of the secondary instance that you want to create.
  * `REGION_ID`: The ID of the secondary cluster's region—for example, `us-central1`.
  * `PROJECT_ID`: The ID of the secondary cluster's project.
  * `LOCATION_ID`: The location where your primary cluster is located—for example, `us-central1`.
  * `PRIMARY_CLUSTER_ID`: The ID of the primary cluster that the secondary cluster is associated with.
  * `SECONDARY_CLUSTER_ID`: The ID of the secondary cluster that the secondary instance is associated with.
  * `ALLOWED_PROJECT` (Optional): The comma separated list of project IDs or [project numbers](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) that you want to allow access to the instance—for example, `my-project-1`, `12345`,`my-project-n`. You must set a list of allowed projects or numbers, if your cluster is using Private Service Connect as the method of connecting to the instance.



To create a Private Service Connect-enabled secondary cluster and instance, add the `--enable-private-service-connect` flag when you create a cluster and add the `--allowed-psc-projects` flag to set a comma separated list of project IDs or [project numbers](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) that you want to allow access to the instance—for example, `my-project-1`, `12345`,`my-project-n`.
    
    
     gcloud alloydb clusters create-secondary SECONDARY_CLUSTER_ID \
     --region=REGION_ID \
     --primary-cluster=projects/PROJECT_ID/locations/LOCATION_ID/clusters/ PRIMARY_CLUSTER_ID \
     --enable-private-service-connect
     gcloud alloydb instances create-secondary SECONDARY_INSTANCE_ID \
     --cluster=SECONDARY_CLUSTER_ID \
     --region=REGION_ID \
     --allowed-psc-projects=ALLOWED_PROJECT_LIST

Replace the following:

  * `ALLOWED_PROJECT` (Optional): The comma separated list of project IDs or project numbers that you want to allow access to the instance—for example,`my-project-1`, `12345`,`my-project-n`. You must set a list of allowed projects or numbers, if your cluster is using Private Service Connect as the method of connecting to the instance.



## View a secondary cluster

To view detailed information about an AlloyDB secondary cluster, follow these steps:

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click a secondary cluster in the **Resource Name** column.

  3. In the **Overview** page, view all details about your secondary cluster.




## Update a secondary instance

You can update a secondary instance to add, modify, or delete database flags. You can also scale your secondary instance's machine type.

### Configure database flags on a secondary instance

To add, modify, or delete database flags, complete the following steps:

### Console

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. In the **Resource Name** column, click a secondary cluster that you want to modify.

  3. In the **Overview** page, go to **Instances in your cluster** , select the secondary instance, and then click **Edit secondary**.

  4. Add, modify, or delete a database flag from your instance:

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
  5. Click **Update secondary**.




### gcloud

Use the [`gcloud alloydb instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/update) command to change the database flags for a secondary instance.

**Caution:** Running the following command overwrites all database flags that are previously set. Any database flags that are not explicitly included in the `--database-flags` list are reset to its default value. To retain your instance's database flags while adding new flags, you must include both current and new flags in the `--database-flags` list.
    
    
     gcloud alloydb instances update SECONDARY_INSTANCE_ID \
      --database-flags FLAGS_LIST \
      --region=REGION_ID \
      --cluster=CLUSTER_ID \
      --project=PROJECT_ID

Replace the following:

  * `SECONDARY_INSTANCE_ID`: The ID of the secondary instance.
  * `FLAGS_LIST`: A comma-separated list of one or more database flag specifications. Each specification consists of the name of the flag, an equals sign (`=`), and the value to assign to the flags. For database flags that do not take values, provide the name of the flag followed by an equals sign (`=`).
  * `REGION_ID`: The region where the secondary instance is placed—for example, `us-central1`.
  * `CLUSTER_ID`: The ID of the cluster where the secondary instance is placed.
  * `PROJECT_ID`: The ID of the project where the secondary cluster is placed.



### Scale your secondary instance's machine type

To scale your secondary instance's machine type, complete the following steps:

### Console

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. In the **Resource Name** column, click a secondary cluster that you want to modify.

  3. In the **Overview** page, go to the **Instances in your cluster** section, and click **Edit secondary**.

Note that this action is not available if the page reports a cluster **Status** of **Maintenance**. The action becomes available again after **Status** changes to **Ready**.

  4. Select a machine type.

  5. Click **Update secondary**.




### gcloud

Use the [`gcloud alloydb instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/update) command to change the machine type of the secondary instance.
    
    
     gcloud alloydb instances update SECONDARY_INSTANCE_ID \
      --cpu-count=CPU_COUNT \
      --region=REGION_ID \
      --cluster=CLUSTER_ID \
      --project=PROJECT_ID

Replace the following:

  * `SECONDARY_INSTANCE_ID`: The ID of the secondary instance that you are updating.
  * `CPU_COUNT`: The number of vCPUs you want for the instance. Valid values include:

    * `2` (2 vCPUs, 16 GB RAM)
    * `4` (4 vCPUs, 32 GB RAM)
    * `8` (8 vCPUs, 64 GB RAM)
    * `16` (16 vCPUs, 128 GB RAM)
    * `32` (32 vCPUs, 256 GB RAM)
    * `64` (64 vCPUs, 512 GB RAM)
  * REGION_ID: The region where the instance is placed.

  * CLUSTER_ID: The ID of the cluster where the instance is placed.

  * PROJECT_ID: The ID of the project where the cluster is placed.




If the command returns an error message that includes the phrase `invalid cluster state MAINTENANCE`, then the cluster is undergoing routine maintenance. This temporarily disallows instance reconfiguration. Run the command again after the cluster returns to a `READY` state.

To check the cluster's status, see [View cluster details](https://docs.cloud.google.com/alloydb/docs/cluster-view).

## Add read pool instances to a secondary cluster

To add a read pool instance to a secondary cluster, follow these steps:

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. In the **Resource Name** column, click a secondary cluster to which you want to add a read pool instance.

  3. In the **Overview** page, go to the **Instances in your cluster** section, and click **Add read pool**.

  4. Configure your read pool instance:

     1. In the **Read pool instance ID** field, enter an ID for the read pool instance.
     2. In the **Node count** field, enter a node count. The number of nodes in a read pool instance determines the instance's overall computing capacity. You can have a maximum of 20 nodes across all the read pool instances in a cluster.
     3. Select a machine type.
     4. Optional: Set custom flags to your instance. For each flag, do the following:

        1. Click **Add flag**.
        2. Select a flag from the **New database flag** list.
        3. Provide a value for the flag.
        4. Click **Done**.
  5. Click **Add read pool**.




## Promote a secondary cluster

Before you promote a secondary cluster, perform the following steps to verify that the secondary cluster has applied all transactions received from the primary cluster:

  1. Stop all writes to the primary cluster.
  2. Check the replication status of the secondary cluster by completing the following steps:

     1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

     2. In the list of clusters, click the name of the secondary cluster that you want to promote.

     3. On the cluster detail page, click **Monitoring**.

     4. In the **Monitoring** list, select the secondary instance. It appears in the list as **Secondary: INSTANCE_NAME**.

     5. In the list of metrics, locate the **Replication lag from primary instance** chart.

     6. Confirm that the chart shows minimal lag.

A lag value of `0` is ideal. If the lag is greater than `0`, then you can still promote the secondary cluster, at the risk of losing some recent transactions already committed at the primary cluster.

     7. In the list of metrics, locate the **Replication status** chart.

     8. Confirm that all nodes represented in the chart have a value of `streaming`.




To promote a secondary cluster to primary cluster, follow these steps:

### Console

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. In the **Resource Name** column, click a secondary cluster that you want to promote as the primary cluster.

  3. In the **Overview** page, click **Promote cluster**.

  4. In the dialog that appears, enter your secondary cluster ID to confirm that you want to promote the cluster.

  5. Click **Promote**.

After the cluster is promoted, the **Type: Secondary cluster (highly available)** field on the **Overview** page is updated to **Type: Highly available with read pools**.




### gcloud

Use the [`gcloud alloydb clusters promote`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/clusters/promote) command:
    
    
     gcloud alloydb clusters promote SECONDARY_CLUSTER_ID \
     --region=REGION_ID \
     --project=PROJECT_ID \

Replace the following:

  * `SECONDARY_CLUSTER_ID`: The ID of the secondary cluster that you want to promote.
  * `REGION_ID`: The ID of the secondary cluster's region—for example,`us-central1`.
  * `PROJECT_ID`: The ID of the secondary cluster's project.



## Perform a switchover

Before you perform a switchover, verify that both regions that the primary and the secondary instances belong to are online and that the instances are in a healthy state. For more information, see [Monitor an instance using the AlloyDB System Insights dashboard](https://docs.cloud.google.com/alloydb/docs/monitor-instance#monitoring).

Use the [`gcloud alloydb clusters switchover`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/clusters/switchover) command:
    
    
       gcloud alloydb clusters switchover SECONDARY_CLUSTER_ID \
       --region=REGION_ID \
       --project=PROJECT_ID \

Replace the following:

  * `SECONDARY_CLUSTER_ID`: The ID of the secondary cluster that you want to promote.
  * `REGION_ID`: The ID of the secondary cluster's region—for example, `us-central1`.
  * `PROJECT_ID`: The ID of the secondary cluster's project.



## What's Next

  * [View cluster details.](https://docs.cloud.google.com/alloydb/docs/cluster-view)
  * [View the list of clusters.](https://docs.cloud.google.com/alloydb/docs/cluster-list)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
