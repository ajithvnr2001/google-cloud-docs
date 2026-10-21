---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks/how-to/update-cluster/
title: Update your AKS attached cluster \u00a0|\u00a0 GKE attached clusters \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:50:21.027648+00:00
---

# Update your AKS attached cluster  |  GKE attached clusters  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks/how-to/update-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE attached clusters ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks/concepts/overview)



Send feedback 

#  Update your AKS attached cluster Stay organized with collections  Save and categorize content based on your preferences. 

Updating a cluster means updating the attributes or version associated with GKE attached clusters. This doesn't change the Kubernetes version that the cluster is running or update cluster attributes not related to GKE attached clusters. You can update the cluster with the Google Cloud CLI or the Google Cloud console.

###  gcloud CLI 

To update an attached cluster, use the [`gcloud container attached clusters update` command](https://docs.cloud.google.com/sdk/gcloud/reference/container/attached/clusters/update):
    
    
    gcloud container attached clusters update CLUSTER_NAME \
      --location GOOGLE_CLOUD_REGION
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster
  * `GOOGLE_CLOUD_REGION`: the name of the Google Cloud region to administer your cluster from



For information about all the arguments you can use when updating a cluster, see the [`gcloud container attached clusters update` command](https://docs.cloud.google.com/sdk/gcloud/reference/container/attached/clusters/update).

### Console

  1. In the Google Cloud console, go to the **Google Kubernetes Engine clusters overview** page.

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Select the Google Cloud project that the cluster is in.

  3. Click the name of the cluster you want to update, and then select **View more details** in the side panel.

  4. On the **Details** tab, you can update basic information about the cluster or upgrade the GKE attached clusters version.

     * To update cluster basics:

       1. Select edit  **Edit** next to a field that you want to change.

       2. When you are finished making changes, select **Done**.

     * To upgrade the GKE attached clusters version:

       1. Select edit **Upgrade available** next to **Platform version**.

       2. Select the version from the list, and click **Done**.

Upgrading the platform version doesn't change the Kubernetes version on the cluster.




## Use the `--platform-version` argument to upgrade your cluster

Use the optional `--platform-version` argument with the `gcloud container attached clusters update` command to upgrade the version of the GKE attached clusters software installed on your cluster. For example, this lets you upgrade from version 1.28.0-gke.1 to 1.28.0-gke.3, or from version 1.28.x to 1.29.y.

However, the `gcloud container attached clusters update` command can't be used to upgrade a cluster attached using the previous generation of [GKE attached clusters](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/previous-generation/how-to/attach-kubernetes-clusters) to the current generation. This previous generation is older and unmanaged software that no longer receives new features, fixes, or support.

To migrate a cluster from the previous generation to the current generation, follow the steps in [Migrate your cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks/how-to/migrate-cluster).

## Platform version numbering

These documents refer to the GKE attached clusters version as the platform version, to distinguish it from the Kubernetes version. GKE attached clusters uses the same version numbering convention as GKE - for example, 1.21.5-gke.1. When attaching or updating your cluster, you must choose a platform version whose minor version is the same as or one level below the Kubernetes version of your cluster. For example, you can attach a cluster running Kubernetes v1.22.* with GKE attached clusters platform version 1.21.* or 1.22.*.

This lets you upgrade your cluster to the next minor version before upgrading GKE attached clusters.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
