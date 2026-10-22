---
url: https://docs.cloud.google.com/compute/docs/regions-zones/tpu-regions-zones/
title: TPU locations \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:22:23.918355+00:00
---

# TPU locations  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/regions-zones/tpu-regions-zones/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  TPU locations Stay organized with collections  Save and categorize content based on your preferences. 

Accelerators, such as Tensor Processing Units (TPUs), are specialized hardware components that can significantly speed up machine learning and high performance computing workloads. When you create Compute Engine instances or other resources on Google Cloud, you can attach accelerators to them. For an overview of these accelerators, see [TPU machines](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines).

The availability of specific TPU models varies by region and zone. This document provides a comprehensive list of accelerator availability to help you plan your deployments and select the appropriate locations for your resources.

The table in this document focuses on TPU availability for Compute Engine. If you use TPUs with other Google Cloud services, accelerator availability might differ. For those services, see the following documentation:

  * [Google Kubernetes Engine (GKE): Validate TPU availability in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#availability)
  * [Vertex AI: accelerator locations](https://docs.cloud.google.com/vertex-ai/docs/general/locations#accelerators)



## Zones that support TPUs

Google Cloud offers TPU resources in multiple locations worldwide. These locations consist of the standard regions and zones, which you can read about on the [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones) page. Each zone offers a variety of TPU versions. When you create resources that use accelerators—such as Compute Engine instances or GKE node pools—you must select a zone where that accelerator type is available. Compute Engine supports TPU7x, TPU v6e, and TPU v5p.

### AI zones

**Important:** When AI zone visibility is turned off, your Google Cloud project's access to AI zones is restricted. To view and access AI zones, [turn on AI zone visibility](https://docs.cloud.google.com/compute/docs/regions-zones/manage-ai-zones#turn_on_ai_zones).

In addition to standard zones, TPUs are available in AI zones. These Google Cloud locations are specifically designed to house resources for large-scale AI and machine learning workloads. AI zones offer access to TPUs, and might also offer other non-accelerator machine types to support the primary AI and machine learning workloads that run on the accelerators. To learn more about these specialized zones, see [About AI zones](https://docs.cloud.google.com/compute/docs/regions-zones/ai-zones). To view accelerator availability by zone type, use the **Select a zone type** filter.

## TPU availability

The following sortable table lets you select different options to see where TPU resources are available on Compute Engine. You can search by location, or TPU version. Note that Compute Engine supports TPU7x, TPU v6e, and TPU v5p.

APACNorth AmericaSouth AmericaEuropeMiddle EastAfricaAI zoneStandardTPU7x (Ironwood)TPU v6e (Trillium)TPU v5pClear all

Zone | Location | Zone type | TPU version  
---|---|---|---  
`asia-northeast1-b` |  Tokyo, Japan, APAC  |  Standard |  • v6e (Trillium)  
  
`europe-west4-a` |  Eemshaven, Netherlands, Europe  |  Standard |  • v6e (Trillium)  
  
`europe-west4-b` |  Eemshaven, Netherlands, Europe  |  Standard |  • v5p  
  
`southamerica-west1-a` |  Santiago, Chile, South America  |  Standard |  • v6e (Trillium)  
  
`us-central1-a` |  Council Bluffs, Iowa, North America  |  Standard |  • v5p  
  
`us-central1-ai1a` |  Lincoln, Nebraska, North America  |  AI zone |  • TPU7x (Ironwood)  
  
`us-central1-b` |  Council Bluffs, Iowa, North America  |  Standard |  • v6e (Trillium)  
  
`us-central1-c` |  Council Bluffs, Iowa, North America  |  Standard |  • TPU7x (Ironwood)  
  
`us-east1-d` |  Moncks Corner, South Carolina, North America  |  Standard |  • v6e (Trillium)  
  
`us-east5-a` |  Columbus, Ohio, North America  |  Standard |  • v6e (Trillium)  
• v5p  
  
`us-east5-b` |  Columbus, Ohio, North America  |  Standard |  • v6e (Trillium)  
  
`us-south1-ai1b` |  Austin, Texas, North America  |  AI zone |  • v6e (Trillium)  
  
  
## What's next?

  * [Learn more about geography and regions](https://docs.cloud.google.com/docs/geography-and-regions).
  * [Learn about TPU pricing](https://docs.cloud.google.com/tpu/pricing).
  * [Learn about TPU resources in Compute Engine](https://docs.cloud.google.com/compute/docs/tpus/tpu-resources-in-compute-engine).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
