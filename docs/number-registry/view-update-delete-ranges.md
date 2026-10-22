---
url: https://docs.cloud.google.com/number-registry/view-update-delete-ranges/
title: View, update, and delete ranges \u00a0|\u00a0 Cloud Number Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:59:18.803258+00:00
---

# View, update, and delete ranges  |  Cloud Number Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/number-registry/view-update-delete-ranges/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Number Registry ](https://docs.cloud.google.com/number-registry)
  * [ Guides ](https://docs.cloud.google.com/number-registry/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# View, update, and delete ranges

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page explains how to view discovered and custom ranges, and how to update and delete custom ranges.

## Before you begin

  1. [Set up Cloud Number Registry](https://docs.cloud.google.com/number-registry/set-up-cloud-number-registry).
  2. Select the project in your organization that has been configured to provide Cloud Number Registry access.
  3. Verify that you have the permissions required to complete this guide.



### Required roles

To get the permissions that you need to manage Cloud Number Registry, ask your administrator to grant you the [Cloud Number Registry IPAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamAdmin) (`roles/cloudnumberregistry.ipamAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## List and view discovered ranges

In the Google Cloud console, you can list all discovered ranges in a given realm. Only realms that are managed by Cloud Number Registry contain discovered ranges. In the gcloud CLI, you can list all discovered ranges in your IPAM admin scope.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Number Registry** page.

[Go to Cloud Number Registry](https://console.cloud.google.com/cloud-number-registry/overview)

  2. Click the **Registry books** tab.

  3. Click a registry book.

  4. Click the **Discovered realms** tab.

  5. Click the discovered realm that you want to view.

The discovered ranges that are associated with the realm are displayed, including the IP address utilization of each range.

  6. Click or expand a range to see child ranges.




###  gcloud 

  * To list all discovered ranges, use the [`gcloud alpha number-registry discovered-ranges list` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/number-registry/discovered-ranges/list).
        
        gcloud alpha number-registry discovered-ranges list \
            --location=global
        

  * To view details for a specific discovered range, use the [`gcloud alpha number-registry discovered-ranges describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/number-registry/discovered-ranges/describe).
        
        gcloud alpha number-registry discovered-ranges describe DISCOVERED_RANGE \
            --location=global
        

Replace `DISCOVERED_RANGE` with the name of the discovered range that you want to view.

  * To view IP address utilization of a discovered range, use the [`gcloud alpha number-registry discovered-ranges show-utilization` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/number-registry/discovered-ranges/show-utilization).
        
        gcloud alpha number-registry discovered-ranges show-utilization DISCOVERED_RANGE \
            --location=global
        

Replace `DISCOVERED_RANGE` with the name of the discovered range that you want to view.




## List and view custom ranges

In the Google Cloud console, you can list all custom ranges in a custom realm. In the gcloud CLI, you can list all custom ranges in your IPAM admin scope.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Number Registry** page.

[Go to Cloud Number Registry](https://console.cloud.google.com/cloud-number-registry/overview)

  2. Click the **Registry books** tab.

  3. Click a registry book.

  4. Click the **Custom realms** tab.

  5. Click the custom realm that you want to view.

The custom ranges that are associated with the realm are displayed, including the IP address utilization of each range.

  6. Click or expand a range to see child ranges.




###  gcloud 

  * To list all custom ranges, use the [`gcloud alpha number-registry custom-ranges list` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/number-registry/custom-ranges/list).
        
        gcloud alpha number-registry custom-ranges list \
            --location=global
        

  * To view details for a specific custom range, use the [`gcloud alpha number-registry custom-ranges describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/number-registry/custom-ranges/describe).
        
        gcloud alpha number-registry custom-ranges describe CUSTOM_RANGE \
            --location=global
        

Replace `CUSTOM_RANGE` with the name of the custom range that you want to view.

  * To view IP address utilization of a custom range, use the [`gcloud alpha number-registry custom-ranges show-utilization` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/number-registry/custom-ranges/show-utilization).
        
        gcloud alpha number-registry custom-ranges show-utilization CUSTOM_RANGE \
            --location=global
        

Replace `CUSTOM_RANGE` with the name of the custom range that you want to view.




## Update a custom range

You can update a custom range. You can't update discovered ranges.

You can modify the following fields on a custom range:

  * Attributes, which can be used when [searching for IP address resources](https://docs.cloud.google.com/number-registry/query-cloud-number-registry#search-ip)
  * Description
  * IP address range
  * Parent range
  * Realm
  * Registry book



You are restricted to making valid changes—for example, you can't move an IPv4 custom range into an IPv6 realm or to a realm that is managed by Cloud Number Registry.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Number Registry** page.

[Go to Cloud Number Registry](https://console.cloud.google.com/cloud-number-registry/overview)

  2. Click the **Registry books** tab.

  3. Click the registry book that is associated with the custom range you want to update.

  4. Click the **Custom realms** tab, and then click the custom realm that contains the custom range you want to update.

  5. Click the custom range that you want to update.

  6. Click edit **Edit custom range** and make your changes.

  7. Click **Save**.




###  gcloud 

You can update a range to change various settings. The following example shows you how to add attributes to a custom range. If you set attributes on a range, you can [use those attributes when you search for IP addresses resources](https://docs.cloud.google.com/number-registry/query-cloud-number-registry#search-ip).

For information about all editable settings, see the [`gcloud alpha number-registry custom-ranges update` reference documentation](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/number-registry/custom-ranges/update).
    
    
    gcloud alpha number-registry custom-ranges update CUSTOM_RANGE \
        --attributes=key=KEY,value=VALUE \
        --location=global
    

Replace the following:

  * `CUSTOM_RANGE`: the name of the custom range.
  * `KEY`: the key of the attribute.
  * `VALUE`: the value of the attribute.



## Delete a custom range

You can delete a custom range. You can't delete discovered ranges. You can't delete custom ranges that contain child ranges—you must delete the child ranges first.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Number Registry** page.

[Go to Cloud Number Registry](https://console.cloud.google.com/cloud-number-registry/overview)

  2. Click the **Registry books** tab.

  3. Click the registry book and custom realm that contains the custom range that you want to delete.

  4. Click the range that you want to delete.

  5. Click **Delete custom range**.




###  gcloud 

To delete a custom range, use the [`gcloud alpha number-registry custom-ranges delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/number-registry/custom-ranges/delete).
    
    
    gcloud alpha number-registry custom-ranges delete CUSTOM_RANGE \
        --location=global
    

Replace `CUSTOM_RANGE` with the name of the custom range to delete.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
