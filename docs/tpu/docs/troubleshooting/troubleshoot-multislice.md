---
url: https://docs.cloud.google.com/tpu/docs/troubleshooting/troubleshoot-multislice/
title: Profiling Multislice environments \u00a0|\u00a0 Cloud TPU \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:59.936317+00:00
---

# Profiling Multislice environments  |  Cloud TPU  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/troubleshooting/troubleshoot-multislice/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Profiling Multislice environments

**Caution:** This page applies to the Cloud TPU API, which is no longer under active development. The Cloud TPU API will receive bug fixes and security updates only. We recommend using Google Kubernetes Engine for Multislice. For more information, see [Deploy TPU Multislices in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpu-multislice).

Cloud TPU Multislice environments are composed of multiple TPU slices that communicate over the Data Center Network (DCN). You can use the Megascale stats tool in XProf to view information about how effectively your Multislice environment is utilizing the DCN network. Specifically, the Megascale Stats tool lets you:

  * View and understand inter-slice network performance based on collected data
  * Identify performance bottlenecks
  * Optimize your model's performance



All metrics in the Megascale stats tool are generated on a per-TPU basis. To enable this tool, follow the same steps to capture profile in your framework and use the XProfiler library to set up a TensorBoard XProf instance for viewing your profiles. As long as your workload was run as a multislice workload, TensorBoard will display the "Megascale stats" tool for any multislice workload.

For more details on Megascale stats tool in XProf, check out [Megascale Stats Tool](https://openxla.org/xprof/megascale_stats) guide.

## Terminology

The DCN collective stats tool displays metrics that describe communication that occurs between TPU slices within a Multislice environment. When the TPU runtime initiates inter-slice communication, a series of operations are used:

  * `send`: Interrupts the host to start Direct Memory Access (DMA) and provides a filled buffer to the host to start the data transfer.
  * `send-done`: Signals the host that the data transfer is completed.
  * `recv`: Provides an empty buffer for the host to fill with the transferred data.
  * `recv-done`: Signals the host that the data has been received.

**Note:** The actual sending of data occurs after the `send` operation is completed. The `send-done` operation occurs after the data has been sent. Likewise, data is received after the `recv` operation is completed. The `recv-done` operation occurs after the data has been received.

A collective is initiated when a `send` operation occurs and is completed when the matching `recv-done` operation occurs.

## Slack Time

A measure of time the collective is able to send and receive data. This does not include the `send`, `send-done`, `recv` or `recv-done` operations. For example, given the following timeline:

![v5e Pod chip](https://docs.cloud.google.com/static/tpu/docs/images/com-timeline.png)

Slack time is calculated in this example as:

**Slack time = t 1 \+ t2 \+ t3**

Increasing slack time reduces the chances to stall the TPU for a collective. You can increase the slack time by choosing a different sharding method.

## Stall duration

The average duration of time the collective spends in the send, send-done, recv, and recv-done operations. Note, this does not include time spent transmitting data. For example, given the following timeline:

![v5e Pod chip](https://docs.cloud.google.com/static/tpu/docs/images/com-timeline.png)

Stall duration is calculated in this example as:

**Stall duration = t send \+ tsend-done \+ trecv \+ trecv-done**

## Observed duration

The amount of time between the `send` and `recv-done` operations, including the time sending and receiving data. For example, given the following timeline:

![v5e Pod chip](https://docs.cloud.google.com/static/tpu/docs/images/com-timeline.png)

Observed duration is calculated as:

**Observed duration = t send \+ t1 \+ tsend-done \+ t2 \+ trecv \+ t3 \+ trecv-done**

## Occurrences

The number of times a collective is initiated and completed during a profile duration. A collective is initiated when a `send` operation occurs and is completed when the matching `recv-end` operation occurs. The `send` operation and its matching `recv-done` operation must occur within a profile duration to be included in this metric.

## Aggregated total stall

The total amount of time a collective stalls a TPU during a profile duration. Aggregation total stall is calculated as:

**Aggregated total stall = stall duration * occurrences**

## Data transmitted size

The amount of data transmitted over the network for the collective during the profile duration.

## Required bandwidth

The bandwidth required to transmit data within the provided slack. You can use this metric to see the number of collectives competing for network bandwidth during the profile duration. Required bandwidth is computed as:

**Required bandwidth = data transmitted size / slack time**

## Tool status

The following table shows the version of TensorFlow or TPU runtime version required for each metric displayed in the DCN Collective Stats tool.

DCN Collective Stats | Supported TensorFlow of TPU runtime version  
---|---  
Slack time | TensorFlow 2.15.0, tensorboard 2.15.1 and tensorboard-plugin-profile 2.15.0  
Stall duration | TensorFlow 2.15.0, tensorboard 2.15.1 and tensorboard-plugin-profile 2.15.0  
Observed duration | TensorFlow 2.15.0, tensorboard 2.15.1 and tensorboard-plugin-profile 2.15.0  
Occurrences | TensorFlow 2.15.0, tensorboard 2.15.1 and tensorboard-plugin-profile 2.15.0  
Aggregated total stall | tf-nightly, tb-nightly, tbp-nightly  
Data transmitted size | tf-nightly, tb-nightly, tbp-nightly  
Required bandwidth | tf-nightly, tb-nightly, tbp-nightly  
  
## How to Analyze DCN Collective Stats tool

  1. Run TensorBoard server and go to **Profile** tab.

  2. Sort the table in DCN collective stats tool by **Aggregated Total Stall** in descending order.

  3. Identify the DCN collective name that has the highest **Aggregated Total Stall**. If the aggregated stall duration of this collective is significantly high compared to others, this could indicate that there is a bottleneck in the DCN collective.

  4. Multiply the required bandwidth of the DCN collective by the number of cores. There are 8 cores per v4 TPU host, so the required bandwidth for a collective is 8 x the value displayed. If the required bandwidth is greater than the maximum network bandwidth of the TPU, this may mean the network is congested. To bring down the required bandwidth, try changing the sharding mechanism you use. For more information about sharding mechanisms, see [Cloud TPU Multislice overview](https://docs.cloud.google.com/tpu/docs/multislice-introduction#optimize).

  5. Generate an HLO dump to determine if there are any compiler issues. It is better to fan out `send` and `recv-done` operations for a collective to allow scheduling of more overlapping HLO Ops. Overlapping more HLO operations reduces TPU stall time.

  6. Check the duration of `recv-done` operations in the Trace Viewer for the DCN collective that has the maximum aggregated total stall. If the duration of the transfer is high, there could be a bandwidth bottleneck because `recv-done` operations are usually blocked on the network to get the data.

  7. If the duration of `recv-done` operations is not too high compared to the slack time, this could indicate a hardware issue.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
