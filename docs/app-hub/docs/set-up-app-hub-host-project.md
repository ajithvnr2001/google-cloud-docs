---
url: https://docs.cloud.google.com/app-hub/docs/set-up-app-hub-host-project/
title: Set up a host project (Legacy) \u00a0|\u00a0 App Hub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:14:34.960659+00:00
---

# Set up a host project (Legacy)  |  App Hub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-hub/docs/set-up-app-hub-host-project/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ App Hub ](https://docs.cloud.google.com/app-hub/docs)
  * [ Guides ](https://docs.cloud.google.com/app-hub/docs/overview)



Send feedback 

#  Set up a host project (Legacy) Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to set up a host project in App Hub and create a multiple-project [boundary](https://docs.cloud.google.com/app-hub/docs/key-concepts#app-mgmt-boundary).

The host project is a legacy application setup model supported for existing App Hub users. We recommend defining folder-level boundaries by [setting up an app-enabled folder](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub-folder) for new implementations. Folder-level boundaries provide access to the complete set of Application-centric Google Cloud features, such as Application Design Center and Gemini Cloud Assist. For a comparison of key differences between the available models for application management, see [Choose your application setup model](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub).

## Overview of host and service projects

A [host project](https://docs.cloud.google.com/app-hub/docs/key-concepts#host-project) is a Google Cloud project to which you attach other projects that contain the services and workloads you want to group as App Hub applications. The projects you attach to the host project are called [service projects](https://docs.cloud.google.com/app-hub/docs/key-concepts#service-project). The attachment of the host project and service projects define a multiple-project [boundary](https://docs.cloud.google.com/app-hub/docs/key-concepts#app-mgmt-boundary).

A host project can manage its own resources directly by attaching to itself. However, for a single-project setup, we recommend using [the single-project approach](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub-single-project).

**Important:** The host and service project model in App Hub is distinct from the model used by [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc). You cannot use a Shared VPC host project and its attached service projects for App Hub. In App Hub, host and service projects are for logically grouping application components, not for sharing VPC networks.

## Before you begin

Before you set up a Google Cloud project as a host project and attach service projects to it, complete the following steps:

  1. Identify the Google Cloud project you want to use as the host project. You can use an existing project or [create a new project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).
  2. Identify the Google Cloud projects that you want to attach to the host project as service projects. You must identify all the projects that contain the services and workloads that you intend to register to App Hub applications. Resources in other projects won't be visible to App Hub. Service projects have the following requirements:

     * Service projects must be in the same [organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization) as the host project.
     * A service project can only be attached to one host project at a time.
     * A host project can act as a service project for itself to manage its own resources, but you cannot attach it as a service project to any other host project.
     * Choose a host project and service projects that aren't descendants of [folders](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub-folder) that you configured for application management. This separation ensures that all resources in a folder are managed with the same type of setup model.



### Required roles

To get the permissions that you need to attach service projects to the host project, ask your administrator to grant you the [App Hub Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.admin) (`roles/apphub.admin`) IAM role on the host project and on each service project that you want to attach. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Set up the host project

To configure a Google Cloud project as a host project, follow these steps:

###  Console 

  1. In the Google Cloud console, use the project picker to select your project.

  2. Navigate to the **Overview** page from App Hub:

[Go to Overview](https://console.cloud.google.com/apphub)

  3. Click **Set up App Hub**.

  4. In the **Enable App Hub** page, choose **Full setup** to create a multiple-project boundary.

  5. Make note of the project name and ID. This information identifies the host project and you'll use these values to grant access.

  6. Review the list of [APIs being enabled](https://docs.cloud.google.com/app-hub/docs/enabled-apis). Some APIs have associated costs. [Learn more about the costs of APIs](https://docs.cloud.google.com/app-hub/docs/enabled-apis#costs) or click each API to see associated costs.

**Note:** This setup process enables several APIs, but only App Hub and Application Monitoring support host projects. Therefore, other enabled APIs might not function as expected in this legacy setup model. For more information, see [Feature support by boundary type](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub#support).
  7. Click **Continue**.

  8. In the **Define boundary** tab, verify your project information.

  9. Click add  **Add project** to add service projects to your boundary or add those later.

  10. Click **Continue**.

  11. In the **Grant access** tab, choose the appropriate [IAM roles and permissions](https://docs.cloud.google.com/app-hub/docs/roles-permissions) for administrators in the project. For a list of recommended application-centric roles across Google Cloud products, see [Grant application-centric roles to your users](https://docs.cloud.google.com/resource-manager/docs/manage-applications#assign-roles).

  12. In the **New principals** box, enter the users, groups, or service accounts who should have administrator access to application-centric tasks in the project.

  13. Click **Grant roles** and then click **Complete**.




Later, you can grant additional IAM roles to your principals from the **IAM** page. For more information, see [Grant an IAM role by using the Google Cloud console](https://docs.cloud.google.com/iam/docs/grant-role-console).

###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Make sure that the most recent version of Google Cloud CLI is installed:
         
         gcloud components update
         

  3. [Find the project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project that you want to configure as the host project.

  4. Set the host project as the default project for commands:
         
         gcloud config set project HOST_PROJECT_ID
         

Replace `HOST_PROJECT_ID` with the ID of the project you want to configure as the host project.

  5. Enable the [App Hub API](https://docs.cloud.google.com/app-hub/docs/reference/rest) in the host project:
         
         gcloud services enable apphub.googleapis.com \
             --project=HOST_PROJECT_ID
         




## Add service projects

Add service projects to your [application management boundary](https://docs.cloud.google.com/app-hub/docs/key-concepts#app-mgmt-boundary) by attaching them to the host project.

To attach service projects to the host project and create a multiple-project boundary, follow these steps:

###  Console 

  1. In the Google Cloud console, use the project picker to select the host project.

[ Go to Welcome](https://console.cloud.google.com/welcome)

  2. Navigate to the **Boundary settings** page from App Hub:

[Go to Boundary settings](https://console.cloud.google.com/apphub/settings)

  3. Click add  **Add project**.

  4. Select the service projects that you want to attach to the host project and add to your boundary in one of the following ways:

     * From the list of projects, select the checkboxes for the projects you want to attach as service projects.
     * Filter the project names and select their checkboxes.
  5. Click **Select**.

The **Projects in your boundary** table displays the selected service projects. The attachment process might take some time to complete.

  6. Verify the list of service projects is complete.




###  gcloud 

  1. [Find the project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of each of the Google Cloud projects that you want to configure as service projects.
  2. Attach each service project:
         
         gcloud apphub service-projects add SERVICE_PROJECT_ID \
             --project=HOST_PROJECT_ID
         

Replace the following:

     * `SERVICE_PROJECT_ID`: the ID of the service project to attach.
     * `HOST_PROJECT_ID`: the ID of the host project.
  3. Repeat the previous process for each service project you want to attach to the host project.




###  Terraform 

To attach a service project to a host project using Terraform, use [the `google_apphub_service_project_attachment` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/apphub_service_project_attachment), for example:
    
    
    resource "google_apphub_service_project_attachment" "example" {
        service_project_attachment_id = google_project.service_project.project_id
        depends_on = [time_sleep.wait_120s]
    }
    
    resource "google_project" "service_project" {
        project_id ="project-1"
        name = "Service Project"
        org_id = "123456789"
        deletion_policy = "DELETE"
    }
    
    resource "time_sleep" "wait_120s" {
        depends_on = [google_project.service_project]
    
        create_duration = "120s"
    }
    

To detach a service project from a host project, see Remove service projects.

## Assign App Hub roles and permissions

To grant appropriate [App Hub roles and permissions](https://docs.cloud.google.com/app-hub/docs/roles-permissions) to App Hub users in the host project and service projects, follow these steps:

###  Console 

  1. In the Google Cloud console, use the project picker to select the host project.

[ Go to Welcome](https://console.cloud.google.com/welcome)

  2. Navigate to the **IAM** page:

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam)

  3. Click person_add **Grant access**. The **Grant access** pane opens.

  4. In the **New principals** field, enter the email address of the principal that you want to grant access to App Hub.

  5. Click **Select a role** and enter _App Hub_ in the **Filter** field.

  6. Select the [App Hub IAM role](https://docs.cloud.google.com/app-hub/docs/roles-permissions) you intend to assign to the principal and click **Save**.

  7. In each of the App Hub service projects you attached to the host project, repeat the previous process to grant the same roles to the same users.




###  gcloud 

  1. [Find the project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of each of the Google Cloud projects that you configured as host and service projects.

  2. Grant access to principals in the host project:
         
         gcloud projects add-iam-policy-binding HOST_PROJECT_ID \
             --member='user:EMAIL_ADDRESS' \
             --role='ROLE_NAME'
         

Replace the following:

     * `HOST_PROJECT_ID`: the ID of the host project.
     * `EMAIL_ADDRESS`: the email address of the principal who must obtain App Hub access in the host project. This value must have the format `username@yourdomain`, for example, `my.user@example.com`.
     * `ROLE_NAME`: the [App Hub IAM role](https://docs.cloud.google.com/app-hub/docs/roles-permissions) you want to assign to the principal, for example, `roles/apphub.admin`.
  3. In each of the App Hub service projects you attached to the host project, grant the same roles to the same users:
         
         gcloud projects add-iam-policy-binding SERVICE_PROJECT_ID \
             --member='user:EMAIL_ADDRESS' \
             --role='ROLE_NAME'
         

Replace `SERVICE_PROJECT_ID` with the ID of the service project you are granting access to.




## Set up VPC Service Controls

To protect your applications with a VPC Service Controls perimeter, add your App Hub host project and service projects to the perimeter before you create your applications. For more information, see [Use VPC Service Controls with App Hub](https://docs.cloud.google.com/app-hub/docs/using-vpc-service-controls).

## Optional: Configure the metrics scope

To view system metrics for applications within your host project in Cloud Monitoring, add the attached service projects to the host project's [metrics scope](https://docs.cloud.google.com/monitoring/settings). The host project serves as a scoping project for time-series data, enabling the charting and monitoring of data. For more information and configuration instructions, see [Configure a metrics scope](https://docs.cloud.google.com/monitoring/settings/multiple-projects) and [Configure a metrics scope by using the API](https://docs.cloud.google.com/monitoring/settings/manage-api).

## Remove service projects

Remove service projects from your [application management boundary](https://docs.cloud.google.com/app-hub/docs/key-concepts#app-mgmt-boundary) by detaching them from the host project.

To detach a service project from a host project, follow these steps:

###  Console 

  1. In the Google Cloud console, use the project picker to select the host project.

[ Go to Welcome](https://console.cloud.google.com/welcome)

  2. Navigate to the **Boundary settings** page from App Hub:

[Go to Boundary settings](https://console.cloud.google.com/apphub/settings)

  3. Select the checkboxes of the service projects that you want to detach from the host project and remove from your boundary.

  4. Click **Detach projects**.

The **Projects in your boundary** table refreshes to display only the projects that remain attached to the host project.

  5. Verify the list of service projects is updated.




###  gcloud 

  1. [Find the project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of each of the service projects that you want to remove from the host project.
  2. Remove each service project:
         
         gcloud apphub service-projects remove SERVICE_PROJECT_ID \
             --project=HOST_PROJECT_ID
         

Replace the following:

     * `SERVICE_PROJECT_ID`: the ID of the service project to remove.
     * `HOST_PROJECT_ID`: the ID of the host project.
  3. Repeat the previous process for each service project you want to remove from the host project.




**Important:** When you remove a service project from a host project, the [registration status of services and workloads](https://docs.cloud.google.com/app-hub/docs/overview#registration-status) from that project that are registered to applications changes to _detached_.

When you remove a service project from a host project, consider removing it also from the host project's metrics scope if you previously configured the metrics scope. For more information, see [Remove projects from a metrics scope](https://docs.cloud.google.com/monitoring/settings/multiple-projects#remove-monitored-project).

## What's next

  * [Register existing resources to an application](https://docs.cloud.google.com/app-hub/docs/register-resources)
  * [Set up application monitoring](https://docs.cloud.google.com/monitoring/docs/setup-application-monitoring)
  * [App Hub IAM roles and permissions](https://docs.cloud.google.com/app-hub/docs/roles-permissions)
  * [App Hub overview](https://docs.cloud.google.com/app-hub/docs/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
