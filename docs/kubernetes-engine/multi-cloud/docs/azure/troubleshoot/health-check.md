---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/troubleshoot/health-check/
title: Diagnose cluster issues \u00a0|\u00a0 GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:57.402358+00:00
---

# Diagnose cluster issues  |  GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/troubleshoot/health-check/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Diagnose cluster issues

The health check feature regularly monitors the health of the cluster control plane and several critical components, and helps you detect and diagnose potential problems with your clusters.

If you need additional assistance, reach out to [Cloud Customer Care](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/getting-support). 

## Issues detected

The cluster health checker detects and alerts you to the following issues in a cluster:

  * **`kube-scheduler` health on control plane nodes**: If the `kube-scheduler` is unhealthy, this suggests that the cluster is having trouble assigning Pods to nodes. To investigate further, you can examine the `kube-scheduler` Pod log.

  * **`kube-controller-manager` health on control plane nodes**: The `kube-controller-manager` monitors various controllers, such as the ReplicaSet, Deployment, and Namespace controllers, among others. If the `kube-controller-manager` is deemed unhealthy, this suggests that one or more of the controllers it manages might not be working properly. To determine the precise issue, you can examine the `kube-controller-manager` Pod log, which might provide more information about the malfunctioning controller(s).

  * **Root volume capacity** : The health checker checks for sufficient capacity on the root volume of each control plane node. If the available capacity falls under 512MB, the health checker alerts you to the potential risk of running out of disk space.




## View health check events

To view alerts from the health checker for a specific cluster, run the following command:
    
    
    gcloud container azure clusters describe CLUSTER_NAME \
        --location GOOGLE_CLOUD_LOCATION
    

Replace the following:

  * `CLUSTER_NAME`: your cluster's name
  * `GOOGLE_CLOUD_LOCATION`: the name of the Google Cloud location that manages the cluster



Here's an excerpt of the kind of output you can expect:
    
    
    {
      "name": "some-cluster-name",
      "description": "test-cluster",
      ...
      "errors": [
      {
        "message": "Replica (replica-name)": kube-controller-manager is unhealthy"
      },
      {
        "message": "Replica (replica-name)": not enough disk space on root volume, only 9 MB left"
      }
      ]
      ...
    }
    

In this example, the error message indicates that a `kube-controller-manager` component is unhealthy, and that the capacity on a control plane node's root volume is getting low.

## What's next

If you need additional assistance, reach out to [Cloud Customer Care](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/getting-support). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
