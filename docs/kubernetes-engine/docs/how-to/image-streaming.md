---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming/
title: Use Image streaming to pull container images \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:35:01.817558+00:00
---

# Use Image streaming to pull container images  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Use Image streaming to pull container images Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to use _Image streaming_ in Google Kubernetes Engine (GKE) to pull container images by streaming the image data as your applications need it.

Autopilot clusters automatically use Image streaming to pull eligible images. The instructions on this page about enabling and disabling image streaming apply to Standard clusters.

## Overview

Image streaming is a method of pulling container images in which GKE streams data from eligible images as requested by your applications. You can use Image streaming to allow your workloads to initialize without waiting for the entire image to download, which leads to significant improvements in initialization times. The shortened pull time provides you with benefits including the following:

  * Faster autoscaling
  * Reduced latency when pulling large images
  * Faster Pod startup



With Image streaming, GKE uses a remote filesystem as the root filesystem for any containers that use eligible container images. GKE streams image data from the remote filesystem as needed by your workloads. Without Image streaming, GKE downloads the entire container image onto each node and uses it as the root filesystem for your workloads.

While streaming the image data, GKE downloads the entire container image onto the local disk in the background and caches it. GKE then serves future data read requests from the cached image.

When you deploy workloads that need to read specific files in the container image, the Image streaming backend serves only those requested files.

## Requirements

You must meet the following requirements to use Image streaming in GKE Autopilot and Standard clusters:

  * You must enable the Container File System API.

