---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/how-to/migrate-cluster/
title: Migrate your EKS attached cluster \u00a0|\u00a0 GKE attached clusters \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:54.142509+00:00
---

# Migrate your EKS attached cluster  |  GKE attached clusters  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/how-to/migrate-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE attached clusters ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/concepts/overview)



Send feedback 

#  Migrate your EKS attached cluster Stay organized with collections  Save and categorize content based on your preferences. 

The predecessor version of GKE attached clusters is known as GKE attached clusters (previous generation). Migrating from the earlier version of GKE attached clusters to the current generation gives you access to this functionality, including lifecycle management and Fleet registration. Migration is a one-way operation: once you have migrated to the current generation of GKE attached clusters, there is no way to return to GKE attached clusters (previous generation).

## Version numbering policy

These documents refer to the GKE attached clusters version as the platform version, to distinguish it from the Kubernetes version. GKE attached clusters uses the same version numbering convention as GKE - for example, 1.21.5-gke.1. When attaching or updating your cluster, you must choose a platform version whose minor version is the same as or one level below the Kubernetes version of your cluster. For example, you can attach a cluster running Kubernetes v1.22.* with GKE attached clusters platform version 1.21.* or 1.22.*.

This lets you upgrade your cluster to the next minor version before upgrading GKE attached clusters.

## Ensure Workload Identity is enabled

Existing clusters from GKE attached clusters (previous generation) must have Workload Identity enabled before being migrated to the current generation of GKE attached clusters.

To determine whether WI is enabled, run the following command and check the output for any Workload Identity field:
    
    
    gcloud container hub memberships describe MEMBERSHIP_NAME

If Workload Identity is not enabled, the membership must be updated to enable it.

  1. Retrieve your cluster's OIDC issuer URL with the following command:
         
         aws eks describe-cluster \
         --region AWS_REGION \
         --name CLUSTER_NAME \
         --query "cluster.identity.oidc.issuer" \
         --output text

The output of this command will be the URL of your OIDC issuer. Save this value for use later.

  2. Update the membership:
         
         gcloud container fleet memberships register MEMBERSHIP_NAME \
         --context=KUBECONFIG_CONTEXT \
         --kubeconfig=KUBECONFIG_PATH \
         --enable-workload-identity \
         --public-issuer-url=OIDC_URL

Replace:

     * MEMBERSHIP_NAME: the membership name of your cluster
     * KUBECONFIG_CONTEXT: context in the kubeconfig for accessing the EKS cluster
     * KUBECONFIG_PATH: path to your kubeconfig file
     * OIDC_URL: the OIDC URL retrieved earlier



## Migrate your cluster

To migrate your cluster from GKE attached clusters (previous generation) to GKE attached clusters:

  1. Extract your cluster's kubeconfig context and store it in the KUBECONFIG_CONTEXT environment variable:
         
         KUBECONFIG_CONTEXT=$(kubectl config current-context)
         

  2. Run the following command to migrate your cluster to the current generation of GKE attached clusters. This command extracts the relevant details of your cluster's configuration and registers your cluster with Google Fleet Management, and installs or upgrades any necessary software, such as the lifecycle agent, on your cluster.
         
         gcloud container attached clusters import \
           --location=GOOGLE_CLOUD_REGION \
           --fleet-membership=FLEET_MEMBERSHIP \
           --platform-version=PLATFORM_VERSION \
           --distribution=CLUSTER_DISTRIBUTION \
           --context=KUBECONFIG_CONTEXT \
           [--kubeconfig=KUBECONFIG_PATH]
         

Replace:

     * GOOGLE_CLOUD_REGION: the Google Cloud location from which your cluster is administered
     * FLEET_MEMBERSHIP: the fully qualified membership designator of your registered cluster (see below)
     * PLATFORM_VERSION: the version of GKE attached clusters that you want to migrate to (example: v1.22.0-gke.1)
     * CLUSTER_DISTRIBUTION: the cluster type - `eks` for AWS's Elastic Kubernetes Service, `aks` for Azure Kubernetes Service, or `generic` for any other distribution
     * KUBECONFIG_CONTEXT: the name of the context in your `kubeconfig` to connect to your cluster with 
     * KUBECONFIG_PATH: the location of your `kubeconfig` file. If not specified, the default is `~/.kube/config`

The membership designator is a string that uniquely identifies your attached cluster and has the form `projects/PROJECT_NUMBER/locations/global/memberships/MEMBERSHIP_ID`, where

     * PROJECT_NUMBER is your Fleet host project number. You must specify the same project number as one your cluster currently belongs to

     * MEMBERSHIP_ID: this must be the fleet membership ID of your existing cluster. GKE attached clusters will use this value as your cluster name.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
