---
url: https://docs.cloud.google.com/docs/quotas/permissions/
title: Quota permissions \u00a0|\u00a0 Cloud Quotas \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:40:31.519175+00:00
---

# Quota permissions  |  Cloud Quotas  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/quotas/permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Quotas ](https://docs.cloud.google.com/docs/quotas)
  * [ Guides ](https://docs.cloud.google.com/docs/quotas/overview)



Send feedback 

#  Quota permissions Stay organized with collections  Save and categorize content based on your preferences. 

The predefined [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) role for permissions is named Quota Administrator. This role can be assigned at the project, folder, and organization levels.

  * If granted at the project level, the user will have permission to perform project-level operations.
  * If granted at the folder level, the user will have permission to perform project-level operations for all projects in that folder.
  * If granted at the organization level, the user will have permission to perform organization level operations. Because IAM permissions are inherited from the top level, this user will also be granted project and folder level permissions.



Users who are part of the Project Owners role can assign the Quota Administrator role to other users at the project level. Users in the Organization Owner role can assign the Quota Administrator role at the organization level.

## Permissions for viewing quota

To view your project quota in the Google Cloud console or to access your project quota programmatically using the Cloud Quotas API, you must have the following IAM permissions:

  * `resourcemanager.projects.get`
  * `resourcemanager.folders.get` if you want to view quota for an entire [Folder.](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#folders)
  * `resourcemanager.organizations.get` if you want to view quota for an entire [Organization.](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations)
  * [`monitoring.timeSeries.list`](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.timeSeries.list)
  * [`serviceusage.services.list`](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.services.list)
  * [`cloudquotas.quotas.get`](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudquotas#cloudquotas.quotas.get)



To learn which [roles](https://docs.cloud.google.com/iam/docs/roles-overview) include these permissions by default, see the [IAM permissions reference](https://docs.cloud.google.com/iam/docs/roles-permissions).

Cloud Quotas can also be viewed programmatically by using the [Service Usage API](https://docs.cloud.google.com/service-usage/docs/reference/rest). To learn about the IAM roles and permissions required for this approach, see [Access control with IAM](https://docs.cloud.google.com/service-usage/docs/access-control) in the Service Usage documentation.

## Permissions for changing quota

To change your quota at the project level, folder level, or organization level, you must have the following IAM permissions:

  * [`serviceusage.quotas.update`](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.quotas.update)
  * [`cloudquotas.quotas.update`](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudquotas#cloudquotas.quotas.update)



These permissions are included by default for the following [roles](https://docs.cloud.google.com/iam/docs/roles-overview): Owner, Editor, Quota Administrator, and Service Usage Admin.

## Permissions for viewing quota increase requests

To view quota increase requests in the Google Cloud console, you must have the following [IAM permissions](https://docs.cloud.google.com/iam/docs/roles-permissions):

  * `resourcemanager.projects.get`
  * [`serviceusage.services.list`](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.services.list)
  * [`serviceusage.quotas.get`](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.quotas.get)



## Permissions for creating an alert policy for a quota

To [set up quota alerts](https://docs.cloud.google.com/docs/quotas/set-up-quota-alerts), you must have the following permission:

  * `monitoring.alertPolicies.create`



## What's next

  * [Configure VPC Service Controls](https://docs.cloud.google.com/docs/quotas/configure-vpc-service-controls)
  * [Use custom organization policies](https://docs.cloud.google.com/docs/quotas/custom-constraints)
  * [View and manage quotas](https://docs.cloud.google.com/docs/quotas/view-manage)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
