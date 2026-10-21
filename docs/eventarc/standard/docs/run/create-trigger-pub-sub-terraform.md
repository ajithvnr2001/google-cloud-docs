---
url: https://docs.cloud.google.com/eventarc/standard/docs/run/create-trigger-pub-sub-terraform/
title: Quickstart: Receive events using Pub/Sub messages (Terraform) \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:25:33.428509+00:00
---

# Quickstart: Receive events using Pub/Sub messages (Terraform)  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/standard/docs/run/create-trigger-pub-sub-terraform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Receive events using Pub/Sub messages (Terraform)

[ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

This quickstart shows you how to use Terraform to create an Eventarc trigger that receives direct events from Pub/Sub and routes the events to a Cloud Run service. For more information about using Terraform to create Eventarc triggers, see [Create a trigger using Terraform](https://docs.cloud.google.com/eventarc/docs/creating-triggers-terraform).

In this quickstart, you will do the following:

  1. Prepare to deploy Terraform.

  2. Define a Terraform configuration that does the following:

     1. Enable APIs.
     2. Create a service account.
     3. Create a Pub/Sub topic as an event provider.
     4. Deploy a service to Cloud Run as an event destination.
     5. Create an Eventarc trigger.
  3. Apply your Terraform configuration.




This lets you generate an event by publishing a message to the Pub/Sub topic. The Eventarc trigger routes the message to the event receiver service deployed on Cloud Run, and the service logs the event message, providing you with a straightforward example of an [event-driven architecture](https://docs.cloud.google.com/eventarc/standard/docs/event-driven-architectures).

## Before you begin

Security constraints defined by your organization might prevent you from completing the following steps. For troubleshooting information, see [Develop applications in a constrained Google Cloud environment](https://docs.cloud.google.com/resource-manager/docs/organization-policy/develop-apps-constrained-environment). 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
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

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Cloud Resource Manager and Identity and Access Management (IAM) APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable cloudresourcemanager.googleapis.com iam.googleapis.com

  8. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

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

  13. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  14. Enable the Cloud Resource Manager and Identity and Access Management (IAM) APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable cloudresourcemanager.googleapis.com iam.googleapis.com

  15. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  16. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

#### Required permissions

To get the permissions that you need to complete this quickstart, ask your administrator to grant you the following IAM roles on your project: 

     * [Cloud Run Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`)
     * [Eventarc Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.admin) (`roles/eventarc.admin`)
     * [Logs View Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewAccessor) (`roles/logging.viewAccessor`)
     * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
     * [Pub/Sub Publisher ](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.publisher) (`roles/pubsub.publisher`)
     * [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`)
     * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




## Prepare to deploy Terraform

Before deploying any Terraform resources, you must create a Terraform configuration file. A Terraform configuration file lets you define your preferred end state for your infrastructure using the Terraform syntax.

  1. If you are using a local shell, [install Terraform](https://docs.cloud.google.com/docs/terraform/install-configure-terraform).

Terraform is already integrated into the Cloud Shell environment and you can use Cloud Shell to deploy your Terraform resources without having to install Terraform.

  2. In Cloud Shell or your local shell, set the default Google Cloud project where you want to apply your Terraform configuration. You need to run this command only once per project, and you can run it in any directory:
         
         export GOOGLE_CLOUD_PROJECT=PROJECT_ID

Replace `PROJECT_ID` with the ID of your Google Cloud project.

Note that environment variables are overridden if you set explicit values in the Terraform configuration file.

  3. Each Terraform configuration file must have its own directory (also called a _root module_). Create a directory and a new file within that directory:
         
         mkdir DIRECTORY && cd DIRECTORY && touch main.tf

Replace `DIRECTORY` with the name of your Terraform directory.

The filename must have the `.tf` extension—for example, in this quickstart, the configuration file is `main.tf`.




## Define your Terraform configuration

Copy the following Terraform code snippets into your `main.tf` file. Or, to copy the entire code sample from GitHub, in the top right corner of a code snippet, click more_vert> **View on GitHub**.

### Enable APIs

To enable the APIs required to apply the Terraform configuration, use the [`google_project_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/google_project_service) Terraform resource:
    
    
    # Enable Cloud Run API
    resource "google_project_service" "run" {
      service            = "run.googleapis.com"
      disable_on_destroy = false
    }
    
    # Enable Eventarc API
    resource "google_project_service" "eventarc" {
      service            = "eventarc.googleapis.com"
      disable_on_destroy = false
    }
    
    # Enable Pub/Sub API
    resource "google_project_service" "pubsub" {
      service            = "pubsub.googleapis.com"
      disable_on_destroy = false
    }

### Create a service account

Every Eventarc trigger is associated with an IAM service account. To create a dedicated service account for testing purposes, use the [`google_service_account`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/google_service_account) Terraform resource:
    
    
    # Create a dedicated service account
    resource "google_service_account" "eventarc" {
      account_id   = "eventarc-trigger-sa"
      display_name = "Eventarc trigger service account"
    }

If you enabled the Pub/Sub service agent on or before April 8, 2021, grant the [Service Account Token Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountTokenCreator) role (`roles/iam.serviceAccountTokenCreator`) to the service agent.
    
    
    resource "google_project_iam_member" "tokencreator" {
      project  = data.google_project.project.id
      role     = "roles/iam.serviceAccountTokenCreator"
      member   = "serviceAccount:service-${data.google_project.project.number}@gcp-sa-pubsub.iam.gserviceaccount.com"
    }

### Create a Pub/Sub topic as an event provider

To create a Pub/Sub topic, use the [`google_pubsub_topic`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/pubsub_topic) Terraform resource. To grant your service account the [Pub/Sub Publisher](https://docs.cloud.google.com/iam/docs/roles-permissions/pubsub#pubsub.publisher) role (`roles/pubsub.publisher`) at the topic level, use the [`google_pubsub_topic_iam_member`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/pubsub_topic_iam) Terraform resource:
    
    
    # Create a Pub/Sub topic
    resource "google_pubsub_topic" "default" {
      name = "pubsub_topic"
    }
    
    # Grant permission to publish messages to a Pub/Sub topic
    resource "google_pubsub_topic_iam_member" "pubsubpublisher" {
      project    = google_pubsub_topic.default.project
      topic      = google_pubsub_topic.default.name
      member     = "serviceAccount:${google_service_account.eventarc.email}"
      role       = "roles/pubsub.publisher"
      depends_on = [google_pubsub_topic.default]
    }

### Deploy an event receiver to Cloud Run

To create a Cloud Run service as an event destination, use the [`google_cloud_run_v2_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service) Terraform resource. To grant your service account the [Cloud Run Invoker](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.invoker) role (`roles/run.invoker`) at the service level, use the [`google_cloud_run_v2_service_iam_member`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service_iam) Terraform resource:
    
    
    # Deploy a Cloud Run service
    resource "google_cloud_run_v2_service" "default" {
      name     = "hello-events"
      location = "us-central1"
    
      deletion_protection = false # set to "true" in production
    
      template {
        containers {
          # This sample container listens to HTTP requests and logs received events
          image = "us-docker.pkg.dev/cloudrun/container/hello"
        }
        service_account = google_service_account.eventarc.email
      }
    
      depends_on = [google_project_service.run]
    }
    
    # Grant permission to invoke Cloud Run services
    resource "google_cloud_run_v2_service_iam_member" "runinvoker" {
      project    = google_cloud_run_v2_service.default.project
      location   = google_cloud_run_v2_service.default.location
      name       = google_cloud_run_v2_service.default.name
      role       = "roles/run.invoker"
      member     = "serviceAccount:${google_service_account.eventarc.email}"
      depends_on = [google_cloud_run_v2_service.default]
    }

### Create an Eventarc trigger

To create an Eventarc trigger to listen for Pub/Sub messages, use the [`google_eventarc_trigger`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/eventarc_trigger) Terraform resource:
    
    
    # Create an Eventarc trigger, routing Pub/Sub events to Cloud Run
    resource "google_eventarc_trigger" "default" {
      name     = "trigger-pubsub-cloudrun-tf"
      location = google_cloud_run_v2_service.default.location
    
      # Capture messages published to a Pub/Sub topic
      matching_criteria {
        attribute = "type"
        value     = "google.cloud.pubsub.topic.v1.messagePublished"
      }
    
      # Send events to Cloud Run
      destination {
        cloud_run_service {
          service = google_cloud_run_v2_service.default.name
          region  = google_cloud_run_v2_service.default.location
        }
      }
    
      transport {
        pubsub {
          topic = google_pubsub_topic.default.id
        }
      }
    
      service_account = google_service_account.eventarc.email
      depends_on = [
        google_project_service.eventarc,
        google_pubsub_topic_iam_member.pubsubpublisher
      ]
    }

**Note:** Although your trigger is created immediately, it can take up to two minutes for triggers to be fully functional.

## Apply the Terraform configuration

Use the Terraform CLI to provision infrastructure based on the configuration file. For more information, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

  1. Initialize Terraform. You need to do this only once per directory.
         
         terraform init

Optionally, to use the latest Google provider version, include the `-upgrade` option:
         
         terraform init -upgrade

  2. Review the configuration and verify that the resources that Terraform will create or update match your expectations:
         
         terraform plan

Correct the configuration as necessary.

  3. Apply the Terraform configuration by running the following command and entering `yes` at the prompt:
         
         terraform apply

Typically, you apply the entire configuration at once. However, you can also target a specific resource. For example:
         
         terraform apply -target="google_eventarc_trigger.default"

After enabling the APIs, it might take a few minutes for the action to propagate before you can deploy any further resources. If you run into an issue, try applying the Terraform configuration again.

Wait until Terraform displays the "Apply complete!" message.




## Verify the creation of resources

  1. Confirm that the Cloud Run service has been created:
         
         gcloud run services list --region us-central1
         

The output should be similar to the following:
         
         SERVICE: hello-events
         REGION: us-central1
         URL: https://hello-events-13335919645.us-central1.run.app
         LAST DEPLOYED BY: ...
         LAST DEPLOYED AT: 2024-12-16T15:00:52.606160Z
         

  2. Confirm that the Eventarc trigger has been created:
         
         gcloud eventarc triggers list --location us-central1
         

The output should be similar to the following:
         
         NAME: trigger-pubsub-cloudrun-tf
         TYPE: google.cloud.pubsub.topic.v1.messagePublished
         DESTINATION: Cloud Run service: hello-events
         ACTIVE: Yes
         LOCATION: us-central1
         




## Generate and view a Pub/Sub topic event

You can generate an event by publishing a message to the Pub/Sub topic. The Eventarc trigger routes the message to the event receiver service deployed on Cloud Run and the service logs the event message.

  1. Find and set the Pub/Sub topic as an environment variable:
         
         gcloud config set eventarc/location us-central1
         export RUN_TOPIC=$(gcloud eventarc triggers describe trigger-pubsub-cloudrun-tf \
             --format='value(transport.pubsub.topic)')
         

  2. To generate an event, publish a message to the Pub/Sub topic:
         
         gcloud pubsub topics publish $RUN_TOPIC --message "Hello World!"
         

The event is routed to the Cloud Run service, which logs the event message.

  3. Filter the log entries created by your service:
         
         gcloud logging read 'jsonPayload.message: "Received event of type google.cloud.pubsub.topic.v1.messagePublished"'
         

  4. Look for a log entry similar to the following:
         
         jsonPayload:
         ...
         message: 'Received event of type google.cloud.pubsub.topic.v1.messagePublished.
             Event data: Hello World!'
         

**Note:** If you don't see a log entry, wait a few minutes and retry the `gcloud logging read` command.



You have successfully used Terraform to deploy an event receiver service to Cloud Run and create an Eventarc trigger. After generating an event from Pub/Sub, you can view it in the Cloud Run logs.

## Clean up

When you finish the tasks that are described in this quickstart, you can avoid continued billing by deleting the resources that you created.

Remove resources previously applied with your Terraform configuration by running the following command and entering `yes` at the prompt:
    
    
    terraform destroy

Alternatively, you can delete your Google Cloud project to avoid incurring charges. Deleting your Google Cloud project stops billing for all the resources used within that project.

**Caution** : Deleting a project has the following effects: 

  * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
  * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 



Delete a Google Cloud project:
    
    
    gcloud projects delete PROJECT_ID

If you plan to explore multiple tutorials and quickstarts, reusing projects can help you avoid exceeding project quota limits.

## What's next

  * [Develop services for Cloud Run](https://docs.cloud.google.com/run/docs/developing)
  * [Terraform on Google Cloud documentation](https://docs.cloud.google.com/docs/terraform)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
