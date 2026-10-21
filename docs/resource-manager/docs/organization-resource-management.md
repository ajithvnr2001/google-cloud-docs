---
url: https://docs.cloud.google.com/resource-manager/docs/organization-resource-management/
title: Manage projects and billing in your organization \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:20:26.683972+00:00
---

# Manage projects and billing in your organization  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/organization-resource-management/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview)



Send feedback 

#  Manage projects and billing in your organization Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to view and manage projects and billing accounts within your Google Cloud organization.

## View billing accounts

You can view the existing billing accounts under an organization using the Google Cloud console.

### Console

  1. Open the Google Cloud console: 

[Open the Billing page](https://console.cloud.google.com/billing)

  2. In the organization picker at the top of the page, select your organization. All billing accounts associated with that organization are listed.




## Create projects in your organization

### Console

You can create a project in the organization using the Google Cloud console once the organization resource is provisioned for your domain.

To create a new project, do the following:

  1. Go to the **Manage resources** page in the Google Cloud console. 

[Go to Manage Resources](https://console.cloud.google.com/cloud-resource-manager?walkthrough_id=resource-manager--create-project&start_index=1#step_index=1)

The remaining steps appear in the Google Cloud console.

  2. Click **Create project**. 
  3. In the **New project** window that appears, enter a project name and select a billing account as applicable. A project name can contain only letters, numbers, single quotes, hyphens, spaces, or exclamation points, and must be between 4 and 30 characters. **Note:** A billing account is available for selection only if you have the [Billing Account User](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.user) role (`roles/billing.user`) on the organization or billing account. When granted in combination with the Project Creator role (`roles/resourcemanager.projectCreator`), these roles let you create new projects linked to that billing account. When granted in combination with the Project Billing Manager role (`roles/billing.projectManager`), these roles let you link and unlink projects on the billing account. 
  4. Enter the parent organization or folder resource in the **Parent resource** box. That resource will be the hierarchical parent of the new project. If **No organization** is an option, you can select it to create your new project as the top level of its own resource hierarchy. 
  5. When you're finished entering new project details, click **Create**.



### REST

To create a new project in your organization, use the [`projects.create()`](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/create) method and set the project's `parent` field to the `organizationId` of the organization.

The following code snippet demonstrates how to create a project in an organization:
    
    
      project = crm.projects().create(
          body={
              'project_id': flags.projectId,
              'name': 'My New Project',
              'parent': {
                  'type': 'organization',
                  'id': flags.organizationId
               }
      }).execute()
    

## View all projects in an organization

### Console

To view all projects under an organization, follow these steps:

  1. Go to the Google Cloud console: 

[Go to Google Cloud console](https://console.cloud.google.com/)

  2. From the project picker at the top of the page, select your organization.

  3. The **Recent** tab will show recently accessed projects and folders. Click the **All** tab to view all projects and folders.


**Note:** Up to 4000 resources can be displayed in the project picker. If you don't see a resource that should appear, go to the **Manage resources** page and filter the list using the name of that resource.

The **No organization** option in the organization picker displays two types of projects:

  * Unassociated projects: Projects that have not yet been migrated into your organization.
  * Inaccessible parent: Projects where you have access to the project itself, but don't have permissions to view the parent organization.



### gcloud

To view all projects directly under the organization, run the following command:
    
    
    gcloud projects list --filter 'parent.id=[ORGANIZATION_ID] AND \
        parent.type=organization'
    

This command does not show every project in your hierarchy, only the projects that are directly under your organization resource. To list every resource in your hierarchy, see [Listing all Resources in your Hierarchy](https://docs.cloud.google.com/resource-manager/docs/listing-all-resources).

### REST

Use the [`projects.list()`](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/list) method to list all the projects directly under the organization resource, as shown in the following code snippet:
    
    
    filter = 'parent.type:organization parent.id:%s' % flags.organizationId
    projects = crm.projects().list(filter=filter).execute()
    

This method does not show every project in your hierarchy, only the projects that are directly under your organization resource. To list every resource in your hierarchy, see [Listing all Resources in your Hierarchy](https://docs.cloud.google.com/resource-manager/docs/listing-all-resources).

## Delete projects in an organization

To delete a project in an organization, follow these steps:

### Console

To delete a project using the Google Cloud console:

  1. Go to the **Projects** page in the **IAM & Admin** section: 

[Open the Projects page](https://console.cloud.google.com/iam-admin/projects)

  2. Click the **Organization** drop-down on top of the page.
  3. Select your organization. All projects in the organization are listed on the page.
  4. In the list of projects, select the project you want to delete, and click **Delete Project**.
  5. Enter the project ID and click **Shut down**.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
