---
url: https://docs.cloud.google.com/dataflow/quotas/
title: Quotas and limits \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:25.498307+00:00
---

# Quotas and limits  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Resources ](https://docs.cloud.google.com/dataflow/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the quotas and system limits that apply to Dataflow.

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

To adjust most quotas, use the Google Cloud console. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase). 

There are also _system limits_ on Dataflow resources. System limits can't be changed. 

The [Dataflow managed service](https://docs.cloud.google.com/dataflow/service/dataflow-service-desc) has the following quotas and limits:

  * Each Google Cloud project can make up to **3,000,000 requests per minute**.
  * Each Dataflow job can use a maximum of **2,000 Compute Engine instances**. Without specifying a [worker zone](https://docs.cloud.google.com/dataflow/docs/concepts/regional-endpoints#workeroverride), each streaming job using [Streaming Engine](https://docs.cloud.google.com/dataflow/docs/streaming-engine) or batch job using [service-based Dataflow Shuffle](https://docs.cloud.google.com/dataflow/docs/shuffle-for-batch) can use a maximum of **4,000 Compute Engine instances**.
  * Each Google Cloud project can run at most **25 concurrent Dataflow jobs** by default.
  * Each Dataflow worker has a maximum limit of logs that it can output in a time interval. [See logging documentation for the exact limit.](https://cloud.google.com/dataflow/docs/guides/logging#LogLimits)
  * If you opt-in to organization level quotas, each organization can run at most **125 concurrent Dataflow jobs** by default.
  * Each user can make up to **15,000 monitoring requests per minute**.
  * Each user can make up to **60 job creation requests per minute**.
  * Each user can make up to **60 job template requests per minute**.
  * Each user can make up to **60 job update requests per minute**.
  * Each Google Cloud project gets the following shuffle slots in each region: 
    * asia-east1: 48 slots 
    * asia-northeast1: 24 slots 
    * asia-northeast3: 32 slots 
    * asia-south1: 64 slots 
    * asia-southeast1: 64 slots 
    * australia-southeast1: 24 slots 
    * europe-west1: 640 slots 
    * europe-west2: 32 slots 
    * europe-west3: 40 slots 
    * europe-west4: 640 slots 
    * northamerica-northeast1: 512 slots 
    * us-central1: 640 slots 
    * us-east1: 640 slots 
    * us-east4: 64 slots 
    * us-west1: 384 slots
    * us-west2: 24 slots
    * us-west3: 24 slots
    * others: 16 slots
16 slots are sufficient to [shuffle](https://docs.cloud.google.com/dataflow/service/dataflow-service-desc#dataflow-shuffle) approximately **10 TB of data** concurrently.
  * Dataflow batch jobs will be cancelled after **10 days**.



### Compute Engine quotas

When you run your pipeline on the Dataflow service, Dataflow creates Compute Engine instances to run your pipeline code.

Compute Engine quota is specified per region. Review your project's Compute Engine [quota](https://docs.cloud.google.com/compute/quotas-limits) and [request](https://support.google.com/cloud/answer/6075746) the following adjustments if needed:

  * **CPUs:** By default, Dataflow uses Auto VM Selection to select machine types for worker VMs. This feature improves job reliability by automatically selecting an available machine type from a flexible range of compatible VM families at runtime. For more information, see [Auto VM Selection for worker machine types](https://docs.cloud.google.com/dataflow/docs/guides/right-fitting#auto_vm_selection). 

Compute Engine calculates the number of CPUs by summing each instance's total CPU count. For example, running 10 instances that each have 4 vCPUs counts as 40 CPUs. For a mapping of machine types to CPU count, see [Compute Engine machine types](https://docs.cloud.google.com/compute/docs/machine-types).

  * **In-Use IP Addresses:** The number of in-use IP addresses in your project must be sufficient to accommodate the desired number of instances. To use 10 Compute Engine instances, you'll need 10 in-use IP addresses.
  * **Persistent Disk:** Dataflow attaches Persistent Disk to each instance. 
    * The default disk size is 250 GB for batch and 400 GB for streaming pipelines. For 10 instances, by default you need 2,500 GB of Persistent Disk for a batch job. 
    * The default disk size is 25 GB for Dataflow Shuffle batch pipelines. 
    * The default disk size is 30 GB for Streaming Engine streaming pipelines.
    * The Dataflow service is currently limited to 15 persistent disks per worker instance when running a streaming job. Each persistent disk is local to an individual Compute Engine virtual machine. A 1:1 ratio between workers and disks is the minimum resource allotment.
    * Compute Engine usage is based on the average number of workers, whereas Persistent Disk usage is based on the exact value of `--maxNumWorkers`. Persistent Disks are redistributed such that each worker has an equal number of attached disks.
  * **Regional Managed Instance Groups:** Dataflow deploys your Compute Engine instances as a Regional Managed Instance Group. You'll need to ensure you have the following related quota available: 
    * One **Instance Group** per Dataflow job
    * One **Instance Template** per Dataflow job
    * One **Regional Managed Instance Group** per Dataflow job
  * If Managed Instance Groups is missing for a streaming job for more than 7 days, the job is cancelled.
  * If Managed Instance Groups is missing for a batch job for more than 1 hour, the job is cancelled.



**Caution:** Manually altering Dataflow-managed Compute Engine resources associated with a Dataflow job is an unsupported operation. You should not attempt to manually stop, delete, or otherwise control the Compute Engine instances that Dataflow has created to run your job. In addition, you should not alter any Persistent Disk resources associated with your Dataflow job.

**Note:** If you're using a [Free Trial](https://cloud.google.com/free/) project, your project has a maximum of 8 cores available. You must [specify](https://docs.cloud.google.com/dataflow/pipelines/specifying-exec-params) a combination of `numWorkers`, `workerMachineType`, and `maxNumWorkers` that fits within your trial limit. 

### Additional quotas

Depending on which sources and sinks you are using, you might also need additional quota.

  1. **Pub/Sub:** If you are using Pub/Sub, you might need additional [quota](https://docs.cloud.google.com/pubsub/quotas). When planning for quota, note that processing 1 message from Pub/Sub involves 3 operations. If you use custom timestamps, you should double your expected number of operations, since Dataflow will create a separate subscription to track custom timestamps.
  2. **BigQuery:** If you are using the streaming API for BigQuery, [quota limits and other restrictions apply](https://docs.cloud.google.com/bigquery/quotas#streaming_inserts).



### Find and increase quotas

You can check your current usage of Dataflow-specific quota:

  1. In the Google Cloud console, go to the **APIs & services**.  
[Go to **API & Services**](https://console.cloud.google.com/apis/api/dataflow/quotas)
  2. To check your current Shuffle slots quota usage, on the **Quotas** tab, find the **Shuffle slots** line in the table, and in the **Usage Chart** column, click **Show usage chart**.



If you want to increase your job quota, contact [Google Cloud Support](https://docs.cloud.google.com/support), and we will increase the limit to a value that better suits your needs. The default quota is 25 concurrent Dataflow jobs for your project or 125 concurrent Dataflow jobs for your organization.

Additionally, you can increase your **Shuffle slots** quota for batch jobs by submitting a support request and specifying the expected maximum concurrent Shuffle dataset size for all jobs in your project. Prior to requesting additional Shuffle quota, please run your pipeline using Dataflow Shuffle and check the actual Shuffle quota usage.

For streaming jobs, you can increase your **Streaming Engine throughput** by submitting a support request to [Google Cloud Platform Support](https://docs.cloud.google.com/support). In your request, specify the maximum amount of data you want to shuffle between workers every minute for each [region](https://cloud.google.com/compute/docs/regions-zones/) in which your job runs.

The Dataflow service also exercises various components of the Google Cloud, such as [BigQuery](https://docs.cloud.google.com/bigquery), [Cloud Storage](https://docs.cloud.google.com/storage), [Pub/Sub](https://docs.cloud.google.com/pubsub), and [Compute Engine](https://docs.cloud.google.com/compute). These (and other Google Cloud services) employ quotas to cap the maximum number of resources you can use within a project. When you use Dataflow, you might need to adjust your quota settings for these services.

## Dataflow Prime

Quotas and limits are the same for Dataflow and Dataflow Prime. If you have quotas for Dataflow, then you don't need additional quota to run your jobs [using Dataflow Prime](https://docs.cloud.google.com/dataflow/docs/guides/enable-dataflow-prime). 

## Limits

This section describes practical production limits for Dataflow.

**Note:** These values are subject to change, and apply to the latest versions of the Apache Beam SDKs. Pipelines compiled with earlier versions of the Dataflow SDKs might encounter stricter runtime limits.Limit | Amount  
---|---  
Maximum number of workers per pipeline. | 2,000  
Maximum size for a job creation request. Pipeline descriptions with a lot of steps and very verbose names may reach this limit. | 10 MB  
Maximum size for a template launch request. | 1 MB  
Maximum number of side input shards. | 20,000  
Maximum size for a single element (except where stricter conditions apply, for example [Streaming Engine](https://docs.cloud.google.com/dataflow/docs/guides/deploying-a-pipeline#streaming-engine)). | 2 GB  
Maximum key size in batch pipelines. | 1.5 MB  
Maximum number of [log entries](https://docs.cloud.google.com/dataflow/docs/guides/logging#LogLimits) in a given time period, per worker.  | 15,000 messages every 30 seconds  
Maximum number of [custom metrics](https://docs.cloud.google.com/dataflow/docs/guides/using-cloud-monitoring#custom_metrics) per project. | 100  
Length of time that [recommendations](https://docs.cloud.google.com/dataflow/docs/guides/using-monitoring-intf#recommendations) will be stored. | 30 days  
Streaming Engine Limits | Amount  
---|---  
Maximum bytes for Pub/Sub messages. | 7 MB  
Maximum size for a single element value. | 80 MB  
Maximum size of a large key. Keys over 64 KB cause decreased performance. | 2 MB  
Maximum size for a side input. | 80 MB  
Maximum length for state tags used by `TagValue` and `TagBag`. | 64 KB  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
