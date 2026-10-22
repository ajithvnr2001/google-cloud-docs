---
url: https://docs.cloud.google.com/number-registry/designate-project-cloud-number-registry/
title: Designate a project to use for Cloud Number Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:59:19.672462+00:00
---

# Designate a project to use for Cloud Number Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/number-registry/designate-project-cloud-number-registry/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Number Registry ](https://docs.cloud.google.com/number-registry)
  * [ Guides ](https://docs.cloud.google.com/number-registry/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Designate a project to use for Cloud Number Registry

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page explains how to designate a project to use for [Cloud Number Registry](https://docs.cloud.google.com/number-registry/cloud-number-registry). Only one project in each organization can use Cloud Number Registry. Before you can set up Cloud Number Registry, an Organization Administrator must designate which project can be used by creating an `org-number-registries` resource.

## Before you begin

  1. Create or select a project to use to manage Cloud Number Registry for the parent organization. We strongly recommend creating a dedicated project for this purpose. For more information, see [ Project designation for Cloud Number Registry](https://docs.cloud.google.com/number-registry/overview#project-designation). 
     1. In the Google Cloud console, go to the project selector page.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

     2. Select or create a Google Cloud project.

**Roles required to select or create a project**

        * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
        * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
  2. Enable the Cloud Number Registry API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudnumberregistry.googleapis.com)

  3. Verify that you have the permissions required to complete this guide.



### Required roles

To get the permissions that you need to designate a project to use for Cloud Number Registry, ask your administrator to grant you the [Cloud Number Registry IPAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamAdmin) (`roles/cloudnumberregistry.ipamAdmin`) IAM role on the parent organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Optional: Check if Cloud Number Registry is configured

Only one project in each organization can configure Cloud Number Registry. You can check if Cloud Number Registry is already configured in your organization from any project in the organization.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Number Registry** page.

[Go to Cloud Number Registry](https://console.cloud.google.com/cloud-number-registry/overview)

     * If Cloud Number Registry is already configured in this organization, you are redirected to the project that manages Cloud Number Registry.
     * If Cloud Number Registry isn't configured for this organization, a **Create admin scope** button is displayed.



###  gcloud 

Check if Cloud Number Registry is already configured in your organization by using the [`gcloud alpha number-registry ipam-admin-scopes check-availability` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/number-registry/ipam-admin-scopes/check-availability).

  * If Cloud Number Registry is already configured, the response is `UNAVAILABLE`.
  * If there's no existing configuration, the response is `AVAILABLE`.


    
    
    gcloud alpha number-registry ipam-admin-scopes check-availability \
        --scopes=organizations/ORGANIZATION_ID \
        --location=global
    

Replace `ORGANIZATION_ID` with the ID number of the organization that you want to manage.

## Designate a project to use for Cloud Number Registry

To designate a project to use for Cloud Number Registry, you create an `org-number-registries` resource that defines which project can be used to set up Cloud Number Registry for its parent organization.

When you [set up Cloud Number Registry](https://docs.cloud.google.com/number-registry/set-up-cloud-number-registry), Google Cloud checks that you're creating the IPAM admin scope in a project that matches the project defined in the `org-number-registries` resource.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Number Registry** page.

[Go to Cloud Number Registry](https://console.cloud.google.com/cloud-number-registry/overview)

  2. Click the **Manage** tab.

  3. In the **Manage designated project** panel, in the **Admin project** field, click **Select** and select the project that you want to use for Cloud Number Registry.

  4. Click **Designate project**.




###  gcloud 

Designate a project to use for Cloud Number Registry by using the [`gcloud alpha number-registry org-number-registries create` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/number-registry/org-number-registries/create).
    
    
    gcloud alpha number-registry org-number-registries create ORG_NUMBER_REGISTRY \
        --admin-project=projects/PROJECT_ID \
        --target-scopes=organizations/ORGANIZATION_ID \
        --organization=ORGANIZATION_ID \
        --location=global
    

Replace the following:

  * `ORG_NUMBER_REGISTRY`: a name for the organization number registry resource.
  * `PROJECT_ID`: the ID number of the project that you want to use to contain Cloud Number Registry information.
  * `ORGANIZATION_ID`: the ID number of the organization that you want to manage.



## List and view project designations

You can view which project has been designated to use with Cloud Number Registry.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Number Registry** page.

[Go to Cloud Number Registry](https://console.cloud.google.com/cloud-number-registry/overview)

  2. Click the **Manage** tab.

  3. In the **Manage designated project** panel, view the **Admin project** field.




###  gcloud 

  * To list project designations for Cloud Number Registry, use the [`gcloud alpha number-registry org-number-registries list` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/number-registry/org-number-registries/list).
        
        gcloud alpha number-registry org-number-registries list \
            --organization=ORGANIZATION_ID \
            --location=global
        

Replace `ORGANIZATION_ID` with the ID number of the organization that you're managing.

  * To view details for a project designation for Cloud Number Registry, use the [`gcloud alpha number-registry org-number-registries describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/number-registry/org-number-registries/describe).
        
        gcloud alpha number-registry org-number-registries describe ORG_NUMBER_REGISTRY \
            --organization=ORGANIZATION_ID \
            --location=global
        

Replace the following:

    * `ORG_NUMBER_REGISTRY`: the name of the organization number registry resource.
    * `ORGANIZATION_ID`: the ID number of the organization that you're managing.



## Delete a project designation

If a project designation exists, but Cloud Number Registry isn't set up in the project, you can delete the `org-number-registries` resource that designates the project.

If Cloud Number Registry is already set up in the project, you must [decommission Cloud Number Registry](https://docs.cloud.google.com/number-registry/decommission-cloud-number-registry) before you can delete the project designation.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Number Registry** page.

[Go to Cloud Number Registry](https://console.cloud.google.com/cloud-number-registry/overview)

  2. Click the **Manage** tab.

  3. In the **Manage designated project** panel, click **Remove project designation**.




###  gcloud 

Delete a project designation by using the [`gcloud alpha number-registry org-number-registries delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/number-registry/org-number-registries/delete).
    
    
    gcloud alpha number-registry org-number-registries delete ORG_NUMBER_REGISTRY \
        --organization=ORGANIZATION_ID \
        --location=global
    

Replace the following:

  * `ORG_NUMBER_REGISTRY`: the name of the organization number registry resource.
  * `ORGANIZATION_ID`: the ID number of the organization that you're managing.



## What's next

  * [Set up Cloud Number Registry](https://docs.cloud.google.com/number-registry/set-up-cloud-number-registry).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
