---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/build-multi-arch-for-arm/
title: Build multi-architecture images for Arm workloads \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:52:29.585956+00:00
---

# Build multi-architecture images for Arm workloads  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/build-multi-arch-for-arm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Build multi-architecture images for Arm workloads Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains what multi-architecture (multi-arch) images are, why the architectures of nodes and container images are important, and why multi-arch images make deploying workloads to GKE clusters easier. This page also provides guidance about how you can check if your workloads are ready to run on Arm, and how you can build multi-arch images.

For a tutorial about deploying across architectures with multi-arch images, see [Migrate x86 application on GKE to multi-arch with Arm](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/migrate-x86-to-multi-arch-arm).

**Note:** The instructions on this page provide just one path for how you can check for Arm readiness and build multi-arch images. We recommend that you consult the documentation for these tools and develop your own path for accomplishing these tasks, based on your environment and workload needs. The third-party tools used here are not supported by GKE and could change at any time without notice.

## What is a multi-arch image?

A [multi-arch image](https://www.docker.com/blog/multi-arch-build-and-images-the-simple-way/) is an image that can support multiple architectures. It looks like a single image with a single tag, but it is a list of images targeting multiple architectures organized by a manifest list. Multi-arch images are compatible with the [Docker Image Manifest V2 Scheme 2](https://docs.docker.com/registry/spec/manifest-v2-2/) or [OCI Image Index Specifications](https://github.com/opencontainers/image-spec/blob/master/image-index.md). When you deploy a multi-arch image to a cluster, GKE automatically chooses the right image that is compatible with the architecture of the node to which it is being deployed. Once you have a multi-arch image for a workload, you can seamlessly deploy this workload across multiple architectures.

Multi-arch images are most useful when you want to use the same workload across architectures. Alternatively, you can use container images with a single architecture with any types of GKE nodes. If you are only using a workload on one architecture and you already have a compatible image, you do not need to build a multi-arch image.

If you are using a single-arch image or multi-arch image that is Arm-compatible and you want to deploy it to an Arm node, you must follow the instructions to include the necessary fields so that GKE schedules the workload as expected. To learn more, see [Prepare an Arm workload for deployment](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/prepare-arm-workloads-for-deployment). You do not need to add these fields to schedule workloads if the workloads are only going to be scheduled to x86-based nodes.

## Why is the architecture of a GKE node important for workloads?

[GKE nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#nodes) are individual Compute Engine VM instances which GKE creates and manages on your behalf. Each node is of a standard machine type (for example, `t2a-standard-1`) which uses either x86 (Intel or AMD) or Arm processors. To learn more see, [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).

**You must use container images that are compatible with the architecture of the node where you intend to run the workloads.** For example, if you want to run a container image with the `arm64` architecture, you must a machine type that supports Arm workloads, such as `t2a-standard-1` from the [Tau T2A machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#t2a_machines). You can use nodes with multiple architecture types in one GKE cluster. If you want to use one workload across multiple architecture types, you must keep all of the container images and deployment files for the architecture-specific images organized. Multi-arch images make the process of deploying across architecture types simpler.

## Build multi-arch image to deploy across x86 and Arm nodes

**Warning:** The following instructions provide guidance on how you can check for Arm readiness and build multi-arch images. These examples use unsupported third-party tools that could change at any time without prior notice from GKE.

The following instructions are for App Developers who already have:

  * a build environment with a downloaded container tool (for example, Docker).
  * an existing container image.



The following commands use [Docker](https://docs.docker.com/), but you might be able to use other container tools to accomplish the same tasks.

### Is my workload ready for Arm?

If you have an existing container image, you can check if this workload is ready to run on an Arm node. The following sections explain how to do this by using [`docker run`](https://docs.docker.com/engine/reference/commandline/run/) to attempt to run the container with the Arm architecture.

#### Prepare Docker in your x86 environment to check a container image

If you are running Docker in an x86 environment, you must download additional packages to run an `arm64` container image. These instructions use `apt` for package management, but you can use your environment's package manager to download the required packages.

If you are running Docker in an Arm environment, you can skip this section.

The following commands download packages and register [QEMU](https://www.qemu.org/docs/master/) as the binfmt interpreter for architectures that your machine does not support:
    
    
    sudo apt-get install qemu binfmt-support qemu-user-static
    docker run --rm --privileged multiarch/qemu-user-static --reset -p yes
    

After setting your binfmt interpreters, you can run the `arm64` image in your x86 environment.

#### Check the workload for Arm readiness

If you are running Docker in an Arm environment, or have prepared your x86 environment for running Arm images, run the following command:
    
    
    docker run --platform linux/arm64 IMAGE_NAME
    

Replace `IMAGE_NAME` with the name of the container image.

The following output indicates that your container image is ready to run on Arm nodes with your GKE cluster:
    
    
    Hello from Docker!
    This message shows that your installation appears to be working correctly.
    

If your workload is ready to run on Arm, you can proceed to [Prepare an Arm workload for deployment](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/prepare-arm-workloads-for-deployment).

The following output indicates that your image is not ready to run on Arm:
    
    
    Unable to find image 'hello-world:latest' locally
    latest: Pulling from library/hello-world
    93288797bd35: Pull complete
    Digest: sha256:507ecde44b8eb741278274653120c2bf793b174c06ff4eaa672b713b3263477b
    Status: Downloaded newer image for hello-world:latest
    standard_init_linux.go:219: exec user process caused: exec format error
    

This output indicates that this is an `x86_64` or `amd64` image and you must build an `arm64` image. Proceed to the next section, Build a multi-arch image, where you can use a non-Arm-compatible container image, a Dockerfile, and build a multi-arch image that can run across architecture types.

## Build a multi-arch image

If you have a Dockerfile, you can use it to build an Arm-compatible and x86-compatible multi-arch image that you can deploy across nodes with different architecture types.

You must download [Docker Buildx](https://docs.docker.com/buildx/working-with-buildx/) to complete the following steps. You must also have an existing Dockerfile.

### Prepare your environment if you have an x86 VM and Arm VM

The following commands assume that you have both an Arm build VM and an x86 build VM in your build environment, and your x86 VM can SSH as root into your Arm VM. If you only have an x86 VM in your build environment, follow the instructions in the next section, Prepare your environment if you only have an x86 VM.

Prepare your environment to build multi-arch images:

  1. Create a context for the x86 node using the local socket, and a context for the Arm node using SSH:
         
         docker context create amd_node --docker "host=unix:///var/run/docker.sock"
          docker context create arm_node --docker "host=ssh://root@NODE_IP"
         

Replace `NODE_IP` with the IP address of the Arm node.

  2. Create a builder using the x86 node:
         
         docker buildx create --use --name BUILDER_NAME --platform linux/amd64 amd_node
         docker buildx create --append --name BUILDER_NAME --platform linux/arm64 arm_node
         

Replace `BUILDER_NAME` with a name that you choose for the Buildx builder.




### Prepare your environment if you only have an x86 VM

If you only have an x86 VM in your build environment, you can follow these steps to prepare your environment to build multi-arch images. With this option, the build step might take longer.

  1. Install [QEMU](https://www.qemu.org/docs/master/) packages:
         
         docker run --rm --privileged multiarch/qemu-user-static
         

  2. Create a multi-arch builder (the default builder does not support multi-arch):
         
         docker buildx create --name BUILDER_NAME --use
         

Replace `BUILDER_NAME` with a name that you choose for the Buildx builder.




### Build the image

Now that your environment is ready, run the following command to build a multi-arch image:
    
    
    docker buildx build . -t PATH_TO_REGISTRY  --platform linux/amd64,linux/arm64 --push
    

Replace `PATH_TO_REGISTRY` with the path to your registry, ending with the name of your container image and a tag (for example, `gcr.io/myproject/myimage:latest`).

If you get an error message at this step, refer to the [Docker guide](https://www.docker.com/blog/multi-arch-build-and-images-the-simple-way/) and associated documentation to troubleshoot further.

Once you have built a multi-arch image, your workload is ready to run on Arm. Proceed to [Prepare an Arm workload for deployment](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/prepare-arm-workloads-for-deployment).

## What's next

  * [Prepare an Arm workload for deployment](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/prepare-arm-workloads-for-deployment)
  * [Migrate x86 application on GKE to multi-arch with Arm](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/migrate-x86-to-multi-arch-arm)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
