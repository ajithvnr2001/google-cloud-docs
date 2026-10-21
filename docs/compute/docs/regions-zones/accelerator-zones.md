---
url: https://docs.cloud.google.com/compute/docs/regions-zones/accelerator-zones/
title: GPU locations \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:58:31.559363+00:00
---

# GPU locations  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/regions-zones/accelerator-zones/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  GPU locations Stay organized with collections  Save and categorize content based on your preferences. 

Accelerators, such as Graphics Processing Units (GPUs), are specialized hardware components that can significantly speed up machine learning and high performance computing workloads. When you create Compute Engine (VM) instances or other resources on Google Cloud, you can attach accelerators to them. For an overview of GPUs, see the [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus) documentation.

The availability of specific GPU models varies by region and zone. This document provides a comprehensive list of accelerator availability to help you plan your deployments and select the appropriate locations for your resources.

This document focuses on accelerator availability for Compute Engine, [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning), and [AI Hypercomputer](https://docs.cloud.google.com/ai-hypercomputer/docs/overview). If you use GPUs with other Google Cloud services, accelerator availability might differ. For those services, see the following documentation:

  * [Vertex AI: accelerator locations](https://docs.cloud.google.com/vertex-ai/docs/general/locations#accelerators)
  * [Cloud Run: regions that support GPUs](https://docs.cloud.google.com/run/docs/configuring/services/gpu#supported-regions)
  * [Confidential Computing: zones that support GPUs](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#supported-zones)



## Zones that support GPUs

Google Cloud offers GPU resources in multiple locations worldwide. These locations consist of the standard regions and zones, which you can read about on the [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones) page. Each zone offers a variety of GPU versions. When you create resources that use accelerators—such as Compute Engine instances or GKE node pools—you must select a zone where that accelerator type is available.

### AI zones

**Important:** When AI zone visibility is turned off, your Google Cloud project's access to AI zones is restricted. To view and access AI zones, [turn on AI zone visibility](https://docs.cloud.google.com/compute/docs/regions-zones/manage-ai-zones#turn_on_ai_zones).

In addition to standard zones, GPUs are available in AI zones. These Google Cloud locations are specifically designed to house resources for large-scale AI and machine learning workloads. AI zones offer access to GPU machine types, and might also offer other non-accelerator machine types to support the primary AI and machine learning workloads that run on the accelerators. To learn more about these specialized zones, see [About AI zones](https://docs.cloud.google.com/compute/docs/regions-zones/ai-zones). To view accelerator availability by zone type, use the **Select a zone type** filter.

## GPU availability

**Caution:** NVIDIA T4 and P4 GPUs reach end of support on August 1, 2027. For more information, see [NVIDIA T4 end of support](https://docs.cloud.google.com/compute/docs/eol/t4-eos) and [NVIDIA P4 end of support](https://docs.cloud.google.com/compute/docs/eol/p4-eos). 

The following sortable table lets you select different options to see where GPU resources are available. You can search by location, GPU machine type, or a combination of these. In the **Select a GPU machine type** list, the machine types that have NVIDIA GPUs automatically attached show the GPU type in brackets.

**Note:** Some GPU machine types have limited availability. For more information, see Limited availability regions and zones. APACNorth AmericaSouth AmericaEuropeMiddle EastAfricaAI zoneStandardA4X Max (NVIDIA GB300 Ultra Superchips)A4X (NVIDIA GB200 Superchips)A4 (NVIDIA B200)A3 Ultra (NVIDIA H200)A3 Mega (NVIDIA H100)A3 High (NVIDIA H100)A3 Edge (NVIDIA H100)A2 Ultra (NVIDIA A100 80GB)A2 Standard (NVIDIA A100 40GB)G4 (NVIDIA RTX PRO 6000)G4 (Fractional GPU) (NVIDIA RTX PRO 6000)G2 (NVIDIA L4)N1 with NVIDIA T4N1 with NVIDIA V100N1 with NVIDIA P4Clear all

Zone | Location | Zone type | GPU machine type  
---|---|---|---  
`asia-east1-a` |  Changhua County, Taiwan, APAC  |  Standard |  • G4  
• G2  
• N1+T4  
  
`asia-east1-b` |  Changhua County, Taiwan, APAC  |  Standard |  • G2  
  
`asia-east1-c` |  Changhua County, Taiwan, APAC  |  Standard |  • A3 High  
• G2  
• N1+T4  
• N1+V100  
  
`asia-east2-a` |  Hong Kong, APAC  |  Standard |  • N1+T4  
  
`asia-east2-c` |  Hong Kong, APAC  |  Standard |  • N1+T4  
  
`asia-northeast1-a` |  Tokyo, Japan, APAC  |  Standard |  • A2 Standard  
• G2  
• N1+T4  
  
`asia-northeast1-b` |  Tokyo, Japan, APAC  |  Standard |  • A4   
• A3 Mega  
• G4  
• G2  
  
`asia-northeast1-c` |  Tokyo, Japan, APAC  |  Standard |  • A2 Standard  
• G2  
• N1+T4  
  
`asia-northeast3-a` |  Seoul, South Korea, APAC  |  Standard |  • G2  
  
`asia-northeast3-b` |  Seoul, South Korea, APAC  |  Standard |  • A2 Standard  
• G2  
• N1+T4  
  
`asia-northeast3-c` |  Seoul, South Korea, APAC  |  Standard |  • A3 High  
• A3 Edge  
• N1+T4  
  
`asia-south1-a` |  Mumbai, India, APAC  |  Standard |  • G2  
• N1+T4  
  
`asia-south1-b` |  Mumbai, India, APAC  |  Standard |  • A3 Ultra  
• G2  
• N1+T4  
  
`asia-south1-c` |  Mumbai, India, APAC  |  Standard |  • A3 Edge  
• G4  
• G2  
  
`asia-south2-a` |  Delhi, India, APAC  |  Standard |  • G4  
  
`asia-south2-c` |  Delhi, India, APAC  |  Standard |  • A3 Ultra  
• G4  
  
`asia-southeast1-a` |  Jurong West, Singapore, APAC  |  Standard |  • A2 Standard  
• G4  
• G2  
• N1+T4  
• N1+P4  
  
`asia-southeast1-b` |  Jurong West, Singapore, APAC  |  Standard |  • A4   
• A3 Mega  
• A3 High  
• G4  
• G2  
• N1+T4  
• N1+P4  
  
`asia-southeast1-c` |  Jurong West, Singapore, APAC  |  Standard |  • A3 Mega  
• A3 High  
• A2 Ultra  
• A2 Standard  
• G2  
• N1+T4  
  
`asia-southeast2-a` |  Jakarta, Indonesia, APAC  |  Standard |  • N1+T4  
  
`asia-southeast2-b` |  Jakarta, Indonesia, APAC  |  Standard |  • G4  
• N1+T4  
  
`asia-southeast2-c` |  Jakarta, Indonesia, APAC  |  Standard |  • G4  
  
`australia-southeast1-a` |  Sydney, Australia, APAC  |  Standard |  • N1+T4  
• N1+P4  
  
`australia-southeast1-b` |  Sydney, Australia, APAC  |  Standard |  • N1+P4  
  
`australia-southeast1-c` |  Sydney, Australia, APAC  |  Standard |  • A3 Mega  
• N1+T4  
  
`australia-southeast2-b` |  Melbourne, Australia, APAC  |  Standard |  • A3 High  
  
`europe-central2-b` |  Warsaw, Poland, Europe  |  Standard |  • N1+T4  
  
`europe-central2-c` |  Warsaw, Poland, Europe  |  Standard |  • N1+T4  
  
`europe-north1-a` |  Hamina, Finland, Europe  |  Standard |  • G4  
  
`europe-north1-b` |  Hamina, Finland, Europe  |  Standard |  • G4  
  
`europe-north1-c` |  Hamina, Finland, Europe  |  Standard |  • A4   
• G4  
  
`europe-west1-b` |  St. Ghislain, Belgium, Europe  |  Standard |  • A4   
• A3 Ultra  
• A3 Mega  
• G4  
• G2  
• N1+T4  
  
`europe-west1-c` |  St. Ghislain, Belgium, Europe  |  Standard |  • A3 Mega  
• A3 High  
• G4  
• G2  
• N1+T4  
  
`europe-west1-d` |  St. Ghislain, Belgium, Europe  |  Standard |  • N1+T4  
  
`europe-west10-b` |  Berlin, Germany, Europe  |  Standard |  • G4  
  
`europe-west2-a` |  London, England, Europe  |  Standard |  • G2  
• N1+T4  
  
`europe-west2-b` |  London, England, Europe  |  Standard |  • G4  
• G2  
• N1+T4  
  
`europe-west2-c` |  London, England, Europe  |  Standard |  • G4  
  
`europe-west3-a` |  Frankfurt, Germany, Europe  |  Standard |  • G2  
  
`europe-west3-b` |  Frankfurt, Germany, Europe  |  Standard |  • G2  
• N1+T4  
  
`europe-west3-c` |  Frankfurt, Germany, Europe  |  Standard |  • A3 High  
  
`europe-west4-a` |  Eemshaven, Netherlands, Europe  |  Standard |  • A3 Ultra  
• A2 Ultra  
• A2 Standard  
• G4  
• G2  
• N1+T4  
• N1+V100  
  
`europe-west4-ai1a` |  De Kooy, Netherlands, Europe  |  AI zone |  • G4  
  
`europe-west4-b` |  Eemshaven, Netherlands, Europe  |  Standard |  • A4X   
• A4   
• A3 Mega  
• A3 High  
• A2 Standard  
• G4  
• G2  
• N1+T4  
• N1+P4  
• N1+V100  
  
`europe-west4-c` |  Eemshaven, Netherlands, Europe  |  Standard |  • A3 Mega  
• A3 High  
• G4  
• G2  
• N1+T4  
• N1+P4  
• N1+V100  
  
`europe-west6-b` |  Zurich, Switzerland, Europe  |  Standard |  • G2  
  
`europe-west6-c` |  Zurich, Switzerland, Europe  |  Standard |  • G2  
  
`europe-west8-b` |  Milan, Italy, Europe  |  Standard |  • G4  
  
`europe-west8-c` |  Milan, Italy, Europe  |  Standard |  • G4  
  
`europe-west9-c` |  Paris, France, Europe  |  Standard |  • A3 High  
  
`me-central2-a` |  Dammam, Saudi Arabia, Middle East  |  Standard |  • G4  
• G2  
  
`me-central2-c` |  Dammam, Saudi Arabia, Middle East  |  Standard |  • G2  
  
`me-west1-a` |  Tel Aviv, Israel, Middle East  |  Standard |  • A2 Standard  
  
`me-west1-b` |  Tel Aviv, Israel, Middle East  |  Standard |  • N1+T4  
  
`me-west1-c` |  Tel Aviv, Israel, Middle East  |  Standard |  • A2 Standard  
• N1+T4  
  
`northamerica-northeast1-b` |  Montréal, Québec, North America  |  Standard |  • G2  
• N1+P4  
  
`northamerica-northeast1-c` |  Montréal, Québec, North America  |  Standard |  • G2  
• N1+T4  
• N1+P4  
  
`northamerica-northeast2-a` |  Toronto, Ontario, North America  |  Standard |  • G2  
  
`northamerica-northeast2-b` |  Toronto, Ontario, North America  |  Standard |  • G2  
  
`northamerica-northeast2-c` |  Toronto, Ontario, North America  |  Standard |  • A3 Edge  
  
`southamerica-east1-a` |  Osasco, São Paulo, Brazil, South America  |  Standard |  • G4  
• N1+T4  
  
`southamerica-east1-b` |  Osasco, São Paulo, Brazil, South America  |  Standard |  • G4  
• N1+T4  
  
`southamerica-east1-c` |  Osasco, São Paulo, Brazil, South America  |  Standard |  • N1+T4  
  
`us-central1-a` |  Council Bluffs, Iowa, North America  |  Standard |  • A4X   
• A3 Mega  
• A3 High  
• A2 Ultra  
• A2 Standard  
• G2  
• N1+T4  
• N1+P4  
• N1+V100  
  
`us-central1-b` |  Council Bluffs, Iowa, North America  |  Standard |  • A4X Max  
• A4X   
• A4   
• A3 Ultra  
• A3 Mega  
• A3 High  
• A2 Standard  
• G4  
• G4 (Fractional GPU)  
• G2  
• N1+T4  
• N1+V100  
  
`us-central1-c` |  Council Bluffs, Iowa, North America  |  Standard |  • A3 Mega  
• A3 High  
• A2 Ultra  
• A2 Standard  
• G4  
• G2  
• N1+T4  
• N1+P4  
• N1+V100  
  
`us-central1-f` |  Council Bluffs, Iowa, North America  |  Standard |  • A2 Standard  
• G4  
• N1+T4  
• N1+V100  
  
`us-east1-b` |  Moncks Corner, South Carolina, North America  |  Standard |  • A4   
• A2 Standard  
• G4  
• G2  
• N1+T4  
• N1+V100  
  
`us-east1-c` |  Moncks Corner, South Carolina, North America  |  Standard |  • G2  
• N1+T4  
  
`us-east1-d` |  Moncks Corner, South Carolina, North America  |  Standard |  • A4X   
• A4   
• G4  
  
`us-east4-a` |  Ashburn, Virginia, North America  |  Standard |  • A4X Max  
• A3 Mega  
• A3 High  
• G2  
• N1+T4  
• N1+P4  
  
`us-east4-b` |  Ashburn, Virginia, North America  |  Standard |  • A4X Max  
• A4X   
• A4   
• A3 Ultra  
• A3 Mega  
• A3 High  
• G4  
• N1+T4  
• N1+P4  
  
`us-east4-c` |  Ashburn, Virginia, North America  |  Standard |  • A3 High  
• A2 Ultra  
• G4  
• G2  
• N1+T4  
• N1+P4  
  
`us-east5-a` |  Columbus, Ohio, North America  |  Standard |  • A3 Mega  
• A3 High  
• A2 Ultra  
• G4  
  
`us-east5-b` |  Columbus, Ohio, North America  |  Standard |  • A4X Max  
• G4  
  
`us-east5-c` |  Columbus, Ohio, North America  |  Standard |  • A4X Max  
• G4  
  
`us-south1-a` |  Dallas, Texas, North America  |  Standard |  • G4  
  
`us-south1-b` |  Dallas, Texas, North America  |  Standard |  • A4   
• A3 Ultra  
• G4  
  
`us-west1-a` |  The Dalles, Oregon, North America  |  Standard |  • A3 Mega  
• A3 High  
• G4  
• G2  
• N1+T4  
• N1+V100  
  
`us-west1-b` |  The Dalles, Oregon, North America  |  Standard |  • A3 Mega  
• A3 High  
• A2 Standard  
• G4  
• G2  
• N1+T4  
• N1+V100  
  
`us-west1-c` |  The Dalles, Oregon, North America  |  Standard |  • A3 Ultra  
• G4  
  
`us-west2-b` |  Los Angeles, California, North America  |  Standard |  • N1+T4  
• N1+P4  
  
`us-west2-c` |  Los Angeles, California, North America  |  Standard |  • A4   
• N1+T4  
• N1+P4  
  
`us-west3-a` |  Salt Lake City, Utah, North America  |  Standard |  • G4  
  
`us-west3-b` |  Salt Lake City, Utah, North America  |  Standard |  • A4   
• A2 Standard  
• N1+T4  
  
`us-west3-c` |  Salt Lake City, Utah, North America  |  Standard |  • A4   
  
`us-west4-a` |  Las Vegas, Nevada, North America  |  Standard |  • A3 Mega  
• A3 High  
• G4  
• G2  
• N1+T4  
  
`us-west4-b` |  Las Vegas, Nevada, North America  |  Standard |  • A2 Standard  
• G4  
• N1+T4  
  
`us-west4-c` |  Las Vegas, Nevada, North America  |  Standard |  • G4  
• G2  
  
  
### Limited availability regions and zones

**Important:** This section lists GPU machine types that are restricted, meaning they either require account team approval due to limited capacity, or are available only in specific zones. Review this section before choosing a region or GPU machine type to avoid procurement delays.

  * For A3 Mega (NVIDIA H100) machine types, the following regions and zones are available with limited capacity. To access these regions and zones, contact your account team.

    * Sydney, Australia, APAC: `australia-southeast1-c`
    * St. Ghislain, Belgium, Europe: `europe-west1-b,c`
    * Council Bluffs, Iowa, North America: `us-central1-b`
  * For A3 High (NVIDIA H100) machine types, the following regions and zones are available with limited capacity. To access these regions and zones, contact your account team.

    * St. Ghislain, Belgium, Europe: `europe-west1-b`
  * For A2 Standard (NVIDIA A100 40GB) machine types, the `a2-megagpu-16g` machine is only available in the following regions and zones:

    * Iowa, North America: `us-central1-a,b,c,f`
    * Netherlands, Europe: `europe-west4-a,b`
    * Singapore, APAC: `asia-southeast1-c`
  * For G4 (NVIDIA RTX PRO 6000) machine types, the machine types that have less than one GPU attached, such as `g4-standard-6`, `g4-standard-12`, and `g4-standard-24`, are only available in Iowa, North America: `us-central1-b`. For more information about G4 machine types that have fractional GPUs (vGPUs) attached, see [G4 machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g4-series).




## Feature availability by region and zone

In addition to the availability of specific accelerator models, some related features and configurations have their own regional or zonal restrictions. The following sections outline the availability for these specific features.

### Future reservations in calendar mode and Flex-start VMs

For GPUs, future reservations in calendar mode and Flex-start VMs are available in all zones where the GPU machine types are available.

### NVIDIA RTX Virtual Workstations

[NVIDIA RTX Virtual Workstations (vWS)](https://www.nvidia.com/en-us/design-visualization/virtual-workstation/) are supported on the following machine series.

  * **G4** : you can enable NVIDIA RTX PRO 6000 vWS on these machine types.
  * **G2** : you can enable NVIDIA L4 vWS on these machine types.
  * **N1** : you can enable NVIDIA T4 or V100 vWS GPUs on these machine types.



For these machine types, vWS is supported in any zone where the machine type is available.

### Local SSD

For all GPU machine types, Local SSD disks are available in the same zones as the machine type with the following exceptions:

  * N1+V100: Local SSD disks aren't available in the `us-east1-c` zone.
  * N1+P4: Local SSD disks are only supported in zones `us-central1-c` and `northamerica-northeast1-b`.



## What's next?

  * Learn more about [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus).
  * Learn more about [geography and regions](https://docs.cloud.google.com/docs/geography-and-regions).
  * Learn about [GPU pricing](https://docs.cloud.google.com/compute/gpus-pricing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
