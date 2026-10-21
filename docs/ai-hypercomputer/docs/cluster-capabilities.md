---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/cluster-capabilities/
title: Cluster management capabilities \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:34:52.117154+00:00
---

# Cluster management capabilities  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/cluster-capabilities/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Cluster management capabilities Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

Clustered GPUs, such as [A4X Max](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus#a4x-max-machine), [A4X](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus#a4x-machine), [A4](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus#a4-machine), [A3 Ultra](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus#a3-ultra), [A3 Mega](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus#a3-mega), and [A3 High (8 GPUs)](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus#a3-high) machine series, are designed to enable you to run large-scale artificial intelligence (AI) and machine learning (ML) clusters and provide the following cluster management capabilities:

  * Clustered GPU infrastructure colocation
  * Cluster topology-aware placement
  * Cluster operational mode
  * Cluster maintenance scheduling and controls
  * Cluster monitoring and diagnostic tooling



## Supported machine series

The cluster management capabilities described on this page are available for the [Clustered GPU machine series](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus), which are optimized for multi-node, large-scale workloads.

These features don't apply to the [General GPU machine series](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus), which consist of independent compute resources that use standard VPC networking and don't support maintenance operational modes or dense colocation.

The following table summarizes the machine series supported in AI Hypercomputer:

Category | Machine series | Supports cluster management  
---|---|---  
Clustered GPUs | [A4X Max](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus#a4x), [A4X](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus#a4x), [A4](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus#a4), [A3 Ultra](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus#a3-ultra), [A3 Mega](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus#a3-mega), [A3 High](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus#a3-high) | Yes  
General GPUs | [A3 Edge](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus#a3-edge), [A2](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus#a2), [G2](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus#g2), [G4](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus#g4), [N1](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus#n1) | No  
  
For more information about each machine series, see [About GPU accelerators](https://docs.cloud.google.com/ai-hypercomputer/docs/understand-gpus).

**Important:** For A3 Mega and A3 High instances created before October 1, 2025, cluster management capabilities aren't supported. To check if reserved A3 Mega or A3 High instances have cluster management capabilities, [view the details of the reservation](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity#view-reservation) that you used to create the Compute Engine instances and verify that the `deploymentType` field in the output is set to `DENSE`. For more information about using A3 Mega or A3 High instances in a cluster, contact your account team.

Most cluster management capabilities are only supported for _reservation-bound capacity_ —infrastructure that uses the [reservation-bound provisioning model](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models), which only supports clustered GPUs machine types. For capacity that uses any other provisioning model, only the following cluster management capabilities are available:

  * AI infrastructure resources colocation
  * Cluster topology-aware placement
  * [Manage host events across instances](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/host-events)



## Clustered GPU infrastructure colocation

When you use clustered GPUs, such as A4X Max, A4X, A4, A3 Ultra, A3 Mega, and A3 High (8 GPUs), you can request [host machines](https://docs.cloud.google.com/ai-hypercomputer/docs/terminology#node) that Compute Engine provisions as close together as possible. These machines offer the following features:

  * Compute Engine provisions the machines as [blocks of resources](https://docs.cloud.google.com/ai-hypercomputer/docs/terminology#block).

  * A [dynamic machine learning (ML) network fabric](https://docs.cloud.google.com/ai-hypercomputer/docs/terminology#network-fabric) interconnects the machines.




This resource arrangement minimizes network hops and optimizes for lowest network latency. To deploy blocks of accelerator-optimized machines that Compute Engine densely allocates, you can use the following options:

  * Resources are required to be densely allocated with each other when you do one or more of the following:

    * Create resources that use the same [Future reservation in AI Hypercomputer](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models#future-reservations) or [Future reservation in calendar mode](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models#calendar-mode).

    * Deploy a [managed instance group (MIG)](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-overview) that uses [resize requests](https://docs.cloud.google.com/compute/docs/instance-groups/about-resize-requests-mig) and create the resources in the same request.

    * Specify that resources use the same [compact placement policy or workload policy](https://docs.cloud.google.com/ai-hypercomputer/docs/placement-policy-and-workload-policy) that specifies a max distance value. Specifically, resources are only required to be as close as the max distance value of the policy specifies.

  * Resources are optionally densely allocated with each other, based on best-effort availability, when you do one or more of the following:

    * Create resources in the same request for [Flex-start VMs](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models#flex-start).

    * Specify that resources use the same [compact placement policy or workload policy](https://docs.cloud.google.com/ai-hypercomputer/docs/placement-policy-and-workload-policy) that doesn't specify a max distance.




## Cluster topology-aware placement

After you create clustered GPUs, you can get topology information at the node and cluster levels. This information helps you do the following:

  * Adjust your application or workload design to further minimize network latency.

  * Understand and troubleshoot network latency and performance issues for instances that communicate frequently with each other. These issues can occur if the instances are unexpectedly located far apart.




Specifically, support for topology capabilities is as follows:

  * Topology information works best with reservation-bound capacity, which is required in order to [view the topology of a reservation](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity#view-capacity-topology).

  * Topology capabilities only support [machine types that support compact placement policies](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview).

  * For Spot VMs, topology information only appears when a machine uses a compact placement policy.




For more information, see [View compute instances topology](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/vms-topology).

## Cluster operational mode

When you reserve capacity to create compute instances or clusters by using clustered GPUs, the machine type that you reserve determines the cluster _operational mode_ for the instances. This mode specifies how your instances behave after [host errors](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#hosterror) or faulty host reports. The available operational modes for an instance are _managed mode_ , where Compute Engine automatically replaces any faulty machines but holds back part of your reserved capacity to provide your instances have the necessary resources to restart. Or _all-capacity mode_ , where you have access to your full reserved capacity but are responsible for managing failures and planned maintenance.

For more information, see [Reservation operational mode](https://docs.cloud.google.com/ai-hypercomputer/docs/create/review-configurations#maintenance-operational-mode).

## Cluster maintenance scheduling and controls

You control maintenance of clustered GPUs by using topology-aware scheduling in a block of resources. This capability helps synchronize upgrades so that your workloads are more resilient to host events and minimize disruptions. This approach helps improve the [_goodput_ of your workload](https://cloud.google.com/blog/products/ai-machine-learning/goodput-metric-as-measure-of-ml-productivity).

To facilitate full control of maintenance events, you can use the following features:

  * Maintenance scheduling type

  * Manage host events




### Maintenance scheduling type

When you reserve capacity to create compute instances or clusters of clustered GPUs, you can define how Compute Engine maintains the infrastructure that your instances run on. Based on the machine type that you want to use for your instances, you can choose between synchronized maintenance across instances (_grouped_), or different maintenance schedules (_independent_).

For more information, see [Maintenance scheduling types](https://docs.cloud.google.com/ai-hypercomputer/docs/create/review-configurations#maintenance-scheduling-types).

### Manage host events

After you create clustered GPUs and start your workload, you can set up alerts and receive notifications when maintenance for your instances or reserved blocks is scheduled, starts, or is completed. You can also view and, if needed, manually start maintenance on an instance or reserved block before its scheduled time. These options help you proactively control and minimize downtimes to your workloads.

For more information, see the following:

  * [Manage host events across instances](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/host-events)

  * [Manage host events across reservations](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/host-events-reservations)




## Cluster monitoring and diagnostic tooling

For monitoring and troubleshooting, clustered GPUs include the following services:

  * [VM health degradation prediction](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/enable-node-health-prediction), which helps you identify VMs that are likely to degrade within the next five hours.

  * [Faulty host reporting](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/report-faulty-host), which you can use to flag issues with individual host machines.

  * [Support for Cloud Monitoring metrics](https://docs.cloud.google.com/ai-hypercomputer/docs/monitor), which help you monitor networks and GPUs performance.




## What's next?

  * [Terminology](https://docs.cloud.google.com/ai-hypercomputer/docs/terminology)

  * [Choose a deployment strategy](https://docs.cloud.google.com/ai-hypercomputer/docs/choose-strategy)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
