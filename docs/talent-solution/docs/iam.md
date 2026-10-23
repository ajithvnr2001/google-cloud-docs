---
url: https://docs.cloud.google.com/talent-solution/docs/iam/
title: Identity and Access Management (IAM) \u00a0|\u00a0 Cloud Talent Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:07.452733+00:00
---

# Identity and Access Management (IAM)  |  Cloud Talent Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/docs/iam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Resources ](https://docs.cloud.google.com/talent-solution/docs/resources)



Send feedback 

#  Identity and Access Management (IAM) Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how you can control CTS access and permissions using Identity and Access Management (IAM).

## Overview

Google Cloud Platform offers Identity and Access Management (IAM), which lets you give more granular access to specific Google Cloud Platform resources and prevents unwanted access to other resources. This page describes the Cloud Talent Solution IAM roles and permissions. For a detailed description of Google Cloud Platform IAM, see the [IAM documentation](https://docs.cloud.google.com/iam/docs).

CTS provides a set of predefined roles designed to help you easily control access to your CTS resources. You can also create your own custom roles, if the predefined roles do not provide the sets of permissions you need. In addition, the older basic roles (Editor, Viewer, and Owner) are also still available to you, although they do not provide the same fine-grained control as the CTS roles. In particular, the basic roles provide access to resources across Google Cloud Platform rather than just for CTS. See the [basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) documentation for more information.

The table below outlines the predefined roles available for Job Search.

Role | Description  
---|---  
Admin | Allows users to access the Google Cloud Platform Management tools only.  
jobsEditor | Allows Job Search users to create, modify or delete job or company content.  
jobsViewer | Allows read-only access to job or company content in Job Search.  
  
## Predefined roles

CTS provides predefined roles you can use to provide finer-grained permissions to principals. The role you grant to a principal controls what actions the principal can take. Principals can be individuals, groups, or service accounts.

You can grant multiple roles to the same principal, and you can change the roles granted to a principal at any time, provided you have the permissions to do so.

The broader roles include the more narrowly defined roles. For example, the jobsEditor role includes all of the permissions of the jobsViewer role, along with the addition permissions of the jobsEditor role.

The basic roles (Owner, Editor, Viewer) provide permissions across Google Cloud Platform. The roles specific to CTS provide only CTS permissions, except for the following GCP permissions, which are needed for general GCP usage:

  * `resourcemanager.projects.get`
  * `resourcemanager.projects.list`
  * `serviceusage.services.list`
  * `serviceusage.services.get`



The following table lists the predefined roles available for CTS, along with their permissions:

Role | Name | CTS permissions | Description  
---|---|---|---  
`roles/owner` | Owner | `cloudjobdiscovery.*` | Full access and control for all Google Cloud Platform resources; manage user access and set up billing for a project.  
`roles/editor` | Editor | All `cloudjobdiscovery` permissions except:  
`cloudjobdiscovery.tools.*`  
`iam.serviceAccounts.list`  
| Read-write access to all GCP and CTS resources except the ability to modify permissions and billing.  
`roles/viewer` | Viewer |  `cloudjobdiscovery.*.get`  
`cloudjobdiscovery.*.list`  
`cloudjobdiscovery.*.search`  
`resourcemanager.projects.get`  
`resourcemanager.projects.list`  
| Read-only access to all GCP resources, including Cloud Talent Solution resources.  
`roles/cloudjobdiscovery.admin` | Cloud Talent Solution Admin |  `cloudjobdiscovery.tools.*`  
`iam.serviceAccounts.list`  
`resourcemanager.projects.get`  
`resourcemanager.projects.list`  
| Access to Cloud Talent Solution self-service tools.  
`roles/cloudjobdiscovery.jobsEditor` | Job Search Editor |  `cloudjobdiscovery.companies.*`  
`cloudjobdiscovery.events.*`  
`cloudjobdiscovery.jobs.*`  
`resourcemanager.projects.list`  
`resourcemanager.projects.get`  
| Write access to all Job Search data.  
`roles/cloudjobdiscovery.jobsViewer` | Job Search Viewer |  `cloudjobdiscovery.companies.get`  
`cloudjobdiscovery.companies.list`  
`cloudjobdiscovery.jobs.get`  
`cloudjobdiscovery.jobs.search`  
`resourcemanager.projects.get`  
`resourcemanager.projects.list`  
| Read-only access to all Job Search resources.  
  
## Managing CTS IAM

You can get and set IAM policies and roles using the Google Cloud Platform Console, IAM API methods, or the Cloud Talent Solution APIs themselves. For more information, see [Granting, Changing, and Revoking Access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## What's next

  * Learn how to [grant and revoke access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).
  * Learn more about [IAM](https://docs.cloud.google.com/iam/docs).
  * Learn more about [basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic).
  * Learn more about [custom roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
