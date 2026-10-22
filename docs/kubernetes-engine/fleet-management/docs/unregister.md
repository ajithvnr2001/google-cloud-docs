---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/unregister/
title: Unregistering a cluster \u00a0|\u00a0 Fleet management \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:21.547091+00:00
---

# Unregistering a cluster  |  Fleet management  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/unregister/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Fleet management ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)



Send feedback 

#  Unregistering a cluster Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manually unregister a cluster from a Google Cloud fleet. When you manually unregister a cluster, its connection to the fleet is removed but the cluster remains. [Deleting a registered GKE cluster on Google Cloud](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deleting-a-cluster) using either the Google Cloud console or gcloud CLI also deletes the cluster's fleet membership.

You can unregister GKE clusters on Google Cloud and attached third-party clusters only. Other cluster types can't be unregistered.

Note that moving registered clusters between fleets (unregistering then reregistering) is not recommended, as it can result in unexpected or unwanted behavior: for example, your workloads' fleet Workload Identity will change, potentially resulting in blocked requests and outages. The recommended approach is to create a new cluster in the fleet in which you want your workloads to reside, then move your workloads from your old cluster to the new cluster.

## Unregister a cluster

### gcloud

### Unregister a GKE cluster

This command can only be used to unregister GKE clusters registered using `gcloud container clusters update` or `gcloud container clusters create`.

Run the following command:
    
    
    gcloud container clusters update CLUSTER_NAME --clear-fleet-project
    

Replace CLUSTER_NAME with the cluster's name you want to delete.

### Unregister a GKE cluster (legacy command)

If you registered a cluster using the older `register` command, run either of the following commands to unregister it:
    
    
    gcloud container fleet memberships unregister [MEMBERSHIP_NAME] \
       --project=[PROJECT_ID] \
       --gke-uri=[GKE_URI]
    
    
    
    gcloud container fleet memberships unregister [MEMBERSHIP_NAME] \
       --project=[PROJECT_ID] \
       --gke-cluster=[GKE_CLUSTER]
    

where:

  * [PROJECT_ID] is your Google Cloud project ID. [Learn how to find this value](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * [MEMBERSHIP_NAME] is the membership name that corresponds to your cluster. To list all the memberships on the Hub, run: `gcloud container fleet memberships list`.
  * [GKE_URI] is the URI of the GKE cluster, for example: 'https://container.googleapis.com/projects/my-project/locations/us-central1-a/clusters/my-cluster'. You can obtain the URI by running `gcloud container clusters list --uri`. The provided URI will be validated to confirm that it maps to the valid GKE cluster.
  * [GKE_CLUSTER] is the `location/name` of the GKE cluster. The location can be a zone or a region for example: `us-central1-a/my-cluster`.



### Unregister an attached cluster

These instructions apply to clusters registered using the latest version of our attached clusters feature. Clusters attached using the deprecated previous generation of this feature should use the legacy command in the next section.

  * [Detach an EKS cluster](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/attached/eks/how-to/detach-cluster)
  * [Detach an AKS cluster](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/attached/aks/how-to/detach-cluster)
  * [Detach another attached cluster type](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/attached/generic/how-to/detach-cluster)



### Unregister an attached cluster (legacy command)

If you registered a cluster using the previous generation of attached clusters, run the following command to unregister it:
    
    
    gcloud container fleet memberships unregister [MEMBERSHIP_NAME] \
       --project=[PROJECT_ID] \
       --context=[KUBECONFIG_CONTEXT] \
       --kubeconfig=[KUBECONFIG_PATH]
    

where:

  * [PROJECT_ID] is your Google Cloud project ID. [Learn how to find this value](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * [MEMBERSHIP_NAME] is the membership name that corresponds to your cluster. To get list of all the memberships on the Hub, run: `gcloud container fleet memberships list`.
  * [KUBECONFIG_PATH] is the local path where your kubeconfig containing an entry for the cluster file is stored. This defaults to `$KUBECONFIG` if that environment variable is set, otherwise this defaults to `$HOME/.kube/config`.
  * [KUBECONFIG_CONTEXT] is the cluster's context as it appears in the kubeconfig file. You can get this value from the command line by running `kubectl config current-context`.



### Console

### Unregister a GKE cluster on Google Cloud

To unregister a GKE cluster:

  1. Go to the **GKE Clusters** page. This page shows all your clusters.

[Go to the GKE Clusters page](https://console.cloud.google.com/kubernetes/list/overview)

  2. Click more_vert **Actions** next to the cluster in the list that you want to unregister.

  3. In the Actions menu, select **Unregister**.

  4. In the dialog that displays, type the name of the cluster and click **Unregister** to confirm the action.




### Unregister an attached third-party cluster

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To unregister an attached cluster:

  1. In the Google Cloud console, go to the **Google Kubernetes Engine clusters overview** page.

[Go to GKE clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Select the Google Cloud project that the cluster is in.

  3. Click the name of the cluster you want to detach, and then select **View more details** in the side panel.

  4. Near the top of the window, click delete  **Delete**.

  5. When prompted to confirm, enter the name of the cluster and click **Confirm**.




### Terraform

To unregister a GKE cluster that you registered using Terraform:

Delete the following block from the `google_container_cluster` resource configuration of the cluster:
    
    
    fleet {
          project = "FLEET_HOST_PROJECT""
        }

`FLEET_HOST_PROJECT` is the Google Cloud project ID your cluster is registered to.

## Manage the Connect Agent

The following steps apply only to unregistering attached clusters, where the Connect Agent is installed on the cluster as part of registration.

### Optional: Verify that the Connect Agent namespace is deleted

After you unregister a cluster, you can verify that the namespace used by the Connect Agent has been deleted. This applies to registrations that install the Connect Agent only. To do so, run:
    
    
    kubectl get ns -l hub.gke.io/project

If this command returns no output, the namespace has already been deleted.

### Delete the Connect Agent Service Account

If you created a service account for the Connect Agent, you can delete it as follows:
    
    
    gcloud iam service-accounts delete [SERVICE_ACCOUNT_NAME]

## Unregister an unavailable cluster

If you want to unregister a cluster that you can no longer access, perform the following steps:

  1. List the clusters (a.k.a memberships) that are currently registered:
         
         gcloud container fleet memberships list

In the command output, the `Name` column lists the membership names of registered clusters, and the `EXTERNAL_ID` column lists the clusters' UIDs of the kube-system namespace.

  2. To unregister an unavailable cluster, run the following command:
         
         gcloud container fleet memberships delete [MEMBERSHIP_NAME]

where [MEMBERSHIP_NAME] is the membership name that corresponds to your cluster.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
