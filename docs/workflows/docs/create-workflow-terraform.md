---
url: https://docs.cloud.google.com/workflows/docs/create-workflow-terraform/
title: Quickstart: Create a workflow by using Terraform \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:30:13.031949+00:00
---

# Quickstart: Create a workflow by using Terraform  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/create-workflow-terraform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a workflow by using Terraform

This quickstart shows you how to create, deploy, and execute your first workflow using Terraform. Terraform is an infrastructure-as-code tool that lets you predictably create, change, and improve your cloud infrastructure by using code. [Learn how to use Terraform](https://docs.cloud.google.com/docs/terraform) to provision infrastructure on Google Cloud.

In this quickstart, the sample workflow sends a request to a public API and then returns the API's response.

You will complete the following:

  1. Enable the Workflows API using Terraform.
  2. Create a service account for the workflow using Terraform.
  3. Define and deploy a workflow using Terraform.
  4. Execute the workflow using the Google Cloud CLI.



## Before you begin

Security constraints defined by your organization might prevent you from completing the following steps. For troubleshooting information, see [Develop applications in a constrained Google Cloud environment](https://docs.cloud.google.com/resource-manager/docs/organization-policy/develop-apps-constrained-environment). 

Note that Cloud Shell has Terraform already integrated. If you need to install Terraform, see the [HashiCorp Terraform documentation](https://developer.hashicorp.com/terraform/tutorials/gcp-get-started/install-cli).

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

  6. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  8. Enable the Cloud Resource Manager, Identity and Access Management (IAM), and Service Usage APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable cloudresourcemanager.googleapis.com iam.googleapis.com serviceusage.googleapis.com

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

  13. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  14. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  15. Enable the Cloud Resource Manager, Identity and Access Management (IAM), and Service Usage APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable cloudresourcemanager.googleapis.com iam.googleapis.com serviceusage.googleapis.com




### Required roles

To get the permissions that you need to complete this quickstart, ask your administrator to grant you the following IAM roles on your project: 

  * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
  * [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
  * [Workflows Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/workflows#workflows.admin) (`roles/workflows.admin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a Terraform configuration file

Create a Terraform configuration file called `main.tf` and include the [Google provider for Terraform](https://registry.terraform.io/providers/hashicorp/google/latest/docs) resources used in this quickstart.

Note that you can use [interpolation](https://www.terraform.io/language/expressions/strings#interpolation) for substitutions such as reference variables, attributes of resources, and call functions.

  1. Create a directory:
         
         mkdir terraform

  2. Go to the `terraform` directory:
         
         cd terraform

  3. Add a new file, `main.tf`, to the directory:
         
         nano main.tf

  4. Add the following resources to the `main.tf` file:

     1. Assign the ID of the project:
            
            provider "google" {
            project = "PROJECT_ID"
            }

Replace `PROJECT_ID` with your project's ID.

     2. Enable the Workflows API: 
            
            # Enable Workflows API
            resource "google_project_service" "default" {
              service            = "workflows.googleapis.com"
              disable_on_destroy = false
            }

     3. Create a service account for the workflow: 
            
            # Create a dedicated service account
            resource "google_service_account" "default" {
              account_id   = "sample-workflows-sa"
              display_name = "Sample Workflows Service Account"
            }

     4. Define the workflow using the [`google_workflows_workflow` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/workflows_workflow):

**Important:** When you define workflows in Terraform, variables must be escaped with `$${...}` and not `${...}`.
            
            # Create a workflow
            resource "google_workflows_workflow" "default" {
              name            = "sample-workflow"
              region          = "us-central1"
              description     = "A sample workflow"
              service_account = google_service_account.default.id
            
              deletion_protection = false # set to "true" in production
            
              labels = {
                env = "test"
              }
              user_env_vars = {
                url = "https://timeapi.io/api/Time/current/zone?timeZone=Europe/Amsterdam"
              }
              source_contents = <<-EOF
              # This is a sample workflow that you can replace with your source code
              #
              # The workflow does the following:
              # - Retrieves the current date from a public API and stores the
              #   response in `currentDate`
              # - Retrieves a list of Wikipedia articles from a public API related
              #   to the day of the week stored in `currentDate`
              # - Returns the list of articles in the workflow output
              #
              # Note that when you define workflows in Terraform, variables must be
              # escaped with two dollar signs ($$) and not a single sign ($)
            
              - getCurrentDate:
                  call: http.get
                  args:
                      url: $${sys.get_env("url")}
                  result: currentDate
              - readWikipedia:
                  call: http.get
                  args:
                      url: https://en.wikipedia.org/w/api.php
                      query:
                          action: opensearch
                          search: $${currentDate.body.dayOfWeek}
                  result: wikiResult
              - returnOutput:
                  return: $${wikiResult.body[1]}
            EOF
            
              depends_on = [google_project_service.default]
            }

The following arguments are used in the sample workflow:

        * `name`: the name of your workflow.
        * `region`: the [location](https://docs.cloud.google.com/workflows/docs/locations) of your workflow.
        * `description`: a description of your workflow.
        * `service_account`: the email address or unique ID of the service account associated with the latest workflow version. This service account represents the identity of the workflow and determines what permissions the workflow has. If you don't specify a service account during the workflow's creation, the workflow uses the default Compute Engine service account for its identity. For more information, see [Grant a workflow permission to access Google Cloud resources](https://docs.cloud.google.com/workflows/docs/authentication).
        * `labels`: a list of key-value label pairs to assign to this workflow that helps you organize your Google Cloud instances. For more information, see [What are labels?](https://docs.cloud.google.com/resource-manager/docs/labels-overview#what-are-labels)
        * `user_env_vars`: user-defined environment variables associated with this workflow revision. For more information, see [Use environment variables](https://docs.cloud.google.com/workflows/docs/use-environment-variables).
        * `source_contents`: the Workflows code to execute. For the file size limit, see [Resource limits](https://docs.cloud.google.com/workflows/quotas#resource_limits).

Other optional arguments include the following:

        * `crypto_key_name`: the resource ID for a Cloud Key Management Service key in the following format:
              
              projects/PROJECT_NAME/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME

For more information, see [Use customer-managed encryption keys](https://docs.cloud.google.com/workflows/docs/use-cmek).

        * `call_log_level`: the level of logging to apply to calls and call responses during executions of this workflow. Possible values are:

          * `CALL_LOG_LEVEL_UNSPECIFIED`
          * `LOG_ALL_CALLS`
          * `LOG_ERRORS_ONLY`
          * `LOG_NONE`

For more information, see [Call logging](https://docs.cloud.google.com/workflows/docs/log-workflow#call_logging).

        * `project`: the ID of the project in which the resource belongs. If it is not provided, the provider project is used.

        * `name_prefix`: creates a unique name beginning with the specified prefix. If this and `name` are unspecified, a random value is chosen for the name.




## Create and execute the workflow

Deploy your Terraform resources to create the workflow and then execute the workflow.

  1. Initialize Terraform in the directory:
         
         terraform init

  2. Check that the changes you propose with Terraform match the expected plan:
         
         terraform plan

You can ignore the note regarding not using the `-out` option.

  3. Create the workflow:
         
         terraform apply

  4. At the **Enter a value** prompt, type `yes` to proceed with the creation of resources.

  5. Confirm that a workflow is created:
         
         gcloud workflows list --location us-central1

The output should be similar to the following:
         
         NAME                                                                    STATE   REVISION_ID  UPDATE_TIME
         projects/project-name/locations/us-central1/workflows/sample-workflow   ACTIVE  000001-f9a   2024-02-24T13:38:58.353765906Z

  6. Optionally, you can execute the workflow:
         
         gcloud workflows execute sample-workflow




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, delete the Google Cloud project with the resources. 

  1. Delete all the resources you created with Terraform: 
         
         terraform destroy

  2. Delete the workflow you created: 
         
         gcloud workflows delete sample-workflow

When asked if you want to continue, enter `y`. 
  3. Alternatively, you can delete your Google Cloud project to avoid incurring charges. Deleting your Google Cloud project stops billing for all the resources used within that project. **Caution** : Deleting a project has the following effects: 
        * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
        * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




## What's next

  * [Control the order of execution in a workflow](https://docs.cloud.google.com/workflows/docs/controlling-execution-order).

  * [Update an existing workflow](https://docs.cloud.google.com/workflows/docs/creating-updating-workflow#updating_a_workflow).

  * [Explore sample workflows](https://docs.cloud.google.com/workflows/docs/samples).

  * [Learn more about the Workflows syntax](https://docs.cloud.google.com/workflows/docs/reference/syntax).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
