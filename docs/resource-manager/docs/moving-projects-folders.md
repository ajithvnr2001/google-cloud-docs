---
url: https://docs.cloud.google.com/resource-manager/docs/moving-projects-folders/
title: Move a project \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:44:05.219288+00:00
---

# Move a project  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/moving-projects-folders/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview)



Send feedback 

#  Move a project Stay organized with collections  Save and categorize content based on your preferences. 

This guide explains how to move a project within your organization resource.

The project is the base-level organizing entity in a Google Cloud organization resource. Projects are created under organization resources, and can be placed under folders or the organization resource itself, forming the [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). You can move project resources within your resource hierarchy, but should consider the policy implications of the move before you make it.

**Note:** The following instructions are only for moving a project within an organization resource. For information about migrating a project between organization resources, see [Migrating projects](https://docs.cloud.google.com/resource-manager/docs/project-migration).

When you move a project, any Identity and Access Management policies or organization policies that are directly attached will move with it. However, a project in your resource hierarchy is also affected by the policies that it inherits from parent resources. If a project inherits an IAM role that provides users permission to use a particular service, users won't have access to that service at the destination unless it would inherit the permission at the destination as well.

For example, consider a service account has the **Storage Object Creator** role bound to a user at Folder A. The service account has permissions to upload data to Cloud Storage in any project in Folder A. If you moved one of these projects to Folder B, which does not have the same inherited permissions, the service account for that project loses the ability to upload data, resulting in a service outage.

These same considerations apply if organization policies are defined at the source and destination folders. Like IAM policies, organization policies are inherited. Consequently, you must ensure that your organization policies are consistent between source and destination folders.

To learn more about organization policies, see [Introduction to the organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview).

To move a project, you need the Project Mover IAM role (`roles/resourcemanager.projectMover`) on both the source folder and the destination folder. If the resource is not in a folder, you need this role on the organization resource.

These roles give you the following required permissions:

  * `resourcemanager.projects.update` on the project
  * **If the resource is in a folder:** `resourcemanager.projects.move` on the source folder and the destination
  * **If the resource is not in a folder:** `resourcemanager.projects.move` on the organization resource



You can also gain these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles), or other predefined roles.

### Console

To move a project:

  1. In the Google Cloud console, go to the **Manage resources** page. 

[ Go to Manage resources](https://console.cloud.google.com/cloud-resource-manager)

  2. Select your Organization from the **Organization** drop-down on the top left of the page.

  3. Click the project's row to select your project from the list of resources. Note that you _must not_ click the name of the project, which takes you to the project's Identity and Access Management (IAM) page.

  4. Click the options menu (the vertical ellipsis) in the row and click **Move**.

  5. Click **Browse** to select the folder to which you want to move the project.

  6. Click **Move**.




### gcloud

To move a project, run the [`gcloud beta projects move`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/projects/move) command:
    
    
    gcloud beta projects move PROJECT_ID \
       --DESTINATION_TYPE DESTINATION_ID

Replace the following:

  * `PROJECT_ID`: The ID or number of the project you want to move.
  * `DESTINATION_TYPE`: The type of the destination, either `organization` or `folder`.
  * `DESTINATION_ID`: The ID of the organization resource or folder where you want to move the project.



### REST

You can use the v3 [`projects.move`](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/move) method to move a project.

Request:
    
    
    POST https://cloudresourcemanager.googleapis.com/v3/{name=PROJECT_NAME}:move
    {
      "destinationParent": DESTINATION_PARENT
    }
    

Replace the following:

  * `PROJECT_NAME`: the name of the project you want to update. For example, `projects/415104041262`

  * `DESTINATION_PARENT`: the new parent organization resource or folder under which you want to move the project. For example: `organizations/12345678901`




If successful, the request will return an [Operation](https://docs.cloud.google.com/resource-manager/reference/rest/Shared.Types/Operation) which can be used to track the project move.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
