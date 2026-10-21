---
url: https://docs.cloud.google.com/number-registry/decommission-cloud-number-registry/
title: Decommission Cloud Number Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:20:01.561289+00:00
---

# Decommission Cloud Number Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/number-registry/decommission-cloud-number-registry/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Number Registry ](https://docs.cloud.google.com/number-registry)
  * [ Guides ](https://docs.cloud.google.com/number-registry/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Decommission Cloud Number Registry

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page explains how to decommission [Cloud Number Registry](https://docs.cloud.google.com/number-registry/cloud-number-registry) in your organization.

## Before you begin

  1. Select the project in your organization that has been configured to provide Cloud Number Registry access.
  2. Verify that you have the permissions required to complete this guide.



### Required roles

To get the permissions that you need to decommission Cloud Number Registry, ask your administrator to grant you the [Cloud Number Registry IPAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamAdmin) (`roles/cloudnumberregistry.ipamAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View the status of the IPAM admin scope

As you go through the decommission process, the IPAM admin scope has different statuses. Check the status to determine which step needs to be taken.

  * `READY_TO_USE`: Cloud Number Registry is active and in use.

From this state, you can disable the IPAM admin scope.

  * `DISABLED`: the IPAM admin scope is disabled.

From this state, you can clean up the IPAM admin scope.

  * `CLEANUP_IN_PROGRESS`: a clean up operation is in progress.

You must wait for cleanup to complete before you can proceed.

  * `READY_FOR_DELETION`: the clean up operation is completed.

From this state, you can delete the IPAM admin scope.




###  Console 

  1. In the Google Cloud console, go to the **Cloud Number Registry** page.

[Go to Cloud Number Registry](https://console.cloud.google.com/cloud-number-registry/overview)

  2. Click **Manage Cloud Number Registry**.

  3. The status is displayed in the **Admin scope state** field.




###  gcloud 

View details about the IPAM admin scope by using the [`gcloud alpha number-registry ipam-admin-scopes describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/number-registry/ipam-admin-scopes/describe).
    
    
    gcloud alpha number-registry ipam-admin-scopes describe SCOPE_NAME \
        --location=global
    

Replace `SCOPE_NAME` with the IPAM admin scope name.

## Disable the IPAM admin scope

Disabling the IPAM admin scope stops Cloud Number Registry from making updates to the discovered resources, and prevents you from creating any user-managed resources.

Check that the status of the IPAM admin scope is in the `READY_TO_USE` state before you disable it.

**Caution:** Disabling the IPAM admin scope can't be undone. If you change your mind after you disable Cloud Number Registry, you must complete the decommission steps described on this page, and then [set up Cloud Number Registry](https://docs.cloud.google.com/number-registry/set-up-cloud-number-registry) again.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Number Registry** page.

[Go to Cloud Number Registry](https://console.cloud.google.com/cloud-number-registry/overview)

  2. Click **Manage Cloud Number Registry**.

  3. Click **Disable admin scope**.




###  gcloud 

Disable the IPAM admin scope by using the [`gcloud alpha number-registry ipam-admin-scopes disable` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/number-registry/ipam-admin-scopes/disable).
    
    
    gcloud alpha number-registry ipam-admin-scopes disable SCOPE_NAME \
        --location=global
    

Replace `SCOPE_NAME` with the IPAM admin scope name.

## Clean up the IPAM admin scope

Clean up the IPAM admin scope to remove all Cloud Number Registry resources except for the IPAM admin scope and the default registry book. All realms and discovered ranges in the registry book are deleted.

Check that the status of the IPAM admin scope is `DISABLED` before you clean up the IPAM admin scope.

**Caution:** Cleaning up the IPAM admin scope can't be undone.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Number Registry** page.

[Go to Cloud Number Registry](https://console.cloud.google.com/cloud-number-registry/overview)

  2. Click **Manage Cloud Number Registry**.

  3. Click **Cleanup admin scope**.




###  gcloud 

Clean up the IPAM admin scope by using the [`gcloud alpha number-registry ipam-admin-scopes cleanup` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/number-registry/ipam-admin-scopes/cleanup).
    
    
    gcloud alpha number-registry ipam-admin-scopes cleanup SCOPE_NAME \
        --location=global
    

Replace `SCOPE_NAME` with the IPAM admin scope name.

## Delete the IPAM admin scope

Deleting the IPAM admin scope removes all Cloud Number Registry information.

Check that the status of the IPAM admin scope is `READY_FOR_DELETION` before you delete the IPAM admin scope. If the status is `CLEANUP_IN_PROGRESS`, check back in a few minutes.

**Caution:** Deleting the IPAM admin scope can't be undone.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Number Registry** page.

[Go to Cloud Number Registry](https://console.cloud.google.com/cloud-number-registry/overview)

  2. Click **Manage Cloud Number Registry**.

  3. Click **Delete admin scope**.




###  gcloud 

Delete the IPAM admin scope by using the [`gcloud alpha number-registry ipam-admin-scopes delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/number-registry/ipam-admin-scopes/delete).
    
    
    gcloud alpha number-registry ipam-admin-scopes delete SCOPE_NAME \
        --location=global
    

Replace `SCOPE_NAME` with the IPAM admin scope name.

## Delete the project designation

During initial setup, this project was designated to use for Cloud Number Registry. If you're no longer using Cloud Number Registry with this project and want to let another project use Cloud Number Registry, the project designation must be deleted by an IAM principal that has the IPAM Admin role granted at the organizational level. For more information, see [Delete a project designation](https://docs.cloud.google.com/number-registry/designate-project-cloud-number-registry#delete-designation).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
