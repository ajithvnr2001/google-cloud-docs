---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/generic/how-to/detach-cluster/
title: Detach your CNCF conformant attached cluster \u00a0|\u00a0 GKE attached clusters \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:14.308211+00:00
---

# Detach your CNCF conformant attached cluster  |  GKE attached clusters  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/generic/how-to/detach-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE attached clusters ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/generic)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/generic/concepts/overview)



Send feedback 

#  Detach your CNCF conformant attached cluster Stay organized with collections  Save and categorize content based on your preferences. 

Detaching a cluster means deregistering it from Google Cloud [Fleet management](https://docs.cloud.google.com/anthos/fleet-management/docs) and removing the associated software from your cluster. You can detach the cluster with the Google Cloud CLI or the Google Cloud console.

###  gcloud CLI 

To detach a cluster, use the [`gcloud container attached clusters delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/container/attached/clusters/delete).

Providing the optional flag `--ignore-errors` forces the cluster to detach even if some in-cluster resources can't be deleted. Including the optional `--allow-missing` flag means that the delete request returns a success code even if the cluster can't be found:
    
    
    gcloud container attached clusters delete CLUSTER_NAME \
      --ignore-errors \
      --allow-missing \
      --location=GOOGLE_CLOUD_REGION
    

Replace the following:

  * CLUSTER_NAME: the name of your cluster
  * GOOGLE_CLOUD_REGION: the name of the Google Cloud region administering your cluster



For more information, see [gcloud container attached clusters delete](https://docs.cloud.google.com/sdk/gcloud/reference/container/attached/clusters/delete).

### Console

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

  1. In the Google Cloud console, go to the **Google Kubernetes Engine clusters overview** page.

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Select the Google Cloud project that the cluster is in.

  3. Click the name of the cluster you want to detach, and then select **View more details** in the side panel.

  4. Near the top of the window, click delete  **Delete**.

  5. When prompted to confirm, enter the name of the cluster and click **Confirm**.




When you detach a cluster, all Google Cloud resources related to the cluster, such as the fleet membership resources and workload identity pool OIDC providers are deleted. The Kubernetes cluster itself isn't deleted.

**Note:** Any features not managed by GKE attached clusters, such as Config Sync and Cloud Service Mesh, need to be cleaned up manually.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
