---
url: https://docs.cloud.google.com/colab/docs/quotas/
title: Quotas and limits \u00a0|\u00a0 Colab Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:27.378972+00:00
---

# Quotas and limits  |  Colab Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/colab/docs/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Colab Enterprise ](https://docs.cloud.google.com/colab/docs)
  * [ Resources ](https://docs.cloud.google.com/colab/docs/release-notes)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Quotas and limits

This document lists the quotas and system limits that apply to Colab Enterprise.

  * _Quotas_ have default values, but you can typically request adjustments.
  * _System limits_ are fixed values that can't be changed.



Google Cloud uses quotas to help ensure fairness and reduce spikes in resource use and availability. A quota restricts how much of a Google Cloud resource your Google Cloud project can use. Quotas apply to a range of resource types, including hardware, software, and network components. For example, quotas can restrict the number of API calls to a service, the number of load balancers used concurrently by your project, or the number of projects that you can create. Quotas protect the community of Google Cloud users by preventing the overloading of services. Quotas also help you to manage your own Google Cloud resources.

The Cloud Quotas system does the following:

  * Monitors your consumption of Google Cloud products and services
  * Restricts your consumption of those resources
  * Provides a way to [request changes to the quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) and [automate quota adjustments](https://docs.cloud.google.com/docs/quotas/quota-adjuster)



In most cases, when you attempt to consume more of a resource than its quota allows, the system blocks access to the resource, and the task that you're trying to perform fails.

Quotas generally apply at the Google Cloud project level. Your use of a resource in one project doesn't affect your available quota in another project. Within a Google Cloud project, quotas are shared across all applications and IP addresses. 

For more information, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview). 

There are also _system limits_ on Colab Enterprise resources. System limits can't be changed. 

## Compute Engine quotas

Colab Enterprise runtimes use Compute Engine quotas, including quotas for virtual machine (VM) instances, disks, CPUs, and GPUs. For more information, see the Compute Engine [Allocation quotas page](https://docs.cloud.google.com/compute/resource-usage).

**Note:** To use GPUs, in addition to the specific GPU models and regions you intend to use, you also need sufficient global quota for `GPUs (all regions)` (API quota name: `GPU_ALL_REGIONS`). This global quota covers the total number of all GPUs of all types used by your project across all regions. If you exceed this global limit, you won't be able to start new GPU runtimes, even if you have available quota for a specific GPU type in a particular region. See [GPU quota](https://docs.cloud.google.com/compute/resource-usage#gpu_quota).

## Agent Platform request quotas

Colab Enterprise runtime and runtime template requests count toward Gemini Enterprise Agent Platform quotas. The relevant Agent Platform quotas include the following:

Agent Platform quota | Colab Enterprise interaction | Limit  
---|---|---  
Resource management requests | Runtime and runtime template requests | 600/minute  
Job or long-running operation requests per minute | Runtime and runtime template requests | 60/minute  
  
## Dataform request quotas

Colab Enterprise notebooks are stored in Dataform. When you create or interact with a notebook, Colab Enterprise sends an API request to Dataform. Dataform has the following relevant API quotas:

Dataform quota | Colab Enterprise interaction | Limit  
---|---|---  
Total requests per project | Notebook (IPYNB file) operations | 6,000/minute  
  
Other Dataform quotas such as package installation requests per project or workflow actions per execution don't apply to Colab Enterprise.

### Notebook operations

Notebook (IPYNB file) operations count toward the Dataform quota for total requests per project. For example, notebook file operations include the following:

  * Creating, saving, and renaming a notebook.
  * Opening, downloading, and importing a notebook.
  * Viewing each version of a notebook's revision history and reinstating a previous version.

**Note:** Colab Enterprise regularly saves your notebook automatically when you make changes. Each of these automatic saves counts toward the Dataform quota.

## Usage limits

Colab Enterprise enforces the following usage limits:

Usage limit | Value  
---|---  
File size per imported notebook |  Approximately 20 MB Working with a notebook that is near the size limit can impact performance.   
  
## Request a quota increase

To adjust most quotas, use the Google Cloud console. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
