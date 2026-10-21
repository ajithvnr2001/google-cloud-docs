---
url: https://docs.cloud.google.com/compute/docs/instances/manage-shared-reservations-creation/
title: Manage shared reservation creation \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:19:27.607948+00:00
---

# Manage shared reservation creation  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/manage-shared-reservations-creation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Manage shared reservation creation Stay organized with collections  Save and categorize content based on your preferences. 

By default, projects can't create or modify shared reservations. This document explains how to allow or restrict projects in your Google Cloud organization from creating and modifying shared reservations. Shared reservations help you maximize reserved capacity usage across projects, as well as manage one reservation instead of many.

To learn more about the best practices for creating and using shared reservations, see [Best practices for shared reservations](https://docs.cloud.google.com/compute/docs/instances/best-practices-shared-reservations).

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).




### Required roles

To get the permissions that you need to allow or restrict projects from creating shared reservations, ask your administrator to grant you the [Organization Policy Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) (`roles/orgpolicy.policyAdmin`) IAM role on the organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to allow or restrict projects from creating shared reservations. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to allow or restrict projects from creating shared reservations:

  * To edit organization policies: `orgpolicy.policy.set` on the organization 
  * To view organization policies: `orgpolicy.policy.get` on the organization 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Allow or restrict projects from creating shared reservations

To allow or restrict a project from creating shared reservations, modify the allowlist within the [**shared reservations owner projects** (`compute.sharedReservationsOwnerProjects`) organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints#:%7E:text=compute.sharedReservationsOwnerProjects).

The following sections explain how to view or edit the shared reservations policy constraint in your project or organization.

### View the shared reservations organization policy constraint

To view if your project or organization has the shared reservations owner projects (`compute.sharedReservationsOwnerProjects`) constraint enabled, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Organization policies** page.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the project or organization for which you want to view organization policies.

  3. In the filter_list **Filter** field, enter `constraints/compute.sharedReservationsOwnerProjects`.

  4. In the **Name** column, click **Shared reservations owner projects**. The **Policy details** page appears.

  5. In the **Effective policy** section, verify whether your project or organization is allowed to create and modify shared reservations.




###  gcloud 

To view which projects the `compute.sharedReservationsOwnerProjects` constraint allows to create and modify shared reservations:

  1. To download the policy for your organization as a file named `policy.yaml`, use the [`gcloud resource-manager org-policies describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/describe):
         
         gcloud resource-manager org-policies describe compute.sharedReservationsOwnerProjects \
             --organization=ORGANIZATION_ID > policy.yaml
         

Replace ORGANIZATION_ID with the [ID of your organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).

  2. Open the `policy.yaml` file in a text editor of your choice.

  3. View the `compute.sharedReservationsOwnerProjects` constraint. The projects that can create and modify shared reservations are listed in the `allowedValues` field, as shown in the following example:
         
         ...
         constraint: constraints/compute.sharedReservationsOwnerProjects
         listPolicy:
           allowedValues:
           - projects/EXAMPLE_PROJECT_NUMBER1
           - projects/EXAMPLE_PROJECT_NUMBER2
           - projects/EXAMPLE_PROJECT_NUMBER3
           ...
         ...
         

  4. Optional: To delete the `policy.yaml` file, do one of the following:

     * If you're using a Linux or macOS terminal, then run the following command:
           
           rm policy.yaml
           

     * If you're using a Windows terminal, then run the following command:
           
           del policy.yaml
           




### Edit the shared reservations organization policy constraint

To edit which projects in your organization can create and modify shared reservations, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Organization policies** page.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the organization for which you want to edit organization policies.

  3. In the filter_list **Filter** field, enter `constraints/compute.sharedReservationsOwnerProjects`.

  4. In the **Name** column, click **Shared reservations owner projects**. The **Policy details** page appears.

  5. Click edit **Manage policy**. The **Policy details** page appears.

  6. Select **Override parent's policy**. Then, in the **Policy enforcement** section, select how you want to apply the policy:

     * **Merge with parent** : this option combines the project-level policy with the organization-level policy. Projects allowed at either level can create shared reservations.

     * **Replace** : this option overrides any inherited policies from higher levels. Only projects that are explicitly allowed at this level can create shared reservations.

  7. Click add **Add a rule**.

  8. In the **Policy values** list, select **Custom**.

  9. In the **Policy type** list, select one of the following options:

     * To authorize one or more projects to create or modify shared reservations, select **Allow**.

     * To prevent one or more projects from creating or modifying shared reservations, select **Deny**.

  10. In the **Custom value** field, enter the number of the project that you want to apply this rule to. For each additional project that you want to apply the rule to, click **Add value** , and then repeat this step.

  11. To apply these changes, click **Set policy**. The **Organization policies** page appears.




###  gcloud 

To edit which projects the `compute.sharedReservationsOwnerProjects` constraint allows to create and modify shared reservations, use one of the following methods:

  * To grant permission to a single project to create and modify shared reservations, use the [`gcloud resource-manager org-policies allow` command](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/allow). You can repeat this command for each project that you want to grant this permission to.
        
        gcloud resource-manager org-policies allow compute.sharedReservationsOwnerProjects projects/PROJECT_NUMBER \
            --organization=ORGANIZATION_ID
        

Replace the following:

    * PROJECT_NUMBER: the [number of the project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

    * ORGANIZATION_ID: the [ID of your organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).

  * To grant or revoke the permissions to multiple projects to create and modify shared reservations, replace the organization policy constraint. To do so, complete the following steps:

    1. To download the policy for your organization as a file named `policy.yaml`, use the [`gcloud resource-manager org-policies describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/describe):
           
           gcloud resource-manager org-policies describe compute.sharedReservationsOwnerProjects \
               --organization=ORGANIZATION_ID > policy.yaml
           

    2. Open the `policy.yaml` file in a text editor of your choice.

    3. Modify the `allowedValues` field to list all projects that can create and modify shared reservations.

       * For each project that you want to grant permission to, add the project number in a new line within the `allowedValues` field.

       * For each project that you want to revoke the permission to create and modify shared reservations, remove the project number from within the `allowedValues` field.

The `policy.yaml` file looks similar to the following example:
    
    ...
    constraint: constraints/compute.sharedReservationsOwnerProjects
    listPolicy:
      allowedValues:
      - projects/EXAMPLE_PROJECT_NUMBER1
      - projects/EXAMPLE_PROJECT_NUMBER2
      - projects/EXAMPLE_PROJECT_NUMBER3
      ...
    ...
    

    4. Save the `policy.yaml` file and close the text editor.

    5. To update the policy for your organization, use the [`gcloud resource-manager org-policies set-policy` command](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/org-policies/set-policy):
           
           gcloud resource-manager org-policies set-policy \
               --organization=ORGANIZATION_ID policy.yaml
           

    6. Optional: To delete the `policy.yaml` file, do one of the following:

       * If you're using a Linux or macOS terminal, then run the following command:
             
             rm policy.yaml
             

       * If you're using a Windows terminal, then run the following command:
             
             del policy.yaml
             




Changes can take up to 15 minutes to take effect.

## What's next

  * [Create a shared reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-shared)

  * [Create a shared future reservation request](https://docs.cloud.google.com/compute/docs/instances/create-shared-future-reservations)

  * [Create a shared future reservation request in calendar mode](https://docs.cloud.google.com/compute/docs/instances/create-future-reservations-calendar-mode)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
