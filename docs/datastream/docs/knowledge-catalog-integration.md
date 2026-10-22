---
url: https://docs.cloud.google.com/datastream/docs/knowledge-catalog-integration/
title: Manage your Datastream resources using Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:41.543566+00:00
---

# Manage your Datastream resources using Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/knowledge-catalog-integration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Manage your Datastream resources using Knowledge Catalog Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can search for and manage your Datastream resources using Knowledge Catalog, which is a platform for storing, managing, and accessing your metadata. Use Knowledge Catalog to help you with the following:

  * Discovering, analyzing, and understanding your Datastream metadata.
  * Browsing your Datastream resources, such as streams, connection profiles and connectivity configurations.
  * Improving operational visibility for troubleshooting and managing data pipelines.
  * Establishing both near real-time and periodic mechanisms for consistent metadata ingestion with live and batch synchronization. For more information, see Synchronization modes.



## Knowledge Catalog modeling

Datastream resources are modeled in Knowledge Catalog under a reserved, Knowledge Catalog-owned entry group and specific entry types.

**Knowledge Catalog entity** | **Resource identifier**  
---|---  
Entry group | `@datastream`  
Entry type | `datastream-stream`  
Entry type | `datastream-connection-profile`  
Entry type | `datastream-private-connection`  
  
## Types of metadata discovery

Knowledge Catalog metadata discovery is an automated process that scans connected data sources—like Datastream—to identify data assets and extract their technical metadata into the Knowledge Catalog.

This process uses both real-time and periodic synchronization to keep the catalog consistent with the source system. For Datastream, metadata for all streams, connection profiles, and private connectivity configurations is discovered by default:

**Resource type** | **Metadata retrieved**  
---|---  
Streams | 

  * Name
  * Location
  * State (for example, `RUNNING`, `PAUSED`, `FAILED`)
  * Backfill strategy
  * Source and destination connection profile names
  * Source and destination configurations

  
Connection profiles | 

  * Name
  * Location
  * Type (for example, `MYSQL`, `ORACLE`, `BIGQUERY`)
  * Connectivity option
  * Hostname, port, and database name

  
Private connectivity configurations | 

  * Name
  * State
  * Connectivity method (for example, Private Service Connect or VPC peering)
  * VPC network and subnet details

  
**Note:** Knowledge Catalog refers to the resources in Datastream and in other Google Cloud services as _assets_.

## Synchronization modes

Datastream uses the following synchronization modes to keep the Knowledge Catalog consistent with the source system.

  * **Live synchronization** : in this mode, Datastream publishes events to Pub/Sub topics when any metadata changes occur. This lets Knowledge Catalog receive near real-time updates by subscribing to these topics.
  * **Batch synchronization** : in this mode, Datastream periodically publishes full metadata exports (checkpoints) to designated Cloud Storage buckets, from which Knowledge Catalog ingests the data.



### Keyword and natural language search

Knowledge Catalog supports keyword and natural language searches.

  * Keyword search lets you find resources using specific keywords, filters, and a defined syntax. For example, you might enter `system=Datastream AND type=Stream` to view all Datastream streams.
  * Natural language search (Preview) uses AI to understand semantic queries. It lets you find resources using everyday language, eliminating the need for complex syntax. For example, you can enter queries like `List all Datastream streams with BigQuery destination`.



For more information, see [Search syntax for Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/search-syntax).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Enable the Dataplex API for the project. 

[Enable the Dataplex API](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com)

  7. Verify that you have the necessary permissions.



### Required IAM roles

This section describes the roles and permissions required to search for resources and to access the search results.

#### Required roles for accessing search results

To search for and view Datastream metadata in Knowledge Catalog, principals must have permissions to view Datastream resources, including the `dataplex.projects.search` permission.

To grant principals—such as users, groups, or service accounts—these permissions, assign them the **Datastream Viewer** ([`roles/datastream.viewer`](https://docs.cloud.google.com/datastream/docs/manage-streams#iam-roles)) IAM role on the project that contains the Datastream resources.

Knowledge Catalog operation | Datastream resource | Roles or permissions required  
---|---|---  
Search for Datastream resources | Streams | `datastream.streams.get`  
Connection profiles | `datastream.connectionProfiles.get`  
Private connectivity configurations | `datastream.privateConnections.get`  
  
For more information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). For more information about Datastream IAM roles, see [IAM roles and permissions for Datastream](https://docs.cloud.google.com/datastream/docs/manage-streams#iam-roles).

#### Required roles for searching entries

To search for entries, you need at least one of the following [ IAM roles](https://docs.cloud.google.com/dataplex/docs/iam-roles#predefined-roles) on the project that is used for search:

  * Dataplex Catalog Admin ([`roles/dataplex.catalogAdmin`](https://docs.cloud.google.com/dataplex/docs/iam-roles#dataplex.catalogAdmin))
  * Dataplex Catalog Editor ([`roles/dataplex.catalogEditor`](https://docs.cloud.google.com/dataplex/docs/iam-roles#dataplex.catalogEditor))
  * Dataplex Catalog Viewer ([`roles/dataplex.catalogViewer`](https://docs.cloud.google.com/dataplex/docs/iam-roles#dataplex.catalogViewer))



Permissions on search results are checked independently of the selected project. For more information, see [Search for data assets with Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/search-assets#required-roles).

## Search for Datastream assets

Use the Knowledge Catalog search page in the Google Cloud console to search for Datastream assets.

  1. Go to the Knowledge Catalog **Search** page.

[Go to Search](https://console.cloud.google.com/dataplex/dp-search)

  2. In **Choose search platform** , select **Knowledge Catalog**.

  3. In the **Filters** panel, click **Systems** , and then select **Datastream**.

  4. Optional. In **Type aliases** , you can filter the search results to a specific type of Datastream asset by selecting one or more of the following type aliases:

     * **Data stream** : to search for Datastream streams.
     * **Connection profile** : to search for Datastream connection profiles.
     * **Connection** : to search for Datastream private connectivity configurations.



### Use queries to perform keyword search

You can use the search field in Knowledge Catalog to perform keyword search queries. For example, you might enter `system=Datastream AND type=Stream` to view all Datastream streams.

For more information, see [Search syntax for Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/search-syntax).

To view all Datastream assets, enter `system=Datastream`.

Then you can enter specific keywords. For example, to view all Datastream streams:
    
    
    system=Datastream AND type=Stream
    

To view all connection profiles, enter the following query:
    
    
    system=Datastream AND type=ConnectionProfile
    

You can also use parentheses and the logical operators `AND` and `OR` for complex expressions. To learn more about the expressions that you can use in the search field, see [Search syntax for Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/search-syntax).

You can directly enter search queries for specific Datastream assets into the search field. The format of the query string is as follows:
    
    
    type="projects/dataplex-types/locations/global/entryTypes/QUERY_STRING"

Replace the following:

  * `QUERY_STRING`: use the following list to identify a query string based on the type of Datastream asset that you want to query:

    * `datastream-stream`
    * `datastream-connection-profile`
    * `datastream-private-connection`



An example query might look like the following:
    
    
    type="projects/dataplex-types/locations/global/entryTypes/datastream-stream"
    

## Pricing

There is no charge for storing Datastream technical metadata in Knowledge Catalog. Standard Knowledge Catalog pricing applies for API calls and additional business metadata enrichment. For more information, see the [ Knowledge Catalog pricing page](https://docs.cloud.google.com/dataplex/pricing).

## What's next

  * Learn about [metadata management in Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/catalog-overview).
  * Learn about [Knowledge Catalog Identity and Access Management roles](https://docs.cloud.google.com/dataplex/docs/iam-roles).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
