---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/data-container-image-preloading/
title: Use secondary boot disks to preload data or container images \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:02:13.611336+00:00
---

# Use secondary boot disks to preload data or container images  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/data-container-image-preloading/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Use secondary boot disks to preload data or container images Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to improve workload startup latency by using secondary boot disks in Google Kubernetes Engine (GKE) to preload data or container images on new nodes. This enables workloads to achieve a fast cold start and to improve the overall utilization of provisioned resources.

Before reading this page, ensure that you're familiar with Google Cloud, Kubernetes, containers, YAML, containerd runtime, and the Google Cloud CLI.

## Overview

You can configure node pools with secondary boot disks, available in recent GKE versions. You can tell GKE to provision the nodes and preload them with data, such as a machine learning (ML) model, or a container image. Using preloaded container images or data in a secondary disk has the following benefits for your workloads:

  * Reduced latency when pulling large container images, or downloading data
  * Faster autoscaling
  * Quicker recovery from disruptions like maintenance events and system errors



The following sections describe how to configure the secondary boot disk in GKE Autopilot and Standard clusters.

## How secondary boot disks work

Your workload can start more quickly by using the preloaded container image or data on secondary boot disks. Secondary boot disks have the following characteristics:

  * Secondary boot disks are [Persistent Disks](https://docs.cloud.google.com/compute/docs/disks/persistent-disks) which are backed by distributed block storage.
  * The Persistent Disk is instantiated from [disk images](https://docs.cloud.google.com/compute/docs/images/create-custom) that you create ahead of time.
  * For scalability reasons, each node gets its own Persistent Disk instance created from the disk image. These Persistent Disk instances are deleted when the node is deleted.
  * If the disk image is already in use in the zone, the creation time of all subsequent disks created from the same disk image will be lower.
  * The secondary boot disk type is the same as the node boot disk.
  * The size of the secondary boot disk is decided by disk image size.



Adding secondary boot disks to your node pools does not normally increase the node provisioning time. GKE provisions secondary boot disks from the disk image in parallel with the node provisioning process.

**Best practice** : 

To support preloaded container images, GKE extends the [containerd](https://containerd.io/) runtime with plugins that read the container images from secondary boot disks. Container images are reused by the base layers.

Preload large base layers into the secondary boot disk, while the small upper layers can be pulled from the container registry.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Enable the Container File System API.

[Enable Container File System API](https://console.cloud.google.com/apis/library/containerfilesystem.googleapis.com?q=container%20file%20system)




## Requirements

The following requirements apply to using secondary boot disk:

  1. Use a supported node image type and GKE version: 
     * Container-Optimized OS with containerd (`COS_CONTAINERD`): 
       * GKE Standard and Autopilot: Version 1.30.1-gke.1329000 or later.
     * Ubuntu with containerd (`UBUNTU_CONTAINERD`): 
       * GKE Standard and Autopilot: Version 1.35.0-gke.1403000 or later.
  2. When you modify the disk image, you must create a new node pool. Updating the disk image on existing nodes is not supported.
  3. Configure [Image streaming](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming) to use the secondary boot disk feature.
  4. Prepare the disk image with data ready during build time or with preloaded container images. Ensure that your cluster has access to the disk image to load onto the nodes.

**Best practice** : 

Automate the disk image in a CI/CD pipeline.




## Limitations

You can't update secondary boot disks for existing nodes. To attach a new disk image, create a new node pool.

## Pricing

When you create node pools with secondary boot disks, GKE attaches a [Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks) to each node within the node pool. Persistent Disks are billed based on [Compute Engine disk pricing](https://docs.cloud.google.com/compute/all-pricing#disk).

## Prepare the secondary boot disk image

To prepare the secondary boot disk image, choose either the **Images** tab for preloading container images or choose the **Data** tab for preloading data, then complete the following instructions:

### Images

GKE provides a tool called [`gke-disk-image-builder`](https://github.com/GoogleCloudPlatform/ai-on-gke/tree/main/tools/gke-disk-image-builder) to create a virtual machine (VM), pull the container images on a disk, and then create a disk image from that disk.

To create a disk image with multiple preloaded container images, complete the following steps:

  1. Create a [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) to store the execution logs of `gke-disk-image-builder`.
  2. Create a disk image with `gke-disk-image-builder`.


    
    
    go run ./cli \
        --project-name=PROJECT_ID \
        --image-name=DISK_IMAGE_NAME \
        --zone=LOCATION \
        --gcs-path=gs://LOG_BUCKET_NAME \
        --disk-size-gb=10 \
        --container-image=docker.io/library/python:latest \
        --container-image=docker.io/library/nginx:latest
    

Replace the following:

  * PROJECT_ID: the name of your Google Cloud project.
  * DISK_IMAGE_NAME: the name of the image of the disk. For example, `nginx-python-image`.
  * LOCATION: the [cluster location](https://docs.cloud.google.com/compute/docs/regions-zones/viewing-regions-zones).
  * LOG_BUCKET_NAME: the name of the Cloud Storage bucket to store the execution logs. For example,`gke-secondary-disk-image-logs/`.

**Note:** The values that you specify for the`--container-image` flag must include an image tag (such as `:latest`) or an image digest (such as `@sha256:exampledigestvalue`). If you specify only the image name, the command fails.

When you create a disk image with [`gke-disk-image-builder`](https://github.com/GoogleCloudPlatform/ai-on-gke/tree/main/tools/gke-disk-image-builder), Google Cloud creates multiple resources to complete the process (for example, a VM instance, a temporary disk, and a persistent disk). After its execution, the image builder cleans up all the resources, except the disk image that you created.

### Data

Create a custom disk image as the data source by completing the following steps:

  1. [Create a VM with a blank disk](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#create_a_vm_instance_with_additional_non-boot_disks).
  2. [Use SSH to connect to the VM](https://docs.cloud.google.com/compute/docs/connect/standard-ssh). 
     1. [Mount the blank disk](https://docs.cloud.google.com/compute/docs/disks/format-mount-disk-linux#mounting).
     2. [Download the data onto the blank disk](https://docs.cloud.google.com/storage/docs/downloading-objects#downloading-an-object).
  3. [Create a custom image from the disk](https://docs.cloud.google.com/compute/docs/images/create-custom#create_image).



## Configure the secondary boot disk

You can configure the secondary boot disk in a GKE Autopilot or Standard cluster.

**Best practices** : 

Use an Autopilot cluster for a fully managed Kubernetes experience. To choose the GKE mode of operation that's the best fit for your workloads, see [Choose a GKE mode of operation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode).

### Use GKE Autopilot

In this section, you create a disk image allowlist to allow the disk image in an existing GKE Autopilot cluster. Then, you modify the Pod node selector to use a secondary boot disk.

#### Allow the disk images in your project

In this section, you create a `GCPResourceAllowlist` to allow GKE to create nodes with secondary boot disks from the disk images in your Google Cloud project.

  1. Save the following manifest as `allowlist-disk.yaml`:
         
         apiVersion: "node.gke.io/v1"
         kind: GCPResourceAllowlist
         metadata:
           name: gke-secondary-boot-disk-allowlist
         spec:
           allowedResourcePatterns:
           - "projects/PROJECT_ID/global/images/.*"
         

Replace the PROJECT_ID with your project ID to host the disk image.

  2. Apply the manifest:
         
         kubectl apply -f allowlist-disk.yaml
         

GKE creates nodes with secondary boot disks from all disk images in the project.




#### Update the Pod node selector to use a secondary boot disk

In this section, you modify the Pod specification so that GKE creates the nodes with the secondary boot disk.

  1. Add a `nodeSelector` to your Pod template:
         
         nodeSelector:
             cloud.google.com.node-restriction.kubernetes.io/gke-secondary-boot-disk-DISK_IMAGE_NAME: CONTAINER_IMAGE_CACHE.PROJECT_ID
         

Replace the following:

     * DISK_IMAGE_NAME: the name of your disk image.
     * PROJECT_ID: your project ID to host the disk image.
  2. Use the `kubectl apply` command to apply the Kubernetes specification with the Pod template.

  3. Confirm that the secondary boot disk cache is in use:
         
         kubectl get events --all-namespaces
         

The output is similar to the following:
         
         75s         Normal      SecondaryDiskCachin
         node/gke-pd-cache-demo-default-pool-75e78709-zjfm   Image
         gcr.io/k8s-staging-jobsejt/pytorch-mnist:latest is backed by secondary disk cache
         

**Note:** Be aware that Kubernetes might throttle events if the volume is high. The missing event is not a definite indication that the secondary boot disk was not used. The next step is more reliable way to verify that the secondary boot disk was used.
  4. The more reliable way to confirm that the secondary boot disk cache is in use:

Query the log from the node you are interested in using this log name:
         
         logName="projects/PROJECT_ID/logs/gcfs-snapshotter"
         

Replace `PROJECT_ID` with your Google Cloud project ID.

The log similar to: `Image gcr.io/k8s-staging-jobsejt/pytorch-mnist:latest is backed by secondary boot disk caching by 100.0%...` is an indication that the secondary boot disk cache was used.

  5. Check the image pull latency:
         
         kubectl describe pod POD_NAME
         

Replace POD_NAME with the name of the Pod.

The output is similar to following:
         
         …
           Normal  Pulled     15m   kubelet            Successfully pulled image "docker.io/library/nginx:latest" in 0.879149587s
         …
         




The expected image pull latency for the cached container image should be significantly reduced, regardless of image size.

### Use GKE Standard

To create a GKE Standard cluster and a node pool, complete the following instructions, choosing either the Images or Data tab based on whether you want to preload container images or preload data onto the secondary boot disk:

### Images

To configure a secondary boot disk, either use the Google Cloud CLI or Terraform:

### gcloud

  1. Create a GKE Standard cluster with image streaming enabled:
         
         gcloud container clusters create CLUSTER_NAME \
             --location=LOCATION \
             --cluster-version=VERSION \
             --enable-image-streaming
         

Replace the following:

     * CLUSTER_NAME: the name of your cluster.
     * LOCATION: the cluster location.
     * VERSION: the GKE version to use. The GKE version must be `1.28.3-gke.1067000` or later.
  2. Create a node pool with a secondary boot disk in the same project:
         
         gcloud container node-pools create NODE_POOL_NAME \
         --cluster=CLUSTER_NAME \
         --location LOCATION \
         --enable-image-streaming \
         --secondary-boot-disk=disk-image=global/images/DISK_IMAGE_NAME,mode=CONTAINER_IMAGE_CACHE
         

Replace the following:

     * NODE_POOL_NAME: the name of the node pool.
     * CLUSTER_NAME: the name of the existing cluster.
     * LOCATION: the compute zone or zones separated by comma of the cluster.
     * DISK_IMAGE_NAME: the name of your disk image.

To create a node pool with a secondary boot disk from the disk image in a different project, complete the steps in Use a secondary boot disk in a different project.

  3. Add a `nodeSelector` to your Pod template:
         
         nodeSelector:
             cloud.google.com/gke-nodepool: NODE_POOL_NAME
         

  4. Confirm that the secondary boot disk cache is in use:
         
         kubectl get events --all-namespaces
         

The output is similar to the following:
         
         75s       Normal      SecondaryDiskCachin
         node/gke-pd-cache-demo-default-pool-75e78709-zjfm Image
         gcr.io/k8s-staging-jobsejt/pytorch-mnist:latest is backed by secondary disk cache
         

**Note:** Be aware that Kubernetes might throttle events if the volume is high. The missing event is not a definite indication that the secondary boot disk was not used. The next step is more reliable way to verify that the secondary boot disk was used.
  5. The more reliable way to confirm that the secondary boot disk cache is in use:

Query the log from the node you are interested in using this log name:
         
         logName="projects/PROJECT_ID/logs/gcfs-snapshotter"
         

Replace `PROJECT_ID` with your Google Cloud project ID.

The log similar to: `Image gcr.io/k8s-staging-jobsejt/pytorch-mnist:latest is backed by secondary boot disk caching by 100.0%...` is an indication that the secondary boot disk cache was used.

  6. Check the image pull latency by running the following command:
         
         kubectl describe pod POD_NAME
         

Replace `POD_NAME` with the name of the Pod.

The output is similar to following:
         
         …
           Normal  Pulled     15m   kubelet            Successfully pulled image "docker.io/library/nginx:latest" in 0.879149587s
         …
         




The expected image pull latency for the cached container image should be no more than a few seconds, regardless of image size.

### Terraform

  1. To create a cluster with the default node pool using Terraform, refer to the following example:
         
         resource "google_container_cluster" "default" {
           name               = "default"
           location           = "us-central1-a"
           initial_node_count = 1
         
           # secondary_boot_disks require GKE 1.28.3-gke.106700 or later, which should
           # be true for all release channels apart from EXTENDED.
           # If required, Use `release_channel = "EXTENDED"` and set `min_master_version`.
         }

  2. Create a node pool with a secondary boot disk in the same project:
         
         resource "google_container_node_pool" "secondary-boot-disk-container" {
           name               = "secondary-boot-disk-container"
           location           = "us-central1-a"
           cluster            = google_container_cluster.default.name
           initial_node_count = 1
         
           node_config {
             machine_type = "e2-medium"
             image_type   = "COS_CONTAINERD"
             gcfs_config {
               enabled = true
             }
             secondary_boot_disks {
               disk_image = ""
               mode       = "CONTAINER_IMAGE_CACHE"
             }
           }
         }

To learn more about using Terraform, see [Terraform support for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/resources/use-terraform-gke).

  3. Add a `nodeSelector` to your Pod template:
         
         nodeSelector:
             cloud.google.com/gke-nodepool: NODE_POOL_NAME
         

  4. Confirm that the secondary boot disk cache is in use:
         
         kubectl get events --all-namespaces
         

The output is similar to the following:
         
         75s       Normal      SecondaryDiskCachin
         node/gke-pd-cache-demo-default-pool-75e78709-zjfm Image
         gcr.io/k8s-staging-jobsejt/pytorch-mnist:latest is backed by secondary disk cache
         

  5. Check the image pull latency by running the following command:
         
         kubectl describe pod POD_NAME
         

Replace POD_NAME with the name of the Pod.

The output is similar to following:
         
         …
           Normal  Pulled     15m   kubelet            Successfully pulled image "docker.io/library/nginx:latest" in 0.879149587s
         …
         




The expected image pull latency for the cached container image should be no more than a few seconds, regardless of image size.

To learn more about using Terraform, see [Terraform support for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/resources/use-terraform-gke).

### Data

You can configure a secondary boot disk and preload data by using the Google Cloud CLI or Terraform:

### gcloud

  1. Create a GKE Standard cluster with image streaming enabled:
         
         gcloud container clusters create CLUSTER_NAME \
             --location=LOCATION \
             --cluster-version=VERSION \
             --enable-image-streaming
         

Replace the following:

     * CLUSTER_NAME: the name of your cluster.
     * LOCATION: the cluster location.
     * VERSION: the GKE version to use. The GKE version must be 1.28.3-gke.1067000 or later.
  2. Create a node pool with a secondary boot disk by using the `--secondary-boot-disk` flag:
         
         gcloud container node-pools create NODE_POOL_NAME \
         --cluster=CLUSTER_NAME \
         --location LOCATION \
         --enable-image-streaming \
         --secondary-boot-disk=disk-image=global/images/DISK_IMAGE_NAME
         

Replace the following:

     * NODE_POOL_NAME: the name of the node pool.
     * CLUSTER_NAME: the name of the existing cluster.
     * LOCATION: the compute zone or zones separated by comma of the cluster.
     * DISK_IMAGE_NAME: the name of your disk image.

To create a node pool with a secondary boot disk from the disk image in a different project, complete the steps in Use a secondary boot disk in a different project.

GKE creates a node pool where each node has a secondary disk with preloaded data. GKE attaches and mounts the secondary boot disk on the node.

  3. To access the data, mount the secondary boot disk image in the Pod containers by using a hostPath volume mount. Set `/usr/local/data_path_sbd` to the path in your container where you want the data to reside:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: pod-name
         spec:
           containers:
           ...
             volumeMounts:
             - mountPath: /usr/local/data_path_sbd
               name: data-path-sbd
           ...
           volumes:
           - name: data-path-sbd
             hostPath:
               path: /mnt/disks/gke-secondary-disks/gke-DISK_IMAGE_NAME-disk
         

Replace DISK_IMAGE_NAME with the name of your disk image.

**Note:** the secondary boot disk is shared by all containers on the same node. Any data written to the secondary boot disk by one container is visible to all other containers on the node that mount it. To prevent accidental changes, you can mount the volume in read-only mode.



### Terraform

  1. To create a cluster with the default node pool using Terraform, refer to the following example:
         
         resource "google_container_cluster" "default" {
           name               = "default"
           location           = "us-central1-a"
           initial_node_count = 1
         
           # secondary_boot_disks require GKE 1.28.3-gke.106700 or later, which should
           # be true for all release channels apart from EXTENDED.
           # If required, Use `release_channel = "EXTENDED"` and set `min_master_version`.
         }

  2. Create a node pool with a secondary boot disk in the same project:
         
         resource "google_container_node_pool" "secondary-boot-disk-data" {
           name               = "secondary-boot-disk-data"
           location           = "us-central1-a"
           cluster            = google_container_cluster.default.name
           initial_node_count = 1
         
           node_config {
             machine_type = "e2-medium"
             image_type   = "COS_CONTAINERD"
             gcfs_config {
               enabled = true
             }
             secondary_boot_disks {
               disk_image = ""
             }
           }
         }

To learn more about using Terraform, see [Terraform support for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/resources/use-terraform-gke).

  3. To access the data, mount the secondary boot disk image in the Pod containers by using a hostPath volume mount. Set `/usr/local/data_path_sbd` to the path in your container where you want the data to reside:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: pod-name
         spec:
           containers:
           ...
             volumeMounts:
             - mountPath: /usr/local/data_path_sbd
               name: data-path-sbd
           ...
           volumes:
           - name: data-path-sbd
             hostPath:
               path: /mnt/disks/gke-secondary-disks/gke-DISK_IMAGE_NAME-disk
         

Replace the DISK_IMAGE_NAME with the name of your disk image.




#### Cluster autoscaling with secondary boot disks

To create a node pool and configure cluster autoscaling on a secondary boot disk, use Google Cloud CLI:
    
    
      gcloud container node-pools create NODE_POOL_NAME \
          --cluster=CLUSTER_NAME \
          --location LOCATION \
          --enable-image-streaming \
          --secondary-boot-disk=disk-image=global/images/DISK_IMAGE_NAME,mode=CONTAINER_IMAGE_CACHE \
          --enable-autoscaling \
          --num-nodes NUM_NODES \
          --min-nodes MIN_NODES \
          --max-nodes MAX_NODES
    

Replace the following:

  * NODE_POOL_NAME: the name of the node pool.
  * CLUSTER_NAME: the name of the existing cluster.
  * LOCATION: the compute zone or zones separated by comma of the cluster.
  * DISK_IMAGE_NAME: the name of your disk image.
  * MIN_NODES: the minimum number of nodes to automatically scale for the specified node pool per zone. To specify the minimum number of nodes for the entire node pool in GKE versions 1.24 and later, use `--total-min-nodes`. The flags `--total-min-nodes` and `--total-max-nodes` are mutually exclusive with the flags `--min-nodes` and `--max-nodes`.
  * MAX_NODES: the maximum number of nodes to automatically scale for the specified node pool per zone. To specify the maximum number of nodes for the entire node pool in GKE versions 1.24 and later, use `--total-max-nodes`. The flags `--total-min-nodes` and `--total-max-nodes` are mutually exclusive with the flags `--min-nodes` and `--max-nodes`.



#### Node auto-provisioning with secondary boot disks

In GKE 1.30.1-gke.1329000 and later, you can [configure node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning) to automatically create and delete node pools to meet the resource demands of your workloads.

  1. Create a disk image allowlist custom resource for secondary boot disk for GKE node auto-provisioning similar to the following:
         
         apiVersion: "node.gke.io/v1"
         kind: GCPResourceAllowlist
         metadata:
           name: gke-secondary-boot-disk-allowlist
         spec:
           allowedResourcePatterns:
           - "projects/<PROJECT_ID>/global/images/.*"
         

Replace the PROJECT_ID with your project ID to host the disk image.

  2. Deploy the allowlist custom resource in the cluster, run the following command:
         
         kubectl apply -f ALLOWLIST_FILE
         

Replace the ALLOWLIST_FILE with the manifest filename.

  3. Update the Pod node selector to use secondary boot disk:
         
         nodeSelector:
             cloud.google.com.node-restriction.kubernetes.io/gke-secondary-boot-disk-DISK_IMAGE_NAME:CONTAINER_IMAGE_CACHE.PROJECT_ID
         

Replace the following:

     * DISK_IMAGE_NAME: the name of your disk image.
     * PROJECT_ID: your project ID to host the disk image.



## Use a secondary boot disk in a different project

When you create a node pool with a secondary boot disk, you can tell GKE to use the disk image in a different project by using the `--secondary-boot-disk` flag.

  1. Create a node pool with a secondary boot disk from the disk image in a different project by using the `--secondary-boot-disk` flag. For example:
         
         gcloud beta container node-pools create NODE_POOL_NAME \
             --cluster=CLUSTER_NAME \
             --location LOCATION \
             --enable-image-streaming \
             --secondary-boot-disk=disk-image=projects/IMAGE_PROJECT_ID/global/images/DISK_IMAGE_NAME,mode=CONTAINER_IMAGE_CACHE
         
         

Replace the following:

     * DISK_IMAGE_NAME: the name of your disk image.
     * IMAGE_PROJECT_ID: the name of the project that the disk image belongs to.

GKE creates a node pool where each node has a secondary disk with preloaded data. GKE attaches and mounts the secondary boot disk onto the node.

  2. Grant access to disk images belonging to a different project by adding "Compute Image User" roles for the cluster service accounts:

     * Default compute service account: CLUSTER_PROJECT_NUMBER@cloudservices.gserviceaccount.com
     * GKE service account: service-CLUSTER_PROJECT_NUMBER@container-engine-robot.iam.gserviceaccount.com
    
    gcloud projects add-iam-policy-binding IMAGE_PROJECT_ID \
        --member serviceAccount:CLUSTER_PROJECT_NUMBER@cloudservices.gserviceaccount.com \
        --role roles/compute.imageUser
    
    gcloud projects add-iam-policy-binding IMAGE_PROJECT_ID \
        --member serviceAccount:service-CLUSTER_PROJECT_NUMBER@container-engine-robot.iam.gserviceaccount.com \
        --role roles/compute.imageUser
    




## What's next

  * Use [Use Image streaming to pull container images](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming) to pull container images by streaming the image data as your workloads need it.
  * See [Improve workload efficiency using NCCL Fast Socket](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nccl-fast-socket) to learn how to use the [NVIDIA Collective Communication Library (NCCL) Fast Socket plugin](https://github.com/google/nccl-fastsocket).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
