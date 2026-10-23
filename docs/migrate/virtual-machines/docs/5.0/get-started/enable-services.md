---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/enable-services/
title: Enable Migrate to Virtual Machines services \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:14.206660+00:00
---

# Enable Migrate to Virtual Machines services  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/enable-services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Guides ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/lifecycle)



Send feedback 

#  Enable Migrate to Virtual Machines services Stay organized with collections  Save and categorize content based on your preferences. 

Before you can begin a migration, you must enable the Migrate to Virtual Machines service on Google Cloud and also enable all other Google Cloud services required by Migrate to Virtual Machines.

## Identifying your host project

[Google Cloud projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) form the basis for creating, enabling, and using Google Cloud services including managing APIs, enabling billing, adding and removing collaborators, and managing permissions for Google Cloud resources.

Migrate to Virtual Machines uses the following types of projects:

  * **Host project (Required)**

Use the _host_ project to control the migration process and optionally to host the Compute Engine instances running your migrated workloads. You **must** create and configure a host project as described in the following sections.

  * **Target project (Optional)**

A _target_ project defines the destination project for a Compute Engine instance running your migrated VM. Your **host** project can be used as a target project. If you want to migrate VMs to additional projects, you must add them as target projects to Migrate to Virtual Machines. See [Adding a target project](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/target-project) for more.




To enable Migrate to Virtual Machines services, you must identify the Google Cloud project that you want to use as the **host** project:

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project to use as the **host** project:

[Go to the project selector page](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Note the name and ID of the selected project.




## Installing the gcloud CLI

Install the gcloud CLI on your workstation, which also installs the Google Cloud CLI. `gcloud` is the primary CLI tool that you use to create and manage Google Cloud resources. You can use `gcloud` to perform many common platform tasks either from the command line or in scripts and other automations.

To install the gcloud CLI:

  1. Install and initialize the [gcloud CLI](https://docs.cloud.google.com/sdk/docs/install).

  2. Update gcloud CLI:
         
         gcloud components update

  3. Make sure that gcloud CLI is authorized to access your data and services:
         
         gcloud auth login

  4. A new browser tab opens and you are prompted to choose an account.




## Enabling required services on the host project

Within your host project, enable the Google Cloud services required by Migrate to Virtual Machines service. For more information about these services, see [gcloud services](https://docs.cloud.google.com/sdk/gcloud/reference/services).

The **host** project for Migrate to Virtual Machines requires that you enable the following Google Cloud services:

Name | Title  
---|---  
`vmmigration.googleapis.com` | Migrate to Virtual Machines API   
`servicemanagement.googleapis.com` | Service Management API   
`servicecontrol.googleapis.com` | Service Control API   
`iam.googleapis.com` | Identity and Access Management (IAM) API   
`cloudresourcemanager.googleapis.com` | Cloud Resource Manager API   
`compute.googleapis.com` | Compute Engine API   
  
To enable the required services:

  1. Ensure that you have set the default project to the **host** project. Replace PROJECT_ID with the project ID of your **host** project:
         
         gcloud config set project PROJECT_ID

  2. View the list of services already enabled on the project:
         
         gcloud services list

  3. If you don't see all of the required services listed, enable them:
         
         gcloud services enable vmmigration.googleapis.com servicemanagement.googleapis.com servicecontrol.googleapis.com iam.googleapis.com cloudresourcemanager.googleapis.com compute.googleapis.com 

  4. You should now be able to open the Migrate to Virtual Machines page in the Google Cloud console:

[Go to the Migrate to Virtual Machines page](https://console.cloud.google.com/compute/mfce)




## Using predefined roles

Identity and Access Management includes two predefined roles that you can use to control access for users in your organization:

Role | Title | Description  
---|---|---  
[roles/vmmigration.admin](https://docs.cloud.google.com/iam/docs/understanding-roles) | VM Migration Administrator  | Allows users to create new Migrate to Virtual Machines sources and perform all other migration operations.   
[roles/vmmigration.viewer](https://docs.cloud.google.com/iam/docs/understanding-roles) | VM Migration Viewer  | Allows users to retrieve information about Migrate to Virtual Machines in the Google Cloud console. Intended for users who are performing migrations, but not setting up the system or adding new migration sources.   
  
For example, if you want to allow a user in your organization to be able to view information about a migration, but not be able to perform a migration, assign them the role `roles/vmmigration.viewer`.

## What's next

  * [Installing the Migrate Connector](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrate-connector)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
