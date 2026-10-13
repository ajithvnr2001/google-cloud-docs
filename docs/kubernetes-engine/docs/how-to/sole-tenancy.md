---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/sole-tenancy/
title: Isolate your GKE workloads using sole-tenant nodes \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:21:14.671558+00:00
---

# Isolate your GKE workloads using sole-tenant nodes  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/sole-tenancy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Isolate your GKE workloads using sole-tenant nodes Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to isolate your workloads running on Google Kubernetes Engine (GKE) Standard clusters by using Compute Engine [sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes), which are dedicated physical servers that only run a specific project's VMs. You can use sole-tenant nodes to keep your VMs physically separated from VMs in other projects or to group your VMs together on the same host hardware.

This feature is not supported on GKE Autopilot. To learn more about Autopilot security boundaries, see [Security boundaries in Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-security#security-boundaries).

To use sole-tenant nodes in GKE, you create a sole-tenant node group in Compute Engine and use that node group to create a GKE node pool. You can create node pools using sole-tenant nodes from the GKE cluster's project or [shared sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/share-node-groups) using resources across projects within your organization. For example, you can designate an _owner project_ in your organization where you create sole-tenant node groups, and _consumer projects_ where you have clusters with node pools using those node groups from the owner project.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



### Request additional quota

Sole-tenant nodes are large (for example, 96 vCPUs and 624 GB memory), and the default project quotas are too low to handle them.

You must request a quota increase for Compute Engine API CPUs on the [quotas page](https://console.cloud.google.com/iam-admin/quotas) to create sole-tenant nodes. For more information about requesting an increase, see [Quotas](https://docs.cloud.google.com/compute/quotas#request_quotas).

**Note:** This request can take up to 48 hours to be fulfilled.

The number of CPUs you need depends on the following:

  * Your current CPU quota usage.
  * The size of the node group.
  * The node template.



Examine the number of cores of your sole-tenant node type, and request a CPU limit of at least that amount, preferably with an additional 10 CPUs to ensure that your project has adequate capacity.

## Create a sole-tenant node template

A sole-tenant [node template](https://docs.cloud.google.com/compute/docs/nodes#node_templates) is a regional resource that defines and applies properties to every node when creating a node group. For more information, see [node types](https://docs.cloud.google.com/compute/docs/nodes#node_types).

If you are using [shared sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/share-node-groups), ensure that you complete these instructions in the owner project for the [node group](https://docs.cloud.google.com/compute/docs/nodes#node_groups_and_vm_provisioning), not the consumer project of the cluster.

### Console

  1. Go to the **Sole-tenant nodes** page in the Google Cloud console.

[Go to Sole-tenant nodes](https://console.cloud.google.com/compute/soleTenancy?tab=nodeTemplates)

  2. Click **Create node template**.

  3. Specify a **Name** and **Region** for your node template.

  4. Select a **Node type**. To see which machine types are supported for each node type, refer to [node types](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#node_types) in "Sole-tenancy overview".

  5. Optionally, add one or more Node affinity labels.

  6. Click **Create** to create the node template.




### gcloud

Use the [`gcloud compute sole-tenancy node-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-templates/create) to create a node template:
    
    
    gcloud compute sole-tenancy node-templates create TEMPLATE_NAME \
        --node-type=NODE_TYPE \
        --node-affinity-labels=AFFINITY_LABELS \
        --region=COMPUTE_REGION
    

Replace the following:

  * `TEMPLATE_NAME`: the name for the new node template.
  * `NODE_TYPE`: the node type for sole-tenant nodes created based on this template. Use the [`gcloud compute sole-tenancy node-types list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-types/list) to get a list of the node types available in each zone.
  * `AFFINITY_LABELS`: the keys and values, `[KEY=VALUE,...]`, for affinity labels. Affinity labels let you logically group nodes and node groups and later, when provisioning VMs, you can specify affinity labels on the VMs to schedule VMs on a specific set of nodes or node groups. For more information, see [Node affinity and anti-affinity](https://docs.cloud.google.com/compute/docs/nodes#node_affinity_and_anti-affinity).
  * `COMPUTE_REGION`: the [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) to create the node template in. You can use this template to create node groups in any zone of this region.



The output is similar to the following:
    
    
    Created [https://www.googleapis.com/compute/v1/projects/my-project/regions/us-central1/nodeTemplates/template-name].
    

## Create a sole-tenant node group

A [node group](https://docs.cloud.google.com/compute/docs/nodes#node_groups_and_vm_provisioning) is a set of sole-tenant nodes in a specific zone from the same sole-tenant node template. For regional clusters and node pools available in multiple zones, you must create a node group with the same name in each zone. Ensure that you have sufficient quota before completing this step.

If you are using [shared sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/share-node-groups), ensure that you complete these instructions in the owner project for the [node group](https://docs.cloud.google.com/compute/docs/nodes#node_groups_and_vm_provisioning), not the consumer project of the cluster.

### Console

To create a sole-tenant node group, perform the following steps:

  1. Go to the **Sole-tenant nodes** page in the Google Cloud console.

[Go to Sole-tenant nodes](https://console.cloud.google.com/compute/soleTenancy?tab=nodeGroups)

  2. Click **Create node group**.

  3. Specify a **Name** for your node template.

  4. Select the same **Region** you created your node template in, then select a **Zone** in that **Region**.

  5. Select your **Node template**.

  6. Optionally, enable **Autoscaling mode**.

  7. Specify the **Number of nodes** you want in the group.

  8. Keep the default **Maintenance Policy** , because other values might cause disruption.

  9. Optionally, to share the sole-tenant node group, configure the share settings by specifying one of the following in the **Configure share settings** section:

     * **Share this node group with all projects within the organization**.
     * **Share this node group with selected projects within the organization**.
  10. Click **Create** to create the node group.




### gcloud

Create a node group from the template:
    
    
    gcloud compute sole-tenancy node-groups create GROUP_NAME \
        --zone COMPUTE_ZONE \
        --node-template TEMPLATE_NAME --target-size TARGET_SIZE \
        --share-settings=SHARE_SETTING \
        --share-with=PROJECTS \
        --maintenance-policy=default
    

Replace the following:

  * `GROUP_NAME`: the name you want for your new node group.
  * `COMPUTE_ZONE`: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) where this node group is located. This zone must be in the same region as the node template that you are using.
  * `TEMPLATE_NAME`: the name of the node template that you are using.
  * `TARGET_SIZE`: the number of nodes that you want to create in the group.
  * `SHARE_SETTING`: the share setting for the node group. Set to `projects` to share with specific projects, or set to `organization` to share with the entire organization.
  * `PROJECTS`: a list of project IDs or project numbers to share the node group with. Only required if you set `SHARE_SETTING` to `projects`.



This command sets the default host maintenance policy. Other values might cause disruption.

## Create a GKE sole-tenant node pool

Now that you have created a sole-tenant node group in Compute Engine, you can create a sole-tenant node pool.

If you already have a GKE cluster, you can add a sole-tenant node pool to it. If not, create a cluster with [`gcloud container clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create).

If you are using a regional cluster or if your node pool is available in multiple zones, you must create a node group with the same name and same host maintenance policy in each of those zones. If you can't reuse the name in each zone, create separate node pools for each zone.

### Create a node pool with a sole-tenant node group from the cluster's project

To create a node pool using a node group from the cluster's project, pass the name of the sole-tenancy node group. If you want to use a shared sole-tenant node group, or you want to use custom node affinity labels that you configured when you created the sole-tenant node template, see the instructions to create a node pool with shared sole-tenant node using a node affinity file.

Create a new node pool with a specified node group:

For zonal node pools:
    
    
      gcloud container node-pools create NODE_POOL_NAME \
          --node-group GROUP_NAME --cluster CLUSTER_NAME \
          --location CONTROL_PLANE_LOCATION --machine-type=MACHINE_TYPE \
          --node-locations=COMPUTE_ZONE1
    

For regional node pools:
    
    
      gcloud container node-pools create NODE_POOL_NAME \
          --node-group GROUP_NAME --cluster CLUSTER_NAME \
          --location CONTROL_PLANE_LOCATION --machine-type=MACHINE_TYPE \
          --node-locations=COMPUTE_ZONE1,COMPUTE_ZONE2
    

Replace the following:

  * `NODE_POOL_NAME`: a name for the new node pool.
  * `GROUP_NAME`: the name of the existing sole-tenancy node group you want to use.
  * `CLUSTER_NAME`: the name of the cluster in which you're creating the node pool.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.
  * `MACHINE_TYPE`: the node pool machine type.
  * `COMPUTE_ZONE1`, `COMPUTE_ZONE2,[...]`: the [zones](https://docs.cloud.google.com/compute/docs/regions-zones#available) for the sole-tenancy node groups.



For a full list of optional flags you can specify, refer to the [`gcloud container node-pools create`](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/create) documentation.

### Create a node pool with shared sole-tenant node using a node affinity file

To create a node pool using a [shared sole-tenant node group](https://docs.cloud.google.com/compute/docs/nodes/share-node-groups), you must use [node affinity labels](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#node_affinity_and_anti-affinity). You can also use node affinity to choose node groups from the same project.

To reference labels, follow the instructions to create a node pool, replacing the `--node-group` flag with `--sole-tenant-node-affinity-file` flag. Pass a JSON file with those labels. For example, see the following command:
    
    
      gcloud container node-pools create sole-tenant-node-pool \
          --sole-tenant-node-affinity-file /path/to/affinity/file --cluster my-cluster \
          --location us-central1 --machine-type n1-standard-4  \
          --node-locations=us-central1-a,us-central1-b,us-central1-c
    

The following sections describe use cases for node affinity labels with sole-tenant nodes.

#### Specify a node group name from a project

To use sole-tenant node groups from a specific project and node group name, specify these values in the node affinity file. You can use this affinity if you are creating a multi-zone node pool where the node group names from each zone must match. To use any node group in the specified owner project, omit the entire `compute-googleapis.com/node-group-name` block from the JSON file.

See the following example:
    
    
    [
      {
        "key" : "compute.googleapis.com/project",
        "operator" : "IN",
        "values" : ["OWNER_PROJECT"]
      },
      {
        "key" : "compute.googleapis.com/node-group-name",
        "operator" : "IN",
        "values" : ["GROUP_NAME"]
      },
    ]
    

#### Specify custom labels

You can also use [node affinity and anti-affinity](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#node_affinity_and_anti-affinity) to create a node pool using node groups with custom labels. Each node group is automatically assigned [default affinity labels](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#default_affinity_labels). You can reference the default labels as with the previous examples, or use custom labels designated when creating the node template. You can use custom labels to isolate or group workloads.

See the following example:
    
    
    [
      {
        "key" : "compute.googleapis.com/project",
        "operator" : "IN",
        "values" : ["OWNER_PROJECT"]
      },
      {
        "key" : "workload",
        "operator" : "IN",
        "values" : ["frontend"]
      },
    ]
    

## Limitations

When creating a node pool with sole-tenant nodes, you are responsible for managing the underlying capacity for sole-tenant node groups. Consider how the following features interact with sole-tenant node groups:

  * You can enable [cluster autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler), however it is limited by the capacity of the underlying node group. You can configure the [node group autoscaler](https://docs.cloud.google.com/compute/docs/nodes/autoscaling-node-groups) in Compute Engine to automatically manage the size of your sole-tenant node groups.
  * You cannot enable [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning) for your cluster if you use sole-tenant nodes.
  * You can use any [node upgrade strategy](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies), however you must ensure you have sufficient capacity to support the node pool using its chosen upgrade strategy.



## CPU overcommit

CPU overcommit is an optional feature that lets you oversubscribe the CPU resources on your sole-tenant nodes. CPU overcommit can be useful for workloads that are not CPU-bound, which lets you run more Pods on fewer nodes and potentially reduce costs.

To enable CPU overcommit, you must specify the `--cpu-overcommit-type=enabled` flag when you create a sole-tenant node template. When you create a node pool, you can specify the minimum number of vCPUs that must be available on the sole-tenant node by using the `--sole-tenant-min-node-cpus` flag. The CPU overcommit feature has the same limits that are described in [Overcommit CPUs on sole-tenant VMs](https://docs.cloud.google.com/compute/docs/nodes/overcommitting-cpus-sole-tenant-vms). This feature is supported on GKE version 1.33.1-gke.1545000 and later.

## What's next

  * [Read about how node pools work](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools).
  * [Learn more about sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