[Enable Container File System API](https://console.cloud.google.com/apis/library/containerfilesystem.googleapis.com?q=container%20file%20system)

  * You must use a node image with containerd. Supported options include:

    * Container-Optimized OS with containerd (`COS_CONTAINERD`): Supported on GKE version 1.30.1-gke.1329000 and later. This is the default for Autopilot nodes. [Learn more about COS](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images#cos).
    * Ubuntu with containerd (`UBUNTU_CONTAINERD`): Supported on GKE version 1.35.0-gke.1403000 and later. [Learn more about Ubuntu node images](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images#ubuntu).
  * Your container images must be stored in standard or [remote repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-overview) in Artifact Registry or in public registries on [Docker Hub](https://hub.docker.com/).

  * If you enable [private nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation#enable-private-nodes) on your cluster, you must [enable Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#enabling-pga) on the subnet for your nodes to access the Image streaming Service.

  * If VPC Service Controls protects your container images and you use Image streaming, you must also include the Image streaming API (`containerfilesystem.googleapis.com`) in the service perimeter.

  * If the GKE nodes in the cluster don't use the default service account, you must ensure that your custom service account has the [Service Usage Consumer](https://docs.cloud.google.com/iam/docs/understanding-roles) (`roles/serviceusage.serviceUsageConsumer`) IAM role in the project that hosts the container image.




## Limitations

  * Container images that use the [V2 Image Manifest, schema version 1](https://docs.docker.com/registry/spec/manifest-v2-1/) are not eligible.
  * Container images with duplicate layers are not supported. GKE downloads these images without streaming the data. Check your container image for empty layers or duplicate layers.
  * If your workloads read many files in an image during initialization, you might notice increased initialization times because of the latency added by the remote file reads.
  * If your workloads require a large proportion of the image to be available before code can execute, you might see a delay between the time that the `kubelet` starts the container and the time that the container actually starts to send logs.
  * You might not notice the benefits of Image streaming during the first pull of an eligible image. However, after Image streaming caches the image, future image pulls on any cluster benefit from Image streaming.
  * GKE Standard clusters use the cluster-level configuration to determine whether to enable Image streaming on new node pools created using [node pool auto-creation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning). However, you cannot use [workload separation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-separation) to create node pools with Image streaming enabled when Image streaming is disabled at the cluster level.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Enable the Container File System API.

[Enable Container File System API](https://console.cloud.google.com/apis/library/containerfilesystem.googleapis.com?q=container%20file%20system)

  * Ensure that you have an existing Standard cluster. If you need one, [create a Standard cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-regional-cluster).




## Enable Image streaming on clusters

You can enable Image streaming on new or existing Standard clusters by using the gcloud CLI `--enable-image-streaming` flag, or using the Google Cloud console. When you create a cluster with the `--enable-image-streaming` flag, Image streaming will be enabled in the default node pool. New node pools you create will also have Image streaming enabled unless you disable it when creating the node pools.

All [Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) clusters use Image streaming to pull eligible images. For instructions, refer to [Set the version and release channel of a new Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster#set-version). The following instructions only apply to GKE Standard clusters.

You can enable Image streaming on existing clusters that meet the requirements using either the gcloud CLI or the Google Cloud console.

### gcloud

To update an existing cluster to use Image streaming, run the following command using the gcloud CLI:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        **--enable-image-streaming**
    

Replace the following:

  * `CLUSTER_NAME`: the name of your cluster.
  * `CONTROL_PLANE_LOCATION`: the [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster.



### Console

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Click the name of the cluster you want to modify.

  3. On the **Clusters** page, in the **Features** section, click _edit_ next to **Image streaming**.

  4. In the **Edit Image streaming** dialog, select the **Enable Image streaming** checkbox.

  5. Click **Save changes**.




After you modify the cluster, GKE enables Image streaming on your existing node pools automatically by default. If you explicitly enabled or disabled Image streaming on individual node pools, those node pools don't inherit the changes to the cluster-level setting.

Changing the Image streaming setting respects maintenance availability when updated at the cluster level, but not at the node pool level.

This change requires recreating the nodes, which can cause disruption to your running workloads. For details about this specific change, find the corresponding row in the [manual changes that recreate the nodes using a node upgrade strategy and respecting maintenance policies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#manual-changes-respecting-policies) table. To learn more about node updates, see [Planning for node update disruptions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#plan-node-disruption).

**Important:** GKE respects maintenance policies when recreating the nodes for this change using the node upgrade strategy, and depends on [resource availability](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-upgrades-quota). Disabling node auto-upgrades [doesn't prevent this change](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades#disable-only-versions). To manually apply the changes to the nodes, use the gcloud CLI to call the [`gcloud container clusters upgrade`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/upgrade) command, passing the `--cluster-version` flag with the same GKE version that the node pool is already running.

### Verify Image streaming is enabled on a cluster

You can check whether Image streaming is enabled at the cluster level using either the gcloud CLI or the Google Cloud console.

### gcloud

Run the following command:
    
    
    gcloud container clusters describe CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --flatten "nodePoolDefaults.nodeConfigDefaults"
    

Replace the following:

  * `CLUSTER_NAME`: the name of your cluster.
  * `CONTROL_PLANE_LOCATION`: the [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster.



The setting is enabled if the output is similar to the following:
    
    
    gcfsConfig:
      enabled: true
    ...
    

The setting is disabled if the output is similar to the following:
    
    
    gcfsConfig: {}
    ...
    

### Console

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Click the name of the cluster you want to check.

  3. On the **Clusters** page, in the **Features** section, next to **Image streaming** it will show whether the setting is enabled.




## Enable Image streaming on node pools

By default, node pools inherit the Image streaming setting at the cluster level. You can enable or disable Image streaming on specific node pools using the gcloud CLI.

**Note:** When you change the Image streaming setting on a specific node pool, the node pool no longer inherits changes to the cluster-level Image streaming setting.

### On a new node pool

To create a new node pool with Image streaming enabled, run the following command:
    
    
    gcloud container node-pools create NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --image-type=IMAGE_TYPE \
        **--enable-image-streaming**
    

Replace the following:

  * `NODE_POOL_NAME`: the name of your new node pool.
  * `CLUSTER_NAME`: the name of the cluster for the node pool.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.
  * `IMAGE_TYPE`: the image type, either `COS_CONTAINERD` (Container-Optimized OS) or `UBUNTU_CONTAINERD` (Ubuntu).



### On an existing node pool

You can enable Image streaming on existing node pools that meet the requirements.

To update an existing node pool to use Image streaming, run the following command:
    
    
    gcloud container node-pools update POOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        **--enable-image-streaming**
    

Replace the following:

  * `POOL_NAME`: the name of your node pool.
  * `CLUSTER_NAME`: the name of the cluster for the node pool.
  * `CONTROL_PLANE_LOCATION`: the [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster.



Changing the Image streaming setting respects maintenance availability when updated at the cluster level, but not at the node pool level.

This change requires recreating the nodes, which can cause disruption to your running workloads. For details about this specific change, find the corresponding row in the [manual changes that recreate the nodes using a node upgrade strategy without respecting maintenance policies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#manual-changes-strategy-but-no-respect-policies) table. To learn more about node updates, see [Planning for node update disruptions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#plan-node-disruption).

**Caution:** GKE immediately begins recreating the nodes for this change using the node upgrade strategy, regardless of active maintenance policies. GKE depends on [resource availability](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-upgrades-quota) for the change. Disabling node auto-upgrades [doesn't prevent this change](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades#disable-only-versions). Ensure that your workloads running on the nodes are prepared for disruption before you initiate this change.

### Verify Image streaming is enabled on a node pool

Check whether Image streaming is enabled for a node pool:
    
    
    gcloud container node-pools describe POOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION
    

Replace the following:

  * `POOL_NAME`: the name of your node pool.
  * `CLUSTER_NAME`: the name of the cluster for the node pool.
  * `CONTROL_PLANE_LOCATION`: the [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster.



The setting is enabled if the output is similar to the following:
    
    
    gcfsConfig:
      enabled: true
    ...
    

The setting is disabled if the output is similar to the following:
    
    
    gcfsConfig: {}
    ...
    

## Schedule a workload using Image streaming

After you enable Image streaming on your cluster, GKE automatically uses Image streaming when pulling eligible container images from Artifact Registry without requiring further configuration.

GKE adds the `cloud.google.com/gke-image-streaming: "true"` label to nodes in node pools with Image streaming enabled. On GKE Standard, if you enable or disable Image streaming on specific node pools so that your cluster has a mix of nodes that use Image streaming and nodes that don't, you can use [node selectors](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/) in your deployments to control whether GKE schedules your workloads on nodes that use Image streaming.

In the following example, you schedule a Deployment that uses a large container image on a cluster with Image streaming enabled. You can then optionally compare the performance to an image pull without Image streaming enabled.

  1. Create a new cluster with Image streaming enabled:
         
         gcloud container clusters create CLUSTER_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --enable-image-streaming \
             --image-type=IMAGE_TYPE
         

  2. Get credentials for the cluster:
         
         gcloud container clusters get-credentials CLUSTER_NAME \
             --location=CONTROL_PLANE_LOCATION
         

  3. Save the following manifest as `frontend-deployment.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: frontend
         spec:
           replicas: 1
           selector:
             matchLabels:
               app: guestbook
               tier: frontend
           template:
             metadata:
               labels:
                 app: guestbook
                 tier: frontend
             spec:
               containers:
               - name: php-redis
                 image: us-docker.pkg.dev/google-samples/containers/gke/gb-frontend:v5
                 env:
                 - name: GET_HOSTS_FROM
                   value: "dns"
                 resources:
                   requests:
                     cpu: 100m
                     memory: 100Mi
                 ports:
                 - containerPort: 80
         

The `gb-frontend` container image is 327 MB in size.

  4. Apply the manifest to your cluster:
         
         kubectl apply -f frontend-deployment.yaml
         

  5. Verify that GKE created the Deployment:
         
         kubectl get pods -l app=guestbook
         

The output is similar to the following:
         
         NAMESPACE    NAME                          READY    STATUS       RESTARTS    AGE
         default      frontend-64bcc69c4b-pgzgm     1/1      Completed    0           3s
         

  6. Get the Kubernetes event log to see image pull events:
         
         kubectl get events --all-namespaces
         

The output is similar to the following:
         
         NAMESPACE  LAST SEEN  TYPE    REASON          OBJECT                                                 MESSAGE
         default    11m        Normal  Pulling         pod/frontend-64bcc69c4b-pgzgm                          Pulling image "us-docker.pkg.dev/google-samples/containers/gke/gb-frontend:v5"
         default    11m        Normal  Pulled          pod/frontend-64bcc69c4b-pgzgm                          Successfully pulled image "us-docker.pkg.dev/google-samples/containers/gke/gb-frontend:v5" in 1.536908032s
         default    11m        Normal  ImageStreaming  node/gke-riptide-cluster-default-pool-f1552ec4-0pjv    Image us-docker.pkg.dev/google-samples/containers/gke/gb-frontend:v5 is backed by image streaming.
         ...
         

In this output:

     * The `Pulled` event shows the time taken for Image streaming to pull the image.
     * The `ImageStreaming` event shows that the node uses Image streaming to serve the container image.

**Note:** The `Reason` field displays `BackedByGCFS` instead of `ImageStreaming` in clusters with GKE versions prior to 1.20.9-gke.1000. `BackedByGCFS` also indicates that the image uses Image streaming.**Note:** If you run a workload that uses the same image on the same node, GKE uses the local cache of the image instead of streaming the image. You will see `Container image "us-docker.pkg.dev/google-samples/containers/gke/gb-frontend:v5" already present on machine` in the `Message` field for the Pod `Pulled` event. To test the performance of Image streaming again, delete the node and create a new one.



### Compare performance with standard image pulls

In this optional example, you create a new cluster with Image streaming disabled and deploy the `frontend` Deployment to compare performance with Image streaming.

  1. Create a new cluster with Image streaming disabled:
         
         gcloud container clusters create CLUSTER2_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --image-type=IMAGE_TYPE
         

**Note:** By default, GKE creates clusters with Image streaming disabled.
  2. Get credentials for the cluster:
         
         gcloud container clusters get-credentials CLUSTER2_NAME \
             --location=CONTROL_PLANE_LOCATION
         

  3. Deploy the `frontend` Deployment from the previous example:
         
         kubectl apply -f frontend-deployment.yaml
         

  4. Get the Kubernetes event log:
         
         kubectl get events --all-namespaces
         

The output is similar to the following:
         
         NAMESPACE  LAST SEEN  TYPE    REASON     OBJECT                             MESSAGE
          default    87s        Normal  Pulled     pod/frontend-64bcc69c4b-qwmfp      Successfully pulled image "us-docker.pkg.dev/google-samples/containers/gke/gb-frontend:v5" in 23.929723476s
         

Notice the time GKE took to pull the entire image. In this example output, GKE needed almost 24 seconds. With Image streaming enabled, GKE only needed 1.5 seconds to pull the image data that the workload required to start.




## Clean up

To avoid charges, delete the clusters you created in the previous examples:
    
    
    gcloud container clusters delete CLUSTER_NAME CLUSTER2_NAME \
        --location=CONTROL_PLANE_LOCATION
    

Replace the following:

  * `CLUSTER_NAME`: the name of your first cluster.
  * `CLUSTER2_NAME`: the name of your second cluster.
  * `CONTROL_PLANE_LOCATION`: the [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of the clusters.



## Disable Image streaming

If you use GKE Autopilot, you can't disable Image streaming on individual clusters. However, you can disable the Container File System API for the entire project, which disables Image streaming by reverting to standard image pulls.

If you use GKE Standard clusters, you can disable Image streaming on individual clusters or specific node pools, as described in the following sections.

### Disable Image streaming on a GKE Standard cluster

You can disable Image streaming on existing GKE Standard clusters using the gcloud CLI or the Google Cloud console.

### gcloud

To disable Image streaming on an existing cluster, run the following command:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        **--no-enable-image-streaming**
    

Replace the following:

  * `CLUSTER_NAME`: the name of your cluster.
  * `CONTROL_PLANE_LOCATION`: the [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster.



### Console

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Click the name of the cluster you want to modify.

  3. On the **Clusters** page, under **Features** , click _edit_ next to **Image streaming**.

  4. In the **Edit Image streaming** dialog box, clear the **Enable Image streaming** checkbox.

  5. Click **Save changes**.




Changing the Image streaming setting respects maintenance availability when updated at the cluster level, but not at the node pool level.

This change requires recreating the nodes, which can cause disruption to your running workloads. For details about this specific change, find the corresponding row in the [manual changes that recreate the nodes using a node upgrade strategy and respecting maintenance policies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#manual-changes-respecting-policies) table. To learn more about node updates, see [Planning for node update disruptions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#plan-node-disruption).

**Important:** GKE respects maintenance policies when recreating the nodes for this change using the node upgrade strategy, and depends on [resource availability](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-upgrades-quota). Disabling node auto-upgrades [doesn't prevent this change](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades#disable-only-versions). To manually apply the changes to the nodes, use the gcloud CLI to call the [`gcloud container clusters upgrade`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/upgrade) command, passing the `--cluster-version` flag with the same GKE version that the node pool is already running.

### On a new node pool

To disable Image streaming when creating a new node pool, specify the `--no-enable-image-streaming` flag, such as in the following command:
    
    
    gcloud container node-pools create NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        **--no-enable-image-streaming**
    

### On auto-created node pools

GKE Standard clusters use the cluster-level configuration to determine whether to enable Image streaming on new node pools that were created by using [node pool auto-creation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning).

With GKE version 1.34.1-gke.1279000 or later, you can also individually control Image streaming on node pools that were created by a [ComputeClass](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#imageStreaming) by specifying the `spec.nodePoolConfig.imageStreaming` attribute:
    
    
    apiVersion: cloud.google.com/v1
    kind: ComputeClass
    metadata:
      name: image-streaming-class
    spec:
      nodePoolConfig:
        imageStreaming
          enabled: true
      priorities:
      - machineFamily: n4
      nodePoolAutoCreation:
        enabled: true
    

### On an existing node pool

To disable Image streaming on an existing node pool, run the following command:
    
    
    gcloud container node-pools update NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        **--no-enable-image-streaming**
    

Replace the following:

  * `NODE_POOL_NAME`: the name of your node pool.
  * `CLUSTER_NAME`: the name of the cluster for the node pool.
  * `CONTROL_PLANE_LOCATION`: the [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster.



Changing the Image streaming setting respects maintenance availability when updated at the cluster level, but not at the node pool level.

This change requires recreating the nodes, which can cause disruption to your running workloads. For details about this specific change, find the corresponding row in the [manual changes that recreate the nodes using a node upgrade strategy without respecting maintenance policies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#manual-changes-strategy-but-no-respect-policies) table. To learn more about node updates, see [Planning for node update disruptions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#plan-node-disruption).

**Caution:** GKE immediately begins recreating the nodes for this change using the node upgrade strategy, regardless of active maintenance policies. GKE depends on [resource availability](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-upgrades-quota) for the change. Disabling node auto-upgrades [doesn't prevent this change](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades#disable-only-versions). Ensure that your workloads running on the nodes are prepared for disruption before you initiate this change.

## Memory reservation for Image streaming

GKE reserves memory resources for Image streaming in addition to the memory that is reserved for node system components to run. GKE does not reserve additional CPU resources for Image streaming. In GKE Standard clusters, this reservation changes the memory resources that are available for you to request in your Pods. In GKE Autopilot, GKE manages system allocations, so there's no impact to scheduling your workloads.

For details about the memory reservations GKE makes for node components, see [Standard cluster architecture](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#memory_cpu).

In nodes that use Image streaming, GKE makes the following additional memory reservations for new reservations:

  * No additional memory for machines with less than 1 GiB of memory
  * 1% of the first 4 GiB of memory
  * 0.8% of the next 4 GiB of memory (up to 8 GiB)
  * 0.4% of the next 8 GiB of memory (up to 16 GiB)
  * 0.24% of the next 112 GiB of memory (up to 128 GiB)
  * 0.08% of any memory above 128 GiB

**Note:** Memory reservations for Image streaming are made on top of existing memory reservations for node system components. For example, the total reserved memory for the first 4 GiB of memory would be 26% (25% for node components and 1% for Image streaming).

## Troubleshooting

The following sections provide advice on troubleshooting Image streaming. For advice on troubleshooting standard image pulls, see [Troubleshoot image pulls](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/image-pulls).

### GKE doesn't use the Image streaming file system

If your GKE event log doesn't show the Image streaming events, your image is not backed by the remote file system. If GKE previously pulled the image on the node, this is expected behavior because GKE uses the local cache of the image for subsequent pulls instead of using Image streaming. You can verify this by looking for `Container image IMAGE_NAME already present on machine` in the `Message` field for the Pod `Pulled` event.

If you don't see the Image streaming event during the first image pull on the node, ensure that you meet the requirements for Image streaming. If you meet the requirements, you can diagnose the issue by checking the logs of the Image streaming Service (named `gcfsd`):

  1. Go to the **Logs Explorer** page in the Google Cloud console:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. In the **Query** field, specify the following query:
         
         logName="projects/PROJECT_ID/logs/gcfsd"
         resource.labels.cluster_name="CLUSTER_NAME"
         

Replace the following:

     * `PROJECT_ID`: The name of your project.
     * `CLUSTER_NAME`: The name of your cluster.
  3. Click **Run query**.




You can also check the `gcfsd` logs using Logs Explorer:

  1. Go to the **Logs Explorer** in the Google Cloud console:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. In the **Query** field, specify the following query:
         
         logName="projects/PROJECT_ID/logs/gcfsd"
         

Replace `PROJECT_ID` with your Google Cloud project ID.




#### PermissionDenied

If the `gcfsd` logs display an error message similar to the following, the node doesn't have the correct API scope. GKE pulls container images for workloads without using Image streaming.
    
    
    level=fatal msg="Failed to create a Container File System client: rpc error:
    code = PermissionDenied desc = failed to probe endpoint: rpc error: code = PermissionDenied
    desc = Request had insufficient authentication scopes."
    

You can fix this by granting the correct scope to the node to allow it to use Image streaming. Add the `devstorage.read_only` scope to the cluster or node pool, similar to the following command:
    
    
    gcloud container node-pools create NODE_POOL_NAME \
        --cluster=CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --image-type=IMAGE_TYPE \
        --enable-image-streaming \
        **--scopes ="https://www.googleapis.com/auth/devstorage.read_only"**
    

#### FailedPrecondition

If you notice an error message with `code = FailedPrecondition`, the image wasn't imported to the Image streaming remote file system.

You might notice this error if you tried to use Image streaming with an existing node pool. If a node in the node pool already has the container image on-disk, GKE uses the local image instead of using Image streaming to get the image.

To fix this, try the following:

  * Wait a few minutes and try to deploy your workload again.
  * Add new nodes or a new node pool and schedule the workload on those nodes.



#### InvalidArgument

If you notice an error message with `code=InvalidArgument`, the container image your workload uses is not eligible for Image streaming. Ensure that the image meets the requirements. If your image is not on Artifact Registry, try migrating to Artifact Registry.

#### `backend.FileContent failed`

The following error might appear when reading container files with Image streaming enabled:
    
    
    level=error msg="backend.FileContent failed" error="rpc error: code = ResourceExhausted desc = Quota exceeded for quota metric 'Content requests per project per region' and limit 'Content requests per project per region per minute per region' of service 'containerfilesystem.googleapis.com' for consumer 'project_number:PROJECT_NUMBER'." layer_id="sha256:1234567890" module=gcfs_backend offset=0 path=etc/passwd size=4096
    

This error indicates project has exceeded the quota required to read files from the remote container file system service. To help resolve this issue, [request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase) to increase the following quota values:

  * Content requests per project per region per minute per region
  * Content requests per project per region



### Stale file handles after a service restart

If the Image streaming service (`gcfsd`) restarts on a node, running containers that use image streaming might encounter disk I/O errors, such as `stale file handle`, when they try to access files in the container image.

To resolve this issue, restart the affected Pods or containers. When the containers restart, GKE re-establishes the connection to the image streaming service. New Pods scheduled to the node after the service restart are not affected.

### GKE downloads the image without streaming the data

Container images using [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/using-cmek) are only eligible for Image streaming on GKE version 1.25.3-gke.1000 or later. Container images with duplicate layers are not eligible for Image streaming. See the Limitations for more information.

#### Checking for empty layers or duplicate layers

To check the container image for empty layers or duplicate layers, run the following command:
    
    
    docker inspect IMAGE_NAME
    

Replace `IMAGE_NAME` with the name of the container image.

In the output of the command, inspect the entries under `"Layers"`.

If one of the entries **exactly matches the following`"sha256"` output**, the container image has an empty layer and is not eligible for Image streaming.
    
    
    "Layers": [
      ...
      **"sha256:a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4"** ,
      ...
    ]
    

If there are duplicate entries like in the following example, the container image has duplicate layers and is not eligible for Image streaming.
    
    
    "Layers": [
      "sha256:28699c71935fe3ffa56533db44ad93e5a30322639f7be70d5d614e06a1ae6d9b",
      ...
      "sha256:28699c71935fe3ffa56533db44ad93e5a30322639f7be70d5d614e06a1ae6d9b",
      ...
    ]
    

### `mv` command and `renameat2` system calls fail on symlink files

For GKE nodes running version 1.25 and later, when Image streaming is enabled, the `mv` command and `renameat2` system call might fail on symlink files in container images with the error message "No such device or address". The issue is caused by a regression on recent Linux kernels.

These system calls are not common, so the majority of images are not affected by this problem. The issue typically happens on container initialization stages when an application is being prepared to run and move around files. It is not possible to test the image locally, so GKE recommends to use Image streaming on test environments to find the issue before the image is used in production.

The fix is available in the following GKE patch versions:

  * 1.25: 1.25.14-gke.1351000 and later
  * 1.26: 1.26.9-gke.1345000 and later
  * 1.27: 1.27.6-gke.100 and later
  * 1.28: 1.28.1-gke.1157000 and later



Alternatively, to mitigate this issue for any affected workloads, you can try replacing the code leading to the `renameat2` system call. If you cannot modify the code, you must disable Image streaming on the node pool to mitigate the issue.

## What's next

  * Learn how to [use secondary boot disks to preload data or container images](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/data-container-image-preloading).
  * Learn how to [troubleshoot GKE](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting).
  * Learn about [GKE cluster autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
