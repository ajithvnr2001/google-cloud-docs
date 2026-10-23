---
url: https://docs.cloud.google.com/sql/docs/sqlserver/iam-authentication/
title: IAM authentication \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:15.929951+00:00
---

# IAM authentication  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/iam-authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  IAM authentication Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/iam-authentication "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/iam-authentication "View this page for the PostgreSQL database engine") | SQL Server

Google Cloud offers Identity and Access Management (IAM), which lets you give access to specific Google Cloud resources and prevent unwanted access to other resources. This page describes how Cloud SQL is integrated with IAM . For a detailed description of Google Cloud IAM, see [IAM documentation](https://docs.cloud.google.com/iam/docs).

Cloud SQL provides a set of [predefined roles](https://docs.cloud.google.com/sql/docs/sqlserver/iam-roles) designed to help you control access to your Cloud SQL resources. You can also create your own [custom roles](https://docs.cloud.google.com/sql/docs/sqlserver/iam-roles#custom-roles), if the predefined roles don't provide the sets of permissions you need. In addition, the legacy basic roles (Editor, Viewer, and Owner) are also still available to you, although they don't provide the same fine-grained control as the Cloud SQL roles. In particular, the basic roles provide access to resources across Google Cloud, rather than just for Cloud SQL. For more information about basic Google Cloud roles, see [Basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic).

You can set an IAM policy at any level in the [resource hierarchy](https://docs.cloud.google.com/iam/docs/overview#resource-hierarchy): the organization level, the folder level, or the project level. Resources inherit the policies of all of their parent resources.

Cloud SQL for SQL Server supports IAM authentication for instance and backup operations only. IAM authentication isn't supported for database operations. Use the following authentication options for database operations and queries:

  * [Built-in database authentication using username and passwords](https://docs.cloud.google.com/sql/docs/sqlserver/built-in-authentication)
  * [Customer-managed Active Directory](https://docs.cloud.google.com/sql/docs/sqlserver/cmad)
  * [Managed Service for Microsoft Active Directory](https://docs.cloud.google.com/sql/docs/sqlserver/ad)



## IAM references for Cloud SQL

  * [Required permissions for common tasks in the Google Cloud console](https://docs.cloud.google.com/sql/docs/sqlserver/iam-permissions#permissions-console)
  * [Required permissions for `gcloud sql` commands](https://docs.cloud.google.com/sql/docs/sqlserver/iam-permissions#permissions-gcloud)
  * [Required permissions for Cloud SQL Admin API methods](https://docs.cloud.google.com/sql/docs/sqlserver/iam-permissions#api-methods)
  * [Predefined Cloud SQL IAM roles](https://docs.cloud.google.com/sql/docs/sqlserver/iam-roles#roles)
  * [Permissions and their roles](https://docs.cloud.google.com/sql/docs/sqlserver/iam-roles#permissions-roles)
  * [Custom roles](https://docs.cloud.google.com/sql/docs/sqlserver/iam-roles#custom-roles)



## IAM authentication concepts

When using IAM authentication, permission to access a resource (a Cloud SQL instance) isn't granted _directly_ to the end user. Instead, permissions are grouped into _roles_ , and roles are granted to _principals_. For more information, see the [IAM overview](https://docs.cloud.google.com/iam/docs/overview).

IAM policies involve the following entities:

  * **Principals**. In Cloud SQL, you can use two types of principals: a _user account_ , and a _service account_ (for applications). For more information, see [Concepts related to identity](https://docs.cloud.google.com/iam/docs/overview#concepts_related_identity).
  * **Roles**. A role is a collection of permissions. You can grant roles to principals to provide them with the privileges required to accomplish specific tasks. For more information about IAM roles, see [Roles](https://docs.cloud.google.com/iam/docs/overview#roles).
  * **Resource**. The resources that principals access are Cloud SQL instances. By default, IAM policy bindings are applied at the project-level, such that principals receive role permissions for all Cloud SQL instances in the project.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
