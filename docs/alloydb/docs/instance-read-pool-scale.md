---
url: https://docs.cloud.google.com/alloydb/docs/instance-read-pool-scale/
title: Scale an instance \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:42:51.609266+00:00
---

# Scale an instance  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/instance-read-pool-scale/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Scale an instance Stay organized with collections  Save and categorize content based on your preferences. 

You can scale an AlloyDB instance to adjust the capacity and performance of your cluster to meet changing workload demands. Scaling helps manage costs and facilitate handling traffic spikes.

You scale vertically (modifying vCPU and RAM) by changing the machine type of a primary instance or read pool instance. You scale horizontally by changing the number of nodes in a read pool instance. You can manage both vertical and horizontal scaling using manual processes. You can also manage horizontal scaling automatically by enabling read pool autoscaling.

You can scale AlloyDB instances in the following ways.

Scaling type | Method | Automation | Primary instances | Read pool instances  
---|---|---|---|---  
Vertical | Changing machine type | Manual | Supported | Supported  
Horizontal | Changing node count | Manual and automatic | Not supported | Supported  
  
## Before you begin

  * The Google Cloud project you are using must have been [enabled to access AlloyDB](https://docs.cloud.google.com/alloydb/docs/quickstart/create-and-connect#before-you-begin). 
  * You must have one of these IAM roles in the Google Cloud project you are using: 
    * `roles/alloydb.admin` (the AlloyDB Admin predefined IAM role)
    * `roles/owner` (the Owner basic IAM role)
    * `roles/editor` (the Editor basic IAM role)

If you don't have any of these roles, contact your Organization Administrator to request access.




## Manually scale an instance

This section describes manual methods for scaling your AlloyDB instances. For example, you can vertically scale an instance by changing its machine type and horizontally scale a read pool instance by changing its node count.

### Scale an instance's machine type

You can vertically scale both primary and read pool instances by changing the instance's machine type, which modifies its vCPU and RAM.

### Console

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click a cluster in the **Resource Name** column.

  3. On the **Overview** page, go to the **Instances in your cluster** section, and click **Edit primary** or **Edit read pool**.

**Note:** This action is not available if the page reports a cluster **Status** of **Maintenance**. The action becomes available again after **Status** changes to **Ready**.
  4. Select one of the following machine series:

     * C4A (Google Axion-based machine series)
     * N2 (x86-based machine series). This is the default machine series.
     * C4 (x86-based machine series)
     * Z3 (Intel Xeon-based machine series)
  5. Select a machine type.

     * C4A supports 1, 2, 4, 8, 16, 32, 48, 64, and 72 vCPUs.
     * N2 supports 2, 4, 8, 16, 32, 64, 96, and 128 vCPUs.
     * C4 supports 4, 8, 16, 24, 32, 48, 96, 144, 192, and 288 vCPUs.
     * Z3 supports 8, 14, 16, 22, 32, 44, and 88 vCPUs.

For more information about using the C4A Axion-based machine series, including the 1 vCPU machine type, see [Considerations when using the C4A Axion-based machine series](https://docs.cloud.google.com/alloydb/docs/cluster-create#considerations-c4a).

  6. Click **Update instance** or **Update read pool**.




### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

Use the [`gcloud alloydb instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/update) command to change the machine type of the primary instance.
    
    
    gcloud alloydb instances update INSTANCE_ID \
         --cpu-count=CPU_COUNT \
         --machine-type=MACHINE_TYPE \
         --region=REGION_ID \
         --cluster=CLUSTER_ID \
         --project=PROJECT_ID

Replace the following:

  * `INSTANCE_ID`: The ID of the instance that you are updating.

  * `CPU_COUNT`: The number of N2 vCPUs that you want for the instance. N2 is the default. Valid values include the following: 

    * `2`: 2 vCPUs, 16 GB RAM
    * `4`: 4 vCPUs, 32 GB RAM
    * `8`: 8 vCPUs, 64 GB RAM
    * `16`: 16 vCPUs, 128 GB RAM
    * `32`: 32 vCPUs, 256 GB RAM
    * `64`: 64 vCPUs, 512 GB RAM
    * `96`: 96 vCPUs, 768 GB RAM
    * `128`: 128 vCPUs, 864 GB RAM
  * `MACHINE_TYPE`: Optional. Select from a list of supported machine-types such as `n2-highmem-4`, `c4-highmem-4-lssd`, or `c4a-highmem-4-lssd`. For more information, see [Choose an AlloyDB machine type.](https://docs.cloud.google.com/alloydb/docs/choose-machine-type)

When you use `MACHINE_TYPE` and `CPU_COUNT` together, the values in `CPU_COUNT` and `MACHINE_TYPE` must match, otherwise you get an error.

**Note:** When you use N2 deployments, you can choose to use only the `CPU_COUNT` parameter.
  * `REGION_ID`: The region where the instance is placed.

  * `CLUSTER_ID`: The ID of the cluster where the instance is placed.

  * `PROJECT_ID`: The ID of the project where the cluster is placed.




If the command returns an error message that includes the phrase `invalid cluster state MAINTENANCE`, then the cluster is undergoing routine maintenance. This temporarily disallows instance reconfiguration. Run the command again after the cluster returns to a `READY` state. To check on the cluster's status, see [View cluster details](https://docs.cloud.google.com/alloydb/docs/cluster-view).

#### Accelerate machine type updates

To update the machine type faster, use the `FORCE_APPLY` option with the `gcloud beta alloydb instances update` command.

**Note:** This approach is best suited for development environments because it lets you change the machine type more quickly, but it can result in longer instance downtime.
    
    
     gcloud beta alloydb instances update INSTANCE_ID \
      --cpu-count=CPU_COUNT \
      --machine-type=MACHINE_TYPE \
      --region=REGION_ID \
      --cluster=CLUSTER_ID \
      --project=PROJECT_ID \
      --update-mode=FORCE_APPLY

  * The instance experiences approximately one minute of downtime.

  * The machine type of an instance changes after 10 to 15 minutes.




###  Terraform 

**Warning:** To keep your Terraform state consistent, update configurations directly in your Terraform files. If you make manual changes using the Google Cloud console, gcloud CLI, or REST API, the following issues can occur: 

  * API errors
  * Perpetual diffs
  * Overwritten changes during `terraform apply`



To change the machine type of an instance, update the `machine_config` block in the [`google_alloydb_instance` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/alloydb_instance).
    
    
    resource "google_alloydb_instance" "default" {
      cluster       = google_alloydb_cluster.default.name
      instance_id   = "alloydb-instance"
      instance_type = "PRIMARY" # or "READ_POOL"
    
      machine_config {
        cpu_count = 4
      }
    }
    

### Scale the node count of a read pool instance

AlloyDB lets you scale the number of nodes in a read pool instance without any downtime at the instance level. When you increase the node count, client connections remain unaffected.

When you decrease the node count, any clients connected to a node that's being shut down can reconnect to the other nodes using the instance endpoint.

### Console

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click a cluster in the **Resource Name** column.

  3. On the **Overview** page, go to the **Instances in your cluster** section, and click **Edit read pool**.

**Note:** This action is not available if the page reports a cluster **Status** of **Maintenance**. The action becomes available again after **Status** changes to **Ready**.
  4. In the **Node count** field, enter a node count.

**Note:** You can have a maximum of 20 nodes across all the read pool instances in a cluster.
  5. Click **Update read pool**.




### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

Use the [`gcloud alloydb instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/update) command to change the number of nodes in a read pool instance.
    
    
    gcloud alloydb instances update INSTANCE_ID \
        --read-pool-node-count=NODE_COUNT \
        --region=REGION_ID \
        --cluster=CLUSTER_ID \
        --project=PROJECT_ID

  * `INSTANCE_ID`: the ID of the read pool instance.

  * `NODE_COUNT`: the number of nodes in the read pool instance. Specify a number `1` through `20`, inclusive. Note that you cannot have more than 20 nodes across all read pool instances in a cluster.

  * `REGION_ID`: the region where the instance is located.

  * `CLUSTER_ID`: the ID of the cluster where the instance is located.

  * `PROJECT_ID`: the ID of the project where the cluster is located.




If the command returns an error message that includes the phrase `invalid cluster state MAINTENANCE`, then the cluster is undergoing routine maintenance. This temporarily disallows instance reconfiguration. Run the command again after the cluster returns to a `READY` state. To check on the cluster's status, see [View cluster details](https://docs.cloud.google.com/alloydb/docs/cluster-view).

###  Terraform 

**Warning:** To keep your Terraform state consistent, update configurations directly in your Terraform files. If you make manual changes using the Google Cloud console, gcloud CLI, or REST API, the following issues can occur: 

  * API errors
  * Perpetual diffs
  * Overwritten changes during `terraform apply`



To change the number of nodes in a read pool instance, update the `node_count` field in the `read_pool_config` block of the [`google_alloydb_instance` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/alloydb_instance).
    
    
    resource "google_alloydb_instance" "default" {
      cluster       = google_alloydb_cluster.default.name
      instance_id   = "alloydb-read-pool-instance"
      instance_type = "READ_POOL"
    
      read_pool_config {
        node_count = 3
      }
    }
    

## Configure read pool autoscaling

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

AlloyDB read pool autoscaling lets you automatically and adaptively change the number of read nodes based on real-time resource usage. This helps you handle usage changes and decrease expenses.

You can configure autoscaling using the following policies:

  * CPU-utilization-based: scales the number of nodes based on a target CPU utilization.
  * Schedule-based: scales the number of nodes to a minimum count during a specified time window.



You can use these policies together. When multiple policies are active, the autoscaler selects the one that recommends the highest number of nodes.

### Limitations

The read pool autoscaler has the following limitations:

  * Load distribution for long-lived connections: to establish an even distribution of traffic and to fully use the added capacity from autoscaling, we recommend that you create new client connections. The autoscaler doesn't close existing long-lived connections when it adds new nodes, so traffic from those connections isn't routed to the newly added nodes.
  * Cache warming for new nodes: when the autoscaler adds new nodes, it might take a few minutes for them to warm their caches and reach peak query performance.



### Enable read pool autoscaling on a new read pool instance

You can enable and can configure automatic scaling when you create a read pool instance using a CPU-based policy, a schedule-based policy, or both.

#### Create a read pool instance with a CPU-based policy

To create a read pool instance with an automatic scaling policy based on a target CPU utilization, run the following command:
    
    
    gcloud beta alloydb instances create INSTANCE_ID \
        --instance-type=READ_POOL \
        --read-pool-node-count=NODE_COUNT \
        --region=REGION_ID \
        --cluster=CLUSTER_ID \
        --project=PROJECT_ID \
        --enable-autoscaler \
        --autoscaler-max-node-count=MAX_NODE_COUNT \
        --autoscaler-cool-down-period-seconds=COOLDOWN_PERIOD \
        --autoscaler-target-cpu-usage=TARGET_CPU_USAGE \
        {--cpu-count=CPU_COUNT | --machine-type=MACHINE_TYPE}

Replace the following:

  * `INSTANCE_ID`: the ID of the read pool instance.

  * `NODE_COUNT`: the minimum number of nodes that the autoscaler can create in the read pool instance. Specify a number `1` through `20`, inclusive. You can't have more than 20 nodes across all read pool instances in a cluster.

  * `REGION_ID`: the region where the instance is placed.

  * `CLUSTER_ID`: the ID of the cluster where the instance is placed.

  * `PROJECT_ID`: the ID of the project where the cluster is placed.

  * `MAX_NODE_COUNT`: the maximum number of nodes that the autoscaler can create in the read pool instance. The total number of nodes across all read pool instances in a single cluster cannot exceed 20.

  * `COOLDOWN_PERIOD`: the amount of time in seconds that AlloyDB waits before factoring the read pool instance's resource usage into the autoscaling algorithm. The default value is `300` seconds.

  * `TARGET_CPU_USAGE`: the target CPU utilization for your read pool instance, expressed as a decimal value between 0.0 and 1.0. For example, 0.7 for 70%.

  * `CPU_COUNT`: The number of N2 vCPUs that you want for the instance. Either `--cpu-count` or `--machine-type` must be specified.

  * `MACHINE_TYPE`: select from a list of supported machine-types such as `n2-highmem-4`, `c4-highmem-4-lssd`, or `c4a-highmem-4-lssd`. For more information, see [Choose an AlloyDB machine type](https://docs.cloud.google.com/alloydb/docs/choose-machine-type).




#### Create a read pool instance with a schedule-based policy

To create a read pool instance with a schedule-based automatic scaling policy that defines a minimum number of nodes for a specific time window, run the following command:

**Note:** If you have an existing autoscaling policy that has `--autoscaler-max-node-count` set, then this becomes an optional field.
    
    
    gcloud beta alloydb instances create INSTANCE_ID \
        --instance-type=READ_POOL \
        --read-pool-node-count=NODE_COUNT \
        --region=REGION_ID \
        --cluster=CLUSTER_ID \
        --project=PROJECT_ID \
        --enable-autoscaler \
        --autoscaler-max-node-count=MAX_NODE_COUNT \
        --autoscaler-cool-down-period-seconds=COOLDOWN_PERIOD \
        --autoscaler-set-schedule=SCHEDULE_NAME \
        --autoscaler-schedule-cron-exp=CRON_EXPRESSION \
        --autoscaler-schedule-duration-seconds=DURATION_SECONDS \
        --autoscaler-schedule-time-zone=TIME_ZONE \
        --autoscaler-schedule-min-node-count=MIN_NODE_COUNT \
        --autoscaler-schedule-description="DESCRIPTION" \
        {--cpu-count=CPU_COUNT | --machine-type=MACHINE_TYPE}

Replace the following:

  * `MAX_NODE_COUNT`: the maximum number of nodes that the autoscaler can create in the read pool instance. The total number of nodes across all read pool instances in a single cluster cannot exceed 20.

  * `COOLDOWN_PERIOD`: amount of time in seconds that AlloyDB waits before factoring the read pool instance's resource usage into the autoscaling algorithm. The default value is `300` seconds.

  * `SCHEDULE_NAME`: a unique name for the scaling schedule.

  * `CRON_EXPRESSION`: the schedule in [cron](https://en.wikipedia.org/wiki/Cron#Overview) format that specifies the start time of the scaling event.

  * `DURATION_SECONDS`: the duration in seconds for which the schedule remains active after it starts. After this period, the instance scales down to the number of nodes determined by other policies or its original configuration.

  * `TIME_ZONE`: an optional time zone for the schedule. For example, `America/Los_Angeles`.

  * `MIN_NODE_COUNT`: the minimum number of nodes to which the autoscaler scales the read pool instance while the schedule is active.

  * `DESCRIPTION`: an optional text description for the schedule.

  * `CPU_COUNT`: The number of N2 vCPUs that you want for the instance. Either `--cpu-count` or `--machine-type` must be specified.

  * `MACHINE_TYPE`: select from a list of supported machine-types such as `n2-highmem-4`, `c4-highmem-4-lssd`, or `c4a-highmem-4-lssd`. For more information, see [Choose an AlloyDB machine type](https://docs.cloud.google.com/alloydb/docs/choose-machine-type).




#### Create a read pool instance with CPU and schedule-based policies

To create a read pool instance with both CPU-based and schedule-based automatic scaling policies, run the following command:
    
    
    gcloud beta alloydb instances create INSTANCE_ID \
        --instance-type=READ_POOL \
        --read-pool-node-count=NODE_COUNT \
        --region=REGION_ID \
        --cluster=CLUSTER_ID \
        --project=PROJECT_ID \
        --enable-autoscaler \
        --autoscaler-max-node-count=MAX_NODE_COUNT \
        --autoscaler-cool-down-period-seconds=COOLDOWN_PERIOD \
        --autoscaler-target-cpu-usage=TARGET_CPU_USAGE \
        --autoscaler-set-schedule=SCHEDULE_NAME \
        --autoscaler-schedule-cron-exp=CRON_EXPRESSION \
        --autoscaler-schedule-duration-seconds=DURATION_SECONDS \
        --autoscaler-schedule-time-zone=TIME_ZONE \
        --autoscaler-schedule-min-node-count=MIN_NODE_COUNT \
        --autoscaler-schedule-description="DESCRIPTION" \
        {--cpu-count=CPU_COUNT | --machine-type=MACHINE_TYPE}

For a description of the placeholders used in this command, see Create a read pool instance with a CPU-based policy and Create a read pool instance with a schedule-based policy policies.

### Enable or update autoscaling on an existing read pool instance

You can enable, disable, or modify automatic scaling settings on an existing read pool instance.

To enable autoscaling for the first time on an existing instance, or to update an existing policy, use the `gcloud beta alloydb instances update` command. For example, to update the target CPU utilization, run:
    
    
    gcloud beta alloydb instances update INSTANCE_ID \
        --region=REGION_ID \
        --cluster=CLUSTER_ID \
        --project=PROJECT_ID \
        --enable-autoscaler \
        --autoscaler-target-cpu-usage=NEW_TARGET_CPU_USAGE

Replace `NEW_TARGET_CPU_USAGE` with the new target CPU utilization that you want to set for your read pool instance, expressed as a decimal value between 0.0 and 1.0.

To add a second schedule to an existing configuration, run the update command with a new schedule name. If the schedule name already exists, the command updates the existing schedule. Otherwise, it creates a new schedule.
    
    
    gcloud beta alloydb instances update INSTANCE_ID \
        --region=REGION_ID \
        --cluster=CLUSTER_ID \
        --project=PROJECT_ID \
        --enable-autoscaler \
        --autoscaler-set-schedule=NEW_SCHEDULE_NAME \
        --autoscaler-schedule-cron-exp=CRON_EXPRESSION \
        --autoscaler-schedule-duration-seconds=DURATION_SECONDS \
        --autoscaler-schedule-min-node-count=MIN_NODE_COUNT

Replace `NEW_SCHEDULE_NAME` with the unique name for the new or updated scaling schedule. If the provided name matches an existing schedule, the command updates that schedule's settings. If the name doesn't exist, the command creates a new schedule with this name.

### How autoscaling policies are evaluated

When multiple automatic scaling policies are active, the autoscaler evaluates each policy and chooses the one that recommends the highest number of nodes.

For example, consider a configuration with two policies:

  * A CPU-based policy with a target of 60% utilization.
  * A schedule-based policy that requires a minimum of three nodes on weekdays between 8 AM and 5 PM.



If it's a weekday at noon and CPU utilization is at 80%, the CPU-based policy might recommend scaling up to four nodes, while the schedule-based policy recommends three. The autoscaler scales the instance to four nodes.

### Autoscaling in

In addition to autoscaling out your read pool instance, AlloyDB also autoscales your instance in when you don't need as many read nodes to support your workflow. When autoscaling in occurs, AlloyDB scales in your node count to the value you set for the `--read-pool-node-count` field.

To determine when your read pool instance should be scaled in, AlloyDB waits until either your autoscaling schedule is inactive or your CPU utilization is less than your utilization target for 10 minutes.

For more information on autoscaling in, see [Understand autoscaler decisions](https://docs.cloud.google.com/compute/docs/autoscaler/understanding-autoscaler-decisions#delays_in_scaling_in).

### Disable autoscaling

To disable automatic scaling, use the `--no-enable-autoscaler` flag. This resets the read pool to its original node count before autoscaling was enabled.
    
    
    gcloud beta alloydb instances update INSTANCE_ID \
        --region=REGION_ID \
        --cluster=CLUSTER_ID \
        --project=PROJECT_ID \
        --no-enable-autoscaler

### View the autoscaled node count

You can view the number of nodes that the autoscaler has scaled to in an instance.

### Console

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click a cluster in the **Resource Name** column.

  3. In the Navigation menu, click **System insights**.

  4. Select an instance from the **Instance** drop-down list.

  5. View the number of nodes under **Active node count**.




### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

Use the [`gcloud alloydb instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/describe) command to view the list of nodes in the instance.
    
    
    gcloud alloydb instances describe INSTANCE_ID \
         --region=REGION_ID \
         --cluster=CLUSTER_ID \
         --project=PROJECT_ID \
         --view=FULL \
         --format="yaml(nodes)"

Replace the following:

  * `INSTANCE_ID`: the ID of the instance that you are updating.

  * `REGION_ID`: the region where the instance is placed.

  * `CLUSTER_ID`: the ID of the cluster where the instance is placed.

  * `PROJECT_ID`: the ID of the project where the cluster is placed.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
