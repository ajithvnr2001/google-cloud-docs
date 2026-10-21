---
url: https://docs.cloud.google.com/batch/docs/create-run-job-using-terraform-and-cloud-scheduler/
title: Create and run Batch jobs using Terraform and Cloud Scheduler \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:28:28.147349+00:00
---

# Create and run Batch jobs using Terraform and Cloud Scheduler  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/create-run-job-using-terraform-and-cloud-scheduler/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Guides ](https://docs.cloud.google.com/batch/docs/get-started)



Send feedback 

#  Create and run Batch jobs using Terraform and Cloud Scheduler Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial explains how you can use Terraform to create and run Batch jobs by using a Cloud Scheduler cron job.

[Terraform](https://registry.terraform.io/) is an open-source tool that lets you provision and manage infrastructure by specifying the desired state in configuration files. These files that can be treated as code and stored in version control systems like GitHub.

Although Terraform doesn't have resources for Batch, this tutorial shows how you can use Terraform to create Batch jobs. Specifically, you can use Terraform to schedule and run a Cloud Scheduler cron job that targets the Batch API to create and run Batch jobs. [Cloud Scheduler](https://docs.cloud.google.com/scheduler) is a Google Cloud service that allows you to automatically schedule cron jobs and supports Terraform.

This tutorial is intended for Batch users who already manage infrastructure with Terraform and want to incorporate Batch jobs into Terraform.

## Objectives

  * Create a Terraform directory and a configuration file that defines a Cloud Scheduler cron job that creates Batch jobs.
  * Deploy the Terraform configuration to run the cron job.
  * Verify that the cron job creates Batch jobs.
  * Update the Terraform configuration to pause the cron job so that it stops creating Batch jobs.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [ Batch](https://docs.cloud.google.com/batch/pricing)
  * [ Cloud Scheduler](https://docs.cloud.google.com/scheduler/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  1. Prepare your development environment, either Cloud Shell or a local shell:

### Cloud Shell

To use an online terminal with the gcloud CLI and Terraform already set up, activate Cloud Shell.

At the bottom of this page, a Cloud Shell session starts and displays a command-line prompt. It can take a few seconds for the session to initialize.

### Local shell

To use a local development environment, follow these steps:

     1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  4. [Install Terraform](https://developer.hashicorp.com/terraform/tutorials/gcp-get-started/install-cli).


* [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

  * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
  * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

  * Create a Google Cloud project:
        
        gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

  * Select the Google Cloud project that you created:
        
        gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.



* [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

* Enable the Batch, Compute Engine, Cloud Logging, Cloud Scheduler, and Resource Manager APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
    
    
    gcloud services enable batch.googleapis.com compute.googleapis.com logging.googleapis.com cloudscheduler.googleapis.com cloudresourcemanager.googleapis.com

* Make sure that your project has at least one [service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) with the permissions required for this tutorial.

**Note:** If you are using a new project, this step is not required [unless your organization prevents automatic role grants for default service accounts](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts#automatic-role-grants). By default, the Compute Engine default service account is automatically granted the Editor (`roles/editor`) IAM role, which already has all the permissions required for this tutorial. 

Specifically, you can use either the same service account or two separate service accounts to grant the following permissions:

  * Allow the cron job to create Batch jobs and attach the service account for the Batch jobs.
  * Allow the Batch jobs to create and access the resources required to run.



To ensure that the service account(s) for this tutorial has the necessary permissions to use Terraform to create Batch jobs through a Cloud Scheduler cron job, ask your administrator to grant the following IAM roles to the service account(s) for this tutorial: 

**Important:** You must grant these roles to the service account(s) for this tutorial, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * Service account for the Cloud Scheduler cron job: 
    * [Batch Job Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.jobsEditor) (`roles/batch.jobsEditor`) on the project
    * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service account for the Batch jobs (even if it's itself)
  * Service account for the Batch jobs: 
    * [Batch Agent Reporter ](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.agentReporter) (`roles/batch.agentReporter`) on the project
    * [Logs Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter) (`roles/logging.logWriter`) on the project



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give the service account(s) for this tutorial the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

* Make sure that you have the permissions required for this tutorial.

**Note:** If you created this project, this step is not required. As the project creator, you are automatically granted the Owner (`roles/owner`) IAM role, which already has all the permissions required for this tutorial. 

Specifically, you need permissions to do the following:

  * Create a cron job and attach the service account for the cron job.
  * View and delete the cron job and Batch jobs. 



To get the permissions that you need to use Terraform to create Batch jobs through a Cloud Scheduler cron job, ask your administrator to grant you the following IAM roles: 

  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service account for the Cloud Scheduler cron job
  * [Cloud Scheduler Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudscheduler#cloudscheduler.admin) (`roles/cloudscheduler.admin`) on the project
  * [Batch Job Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/batch#batch.jobsEditor) (`roles/batch.jobsEditor`) on the project
  * [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) on the project



## Create the Terraform directory and configuration file

Create a directory for Terraform and a configuration file that defines the resources that you want create or update using Terraform. The example configuration file for this tutorial defines a Cloud Scheduler cron job named `batch-job-invoker`. When it is enabled, the `batch-job-invoker` cron job runs every 5 minutes to create a new instance of the defined Batch job.

  1. To create a directory and a new Terraform configuration (`.tf`) file within that directory, type the following command, and then press `Enter`:
         
         mkdir terraform && cd terraform && cat > main.tf
         

This command creates the `terraform` directory, navigates you to it, and starts defining a new `main.tf` configuration file on the next line.

  2. Copy and paste the following Terraform configuration:
         
         # define variables
         variable "project_id" {
           type        = string
           description = "The project name to use."
           default = "PROJECT_ID"
         }
         
         variable "project_number" {
           type        = string
           description = "The project number to use."
           default = "PROJECT_NUMBER"
         }
         
         variable "region" {
           type        = string
           description = "The region where resources are created."
           default = "us-central1"
         }
         
         variable "cloud_scheduler_service_account_email" {
           type        = string
           description = "The service account email."
           default = "CLOUD_SCHEDULER_SERVICE_ACCOUNT_EMAIL"
         }
         
         variable "batch_service_account_email" {
           type        = string
           description = "The service account email."
           default = "BATCH_SERVICE_ACCOUNT_EMAIL"
         }
         
         # define a Cloud Scheduler cron job which triggers Batch jobs
         resource "google_cloud_scheduler_job" "batch-job-invoker" {
           paused           = false # this cron job is enabled
           name             = "batch-job-invoker"
           project          = var.project_id
           region           = var.region
           schedule         = "*/5 * * * *" # when enabled, run every 5 minutes
           time_zone        = "America/Los_Angeles"
           attempt_deadline = "180s"
         
           retry_config {
             max_doublings        = 5
             max_retry_duration   = "0s"
             max_backoff_duration = "3600s"
             min_backoff_duration = "5s"
           }
         
           # when this cron job runs, create and run a Batch job
           http_target {
             http_method = "POST"
             uri = "https://batch.googleapis.com/v1/projects/${var.project_id}/locations/${var.region}/jobs"
             headers = {
               "Content-Type" = "application/json"
               "User-Agent"   = "Google-Cloud-Scheduler"
             }
             # Batch job definition
             body = base64encode(<<EOT
             {
               "taskGroups":[
                 {
                   "taskSpec": {
                     "runnables":{
                       "script": {
                         "text": "echo Hello world! This job was created using Terraform and Cloud Scheduler."
                       }
                     }
                   }
                 }
               ],
               "allocationPolicy": {
                 "serviceAccount": {
                   "email": "${var.batch_service_account_email}"
                 }
               },
               "labels": {
                 "source": "terraform_and_cloud_scheduler_tutorial"
               },
               "logsPolicy": {
                 "destination": "CLOUD_LOGGING"
               }
             }
             EOT
             )
             oauth_token {
               scope                 = "https://www.googleapis.com/auth/cloud-platform"
               service_account_email = var.cloud_scheduler_service_account_email
             }
           }
         }
         
         

Replace the following:

     * `PROJECT_ID`: the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your project.
     * `PROJECT_NUMBER`: the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of your project.
     * `CLOUD_SCHEDULER_SERVICE_ACCOUNT_EMAIL`: the email address of the service account that you prepared for the Cloud Scheduler cron job.

For example, to use the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account), specify the following:
           
           PROJECT_NUMBER-compute@developer.gserviceaccount.com
           

     * `BATCH_SERVICE_ACCOUNT_EMAIL`: the email address of the service account that you prepared for Batch jobs.

For example, to use the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account), specify the following:
           
           PROJECT_NUMBER-compute@developer.gserviceaccount.com
           

This Terraform configuration defines some input variables and a cron job that contacts the API method for creating a Batch job.

**Objective:** If you want to learn more about how this Terraform configuration is defined and how to write your own, see the following pages: 
     * To learn more about the fields that define variables, see the documentation for [Terraform input variables](https://developer.hashicorp.com/terraform/language/values/variables).
     * To learn more about the fields that define the cron job, see the documentation for the [`google_cloud_scheduler_job` Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_scheduler_job).
     * To learn more about the fields that request to create a Batch job, see the documentation for the [`jobs.create` Batch API method](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs/create).
  3. To save and close the file, press `Ctrl+D` (or `Command+D` on macOS).




## Deploy the Terraform configuration to create the cron job

Deploy the Terraform configuration by initializing Terraform, generating the planned changes, and applying these changes. After deploying the Terraform configuration, you can describe the resources in your project to verify that Terraform successfully created the `batch-job-invoker` cron job.

  1. Initialize Terraform in the directory:
         
         terraform init
         

The output is similar to the following:
         
         ...
         Terraform has been successfully initialized!
         
         You may now begin working with Terraform. Try running "terraform plan" to see
         any changes that are required for your infrastructure. All Terraform commands
         should now work.
         
         If you ever set or change modules or backend configuration for Terraform,
         rerun this command to reinitialize your working directory. If you forget, other
         commands will detect it and remind you to do so if necessary.
         

  2. Generate the Terraform execution plan based on the current state of your project and the configuration file:
         
         terraform plan
         

The output is similar to the following, which shows that the plan is to create the `batch-job-invoker` cron job:
         
         Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
           + create
         
         Terraform will perform the following actions:
         
           # google_cloud_scheduler_job.batch-job-invoker will be created
           + resource "google_cloud_scheduler_job" "batch-job-invoker" {
               + id        = (known after apply)
               + name      = "batch-job-invoker"
               + paused    = false
               + project   = "PROJECT_ID"
               + region    = "us-central1"
               + schedule  = "*/5 * * * *"
               + state     = (known after apply)
               + time_zone = "America/Los_Angeles"
         
               + http_target {
                   + body        = "..."
                   + headers     = {
                       + "Content-Type" = "application/json"
                       + "User-Agent"   = "Google-Cloud-Scheduler"
                     }
                   + http_method = "POST"
                   + uri         = "https://batch.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/jobs"
         
                   + oauth_token {
                       + scope                 = "https://www.googleapis.com/auth/cloud-platform"
                       + service_account_email = "CLOUD_SCHEDULER_SERVICE_ACCOUNT_EMAIL"
                     }
                 }
         
               + retry_config {
                   + max_backoff_duration = "3600s"
                   + max_doublings        = 5
                   + max_retry_duration   = "0s"
                   + min_backoff_duration = "5s"
                   + retry_count          = (known after apply)
                 }
             }
         
         Plan: 1 to add, 0 to change, 0 to destroy.
         
         ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
         
         Note: You didn't use the -out option to save this plan, so Terraform can't guarantee to take exactly these actions if you run "terraform apply" now.
         

  3. To apply the plan to create the `batch-job-invoker` cron job, follow these steps:

     1. Enter the following command:
            
            terraform apply
            

The output is similar to the previous `terraform plan` command except that it ends with a confirmation prompt.

     2. To confirm and apply the plan, enter `yes`.

The output is similar to the following:
            
            google_cloud_scheduler_job.batch-job-invoker: Creating...
            google_cloud_scheduler_job.batch-job-invoker: Creation complete after 0s [id=projects/PROJECT_ID/locations/us-central1/jobs/batch-job-invoker]
            
            Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
            

  4. To verify that the `batch-job-invoker` cron job exists and is enabled, describe it:
         
         gcloud scheduler jobs describe batch-job-invoker --location us-central1
         

The output is similar to the following:
         
         attemptDeadline: 180s
         httpTarget:
           body: ...
           headers:
             Content-Type: application/json
             User-Agent: Google-Cloud-Scheduler
           httpMethod: POST
           oauthToken:
             scope: https://www.googleapis.com/auth/cloud-platform
             serviceAccountEmail: CLOUD_SCHEDULER_SERVICE_ACCOUNT_EMAIL
           uri: https://batch.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/jobs
         lastAttemptTime: '...'
         name: projects/PROJECT_ID/locations/us-central1/jobs/batch-job-invoker
         retryConfig:
           maxBackoffDuration: 3600s
           maxDoublings: 5
           maxRetryDuration: 0s
           minBackoffDuration: 5s
         schedule: '*/5 * * * *'
         scheduleTime: '...'
         state: ENABLED
         status: {}
         timeZone: America/Los_Angeles
         userUpdateTime: '...'
         

In the output, verify that the `state` field is set to `ENABLED`.




## Verify that the cron job creates a Batch job

Verify that the `batch-job-invoker` cron job is correctly creating Batch jobs.

  1. Either wait 5 minutes for the cron job to run automatically or trigger the cron job to run immediately:
         
         gcloud scheduler jobs run batch-job-invoker --location us-central1
         

  2. List the Batch jobs that have been created by the `batch-job-invoker` cron job:
         
         gcloud batch jobs list \
         --filter labels.source=\"terraform_and_cloud_scheduler_tutorial\" \
         --sort-by ~createTime
         

     * The `--filter labels.source=\"terraform_and_cloud_scheduler_tutorial\"` flag filters the list to only include Batch jobs that have a label with the key `source` and the value `terraform_and_cloud_scheduler_tutorial`.
     * The `--sort-by ~createTime` flag sorts the list from newest to oldest.



## Update the Terraform configuration to pause the cron job

After you have the desired number of Batch jobs, update and deploy the Terraform configuration to pause the `batch-job-invoker` cron job. If you want to update other properties of the cron job or future Batch jobs, this same process applies.

**Note:** For recurring workloads, you don't need to pause the Cloud Scheduler cron job if you want to continue to automatically create Batch jobs. For example, you could configure the [cron job schedule](https://docs.cloud.google.com/scheduler/docs/configuring/cron-job-schedules) to run a Batch job on the first day of each month.

  1. Update the Terraform configuration file to pause the cron job by setting the `paused` field to `true`:
         
         sed -i 's/paused           = false # this cron job is enabled/paused           = true # this cron job is paused/g' main.tf
         

  2. Generate the Terraform execution plan based on the current state of your project and the configuration file:
         
         terraform plan
         

The output is similar to the following, which shows that the plan is to update the value of `paused` field from `false` to `true`:
         
         google_cloud_scheduler_job.batch-job-invoker: Refreshing state... [id=projects/PROJECT_ID/locations/us-central1/jobs/batch-job-invoker]
         
         Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
           ~ update in-place
         
         Terraform will perform the following actions:
         
           # google_cloud_scheduler_job.batch-job-invoker will be updated in-place
           ~ resource "google_cloud_scheduler_job" "batch-job-invoker" {
                 id               = "projects/PROJECT_ID/locations/us-central1/jobs/batch-job-invoker"
                 name             = "batch-job-invoker"
               ~ paused           = false -> true
                 # (6 unchanged attributes hidden)
         
               ~ http_target {
                   ~ headers     = {
                       + "User-Agent"   = "Google-Cloud-Scheduler"
                         # (1 unchanged element hidden)
                     }
                     # (3 unchanged attributes hidden)
         
                     # (1 unchanged block hidden)
                 }
         
                 # (1 unchanged block hidden)
             }
         
         Plan: 0 to add, 1 to change, 0 to destroy.
         
         ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
         
         Note: You didn't use the -out option to save this plan, so Terraform can't guarantee to take exactly these actions if you run "terraform apply" now.
         

  3. To apply the plan to update the `batch-job-invoker` cron job, follow these steps:

     1. Enter the following command:
            
            terraform apply
            

The output is similar to the previous `terraform plan` command except that it ends with a confirmation prompt.

     2. To confirm and apply the plan, enter `yes`.

The output is similar to the following:
            
            google_cloud_scheduler_job.batch-job-invoker: Modifying... [id=projects/PROJECT_ID/locations/us-central1/jobs/batch-job-invoker]
            google_cloud_scheduler_job.batch-job-invoker: Modifications complete after 1s [id=projects/PROJECT_ID/locations/us-central1/jobs/batch-job-invoker]
            
            Apply complete! Resources: 0 added, 1 changed, 0 destroyed.
            

  4. To verify that the `batch-job-invoker` cron job is paused, describe it:
         
         gcloud scheduler jobs describe batch-job-invoker --location us-central1
         

The output is similar to the following:
         
         attemptDeadline: 180s
         httpTarget:
           body: ...
           headers:
             Content-Type: application/json
             User-Agent: Google-Cloud-Scheduler
           httpMethod: POST
           oauthToken:
             scope: https://www.googleapis.com/auth/cloud-platform
             serviceAccountEmail: CLOUD_SCHEDULER_SERVICE_ACCOUNT_EMAIL
           uri: https://batch.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/jobs
         lastAttemptTime: '...'
         name: projects/PROJECT_ID/locations/us-central1/jobs/batch-job-invoker
         retryConfig:
           maxBackoffDuration: 3600s
           maxDoublings: 5
           maxRetryDuration: 0s
           minBackoffDuration: 5s
         schedule: '*/5 * * * *'
         scheduleTime: '...'
         state: PAUSED
         status: {}
         timeZone: America/Los_Angeles
         userUpdateTime: '...'
         

In the output, verify that the `state` field is set to `PAUSED`.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

  1. **Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID

  2. Go to the parent directory, and then delete the Terraform directory and all of its files.
         
         cd .. && rm -r terraform
         




### Delete individual resources

  1. Delete the `batch-job-invoker` cron job.

**Note:** For this tutorial, it's easiest to use the following [`terraform destroy` command](https://developer.hashicorp.com/terraform/cli/commands/destroy), which deletes all the resources managed by the Terraform configuration file. However, if a Terraform configuration file has other resources that you don't want to delete, update the Terraform configuration instead.
         
         terraform destroy
         

  2. To delete all the Batch jobs from this tutorial, follow these steps:

     1. List all the Batch jobs that were created by the `batch-job-invoker` cron job:
            
            gcloud batch jobs list \
            --filter labels.source=\"terraform_and_cloud_scheduler_tutorial\" \
            --sort-by ~createTime
            

Record the name of each job that you need to delete.

     2. Delete a Batch job from this tutorial:
            
            gcloud batch jobs delete JOB_NAME --location us-central1
            

Replace `JOB_NAME` with the name of a Batch job.

Repeat this step for all the Batch jobs.

  3. If you created a service account for this tutorial, delete the service account:
         
         gcloud iam service-accounts delete SERVICE_ACCOUNT_EMAIL
         

Replace `SERVICE_ACCOUNT_EMAIL` with the email address of a service account that you created for this tutorial. Namely, you used the following service accounts:

     * `CLOUD_SCHEDULER_SERVICE_ACCOUNT_EMAIL`: the service account for Cloud Scheduler.
     * `BATCH_SERVICE_ACCOUNT_EMAIL`: the service account for Batch.

If you created two separate service accounts, repeat this step.

  4. Go to the parent directory, and then delete the Terraform directory and all of its files.
         
         cd .. && rm -r terraform
         




## What's next

  * Learn more about using Terraform with Google Cloud: 
    * [Terraform documentation for Google Cloud](https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/getting_started)
    * [Google Cloud documentation for Terraform](https://docs.cloud.google.com/docs/terraform)
  * Learn more about [Cloud Scheduler cron jobs](https://docs.cloud.google.com/scheduler/docs/creating).
  * Learn more about [Batch jobs](https://docs.cloud.google.com/batch/docs/create-run-job).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
