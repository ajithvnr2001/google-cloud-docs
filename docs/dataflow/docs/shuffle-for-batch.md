---
url: https://docs.cloud.google.com/dataflow/docs/shuffle-for-batch/
title: Dataflow shuffle for batch jobs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:51:22.589244+00:00
---

# Dataflow shuffle for batch jobs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/shuffle-for-batch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Dataflow shuffle for batch jobs Stay organized with collections  Save and categorize content based on your preferences. 

Batch jobs use Dataflow shuffle by default. Dataflow shuffle moves the shuffle operation out of the worker VMs and into the Dataflow service backend.

The information on this page applies to batch jobs. Streaming jobs use a different shuffle mechanism, called [streaming shuffle](https://docs.cloud.google.com/dataflow/docs/concepts/exactly-once#streaming-shuffle).

## About Dataflow shuffle

  * Dataflow shuffle is the base operation behind Dataflow transforms such as `GroupByKey`, `CoGroupByKey`, and `Combine`.
  * The Dataflow shuffle operation partitions and groups data by key in a scalable, efficient, fault-tolerant manner.



## Benefits of Dataflow shuffle

The service-based Dataflow shuffle has the following benefits:

  * Faster execution time of batch pipelines for the majority of pipeline job types.
  * A reduction in consumed CPU, memory, and Persistent Disk storage resources on the worker VMs.
  * Better [Horizontal Autoscaling](https://docs.cloud.google.com/dataflow/docs/horizontal-autoscaling), because VMs don't hold any shuffle data and can therefore be scaled down earlier.
  * Better fault tolerance, because an unhealthy VM holding Dataflow shuffle data doesn't cause the entire job to fail.



## Support and limitations

  * This feature is available in all regions where Dataflow is supported. To see available locations, read [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). There might be performance differences between regions.
  * Workers must be deployed in the same region as the Dataflow job.
  * Don't specify the `zone` pipeline option. Instead, specify the `region`, and set the value to one of the available regions. Dataflow automatically selects the zone in the region you specified.

If you specify the `zone` pipeline option and set it to a zone outside of the available regions, the Dataflow job returns an error. If you set an incompatible combination of `region` and `zone`, your job can't use Dataflow shuffle.

  * For Python, Dataflow shuffle requires Apache Beam SDK for Python version 2.1.0 or later.

  * In some cases, Dataflow worker VMs are assigned [IPv6 addresses](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-ranges) from Google's internal ranges (for example, `2600:2d00::/28`). These addresses are used to facilitate optimized, direct communication with the Dataflow Shuffle service backend. This is an internal networking mechanism used specifically for Shuffle communication.




## Disk size considerations

The default boot disk size for each batch job is 25 GB. For some batch jobs, you might be required to modify the size of the disk. Consider the following:

  * A worker VM uses part of the 25 GB of disk space for the operating system, binaries, logs, and containers. Jobs that use a significant amount of disk and exceed the remaining disk capacity may fail when you use Dataflow shuffle.
  * Jobs that use a lot of disk I/O may be slow due to the performance of the small disk. For more information about performance differences between disk sizes, see [Compute Engine Persistent Disk Performance](https://docs.cloud.google.com/compute/docs/disks/performance).



To specify a larger disk size for a Dataflow shuffle job, you can use the [`--disk_size_gb`](https://docs.cloud.google.com/dataflow/pipelines/specifying-exec-params#setting-other-cloud-pipeline-options) parameter.

## Pricing

Most of the reduction in worker resources comes from offloading the shuffle work to the Dataflow service. For that reason, there is a [charge](https://cloud.google.com/dataflow/pricing) associated with the use of Dataflow shuffle. The execution times might vary from run to run. If you are running a pipeline that has important deadlines, we recommend allocating sufficient buffer time before the deadline.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
