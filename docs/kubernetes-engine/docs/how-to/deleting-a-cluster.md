---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deleting-a-cluster/
title: Deleting a cluster \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:43:55.014812+00:00
---

# Deleting a cluster  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deleting-a-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Deleting a cluster Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains how to delete a Google Kubernetes Engine (GKE) cluster.

When you delete a cluster, GKE deletes the following resources:

  * The control plane resources
  * All of the node instances in the cluster
  * Any Pods that are running on those instances
  * Any firewalls and routes created by GKE at the time of cluster creation
  * Data stored in host `hostPath` and `emptyDir` volumes
  * If [registered to a fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/register/gke#register_your_cluster), the cluster's [fleet membership](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation#about_fleet_membership), unless the cluster was registered using a legacy command.



Review how GKE handles the following resources during cluster deletion:

  * GKE attempts to delete all [load balancer](https://docs.cloud.google.com/compute/docs/load-balancing) resources. However, for Services (`type: LoadBalancer`), we recommend that you delete the Services before deleting your cluster. For clusters with hundreds of Services or more, GKE might not delete all load balancer resources upon cluster deletion.
  * GKE retains [persistent disk](https://docs.cloud.google.com/compute/docs/disks#pdspecs) volumes during cluster deletion. See how to [manage persistent storage during cluster deletion](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#persistent-storage-cluster-deletion).



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Deleting a cluster

### gcloud

To delete a cluster using the Google Cloud CLI, run the following command:
    
    
    gcloud container clusters delete CLUSTER_NAME
    

Replace `CLUSTER_NAME` with the name of the cluster that you want to delete.

For more information, refer to the [`gcloud container clusters delete`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/delete) documentation.

### Console

To delete a cluster using the Google Cloud console, perform the following steps:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Next to the cluster you want to delete, click _more_vert_ **Actions** , then click _delete_ **Delete**.

  3. When prompted to confirm, click **Delete** again.




To delete multiple clusters at once, select them and click _delete_ **Delete**. When prompted to confirm, click **Delete** again.

## What's next

  * [Prevent cluster deletion by using deny policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/managing-clusters#prevent-deletion-deny-policies)
  * [Learn more about clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
