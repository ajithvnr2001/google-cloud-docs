---
url: https://docs.cloud.google.com/functions/1stgendocs/configuring/memory/
title: Configure memory and vCPU limits (1st gen) \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:38.189816+00:00
---

# Configure memory and vCPU limits (1st gen)  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/configuring/memory/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure memory and vCPU limits (1st gen)

You can provision Cloud Run functions with different amounts of memory to control the limit on how much memory a function can use. The amount of allocated memory you choose corresponds to an amount of allocated CPU for your function. Available memory and CPU tiers are shown in the following table:

Memory | CPU  
---|---  
128MB | .083 vCPU  
256MB | .167 vCPU  
512MB | .333 vCPU  
1024MB | .583 vCPU  
2048MB | 1 vCPU  
4096MB | 2 vCPU  
8192MB | 2 vCPU  
_Not available_ | 4 vCPU  
_Not available_ | 8 vCPU  
**Note:** 1 vCPU is equal to 2.4GHz. CPU allocations are an approximation. Actual allocation of CPU clock cycles may vary slightly across function invocations.

By default, the memory allocated for a function is 256MB or 256 MiB depending on the Cloud Run functions product version.

See [Cloud Run functions Pricing](https://cloud.google.com/functions/pricing) for information about costs associated with memory and CPU allocations.

## Set a memory limit

You can set a function's allocated memory at deployment using the Google Cloud CLI or the Google Cloud console:

###  gcloud 

If you are deploying a function using the gcloud CLI, use the [`--memory`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--memory) flag:
    
    
    gcloud functions deploy YOUR_FUNCTION_NAME --no-gen2 --memory=MEMORY_LIMIT ...
    

###  Console 

To set the allocated memory during function creation in the Google Cloud console:

  1. Go to the [Cloud Run functions Overview page](https://console.cloud.google.com/functions/list) in the Google Cloud console.
  2. Click **Create function**.
  3. Fill in the required fields for your function.
  4. Expand the **Runtime, build...** section at the end of the page and click the **Runtime** tab.
  5. In the **Memory allocated** field, select an amount of memory.
  6. Click **Next**.
  7. Click **Deploy**.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
