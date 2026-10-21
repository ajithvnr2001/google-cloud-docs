---
url: https://docs.cloud.google.com/run/docs/configuring/parallelism/
title: Set parallelism for jobs \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:10:51.854170+00:00
---

# Set parallelism for jobs  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/parallelism/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Set parallelism for jobs Stay organized with collections  Save and categorize content based on your preferences. 

You use `parallelism` to specify the maximum number of tasks in a job execution that can run in parallel. By default, tasks will be started as quickly as possible, up to a [maximum](https://docs.cloud.google.com/run/quotas) that varies depending on how many CPUs you are using.

Lowering parallelism limits how many tasks run in parallel. This is useful in cases where one of your backing resources, such as a database, has limited scaling and cannot handle a large number of parallel requests.

## Required roles

To get the permissions that you need to configure Cloud Run jobs, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) on the Cloud Run job
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service identity



For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run job interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/jobs/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Configure parallelism

You can configure parallelism for a Cloud Run job using the Google Cloud console, the gcloud CLI, YAML, or Terraform:

### Console

  1. In the Google Cloud console, go to the Cloud Run page:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Jobs** from the Cloud Run navigation menu:

     1. If you are creating a new job, click **Deploy container** to fill out the initial job settings page.

     2. If you are configuring an existing job, select the job, then click **View and edit job configuration**.

  3. Click **Containers, Connections, Security** to expand the job properties page.

  4. In the **Parallelism** section, select **Run as many tasks concurrently as possible** for best performance. If you need to lower the number of concurrent tasks, for example, if your backing resources are limited, select **Limit the number of concurrent tasks**. Then, specify an integer between 0 and the [maximum](https://docs.cloud.google.com/run/quotas) number of tasks running in parallel allowed by quota that don't exceed the number of tasks.

  5. Click **Create** or **Update**.




###  gcloud 

  * To [set parallelism](https://docs.cloud.google.com/sdk/gcloud/reference/run/jobs/create) when you create a new job, run the following command:
        
        gcloud run jobs create JOB --image IMAGE_URL --parallelism PARALLELISM

Replace the following:

    * `JOB`: the name of your Cloud Run job.
    * `IMAGE_URL`: a reference to the [container image](https://docs.cloud.google.com/run/docs/building/containers)—for example, `us-docker.pkg.dev/cloudrun/container/job:latest`.
    * `PARALLELISM`: an integer between 0 and the [maximum](https://docs.cloud.google.com/run/quotas) number of tasks running in parallel, allowed by quota, that don't exceed the number of tasks.
  * To [update parallelism](https://docs.cloud.google.com/sdk/gcloud/reference/run/jobs/update) for an existing job, run the following command:
        
        gcloud run jobs update JOB --parallelism PARALLELISM




### YAML

  1. If you are creating a new job, skip this step. If you are updating an existing job, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1#job):
         
         gcloud run jobs describe JOB --format export > job.yaml

  2. Update the `parallelism:` attribute:
         
         apiVersion: run.googleapis.com/v1
         kind: Job
         metadata:
           name: JOB
         spec:
           template:
             spec:
               parallelism: PARALLELISM
               template:
                 spec:
                   containers:
                   - image: IMAGE_URL

Replace the following:

     * `JOB`: the name of your Cloud Run job.
     * `IMAGE_URL`: a reference to the [container image](https://docs.cloud.google.com/run/docs/building/containers)—for example, `us-docker.pkg.dev/cloudrun/container/job:latest`.
     * `PARALLELISM`: an integer between 0 and the [maximum](https://docs.cloud.google.com/run/quotas) number of tasks running in parallel, allowed by quota, that don't exceed the number of tasks.

You can also specify more configuration such as environment variables or memory limits.

  3. Create or update the job using the following command:
         
         gcloud run jobs replace job.yaml

The `gcloud run jobs replace` command defaults to using `job.yaml` file if present.




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

Add the following to a [`google_cloud_run_v2_job`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_job) resource in your Terraform configuration:  

    
    
    resource "google_cloud_run_v2_job" "default" {
      name     = "cloud-run-job-parallelism"
      location = "us-central1"
    
      deletion_protection = false # set to "true" in production
    
      template {
        task_count  = 3
        parallelism = 3
    
        template {
          containers {
            image = "us-docker.pkg.dev/cloudrun/container/job:latest"
          }
        }
      }
    }

## View parallelism settings

To view the current parallelism settings for your Cloud Run job, use the Google Cloud console or the Google Cloud CLI:

### Console

  1. In the Google Cloud console, go to the Cloud Run jobs page:

[Go to Cloud Run jobs](https://console.cloud.google.com/run/jobs)

  2. Click the job to open the **Job details** page.

  3. Click **View and edit job configuration**.

  4. Locate the parallelism setting in the configuration details.




###  gcloud 

  1. Run the following command:
         
         gcloud run jobs describe JOB

  2. Locate the parallelism setting in the returned configuration.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
