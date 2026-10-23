---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-node-pool/
title: Create a node pool \u00a0|\u00a0 GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:16.474282+00:00
---

# Create a node pool  |  GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-node-pool/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a node pool

This page describes how to create a node pool.

## Before you begin

This page assumes you are familiar with the cluster autoscaler. For more information, see [Cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/cluster-autoscaler).

## Customize network security groups

To customize a network security group (NSG) for a node pool, see [Network security groups](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/reference/security-groups).

## Create a node pool

Before you create a node pool, you need the following:

  * Permissions to use the `az` command-line tool to retrieve an Azure subnet ID.
  * Access to the cluster's SSH public key.



To create a node pool, run the following commands:

  1. Save your Azure VNet subnet ID and SSH public key to environment variables:
         
         SUBNET_ID=$(az network vnet subnet show \
           --resource-group=VNET_RESOURCE_GROUP_NAME --vnet-name=VNET_NAME \
           --name default --query "id" -otsv)
         SSH_PUBLIC_KEY=$(cat KEY_PATH.pub)
         

Replace the following:

     * `VNET_RESOURCE_GROUP_NAME`: the resource group name that holds VNet
     * `VNET_NAME`: the name of your VNet
     * `KEY_PATH`: the path to your key pair
  2. Create a node pool with the Google Cloud CLI:
         
         gcloud container azure node-pools create NODE_POOL_NAME \
             --cluster CLUSTER_NAME \
             --location GOOGLE_CLOUD_LOCATION \
             --node-version 1.35.3-gke.300 \
             --vm-size VM_SIZE \
             --max-pods-per-node 110 \
             --min-nodes MIN_NODES \
             --max-nodes MAX_NODES \
             --ssh-public-key "${SSH_PUBLIC_KEY}" \
             --subnet-id "${SUBNET_ID}"
         

Replace the following:

     * `NODE_POOL_NAME`: a unique name for your node pool—for example, `node-pool-1`
     * `CLUSTER_NAME`: the name of your GKE on Azure cluster
     * `GOOGLE_CLOUD_LOCATION`: the [Google Cloud location](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/reference/supported-regions) that manages your cluster
     * `VM_SIZE`: a [supported Azure VM size](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/reference/supported-vms)
     * `MIN_NODES`: the minimum number of nodes in the node pool—for more information, see [Cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/cluster-autoscaler)
     * `MAX_NODES`: the maximum number of nodes in the node pool
  3. Check the status of your node pool:
         
         gcloud container azure node-pools describe NODE_POOL_NAME \
             --cluster CLUSTER_NAME \
             --location GOOGLE_CLOUD_LOCATION
         

Replace the following:

     * `NODE_POOL_NAME`: a unique name for your node pool—for example, `node-pool-1`
     * `CLUSTER_NAME`: the name of your GKE on Azure cluster
     * `GOOGLE_CLOUD_LOCATION`: the [Google Cloud location](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/reference/supported-regions) that manages your cluster

The output includes the status of your node pool, including if it is `PROVISIONING` or `RUNNING`.




### Create a node pool in a specific zone

To create a node pool in a specific Azure availability zone, pass the [`--azure-availability-zone`](https://docs.cloud.google.com/sdk/gcloud/reference/container/azure/node-pools/create#--azure-availability-zone) flag to the Google Cloud CLI when you create the node pool.

To create a node pool in a specific Azure availability zone with the Google Cloud CLI, run the following command:
    
    
    gcloud container azure node-pools create NODE_POOL_NAME \
        --cluster CLUSTER_NAME \
        --location GOOGLE_CLOUD_LOCATION \
        --node-version 1.35.3-gke.300 \
        --vm-size VM_SIZE \
        --max-pods-per-node 110 \
        --min-nodes MIN_NODES \
        --max-nodes MAX_NODES \
        --azure-availability-zone AZURE_ZONE \
        --ssh-public-key "${SSH_PUBLIC_KEY}" \
        --subnet-id "${SUBNET_ID}"
    

Replace the following:

  * `NODE_POOL_NAME`: a unique name for your node pool—for example, `node-pool-1`
  * `CLUSTER_NAME`: the name of your cluster
  * `GOOGLE_CLOUD_LOCATION`: the [Google Cloud location](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/reference/supported-regions) that manages your cluster
  * `VM_SIZE`: a [supported Azure VM size](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/reference/supported-vms)
  * `MIN_NODES`: the minimum number of nodes in the node pool—for more information, see [Cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/cluster-autoscaler)
  * `MAX_NODES`: the maximum number of nodes in the node pool
  * `AZURE_ZONE`: the Azure availability zone where GKE on Azure launches the node pool— for example, `3`



## What's next

  * [View your cluster's status](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/view-cluster-status).
  * Try the [Quickstart](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/quickstart) to launch your first workload on GKE on Azure.
  * Learn about [Cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/cluster-autoscaler).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
