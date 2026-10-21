---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/generic/how-to/attach-cluster/
title: Attach your CNCF conformant cluster \u00a0|\u00a0 GKE attached clusters \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:20:13.115382+00:00
---

# Attach your CNCF conformant cluster  |  GKE attached clusters  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/generic/how-to/attach-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE attached clusters ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/generic)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/generic/concepts/overview)



Send feedback 

#  Attach your CNCF conformant cluster Stay organized with collections  Save and categorize content based on your preferences. 

You can use GKE attached clusters to manage existing CNCF conformant Kubernetes clusters centrally in the Google Cloud console, including clusters that are hosted on AWS, Azure, or elsewhere. This centralized management consolidates operations and helps you to deploy and run clusters more efficiently across multiple environments. This document shows platform administrators how to attach eligible Kubernetes clusters to Google Cloud.

If you're attaching an Amazon EKS or Azure AKS cluster, see [Attach your EKS cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/eks/how-to/attach-cluster) or [Attach your AKS cluster](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks/how-to/attach-cluster). For instructions on using the _previous generation_ of GKE attached clusters, see [Attach third-party clusters](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/previous-generation/how-to/attach-kubernetes-clusters).

**Caution:** the previous generation of GKE attached clusters is in maintenance mode and doesn't receive new features, fixes, or support.

## Supported Kubernetes Clusters

