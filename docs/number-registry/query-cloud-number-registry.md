---
url: https://docs.cloud.google.com/number-registry/query-cloud-number-registry/
title: Query Cloud Number Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:05:01.254274+00:00
---

# Query Cloud Number Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/number-registry/query-cloud-number-registry/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Number Registry ](https://docs.cloud.google.com/number-registry)
  * [ Guides ](https://docs.cloud.google.com/number-registry/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Query Cloud Number Registry

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page explains how to query information that is stored in [Cloud Number Registry](https://docs.cloud.google.com/number-registry/cloud-number-registry).

## Before you begin

  1. [Set up Cloud Number Registry](https://docs.cloud.google.com/number-registry/set-up-cloud-number-registry).
  2. Select the project in your organization that has been configured to provide Cloud Number Registry access.
  3. Verify that you have the permissions required to complete this guide.



### Required roles

To get the permissions that you need to view information stored in Cloud Number Registry, ask your administrator to grant you the [Cloud Number Registry IPAM Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudnumberregistry#cloudnumberregistry.ipamViewer) (`roles/cloudnumberregistry.ipamViewer`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Find free IP ranges

You can find available IP address ranges within discovered ranges or custom ranges.

### Find free IP ranges in discovered ranges

When you find free IP ranges in discovered ranges, the following limitations apply:

  * Results might include [unusable addresses in IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#unusable-ip-addresses-in-every-subnet) and [unusable addresses in IPv6 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#unusable-ip-addresses-in-every-ipv6-subnet).

  * Results might include ephemeral IP addresses that are assigned to instances that are shut down.




###  Console 

  1. In the Google Cloud console, go to the **Cloud Number Registry** page.

[Go to Cloud Number Registry](https://console.cloud.google.com/cloud-number-registry/overview)

  2. Click the **Registry books** tab.

  3. Click a registry book.

  4. Click the **Discovered realms** tab.

  5. Click a discovered realm, and click a discovered range inside that realm.

  6. Click **Find free IP ranges**.

  7. In **Prefix length** , select the size of the range that you want to find.

The available ranges of the specified size are listed.




###  gcloud 

Find free IP ranges in discovered ranges by using the [`gcloud alpha number-registry discovered-ranges find-free-ip-ranges` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/number-registry/discovered-ranges/find-free-ip-ranges).
    
    
    gcloud alpha number-registry discovered-ranges find-free-ip-ranges DISCOVERED_RANGE_NAME \
        --cidr-prefix-length=PREFIX_LENGTH \
        --range-count=RANGE_COUNT \
        --location=global
    

Replace the following:

  * `DISCOVERED_RANGE_NAME`: the name of the discovered range.
  * `PREFIX_LENGTH`: the CIDR prefix length of the ranges to find. Use `32` to find individual IPv4 addresses.
  * `RANGE_COUNT`: the number of free ranges to find.



### Find free IP ranges in custom ranges

If a custom range doesn't exist for a given IP address range, the range is considered to be a free IP range. If you want to use Cloud Number Registry to find free IP ranges within custom ranges, make sure that all in-use IP addresses and IP address ranges have a corresponding custom range.

###  Console 

  1. In the Google Cloud console, go to the **Cloud Number Registry** page.

[Go to Cloud Number Registry](https://console.cloud.google.com/cloud-number-registry/overview)

  2. Click the **Registry books** tab.

  3. Click a registry book.

  4. Click the **Custom realms** tab.

  5. Click a custom realm, and click a custom range inside that realm.

  6. Click **Find free IP ranges**.

  7. In **Prefix length** , select the size of the range that you want to find.

The available ranges of the specified size are listed.




###  gcloud 

Find free IP ranges in custom ranges by using the [`gcloud alpha number-registry custom-ranges find-free-ip-ranges` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/number-registry/custom-ranges/find-free-ip-ranges).
    
    
    gcloud alpha number-registry custom-ranges find-free-ip-ranges CUSTOM_RANGE_NAME \
        --cidr-prefix-length=PREFIX_LENGTH \
        --range-count=RANGE_COUNT \
        --location=global
    

Replace the following:

  * `CUSTOM_RANGE_NAME`: the name of the custom range.
  * `PREFIX_LENGTH`: the CIDR prefix length of the ranges to find. Use `32` to find individual IPv4 addresses.
  * `RANGE_COUNT`: the number of free ranges to find.



## Search IP address resources

You can search for IP address resources within a registry book.

You can use the following filters in queries:

  * **IP address** : The IP address to search for—for example, `10.10.10.46`.
  * **Realm** : The realm name to search in—for example, `vpc-global-123456789`.
  * **Parent range** : The URI of the parent range you want to search within—for example, `projects/project3/locations/global/customRanges/range7`.
  * **IP version** : The IP version to filter for.
  * **Attributes** : You can filter by attribute text or you can filter by keys and values, but you can't include both in the same query.

    * **Filter by text** : The attribute text to search for within ranges—for example, `europe-west1`.
    * **Filter by keys and values** : The attribute key and value to filter for—for example, the key `addressType` with the value `INTERNAL`.



###  Console 

  1. In the Google Cloud console, go to the **Cloud Number Registry** page.

[Go to Cloud Number Registry](https://console.cloud.google.com/cloud-number-registry/overview)

  2. Click the **Registry books** tab.

  3. Click a registry book.

  4. Click the **IP search** tab.

  5. Enter your search query by using the **IP address** field and the **Filters** section, and click **Search**.

     * To search for a specific IP address, enter the IP address in the **IP address** field.
     * To filter your search by IP version, realm, parent range, or attributes, enter your search query in the **Filters** section.



###  gcloud 

Search IP resources by using the [`gcloud alpha number-registry registry-books search-ip-resources` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/number-registry/registry-books/search-ip-resources).

You can combine filters in the following ways:

  * You can combine two or more filters in the same query by using `AND`.
  * You can use `AND NOT` in combination with the `attribute:(KEY=VALUE)` filter only.
  * You can use either `attribute` or `attribute_text` in a given query, but not both.


    
    
    gcloud alpha number-registry registry-books search-ip-resources REGISTRY_BOOK \
        --query=QUERY \
        --show-utilization \
        --location=global
    

Replace the following:

  * `REGISTRY_BOOK`: the name of the registry book to search within.
  * `QUERY`: the query for your search—for example: 
    * `"ip_address=\"2001:db8::/64\""`
    * `"attribute_text=europe-west1"`
    * `"attribute:(resourceName=projects/project123/regions/us-east1/subnetworks/subnet1)"`
    * `"realm=vpc-global-123456789"`
    * `"realm=vpc-global-123456789 AND ip_address=10.10.10.46"`
    * `"realm=vpc-global-123456789 AND ip_version=IPV6"`
    * `"realm=vpc-global-123456789 AND attribute_text=production"`
    * `"realm=vpc-global-123456789 AND attribute:(team=\"Sales Europe\")"`
    * `"parent_range=projects/project3/locations/global/customRanges/range7"`
    * `"parent_range=projects/project3/locations/global/customRanges/range7 AND attribute:(team=marketing)"`
    * `"parent_range=projects/project3/locations/global/customRanges/range7 AND NOT attribute:(environment=production)"`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
