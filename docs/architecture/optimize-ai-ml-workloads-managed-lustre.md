---
url: https://docs.cloud.google.com/architecture/optimize-ai-ml-workloads-managed-lustre/
title: Optimize AI and ML workloads with Google Cloud Managed Lustre \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:35:36.468850+00:00
---

# Optimize AI and ML workloads with Google Cloud Managed Lustre  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/optimize-ai-ml-workloads-managed-lustre/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Optimize AI and ML workloads with Google Cloud Managed Lustre Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-10-13 UTC

This document provides a reference architecture that shows how you can use [Google Cloud Managed Lustre](https://docs.cloud.google.com/managed-lustre/docs/overview) to optimize performance for AI and ML workloads that are deployed on Google Kubernetes Engine (GKE). The intended audience for this document includes architects and technical practitioners who design, provision, and manage storage for their AI workloads on Google Cloud. The document assumes that you have an understanding of [Kubernetes concepts](https://kubernetes.io/docs/concepts/) and the [ML lifecycle, processes, and capabilities](https://docs.cloud.google.com/architecture/ml-on-gcp-best-practices).

Managed Lustre is a fully Google Cloud-managed, persistent parallel file system (PFS) that's based on [DDN's EXAScaler Lustre](https://www.ddn.com/products/lustre-file-system-exascaler/). Managed Lustre is a recommended solution for AI training and checkpointing workloads. It is particularly effective for migrating existing workloads from Lustre or other PFS solutions. To maximize resource utilization, workloads that use Managed Lustre for training should also use the same instance for serving and inference.

Managed Lustre is the recommended solution for AI workloads that meet the following criteria:

  * Require PiB-scale storage capacity.
  * Provide ultra low-latency (sub-millisecond) access with high throughput.
  * Provide high [input/output operations per second (IOPS)](https://en.wikipedia.org/wiki/IOPS).



Managed Lustre offers these advantages for AI workloads:

  * **Lower total cost of ownership (TCO) for training** : Managed Lustre helps to reduce training time by efficiently delivering data to compute nodes. This capability helps to reduce the total cost of ownership for AI and ML model training.
  * **Lower TCO for serving** : Managed Lustre provides high-performance capabilities that enable faster model loading and optimized inference serving. These capabilities help to lower compute costs and improve resource utilization.
  * **Efficient resource utilization** : Managed Lustre lets you combine checkpointing and training within a single instance. This resource sharing helps to maximize the efficient use of read and write throughput in a single, high-performance storage system.



## Architecture

The following diagram shows a sample architecture for using Managed Lustre to optimize the performance of a model training workload and serving workload:

![An architecture uses Managed Lustre to optimize performance of a model training workload and serving workload.](https://docs.cloud.google.com/static/architecture/images/optimize-ai-ml-workloads-managed-lustre-architecture.svg)![](https://docs.cloud.google.com/static/architecture/images/optimize-ai-ml-workloads-managed-lustre-architecture.svg)

The workloads that are shown in the preceding architecture are described in detail in later sections. This architecture includes the following components:

  * [GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview) cluster: GKE manages the compute hosts on which your AI and ML model training and serving processes execute. GKE manages the underlying infrastructure of clusters, including the control plane, nodes, and all system components.
  * [Kubernetes Scheduler](https://kubernetes.io/docs/concepts/scheduling-eviction/kube-scheduler/): The GKE control plane schedules workloads and manages their lifecycle, scaling, and upgrades.
  * [Virtual Private Cloud (VPC) network](https://docs.cloud.google.com/vpc/docs/vpc): All of the Google Cloud resources that are in the architecture use a single VPC network.
  * [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview): In this architecture, Cloud Load Balancing efficiently distributes incoming inference requests from application users to the serving containers in the GKE cluster. The use of Cloud Load Balancing helps to ensure high availability, scalability, and optimal performance for the AI and ML application. For more information, see [Understanding GKE load balancing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-networking#understanding-load-balancing).
  * [Graphics Processing Units (GPUs)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus) or [Tensor Processing Units (TPUs)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus): GPUs and TPUs are specialized [machine accelerators](https://docs.cloud.google.com/tpu/docs/intro-to-tpu) that improve the performance of your AI and ML workload. To help ensure optimal efficiency and compatibility, use the same type of accelerator for your entire AI and ML workload. For more information about how to choose an appropriate processor type, see Accelerator options later in this document.
  * [Managed Lustre](https://docs.cloud.google.com/managed-lustre/docs/overview): Managed Lustre accelerates AI and ML training and serving by providing a high-performance, persistent, PFS that's optimized for low latency and high throughput. Compared to using Cloud Storage alone, using Managed Lustre significantly reduces training time and improves the responsiveness of your models during serving. These improvements are especially realized in demanding workloads that require fast and consistent access to shared data.
  * [Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/gcs-fuse): Cloud Storage FUSE provides persistent and cost-effective storage for your AI and ML workloads. Cloud Storage serves as the central repository for your raw training datasets, model [checkpoints](https://developers.google.com/machine-learning/glossary#checkpoint), and model backups. Using Cloud Storage helps to ensure data durability, long-term availability, and cost-efficiency for data that isn't actively being used in computations.



### Training workload

In the preceding architecture, the following are the steps in the data flow during model _training_ :

  1. **Upload training data to Cloud Storage** : You upload training data to a Cloud Storage bucket, which serves as a secure and scalable central repository and source of truth.
  2. **Copy data to Managed Lustre** : The training data corpus is transferred by [importing data to a Managed Lustre instance](https://docs.cloud.google.com/managed-lustre/docs/transfer-data#import) from Cloud Storage. Transferring the training data lets you take advantage of Managed Lustre's high-performance file system capabilities to optimize data loading and processing speeds during model training.
  3. **Run training jobs in GKE** : The model training process runs on GKE nodes. By using Managed Lustre as the data source instead of loading data from Cloud Storage directly, the GKE nodes can access and load training data with significantly increased speed and lower latency. Managed Lustre also enables shorter time for the transfer of the first byte to begin as measured by [time to first byte (TTFB)](https://web.dev/articles/ttfb). Using Managed Lustre helps to reduce data loading times and accelerate the overall training process, especially for large datasets that have small read files and complex models. Depending on your workload requirements, you can use GPUs or TPUs. For information about how to choose an appropriate processor type, see Accelerator options later in this document.
  4. **Save training checkpoints to Managed Lustre** : During the training process, checkpoints are saved to Managed Lustre based on metrics or intervals that you define. The checkpoints capture the state of the model at frequent intervals. The checkpoints can selectively be [exported to Cloud Storage](https://docs.cloud.google.com/managed-lustre/docs/transfer-data#export_data) for long-term storage.



### Serving workload

In the preceding architecture, the following are the steps in the data flow during model _serving_ :

  1. **Load model for serving** : When your model is ready for deployment, your GKE Pods load the trained model from your Managed Lustre instance to the serving nodes. If the Managed Lustre instance that you used during training has sufficient IOPS capacity and if it's in the same zone as your accelerators, you can use the same Managed Lustre instance to serve your model. Reusing the Managed Lustre instance enables efficient resource sharing between training and serving. To maintain optimal performance and compatibility, use the same GPU or TPU processor type that you selected for your serving GKE nodes. 
  2. **Inference request** : Application users send inference requests through the serving endpoints. These requests are directed to the Cloud Load Balancing service. Cloud Load Balancing distributes the incoming requests across the serving containers in the GKE cluster. This distribution helps to ensure that no single container is overwhelmed and that requests are processed efficiently. 
  3. **Serving inference requests** : When an inference request is received, the compute nodes access the pre-loaded model to perform the necessary computations and generate a prediction. 
  4. **Response delivery** : The serving containers send the responses back through Cloud Load Balancing. Cloud Load Balancing routes the responses back to the appropriate application users, which completes the inference request cycle. 



## Products used

This reference architecture uses the following Google Cloud products:

  * [ Virtual Private Cloud (VPC)](https://cloud.google.com/vpc): A virtual system that provides global, scalable networking functionality for your Google Cloud workloads. VPC includes VPC Network Peering, Private Service Connect, private services access, and Shared VPC.
  * [ Cloud Load Balancing](https://cloud.google.com/load-balancing): A portfolio of high performance, scalable, global and regional load balancers. 
  * [ Google Kubernetes Engine (GKE)](https://cloud.google.com/kubernetes-engine): A Kubernetes service that you can use to deploy and operate containerized applications at scale using Google's infrastructure. 
  * [ Cloud Storage](https://cloud.google.com/storage): A low-cost, no-limit object store for diverse data types. Data can be accessed from within and outside Google Cloud, and it's replicated across locations for redundancy.
  * [ Google Cloud Managed Lustre](https://cloud.google.com/products/managed-lustre): A fully managed parallel file system for AI, high performance computing (HPC), and data-intensive applications.



## Use cases

Managed Lustre is ideal for AI workloads that need PiB-scale storage capacity and that need to provide low-latency (sub-millisecond) access with high throughput and high IOPS. This section provides examples of use cases for which you can use Managed Lustre.

### Text-based processing and text generation

[LLMs](https://docs.cloud.google.com/docs/generative-ai/glossary#large-language-model) are specialized AI models that are designed specifically for understanding and processing text-based data. LLMs are trained on massive text datasets, which enables them to perform a variety of tasks, including machine translation, question answering, and text summarization. To facilitate efficient training and batch processing, your LLM needs low-latency access to the datasets. Managed Lustre excels in data-intensive applications by providing the high throughput and low latency that's needed for both training and inference, which results in more responsive LLM-powered applications.

### High-resolution image or video processing

AI and ML applications or multimodal generative models that process high-resolution images or videos, such as medical imaging analysis or autonomous driving systems, require large storage capacity and rapid data access. Managed Lustre provides a high-performance persistent file system that allows for fast data loading to accelerate the application performance. For example, Managed Lustre can store large volumes of patient data, such as MRI and CT scans, and it can facilitate rapid data loading to compute nodes for model training. This functionality enables AI and ML models to quickly analyze the data for diagnosis and treatment.

## Design alternatives

This section presents alternative design approaches that you can consider for your AI and ML application in Google Cloud.

### Compute infrastructure alternative

The reference architecture in this document uses GKE for the AI and ML workloads. Depending on the requirements of your workload, you can alternatively deploy Managed Lustre instances on [Compute Engine](https://cloud.google.com//products/compute) with [Slurm](https://slurm.schedmd.com/overview.html). We recommend this approach if you need to integrate proprietary AI intellectual property (IP) into a scalable environment and if you need flexibility and control to optimize performance for specialized workloads.

Compute Engine lets you have more granular operating system-level control compared to GKE. When you use Compute Engine, you can do the following:

  * Select, configure, and manage the OS environment within your virtual machines to meet specific workload requirements.
  * Tailor your infrastructure to your exact needs, including the selection of specific VM machine types.
  * Use the [accelerator-optimized machine family](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines) for enhanced performance with your AI workloads.



Slurm is a highly configurable open source workload and resource manager. Slurm offers a powerful option for managing AI workloads and lets you control the configuration and management of the compute resources. To use this approach, you need expertise in Slurm administration and Linux system management. GKE provides a managed Kubernetes environment that automates cluster management.

For information about deploying Slurm, see [Deploy an HPC cluster with Slurm](https://docs.cloud.google.com/cluster-toolkit/docs/quickstarts/slurm-cluster). You can also deploy using [Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/overview) with the [Managed Lustre starter blueprint](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/machine-learning/a4-highgpu-8g/a4high-slurm-blueprint.yaml).

### Accelerator options

[Machine accelerators](https://docs.cloud.google.com/tpu/docs/intro-to-tpu) are specialized processors that are designed to speed up the computations that are required for AI and ML workloads. You can choose either GPUs or TPUs.

  * GPU accelerators provide excellent performance for a wide range of tasks, including graphic rendering, deep learning training, and scientific computing. Google Cloud has a wide selection of GPUs to match a range of performance and price points. For information about GPU models and pricing, see [GPU pricing](https://cloud.google.com/products/compute/pricing/accelerator-optimized).
  * TPUs are custom-designed AI accelerators, which are optimized for training and inference of large AI models. TPUs are ideal for a variety of use cases, such as chatbots, code generation, media content generation, synthetic speech, vision services, recommendation engines, and personalization models. For more information about TPU models and pricing, see [TPU pricing](https://cloud.google.com/tpu/pricing).



### Storage alternatives

[Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/overview) with [Rapid Cache](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache) can be used for training, checkpointing, and serving workloads. Cloud Storage FUSE with Rapid Cache is the recommended storage solution for serving and inference due to its lower cost and ease for multi-regional inference when compared to Managed Lustre. To help ensure the highest level of availability, use Cloud Storage FUSE with Rapid Cache and a multi-regional or dual-region bucket. This configuration makes your trained AI models available across multiple [regions](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache#supported-locations). However, in comparison to Managed Lustre instances, Cloud Storage FUSE can have lower per-VM throughput. For more information, see [Optimize AI and ML workloads with Cloud Storage FUSE](https://docs.cloud.google.com/architecture/optimize-ai-ml-workloads-cloud-storage-fuse).

## Design considerations

To design a Managed Lustre deployment that optimizes the security, reliability, cost, operations, and performance of your AI and ML workloads on Google Cloud, use the guidelines in the following sections.

**Note:** The guidance in this section isn't exhaustive. Depending on the specific requirements of your application and the Google Cloud products and features that you use, there might be additional design factors and trade-offs that you should consider.

For an overview of architectural principles and recommendations that are specific to AI and ML workloads in Google Cloud, see the [AI and ML perspective](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml) in the Well-Architected Framework. 

### Security, privacy, and compliance

This section describes considerations for your AI and ML workloads in Google Cloud that meet your security, privacy, and compliance requirements.

#### SSH security

To facilitate enhanced access control for your applications that run in GKE, you can use Identity-Aware Proxy (IAP). IAP integrates with the GKE Ingress resource and helps to verify that only authenticated users with the correct Identity and Access Management (IAM) role can access the applications. For more information, see [Enabling IAP for GKE](https://docs.cloud.google.com/iap/docs/enabling-kubernetes-howto) and [Access control with IAM](https://docs.cloud.google.com/managed-lustre/docs/access-control).

#### Data encryption

By default, your data in GKE, including data stored in your Managed Lustre instance, is encrypted [at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption) and [in transit](https://docs.cloud.google.com/docs/security/encryption-in-transit) by using Google-owned and Google-managed encryption keys. If you need to manage your own encryption keys, you can use customer-managed encryption keys (CMEK) in Cloud Key Management Service to encrypt data at rest in your Managed Lustre instance, and you can encrypt GKE secrets at the application layer. For more information, see [Use customer-managed encryption keys](https://docs.cloud.google.com/managed-lustre/docs/cmek) and [Encrypt secrets at the application layer](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/encrypting-secrets).

If you use a GKE Standard cluster, then you can use the following additional data-encryption capabilities:

  * Encrypt data in use (that is, in memory) by using Confidential Google Kubernetes Engine Nodes. For more information about the features, availability, and limitations of Confidential GKE Nodes, see [Encrypt workload data in-use with Confidential GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes).
  * If you need more control over the encryption keys that are used to encrypt Pod traffic across GKE nodes, then you can encrypt the data in transit by using keys that you manage. For more information, see [Encrypt your data in-transit in GKE with user-managed encryption keys](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/enable-inter-node-transparent-encryption).



#### Data isolation

To enhance security and improve data protection, store training data in a separate Managed Lustre instance from the checkpoints and trained models. The use of separate storage instances provides performance isolation, enhances security by isolating training data, and improves data protection. Although access control lists let you manage security within a single instance, using separate instances provides a more robust security boundary.

#### More security considerations

In the Autopilot mode of operation, GKE preconfigures your cluster and manages nodes according to security best practices, which lets you focus on workload-specific security. For more information, see [GKE Autopilot security capabilities](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-security) and [Move-in ready Kubernetes security with GKE Autopilot](https://cloud.google.com/blog/products/containers-kubernetes/move-in-ready-kubernetes-security-with-gke-autopilot).

For information about securing the privacy of your data, see [Sensitive Data Protection overview](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview) and [Inspect Google Cloud storage and databases for sensitive data](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage).

For security principles and recommendations that are specific to AI and ML workloads, see [AI and ML perspective: Security](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/security) in the Well-Architected Framework. 

### Reliability

This section describes design factors that you should consider when you use this reference architecture to build and operate reliable infrastructure for your regional deployment in Google Cloud.

#### Robustness against infrastructure outages

With the Autopilot mode of operation that's used in this architecture, GKE provides the following built-in reliability capabilities:

  * Your workload uses a [regional GKE cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/regional-clusters). The control plane and worker nodes are spread across three different zones within a region. Your workloads are robust against zone outages. Regional GKE clusters have a higher uptime [Service Level Agreement (SLA)](https://cloud.google.com/kubernetes-engine/sla) than zonal clusters.
  * You don't need to create nodes or manage node pools. GKE automatically creates the node pools and scales them automatically based on the requirements of your workloads.



To increase the availability of your application, you can serve it from multiple zones by deploying a Managed Lustre instance in each zone.

#### Cluster capacity planning

To help ensure that sufficient GPU capacity is available when it's required for autoscaling the GKE cluster, you can create and use reservations. A reservation provides assured capacity in a specific zone for a specified resource. A reservation can be specific to a project or shared across multiple projects. You incur charges for reserved resources even if the resources aren't provisioned or used. For more information, see [Consuming reserved zonal resources](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations).

#### Data durability

To back up and restore workloads in GKE, enable [backup for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke) in each cluster. Backup for GKE is useful for disaster recovery, CI/CD pipelines, cloning workloads, and upgrade scenarios.

You can select specific workloads or all workloads that you want to back up and restore. You can also back up workloads from one cluster and restore them into another cluster. To reduce workload downtime, you can schedule your backups to automatically run so that you can quickly recover your workloads in the event of an incident.

#### More reliability considerations

For reliability principles and recommendations that are specific to AI and ML workloads, see [AI and ML perspective: Reliability](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/reliability) in the Well-Architected Framework. 

### Cost optimization

This section provides guidance to help you optimize the cost of setting up and operating your AI and ML workflow in Google Cloud.

#### Managed Lustre performance tiers

When you create a Managed Lustre instance, you need to select a [performance tier](https://docs.cloud.google.com/managed-lustre/docs/performance-tiers). Choose an appropriate tier based on the performance and cost requirements of your workload.

#### Node provisioning model

In Autopilot mode, GKE optimizes the efficiency of your cluster's infrastructure based on workload requirements. To control costs, you don't need to constantly monitor resource utilization or manage capacity.

If you can predict the CPU, memory, and ephemeral storage usage of your Autopilot cluster, then you can get [committed use discounts](https://docs.cloud.google.com/kubernetes-engine/cud). To reduce the cost of running your application, you can use [Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms#how-it-works) for your GKE nodes. Spot VMs are priced lower than standard VMs, but they don't provide a guarantee of availability.

#### Resource management

To optimize cost and performance through efficient management, use [Dynamic Workload Scheduler](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/provisioningrequest). Dynamic Workload Scheduler is a resource management and job scheduler that helps you improve access to AI accelerators (GPUs and TPUs). Dynamic Workload Scheduler schedules all of your accelerators simultaneously and it can run during off-peak hours with defined accelerator capacity management. By scheduling jobs strategically, Dynamic Workload Scheduler helps to maximize accelerator utilization, reduce idle time, and optimize your cloud spend.

#### Resource utilization

To maximize resource utilization, use one Managed Lustre instance for training and serving. Consolidating training and serving workloads onto a single Managed Lustre instance minimizes costs by eliminating redundant infrastructure and simplifying resource management. However, there can be potential resource contention if both workloads have high throughput demands. If spare IOPS are available after training, using the same instance can accelerate model loading for serving. Use Cloud Monitoring to help verify that you allocate sufficient resources to meet your throughput demands.

To minimize storage costs, [export your data from your Managed Lustre instance](https://docs.cloud.google.com/managed-lustre/docs/transfer-data#export_data) to a lower-cost Cloud Storage class after training and checkpointing. Exporting your data to Cloud Storage also lets you destroy and recreate Managed Lustre instances as needed for your workload.

To help control the costs of your Cloud Storage bucket, enable [object lifecycle management](https://docs.cloud.google.com/storage/docs/lifecycle) or [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass). Object lifecycle management automatically moves older or less-used data to less expensive storage classes or deletes the data, based on the rules that you set. Autoclass moves data between storage classes based on your access patterns. Using object lifecycle management or Autoclass helps to ensure the most cost-effective storage class for your data usage by minimizing expenses and helping to prevent unexpected retrieval fees.

#### More cost considerations

For cost optimization principles and recommendations that are specific to AI and ML workloads, see [AI and ML perspective: Cost optimization](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/cost-optimization) in the Well-Architected Framework. For information about optimizing cost on GKE, see [Best practices for running cost-optimized Kubernetes applications on GKE](https://docs.cloud.google.com/architecture/best-practices-for-running-cost-effective-kubernetes-applications-on-gke).

### Operational excellence

This section provides guidance to help you design an infrastructure for your AI and ML workflow that you can operate efficiently.

#### Model management

To track and manage model artifacts, including binaries and metadata, use [Model Registry on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-registry/introduction), which lets you store, organize, and deploy model versions seamlessly.

To optimize model reliability, implement [Model Monitoring on Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/model-monitoring/overview) to detect data [drift](https://en.wikipedia.org/wiki/Concept_drift), track performance, and identify anomalies in production.

#### GKE cluster autoscaling

With Autopilot clusters, you don't need to provision or manage node pools. Node pools are automatically provisioned through [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning), and they're automatically scaled to meet the requirements of your workloads.

For GKE Standard clusters, the cluster autoscaler automatically resizes the number of nodes within a node pool based on workload demands. To control the autoscaling behavior of the cluster autoscaler, you can specify a minimum and maximum size for the node pool.

When you use the GKE cluster autoscaler, don't enable Compute Engine [autoscaling for managed instance groups (MIGs)](https://docs.cloud.google.com/compute/docs/autoscaler) for your cluster nodes. The GKE cluster autoscaler is separate from the Compute Engine autoscaler. The GKE cluster autoscaler is designed to scale your workload by analyzing resource utilization across your GKE cluster, including the underlying MIGs. Using both autoscalers can lead to conflicting scaling decisions. For more information, see [About GKE cluster autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler).

#### Metric monitoring

To identify bottlenecks, monitor key metrics like latency, error rate, and resource use, use [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview). Cloud Monitoring provides real-time visibility to track resource usage patterns and identify potential inefficiencies.

#### Storage management

To automate data management based on usage for your Cloud Storage bucket, enable [object lifecycle management](https://docs.cloud.google.com/storage/docs/lifecycle) or [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass). Object lifecycle management automatically moves older or less-used data to less expensive storage classes or deletes the data, based on rules you set. Autoclass moves data between storage classes based on your access patterns. Using object lifecycle management or Autoclass helps to ensure consistent policy application across your storage infrastructure and helps to reduce potential human error, which provides both performance and cost savings without manual intervention.

#### More operational considerations

For operational excellence principles and recommendations that are specific to AI and ML workloads, see [AI and ML perspective: Operational excellence](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/operational-excellence) in the Well-Architected Framework. 

### Performance optimization

This section provides guidance to help you optimize the performance of your AI and ML workflow in Google Cloud. The guidance in this section isn't exhaustive. For more information about optimizing performance for your Managed Lustre environment, see [Performance considerations](https://docs.cloud.google.com/managed-lustre/docs/performance).

#### Training considerations

Each [A3 or A4 VM](https://docs.cloud.google.com/compute/docs/gpus) can deliver 20 GB/s, approximately 2.5 GB/s per GPU, from a Managed Lustre instance. Before training begins, training data must be prefetched from Cloud Storage and [imported to Managed Lustre](https://docs.cloud.google.com/managed-lustre/docs/transfer-data#import) to minimize latency during training. To maximize throughput for your training workload, provision your Managed Lustre instance to match your throughput and storage capacity needs. For example, a 20 TiB Managed Lustre instance provides between 2.5 GB/s and 20 GB/s aggregate throughput across all clients, depending on the selected performance tier. If your training demands higher throughput, you'll need to increase your Managed Lustre instance size accordingly.

#### Checkpointing considerations

To take advantage of the high write throughput that Managed Lustre offers and to minimize training time, use Managed Lustre for both training and checkpointing. This approach helps to achieve efficient utilization of resources and helps lower the TCO for your GPU resources by keeping both training and checkpointing as fast as possible. To achieve fast checkpointing, you can run distributed, asynchronous checkpointing. Because Managed Lustre is persistent, you can store your checkpoints within the same instance. For additional cost optimization and long-term storage, consider exporting checkpoints to a Cloud Storage bucket.

#### Serving considerations

To achieve optimal performance during serving, you need to minimize the time that it takes to load models into memory. Managed Lustre offers high per-VM throughput of more than 20 GB/s, which provides high aggregate cluster throughput. This capability can help you to minimize model load times across thousands of VMs. To track key metrics that enable you to identify bottlenecks, use Cloud Monitoring and check that you deploy sufficient capacity as performance increases with storage capacity.

#### Resource placement

To minimize latency and maximize performance, create your Managed Lustre instance in a region that's geographically close to your GPU or TPU compute clients. In the reference architecture that this document describes, the GKE containers and file system are colocated in the same zone.

  * **For training and checkpointing** : For optimal results, deploy the clients and the Managed Lustre instances in the same zone. This colocation minimizes data transfer times and maximizes the utilization of the Managed Lustre write throughput.
  * **For serving:** Although colocating with compute clients in the same zone is ideal, having one Managed Lustre instance per region can be sufficient. This approach avoids extra costs that are associated with deploying multiple instances and helps to maximize compute performance. However, if you require additional capacity or throughput, you might consider deploying more than one instance per region.



For information about the supported regions and zones for Managed Lustre instances, see [Supported locations](https://docs.cloud.google.com/managed-lustre/docs/locations).

#### More performance considerations

For performance optimization principles and recommendations that are specific to AI and ML workloads, see [AI and ML perspective: Performance optimization](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/performance-optimization) in the Well-Architected Framework. 

## Deployment

To create and mount a Managed Lustre instance, we recommend that you use the [Managed Lustre module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/file-system/managed-lustre) that's available in [Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/overview). Cluster Toolkit is a modular, Terraform-based toolkit that's designed for deployment of repeatable AI and ML environments on Google Cloud.

For information about how to manually deploy Managed Lustre on GKE, see [Create a Managed Lustre instance](https://docs.cloud.google.com/managed-lustre/docs/create-instance) and [Access existing Managed Lustre instances on GKE using the Managed Lustre CSI driver](https://docs.cloud.google.com/managed-lustre/docs/lustre-csi-driver-existing-instance).

For information about how to configure a VPC network for Managed Lustre, see [Configure a VPC network](https://docs.cloud.google.com/managed-lustre/docs/vpc).

## What's next

  * Learn more about [best practices for implementing machine learning on Google Cloud](https://docs.cloud.google.com/architecture/ml-on-gcp-best-practices).
  * Learn more about [storage services for AI and ML workloads in AI Hypercomputer](https://docs.cloud.google.com/ai-hypercomputer/docs/storage).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Author: [Samantha He](https://www.linkedin.com/in/samantha-he-05a98173) | Technical Writer

Other contributors: 

  * [Dean Hildebrand](https://www.linkedin.com/in/dean) | Technical Director, Office of the CTO
  * [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer
  * [Sean Derrington](https://www.linkedin.com/in/seanderrington) | Group Product Manager, Storage



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
