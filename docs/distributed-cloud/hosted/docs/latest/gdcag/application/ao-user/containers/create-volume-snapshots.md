---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/containers/create-volume-snapshots/
title: Create volume snapshots \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:31:47.061008+00:00
---

# Create volume snapshots  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/containers/create-volume-snapshots/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create volume snapshots Stay organized with collections  Save and categorize content based on your preferences. 

[ Shared ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs#shared-cluster) [ Standard ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs#standard-cluster)

This document explains how to create a copy, or snapshot, of a storage volume at a specific point in time for your container application. A volume snapshot lets you bring a volume back to a prior state or provision a new volume.

This document is for developers within the application operator group, who are responsible for creating application workloads for their organization. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

To complete the tasks in this document, you must request the necessary permissions and prepare your environment.

### Request IAM roles

You must have specific roles to get the permissions you need to create volume snapshots. The roles you require depend on whether you are working within an organization-scoped shared cluster or project-scoped standard cluster. For more information, see [Kubernetes cluster configurations](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs).

#### Shared cluster roles

To create, delete, edit, or view volume snapshots in a shared cluster, ask your Project IAM Admin to grant you the **Namespace Admin** (`namespace-admin`) role. This role is bound to your project namespace.

#### Standard cluster roles

To create, delete, edit, or view volume snapshots in a standard cluster, ask your Project IAM Admin to grant you the **Cluster Developer** (`cluster-developer`) role. This role is bound to your project namespace.

### Prepare your environment

To run commands against a [Kubernetes cluster](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/clusters#cluster-architecture) using the API, make sure you have the following resources:

  * Locate the Kubernetes cluster name, or ask a member of the platform administrator group what the cluster name is.

  * [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/sign-in#zonal-cluster-kubeconfig) the kubeconfig file for the Kubernetes cluster.

  * Use the kubeconfig path of the Kubernetes cluster to replace `KUBERNETES_CLUSTER_KUBECONFIG` in these instructions.




## Take a volume snapshot

To take a snapshot of a `PersistentVolumeClaim` object, create a `VolumeSnapshot` object. The system does not guarantee data consistency. Pause the application and flush data before taking a snapshot.

  1. Create a `VolumeSnapshot` custom resource:
         
         kubectl --kubeconfig KUBERNETES_CLUSTER_KUBECONFIG \
             --namespace NAMESPACE apply -f - <<EOF
         apiVersion: snapshot.storage.k8s.io/v1
         kind: VolumeSnapshot
         metadata:
           name: VOLUME_SNAPSHOT_NAME
         spec:
           source:
             persistentVolumeClaimName: PVC_NAME
         EOF
         

Replace the following:

     * `KUBERNETES_CLUSTER_KUBECONFIG`: the kubeconfig file for the cluster.

     * `NAMESPACE`: the namespace in which to create the volume snapshot. For shared clusters, this must be a project namespace. For standard clusters, it can be any namespace.

     * `VOLUME_SNAPSHOT_NAME`: the `VolumeSnapshot` object name.

     * `PVC_NAME`: the name of the PVC for which you are creating a snapshot.

  2. The snapshot operation is complete when the `.status.readyToUse` field becomes `true`. You can use the following command to check the status:
         
         kubectl --kubeconfig KUBERNETES_CLUSTER_KUBECONFIG get volumesnapshot \
             -o custom-columns='NAME:.metadata.name,READY:.status.readyToUse'
         

  3. Update the PVC manifest with the volume snapshot specified as a data source:
         
         kubectl --kubeconfig KUBERNETES_CLUSTER_KUBECONFIG \
             --namespace NAMESPACE apply -f - <<EOF
         apiVersion: v1
         kind: PersistentVolumeClaim
         metadata:
           name: PVC_NAME
         spec:
           dataSource:
             name: VOLUME_SNAPSHOT_NAME
             kind: VolumeSnapshot
             apiGroup: snapshot.storage.k8s.io
           storageClassName: standard-rwo
           accessModes:
             - ReadWriteOnce
         resources:
           requests:
             storage: 10Gi
         EOF
         

Replace the following:

     * `KUBERNETES_CLUSTER_KUBECONFIG`: the kubeconfig file for the cluster.

     * `NAMESPACE`: the namespace in which the PVC resource exists. For shared clusters, this must be a project namespace. For standard clusters, it can be any namespace.

     * `PVC_NAME`: the name of the PVC for which you are creating a snapshot.

     * `VOLUME_SNAPSHOT_NAME`: the name of the volume snapshot.




## What's next

  * [Container workloads overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/containers/containers-intro)
  * [Create stateful workloads](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/containers/create-stateful-workloads)
  * [Access persistent storage](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/containers/access-persistent-storage)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
