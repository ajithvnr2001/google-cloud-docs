---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/troubleshooting/known-issues/
title: Known issues \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:35:07.301472+00:00
---

# Known issues  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/troubleshooting/known-issues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Known issues Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This page describes known issues that you might run into while running your AI-optimized VMs or clusters. For issues with Compute Engine VMs, see [Compute Engine known issues](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues).

## Issues

The following section lists known issues and workarounds for AI Hypercomputer.

### Workload interruptions on A4 VMs due to firmware issues for NVIDIA B200 GPUs

NVIDIA has identified two firmware issues for B200 GPUs, which A4 VMs use. These issues can cause workload interruptions, such as the `nvidia-smi` command not responding. If you notice workload interruptions on A4 VMs, then confirm that one of the following conditions are true:

  * The VM's uptime (`lastStartTimestamp`) exceeds 65 days.
  * Logs show an [`Xid 149` error message that mentions `0x02a`](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-gpus#xid-149-0x02a).



If one of these conditions is true, then you must reset the GPUs that are attached to your A4 VMs. To prevent future interruptions to your workload due to firmware issues, we recommend that you reset your GPUs at least once every 60 days. For more information, see [Reset GPUs](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-gpus#reset-gpus).

**Note:** If your A4 VMs are part of a GKE cluster, then you can use the [GKE GPU node reset tool](https://github.com/ai-on-gke/tutorials-and-examples/tree/main/gpu-reset-tool) to resolve minor GPU issues, such as unresponsive `nvidia-smi` commands, without rebooting your VMs.

### The metadata server might display old `physicalHost` VM metadata

After experiencing a [host error](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#hosterror) or using the [report faulty host API](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/report-faulty-host) to move a compute instance to a new host, when you [query the metadata server](https://docs.cloud.google.com/compute/docs/metadata/querying-metadata#programmatically-query-metadata), it might display the `physicalHost` metadata of the compute instance's previous host.

To workaround this issue, do one of the following:

  * Use the [`instances.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/get) or the [`gcloud compute instances describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/describe) to retrieve the correct `physicalHost` information.
  * [Stop and then start](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance) your instance. This process updates the `physicalHost` information in the metadata server.
  * Wait 24 hours for the impacted instance's `physicalHost` information to be updated.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
