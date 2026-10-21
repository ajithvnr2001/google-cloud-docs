---
url: https://docs.cloud.google.com/kubernetes-engine/docs/archive/windows-server-sac/
title: Windows Server Semi-Annual Channel end of servicing \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:29:29.464857+00:00
---

# Windows Server Semi-Annual Channel end of servicing  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/archive/windows-server-sac/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Windows Server Semi-Annual Channel end of servicing Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page provides information about the end of servicing for Windows Server Semi-Annual Channel (SAC) node image types in Google Kubernetes Engine (GKE) Standard clusters. For instructions to migrate to supported node images, refer to Migrate to supported Windows images.

## About the Windows Server SAC removal

[Microsoft is retiring the Windows Server Semi-Annual Channel on August 9, 2022](https://docs.microsoft.com/en-us/windows-server/get-started/servicing-channels-comparison#semi-annual-channel). This coincides with the [end of servicing for Windows Server, version 20H2](https://docs.microsoft.com/en-us/windows-server/get-started/windows-server-release-info). Windows Server will use the Long-Term Servicing Channel (LTSC) as the primary release channel. With this change, Microsoft will no longer release critical updates, including security updates, for Windows Server SAC images. As a result of this, GKE can no longer provide support for these images.

GKE Standard will no longer let you create **new node pools** that use Windows Server SAC image types. If you use one of the following image types in your existing node pools, you must migrate to a supported image type if you want to upgrade your GKE version.

  * `windows_sac`: Windows Server SAC with Docker
  * `windows_sac_containerd`: Windows Server SAC with containerd



Your existing Windows Server SAC node pools will continue to function as expected after August 9, 2022. However, you risk exposing these nodes to security vulnerabilities and platform instability because of the lack of future updates for SAC.

## Timeline and milestones

After **August 9, 2022** , you can no longer do the following:

  * Create new clusters that use Windows Server SAC node images.
  * Create new node pools that use Windows Server SAC node images.
  * Enable node auto-provisioning with the `--autoprovisioning-image-type` flag set to `windows_sac` or `windows_sac_containerd`.
  * Upgrade the GKE version of existing Windows Server SAC nodes.



## What should you do?

We recommend that you migrate your Windows Server SAC node pools to the `windows_ltsc_containerd` node image type. In GKE version 1.23 and later, this is the only supported Windows Server image type for new clusters and node pools.

The `windows_ltsc` image type, which uses Docker as the container runtime, is not supported in GKE version 1.23 and later because of the [Docker node image deprecation](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/docker-containerd).

Depending on your current GKE version, do the following:

  * **GKE version 1.20 and earlier** : Migrate your node pools to the `windows_ltsc` image.
  * **GKE version 1.21 and later** : Migrate your node pools to the `windows_ltsc_containerd` image.



### Impact of migrating

If you currently use the `windows_sac` image, which has Docker as the container runtime, migrating to the `windows_ltsc_containerd` image type might impact any of your existing tooling that depends on Docker commands. For information on the potential impact of migrating to an image type that uses containerd, refer to the list of situations in [About the Docker node image deprecation](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/docker-containerd#impact_of_migrating).

## Migrate to Windows Server LTSC

The migration process consists of the following steps:

  1. Identify container images for architecture updates
  2. Build multi-arch Windows container images
  3. Update existing node pools to Windows Server LTSC 



### Identify container images for architecture updates

Single-architecture container images running on Windows Server SAC aren't compatible with Windows Server LTSC images. You'll need to identify incompatible container images and prepare to update their architecture. If you have multi-arch images, you should inspect them to make sure that the images support the Windows Server 2019 LTSC variant, which has the version number `10.0.17763.X`.

### Single-arch images

To inspect the supported Windows version, run the following command from inside a Windows Server SAC node where the Pod is running:
    
    
    docker image inspect IMAGE_NAME
    

Replace `IMAGE_NAME` with the name of the container image.

If the image supports the Windows Server SAC variant, the output is similar to the following:
    
    
    [
      {
        ...
        "Architecture": "amd64",
        "Os": "windows",
        "OsVersion": "10.0.**19042**.1645" // 1645 can be any build number
      }
    ]
    

If the image supports the Windows Server LTSC variant, the output is similar to the following:
    
    
    [
      {
        ...
        "Architecture": "amd64",
        "Os": "windows",
        "OsVersion": "10.0.**17763**.2686" // 2686 can be any build number
      }
    ]
    

### Multi-arch images

If you already use multi-arch Windows container images, inspect the images to ensure that they support the Windows Server 2019 LTSC variant, which has the version number `10.0.17763.X`.
    
    
    docker manifest inspect MANIFEST_NAME
    

Replace `MANIFEST_NAME` with the name of your Docker manifest, such as `eu.gcr.io/gke-release-staging/internet-explorer:v2`.

The output is similar to the following:
    
    
    {
      {
        "mediaType": "application/vnd.docker.distribution.manifest.v2+json",
        "size": 1575,
        "digest": "...",
        "platform": {
            "architecture": "amd64",
            "os": "windows",
            "os.version": "10.0.**17763**.1935"
    
      }
    }
    

### Build multi-arch Windows container images

After you identify any images that need updates to support the Windows Server 2019 LTSC variant, we recommend that you build multi-arch Windows Server images.

Building multi-arch images ensures that your containers run on any Windows version offered by GKE. Multi-arch images will ease your migration experience, because containerd detects the Windows Server LTSC version on your migrated node pools and chooses the appropriate image from your manifest.

You can build these images manually, or by using the Cloud Build gke-windows-builder. We recommend the Cloud Build builder, which is regularly updated to support new Windows Server LTSC images as they become available. For both manual and Cloud Build instructions for multi-arch images, refer to [Building Windows Server multi-arch images](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/building-windows-multi-arch-images).

### Upgrade nodes to Windows Server LTSC

After you update your container images to support the Windows Server LTSC variant, migrate your node pools to the Windows Server LTSC node image. We strongly recommend that you test the migration in a staging or test cluster to ensure that your deployments work as intended before upgrading your production environment. To update your image, do one of the following:

  * Create new node pools and migrate workloads to the new nodes
  * Upgrade the image type on your existing node pools




### Create new node pools

  1. Create a new node pool:
         
         gcloud container node-pools create NODE_POOL_NAME \
             --cluster=CLUSTER_NAME \
             --image-type=WINDOWS_LTSC_IMAGE
         

Replace the following:

     * `NODE_POOL_NAME`: the name of your new node pool.
     * `CLUSTER_NAME`: the name of your GKE cluster.
     * `WINDOWS_LTSC_IMAGE`: the Windows Server LTSC image to use, which can be `windows_ltsc_containerd` or `windows_ltsc`.
  2. Add the following nodeSelector to your workload manifests:
         
         spec:
           ...
           nodeSelector:
             kubernetes.io/os: windows
             cloud.google.com/gke-os-distribution: windows_ltsc
         

You can also use this nodeSelector with `windows_sac` as the label value to tell GKE to avoid scheduling specific Pods on the new nodes.

  3. Deploy your updated manifests:
         
         kubectl apply -f MANIFEST_NAME
         

  4. Scale your old node pool to zero:
         
         gcloud container node-pools update OLD_POOL \
             --cluster=CLUSTER_NAME \
             --min-nodes=0 \
             --max-nodes=NODE_COUNT
         

Replace the following:

     * `OLD_POOL`: the name of your existing Windows Server SAC node pool.
     * `NODE_COUNT`: the maximum number of nodes in the node pool. Gradually scale this number down to 0 by repeating this command. If you encounter issues, scale this value back up.
  5. When fully migrated, delete the old node pool:
         
         gcloud container node-pools delete OLD_POOL \
             --cluster=CLUSTER_NAME
         




### Update existing node pools

  1. Switch the node image type on your existing Windows Server SAC node pools:
         
         gcloud container clusters upgrade CLUSTER_NAME \
             --location=CONTROL_PLANE_LOCATION \
             --node-pool=NODE_POOL \
             --image-type=WINDOWS_LTSC_IMAGE
         

Replace the following:

     * `CLUSTER_NAME`: the name of your GKE cluster.
     * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.
     * `NODE_POOL`: the name of your Windows Server SAC node pool.
     * `WINDOWS_LTSC_IMAGE`: the Windows Server LTSC image to use, which can be `windows_ltsc_containerd` or `windows_ltsc`.



## What's next

  * [Learn about the supported node image types](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images).
  * [Learn how to build multi-arch Windows Server images](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/building-windows-multi-arch-images).
  * [Learn how to configure Windows nodes to automatically join an Active Directory domain](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/auto-join-windows-nodepools).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
