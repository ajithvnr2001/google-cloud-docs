---
url: https://docs.cloud.google.com/tpu/docs/capacity-modes/
title: TPU capacity modes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:39:22.761722+00:00
---

# TPU capacity modes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/capacity-modes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# TPU capacity modes

**Caution:** The [Compute Engine Service Level Agreement (SLA)](https://cloud.google.com/compute/sla) doesn't apply to All Capacity mode TPUs.

TPUs offer two capacity modes: _managed capacity mode_ and _All Capacity mode_. Each mode defines how hardware maintenance and host errors are handled, as well as your level of visibility and control over the TPU hardware topology.

**Note:** By default, TPU resources use managed capacity mode for automated host recovery. Managed capacity mode is separate from the [managed reservation operational mode](https://docs.cloud.google.com/ai-hypercomputer/docs/create/review-configurations#managed), which is not supported on TPUs.

## Overview of TPU capacity modes

The following table summarizes the key differences between managed capacity mode and All Capacity mode:

| Managed capacity mode | All Capacity mode  
---|---|---  
**Capacity access** | Google manages capacity allocation and host recovery across available infrastructure. | 100% of reserved capacity is accessible for workloads. You're responsible for managing spare capacity for failure recovery. You can target specific blocks or sub-blocks for precise, topology-aware workload placement.  
**Hardware topology visibility** | Compute Engine abstracts the physical topology. | Full visibility into cluster, block, sub-block, and host topology and utilization.  
**Fault recovery** | Compute Engine automatically detects faulty TPU slices and restarts them on healthy hardware. | Google automatically detects and repairs faulty hardware. You are responsible for monitoring TPU slice health and rescheduling unhealthy slices to healthy spare hardware that you set aside in your reservation.  
**Maintenance control** | Compute Engine schedules and manages maintenance events. You can optionally start maintenance before the scheduled maintenance time. | You have granular control to schedule and initiate maintenance on a reservation, block, or sub-block level.  
**Supported TPU versions** | All TPU versions. | TPU v6e (Trillium) and TPU7x (Ironwood)  
**Supported consumption options** | All consumption options. | You must have a future reservation with a minimum capacity size for one year or longer. Future reservations in calendar mode aren't supported. Contact your Google Cloud account team for details and to request an All Capacity mode reservation.  
  
## Managed capacity mode

By default, TPU capacity operates in managed capacity mode. In this mode, Compute Engine automatically detects hardware faults and replaces affected TPU instances to ensure that your workloads can restart on healthy hardware.

Managed capacity mode has the following features:

  * **Automated instance recovery** : For on-demand, Flex-start, and reservation consumption options, Compute Engine automatically detects hardware faults and replaces affected TPU instances.
  * **Streamlined management** : No manual intervention required for host maintenance or repair operations.



## All Capacity mode

All Capacity mode is designed to give you direct, reservation-based control over your TPU resources. In All Capacity mode, you have access to 100% of your reserved capacity. You are responsible for managing TPU slice recovery using sufficient healthy spare capacity and for scheduling maintenance events.

All Capacity mode has the following features:

  * **Full capacity allocation** : Access all of your reserved capacity with no holdbacks, including any spare capacity allocated for failure recovery or workload bursting.
  * **Topology-aware placement** : Gain full visibility into cluster, block, sub-block, and host topology to optimize workload placement.
  * **Advanced maintenance control** : Schedule and trigger maintenance events at the reservation, block, or sub-block level.
  * **Report and repair** : Report low-performing hardware for repair.



Contact your Google Cloud account team to request an All Capacity mode reservation. For more information, see [All Capacity mode overview](https://docs.cloud.google.com/tpu/docs/all-capacity-overview).

## What's next

  * [Plan your Cloud TPU resources](https://docs.cloud.google.com/tpu/docs/plan-tpus)
  * [All Capacity mode overview](https://docs.cloud.google.com/tpu/docs/all-capacity-overview)
  * [Request an All Capacity mode reservation](https://docs.cloud.google.com/tpu/docs/request-all-capacity-mode-reservation)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
