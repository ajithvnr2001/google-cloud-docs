---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/containers/access-persistent-storage/
title: Access persistent storage \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:21:00.178309+00:00
---

# Access persistent storage  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/containers/access-persistent-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Access persistent storage Stay organized with collections  Save and categorize content based on your preferences. 

Persistent storage in Google Distributed Cloud (GDC) air-gapped appliance lets you preserve container data independently of pod lifecycles. You can claim volumes with `PersistentVolumeClaim` (PVC) resources and expand capacity to retain state across restarts and rescheduling.

This document is for developers within the application operator group who create workloads for their organization.

## Before you begin

To complete the tasks in this document, you must request the necessary permissions and prepare your environment.

### Request IAM roles

To create, delete, edit, or view persistent volumes in a Kubernetes cluster, ask your Organization IAM Admin to grant you the **Namespace Admin** (`namespace-admin`) role. This role is bound to your project namespace.

### Prepare your environment

To run commands against the pre-configured bare metal Kubernetes cluster, make sure you have the following resources:

  1. Locate the Kubernetes cluster name, or ask your Platform Administrator what the cluster name is.

  2. [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/sign-in#kubernetes-cluster-kubeconfig) the kubeconfig file for the Kubernetes cluster if you don't have one.

  3. Use the kubeconfig path of the Kubernetes cluster to replace `CLUSTER_KUBECONFIG` in these instructions.




## Create a persistent volume

The following instructions show how to create a volume using the GDC `standard-rwo` `StorageClass`. For more information on the available `StorageClass` resources in GDC, see [Persistent storage for containers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/containers/containers-intro#persistent-storage).

  1. Create a `PersistentVolumeClaim` and configure it with a `ReadWriteOnce` access mode and a `standard-rwo` storage class:
         
         kubectl --kubeconfig CLUSTER_KUBECONFIG \
             --namespace NAMESPACE apply -f - <<EOF
         apiVersion: v1
         kind: PersistentVolumeClaim
         metadata:
           name: PVC_NAME
         spec:
           accessModes:
             - ReadWriteOnce
           resources:
             requests:
               storage: 10Gi
           storageClassName: standard-rwo
         EOF
         

Replace the following:

     * `CLUSTER_KUBECONFIG`: the kubeconfig file for the Kubernetes cluster.

     * `NAMESPACE`: the project namespace in which to create the PVC.

     * `PVC_NAME`: the name of the `PersistentVolumeClaim` object.

  2. The `PersistentVolume` (PV) objects are dynamically provisioned. Check the status of the new PVs in your Kubernetes cluster:
         
         kubectl get pv --kubeconfig CLUSTER_KUBECONFIG
         

The output is similar to the following:
         
         NAME       CAPACITY   ACCESS MODES   STATUS      CLAIM     STORAGECLASS   AGE
         pvc-uuidd  10Gi       RWO            Bound       pvc-name  standard-rwo   60s
         

  3. Configure your container workloads to use the PVC. The following is an example `nginx` pod that uses a `standard-rwo` PVC:
         
         kubectl --kubeconfig CLUSTER_KUBECONFIG \
             --namespace NAMESPACE apply -f - <<EOF
         apiVersion: apps/v1
         kind: Pod
         metadata:
           name: web-server-deployment
           labels:
             app: nginx
         spec:
           containers:
           - name: nginx
             image: nginx
             volumeMounts:
             - mountPath: /usr/share/nginx/html
               name: data
           volumes:
           - name: data
             persistentVolumeClaim:
               claimName: PVC_NAME
         EOF
         

Replace `PVC_NAME` with the PVC you created.




## Expand volume capacity

To increase the capacity of a `PersistentVolumeClaim` object, update the `spec.resources.storage` field to the new capacity. The maximum supported volume size is 14.5 Ti.

  1. Update the volume to a larger size in the manifest file of the `PersistentVolumeClaim` object:
         
         kubectl --kubeconfig CLUSTER_KUBECONFIG \
             --namespace NAMESPACE apply -f - <<EOF
         apiVersion: v1
         kind: PersistentVolumeClaim
         metadata:
           name: PVC_NAME
         spec:
           accessModes:
             - ReadWriteOnce
           resources:
             requests:
               storage: VOLUME_STORAGE_SIZE
         EOF
         

Replace the following:

     * `CLUSTER_KUBECONFIG`: the kubeconfig file for the Kubernetes cluster.

     * `NAMESPACE`: the project namespace in which the PVC resource exists.

     * `PVC_NAME`: the name of the PVC for which you are increasing the storage size.

     * `VOLUME_SNAPSHOT_SIZE`: the storage size amount to increase, such as `50Gi`.

  2. Check the status of the updated PVs in your cluster:
         
         kubectl get pv --kubeconfig CLUSTER_KUBECONFIG
         




## What's next

  * [Container workloads overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/containers/containers-intro)
  * [Create stateful workloads](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/containers/create-stateful-workloads)
  * [Create volume snapshots](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/containers/create-volume-snapshots)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
