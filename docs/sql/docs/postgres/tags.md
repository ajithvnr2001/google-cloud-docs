---
url: https://docs.cloud.google.com/sql/docs/postgres/tags/
title: Access control with Google Cloud tags \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:46.769258+00:00
---

# Access control with Google Cloud tags  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/tags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Access control with Google Cloud tags Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/tags "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/tags "View this page for the SQL Server database engine")

This page describes Google Cloud tags and how to use them with Cloud SQL. To add tags to your Cloud SQL instances using `gcloud` now, see [Attach and manage tags on Cloud SQL instances](https://docs.cloud.google.com/sql/docs/postgres/manage-tags). To add tags to your Cloud SQL instances using the Google Cloud console now, see [Create and manage tags on your instance](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing).

## Overview

Google Cloud _tags_ are a way to organize your Cloud SQL resources.

Tags are applied at higher levels of the [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) across Google Cloud. Cloud SQL and other instances inherit the tags. They are managed using [Resource Manager](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview). You can add a reference to tags in [IAM policy bindings](https://docs.cloud.google.com/iam/docs/tags-access-control) to grant conditional access to resources.

Tags are different from [labels](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels#what-are-labels), which are another way to organize and filter your instances. Tags and labels work independently of each other, and you can use both on the same instance. For more information about using labels in Cloud SQL, see [Label instances](https://docs.cloud.google.com/sql/docs/mysql/label-instance).

## What are tags?

Tags are key-value pairs you can apply to your resources for fine-grained access control.

A tag key could be a property, such as `environment`, and the tag value could be an attribute, such as `development` or `production`. A tag can have only one value for a given key on a particular resource.

Tags are created at the Organization level. Tags are attached to resources, such as a project or a Cloud SQL instance, through the [Resource Manager](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview), which is used across Google Cloud.

## Grant permissions based on conditional tag bindings

Once a tag is attached to or inherited by a Cloud SQL instance, you can [use the tag](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#resource-tags) with IAM Conditions to grant access to Cloud SQL resources conditionally. IAM Conditions let you impose fine-grain access control to Cloud SQL instances. To use IAM Conditions, you reference the tags in IAM policy bindings. For more information on how to use tags to grant conditional access to Cloud SQL instances, see [Use IAM conditions](https://docs.cloud.google.com/sql/docs/postgres/iam-conditions).

If you add tag-based bindings to an instance, then you can grant access to Cloud SQL resources conditionally. Based on this conditional access, you can see all backups of the active instance as well as the [final backups](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backups#final-backups) of instances that are deleted and have the same name. However, after you delete an instance with tag bindings, you can't see any backups related to the instance name. This is because you deleted the instance and the tags can no longer be determined.

## Restrictions

Tags have the following restrictions:

  * [Organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/tags-organization-policy) can conditionally reference tags inherited from the Project level and above, but don't support tags that are directly attached to Cloud SQL instances.
  * [Cloud Audit logs](https://docs.cloud.google.com/storage/docs/audit-logging) show the creation and deletion of tags, but entries are not generated for attaching tags and viewing tag bindings on Cloud SQL instances.



## What's next

  * Learn how to [create and manage tags on your instance](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing) using Resource Manager.
  * See specific `gcloud` commands for Cloud SQL in [Manage tags on Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/manage-tags).
  * Learn about [IAM conditions](https://docs.cloud.google.com/sql/docs/postgres/iam-overview#iam-conditions).
  * Learn how to [use IAM conditions with Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/iam-conditions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
