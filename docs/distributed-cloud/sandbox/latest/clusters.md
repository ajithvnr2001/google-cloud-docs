---
url: https://docs.cloud.google.com/distributed-cloud/sandbox/latest/clusters/
title: Work with clusters \u00a0|\u00a0 Google Distributed Cloud Sandbox \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:18.096738+00:00
---

# Work with clusters  |  Google Distributed Cloud Sandbox  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/sandbox/latest/clusters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Sandbox ](https://docs.cloud.google.com/distributed-cloud/sandbox/latest)



Send feedback 

#  Work with clusters Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud air-gapped provides a managed Kubernetes service with [Google Kubernetes Engine (GKE) Enterprise edition](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gke-editions#why), letting you deploy and run container workloads using industry standard Kubernetes methodologies. Your GDC Sandbox instance comes with three clusters created for you:

  * An _org infrastructure cluster_ , which serves as the control plane for your instance, and
  * Two _Kubernetes clusters_ for running your container workloads.



For details on Google Distributed Cloud air-gapped clusters, see [Cluster architecture](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/platform/pa-user/clusters#cluster-architecture).

## The org infrastructure cluster

GDC Sandbox provides you an org infrastructure cluster called `org-1-admin`. The org infrastructure runs the control plane and data plane components of the organization. It also hosts the Management API server where all non-container workloads and services are deployed. For example, you would use the Management API server to launch and control VMs.

To work with the Management API server on the command line, do the following:

  1. Make sure that you have downloaded, configured, and authenticated with the `gdcloud` command as described in [Connect](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/gdcloud).

  2. Set a `KUBECONFIG` environment variable and download a kubeconfig file for the Management API server:
         
         export KUBECONFIG=org-1-admin-kubeconfig
         gdcloud clusters get-credentials org-1-admin
         




In a similar way, to work with the `org-infra` cluster, do the following:

  1. Set a `KUBECONFIG` environment variable and download a kubeconfig file for the Management API server:
         
         export KUBECONFIG=org-1-infra-kubeconfig
         gdcloud clusters get-credentials org-1-infra
         




## Kubernetes clusters

Your GDC Sandbox instance comes with two pre-created Kubernetes clusters, called `user-vm-1` and `user-vm-2`, in the `org-1` organization. Use these clusters for container-based workloads.

Distributed Cloud supports "shared" clusters for running container workloads. For more background, see [Kubernetes cluster configurations](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/platform/pa-user/cluster-configs). The clusters `user-vm-1` and `user-vm-2` are of the "shared" cluster type. GDC Sandbox does not support the "standard" cluster type.

**Warning:** Don't attempt to create new Kubernetes clusters. GDC Sandbox doesn't support additional clusters.

You can attach clusters to a project when you [create a project](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/create-project).

To work with Kubernetes clusters on the command line, do the following:

  1. Make sure that you have downloaded, configured, and authenticated with the `gdcloud` command as described in [Connect](https://docs.cloud.google.com/distributed-cloud/sandbox/latest/gdcloud).

  2. Set a `KUBECONFIG` environment variable and download a kubeconfig file for the cluster you want to use, either `user-vm-1` or `user-vm-2`. The following example downloads a kubeconfig for `user-vm-1`:
         
         export KUBECONFIG=user-vm-1-kubeconfig
         gdcloud clusters get-credentials user-vm-1 --zone zone1
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
