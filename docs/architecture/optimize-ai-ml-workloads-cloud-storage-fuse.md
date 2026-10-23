---
url: https://docs.cloud.google.com/architecture/optimize-ai-ml-workloads-cloud-storage-fuse/
title: Optimize AI and ML workloads with Cloud Storage FUSE \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:14:01.131861+00:00
---

# Optimize AI and ML workloads with Cloud Storage FUSE  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/optimize-ai-ml-workloads-cloud-storage-fuse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Optimize AI and ML workloads with Cloud Storage FUSE Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-08-22 UTC

This document provides reference architectures that show how you can use [Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/gcs-fuse) to optimize performance for AI and ML workloads on Google Kubernetes Engine (GKE).

The intended audience for this document includes architects and technical practitioners who design, provision, and manage storage for their AI and ML workloads on Google Cloud. This document assumes that you have an understanding of the [ML lifecycle, processes, and capabilities](https://docs.cloud.google.com/architecture/ml-on-gcp-best-practices).

Cloud Storage FUSE is an open source [FUSE](https://github.com/libfuse/libfuse) adapter that lets you mount Cloud Storage buckets as local file systems. This configuration enables applications to seamlessly interact with cloud-based storage buckets by using standard file-like system semantics. Cloud Storage FUSE lets you take advantage of the scalability and cost-effectiveness of Cloud Storage.

**Note:** Cloud Storage FUSE isn't fully compliant with [Portable Operating System Interface (POSIX)](https://en.wikipedia.org/wiki/POSIX). For information about how to select storage services for AI and ML workloads, see [Overview of storage services for AI and ML workloads in AI Hypercomputer](https://docs.cloud.google.com/ai-hypercomputer/docs/storage).

## Architecture

Depending on your requirements for performance, availability, and disaster recovery (DR), you can choose one of the following Google Cloud [deployment archetypes](https://docs.cloud.google.com/architecture/deployment-archetypes#what_is_a_deployment_archetype) to run your AI and ML workloads on Google Cloud:

  * **Regional** : Your applications run independently within a single Google Cloud [region](https://docs.cloud.google.com/docs/geography-and-regions). We recommend this deployment archetype for applications that aren't mission-critical but that need to be robust against zone outages.
  * **Multi-regional** : Your applications run independently across two or more Google Cloud regions, in either active-active or active-passive mode. This deployment archetype is ideal to support DR scenarios. We recommend this deployment archetype for mission-critical applications that need resilience against region outages and disasters. Dual or multi-regional deployments can reduce latency and improve throughput through closer resource proximity.



The deployment archetype that you choose informs the Google Cloud products and features that you need for your architecture. The multi-regional architecture uses [Rapid Cache](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache) to increase network bandwidth and provide lower latency zonal cache hits when compared to a regional bucket. Rapid Cache is generally recommended for all workloads and eliminates data transfer fees when used with multi-region buckets. To assess whether Rapid Cache is suitable for your workload, use the [Rapid Cache recommender](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache-recommender) to analyze your data usage and storage.

The following tabs provide reference architectures for the regional and multi-regional deployment archetypes:

### Regional

The following diagram shows a sample regional architecture that uses Cloud Storage FUSE to optimize the performance of the model training and model serving workflows:

![Regional architecture that uses Cloud Storage FUSE to optimize AI and ML workloads.](https://docs.cloud.google.com/static/architecture/images/gcsfuse-aiml-regional.svg)![](https://docs.cloud.google.com/static/architecture/images/gcsfuse-aiml-regional.svg)

This architecture includes the following components:

  * **GKE cluster** : GKE manages the compute nodes on which your AI and ML model training and serving processes run. GKE manages the underlying infrastructure of the Kubernetes clusters, including the control plane, nodes, and all system components.
  * **Kubernetes scheduler** : The GKE control plane schedules workloads and manages their lifecycle, scaling, and upgrades. The Kubernetes node agent (`kubelet`), which isn't shown in the diagram, communicates with the control plane. The `kubelet` agent is responsible for starting and running containers that are scheduled on the GKE nodes. For more information about the scheduler, see [AI/ML orchestration on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra).
  * **Virtual Private Cloud (VPC) network** : All of the Google Cloud resources in the architecture use a single VPC network. Depending on your requirements, you can choose to build an architecture that uses multiple networks. For more information about configuring a VPC network for Cloud Storage FUSE, see [Deciding whether to create multiple VPC networks](https://docs.cloud.google.com/architecture/best-practices-vpc-design#decide-whether-to-create-multiple-vpcs).
  * **Cloud Load Balancing** : In this architecture, Cloud Load Balancing efficiently distributes incoming inference requests from application users to the serving containers in the GKE cluster. For more information, see [Understanding GKE load balancing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-networking#understanding-load-balancing).
  * **[Graphics Processing Unit (GPU)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus) or [Tensor Processing Units (TPUs)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus)**: GPUs and TPUs are specialized machine accelerators that improve the performance of your AI and ML workloads. For information about how to choose an appropriate processor type, see Accelerator options later in this document.
  * **Cloud Storage** : Cloud Storage provides persistent, scalable, and cost-effective storage for your AI and ML workloads. Cloud Storage serves as the central repository for your raw training datasets, model [checkpoints](https://developers.google.com/machine-learning/glossary#checkpoint), and final trained models.
  * **Cloud Storage FUSE with file cache enabled** : Cloud Storage FUSE lets you mount a Cloud Storage bucket as a local file system. The [file cache](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/caching#file-cache-overview) in Cloud Storage FUSE is a directory on the local machine that stores frequently accessed files from your Cloud Storage buckets. The [Cloud Storage FUSE CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cloud-storage-fuse-csi-driver) manages the integration of Cloud Storage FUSE with the Kubernetes API to consume Cloud Storage buckets as volumes.



The following sections describe the workflow in the training and serving workloads of the architecture.

### Multi-regional

The following diagram shows a sample multi-regional architecture that uses Cloud Storage FUSE and [Rapid Cache](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache) to optimize the performance of the model training and model serving workflows:

![Multi-regional architecture that uses Cloud Storage FUSE to optimize AI and ML workloads.](https://docs.cloud.google.com/static/architecture/images/gcsfuse-aiml-multiregional.svg)![](https://docs.cloud.google.com/static/architecture/images/gcsfuse-aiml-multiregional.svg)

This architecture includes the following components:

  * **GKE cluster** : GKE manages the compute nodes on which your AI and ML model training and serving processes run. GKE manages the underlying infrastructure of the Kubernetes clusters, including the control plane, nodes, and all system components.
  * **Kubernetes scheduler** : The GKE control plane schedules workloads and manages their lifecycle, scaling, and upgrades. The Kubernetes node agent (`kubelet`), which isn't shown in the diagram, communicates with the control plane. The `kubelet` agent is responsible for starting and running containers that are scheduled on the GKE nodes. For more information about the scheduler, see [AI/ML orchestration on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra).
  * **Virtual Private Cloud (VPC) network** : All of the Google Cloud resources in the architecture use a single VPC network. Depending on your requirements, you can choose to build an architecture that uses multiple networks. For more information about configuring a VPC network for Cloud Storage FUSE, see [Deciding whether to create multiple VPC networks](https://docs.cloud.google.com/architecture/best-practices-vpc-design#decide-whether-to-create-multiple-vpcs).
  * **Cloud DNS** : In multi-regional architectures, Cloud DNS directs traffic to the load balancers to ensure optimal performance and availability through [anycast](https://en.wikipedia.org/wiki/Anycast) routing. Requests are automatically routed to the nearest location, which reduces latency and improves authoritative name lookup performance for your users. For information about general principles and best practices, see [Best practices for Cloud DNS](https://docs.cloud.google.com/dns/docs/best-practices).
  * **Cloud Load Balancing** : In this architecture, Cloud Load Balancing efficiently distributes incoming inference requests from application users to the serving containers in the GKE cluster. For more information, see [Understanding GKE load balancing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-networking#understanding-load-balancing).
  * **[Graphics Processing Unit (GPU)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus) or [Tensor Processing Units (TPUs)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus)**: GPUs and TPUs are specialized machine accelerators that improve the performance of your AI and ML workloads. For information about how to choose an appropriate processor type, see Accelerator options later in this document.
  * **Cloud Storage** : Cloud Storage provides persistent, scalable, and cost-effective storage for your AI and ML workloads. Cloud Storage serves as the central repository for your raw training datasets, model [checkpoints](https://developers.google.com/machine-learning/glossary#checkpoint), and final trained models.
  * **Cloud Storage FUSE** : Cloud Storage FUSE lets you mount a Cloud Storage bucket as a local file system. The [Cloud Storage FUSE CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cloud-storage-fuse-csi-driver), which isn't shown in the diagram, manages the integration of Cloud Storage FUSE with the Kubernetes API to consume Cloud Storage buckets as volumes.
  * **Rapid Cache** : Rapid Cache is a feature of Cloud Storage that provides up to 1 PiB of SSD-backed zonal read-only cache for Cloud Storage buckets. During training and serving, Rapid Cache helps you reduce read latencies and achieve throughput that exceeds 2 TB/s by scaling cache capacity and bandwidth. When combined with multi-region buckets, Rapid Cache can be used across multiple zones and multiple regions. For information about supported regions and zones, see [Caching data in zones](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache#supported-locations).



The following sections describe the workflow in the training and serving workloads of the architecture.

### Training workload

In the preceding architectures, the following are the steps in the data flow during model _training_ :

  1. **Load training data to Cloud Storage** : Training data is uploaded to a Cloud Storage bucket with [hierarchical namespaces](https://docs.cloud.google.com/storage/docs/hns-overview) enabled. Cloud Storage serves as a scalable central repository.
  2. **Load training data and run training jobs in GKE** : The Cloud Storage bucket that's mounted to your GKE pods lets your training applications efficiently load and access the training data by using the FUSE interface. The GKE nodes run the model training process by using the mounted file cache as the data source. Your training applications continuously feed training data to the machine accelerators to perform the complex calculations that are required for model training. Depending on your workload requirements, you can use GPUs or TPUs. For information about how to choose an appropriate processor type, see Accelerator options later in this document.
  3. **Checkpoint and model save and restore** :

     * **Save checkpoints or model** : During training, [save checkpoints](https://docs.cloud.google.com/architecture/ml-on-gcp-best-practices#use-training-checkpoints-to-save-the-current-state-of-your-experiment) asynchronously at frequent intervals to a separate Cloud Storage bucket. The checkpoints capture the state of the model based on metrics or intervals that you define.
     * **Restore checkpoints or model** : When your training workload requires that you restore a checkpoint or model data, you need to locate the asset that you want to restore in Cloud Storage. You can use the restored checkpoint or model to resume training, fine-tune parameters, or evaluate performance on a validation set.



### Serving workload

In the preceding architectures, the following are the steps in the data flow during model _serving_ :

  1. **Load model** : After training is complete, your pods load the trained model by using Cloud Storage FUSE with parallel downloads enabled. [Parallel downloads](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/file-caching#parallel-downloads) accelerate model loading by fetching the parts of the model in parallel from Cloud Storage. To significantly reduce model loading times, the process uses the cache directory as a prefetch buffer. 
  2. **Inference request** : Application users send inference requests from the AI and ML application through the Cloud Load Balancing service. Cloud Load Balancing distributes the incoming requests across the serving containers in the GKE cluster. This distribution ensures that no single container is overwhelmed and requests are processed efficiently. 
  3. **Response delivery** : The nodes process the request and generate a prediction. The serving containers send the responses back through Cloud Load Balancing and then to the application users. 



## Products used

The reference architectures use the following Google Cloud products:

  * [ Google Kubernetes Engine (GKE)](https://cloud.google.com/kubernetes-engine): A Kubernetes service that you can use to deploy and operate containerized applications at scale using Google's infrastructure. 
  * [ Cloud Storage](https://cloud.google.com/storage): A low-cost, no-limit object store for diverse data types. Data can be accessed from within and outside Google Cloud, and it's replicated across locations for redundancy.
  * [ Virtual Private Cloud (VPC)](https://cloud.google.com/vpc): A virtual system that provides global, scalable networking functionality for your Google Cloud workloads. VPC includes VPC Network Peering, Private Service Connect, private services access, and Shared VPC.
  * [ Cloud Load Balancing](https://cloud.google.com/load-balancing): A portfolio of high performance, scalable, global and regional load balancers. 
  * [ Cloud DNS](https://cloud.google.com/dns): A service that provides resilient, low-latency DNS serving from Google's worldwide network. 



## Use case

For AI and ML workloads that require large storage capacity and high performance file access, we recommend that you use an architecture that's built around Cloud Storage FUSE. With proper planning, you can achieve over 1 TB/s of throughput with these architectures. Additionally, Cloud Storage FUSE lets you take advantage of a central storage repository that serves as a single source of truth for all of the stages of the AI and ML workflow. This approach can be used for any workloads, regardless of their scale or size.

For these workloads, Cloud Storage FUSE provides the following benefits:

  * **Simplified data access** : Access training data and checkpoints with AI and ML frameworks like [Connector for PyTorch](https://pytorch.org/), [JAX](https://jax.readthedocs.io/en/latest/), and TensorFlow. Access to data through AI and ML frameworks eliminates the need for code refactoring.
  * **Accelerated startup** : Eliminate the need to download large datasets to compute resources by using Cloud Storage FUSE to directly access data in Cloud Storage. This direct access to data leads to faster job startup times.
  * **Cost-effectiveness** : Optimize costs by using the inherent scalability and cost-efficiency of Cloud Storage.



Cloud Storage FUSE isn't suitable for latency-sensitive workloads that contain files less than 50 MB or that require less than 1 millisecond latency for random I/O and metadata access.

For data-intensive training or checkpoint and restart workloads, consider a storage alternative during the I/O intensive training phase.

## Design alternatives

The following sections present alternative design approaches that you can consider for your AI and ML application in Google Cloud.

### Platform alternative

Instead of hosting your model training and serving workflow on GKE, you can consider [Compute Engine](https://cloud.google.com/products/compute) with [Slurm](https://slurm.schedmd.com/overview.html). Slurm is a highly configurable and open source workload and resource manager. Using Compute Engine with Slurm is particularly well-suited for large-scale model training and simulations. We recommend that you use Compute Engine with Slurm if you need to integrate proprietary AI and ML intellectual property (IP) into a scalable environment with the flexibility and control to optimize performance for specialized workloads. For more information about how to use Compute Engine with Slurm, see [Deploy an HPC cluster with Slurm](https://docs.cloud.google.com/cluster-toolkit/docs/quickstarts/slurm-cluster).

On Compute Engine, you provision and manage your virtual machines (VMs), which gives you granular control over instance types, storage, and networking. You can tailor your infrastructure to your exact needs, including the selection of specific VM machine types. For information about how to use the Cloud Storage FUSE command-line options in Compute Engine, see [gcsfuse CLI](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options) and [Cloud Storage FUSE configuration file](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file). You can also use the accelerator-optimized machine family for enhanced performance with your AI and ML workloads. For more information about the machine type families that are available on Compute Engine, see [Machine families resource and comparison guide](https://docs.cloud.google.com/compute/docs/machine-resource).

Slurm offers a powerful option for managing AI and ML workloads and it lets you control the configuration and management of the compute resources. To use this approach, you need expertise in Slurm administration and Linux system management.

### Accelerator options

[Machine accelerators](https://docs.cloud.google.com/tpu/docs/intro-to-tpu) are specialized processors that are designed to speed up the computations that are required for AI and ML workloads. You can choose either GPUs or TPUs.

  * GPU accelerators provide excellent performance for a wide range of tasks, including graphic rendering, deep learning training, and scientific computing. Google Cloud has a wide selection of GPUs to match a range of performance and price points. GPUs often include [local SSDs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/local-ssd) in each machine configuration, which can be used by Cloud Storage FUSE as a cache directory. For information about GPU models and pricing, see [GPU pricing](https://docs.cloud.google.com/compute/gpus-pricing#gpu-pricing).
  * TPUs are custom-designed AI accelerators, which are optimized for training and inference of large AI models. They are ideal for a variety of use cases, such as chatbots, code generation, media content generation, synthetic speech, vision services, recommendation engines, and personalization models. For more information about TPU models and pricing, see [TPU pricing](https://cloud.google.com/tpu/pricing).



### Storage alternatives

Cloud Storage FUSE provides a convenient file system that lets you take advantage of the scalability and cost-effectiveness of Cloud Storage. However, Cloud Storage FUSE isn't ideal for workloads that demand low latency for small file reads or for workloads that require a full POSIX-compliant storage solution. For these use cases, we recommend that you consider the following storage alternatives:

  * **[Google Cloud Managed Lustre](https://docs.cloud.google.com/managed-lustre/docs/overview)** : A fully Google Cloud-managed, persistent parallel file system (PFS) that's based on [DDN's EXAScaler Lustre](https://www.ddn.com/products/lustre-file-system-exascaler/). Managed Lustre is the recommended primary solution for training and checkpointing AI workloads. It is particularly effective for migrating existing workloads from Lustre or other PFS solutions. For increased performance during checkpointing, consider using Managed Lustre to augment Cloud Storage FUSE with Rapid Cache. For more information, see [Optimize AI and ML workloads with Google Cloud Managed Lustre](https://docs.cloud.google.com/architecture/optimize-ai-ml-workloads-managed-lustre).
  * **[Connector for PyTorch](https://docs.cloud.google.com/storage/docs/pytorch-connector)** : An open source product in Cloud Storage that's ideal for workloads that use PyTorch. Connector for PyTorch optimizes your training workload by streaming data directly from your Cloud Storage buckets and eliminating the need for intermediate storage. This direct access and optimization provides significantly better performance than direct API calls to Cloud Storage for data loading, training, and checkpointing.



Although alternative storage options can offer performance advantages for certain AI and ML workloads, it's crucial to evaluate your needs for latency, throughput, and storage capacity.

For a comprehensive comparison of storage options for AI and ML workloads, see [Overview of storage services for AI and ML workloads in AI Hypercomputer](https://docs.cloud.google.com/ai-hypercomputer/docs/storage).

## Design considerations

This section provides guidance about best practices and design considerations for configuring Cloud Storage FUSE for security, reliability, cost, and performance. Although the recommendations here aren't exhaustive, they address key considerations for maximizing the benefits of Cloud Storage FUSE in your environment. Depending on your specific needs and workload characteristics, you might need to consider additional configuration options and trade-offs.

The following design recommendations highlight configurations to refine how you deploy Cloud Storage FUSE in GKE. Most Cloud Storage FUSE options are configured with [mount options](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf#mount-options). For more information about Cloud Storage FUSE command-line options and how to use them, see [gcsfuse CLI](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#options) and [Optimize Cloud Storage FUSE CSI driver for GKE performance](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf).

For an overview of architectural principles and recommendations that are specific to AI and ML workloads in Google Cloud, see the [AI and ML perspective](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml) in the Well-Architected Framework. 

### Security, privacy, and compliance

This section describes considerations for your AI and ML workloads in Google Cloud that meet your security, privacy, and compliance requirements.

#### GKE considerations

In the Autopilot mode of operation, GKE preconfigures your cluster and manages nodes according to security best practices, which lets you focus on workload-specific security. For more information, see the following:

  * [GKE Autopilot security capabilities](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-security)
  * [Move-in ready Kubernetes security with GKE Autopilot](https://cloud.google.com/blog/products/containers-kubernetes/move-in-ready-kubernetes-security-with-gke-autopilot)



To ensure enhanced access control for your applications that run in GKE, you can use Identity-Aware Proxy (IAP). IAP integrates with the GKE Ingress resource and helps to ensure that only authenticated users with the correct Identity and Access Management (IAM) role can access the applications. For more information, see [Enabling IAP for GKE](https://docs.cloud.google.com/iap/docs/enabling-kubernetes-howto).

By default, your data in GKE is encrypted [at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption) and [in transit](https://docs.cloud.google.com/docs/security/encryption-in-transit) by using Google-owned and Google-managed encryption keys. As an additional layer of security for sensitive data, you can encrypt data at the application layer by using a key that you own and manage with Cloud Key Management Service (Cloud KMS). For more information, see [Encrypt secrets at the application layer](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/encrypting-secrets).

If you use a Standard GKE cluster, then you can use the following additional data-encryption capabilities:

  * Encrypt data in use (that is, in memory) by using Confidential GKE Nodes. For more information about the features, availability, and limitations of Confidential GKE Nodes, see [Encrypt workload data in-use with Confidential GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes).
  * If you need more control over the encryption keys that are used to encrypt Pod traffic across GKE nodes, then you can encrypt the data in transit by using keys that you manage. For more information, see [Encrypt your data in-transit in GKE with user-managed encryption keys](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/enable-inter-node-transparent-encryption).



#### Cloud Storage considerations

By default, the data that's stored in Cloud Storage is encrypted by using Google-owned and Google-managed encryption keys. If required, you can use customer-managed encryption keys (CMEKs) or your own keys that you manage by using an external management method like customer-supplied encryption keys (CSEKs). For more information, see [Data encryption options](https://docs.cloud.google.com/storage/docs/encryption).

Cloud Storage supports two methods to grant users access to your buckets and objects: IAM and access control lists (ACLs). In most cases, we recommend that you use IAM, which lets you grant permissions at the bucket and project levels. For more information, see [Overview of access control](https://docs.cloud.google.com/storage/docs/access-control).

The training data that you load through Cloud Storage might include sensitive data. To protect such data, you can use Sensitive Data Protection to discover, classify, and de-identify the data. To separate your training and serving workloads, save your model and checkpoints to separate Cloud Storage buckets. This isolation helps prevent accidental exposure of sensitive information from your training dataset during serving. For more information, see [Using Sensitive Data Protection with Cloud Storage](https://docs.cloud.google.com/sensitive-data-protection/docs/dlp-gcs).

If you have data residency requirements, Cloud Storage can help you to meet those requirements. Data is stored or replicated within the regions that you specify.

#### Cloud Storage FUSE considerations

When you enable caching, Cloud Storage FUSE stores persistent files from your Cloud Storage bucket in an unencrypted format within the directory that you specify. Cloud Storage exposes all files to any user or process that has directory access. To mitigate these risks and improve security, the FUSE kernel layer restricts file system access to the user who mounted the system. This restriction denies access to other users, including the root user, even if inode permissions are more permissive.

However, there are use cases where overriding the default access restrictions might be necessary. For example, in a distributed AI and ML training workload where multiple nodes need to access and share checkpoints that are stored in Cloud Storage, you might need to allow broader access. In such cases, you can override the default restriction by using the `-o allow_other` option. However, if you broaden access to your files, you can potentially [expose your data to unauthorized users](https://github.com/torvalds/linux/blob/a33f32244d8550da8b4a26e277ce07d5c6d158b5/Documentation/filesystems/fuse.txt#L218-L310). Therefore, you should exercise caution when you use this option.

By default, all inodes in a Cloud Storage FUSE file system are owned by the user who mounted the file system. Although these defaults might be suitable for many cases, you can customize a Security Context for your Pod. For information about customizing a Security Context, see [Security and permissions](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf#security-and-permissions).

#### Other security considerations

For security principles and recommendations that are specific to AI and ML workloads, see [AI and ML perspective: Security](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/security) in the Well-Architected Framework. 

### Reliability

To ensure reliable operation, Cloud Storage FUSE incorporates automatic retries to handle potential disruptions and maintain data consistency. Failed requests are automatically [retried with exponential backoff](https://docs.cloud.google.com/storage/docs/retry-strategy#exponential-backoff) to Cloud Storage. Exponential backoff gradually increases the time between retries. This built-in mechanism helps your application overcome transient network issues or temporary Cloud Storage unavailability.

Although Cloud Storage FUSE offers many advantages, consider the following:

  * **Concurrent writes** : When multiple users try to modify a file, the _last write wins_ operation takes precedence and all previous write operations are lost. To maintain data integrity, we recommend that a single object is modified by only one source at any given moment.
  * **Cache persistence** : When you unmount or restart your bucket, caches don't persist. To avoid potential security issues, after you unmount or restart your bucket, it's essential that you manually delete the file cache directory.
  * **Processes with dedicated caches** : Although Cloud Storage FUSE supports concurrent access for efficient parallel processing, it's important to remember that caches are specific to each Cloud Storage FUSE process. Therefore, the same cache directory shouldn't be used by different Cloud Storage FUSE processes that run on the same or different machines.



#### Other reliability considerations

For reliability principles and recommendations that are specific to AI and ML workloads, see [AI and ML perspective: Reliability](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/reliability) in the Well-Architected Framework. 

### Cost optimization

This section provides guidance to help you optimize the cost of setting up and operating your AI and ML workflow in Google Cloud.

#### GKE considerations

In Autopilot mode, GKE optimizes the efficiency of your cluster's infrastructure based on workload requirements. To control costs, you don't need to constantly monitor resource utilization or manage capacity.

If you can predict the CPU, memory, and ephemeral storage usage of your Autopilot cluster, then you can get [committed use discounts](https://docs.cloud.google.com/kubernetes-engine/cud). To reduce the cost of running your application, you can use [Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms#how-it-works) for your GKE nodes. Spot VMs are priced lower than standard VMs, but they don't provide a guarantee of availability.

To optimize cost and performance through efficient management, use [Dynamic Workload Scheduler](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/provisioningrequest). Dynamic Workload Scheduler is a resource management and job scheduler that helps you improve access to AI and ML resources. Dynamic Workload Scheduler schedules all of your accelerators simultaneously and it can run during off-peak hours with defined accelerator capacity management. By scheduling jobs strategically, Dynamic Workload Scheduler helps to maximize accelerator utilization, reduce idle time, and ultimately optimize your cloud spend.

For more information about cost-optimization guidance, see [Best practices for running cost-optimized Kubernetes applications on GKE](https://docs.cloud.google.com/architecture/best-practices-for-running-cost-effective-kubernetes-applications-on-gke).

#### Cloud Storage considerations

Your AI and ML storage needs can be dynamic. For example, you might require significant storage capacity for your training data, but your capacity requirement decreases for serving, where you primarily store model data and checkpoints. To control costs, we recommend that you enable [object lifecycle management](https://docs.cloud.google.com/storage/docs/lifecycle) and [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass).

Object lifecycle management lets you automatically move older or unused data to cheaper storage classes or even delete the data, based on rules you set.

The Autoclass feature automatically moves data between storage classes based on how your access patterns. This feature ensures that you get the best balance of performance and cost.

#### Cloud Storage FUSE considerations

The standard Cloud Storage charges apply for storage, metadata operations, and network traffic that's generated by your FUSE activities. There's no additional cost to use Cloud Storage FUSE. For more information on common Cloud Storage FUSE operations and how they map to Cloud Storage operations, see the [operations mapping](https://docs.cloud.google.com/storage/docs/gcs-fuse#operations-mapping).

To optimize costs for your cache directory, you can use existing provisioned machine capacity, including local SSDs, persistent disks, or in-memory data for temporary file systems. When you use existing machine capacity, you can avoid incurring charges for additional storage resources. In addition, maximizing cache hits can significantly reduce Cloud Storage costs because locally served data doesn't incur operation charges or data transfer charges.

For more information about charges, see [Cloud Storage pricing](https://cloud.google.com/storage/pricing).

#### Other cost considerations

For cost optimization principles and recommendations that are specific to AI and ML workloads, see [AI and ML perspective: Cost optimization](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/cost-optimization) in the Well-Architected Framework. 

### Performance optimization

Cloud Storage FUSE is designed to provide efficient access to data in Cloud Storage for your AI and ML workloads. However, frequent metadata requests can reduce performance, especially in high-scale clusters. For more information about improving performance, see [Optimize Cloud Storage FUSE CSI driver for GKE performance](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf) and [Performance tuning best practices](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/performance).

To optimize performance, consider the following configurations:

  * **Enable hierarchical namespaces** : To enhance data access and organization, [create Cloud Storage buckets with hierarchical namespaces](https://docs.cloud.google.com/storage/docs/create-hns-bucket) enabled. Hierarchical namespaces let you organize data in a file system structure, which improves performance, ensures consistency, and simplifies management for AI and ML workloads. Hierarchical namespaces enable higher initial QPS and fast atomic directory renames.
  * **Enable file caching** : File caching accelerates repeated access to training data by using a local node directory to cache frequently read files. Serving repeat reads from a cache media reduces latency and minimizes operations back to Cloud Storage. On GPU machine types with a local SSD, the local SSD directory is automatically used. For machine types that don't include local SSD, such as TPUs, you can use a [RAM disk directory](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf#ram-cache), such as `/tmpfs`.

To enable the file cache, use the following mount options:

    * To set the usable file cache value to the cache capacity limit, set `file-cache:max-size-mb:` to `-1`.
    * To set metadata cache time–to-live (TTL) to unlimited duration and eviction based on the least-recently-used (LRU) algorithm after the maximum capacity is reached, set `metadata-cache:ttl-secs:` to `-1`.
  * **Increase metadata cache values** : Cloud Storage FUSE has two forms of metadata cache that improve performance for operations that are related to metadata lookups: [stat cache](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/caching#stat-cache-overview) and [type cache](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/caching#type-cache-overview).

To increase metadata cache values, set the following mount options:

    * To set the usable stat cache value to cache capacity limit, set `metadata-cache:stat-cache-max-size-mb:` to `-1`.
    * To set the usable type cache value to the capacity limit, set `metadata-cache:type-cache-max-size-mb:` to `-1`.
    * To prevent cached metadata items from expiring, with a default value of 60 seconds, set `metadata-cache:ttl-secs:` to `-1`. Infinite values should be used only for read-only volumes and nodes with large memory configurations.
  * **Pre-populate the metadata cache** : The metadata prefetch feature lets the Cloud Storage FUSE CSI driver proactively load relevant metadata about the objects in your Cloud Storage bucket into Cloud Storage FUSE caches. This approach reduces calls to Cloud Storage and it's especially beneficial for applications that access large datasets that have many files, such as AI and ML training workloads.

To pre-populate the metadata cache, enable metadata prefetch for the given volume. Set the volume attribute `gcsfuseMetadataPrefetchOnMount` to `true`. To avoid workload interruptions, consider increasing the memory limit of the `gke-gcsfuse-metadata-prefetch` sidecar by [configuring the sidecar resources](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-sidecar#configure-sidecar-resources).

  * **Enable list caching** : This feature optimizes listing directories and files. It's particularly beneficial for AI and ML training workloads, which often involve repeatedly accessing and listing entire directories. List caching provides highly efficient training processes by reducing the need to repeatedly access directory listings in your computer's memory.

To enable list caching and prevent kernel list cache items from expiring, set the mount option `file-system:kernel-list-cache-ttl-secs:` to `-1`.

  * **Enable parallel downloads** : Parallel downloads accelerate the initial loading of the model by fetching multiple chunks concurrently. Enabling parallel downloads results in faster model loading and improved responsiveness during serving.

To enable parallel downloads, enable file cache and set the mount option `file-cache:enable-parallel-downloads:` to `true`.

  * **Increase GKE sidecar limits** : To prevent resource constraints from hindering performance, [configure limits on the sidecar container](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-sidecar#configure-sidecar-resources) resources, like CPU and memory consumption. If you use a local SSD cache, consider setting `ephemeral-storage-limit` to unlimited. This setting enables Cloud Storage FUSE to fully use the available local SSD storage for enhanced caching.

  * **Read-only mount** : Because training workloads typically only need to read data, configure the mount point as read-only for optimal performance, especially when you use file caching. This configuration also helps maximize the benefits of optimizations in high-scale clusters and helps prevent potential data inconsistencies.




#### Other performance considerations

For performance optimization principles and recommendations that are specific to AI and ML workloads, see [AI and ML perspective: Performance optimization](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/performance-optimization) in the Well-Architected Framework. 

## What's next

  * Learn more: 
    * [Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/overview) overview.
    * [About Cloud Storage FUSE CSI driver for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cloud-storage-fuse-csi-driver).
    * [Cloud Storage FUSE performance tuning best practices](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/performance).
    * [Optimize Cloud Storage FUSE CSI driver for GKE performance](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf).
    * [Best practices for implementing machine learning on Google Cloud](https://docs.cloud.google.com/architecture/ml-on-gcp-best-practices).
    * [Overview of storage services for AI and ML workloads in AI Hypercomputer](https://docs.cloud.google.com/ai-hypercomputer/docs/storage).
  * Implement: 
    * [Create a GKE cluster with A4 nodes](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-a4/README.md).
    * [Quickstart: Access Cloud Storage buckets with the FUSE CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/cloud-storage-fuse-csi-driver).
    * [Create and manage Rapid Cache caches](https://docs.cloud.google.com/storage/docs/rapid/use-rapid-cache).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Author: [Samantha He](https://www.linkedin.com/in/samantha-he-05a98173) | Technical Writer

Other contributors: 

  * [Dean Hildebrand](https://www.linkedin.com/in/dean) | Technical Director, Office of the CTO
  * [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer
  * [Marco Abela](https://www.linkedin.com/in/marco-abela-a7b24963) | Product Manager
  * [Sean Derrington](https://www.linkedin.com/in/seanderrington) | Group Product Manager, Storage



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-22 UTC."],[],[]] 
