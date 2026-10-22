---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cloud-storage-fuse-csi-driver/
title: About Cloud Storage FUSE CSI driver for GKE \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:32:10.182417+00:00
---

# About Cloud Storage FUSE CSI driver for GKE  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cloud-storage-fuse-csi-driver/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  About Cloud Storage FUSE CSI driver for GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This overview introduces the [Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/gcs-fuse) CSI driver for mounting [Cloud Storage buckets](https://docs.cloud.google.com/storage/docs/buckets) as local file systems in Google Kubernetes Engine (GKE). This feature is particularly useful for machine learning workloads that need to store training data, models, and checkpoints in Cloud Storage.

This overview is for Developers and Data scientists who want to access or store training data, inference model weights, and checkpoints stored in Cloud Storage from their Kubernetes applications.

Before reading this page, ensure you're familiar with Kubernetes, GKE, and Cloud Storage.

**Tip:** To get started, follow the [Cloud Storage FUSE CSI driver quickstart](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/cloud-storage-fuse-csi-driver).

## How it works

The driver uses the [Container Storage Interface](https://github.com/container-storage-interface) (CSI) standard to allow your applications running in Pods to seamlessly access Cloud Storage buckets as if they were mounted filesystems. This means you can treat your Cloud Storage buckets as a persistent and scalable data source for your Kubernetes applications without complex configuration or code changes.

The Cloud Storage FUSE CSI driver provides a fully-managed experience powered by the open source [Google Cloud Storage FUSE CSI plugin](https://github.com/GoogleCloudPlatform/gcs-fuse-csi-driver). The CSI driver lets you use the Kubernetes API to consume pre-existing Cloud Storage buckets as volumes. Your applications can upload and download objects using [Cloud Storage FUSE file system semantics](https://github.com/googlecloudplatform/gcsfuse/blob/master/docs/semantics.md).

[Filesystem in Userspace (FUSE)](https://www.kernel.org/doc/html/next/filesystems/fuse.html) is an interface used to export a file system to the Linux kernel. Cloud Storage FUSE lets you mount Cloud Storage buckets as a file system so that applications can access the objects in a bucket using common File I/O operations (for example, open, read, write, and close) rather than using cloud-specific APIs.

The driver natively supports the following ways for you to configure your Cloud Storage-backed volumes:

  * **CSI ephemeral volumes** : You specify the Cloud Storage bucket in-line with the Pod specification. Use ephemeral CSI volumes if you want a streamlined Pod-based interface that requires no previous experience with Kubernetes persistent volumes. To use this option, see [Mount Cloud Storage buckets as CSI ephemeral volumes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-ephemeral).
  * **PersistentVolumes** : You create a PersistentVolume resource that refers to the Cloud Storage bucket, using static provisioning. Your Pod can then reference a PersistentVolumeClaim that is bound to this PersistentVolume. Use this option if you are already familiar with PersistentVolumes and want consistency with your existing deployments that rely on this resource type. To use this option, see [Mount Cloud Storage buckets as persistent volumes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-pv).



## Use cases

The Cloud Storage FUSE CSI driver is suitable for the scenarios like the following:

### AI and machine learning

  * **Training** : You can use the Cloud Storage FUSE CSI driver to read training data and checkpoint saved models using Cloud Storage as the source of truth. For example, when training a model on GKE using PyTorch, JAX, or TensorFlow, the driver can provide access to training datasets stored in Cloud Storage buckets.
  * **Inference** : You can serve ML inference models that infer results from files stored in Cloud Storage. You can use Cloud Storage FUSE CSI to preload model weights stored in Cloud Storage. Additionally, you can use the [parallel download](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf#parallel-download) with [file cache](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf#file-caching) to accelerate reading large files from Cloud Storage for multi-threaded downloads. You can use this feature to improve model load times, especially for reads of over 1 GB in size



### Data analytics pipelines

You can use the Cloud Storage FUSE CSI driver to streamline data processing tasks by allowing applications to directly access and analyze large datasets stored in Cloud Storage. For example, a Spark job running on GKE could use the CSI driver to process data stored in Cloud Storage without needing to download it first.

## Benefits

Using the CSI driver gives you these benefits:

  * **Easy to set up** : The Cloud Storage FUSE CSI driver automatically deploys and manages the driver on both Standard and Autopilot clusters. Using CSI ephemeral volumes simplifies volume configuration and management. This is because there is no need for PersistentVolumeClaim and PersistentVolume objects.
  * **Security** : The Cloud Storage FUSE CSI driver does not need privileged access. This minimizes the risks associated with privileged access and leads to a better security posture. You can use [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity) to manage authentication, giving you granular control over how your Pods access Cloud Storage objects.
  * **Performance** : For AI/ML workloads, you can use [pre-defined Cloud Storage FUSE profiles](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gcsfuse-profiles) for training, serving, and checkpointing to automatically tune performance based on your workload and node configuration. The Cloud Storage FUSE CSI driver also enhances performance through features like a sidecar for optimized interactions, parallel downloads for faster data access, and metadata and file caching to improve read performance and reduce latency. To learn more about these features, see Performance tuning options and features.
  * **Portability and flexibility:** The Cloud Storage FUSE CSI driver lets you use standard file system semantics to mount and access Cloud Storage buckets. This provides a familiar interface that improves portability for ML workloads, and avoids the need for you to make extensive code or application changes. The driver is supported on all accelerators available on GKE including GPUs and TPUs. The Cloud Storage FUSE CSI driver supports the `ReadWriteMany`, `ReadOnlyMany`, and `ReadWriteOnce` [access modes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes). You can consume Cloud Storage FUSE volumes in init containers.
  * **Manageability** : The driver lets you run Cloud Storage FUSE under the covers without needing to install or manage it. You can also view [metrics insights for Cloud Storage FUSE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf#cloud-storage-fuse-metrics), including file system, Cloud Storage, and file cache usage.



## Performance tuning options and features

The Cloud Storage FUSE CSI driver comes with several performance tuning options and features for optimizing how your Pods access data stored in Cloud Storage buckets.

For example, by enabling file caching and adjusting the request concurrency, you could significantly reduce the time it takes to load the training data, leading to faster training times.

  * **[Native sidecar](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-sidecar)** : The Cloud Storage FUSE CSI driver [attaches a sidecar container in your Pods](https://kubernetes.io/blog/2023/08/25/native-sidecar-containers/) to manage interactions with Cloud Storage. The sidecar handles the mounting and interaction with Cloud Storage, allowing your applications to seamlessly access data. You can fine-tune performance by configuring resources like CPU and memory for the sidecar container, or by adjusting settings related to caching and buffering. The Cloud Storage FUSE CSI driver sidecar container and [Istio](https://istio.io/) can coexist and run concurrently in your Pod.

  * **[Parallel download](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf#parallel-download)** : Starting from GKE version 1.30.3-gke.1571000 and [Cloud Storage FUSE v.2.4.0](https://github.com/GoogleCloudPlatform/gcsfuse/releases/tag/v2.4.0) with file cache enabled, you can use the [parallel download](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf#parallel-download) feature to accelerate reading large files from Cloud Storage for multi-threaded downloads. You can use this feature to improve model load times, especially for reads over 1 GB in size (for example, up to twice as fast when loading Llama 2 70B).

  * **[Metadata caching support](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf#stat-cache)** : The Cloud Storage FUSE CSI driver enhances performance by caching file metadata, like size and modification time. The CSI driver enables this [stat cache](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/caching#stat-cache-overview) by default and reduces latency by storing information locally instead of repeatedly requesting it from Cloud Storage. You can configure its maximum size and the duration for which the data stays in the cache. By fine-tuning the metadata cache, you can reduce API calls to Google Cloud Storage, improving application performance and efficiency by minimizing network traffic and latency.

  * **[File caching support](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf#file-caching)** : You can use the Cloud Storage FUSE CSI driver with [file caching](https://docs.cloud.google.com/storage/docs/gcsfuse-file-cache) to improve the read performance of applications handling small files from Cloud Storage buckets. The Cloud Storage FUSE file cache feature is a client-based read cache that allows repeated file reads to be served more quickly from cache storage of your choice. You can choose from a range of storage options for the read cache, including Local SSDs, Persistent Disk-based storage, and RAM disk, based on your price-performance needs.

  * **[Node restart support](https://github.com/GoogleCloudPlatform/gcs-fuse-csi-driver/blob/main/docs/troubleshooting.md#node-level-restarts)** : Starting from GKE version 1.33.1-gke.1959000, Pods using Cloud Storage FUSE CSI volumes can automatically recover after a GKE node restart. If the Pod is on a node with [Graceful Node Shutdown enabled](https://kubernetes.io/docs/concepts/cluster-administration/node-shutdown/#graceful-node-shutdown), it must be managed by a controller (such as a Job or Deployment) that replaces failed Pods. Meanwhile, standalone Pods can restart automatically on nodes without Graceful Node Shutdown enabled. For GKE versions earlier than 1.33.1-gke.1959000, Pods are unable to recover and you need to redeploy. Graceful Node Shutdown is enabled by default only for preemptible VMs, Spot VMs, Confidential VMs, GPU VMs, TPU VMs, and the Z3, Z4D, C3 Metal, and C4 machine series.




For performance tuning best practices, refer to [Optimize Cloud Storage FUSE CSI driver for GKE performance](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf#best-practices-for-performance-tuning).

## Limitations

The CSI driver has these limitations:

  * The Cloud Storage FUSE file system has [differences in performance, availability, access authorization, and semantics](https://docs.cloud.google.com/storage/docs/gcs-fuse#differences-and-limitations) compared to a POSIX file system.
  * The Cloud Storage FUSE CSI driver is not supported on [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods).
  * The Cloud Storage FUSE CSI driver does not support volume snapshots, volume cloning, or volume expansions.
  * [Uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) is required for read-write workloads when using Workload Identity Federation for GKE.
  * See the [known issues](https://github.com/GoogleCloudPlatform/gcs-fuse-csi-driver/blob/main/docs/known-issues.md) in the Cloud Storage FUSE CSI driver GitHub project.
  * See the [open issues](https://github.com/GoogleCloudPlatform/gcs-fuse-csi-driver/issues) in the Cloud Storage FUSE CSI driver GitHub project.
  * For GKE versions earlier than `1.33.3-gke.1226000`, the Cloud Storage FUSE CSI driver does not support Pods running on the [host network](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#hosts-namespaces) (`hostNetwork: true`) due to [restrictions of Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity#restrictions). However, on Standard GKE clusters with version `1.33.3-gke.1226000` or later, the Pods on the host network that use the Cloud Storage FUSE CSI driver can use their own Kubernetes Service Account to authenticate. For more information, see [Configure access for Pods with host network](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-setup#access-for-pods-with-host-network).
  * GKE cluster versions earlier than 1.32.3-gke.1099000 have a restrictive limit on the size of JSON encrypted `mountOption` strings. The combination of bucket name, user provided mount options, and the driver provided `mountOptions` must be fewer than 500 characters. We increased the threshold of JSON message to 5,000 bytes in GKE cluster versions 1.32.3-gke.1099000 or later.



## Requirements

To use the Cloud Storage FUSE CSI driver, your clusters must meet the following GKE version requirements:

  * Use Linux clusters running GKE version 1.24 or later.
  * Have [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#enable) and [GKE metadata server](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#migrate_applications_to) enabled.
  * Use the latest version of the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud#download_and_install_the).



To use specific features for the Cloud Storage FUSE CSI driver, you also need to meet the requirements specified in the [Cloud Storage FUSE CSI driver repository](https://github.com/GoogleCloudPlatform/gcs-fuse-csi-driver/blob/main/docs/releases.md#requirements).

## What's next

  * [Learn how to prepare to use the Cloud Storage FUSE CSI for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-setup).
  * [Troubleshoot Cloud Storage FUSE ](https://github.com/GoogleCloudPlatform/gcs-fuse-csi-driver/blob/main/docs/troubleshooting.md)
  * [Optimize Cloud Storage FUSE for performance](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
