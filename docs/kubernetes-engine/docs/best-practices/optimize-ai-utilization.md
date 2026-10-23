---
url: https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/optimize-ai-utilization/
title: Best practices for GKE AI/ML workload prioritization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:57.399499+00:00
---

# Best practices for GKE AI/ML workload prioritization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/optimize-ai-utilization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Best practices for GKE AI/ML workload prioritization Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document describes tools and best practices for maximizing resource utilization and minimizing downtime of heterogeneous AI/ML workloads in Google Kubernetes Engine (GKE), especially when there's no capacity in reservations or through on-demand resources. _Heterogeneous workloads_ refer to different types of AI/ML workloads that run simultaneously in the same GKE cluster. For example, you might run a latency-sensitive online inference service alongside a series of interruptible batch training jobs.

This guide provides recommendations for Platform admins and operators and Data and AI specialists. For a consolidated overview of all GKE best practices, see [Best practices for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices).

## Benefits of AI/ML workload prioritization

Heterogeneous workloads have different priorities and share limited capacity and resources. The best practices in this page describe how to configure GKE and open source tools to help you get the following benefits:

  * Minimize downtime for high-priority workloads.
  * Quickly execute high-priority workloads.
  * Optimize resource consumption.



## Background

GKE supports the following open source tools for optimizing resource utilization.

  * **Kueue:** a Kubernetes-native workload queueing system designed for batch, AI, and high performance computing workloads. Kueue can be extended to manage other workload types, such as those defined by Custom Resource Definitions like `leaderworkerset`. Kueue manages quotas and how workloads consume them in a Kubernetes cluster. Kueue makes decisions about when a workload waits, when a workload starts (for example, by creating the Pod), and when a Pod belonging to a workload gets preempted.

