---
url: https://docs.cloud.google.com/bigtable/docs/manage-data-assets-using-knowledge-catalog/
title: Manage data assets using Knowledge Catalog \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:36:38.205495+00:00
---

# Manage data assets using Knowledge Catalog  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/manage-data-assets-using-knowledge-catalog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage data assets using Knowledge Catalog

Knowledge Catalog automatically catalogs metadata about Bigtable resources. This feature helps you search for and manage your Bigtable data assets.

Metadata is automatically synced from Bigtable to Knowledge Catalog for the following Bigtable resources:

  * Instances
  * Clusters
  * Tables, including column family details



Knowledge Catalog is a fully managed metadata management service. It provides unified view and tagging mechanisms for technical and business metadata. To learn more about Knowledge Catalog and why you should use it, see [Knowledge Catalog overview](https://docs.cloud.google.com/dataplex/docs/introduction).

## Benefits of using Knowledge Catalog with Bigtable

Information from Knowledge Catalog about your data can help facilitate analysis, data reuse, application development, and data management.

You can search entries in Knowledge Catalog by details, such as resource name. For example, you can search for an instance name to find the entry for an instance or search for a column family to find the entry for a table. You can also use a faceted search, applying filters to narrow down your search. For more information, see [Search for resources in Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/search-assets).

[Tagging](https://docs.cloud.google.com/dataplex/docs/catalog-overview#tags) data assets can help you understand and catalog the data that is available in your Bigtable tables to make the data more discoverable and searchable by Knowledge Catalog users, and as part of your larger data estate. You can use _aspects_ to add your own metadata to your cataloged metadata, and then you can use those aspects to conduct searches.

## Get started with Knowledge Catalog

To start using Knowledge Catalog to manage your Bigtable data assets, complete the following tasks:

  1. [Enable the Dataplex API](https://docs.cloud.google.com/dataplex/docs/enable-api).

  2. Grant IAM roles to principals who require access to Bigtable entries in Knowledge Catalog.

  3. Learn [how to search for data assets](https://docs.cloud.google.com/dataplex/docs/search-assets).

  4. Review [Knowledge Catalog search syntax](https://docs.cloud.google.com/dataplex/docs/search-syntax) to understand how to find your metadata.

  5. Read the concepts on tagging Knowledge Catalog entries. For more information, see [About metadata management in Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/catalog-overview).




## Ways to search for Bigtable metadata

You can search synced Bigtable metadata using Knowledge Catalog.

In addition to [qualified predicates](https://docs.cloud.google.com/dataplex/docs/search-syntax#qualified-predicates), you can search for Bigtable resources with the following metadata fields:

  * Instance

    * Bigtable instance name
    * Bigtable instance ID
    * Cluster location
    * Cluster ID
  * Table

    * Table ID
    * Column family name
    * Bigtable instance name
    * Bigtable instance ID



## Required roles

Viewing, tagging, and searching Bigtable resources in Knowledge Catalog have different permission requirements. In general, grant principals in your organization the minimum role required to accomplish a task.

### Permission to view public and private aspects

To get the permissions that you need to view public and private aspects on Bigtable resources, ask your administrator to grant you the following IAM roles:

  * [`roles/dataplex.catalogViewer`](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer)
  * [`roles/bigtable.viewer`](https://docs.cloud.google.com/bigtable/docs/access-control#bigtable.viewer)



These predefined roles contain the permissions required to view public and private aspects. The exact permissions that are required are the following:

  * `bigtable.instances.get`
  * `bigtable.clusters.get`
  * `bigtable.tables.get`
  * `dataplex.aspectTypes.get`



### Permission to search Bigtable resources

To get the permissions that you need to search Bigtable resources in Knowledge Catalog, ask your administrator to grant you the following IAM roles:

  * [`roles/bigtable.viewer`](https://docs.cloud.google.com/bigtable/docs/access-control#bigtable.viewer)



These predefined roles contain the permissions required to search Bigtable resources. The exact permissions that are required are the following:

  * `bigtable.instances.get`
  * `bigtable.clusters.get`
  * `bigtable.tables.get`



### Permission to attach aspects to Bigtable resources

To get the permissions that you need to attach aspects to Bigtable resources in Knowledge Catalog, ask your administrator to grant you the following IAM roles:

  * [`roles/dataplex.aspectTypeUser`](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.aspectTypeUser)
  * [`roles/dataplex.catalogEditor`](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor)
  * [`roles/bigtable.admin`](https://docs.cloud.google.com/bigtable/docs/access-control#bigtable.admin)



These predefined roles contain the permissions required to add public and private aspects. The exact permissions that are required are the following:

  * `bigtable.instances.update`
  * `bigtable.clusters.update`
  * `bigtable.tables.update`
  * `dataplex.aspectTypes.use`
  * `dataplex.entries.update`



### Optional: Create a custom role

You can create a custom role to grant to users who require complete access to all Bigtable metadata in Knowledge Catalog across your project or organization. Then you can make any user or service account that needs access to a principal of the custom role. To learn more about custom roles, see [Roles and permissions](https://docs.cloud.google.com/iam/docs/roles-overview#custom).

Choose a meaningful name for the role, such as Bigtable Dataplex Editor, and then assign only the principals who need access to the role. For setup instructions, see [Create and manage custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles#creating_a_custom_role).

Grant the following permissions to the custom role:

  * `bigtable.instances.get`
  * `bigtable.instances.update`
  * `bigtable.clusters.get`
  * `bigtable.clusters.update`
  * `bigtable.tables.get`
  * `bigtable.tables.update`
  * `dataplex.aspectTypes.get`
  * `dataplex.aspectTypes.use`



For more information, see [Knowledge Catalog IAM permissions](https://docs.cloud.google.com/dataplex/docs/iam-permissions). For descriptions of Bigtable permissions, see [Permissions](https://docs.cloud.google.com/bigtable/docs/access-control#permissions).

## Limitations

The following section lists constraints that you must consider before you use Knowledge Catalog to manage your Bigtable metadata.

#### Location constraints

If your organization has set up [location constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations), metadata entries for your Bigtable resources might not be synced to Knowledge Catalog. Any entries created before enforcing the location constraints are retained by Knowledge Catalog.

To allow Knowledge Catalog to load resources, we recommend that you add the `global` multi-region to your location policy.

#### Column family name exception

The Dataplex API rejects requests where the column family name in your request includes a period (`.`). For example, if the column family name is `personal.info`.

## What's next

  * [Read an overview of Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/introduction).
  * [Explore additional Google Cloud integrations with Knowledge Catalog.](https://docs.cloud.google.com/dataplex/docs/integrate-data-sources)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
