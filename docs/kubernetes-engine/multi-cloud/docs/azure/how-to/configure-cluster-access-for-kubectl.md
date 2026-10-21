---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/configure-cluster-access-for-kubectl/
title: Configure cluster access for kubectl \u00a0|\u00a0 GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:35:53.499216+00:00
---

# Configure cluster access for kubectl  |  GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/configure-cluster-access-for-kubectl/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure cluster access for kubectl

This page explains how to configure cluster access for the kubectl command-line tool for GKE on Azure.

This page is for IT administrators and Operators who want to set up, monitor, and manage cloud infrastructure. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Overview

To access your GKE on Azure, you need to configure `kubectl`. You can set a default cluster for `kubectl` by setting the current context in Kubernetes' `kubeconfig` file. Additionally, you can run `kubectl` commands against a specific cluster using the `--cluster` flag.

For more information about `kubeconfig` and cluster endpoints, see [About Kubeconfig](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/about-kubeconfig).

## Before you begin

If you use the [Connect gateway](https://docs.cloud.google.com/anthos/multicluster-management/gateway) for `kubectl` access, you must grant admin users who aren't project owners the IAM roles described in [Use kubectl with identity from the gcloud CLI](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/connect-and-authenticate-to-your-cluster#use-kubectl-with-identity-from-the-gcloud-cli).

## Check current kubeconfig

This section explains how to check your current `kubeconfig`.

### View kubeconfig contexts

To view your environment's `kubeconfig` and all of the contexts it contains, run the following command:
    
    
    kubectl config view
    

The command returns a list of all clusters for which `kubeconfig` entries have been generated. If a GKE on Azure cluster is listed, you can run `kubectl` commands against it in your current environment. Otherwise, you need to generate a `kubeconfig` entry for the cluster.

### View the current context for kubectl

To view the current context that the kubectl command-line tool uses, run the following command:
    
    
    kubectl config current-context
    

`kubectl` outputs the name of the current context.

## Generate a kubeconfig entry

To run `kubectl` commands against GKE clusters, you need to generate a `kubeconfig` entry. How you generate a `kubeconfig` file depends on how you want to connect to your cluster. We recommend that you use the [Connect gateway](https://docs.cloud.google.com/anthos/multicluster-management/gateway). When you use the Connect gateway, the `gke-connect-agent` Deployment sends requests through Google to the cluster control plane.

To check which `kubectl` commands are supported by the Connect gateway, see [Limitations](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway/using#limitations).

If you want to connect through a [private endpoint](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/about-kubeconfig#cluster_endpoint), you need to have a connection and routing to the control plane endpoint in your Azure Virtual Network. The cluster's [kube-apiserver](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/) is part of the control plane. In order to send requests directly to the private endpoint, you might need to widen firewall rules. For more information on connecting to your control plane, see [Network security groups](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/reference/security-groups#application_security_groups).

### Connect gateway
    
    
    gcloud container azure clusters get-credentials CLUSTER_NAME \
      --location GOOGLE_CLOUD_LOCATION
    

Replace the following:

  * `CLUSTER_NAME`: the name of your cluster
  * `GOOGLE_CLOUD_LOCATION`: the Google Cloud region or zone where your GKE on Azure are managed



### Private endpoint

To connect to the private endpoint, you need connectivity to the cluster's control plane. See [Connect to your cluster's control plane](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/connect-and-authenticate-to-your-cluster#connect-to-vpn).
    
    
    gcloud container azure clusters get-credentials CLUSTER_NAME \
      --location GOOGLE_CLOUD_LOCATION \
      --private-endpoint
    

Replace the following:

  * `CLUSTER_NAME`: the name of your cluster
  * `GOOGLE_CLOUD_LOCATION`: the Google Cloud region or zone where your GKE on Azure are managed



## Work with multiple clusters

This section describes how to use `kubectl` with multiple GKE clusters.

### Set a default cluster for kubectl commands

You can switch the current context for `kubectl` to that cluster by running:
    
    
    gcloud container azure clusters get-credentials CLUSTER_NAME \
      --location GOOGLE_CLOUD_LOCATION \
    

Replace the following:

  * `CLUSTER_NAME`: the name of your cluster
  * `GOOGLE_CLOUD_LOCATION`: the Google Cloud region or zone where your GKE on Azure are managed



For example, consider a project with two clusters, `cluster-1` and `cluster-2`. The current context is `cluster-2`. To switch the current context from `cluster-2` to `cluster-1`, run the following command:
    
    
    gcloud container azure clusters get-credentials cluster-1 \
      --location GOOGLE_CLOUD_LOCATION
    

### Run individual kubectl commands against a specific cluster

You can run individual `kubectl` commands against a specific cluster by passing in the name of the cluster as it appears in `kubeconfig` as the argument to the `--cluster` flag.

For example, consider an environment with two clusters, `cluster-1` and `cluster-2`, in which the current context is `cluster-1`. You don't want to change the current context. To get a list of Pod objects on `cluster-2` without changing the current context, run the following command:
    
    
    kubectl get pod --cluster cluster-2
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
