---
url: https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/troubleshoot-quota-errors/
title: GPU quota errors \u00a0|\u00a0 Confidential VM \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:38.166577+00:00
---

# GPU quota errors  |  Confidential VM  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/troubleshoot-quota-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Confidential VM ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs)
  * [ Guides ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview)



Send feedback 

#  GPU quota errors Stay organized with collections  Save and categorize content based on your preferences. 

You might encounter the following errors related to [GPU quotas](https://docs.cloud.google.com/compute/resource-usage#gpu_quota) when creating Confidential VM instances with NVIDIA H100 GPUs on the A3 machine series.

## Insufficient regional quota

This error occurs when a request exceeds your available GPU quota in a specific region.

**Example error message:**
    
    
    RESOURCE_NAME Could not fetch resource:
    Quota GPUS_PER_GPU_FAMILY exceeded. Limit: QUOTA_LIMIT in
    region REGION
    

In the Google Cloud console, GPU quota error messages might show a generic quota name, such as `GPUS_PER_GPU_FAMILY`, instead of the specific quota type you need to increase. For Confidential VM instances with GPUs, this quota name refers to the preemptible quota.

To request a regional preemptible NVIDIA H100 GPU quota increase, see [Request preemptible quota](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/create-a-confidential-vm-instance-with-gpu#request-preemptible-quota).

## Insufficient global quota

This error occurs when your total GPU usage across all regions exceeds your global GPU quota.

**Example error message:**
    
    
    RESOURCE_NAME Could not fetch resource:
    Quota GPUS_ALL_REGIONS exceeded. Limit: QUOTA_LIMIT globally
    

To request a global quota increase, see [Request global quota](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/create-a-confidential-vm-instance-with-gpu#request-global-quota).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
