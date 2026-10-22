---
url: https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/batch-platform-on-gke/
title: Best practices for running batch workloads on GKE \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:31:54.295415+00:00
---

# Best practices for running batch workloads on GKE  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/batch-platform-on-gke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)



Send feedback 

#  Best practices for running batch workloads on GKE Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot  Standard 

This page introduces the best practices for building and optimizing batch processing platforms with Google Kubernetes Engine (GKE), including best practices for:

  * Architecture
  * Job management
  * Multi-tenancy
  * Security
  * Queueing
  * Storage
  * Performance
  * Cost efficiency
  * Monitoring



GKE provides a powerful framework for orchestrating batch workloads such as data processing, [training machine learning models](https://cloud.google.com/blog/products/ai-machine-learning/build-a-ml-platform-with-kubeflow-and-ray-on-gke), [running scientific simulations](https://cloud.google.com/blog/products/containers-kubernetes/gke-gpu-sharing-helps-scientists-quest-for-neutrinos), and other [high performance computing workloads](https://www.pgs.com/company/newsroom/news/industry-insights--hpc-in-the-cloud/).

These best practices are intended for platform administrators, cloud architects, and operations professionals interested in deploying batch workloads in GKE. The [Reference Architecture: Batch Processing Platform on GKE](https://github.com/ai-on-gke/batch-reference-architecture) showcases many of the best practices discussed in this guide, and can be deployed in your own Google Cloud project.

For a consolidated overview of all GKE best practices, see [Best practices for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices). 

## How batch workloads work

A batch workload is a group of tasks that run to completion without user intervention. To define tasks, you use the Kubernetes [Jobs](https://kubernetes.io/docs/concepts/workloads/controllers/job) resource. A batch platform receives the Jobs and queues them in the order they are received. The queue in the batch platform applies processing logic such as priority, quota, and allocable resources. By queueing and customizing the batch processing parameters, Kubernetes lets you optimize the use of available resources, minimize the idle time for scheduled Jobs, and maximize cost savings. The following diagram shows the GKE components that can be part of a batch platform.

[ ![](https://docs.cloud.google.com/static/kubernetes-engine/images/batch-process.svg)](https://docs.cloud.google.com/static/kubernetes-engine/images/batch-process.svg)

## Batch platform management

Traditionally, batch platforms have two main user personas, developers and platform administrators:

  * A developer submits a Job specifying the program, the data to be processed, and requirements for the Job. Then, the developer receives confirmation of the Job submission and a unique identifier. Once the Job is complete, the developer would get a notification along with any output or results of the Job.
  * A platform administrator manages and delivers an efficient and reliable batch processing platform to the developers.



A batch processing platform must meet the following requirements:

  * The platform resources are properly provisioned to ensure that Jobs run with little to no user intervention required.
  * The platform resources are configured according to the organization's security and observability best practices.
  * The platform resources are used as efficiently as possible. In case of resource contention, the most important work gets done first.



### Prepare the batch platform architecture in GKE

A GKE environment consists of nodes, which are Compute Engine virtual machines (VMs), that are grouped together to form a cluster.

The following table lists the key recommendations when planning and designing your batch platform architecture:

Recommendation | Resources  
---|---  
Select a GKE mode of operation |  GKE has the following modes of operation available:

  * With Autopilot mode, GKE automatically manages your cluster configuration, including your nodes, scaling, security, and other preconfigured settings so you can focus on your workload. Autopilot clusters are highly-available by default.
  * With Standard mode, you define and manage your cluster configuration, including your nodes, scaling, security, and other advanced settings.

See the [high-level comparison between Autopilot and Standard mode](https://docs.cloud.google.com/kubernetes-engine/docs/resources/autopilot-standard-feature-comparison).  
Choose the machine type for your nodes |  GKE supports the following Compute Engine VMs series:

  * Cost-optimized, such as E2
  * Balanced, such as N2, N2D, or N1
  * Scale-out optimized, such as Tau T2D, or Tau T2A
  * Memory-optimized, such as M2 or M1
  * Compute-optimized, such as C2 or C2D
  * Accelerator-optimized, such as A4 featuring NVIDIA B200 GPUs

Each machine series is associated with one or more CPU platforms, such as Arm processors and x86 processors from Intel and AMD. Learn [about the options that are currently available for your workload](https://docs.cloud.google.com/compute/docs/machine-resource).  
Use hardware accelerators for your nodes |  You can also use hardware accelerators such as graphics processing units (GPUs) and Tensor Processing Units (TPUs) in GKE. Consider is GPU _time-sharing_ strategy, which allows multiple containers to share time on the same physical GPU. This approach is useful for burstable and homogenous GPU workloads with low requests. Multi-instance GPUs to partition GPUs to share a single GPU resource across multiple containers at the same time.

  * Learn about the available GPU accelerator strategies, such as [Time-sharing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/timesharing-gpus) and [Multi-instance GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus-multi).
  * Learn about [TPUs accelerator strategies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus).

  
Enable cluster autoscaler on Standard clusters | GKE automatically resizes the number of nodes in a given node pool based on the demands of your workloads. You don't need to manually add or remove nodes or over-provision your node pools. Instead, you only specify a minimum and maximum size for the node pool. We recommend you set cluster autoscaler with the following configuration:

  * Use `optimize-utilization` profile that removes unused nodes up to three times faster than the `balanced` profile. To learn more, see [Autoscaling profiles](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#autoscaling_profiles).
  * Set location policy to `ANY`. The GKE cluster autoscaler prioritizes utilization of unused reservations and create nodes in any available zone in the regions. To learn more, see [Location policy](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#location_policy).
  * Enable node auto-provisioning to automatically manage and autoscale your infrastructure. Once a node pool is created using auto-provisioning, cluster autoscaler can dynamically scale the nodepool. To learn more, see [How node auto-provisioning works](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#operation).

With Autopilot clusters, you don't need to worry about provisioning nodes or managing node pools because node pools are automatically provisioned through node auto-provisioning, and are automatically scaled to meet the requirements of your workloads.  
Enroll your cluster in a release channel | GKE can automatically manage your cluster version and upgrades. Based on your release adoption model, you can enroll your cluster in the GKE available channels. To learn more, see [How to choose the best release channel for your clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#what_channel_should_i_use)  
Define a scope of maintenance to exclude for your cluster | With a upgrade scope exclusion window defined, GKE respects that long running batch workloads aren't disrupted for maintenance until completion. To learn more, see [Scope of maintenance to exclude](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#scope_of_maintenance_to_exclude).  
  
### Manage the Job lifecycle

In Kubernetes, you run your workloads in a set of [_Pods_](https://kubernetes.io/docs/concepts/workloads/pods/). Pods are groups of single or multiple containers, with shared storage and network resources. Pods are defined by a Kubernetes specification.

A Job creates one or more Pods and continually tries to run them until a specified number of Pods successfully terminate. As Pods complete, the Job tracks the successful completions. When a specified number of successful completions is reached, the Job is complete.

The following table lists the key recommendations when designing and managing Jobs:

Recommendation | Resources  
---|---  
Select the Job completion mode | Specify the [Completion mode](https://kubernetes.io/docs/concepts/workloads/controllers/job/#completion-mode) as `Indexed`. This configuration is useful when assigning a partition of the data to be processed based on the Pod's index. The Pods of a Job get an associated completion index. Deleting a Job cleans up the Pods it created. Suspending a Job deletes its active Pods until the Job is resumed again.   
Set CronJobs for regular scheduled actions | Use [CronJob](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs) for GKE to perform regular scheduled actions, such as backups, report generation, or scheduled training for machine learning models.   
Manage failures in a Job | Define the Kubernetes Pod failure policy and Pod backoff failure limit to handle retriable and non-retriable failures in a Job. This definition improves the cluster resources consumption by avoiding unnecessary Pod retries and Job failures due to Pod disruptions. For example, you can configure [preemption](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/), [API-initiated eviction](https://kubernetes.io/docs/concepts/scheduling-eviction/api-eviction/), or [taint-based eviction](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/#taint-based-evictions) where Pods that don't have a toleration for the `NoExecute` taint effect are evicted. Learn how to [Handle retriable and non-retriable pod failures with Pod failure policy](https://kubernetes.io/docs/tasks/job/pod-failure-policy/).   
Manage multiple Jobs as a unit | Use the [JobSet API](https://github.com/kubernetes-sigs/jobset) to manage multiple Jobs as a unit to address workload patterns, such as one driver (or coordinator) and multiple workers (for example, `MPIJob`) while setting Job defaults that are aligned with common patterns based on your use cases. For example, you can create an Indexed Job by default, create a headless service for predictable fully qualified domain names (FQDN) for Pods, and set the associated Pod failure policy.  
Extend run time for a Pod that doesn't tolerate restarts | Set the Kubernetes `cluster-autoscaler.kubernetes.io/safe-to-evict` annotation to `false` in the Pod specification. The cluster autoscaler respects the eviction rules set on Pods. These restrictions can prevent a node from being deleted by the autoscaler if it contains a Pod with the `cluster-autoscaler.kubernetes.io/safe-to-evict` annotation. To learn more, see [Considering Pod scheduling and disruption](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#scheduling-and-disruption).  
  
## Manage Multi-tenancy

GKE cluster [multi-tenancy](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multitenancy-overview) is an alternative to managing GKE resources by different users or workloads, named as _tenants_ , in a single organization. The management of GKE resources might follow criteria such as tenant isolation, [quotas and limit ranges](https://docs.cloud.google.com/kubernetes-engine/quotas), or cost allocation.

[ ![](https://docs.cloud.google.com/static/kubernetes-engine/images/enterprise-multitenancy.svg)](https://docs.cloud.google.com/static/kubernetes-engine/images/enterprise-multitenancy.svg)

The following table lists the key recommendations when managing multi-tenancy:

Recommendation | Resources  
---|---  
Use namespaces to manage tenant isolation | You can separate each tenant and their Kubernetes resources into their own [namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/).   
Use policies to enforce tenant isolation | Define [Policies](https://kubernetes.io/docs/concepts/policy/) to restrict API access, set quotas, constrain resource usage, and restrict what containers are allowed to do. These policies are scoped by namespaces.   
Set GKE cost allocation | Use [GKE cost allocation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cost-allocations) get insights about cluster resource requests for each tenant on a namespace basis.   
  
### Control access to the batch platform

GKE allows you to finely tune the access permissions of the workloads running on the cluster.

The following table lists the key recommendations when managing access and security

Recommendation | Resources  
---|---  
Set Workload Identity Federation for GKE | GKE allows workloads in your GKE cluster to impersonate Identity and Access Management (IAM) service accounts to access Google Cloud services. By using Workload Identity Federation for GKE, workloads can securely access secrets stored outside GKE. To learn more, see [ Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity) and [access secrets stored](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/workload-identity-secrets).  
Set cluster network isolation | Configure the network isolation of your clusters so that both the control plane endpoint and worker nodes can have internal IP addresses. To learn more, see [About customizing network isolation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation).   
Use Shielded GKE Nodes | Configure [ Shielded GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/shielded-gke-nodes) to provide strong, verifiable node identity and integrity to increase the security of GKE nodes.   
Physical isolation | For security reasons your workloads might need stronger isolation. [ Control scheduling with node taints](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/) to physically separate tenants in node pools using node taints and workload tolerations. This helps ensure that only the appropriate workloads are scheduled on those node pools.  
  
#### Queueing and fair sharing

To control resource consumption, you can assign resource quota limits for each tenant, queue incoming Jobs, and process Jobs in the order they were received.

The following table lists the key recommendations when managing queueing and fair sharing among batch workloads:

Recommendation | Resources  
---|---  
Use Kueue | Kueue is a kubernetes-native Job queueing system for batch, high performance computing, machine learning, and similar applications in a Kubernetes cluster. To help with fair sharing of cluster resources between its tenants, Kueue manages quotas and how Jobs consume them. Kueue makes the following decisions:

  * When a Job should wait
  * When a Job should be admitted to start, for example by creating the Pod
  * When a Job should be preempted, for example by deleting the Pod

To learn how to implement a Job queueing system, see [Implement a Job queuing system with quota sharing between namespaces on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/kueue-cohort). To learn more about Kueue, see [Kueue concepts](https://kueue.sigs.k8s.io/docs/concepts/).  
  
### Optimize storage, performance, and cost efficiency

The efficient use of our GKE compute and [storage](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/storage-overview) resources can reduce costs. One strategy is to right-size and configure your compute instances to align with your batch processing needs while not sacrificing performance.

The following table lists the key recommendations when designing and managing storage and optimizing performance:

Recommendation | Resources  
---|---  
Use Compute Engine Persistent Disks | We recommend you use the following Compute Engine Persistent Disks configurations:

  * Use [Regional persistent disks](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes#regional_persistent_disks) to allow worker nodes in all zones in a region to access the same underlying durable storage.
  * For workloads that require high-performance storage, use [Local SSDs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/local-ssd) for ephemeral data, or [Extreme Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/extreme-persistent-disk) for persistent data.
  * Use [Hyperdisk Throughput Persistent Disk](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/hyperdisk) to independently and dynamically provision throughput and capacity optimized for batch workloads.

  
Use network-attached storage | Use the following network-attached storage alongside Persistent Disk for optimal storage performance:

  * Use [Filestore](https://docs.cloud.google.com/filestore/docs/csi-driver) to allow all worker nodes in a Pod to access the same storage namespace and [scale capacity](https://docs.cloud.google.com/filestore/docs/scale).
  * Use [Cloud Storage FUSE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/cloud-storage-fuse-csi-driver) to access Cloud Storage directly from a container as a local POSIX mount.

  
Define Pub/Sub | Your batch workload may also read and write data. For example, you can use [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview) and write the results to a data warehouse such as [BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction) from where reports and dashboards are updated. We recommend you use the following storage solutions:

  * For managed object storage, use [Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction).
  * For managed network file storage, use [Filestore](https://docs.cloud.google.com/filestore).
  * For workloads that require file-system semantics, use [Cloud Storage FUSE CSI driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/cloud-storage-fuse-csi-driver#enable). This driver allows Kubernetes applications to mount Cloud Storage buckets as local file systems

  
Specify tuning parameters for your workload | We recommend you use the following configurations:

  * Customize your node system configuration for your workload. For example, set the minimum, default, and maximum values of the TCP socket receive buffer. Use [node system configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config#create).
  * Enable busy polling using network profiles. Some workloads that are sensitive to network latency might be improved. Use network profiles.
  * Increase network bandwidth for GKE nodes by enabling [Google Virtual NIC (gVNIC)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/using-gvnic), a virtual network interface designed specifically for Compute Engine recommended for high performance applications.
  * Specify the number of threads per core to disable [Simultaneous multi-threading](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-smt).

  
Optimize your workloads networking and latency | GKE supports compact placement policy for node pools which specifies that these nodes (and thus the workloads running on them) should be placed in closer physical proximity to each other within a zone. This is especially useful for tightly coupled and high performance workloads where low latency between different processes comprising the workload is a major concern. To learn more, see [compact placement](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/compact-placement).  
Use Spot VMs | Spot VMs are Compute Engine virtual machine (VM) instances that are priced lower than standard Compute Engine VMs and provide no guarantee of availability. We recommend you use the following solutions:

  * Set autoscaling Spot VMs node pools combined with [`location_policy= "ANY"`](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#location_policy) . With this policy, Spot VMs have a lower risk of being preempted. This combination is especially useful for workloads that can survive the preemption of individual worker nodes, such as pleasingly parallel computations.
  * If your workload has a predictable resource footprint, combine [Google Cloud Reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#reservation-billing) and [committed use discounts](https://docs.cloud.google.com/compute/vm-instance-pricing#committed_use) may yield significant savings. Create a node pool with its size set to the number of reserved instances and prioritize saturating this node pool for maximum usage.

  
Use image steaming | Use [Image streaming](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming) to pull container images. GKE streams data from eligible images. This allows your workloads to initialize without waiting for the entire image to download, leading to significantly improved initialization times and better cost efficiency.  
  
### Monitor clusters

GKE is integrated with observability and logging tools that help you monitor the reliability and efficiency of your cluster. The following table lists the key recommendations when enabling and using GKE observability tools:

Recommendation | Resources  
---|---  
Use Prometheus | GKE is integrated with Google Cloud Observability. Customize the metrics that you want GKE to send to Cloud Logging and Cloud Monitoring Google Cloud Managed Service for Prometheus is enabled for GKE clusters by default. We recommend that you use managed collection to eliminate the complexity of setting up and maintaining Prometheus servers. To learn more, see [Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus).  
Use Cloud Monitoring dashboards | Use the Monitoring dashboards for GKE to see a high level overview of cluster and resource utilization and drill down and filter through various metrics and dimensions. To learn more, see [Observing your GKE clusters](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/observing).  
Observe your AI/ML workloads in Google Cloud console |  In Google Cloud console, navigate to **Kubernetes Engine > AI/ML > Jobs** to view your JobSets, Jobs, PyTorchJobs, and RayJobs. You can access details such as logs, events, and visualizations in observability dashboards. To view child Jobs inside a JobSet or workers belonging to a RayJob, in the user interface, navigate to the parent resource. [View Jobs in the Google Cloud console](https://console.cloud.google.com/kubernetes/aiml/jobs)  
  
## What's next

  * Learn how to [Deploy a batch system using Kueue](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/kueue-intro)
  * See the [Best practices for running cost-optimized Kubernetes applications on GKE](https://docs.cloud.google.com/architecture/best-practices-for-running-cost-effective-kubernetes-applications-on-gke#make_sure_your_application_can_grow_vertically_and_horizontally)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
