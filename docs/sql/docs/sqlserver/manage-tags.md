---
url: https://docs.cloud.google.com/sql/docs/sqlserver/manage-tags/
title: Attach and manage tags on Cloud SQL instances \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:04.872493+00:00
---

# Attach and manage tags on Cloud SQL instances  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/manage-tags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Attach and manage tags on Cloud SQL instances Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/manage-tags "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/manage-tags "View this page for the PostgreSQL database engine") | SQL Server

This page describes how to attach, detach, and list tags on Cloud SQL instances. For an overview of tags on Cloud SQL, see [Access control with Google Cloud tags](https://docs.cloud.google.com/sql/docs/sqlserver/tags).

## Before you begin

Tags are managed through Resource Manager. To create and define tags before attaching them to Cloud SQL instances, see [Creating and managing tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing).

### Required roles

To get the permissions that you need to view and manage tags on Cloud SQL instances, ask your administrator to grant you the following IAM roles: 

  * Manage Cloud SQL instances and tag bindings: [Cloud SQL Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`) on the project 
  * Attach and detach tags on Cloud SQL instances: [Tag User ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`) on the tag value and the project 
  * View and list tags on Cloud SQL instances: [Tag Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`) on the project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to view and manage tags on Cloud SQL instances. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view and manage tags on Cloud SQL instances:

  * Create an instance with a tag attached: 
    * `cloudsql.instances.create`
    * `cloudsql.instances.createTagBinding`
    * `resourcemanager.tagValueBindings.create`
  * Attach a tag to an instance: 
    * `cloudsql.instances.createTagBinding`
    * `resourcemanager.tagValueBindings.create`
  * Detach a tag from an instance: 
    * `cloudsql.instances.deleteTagBinding`
    * `resourcemanager.tagValueBindings.delete`
  * List tags on an instance: 
    * `cloudsql.instances.listTagBindings`
    * `cloudsql.instances.listEffectiveTags`
    * `resourcemanager.tagKeys.get`
    * `resourcemanager.tagKeys.list`
    * `resourcemanager.tagValues.get`
    * `resourcemanager.tagValues.list`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a Cloud SQL instance with a tag

To create an instance with a tag attached, use the `--tags` flag when creating the instance. This combines the tags with organization policies, custom organization policies, and IAM conditions to give more customization to instance creation policies.

For example, the following command creates an instance in the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) with the 1234 tag with a value of 5678 [`gcloud sql instances create tags-instance --tags=tagKeys/1234=tagValues/5678`]

## Attach tags to Cloud SQL instances

Once you've [created and defined](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#creating) a tag using Resource Manager, you can attach the tag to a Cloud SQL instance. To attach a tag to a Cloud SQL instance, create a tag binding by running the [`gcloud resource-manager tags bindings create`](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/bindings/create) command:
    
    
    gcloud resource-manager tags bindings create \
    --tag-value=TAG_VALUE_ID \
    --parent=PARENT \
    --location=LOCATION

In the previous command, make the following replacements:

  * TAG_VALUE_ID: the permanent ID or the namespaced name of the tag value. For example, `tagValues/4567890123` or `12345678/environment/production`. For more information about tag identifiers, see [Tag definitions and identifiers](https://docs.cloud.google.com/iam/docs/tags-access-control#definitions).

  * PARENT: the full resource name of the Cloud SQL instance to attach the tag to. For example, `//sqladmin.googleapis.com/projects/my-project/instances/my-instance`.

  * LOCATION: the regional location of the Cloud SQL resource. For example, `us-central1`.




## Detach tags from Cloud SQL instances

The [`gcloud resource-manager tags bindings delete`](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/bindings/delete) command detaches the tag from `my-instance`:
    
    
    gcloud resource-manager tags bindings delete \
    --tag-value=815471563813/environment/development \
    --parent=//sqladmin.googleapis.com/projects/my-project/instances/my-instance \
    --location=us-central1
    

## List tags on Cloud SQL instances

The [`gcloud resource-manager tags bindings list`](https://docs.cloud.google.com/sdk/gcloud/reference/resource-manager/tags/bindings/list) command lists all tags directly attached to `my-instance`, except tags that `my-instance` has inherited:
    
    
    gcloud resource-manager tags bindings list \
        --parent=//sqladmin.googleapis.com/projects/my-project/instances/my-instance \
        --location=us-central1
    

## What's next

  * For an overview of tags on Cloud SQL, see [Access control with Google Cloud tags](https://docs.cloud.google.com/sql/docs/sqlserver/tags)
  * For more detailed instructions, see [Attach tags to resources](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#attaching).
  * Learn about [IAM conditionals](https://docs.cloud.google.com/sql/docs/sqlserver/iam-overview#iam-conditions).
  * Learn how to [use IAM conditionals with Cloud SQL](https://docs.cloud.google.com/sql/docs/sqlserver/iam-conditions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
