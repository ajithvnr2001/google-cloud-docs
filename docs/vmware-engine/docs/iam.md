---
url: https://docs.cloud.google.com/vmware-engine/docs/iam/
title: VMware Engine IAM roles and permissions \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:25.652717+00:00
---

# VMware Engine IAM roles and permissions  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/iam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# VMware Engine IAM roles and permissions

When you add a new member to your project, you can use an [ Identity and Access Management (IAM)](https://docs.cloud.google.com/iam) policy to give that member one or more IAM roles. Each IAM role contains permissions that grant the member access to VMware Engine resources.

This document focuses on the IAM permissions relevant to VMware Engine and the [IAM roles](https://docs.cloud.google.com/iam/docs/understanding-roles) that grant those permissions. For a detailed description of IAM and its features, see the [Identity and Access Management Overview](https://docs.cloud.google.com/iam/docs/overview) and [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Role types

You grant access to a resource by setting an IAM policy on the resource. The policy binds one or more members, such as a user or a service account, to one or more roles. Each role contains a list of permissions that let the member interact with the resource.

There are three types of roles in IAM:

  * **Predefined roles** provide granular access for a specific service and are managed by Google Cloud. Predefined roles are designed to support common use cases and access control patterns.
  * **Custom roles** provide granular access according to a user-specified list of permissions.
  * **Basic roles** are project-level roles which include broad permissions that apply to all of your Google Cloud resources. Basic roles include the Owner, Editor, and Viewer roles that existed prior to the introduction of IAM.



We recommend using a _predefined role_ or a _custom role_ whenever possible, as they include more fine-grained permissions that apply only to VMware Engine.

### Predefined roles

A predefined role contains a set of permissions that's suitable for a specific task. Specific permissions and roles apply only to Google Cloud CLI and VMware Engine API. To view a comprehensive list of predefined roles for VMware Engine, go to the [VMware Engine roles reference](https://docs.cloud.google.com/iam/docs/roles-permissions/vmwareengine) on the IAM documentation.

### Custom roles

If the predefined roles for VMware Engine don't meet your needs, then you can create a custom role that contains only the permissions that you specify. Identify the tasks that you need to perform, then add the permissions that are required for each task to the custom role.

To view a comprehensive list of permissions for VMware Engine, go to the [Permissions reference](https://docs.cloud.google.com/iam/docs/permissions-reference) and search for the prefix `vmwareengine`.

For more details on creating a custom role, see [Creating and managing custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

## Grant or revoke access to VMware Engine

Roles apply to VMware Engine resources at the project level. A role cannot be applied to an individual private cloud if a project contains multiple private clouds.

### Grant access

To add a team member to a project and grant them a VMware Engine role, do the following:

  1. In the Google Cloud console, go to **IAM & Admin > IAM**.

[Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

  2. Click **Add**.

  3. Enter an email address. You can add individuals, service accounts, or Google Groups as members.

  4. Select the `VMware Engine Service Viewer` or `VMware Engine Service Admin` role based on the type of access that the user or group needs.

  5. Click **Save**.




### Revoke access

To remove a role and its corresponding permissions from a user or group, do the following:

  1. In the Google Cloud console, go to **IAM & Admin > IAM**.

[Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

  2. Locate the user or group from which you want to revoke access and click **Edit member**.

  3. For each role you want to revoke, click **Delete**.

  4. Click **Save**.




## VMware Engine permissions

To view a comprehensive list of permissions for VMware Engine, go to the [Permissions reference](https://docs.cloud.google.com/iam/docs/permissions-reference) and search for the prefix `vmwareengine`.

Permissions let users perform specific actions to VMware Engine resources. You don't directly give users permissions; instead, you grant them predefined roles or custom roles, which have one or more permissions associated with them.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
