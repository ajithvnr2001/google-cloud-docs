---
url: https://docs.cloud.google.com/vpc-service-controls/docs/configure-folder/
title: Configure folders in service perimeters \u00a0|\u00a0 VPC Service Controls \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:06.101923+00:00
---

# Configure folders in service perimeters  |  VPC Service Controls  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc-service-controls/docs/configure-folder/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ VPC Service Controls ](https://docs.cloud.google.com/vpc-service-controls/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc-service-controls/docs/overview)



Send feedback 

#  Configure folders in service perimeters Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure [Google Cloud folders as members in service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/folder-membership).

## Before you begin

  * Read about [creating service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters).

  * Verify that you have the [permissions required](https://docs.cloud.google.com/vpc-service-controls/docs/access-control) to create and manage service perimeters (`roles/accesscontextmanager.policyAdmin`).

  * [Identify the IDs of the folders](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders#view-folder) that you want to add to service perimeters.




## Add folders to a perimeter

You can configure a perimeter to include folders as protected resources when you [create](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters) or [update](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#update) a perimeter.

### Console

  1. In the Google Cloud console navigation menu, click **Security > VPC Service Controls**.

[Go to VPC Service Controls](https://console.cloud.google.com/security/service-perimeter)

  2. To create a new perimeter, click **New perimeter**.

To modify an existing perimeter, select the perimeter and click **Edit**.

  3. Select **Resources to protect**.

  4. In the **Resources to protect** pane, click **Add folders**.

  5. In the **Search folders** dialog, search for and select the folders that you want to protect.

  6. Click **Select**. The added folders appear in the **Folders** section.

  7. Click **Continue**.

  8. Click **Create** or **Save**.




For information about other perimeter configurations, see [Create a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters#console).

### gcloud

  * To create a perimeter in [enforced mode](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters#enforced-mode) and include folders as protected resources, run the following [`perimeters create`](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/create) command:
        
        gcloud access-context-manager perimeters create NAME \
            --title=TITLE \
            --resources=FOLDER_ID \
            --restricted-services=RESTRICTED-SERVICES \
            --policy=POLICY_NAME

To create a perimeter in [dry run mode](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters#dry-run-mode) and include folders as protected resources, use the [`perimeters dry-run create`](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/dry-run/create) command.

  * To update an existing perimeter in enforced mode and include folders as protected resources, run the following [`perimeters update`](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/update) command:
        
        gcloud access-context-manager perimeters update \
            PERIMETER_ID \
            --add-resources=FOLDER_ID

To update an existing perimeter in dry run mode and include folders as protected resources, use the [`perimeters dry-run update`](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/dry-run/update) command.




Replace FOLDER_ID with a comma-separated list of one or more folder IDs. For example, `folders/12345`. The `--resources` and `--add-resources` arguments also support projects and VPC networks.

For information about other perimeter configurations, see [Create a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters#gcloud).

## Remove folders from a perimeter

You can remove folders from an existing perimeter.

### Console

  1. In the Google Cloud console navigation menu, click **Security > VPC Service Controls**.

[Go to VPC Service Controls](https://console.cloud.google.com/security/service-perimeter)

  2. To modify an existing perimeter, select the perimeter and click **Edit**.

  3. Select **Resources to protect**.

  4. In the **Folders** section of the **Resources to protect** pane, select the folders that you want to remove.

  5. Click **Remove selected**.

  6. Click **Continue**.

  7. Click **Save**.




For more information, see [Update a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#update).

### gcloud

To remove folders from an existing perimeter in enforced mode, run the following [`perimeters update`](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/update) command:
    
    
    gcloud access-context-manager perimeters update \
        PERIMETER_ID \
        --remove-resources=FOLDER_ID

To remove folders from an existing perimeter in dry run mode, use the [`perimeters dry-run update`](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/perimeters/dry-run/update) command.

Replace FOLDER_ID with a comma-separated list of one or more folder IDs. For example, `folders/12345`. The `--remove-resources` argument also supports projects and VPC networks.

For more information, see [Update a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#update).

## Look up configured perimeters for a resource

Use the gcloud CLI or the `LookupConfiguredServicePerimeter` API method to see which enforced or dry run service perimeters apply to a project or folder.

### gcloud

To look up the configured perimeter for a project or folder, run the following [`lookup-configured-perimeter`](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager/lookup-configured-perimeter) command:
    
    
    gcloud access-context-manager lookup-configured-perimeter \
        --resource=RESOURCE

Replace RESOURCE with the resource name in the format `projects/PROJECT_NUMBER` or `folders/FOLDER_NUMBER`.

### API

To look up the configured perimeter for a project, call the `LookupConfiguredServicePerimeter` method:
    
    
    GET https://accesscontextmanager.googleapis.com/v1/projects/PROJECT_NUMBER:lookupConfiguredServicePerimeter
    

To look up the configured perimeter for a folder, call the `LookupConfiguredServicePerimeter` method:
    
    
    GET https://accesscontextmanager.googleapis.com/v1/folders/FOLDER_NUMBER:lookupConfiguredServicePerimeter
    

### Required permissions

To query configured perimeters for a resource, ensure that you have the following IAM permissions on the relevant Access Policies:

  * `accesscontextmanager.policies.get`
  * `accesscontextmanager.servicePerimeters.list`



### Example response
    
    
    {
      "servicePerimeter": "accessPolicies/123456/servicePerimeters/my_enforced_perimeter",
      "servicePerimeterDryRun": "accessPolicies/123456/servicePerimeters/my_dry_run_perimeter",
      "restrictedResource": "folders/789012",
      "restrictedResourceDryRun": "projects/345678"
    }
    

In this example, the project inherits the enforced perimeter from the `folders/789012` ancestor folder. In contrast, the dry run perimeter is configured directly on the `projects/345678` project.

## Manage projects in a perimeter using folders

You can add or remove a project indirectly from a perimeter by moving the project into or out of a folder that you have configured in the perimeter. For more information, see [Move a project into a folder](https://docs.cloud.google.com/resource-manager/docs/manage-projects-within-folder#move-project-into-folder).

For information about adding or removing projects explicitly from a perimeter, see [Update a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#update).

## Troubleshoot

If you encounter issues or unexpected behavior while configuring folder memberships, do the following:

  * Look up the configured perimeters for the resource to confirm whether the resource inherits a perimeter from an ancestor folder.
  * Check audit logs for perimeter violation details. For more information, see [Retrieve troubleshooting information from audit logs](https://docs.cloud.google.com/vpc-service-controls/docs/retrieve-troubleshoot-errors).
  * Verify that projects migrated to folder-based perimeters have completed the 48-hour hierarchy propagation window before removing explicit project bindings.



## What's next

  * Learn more about [dry run mode](https://docs.cloud.google.com/vpc-service-controls/docs/dry-run-mode).
  * Learn more about [ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules).
  * Learn more about [troubleshooting common issues](https://docs.cloud.google.com/vpc-service-controls/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
