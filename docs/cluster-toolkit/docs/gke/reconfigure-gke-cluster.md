---
url: https://docs.cloud.google.com/cluster-toolkit/docs/gke/reconfigure-gke-cluster/
title: Reconfigure a GKE cluster \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:25:56.975265+00:00
---

# Reconfigure a GKE cluster  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/gke/reconfigure-gke-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Reconfigure a GKE cluster Stay organized with collections  Save and categorize content based on your preferences. 

You can make basic configuration changes to your deployed Google Kubernetes Engine (GKE) resources by editing and redeploying the associated blueprint. This approach helps ensure consistent, repeatable deployments and supports managing your cluster's configuration as code. Using blueprints simplifies maintenance and promotes best practices for infrastructure management.

In this document, you learn how to reconfigure an active GKE cluster that Cluster Toolkit manages. You can update specific configurations, such as resizing a node pool. For fundamental architectural changes, such as switching to a new VPC or changing the scheduler, you must redeploy your cluster. For more information about Cluster Toolkit, see [Cluster Toolkit overview](https://docs.cloud.google.com/cluster-toolkit/docs/overview).

## Limitations

The following changes can't be made by editing the blueprint:

  * You can't switch from a zonal to a regional GKE cluster. To switch from a zonal to a regional cluster, you must create a new cluster.
  * You can't update the GKE version by using the Cluster Toolkit. To update the GKE version, you must [change the version using the Google Cloud console or Google Cloud CLI](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrade_cp).



## Reconfigure the cluster

For GKE clusters, you can update the cluster as follows:

  1. Edit the deployment blueprint to update the supported parameters. For a list of supported parameters, see Supported parameters.
  2. Use the [`./gcluster deploy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-deploy) to run `./gcluster deploy BLUEPRINT_FILE -w` and redeploy the environment.

Replace `BLUEPRINT_FILE` with the path to the deployment blueprint.




## Supported parameters

When you update the blueprint, the following parameters can be modified.

Parameters | Description  
---|---  
`autoscaling_total_min_nodes` and `autoscaling_total_max_nodes` in a nodepool | Use this parameter to update the minimum and maximum number of nodes that exist within an autoscaling nodepool.  
`static_node_count` in a nodepool | Use this parameter to adjust the static number of nodes in the nodepool. You can also replace this parameter with `autoscaling_total_min_nodes` and `autoscaling_total_max_nodes` to switch your cluster from a static to an autoscale nodepool.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