You can add any [conformant Kubernetes cluster](https://www.cncf.io/certification/software-conformance/) with x86 nodes to your fleet, and then view it within the Google Cloud console alongside your GKE clusters.

While Google doesn't verify every Kubernetes distribution for complete feature compatibility, any discovered incompatibilities are documented here. For further details and troubleshooting assistance, refer to [GKE cluster version and upgrade support](https://docs.cloud.google.com/anthos/docs/version-and-upgrade-support#anthos).

## Prerequisites

Ensure that your cluster meets the [cluster requirements](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/generic/reference/cluster-prerequisites).

When attaching your cluster, you must specify the following:

  * A supported Google Cloud [administrative region](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/generic/reference/supported-regions)
  * A platform version



The administrative region is a Google Cloud region to administer your attached cluster from. You can choose any supported region, but best practice is to choose the region geographically closest to your cluster. No user data is stored in the administrative region.

The platform version is the version of GKE attached clusters to be installed on your cluster. You can list all supported versions by running the following command:
    
    
    gcloud container attached get-server-config  \
      --location=GOOGLE_CLOUD_REGION
    

Replace GOOGLE_CLOUD_REGION with the name of the Google Cloud location to administer your cluster from.

## Platform version numbering

These documents refer to the GKE attached clusters version as the platform version, to distinguish it from the Kubernetes version. GKE attached clusters uses the same version numbering convention as GKE - for example, 1.21.5-gke.1. When attaching or updating your cluster, you must choose a platform version whose minor version is the same as or one level below the Kubernetes version of your cluster. For example, you can attach a cluster running Kubernetes v1.22.* with GKE attached clusters platform version 1.21.* or 1.22.*.

This lets you upgrade your cluster to the next minor version before upgrading GKE attached clusters.

## Attach your cluster

**Note:** The default number of clusters that you can attach per project is 50. To increase this quota, contact [Google Cloud support](https://docs.cloud.google.com/support).

To attach your CNCF conformant cluster to Google Cloud [Fleet management](https://docs.cloud.google.com/anthos/fleet-management/docs), run the following commands:

  1. Ensure that your kubeconfig file has an entry for the cluster you'd like to attach. Specific instructions vary by distribution.

  2. Run this command to extract your cluster's kubeconfig context and store it in the `KUBECONFIG_CONTEXT` environment variable:
         
         KUBECONFIG_CONTEXT=$(kubectl config current-context)
         

  3. The command to register your cluster varies slightly depending on whether your cluster has a public or private OIDC issuer. Choose the tab that applies to your cluster:

### Private OIDC issuer

Use the [`gcloud container attached clusters register` command](https://docs.cloud.google.com/sdk/gcloud/reference/container/attached/clusters/register) to register the cluster:
         
         gcloud container attached clusters register CLUSTER_NAME \
           --location=GOOGLE_CLOUD_REGION \
           --fleet-project=PROJECT_NUMBER \
           --platform-version=PLATFORM_VERSION \
           --distribution=generic \
           --context=KUBECONFIG_CONTEXT \
           --has-private-issuer \
           --kubeconfig=KUBECONFIG_PATH
         

Replace the following:

     * CLUSTER_NAME: the name of your cluster. The CLUSTER_NAME must be compliant with the [RFC 1123 Label Names standard](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-label-names).
     * GOOGLE_CLOUD_REGION: the Google Cloud region to administer your cluster from
     * PROJECT_NUMBER: the fleet host project to register the cluster with
     * PLATFORM_VERSION: the platform version to use for the cluster
     * KUBECONFIG_CONTEXT: context in the kubeconfig for accessing the cluster
     * KUBECONFIG_PATH: path to your kubeconfig

### Public OIDC issuer

     1. Retrieve your cluster's OIDC issuer URL and save it for use later. Specific instructions vary by distribution.

     2. Run this command to extract your cluster's kubeconfig context and store it in the `KUBECONFIG_CONTEXT` environment variable:
            
            KUBECONFIG_CONTEXT=$(kubectl config current-context)
            

     3. Use the [`gcloud container attached clusters register` command](https://docs.cloud.google.com/sdk/gcloud/reference/container/attached/clusters/register) to register the cluster:
            
            gcloud container attached clusters register CLUSTER_NAME \
              --location=GOOGLE_CLOUD_REGION \
              --fleet-project=PROJECT_NUMBER \
              --platform-version=PLATFORM_VERSION \
              --distribution=generic \
              --issuer-url=ISSUER_URL \
              --context=KUBECONFIG_CONTEXT \
              --kubeconfig=KUBECONFIG_PATH
            

Replace the following:

        * CLUSTER_NAME: the name of your cluster. The CLUSTER_NAME must be compliant with the [RFC 1123 Label Names standard](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-label-names).
        * GOOGLE_CLOUD_REGION: the Google Cloud region to administer your cluster
        * PROJECT_NUMBER: the fleet host project where the cluster will be registered
        * PLATFORM_VERSION: the GKE attached clusters version to use for the cluster
        * ISSUER_URL: the issuer URL retrieved earlier
        * KUBECONFIG_CONTEXT: context in the kubeconfig for accessing your cluster, as extracted earlier
        * KUBECONFIG_PATH: path to your kubeconfig




## Authorize Cloud Logging / Cloud Monitoring

**Note:** Starting with Kubernetes version 1.28, manual policy binding to authorize the `gke-system/gke-telemetry-agent` service account for log and metric collection is no longer necessary. The required permissions are now automatically granted to this service account. You can therefore disregard this section.

In order for GKE attached clusters to create and upload system logs and metrics to Google Cloud, it must be authorized.

To authorize the Kubernetes workload identity `gke-system/gke-telemetry-agent` to write logs to Google Cloud Logging, and metrics to Google Cloud Monitoring, run this command:
    
    
    gcloud projects add-iam-policy-binding GOOGLE_PROJECT_ID \
      --member="serviceAccount:GOOGLE_PROJECT_ID.svc.id.goog[gke-system/gke-telemetry-agent]" \
      --role=roles/gkemulticloud.telemetryWriter
    

Replace `GOOGLE_PROJECT_ID` with the cluster's Google Cloud project ID.

This IAM binding grants access for all clusters in the Google Cloud project project to upload logs and metrics. You only need to run it after creating your first cluster for the project.

Adding this IAM binding will fail unless at least one cluster has been created in your Google Cloud project. This is because the workload identity pool it refers to (`GOOGLE_PROJECT_ID.svc.id.goog`) is not provisioned until cluster creation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
