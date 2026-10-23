---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-network-tags/
title: Use network tags to apply firewall rules to nodes \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:43.626025+00:00
---

# Use network tags to apply firewall rules to nodes  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-network-tags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Use network tags to apply firewall rules to nodes Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to dynamically apply network tags to nodes in your Google Kubernetes Engine (GKE) clusters. Network tags let you make firewall rules and allow routes to specific VM instances without disrupting running workloads. On this page, you learn how to apply and update network tags.

This page is for Security specialists who use network tags to apply firewall rules to their nodes. This page provides essential information about available authentication methods and how to implement them. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Before reading this page, ensure that you're familiar with the [general overview of network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags).

## About network tags

_Network tags_ are metadata on Compute Engine virtual machines (VMs) that allow you to make firewall rules and routes applicable to specific VM instances. In GKE, you can use network tags to make VPC firewall rules or routes applicable to the nodes in your cluster.

You can use the GKE API to apply and update network tags on your GKE clusters without disrupting running workloads. Network tags that you specify are also applied to any new nodes that GKE automatically provisions.

### Use Tags instead of network tags

Network tags are simple strings that aren't subject to Identity and Access Management access controls. Anyone with access to your nodes in the GKE API can add network tags to those nodes.

If you use GKE version 1.28 or later, we recommend that you use _Tags_ that have a firewall designation to enforce regional or global [network firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview), which improve on the capabilities of VPC firewall rules.

