---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/jobs/life-of-a-job/
title: Life of a job \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:34:18.499558+00:00
---

# Life of a job  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/jobs/life-of-a-job/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Life of a job Stay organized with collections  Save and categorize content based on your preferences. 

This page delineates the sequence of steps involved with the submission, execution, and completion of a Managed Service for Apache Spark job. It also discusses job throttling and debugging.

**Key Terms**. Below are key terms and associated actions related to the Managed Service for Apache Spark jobs flow. 

  * **Managed Service for Apache Spark** – receives job requests from the user and submits the request to the `dataproc agent`
  * **dataproc agent** – runs on the VM, receives job requests from Managed Service for Apache Spark, and spawns `driver`
  * **driver** – runs customer-supplied code, such as Hadoop jar, spark-submit, beeline, and pig applications



## Dataproc jobs flow

  1. User submits job to Managed Service for Apache Spark. 
     * [JobStatus.State](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.jobs#State) is marked as `PENDING`.
  2. Job waits to be acquired by the `dataproc` agent. 
     * If the job is acquired, [JobStatus.State](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.jobs#State) is marked as `RUNNING`.
     * If the job is not acquired due to agent failure, Compute Engine network failure, or other cause, the job is marked `ERROR`.
  3. Once a job is acquired by the agent, the agent verifies that there are sufficient resources available on the Managed Service for Apache Spark cluster's master node to start the driver. 
     * If sufficient resources are not available, the job is delayed (throttled). [JobStatus.Substate](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.jobs#substate) shows the job as `QUEUED`, and [Job.JobStatus.details](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.jobs#jobstatus) provides information on the cause of the delay.
  4. If sufficient resources are available, the `dataproc` agent starts the job driver process. 
     * At this stage, typically there are one or more applications running in [Apache Hadoop YARN](https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/YARN.html). However, Yarn applications may not start until the driver finishes scanning Cloud Storage directories or performing other start-up job tasks.
  5. The `dataproc` agent periodically sends updates to Managed Service for Apache Spark on job progress, cluster metrics, and Yarn applications associated with the job (see [Job monitoring and debugging](https://docs.cloud.google.com/managed-spark/docs/concepts/jobs/troubleshoot-jobs#job_monitoring_and_debugging)).
  6. Yarn application(s) complete. 
     * Job continues to be reported as `RUNNING` while driver performs any job completion tasks, such as materializing collections.
     * An unhandled or uncaught failure in the Main thread can leave the driver in a zombie state (marked as `RUNNING` without information as to the cause of the failure).
  7. Driver exits. `dataproc` agent reports completion to Managed Service for Apache Spark. 
     * Managed Service for Apache Spark reports job as `DONE`.



## Job concurrency

You can configure the maximum number of concurrent Managed Service for Apache Spark jobs with the [dataproc:dataproc.scheduler.max-concurrent-jobs](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties#service_properties) cluster property when you create a cluster. If this property value is not set, the upper limit on concurrent jobs is calculated as `max((masterMemoryMb - 3584) / masterMemoryMbPerJob, 5)`. `masterMemoryMb` is determined by the master VM's machine type. `masterMemoryMbPerJob` is `1024` by default, but is configurable at cluster creation with the [dataproc:dataproc.scheduler.driver-size-mb](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties#service_properties) cluster property.

For information on troubleshooting job delays due to excessive job concurrency and other causes, see [Troubleshoot job delays](https://docs.cloud.google.com/managed-spark/docs/concepts/jobs/troubleshoot-job-delays).

## Whats next

  * See [Troubleshoot jobs](https://docs.cloud.google.com/managed-spark/docs/concepts/jobs/troubleshoot-jobs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
