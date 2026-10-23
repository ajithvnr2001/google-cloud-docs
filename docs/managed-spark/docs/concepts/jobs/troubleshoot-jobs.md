---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/jobs/troubleshoot-jobs/
title: Troubleshoot jobs \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:02.846857+00:00
---

# Troubleshoot jobs  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/jobs/troubleshoot-jobs/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Troubleshoot jobs Stay organized with collections  Save and categorize content based on your preferences. 

This document lists common job error messages, provides job monitoring and debugging information to help you troubleshoot Managed Service for Apache Spark jobs.

## Common job error messages

This section lists common job errors and solutions.

### Task was not acquired

This indicates that the Managed Service for Apache Spark agent on the master node was unable to acquire the task from the control plane. This often happens due to out-of-memory (OOM) or network issues. If the job ran successfully previously and you have not changed network configuration settings, OOM is the most likely cause, often the result of the submission of many concurrently running jobs or jobs whose drivers consume significant memory (for example, jobs that load large datasets into memory).

### No agent on master node(s) found to be active

This indicates that the Managed Service for Apache Spark agent on the master node is not active and cannot accept new jobs. This often happens due to out-of-memory (OOM) or network issues, or if the master node VM is unhealthy. If the job ran successfully previously and you have not changed network configuration settings, OOM is the most likely cause, which often results from the submission of many concurrently running jobs or jobs whose drivers consume significant memory (jobs that load large datasets into memory).

To help resolve the problem, try the following actions:

  * Restart the job.
  * [Connect using SSH to the cluster master node](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/ssh), and then determine what job or other resource is using the most memory.
  * If you can't sign in to the master node, check the [serial port (console) logs](https://docs.cloud.google.com/compute/docs/troubleshooting/viewing-serial-port-output).

![serial-port-log](https://docs.cloud.google.com/static/managed-spark/images/serial-port-log.png)

  * [Generate a diagnostic bundle](https://docs.cloud.google.com/managed-spark/docs/support/diagnose-clusters), which contains the syslog and other data.




### Task not found

This error indicates that the cluster was deleted while a job was running. You can perform the following actions to identify the principal that performed the deletion and confirm that cluster deletion occurred when a job was running:

  * View the Managed Service for Apache Spark audit logs to identify the principal that performed the [delete operation](https://docs.cloud.google.com/managed-spark/docs/guides/audit-logging#google.cloud.dataproc.v1.ClusterController.DeleteCluster).

  * Use Logging or the gcloud CLI to check that the YARN application's last known state was [RUNNING](https://hadoop.apache.org/docs/current/api//org/apache/hadoop/yarn/api/records/YarnApplicationState.html#RUNNING):

    * Use the following filter in Logging:
    
    resource.type="cloud_dataproc_cluster"
    resource.labels.cluster_name="CLUSTER_NAME"
    resource.labels.cluster_uuid="CLUSTER_UUID"
    "YARN_APPLICATION_ID State change from"
    

    * Run `gcloud dataproc jobs describe job-id --region=REGION`, then check `yarnApplications: > STATE` in the output.
  * If the principal that deleted the cluster is the [Managed Service for Apache Spark service agent service account](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/principals#service_agent_control_plane_identity), check if the cluster was configured with an [auto-delete duration](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/scheduled-deletion) that is less than the job duration.




To avoid `Task not found` errors, use automation to make sure that clusters are not deleted before all running jobs have completed.

### No space left on device

Managed Service for Apache Spark writes HDFS and scratch data to disk. This error message indicates that the cluster was created with insufficient disk space. To analyze and avoid this error:

  * Check the cluster primary disk size listed under the **Configuration** tab on the **Cluster details** page in the Google Cloud console. The recommended minimum disk size is `1000 GB` for clusters using the `n1-standard-4` machine-type and `2 TB` for clusters using the `n1-standard-32` machine-type.

  * If the cluster disk size is less than the recommended size, [recreate the cluster](https://docs.cloud.google.com/managed-spark/docs/guides/recreate-cluster) with at least the recommended disk size.

  * If disk size is the recommended size or greater, use [SSH to connect to the cluster](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/ssh) master VM, and then run `df -h` on the master VM to check disk utilization to determine if additional disk space is needed.

  * [Collect and check disk metrics](https://docs.cloud.google.com/managed-spark/docs/guides/metrics#custom_metric_collection).




## Job monitoring and debugging

Use the Google Cloud CLI, Managed Service for Apache Spark REST API, and Google Cloud console to analyze and debug Managed Service for Apache Spark jobs.

### gcloud CLI

To examine a running job's status:
    
    
    gcloud dataproc jobs describe job-id \
        --region=region
    

To view job driver output, see [View job output](https://docs.cloud.google.com/managed-spark/docs/guides/job-output#view_job_output).

### REST API

Call [jobs.get](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.jobs/get) to examine a job's [JobStatus.State](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.jobs#State), [JobStatus.Substate](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.jobs#substate), [JobStatus.details](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.jobs#jobstatus), and [YarnApplication](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.jobs#YarnApplication) fields.

### Console

To view job driver output, see [View job output](https://docs.cloud.google.com/managed-spark/docs/guides/job-output#view_job_output).

To view the dataproc agent log in [Logging](https://console.cloud.google.com/logs/query), select **Managed Service for Apache Spark Cluster→Cluster Name→Cluster UUID** from the Logs Explorer cluster selector.

![](https://docs.cloud.google.com/static/managed-spark/images/logs-cluster-selector.png)

Then use the logs selector to select `google.dataproc.agent` logs.

![](https://docs.cloud.google.com/static/managed-spark/images/logs-selector.png)

### View job logs in Logging

If a job fails, you can [access job logs in Logging](https://docs.cloud.google.com/managed-spark/docs/guides/logging#access-job-logs).

### Determine who submitted a job

**Google Cloud console support**  
The ability to see who submitted a job in the Google Cloud console will be added in a future Managed Service for Apache Spark release. 

[Looking up the details of a job](https://docs.cloud.google.com/managed-spark/docs/guides/job-output#view_job_output) will show who submitted that job in the `submittedBy` field. For example, this job output shows `user@domain` submitted the example job to a cluster.
    
    
    ...
    placement:
      clusterName: cluster-name
      clusterUuid: cluster-uuid
    reference:
      jobId: job-uuid
      projectId: project
    status:
      state: DONE
      stateStartTime: '2018-11-01T00:53:37.599Z'
    statusHistory:
    - state: PENDING
      stateStartTime: '2018-11-01T00:33:41.387Z'
    - state: SETUP_DONE
      stateStartTime: '2018-11-01T00:33:41.765Z'
    - details: Agent reported job success
      state: RUNNING
      stateStartTime: '2018-11-01T00:33:42.146Z'
    **submittedBy: user@domain**
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
