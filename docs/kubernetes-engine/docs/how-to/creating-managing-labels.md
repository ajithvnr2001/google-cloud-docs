---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-managing-labels/
title: Create and manage cluster and node pool labels \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:07.474797+00:00
---

# Create and manage cluster and node pool labels  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-managing-labels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Create and manage cluster and node pool labels Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page provides an overview of cluster labels and node pool labels in Google Kubernetes Engine (GKE).

## GKE cluster and node pool labels and Kubernetes labels

GKE cluster and node pool labels are distinct from [labels in Kubernetes](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/). The two labeling systems work independently and don't inherit or share labels.

GKE cluster and node pool labels are arbitrary metadata that are attached to your resources. You can use these labels to track information about billing and usage.

Separately, in Kubernetes, the system uses labels internally to associate cluster components and resources (for example, Pods and nodes) with one another and manage resource lifecycles. You can edit Kubernetes labels with the Kubernetes API. You can also use the GKE API to edit Kubernetes labels on your nodes with [cluster creation](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--node-labels) or with a [cluster update](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/update-existing-nodepools#updating_node_labels). For more information, see [Update Kubernetes node labels and taints for node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/update-existing-nodepools).

## What are cluster labels?

A cluster label is a key-value pair that you can assign to Google Cloud clusters. They help you organize these resources and manage your costs at scale, with the granularity you need. You can attach a label to each resource, then filter the resources based on their labels. Information about labels is forwarded to the billing system that lets you break down your billed charges by label. With built-in [billing reports](https://docs.cloud.google.com/billing/docs/how-to/reports), you can filter and group costs by resource labels. You can also use labels to query [billing data exports](https://docs.cloud.google.com/billing/docs/how-to/bq-examples).

## Requirements for cluster labels

The cluster labels applied to a resource must meet the following requirements:

  * Each resource can have up to 64 cluster labels.
  * Each cluster label must be a key-value pair.
  * Keys have a minimum length of 1 character and a maximum length of 63 characters, and cannot be empty. Values can be empty, and have a maximum length of 63 characters.
  * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. All characters must use UTF-8 encoding, and international characters are allowed. Keys must start with a lowercase letter or international character.
  * The key portion of a cluster label must be unique within a single resource. However, you can use the same key with multiple resources.



These limits apply to the key and value for each cluster label, and to the individual Google Cloud resources that have cluster labels. There is no limit on how many cluster labels you can apply across all resources within a project.

## Common uses of cluster labels

Here are some common use cases for cluster labels:

  * **Team or cost center cluster labels** : Add labels based on team or cost center to distinguish clusters owned by different teams (for example, `team:research` and `team:analytics`). You can use this type of label for cost accounting or budgeting.

  * **Component cluster labels** : For example, `component:redis`, `component:frontend`, `component:ingest`, and `component:dashboard`.

  * **Environment or stage cluster labels** : For example, `environment:production` and `environment:test`.

  * **State cluster labels** : For example, `state:active`, `state:readytodelete`, and `state:archive`.

  * **Ownership cluster labels** : Used to identify the teams that are responsible for operations, for example: `team:shopping-cart`.




  * **Billing breakdown** : Use node pool labels to break down your billed charges by node pool. For more information, see [View detailed breakdown of cluster costs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cost-allocations).

**Note:** Don't include sensitive information in labels, including personally identifiable information, such as an individual's name or title. Labels are not designed to handle sensitive information.

We don't recommend creating large numbers of unique labels, such as for timestamps or individual values for every API call. The problem with this approach is that when the values change frequently or with keys that clutter the catalog, this makes it difficult to effectively filter and report on resources.

## Labels and tags

Labels can be used as queryable annotations for resources, but can't be used to set conditions on policies. Tags provide a way to conditionally allow or deny policies based on whether a resource has a specific tag, by providing fine-grained control over policies. For more information, see the [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview).

## Automatically applied labels

GKE automatically applies several labels to cluster resources.

For example, GKE applies labels to Compute Engine instances, persistent disks, and accelerators (TPU). 

The following table lists the labels that GKE automatically applies to resources:

Label | Applied resources  
---|---  
`goog-gke-node` | Compute Engine VM instance underlying a GKE node.  
`goog-gke-volume` | Compute Engine persistent disk attached to a VM instance underlying a GKE node.  
`goog-gke-tpu` | [Cloud TPU on GKE](https://docs.cloud.google.com/tpu/docs/kubernetes-engine-setup).  
`goog-k8s-cluster-name` | Compute Engine VM instance and persistent disks attached to a VM instance underlying a GKE node.  
`goog-k8s-cluster-location` | Compute Engine VM instance and persistent disks attached to a VM instance underlying a GKE node.  
`goog-k8s-node-pool-name` | Compute Engine VM instances and their boot disks underlying a GKE node.  
`goog-fleet-project` | Compute Engine VM instance and persistent disks attached to a VM instance underlying a GKE node, if the cluster is registered to a fleet.  
`goog-gke-accelerator-type` | GKE node pool.  
`goog-gke-tpu-node-pool-type` | GKE node pool.  
`goog-gke-node-pool-provisioning-model` | GKE node pool.  
`goog-gke-node-pool-protection-tier` | GKE node pool.  
  
Do not edit or delete reserved labels. Any changes that you make to reserved labels are reconciled automatically.

## Label propagation

In GKE, _you can apply labels to clusters and to Standard mode node pools_. When you label a cluster, the label propagates to all of the cluster's individual resources such as nodes, instances, and persistent disks. When you label a node pool, the label propagates to all the node pool's individual resources such as instances, and persistent disks. In Standard clusters, if the cluster labels conflict with node pool labels, such as when the label key is the same but the value is different, node pool labels override cluster labels.

Any labels you apply to your clusters or node pools propagate through a background process that runs hourly. It can take up to one hour for a label to appear on all resources associated with a given cluster. In addition, labels only propagate to Compute Engine instances and Persistent Disks that are attached to Compute Engine instances. Other resources such as workloads, forwarding rules, IP addresses, and non-attached Persistent Disks are not labeled.

For Standard clusters, when cluster and node pool labels are applied to Compute Engine resources, you can [manually change the resource labels](https://docs.cloud.google.com/compute/docs/labeling-resources#add_or_update_labels_to_existing_resources) without those changes being reconciled by GKE. In Autopilot clusters, you can't manually modify the labels on the Compute Engine resources because GKE manages the nodes for you. However, we recommend managing these labels through GKE. Existing labels on those Compute Engine resources will not be removed by GKE unless they conflict with the automatically applied labels.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Get a label fingerprint for API requests

You can skip this step if you use the Google Cloud console or the gcloud CLI.

When you update or add cluster labels using the GKE API, you must provide the latest cluster label fingerprint with your request to prevent any conflicts with other requests.

To get the latest cluster label fingerprint, run a `GET` request for the appropriate cluster. For example:
    
    
    GET https://container.googleapis.com/v1/projects/myproject/zones/us-central1-f/clusters/example-cluster
    

The output is similar to the following:
    
    
    200 OK
    
    {
    
     "name": "mycluster",
     "description": "production-cluster",
     "initialNodeCount": 3,
     ...
     "resourceLabels": {
        "environment": "production",
        ...
      },
      "labelFingerprint": "p1ty_9HoBk0="
    }
    

In this output, the `labelFingerprint` property is the cluster label fingerprint.

## Create a cluster with labels

You can create Autopilot and Standard clusters with labels by using the gcloud CLI, the Google Cloud console, the GKE API, or Terraform.

### gcloud

Run the following command to create an Autopilot cluster with labels:
    
    
    gcloud container clusters create-auto CLUSTER_NAME \
        --labels=KEY=VALUE
    

Or, run the following command to create a Standard cluster with labels:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --labels=KEY=VALUE
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster.
  * `KEY`: the key for the label's key-value pair.
  * `VALUE`: the value for the label's key-value pair.



### Console

To add labels when creating your cluster, do the following:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Click add_box **Create** , and then in the Standard or Autopilot section, click **Configure**.

  3. Configure your cluster.

  4. In the navigation pane, click **Advanced settings** , and then do one of the following:

     * **Autopilot** : Expand **Metadata** , click _add_ **Add label** , and add your labels.
     * **Standard** : In the **Metadata attributes** row, click _edit_ **Edit configuration** , click _add_ **Add label** , add your labels, and then click **Save**.
  5. Click **Create**.




### API

To include a label when creating your cluster, specify the `resourceLabels` object within the `cluster` object that you provide to [projects.zones.clusters.create](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters/create).

### Terraform

To create an Autopilot cluster with labels using Terraform, refer to the following example:
    
    
    resource "google_container_cluster" "default" {
      name     = "gke-autopilot-labels"
      location = "us-central1"
    
      enable_autopilot = true
    
      resource_labels = {
        foo = "bar"
      }
    }

To create a Standard cluster with labels using Terraform, refer to the following example:
    
    
    resource "google_container_cluster" "default" {
      name               = "gke-standard-regional-labels"
      location           = "us-central1"
      initial_node_count = 2
    
      resource_labels = {
        foo = "bar"
      }
    }

To learn more about using Terraform, see [Terraform support for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/resources/use-terraform-gke).

## Add or update labels for existing clusters

You can add or update labels for existing Autopilot and Standard clusters using the gcloud CLI, the Google Cloud console, or the GKE API.

### gcloud

Run the following command:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location =CONTROL_PLANE_LOCATION \
        --update-labels=KEY=VALUE
    

Replace the following:

  * `CLUSTER_NAME`: the name of your cluster.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.
  * `KEY`: the key for the label's key-value pair.
  * `VALUE`: the value for the label's key-value pair.



The label update overwrites any existing labels on the cluster. If the cluster has existing labels that you want to keep, you must include those labels along with any new labels that you want to add.

### Console

To add or update labels, do the following:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. On the **Cluster details** page, select the checkboxes for one or more clusters that you want to modify.

  3. Click sell **Labels**.

  4. Add or update labels.

  5. Click **Save**.




### API

Make a `POST` request to the cluster's [`resourceLabels`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters/resourceLabels) method with the latest fingerprint and a full list of labels to apply.

Similar to metadata and tags, if the cluster has existing labels you want to keep, you must include those labels in the request along with any new labels that you want to add.

For example, the following snippet makes a request to the `resourceLabels` method:
    
    
    POST https://container.googleapis.com/v1/projects/myproject/zones/us-central1-f/clusters/example-cluster/resourceLabels
    
    {
     "resourceLabels": {
      "environment": "production",
      "an-existing-tag": ""
     },
     "labelFingerprint": "42WmSpB8rSM="
    }
    

## Remove cluster labels

You can remove labels from Autopilot and Standard clusters using the gcloud CLI, the Google Cloud console, or the GKE API.

### gcloud

Run the `update` command with the `--remove-labels` flag:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --remove-labels=KEYS
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster.
  * `KEYS`: a comma separated list of keys for the labels you want to remove.



### Console

To remove labels, do the following:

  1. Go to the **Google Kubernetes Engine** page in Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, select the checkboxes for one or more clusters that you want to modify.

  3. Click sell **Labels**.

  4. Click _delete_ **Delete item** next to the **Value** field for the labels that you want to delete.

  5. Click **Save**.




### API

Make a `POST` request to the `resourceLabels` method for the appropriate cluster. Provide the current `labelsFingerprint` and an empty list of labels to remove all labels, or provide a list of labels you want to keep, omitting the labels you want to remove. For example:
    
    
    Request
    
    POST https://container.googleapis.com/v1/projects/myproject/zones/us-central1-f/clusters/example-cluster/resourceLabels
    
    {
     "resourceLabels": { },
     "labelFingerprint": "42WmSpB8rSM="
    }
    

## Create a Standard node pool with labels

You can create a node pool with labels in a Standard cluster by using the gcloud CLI, the Google Cloud console, or the GKE API.

###  gcloud 

Run the following command:
    
    
    gcloud container node-pools create NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --labels=KEY=VALUE
    

Replace the following:

  * `NODE_POOL_NAME`: the name of the node pool.
  * `CLUSTER_NAME`: the name of the cluster.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.
  * `KEY`: the key for the label's key-value pair.
  * `VALUE`: the value for the label's key-value pair.



### API

To include a label when creating your node pool, specify the `resourceLabels` object within the node pool object that you provide to [`projects.zones.clusters.nodePools.create`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters.nodePools/create).

###  Console 

To add labels to new node pool, do the following:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. On the **Cluster details** page, click the name of the cluster you want to modify.

  3. Click the **Nodes** tab.

  4. Click _add_box_ **Create user-managed node pool**.

  5. Configure your new node pool.

  6. From the navigation pane, click **Metadata**.

  7. Click _add_ **Add label**.

  8. Add labels.

  9. Click **Create**.




## Add or update labels for an existing node pool

You can add or update labels for existing node pools using the gcloud CLI, the Google Cloud console, or the GKE API.

This change requires recreating the nodes, which can cause disruption to your running workloads. For details about this specific change, find the corresponding row in the [manual changes that recreate the nodes using a node upgrade strategy without respecting maintenance policies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#manual-changes-strategy-but-no-respect-policies) table. To learn more about node updates, see [Planning for node update disruptions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#plan-node-disruption).

**Caution:** GKE immediately begins recreating the nodes for this change using the node upgrade strategy, regardless of active maintenance policies. GKE depends on [resource availability](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-upgrades-quota) for the change. Disabling node auto-upgrades [doesn't prevent this change](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades#disable-only-versions). Ensure that your workloads running on the nodes are prepared for disruption before you initiate this change.

###  gcloud 

Run the following command:
    
    
    gcloud container node-pools update NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --labels=KEY=VALUE
    

Replace the following:

  * `NODE_POOL_NAME`: the name of the node pool
  * `CLUSTER_NAME`: the name of the cluster.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.
  * `KEY`: the key for the label's key-value pair.
  * `VALUE`: the value for the label's key-value pair.



The label update overwrites any existing labels on the node pool. If the node pool has existing labels that you want to keep, you must include those labels along with any new labels that you want to add.

###  API 

To include a label when modifying your node pool, specify the `resourceLabels` object within the node pool object that you provide to [`projects.zones.clusters.nodePools.update`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters.nodePools/update).

###  Console 

To add or update labels, do the following:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster that contains the node pool that you want to modify.

  3. In the **Node Pools** section, click the name of the node pool that you want to modify.

  4. Click _edit_**Edit**

  5. In the **Labels** section, add or update labels.

  6. Click **Save**.




## Remove node pool labels

You can remove labels from node pools using the gcloud CLI, the Google Cloud console, or the GKE API.

###  gcloud 

Run the following command:
    
    
    gcloud container node-pools update NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --labels=KEY=VALUE
    

Replace the following:

  * `NODE_POOL_NAME`: the name of the node pool.
  * `CLUSTER_NAME`: the name of the cluster.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.
  * `KEY`: the key for the label's key-value pair.
  * `VALUE`: the value for the label's key-value pair.



The label update overwrites any existing labels on the node pool. If the node pool has existing labels that you want to keep, you must exclude any labels that you want to remove. If you want to remove all labels, use `--labels=` without any key-value pairs.

###  API 

To include a label when modifying your node pool, specify the `resourceLabels` object within the node pool object that you provide to [`projects.zones.clusters.nodePools.update`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters.nodePools/update). Provide an empty list of labels to remove all labels, or provide a list of labels you want to keep. Omit the labels you want to remove.

###  Console 

To remove labels from a node pool, do the following

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster that contains the node pool that you want to modify.

  3. In the **Node Pools** section, click the name of the node pool that you want to modify.

  4. Click _delete_ **Delete item** next to the **Value** field for the labels that you want to delete.

  5. Click **Save**.




## What's next

[Read the GKE overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
