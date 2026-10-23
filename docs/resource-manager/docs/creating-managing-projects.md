---
url: https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects/
title: Create projects \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:44:06.835756+00:00
---

# Create projects  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview)



Send feedback 

#  Create projects Stay organized with collections  Save and categorize content based on your preferences. 

Projects are the fundamental operating unit in the Google Cloud resource hierarchy. Projects exist between folders (or the organization) and resources such as virtual machines and storage. This page explains how to create Google Cloud projects using the Cloud Resource Manager API and the Google Cloud console.

Key characteristics of projects include the following:

  * The primary service container: A project is the base level where all Google Cloud services (APIs) are enabled and where resources like Compute Engine instances or BigQuery datasets are created.

  * The trust boundary: Projects serve as an isolation layer. By default, resources in one project don't have access to resources in another, establishing a secure perimeter for different applications or environments.

  * The billing unit: Projects are the primary way businesses track, organize, and separate costs across their organization.

  * The policy attachment point: While policies often inherit from folders, the project level is the most common place where specific permissions ( Identity and Access Management (IAM)) are granted to developers and service accounts for daily tasks.




## Before you begin

Read about the project resource in the [resource hierarchy overview](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#projects). For guidance on setting up your resource hierarchy, see [Decide a resource hierarchy for your Google Cloud landing zone](https://docs.cloud.google.com/architecture/landing-zones/decide-resource-hierarchy).

The following identifiers are used for your project:

  * **Project name** : A human-readable name for your project.

The project name has the following requirements:

    * It must be 4 to 30 characters in length.
    * It can contain letters, numbers, single quotes, hyphens, spaces, or exclamation points.
    * It must end with a letter or a digit.

The project name isn't used by any Google APIs. You can edit the project name at any time during or after project creation. Project names don't need to be unique.

  * **Project ID** : A globally unique identifier for your project.

A project ID is a unique string that differentiates your project from all others in Google Cloud. After you enter a project name, the Google Cloud console generates a unique project ID that can be a combination of letters, numbers, and hyphens. Use the generated project ID, but you can edit it during project creation. After project creation, the project ID is permanent.

A project ID has the following requirements:

    * It must be 6 to 30 characters in length.
    * It can only contain lowercase letters, numbers, and hyphens.
    * It must start with a letter.
    * It cannot end with a hyphen.
    * It cannot be in use or previously used; this includes deleted projects.
    * It cannot contain restricted strings such as `google` and `ssl`. Avoid using strings such as `undefined` and `null` in a project ID.

  * **Project number** : A project number is an automatically generated unique identifier for your project. To find the project number, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/view-update-projects#identifying_projects).




Don't include sensitive information, for example, personally identifiable information or security data, in your project name, project ID, or other resource names. The project ID appears in the name of many other Google Cloud resources. Referencing the project or its resources exposes the project ID and resource name.

## Create a project

To create a project, you must have the `resourcemanager.projects.create` permission. This permission is included in roles like the Project Creator role (`roles/resourcemanager.projectCreator`).

The Project Creator role is granted by default to the entire domain of a new organization resource and to free trial users.

For information on how to grant individuals the role and limit organization-resource wide access, see the [Managing Default Organization Roles](https://docs.cloud.google.com/resource-manager/docs/default-access-control) page.

If you don't specify the parent resource, a parent resource is selected automatically if applicable based on the user account's domain.

You can create a new project using the Google Cloud console, the Google Cloud CLI, or the [`projects.create()`](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/create) method.

### Console

To create a new project, do the following:

  1. Go to the **Manage resources** page in the Google Cloud console. 

[Go to Manage Resources](https://console.cloud.google.com/cloud-resource-manager?walkthrough_id=resource-manager--create-project&start_index=1#step_index=1)

The remaining steps appear in the Google Cloud console.

  2. Click **Create project**. 
  3. In the **New project** window that appears, enter a project name and select a billing account as applicable. A project name can contain only letters, numbers, single quotes, hyphens, spaces, or exclamation points, and must be between 4 and 30 characters. **Note:** A billing account is available for selection only if you have the [Billing Account User](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.user) role (`roles/billing.user`) on the organization or billing account. When granted in combination with the Project Creator role (`roles/resourcemanager.projectCreator`), these roles let you create new projects linked to that billing account. When granted in combination with the Project Billing Manager role (`roles/billing.projectManager`), these roles let you link and unlink projects on the billing account. 
  4. Enter the parent organization or folder resource in the **Parent resource** box. That resource will be the hierarchical parent of the new project. If **No organization** is an option, you can select it to create your new project as the top level of its own resource hierarchy. 
  5. When you're finished entering new project details, click **Create**.



### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To create a new project, use the [`gcloud projects create`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/create) command:
         
         gcloud projects create PROJECT_ID
         

Where PROJECT_ID is the ID for the project you want to create. A project ID must start with a lowercase letter, and can contain only ASCII letters, digits, and hyphens, and must be between 6 and 30 characters.

To create a project with an organization resource or a folder as parent, use the `--organization` or `--folder` flags. As a resource can only have one parent, only one of these flags can be used:
         
         gcloud projects create PROJECT_ID --organization=ORGANIZATION_ID
         
         
         gcloud projects create PROJECT_ID --folder=FOLDER_ID
         




### REST

You can't use certain words in the project ID when you create a new project with the `projects.create()` method. Some examples include `google`, `null`, `undefined`, and `ssl`. When you use a restricted word, the request returns with an `INVALID_ARGUMENT` error.

The following request only creates a project, and doesn't associate it automatically with a billing account. Use the [`projects.updateBillingInfo`](https://docs.cloud.google.com/billing/reference/rest/v1/projects/updateBillingInfo) method to set or update the billing account associated with a project.

Create Project Request:
    
    
    POST https://cloudresourcemanager.googleapis.com/v3/projects/
    Authorization: *************
    Content-Type: application/json
    
    {
        "projectId": "our-project-123",
        "name": "my project",
        "labels": {
          "mylabel": "prod"
        }
    }
    

Create Project Response:
    
    
    {
        "name": "operations/pc.123456789",
    }
    

Get Operation Request:
    
    
    GET https://cloudresourcemanager.googleapis.com/v3/operations/pc.123456789
    Authorization: *************
    Content-Type: application/json
    

Get Operation Response:
    
    
    {
        "name": "operations/pc.123456789",
        "done": true,
        "response": {
            "@type": "type.googleapis.com/google.cloudresourcemanager.v3.Project",
            "projectNumber": "464036093014",
            "projectId": "our-project-123",
            "lifecycleState": "ACTIVE",
            "name": "my project",
            "labels": {
            "mylabel": "prod"
            },
        "createTime": "2016-01-07T21:59:43.314Z"
        }
    }
    

### Add tags during project creation

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Tags provide a way to create annotations for resources. You can add tags at the time of creating projects. You must assign the **Tag User** role while adding tags. For more information on the permissions assigned to this role, see [Manage tags on resources](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#required-permissions-attach). You can only add the namespace for the tag key-value pairs in one of the following ways:

### gcloud

To add tags during project creation, run the following command:
    
    
    gcloud projects create PROJECT_ID --organization=ORGANIZATION_ID --tags=KEY_VALUE_PAIRS
    

Replace the following:

  * PROJECT_ID is the unique identifier of the project.
  * ORGANIZATION_ID is the unique identifier of the organization.
  * KEY_VALUE_PAIRS is a comma-separated list of key-value pairs that you can assign to your resource. An example of comma-separated key-value pairs is `123/environment=production, 456/create=testresource`. In this example, `123` and `456` are the unique identifiers (IDs) of the organization or folder resources where the tag keys are defined.



### REST

The following snippet is a JSON request where you create a project and add tags to it.
    
    
      POST https://cloudresourcemanager.googleapis.com/v3/projects/
      Authorization: *************
      Content-Type: application/json
    
      {
        "projectId": "our-project-456",
        "name": "my project",
        "parent": "organizations/123",
        "tags": {
          "key": "123/environment"
          "value": "production"
        },
    "tags": {
          "key": "123/costCenter"
          "value": "marketing"
      }
    }
    

### Designate project environments with tags

You can use tags to visually distinguish projects based on their environment, such as production, staging, or development. This helps prevent errors and improves awareness when you are working in sensitive environments. Google adds a visual indicator to the project in the Google Cloud console project picker when a project with a specific tag key-value pair is selected. This indicator reminds you that any changes could affect your associated production or non-production applications. Tags can either be inherited by the project or set directly on the project.

To use this feature, do the following:

  1. [Create a tag key](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#creating-tag-key) named `environment`.
  2. [Create tag values](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#creating-tag-value) for the environment categories you use. The following values are supported and are mapped to a corresponding badge in the console's project picker: 
     * Prod: Prod, prod, Production, production
     * Dev: Dev, dev, Development, development
     * Test: Test, test, Testing, testing, QA, qa, Quality assurance, quality assurance
     * Staging: Staging, staging, Stage, stage
  3. [Attach the appropriate tag to your project](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#attaching) by creating a tag binding.



If a project has multiple environment tags (for example, one inherited from a folder and one directly on the project), the most specific tag is used to determine the badge.

**Note:** To see environment badges in the **project picker** , users must have the Tag Viewer role (`roles/resourcemanager.tagViewer`) at the organization or folder level.

### Creating a project using a service account

You can use a service account to automate project creation. Like user accounts, service accounts can be granted permission to create projects within an organization resource. Service accounts are not allowed to create projects outside of an organization resource and must specify the parent resource when creating a project. Service accounts can create a new project using the gcloud CLI or the `projects.create()` method.

## Managing project quotas

The number of projects any user or service account can create is limited. If you create a project outside an organization resource, the quota on your user account is used. If you are creating a project within an organization resource, the quota on both your user account and the organization resource are checked. If either one has quota remaining, the project can be created.

If you have fewer than 30 projects remaining in your quota, a notification displays the number of projects remaining in your quota on the [**New Project**](https://console.cloud.google.com/projectcreate) page. After you have reached your project limit, to create more projects you must request a project limit increase. Alternatively, you can schedule some projects to be deleted after 30 days on the [Manage Resources page](https://console.cloud.google.com/cloud-resource-manager). Projects that users have [soft-deleted](https://docs.cloud.google.com/resource-manager/docs/delete-restore-projects#shutting_down_projects) count against your quota. These projects are fully deleted after 30 days.

To request additional capacity for projects in your organization quota, do the following:

  1. Go to the **Quotas & System Limits** page.

[Go to Quotas & System Limits](https://console.cloud.google.com/iam-admin/quotas)

  2. From the resource selector, select the organization for which you want to increase the project quota.

  3. In the **Filter** option, select **Metric** and enter `cloudresourcemanager.googleapis.com/projects_count`.

  4. Select **Cloud Resource Manager API** , click more_vert  **More actions** , and then select edit **Edit quota**.

  5. In the **Quota changes** dialog, enter a new quota value and a description, and then click **Next**.

  6. Enter your contact details and click **Submit request**.




You receive an email acknowledging receipt of your request. If you need further assistance, respond to the email. After the review, you receive an email notification indicating whether your request was approved.

If you don't have an organization and want to request additional capacity for projects in your quota, then use the [Request Project Quota Increase](https://support.google.com/code/contact/project_quota_increase) form.

For more information about quotas and why they are used, see the [Free Trial Project Quota Requests](https://support.google.com/cloud/answer/6330231) support page. For more information about billing reports, see the [Billing Reports](https://docs.cloud.google.com/billing/docs/how-to/reports) support page.

## What's next

  * Learn about [viewing and updating projects](https://docs.cloud.google.com/resource-manager/docs/view-update-projects).
  * Learn about [deleting and restoring projects](https://docs.cloud.google.com/resource-manager/docs/delete-restore-projects).
  * Learn how to [move a project within your resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/moving-projects-folders).
  * Learn how to [migrate a project from one organization resource to another](https://docs.cloud.google.com/resource-manager/docs/project-migration).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
