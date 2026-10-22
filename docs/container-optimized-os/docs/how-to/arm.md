---
url: https://docs.cloud.google.com/container-optimized-os/docs/how-to/arm/
title: Using Arm-based Container-Optimized OS images \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:47.530629+00:00
---

# Using Arm-based Container-Optimized OS images  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/container-optimized-os/docs/how-to/arm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Container-Optimized OS ](https://docs.cloud.google.com/container-optimized-os/docs)
  * [ Guides ](https://docs.cloud.google.com/container-optimized-os/docs/how-to/create-configure-instance)



Send feedback 

#  Using Arm-based Container-Optimized OS images Stay organized with collections  Save and categorize content based on your preferences. 

Starting with [Milestone 101](https://docs.cloud.google.com/container-optimized-os/docs/release-notes/m101), Container-Optimized OS publishes Arm-based OS images. The images can be used to create [Tau T2A VMs](https://docs.cloud.google.com/compute/docs/instances/arm-on-compute) on Compute Engine. To learn more about what types of workloads work well with Tau T2A, see [Workload Recommendations](https://docs.cloud.google.com/compute/docs/instances/arm-on-compute#workload_recommendations). To learn how you can run Arm workloads on Google Kubernetes Engine (GKE), see [Arm workloads on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/arm-on-gke).

## View Arm-based images

Arm-based Container-Optimized OS images are hosted under the `cos-cloud` project with the prefix `cos-arm64`. You can also see all available releases on command line by running the following command:
    
    
    gcloud compute images list --project cos-cloud --no-standard-images  --filter="name~'cos-arm64-*'"
    

The output is similar to the following:
    
    
    NAME                             PROJECT    FAMILY             DEPRECATED  STATUS
    cos-arm64-101-17162-40-5         cos-cloud  cos-arm64-101-lts              READY
    cos-arm64-beta-101-17162-40-5    cos-cloud  cos-arm64-beta                 READY
    cos-arm64-dev-105-17228-0-0      cos-cloud  cos-arm64-dev                  READY
    cos-arm64-stable-101-17162-40-5  cos-cloud  cos-arm64-stable               READY
    

Arm-based Container-Optimized OS images share the same [versioning scheme](https://docs.cloud.google.com/container-optimized-os/docs/concepts/versioning) and [LTS milestone lifecycle](https://docs.cloud.google.com/container-optimized-os/docs/concepts/versioning#lifecycle_of_an_lts_milestone) with x86-based images. There are also similar image families `cos-arm64-dev`, `cos-arm64-beta`, `cos-arm64-stable` and `cos-arm64-[MILESTONE]-lts` for Arm-based Container-Optimized OS images.

## Differences between Arm and x86 images

The Arm-based and x86-based Container-Optimized OS images share the same [source code](https://docs.cloud.google.com/container-optimized-os/docs/resources/sources#image_source), but the build and compile configurations are different. This means that an Arm-based Container-Optimized OS image might not be functionally identical with a x86-based Container-Optimized OS image even if they have the same version.

The following sections describe the differences between Arm-based and x86-based Container-Optimized OS images.

### Kernel

Container-Optimized OS Arm-based images have a separate kernel configuration that is different from x86-based images. The most noticeable difference is that Arm-based images use NVMe interface for storage instead of SCSI interface, and [Google virtual NIC (gVNIC)](https://docs.cloud.google.com/compute/docs/networking/using-gvnic) for networking instead of Virtionet. The [Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview) feature also doesn't work on Arm-based images.

### Cloud Logging agent

Container-Optimized OS Arm-based images use [fluent-bit](https://github.com/fluent/fluent-bit) as [Cloud Logging agent](https://docs.cloud.google.com/container-optimized-os/docs/how-to/logging) and x86-based images use fluentd. You shouldn't see any difference if you only rely on the default logging configuration built into the OS images. However, if you have custom fluentd configurations, you might experience breakage when migrating workloads to Arm-based Container-Optimized OS images. For more information, see the [Cloud Logging agent](https://docs.cloud.google.com/container-optimized-os/docs/how-to/logging).

### Automatic updates

[Automatic updates](https://docs.cloud.google.com/container-optimized-os/docs/concepts/auto-update) are not supported on Container-Optimized OS Arm-based images.

### GPU accelerators

Using graphics processing unit (GPU) hardware accelerators is not supported on Container-Optimized OS Arm-based images.

### Create instances with the `create-with-container` command

Container-Optimized OS Arm-based images don't support creating VM instances with the [`create-with-container`](https://docs.cloud.google.com/container-optimized-os/docs/how-to/create-configure-instance#simple) command. You can use [`cloud-init`](https://docs.cloud.google.com/container-optimized-os/docs/how-to/create-configure-instance#using_cloud-init_with_the_cloud_config_format) to configure Arm-based instances if you want to start containers when instances are created.

### Container images

Container-Optimized OS includes tools that download [containers](https://docs.cloud.google.com/container-optimized-os/docs/resources/sources#container_source) at runtime. The following table describes which containers are compatible with Arm-based images:

Container images | Compatible with Arm-based images  
---|---  
gcr.io/cos-cloud/toolbox | Yes  
gcr.io/cos-cloud/cos-gpu-installer | No  
gcr.io/stackdriver-agents/stackdriver-logging-agent | No  
gcr.io/gce-containers/konlet | No  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
