---
url: https://docs.cloud.google.com/number-registry/create-registry-books-realms-custom-ranges/
title: Create registry books, realms, and custom ranges \u00a0|\u00a0 Cloud Number Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:20:01.399595+00:00
---

# Create registry books, realms, and custom ranges  |  Cloud Number Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/number-registry/create-registry-books-realms-custom-ranges/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Number Registry ](https://docs.cloud.google.com/number-registry)
  * [ Guides ](https://docs.cloud.google.com/number-registry/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create registry books, realms, and custom ranges

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page explains how to organize your Compute Engine and other IP address resources in [Cloud Number Registry](https://docs.cloud.google.com/number-registry/overview).

## Before you begin

  1. [Set up Cloud Number Registry](https://docs.cloud.google.com/number-registry/set-up-cloud-number-registry).
  2. Select the project in your organization that has been configured to provide Cloud Number Registry access.
  3. Verify that you have the permissions required to complete this guide.



### Required roles

To get the permissions that you need to create Cloud Number Registry resources, ask your administrator to grant you the [Cloud Number Registry IPAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamAdmin) (`roles/cloudnumberregistry.ipamAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a registry book

When you create an IPAM admin scope, a default registry book is created. The default registry book contains information about all discovered realms and ranges in your organization.

Alternatively, you can create additional registry books to organize your IP address resources.

  * To organize discovered realms and ranges, specify one or more projects in the _claimed scope_ of the registry book. The registry book contains information about those projects. You can also add user-managed realms to this registry book.

  * To organize only user-managed realms, don't specify any projects in the claimed scope.




###  Console 

  1. In the Google Cloud console, go to the **Cloud Number Registry** page.

[Go to Cloud Number Registry](https://console.cloud.google.com/cloud-number-registry/overview)

  2. Click **Create a registry book**.

  3. In the **Name** field, enter a name for the registry book.

  4. To use this registry book to organize discovered realms and ranges, do the following:

     1. Click **Add project** to add a project to the registry book.
     2. Repeat the previous step if needed to add additional claimed projects.
  5. Click **Create registry book**.




###  gcloud 

Create a registry book by using the [`gcloud alpha number-registry registry-books create` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/number-registry/registry-books/create).

To create a registry book to organize only user-managed realms and ranges, omit the `--claimed-scopes` flag.
    
    
    gcloud alpha number-registry registry-books create REGISTRY_BOOK \
        --claimed-scopes=PROJECT_LIST \
        --location=global
    

Replace the following:

  * `REGISTRY_BOOK`: a name for the registry book.
  * `PROJECT_LIST`: a comma-separated list of projects to claim in this registry book—for example `projects/12345678,projects/test-project`.



## Create a realm

You can create realms in any registry book.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Number Registry** page.

[Go to Cloud Number Registry](https://console.cloud.google.com/cloud-number-registry/overview)

  2. Click the **Registry books** tab.

  3. Click the registry book that you want add a realm to.

  4. Click **Create realm**.

  5. For **Name** , enter a name for the realm.

  6. For **Traffic type** , select a traffic type.

  7. For **IP version** , select **IPv4** or **IPv6**.

  8. Click **Create realm**.




###  gcloud 

Create a realm by using the [`gcloud alpha number-registry realms create` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/number-registry/realms/create).
    
    
    gcloud alpha number-registry realms create REALM \
        --registry-book=REGISTRY_BOOK \
        --traffic-type=TRAFFIC_TYPE \
        --management-type=USER \
        --ip-version=IP_VERSION \
        --location=global
    

Replace the following:

  * `REALM`: a name for the realm.
  * `REGISTRY_BOOK`: the URI of the parent registry book for this realm.
  * `TRAFFIC_TYPE`: the traffic type for this realm. Valid values are `PRIVATE`, `INTERNET`, `LINK_LOCAL`, or `UNSET`.
  * `IP_VERSION`: the IP version for this realm. Valid values are `ipv4` or `ipv6`.



## Create a custom range

Custom ranges can be created inside a realm, or inside a parent custom range. You can add custom ranges only to user-managed realms.

You can use custom ranges to track IP address ranges that aren't discovered by Cloud Number Registry—for example, IP address ranges that are used in subnets in on-premises environments.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Number Registry** page.

[Go to Cloud Number Registry](https://console.cloud.google.com/cloud-number-registry/overview)

  2. Click the **Registry books** tab.

  3. Click registry book that you want add the custom range to.

  4. Navigate to the parent resource where you want to add the range:

     * Click a realm, and then click **Create custom range**.
     * Click a realm, then click a custom range, and then click **Create child range**.
  5. For **Name** , enter a name for the custom range.

  6. For **IP range** , enter the IP address range.

  7. Click **Create custom range**.




###  gcloud 

Add custom ranges by using the [`gcloud alpha number-registry custom-ranges create` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/number-registry/custom-ranges/create).

  * Add a custom IPv4 range, assigning a realm as the parent of the range.

To create a custom IPv6 range, use the `--ipv6-cidr-range` flag instead of `--ipv4-cidr-range`.
        
        gcloud alpha number-registry custom-ranges create CUSTOM_RANGE_NAME \
            --realm=REALM_NAME \
            --ipv4-cidr-range=CIDR_RANGE \
            --location=global
            

Replace the following:

    * `CUSTOM_RANGE_NAME`: a name for the custom range.
    * `REALM_NAME`: the name of the parent realm for this custom range.
    * `CIDR_RANGE`: the IP address range that you want to add to the realm, for example `10.0.0.0/22`.
  * Add a custom IPv4 range, assigning another range as the parent of the range.

To create a custom IPv6 range, use the `--ipv6-cidr-range` flag instead of `--ipv4-cidr-range`.
        
        gcloud alpha number-registry custom-ranges create CUSTOM_RANGE_NAME \
            --parent-range=PARENT_RANGE \
            --ipv4-cidr-range=CIDR_RANGE \
            --location=global
        

Replace the following:

    * `CUSTOM_RANGE_NAME`: a name for the custom range.
    * `PARENT_RANGE`: the URI of the parent range.
    * `CIDR_RANGE`: the IP address range that you want to add to the realm, for example `10.0.0.0/24`.
  * Add a custom IPv4 range, assigning another range as the parent of the range, and setting attributes on the range. If you set attributes on a range, you can [use those attributes when you search for IP addresses resources](https://docs.cloud.google.com/number-registry/query-cloud-number-registry#search-ip).
        
        gcloud alpha number-registry custom-ranges create CUSTOM_RANGE_NAME \
            --parent-range=PARENT_RANGE \
            --ipv4-cidr-range=CIDR_RANGE \
            --attributes=key=KEY,value=VALUE \
            --location=global
        

Replace the following:

    * `CUSTOM_RANGE_NAME`: a name for the custom range.
    * `PARENT_RANGE`: the URI of the parent range.
    * `CIDR_RANGE`: the IP address range that you want to add to the realm, for example `10.0.0.0/24`.
    * `key`: the key of the attribute—for example, `env`.
    * `value`: the value of the attribute—for example, `prod`.



## What's next

  * [Query Cloud Number Registry](https://docs.cloud.google.com/number-registry/query-cloud-number-registry)
  * [View, update, and delete registry books](https://docs.cloud.google.com/number-registry/view-update-delete-registry-books)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
