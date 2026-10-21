---
url: https://docs.cloud.google.com/run/docs/execute/jobs/
title: Execute jobs \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:15:47.180560+00:00
---

# Execute jobs  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/execute/jobs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Execute jobs Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to execute Cloud Run jobs. Executing a job creates a [job execution](https://docs.cloud.google.com/run/docs/managing/job-executions) in which all tasks must run to completion successfully in order for the job execution to be successful. Job executions write logs to [Cloud Logging](https://docs.cloud.google.com/run/docs/logging) and send monitoring data to [Cloud Monitoring](https://docs.cloud.google.com/run/docs/monitoring).

In addition to these logging features, you can also view job execution details for the most recent 1,000 executions of a job using the [execution details pane](https://docs.cloud.google.com/run/docs/managing/job-executions#view-details), _along with any executions that occurred within the last seven days_. Older execution details are removed and are no longer visible in the execution details pane. However, the logs and monitoring data for older executions are still available in [Cloud Logging](https://docs.cloud.google.com/logging/docs) and [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs), subject to the retention policies for those products.

## What is job execution?

To _execute_ a Cloud Run job means to instantiate and run a configured workload to completion, divided into one or more parallel or sequential tasks, without listening for or serving HTTP requests.

The core entities of a job are as follows:

  * **Job** : A static, persistent configuration. It defines the container image, resource allocations (CPU, memory, GPU), environment variables, and execution parameters (total tasks, parallelism, timeouts, and retries).

  * **Execution** : The temporal lifecycle event created when you trigger a job. An "execution" represents the overall tracking object for a single run of the job.

  * **Task** : A single running instance of the configured container. An execution is composed of one or more tasks ([`taskCount`](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.jobs.executions)).




There are fundamentally two different ways to execute a job:

  * As a regular job.

When you execute a job as a regular job (the default), execution starts as soon as possible.

  * As a [delayed job](https://docs.cloud.google.com/run/docs/delayed-jobs).

When you execute a job as a delayed job, you are agreeing to defer non-urgent tasks by up to a maximum duration of 12 hours, in exchange for a better price.




While every job is either regular or delayed, you can override these settings for a single job execution, so that a regular job executes as a delayed job, or a delayed job executes as a regular job. See [Delay execution of a job](https://docs.cloud.google.com/run/docs/delayed-jobs) for details.

The following table provides a more granular view of the possible execution scenarios for a given job instance:

Execution Method | Command / Trigger | Resource Allocation Timing | Cost Tier | Max Delay / Timeout | Typical Use Case  
---|---|---|---|---|---  
**Standard (On-Demand)** | `gcloud run jobs execute` | Starts immediately / ASAP | Standard Job Rates | Immediate start; max 7 days runtime | Ad-hoc data processing, manual triggers, event-driven pipelines  
**Create/Update & Run** | `gcloud run jobs create/update --execute-now` | Starts immediately upon creation | Standard Job Rates | Immediate start; max 7 days runtime | CI/CD deployments, schema migrations, post-deployment warmups  
**Delayed Execution** | `gcloud beta run jobs execute --delay-execution` | Starts within a system-optimized window | Discounted Rate | Max 12h delay before auto-cancellation, max 12 hour timeout | Non-urgent batch jobs, overnight analytics, bulk AI inference  
**Execution with Overrides** | `gcloud run jobs execute --args=... --tasks=...` | Starts immediately / ASAP | Standard Job Rates | Immediate start; overridden timeout | Partition-specific backfills, dynamic batch sizing, debug runs  
  
## Required roles

To get the permissions that you need for the operations described on this page, ask your administrator to grant you one of the following IAM roles on your Cloud Run job:

  * To execute jobs using the Google Cloud CLI: [Cloud Run Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.invoker) (`roles/run.invoker`) on the Cloud Run job
  * To execute jobs using the Google Cloud console, to override job configurations, or to cancel job executions: [Cloud Run Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) on the Cloud Run job



For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run job interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/jobs/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Execute jobs

You can execute jobs using the Google Cloud console, the gcloud CLI, client libraries, or REST API.

### Console

To execute a job, follow these steps:

  1. In the Google Cloud console, go to the Cloud Run **Jobs** page:

[Go to Cloud Run jobs](https://console.cloud.google.com/run/jobs)

  2. Locate the job you are interested in.

  3. Click the job to display the job details page.

  4. Click **Execute**.




###  gcloud 

To execute an existing job, run the following command:
    
    
    gcloud run jobs execute JOB

If you want the command to wait until the execution completes, run the following command:
    
    
    gcloud run jobs execute JOB --wait --region=REGION

To tail the logs of the execution immediately after launching it, run the following command:
    
    
    gcloud beta run jobs execute JOB --tail --region=REGION

Replace the following:

  * `JOB`: the name of your Cloud Run job.
  * `REGION`: the region in which the resource can be found. For example, `europe-west1`. Alternatively, set the `run/region` property.



### Client libraries

To execute an existing job from code:

  * [Go](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/run/latest/apiv2#cloud_google_com_go_run_apiv2_JobsClient_RunJob)
  * [Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.JobsClient#com_google_cloud_run_v2_JobsClient_runJobAsync_com_google_cloud_run_v2_JobName_)
  * [Node.js](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/protos.google.cloud.run.v2.job#_google_cloud_run_protos_google_cloud_run_v2_Job_startExecutionToken_member)
  * [Python](https://docs.cloud.google.com/python/docs/reference/run/latest/google.cloud.run_v2.services.jobs.JobsClient#google_cloud_run_v2_services_jobs_JobsClient_run_job)
  * [Ruby](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Jobs-Client#Google__Cloud__Run__V2__Jobs__Client_run_job_instance_)
  * [PHP](https://docs.cloud.google.com/php/docs/reference/cloud-run/latest/V2.Client.JobsClient#_Google_Cloud_Run_V2_Client_JobsClient__runJob__)
  * [.NET](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/latest/Google.Cloud.Run.V2.JobsClient#Google_Cloud_Run_V2_JobsClient_RunJob_Google_Cloud_Run_V2_JobName_Google_Api_Gax_Grpc_CallSettings_)



### REST API

To execute an existing job, send a `POST` HTTP request to the [`jobs.run` API method](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.jobs.executions).

For example, using `curl`:
    
    
    curl -H "Content-Type: application/json" \
      -H "Authorization: Bearer ACCESS_TOKEN" \
      -X POST \
      -d '' \
      https://run.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/jobs/JOB:run

Replace the following:

  * `ACCESS_TOKEN`: a valid access token for an account that has the [IAM permissions to execute a job](https://docs.cloud.google.com/run/docs/reference/iam/permissions). For example, if you are logged into gcloud, you can retrieve an access token using `gcloud auth print-access-token`. From within a Cloud Run container instance, you can retrieve an access token using the [container instance metadata server](https://docs.cloud.google.com/run/docs/container-contract#metadata-server).
  * `PROJECT_ID`: the Google Cloud project ID.
  * `REGION`: the Google Cloud region of the job.
  * `JOB`: the name of your Cloud Run job.



## Execute jobs immediately

### Console

To execute a job immediately, follow these steps:

  1. In the Google Cloud console, go to the Cloud Run page:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Jobs** from the Cloud Run navigation menu:

     1. If you are creating a new job, click **Deploy container** to fill out the initial job settings page.

     2. If you are configuring an existing job, select the job, then click **View and edit job configuration**.

  3. Go to the bottom of the page and check the **Execute job immediately** box before creating or updating the job.




###  gcloud 

You can specify the [`--execute-now`](https://docs.cloud.google.com/sdk/gcloud/reference/run/jobs/create#--execute-now) flag when creating or updating a job.

  * To create a job, run the following command:
        
        gcloud run jobs create JOB \
          --image IMAGE_URL \
          --execute-now \
          --region=REGION

  * To update a job, run the following command:
        
        gcloud run jobs update JOB --execute-now --region=REGION




Replace the following:

  * `JOB`: the name of your Cloud Run job.
  * `IMAGE_URL`: a reference to the [container image](https://docs.cloud.google.com/run/docs/building/containers)—for example, `us-docker.pkg.dev/cloudrun/container/job:latest`.
  * `REGION`: the region in which the resource can be found. For example, `europe-west1`.



### YAML

You can store your job specification in a `YAML` file and then deploy it using the gcloud CLI.

  1. If you are creating a new job, skip this step. If you are updating an existing job, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1#job):
         
         gcloud run jobs describe JOB --format export > job.yaml

  2. Configure the `startExecutionToken` attribute as shown:
         
         apiVersion: run.googleapis.com/v2
         kind: Job
         metadata:
           name: JOB
         spec:
           template:
             spec:
               template:
                 spec:
                   containers:
                   - image: IMAGE_URL
           startExecutionToken: START_EXECUTION_SUFFIX

Replace the following:

     * `JOB`: the name of your Cloud Run job.
     * `IMAGE_URL`: a reference to the [container image](https://docs.cloud.google.com/run/docs/building/containers)—for example, `us-docker.pkg.dev/cloudrun/container/job:latest`.
     * `START_EXECUTION_SUFFIX`: a unique string used as a suffix for creating a new execution. The job will become ready when the execution is successfully started. The sum of job name and token length must be fewer than 63 characters.

You can also specify more configuration such as environment variables or memory limits.

  3. Create or update the job using the following command:
         
         gcloud run jobs replace job.yaml

The `gcloud run jobs replace` command defaults to using `job.yaml` file if present.




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

Add the following to a [`google_cloud_run_v2_job`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_job) resource in your Terraform configuration:  

    
    
    resource "google_cloud_run_v2_job" "default" {
       name     = "cloudrun-job"
       location = "REGION"
       deletion_protection = false
       start_execution_token = "START_EXECUTION_SUFFIX"
       template {
          template {
             containers {
             image = "us-docker.pkg.dev/cloudrun/container/job"
             }
          }
       }
    }
    

Replace the following:

  * `REGION`: the Google Cloud region. For example, europe-west1.
  * `START_EXECUTION_SUFFIX`: a unique string used as a suffix for creating a new execution. The job will become ready when the execution is successfully started. The sum of job name and token length must be fewer than 63 characters.



### Client libraries

To immediately execute a job from code using Cloud Client Libraries:

  * [Go](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/run/latest/apiv2/runpb#cloud_google_com_go_run_apiv2_runpb_Job_StartExecutionToken)
  * [Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Job#com_google_cloud_run_v2_Job_getStartExecutionToken__)
  * [Node.js](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/protos.google.cloud.run.v2.job#_google_cloud_run_protos_google_cloud_run_v2_Job_startExecutionToken_member)
  * [Python](https://docs.cloud.google.com/python/docs/reference/run/latest/google.cloud.run_v2.services.jobs.JobsClient#google_cloud_run_v2_services_jobs_JobsClient_create_job)
  * [Ruby](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Job#Google__Cloud__Run__V2__Job_start_execution_token_instance_)
  * [PHP](https://docs.cloud.google.com/php/docs/reference/cloud-run/latest/V2.Job#_Google_Cloud_Run_V2_Job__getStartExecutionToken__)
  * [.NET](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/latest/Google.Cloud.Run.V2.Job#Google_Cloud_Run_V2_Job_StartExecutionToken)



### REST API

To execute jobs immediately on creation, send a `POST` HTTP request to the Cloud Run Admin API [`jobs` endpoint](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.jobs).

For example, using `curl`:
    
    
    curl -H "Content-Type: application/json" \
      -H "Authorization: Bearer ACCESS_TOKEN" \
      -X POST \
      -d '{
         "template": {
            "template": {
               "containers":
                  {
                     "image": "IMAGE_URL"
                  }
            }
         },
         "startExecutionToken": "START_EXECUTION_SUFFIX"
      }' \
      "https://run.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/jobs?jobId=JOB"

Replace the following:

  * `ACCESS_TOKEN`: a valid access token for an account that has the [IAM permissions to create jobs](https://docs.cloud.google.com/run/docs/reference/iam/permissions). For example, if you are logged into gcloud, you can retrieve an access token using `gcloud auth print-access-token`. From within a Cloud Run container instance, you can retrieve an access token using the [container instance metadata server](https://docs.cloud.google.com/run/docs/container-contract#metadata-server).
  * `IMAGE_URL`: a reference to the [container image](https://docs.cloud.google.com/run/docs/building/containers)—for example, `us-docker.pkg.dev/cloudrun/container/job:latest`.
  * `START_EXECUTION_SUFFIX`: a unique string used as a suffix for creating a new execution. The job will become ready when the execution is successfully started. The sum of job name and token length must be fewer than 63 characters.
  * `PROJECT_ID`: the Google Cloud project ID.
  * `REGION`: the Google Cloud region of the job.
  * `JOB`: the name of your Cloud Run job.



## Delay execution

To disable immediate execution, or convert your regular job to a delayed job, see [Delay execution of a job](https://docs.cloud.google.com/run/docs/delayed-jobs).

## Override job configuration for a specific execution

You can override the arguments, environment variables, number of tasks, and task timeout configured for a job when you execute a job by setting these parameters when you start a new job execution. The parameters you specify affect only this execution and not subsequent ones, because the underlying job definition remains unchanged.

Some common use cases include:

  * You execute the job programmatically from your code, and want to override arguments or environment variables, for example to tell the job where the input data is located for this execution.
  * You have a job where each task is intended to only process one piece of input data. You want to override the number of tasks based on the number of inputs to be processed.
  * The running time of your job varies between executions. You want to override the task timeout based on the expected running time of the job.



You can override job configuration for an execution using the Google Cloud console, the gcloud CLI, client libraries, or the REST API:

### Console

  1. In the Google Cloud console, go to the Cloud Run jobs page:

[Go to Cloud Run jobs](https://console.cloud.google.com/run/jobs)

  2. Click the job to open the job details pane.

  3. Click the expander arrow in front of the **Edit** button and click **Execute with overrides** to display the **Execute job with overrides** form.

  4. Configure the arguments, environment variables, number of tasks, and task timeout configuration for this execution, then click **Execute**.




###  gcloud 

Use the command:
    
    
    gcloud run jobs execute JOB \
         --args ARGS \
         --update-env-vars KEY=VALUE,KEY_N=VALUE_N \
         --tasks TASKS \
         --task-timeout TIMEOUT

Replace the following:

  * `JOB`: the name of your Cloud Run job.
  * `ARGS`: the [job arguments](https://docs.cloud.google.com/run/docs/configuring/containers#command-line_2).
  * `KEY` and `VALUE` pairs: the [environment variables](https://docs.cloud.google.com/run/docs/configuring/environment-variables#command-line_1).
  * `TASKS`: the [number of tasks](https://docs.cloud.google.com/run/docs/create-jobs#command-line).
  * `TIMEOUT`: the [task timeout](https://docs.cloud.google.com/run/docs/configuring/task-timeout).



### Client libraries

To execute an existing job from code, overriding the job configuration:

  * [Go](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/run/latest/apiv2/runpb#cloud_google_com_go_run_apiv2_runpb_RunJobRequest_Overrides)
  * [Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.RunJobRequest.Overrides)
  * [Node.js](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/protos.google.cloud.run.v2.runjobrequest.ioverrides)
  * [Python](https://docs.cloud.google.com/python/docs/reference/run/latest/google.cloud.run_v2.types.RunJobRequest.Overrides)
  * [Ruby](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-RunJobRequest-Overrides)
  * [PHP](https://docs.cloud.google.com/php/docs/reference/cloud-run/latest/V2.RunJobRequest.Overrides)
  * [.NET](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/latest/Google.Cloud.Run.V2.RunJobRequest.Types.Overrides)



### REST API

To override job configuration for an existing job, send a `POST` HTTP request to request to the Cloud Run Admin API [`jobs` endpoint](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.jobs/run#overrides)

For example, using `curl`:
    
    
    curl -H "Content-Type: application/json" \
      -H "Authorization: Bearer ACCESS_TOKEN" \
      -X POST \
      -d '{"overrides": {"containerOverrides": [{"args": ["ARGS"], "env": [{"name": "KEY", "value": "VALUE"}]}], "taskCount": TASKS, "timeout": "TIMEOUT" }}' \
      https://run.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/jobs/JOB:run

Replace the following:

  * `ACCESS_TOKEN`: a valid access token for an account that has the [IAM permissions to execute job overrides](https://docs.cloud.google.com/run/docs/reference/iam/permissions). For example, if you are logged into gcloud, you can retrieve an access token using `gcloud auth print-access-token`. From within a Cloud Run container instance, you can retrieve an access token using the [container instance metadata server](https://docs.cloud.google.com/run/docs/container-contract#metadata-server).
  * `ARGS`: [job arguments](https://docs.cloud.google.com/run/docs/configuring/containers#command-line_2).
  * `KEY` and `VALUE` pairs: [environment variables](https://docs.cloud.google.com/run/docs/configuring/environment-variables#command-line_1).
  * `TASKS`: the [number of tasks](https://docs.cloud.google.com/run/docs/create-jobs#command-line).
  * `TIMEOUT`: the [task timeout](https://docs.cloud.google.com/run/docs/configuring/task-timeout).
  * `PROJECT_ID`: the Google Cloud project ID.
  * `REGION`: the Google Cloud region of the job.
  * `JOB`: the name of your Cloud Run job.



## Cancel job execution

**Important:** On September 16, 2024, the permission required to cancel a Cloud Run job changed to run.executions.cancel. The Cloud Run Developer and Cloud Run Source Developer predefined roles contain this permission.

To stop a currently running Cloud Run job execution, use the cancel feature. Cancelling a job execution stops the current job execution. Cancelled executions have the status _cancelled_. You will still be able to view the execution, including its configuration data, logs, and monitoring data.

**Note:** In comparison, if you use the job execution [delete](https://docs.cloud.google.com/run/docs/managing/job-executions#delete) method to stop the current job execution, Cloud Run removes the execution from the job execution list and you can't view it.

Cancelling a job execution _does not reverse the charges_ for any Cloud Run jobs usage for the time that the job was executing.

To cancel an execution, use the Google Cloud console, the gcloud CLI, client libraries, or the REST API:

### Console

  1. In the Google Cloud console, go to the Cloud Run jobs page:

[Go to Cloud Run jobs](https://console.cloud.google.com/run/jobs)

  2. Click the job to open the job details pane.

  3. Select the job execution you want to cancel.

  4. In the **Actions** menu, click the ellipsis icon, then click **Cancel**.




###  gcloud 

Use the command:
    
    
    gcloud run jobs executions cancel EXECUTION_NAME

Replace `EXECUTION_NAME` with the name of the execution.

This command asks for confirmation, so respond to the prompt by entering `y` to confirm.

### Client libraries

To cancel a job execution from code:

  * [Go](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/run/latest/apiv2#cloud_google_com_go_run_apiv2_ExecutionsClient_CancelExecution)
  * [Java](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.ExecutionsClient#com_google_cloud_run_v2_ExecutionsClient_cancelExecutionAsync_com_google_cloud_run_v2_CancelExecutionRequest_)
  * [Node.js](https://docs.cloud.google.com/nodejs/docs/reference/run/latest/run/v2.executionsclient#_google_cloud_run_v2_ExecutionsClient_cancelExecution_member_1_)
  * [Python](https://docs.cloud.google.com/python/docs/reference/run/latest/google.cloud.run_v2.services.executions.ExecutionsClient#google_cloud_run_v2_services_executions_ExecutionsClient_cancel_execution)
  * [Ruby](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Executions-Rest-Client#Google__Cloud__Run__V2__Executions__Rest__Client_cancel_execution_instance_)
  * [PHP](https://docs.cloud.google.com/php/docs/reference/cloud-run/latest/V2.Client.ExecutionsClient#_Google_Cloud_Run_V2_Client_ExecutionsClient__cancelExecution__)
  * [.NET](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Run.V2/latest/Google.Cloud.Run.V2.ExecutionsClient#Google_Cloud_Run_V2_ExecutionsClient_CancelExecution_Google_Cloud_Run_V2_CancelExecutionRequest_Google_Api_Gax_Grpc_CallSettings_)



### REST API

To cancel a job execution, send a `POST` HTTP request to request to the Cloud Run Admin API [`jobs` endpoint](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.jobs.executions/cancel)

For example, using `curl`:
    
    
    curl -H "Content-Type: application/json" \
      -H "Authorization: Bearer ACCESS_TOKEN" \
      -X POST \
      -d '' \
      https://run.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/jobs/JOB/executions/EXECUTION_NAME:cancel

Replace the following:

  * `ACCESS_TOKEN`: a valid access token for an account that has the [IAM permissions to cancel job executions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). For example, if you are logged into gcloud, you can retrieve an access token using `gcloud auth print-access-token`. From within a Cloud Run container instance, you can retrieve an access token using the [container instance metadata server](https://docs.cloud.google.com/run/docs/container-contract#metadata-server).
  * `PROJECT_ID`: the Google Cloud project ID.
  * `REGION`: the Google Cloud region of the job.
  * `JOB`: the name of your Cloud Run job.
  * `EXECUTION_NAME`: the name of the job execution.



## Delete a job execution

You can delete a job execution, even if it is executing. If you delete an execution, it stops the execution from continuing. For details, see [Delete a job execution](https://docs.cloud.google.com/run/docs/managing/job-executions#delete).

## What's next

After you execute a job, you can follow these steps:

  * [View job logs](https://docs.cloud.google.com/run/docs/logging)
  * [Monitor job performance](https://docs.cloud.google.com/run/docs/monitoring)
  * [Manage job executions](https://docs.cloud.google.com/run/docs/managing/job-executions)
  * [Manage jobs](https://docs.cloud.google.com/run/docs/managing/jobs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
