---
url: https://docs.cloud.google.com/service-catalog/docs/assign-solutions/
title: Assigning solutions to a catalog \u00a0|\u00a0 Service Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:22.417622+00:00
---

# Assigning solutions to a catalog  |  Service Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-catalog/docs/assign-solutions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Service Catalog ](https://docs.cloud.google.com/service-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/service-catalog/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Assigning solutions to a catalog

In this guide, you learn how to assign Service Catalog solutions to a catalog. By curating solutions into catalogs, you control which users can view and launch approved solutions in your organization.

**Note:** Service Catalog users can only access solutions in shared catalogs. To share a catalog, see [Sharing a catalog](https://docs.cloud.google.com/service-catalog/docs/share-private-catalog).

You must create the solution in Service Catalog before you assign it to a catalog. To create one, see [Creating Solutions](https://docs.cloud.google.com/service-catalog/docs/create-solutions).

## Before you begin

  * You must have Service Catalog [enabled for your Google Cloud organization](https://docs.cloud.google.com/service-catalog/docs/quickstart#before_you_begin).
  * You must have the [Catalog Admin](https://docs.cloud.google.com/service-catalog/docs/access-control#instance_admin_role) (`roles/cloudprivatecatalogproducer.admin`) _OR_ [Catalog Manager](https://docs.cloud.google.com/service-catalog/docs/access-control#catalog_manager_role) (`roles/cloudprivatecatalogproducer.manager`) role for the Google Cloud project where Service Catalog is enabled. If you don't have either role, contact your Organization Administrator to request access.
  * [Create a catalog](https://docs.cloud.google.com/service-catalog/docs/create-catalog) for your solutions.



## Assigning solutions to a catalog

To assign solutions:

  1. Go to the Service Catalog Admin [**Solutions** page](https://console.cloud.google.com/project/_/catalog/admin/solutions) in the Google Cloud console.   
[Go to the Solutions page](https://console.cloud.google.com/project/_/catalog/admin/solutions)
  2. Click **Select** to choose the Google Cloud project.
  3. For each solution you want to assign, find the solution in the list and click **Assign to Catalogs**.
  4. In the **Assigned Catalogs** window, check the box for the catalog.
  5. Click **SAVE**.



The solution now appears in the catalog. If you've already [shared the catalog](https://docs.cloud.google.com/service-catalog/docs/share-catalog) to a Google Cloud resource, users who have access to the resource can now view and launch the solution.

## Removing a solution from a catalog

When you remove a solution, end users can no longer view or deploy the solution in the catalog. Removing the solution doesn't delete it from Service Catalog and doesn't affect your users' existing deployments. To remove a solution from all associated catalogs and delete it from Service Catalog, see [deleting solutions from Service Catalog](https://docs.cloud.google.com/service-catalog/docs/manage-solutions#delete_solutions).

To remove a solution from a catalog:

  1. Go to the Service Catalog Admin [**Solutions** page](https://console.cloud.google.com/project/_/catalog/admin/solutions) in the Google Cloud console.   
[Go to the Solutions page](https://console.cloud.google.com/project/_/catalog/admin/solutions)
  2. Find the solution and in the **Assigned catalogs** column, click the icon to modify catalogs.
  3. In the **Assigned Catalogs** window, uncheck the catalog.
  4. Click **SAVE**.



Your solution no longer appears in the catalog.

## Next steps

  * [Share a catalog](https://docs.cloud.google.com/service-catalog/docs/share-catalog) with users in your organization, so that they can access and deploy your solution.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
