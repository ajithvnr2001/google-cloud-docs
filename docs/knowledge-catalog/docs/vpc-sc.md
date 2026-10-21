---
url: https://docs.cloud.google.com/knowledge-catalog/docs/vpc-sc/
title: VPC Service Controls with Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:37:40.769707+00:00
---

# VPC Service Controls with Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/vpc-sc/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  VPC Service Controls with Knowledge Catalog Stay organized with collections  Save and categorize content based on your preferences. 

This document is for security administrators and data engineers who need to secure Knowledge Catalog (formerly Dataplex Universal Catalog) services. It explains how to use VPC Service Controls to create service perimeters that protect your Knowledge Catalog resources and mitigate data exfiltration risks. For more information, see [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

## Supported features

When you secure Knowledge Catalog with a service perimeter, the following features are supported:

  * **Lakes** : you can create and manage Knowledge Catalog lakes within the perimeter.

  * **Assets** : you can manage assets within the perimeter.

  * **Metadata resources in Catalog** : you can manage metadata resources within the perimeter.

  * **Metadata export** : you can export metadata to Dataproc Metastore, which requires additional VPC Service Controls configuration. For more information, see [VPC Service Controls](https://docs.cloud.google.com/knowledge-catalog/docs/export-metadata#vpc-service-controls).

  * **Data insights** : you can run data profiling, data quality, and metadata insights scans.

  * **Data lineage** : you can track data lineage by using the restricted [Virtual IP (VIP)](https://docs.cloud.google.com/vpc-service-controls/docs/restricted-vip-services).

  * **Knowledge Catalog Search** : you can use the [`SearchEntries` API](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations/searchEntries). When you use Knowledge Catalog search in a project protected by a service perimeter, search results include only resources that are within the same perimeter. For more information, see [Search scope](https://docs.cloud.google.com/knowledge-catalog/docs/about-search#search-scope) and [Isolate search results by environment using VPC Service Controls](https://docs.cloud.google.com/knowledge-catalog/docs/about-search#environments).

  * **Data products ([Preview](https://docs.cloud.google.com/products#product-launch-stages))**: you can use VPC Service Controls to secure data products, ensuring that communication between the data product, its constituent data assets (such as BigQuery tables), and users remains within authorized perimeters. For more information, see [Use VPC Service Controls with data products](https://docs.cloud.google.com/knowledge-catalog/docs/vpcsc-data-products).




### Knowledge Catalog search and VPC Service Controls

When you use Knowledge Catalog search in a project protected by a service perimeter, search results include only resources that belong to the same project under which the search is performed.

To include resources from other projects that are in the same service perimeter, you must configure VPC Service Controls egress rules for the Knowledge Catalog caller project. For more information, see [Configuring ingress and egress policies](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies). These rules allow the search results to cross project boundaries within the perimeter.

The following example shows an egress policy configuration that allows search results to include BigQuery resources from `project A` when the search is performed from `project B`:
    
    
    egressPolicies:
    -   egressFrom:
        identityType: ANY_USER_ACCOUNT
      egressTo:
        operations:
        -   serviceName: bigquery.googleapis.com
          methodSelectors:
          -   method: '*'
        resources:
        -   projects/projectA
    

When you perform a Knowledge Catalog search in `project B`, Knowledge Catalog calls the BigQuery API to locate assets in `project A`. This policy explicitly permits any user account in `project B` to make BigQuery API calls against `project A`, allowing BigQuery assets from `project A` to appear in your Knowledge Catalog search results.

## Limitations

You can create Knowledge Catalog resources before setting up the VPC Service Controls security perimeter, but those resources won't have perimeter protection.

By design, VPC Service Controls prevents resources within a service perimeter from accessing data and services outside that perimeter. For example, Knowledge Catalog data profiling and data quality scans cannot access data sources, such as BigQuery tables or Cloud Storage files, that are outside the service perimeter. Similarly, when exporting data scan results, the destination BigQuery table must be in a project protected by the perimeter. For information about granting access to your protected resources from outside the perimeter, see Create an access level.

## Set up VPC Service Controls

To protect Knowledge Catalog resources with VPC Service Controls, perform the following steps:

  1. Configure the VPC network.
  2. Create a service perimeter.
  3. Add projects to the perimeter.
  4. Add the Dataplex API to the service perimeter.
  5. Optional: Create an access level.



### Configure the Virtual Private Cloud (VPC) network

You can configure the VPC network to restrict Private Google Access with respect to a service perimeter. This ensures that hosts on your VPC or on-premises network can only communicate with Google APIs and services that are supported by VPC Service Controls in ways which conform to the associated perimeter's policy.

For more information, see [Setting up private connectivity to Google APIs and services](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity).

### Create a service perimeter

When you create a service perimeter, you select the Knowledge Catalog projects that you want the VPC Service Controls service perimeter to protect.

To create a service perimeter, follow the instructions in [Create a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters).

### Add more projects to the service perimeter

To add existing Knowledge Catalog projects to the perimeter, follow the instructions in [Update a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#update).

### Add the Dataplex API to the service perimeter

To mitigate the risk of your data being exfiltrated from Knowledge Catalog, for example, using Dataplex API methods, you must restrict the Dataplex API.

To add the Dataplex API as a restricted service, follow these steps:

### Console

  1. In the Google Cloud console, go to the **VPC Service Controls** page.

[Go to VPC Service Controls](https://console.cloud.google.com/security/service-perimeter)

  2. On the **VPC Service Controls** page, in the table, click the name of the service perimeter that you want to modify.

  3. Click **Edit Perimeter**.

  4. On the **Edit Service Perimeter** page, click **Add Services**.

  5. Add **Dataplex API**.

  6. Click **Save**.




### gcloud

  * Use the `gcloud access-context-manager perimeters update` command:
        
        gcloud access-context-manager perimeters update PERIMETER_ID \
        --policy=POLICY_ID \
        --add-restricted-services=dataplex.googleapis.com
        

Replace the following:

    * `PERIMETER_ID`: the ID of the perimeter or the fully qualified identifier for the perimeter
    * `POLICY_ID`: the ID of the access policy



### Optional: Create an access level

To permit external access to protected resources inside a perimeter, you can use access levels. Access levels apply only to requests for protected resources coming from outside the service perimeter. You can't use access levels to give protected resources permission to access data and services outside the perimeter.

For more information, see [Allow access to protected resources from outside a perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/use-access-levels).

## What's next

  * Learn more about [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs).
  * Learn more about [Knowledge Catalog access control with IAM](https://docs.cloud.google.com/knowledge-catalog/docs/iam-and-access-control).
  * Learn more about [Knowledge Catalog security](https://docs.cloud.google.com/knowledge-catalog/docs/lake-security).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
