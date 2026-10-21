---
url: https://docs.cloud.google.com/eventarc/advanced/docs/quickstarts/publish-events-google-api-source-terraform/
title: Quickstart: Publish and receive events by creating a bus and enrollment (Terraform) \u00a0|\u00a0 Eventarc Advanced \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:54:37.256655+00:00
---

# Quickstart: Publish and receive events by creating a bus and enrollment (Terraform)  |  Eventarc Advanced  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/advanced/docs/quickstarts/publish-events-google-api-source-terraform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/advanced/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Publish and receive events by creating a bus and enrollment (Terraform)

[ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs/overview)

This quickstart shows you how to use Terraform to create an Eventarc Advanced bus and enrollment in your Google Cloud project so that you can publish and receive event messages.

  * A _bus_ acts as a central router, receiving messages from event sources or published by providers.

  * An _enrollment_ routes messages received by the bus to one or more destinations through a processing _pipeline_.




In this quickstart, you:

  1. Deploy an event receiver service to Cloud Run.

  2. Create an Eventarc Advanced bus.

  3. Enable events from Google sources.

  4. Create an Eventarc Advanced pipeline and enrollment.

  5. Publish an event message to the bus by creating a workflow.

  6. View the event data in the Cloud Run logs.




You can complete most of the steps in this quickstart using Terraform. To complete all of the steps using the Google Cloud CLI, see [Publish events from a Google source](https://docs.cloud.google.com/eventarc/advanced/docs/quickstarts/publish-events-google-api-source).

For more information about using Terraform, see the [Terraform on Google Cloud](https://docs.cloud.google.com/docs/terraform) documentation.

## Before you begin

Security constraints defined by your organization might prevent you from completing the following steps. For troubleshooting information, see [Develop applications in a constrained Google Cloud environment](https://docs.cloud.google.com/resource-manager/docs/organization-policy/develop-apps-constrained-environment). 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Enable the Cloud Resource Manager and Identity and Access Management (IAM) APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudresourcemanager.googleapis.com,iam.googleapis.com&redirect=https%3A//cloud.google.com/eventarc/docs/run/create-trigger-storage-console)

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. Enable the Cloud Resource Manager and Identity and Access Management (IAM) APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudresourcemanager.googleapis.com,iam.googleapis.com&redirect=https%3A//cloud.google.com/eventarc/docs/run/create-trigger-storage-console)

  10. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

Terraform is integrated into the Cloud Shell environment and you can use Cloud Shell to deploy your Terraform resources without having to install Terraform.




### Required roles

To get the permissions that you need to complete this quickstart, ask your administrator to grant you the following IAM roles on your project: 

  * [Cloud Run Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`)
  * [Eventarc Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.developer) (`roles/eventarc.developer`)
  * [Eventarc Message Bus Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.messageBusAdmin) (`roles/eventarc.messageBusAdmin`)
  * [Logs View Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewAccessor) (`roles/logging.viewAccessor`)
  * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
  * [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
  * [Workflows Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/workflows#workflows.editor) (`roles/workflows.editor`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Prepare to deploy Terraform

Before deploying any Terraform resources, you must create a Terraform configuration file. A Terraform configuration file lets you define your preferred end state for your infrastructure using the Terraform syntax.

  1. In Cloud Shell, set the default Google Cloud project where you want to apply your Terraform configuration. You need to run this command only once per project, and you can run it in any directory:
         
         export GOOGLE_CLOUD_PROJECT=PROJECT_ID

Replace `PROJECT_ID` with the ID of your Google Cloud project.

Note that environment variables are overridden if you set explicit values in the Terraform configuration file.

  2. Each Terraform configuration file must have its own directory (also called a _root module_). In Cloud Shell, create a directory and a new file within that directory:
         
         mkdir DIRECTORY && cd DIRECTORY && touch main.tf

Replace `DIRECTORY` with the name of your Terraform directory.

The filename must have the `.tf` extension—for example, in this quickstart, the configuration file is `main.tf`.




## Define your Terraform configuration

Copy the following Terraform code snippets into your `main.tf` file. Or, to copy the entire code sample from GitHub, in the top right corner of a code snippet, click more_vert> **View on GitHub**.

### Enable APIs

Use the [`google_project_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/google_project_service) Terraform resource to enable the APIs required to apply the Terraform configuration:
    
    
    # Enable APIs
    resource "google_project_service" "apis" {
      for_each = toset([
        "eventarc.googleapis.com",
        "eventarcpublishing.googleapis.com",
        "run.googleapis.com"
      ])
      service            = each.key
      disable_on_destroy = false
    }

### Create a service account

For testing purposes, create a dedicated service account, and grant it specific IAM roles.

Use the [`google_service_account`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/google_service_account) and [`google_project_iam_member`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/google_project_iam#google_project_iam_member) Terraform resources to create the service account and grant it the necessary roles to publish and receive events:
    
    
    # Used to retrieve project information later
    data "google_project" "project" {}
    
    # Create a dedicated service account
    resource "google_service_account" "default" {
      account_id   = "eventarc-advanced-sa"
      display_name = "Eventarc Advanced quickstart service account"
    }
    
    # Grant permission to receive Eventarc events
    resource "google_project_iam_member" "eventreceiver" {
      project = data.google_project.project.id
      role    = "roles/eventarc.eventReceiver"
      member  = "serviceAccount:${google_service_account.default.email}"
    }
    
    # Grant permission to invoke Cloud Run services
    resource "google_project_iam_member" "runinvoker" {
      project = data.google_project.project.id
      role    = "roles/run.invoker"
      member  = "serviceAccount:${google_service_account.default.email}"
    }

### Create an event destination

Use the [`google_cloud_run_v2_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service) Terraform resource to create a [Cloud Run service](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run) as an event destination that logs the contents of an event:
    
    
    # Deploy Cloud Run service
    resource "google_cloud_run_v2_service" "default" {
      name     = "example-service"
      location = "us-central1"
    
      deletion_protection = false # set to "true" in production
    
      template {
        containers {
          # This sample container listens to HTTP requests and logs received events
          image = "us-docker.pkg.dev/cloudrun/container/hello"
        }
        service_account = google_service_account.default.email
      }
    
      depends_on = [google_project_service.apis]
    }

### Create an Eventarc Advanced bus

A bus receives event messages from a message source or published by a provider and acts as a message router. For more information, see [Create a bus to route messages](https://docs.cloud.google.com/eventarc/advanced/docs/publish-events/create-bus).

**Note:** You can create one bus per Google Cloud project per [supported region](https://docs.cloud.google.com/eventarc/docs/locations#advanced-regions).

Use the [`google_eventarc_message_bus`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/eventarc_message_bus) Terraform resource to create an Eventarc Advanced bus:
    
    
    # Create an Eventarc Advanced bus
    resource "google_eventarc_message_bus" "default" {
      location       = "us-central1"
      message_bus_id = "example-bus"
    }

### Enable events from Google sources

To publish events from Google sources, you must create a [`GoogleApiSource`](https://docs.cloud.google.com/eventarc/docs/reference/rest/v1/projects.locations.googleApiSources#resource:-googleapisource) resource that represents a subscription to Google API events for a particular Eventarc Advanced bus. For more information, see [Publish events from Google sources](https://docs.cloud.google.com/eventarc/advanced/docs/publish-events/publish-events-google-sources).

**Note:** You can create one `GoogleApiSource` resource per Google Cloud project per [supported region](https://docs.cloud.google.com/eventarc/docs/locations#advanced-regions).

Use the [`google_eventarc_google_api_source`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/eventarc_google_api_source) Terraform resource to enable events from Google sources:
    
    
    # Enable events from Google API sources
    resource "google_eventarc_google_api_source" "default" {
      location             = "us-central1"
      google_api_source_id = "example-google-api-source"
      destination          = google_eventarc_message_bus.default.id
    }

All [supported Google event types](https://docs.cloud.google.com/eventarc/advanced/docs/event-types#advanced-events) sent directly from a Google source are now collected and published to your bus.

### Create an Eventarc Advanced pipeline

A pipeline lets you configure a target destination and also provides the option of transforming any matched events prior to delivering them to the destination.

Use the [`google_eventarc_pipeline`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/eventarc_pipeline) Terraform resource to create a pipeline:
    
    
    # Create an Eventarc Advanced pipeline
    resource "google_eventarc_pipeline" "default" {
      location    = "us-central1"
      pipeline_id = "example-pipeline"
      destinations {
        http_endpoint {
          uri = google_cloud_run_v2_service.default.uri
        }
        authentication_config {
          google_oidc {
            service_account = google_service_account.default.email
          }
        }
      }
    }

The event destination is the fully qualified URL of your Cloud Run service—for example, `https://SERVICE_NAME-abcdef-uc.a.run.app`. The service account email address is used to generate an [OIDC token](https://developers.google.com/identity/protocols/OpenIDConnect).

**Note:** Creating a pipeline can take several minutes.

### Create an Eventarc Advanced enrollment

An enrollment determines which messages are routed to a destination and it also specifies the pipeline that is used to configure a destination for the event messages. For more information, see [Create an enrollment to receive events](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/create-enrollment).

Use the [`google_eventarc_enrollment`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/eventarc_enrollment) Terraform resource to create an enrollment:
    
    
    # Create an Eventarc Advanced enrollment
    resource "google_eventarc_enrollment" "default" {
      location      = "us-central1"
      enrollment_id = "example-enrollment"
      message_bus   = google_eventarc_message_bus.default.id
      destination   = google_eventarc_pipeline.default.id
      cel_match     = "message.type == 'google.cloud.workflows.workflow.v1.created'"
    }

The matching expression for the enrollment [uses Common Expression Language (CEL)](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/use-cel) to publish event messages whenever a workflow is created. In a subsequent step, you will create a workflow.

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
         
         terraform apply -target="google_eventarc_message_bus.default"

Wait until Terraform displays the "Apply complete!" message.




## Publish an event message to the bus by creating a workflow

[Workflows](https://docs.cloud.google.com/workflows/docs/overview) is a fully managed orchestration platform that executes services in an order that you define: a _workflow_. Create a workflow to generate a [supported event type](https://docs.cloud.google.com/eventarc/advanced/docs/event-types#advanced-events) from a Google source.

  1. In your home directory, create a new file called `myWorkflow.yaml`.

  2. Copy and paste the following workflow into the new file, then save it:
         
         main:
             params: [input]
             steps:
             - checkSearchTermInInput:
                 switch:
                     - condition: '${"searchTerm" in input}'
                       assign:
                         - searchTerm: '${input.searchTerm}'
                       next: readWikipedia
             - getLocation:
                 call: sys.get_env
                 args:
                     name: GOOGLE_CLOUD_LOCATION
                 result: location
             - setFromCallResult:
                 assign:
                     - searchTerm: '${text.split(location, "-")[0]}'
             - readWikipedia:
                 call: http.get
                 args:
                     url: 'https://en.wikipedia.org/w/api.php'
                     query:
                         action: opensearch
                         search: '${searchTerm}'
                 result: wikiResult
             - returnOutput:
                     return: '${wikiResult.body[1]}'
         

This workflow passes the region where the workflow is deployed to the [Wikipedia API](https://wikipedia.org/w/api.php) and returns a list of related Wikipedia articles.

  3. Deploy the workflow by using the [`gcloud workflows deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/workflows/deploy) command:
         
         gcloud workflows deploy example-workflow --source=myWorkflow.yaml \
             --service-account=eventarc-advanced-sa@PROJECT_ID.iam.gserviceaccount.com \
             --location=us-central1




## View the event data in the Cloud Run logs

After publishing an event to your Eventarc Advanced bus, you can check the logs of your Cloud Run service to verify that the event was received as expected.

  1. Filter the log entries created by your service:
         
         gcloud logging read 'jsonPayload.message: "Received event of type google.cloud.workflows.workflow.v1.created."'
         

  2. Look for a log entry similar to the following:
         
         message: 'Received event of type google.cloud.workflows.workflow.v1.created.
         Event data: {"@type":"type.googleapis.com/google.events.cloud.workflows.v1.WorkflowEventData","payload":{"name":"projects/PROJECT_ID/locations/us-central1/workflows/example-workflow","state":"ACTIVE"...
         


**Note:** If you don't see a log entry, wait a few minutes and retry the `gcloud logging read` command.

You have successfully created an Eventarc Advanced bus and enrollment, enabled the publishing of events from Google sources, created a workflow to generate a supported event type from a Google provider, and then verified the expected outcome in the logs of the event receiver service.

## Clean up

Remove resources previously applied with your Terraform configuration by running the following command and entering `yes` at the prompt:
    
    
    terraform destroy

You can also delete your Google Cloud project to avoid incurring charges. Deleting your Google Cloud project stops billing for all the resources used within that project.

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 
  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * [Publish events directly](https://docs.cloud.google.com/eventarc/advanced/docs/publish-events/publish-events-direct-format)
  * [Transform received events](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/transform-events)
  * [Format received events](https://docs.cloud.google.com/eventarc/advanced/docs/receive-events/configure-format-events)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
