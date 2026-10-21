---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/create-gke-cluster/
title: Create a GKE Cluster with Pathways \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:34:59.740240+00:00
---

# Create a GKE Cluster with Pathways  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/create-gke-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Create a GKE Cluster with Pathways Stay organized with collections  Save and categorize content based on your preferences. 

You can use [Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/overview) to create pre-configured Google Kubernetes Engine (GKE) clusters for Pathways-based workloads. You can also use `gcloud` to manually create GKE clusters for Pathways-based workloads.

## Before you begin

Make sure you have:

  * [Installed Kubernetes tools](https://kubernetes.io/docs/tasks/tools/)
  * [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment)
  * [Enabled the Google Kubernetes Engine API](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api)



## Set up your local environment

Sign in with your Google Cloud credentials.
    
    
    gcloud auth application-default login
    

Define the following environment variables with values appropriate to your workload.

## Create a GKE cluster

In the following example, you create a cluster with TPU v6e 2x4 node pools. You can create a cluster by using Cluster Toolkit or the `gcloud` CLI.

### Cluster Toolkit

  1. [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  2. Deploy a GKE TPU cluster by following the instructions in [Deploy a GKE TPU v6e cluster](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-tpu-v6e) (for an overview of all TPU deployment options, see [Cloud TPU deployments overview](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-tpu-overview)).

When configuring your deployment blueprint, do the following:

     * Ensure that `enable_pathways_for_tpus` is set to `true` (enabled by default in Cluster Toolkit TPU blueprints). This automatically provisions the required `cpu-np` CPU node pool (`n4-standard-64`) and Kueue configurations for the Pathways controller.
     * Set `num_slices` to the number of TPU slice node pools required for your workload.
     * Set `tpu_topology` to your selected TPU slice topology (for example, `2x4` or `4x4`).
     * If you're using reserved capacity, set `reservation` to your [TPU reservation](https://docs.cloud.google.com/tpu/docs/about-tpu-reservations) name.

After the cluster is created, you can submit Pathways workloads by using the `gcluster job submit` command with the `--pathways` flag.




### gcloud

  1. Set some environment variables
         
         CLUSTER=GKE_CLUSTER_NAME
         PROJECT=PROJECT_ID
         ZONE=ZONE
         REGION=REGION
         CLUSTER_VERSION=GKE_CLUSTER_VERSION
         PW_CPU_MACHINE_TYPE="n2-standard-64"
         NETWORK=NETWORK
         SUBNETWORK=SUB_NETWORK
         CLUSTER_NODEPOOL_COUNT=3
         TPU_MACHINE_TYPE="ct6e-standard-4t"
         WORKERS_PER_SLICE=2
         TOPOLOGY="2x4"
         NUM_CPU_NODES=1

Replace the following:

     * `CLUSTER`: the GKE cluster name
     * `PROJECT_ID`: your Google Cloud project name
     * `ZONE`: the zone where you are creating resources
     * `REGION`: the region where you are creating resources
     * `CLUSTER_VERSION`: [Optional] the GKE cluster version, use 1.32.2-gke.1475000 or later
     * `NETWORK`: [Optional] set a Virtual Private Cloud name, this must be created before creating your cluster
     * `SUBNETWORK`: [Optional] set a subnetwork name, this must be created before creating your cluster



The following steps explain how to create a GKE cluster and set it up for running Pathways workloads.

  1. Create a GKE cluster:
         
         gcloud beta container clusters create ${CLUSTER} \
         --project=${PROJECT} \
         --zone=${ZONE} \
         --cluster-version=${CLUSTER_VERSION} \
         --scopes=storage-full,gke-default,cloud-platform \
         --machine-type ${PW_CPU_MACHINE_TYPE} \
         --network=${NETWORK} \
         --subnetwork=${SUBNETWORK}
         

  2. Create TPU node pools:
         
         for i in $(seq 1 ${CLUSTER_NODEPOOL_COUNT}); do
         gcloud container node-pools create "tpu-np-${i}" \
         --project=${PROJECT} \
         --zone=${ZONE} \
         --cluster=${CLUSTER} \
         --machine-type=${TPU_MACHINE_TYPE} \
         --num-nodes=${WORKERS_PER_SLICE} \
         --placement-type=COMPACT \
         --tpu-topology=${TOPOLOGY} \
         --scopes=storage-full,gke-default,cloud-platform \
         --workload-metadata=GCE_METADATA
         done
         

  3. Create a CPU node pool:
         
         gcloud container node-pools create "cpu-pathways-np" \
         --project ${PROJECT} \
         --zone ${ZONE} \
         --cluster ${CLUSTER} \
         --machine-type ${PW_CPU_MACHINE_TYPE} \
         --num-nodes ${NUM_CPU_NODES} \
         --scopes=storage-full,gke-default,cloud-platform \
         --workload-metadata=GCE_METADATA
         

  4. Install the `JobSet` API

Get credentials for the cluster and add them to your local kubectl context.

**Note:** in the following command, if you are using zonal clusters, specify `--zone`, if you are using regional clusters, specify `--region`.
         
         gcloud container clusters get-credentials ${CLUSTER} \
             [--zone=${ZONE} | --region=${REGION}] \
             --project=${PROJECT} \
             && kubectl config set-context --current --namespace=default
         

To use the Pathways architecture on your GKE cluster, you need to install the `JobSet` API.
         
         kubectl apply --server-side -f https://github.com/kubernetes-sigs/jobset/releases/download/v0.8.0/manifests.yaml
         




## What's next

  * [Run a batch workload with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/batch-workload)
  * [Pathways interactive mode](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/pathways-interactive-mode)
  * [Multihost inference with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/multihost-inference)
  * [Resilient training with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/resilient-training)
  * [Porting JAX workloads to Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/porting-jax-workloads)
  * [Troubleshoot Pathways on cloud](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/troubleshooting-pathways)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
