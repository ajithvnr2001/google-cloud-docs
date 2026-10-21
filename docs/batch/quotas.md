---
url: https://docs.cloud.google.com/batch/quotas/
title: Quotas and limits \u00a0|\u00a0 Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:45:09.795489+00:00
---

# Quotas and limits  |  Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Resources ](https://docs.cloud.google.com/batch/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the quotas and system limits that apply to Batch.

  * _Quotas_ have default values, but you can typically request adjustments.
  * _System limits_ are fixed values that can't be changed.



Batch jobs run on Compute Engine resources, so Batch is also subject to [Compute Engine quotas and limits](https://docs.cloud.google.com/compute/quotas). If your Batch job also uses other Google Cloud services, then it is subject to the quotas for those services too. Attempts to exceed a quota or limit return an [error](https://docs.cloud.google.com/batch/docs/troubleshooting#insufficient-quota). For more information, see the [Cloud Quotas documentation](https://docs.cloud.google.com/docs/quotas/overview).

In addition to the quotas and limits from other Google Cloud services, Batch has the following quotas and limits, which cannot be changed.

## Rate quotas

The following limits apply to Batch requests. These limits appear as quotas–for example, in the Google Cloud console–however, they can not be increased.

Limit | Value  
---|---  
Agent requests per minute per region | 30,000  
Mutation requests per minute per region | 6,000  
Read requests per minute per region | 15,000  
  
## Job limits

The following limits apply to Batch jobs.

Limit | Value  
---|---  
Tasks per task group | 100,000  
Parallel tasks per job | 5,000  
Concurrent VMs per single-zone job1 | 2,000  
Concurrent VMs per multi-zone job1 | 4,000  
Size of the job definition2 | 1 MB  
Wait time (duration of `QUEUED` job state) before automatic failure | 2 days  
Run time (duration of `RUNNING` job state) before automatic failure3 | 14 days  
  
1 The terms _single-zone job_ and _multi-zone job_ here refer to the number of zones allowed for a job's VMs, which might be different than the zones for a job's location. For more information, see [Batch locations](https://docs.cloud.google.com/batch/docs/locations).

2 For example, roughly the size of the REST request to the [`jobs.create` method](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs/create) or gcloud CLI [`--config` file](https://docs.cloud.google.com/sdk/gcloud/reference/batch/jobs/submit#--config). You can work around this limit by the dividing the tasks across multiple jobs—for example, learn how to [schedule dependent jobs](https://docs.cloud.google.com/batch/docs/create-run-dependent-job) ([Preview](https://cloud.google.com/products/#product-launch-stages)).

3 This limit has the following exceptions: 

  * If you set the `provisioningModel` field for a job to `FLEX_START`, then the maximum run time before automatic failure is 7 days instead.
  * If a job uses a machine type from the A3 series, sets the `reservation` field to `NO_RESERVATION`, and has the `provisioningModel` either undefined or set to `STANDARD`, then the maximum run time before automatic failure is 7 days instead.
  * Optionally, you can reduce the maximum run time before automatic failure for a job by using [timeouts](https://docs.cloud.google.com/batch/docs/set-timeouts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
