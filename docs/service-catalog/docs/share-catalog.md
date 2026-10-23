---
url: https://docs.cloud.google.com/service-catalog/docs/share-catalog/
title: Sharing a catalog \u00a0|\u00a0 Service Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:28:44.172711+00:00
---

# Sharing a catalog  |  Service Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-catalog/docs/share-catalog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Service Catalog ](https://docs.cloud.google.com/service-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/service-catalog/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Sharing a catalog

In this guide, you learn how to share a catalog with users in your organization.

After you assign solutions to a catalog, you must share the catalog to a [Google Cloud resource](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy), such as a project, folder, or organization. Users who have access to the resource can then view and launch the catalog's solutions. When users browse Service Catalog, they only see solutions from catalogs that have been shared with them.

## Before you begin

  * You must have the [Catalog Admin](https://docs.cloud.google.com/service-catalog/docs/access-control#instance_admin_role) (`roles/cloudprivatecatalogproducer.admin`) _OR_ [Catalog Manager](https://docs.cloud.google.com/service-catalog/docs/access-control#catalog_manager_role) (`roles/cloudprivatecatalogproducer.manager`) role for the Google Cloud project where Service Catalog is enabled, and the folder, project, or organization where you're sharing the catalog. If you don't have either role, contact your Organization Administrator to request access.
  * Grant the following [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/iam/docs/understanding-roles) to users who will use the shared catalog:

    * [Catalog Consumer](https://docs.cloud.google.com/service-catalog/docs/access-control#catalog_consumer) (`roles/cloudprivatecatalog.consumer`) _OR_ the [IAM Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`) role for the relevant organization, project, or folder. Most users access Service Catalog using the IAM Viewer role.
    * If your catalog contains DM-based solutions, the [Deployment Manager Editor](https://docs.cloud.google.com/deployment-manager/docs/access-control#roles) (`roles/deploymentmanager.editor`) role for the project where your users deploy the solution.

For steps on granting IAM roles, see [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). For details on Service Catalog's IAM roles and permissions, see [Access control](https://docs.cloud.google.com/service-catalog/docs/access-control).




## Sharing a catalog

Make sure to share the catalog to a resource that your users can access. End users can only see catalogs that are shared to a Google Cloud organization, folder, or project that they have access to.

If you're sharing a catalog with a new project, users are prompted to enable the Service Catalog API when launching a solution. If launching a DM-based solution to a new project, they are also prompted to enable the Cloud Deployment Manager API.

To share a catalog:

  1. In the Google Cloud console, go to the Service Catalog [Admin page](https://console.cloud.google.com/catalog/admin).   
[Go to the Service Catalog Admin page](https://console.cloud.google.com/catalog/admin)
  2. Click **Select** to choose the Google Cloud project.
  3. Go to the **Catalogs** page.
  4. From the list of catalogs, click the catalog name.
  5. On the **Catalog Details** page, click **SHARE**.

![Share a catalog button](https://docs.cloud.google.com/static/service-catalog/images/screen-privatecatalog-share-catalog.png)
  6. Select a folder, organization, or project that you want to share the catalog with, and then click **Select**.




Users who have access to the shared catalog can now view and launch its solutions.

## Unsharing a catalog

When you unshare a catalog, users who had access to the catalog can no longer view or deploy its solutions. Unsharing a catalog doesn't affect your users' existing deployments.

To unshare a catalog:

  1. On the **Catalog Details** page, go to the **SHARING** tab.
  2. In the **Shared with** table, click **UNSHARE** for any organization, folder, or project from which you want to unshare the catalog.
  3. Click **CONFIRM**.



Your catalog is no longer shared with the resource.

## Next steps

  * [Viewing and launching a solution](https://docs.cloud.google.com/service-catalog/docs/view-and-launch).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
