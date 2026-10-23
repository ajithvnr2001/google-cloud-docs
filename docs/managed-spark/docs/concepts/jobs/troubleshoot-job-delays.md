---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/jobs/troubleshoot-job-delays/
title: Troubleshoot job delays \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:24.875734+00:00
---

# Troubleshoot job delays  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/jobs/troubleshoot-job-delays/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Troubleshoot job delays Stay organized with collections  Save and categorize content based on your preferences. 

This page lists common causes of Managed Service for Apache Spark job scheduling delays, with information that can help you avoid them.

## Overview

The following are common reasons why a Managed Service for Apache Spark job is being delayed (throttled):

  * Too many running jobs
  * High system memory usage
  * Not enough free memory
  * Rate limit exceeded



Typically, the job delay message will be issued in the following format:
    
    
    Awaiting execution [SCHEDULER_MESSAGE]"
    

The following sections provide possible causes and solutions for specific job delay scenarios.

## Too many running jobs

Scheduler message:
    
    
    Throttling job ### (and maybe others): Too many running jobs (current=xx max=xx)
    

Causes:

The maximum number of concurrent jobs based on master VM memory is exceeded (the job driver runs on the Managed Service for Apache Spark cluster master VM). By default, Managed Service for Apache Spark reserves 3.5GB of memory for applications, and allows 1 job per GB.

Example: The `n1-standard-4` machine type has `15GB` memory. With `3.5GB` reserved for overhead, `11.5GB` remains. Rounding down to an integer, `11GB` is available for up to 11 concurrent jobs.

Solutions:

  1. Monitor log metrics, such as CPU usage and memory, to estimate job requirements.

  2. When you create a job cluster:

     1. Use a larger memory machine type for the cluster master VM.

     2. If `1GB` per job is more than you need, set the `dataproc:dataproc.scheduler.driver-size-mb` [cluster property](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties#service_properties) to less than `1024`.

     3. Set the `dataproc:dataproc.scheduler.max-concurrent-jobs` [cluster property](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties#service_properties) to a value suited to your job requirements.




## High system memory or not enough free memory

Scheduler message:
    
    
    Throttling job xxx_____JOBID_____xxx (and maybe others): High system memory usage (current=xx%)
    
    Throttling job xxx_____JOBID_____xxx (and maybe others): Not enough free memory (current=xx min=xx)
    

Causes:

By default, the Managed Service for Apache Spark agent throttles job submission when memory use reaches 90% (`0.9)`. When this limit is reached, new jobs cannot be scheduled.

The amount of free memory needed to schedule another job on the cluster is not sufficient.

Solution:

  1. When you create a cluster:

     1. Increase the value of the `dataproc:dataproc.scheduler.max-memory-used` [cluster property](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties#service_properties). For example, set it above the `0.90` default to `0.95`. Setting the value to `1.0` disables master-memory-utilization job throttling. 
     2. Increase the value of the `dataproc.scheduler.min-free-memory.mb` [cluster property](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties#service_properties). The default value is `256` MB.



## Job rate limit exceeded

Scheduler message:
    
    
    Throttling job xxx__JOBID___xxx (and maybe others): Rate limit
    

Causes:

The Managed Service for Apache Spark agent reached the job submission rate limit.

Solutions:

  1. By default, the Managed Service for Apache Spark agent job submission is limited at `1.0 QPS`, which you can set to a different value when you create a cluster with the `dataproc:dataproc.scheduler.job-submission-rate` [cluster property](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties#service_properties).



## View job status

To view job status and details, see [Job monitoring and debugging](https://docs.cloud.google.com/managed-spark/docs/concepts/jobs/troubleshoot-jobs#job_monitoring_and_debugging).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