For more information about Kueue, see the [Kueue concepts](https://kueue.sigs.k8s.io/docs/concepts/) documentation.

  * **Hotswap:** a technique that reduces mean time to recovery (MTTR). Hotswap enables preemption based on workload priority when cluster resources are fully utilized and no additional capacity is available, either from on-demand instances or existing reservations.

    * When a node that hosts a workload becomes unhealthy, the workload is rescheduled on eligible spare nodes. If no spare nodes are available, Hotswap can preempt a lower-priority workload to make room for the workload being recovered.
    * If you configure your Pods with `PriorityClass`, the workload configured with higher priority evicts a running low-priority workload to acquire its resources. This eviction process is known as preemption.



## Use cases

Use the following table to understand the best practices for each use case:

Use case | Best practice | Description  
---|---|---  
Multiple workloads with different priorities | Use Kueue to define queues and assign priorities to workloads based on their importance. Kueue can manage quota so that certain teams or projects have access to a set amount of resources. |  Kueue lets you apply the following configurations:

  * Prioritize high priority Jobs by assigning higher Kueue `WorkloadPriority` to them.
  * Enable Kueue's fair-share queuing so that all workloads eventually receive resources, even low-priority ones.

To test the best practice configuration, see the Kueue example in this document.  
You have to reduce the current MTTR. | Use Hotswap to reschedule workloads in healthy resources when an interruption occurs, and preempt low-priority workloads in favor of high-priority workloads. |  Hotswap lets you apply the following configurations:

  * Configure [PriorityClasses](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/) to define priority levels for your workloads.
  * Assign higher `PriorityClasses` to critical workloads.
  * Automatically reschedule workloads on healthy nodes when interruptions occur.

To test the best practice configuration, see the Hotswap example in this document.  
Multiple AI workloads competing for limited resources | Combine Kueue and Hotswap. This combination provides a robust system that prioritizes critical workloads both during initial scheduling and during runtime. |  Kueue and Hotswap let you apply the following configurations:

  * Use Kueue to manage the initial scheduling and admission of workloads based on priority.
  * Use Hotswap to handle workload interruptions and enable rapid recovery. Hotswap helps to reduce the time to recovery of a high-priority workload when an interruption occurs.

To test the best practice configuration, see the Kueue and Hotswap example in this document.  
  
## Examples of best practice implementations

The following examples demonstrate how to implement Kueue and Hotswap, and how to combine them for the best practices described in the preceding section.

### Kueue

The following example manifest shows a Kueue configuration:
    
    
      apiVersion: kueue.x-k8s.io/v1beta1
      kind: ResourceFlavor
      metadata:
        name: tpu-v6e-slice
      spec:
        nodeLabels:
          cloud.google.com/gke-tpu-accelerator: tpu-v6e-slice
      ---
      apiVersion: kueue.x-k8s.io/v1beta1
      kind: ClusterQueue
      metadata:
        name: tpu-training-cq
      spec:
        resourceGroups:
        - flavors:
          - name: tpu-v6e-slice
            resources:
            - name: google.com/tpu
              nominalQuota: 32
        queueingStrategy: BestEffortFIFO
        preemption:
          reclaimWithinCohort: Never
          reclaimOutOfCohort:
            enable: true
            reclaimMoreThanNominalQuota: false
      ---
      apiVersion: kueue.x-k8s.io/v1beta1
      kind: LocalQueue
      metadata:
        name: default-queue
        namespace: default
      spec:
        clusterQueue: tpu-training-cq
    

This manifest does the following:

  * Defines a `ResourceFlavor` named `tpu-v6e-slice` that specifies the node labels for TPU v6e slices.
  * Defines a `ClusterQueue` named `tpu-training-cq` that manages the quota for TPU resources.
  * Defines a `LocalQueue` named `default-queue` that allows workloads in the `default` namespace to use the `tpu-training-cq` cluster queue.



### Hotswap

The following example shows a Hotswap configuration that defines two Priority Classes, `low-priority-job` and `high-priority-job`. This Hotswap configuration creates a high-priority JobSet workload and uses [MaxText](https://github.com/google/maxtext).
    
    
      apiVersion: scheduling.k8s.io/v1
      kind: PriorityClass
      metadata:
        name: low-priority-job
      value: 1000000
      globalDefault: false
      description: "This priority class should be used for low priority pods only."
      ---
      apiVersion: scheduling.k8s.io/v1
      kind: PriorityClass
      metadata:
        name: high-priority-job
      value: 2000000
      globalDefault: false
      description: "This priority class should be used for critical pods only."
      ---
      apiVersion: jobset.x-k8s.io/v1alpha2
      kind: JobSet
      metadata:
        name: high-jax-trillium
        annotations:
          alpha.jobset.sigs.k8s.io/exclusive-topology: cloud.google.com/gke-nodepool
      spec:
        failurePolicy:
          maxRestarts: 10
          restartStrategy: BlockingRecreate
        replicatedJobs:
        - name: slice
          replicas: 2
          template:
            spec:
              backoffLimit: 0
              completions: 4
              parallelism: 4
              template:
                spec:
                  nodeSelector:
                    cloud.google.com/gke-tpu-accelerator: tpu-v6e-slice
                    cloud.google.com/gke-tpu-topology: 4x4
                  hostNetwork: true
                  dnsPolicy: ClusterFirstWithHostNet
                  priorityClassName: high-priority-job
                  containers:
                  - name: jax-program
                    image: <IMAGE LOCATION>
                    command:
                    -   python3
                    -   MaxText/train.py
                    -   MaxText/configs/base.yml
                    -   model_name=llama2-7b
                    -   run_name=<UNIQUE RUN NAME>
                    -   steps=300
                    -   base_output_directory=gs://<OUTPUT BUCKET>
                    -   dataset_path=gs://max-datasets-rogue
                    -   max_target_length=4096
                    -   dataset_type=synthetic
                    -   enable_checkpointing=False
                    resources:
                      limits:
                        google.com/tpu: 4
    

Based on this configuration, Hotswap performs the following actions:

  * If an infrastructure failure interrupts the high-priority workload, the JobSet restarts it. Hotswap preempts the low-priority workload to reschedule the high-priority workload before the infrastructure recovers. The low-priority workload remains in a failed status. This process significantly reduces workload idle time.
  * When the infrastructure recovers, Hotswap reschedules the low-priority workload in the node pool that recovered.



### Kueue and Hotswap

Combine Kueue and Hotswap when you operate in a complex environment with limited resources. This combination provides a robust system that prioritizes critical workloads during initial scheduling and during runtime.

The following example shows a combined Kueue and Hotswap configuration. This example uses [MaxText](https://github.com/google/maxtext):
    
    
      apiVersion: scheduling.k8s.io/v1
      kind: PriorityClass
      metadata:
        name: low-priority-job
      value: 1000000
      globalDefault: false
      description: "This priority class should be used for low priority pods only."
      ---
      apiVersion: scheduling.k8s.io/v1
      kind: PriorityClass
      metadata:
        name: high-priority-job
      value: 2000000
      globalDefault: false
      description: "This priority class should be used for critical pods only."
      ---
      apiVersion: kueue.x-k8s.io/v1beta1
      kind: ResourceFlavor
      metadata:
        name: tpu-v6e-slice
      spec:
        nodeLabels:
          cloud.google.com/gke-tpu-accelerator: tpu-v6e-slice
      ---
      apiVersion: kueue.x-k8s.io/v1beta1
      kind: ClusterQueue
      metadata:
        name: tpu-training-cq
      spec:
        resourceGroups:
        - flavors:
          - name: tpu-v6e-slice
            resources:
            - name: google.com/tpu
              nominalQuota: 32
        queueingStrategy: BestEffortFIFO
        preemption:
          reclaimWithinCohort: Never
          reclaimOutOfCohort:
            enable: true
            reclaimMoreThanNominalQuota: false
      ---
      apiVersion: kueue.x-k8s.io/v1beta1
      kind: LocalQueue
      metadata:
        name: default-queue
        namespace: default
      spec:
        clusterQueue: tpu-training-cq
      ---
      apiVersion: jobset.x-k8s.io/v1alpha2
      kind: JobSet
      metadata:
        name: low-jax-trillium
        annotations:
          kueue.x-k8s.io/queue-name: default-queue
          alpha.jobset.sigs.k8s.io/exclusive-topology: cloud.google.com/gke-nodepool
      spec:
        failurePolicy:
          maxRestarts: 10
          restartStrategy: BlockingRecreate
        replicatedJobs:
        - name: slice
          replicas: 2
          template:
            spec:
              backoffLimit: 0
              completions: 4
              parallelism: 4
              template:
                metadata:
                  labels:
                    kueue.x-k8s.io/managed-by: kueue
                    kueue.x-k8s.io/priority-class: low-priority-job
                spec:
                  nodeSelector:
                    cloud.google.com/gke-tpu-accelerator: tpu-v6e-slice
                    cloud.google.com/gke-tpu-topology: 4x4
                  hostNetwork: true
                  dnsPolicy: ClusterFirstWithHostNet
                  priorityClassName: low-priority-job
                  containers:
                  - name: jax-program
                    image: <IMAGE LOCATION>
                    command:
                    - python3
                    - MaxText/train.py
                    - MaxText/configs/base.yml
                    - model_name=llama2-7b
                    - run_name=low-priority-run
                    - steps=30000
                    - base_output_directory=gs://<OUTPUT BUCKET>
                    - dataset_path=gs://max-datasets-rogue
                    - max_target_length=4096
                    - dataset_type=synthetic
                    - enable_checkpointing=False
                    resources:
                      limits:
                        google.com/tpu: 4
      ---
      apiVersion: jobset.x-k8s.io/v1alpha2
      kind: JobSet
      metadata:
        name: high-jax-trillium
        annotations:
          kueue.x-k8s.io/queue-name: default-queue
          alpha.jobset.sigs.k8s.io/exclusive-topology: cloud.google.com/gke-nodepool
      spec:
        failurePolicy:
          maxRestarts: 10
          restartStrategy: BlockingRecreate
        replicatedJobs:
        - name: slice
          replicas: 2
          template:
            spec:
              backoffLimit: 0
              completions: 4
              parallelism: 4
              template:
                metadata:
                  labels:
                    kueue.x-k8s.io/managed-by: kueue
                    kueue.x-k8s.io/priority-class: high-priority-job
                spec:
                  nodeSelector:
                    cloud.google.com/gke-tpu-accelerator: tpu-v6e-slice
                    cloud.google.com/gke-tpu-topology: 4x4
                  hostNetwork: true
                  dnsPolicy: ClusterFirstWithHostNet
                  priorityClassName: high-priority-job
                  containers:
                  - name: jax-program
                    image: <IMAGE LOCATION>
                    command:
                    - python3
                    - MaxText/train.py
                    - MaxText/configs/base.yml
                    - model_name=llama2-7b
                    - run_name=high-priority-run
                    - steps=300
                    - base_output_directory=gs://<OUTPUT BUCKET>
                    - dataset_path=gs://max-datasets-rogue
                    - max_target_length=4096
                    - dataset_type=synthetic
                    - enable_checkpointing=False
                    resources:
                      limits:
                        google.com/tpu: 4
    

Based on this configuration, Kueue is combined with Hotswap, and performs the following actions:

  * Kueue manages the admission of both `low-jax-trillium` and `high-jax-trillium` JobSets into the cluster queue based on their defined priorities and available resources.
  * If the `high-jax-trillium` JobSet is interrupted by an infrastructure failure, Hotswap preempts the `low-jax-trillium` JobSet to reschedule the high-priority JobSet.
  * Hotswap ensures the high-priority JobSet restarts quickly, minimizing its idle time.
  * When the infrastructure recovers, Hotswap reschedules the low-priority JobSet in the recovered node pool.



## What's next

  * Learn how to [deploy GPU workloads in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gpus).
  * Learn how to [deploy TPU workloads in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
