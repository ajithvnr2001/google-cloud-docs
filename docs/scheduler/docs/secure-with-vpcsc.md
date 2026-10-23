---
url: https://docs.cloud.google.com/scheduler/docs/secure-with-vpcsc/
title: Secure cron jobs with VPC Service Controls \u00a0|\u00a0 Cloud Scheduler \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:56:03.472562+00:00
---

# Secure cron jobs with VPC Service Controls  |  Cloud Scheduler  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/scheduler/docs/secure-with-vpcsc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Scheduler ](https://docs.cloud.google.com/scheduler/docs)
  * [ Guides ](https://docs.cloud.google.com/scheduler/docs/overview)



Send feedback 

#  Secure cron jobs with VPC Service Controls Stay organized with collections  Save and categorize content based on your preferences. 

[VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) lets you set up a secure perimeter around Google Cloud resources to help guard against data exfiltration. You can include Cloud Scheduler jobs in a VPC Service Controls perimeter to protect your scheduled workloads and restrict job targets.

## Limitations

The following limitations apply to VPC Service Controls support for Cloud Scheduler.

### Enforced actions

VPC Service Controls is enforced on the following actions:

  * Cloud Scheduler job creations
  * Cloud Scheduler job updates



### Why does this matter?

Because VPC Service Controls is enforced only on job creations and updates, VPC Service Controls is not automatically enforced for jobs that were created before you added Cloud Scheduler to your VPC Service Controls perimeter. Jobs continue to execute even if the job targets are not part of your VPC Service Controls perimeter or are not supported targets. To enforce VPC Service Controls for all Cloud Scheduler jobs:

  * **Jobs with targets that are either unsupported or are outside your perimeter:** Delete the jobs. In this document, see Delete non-compliant jobs.
  * **Jobs with targets that are both supported and inside your perimeter:** Run an update on each job after adding Cloud Scheduler to your perimeter. In this document, see Enforce VPC Service Controls on pre-existing jobs.



### Supported targets

The Cloud Scheduler integration with VPC Service Controls supports the following targets. HTTP endpoints are supported if listed; however, arbitrary HTTP endpoints are _not_ supported.

  * Cloud Run services—must use the canonical default `run.app` domain. Custom domains and custom DNS are not supported and will cause job creation to fail.
  * Cloud Run functions—must use the canonical default `cloudfunctions.net` or `run.app` domain. Custom domains and custom DNS are not supported and will cause job creation to fail.
  * Google Cloud APIs that are VPC Service Controls-compliant (either in Preview or GA) can be in a different Google Cloud project from your Cloud Scheduler job.

    * You must use the global endpoint format (`https://SERVICE.googleapis.com`). Regional endpoints—such as `*.rep.googleapis.com`, `LOCATION.SERVICE.googleapis.com`, and `REGION-SERVICE.googleapis.com`—and mTLS endpoints (`*.mtls.googleapis.com`) are rejected.

This requirement applies to job target URIs only. To send your own requests to the Cloud Scheduler API through a regional endpoint, see [Use regional endpoints](https://docs.cloud.google.com/scheduler/docs/regional-endpoints).

    * For Cloud Run jobs, the supported URI format is the following: `https://run.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/jobs/JOB_NAME:run`

To learn about the difference between Cloud Run service and job resources, see [Services, jobs, worker pools, and instances: four ways to run your code](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run#services-and-jobs).

  * Pub/Sub




### Unsupported targets

When Cloud Scheduler is a restricted service in your VPC Service Controls perimeter, any attempt to create or update a job with an unsupported target will fail with a `TARGET_TYPE_NOT_PERMITTED_FOR_VPC` error code. This action does _not_ generate a violation log when using [dry run mode](https://docs.cloud.google.com/vpc-service-controls/docs/dry-run-mode).

Custom domains (such as external application load balancers or custom DNS) for serverless endpoints are not supported targets. Runtime invocations to custom domains are blocked by the destination service due to missing in-perimeter credentials, even for pre-existing jobs created before the perimeter enrollment.

To avoid unexpectedly blocking your workloads, delete any jobs with unsupported targets or with targets outside of the VPC Service Controls perimeter you plan to use, before moving your perimeter to [enforced mode](https://docs.cloud.google.com/vpc-service-controls/docs/manage-dry-run-configurations#enforce-configuration).

## Delete non-compliant jobs

Recommended. Delete Cloud Scheduler jobs with targets that are either:

  * Unsupported (see Supported targets)
  * Outside of the VPC Service Controls perimeter you plan to use



For instructions on deleting jobs, see [Delete a job](https://docs.cloud.google.com/scheduler/docs/creating#delete).

If you don't delete these jobs before adding Cloud Scheduler to your VPC Service Controls perimeter, the jobs continue to run, but VPC Service Controls is not enforced on them. In this document, see Enforced actions.

For example, if you have a Cloud Scheduler job that targets an unsupported target (such as an arbitrary HTTP endpoint), the job continues to run after you add Cloud Scheduler to your VPC Service Controls perimeter, but it is not protected by VPC Service Controls. The same is true for a pre-existing job with a target outside of your VPC Service Controls perimeter. However, if a pre-existing job targets a serverless custom domain inside your perimeter, the destination service blocks runtime invocations.

## Add required IAM roles

Required. In order to use VPC Service Controls, the Cloud Scheduler service account must have the **Cloud Scheduler Service Agent** IAM role. The Cloud Scheduler service account is created for your project automatically. To verify that it has the Cloud Scheduler Service Agent IAM role, or to grant this role, take the following steps:

  1. In the Google Cloud console, go to **IAM**.

[Go to IAM](https://console.cloud.google.com/iam-admin)

  2. Select the **Include Google-provided role grants** checkbox.

  3. In the filter, type **Cloud Scheduler Service Account** , and select this principal.

  4. Look at the **Role** column for the **Cloud Scheduler Service Account** principal. You can proceed if the following role is listed:

     * **Cloud Scheduler Service Agent**

If the Cloud Scheduler Service Agent role is not listed, click the **Edit** icon and grant the **Cloud Scheduler Service Agent** role to the Cloud Scheduler Service Account principal.




## Specify a VPC Service Controls perimeter

Required. You can use an existing perimeter or create a new perimeter to protect your Cloud Scheduler jobs that have supported targets. Both approaches give you the chance to specify services to restrict. Specify the **Cloud Scheduler API**.

  * **Existing perimeters:** To update an existing VPC Service Controls perimeter to include Cloud Scheduler, follow the steps to [update a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#update).

  * **New perimeters:** To create a new perimeter for Cloud Scheduler, follow the steps to [create a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters).




## Enforce VPC Service Controls on pre-existing jobs

Recommended. To enforce VPC Service Controls on Cloud Scheduler jobs that you created before you added Cloud Scheduler to your VPC Service Controls perimeter, run an `update` on the job. You don't have to change the job, but you must run the update for VPC Service Controls to apply to the job and its future executions.

You can run an update for the job using the Google Cloud console (select the job and click **Edit**), the API, or the gcloud CLI.

To enforce VPC Service Controls on a pre-existing job by using the gcloud CLI, run the following:

### HTTP targets
    
    
    gcloud scheduler jobs update http JOB_ID

Replace `JOB_ID` with the ID of your job.

### Pub/Sub targets
    
    
    gcloud scheduler jobs update pubsub JOB_ID

Replace `JOB_ID` with the ID of your job.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
