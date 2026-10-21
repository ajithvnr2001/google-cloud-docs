---
url: https://docs.cloud.google.com/scheduler/docs/schedule-run-cron-job-terraform/
title: Schedule and run a cron job using Terraform \u00a0|\u00a0 Cloud Scheduler \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:10:59.255444+00:00
---

# Schedule and run a cron job using Terraform  |  Cloud Scheduler  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/scheduler/docs/schedule-run-cron-job-terraform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Scheduler ](https://docs.cloud.google.com/scheduler/docs)
  * [ Guides ](https://docs.cloud.google.com/scheduler/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Schedule and run a cron job using Terraform

This quickstart shows you how to use Terraform to create a Cloud Scheduler cron job. Terraform is an infrastructure as code (IaC) tool that lets you predictably create, change, and improve your cloud infrastructure by using code. You can learn more about [using Terraform](https://docs.cloud.google.com/docs/terraform) to provision infrastructure on Google Cloud.

Cloud Scheduler has a free tier and running this quickstart shouldn't result in any costs. For more information, see [Pricing](https://cloud.google.com/scheduler/pricing).

In this quickstart, you:

  1. Use Terraform to create a cron job for Cloud Scheduler.
  2. Set a recurring schedule for the job.
  3. Specify a Pub/Sub topic as the job target.
  4. Run the job.
  5. Verify that the job has run successfully.



## Before you begin

Security constraints defined by your organization might prevent you from completing the following steps. For troubleshooting information, see [Develop applications in a constrained Google Cloud environment](https://docs.cloud.google.com/resource-manager/docs/organization-policy/develop-apps-constrained-environment). 

  1. [ Sign in](https://accounts.google.com/Login) to your Google Account.

If you don't already have one, [ sign up for a new account](https://accounts.google.com/SignUp).

  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

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

  6. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  7. Enable the Resource Manager and Service Usage APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable cloudresourcemanager.googleapis.com serviceusage.googleapis.com

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

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

  12. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  13. Enable the Resource Manager and Service Usage APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable cloudresourcemanager.googleapis.com serviceusage.googleapis.com

  14. Cloud Shell has Terraform already integrated. If you need to install Terraform, see the [HashiCorp Terraform documentation](https://developer.hashicorp.com/terraform/tutorials/gcp-get-started/install-cli).



### Required roles

To get the permissions that you need to complete this quickstart, ask your administrator to grant you the following IAM roles on your project: 

  * [Cloud Scheduler Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudscheduler#cloudscheduler.admin) (`roles/cloudscheduler.admin`)
  * [Pub/Sub Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.editor) (`roles/pubsub.editor`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a Terraform configuration file

To use Terraform with Cloud Scheduler, you need to create a configuration file to describe your infrastructure and create an execution plan. You then apply the configuration file to your platform or service to perform operations that provision your infrastructure.

Complete the following steps to create a Terraform configuration file called `main.tf`:

  1. Open a terminal and create a directory:
         
         mkdir terraform

  2. Go to the `terraform` directory:
         
         cd terraform

  3. Add a new file, `main.tf`, to the directory:
         
         nano main.tf

  4. Add the following [Terraform provider for Google Cloud](https://registry.terraform.io/providers/hashicorp/google/latest/docs) resources to the `main.tf` file:

     1. Enable the Cloud Scheduler and Pub/Sub APIs:
            
            # Enable Cloud Scheduler API
            resource "google_project_service" "scheduler" {
              service            = "cloudscheduler.googleapis.com"
              disable_on_destroy = false
            }
            # Enable Pub/Sub API
            resource "google_project_service" "pubsub" {
              service            = "pubsub.googleapis.com"
              disable_on_destroy = false
            }

     2. Create a Pub/Sub topic as a resource to which messages can be sent by publishers:
            
            # Create Pub/Sub topic
            resource "google_pubsub_topic" "default" {
              name = "pubsub_topic"
            }

This creates a topic called `pubsub_topic`.

     3. Create a subscription to receive messages published to the Pub/Sub topic:
            
            # Create Pub/Sub subscription
            resource "google_pubsub_subscription" "default" {
              name  = "pubsub_subscription"
              topic = google_pubsub_topic.default.name
            }

     4. Create a cron job using the [`google_cloud_scheduler_job`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_scheduler_job) resource:
            
            # Create a cron job using Cloud Scheduler
            resource "google_cloud_scheduler_job" "default" {
              name        = "test-job"
              description = "test job"
              schedule    = "30 16 * * 7"
              region      = "us-east1"
            
              pubsub_target {
                topic_name = google_pubsub_topic.default.id
                data       = base64encode("Hello world!")
              }
            }

The following arguments are used in the sample:

        * `name`: the name of the job.
        * `description`: a description for the job.
        * `schedule`: the frequency for the job, using a format based on unix-cron.

In this sample, `30 16 * * 7` means that the job will run at 16:30 on Sundays. For more information, see [Cron job format and time zone](https://docs.cloud.google.com/scheduler/docs/configuring/cron-job-schedules).

        * `region`: the region where the job resides.

        * `pubsub_target`: the Pub/Sub topic target, including the full resource name of the topic (`topic_name`) to which the message payload (`data`) is published when the job is run.

Other arguments are supported. For details, see the [Terraform Registry argument reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_scheduler_job#argument-reference).




For another example of using Terraform with Cloud Scheduler, see [Running Cloud Run services on a schedule](https://docs.cloud.google.com/run/docs/triggering/using-scheduler).

## Create the cron job

Deploy your Terraform resources to create the cron job.

  1. Open a terminal and in the `terraform` directory, initialize Terraform:
         
         terraform init

  2. Check that the changes you propose with Terraform match the expected plan:
         
         terraform plan

You can ignore the note regarding not using the `-out` option.

  3. Create the cron job:
         
         terraform apply

  4. At the **Enter a value** prompt, type `yes` to proceed with the creation of resources.

  5. Confirm that a job is created:
         
         gcloud scheduler jobs describe test-job --location=us-east1

The output should be similar to the following:
         
         description: test job
         lastAttemptTime: '2024-04-04T13:56:00.669530Z'
         name: projects/PROJECT_ID/locations/us-east1/jobs/test-job
         pubsubTarget:
         data: dGVzdA==
         topicName: projects/PROJECT_ID/topics/pubsub_topic
         schedule: '30 16 * * 7'
         scheduleTime: '2024-04-04T13:58:00.737907Z'
         state: ENABLED




You've created a job that sends a message to a Pub/Sub topic at 16:30 on Sundays. You can now run the job.

## Run your job

In addition to executing according to its specified schedule, you can force your job to execute immediately by running the following command.
    
    
    gcloud scheduler jobs run test-job --location=us-east1

Note that due to some initial configuration, the first job created in a project can take a few minutes to run.

## Verify the results

Verify that your Pub/Sub topic is receiving messages from your job.

  1. Pull Pub/Sub messages from a subscription:
         
         gcloud pubsub subscriptions pull pubsub_subscription --limit 5
         

If there are no messages pulled initially, run the command again.

  2. View the results of running your job. The output should look similar to the following:
         
         DATA: Hello world!
         MESSAGE_ID: 5028933846601543
         ORDERING_KEY:
         ATTRIBUTES:
         DELIVERY_ATTEMPT:
         ACK_ID: RFAGFixdRkhRNxkIaFEOT14jPzUgKEUQAgVPAihdeTFXLkFacGhRDRlyfWB9[...]
         




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, delete the Google Cloud project with the resources. 

  1. Deleting your Google Cloud project stops billing for all the resources used within that project. Note that by default, any files in your Cloud Shell home directory (for example, any Terraform files) persist between sessions. **Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID

  2. Alternatively, you can delete all the resources you created with Terraform.

The `terraform destroy` command terminates all the resources specified in your [Terraform state](https://developer.hashicorp.com/terraform/language/state). It doesn't destroy resources that aren't managed by the current Terraform project. Your Terraform configuration file is not destroyed. For more information, see [Destroy infrastructure](https://developer.hashicorp.com/terraform/tutorials/gcp-get-started/google-cloud-platform-destroy).
         
         terraform destroy




## What's next

  * [What is Terraform?](https://developer.hashicorp.com/terraform/intro)
  * [Viewing Cloud Scheduler logs](https://docs.cloud.google.com/scheduler/docs/viewing-logs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
