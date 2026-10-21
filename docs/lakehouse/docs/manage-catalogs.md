---
url: https://docs.cloud.google.com/lakehouse/docs/manage-catalogs/
title: Manage Iceberg REST catalog resources \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:44.671242+00:00
---

# Manage Iceberg REST catalog resources  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/manage-catalogs/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Manage Iceberg REST catalog resources Stay organized with collections  Save and categorize content based on your preferences. 

The Lakehouse runtime catalog lets you manage [catalog endpoints](https://docs.cloud.google.com/lakehouse/docs/about-lakehouse-catalogs#configuration) in borderless Lakehouse. You can use the Google Cloud console or the REST API to create, configure, and monitor these catalog endpoints to establish the metadata layer required for query engine connections.

## Before you begin

  1. Read [About the Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/about-lakehouse-catalogs) to understand how the Lakehouse runtime catalog works and the limitations for the service.

Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

[Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

Enable the BigLake API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=biglake.googleapis.com)

In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

[Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

Enable the BigLake API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=biglake.googleapis.com)




### Required roles

To get the permissions that you need to use the Lakehouse runtime catalog, ask your administrator to grant you the following IAM roles on your project: 

  * [BigLake Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`)
  * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Management actions

You can perform the following management actions on your Apache Iceberg REST catalog endpoint resources using the Google Cloud console or the REST API:

  * **[Create a catalog](https://docs.cloud.google.com/lakehouse/docs/create-catalog):** Create an Apache Iceberg REST catalog management endpoint pointing to underlying Cloud Storage warehouse locations (`CreateIcebergCatalog`).
  * **[Update a catalog](https://docs.cloud.google.com/lakehouse/docs/update-catalog):** Upgrade an existing single bucket catalog to a multiple-bucket catalog (`UpdateIcebergCatalog`).
  * **[Create a namespace](https://docs.cloud.google.com/lakehouse/docs/create-namespace):** Create a namespace within an Iceberg REST catalog endpoint to group related tables (`CreateIcebergNamespace`).
  * **[Enable credential vending](https://docs.cloud.google.com/lakehouse/docs/enable-credential-vending):** Switch an existing catalog's authentication method to credential vending mode to vend short-lived storage tokens directly to query engines (`UpdateIcebergCatalog`).
  * **[Get catalog details](https://docs.cloud.google.com/lakehouse/docs/get-catalog-details):** View properties and metadata for your catalog, including the REST catalog URI required for client connections (`GetIcebergCatalog`).
  * **[Manage namespace ACLs](https://docs.cloud.google.com/lakehouse/docs/manage-tables-acl#apply-acl-namespaces):** View and update IAM policies on your catalog namespaces to control access for specific principals (`get-iam-policy`, `set-iam-policy`).
  * **[Delete a catalog](https://docs.cloud.google.com/lakehouse/docs/delete-catalog):** Unregister a catalog metadata management endpoint from the Lakehouse runtime catalog (`DeleteIcebergCatalog`).
  * **[Delete a namespace](https://docs.cloud.google.com/lakehouse/docs/delete-namespace):** Delete a namespace from your Iceberg REST catalog when it is no longer needed (`DeleteIcebergNamespace`).
  * **[View audit logs](https://docs.cloud.google.com/lakehouse/docs/view-audit-logs):** Inspect Cloud Audit Logs for verifiable records of administrative and data access activities.



## Pricing

For pricing details, see [Lakehouse pricing](https://cloud.google.com/products/biglake/pricing).

## What's next

  * Learn how to [manage namespace ACLs](https://docs.cloud.google.com/lakehouse/docs/manage-tables-acl#apply-acl-namespaces).
  * Learn more about the [Apache Iceberg REST catalog endpoint](https://docs.cloud.google.com/lakehouse/docs/lakehouse-iceberg-rest-catalog).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
