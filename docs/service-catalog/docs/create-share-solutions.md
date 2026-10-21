---
url: https://docs.cloud.google.com/service-catalog/docs/create-share-solutions/
title: Quickstart: Create and share solutions by using Service Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:40:49.318558+00:00
---

# Quickstart: Create and share solutions by using Service Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-catalog/docs/create-share-solutions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Service Catalog ](https://docs.cloud.google.com/service-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/service-catalog/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create and share solutions by using Service Catalog

This page shows you how to do basic tasks in Service Catalog using the Google Cloud console.

## What you learn

  * How to create a catalog and share a solution as a Service Catalog admin
  * How to view and launch a solution as a Service Catalog user



## Before you begin

  * You must have a Google Cloud organization. If you don't have one, see [Creating and managing organizations](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization).
  * You must have the following [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/iam/docs/understanding-roles) at the organization level:

    * [Organization Administrator](https://docs.cloud.google.com/resource-manager/docs/access-control-org#using_predefined_roles) (`roles/resourcemanager.organizationAdmin`)
    * [Catalog Org Admin](https://docs.cloud.google.com/service-catalog/docs/access-control#catalog_org_admin_role) (`roles/cloudprivatecatalogproducer.orgAdmin`)

As Organization Administrator, you can grant yourself the remaining IAM roles. For steps on granting roles, see [Access control](https://docs.cloud.google.com/service-catalog/docs/access-control#adding_users).

  * Set up Service Catalog for your organization:

    1. Go to the [Service Catalog Admin page](https://console.cloud.google.com/catalog/admin) and click **ENABLE**.   
[Go to the Service Catalog Admin page](https://console.cloud.google.com/catalog/admin)
    2. Select or create a Google Cloud project.
    3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

Service Catalog is free to use, but we require billing information in case your organization incurs costs while creating or deploying a solution, such as using Cloud Build to deploy a Terraform solution.


**Note:** Third-Party Software: The Customer agrees not to upload third-party software to Service Catalog, unless the customer has the appropriate third-party software licenses to do so.

## Create a catalog

A _catalog_ is where you curate solutions that Service Catalog users can view and launch.

To create a catalog:

  1. In the Google Cloud console, go to the Service Catalog [Admin page](https://console.cloud.google.com/catalog/admin).   
[Go to the Service Catalog Admin page](https://console.cloud.google.com/catalog/admin)
  2. On the **Catalogs** page, click **CREATE CATALOG**.
  3. Enter a name and description for the catalog.
  4. Click **Create**.



The catalog now appears in the **Catalogs** table.

## Create a link-based solution

In the following steps, you create a link-based solution, or reference link, to Service Catalog and then assign the solution to your catalog.

### Create solution in Service Catalog

  1. Go to the Service Catalog Admin [**Solutions** page](https://console.cloud.google.com/catalog/admin/solutions) in the Google Cloud console.   
[Go to the Solutions page](https://console.cloud.google.com/catalog/admin/solutions)
  2. Click **CREATE SOLUTION**. In the drop-down list, select **Create a Link solution**.
  3. Enter a name, URL, description, and tagline for your solution. The tagline is the short description shown on the tile in the end-user Service Catalog view.
  4. Optionally, upload an icon for the solution.
  5. Optionally, add a link for getting support.
  6. Optionally, add a link to documentation for the solution.
  7. Click **CREATE**.



The following screenshot illustrates creating a link-based solution:

![Form to create a link-based solution](https://docs.cloud.google.com/static/service-catalog/images/screen-privatecatalog-create-link.png)

The solution now appears in the **Solutions** table.

### Assign solution to your catalog

  1. Go to the Service Catalog Admin [**Solutions** page](https://console.cloud.google.com/catalog/admin/solutions) in the Google Cloud console.   
[Go to the Solutions page](https://console.cloud.google.com/catalog/admin/solutions)
  2. In the list of solutions, find your link-based solution and click **Assign to Catalogs**.
  3. In the **Assigned Catalogs** window, check the box next to your catalog.
  4. Click **SAVE**.



The solution now appears in your catalog.

## Share your catalog

Share your catalog with a Google Cloud resource, such as your organization, a folder, or a project, so that Service Catalog users who have access to that resource can view and launch the link-based solution in your catalog.

To share your catalog:

  1. Go to the Service Catalog Admin [**Catalogs** page](https://console.cloud.google.com/catalog/admin/catalogs) in the Google Cloud console.   
[Go to the Catalogs page](https://console.cloud.google.com/catalog/admin/catalogs)
  2. From the list of catalogs, click the catalog name.
  3. On the **Catalog Details** page, click **SHARE**.

![Share a catalog button](https://docs.cloud.google.com/static/service-catalog/images/screen-privatecatalog-share-catalog.png)
  4. Select a folder, organization, or project that you want to share the catalog with, and then click **Select**.




Your catalog is now shared with the folder, organization, or project you selected.

## View and launch a solution

Service Catalog users can see solutions from all the catalogs that are shared with them in their Google Cloud resource hierarchy.

To access and deploy a solution as a user:

  1. Go to [Service Catalog](https://console.cloud.google.com/project/_/catalog) page in the Google Cloud console.   
[Go to the Service Catalog page](https://console.cloud.google.com/project/_/catalog)

  2. In the main panel, you see the link-based solution that has been shared in your organization. Click the solution to go to its **Details** page.

  3. Click **Go to link**.

This button takes you to a link outside of the Google domain where you can download and launch the solution.




## Clean up

To avoid unnecessary Google Cloud charges, use the Google Cloud console to delete your project if you no longer need it.

## What's next

  * Read the [Service Catalog overview](https://docs.cloud.google.com/service-catalog/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
