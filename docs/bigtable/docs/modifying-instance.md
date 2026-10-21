---
url: https://docs.cloud.google.com/bigtable/docs/modifying-instance/
title: Modify an instance \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:29:09.339133+00:00
---

# Modify an instance  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/modifying-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Modify an instance

After you create a Bigtable instance, you can update the following settings without any downtime:

  * [Edition](https://docs.cloud.google.com/bigtable/docs/editions-overview)

You can upgrade to Enterprise Plus or downgrade to Enterprise.

  * [In-memory tier](https://docs.cloud.google.com/bigtable/docs/in-memory-overview) ([Preview](https://cloud.google.com/products#product-launch-stages))

You can enable or disable the in-memory tier for a cluster in an instance.

  * Autoscaling

You can enable or disable autoscaling for an instance's clusters or configure the settings for clusters that already have autoscaling enabled.

  * The number of nodes in manually scaled clusters

After you add or remove nodes, it typically takes a few minutes under load for Bigtable to optimize the cluster's performance.

  * The number of clusters in the instance

After you add a cluster, it takes time for Bigtable to replicate your data to the new cluster. New clusters are replicated from the geographically nearest cluster in the instance. In general, the greater the distance, the longer replication will take.

  * The application profiles for the instance, which contain [replication](https://docs.cloud.google.com/bigtable/docs/replication-overview) settings

  * The location of your data

  * The labels for the instance, which provide metadata about the instance

  * The display name for the instance




You can change a cluster ID only by deleting and recreating the cluster.

To change any of the following, you must [create a new instance](https://docs.cloud.google.com/bigtable/docs/creating-instance) with your preferred settings, [export your data](https://docs.cloud.google.com/bigtable/docs/exporting-sequence-files#bigtable) from the old instance, [import your data](https://docs.cloud.google.com/bigtable/docs/importing-sequence-files) into the new instance, and then [delete the old instance](https://docs.cloud.google.com/bigtable/docs/deleting-instance).

  * Instance ID

  * Storage type (SSD or HDD)

  * Customer-managed encryption key (CMEK) configuration




## Before you begin

If you want to use the command-line interfaces for Bigtable, [install the Google Cloud CLI](https://docs.cloud.google.com/bigtable/docs/installing-cloud-sdk) and the [ `cbt` CLI ](https://docs.cloud.google.com/bigtable/docs/cbt-overview) if you haven't already. 

## Change editions

You can change between editions by upgrading to Enterprise Plus or downgrading to Enterprise.

### Upgrade to Enterprise Plus

Once you change the edition, Bigtable automatically updates billing and you have immediate access to Enterprise Plus features.

###  Console 

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the Enterprise instance that you want to upgrade, and then click **Edit instance**.

  3. In the **Edition** section, select **Enterprise Plus**.

  4. Click **Save**.

  5. Optional: enable the in-memory tier.




###  gcloud 

Use the [`bigtable instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/update) command to change the edition:
    
    
    gcloud bigtable instances update INSTANCE_ID \
        --edition=ENTERPRISE_PLUS
    

Provide the following: 

  * `INSTANCE_ID`: The permanent identifier for the instance. 



### Downgrade to Enterprise

To downgrade from Enterprise Plus to Enterprise, you must disable features that are exclusive to Enterprise Plus. Once you change the edition, Bigtable automatically updates billing and you lose access to Enterprise Plus features.

###  Console 

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the Enterprise instance that you want to downgrade, and then click **Edit instance**.

  3. In the **Edition** section, select **Enterprise**.

  4. Click **Save**.




###  gcloud 

Use the [`bigtable instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/update) command to change the edition:
    
    
    gcloud bigtable instances update INSTANCE_ID \
        --edition=ENTERPRISE
    

Provide the following: 

  * `INSTANCE_ID`: The permanent identifier for the instance. 



## Configure the in-memory tier

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can enable, disable, or view information about the in-memory tier.

### Required roles

To get the permissions that you need to configure the in-memory tier, ask your administrator to grant you the Bigtable Admin (`roles/bigtable.admin`) Identity and Access Management (IAM) role on the instance.

This predefined role contains the permissions that Bigtable requires to work with the in-memory tier. To see the exact permissions that are required, expand the **Required permissions** section:

#### Required permissions

  * `bigtable.memoryLayer.get`
  * `bigtable.memoryLayer.list`
  * `bigtable.memoryLayer.update`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

For more information about Bigtable roles and permissions, see [Access control with IAM](https://docs.cloud.google.com/bigtable/docs/access-control).

### Enable the in-memory tier

In the Enterprise Plus edition, you can enable the in-memory tier on a cluster. To use the in-memory tier, you must use an app profile that you configured for in-memory. For more information, see [In-memory tier overview](https://docs.cloud.google.com/bigtable/docs/in-memory-overview).

###  Console 

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the Enterprise instance that you want to update, and then click **Edit instance**.

  3. Click **Edit cluster** for the cluster where you want to enable the in-memory tier.

  4. Select **Enable in-memory**.

  5. Click **Save**.




###  gcloud 

To enable the in-memory tier on a cluster, use the [`gcloud beta bigtable memory-layers update`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/bigtable/memory-layers/update) command.
    
    
    gcloud beta bigtable memory-layers update CLUSTER_ID \
        --instance=INSTANCE_ID \
        --enable
    

Provide the following: 

  * `CLUSTER_ID`: The permanent identifier for the cluster. 
  * `INSTANCE_ID`: The permanent identifier for the instance. 



### Disable the in-memory tier

Before you downgrade from Enterprise Plus to Enterprise, you must disable the in-memory tier.

###  Console 

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the Enterprise instance that you want to update, and then click **Edit instance**.

  3. Click **Edit cluster** for the cluster where you want to disable the in-memory tier.

  4. Clear **Enable in-memory**.

  5. Click **Save**.




###  gcloud 

To disable the in-memory tier on a cluster, use the [`gcloud beta bigtable memory-layers update`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/bigtable/memory-layers/update) command.
    
    
    gcloud beta bigtable memory-layers update CLUSTER_ID \
        --instance=INSTANCE_ID \
        --disable
    

Provide the following: 

  * `CLUSTER_ID`: The permanent identifier for the cluster. 
  * `INSTANCE_ID`: The permanent identifier for the instance. 



### Get a list of clusters with the in-memory tier

###  Console 

To view clusters with in-memory tier enabled on the instance overview page, follow these steps:

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the ID of the instance that has the cluster that you want to view.

  3. In the cluster table, view the **In-memory tier** column.




###  gcloud 

To list the clusters with in-memory tier enabled on an instance, use the [`gcloud beta bigtable memory-layers list`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/bigtable/memory-layers/list) command.
    
    
    gcloud beta bigtable memory-layers list \
        --instance=INSTANCE_ID
    

Provide the following: 

  * `INSTANCE_ID`: The permanent identifier for the instance. 



### View information about the in-memory tier

You can view the status and capacity of a cluster's in-memory tier.

###  Console 

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the ID of the instance that has the cluster that you want to view.

  3. In the cluster table, view the **In-memory** column of your cluster.




###  gcloud 

To view information about the in-memory tier on a cluster, such as the in-memory tier state, use the [`gcloud beta bigtable memory-layers describe`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/bigtable/memory-layers/describe) command.
    
    
    gcloud beta bigtable memory-layers describe CLUSTER_ID \
        --instance=INSTANCE_ID
    

Provide the following: 

  * `CLUSTER_ID`: The permanent identifier for the cluster. 
  * `INSTANCE_ID`: The permanent identifier for the instance. 



## Configure autoscaling

You can enable or disable autoscaling for any existing cluster. You can also change the CPU utilization target, minimum number of nodes, and maximum number of nodes for a cluster. For guidance on choosing your autoscaling settings, see [Autoscaling](https://docs.cloud.google.com/bigtable/docs/autoscaling). You are not able to use the `cbt` CLI to configure autoscaling.

### Enable autoscaling

###  Console 

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance that you want to change, then click **Edit instance**. 

  3. Under **Configure clusters** , click **Edit** edit for the cluster that you want to update.

  4. Select **Autoscaling**.

  5. Enter values for the following:

     * Minimum number of nodes
     * Maximum number of nodes
     * CPU utilization target
     * Storage utilization target
  6. Click **Save**.




###  gcloud 

  1. If you don't know the instance ID, use the [`bigtable instances list` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/list) to view a list of your project's instances: 
         
         gcloud bigtable instances list
         

  2. If you don't know the instance's cluster IDs, use the [`bigtable clusters list` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/clusters/list) to view a list of clusters in the instance: 
         
         gcloud bigtable clusters list --instances=INSTANCE_ID
         

Replace `INSTANCE_ID` with the permanent identifier for the instance. 

  3. Use the [`bigtable clusters update` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/clusters/update) to enable autoscaling:
         
         gcloud bigtable clusters update CLUSTER_ID \
             --instance=INSTANCE_ID \
             --autoscaling-max-nodes=AUTOSCALING_MAX_NODES \
             --autoscaling-min-nodes=AUTOSCALING_MIN_NODES \
             --autoscaling-cpu-target=AUTOSCALING_CPU_TARGET \
             --autoscaling-storage-target=AUTOSCALING_STORAGE_TARGET
         

Provide the following: 

     * `CLUSTER_ID`: The permanent identifier for the cluster. 
     * `INSTANCE_ID`: The permanent identifier for the instance. 
     * `AUTOSCALING_MAX_NODES`: The minimum number of nodes
     * `AUTOSCALING_MIN_NODES`: The maximum number of nodes
     * `AUTOSCALING_CPU_TARGET`: The CPU utilization target percentage that Bigtable maintains by adding or removing nodes. This value must be from 10 to 80.
     * `AUTOSCALING_STORAGE_TARGET`: The storage utilization target in GiB per node that Bigtable maintains by adding or removing nodes

In many cases, each cluster in an instance should have the same number of nodes, but there are exceptions. [Learn about nodes and replication](https://docs.cloud.google.com/bigtable/docs/instances-clusters-nodes#nodes-replication). 




### Disable autoscaling

###  Console 

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance that you want to change, then click **Edit instance**. 

  3. Under **Configure clusters** , click **edit** for the cluster that you want to update.

  4. Select **Manual node allocation**.

  5. Enter the number of nodes for the cluster in the **Quantity** field.

In many cases, each cluster in an instance should have the same number of nodes, but there are exceptions. [Learn about nodes and replication](https://docs.cloud.google.com/bigtable/docs/instances-clusters-nodes#nodes-replication). 

  6. Click **Save**.




###  gcloud 

  1. If you don't know the instance ID, use the [`bigtable instances list` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/list) to view a list of your project's instances: 
         
         gcloud bigtable instances list
         

  2. If you don't know the instance's cluster IDs, use the [`bigtable clusters list` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/clusters/list) to view a list of clusters in the instance: 
         
         gcloud bigtable clusters list --instances=INSTANCE_ID
         

Replace `INSTANCE_ID` with the permanent identifier for the instance. 

  3. Use the [`bigtable clusters update` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/clusters/update) to disable autoscaling and configure a constant number of nodes:
         
         gcloud bigtable clusters update CLUSTER_ID \
             --instance=INSTANCE_ID \
             --num-nodes=NUM_NODES --disable-autoscaling
         

Provide the following: 

     * `CLUSTER_ID`: The permanent identifier for the cluster. 
     * `INSTANCE_ID`: The permanent identifier for the instance. 
     * `NUM_NODES`: This field is optional. If no value is set, Bigtable automatically allocates nodes based on your data footprint and optimizes for 50% storage utilization. If you want to control the number of nodes in a cluster, update the `NUM_NODES` value. Ensure that number of nodes is set to a non-zero value. 

In many cases, each cluster in an instance should have the same number of nodes, but there are exceptions. [Learn about nodes and replication](https://docs.cloud.google.com/bigtable/docs/instances-clusters-nodes#nodes-replication). 




### Change autoscaling settings

###  Console 

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance that you want to change, then click **Edit instance**. 

  3. Under **Configure clusters** , click **edit** for the cluster that you want to update.

  4. Enter new values for any of the floowing that you want to change:

     * Minimum number of nodes
     * Maximum number of nodes
     * CPU utilization target
     * Storage utilization target
  5. Click **Save**.




###  gcloud 

  1. If you don't know the instance ID, use the [`bigtable instances list` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/list) to view a list of your project's instances: 
         
         gcloud bigtable instances list
         

  2. If you don't know the instance's cluster IDs, use the [`bigtable clusters list` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/clusters/list) to view a list of clusters in the instance: 
         
         gcloud bigtable clusters list --instances=INSTANCE_ID
         

Replace `INSTANCE_ID` with the permanent identifier for the instance. 

  3. Use the [`bigtable clusters update` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/clusters/update) to update the settings for autoscaling:
         
         gcloud bigtable clusters update CLUSTER_ID \
             --instance=INSTANCE_ID \
             --autoscaling-max-nodes=AUTOSCALING_MAX_NODES \
             --autoscaling-min-nodes=AUTOSCALING_MIN_NODES \
             --autoscaling-cpu-target=AUTOSCALING_CPU_TARGET \
             --autoscaling-storage-target=AUTOSCALING_STORAGE_TARGET
         

Provide the following: 

     * `CLUSTER_ID`: The permanent identifier for the cluster. 
     * `INSTANCE_ID`: The permanent identifier for the instance. 

The command accepts optional autoscaling flags. You can use all of the flags or just the flags for the values that you want to change.

     * `AUTOSCALING_MAX_NODES`: The minimum number of nodes.
     * `AUTOSCALING_MIN_NODES`: The maximum number of nodes.
     * `AUTOSCALING_CPU_TARGET`: The CPU utilization target percentage that Bigtable maintains by adding or removing nodes. This value must be from 10 to 80.
     * `AUTOSCALING_STORAGE_TARGET`: The storage utilization target in GiB per node that Bigtable maintains by adding or removing nodes.

In many cases, each cluster in an instance should have the same number of nodes, but there are exceptions. [Learn about nodes and replication](https://docs.cloud.google.com/bigtable/docs/instances-clusters-nodes#nodes-replication). 




## Add or remove nodes manually

In most cases, we recommend that you enable autoscaling. If you choose not to, and your cluster's _node scaling mode_ is **manual** , you can add or remove nodes, and the number of nodes remains constant until you change it again. To review the default node quotas per zone per Google Cloud project, see [Node quotas](https://docs.cloud.google.com/bigtable/quotas#nodes-per-project). If you need to provision more nodes than the default, you can [request more](https://docs.cloud.google.com/bigtable/quotas#quota-increase).

**Caution:** To avoid performance issues, don't reduce a cluster size by more than 10% in a 10-minute period. For details, see [Latency increases caused by scaling down too quickly](https://docs.cloud.google.com/bigtable/docs/scaling#scale-down).

To change the number of nodes in a cluster that uses manual scaling:

###  Console 

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance that you want to change, then click **Edit instance**. 

  3. Under **Configure clusters** , click **Edit** edit for the cluster that you want to update.

  4. In the **Manual node allocation** section, enter the number of nodes for the cluster in the **Quantity** field.

In many cases, each cluster in an instance should have the same number of nodes, but there are exceptions. [Learn about nodes and replication](https://docs.cloud.google.com/bigtable/docs/instances-clusters-nodes#nodes-replication). 

  5. Click **Save**.




###  gcloud 

  1. If you don't know the instance ID, use the [`bigtable instances list` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/list) to view a list of your project's instances: 
         
         gcloud bigtable instances list
         

  2. If you don't know the instance's cluster IDs, use the [`bigtable clusters list` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/clusters/list) to view a list of clusters in the instance: 
         
         gcloud bigtable clusters list --instances=INSTANCE_ID
         

Replace `INSTANCE_ID` with the permanent identifier for the instance. 

  3. Use the [`bigtable clusters update` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/clusters/update) to change the number of nodes:
         
         gcloud bigtable clusters update CLUSTER_ID \
             --instance=INSTANCE_ID \
             --num-nodes=NUM_NODES
         

Provide the following: 

     * `CLUSTER_ID`: The permanent identifier for the cluster. 
     * `INSTANCE_ID`: The permanent identifier for the instance. 
     * `NUM_NODES`: This field is optional. If no value is set, Bigtable automatically allocates nodes based on your data footprint and optimizes for 50% storage utilization. If you want to control the number of nodes in a cluster, update the `NUM_NODES` value. Ensure that number of nodes is set to a non-zero value. 

In many cases, each cluster in an instance should have the same number of nodes, but there are exceptions. [Learn about nodes and replication](https://docs.cloud.google.com/bigtable/docs/instances-clusters-nodes#nodes-replication). 




###  cbt 

  1. If you don't know the instance ID, use the `listinstances` command to view a list of your project's instances: 
         
         cbt listinstances
         

  2. If you don't know the instance's cluster IDs, use the `listclusters` command to view a list of clusters in the instance: 
         
         cbt -instance=INSTANCE_ID listclusters
         

Replace `INSTANCE_ID` with the permanent identifier for the instance. 

  3. Use the `updatecluster` command to change the number of nodes:
         
         cbt -instance=INSTANCE_ID updatecluster CLUSTER_ID NUM_NODES
         

Provide the following: 

     * `INSTANCE_ID`: The permanent identifier for the instance. 
     * `CLUSTER_ID`: The permanent identifier for the cluster. 
     * `NUM_NODES`: This field is optional. If no value is set, Bigtable automatically allocates nodes based on your data footprint and optimizes for 50% storage utilization. If you want to control the number of nodes in a cluster, update the `NUM_NODES` value. Ensure that number of nodes is set to a non-zero value. 

In many cases, each cluster in an instance should have the same number of nodes, but there are exceptions. [Learn about nodes and replication](https://docs.cloud.google.com/bigtable/docs/instances-clusters-nodes#nodes-replication). 




## Add a cluster

You can add clusters to an existing instance. An instance can have clusters in up to 8 regions where Bigtable is available. Each [zone in a region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) can contain only one cluster. The ideal locations for additional clusters depend on your use case.

If your instance is [protected by CMEK](https://docs.cloud.google.com/bigtable/docs/cmek), each new cluster must use a CMEK key that is in the same region as the cluster. Before you add a new cluster to a CMEK-protected instance, identify or [create a CMEK key](https://docs.cloud.google.com/bigtable/docs/use-cmek#create-key) in the region where you plan to locate the cluster.

Before you add clusters to a single-cluster instance, read about the restrictions that apply when you change [garbage collection policies](https://docs.cloud.google.com/bigtable/docs/garbage-collection#changes) on replicated tables. Then see [examples of replication settings](https://docs.cloud.google.com/bigtable/docs/replication-settings) for recommendations.

To add a cluster to an instance:

###  Console 

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance that you want to change, then click **Edit instance**. 

  3. Under **Configure clusters** , click **Add cluster**.

If this button is inactive, the instance already has the maximum number of clusters.

  4. Enter a cluster ID for the first cluster.

The cluster ID is a permanent identifier for the cluster.

  5. Choose the [region and zone](https://docs.cloud.google.com/bigtable/docs/locations) where the first cluster will run.

  6. Optional: To configure the cluster to always scale in increments of two nodes, select **Enable 2x node scaling**. For more information, see [Node scaling factor](https://docs.cloud.google.com/bigtable/docs/scaling#node-scaling).

  7. Choose a node scaling mode for the cluster. In most cases, you should choose autoscaling. For scaling guidance, see [Autoscaling](https://docs.cloud.google.com/bigtable/docs/autoscaling).

     1. For **Manual node allocation** , enter the number of Bigtable nodes for the first cluster. If you aren't sure how many nodes you need, use the default. You can add more nodes later. 
     2. For **Autoscaling** , enter values for the following: 
        * **Minimum** number of nodes
        * **Maximum** number of nodes
        * **CPU utilization target**
        * **Storage utilization target**
  8. Optional: To protect your instance with CMEK instead of the default Google-managed encryption, complete the following:

     1. Click **Show encryption options**.
     2. Select the radio button next to **Customer-managed encryption key (CMEK)**.
     3. Select or enter the resource name for the [CMEK key](https://docs.cloud.google.com/bigtable/docs/use-cmek) that you want to use for the cluster. You cannot add this later.
     4. If you are prompted to grant permission to the CMEK key's service account, click **Grant**. Your user account must be granted the Cloud KMS Admin role to complete this task.
     5. Click **Save**.
  9. Enter the number of nodes for the cluster.

In many cases, each cluster in an instance should have the same number of nodes, but there are exceptions. [Learn about nodes and replication](https://docs.cloud.google.com/bigtable/docs/instances-clusters-nodes#nodes-replication). 

  10. If the instance is CMEK-protected, select or enter a customer-managed key. The CMEK key must be in the same region as the cluster.

  11. Click **Add**.

  12. Repeat these steps for each additional cluster, then click **Save**. Bigtable creates the cluster and starts replicating your data to the new cluster. You may see CPU utilization increase as replication begins.

**Note:** You cannot access your data in the new cluster until Bigtable completes the initial copy to the cluster. Click **Tables** in the left pane to check whether your replicated tables are available in the new cluster.
  13. [Review the replication settings in the default app profile](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles#updating-app-profile) to see if they make sense for your [replication use case](https://docs.cloud.google.com/bigtable/docs/replication-overview#use-cases). You might need to [update the default app profile](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles#updating-app-profile) or [create custom app profiles](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles#creating-app-profile). 




###  gcloud 

  1. If you don't know the instance ID, use the [`bigtable instances list` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/list) to view a list of your project's instances: 
         
         gcloud bigtable instances list
         

  2. If you don't know the instance's cluster IDs, use the [`bigtable clusters list` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/clusters/list) to view a list of clusters in the instance: 
         
         gcloud bigtable clusters list --instances=INSTANCE_ID
         

Replace `INSTANCE_ID` with the permanent identifier for the instance. 

  3. Use the [`bigtable clusters create` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/clusters/create) to add a cluster:
         
         gcloud bigtable clusters create CLUSTER_ID \
             --async \
             --instance=INSTANCE_ID \
             --zone=ZONE \
             [--num-nodes=NUM_NODES] \
             [--autoscaling-min-nodes=AUTOSCALING_MIN_NODES, \
             --autoscaling-max-nodes=AUTOSCALING_MAX_NODES, \
             --autoscaling-cpu-target=AUTOSCALING_CPU_TARGET \
             --autoscaling-storage-target=AUTOSCALING_STORAGE_TARGET] \
             [--kms-key=KMS_KEY --kms-keyring=KMS_KEYRING \
             --kms-location=KMS_LOCATION --kms-project=KMS_PROJECT] \
         

Provide the following: 

     * `CLUSTER_ID`: The permanent identifier for the cluster. 
     * `INSTANCE_ID`: The permanent identifier for the instance. 
     * `ZONE`: The [zone](https://docs.cloud.google.com/bigtable/docs/locations) where the cluster runs. 

Each [zone in a region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) can contain only one cluster. For example, if an instance has a cluster in `us-east1-b`, you can add a cluster in a different zone in the same region, such as `us-east1-c`, or a zone in a separate region, such as `europe-west2-a`. [View the zone list](https://docs.cloud.google.com/bigtable/docs/locations). 

The `--async` flag is not required but is strongly recommended. Without this flag, the command might time out before the operation is complete. Bigtable will continue to create the cluster in the background.

The command accepts the following optional flags: 

     * `--kms-key=KMS_KEY`: The CMEK key in use by the cluster. You can add CMEK clusters only to instances that are already CMEK-protected.
     * `--kms-keyring=KMS_KEYRING`: The KMS keyring ID for the key.
     * `--kms-location=KMS_LOCATION`: The Google Cloud location for the key.
     * `--kms-project=KMS_PROJECT`: The Google Cloud project ID for the key.
     * `--storage-type=STORAGE_TYPE`: The type of storage to use for the cluster. Each cluster in an instance must use the same storage type. Accepts the values `SSD` and `HDD`. The default value is `SSD`. 
     * `--node-scaling-factor=node-scaling-factor-2x`: A flag that enables [2x node scaling](https://docs.cloud.google.com/bigtable/docs/scaling#node-scaling). You can enable this feature with both manual scaling and autoscaling.

To view a list of Bigtable zones that aren't available for 2x node scaling, see [Node scaling factor limitations](https://docs.cloud.google.com/bigtable/docs/scaling#node-scaling-limitations).

If no value is set for the `--num-nodes` option, Bigtable allocates nodes to the cluster automatically based on your data footprint and optimizes for 50% storage utilization. This automatic allocation of nodes has a pricing impact. If you want to control the number of nodes in a cluster, update the `NUM_NODES` value. Ensure that number of nodes is set to a non-zero value. In many cases, each cluster in an instance should have the same number of nodes, but there are exceptions. [Learn about nodes and replication](https://docs.cloud.google.com/bigtable/docs/instances-clusters-nodes#nodes-replication). 

For _autoscaling_ , provide all `autoscaling-` flags and don't use `num-nodes`. For guidance on choosing the values for your autoscaling settings, see [Autoscaling](https://docs.cloud.google.com/bigtable/docs/autoscaling). Replace the following:

     * `AUTOSCALING_MIN_NODES`: The minimum number of nodes for the cluster.
     * `AUTOSCALING_MAX_NODES`: The maximum number of nodes for the cluster.
     * `AUTOSCALING_CPU_TARGET`: The target CPU utilization for the cluster. This value must be from 10 to 80.
     * `AUTOSCALING_STORAGE_TARGET`: The storage utilization target in GiB that Bigtable maintains by adding or removing nodes.
  4. [Review the replication settings in the default app profile](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles#updating-app-profile) to see if they make sense for your [replication use case](https://docs.cloud.google.com/bigtable/docs/replication-overview#use-cases). You might need to [update the default app profile](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles#updating-app-profile) or [create custom app profiles](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles#creating-app-profile). 




###  cbt 

**Note:** You are not able to create CMEK-protected resources or configure autoscaling using the `cbt` CLI .

  1. If you don't know the instance ID, use the `listinstances` command to view a list of your project's instances: 
         
         cbt listinstances
         

  2. If you don't know the instance's cluster IDs, use the `listclusters` command to view a list of clusters in the instance: 
         
         cbt -instance=INSTANCE_ID listclusters
         

Replace `INSTANCE_ID` with the permanent identifier for the instance. 

  3. Use the `createcluster` command to add a cluster:
         
         cbt -instance=INSTANCE_ID \
         createcluster CLUSTER_ID \
         ZONE \
         NUM_NODES \
         STORAGE_TYPE
         
         

Provide the following: 

     * `INSTANCE_ID`: The permanent identifier for the instance. 
     * `CLUSTER_ID`: The permanent identifier for the cluster. 
     * `ZONE`: The [zone](https://docs.cloud.google.com/bigtable/docs/locations) where the cluster runs. 

Each [zone in a region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) can contain only one cluster. For example, if an instance has a cluster in `us-east1-b`, you can add a cluster in a different zone in the same region, such as `us-east1-c`, or a zone in a separate region, such as `europe-west2-a`. [View the zone list](https://docs.cloud.google.com/bigtable/docs/locations). 

     * `NUM_NODES`: This field is optional. If no value is set, Bigtable automatically allocates nodes based on your data footprint and optimizes for 50% storage utilization. If you want to control the number of nodes in a cluster, update the `NUM_NODES` value. Ensure that number of nodes is set to a non-zero value. 

In many cases, each cluster in an instance should have the same number of nodes, but there are exceptions. [Learn about nodes and replication](https://docs.cloud.google.com/bigtable/docs/instances-clusters-nodes#nodes-replication). 

     * `STORAGE_TYPE`: The type of storage to use for the cluster. Each cluster in an instance must use the same storage type. Accepts the values `SSD` and `HDD`. 

  4. [Review the replication settings in the default app profile](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles#updating-app-profile) to see if they make sense for your [replication use case](https://docs.cloud.google.com/bigtable/docs/replication-overview#use-cases). You might need to [update the default app profile](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles#updating-app-profile) or [create custom app profiles](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles#creating-app-profile). 




## Delete a cluster

If an instance has multiple clusters, you can delete all but 1 of the clusters. Deleting all but 1 cluster automatically disables replication.

**Note:** If you delete a cluster, and some writes to that cluster have not been replicated yet, Bigtable finishes the replication process before it removes the deleted cluster's copy of your data. The remaining cluster continues to show incoming writes and CPU utilization until the replication process is complete.

Bigtable doesn't let you delete a cluster in the following cases:

  * If one of your [application profiles](https://docs.cloud.google.com/bigtable/docs/app-profiles) routes all traffic to a single cluster. You must [edit or delete the application profile](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles) before you can remove the cluster.
  * If you add new clusters to an existing instance, you can't delete clusters in that instance until the initial data copy to the new clusters is complete.
  * If a cluster contains one or more backups. To delete the cluster, you must delete those backups or wait for them to expire.
  * If a cluster is configured as a location in a table's automated backup policy. To delete the cluster, you must first [update the automated backup policy](https://docs.cloud.google.com/bigtable/docs/managing-backups#automated-backup-cluster-locations).



To delete a cluster from an instance:

###  Console 

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance that you want to change, then click **Edit instance**. 

  3. Under **Configure clusters** , click **Delete cluster** delete for the cluster that you want to delete.

  4. To cancel the delete operation, click **Undo** , which is available until you click **Save**. Otherwise, click **Save**.




###  gcloud 

  1. If you don't know the instance ID, use the [`bigtable instances list` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/list) to view a list of your project's instances: 
         
         gcloud bigtable instances list
         

  2. If you don't know the instance's cluster IDs, use the [`bigtable clusters list` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/clusters/list) to view a list of clusters in the instance: 
         
         gcloud bigtable clusters list --instances=INSTANCE_ID
         

Replace `INSTANCE_ID` with the permanent identifier for the instance. 

  3. Use the [`bigtable clusters delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/clusters/delete) to delete the cluster:
         
         gcloud bigtable clusters delete CLUSTER_ID \
             --instance=INSTANCE_ID
         

Provide the following: 

     * `CLUSTER_ID`: The permanent identifier for the cluster. 
     * `INSTANCE_ID`: The permanent identifier for the instance. 



###  cbt 

  1. If you don't know the instance ID, use the `listinstances` command to view a list of your project's instances: 
         
         cbt listinstances
         

  2. If you don't know the instance's cluster IDs, use the `listclusters` command to view a list of clusters in the instance: 
         
         cbt -instance=INSTANCE_ID listclusters
         

Replace `INSTANCE_ID` with the permanent identifier for the instance. 

  3. Use the `deletecluster` command to delete the cluster:
         
         cbt -instance=INSTANCE_ID deletecluster CLUSTER_ID
         

Provide the following: 

     * `INSTANCE_ID`: The permanent identifier for the instance. 
     * `CLUSTER_ID`: The permanent identifier for the cluster. 



## Move data to a new location

To move the data in a Bigtable instance to a new zone or region, add a new cluster in the location that you want to move to, and then delete the cluster in the location you want to move from. The deleted cluster remains available until data has been replicated to the new cluster, so you don't have to worry about any requests failing. Bigtable replicates all data to the new cluster automatically.

## Manage app profiles

Application profiles, or _app profiles_ , control how your applications connect to an instance that uses replication. Every instance with more than 1 cluster has its own default app profile. You can also create many different custom app profiles for each instance, using a different app profile for each kind of application that you run.

To learn how to set up an instance's app profiles, see [Configuring App Profiles](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles). For examples of settings you can use to implement common use cases, see [Examples of replication configurations](https://docs.cloud.google.com/bigtable/docs/replication-settings). 

## Manage labels

Labels are key-value pairs that you can use to group related instances and store metadata about an instance.

To learn how to manage labels, see [Adding or updating an instance's labels](https://docs.cloud.google.com/bigtable/docs/creating-managing-labels#adding-updating-labels) and [Removing a label from an instance](https://docs.cloud.google.com/bigtable/docs/creating-managing-labels#removing-labels).

## Change an instance's display name

To change an instance's display name, which the Google Cloud console uses to identify the instance:

###  Console 

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance that you want to change, then click **Edit instance**. 

  3. Edit the instance name, then click **Save**.




###  gcloud 

  1. If you don't know the instance ID, use the [`bigtable instances list` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/list) to view a list of your project's instances: 
         
         gcloud bigtable instances list
         

  2. Use the [`bigtable instances update` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/update) to update the display name:
         
         gcloud bigtable instances update INSTANCE_ID \
             --display-name=DISPLAY_NAME
         

Provide the following: 

     * `INSTANCE_ID`: The permanent identifier for the instance. 
     * `DISPLAY_NAME`: A human-readable name that identifies the instance in the Google Cloud console. 



###  cbt 

This feature is not available in the `cbt` CLI. 

## What's next

  * Learn how to [add, update, and remove labels for an instance](https://docs.cloud.google.com/bigtable/docs/creating-managing-labels).
  * Find out how to [create and update an instance's app profiles](https://docs.cloud.google.com/bigtable/docs/configuring-app-profiles), which contain settings for replication.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
