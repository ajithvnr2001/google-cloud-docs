---
url: https://docs.cloud.google.com/number-registry/view-update-delete-realms/
title: View, update, and delete realms \u00a0|\u00a0 Cloud Number Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:05:03.887265+00:00
---

# View, update, and delete realms  |  Cloud Number Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/number-registry/view-update-delete-realms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Number Registry ](https://docs.cloud.google.com/number-registry)
  * [ Guides ](https://docs.cloud.google.com/number-registry/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# View, update, and delete realms

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page explains how to view, update, and delete [realms](https://docs.cloud.google.com/number-registry/overview#realms) in Cloud Number Registry. A realm is a set of managed IP address ranges that represent a network routing domain. For more information about discovered realms, see [Discovered resources](https://docs.cloud.google.com/number-registry/overview#supported-compute-engine-resources).

## Before you begin

  1. [Set up Cloud Number Registry](https://docs.cloud.google.com/number-registry/set-up-cloud-number-registry).
  2. Select the project in your organization that has been configured to provide Cloud Number Registry access.
  3. Verify that you have the permissions required to complete this guide.



### Required roles

To get the permissions that you need to manage Cloud Number Registry, ask your administrator to grant you the [Cloud Number Registry IPAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamAdmin) (`roles/cloudnumberregistry.ipamAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## List and view realms

In the Google Cloud console, you can list all realms in a given registry book. In the gcloud CLI, you can list all realms in your IPAM admin scope.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Number Registry** page.

[Go to Cloud Number Registry](https://console.cloud.google.com/cloud-number-registry/overview)

  2. Click the **Registry books** tab.

  3. Click a registry book. The realms associated with the registry book are displayed.

  4. To filter the list of realms, click the **Discovered realms** or **Custom realms** tab.

  5. Click the realm that you'd like to view. Details about the realm are displayed.

     * If the realm is managed by Cloud Number Registry, the associated discovered ranges are displayed.
     * If the realm is user-managed, the associated custom ranges are displayed.



###  gcloud 

  * List realms by using the [`gcloud alpha number-registry realms list` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/number-registry/realms/list).
        
        gcloud alpha number-registry realms list \
            --location=global
        

  * View details about a realm by using the [`gcloud alpha number-registry realms describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/number-registry/realms/describe).
        
        gcloud alpha number-registry realms describe REALM \
            --location=global
        

Replace the following:

    * `REALM`: the name of the realm that you want to view.



## Update a custom realm

You can update custom realms—realms that are user-managed. You can't update discovered realms—realms that are managed by Cloud Number Registry. The management type is displayed when you view details about a realm.

You can modify the following fields on a custom realm:

  * Registry book
  * Traffic type




###  Console 

  1. In the Google Cloud console, go to the **Cloud Number Registry** page.

[Go to Cloud Number Registry](https://console.cloud.google.com/cloud-number-registry/overview)

  2. Click the **Registry books** tab.

  3. Click the registry book that contains the realm you want to update.

  4. Click the **Custom realms** tab.

  5. Click the realm that you want to update.

  6. Click edit Edit for the field you want to update.

  7. In the dialog that appears, make your changes.

  8. Click **Save**.




###  gcloud 

The following example shows how to change the traffic type of a custom realm. For information about all editable settings, see the [`gcloud alpha number-registry realms update` reference documentation](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/number-registry/realms/update).
    
    
    gcloud alpha number-registry realms update REALM \
        --traffic-type=TRAFFIC_TYPE \
        --location=global
    

Replace the following:

  * `REALM`: the name of the realm to update.
  * `TRAFFIC_TYPE`: the updated traffic type for the realm.



## Delete a custom realm

You can delete realms that are user-managed. You can't delete a realm if it is managed by Cloud Number Registry. The management type is displayed when you view details about a realm.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Number Registry** page.

[Go to Cloud Number Registry](https://console.cloud.google.com/cloud-number-registry/overview)

  2. Click the **Registry books** tab.

  3. Click the registry book that contains the realm you want to delete.

  4. To filter the list of realms, click the **Discovered realms** or **Custom realms** tab.

  5. Click the realm that you want to delete.

  6. Click **Delete realm**.




###  gcloud 

Delete a realm by using the [`gcloud alpha number-registry realms delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/number-registry/realms/delete).
    
    
    gcloud alpha number-registry realms delete REALM \
        --location=global
    

Replace `REALM` with the name of the realm to delete.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
