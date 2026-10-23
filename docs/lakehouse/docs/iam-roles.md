---
url: https://docs.cloud.google.com/lakehouse/docs/iam-roles/
title: Borderless Lakehouse IAM roles \u00a0|\u00a0 BigLake API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:48.676402+00:00
---

# Borderless Lakehouse IAM roles  |  BigLake API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/iam-roles/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ BigLake API ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



#  Borderless Lakehouse IAM roles Stay organized with collections  Save and categorize content based on your preferences. 

_Borderless Lakehouse_ defines several [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam) roles for managing resources. Each predefined role contains a set of IAM permissions that allow principals to perform certain actions. You can use an IAM policy to give a principal one or more IAM roles.

IAM also offers the ability to create customized IAM roles. You can create custom IAM roles and assign the role one or more permissions. Then, you can grant the new role to your principals. Use custom roles to create an access control model that maps directly to your needs, alongside the available predefined roles.

This page focuses on the IAM roles relevant to the _Lakehouse runtime catalog_.

## Before you begin

  * Read the [IAM](https://docs.cloud.google.com/iam) documentation.



## Lakehouse roles

IAM Lakehouse roles are a bundle of one or more permissions. You grant roles to principals to allow them to perform actions on the Lakehouse resources in your project. For example, the BigLake Viewer role contains the `biglake.*.get` and `biglake.*.list` permissions, which allow a user to get and list Lakehouse resources in a project.

The following table lists all Lakehouse roles and the permissions associated with each role:

Role | Permissions  
---|---  
  
#### BigLake Admin 

(`roles/biglake.admin`) Provides full access to all BigLake resources.  |  `biglake.*`

  * `biglake.catalogs.create`
  * `biglake.catalogs.delete`
  * `biglake.catalogs.get`
  * `biglake.catalogs.getIamPolicy`
  * `biglake.catalogs.list`
  * `biglake.catalogs.setIamPolicy`
  * `biglake.catalogs.update`
  * `biglake.databases.create`
  * `biglake.databases.delete`
  * `biglake.databases.get`
  * `biglake.databases.list`
  * `biglake.databases.update`
  * `biglake.locks.check`
  * `biglake.locks.create`
  * `biglake.locks.delete`
  * `biglake.locks.list`
  * `biglake.namespaces.create`
  * `biglake.namespaces.delete`
  * `biglake.namespaces.get`
  * `biglake.namespaces.getIamPolicy`
  * `biglake.namespaces.list`
  * `biglake.namespaces.setIamPolicy`
  * `biglake.namespaces.update`
  * `biglake.tables.create`
  * `biglake.tables.createPartitions`
  * `biglake.tables.delete`
  * `biglake.tables.deletePartitions`
  * `biglake.tables.get`
  * `biglake.tables.getData`
  * `biglake.tables.getIamPolicy`
  * `biglake.tables.list`
  * `biglake.tables.listPartitions`
  * `biglake.tables.lock`
  * `biglake.tables.register`
  * `biglake.tables.setIamPolicy`
  * `biglake.tables.update`
  * `biglake.tables.updateData`
  * `biglake.tables.updatePartitions`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### BigLake Editor Beta

(`roles/biglake.editor`) Provides read and write access to all BigLake resources.  |  `biglake.catalogs.create` `biglake.catalogs.delete` `biglake.catalogs.get` `biglake.catalogs.getIamPolicy` `biglake.catalogs.list` `biglake.catalogs.update` `biglake.databases.*`

  * `biglake.databases.create`
  * `biglake.databases.delete`
  * `biglake.databases.get`
  * `biglake.databases.list`
  * `biglake.databases.update`

`biglake.locks.*`

  * `biglake.locks.check`
  * `biglake.locks.create`
  * `biglake.locks.delete`
  * `biglake.locks.list`

`biglake.namespaces.create` `biglake.namespaces.delete` `biglake.namespaces.get` `biglake.namespaces.getIamPolicy` `biglake.namespaces.list` `biglake.namespaces.update` `biglake.tables.create` `biglake.tables.createPartitions` `biglake.tables.delete` `biglake.tables.deletePartitions` `biglake.tables.get` `biglake.tables.getData` `biglake.tables.getIamPolicy` `biglake.tables.list` `biglake.tables.listPartitions` `biglake.tables.lock` `biglake.tables.update` `biglake.tables.updateData` `biglake.tables.updatePartitions` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### BigLake Viewer 

(`roles/biglake.viewer`) Provides read-only access to all BigLake resources.  |  `biglake.catalogs.get` `biglake.catalogs.getIamPolicy` `biglake.catalogs.list` `biglake.databases.get` `biglake.databases.list` `biglake.locks.list` `biglake.namespaces.get` `biglake.namespaces.getIamPolicy` `biglake.namespaces.list` `biglake.tables.get` `biglake.tables.getData` `biglake.tables.getIamPolicy` `biglake.tables.list` `biglake.tables.listPartitions` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### BigLake Metadata Viewer Beta

(`roles/biglake.metadataViewer`) Provides read-only metadata access to all BigLake resources.  |  `biglake.catalogs.get` `biglake.catalogs.getIamPolicy` `biglake.catalogs.list` `biglake.namespaces.get` `biglake.namespaces.getIamPolicy` `biglake.namespaces.list` `biglake.tables.get` `biglake.tables.getIamPolicy` `biglake.tables.list` `biglake.tables.listPartitions` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## What's next

  * Learn how to [create custom IAM roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).
  * Learn how to [grant and manage roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