Tags are key-value pairs that you attach to Compute Engine VMs. You can use IAM to control who can interact with specific Tags.

  * To use Tags to enforce firewall policies in GKE, see [Selectively enforce network firewall policies in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tags-firewall-policies).
  * For more benefits of Tags, see [Comparison of Tags and network tags](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview#differences).
  * For help with migrating your firewall rules to network firewall policies, see [Google Cloud VPC firewall rules to network firewall policies - migration guide (PDF)](https://services.google.com/fh/files/misc/vpc_firewall_rules_network_firewall_policy_migration_guide.pdf).



### Command-line options for applying network tags

The following table describes the flags that you can specify using the Google Cloud CLI to apply network tags to your clusters, as well as their use cases.

Flag | Mode of operation | Level | Description  
---|---|---|---  
`--autoprovisioning-network-tags` | 

  * Autopilot
  * Standard

| Cluster |  Applies the specified network tags to all Autopilot nodes and all auto-provisioned Standard node pools.  
`--tags` | 

  * Standard

| Node pool |  Manually applies network tags to specific Standard node pools.  **Note:** If you used `--autoprovisioning-network-tags` to apply network tags to auto-provisioned node pools, GKE prevents you from using `--tags` for those node pools  
  
## Limitations

Using `--autoprovisioning-network-tags` prevents you from using `--tags` to update the network tags for auto-provisioned Standard node pools.

We recommend that you use `--autoprovisioning-network-tags` for auto-provisioned node pools, and that you use `--tags` only for manually-created node pools.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Add network tags to new clusters

You can add network tags when you create a new cluster.

### Add network tags to new Autopilot clusters

Run the following command:
    
    
    gcloud container clusters create-auto CLUSTER_NAME \
        --location=LOCATION \
        **--autoprovisioning-network-tags =TAG1,TAG2,...**
    

Replace the following:

  * `CLUSTER_NAME`: the name of your new Autopilot cluster.
  * `LOCATION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones#available) for your new cluster.
  * `TAG1,TAG2, ...`: a comma-separated list of the network tags you want to apply.



### Add network tags to new Standard clusters

For Standard, you can also specify network tags specifically for node auto-provisioning to use.

#### Apply network tags to the default node pool

Run the following command to create a new Standard cluster and apply network tags to the default node pool:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --location=LOCATION \
        **--tags =NETWORK_TAG1,NETWORK_TAG2,...**
    

Replace the following:

  * `CLUSTER_NAME`: the name of your new Standard cluster.
  * `COMPUTE_REGION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones#available) for your new cluster.
  * `NETWORK_TAG1,NETWORK_TAG2, ...`: a comma-separated list of the network tags that you want to apply.



#### Apply network tags to auto-provisioned node pools

You can automatically apply network tags to all node pools that are created by node auto-provisioning.

Run the following command:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --location=LOCATION \
        --enable-autoprovisioning \
        **--autoprovisioning-network-tags =TAG1,TAG2,...**
    

Replace `TAG1,TAG2,...` with a comma-separated list of network tags that you want applied to all autoprovisioned node pools.

**Note:** Using `--autoprovisioning-network-tags` prevents you from later using `--tags` to manually update network tags on auto-provisioned node pools.

## Update network tags on existing clusters

You can update the network tags on existing clusters.

**Caution:** This overwrites any previously specified values for network tags.

### Update network tags on existing Autopilot clusters

Run the following command:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --autoprovisioning-network-tags=TAG1,TAG2,...
    

### Update network tags on existing Standard clusters

Run the following command to update the network tags on a specific Standard node pool. You **cannot** use this command to update auto-provisioned node pools if you used `--autoprovisioning-network-tags`.
    
    
    gcloud container node-pools update NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        **--tags =NETWORK_TAG1,NETWORK_TAG2,...**
    

If `--autoprovisioning-network-tags` is set for the cluster, this command returns an error.

**Note:** We recommend that you use `--autoprovisioning-network-tags` to specify network tags for auto-provisioned node pools. If you want to manually update the network tags for those node pools, you must first remove existing auto-provisioning network tags.

#### Update network tags for auto-provisioned node pools

You can update the network tags that node auto-provisioning applies to new and existing auto-provisioned node pools.

Run the following command:
    
    
    gcloud container clusters update CLUSTER_NAME \
        **--autoprovisioning-network-tags =TAG1,TAG2,...**
    

**Note:** Using `--autoprovisioning-network-tags` prevents you from later using `--tags` to update network tags on auto-provisioned node pools.

## Add network tags to new Standard node pools

To create a new node pool in a Standard clusters with specific network tags, run the following command:
    
    
    gcloud container node-pools create NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        **--tags =NETWORK_TAG1,NETWORK_TAG2,...**
    

Replace `NODE_POOL_NAME` with the name of the new node pool.

## View existing network tags

This section shows you how to view your existing network tags.

### View existing network tags in Autopilot

Run the following command:
    
    
    gcloud container clusters describe CLUSTER_NAME \
        --flatten=nodePoolAutoConfig.networkTags
    

If the cluster has network tags, the output is similar to the following:
    
    
    ---
    tags:
    - example-tag
    

### View existing network tags in Standard

You can view network tags in auto-provisioned node pools or in node pools that you created.

#### View network tags in auto-provisioned node pools

Run the following command:
    
    
    gcloud container clusters describe CLUSTER_NAME \
        --flatten=nodePoolAutoConfig.networkTags
    

If the cluster has network tags, the output is similar to the following:
    
    
    ---
    tags:
    - example-tag
    

#### View network tags in node pools without node auto-provisioning

To view the network tags for a specific Standard node pool where applied the tags using the `--tags` flag, run the following command:
    
    
    gcloud container node-pools describe NODE_POOL_NAME\
        --cluster=CLUSTER_NAME \
        --format='value(config.tags)'
    

Replace `NODE_POOL_NAME` with the name of the node pool.

If the node pool has tags, the output is similar to the following:
    
    
    example-tag
    

## Remove network tags

You can remove the network tags from GKE.

### Remove network tags from Autopilot clusters

Run the following command:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --autoprovisioning-network-tags=""
    

### Remove network tags from Standard clusters and node pools

You can remove tags from all auto-provisioned node pools or from specific node pools.

#### Remove network tags from auto-provisioned node pools

To remove network tags from all auto-provisioned node pools, run the following command:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --autoprovisioning-network-tags=""
    

This command also restores your ability to use the `--tags` option to manually specify network tags for auto-provisioned node pools.

#### Remove network tags from specific node pools

To remove network tags from specific node pools, run the following command:
    
    
    gcloud container node-pools update NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --tags=""
    

## What's next

  * [Learn more about network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags).
  * [Learn how to apply cluster labels for better cluster management](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-managing-labels).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
