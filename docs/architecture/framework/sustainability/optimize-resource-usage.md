---
url: https://docs.cloud.google.com/architecture/framework/sustainability/optimize-resource-usage/
title: Optimize resource usage for sustainability \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:22.219746+00:00
---

# Optimize resource usage for sustainability  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/framework/sustainability/optimize-resource-usage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Optimize resource usage for sustainability Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-01-28 UTC

This principle in the sustainability pillar of the [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework/sustainability) provides recommendations to help you optimize resource usage by your workloads in Google Cloud.

## Principle overview

Optimizing resource usage is crucial for enhancing the sustainability of your cloud environment. Every resource that's provisioned—from compute cycles to data storage—directly affects energy usage, water intensity, and carbon emissions. To reduce the environmental footprint of your workloads, you need to make informed choices when you provision, manage, and use cloud resources.

## Recommendations

To optimize resource usage, consider the recommendations in the following sections.

### Implement automated and dynamic scaling

Automated and dynamic scaling ensures that resource usage is optimal, which helps to prevent energy waste from idle or over-provisioned infrastructure. The reduction in wasted energy translates to lower costs and lower carbon emissions.

Use the following techniques to implement automated and dynamic scalability.

#### Use horizontal scaling

Horizontal scaling is the preferred scaling technique for most cloud-first applications. Instead of increasing the size of each instance, known as _vertical scaling_ , you add instances to distribute the load. For example, you can use [managed instance groups (MIGs)](https://docs.cloud.google.com/compute/docs/autoscaler) to automatically scale out a group of Compute Engine VMs. Horizontally scaled infrastructure is more resilient because the failure of an instance doesn't affect the availability of the application. Horizontal scaling is also a resource-efficient technique for applications that have variable load levels.

#### Configure appropriate scaling policies

Configure autoscaling settings based on the requirements of your workloads. Define custom metrics and thresholds that are specific to application behavior. Instead of relying solely on CPU utilization, consider metrics like queue depth for asynchronous tasks, request latency, and custom application metrics. To prevent frequent, unnecessary scaling or _flapping_ , define clear scaling policies. For example, for workloads that you deploy in Google Kubernetes Engine (GKE), configure an appropriate [cluster autoscaling policy](https://cloud.google.com/blog/products/containers-kubernetes/gke-features-to-optimize-resource-allocation).

#### Combine reactive and proactive scaling

With reactive scaling, the system scales in response to real-time load changes. This technique is suitable for applications that have unpredictable spikes in load.

Proactive scaling is suitable for workloads with predictable patterns, such as fixed daily business hours and weekly reports generation. For such workloads, use scheduled autoscaling to pre-provision resources so that they can handle an anticipated load level. This technique prevents a scramble for resources and ensures smoother user experience with higher efficiency. This technique also helps you plan proactively for known spikes in load such as major sales events and focused marketing efforts.

Google Cloud managed services and features like GKE Autopilot, Cloud Run, and MIGs automatically manage proactive scaling by learning from your workload patterns. By default, when a Cloud Run service doesn't receive any traffic, it scales to zero instances.

#### Design stateless applications

For an application to scale horizontally, its components should be stateless. This means that a specific user's session or data isn't tied to a single compute instance. When you store session state outside the compute instance, such as in Memorystore for Redis, any compute instance can handle requests from any user. This design approach enables horizontal scaling that's seamless and efficient.

### Use scheduling and batches

Batch processing is ideal for large-scale, non-urgent workloads. Batch jobs can help to optimize your workloads for energy efficiency and cost.

Use the following techniques to implement scheduling and batch jobs.

#### Schedule for low carbon intensity

Schedule your batch jobs to run in low-carbon regions and during periods when the local electrical grid has a high percentage of clean energy. To identify the least carbon-intensive times of day for a region, use the [Carbon Footprint report](https://docs.cloud.google.com/carbon-footprint/docs/view-carbon-data).

#### Use Spot VMs for noncritical workloads

[Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot) let you take advantage of unused Compute Engine capacity at a steep discount. Spot VMs can be preempted, but they provide a cost-effective way to process large datasets without the need for dedicated, always-on resources. Spot VMs are ideal for non-critical, fault-tolerant batch jobs.

#### Consolidate and parallelize jobs

To reduce the overhead for starting up and shutting down individual jobs, group similar jobs into a single large batch. Run these high-volume workloads on services like [Batch](https://docs.cloud.google.com/batch/docs/get-started). The service automatically provisions and manages the necessary infrastructure, which helps to ensures optimal resource utilization.

#### Use managed services

Managed services like Batch and [Dataflow](https://docs.cloud.google.com/dataflow/docs/overview) automatically handle resource provisioning, scheduling, and monitoring. The cloud platform handles resource optimization. You can focus on the application logic. For example, [Dataflow automatically scales the number of workers](https://docs.cloud.google.com/dataflow/docs/horizontal-autoscaling) based on the data volume in the pipeline, so you don't pay for idle resources.

### Match VM machine families to workload requirements

The machine types that you can use for your Compute Engine VMs are grouped into [machine families](https://docs.cloud.google.com/compute/docs/machine-resource), which are optimized for different workloads. Choose appropriate machine families based on the requirements of your workloads.

Machine family | Recommended for workload types | Sustainability guidance  
---|---|---  
**General-purpose instances (E2, N2, N4, Tau T2A/T2D)** : These instances provide a balanced ratio of CPU to memory. | Web servers, microservices, small to medium databases, and development environments. | The E2 series is highly cost-efficient and energy-efficient due to its dynamic allocation of resources. The Tau T2A series uses Arm-based processors, which are often more energy-efficient per unit of performance for large-scale workloads.  
**Compute-optimized instances (C2, C3)** : These instances provide a high vCPU-to-memory ratio and high performance per core. | High performance computing (HPC), batch processing, gaming servers, and CPU-based data analytics. | A C-series instance lets you complete CPU-intensive tasks faster, which reduces the total compute time and energy consumption of the job.   
**Memory-optimized instances (M3, M2)** : These instances are designed for workloads that require a large amount of memory. | Large in-memory databases and data warehouses, such as SAP HANA or in-memory analytics. | Memory-optimized instances enable the consolidation of memory-heavy workloads on fewer physical nodes. This consolidation reduces the total energy that's required when compared to using multiple smaller instances. High-performance memory reduces data-access latency, which can reduce the total time that the CPU spends in an active state.  
**Storage-optimized instances (Z3):** These instances provide high-throughput, low-latency local SSD storage. | Data warehousing, log analytics, and SQL, NoSQL, and vector databases.  | Storage-optimized instances process massive datasets locally, which helps to eliminate the energy that's used for cross-location network data egress. When you use local storage for high-IOPS tasks, you avoid over-provisioning multiple standard instances.  
**Accelerator-optimized instances (A3, A2, G2)** : These instances are built for GPU and TPU-accelerated workloads, such as AI, ML, and HPC. | ML model training and inference, and scientific simulations. | [TPUs](https://docs.cloud.google.com/tpu) are engineered for optimal energy efficiency. They deliver higher computations per watt. A GPU-accelerated instance like the A3 series with NVIDIA H100 GPUs can be significantly more energy-efficient for training large models than a CPU-only alternative. Although a GPU-accelerated instance has higher nominal power usage, the task is completed much faster.  
  
### Upgrade to the latest machine types

Use of the latest machine types might help to improve sustainability. When machine types are updated, they're often designed to be more energy-efficient and to provide higher performance per watt. VMs that use the latest machine types might complete the same amount of work with lower power consumption.

CPUs, GPUs, and TPUs often benefit from technical advancements in chip architecture, such as the following:

  * **Specialized cores** : Advancements in processors often include specialized cores or instructions for common workloads. For example, CPUs might have dedicated cores for vector operations or integrated AI accelerators. When these tasks are offloaded from the main CPU, the tasks are completed more efficiently and they consume less energy.
  * **Improved power management** : Advancements in chip architectures often include more sophisticated power management features, such as dynamic adjustment of voltage and frequency based on the workload. These power-management features enable the chips to run at peak efficiency and enter low-power states when they are idle, which minimizes energy consumption.



The technical improvements in chip architecture provide the following direct benefits for sustainability and cost:

  * **Higher performance per watt** : This is a key metric for sustainability. For example, the [C4 VMs demonstrate 40% higher price-performance](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4_series) when compared to C3 VMs for the same energy consumption. The [C4A processor provides 60% higher energy-efficiency](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_series) over comparable x86 processors. These performance capabilities let you complete tasks faster or use fewer instances for the same load.
  * **Lower total energy consumption** : With improved processors, compute resources are used for a shorter duration for a given task, which reduces the overall energy usage and carbon footprint. The carbon impact is particularly high for short-lived, compute-intensive workloads like batch jobs and ML model training.
  * **Optimal resource utilization** : The latest machine types are often better suited for modern software and are more compatible with advanced features of cloud platforms. These machine types typically enable better resource utilization, which reduces the need for over-provisioning and helps to ensure that every watt of power is used productively.



### Deploy containerized applications

You can use container-based, fully-managed services such as GKE and Cloud Run as a part of your strategy for sustainable cloud computing. These services help to optimize resource utilization and automate resource management.

#### Leverage the scale-to-zero capability of Cloud Run

Cloud Run provides a managed serverless environment that automatically scales instances to zero when there is no incoming traffic for a service or when a job is completed. Autoscaling helps to eliminate energy consumption by idle infrastructure. Resources are powered only when they actively process requests. This strategy is highly effective for intermittent or event-driven workloads. For AI workloads, you can use [GPUs with Cloud Run](https://docs.cloud.google.com/run/docs/configuring/services/gpu), which lets you consume and pay for GPUs only when they are used.

#### Automate resource optimization using GKE

GKE is a container orchestration platform, which ensures that applications use only the resources that they need. To help you automate resource optimization, GKE provides the following techniques:

  * **[Bin packing](https://kubernetes.io/docs/concepts/scheduling-eviction/resource-bin-packing/)** : GKE Autopilot intelligently packs multiple containers on the available nodes. Bin packing maximizes the utilization of each node and reduces the number of idle or underutilized nodes, which helps to reduce energy consumption.
  * **[Horizontal Pod autoscaling (HPA)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler)** : With HPA, the number of container replicas (Pods) is adjusted automatically based on predefined metrics like CPU usage or custom application-specific metrics. For example, if your application experiences a spike in traffic, GKE adds Pods to meet the demand. When the traffic subsides, GKE reduces the number of Pods. This dynamic scaling prevents over-provisioning of resources, so you don't pay for or power up unnecessary compute capacity.
  * **[Vertical Pod autoscaling (VPA)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler)** : You can configure GKE to automatically adjust the CPU and memory allocations and limits for individual containers. This configuration ensures that a container isn't allocated more resources than it needs, which helps to prevent resource over-provisioning.
  * **[GKE multidimensional Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multidimensional-pod-autoscaling)** : For complex workloads, you can configure HPA and VPA simultaneously to optimize both the number of Pods and the size of each Pod. This technique helps to ensure the smallest possible energy footprint for the required performance.
  * **[Topology-Aware Scheduling (TAS)](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/schedule-gke-workloads-tas)** : TAS enhances the network efficiency for AI and ML workloads in GKE by placing Pods based on the physical structure of the data center infrastructure. TAS strategically colocates workloads to minimize network hops. This colocation helps to reduce communication latency and energy consumption. By optimizing the physical alignment of nodes and specialized hardware, TAS accelerates task completion and maximizes the energy efficiency of large-scale AI and ML workloads.



### Configure carbon-aware scheduling

At Google, we continually shift our workloads to [locations](https://blog.google/outreach-initiatives/sustainability/carbon-aware-computing-location/) and [times](https://blog.google/inside-google/infrastructure/data-centers-work-harder-sun-shines-wind-blows/) that provide the cleanest electricity. We also repurpose, or [harvest](https://cloud.google.com/blog/topics/sustainability/hardware-harvesting-at-google-reducing-waste-and-emissions), older equipment for alternative use cases. You can use this carbon-aware scheduling strategy to ensure that your containerized workloads use clean energy.

To implement carbon-aware scheduling, you need information about the energy mix that powers data centers in a region in real time. You can get this information in a machine-readable format from the [Carbon free energy for Google Cloud regions](https://github.com/GoogleCloudPlatform/region-carbon-info) repository in GitHub or from a [BigQuery public dataset](https://console.cloud.google.com/marketplace/product/bigquery-public-datasets/regional-cfe). The hourly grid mix and carbon intensity data that's used to calculate the Google annual carbon dataset is sourced from [Electricity Maps](https://app.electricitymaps.com/).

To implement carbon-aware scheduling, we recommend the following techniques:

  * **Geographical shifting** : Schedule your workloads to run in regions that use a higher proportion of renewable energy sources. This approach lets you use cleaner electrical grids.
  * **Temporal shifting** : For non-critical, flexible workloads like batch processing, configure the workloads to run during off-peak hours or when renewable energy is most abundant. This approach is known as temporal shifting and helps reduce the overall carbon footprint by taking advantage of cleaner energy sources when they are available.



### Architect energy-efficient disaster recovery

Preparing for disaster recovery (DR) often involves pre-provisioning redundant resources in a secondary region. However, idle or under-utilized resources can cause significant energy waste. Choose DR strategies that maximize resource utilization and minimize the carbon impact without compromising your recovery time objectives (RTO).

#### Optimize for cold start efficiency

Use the following approaches to minimize or eliminate active resources in your secondary (DR) region:

  * **Prioritize[cold DR](https://en.wikipedia.org/wiki/Backup_site#Cold_site)**: Keep resources in the DR region turned off or in a scaled-to-zero state. This approach helps to eliminate the carbon footprint of idle compute resources.
  * **Take advantage of serverless failover** : Use managed serverless services like Cloud Run for DR endpoints. Cloud Run scales to zero when it isn't in use, so you can maintain a DR topology that consumes no energy until traffic is diverted to the DR region.
  * **Automate recovery with infrastructure-as-code (IaC)** : Instead of keeping resources in the DR site running (warm), use an IaC tool like Terraform to rapidly provision environments only when needed.



#### Balance redundancy and utilization

Resource redundancy is a primary driver of energy waste. To reduce redundancy, use the following approaches:

  * **Prefer active-active over active-passive** : In an active-passive setup, the resources in the passive site are idle, which results in wasted energy. An active-active architecture that's optimally sized ensures that all of the provisioned resources across both regions actively serve traffic. This approach helps you maximize the energy efficiency of your infrastructure.
  * **Right-size redundancy** : Replicate data and services across regions only when the replication is necessary to meet high-availability or DR requirements. Every additional replica increases the energy cost of persistent storage and network egress.



[ Previous arrow_back  Optimize AI and ML workloads  ](https://docs.cloud.google.com/architecture/framework/sustainability/ai-ml-energy-efficiency)

[ Next Develop energy-efficient software  arrow_forward  ](https://docs.cloud.google.com/architecture/framework/sustainability/energy-efficient-software)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-28 UTC."],[],[]] 
