---
url: https://docs.cloud.google.com/number-registry/set-up-cloud-number-registry/
title: Set up Cloud Number Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:20:01.174292+00:00
---

# Set up Cloud Number Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/number-registry/set-up-cloud-number-registry/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Number Registry ](https://docs.cloud.google.com/number-registry)
  * [ Guides ](https://docs.cloud.google.com/number-registry/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up Cloud Number Registry

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page explains how to set up [Cloud Number Registry](https://docs.cloud.google.com/number-registry/cloud-number-registry) in your organization.

## Before you begin

  1. [Designate a project to use for Cloud Number Registry in this organization](https://docs.cloud.google.com/number-registry/designate-project-cloud-number-registry).
  2. Select the designated project to perform the steps in this guide.
  3. Verify that you have the permissions required to complete this guide.



### Required roles

To get the permissions that you need to set up and manage Cloud Number Registry, ask your administrator to grant you the [Cloud Number Registry IPAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamAdmin) (`roles/cloudnumberregistry.ipamAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create an IPAM admin scope

When you create the IPAM admin scope, Cloud Number Registry performs setup tasks and identifies supported Compute Engine resources in your organization and adds them to a default registry book.

It can take up to 24 hours for all resources in the organization to be discovered. You can view the status of the IPAM admin scope to check if resource discovery is complete.

You can manage Cloud Number Registry through this default registry book, or you optionally [create additional registry books](https://docs.cloud.google.com/number-registry/create-registry-books-realms-custom-ranges) to organize your resources.

If you get an error when you try to create an IPAM admin scope, see Troubleshooting.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Number Registry** page.

[Go to Cloud Number Registry](https://console.cloud.google.com/cloud-number-registry/overview)

  2. Click the **Manage** tab.

  3. In the **Manage IPAM admin scope** panel, click **Create IPAM admin scope**.




The IPAM admin scope creation process starts. To check the progress of setup, view the status of the IPAM admin scope.

###  gcloud 

Create the IPAM admin scope by using the [`gcloud alpha number-registry ipam-admin-scopes create` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/number-registry/ipam-admin-scopes/create).

To check the progress of the Cloud Number Registry setup, view the status of the IPAM admin scope.
    
    
    gcloud alpha number-registry ipam-admin-scopes create SCOPE_NAME \
        --enabled-addon-platforms=COMPUTE_ENGINE \
        --scopes=organizations/ORGANIZATION_ID \
        --location=global
    

Replace the following:

  * `SCOPE_NAME`: a name for the IPAM admin scope
  * `ORGANIZATION_ID`: the ID number of the organization that you want to manage.



## View the status of the IPAM admin scope

The admin scope can have the following statuses during setup:

  * `SETUP_IN_PROGRESS`: setup has started but the discovery process isn't complete. It can take up to 24 hours for all existing resources in the organization to be discovered. However, any new resources that are created in the organization are discovered within a few minutes.
  * `READY_TO_USE`: the discovery process is complete and Cloud Number Registry is ready to use.




###  Console 

  1. In the Google Cloud console, go to the **Cloud Number Registry** page.

[Go to Cloud Number Registry](https://console.cloud.google.com/cloud-number-registry/overview)

  2. Click the **Manage** tab.

  3. In the **Manage IPAM admin scope** panel, view the **State** field.




###  gcloud 

View details about the IPAM admin scope by using the [`gcloud alpha number-registry ipam-admin-scopes describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/number-registry/ipam-admin-scopes/describe).
    
    
    gcloud alpha number-registry ipam-admin-scopes describe SCOPE_NAME \
        --location=global
    

Replace `SCOPE_NAME` with the IPAM admin scope name.

## Troubleshooting

The following sections explain how to resolve issues that you might encounter when setting up Cloud Number Registry.

### IPAM admin scope creation fails with `ALREADY_EXISTS` or `INVALID_ARGUMENT` error

If creation of the IPAM admin scope fails due to either of these errors, this is because an IPAM admin scope already exists in the project.

  * An IPAM admin scope with the same name already exists in this project:
        
        ALREADY_EXISTS: Resource 'projects/PROJECT_ID/locations/global/ipamAdminScopes/SCOPE_NAME'
        already exists.
        

  * An IPAM admin scope with a different name already exists in this project:
        
        INVALID_ARGUMENT: Violation in ipam_admin_scope.scopes: Scope
        organizations/ORGANIZATION_ID is already administered by another ipam admin scope
        'projects/PROJECT_ID/locations/global/ipamAdminScopes/EXISTING_SCOPE_NAME'
        




### IPAM admin scope creation fails with `FAILED_PRECONDITION` error

If creation of an IPAM admin scope fails with the following error message, this means that this project hasn't been designated to use for Cloud Number Registry for this organization.
    
    
    FAILED_PRECONDITION: There is no existing registry for 'projects/PROJECT_ID in scope
    organizations/ORGANIZATION_ID'
    

To resolve this issue, do the following:

  1. [Check if Cloud Number Registry is already set up for this organization](https://docs.cloud.google.com/number-registry/designate-project-cloud-number-registry#verify-project) in another project.

  2. If Cloud Number Registry isn't set up for this organization, [check if a project is already designated for Cloud Number Registry](https://docs.cloud.google.com/number-registry/designate-project-cloud-number-registry#view-designated-project) in this organization.

  3. If no project is designated, ask your organization's administrator to [designate a project for use with Cloud Number Registry](https://docs.cloud.google.com/number-registry/designate-project-cloud-number-registry#designate-project) or grant you access to do so.




## What's next

  * [Create registry books, realms, and custom ranges](https://docs.cloud.google.com/number-registry/create-registry-books-realms-custom-ranges)
  * [Query Cloud Number Registry](https://docs.cloud.google.com/number-registry/query-cloud-number-registry)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
