---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/how-to/enable-slurm-operator-addon/
title: Enable the Slurm Operator add-on for GKE \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:58.531274+00:00
---

# Enable the Slurm Operator add-on for GKE  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/how-to/enable-slurm-operator-addon/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Enable the Slurm Operator add-on for GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview — Slurm Operator add-on for GKE**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document explains how to enable and disable the Slurm Operator add-on for your Google Kubernetes Engine (GKE) clusters. The Slurm Operator add-on is only supported on Standard clusters; it is not supported on Autopilot clusters. The Slurm Operator add-on runs components in the Kubernetes control plane to manage Slurm workloads within the cluster.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Enable the Slurm Operator add-on on a GKE cluster

You can enable the Slurm Operator add-on on new or existing Standard GKE clusters by using the Google Cloud CLI.
    
    
    gcloud container clusters create CLUSTER_NAME \
        --location LOCATION \
        --cluster-version=VERSION \
        --addons=SlurmOperator
    

Replace the following:

  * `CLUSTER_NAME`: the name of the new cluster.
  * `LOCATION`: the region of cluster.
  * `VERSION`: the GKE version, which must be 1.35.2-gke.1842000 or later. You can also use the `--release-channel` option to select a release channel. The release channel must have a default version of 1.35.2-gke.1842000 or later.



You can enable the Slurm Operator add-on on an existing cluster by using the [`gcloud container clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/update) command and appending the `--update-addons=SlurmOperator=ENABLED` flag.

## Verify the Slurm Operator add-on is enabled

You can verify that the Slurm Operator add-on is enabled on a cluster by using the gcloud CLI.
    
    
    gcloud container clusters describe CLUSTER_NAME \
        --location=LOCATION
    

Replace the following:

  * `CLUSTER_NAME`: the name of the new cluster.
  * `LOCATION`: the region of cluster.



The output should be similar to the following:
    
    
    # Several lines omitted
    addonsConfig:
      slurmOperatorConfig:
        enabled: true
    

This output indicates that the Slurm Operator add-on is enabled for the cluster.

## Disable the Slurm Operator add-on for a cluster

To disable the Slurm Operator add-on on an existing cluster, run the following command:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=LOCATION \
        --update-addons=SlurmOperator=DISABLED
    

Replace the following:

  * `CLUSTER_NAME`: the name of the new cluster.
  * `LOCATION`: the region of cluster.



You can verify that the Slurm Operator add-on is disabled by re-running the `gcloud container clusters describe` command. The `slurmOperatorConfig` section should show `enabled: false`.

## What's next

  * Learn how to deploy a full Slurm cluster on GKE in the [Quickstart: Deploy a Slurm cluster on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/slurm-on-gke/quickstarts/deploy-slurm-on-gke)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
