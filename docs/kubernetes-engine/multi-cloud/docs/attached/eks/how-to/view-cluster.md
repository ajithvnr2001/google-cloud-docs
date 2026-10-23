---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/how-to/view-cluster/
title: View your EKS attached cluster's status \u00a0|\u00a0 GKE attached clusters \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:04.349228+00:00
---

# View your EKS attached cluster's status  |  GKE attached clusters  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/how-to/view-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE attached clusters ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/concepts/overview)



Send feedback 

#  View your EKS attached cluster's status Stay organized with collections  Save and categorize content based on your preferences. 

After you create a cluster and node pool, you can view a cluster's status with the Google Cloud CLI or the Google Cloud console.

###  gcloud CLI 

To see the state of an attached cluster, run the following command:
    
    
    gcloud container attached clusters describe CLUSTER_NAME \
        --location=GOOGLE_CLOUD_REGION
    

Replace:

  * CLUSTER_NAME: the name of your cluster
  * GOOGLE_CLOUD_REGION: the name of the Google Cloud region administering your cluster



For more information, see [gcloud container attached clusters describe](https://docs.cloud.google.com/sdk/gcloud/reference/container/attached/clusters/describe).

To see the state of all clusters in a Google Cloud region:
    
    
    gcloud container attached clusters list --location=GOOGLE_CLOUD_REGION
    

Replace GOOGLE_CLOUD_REGION with the name of the Google Cloud region administering your cluster.

For more information, see [gcloud container attached clusters list](https://docs.cloud.google.com/sdk/gcloud/reference/container/attached/clusters/list).

###  Console 

  1. In the Google Cloud console, go to the **Google Kubernetes Engine clusters overview** page.

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Your clusters are listed by their name and location.

  3. Click the cluster's name. A panel with information on the cluster, including its status and enabled features, appears.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
