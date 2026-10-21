---
url: https://docs.cloud.google.com/run/docs/configuring/task-timeout/
title: Set task timeout for jobs \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:15:47.674604+00:00
---

# Set task timeout for jobs  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/task-timeout/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Set task timeout for jobs Stay organized with collections  Save and categorize content based on your preferences. 

By default, each task runs for a maximum of 10 minutes: you can change this to a shorter time or a longer time up to 168 hours (7 days). For tasks using GPUs, the maximum available timeout is 1 hour.

You can set the task timeout as described on this page. There is no explicit timeout on a job execution: when all tasks are done, the job execution is done.

The units specify a duration. You can specify the timeout duration as an integer value in seconds, minutes, or hours. For example, to set the timeout duration as 10 minutes and 5 seconds, specify the value as `605` seconds.

If your job has retries enabled, the timeout setting applies to each attempt of a task. If the task attempt does not complete within this time, it will be stopped. The longer a job runs, the more likely it is to run into issues that cause it to fail, such as downstream dependency failures, out of memory errors, or infrastructure issues. We recommend enabling retries for all jobs, but especially for jobs with long-running tasks.

### Maintenance events

Jobs periodically undergo maintenance events. During a maintenance event, any in-progress tasks are migrated from the current machine to a different machine. There is a brief pause in processing while the task is migrated.

The migration process preserves the state of the task, with one notable exception: outbound VPC network connections break during maintenance events. We recommend that you use client libraries that can handle occasional connection resets.

Cloud Run prints out a log message every time a task starts and finishes migrating.

Additionally, if you want to monitor or handle maintenance events in a specific way, you can catch the `SIGTSTP` signal, which is sent 10 seconds before a task is migrated. After migration, the task receives a `SIGCONT` signal immediately after the task is restarted.

The following Go sample is a function that catches these signals and prints out a log entry:
    
    
    func testSignals() {
        sigs := make(chan os.Signal, 1)
        signal.Notify(sigs, syscall.SIGTSTP, syscall.SIGCONT)
        go func() {
            for  {
                sig := <-sigs
                log.Printf("Got Signal: %v", sig)
            }
        }()
     }
     

## Required roles

To get the permissions that you need to configure Cloud Run jobs, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) on the Cloud Run job
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service identity



For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run job interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/jobs/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Set task timeout

You can set the task timeout for a Cloud Run job using the Google Cloud console, the gcloud CLI, YAML, or Terraform:

### Console

  1. In the Google Cloud console, go to the Cloud Run page:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Jobs** from the Cloud Run navigation menu:

     1. If you are creating a new job, click **Deploy container** to fill out the initial job settings page.

     2. If you are configuring an existing job, select the job, then click **View and edit job configuration**.

  3. Click **Containers, Connections, Security** to expand the job properties page.

  4. In the **Task timeout** field, specify the maximum duration for the job tasks in the current job, and select a **Time unit**. You can only specify the timeout duration as an integer value in **second** , **minute** , or **hour**. For example, to set a duration of 10 minutes and 5 seconds, in the **Task timeout** field, specify `605`, and select the **Time unit** as **second**.

  5. Click **Create** or **Update**.




###  gcloud 

  * To [set the task timeout](https://docs.cloud.google.com/sdk/gcloud/reference/run/jobs/create) when you create a new job, run the following command:
        
        gcloud run jobs create JOB --image IMAGE_URL --task-timeout TIMEOUT

Replace the following:

    * `JOB`: the name of your Cloud Run job.
    * `IMAGE_URL`: a reference to the [container image](https://docs.cloud.google.com/run/docs/building/containers)—for example, `us-docker.pkg.dev/cloudrun/container/job:latest`.
    * `TIMEOUT`: the maximum duration for the job tasks, specifying the amount of time and the units: for example, `10m5s` is ten minutes and five seconds.
  * To [update the task timeout](https://docs.cloud.google.com/sdk/gcloud/reference/run/jobs/update) for an existing job, run the following command:
        
        gcloud run jobs update JOB --task-timeout TIMEOUT




### YAML

  1. If you are creating a new job, skip this step. If you are updating an existing job, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1#job):
         
         gcloud run jobs describe JOB --format export > job.yaml

  2. Update the `timeoutSeconds:` attribute:
         
         apiVersion: run.googleapis.com/v1
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
                   timeoutSeconds: TIMEOUT

Replace the following:

     * `JOB`: the name of your Cloud Run job.
     * `IMAGE_URL`: a reference to the [container image](https://docs.cloud.google.com/run/docs/building/containers)—for example, `us-docker.pkg.dev/cloudrun/container/job:latest`.
     * `TIMEOUT`: the maximum duration for the job tasks, specifying the amount of time and the units. You can only specify time as an integer value in seconds, minutes, or hours. For example, to set a duration of 10 minutes and 5 seconds, specify `605`.

You can also specify more configuration details, such as environment variables or memory limits.

  3. Create or update the job using the following command:
         
         gcloud run jobs replace job.yaml

The `gcloud run jobs replace` command defaults to using `job.yaml` file if present.




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

Add the following to a [`google_cloud_run_v2_job`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_job) resource in your Terraform configuration:  

    
    
    resource "google_cloud_run_v2_job" "default" {
      name     = "cloud-run-job-timeout"
      location = "us-central1"
    
      deletion_protection = false # set to "true" in production
    
      template {
        template {
          timeout = "3.500s"
    
          containers {
            image = "us-docker.pkg.dev/cloudrun/container/job:latest"
          }
        }
      }
    }

## View task timeout settings

To view the current task timeout settings for your Cloud Run job, use the Google Cloud console or the Google Cloud CLI:

### Console

  1. In the Google Cloud console, go to the Cloud Run jobs page:

[Go to Cloud Run jobs](https://console.cloud.google.com/run/jobs)

  2. Click the job to open the **Job details** page.

  3. Click **View and edit job configuration**.

  4. Locate the task timeout setting in the configuration details.




###  gcloud 

  1. Run the following command:
         
         gcloud run jobs describe JOB

  2. Locate the task timeout setting in the returned configuration.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
