---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/generic-ephemeral-volumes/
title: Use dedicated Persistent Disks as ephemeral volumes \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:52.821070+00:00
---

# Use dedicated Persistent Disks as ephemeral volumes  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/generic-ephemeral-volumes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Use dedicated Persistent Disks as ephemeral volumes Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to use external storage hardware, such as Compute Engine Persistent Disks, as ephemeral volumes in your Google Kubernetes Engine (GKE) workloads. You should already be familiar with Kubernetes [Volumes](https://kubernetes.io/docs/concepts/storage/volumes/) and [StorageClasses](https://kubernetes.io/docs/concepts/storage/storage-classes/).

## When to use ephemeral storage in Kubernetes

Ephemeral storage is useful in any situation where your workloads only need the data during the lifecycle of the application, such as for data-processing pipelines, machine learning jobs, batch processing, local caching, or analytics. By default, part of the GKE node boot disk is available to use as ephemeral storage in your Pods. This approach often requires careful space planning.

Kubernetes [_generic ephemeral volumes_](https://kubernetes.io/docs/concepts/storage/ephemeral-volumes/#generic-ephemeral-volumes) let you explicitly request ephemeral storage for your Pods by using PersistentVolumeClaims. GKE dynamically provisions Compute Engine [Persistent Disks](https://docs.cloud.google.com/compute/docs/disks/persistent-disks) and attaches the disks to your nodes. This type of ephemeral storage is useful in situations like the following:

  * Your workloads have high performance requirements, so you need to control the storage hardware.
  * You need short-term, container-specific ephemeral storage.
  * You want to avoid using `emptyDir` to provision ephemeral storage. `emptyDir` volumes are still useful in situations where you want multiple containers to share the data in the ephemeral storage.
  * You want more ephemeral storage capacity than the GKE built-in defaults.
  * You want to avoid having to plan your node boot disk size and type in advance for Standard mode GKE clusters.



## Ephemeral storage types in GKE

In general, you can use boot disk storage capacity or dedicated Persistent Disks as ephemeral storage in your Pods and containers. The following table describes the differences:

Storage type | How to use | Description  
---|---|---  
Boot disk - Persistent Disks | Mount a volume using `emptyDir` in the Pod specification and request the capacity that you need. For instructions, see [Creating volumes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/volumes). | The requested ephemeral storage is taken from a reserved portion of the node boot disk. This is the default in both Autopilot and Standard clusters. Use when Pods have small ephemeral storage requests or when you want to share the ephemeral data between multiple containers in the Pod. **Autopilot**

  * The request must be between 10 MiB and 10 GiB.
  * The storage hardware type is pre-configured.

**Standard** No size limit, but requires careful planning of node boot disk size and storage hardware type. For details about how GKE calculates the ephemeral storage reservation in the node boot disk, see [Local ephemeral storage reservation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-node-sizes#local_ephemeral_storage_reservation).  
Local SSD disks | 

  1. Create a node pool with attached Local SSD disks and a compatible machine series.
  2. Mount a volume using `emptyDir` with the required capacity.
  3. Use a nodeSelector to place Pods on nodes with attached Local SSD disks.

For instructions, see [Provision ephemeral storage with local SSDs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd). | Local SSD disks use fixed 375 GB increments that are supported in Standard mode GKE clusters and in Autopilot nodes that run A100 (80 GB) GPUs. Use when you need ephemeral storage that has high throughput. For details, see [About local SSDs for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/local-ssd).  
Dedicated Persistent Disks | 

  1. Optionally, create a Kubernetes StorageClass for the hardware.
  2. Mount a volume using the `ephemeral` volume type in the Pod specification.

This document provides instructions to request this ephemeral storage type. | Google Cloud dynamically provisions the requested external hardware, attached it to your nodes, and mounts the requested volume into your Pod. Use when Pods have large ephemeral storage requests or when you want to control the underlying Persistent Disk type. These volumes have the following properties:

  * Up to 64 TiB in Autopilot mode and Standard mode.
  * The Pod ephemeral storage request can be up to 64 TiB.
  * Specialized hardware such as SSD-backed volumes supported.
  * Network-attached storage.
  * Uses Kubernetes Volumes to get storage, instead of using `emptyDir` to share the node boot disk.

For details about this ephemeral volume type, see [Generic ephemeral volumes](https://kubernetes.io/docs/concepts/storage/ephemeral-volumes/#generic-ephemeral-volumes).  
  
## Pricing

Storage that you provision through generic ephemeral volumes as described in this guide is billed based on [Compute Engine disk pricing](https://docs.cloud.google.com/compute/all-pricing#disk).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have a GKE Autopilot or Standard cluster running version 1.23 or later.
  * Ensure that you have enough quota in your Google Cloud project for the storage hardware. To manage your quota, see [View and manage quotas](https://docs.cloud.google.com/docs/quotas/view-manage).



## Create a StorageClass

Creating a custom Kubernetes StorageClass lets you specify the type of storage to provision based on your price and performance requirements. This step is optional but recommended. If you want to use the GKE default StorageClass, which has the `pd-balanced` Persistent Disk type, skip this step.

  1. Save the following manifest as `ephemeral-pd-class.yaml`:
         
         apiVersion: storage.k8s.io/v1
         kind: StorageClass
         metadata:
           name: ephemeral-ssd
         provisioner: pd.csi.storage.gke.io
         volumeBindingMode: WaitForFirstConsumer
         allowVolumeExpansion: true
         parameters:
           type: STORAGE_TYPE
         

Replace `STORAGE_TYPE` with the name of the Persistent Disk type that you want, like `pd-ssd`. For a list of supported types, see [Persistent Disk types](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#disk-types) in the Compute Engine documentation.

  2. Create the StorageClass:
         
         kubectl create -f ephemeral-pd-class.yaml
         




## Request ephemeral storage capacity in a Pod

To provision, attach, and use external hardware as ephemeral storage, add the corresponding volume to your Pod manifest and add a volume mount to the container specification.

  1. Save the following manifest as `ephemeral-ssd-deployment.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: ephemeral-deployment
         spec:
           replicas: 1
           selector:
             matchLabels:
               storage: ephemeral
           template:
             metadata:
               labels:
                 storage: ephemeral
             spec:
               containers:
               - name: ephemeral-container
                 image: nginx
                 resources:
                   requests:
                     cpu: 500m
                     memory: 2Gi
                     ephemeral-storage: 2Gi
                 **volumeMounts :
                 - mountPath: "/short-term"
                   name: ephemeral-volume
               volumes:
               - name: ephemeral-volume
                 ephemeral:
                   volumeClaimTemplate:
                     metadata:
                       labels:
                         type: ephemeral
                     spec:
                       accessModes: ["ReadWriteOnce"]
                       storageClassName: "ephemeral-ssd"
                       resources:
                         requests:
                           storage: 1Ti**
         

This manifest creates a new Kubernetes PersistentVolumeClaim that requests a new PersistentVolume named `ephemeral-volume` with the following properties:

     * **`spec.volumes.ephemeral`:** The `ephemeral` volume type.
     * **`.spec.accessModes`:** The volume access mode, which determines read-write access from Pods and volume sharing between nodes. This examples uses `ReadWriteOnce`, which mounts the PersistentVolume to a single node for access by one or more Pods on the node. For details, see [Access modes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes).
     * **`.spec.storageClassName`:** Optionally, the name of the StorageClass that you created. If you omit this field, GKE uses the default StorageClass and provisions a `pd-balanced` Persistent Disk.
     * **`.spec.resources.requests.storage`:** The storage capacity that you want.
  2. Create the Deployment:
         
         kubectl create -f ephemeral-ssd-deployment.yaml
         




GKE provisions a Compute Engine disk that meets the requirements of the PersistentVolumeClaim and attaches the disk to the node. GKE mounts the volume into the Pod and provides the requested capacity to the container.

## Verify that GKE mounted an ephemeral volume

  1. Create a shell session in the Pod:
         
         kubectl exec -it deploy/ephemeral-deployment -- bash
         

  2. Check the mounted volumes:
         
         df -h

The output is similar to the following:
         
         Filesystem                Size      Used Available Use% Mounted on
         ...
         **/dev/sdb               1006.9G     28.0K   1006.8G   0% /short-term**
         /dev/sda1                94.3G      3.6G     90.6G   4% /etc/hosts
         /dev/sda1                94.3G      3.6G     90.6G   4% /dev/termination-log
         /dev/sda1                94.3G      3.6G     90.6G   4% /etc/hostname
         /dev/sda1                94.3G      3.6G     90.6G   4% /etc/resolv.conf
         ...
         

  3. Exit the shell session:
         
         exit
         


**Success:** You dynamically provisioned external storage hardware and mounted it to your Kubernetes workload as ephemeral storage.

## What's next

  * [Learn about the available storage options in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/storage-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
