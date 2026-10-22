---
url: https://docs.cloud.google.com/app-hub/docs/set-up-app-hub-single-project/
title: Set up a single project \u00a0|\u00a0 App Hub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:45:14.287014+00:00
---

# Set up a single project  |  App Hub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-hub/docs/set-up-app-hub-single-project/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ App Hub ](https://docs.cloud.google.com/app-hub/docs)
  * [ Guides ](https://docs.cloud.google.com/app-hub/docs/overview)



Send feedback 

#  Set up a single project Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to set up a single Google Cloud project to manage applications. This configuration is also known as the [single-project boundary](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub#compare-models).

In this setup, the Google Cloud project is configured to manage its own applications and components, acting as a standalone [management project](https://docs.cloud.google.com/app-hub/docs/key-concepts#mgmt-project). This approach is the quickest way to begin managing applications if all your application components reside within this single project. App Hub automatically discovers all supported resources within the project, making them ready to be organized into applications.

## Limitations

The single-project boundary has different feature support compared to the folder-level boundary. App Hub, Application Design Center, and Application Monitoring fully support single projects, but other Application-centric Google Cloud services, like Cloud Hub and Gemini Cloud Assist, require a folder-level boundary.

For a comparison of feature support between the single-project and folder-level models, see [Feature support by boundary type](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub#support).

## Before you begin

Choose the Google Cloud project you want to use for managing your applications. This project will function as the standalone [management project](https://docs.cloud.google.com/app-hub/docs/key-concepts#mgmt-project). You can use an existing project or [create a new one](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

### Required roles

To get the permissions that you need to configure a single project for application management, ask your administrator to grant you the following IAM roles on the project that you want to configure as the standalone management project: 

  * Manage resources, permissions, and billing on the project: [Project Owner ](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`) 
  * Manage all application components on the project: [App Hub Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/apphub#apphub.admin) (`roles/apphub.admin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Enable application management on a project

This action configures the project as a standalone management project and enables the [required APIs](https://docs.cloud.google.com/app-hub/docs/enabled-apis) for application metadata and configurations. The project is then called an app-enabled project.

To enable application management on a single project, follow these steps:

###  Console 

  1. In the Google Cloud console, use the project picker to select your project.

  2. Navigate to the **Overview** page from App Hub:

[Go to Overview](https://console.cloud.google.com/apphub)

  3. Click **Set up App Hub**.

If your project is already inside an [app-enabled folder](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub-folder), the page doesn't display the **Set up App Hub** option. Instead, you are prompted to either select the app-enabled folder or to use the current project from a menu. Select the current project to continue with the single-project setup. To learn more about resource hierarchy considerations for application management, see [Plan your resource hierarchy for application management](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub#resource-hierarchy).

  4. In the **Enable App Hub** page, choose one of the following options:

     * **Quick setup** : manage a default configuration for resources in this project and define your first application for initial adoption.
     * **Full setup** : manage custom configurations for your applications, including setting up upfront access controls and, optionally, adding more projects for [multiple-project boundaries](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub#compare-models).
  5. Make note of the project name and ID. This information identifies the [management project](https://docs.cloud.google.com/app-hub/docs/key-concepts#mgmt-project) and you'll use these values to grant access.

  6. Review the list of [APIs being enabled](https://docs.cloud.google.com/app-hub/docs/enabled-apis). Some APIs have associated costs. [Learn more about the costs of APIs](https://docs.cloud.google.com/app-hub/docs/enabled-apis#costs) or click each API to see associated costs.

  7. Click **Continue**.

  8. Complete the setup based on your selection:

     * If you selected **Quick setup** , the **Define application** tab lets you optionally define an application now or complete the setup without creating one. You are now ready to [create applications and register resources to them](https://docs.cloud.google.com/app-hub/docs/register-resources). You can also get started with a [quickstart guide for applications](https://docs.cloud.google.com/app-hub/docs/quickstart-create-application).

     * If you selected **Full setup** , grant custom application-centric access for your administrators:

       1. In the **Define boundary** tab, verify your project information. The **Projects in your boundary** table shows only the project that defines your single-project boundary. For the single-project boundary setup, don't add any additional projects.

       2. Click **Continue**.

       3. In the **Grant access** tab, choose the appropriate [IAM roles and permissions](https://docs.cloud.google.com/app-hub/docs/roles-permissions) for administrators in the project. For a list of recommended application-centric roles across Google Cloud products, see [Grant application-centric roles to your users](https://docs.cloud.google.com/resource-manager/docs/manage-applications#assign-roles).

       4. In the **New principals** box, enter the users, groups, or service accounts who should have administrator access to application-centric tasks in the project.

       5. Click **Grant roles** and then click **Complete**.

You can now [register existing resources to an application](https://docs.cloud.google.com/app-hub/docs/register-resources#register-services-and-workloads) or [create an application template](https://docs.cloud.google.com/app-hub/docs/create-applications-from-templates) with Application Design Center.




Later, you can grant additional IAM roles to your principals from the **IAM** page. For more information, see [Grant an IAM role by using the Google Cloud console](https://docs.cloud.google.com/iam/docs/grant-role-console).

###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Make sure that the most recent version of Google Cloud CLI is installed:
         
         gcloud components update
         

  3. [Find the project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

  4. Set the project as the default project for commands:
         
         gcloud config set project PROJECT_ID
         

Replace `PROJECT_ID` with the ID of the project.

  5. Enable the App Hub API:
         
         gcloud services enable apphub.googleapis.com \
             --project PROJECT_ID
         

  6. Attach the project to itself to create an application management boundary:
         
         gcloud apphub boundary update \
             --crm-node=projects/PROJECT_ID \
             --project=PROJECT_ID \
             --location=global
         

This command configures the project as its own management project, letting App Hub automatically discover all [supported resources](https://docs.cloud.google.com/app-hub/docs/supported-resources) within it.

  7. Confirm the attachment status:
         
         gcloud apphub boundary describe \
             --project=PROJECT_ID \
             --location=global
         

You obtain an output similar to the following example:
         
         name: projects/PROJECT_ID/locations/LOCATION/boundary
         crmNode: projects/PROJECT_ID
         createTime: 2025-08-28T19:04:47Z
         updateTime: 2025-08-28T19:04:47Z
         type: AUTOMATIC
         




When you finish configuring the management project, the required APIs for application management are enabled, and you can start using App Hub to group services and workloads in applications. Optionally, review [recommended APIs](https://docs.cloud.google.com/app-hub/docs/enabled-apis) to gain access to advanced features.

## Assign App Hub roles and permissions

To let users discover, register, and manage application components within this project using App Hub, you need to grant them the appropriate [App Hub roles and permissions](https://docs.cloud.google.com/app-hub/docs/roles-permissions).

Follow these steps:

###  Console 

  1. In the Google Cloud console, use the project picker to select the management project.

  2. Navigate to the **IAM** page:

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam)

  3. Click person_add **Grant access**. The **Grant access** pane opens.

  4. In the **New principals** field, enter the email address of the principal that you want to grant access to App Hub.

  5. Click **Select a role** and enter _App Hub_ in the **Filter** field.

  6. Select the [App Hub IAM role](https://docs.cloud.google.com/app-hub/docs/roles-permissions) you intend to assign to the principal and click **Save**.




###  gcloud 

  1. Grant access to principals in the management project:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member='user:EMAIL_ADDRESS' \
             --role='ROLE_NAME'
         

Replace the following:

     * `PROJECT_ID`: the ID of the management project.
     * `EMAIL_ADDRESS`: the email address of the principal who must obtain App Hub access. This value must have the format `username@yourdomain`, for example, `my.user@example.com`.
     * `ROLE_NAME`: the [App Hub IAM role](https://docs.cloud.google.com/app-hub/docs/roles-permissions) you want to assign to the principal, for example, `roles/apphub.admin`.



## Change the application management boundary

If you want to change the project that defines your single-project boundary, disable application management on the old project and enable it on the new one. Your application data isn't migrated, and you must recreate your applications in the new project.

To move from a single-project boundary to a folder-level boundary, [set up an app-enabled folder](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub-folder). This action configures a new management project in the folder. You'll need to recreate applications in this new management project.

## Disable application management on a project

You can disable application management on a project if you no longer want to manage its resources in App Hub applications.

When you disable application management on the project, the project is detached from its [application management boundary](https://docs.cloud.google.com/app-hub/docs/key-concepts#app-mgmt-boundary). The services and workloads in your applications continue to exist, but their [registration status](https://docs.cloud.google.com/app-hub/docs/overview#registration-status) changes to detached. If you decide to re-enable application management on the project, App Hub can rediscover your applications, services, and workloads and update the registration status if the underlying resources still exist.

To disable application management on a single project, follow these steps:

###  Console 

  1. In the Google Cloud console, use the project picker to select the management project.

[ Go to Welcome](https://console.cloud.google.com/welcome)

  2. Navigate to the **Boundary settings** page from App Hub:

[Go to Boundary settings](https://console.cloud.google.com/apphub/settings)

  3. Select the checkbox of the project to detach it from the [boundary](https://docs.cloud.google.com/app-hub/docs/key-concepts#app-mgmt-boundary) and disable application management.

  4. Click **Detach projects**.

The **Projects in your boundary** table refreshes and doesn't display your project information anymore.




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Make sure that the most recent version of Google Cloud CLI is installed:
         
         gcloud components update
         

  3. [Find the project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

  4. Set the project as the default project for commands:
         
         gcloud config set project PROJECT_ID
         

Replace `PROJECT_ID` with the ID of the project.

  5. Detach the project from its [boundary](https://docs.cloud.google.com/app-hub/docs/key-concepts#app-mgmt-boundary) to disable application management:
         
         gcloud apphub boundary update \
             --project=PROJECT_ID \
             --location=global \
             --crm-node=""
         

This command updates the boundary resource and removes the attachment, disabling application management for the project.

  6. Confirm the detachment by describing the boundary:
         
         gcloud apphub boundary describe \
             --project=PROJECT_ID \
             --location=global
         

The output doesn't contain a `crmNode` field, confirming that application management is disabled on the project.

  7. Optionally, [delete all the applications in the project](https://docs.cloud.google.com/app-hub/docs/manage-applications#delete) and then disable the App Hub API if you won't use application features in this project anymore:
         
         gcloud services disable apphub.googleapis.com \
             --project=PROJECT_ID
         




## What's next

  * [Quickstart: Create an application from existing resources](https://docs.cloud.google.com/app-hub/docs/quickstart-create-application)
  * [Register resources to an application](https://docs.cloud.google.com/app-hub/docs/register-resources)
  * [Set up application monitoring](https://docs.cloud.google.com/monitoring/docs/setup-application-monitoring)
  * [App Hub IAM roles and permissions](https://docs.cloud.google.com/app-hub/docs/roles-permissions)
  * [App Hub overview](https://docs.cloud.google.com/app-hub/docs/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
