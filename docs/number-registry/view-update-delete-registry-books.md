---
url: https://docs.cloud.google.com/number-registry/view-update-delete-registry-books/
title: View, update, and delete registry books \u00a0|\u00a0 Cloud Number Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:05:01.464789+00:00
---

# View, update, and delete registry books  |  Cloud Number Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/number-registry/view-update-delete-registry-books/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Number Registry ](https://docs.cloud.google.com/number-registry)
  * [ Guides ](https://docs.cloud.google.com/number-registry/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# View, update, and delete registry books

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page explains how to view, update, and delete registry books in [Cloud Number Registry](https://docs.cloud.google.com/number-registry/cloud-number-registry).

## Before you begin

  1. [Set up Cloud Number Registry](https://docs.cloud.google.com/number-registry/set-up-cloud-number-registry).
  2. Select the project in your organization that has been configured to provide Cloud Number Registry access.
  3. Verify that you have the permissions required to complete this guide.



### Required roles

To get the permissions that you need to manage Cloud Number Registry, ask your administrator to grant you the [Cloud Number Registry IPAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamAdmin) (`roles/cloudnumberregistry.ipamAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## List and view registry books

###  Console 

  1. In the Google Cloud console, go to the **Cloud Number Registry** page.

[Go to Cloud Number Registry](https://console.cloud.google.com/cloud-number-registry/overview)

  2. Click the **Registry books** tab.

  3. All registry books are displayed.

  4. Click the registry book that you'd like to view.

  5. Details about the registry book are displayed, including the associated realms.




###  gcloud 

  * List all registry books by using the [`gcloud alpha number-registry registry-books list` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/number-registry/registry-books/list).
        
        gcloud alpha number-registry registry-books list \
            --location=global
        

  * View details about a registry book by using the [`gcloud alpha number-registry registry-books describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/number-registry/registry-books/describe).
        
        gcloud alpha number-registry registry-books describe REGISTRY_BOOK \
            --location=global
        

Replace the following:

    * `REGISTRY_BOOK`: the name of the registry book that you want to view.



## Update a registry book

You can update the claimed scopes that are associated with a user-managed registry book.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Number Registry** page.

[Go to Cloud Number Registry](https://console.cloud.google.com/cloud-number-registry/overview)

  2. Click the **Registry books** tab.

  3. Click the registry book that you want to update.

  4. Click the **Claimed projects** tab.

  5. To add projects:

     1. Click **Add claimed project**.
     2. In the **Add claimed projects** panel, enter or select the project ID or project number to add.
     3. For each additional project that you want to add, click **Add project** , and then enter the project ID or project number to add.
     4. Click **Save**.
  6. To remove projects:

     1. Select the checkbox next to each project that you want to remove.
     2. Click **Remove**.



###  gcloud 

The following example shows you how to add projects to the claimed scope of the registry book. You can also use the `--clear-claimed-scopes` flag to clear all projects, or use the `--remove-claimed-scopes` flag to remove specific projects.

For information about all editable settings, see the [`gcloud alpha number-registry registry-books update` reference documentation](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/number-registry/registry-books/update).
    
    
    gcloud alpha number-registry registry-books update REGISTRY_BOOK \
        --add-claimed-scopes=PROJECT_LIST \
        --location=global
    

Replace the following:

  * `REGISTRY_BOOK`: the name of the registry book.
  * `PROJECT_LIST`: a comma-separated list of projects that you want to add to this registry book—for example `projects/12345678,projects/staging-project`.



## Delete a registry book

You can delete user-managed registry books. You can't delete the default registry book.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Number Registry** page.

[Go to Cloud Number Registry](https://console.cloud.google.com/cloud-number-registry/overview)

  2. Click the **Registry books** tab.

  3. Select the registry book that you want to delete and click **Delete**.




###  gcloud 

Delete a registry book by using the [`gcloud alpha number-registry registry-books delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/number-registry/registry-books/delete).
    
    
    gcloud alpha number-registry registry-books delete REGISTRY_BOOK \
        --location=global
    

Replace `REGISTRY_BOOK` with the name of the registry book to delete.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
