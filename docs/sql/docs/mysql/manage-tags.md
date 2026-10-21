---
url: https://docs.cloud.google.com/sql/docs/mysql/manage-tags/
title: Attach and manage tags on Cloud SQL instances \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:45.691636+00:00
---

# Attach and manage tags on Cloud SQL instances  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/manage-tags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Attach and manage tags on Cloud SQL instances Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/manage-tags "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/manage-tags "View this page for the SQL Server database engine")

This page describes how to attach, detach, and list tags on Cloud SQL instances. For an overview of tags on Cloud SQL, see [Access control with Google Cloud tags](https://docs.cloud.google.com/sql/docs/mysql/tags).

## Before you begin

Tags are managed through the Resource Manager. You need the following Cloud SQL IAM permissions to view and set tags on Cloud SQL instances:

  * `cloudsql.instances.createTagBinding`
  * `cloudsql.instances.deleteTagBinding`
  * `cloudsql.instances.listTagBindings`
  * `resourcemanager.tagUser`



The `cloudsql` permissions are inherited through the `cloudsql.admin` IAM role. The `resourcemanager.tagUser` is required to tag and instance during instance creation

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

  * For an overview of tags on Cloud SQL, see [Access control with Google Cloud tags](https://docs.cloud.google.com/sql/docs/mysql/tags)
  * For more detailed instructions, see [Attach tags to resources](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#attaching).
  * Learn about [IAM conditionals](https://docs.cloud.google.com/sql/docs/mysql/iam-overview#iam-conditions).
  * Learn how to [use IAM conditionals with Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/iam-conditions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
