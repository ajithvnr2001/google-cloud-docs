---
url: https://docs.cloud.google.com/tpu/docs/monitor-capacity/
title: Monitor fleetwide capacity \u00a0|\u00a0 Cloud TPU \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:30.544360+00:00
---

# Monitor fleetwide capacity  |  Cloud TPU  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/monitor-capacity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Monitor fleetwide capacity

Fleetwide capacity metrics provide you with key information about the health states, availability, and efficiency of your entire TPU fleet. You can use capacity metrics to identify optimization opportunities, improve resource allocation, and enhance workload performance.

## Metrics

The following fleetwide capacity metrics are available under the `compute.googleapis.com` namespace. They also serve as the building blocks for the derived capacity metrics, which use the fleetwide capacity metrics to gauge fleetwide usage and efficiency at a given time point.

### Committed Chips Count

**Note:** This metric is only available for [All Capacity mode](https://docs.cloud.google.com/tpu/docs/all-capacity-overview) reservations.

The Committed Chips Count (`compute.googleapis.com/tpu/slice/capacity/committed_chips`) represents the current number of purchased TPU chips in the reservation.

**Label** | **Type** | **Description** | **Values**  
---|---|---|---  
`accelerator_type` | String | The accelerator type and generation. | [`TPU_7X`, `TPU_V6_LITEPOD`, …]  
`reservation_id` | String | The ID of the physical machine reservation. | `<String>`  
`provisioning_model` | String | The associated provisioning model. | [`RESERVED`, `ON-DEMAND`]  
`protection_tier` | String | The associated protection model. | [`STANDARD`, `CAPACITY_OPTIMIZED`, `UNKNOWN`]  
`is_exr` | Bool | Whether the chips are part of an All Capacity mode reservation (extended reservation). | [`TRUE`, `FALSE`]  
`block_id` | String | The ID of the block of the associated slice. | `<String>`  
`subblock_id` | String | The ID of the sub-block of the associated slice. | `<String>`  
  
### Available Chips Count

**Note:** This metric is only available for [All Capacity mode](https://docs.cloud.google.com/tpu/docs/all-capacity-overview) reservations.

The Available Chips Count (`compute.googleapis.com/tpu/slice/capacity/available_chips`) represents the current number of TPU chips in the reservation that are available and ready to use.

**Label** | **Type** | **Description** | **Values**  
---|---|---|---  
`accelerator_type` | String | The accelerator type and generation. | [`TPU_7X`, `TPU_V6_LITEPOD`, ...]  
`reservation_id` | String | The ID of the physical machine reservation. | `<String>`  
`provisioning_model` | String | The associated provisioning model. | [`RESERVED`, `ON-DEMAND`]  
`protection_tier` | String | The associated protection model. | [`STANDARD`, `CAPACITY_OPTIMIZED`, `UNKNOWN`]  
`is_exr` | Bool | Whether the chips are part of an All Capacity mode reservation (extended reservation). | [`TRUE`, `FALSE`]  
`block_id` | String | The ID of the block of the associated slice. | `<String>`  
`subblock_id` | String | The ID of the sub-block of the associated slice. | `<String>`  
  
### Scheduled Chips Count

The Scheduled Chips Count (`compute.googleapis.com/instance/tpu/scheduled_chips`) represents the current number of chips with a `HEALTHY` status allocated to a VM. This metric excludes chips labeled `DISABLED`.

**Label** | **Type** | **Description** | **Values**  
---|---|---|---  
`accelerator_type` | String | The accelerator type and generation. | [`TPU_7X`, `TPU_V6_LITEPOD`, …]  
`reservation_id` | String | The ID of the physical machine reservation. | `<String>`  
`provisioning_model` | String | The associated provisioning model. | [`RESERVED`, `ON-DEMAND`]  
`protection_tier` | String | The associated protection model. | [`STANDARD`, `CAPACITY_OPTIMIZED`, `UNKNOWN`]  
`block_id` | String | The ID of the block within the cluster hosting the VM. | `<String>`  
`subblock_id` | String | The ID of the sub-block hosting the VM. | `<String>`  
`is_exr` | Bool | Whether the chip is part of an All Capacity mode reservation (extended reservation). | [`TRUE`, `FALSE`]  
  
### Active Chips Count

The Active Chips Count (`compute.googleapis.com/instance/tpu/active_chips`) represents the current number of chips that are actively utilized.

**Label** | **Type** | **Description** | **Values**  
---|---|---|---  
`accelerator_type` | String | The accelerator type and generation. | [`TPU_7X`, `TPU_V6_LITEPOD`, …]  
`reservation_id` | String | The ID of the physical machine reservation. | `<String>`  
`provisioning_model` | String | The associated provisioning model. | [`RESERVED`, `ON-DEMAND`]  
`protection_tier` | String | The associated protection model. | [`STANDARD`, `CAPACITY_OPTIMIZED`, `UNKNOWN`]  
`block_id` | String | The ID of the block within the cluster hosting the VM. | `<String>`  
`subblock_id` | String | The ID of the sub-block hosting the VM. | `<String>`  
`is_exr` | Bool | Whether the chip is part of an All Capacity mode reservation (extended reservation). | [`TRUE`, `FALSE`]  
  
## Derived capacity metrics

You can use the fleetwide capacity metrics to derive more advanced metrics to gauge fleetwide usage and efficiency at a given time point. You can use a [PromQL](https://prometheus.io/docs/prometheus/latest/querying/basics/) (Prometheus Query Language) query to define and aggregate these metrics. For example, the following query creates the Average Fleet Activation Efficiency metric:
    
    
    (
      sum(
        avg_over_time(
          {"__name__"="compute.googleapis.com/instance/tpu/active_chips",
          "monitored_resource"="gce_instance"
          }
          [5m]
        )
      )
      /
      sum(
        avg_over_time(
          {"__name__"="compute.googleapis.com/instance/tpu/scheduled_chips",
          "monitored_resource"="gce_instance"
          }
          [5m]
        )
      )
    ) * 100
    
    

The following metrics can provide more granular and detailed insights into the states of your TPU fleet.

### Fleet Availability Rate

The Fleet Availability Rate measures the proportion of _Committed Chips_ that are available and ready for use. The metric represents the usability of the entire reserved fleet.

$$ \text{Fleet Availability Rate} = \frac{\text{Available Chips}}{\text{Committed Chips}} $$ 

### Fleet Scheduling Rate

The Fleet Scheduling Rate measures the proportion of _Committed Chips_ scheduled to a VM. The metric represents how efficiently chips are scheduled.

$$ \text{Fleet Scheduling Rate} = \frac{\text{Scheduled Chips}}{\text{Committed Chips}} $$ 

### Fleet Activation Rate

The Fleet Activation Rate measures the proportion of _Scheduled Chips_ that are active. The metric represents the efficiency of the runtime environment.

$$ \text{Fleet Activation Rate} = \frac{\text{Active Chips}}{\text{Scheduled Chips}} $$ 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
