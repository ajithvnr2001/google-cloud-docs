---
url: https://docs.cloud.google.com/tpu/docs/regions-zones/
title: TPU regions and zones \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:17.224005+00:00
---

# TPU regions and zones  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/regions-zones/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# TPU regions and zones

Google Cloud uses regions, subdivided into zones, to define the geographic location of physical compute resources. For example, the `us-central1` region denotes a region near the geographic center of the United States.

Google Cloud also offers AI zones which are specialized Google Cloud zones for AI/ML training and inference workloads. They provide significant ML accelerator (GPU/TPU) capacity. AI zones are geographically located typically within a 5ms radius from standard Google Cloud zones. For more information see [About AI zones](https://docs.cloud.google.com/compute/docs/regions-zones/ai-zones).

When you create a TPU VM, you specify the zone in which you want to create it. For more information about regional and zonal resources, see Compute Engine [Global, regional, and zonal resources](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources). You can create TPU VMs in the zones shown in the following table.

### North America

**TPU type (TPU7x)** | TPU cores | Supported zones  
---|---|---  
[All TPU7x configurations](https://docs.cloud.google.com/tpu/docs/tpu7x#configurations) | Varies by slice size | 

  * `us-central1-ai1a`
  * `us-central1-c`

  
**TPU type (v6e)** | TPU cores | Supported zones  
---|---|---  
[All v6e configurations](https://docs.cloud.google.com/tpu/docs/v6e#configurations) | Varies by slice size | 

  * `us-central1-b`
  * `us-east1-d`
  * `us-east5-a`
  * `us-east5-b`
  * `us-south1-ai1b`

  
**TPU type (v5p)** | TPU cores | Supported zones  
---|---|---  
[All v5p configurations](https://docs.cloud.google.com/tpu/docs/v5p#configurations) | Varies by slice size | 

  * `us-central1-a`
  * `us-east5-a`

  
**TPU type (v5e)** | TPU cores | Supported zones  
---|---|---  
[All v5e configurations](https://docs.cloud.google.com/tpu/docs/v5e#configurations) | Varies by slice size | 

  * `us-central1-a`
  * `us-south1-a`
  * `us-west1-c`
  * `us-west4-a`

  
**TPU type (v4)** | TPU cores | Supported zones  
---|---|---  
[All v4 configurations](https://docs.cloud.google.com/tpu/docs/v4#configurations) | Varies by slice size | 

  * `us-central2-b`

  
**TPU type (v3)** | TPU cores | Supported zones  
---|---|---  
v3-8  | 8 | 

  * `us-central1-a`
  * `us-central1-b`

  
**TPU type (v2)** | TPU cores | Supported zones  
---|---|---  
v2-8  | 8 | 

  * `us-central1-b`
  * `us-central1-c`

  
v2-32  | 32 | 

  * `us-central1-a`

  
v2-128  | 128 | 

  * `us-central1-a`

  
v2-256  | 256 | 

  * `us-central1-a`

  
v2-512  | 512 | 

  * `us-central1-a`

  
  
### Europe

**TPU type (v6e)** | TPU cores | Supported zones  
---|---|---  
[All v6e configurations](https://docs.cloud.google.com/tpu/docs/v6e#configurations) | Varies by slice size | 

  * `europe-west4-a`

  
**TPU type (v5p)** | TPU cores | Supported zones  
---|---|---  
[All v5p configurations](https://docs.cloud.google.com/tpu/docs/v5p#configurations) | Varies by slice size | 

  * `europe-west4-b`

  
**TPU type (v5e)** | TPU cores | Supported zones  
---|---|---  
[All v5e configurations](https://docs.cloud.google.com/tpu/docs/v5e#configurations) | Varies by slice size | 

  * `europe-west4-b`

  
**TPU type (v3)** | TPU cores | Supported zones  
---|---|---  
v3-8  | 8 | 

  * `europe-west4-a`

  
v3-32  | 32 | 

  * `europe-west4-a`

  
v3-64  | 64 | 

  * `europe-west4-a`

  
v3-128  | 128 | 

  * `europe-west4-a`

  
v3-256  | 256 | 

  * `europe-west4-a`

  
v3-512  | 512 | 

  * `europe-west4-a`

  
v3-1024  | 1024 | 

  * `europe-west4-a`

  
v3-2048  | 2048 | 

  * `europe-west4-a`

  
**TPU type (v2)** | TPU cores | Supported zones  
---|---|---  
v2-8  | 8 | 

  * `europe-west4-a`

  
v2-32  | 32 | 

  * `europe-west4-a`

  
v2-128  | 128 | 

  * `europe-west4-a`

  
v2-256  | 256 | 

  * `europe-west4-a`

  
v2-512  | 512 | 

  * `europe-west4-a`

  
  
### Asia Pacific

**TPU type (v6e)** | TPU cores | Supported zones  
---|---|---  
[All v6e configurations](https://docs.cloud.google.com/tpu/docs/v6e#configurations) | Varies by slice size | 

  * `asia-northeast1-b`

  
**TPU type (v2)** | TPU cores | Supported zones  
---|---|---  
v2-8  | 8 | 

  * `asia-east1-c`

  
  
### South America

**TPU type (v6e)** | TPU cores | Supported zones  
---|---|---  
[All v6e configurations](https://docs.cloud.google.com/tpu/docs/v6e#configurations) | Varies by slice size | 

  * `southamerica-west1-a`

  
  
TPU types with higher numbers of chips or cores are available only in limited quantities. TPU types with lower chip or core counts are more likely to be available.

**Note:** The [Cloud TPU pricing](https://cloud.google.com/tpu/pricing) page might display pricing for regions where public TPU zones aren't generally available. Use the tables on this page to verify which regions and zones currently support each TPU version.

## What's next

  * To see pricing for TPUs in each region, see [Cloud TPU pricing](https://cloud.google.com/tpu/pricing).

  * To learn how to work with TPUs, see [Get started](https://docs.cloud.google.com/tpu/docs/quick-starts).

  * To learn about TPU architecture, see [TPU Architecture](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm).

  * To learn about the types of models that are well-suited to Cloud TPU, see [When to use TPUs](https://docs.cloud.google.com/tpu/docs/tpus#when_to_use_tpus).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
