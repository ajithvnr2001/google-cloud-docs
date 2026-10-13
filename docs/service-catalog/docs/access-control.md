---
url: https://docs.cloud.google.com/service-catalog/docs/access-control/
title: Access control with IAM \u00a0|\u00a0 Service Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:02:57.769984+00:00
---

# Access control with IAM  |  Service Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-catalog/docs/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Service Catalog ](https://docs.cloud.google.com/service-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/service-catalog/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Access control with IAM

This page explains how you grant and manage access to Service Catalog using Identity and Access Management (IAM).

### Before you begin

  * You must have Service Catalog [enabled for your Google Cloud organization](https://docs.cloud.google.com/service-catalog/docs/quickstart#before_you_begin).
  * To grant Service Catalog IAM roles, you must have the [Organization Administrator](https://docs.cloud.google.com/resource-manager/docs/access-control-org#using_predefined_roles) (`roles/resourcemanager.organizationAdmin`) role for your Google Cloud organization.



## What is Identity and Access Management (IAM)?

Google Cloud offers [Identity and Access Management (IAM)](https://cloud.google.com/iam/), which lets you give more granular access to specific Google Cloud resources and prevents unwanted access to other resources. IAM lets you adopt the [security principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege) , so you grant only the necessary access to your resources.

IAM lets you control **who (identity)** has **what (roles)** permissions to **which** resources by setting IAM policies. IAM policies grant specific role(s) to a principal, giving the identity certain permissions.

For example, for a given resource, such as a project, you can assign the `roles/compute.networkAdmin` role to a Google account and that account can control network-related resources in the project, but cannot manage other resources, like instances and disks.

## Service Catalog IAM roles

With IAM, every API method in both the Service Catalog API and Service Catalog Producer API require that the identity making the API request has the appropriate permissions to use the resource. Permissions are granted by setting policies that grant roles to a principal, such as a user, group, or service account. In addition to the basic roles, [Owner, Editor, and Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic), you can assign the Service Catalog and Service Catalog Producer roles described in this page to principals.

**Note:** You can grant multiple roles to a principal on the same resource. For example, you can grant both `roles/cloudprivatecatalogproducer.admin` and `roles/cloudprivatecatalogproducer.manager` to your cloud admin team's [Google group](https://cloud.google.com/iam/docs/overview#google_group).

The following tables list the IAM roles available to Service Catalog users. The tables are organized into different roles.

### Catalog Org Admin

**Role name** | **Description** | **Includes permissions** | `roles/cloudprivatecatalogproducer.orgAdmin` | Manages Service Catalog settings at the Google Cloud organization level. Creates and manages Service Catalog resources, such as solutions and catalogs. | 

  * `cloudprivatecatalogproducer.settings.*`
  * `cloudprivatecatalogproducer.catalogs.*`
  * `cloudprivatecatalogproducer.associations.*`
  * `cloudprivatecatalogproducer.targets.*`
  * `cloudprivatecatalogproducer.producerCatalogs.*`
  * `cloudprivatecatalogproducer.catalogAssociations.*`
  * `cloudprivatecatalogproducer.products.*`
  * `cloudprivatecatalog.targets.*`
  * `resourcemanager.projects.get`
  * `resourcemanager.projects.list`
  * `resourcemanager.folders.get`
  * `resourcemanager.folders.list`
  * `resourcemanager.organizations.get`

  
---|---|---  
  
### Catalog Admin

**Role name** | **Description** | **Includes permissions** | `roles/cloudprivatecatalogproducer.admin` | Creates and manages Service Catalog resources, such as solutions and catalogs. | 

  * `cloudprivatecatalogproducer.catalogs.* `
  * `cloudprivatecatalogproducer.associations.*`
  * `cloudprivatecatalogproducer.targets.*`
  * `cloudprivatecatalogproducer.producerCatalogs.*`
  * `cloudprivatecatalogproducer.catalogAssociations.*`
  * `cloudprivatecatalogproducer.products.*`
  * `cloudprivatecatalog.targets.*`
  * `resourcemanager.projects.get`
  * `resourcemanager.projects.list`
  * `resourcemanager.folders.get`
  * `resourcemanager.folders.list`
  * `resourcemanager.organizations.get`

  
---|---|---  
  
### Catalog Manager

**Role name** | **Description** | **Includes permissions** | `roles/cloudprivatecatalogproducer.manager` | Views solutions and catalogs, and shares catalogs with Service Catalog users. | 

  * `cloudprivatecatalog.targets.get`
  * `cloudprivatecatalogproducer.catalogs.get`
  * `cloudprivatecatalogproducer.catalogs.list`
  * `cloudprivatecatalogproducer.targets.*`
  * `cloudprivatecatalogproducer.associations.*`
  * `cloudprivatecatalogproducer.producerCatalogs.get`
  * `cloudprivatecatalogproducer.producerCatalogs.list`
  * `cloudprivatecatalogproducer.catalogAssociations.*`
  * `resourcemanager.projects.get`
  * `resourcemanager.projects.list`
  * `resourcemanager.folders.get`
  * `resourcemanager.folders.list`
  * `resourcemanager.organizations.get`

  
---|---|---  
  
### Catalog Consumer

**Role name** | **Description** | **Includes permissions** | `roles/cloudprivatecatalog.consumer` | Browses catalogs. Views and launches solutions. Operates under a target Google Cloud resource, such as an organization, project, or folder. | 

  * `cloudprivatecatalog.targets.get`
  * `resourcemanager.projects.get`
  * `resourcemanager.projects.list`

  
---|---|---  
  
## Adding users to Service Catalog IAM roles

Users, Google Groups, or domains must have the `resourcemanager.organizations.setIamPolicy` permission on the organization to add users to the Service Catalog IAM roles. You can give a user or group that permission by granting them the Organization Administrator role (`roles/resourcemanager.organizationAdmin`).

For example, if your organization would like users granted the Catalog Admin role to _also_ be able to add and remove users and groups from the other Service Catalog IAM roles, then an Organization Administrator can do the following:

  * Create a Google Group for the users (`MyCompanyCatalogAdmins`).
  * Assign the Google Group (`MyCompanyCatalogAdmins`) the Organization Administrator role.
  * Assign the Google Group (`MyCompanyCatalogAdmins`) the Catalog Admin role.



In the example, members of the Google Group (`MyCompanyCatalogAdmins`) can assign users and groups to IAM roles in the organization because the group has been granted the `setIamPolicy` permission when granted the Organization Administrator role. As new Catalog Administrators join the organization, add them to the Google Group (`MyCompanyCatalogAdmins`) to grant them the desired roles.

To add a user, group, or domain to a Service Catalog IAM role, follow these steps.

  1. Sign in to the Google Cloud console [IAM & admin page](https://console.cloud.google.com/iam-admin) as an Organization Administrator.   
[Go to the Google Cloud console IAM & admin page](https://console.cloud.google.com/iam-admin)
  2. Select **Cloud Private Catalog** from the side menu.
  3. Select the role to assign: 
     * **Catalog Admin**
     * **Catalog Manager**
     * **Catalog Consumer**
  4. Specify the users, groups, or domains to add.



## What's next

  * [Create a catalog](https://docs.cloud.google.com/service-catalog/docs/create-catalog).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
