---
url: https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/sample-yaml-files/
title: Optimize performance with pre-configured GKE YAML files \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:29:22.126629+00:00
---

# Optimize performance with pre-configured GKE YAML files  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/sample-yaml-files/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Optimize performance with pre-configured GKE YAML files Stay organized with collections  Save and categorize content based on your preferences. 

Pre-configured Google Kubernetes Engine YAML files help you optimize Cloud Storage FUSE performance for your specific workload and quickly deploy GKE pods that access your Cloud Storage bucket. This document provides sample Cloud Storage FUSE configurations for training, serving, and checkpointing workloads.

**Note:** This page provides instructions for tuning Cloud Storage FUSE performance in Google Kubernetes Engine-specific pre-configured YAML files. To learn about tuning Cloud Storage FUSE using the configuration file and `gcsfuse` options, see [Cloud Storage FUSE performance tuning best practices](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/performance).

## Configure and deploy GKE workloads with Cloud Storage FUSE using sample YAML files

To utilize sample configurations, perform the following steps:

  1. Verify that the Cloud Storage FUSE CSI driver for Google Kubernetes Engine is running on GKE clusters of GKE versions 1.32.2-gke.1297001 or later.

  2. Verify that the Google Kubernetes Engine service account possesses the necessary permissions to access the target Cloud Storage bucket.

  3. Locate the sample configurations you want to apply based on your machine type and workload by using one of the following YAML files:

### GPU

Use one of the following Cloud GPUs-specific YAML files based on your workload type:

     * [Training](https://github.com/GoogleCloudPlatform/gcsfuse/blob/master/samples/gke-csi-yaml/gpu/training-pv.yaml)

     * [Serving](https://github.com/GoogleCloudPlatform/gcsfuse/blob/master/samples/gke-csi-yaml/gpu/serving-pv.yaml)

     * [Checkpointing and JIT cache](https://github.com/GoogleCloudPlatform/gcsfuse/blob/master/samples/gke-csi-yaml/gpu/checkpointing-pv.yaml)

### TPU

Use one of the following Cloud TPU-specific YAML files based on your workload type:

     * [Training](https://github.com/GoogleCloudPlatform/gcsfuse/blob/master/samples/gke-csi-yaml/tpu/training-pv.yaml)

     * [Serving](https://github.com/GoogleCloudPlatform/gcsfuse/blob/master/samples/gke-csi-yaml/tpu/serving-pv.yaml)

     * [Checkpointing and JIT cache](https://github.com/GoogleCloudPlatform/gcsfuse/blob/master/samples/gke-csi-yaml/tpu/checkpointing-pv.yaml)

  4. Deploy the corresponding pod specification that accesses the `PersistentVolumeClaim` using one the following YAML files:

### GPU

Deploy the corresponding Cloud GPUs-specific pod specification that accesses the `PersistentVolumeClaim` based on your workload type:

     * [Training](https://github.com/GoogleCloudPlatform/gcsfuse/blob/master/samples/gke-csi-yaml/gpu/training-pod.yaml)

     * [Serving](https://github.com/GoogleCloudPlatform/gcsfuse/blob/master/samples/gke-csi-yaml/gpu/serving-pod.yaml)

     * [Checkpointing and JIT cache](https://github.com/GoogleCloudPlatform/gcsfuse/blob/master/samples/gke-csi-yaml/gpu/checkpointing-pod.yaml)

### TPU

Deploy the corresponding Cloud TPU-specific pod specification that accesses the `PersistentVolumeClaim` based on your workload type:

     * [Training](https://github.com/GoogleCloudPlatform/gcsfuse/blob/master/samples/gke-csi-yaml/tpu/training-pod.yaml)

     * [Serving](https://github.com/GoogleCloudPlatform/gcsfuse/blob/master/samples/gke-csi-yaml/tpu/serving-pod.yaml)

     * [Checkpointing and JIT cache](https://github.com/GoogleCloudPlatform/gcsfuse/blob/master/samples/gke-csi-yaml/tpu/checkpointing-pod.yaml)

  5. Deploy the `PersistentVolume` and `PersistentVolumeClaim` by applying the `PersistentVolume` file.

The GKE pod admission webhook inspects the `PersistentVolume` attributes to apply potential optimizations such as the injection of sidecar containers before the pod is scheduled.
         
         kubectl apply -f PERSISTENT_VOLUME_YAML_FILE_NAME
         

Replace the following:

     * `PERSISTENT_VOLUME_YAML_FILE_NAME` is the name of the PersistentVolume YAML filename. For example, `serving-pv.yaml`.
  6. Deploy the pod specification that references the `PersistentVolumeClaim`:
         
         kubectl apply -f POD_YAML_FILE_NAME
         

Replace the following:

     * `POD_YAML_FILE_NAME` is the name of the pod YAML configuration file. For example, `serving-pod.yaml`.



## What's next

  * [Learn how to monitor Cloud Storage FUSE performance using metrics](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/metrics).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
