---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/containers/create-volume-snapshots/
title: Create volume snapshots \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:39:53.550867+00:00
---

# Create volume snapshots  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/containers/create-volume-snapshots/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Create volume snapshots Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to create a copy, or snapshot, of a storage volume at a specific point in time for your container application. A volume snapshot lets you bring a volume back to a prior state or provision a new volume.

This page is for developers within the application operator group, who are responsible for creating application workloads for their organization.

## Before you begin

To complete the tasks in this document, you must request the necessary permissions and prepare your environment.

### Request IAM roles

To create, delete, edit, or view volume snapshots in a Kubernetes cluster, ask your Organization IAM Admin to grant you the **Namespace Admin** (`namespace-admin`) role. This role is bound to your project namespace.

### Prepare your environment

To run commands against the pre-configured bare metal Kubernetes cluster, make sure you have the following resources:

  1. Locate the Kubernetes cluster name, or ask your Platform Administrator what the cluster name is.

  2. [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/sign-in#kubernetes-cluster-kubeconfig) the kubeconfig file for the Kubernetes cluster if you don't have one.

  3. Use the kubeconfig path of the Kubernetes cluster to replace `CLUSTER_KUBECONFIG` in these instructions.




## Take a volume snapshot

To take a snapshot of a `PersistentVolumeClaim` object, create a `VolumeSnapshot` object. The system does not guarantee data consistency. Pause the application and flush data before taking a snapshot.

  1. Create a `VolumeSnapshot` custom resource:
         
         kubectl --kubeconfig CLUSTER_KUBECONFIG \
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

     * `CLUSTER_KUBECONFIG`: the kubeconfig file for the Kubernetes cluster.

     * `NAMESPACE`: the project namespace in which to create the volume snapshot.

     * `VOLUME_SNAPSHOT_NAME`: the `VolumeSnapshot` object name.

     * `PVC_NAME`: the name of the PVC for which you are creating a snapshot.

  2. The snapshot operation is complete when the `.status.readyToUse` field becomes `true`. You can use the following command to check the status:
         
         kubectl --kubeconfig CLUSTER_KUBECONFIG get volumesnapshot \
             -o custom-columns='NAME:.metadata.name,READY:.status.readyToUse'
         

  3. Update the PVC manifest with the volume snapshot specified as a data source:
         
         kubectl --kubeconfig CLUSTER_KUBECONFIG \
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

     * `CLUSTER_KUBECONFIG`: the kubeconfig file for the Kubernetes cluster.

     * `NAMESPACE`: the namespace in which the PVC resource exists.

     * `PVC_NAME`: the name of the PVC for which you are creating a snapshot.

     * `VOLUME_SNAPSHOT_NAME`: the name of the volume snapshot.




## What's next

  * [Container workloads overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/containers/containers-intro)
  * [Create stateful workloads](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/containers/create-stateful-workloads)
  * [Access persistent storage](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/containers/access-persistent-storage)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
