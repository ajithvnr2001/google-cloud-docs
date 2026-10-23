---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/generate-inventory-for-integrations/
title: Generate inventory for third-party integrations \u00a0|\u00a0 Fleet management \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:28.271831+00:00
---

# Generate inventory for third-party integrations  |  Fleet management  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/generate-inventory-for-integrations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Fleet management ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)



Send feedback 

#  Generate inventory for third-party integrations Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to generate a cluster inventory for an existing fleet. A cluster inventory for a fleet lets you work with open source and third party integrations that use the [ClusterProfile](https://multicluster.sigs.k8s.io/concepts/cluster-profile-api/) specification.

A cluster inventory is the open-source equivalent of a fleet: a logical grouping of Kubernetes clusters and other resources that can be managed together. The [ClusterProfile](https://multicluster.sigs.k8s.io/concepts/cluster-profile-api/) specification contains information that is a subset of the information in a fleet.

ClusterProfile sync feature is a one-way sync between a fleet and a cluster inventory. When ClusterProfile sync is enabled, the fleet is the source of truth, and any changes to the fleet are automatically applied to the cluster inventory by ClusterProfile sync. Changes made directly to the cluster profile resources are not applied to the fleet.

## Before you begin

  1. Ensure that you have followed the [general prerequisites](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/before-you-begin) for working with fleets.

  2. [Create a fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation) or identify an existing fleet to work with.




## Enable ClusterProfile sync

ClusterProfile sync runs against one cluster within the fleet. This cluster is called a hub cluster and can be used to run multi-cluster controllers that need information about the rest of the clusters in the fleet. Examples of multi-cluster controllers include [Argo CD controllers](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/%5D\(https:/github.com/GoogleCloudPlatform/gke-fleet-management/tree/main/argocd-clusterprofile-syncer\)), and [multi-cluster orchestrator](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/%5D\(https:/github.com/GoogleCloudPlatform/gke-fleet-management/blob/main/multi-cluster-orchestrator/docs/overview.md\)). We recommend that you don't run other workloads in the hub cluster.

Enable ClusterProfile sync on a cluster by adding the label `fleet-clusterinventory-management-cluster=true`. You can do the following:

  * Create a new cluster to use as a hub cluster. See the following section to enable ClusterProfile sync on an new cluster.
  * Identify a cluster in the fleet to use as the hub cluster. See the following section to enable ClusterProfile sync on an existing cluster.



After you enable the ClusterProfile sync feature for a fleet, it automatically creates a cluster profile for each cluster in the fleet using the [ClusterProfile](https://multicluster.sigs.k8s.io/concepts/cluster-profile-api/) API. These cluster profiles are automatically created, updated, and deleted when changes are made to the fleet.

### Enable ClusterProfile sync on a new cluster

To create a cluster for the hub cluster, and enable ClusterProfile sync, use the following command:
    
    
    gcloud container clusters create CLUSTER --location LOCATION --enable-fleet
        --labels=fleet-clusterinventory-management-cluster=true
    

Replace the following:

  * CLUSTER: the name of your `google_container_cluster` resource.
  * LOCATION: the location where the cluster is created.



By default, cluster profiles are created in the `fleet-cluster-inventory` namespace. To change the namespace, specify the `fleet-clusterinventory-namespace` label.
    
    
    gcloud container clusters update CLUSTER --location LOCATION
        --update-labels=fleet-clusterinventory-namespace=NAMESPACE
    

Replace the following:

  * CLUSTER: the name of your `google_container_cluster` resource.
  * LOCATION: the location where the cluster is created.
  * NAMESPACE: the namespace where the cluster profiles are generated. If not specified, the cluster profiles are generated in the `fleet-cluster-inventory` namespace.



### Enable ClusterProfile sync on an existing cluster

To enable ClusterProfile sync on an existing cluster, use the following command:
    
    
    gcloud container clusters update CLUSTER --location LOCATION
        --update-labels=fleet-clusterinventory-management-cluster=true
    

Replace the following:

  * CLUSTER: the name of your `google_container_cluster` resource.
  * LOCATION: the location where the cluster is created.



By default, cluster profiles are created in the `fleet-cluster-inventory` namespace. To change the namespace, specify the `fleet-clusterinventory-namespace` label.
    
    
    gcloud container clusters update CLUSTER --location LOCATION
        --update-labels=fleet-clusterinventory-namespace=NAMESPACE
    

Replace the following:

  * CLUSTER: the name of your `google_container_cluster` resource.
  * LOCATION: the location where the cluster is created.
  * NAMESPACE: the namespace where the cluster profiles are generated. If not specified, the cluster profiles are generated in the `fleet-cluster-inventory` namespace.



## Verify the ClusterProfile sync is enabled

Verify that ClusterProfile sync is enabled by verifying that the hub cluster includes the `fleet-clusterinventory-management-cluster = true` label. To do so, use the following command:
    
    
    gcloud container clusters describe CLUSTER --location LOCATION
    

Replace the following::

  * CLUSTER: the name of your `google_container_cluster` resource.
  * LOCATION: the location where the cluster is created.



The output should be similar to the following:
    
    
    resourceLabels:
      fleet-clusterinventory-management-cluster: 'true'
    

## Verify the generated cluster profile resources

Verify that the cluster profile resources are generated in the hub cluster by using the following command:
    
    
    gcloud container clusters get-credentials CLUSTER --location LOCATION
    
    kubectl get clusterprofiles -n fleet-cluster-inventory
    

Replace the following:

  * CLUSTER: the name of your `google_container_cluster` resource.
  * LOCATION: the location where the cluster is created.



The output should be similar to:
    
    
    NAME                           AGE
    cluster-1-us-west1             10s
    cluster-2-us-west1             20s
    

This output should include a cluster profile for each cluster in the fleet. The cluster profile name has the format MEMBERSHIP`-`LOCATION.

## View the contents of the cluster profile

To view the contents of the cluster profile for a specific cluster, use the following command:
    
    
    kubectl get clusterprofile CLUSTER-LOCATION -n fleet-cluster-inventory -o yaml
    

Replace the following:

  * CLUSTER: the name of your `google_container_cluster` resource.
  * LOCATION: the location where the cluster is created.



The output should be similar to:
    
    
    apiVersion: multicluster.x-k8s.io/v1alpha1
    kind: ClusterProfile
    metadata:
      annotations:
        fleet.gke.io/membershipName: projects/123456789/locations/us-west1/memberships/cluster-1
      labels:
        x-k8s.io/cluster-manager: gke-fleet
      name: cluster-1-us-west1
      namespace: fleet-cluster-inventory
    

## Disable ClusterProfile Sync

Disable ClusterProfile sync on the fleet's hub cluster by removing the `fleet-clusterinventory-management-cluster` label:
    
    
    gcloud container clusters update CLUSTER --location LOCATION \
        --remove-labels=fleet-clusterinventory-management-cluster
    

Replace the following:

  * CLUSTER: the name of your `google_container_cluster` resource.
  * LOCATION: the location where the cluster is created.

**Note:** Disabling ClusterProfile sync doesn't delete existing cluster profiles from the hub cluster. However, when changes are made to the fleet, cluster profiles aren't automatically created, updated, or deleted.

## What's next

  * For details about integrating ClusterProfile sync with Argo CD, see [Argo CD ClusterProfile Syncer](https://github.com/GoogleCloudPlatform/gke-fleet-management/tree/main/argocd-clusterprofile-syncer).
  * Multi-cluster Orchestrator uses cluster profiles. It helps schedule multi-cluster and multi-region deployments. For details, see [Overview of Multi-Cluster Orchestrator](https://github.com/GoogleCloudPlatform/gke-fleet-management/blob/main/multi-cluster-orchestrator/docs/overview.md).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
