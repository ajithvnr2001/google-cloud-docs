---
url: https://docs.cloud.google.com/mainframe-connector/docs/run-jobs/
title: Use Cloud Run with Mainframe Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:18.678382+00:00
---

# Use Cloud Run with Mainframe Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mainframe-connector/docs/run-jobs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Mainframe Connector ](https://docs.cloud.google.com/mainframe-connector/docs)
  * [ Guides ](https://docs.cloud.google.com/mainframe-connector/docs/overview)



Send feedback 

#  Use Cloud Run with Mainframe Connector Stay organized with collections  Save and categorize content based on your preferences. 

Mainframe Connector lets you trigger and monitor Cloud Run jobs from your Mainframe. For example, you can use this feature, to integrate your existing extraction, transformation, and loading (ETL) tool with Mainframe Connector using Cloud Run jobs.

This page discusses how you can perform the following tasks using Mainframe Connector:

  * **Trigger a Cloud Run job:** initiate a Cloud Run job from Mainframe Connector
  * **View Cloud Run job logs:** view Cloud Run job logs locally on your Mainframe for monitoring
  * **Cancel a Cloud Run job:** cancel an ongoing Cloud Run job



For more information about creating and managing Cloud Run jobs, see [Cloud Run documentation](https://docs.cloud.google.com/run/docs).

## Before you begin

  * If you haven't already, then [install Mainframe Connector on your Mainframe](https://docs.cloud.google.com/mainframe-connector/docs/installation).
  * To run the Cloud Run commands, ensure that you assign the following roles to your user account: 
    * [Cloud Run Invoker](https://docs.cloud.google.com/run/docs/reference/iam/roles#run.invoker)
    * [Cloud Run Jobs Executor](https://docs.cloud.google.com/run/docs/reference/iam/roles#run.jobsExecutor)
    * [Cloud Run Jobs Executor With Overrides](https://docs.cloud.google.com/run/docs/reference/iam/roles#run.jobsExecutorWithOverrides)
    * [Cloud Run Viewer](https://docs.cloud.google.com/run/docs/reference/iam/roles#run.viewer)
    * [Logs Viewer](https://docs.cloud.google.com/logging/docs/access-control#logging.viewer) For more information about assigning roles to a user account, see [Managing access using IAM](https://docs.cloud.google.com/run/docs/securing/managing-access).
  * Set up [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc).



## Run a Cloud Run job using Mainframe Connector

To run a Cloud Run job using Mainframe Connector, follow these steps:

  1. To trigger a Cloud Run job from your Mainframe, use the [`cloud run job execute` command](https://docs.cloud.google.com/mainframe-connector/docs/api-reference#cloud-run-job-execute) from your Mainframe Job Control Language (JCL) file:
         
         //STEP01 EXEC BQSH
         //STDIN DD *
         cloud run job execute JOB_NAME
         /*
         

Replace JOB_NAME with the Cloud Run job that you want to run.

You can run the `cloud run job execute` command in the synchronous and asynchronous mode. If you want to trigger a job in synchronous mode and print job logs as the job progresses, then use the previous command with the `--tail_logs` flag.

  2. To view the logs for a specific Cloud Run job execution, use the [`cloud run job logs` command](https://docs.cloud.google.com/mainframe-connector/docs/api-reference#cloud-run-job-logs) from your Mainframe JCL file:
         
         //STEP01 EXEC BQSH
         //STDIN DD *
         cloud run job logs EXECUTION_ID
         /*
         

Replace EXECUTION_ID with the execution ID of the Cloud Run job.

  3. (Optional) To cancel a Cloud Run job, use the [`cloud run job cancel` command](https://docs.cloud.google.com/mainframe-connector/docs/api-reference#cloud-run-job-cancel) from your Mainframe JCL file:
         
         Example JCL
         //STEP01 EXEC BQSH
         //STDIN DD *
         cloud run job cancel EXECUTION_ID
         /*
         

Replace EXECUTION_ID with the execution ID of the Cloud Run job that you want to cancel.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
