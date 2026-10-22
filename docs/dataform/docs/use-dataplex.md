---
url: https://docs.cloud.google.com/dataform/docs/use-dataplex/
title: Manage metadata of Dataform repositories with Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:19.041111+00:00
---

# Manage metadata of Dataform repositories with Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/docs/use-dataplex/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataform ](https://docs.cloud.google.com/dataform/docs)
  * [ Guides ](https://docs.cloud.google.com/dataform/docs/overview)



Send feedback 

#  Manage metadata of Dataform repositories with Knowledge Catalog Stay organized with collections  Save and categorize content based on your preferences. 

This document describes using [Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/introduction) to view metadata of Dataform repositories and annotate them with aspects. 

Knowledge Catalog lets you store and manage your metadata. Dataform repositories are available in Knowledge Catalog by default, without any additional configuration. Knowledge Catalog automatically retrieves the following metadata from Dataform repositories:

  * Data asset name
  * Data asset parent
  * Data asset location
  * Data asset type
  * Corresponding Google Cloud project
  * Third-party repository source
  * Service account



## Before you begin

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Enable the Dataplex API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com)

  3. Ensure that you have the necessary Identity and Access Management (IAM) permissions.



### Required roles

To manage Dataform repositories in Knowledge Catalog, you need the [predefined Dataform roles](https://docs.cloud.google.com/dataform/docs/access-control#predefined-roles) that give you access to Dataform resources, and required [Knowledge Catalog roles](https://docs.cloud.google.com/dataplex/docs/iam-roles).

## Manage metadata in Knowledge Catalog

Knowledge Catalog logs Dataform repositories as [entries](https://docs.cloud.google.com/dataplex/docs/ingest-custom-sources#entries) with the following entry values:

System entry group
    The [system entry group](https://docs.cloud.google.com/dataplex/docs/ingest-custom-sources#entry-groups) for Dataform repositories is `@dataform`. To view details of repository entries in Knowledge Catalog, you need to view the `dataform` system entry group. For instructions about how to view a list of all entries in an entry group, see [View details of an entry group](https://docs.cloud.google.com/dataplex/docs/ingest-custom-sources#entry-group-details) in the Knowledge Catalog documentation.
System entry type
    The [system entry type](https://docs.cloud.google.com/dataplex/docs/ingest-custom-sources#entry-types) for Dataform repositories is `dataform-repository`. To view details of Dataform repositories, you need to view the `dataform-repository` system entry type. For instructions about how to view details of a selected entry type, see [View details of an entry type](https://docs.cloud.google.com/dataplex/docs/ingest-custom-sources#entry-type-details) in the Knowledge Catalog documentation. For instructions about how to view details of a selected entry, see [View details of an entry](https://docs.cloud.google.com/dataplex/docs/search-assets#view-entry-details) in the Knowledge Catalog documentation.

### Search for assets

For instructions about how to search for data assets in Knowledge Catalog, see [Search for data assets in Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/search-assets) in the Knowledge Catalog documentation.

## Annotate repositories

To provide additional context to Dataform repositories in Knowledge Catalog, you can annotate Dataform entries with [aspects](https://docs.cloud.google.com/dataplex/docs/enrich-entries-metadata#aspects).

The system aspect type for Dataform repositories is `dataform-repository`.

For instructions about how to annotate entries with aspects, see [Manage aspects and enrich metadata](https://docs.cloud.google.com/dataplex/docs/enrich-entries-metadata) in the Knowledge Catalog documentation.

## Limitations

Managing Dataform repositories in Knowledge Catalog is available with the following limitations:

  * You cannot view or manage Dataform file-level assets in Knowledge Catalog—for example, tables, or views.



## Locations

You can use Knowledge Catalog to manage Dataform repositories from all [Dataform locations](https://docs.cloud.google.com/dataform/docs/locations).

## Quotas

Managing Dataform repositories in Knowledge Catalog is subject to [Knowledge Catalog quotas and limits](https://docs.cloud.google.com/dataplex/docs/quotas).

## Pricing

Managing Dataform repositories in Knowledge Catalog is subject to [Knowledge Catalog pricing](https://cloud.google.com/dataplex/pricing).

## What's next

  * To learn more about Knowledge Catalog, see [Knowledge Catalog overview](https://docs.cloud.google.com/dataplex/docs/introduction) in the Knowledge Catalog documentation. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
